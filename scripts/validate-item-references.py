#!/usr/bin/env python3
"""
Validates the reference mappings carried by risk and mitigation pages.

Where scripts/validate-references.py checks the reference *library*
(docs/_data/references/*.yml), this checks the *items* that cite it:

  Floor    Each risk cites at least one threat and one obligation reference;
           each mitigation cites at least one control reference. The lens of
           each reference comes from the `lens:` field of its library file.

  Cap      No item cites more than CAP distinct entries from a single standard.
           Reported only -- whether exceeding the cap is a defect or purely a
           display matter is an open question in #426.

  Reverse  Library entries that nothing cites, citations of keys that are not
           in the library at all, and citations of entries the library marks
           `superseded_by`.

Assumes scripts/validate-references.py has already passed, since that is what
guarantees every library file carries a valid lens. A missing lens is reported
here as a warning pointing at that script, not re-validated.

On the obligation floor, #426 states that IOSCO's toolkit "supports but doesn't
satisfy the floor on its own", so that is the default. --lenient-iosco lets a
citation of IOSCO alone satisfy it, matching how the lens is tagged today.

Usage:
    python scripts/validate-item-references.py
    python scripts/validate-item-references.py --lenient-iosco
    python scripts/validate-item-references.py --warn

Refs #426
"""
import argparse
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT, "docs")
REFERENCES_DIR = os.path.join(DOCS_DIR, "_data", "references")

# Which lenses an item of each kind must cite at least one of.
FLOOR = {
    "_risks": ["threat", "obligation"],
    "_mitigations": ["control"],
}

# Collections searched when working out what cites what. Use cases carry
# references too -- sr11-7 is cited only from there.
CITING_COLLECTIONS = ["_risks", "_mitigations", "_usecases"]

CAP = 3

IOSCO = "iosco-supervisory-toolkit"

# docs/_risks/ri-30_skill-plugin-supply-chain-compromise.md -> ri-30
ITEM_FILENAME = re.compile(r"^((?:ri|mi|uc)-(\d+))(?:_.*)?\.md$")

REFERENCES_SUFFIX = "_references"

# Pages whose front matter could not be parsed. Collected during the first
# pass over a collection and surfaced as errors, so a broken page cannot
# silently hide a missing mapping.
PARSE_FAILURES = []

# Items declaring a *_references value that is not a list. A set, because
# references_of() runs once per check and must not report the same page twice.
MALFORMED_REFERENCES = set()

# Parsed pages, by collection. Each collection is read once so warnings are
# not repeated by the floor, cap and reverse passes.
_ITEM_CACHE = {}


def _key(value):
    """Normalise an entry key for comparison.

    YAML turns a bare `14:` into an int on both the library and citing sides,
    but quoting differs between files, so compare as text throughout.
    """
    return str(value)


# ----------------------------------------------------------------- loading

def load_library(directory):
    """{dataset: {"lens": str|None, "entries": set, "superseded": {old: new}}}"""
    if not os.path.isdir(directory):
        raise SystemExit(
            f"error: reference directory not found: {directory}\n"
            f"       run this script from a checkout of the repository, with "
            f"the script in scripts/."
        )

    library = {}
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".yml"):
            continue
        path = os.path.join(directory, filename)
        try:
            with open(path, encoding="utf-8") as handle:
                data = yaml.safe_load(handle) or {}
        except yaml.YAMLError as exc:
            raise SystemExit(
                f"error: {filename} did not parse: {exc}\n"
                f"       run scripts/validate-references.py first."
            )
        entries = data.get("entries") or {}
        library[filename[: -len(".yml")]] = {
            "lens": data.get("lens"),
            "entries": {_key(k) for k in entries},
            "superseded": {
                _key(key): _key(value["superseded_by"])
                for key, value in entries.items()
                if isinstance(value, dict) and value.get("superseded_by")
            },
        }
    return library


def read_front_matter(path):
    """The YAML front matter of a markdown page, or None if absent/unparseable."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    if not text.startswith("---") or "\n---" not in text[3:]:
        return None
    try:
        front_matter = yaml.safe_load(text[3: text.index("\n---", 3)])
    except yaml.YAMLError as exc:
        PARSE_FAILURES.append((os.path.basename(path), str(exc).split("\n")[0]))
        return None
    return front_matter if isinstance(front_matter, dict) else None


def iter_items(collection):
    """(item_id, front_matter) for each page in a collection, in sequence order.

    Files whose names do not match the item convention (README.md, an index
    page) are skipped rather than sorted on, which would raise. Results are
    cached so each collection is parsed once per run.
    """
    if collection in _ITEM_CACHE:
        return _ITEM_CACHE[collection]

    directory = os.path.join(DOCS_DIR, collection)
    items = []
    if os.path.isdir(directory):
        matched = []
        for filename in os.listdir(directory):
            match = ITEM_FILENAME.match(filename)
            if match:
                matched.append((int(match.group(2)), match.group(1), filename))

        for _, item_id, filename in sorted(matched):
            front_matter = read_front_matter(os.path.join(directory, filename))
            if front_matter is not None:
                items.append((item_id, front_matter))

    _ITEM_CACHE[collection] = items
    return items


def references_of(item_id, front_matter):
    """{dataset: [entry keys]} for every *_references list in the front matter.

    A value that is not a list is recorded and skipped; iterating a bare
    string would yield one phantom citation per character.
    """
    out = {}
    for key, value in front_matter.items():
        if not key.endswith(REFERENCES_SUFFIX):
            continue
        dataset = key[: -len(REFERENCES_SUFFIX)]
        if value is None:
            out[dataset] = []
        elif isinstance(value, list):
            out[dataset] = [_key(entry) for entry in value]
        else:
            MALFORMED_REFERENCES.add((item_id, key, type(value).__name__))
    return out


def domain_of(front_matter):
    """The item's domain as display text. `domain:` with no value gives None."""
    domain = front_matter.get("domain")
    return str(domain) if domain else "?"


# ------------------------------------------------------------------ checks

def check_floor(library, strict_iosco=True):
    """([(collection, item_id, domain, [missing lenses])], {datasets with no lens})"""
    findings, unknown = [], set()

    for collection, required in FLOOR.items():
        for item_id, front_matter in iter_items(collection):
            present = set()
            for dataset, keys in references_of(item_id, front_matter).items():
                if not keys:
                    continue                      # declared but empty is not a citation
                if strict_iosco and dataset == IOSCO:
                    continue                      # supervisory only, per #426
                lens = (library.get(dataset) or {}).get("lens")
                if lens is None:
                    unknown.add(dataset)
                else:
                    present.add(lens)

            missing = [lens for lens in required if lens not in present]
            if missing:
                findings.append(
                    (collection, item_id, domain_of(front_matter), missing)
                )

    return findings, unknown


def check_cap(cap=CAP):
    """([(collection, item_id, domain, dataset, distinct)], [duplicates])

    The cap counts distinct entries, so a key repeated in one list does not
    push an item over on its own. Repeats are reported separately.
    """
    findings, duplicates = [], []
    seen_duplicates = set()
    for collection in FLOOR:
        for item_id, front_matter in iter_items(collection):
            for dataset, keys in sorted(references_of(item_id, front_matter).items()):
                distinct = len(set(keys))
                if len(keys) != distinct:
                    repeated = tuple(sorted({k for k in keys if keys.count(k) > 1}))
                    if (item_id, dataset, repeated) not in seen_duplicates:
                        seen_duplicates.add((item_id, dataset, repeated))
                        duplicates.append((item_id, dataset, list(repeated)))
                if distinct > cap:
                    findings.append(
                        (collection, item_id, domain_of(front_matter), dataset, distinct)
                    )
    return findings, duplicates


def check_reverse(library):
    """(usage, dangling, superseded_in_use)"""
    cited = {}
    for collection in CITING_COLLECTIONS:
        for item_id, front_matter in iter_items(collection):
            for dataset, keys in references_of(item_id, front_matter).items():
                for key in keys:
                    cited.setdefault(dataset, {}).setdefault(key, []).append(item_id)

    usage, dangling, superseded_in_use = {}, [], []
    for dataset, spec in sorted(library.items()):
        used = set(cited.get(dataset, {}))
        usage[dataset] = {
            "lens": spec["lens"],
            "used": len(used & spec["entries"]),
            "unused": len(spec["entries"] - used),
            "total": len(spec["entries"]),
        }
        for key in sorted(used - spec["entries"]):
            dangling.append((dataset, key, cited[dataset][key]))
        for key, successor in sorted(spec["superseded"].items()):
            if key in used:
                superseded_in_use.append((dataset, key, successor, cited[dataset][key]))

    # A *_references key whose dataset has no library file at all. The mapping
    # from front-matter key to filename is by convention; this surfaces any
    # item relying on a convention the library does not honour.
    unknown_datasets = sorted(set(cited) - set(library))

    return usage, dangling, superseded_in_use, unknown_datasets



def coverage_by_domain(library):
    """{collection: {domain: {"items": n, lens: n, ...}}}

    Rows are the domains introduced by #398, columns the lenses from #426.
    Crossing the two is what turns a list of defective items into a statement
    about which part of the catalogue is under-mapped.
    """
    out = {}
    for collection in FLOOR:
        rows = {}
        for item_id, front_matter in iter_items(collection):
            present = set()
            for dataset, keys in references_of(item_id, front_matter).items():
                if keys:
                    lens = (library.get(dataset) or {}).get("lens")
                    if lens:
                        present.add(lens)
            row = rows.setdefault(domain_of(front_matter),
                                  {"items": 0, "threat": 0, "obligation": 0, "control": 0})
            row["items"] += 1
            for lens in present:
                if lens in row:
                    row[lens] += 1
        out[collection] = rows
    return out


def coverage_by_standard(library):
    """{dataset: {"lens": str, collection: count_of_items_citing_it}}"""
    out = {dataset: dict({"lens": spec["lens"]},
                         **{collection: 0 for collection in FLOOR})
           for dataset, spec in library.items()}
    for collection in FLOOR:
        for item_id, front_matter in iter_items(collection):
            for dataset, keys in references_of(item_id, front_matter).items():
                if keys and dataset in out:
                    out[dataset][collection] += 1
    return out


def print_tables(library):
    """Markdown tables, for pasting into an issue or a PR description."""
    lenses = ["threat", "obligation", "control"]

    for collection, rows in coverage_by_domain(library).items():
        label = collection.lstrip("_")
        required = FLOOR[collection]
        headers = " | ".join(
            lens + (" *" if lens in required else "") for lens in lenses
        )
        print(f"\n### Coverage by domain — {label}\n")
        print(f"| domain | items | {headers} |")
        print("|---|---:|" + "---:|" * len(lenses))
        for domain in sorted(rows):
            row = rows[domain]
            cells = []
            for lens in lenses:
                # Only a lens this collection's floor requires can be short.
                short = lens in required and row[lens] < row["items"]
                cells.append(f"{row[lens]}" + (" ⚠" if short else ""))
            print(f"| {domain} | {row['items']} | {' | '.join(cells)} |")
        print(f"\n<sub>* required by the floor for {label}. "
              f"⚠ marks a required lens that not every item in the domain "
              f"holds.</sub>")

    totals = {c: len(iter_items(c)) for c in FLOOR}
    print("\n### Coverage by standard\n")
    print("| lens | standard | risks | mitigations |")
    print("|---|---|---:|---:|")
    by_standard = coverage_by_standard(library)
    for dataset in sorted(by_standard,
                          key=lambda d: (str(by_standard[d]["lens"]), d)):
        row = by_standard[dataset]
        print(f"| {row['lens']} | {dataset} | "
              f"{row['_risks']}/{totals['_risks']} | "
              f"{row['_mitigations']}/{totals['_mitigations']} |")
    print("\n<sub>Items citing the standard at least once. Generated by "
          "scripts/validate-item-references.py --tables.</sub>")


# ----------------------------------------------------------------- output

def plural(count, singular, suffix="s"):
    """'1 error' / '4 errors'."""
    return f"{count} {singular}{'' if count == 1 else suffix}"


def report(args):
    """Run all three checks, print the findings, and return an exit code.

    Only the floor, dangling citations, unparseable front matter and malformed
    reference values are errors. The cap, unused entries and repeated keys are
    printed for information.
    """
    library = load_library(REFERENCES_DIR)

    floor_findings, no_lens = check_floor(library, strict_iosco=not args.lenient_iosco)
    cap_findings, duplicates = check_cap(args.cap)
    usage, dangling, superseded_in_use, unknown_datasets = check_reverse(library)

    mode = "IOSCO counts (--lenient-iosco)" if args.lenient_iosco else "IOSCO excluded"
    print(f"Item reference check  [floor: {mode}; cap: {args.cap} per standard]")

    print("\nFloor")
    for collection, required in FLOOR.items():
        in_collection = [f for f in floor_findings if f[0] == collection]
        total = len(iter_items(collection))
        print(f"  {collection}  (needs {' + '.join(required)}): "
              f"{len(in_collection)} of {total} below floor")
        for _, item_id, domain, missing in in_collection:
            print(f"    {item_id:7s} [{domain:11s}] missing {', '.join(missing)}")

    print("\nCap  (reported, not failed)")
    over = {item_id for _, item_id, _, _, _ in cap_findings}
    extra = sum(count - args.cap for *_, count in cap_findings)
    verb = "cites" if len(over) == 1 else "cite"
    print(f"  {plural(len(over), 'item')} {verb} more than {args.cap} from a "
          f"standard ({plural(extra, 'reference')} above the cap)")
    for _, item_id, domain, dataset, count in sorted(
            cap_findings, key=lambda f: -f[4])[: args.top]:
        print(f"    {item_id:7s} [{domain:11s}] {dataset:28s} {count:3d}")
    if len(cap_findings) > args.top:
        print(f"    ... and {len(cap_findings) - args.top} more")

    print("\nReverse coverage")
    print(f"  {'standard':28s} {'lens':11s} {'used':>5s} {'unused':>7s} {'total':>6s}")
    for dataset, row in usage.items():
        print(f"  {dataset:28s} {str(row['lens']):11s} "
              f"{row['used']:5d} {row['unused']:7d} {row['total']:6d}")

    print("\n  Dangling citations (key not in the library):")
    for dataset, key, items in dangling:
        print(f"    {dataset}:{key}  cited by {', '.join(items)}")
    if not dangling:
        print("    none")

    print("\n  Superseded entries still cited:")
    for dataset, key, successor, items in superseded_in_use:
        print(f"    {dataset}:{key} -> {successor}  cited by {', '.join(items)}")
    if not superseded_in_use:
        print("    none")

    if duplicates:
        print("\n  Repeated keys within one reference list:")
        for item_id, dataset, repeated in duplicates:
            print(f"    {item_id} {dataset}: {', '.join(repeated)}")

    if PARSE_FAILURES:
        print("\n  Front matter that did not parse:")
        for filename, message in PARSE_FAILURES:
            print(f"    {filename}: {message}")

    if MALFORMED_REFERENCES:
        print("\n  Reference values that are not lists:")
        for item_id, key, kind in sorted(MALFORMED_REFERENCES):
            print(f"    {item_id} {key}: {kind}, expected a list")

    if args.tables:
        print_tables(library)

    for dataset in sorted(set(no_lens) | set(unknown_datasets)):
        print(f"\n  WARNING: '{dataset}' has no lens, or no file in "
              f"docs/_data/references/. Run scripts/validate-references.py.")

    # Errors fail the build. The cap is advisory until #426 settles whether the
    # front matter is meant to hold the full mapping; unused entries and
    # repeated keys are informational.
    errors = (len(floor_findings) + len(dangling)
              + len(PARSE_FAILURES) + len(MALFORMED_REFERENCES))
    print(f"\n{plural(errors, 'error')}: "
          f"{len(floor_findings)} below floor, "
          f"{len(dangling)} dangling, "
          f"{len(PARSE_FAILURES)} unparseable, "
          f"{len(MALFORMED_REFERENCES)} malformed.")
    if args.warn and errors:
        print("Reporting only (--warn); not failing the build.")
        return 0
    return 1 if errors else 0


def main(argv=None):
    """Parse arguments and run the report. Returns the process exit code."""
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--lenient-iosco", action="store_true",
                        help="let a citation of IOSCO alone satisfy the obligation "
                             "floor (#426 says it should not)")
    parser.add_argument("--warn", action="store_true",
                        help="report findings but always exit 0")
    parser.add_argument("--cap", type=int, default=CAP,
                        help=f"distinct references allowed per standard per item "
                             f"(default {CAP})")
    parser.add_argument("--tables", action="store_true",
                        help="also print markdown coverage tables, grouped by the "
                             "domains from #398")
    parser.add_argument("--top", type=int, default=10,
                        help="how many cap findings to list (default 10)")
    return report(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
