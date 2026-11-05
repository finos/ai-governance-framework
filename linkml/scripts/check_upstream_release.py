#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check FINOS's tree in this repository against FINOS's repository.

The schema models the FINOS AI Governance Framework at one commit of main, since
FINOS has tagged no v3 release. This fork holds FINOS's tree, and
tests/upstream_tree.tsv lists every file of that commit with its git object hash.
Three things can change:

- this repository's copy of a file drifts from the pin;
- main changes, adds or drops a file the schema reads, or changes the licence;
- FINOS adds a tag.

This script compares every local file with the list offline. It asks the GitHub API
for main's tree and tags, so nothing is downloaded but listings.

It prints a Markdown report, writes it to ``--report`` when given, and exits 0 when
nothing needs a person's attention. It exits 1 when one of the three happened, or a
check could not finish.

Set ``GITHUB_TOKEN`` to raise the API rate limit; it is sent to api.github.com alone
and never on to a redirect. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT.parent
MANIFEST = ROOT / "tests" / "upstream_tree.tsv"
API_ORIGIN = "https://api.github.com"
API = f"{API_ORIGIN}/repos/finos/ai-governance-framework"
USER_AGENT = "lmodel-ai-governance-framework-upstream-check"
# The most one answer may hold. main's tree and the tag list are a few tens of
# kilobytes; a larger answer is refused.
MAX_BYTES = 5 * 1024 * 1024

# The edition docs/_config.yml states and the commit that merged it. The schema
# header carries the same values, and tests/test_upstream_tree.py holds them equal.
PINNED_EDITION = "v3"
PINNED_COMMIT = "67b8c3257695d5ede09d262798bf28a0e58d4740"
BRANCH = "main"
KNOWN_TAGS = {"v1", "v2"}

# What the schema models or rests on, and the licence files.
READ_FOLDERS = (
    "docs/_risks/",
    "docs/_mitigations/",
    "docs/_usecases/",
    "docs/_data/",
    "templates-for-ri-md/",
)
READ_FILES = {
    "CONVENTIONS.md",
    "docs/_config.yml",
    "scripts/validate-references.py",
}
LICENCES = {"LICENSE", "LICENSE.spdx", "NOTICE"}


class _HttpsApiOnly(urllib.request.HTTPRedirectHandler):
    """Follows a redirect only to another https address of the GitHub API, so a
    read never moves to plain http or to another host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not newurl.startswith(API_ORIGIN + "/"):
            raise urllib.error.HTTPError(
                newurl, code, f"refused a redirect off {API_ORIGIN}", headers, fp
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_HttpsApiOnly)


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        # urllib copies ordinary headers onto a redirect, so the token goes in an
        # unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with _OPENER.open(req, timeout=60) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is over {MAX_BYTES} bytes")
    return data


def _code(text: object) -> str:
    """Text a server chose, such as a file name or an error message, as a code span,
    so it cannot mention a person or add a link in the issue."""
    return "`" + str(text).replace("`", "'") + "`"


def blob_sha(path: Path) -> str:
    """The git object hash of a file, as the GitHub API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def pins() -> dict[str, str]:
    """Each file of the pinned commit, with its git object hash."""
    found = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha, path = line.split("\t", 1)
        # A path is read under FINOS's tree alone, so one that climbs out of it, or
        # starts at the root, is refused rather than followed.
        if path.startswith("/") or ".." in path.split("/"):
            raise ValueError(f"a manifest path outside FINOS's tree: {path}")
        found[path] = sha
    return found


def _is_read(path: str) -> bool:
    return path in READ_FILES or path.startswith(READ_FOLDERS)


def check_copy() -> tuple[list[str], bool]:
    """Report each pinned file that differs here or is gone, offline."""
    pinned = pins()
    differing = sorted(
        path
        for path, sha in pinned.items()
        if not (TREE / path).is_file() or blob_sha(TREE / path) != sha
    )
    report = [
        f"- {len(pinned) - len(differing)} of {len(pinned)} of FINOS's files here match the pin."
    ]
    if differing:
        report.append(
            f"- **{len(differing)} file(s) differ from the pin:** "
            + ", ".join(_code(p) for p in differing)
            + "."
        )
    return report, bool(differing)


def _tree(ref: str) -> dict[str, str]:
    """Each file of FINOS's repository at a ref, with its git object hash."""
    answer = json.loads(_get(f"{API}/git/trees/{ref}?recursive=1"))
    if answer.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in answer["tree"] if e["type"] == "blob"}


def check_main() -> tuple[list[str], bool]:
    """Report each file the schema reads that main changed, dropped or added, and a
    changed licence."""
    head = json.loads(_get(f"{API}/commits/{BRANCH}"))["sha"]
    report = [
        f"- Pinned commit: `{PINNED_COMMIT[:12]}` of finos/ai-governance-framework; "
        f"{BRANCH} is at {_code(head[:12])}."
    ]
    if head == PINNED_COMMIT:
        report.append(f"- {BRANCH} has not moved.")
        return report, False
    tree = _tree(head)
    pinned = pins()
    changed = sorted(
        p for p, sha in pinned.items() if _is_read(p) and p in tree and tree[p] != sha
    )
    dropped = sorted(p for p in pinned if _is_read(p) and p not in tree)
    added = sorted(p for p in tree if _is_read(p) and p not in pinned)
    licence = sorted(p for p in LICENCES if tree.get(p) != pinned.get(p))
    for label, paths in (("changes", changed), ("drops", dropped), ("adds", added)):
        if paths:
            report.append(
                f"- **{BRANCH} {label} {len(paths)} file(s) the schema reads:** "
                + ", ".join(_code(p) for p in paths)
                + "."
            )
    if licence:
        report.append(
            f"- **{BRANCH} changes the licence files:** "
            + ", ".join(_code(p) for p in licence)
            + ". Read them before merging."
        )
    attention = bool(changed or dropped or added or licence)
    if attention:
        report.append(
            f"- Read the changes, merge {BRANCH} into a branch, follow them in the "
            "schema, and move the pins here, in the header and in "
            "`tests/upstream_tree.tsv`."
        )
    else:
        report.append(
            f"- {BRANCH} moved, but no file the schema reads and not the licence."
        )
    return report, attention


def check_tags() -> tuple[list[str], bool]:
    """Report a tag FINOS added."""
    answer = json.loads(_get(f"{API}/tags?per_page=100"))
    new = sorted({t["name"] for t in answer} - KNOWN_TAGS)
    report = [
        f"- Pinned edition: {PINNED_EDITION}, which FINOS's `docs/_config.yml` states."
    ]
    if new:
        report.append(
            "- **FINOS adds "
            + ", ".join(_code(t) for t in new)
            + ".** Read it, decide whether the schema moves to it, and move the pins."
        )
        return report, True
    report.append(f"- FINOS has only the tags {', '.join(sorted(KNOWN_TAGS))}.")
    return report, False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (("copy", check_copy), ("main", check_main), ("tags", check_tags))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed fetch and a timeout, and HTTPException a
        # connection cut off mid-answer. ValueError covers an answer that is not JSON
        # or UTF-8 or is too large, and LookupError and TypeError one of another shape
        # than the API documents.
        except (
            OSError,
            http.client.HTTPException,
            ValueError,
            LookupError,
            TypeError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
