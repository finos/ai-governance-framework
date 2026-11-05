#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Write the catalogue from FINOS's files in this repository.

The catalogue is src/ai_governance_framework/data/aigf-<edition>.yaml. It holds
what the front matter of FINOS's risk, mitigation and use case pages states, and
what docs/_config.yml and docs/_data/ state. It names each reference file's entries
by key and leaves their titles in FINOS's files.

Each record keeps FINOS's keys, with three changes the schema's comments explain. A
slot's `aliases` name the key FINOS writes where the two differ; a page gains
item_id and source_file from its file name; and the two taxonomy files, which nest
one-key mappings, become lists of named records.

Usage::

    python scripts/build_catalogue.py          # write the catalogue
    python scripts/build_catalogue.py --check  # exit 1 when it differs
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT.parent
SCHEMA = (
    ROOT / "src" / "ai_governance_framework" / "schema" / "ai_governance_framework.yaml"
)
DOCS = TREE / "docs"
COLLECTIONS = {
    "AigfRisk": "_risks",
    "AigfMitigation": "_mitigations",
    "AigfUseCase": "_usecases",
}
ITEM_FILE = re.compile(r"^((?:ri|mi|uc)-[1-9][0-9]*)_")
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def catalogue_path(edition: str) -> Path:
    return ROOT / "src" / "ai_governance_framework" / "data" / f"aigf-{edition}.yaml"


def read_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def front_matter(path: Path) -> dict | None:
    """A page's front matter, or None for a file with none, such as uc-index.md."""
    found = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(found.group(1)) if found else None


def class_slots(schema: dict, name: str) -> list[str]:
    """Every slot a class lists, with those of its parents and mixins."""
    cls = schema["classes"][name]
    slots = list(cls.get("slots") or [])
    for parent in ([cls["is_a"]] if "is_a" in cls else []) + (cls.get("mixins") or []):
        slots += class_slots(schema, parent)
    return slots


def renames(schema: dict, name: str) -> dict[str, str]:
    """FINOS's key for each slot of a class that spells it otherwise."""
    return {
        alias: slot
        for slot in class_slots(schema, name)
        for alias in schema["slots"][slot].get("aliases") or []
    }


def pages(class_name: str) -> list[tuple[Path, dict]]:
    """Each page of a class that has front matter, in FINOS's order of sequence."""
    found = []
    for path in (DOCS / COLLECTIONS[class_name]).glob("*.md"):
        matter = front_matter(path)
        if matter is not None:
            found.append((path, matter))
    return sorted(found, key=lambda pair: pair[1]["sequence"])


def page_record(schema: dict, class_name: str, path: Path, matter: dict) -> dict:
    """A page's record: FINOS's keys through the schema's list, and what the file's
    name states."""
    table = renames(schema, class_name)
    record = {
        "item_id": ITEM_FILE.match(path.name).group(1),
        "source_file": path.relative_to(TREE).as_posix(),
    }
    for key, value in matter.items():
        record[table.get(key, key)] = value
    return record


def reference_files() -> dict[str, dict]:
    """Each reference file, by its stem."""
    folder = DOCS / "_data" / "references"
    return {path.stem: read_yaml(path) for path in sorted(folder.glob("*.yml"))}


def named_list(items: list[dict], child: str, leaf) -> list[dict]:
    """A list of one-key mappings as a list of records named by that key."""
    return [
        {"name": name, child: leaf(value)}
        for item in items
        for name, value in item.items()
    ]


def stripped(record: dict) -> dict:
    """A data file's record, without the newline a folded description ends with."""
    return {
        key: value.strip() if isinstance(value, str) else value
        for key, value in record.items()
    }


def use_case_taxonomy() -> dict:
    data = read_yaml(DOCS / "_data" / "ai_use_cases.yml")
    return {
        "ai_use_cases": named_list(
            data["AI_use_cases"],
            "use_case_areas",
            lambda areas: named_list(areas, "use_case_names", list),
        ),
        "cross_cutting_capabilities": data["cross_cutting_capabilities"],
    }


def deployment_taxonomy() -> list[dict]:
    axes = read_yaml(DOCS / "_data" / "ai_deployment_model.yml")
    return named_list(
        axes["ai_deployment_model_taxonomy"],
        "options",
        lambda options: [
            {"name": name, **stripped(value)}
            for option in options
            for name, value in option.items()
        ],
    )


def catalogue(schema: dict) -> dict:
    config = read_yaml(DOCS / "_config.yml")
    references = reference_files()
    classes = read_yaml(DOCS / "_data" / "data_classification.yml")
    return {
        "title": config["title"],
        "version": config["version"],
        "release_date": str(config["release-date"]),
        "source_commit": schema["annotations"]["upstream_commit"],
        "reference_lenses": [
            {"lens": lens, **values}
            for lens, values in config["reference_lenses"].items()
        ],
        "reference_indexes": [
            {
                "reference_file": stem,
                "lens": data["lens"],
                "entry_keys": list(data["entries"]),
            }
            for stem, data in references.items()
        ],
        "risks": [
            page_record(schema, "AigfRisk", path, matter)
            for path, matter in pages("AigfRisk")
        ],
        "mitigations": [
            page_record(schema, "AigfMitigation", path, matter)
            for path, matter in pages("AigfMitigation")
        ],
        "use_cases": [
            page_record(schema, "AigfUseCase", path, matter)
            for path, matter in pages("AigfUseCase")
        ],
        "financial_data_classification": [
            stripped(item) for item in classes["financial_data_classification"]
        ],
        **use_case_taxonomy(),
        "ai_deployment_model_taxonomy": deployment_taxonomy(),
    }


class _Dumper(yaml.SafeDumper):
    """Indents a list under its key, as the repository's YAML lint asks."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def render(data: dict) -> str:
    return (
        "# Written by scripts/build_catalogue.py from FINOS's files. Do not edit it.\n"
        + yaml.dump(data, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=88)
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="Exit 1 when the catalogue differs"
    )
    args = parser.parse_args(argv)
    schema = read_yaml(SCHEMA)
    data = catalogue(schema)
    text = render(data)
    path = catalogue_path(data["version"])
    if args.check:
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            print(
                f"{path.relative_to(ROOT)} differs from FINOS's files.", file=sys.stderr
            )
            return 1
        print(f"{path.relative_to(ROOT)} matches FINOS's files.")
        return 0
    path.write_text(text, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
