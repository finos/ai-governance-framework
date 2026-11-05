"""The rules FINOS states that no generated validator checks.

Each function reads a catalogue, or a reference file, and returns what breaks a
rule. tests/test_upstream_tree.py runs them over FINOS's files, and
tests/test_rules.py shows that each one finds a planted fault.
"""

from __future__ import annotations

import re

SECTIONS = ("risks", "mitigations", "use_cases")
CROSS_REFERENCES = {
    "related_risks": "risks",
    "mitigates": "risks",
    "related_mitigations": "mitigations",
}


def citation_slot(stem: str) -> str:
    """The slot that holds a page's citations of one reference file."""
    return stem.replace("-", "_") + "_references"


def items(catalogue: dict):
    """Every page of a catalogue."""
    for section in SECTIONS:
        yield from catalogue.get(section) or []


def page_faults(catalogue: dict) -> list[str]:
    """A page's sequence differs from its identifier, an identifier repeats, or a
    list repeats a value."""
    faults = []
    seen = set()
    for item in items(catalogue):
        identifier = item["item_id"]
        if identifier in seen:
            faults.append(f"{identifier}: repeated")
        seen.add(identifier)
        if int(identifier.split("-")[1]) != item["sequence"]:
            faults.append(f"{identifier}: sequence is {item['sequence']}")
        if not item["source_file"].rsplit("/", 1)[1].startswith(f"{identifier}_"):
            faults.append(f"{identifier}: file is {item['source_file']}")
        for key, value in item.items():
            if isinstance(value, list) and all(isinstance(v, str) for v in value):
                if len(set(value)) != len(value):
                    faults.append(f"{identifier}: {key} repeats a value")
    return faults


def cross_reference_faults(catalogue: dict) -> list[str]:
    """A page names a risk or a mitigation that does not exist, or itself."""
    known = {
        section: {item["item_id"] for item in catalogue.get(section) or []}
        for section in SECTIONS
    }
    faults = []
    for item in items(catalogue):
        for key, section in CROSS_REFERENCES.items():
            for target in item.get(key) or []:
                if target not in known[section]:
                    faults.append(f"{item['item_id']}: {key} names {target}")
                if target == item["item_id"]:
                    faults.append(f"{item['item_id']}: {key} names itself")
    return faults


def citation_faults(catalogue: dict) -> list[str]:
    """A page cites a key its reference file does not hold."""
    faults = []
    for index in catalogue.get("reference_indexes") or []:
        slot = citation_slot(index["reference_file"])
        keys = set(index["entry_keys"])
        for item in items(catalogue):
            for key in item.get(slot) or []:
                if key not in keys:
                    faults.append(f"{item['item_id']}: {slot} names {key}")
    return faults


def use_case_faults(catalogue: dict) -> list[str]:
    """A use case names a data classification or a data handling option that the
    data files do not list."""
    classes = {c["name"] for c in catalogue.get("financial_data_classification") or []}
    options = {
        option["name"]
        for axis in catalogue.get("ai_deployment_model_taxonomy") or []
        if axis["name"] == "data_handling"
        for option in axis["options"]
    }
    faults = []
    for item in catalogue.get("use_cases") or []:
        for use in item.get("data_classifications") or []:
            if use["name"] not in classes:
                faults.append(f"{item['item_id']}: classification {use['name']}")
        for aspect in item.get("data_handling_aspects") or []:
            if aspect not in options:
                faults.append(f"{item['item_id']}: data handling {aspect}")
    return faults


def reference_file_faults(stem: str, reference: dict) -> list[str]:
    """A file has no entries or superseded_by names no entry of the file, as
    scripts/validate-references.py refuses, or an entry's key has a character
    outside letters, digits, dots and hyphens. That last rule is this project's:
    docs/_data/references/README.md asks for a stable identifier, and the key is
    the local part of a CURIE in the SSSOM sets."""
    entries = reference.get("entries") or {}
    faults = [] if entries else [f"{stem}: no entries"]
    for key, entry in entries.items():
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*", key):
            faults.append(f"{stem}: key {key} has a character outside the keys' form")
        successor = entry.get("superseded_by")
        if successor is not None and successor not in entries:
            faults.append(
                f"{stem}: {key} is superseded by {successor}, which is not there"
            )
    return faults
