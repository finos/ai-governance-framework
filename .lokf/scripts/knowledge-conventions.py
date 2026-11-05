#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml==6.0.3"]
# [tool.uv]
# exclude-newer = "2025-10-01T00:00:00Z"
# ///
# The parser's half of knowledge-conventions.sh: rules 2, 3, 4, 7, 9, 10, 12,
# 13, 14, 15, 16, 17 and 18 (see that script's header for the list).
#
# Rules 2, 3, 7 and 9 are questions about a document's YAML that a real
# parser can decide, where grep and awk could only approximate. Is this
# scalar quoted, is this key a list or a mapping, do two files share an id,
# does the block even parse? An unquoted `at:` is only visible as a
# `datetime` once something parses the document. A flow-style
# `verified: { by: ... }` or a multi-line flow item is where a line-oriented
# regex used to guess wrong.
#
# Rule 4 is a body rule, checked with them. Rule 10 exists because the
# provenance gates do read the frontmatter line by line: it keeps the fields
# they read to spellings a line reader and a parser agree on. Rule 12 compares
# a concept's title and description, which only a parser reads whole, with
# the index bullets that copy them. Rule 13 asks git for the text a person
# confirmed and compares it with today's as parsed values, since
# knowledge-apply.sh writes the whole frontmatter back and a requoted value is
# no change. Rule 14 walks the commits after a base and compares each concept
# that gains a person's confirmation with the same file in every parent, as
# parsed values too. Rule 18 reads each exclusion beside the concept's
# sources, which a line reader cannot pair. The shell half checks rules 1, 5,
# 6, 8 and 11: they are git and filesystem facts, and need no uv.
#
# Rules 15, 16 and 17 join one parsed thing to another. Rule 15 reads
# `resource` and `sources` as parsed values, so a key with no value counts as
# absent. Rule 16 reads each `sources[].id` and its `resource` from the
# frontmatter and the footnotes from the body, and keeps one table of ids for
# the whole bundle, since one id names one source node in the graph. Rule 17
# reads the title of every concept, and then the bullets of log.md, so a
# logged write is held to a file the bundle holds.
#
# Usage: knowledge-conventions.py <bundle-dir> [--since <commit>]
#
# Same contract as the shell half: one line per finding on stdout, exit 1 if
# any; "OK" and exit 0 if none. The shell half runs it with the sidecar's
# .venv, or through `uv run`, which installs what the dependency block above
# names. Run directly, it needs python3 3.9 or later and pyyaml.
#
# That block names one PyYAML release, and `exclude-newer` takes no file
# uploaded after its date. A registry never replaces a file, so every run
# installs the files that were there when the pin was set, and this gate runs
# what a person reviewed. Behind a mirror with no upload times, the shell
# half lifts the date but keeps the version. The .venv holds what uv.lock
# pins, by hash, which a person reviewed too. Move the version and the date
# together, here and in knowledge-apply.py; the skills repository's contract
# holds the two equal.

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml

RESERVED = {"index.md", "log.md", "diataxis.md"}
OPEN_QUESTION = re.compile(r"^- \d{4}-\d{2}-\d{2}, (human|process):[^ :]+: ")
# An index bullet in the shape knowledge-apply.sh writes: the title linked to
# the concept, then its description. A line that lists two concepts is
# neither one's bullet, so the title holds no closing bracket.
INDEX_BULLET = re.compile(r"^\* \[([^\]]*)\]\(([^)]+)\) - (.*)$")
# The fields the provenance gates read line by line: a concept's id, and the
# actor, time and revision of each event.
GATE_FIELDS = {"id", "by", "at", "revision"}
# The keys those gates find an event under.
EVENT_KEYS = {"verified", "generated"}
# What a parser ends a line at and a line reader does not.
UNSEEN_BREAK = re.compile("[\x85\u2028\u2029]")
# Rule 2's one shape for a time: UTC to the second, as `date -u
# +%Y-%m-%dT%H:%M:%SZ` writes it, and as every writer here does. In it the
# federation build reads the moment knowledge-report.sh and rule 11 read, and
# the workspace's stored queries, which compare times as written, put two of
# them in order. A time in a shape a script cannot read counts there as no
# time, so a person's event spelt that way would confirm every later edit.
UTC_TIME = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")
# What a person's confirmation does not cover, for rule 13. In the
# frontmatter these are the trust, lifecycle and usage fields, which record
# who checked what and when rather than what the concept claims. In the body
# they are the open questions and the block KTL Registrar derives from the
# frontmatter.
NOT_CLAIMS = {"generated", "verified", "status", "stale_after", "timestamp", "usage_window"}
RELATED_START, RELATED_END = "<!-- lokf:related -->", "<!-- /lokf:related -->"
# A base commit as `--since` may name it: no leading dash, so git never reads
# it as an option.
COMMIT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/~^-]*")
# Rule 16's shape for a `sources[].id`: what rule 8 allows in a path segment.
# Under LOKF's published context the id becomes the IRI of the source's node
# under the bundle base, so it is held to the shape a path is.
SOURCE_ID = re.compile(r"[a-z0-9][a-z0-9._-]*")
# A footnote reference, and a definition line, which Markdown reads at the
# start of a line with at most three spaces before it.
FOOTNOTE = re.compile(r"\[\^([^\]\s]+)\]")
FOOTNOTE_DEFINITION = re.compile(r"^ {0,3}\[\^([^\]\s]+)\]:[ \t]*(.*)$")
CODE_SPAN = re.compile(r"`[^`]*`")
# Rule 17's log lines: a day heading in rule 1's shape, the three bullet kinds
# the rule reads, and a Markdown link.
DAY_HEADING = re.compile(r"^## (\d{4}-\d{2}-\d{2})$")
LOG_BULLET = re.compile(r"^[*-] \*\*(Added|Deprecation|Removal)\*\*:[ \t]*(.*)$")
MARKDOWN_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
# What may follow a concept's title in an Added bullet: the end of the line,
# or one of these, as the pen writes `**Added**: <title>, from ...`.
AFTER_TITLE = ",.:; "


def plain_spellings(fm_text: str) -> list[str]:
    """Rule 10: what a line reader could not read the way a parser does."""
    findings: list[str] = []
    stack: list[dict] = []  # one entry per open collection
    lines = fm_text.split("\n")
    found = UNSEEN_BREAK.search(fm_text)
    if found:
        # A parser counts these as lines, so its marks no longer index `lines`.
        return [f"a line break a line reader does not see (U+{ord(found.group()):04X})"]
    commented: set[int] = set()  # the lines already reported for a comment

    def at(ev) -> str:
        return f"line {ev.start_mark.line + 2}"  # +1 for zero-based, +1 for the opening ---

    def comment_after(ev) -> bool:
        """A `#` comment follows this value on its line. A parser drops it, and a line reader takes it for part of the value: an actor nobody is, or a time no script can compare."""
        row = ev.end_mark.line
        if row in commented or row >= len(lines):
            return False
        rest = re.sub(r"\"[^\"]*\"|'[^']*'", "", lines[row][ev.end_mark.column :])
        if re.search(r"(^|\s)#", rest):
            commented.add(row)
            return True
        return False

    for ev in yaml.parse(fm_text):
        top = stack[-1] if stack else None
        in_value = top is not None and top["kind"] == "map" and not top["expect_key"]
        field = top["key"] if in_value else None
        if isinstance(ev, yaml.AliasEvent):
            findings.append(f"an alias (*{ev.anchor}) at {at(ev)}")
        elif getattr(ev, "anchor", None):
            findings.append(f"an anchor (&{ev.anchor}) at {at(ev)}")
        if isinstance(ev, yaml.ScalarEvent):
            if ev.tag is not None:
                findings.append(f"a tag on '{ev.value}' at {at(ev)}")
            if top is not None and top["kind"] == "map" and top["expect_key"]:
                row = ev.start_mark.line
                if ev.value == "<<" and ev.style is None:
                    findings.append(f"a merge key at {at(ev)}")
                if ev.value in GATE_FIELDS | EVENT_KEYS:
                    if ev.style is not None:
                        findings.append(f"a quoted key ({ev.value}) at {at(ev)}")
                    elif "?" in lines[row][: ev.start_mark.column]:
                        findings.append(f"an explicit key (? {ev.value}) at {at(ev)}")
                    elif not lines[row][ev.end_mark.column :].startswith(":"):
                        findings.append(f"a space before the colon of {ev.value} at {at(ev)}")
                if len(stack) == 1 and ev.start_mark.column != 0 and not top["indented"]:
                    top["indented"] = True
                    findings.append(f"a frontmatter block indented whole at {at(ev)}")
                top["key"] = ev.value
                top["key_row"] = row
                top["expect_key"] = False
                continue
            if field in GATE_FIELDS:
                source = lines[ev.start_mark.line][ev.start_mark.column : ev.end_mark.column]
                if ev.style in ("|", ">"):
                    findings.append(f"a block scalar for {field} at {at(ev)}")
                elif ev.start_mark.line != ev.end_mark.line:
                    findings.append(f"a {field} spanning lines at {at(ev)}")
                elif ev.start_mark.line != top["key_row"]:
                    findings.append(f"a {field} on the line below its key at {at(ev)}")
                elif (ev.style == '"' and "\\" in source) or (ev.style == "'" and "''" in source[1:-1]):
                    findings.append(f"an escape in {field} at {at(ev)}")
                elif comment_after(ev):
                    findings.append(f"a comment beside {field} at {at(ev)}")
        if isinstance(ev, (yaml.MappingStartEvent, yaml.SequenceStartEvent)):
            if field in GATE_FIELDS:
                findings.append(f"a collection where {field} should be one scalar at {at(ev)}")
            if in_value:
                top["expect_key"] = True
            if not stack and ev.flow_style:
                findings.append(f"a flow mapping for the whole frontmatter at {at(ev)}")
            stack.append(
                {
                    "kind": "map" if isinstance(ev, yaml.MappingStartEvent) else "seq",
                    "expect_key": True,
                    "key": None,
                    "key_row": None,
                    "indented": False,
                    "flow_of": field if field in EVENT_KEYS and ev.flow_style else None,
                    "row": ev.start_mark.line,
                }
            )
            continue
        if isinstance(ev, (yaml.MappingEndEvent, yaml.SequenceEndEvent)):
            closed = stack.pop()
            # A comment can hide the closing bracket a line reader looks for.
            if closed["flow_of"] and any(
                re.search(r"(^|\s)#", re.sub(r"\"[^\"]*\"|'[^']*'", "", line))
                for line in lines[closed["row"] : ev.end_mark.line + 1]
            ):
                findings.append(f"a comment inside the flow form of {closed['flow_of']} at {at(ev)}")
            continue
        if in_value:
            top["expect_key"] = True
    return findings


def split_frontmatter(text: str) -> tuple[str, str] | None:
    lines = text.split("\n")
    if not lines or lines[0] != "---":
        return None
    for i, line in enumerate(lines[1:], start=1):
        if line == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :])
    return None


def find_odd_at(node, where: str) -> list[tuple[str, object]]:
    """Each `at:` that is not a quoted time in rule 2's shape, with where it sits."""
    found: list[tuple[str, object]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "at" and not utc_time(value):
                found.append((f"{where}at", value))
            found.extend(find_odd_at(value, f"{where}{key}."))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            found.extend(find_odd_at(item, f"{where}[{index}]."))
    return found


def utc_time(value) -> bool:
    """A string in rule 2's shape that names a real moment.

    The pattern alone passes 30 February, which the report reads and the
    build cannot, and 24:00, which only some Pythons read.
    """
    if not isinstance(value, str) or not UTC_TIME.fullmatch(value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def moment(value) -> str:
    """A time in the one UTC shape rule 11 and knowledge-report.sh compare, or '' for any other shape."""
    if not isinstance(value, str):
        return ""
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return value + "T00:00:00Z"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z", value):
        return value[:16] + ":00Z"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z", value):
        return value[:19] + "Z"
    return ""


def listed(frontmatter: dict, field: str) -> list[tuple[int, dict]]:
    """The mapping entries of a list field with their positions in it, a bare mapping read as a one-item list."""
    found = frontmatter.get(field) or []
    if isinstance(found, dict):
        found = [found]
    if not isinstance(found, list):
        return []
    return [(i, e) for i, e in enumerate(found) if isinstance(e, dict)]


def same_material(value) -> str | None:
    """A resource as rule 18 compares it, as `lokf validate` does: `./docs/a.md`, `docs/a.md` and `docs/a.md/` name one material."""
    if not isinstance(value, str) or not value.strip():
        return None
    key = value.strip()
    while key.startswith("./"):
        key = key[2:]
    return key.rstrip("/") or key


def under(value, base: str):
    """A value with each IRI under `base` written as the path after it, in every string it holds."""
    if isinstance(value, str):
        return value.replace(base, "<base_iri>/")
    if isinstance(value, list):
        return [under(v, base) for v in value]
    if isinstance(value, dict):
        return {k: under(v, base) for k, v in value.items()}
    return value


def claims(frontmatter: dict, body: str, base: str = ""):
    """What a person confirms: the frontmatter without NOT_CLAIMS, and the body without its open questions and its lokf:related block, with blank lines and trailing spaces evened out.

    With a `base`, each IRI under it counts as its path after it, so a
    concept that moved with the bundle's `base_iri` still says the same.
    """
    kept = {k: v for k, v in frontmatter.items() if k not in NOT_CLAIMS}
    if base:
        kept, body = under(kept, base), under(body, base)
    if isinstance(kept.get("sources"), list):  # a source's usage_count is a usage signal too
        kept["sources"] = [{k: v for k, v in s.items() if k != "usage_count"} if isinstance(s, dict) else s for s in kept["sources"]]
    out: list[str] = []
    fenced = in_questions = in_related = False
    for line in body.split("\n"):
        line = line.rstrip()
        # The registrar appends its block at the end, after any open questions,
        # and the block holds a `## Related` heading of its own: skip it first.
        if in_related or line.strip() == RELATED_START:
            in_related = line.strip() != RELATED_END
            continue
        if line.startswith("```") or line.startswith("~~~"):
            fenced = not fenced
        elif not fenced and re.match(r"^#{1,2} ", line):
            in_questions = line == "## Open questions"
        if in_questions:
            continue
        if line or (out and out[-1]):
            out.append(line)
    return kept, "\n".join(out).strip("\n")


def git(cwd: Path, *args: str) -> str | None:
    try:
        done = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, encoding="utf-8", errors="replace", timeout=120)
    except (OSError, subprocess.SubprocessError):
        return None
    return done.stdout if done.returncode == 0 else None


def base_iri(text: str | None) -> str:
    """The `base_iri` in the frontmatter of a bundle's root index.md, or ''."""
    found = parsed(text) if text else None
    value = found[0].get("base_iri") if found else None
    return value if isinstance(value, str) else ""


def unstamped_edit(path: Path, frontmatter: dict, body: str, bundle: Path) -> str | None:
    """Rule 13: a concept that reads as confirmed by a person still holds the claims they confirmed.

    The text they confirmed is the concept at the newest commit that recorded
    the time of its latest confirmation. Any later commit can only be an
    edit after it, so the rule can miss one but never flags a concept that
    person saw. Outside git, or before that commit exists, there is nothing
    to compare and nothing is said. A move of the bundle's `base_iri` is no
    edit: the ids and relation targets it carries along are compared by
    their paths under the base each commit held.
    """
    if frontmatter.get("status") == "deprecated":
        return None
    verified = frontmatter.get("verified")
    events = [verified] if isinstance(verified, dict) else verified if isinstance(verified, list) else []
    confirmations = [
        (moment(e.get("at")), e.get("at"), str(e.get("by")))
        for e in events
        if isinstance(e, dict) and str(e.get("by", "")).startswith("human:") and moment(e.get("at"))
    ]
    if not confirmations:
        return None
    confirmed_at, written, by = max(confirmations)
    generated = frontmatter.get("generated")
    stamp = moment(generated.get("at")) if isinstance(generated, dict) else moment(frontmatter.get("timestamp"))
    if stamp > confirmed_at:
        return None  # it already reads as edited since that confirmation
    real = path.resolve()
    found = git(real.parent, "log", "--format=%H", "-S" + written, "--", real.name)
    commit = found.split("\n", 1)[0].strip() if found else ""
    if not commit:
        return None
    then = git(real.parent, "show", f"{commit}:./{real.name}")
    split = split_frontmatter(then.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")) if then else None
    if split is None:
        return None
    try:
        frontmatter_then = yaml.safe_load(split[0])
    except yaml.YAMLError:
        return None
    if not isinstance(frontmatter_then, dict) or claims(frontmatter_then, split[1]) == claims(frontmatter, body):
        return None
    index = bundle.resolve() / "index.md"
    base_now = base_iri(index.read_text(encoding="utf-8", errors="replace")) if index.is_file() else ""
    base_then = base_iri(git(index.parent, "show", f"{commit}:./index.md"))
    if base_now and base_then and base_now != base_then:
        if claims(frontmatter_then, split[1], base_then) == claims(frontmatter, body, base_now):
            return None
    return (
        f"{path}: changed since {by} confirmed it ({confirmed_at[:10]}, in {commit[:7]}), and `generated` was not "
        "restamped, so it still reads as confirmed - knowledge-apply.sh restamps every change it writes; by hand, "
        f"move generated.at to the time of the change, or have {by} confirm it again"
    )


def human_events(frontmatter: dict) -> set[tuple[str, str]]:
    """The (actor, time) of each `verified` event a person recorded."""
    verified = frontmatter.get("verified")
    events = [verified] if isinstance(verified, dict) else verified if isinstance(verified, list) else []
    return {
        (str(e.get("by")), str(e.get("at")))
        for e in events
        if isinstance(e, dict) and str(e.get("by", "")).startswith("human:")
    }


def parsed(text: str | None) -> tuple[dict, str] | None:
    """A concept's frontmatter and body as git holds them, or None when there is no such file or no mapping."""
    if text is None:
        return None
    split = split_frontmatter(text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n"))
    if split is None:
        return None
    try:
        frontmatter = yaml.safe_load(split[0])
    except yaml.YAMLError:
        return None
    return (frontmatter, split[1]) if isinstance(frontmatter, dict) else None


def verdict_edits(bundle: Path, since: str) -> list[str]:
    """Rule 14: a commit that records a person's confirmation changes the verdict, not what the concept says.

    Each commit after `since` that touches the bundle is read against every
    parent, as the provenance job reads one. A person's event that no parent
    holds is new in that commit. The commit may then change the concept's
    claims only when `generated.by` names the same person, the shape of
    Correct now: that person wrote the text as well as confirming it. A merge
    that brings in a confirmation made elsewhere adds nothing new, so it is
    never read as one. Outside git, or with no such base, nothing is said.
    """
    if not COMMIT.fullmatch(since):
        return [f"rule 14: '{since}' is not a commit - pass the base the pull request was opened against"]
    real = bundle.resolve()
    top = git(real, "rev-parse", "--show-toplevel")
    if top is None:
        return []
    top_path = Path(top.strip())
    if git(top_path, "rev-parse", "--verify", "--quiet", since + "^{commit}") is None:
        return [f"rule 14: the base commit {since} is not in this clone's history - check out the full history"]
    rel = real.relative_to(top_path.resolve()).as_posix()
    findings: list[str] = []
    for commit in (git(top_path, "rev-list", "--reverse", f"{since}..HEAD", "--", rel) or "").split():
        parents = (git(top_path, "rev-list", "--parents", "-n", "1", commit) or "").split()[1:]
        names: set[str] = set()
        for parent in parents or [""]:
            against = [parent, commit] if parent else ["--root", commit]
            out = git(top_path, "diff-tree", "--no-commit-id", "--name-only", "-r", "--diff-filter=AM", *against, "--", rel)
            names.update(n for n in (out or "").splitlines() if n.endswith(".md") and Path(n).name not in RESERVED)
        for name in sorted(names):
            now = parsed(git(top_path, "show", f"{commit}:{name}"))
            if now is None:
                continue
            frontmatter, body = now
            before = [parsed(git(top_path, "show", f"{parent}:{name}")) for parent in parents]
            held: set[tuple[str, str]] = set()
            for earlier in before:
                if earlier is not None:
                    held |= human_events(earlier[0])
            added = human_events(frontmatter) - held
            if not added or any(e is not None and claims(e[0], e[1]) == claims(frontmatter, body) for e in before):
                continue
            generated = frontmatter.get("generated")
            author = str(generated.get("by")) if isinstance(generated, dict) else ""
            for by in sorted({by for by, _ in added} - {author}):
                findings.append(
                    f"{name}: commit {commit[:7]} records a confirmation by {by} and changes what the concept says - "
                    f"record the verdict in a commit of its own, or as Correct now, with generated.by set to {by}"
                )
    return findings


def footnotes(path: Path, frontmatter: dict, body: str, source_ids: dict[str, dict[str, list[Path]]]) -> list[str]:
    """Rule 16: each footnote in the body joins a claim to one of the concept's `sources` entries, by that entry's `id`.

    A reference `[^label]` and a definition line `[^label]: text` each use
    an id the entry list holds. Each id is cited at least once, each cited
    label has its definition line, and the definition holds the entry's
    `resource` verbatim, so a reader sees the source beside the claim and
    the footnote cannot drift from its entry. A footnote mark in a code
    fence or a code span is an example, not a reference. Each id is recorded
    in `source_ids` with its resource, for the check across the bundle in
    main: one id names one resource.
    """
    findings: list[str] = []
    sources = frontmatter.get("sources")
    entries = [sources] if isinstance(sources, dict) else sources if isinstance(sources, list) else []
    ids: dict[str, str] = {}
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("id") is None:
            continue
        label = str(entry["id"])
        resource = entry.get("resource")
        resource = resource if isinstance(resource, str) else ""
        if not SOURCE_ID.fullmatch(label):
            findings.append(
                f"{path}: sources[].id {json.dumps(label)} is not lowercase a-z, 0-9, '.', '_', '-' - "
                "the id mints the source's node under the bundle base, so write it as rule 8 has a path written"
            )
        ids.setdefault(label, resource)
        source_ids.setdefault(label, {}).setdefault(resource, []).append(path)
    referenced: set[str] = set()
    defined: dict[str, str] = {}
    fenced = False
    for line in body.split("\n"):
        if line.startswith("```") or line.startswith("~~~"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = FOOTNOTE_DEFINITION.match(line)
        if m:
            defined.setdefault(m.group(1), m.group(2))
            continue
        referenced.update(FOOTNOTE.findall(CODE_SPAN.sub("", line)))
    for label in sorted((referenced | set(defined)) - set(ids)):
        findings.append(
            f"{path}: footnote [^{label}] names no sources[].id - give the entry it cites the id {label}, "
            "or cite an id the frontmatter holds"
        )
    for label, resource in sorted(ids.items()):
        if label not in referenced:
            findings.append(f"{path}: sources[].id {label} is cited by no footnote - write [^{label}] after a claim it backs, or drop the id")
        elif label not in defined:
            findings.append(
                f'{path}: footnote [^{label}] has no definition line - add "[^{label}]: {resource}, <where in it>" at the end of the body'
            )
        if label in defined and resource and resource not in defined[label]:
            findings.append(
                f"{path}: footnote definition [^{label}] does not quote its resource {resource} - "
                "write the resource value in it verbatim, so the footnote cannot drift from its entry"
            )
    return findings


def bullet_target(text: str, bundle: Path) -> tuple[Path | None, str]:
    """The file a log bullet links, and the link's text, or (None, '') when it holds no link to a file.

    The first link decides, and its path is read as successors() in
    knowledge-report.sh reads a Deprecation line: against the bundle root,
    with one leading `../` or `./` stripped.
    """
    m = MARKDOWN_LINK.search(text)
    if m is None or "://" in m.group(2):
        return None, ""
    return bundle / re.sub(r"^(\.\./|\./)", "", m.group(2)), " ".join(m.group(1).split())


def bullet_head(text: str) -> str:
    """A log bullet's text up to its first ',', '.', ':' or ';', links replaced by their text and whitespace collapsed: the title as the pen writes an Added or a Removal line."""
    plain = MARKDOWN_LINK.sub(lambda m: m.group(1), text)
    return " ".join(re.split(r"[,.:;]", plain, maxsplit=1)[0].split())


def bullet_names(bullet: dict, bundle: Path) -> set[str]:
    """What a bullet names, for matching an Added or Deprecation bullet with a Removal: the linked path, the link's text and the head."""
    path, link_text = bullet_target(bullet["text"], bundle)
    found = {str(path), link_text} if path is not None else set()
    found.add(bullet_head(bullet["text"]))
    return found - {""}


def starts_with_title(text: str, titles: set[str]) -> bool:
    """The text, whitespace collapsed, starts with a concept's title, followed by the end of the line or one of AFTER_TITLE."""
    collapsed = " ".join(text.split())
    return any(collapsed.startswith(t) and (len(collapsed) == len(t) or collapsed[len(t)] in AFTER_TITLE) for t in titles if t)


def logged_writes(bundle: Path, titles: set[str], since: str) -> list[str]:
    """Rule 17: each `**Added**` and `**Deprecation**` bullet in log.md names a concept the bundle holds.

    A bullet that holds a Markdown link names the concept its first link
    resolves to, as bullet_target reads it. Any other bullet starts with a
    concept's title, as the pen writes an Added line. With `--since`, the
    bullets read are the ones `git diff` shows added to log.md since that
    base, in the working tree; without it, or where git cannot diff, the
    ones under the newest day heading, where the latest run's claims sit. A
    `**Removal**` bullet under the same or a newer day that names the same
    path or title excuses a bullet whose concept is gone. A wrapped bullet
    is read with its continuation lines joined.
    """
    log = bundle / "log.md"
    if not log.is_file():
        return []
    text = log.read_bytes().decode("utf-8", errors="replace").lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    bullets: list[dict] = []
    day = first_day = ""
    current: dict | None = None
    for line in text.split("\n"):
        if line.startswith("## "):
            m = DAY_HEADING.match(line)
            day = m.group(1) if m else ""  # under a heading rule 1 reports, nothing is read
            first_day = first_day or day
            current = None
            continue
        b = LOG_BULLET.match(line)
        if b and day:
            current = {"day": day, "kind": b.group(1), "text": b.group(2), "line": line}
            bullets.append(current)
        elif current is not None and line[:1] in (" ", "\t") and line.strip():
            current["text"] += " " + line.strip()
        else:
            current = None
    diff = None
    if since and COMMIT.fullmatch(since):
        diff = git(log.resolve().parent, "diff", "--no-color", "--no-ext-diff", "--unified=0", since, "--", "log.md")
    if diff is not None:
        added = {line[1:] for line in diff.split("\n") if line.startswith("+") and not line.startswith("+++")}
        chosen = [b for b in bullets if b["line"] in added]
    else:
        chosen = [b for b in bullets if b["day"] == first_day]
    findings: list[str] = []
    for b in chosen:
        if b["kind"] == "Removal":
            continue
        path, _ = bullet_target(b["text"], bundle)
        if path is not None:
            if path.is_file():
                continue
            which = "the retired concept" if b["kind"] == "Deprecation" else "the concept it names"
            what = f"links {path}, which the bundle lacks - link {which}, or log its removal"
        else:
            if starts_with_title(b["text"], titles):
                continue
            what = (
                f"names no concept the bundle holds: {' '.join(b['text'].split())[:60]} - "
                "start it with the concept's title, or link the concept"
            )
        if any(bullet_names(r, bundle) & bullet_names(b, bundle) for r in bullets if r["kind"] == "Removal" and r["day"] >= b["day"]):
            continue
        findings.append(f"{log}: {b['kind']} bullet under {b['day']} {what}")
    return findings


def index_bullets(index: Path, cache: dict[Path, dict[str, tuple[str, str]]]) -> dict[str, tuple[str, str]]:
    """The bullets of one index.md, as link -> (title, description), each with its whitespace collapsed."""
    if index not in cache:
        found: dict[str, tuple[str, str]] = {}
        if index.is_file():
            text = index.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
            for line in text.split("\n"):
                m = INDEX_BULLET.match(line)
                if m:
                    found[m.group(2)] = (" ".join(m.group(1).split()), " ".join(m.group(3).split()))
        cache[index] = found
    return cache[index]


def check_file(
    path: Path,
    bundle: Path,
    ids: dict[str, list[Path]],
    entries: dict[Path, tuple[str, str]],
    titles: set[str],
    source_ids: dict[str, dict[str, list[Path]]],
) -> list[str]:
    findings: list[str] = []
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        findings.append(f"{path}: starts with a byte order mark - save as UTF-8 without BOM")
        raw = raw[3:]
    decoded = raw.decode("utf-8", errors="replace")
    text = decoded.replace("\r\n", "\n").replace("\r", "\n")
    # The toolkit reads a bare carriage return as a line break, and the gates
    # do not, so rule 10 reads it before this script reads it as the toolkit does.
    block = decoded.split("---", 2)
    if len(block) == 3 and "\r" in block[1].replace("\r\n", ""):
        findings.append(f"{path}: frontmatter uses a bare carriage return - write it plainly, so the gate reads the event a parser reads")

    split = split_frontmatter(text)
    if split is None:
        findings.append(
            f"{path}: no closed frontmatter block - a concept starts with '---' and closes it before the body"
        )
        return findings
    fm_text, body = split
    # The toolkit ends the block at the first `---` it meets, in a line or not,
    # so it would read less of this block than every script here reads.
    if "---" in fm_text:
        findings.append(f"{path}: frontmatter holds '---', where the toolkit ends the block - write the value another way")

    try:
        frontmatter = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        problem = getattr(exc, "problem", None) or " ".join(str(exc).split())
        mark = getattr(exc, "problem_mark", None)
        where = f" at line {mark.line + 2}" if mark is not None else ""
        findings.append(f"{path}: frontmatter is not valid YAML - {problem}{where}")
        return findings
    if not isinstance(frontmatter, dict):
        findings.append(f"{path}: frontmatter is not a mapping")
        return findings

    # 10. the fields the provenance gates read line by line are spelt so a
    #     line reader and a parser see the same event.
    for what in plain_spellings(fm_text):
        findings.append(f"{path}: frontmatter uses {what} - write it plainly, so the gate reads the event a parser reads")

    # 2. every `at:` a quoted time in one shape: unquoted, YAML resolves it to
    #    a datetime, a date or a number, and only a string reaches every
    #    consumer the same. In any other shape not every consumer reads it
    #    alike, as UTC_TIME says. The finding prints the time as JSON writes
    #    it, so it stays on one line and shows a character no reader would
    #    see. The fix respells the same moment, since a new time from the
    #    clock would re-date the event.
    for where, value in find_odd_at(frontmatter, ""):
        if isinstance(value, str):
            findings.append(
                f"{path}: timestamp {json.dumps(value[:40])} at {where} is not a UTC time to the second, such as "
                '"2026-09-08T14:00:00Z" - write the same moment in that shape, in quotes'
            )
        else:
            findings.append(f"{path}: unquoted timestamp at {where}")

    # 3. verified is a list, never a bare mapping, and carries at most one
    #    process:ktl-librarian event.
    verified = frontmatter.get("verified")
    if isinstance(verified, dict):
        findings.append(f"{path}: verified is a bare mapping - write a one-item list")
        events = [verified]
    elif isinstance(verified, list):
        events = [item for item in verified if isinstance(item, dict)]
    else:
        events = []
    librarian_events = [e for e in events if e.get("by") == "process:ktl-librarian"]
    if len(librarian_events) > 1:
        findings.append(
            f"{path}: {len(librarian_events)} process:ktl-librarian events - "
            "the librarian replaces its own, never stacks"
        )

    # 4. a bullet under `## Open questions` is `- YYYY-MM-DD, <actor>: ...`.
    in_section = False
    for line in body.split("\n"):
        if line == "## Open questions":
            in_section = True
            continue
        if in_section and line.startswith("#"):
            in_section = False
        if in_section and line.startswith("- ") and not OPEN_QUESTION.match(line):
            findings.append(f"{path}: open question not '- YYYY-MM-DD, <actor>: ...': {line[:60]}")

    # 18. each exclusion says why the material was left out, and no material
    #     is both a source and an exclusion of one concept.
    used = {same_material(s.get("resource")) for _, s in listed(frontmatter, "sources")}
    for i, exclusion in listed(frontmatter, "exclusions"):
        reason = exclusion.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            findings.append(f"{path}: exclusions[{i}] gives no reason - say in a sentence why the material was left out")
        key = same_material(exclusion.get("resource"))
        if key is not None and key in used:
            findings.append(
                f"{path}: exclusions[{i}].resource {json.dumps(exclusion.get('resource'))} is also one of its sources - "
                "a concept cannot derive from a material and leave it out; keep one"
            )

    # 7. one file per id: collected here, reported once every file is read.
    concept_id = frontmatter.get("id")
    if isinstance(concept_id, str) and concept_id:
        ids.setdefault(concept_id, []).append(path)

    # 12. the catalogue entry: collected here, compared with the index
    #     bullets once every file is read.
    title, description = frontmatter.get("title"), frontmatter.get("description")
    if isinstance(title, str) and isinstance(description, str):
        entries[path] = (" ".join(title.split()), " ".join(description.split()))
    if isinstance(title, str):
        titles.add(" ".join(title.split()))  # for rule 17

    # 13. a concept that reads as confirmed by a person still says what that
    #     person confirmed: an edit since then restamps `generated`.
    finding = unstamped_edit(path, frontmatter, body, bundle)
    if finding:
        findings.append(finding)

    # 15. the concept names where it came from: a `resource`, or a `sources`
    #     entry. The librarian's refresh follows those back to the origin,
    #     and the coverage count credits a file to a concept through them, so
    #     a concept with neither can be neither re-verified nor counted.
    resource, sources = frontmatter.get("resource"), frontmatter.get("sources")
    has_resource = isinstance(resource, str) and bool(resource.strip())
    has_sources = isinstance(sources, dict) or (isinstance(sources, list) and bool(sources))
    if not has_resource and not has_sources:
        findings.append(
            f"{path}: neither resource nor sources names where it came from - "
            "name the source of truth it was derived from, as resource or as a sources entry"
        )

    # 16. each footnote joins a claim to a `sources` entry by its id.
    findings.extend(footnotes(path, frontmatter, body, source_ids))

    return findings


def main(argv: list[str]) -> int:
    args, since = argv[1:], ""
    if len(args) == 3 and args[1] == "--since":
        args, since = args[:1], args[2]
    if len(args) != 1:
        print("usage: knowledge-conventions.py <bundle-dir> [--since <commit>]", file=sys.stderr)
        return 2
    bundle = Path(args[0])
    if not bundle.is_dir():
        print(f"no bundle directory at {bundle}", file=sys.stderr)
        return 2

    findings: list[str] = []
    ids: dict[str, list[Path]] = {}
    entries: dict[Path, tuple[str, str]] = {}
    titles: set[str] = set()
    source_ids: dict[str, dict[str, list[Path]]] = {}
    # 9. the toolkit reads a link as the file it points at, and the gates read
    #    it as the path it names, so its events would go unseen.
    for path in sorted(bundle.rglob("*")):
        if path.is_symlink() and (path.suffix == ".md" or ".obsidian" not in path.parts):
            findings.append(f"{path}: is a symbolic link - a concept is a file of its own, which the gates can read")
    for path in sorted(bundle.rglob("*.md")):
        if path.is_symlink():
            continue
        if ".obsidian" in path.parts or path.name in RESERVED:
            continue
        findings.extend(check_file(path, bundle, ids, entries, titles, source_ids))

    # 12. an index bullet that names a concept says what the concept says. A
    #     reader chooses from the index before opening anything, so a bullet
    #     left behind by an edited title or description hides the concept as
    #     surely as a missing one. Only a bullet that exists is compared, in
    #     the folder's index.md and in the root's: a concept no index lists
    #     is a choice this rule leaves alone.
    cache: dict[Path, dict[str, tuple[str, str]]] = {}
    for path, entry in entries.items():
        places = {path.parent / "index.md": path.name, bundle / "index.md": path.relative_to(bundle).as_posix()}
        for index, link in places.items():
            bullet = index_bullets(index, cache).get(link)
            if bullet is not None and bullet != entry:
                findings.append(
                    f"{path}: its bullet in {index} does not match its title and description - "
                    "a reindex operation through knowledge-apply.sh re-derives it"
                )

    for concept_id, paths in ids.items():
        if len(paths) > 1:
            files = "".join(f"{p} " for p in paths)
            findings.append(
                f"id {concept_id} is declared by more than one file: {files}- "
                "a sync conflict copy or a pasted duplicate; keep one"
            )

    # 16. across the bundle, one id names one resource. Under LOKF's published
    #     context a Source id, resolved against the bundle base, becomes the
    #     IRI of the source's node, so one id for two resources merges them
    #     into one RDF node, and a query then credits each claim to both.
    for label, by_resource in sorted(source_ids.items()):
        if len(by_resource) > 1:
            where = "; ".join(f"{resource or '(no resource)'} in {' '.join(str(p) for p in paths)}" for resource, paths in by_resource.items())
            findings.append(
                f"id {label} names more than one resource: {where} - "
                "one id names one resource across the bundle, since the id mints one source node under the bundle base"
            )

    # 14. a commit after the base that records a person's confirmation
    #     changes only the verdict, unless that person also wrote the text.
    #     Asked for a pull request's commits only: on a branch's whole
    #     history a squash merge folds an edit and a confirmation into one.
    if since:
        findings.extend(verdict_edits(bundle, since))

    # 17. each Added and Deprecation bullet the latest run logged names a
    #     concept the bundle holds, read since the base when one is given.
    findings.extend(logged_writes(bundle, titles, since))

    for line in findings:
        print(line)
    if findings:
        return 1
    print(f"OK - {bundle} keeps the frontmatter conventions lokf validate cannot check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
