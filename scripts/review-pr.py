#!/usr/bin/env python3
"""
Deterministic pre-review checks for pull requests against the catalogue.

Answers the questions a reviewer would otherwise work out by hand before a
working session, so that judgement can be spent on content rather than on
mechanics:

  merge        Does it merge cleanly, and if not, which files collide?
  checks       CI and DCO status.
  doc-status   Does it amend a document that is already Approved-Specification?
  sequence     Does a newly added ri-N / mi-N collide with an existing entry?
  references   Does every id in the front matter resolve?
  frontmatter  Has a missing newline swallowed a key into the list above it?
  links        Do cross-links follow the conventions in CONVENTIONS.md?
  review       Who has been asked to review, who has replied, how stale is it?

Catalogue problems are reported as a delta: a problem that already exists on
main is not this contributor's to fix, so it is counted separately from one
the pull request introduces. Everything is resolved against the tree being
examined, so a pull request that updates a reference file and the ids that
point at it validates as a single consistent change.

Front matter ids are resolved as documented in CONVENTIONS.md:

    mitigates            -> docs/_risks/ri-<n>_*.md
    related_risks        -> docs/_risks/ri-<n>_*.md
    related_mitigations  -> docs/_mitigations/mi-<n>_*.md
    <namespace>_references -> keys of docs/_data/references/<namespace>.yml

Requires the GitHub CLI (`gh`) to be authenticated, and PyYAML.

Usage:
    python scripts/review-pr.py 354
    python scripts/review-pr.py 335 338 339 347
    python scripts/review-pr.py --agenda 358
    python scripts/review-pr.py --tree origin/main     # audit a branch directly
    python scripts/review-pr.py 354 --json
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COLLECTIONS = {
    "docs/_risks": "ri",
    "docs/_mitigations": "mi",
    "docs/_usecases": "uc",
}
REFERENCES_DIR = "docs/_data/references"

# Front matter keys that hold catalogue ids, and the prefix each expects.
ID_LISTS = {
    "mitigates": "ri",
    "related_risks": "ri",
    "related_mitigations": "mi",
}

CATALOGUE_ID = re.compile(r"(ri|mi|uc)-(\d+)$")

# Cross-links should be absolute site paths. Jekyll renders these collections
# at /<collection>/<name>/ -- see docs/_config.yml.
RELATIVE_MD_LINK = re.compile(r"\]\(\.{0,2}/?((?:ri|mi|uc)-\d+[^)]*\.md)\)")
ANCHOR_LINK = re.compile(r"\]\(#((?:ri|mi)-\d+)\)")

OK, INFO, WARN, FAIL = "OK", "INFO", "WARN", "FAIL"


# ---------------------------------------------------------------- shell


def run(cmd, check=True):
    """Run a command and return stdout, or None when it fails and check is False."""
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    if result.returncode != 0:
        if check:
            sys.exit(f"error: {' '.join(cmd)}\n{result.stderr.strip()}")
        return None
    return result.stdout


def gh_json(args):
    out = run(["gh"] + args, check=False)
    return json.loads(out) if out and out.strip() else None


def repo_slug():
    out = run(["gh", "repo", "view", "--json", "nameWithOwner"], check=False)
    return json.loads(out)["nameWithOwner"] if out else "finos/ai-governance-framework"


# ---------------------------------------------------------------- git


def fetch_pr(number):
    """Fetch the pull request head into a local ref and return its sha."""
    ref = f"refs/aigf-review/pr-{number}"
    run(["git", "fetch", "--quiet", "origin", f"pull/{number}/head:{ref}", "-f"])
    return run(["git", "rev-parse", ref]).strip()


def show(sha, path):
    """Read a file at a revision, or None when it does not exist there."""
    return run(["git", "show", f"{sha}:{path}"], check=False)


def ls_tree(sha, path):
    out = run(["git", "ls-tree", "-r", "--name-only", sha, path], check=False)
    return out.splitlines() if out else []


# ---------------------------------------------------------------- parsing


def front_matter(text):
    """Return the YAML front matter of a Markdown document as a dict."""
    if not text or not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def collection_of(path):
    for prefix, kind in COLLECTIONS.items():
        if path.startswith(prefix + "/"):
            return kind
    return None


def sequence_of(path):
    match = re.search(r"/(?:ri|mi|uc)-(\d+)[_.]", path)
    return int(match.group(1)) if match else None


def days_since(timestamp):
    if not timestamp:
        return None
    when = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=datetime.timezone.utc
    )
    return (datetime.datetime.now(datetime.timezone.utc) - when).days


# ------------------------------------------------------- tree-wide analysis


def reference_keys_at(sha):
    """Map each reference namespace to the ids it defines, at a given tree."""
    keys = {}
    for path in ls_tree(sha, REFERENCES_DIR):
        if not path.endswith(".yml"):
            continue
        namespace = os.path.basename(path)[: -len(".yml")]
        try:
            data = yaml.safe_load(show(sha, path) or "") or {}
        except yaml.YAMLError:
            data = {}
        entries = data.get("entries") if isinstance(data, dict) else None
        keys[namespace] = set(entries) if isinstance(entries, dict) else set()
    return keys


def catalogue_at(sha):
    """Map each catalogue prefix to the sequence numbers present at a tree."""
    catalogue = {"ri": set(), "mi": set(), "uc": set()}
    for prefix, kind in COLLECTIONS.items():
        for path in ls_tree(sha, prefix):
            seq = sequence_of(path)
            if seq is not None:
                catalogue[kind].add(seq)
    return catalogue


def catalogue_problems(sha):
    """
    Every unresolved id and malformed front matter block at a given tree.

    Returned as a set of stable strings so that two trees can be compared and
    a pull request judged on what it changes rather than what it inherits.
    """
    reference_keys = reference_keys_at(sha)
    catalogue = catalogue_at(sha)
    problems = set()

    for prefix in COLLECTIONS:
        for path in ls_tree(sha, prefix):
            if not path.endswith(".md"):
                continue
            meta = front_matter(show(sha, path))
            name = os.path.basename(path)

            for key, expected in ID_LISTS.items():
                for value in meta.get(key) or []:
                    ident = str(value).strip()
                    match = CATALOGUE_ID.fullmatch(ident)
                    if not match:
                        problems.add(f"{name}: {key} -> malformed '{ident}'")
                    elif match.group(1) != expected:
                        problems.add(
                            f"{name}: {key} -> '{ident}' should be a {expected}- id"
                        )
                    elif int(match.group(2)) not in catalogue[match.group(1)]:
                        problems.add(f"{name}: {key} -> '{ident}' does not exist")

            for key, values in meta.items():
                if not key.endswith("_references") or not isinstance(values, list):
                    continue
                namespace = key[: -len("_references")]

                # A catalogue id inside a reference list is almost always a
                # missing newline gluing the next key onto the previous
                # comment, which silently deletes that key from the document.
                swallowed = [v for v in values if CATALOGUE_ID.fullmatch(str(v).strip())]
                if swallowed:
                    problems.add(
                        f"{name}: {key} contains catalogue ids "
                        f"{sorted(swallowed)} -- a missing newline has swallowed "
                        f"the following key; those relationships are lost"
                    )

                if namespace not in reference_keys:
                    problems.add(f"{name}: no reference file for '{key}'")
                    continue
                for value in values:
                    ident = str(value).strip()
                    if ident in reference_keys[namespace] or ident in swallowed:
                        continue
                    problems.add(f"{name}: {key} -> '{ident}' not in {namespace}.yml")

    return problems


# ---------------------------------------------------------------- checks


def check_merge(pr, head_sha, findings):
    state = pr.get("mergeable")
    status = pr.get("mergeStateStatus")

    if state == "MERGEABLE" and status in ("CLEAN", "UNSTABLE"):
        findings.append((OK, "merge", f"Merges cleanly ({status})."))
        return
    if state != "CONFLICTING":
        findings.append((INFO, "merge", f"Merge state {state} / {status}."))
        return

    base = run(["git", "merge-base", "origin/main", head_sha], check=False)
    detail = "Conflicts with main."
    if base:
        moved = set(
            (run(["git", "diff", "--name-only", f"{base.strip()}..origin/main"]) or "")
            .splitlines()
        )
        collide = sorted(moved & {f["path"] for f in pr.get("files", [])})
        if collide:
            detail += " Both sides changed: " + ", ".join(collide)
    findings.append((FAIL, "merge", detail))


def check_status(pr, findings):
    rollup = pr.get("statusCheckRollup") or []
    failed = [
        c for c in rollup if c.get("conclusion") not in ("SUCCESS", "NEUTRAL", None)
    ]
    if failed:
        names = ", ".join(f"{c.get('name')}={c.get('conclusion')}" for c in failed)
        findings.append((FAIL, "checks", f"Failing: {names}"))
    elif rollup:
        findings.append(
            (OK, "checks", "All passing (" + ", ".join(c.get("name", "?") for c in rollup) + ").")
        )
    else:
        findings.append((INFO, "checks", "No checks reported."))


def check_doc_status(pr, findings):
    """Flag edits to documents that are already Approved-Specification."""
    amended = []
    for entry in pr.get("files", []):
        path = entry["path"]
        if not collection_of(path) or show("origin/main", path) is None:
            continue
        if front_matter(show("origin/main", path)).get("doc-status") == "Approved-Specification":
            amended.append((path, entry.get("additions", 0), entry.get("deletions", 0)))

    if not amended:
        findings.append((OK, "doc-status", "No approved documents amended."))
        return
    for path, added, removed in amended:
        findings.append(
            (
                WARN,
                "doc-status",
                f"Amends Approved-Specification: {os.path.basename(path)} (+{added}/-{removed}).",
            )
        )


def check_sequence(pr, findings):
    """A newly added ri-N / mi-N must not reuse an existing sequence number."""
    existing = catalogue_at("origin/main")
    added = [
        f["path"]
        for f in pr.get("files", [])
        if collection_of(f["path"]) and show("origin/main", f["path"]) is None
    ]
    if not added:
        findings.append((OK, "sequence", "No new catalogue entries."))
        return

    for path in added:
        kind, seq, name = collection_of(path), sequence_of(path), os.path.basename(path)
        if seq is None:
            findings.append((WARN, "sequence", f"Cannot read a sequence from {name}."))
        elif seq in existing[kind]:
            findings.append((FAIL, "sequence", f"{kind}-{seq} already exists on main ({name})."))
        else:
            findings.append((OK, "sequence", f"New entry {kind}-{seq} is free ({name})."))


def check_catalogue_delta(head_sha, findings):
    """Report catalogue problems this pull request introduces, fixes, or inherits."""
    base = run(["git", "merge-base", "origin/main", head_sha], check=False)
    base_problems = catalogue_problems(base.strip()) if base else set()
    head_problems = catalogue_problems(head_sha)

    introduced = sorted(head_problems - base_problems)
    fixed = sorted(base_problems - head_problems)
    inherited = head_problems & base_problems

    for problem in introduced:
        findings.append((FAIL, "references", problem))
    if fixed:
        findings.append((OK, "references", f"Fixes {len(fixed)} pre-existing problem(s)."))
    if not introduced:
        findings.append((OK, "references", "Introduces no unresolved references."))
    if inherited:
        findings.append(
            (
                INFO,
                "references",
                f"{len(inherited)} pre-existing problem(s) on main, not this "
                f"pull request's to fix (see --tree origin/main).",
            )
        )


def check_links(number, findings):
    """Cross-links added by the pull request should use absolute site paths."""
    diff = run(["gh", "pr", "diff", str(number)], check=False) or ""
    added = [line[1:] for line in diff.splitlines() if line.startswith("+")]

    relative = sorted({m for line in added for m in RELATIVE_MD_LINK.findall(line)})
    anchors = sorted({m for line in added for m in ANCHOR_LINK.findall(line)})

    if relative:
        findings.append(
            (
                WARN,
                "links",
                "Relative .md links do not resolve on the site; use "
                "/mitigations/<name>/ or /risks/<name>/: " + ", ".join(relative),
            )
        )
    if anchors:
        findings.append(
            (
                INFO,
                "links",
                "Anchor links match existing precedent but resolve to nothing: "
                + ", ".join(f"#{a}" for a in anchors),
            )
        )
    if not relative and not anchors:
        findings.append((OK, "links", "No non-conforming cross-links added."))


def check_review(pr, findings):
    author = (pr.get("author") or {}).get("login")

    voices = []
    for review in pr.get("reviews") or []:
        voices.append(((review.get("author") or {}).get("login"), review.get("submittedAt")))
    for comment in pr.get("comments") or []:
        voices.append(((comment.get("author") or {}).get("login"), comment.get("createdAt")))
    voices = [(who, when) for who, when in voices if who and who != author and "[bot]" not in who and "copilot" not in who.lower()]

    if not voices:
        findings.append((WARN, "review", "Nobody other than the author has commented."))
    else:
        latest = {}
        for who, when in voices:
            if when and (who not in latest or when > latest[who]):
                latest[who] = when
        findings.append(
            (
                INFO,
                "review",
                "Heard from: "
                + ", ".join(f"{w} ({days_since(t)}d ago)" for w, t in sorted(latest.items())),
            )
        )

    # A mention that never drew a reply is the usual reason a pull request stalls.
    mentioned = set()
    for comment in pr.get("comments") or []:
        mentioned.update(re.findall(r"@([A-Za-z0-9-]+)", comment.get("body") or ""))
    spoke = {who for who, _ in voices} | {author}
    silent = sorted(h for h in mentioned if h not in spoke and "/" not in h)
    if silent:
        findings.append((WARN, "review", "Asked but never replied: " + ", ".join(silent)))

    last = max(
        [c.get("createdAt") for c in pr.get("comments") or [] if c.get("createdAt")]
        + [pr.get("createdAt")],
        default=None,
    )
    age = days_since(last)
    if age is not None and age >= 7:
        findings.append((WARN, "review", f"No activity for {age} days."))


# ---------------------------------------------------------------- driver


PR_FIELDS = (
    "number,title,author,createdAt,updatedAt,isDraft,mergeable,mergeStateStatus,"
    "additions,deletions,files,reviews,comments,statusCheckRollup"
)


def load_pr(number, slug):
    """
    Read a pull request, waiting for GitHub to compute mergeability.

    GitHub computes it lazily, so the first read of a pull request that has
    not been visited recently reports UNKNOWN.
    """
    for attempt in range(5):
        pr = gh_json(["pr", "view", str(number), "--repo", slug, "--json", PR_FIELDS])
        if not pr or pr.get("mergeable") != "UNKNOWN":
            return pr
        time.sleep(1.5 * (attempt + 1))
    return pr


def review(number, slug):
    pr = load_pr(number, slug)
    if not pr:
        return {"number": number, "error": "could not be read"}

    head_sha = fetch_pr(number)
    findings = []

    check_merge(pr, head_sha, findings)
    check_status(pr, findings)
    check_doc_status(pr, findings)
    check_sequence(pr, findings)
    check_catalogue_delta(head_sha, findings)
    check_links(number, findings)
    check_review(pr, findings)

    return {
        "number": pr["number"],
        "title": pr["title"],
        "author": (pr.get("author") or {}).get("login"),
        "additions": pr.get("additions"),
        "deletions": pr.get("deletions"),
        "files": len(pr.get("files") or []),
        "draft": pr.get("isDraft"),
        "head": head_sha,
        "findings": [
            {"level": level, "check": check, "detail": detail}
            for level, check, detail in findings
        ],
    }


def audit(ref):
    """Report every catalogue problem present on a branch."""
    problems = sorted(catalogue_problems(ref))
    return {
        "number": ref,
        "title": f"catalogue audit of {ref}",
        "author": None,
        "additions": None,
        "deletions": None,
        "files": None,
        "draft": False,
        "head": ref,
        "findings": [{"level": FAIL, "check": "references", "detail": p} for p in problems]
        or [{"level": OK, "check": "references", "detail": "No problems found."}],
    }


def agenda_prs(number, slug):
    """Pull pull-request numbers out of a meeting agenda issue, in order."""
    issue = gh_json(["issue", "view", str(number), "--repo", slug, "--json", "body"])
    pattern = re.compile(re.escape(slug) + r"/pull/(\d+)")
    seen = []
    for match in pattern.finditer((issue or {}).get("body", "")):
        found = int(match.group(1))
        if found not in seen:
            seen.append(found)
    return seen


def report(results):
    worst = 0
    for result in results:
        if "error" in result:
            print(f"\n#{result['number']}  {result['error']}")
            worst = 2
            continue

        title = f"#{result['number']}  {result['title']}"
        print("\n" + title)
        if result["author"]:
            print(
                f"  @{result['author']}  +{result['additions']}/-{result['deletions']}  "
                f"{result['files']} files"
            )
        print("  " + "-" * max(len(title) - 2, 12))

        for finding in result["findings"]:
            print(f"  {finding['level']:<4} {finding['check']:<11} {finding['detail']}")
            if finding["level"] == FAIL:
                worst = 2
            elif finding["level"] == WARN and worst < 1:
                worst = 1

    counts = {level: 0 for level in (OK, INFO, WARN, FAIL)}
    for result in results:
        for finding in result.get("findings", []):
            counts[finding["level"]] += 1
    print(
        f"\n{len(results)} target(s): {counts[FAIL]} fail, {counts[WARN]} warn, "
        f"{counts[INFO]} info, {counts[OK]} ok."
    )
    return worst


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Deterministic pre-review checks for catalogue pull requests."
    )
    parser.add_argument("prs", nargs="*", type=int, help="pull request numbers")
    parser.add_argument("--agenda", type=int, help="read the list from a meeting agenda issue")
    parser.add_argument("--tree", help="audit a branch or ref instead of a pull request")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of a report")
    args = parser.parse_args(argv)

    run(["git", "fetch", "--quiet", "origin", "main"])

    if args.tree:
        results = [audit(args.tree)]
    else:
        slug = repo_slug()
        numbers = agenda_prs(args.agenda, slug) if args.agenda else []
        numbers += [n for n in args.prs if n not in numbers]
        if not numbers:
            parser.error("give a pull request number, --agenda <issue>, or --tree <ref>")
        results = [review(number, slug) for number in numbers]

    if args.json:
        print(json.dumps(results, indent=2))
        return 0
    return report(results)


if __name__ == "__main__":
    sys.exit(main())
