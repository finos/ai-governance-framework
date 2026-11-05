#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Write one SSSOM set for each of FINOS's reference files.

Each row says that a page of the framework cites an entry of that file, as the
page's front matter states. FINOS's maintainers wrote the citations, so the rows
are curated, and FINOS is their provider. A citation is not an equivalence, so
every predicate is skos:relatedMatch. Each object keeps the key FINOS's file gives
it, under a namespace this project binds for that file, and object_source names the
address the file was generated from. A row carries the entry's title as its label
only where LABEL_POSITIONS records that the publisher's terms allow it: a file whose
titles may be another publisher's headings, or whose terms could not be read, names
each entry by key alone.

Usage::

    python scripts/build_sssom_mappings.py          # write the sets
    python scripts/build_sssom_mappings.py --check  # exit 1 when one differs
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS = ROOT / "src" / "ai_governance_framework" / "mappings"
NAMESPACE = "https://w3id.org/lmodel/ai-governance-framework/"
# Whether a set carries each entry's title as object_label, by reference file, with
# the terms read on 2026-11-05 that decide it. FINOS publishes every file under
# CC-BY-4.0, and the catalogue holds the keys alone; a label here is a copy of the
# cited work's own name, so the cited work's terms decide. None means the set names
# the entry by key alone. tests/test_mappings.py holds every reference file to an
# entry here, so a file FINOS adds is decided before its set is written.
LABEL_POSITIONS = {
    "atr": "MIT; the rules' own identifiers and names",
    "canada-regulations": "the names of Crown and regulators' documents, as FINOS cites them",
    "eu-ai-act": "the regulation's article headings; EU law is free to reuse (Decision 2011/833/EU)",
    "ffiec-itbooklets": "a United States government work (17 U.S.C. 105)",
    "iosco-supervisory-toolkit": None,  # IOSCO's; its terms could not be read on 2026-11-05
    "iso-42001": None,  # the titles may be ISO's headings
    "nist-ai-600-1": "a United States government work (17 U.S.C. 105)",
    "nist-sp-800-53r5": "a United States government work (17 U.S.C. 105)",
    "owasp-asi": "CC BY-SA 4.0; the entries' names, with OWASP named as the source",
    "owasp-llm": "CC BY-SA 4.0; the entries' names, with OWASP named as the source",
    "owasp-ml": "CC BY-SA 4.0; the entries' names, with OWASP named as the source",
    "sr11-7": "a United States government work (17 U.S.C. 105)",
    "uk-regulations": "the names of Crown and regulators' documents, as FINOS cites them",
}
COLUMNS = (
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "object_source",
    "mapping_justification",
)
LICENSE = "https://creativecommons.org/licenses/by/4.0/"
PROVIDER = "https://github.com/finos/ai-governance-framework"


def _builder():
    spec = importlib.util.spec_from_file_location(
        "build_catalogue", Path(__file__).parent / "build_catalogue.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def object_prefix(stem: str) -> str:
    """The prefix a set binds for the keys of one reference file."""
    return "aigf_" + stem.replace("-", "_")


def set_path(stem: str) -> Path:
    return MAPPINGS / f"finos_to_{stem.replace('-', '_')}.sssom.tsv"


def cell(value: object) -> str:
    """One field of a row. A tab or a line break would split the row, so a value
    that holds one is refused rather than written."""
    text = str(value)
    if "\t" in text or "\n" in text or "\r" in text:
        raise ValueError(f"a tab or a line break in an SSSOM field: {text!r}")
    return text


def citations(catalogue: dict, stem: str):
    """Each page's citation of one reference file, in the catalogue's order."""
    slot = stem.replace("-", "_") + "_references"
    for section in ("risks", "mitigations", "use_cases"):
        for record in catalogue.get(section) or []:
            for key in record.get(slot) or []:
                yield record, key


def render(catalogue: dict, stem: str, reference: dict) -> str:
    prefix = object_prefix(stem)
    header = [
        ("mapping_set_id", f"{NAMESPACE}mappings/{set_path(stem).name}"),
        ("mapping_set_version", catalogue["version"]),
        (
            "mapping_set_title",
            f"Citations of {stem} in the FINOS AI Governance Framework {catalogue['version']}",
        ),
        (
            "mapping_set_description",
            "Each row says that a page of the framework cites an entry of this "
            "reference file. FINOS's maintainers wrote the citations in the pages' "
            "front matter. A citation is not an equivalence.",
        ),
        ("license", LICENSE),
        ("mapping_provider", PROVIDER),
        ("mapping_date", catalogue["release_date"]),
    ]
    lines = [f"# {key}: {value}" for key, value in header]
    lines.append("# curie_map:")
    for key, value in (
        ("ai_governance_framework", NAMESPACE),
        (prefix, f"{NAMESPACE}references/{stem}/"),
        ("semapv", "https://w3id.org/semapv/vocab/"),
        ("skos", "http://www.w3.org/2004/02/skos/core#"),
    ):
        lines.append(f"#   {key}: {value}")
    labelled = LABEL_POSITIONS[stem] is not None
    lines.append("\t".join(c for c in COLUMNS if labelled or c != "object_label"))
    for record, key in citations(catalogue, stem):
        row = [
            f"ai_governance_framework:{record['item_id']}",
            record["title"],
            "skos:relatedMatch",
            f"{prefix}:{key}",
            *([reference["entries"][key]["title"]] if labelled else []),
            reference.get("source_url") or "",
            "semapv:ManualMappingCuration",
        ]
        lines.append("\t".join(cell(value) for value in row))
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="Exit 1 when a set differs"
    )
    args = parser.parse_args(argv)
    builder = _builder()
    catalogue = builder.catalogue(builder.read_yaml(builder.SCHEMA))
    status = 0
    for stem, reference in builder.reference_files().items():
        path = set_path(stem)
        text = render(catalogue, stem, reference)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                print(
                    f"{path.relative_to(ROOT)} differs from FINOS's files.",
                    file=sys.stderr,
                )
                status = 1
        else:
            path.write_text(text, encoding="utf-8")
    if not args.check:
        print(f"Wrote {len(builder.reference_files())} sets.")
    return status


if __name__ == "__main__":
    sys.exit(main())
