"""Holds the schema to FINOS's own files, and FINOS's files to the pin.

FINOS's tree sits beside linkml/, unchanged. These tests show that it matches the
pinned commit byte for byte, that every file the schema models validates, and that
the rules FINOS states and no validator checks hold over it.
"""

import hashlib
import importlib.util
import json
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from aigf_rules import (
    citation_faults,
    citation_slot,
    cross_reference_faults,
    items,
    page_faults,
    reference_file_faults,
    use_case_faults,
)

ROOT = Path(__file__).parent.parent
TREE = ROOT.parent
DOCS = TREE / "docs"
SCHEMA = (
    ROOT / "src" / "ai_governance_framework" / "schema" / "ai_governance_framework.yaml"
)
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "ai_governance_framework.schema.json"
BUILDER = ROOT / "scripts" / "build_catalogue.py"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
MANIFEST = Path(__file__).parent / "upstream_tree.tsv"
DEPARTURES = Path(__file__).parent / "departures.yaml"


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _builder():
    return _module("build_catalogue_under_test", BUILDER)


@lru_cache(maxsize=1)
def _watch():
    return _module("watch_pins", WATCH)


@lru_cache(maxsize=1)
def _schema():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _config():
    return yaml.safe_load((DOCS / "_config.yml").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _catalogue():
    return _builder().catalogue(_schema())


@lru_cache(maxsize=1)
def _json_schema():
    return json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))


def _errors(instance, class_name):
    """What the committed JSON Schema refuses in an instance of a class."""
    schema = {
        "$schema": _json_schema()["$schema"],
        "$defs": _json_schema()["$defs"],
        "$ref": f"#/$defs/{class_name}",
    }
    return [
        e.message for e in jsonschema.Draft202012Validator(schema).iter_errors(instance)
    ]


def _blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_finos_tree_is_the_pinned_commit():
    """Every file the pinned commit holds is here, byte for byte."""
    differing = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha, path = line.split("\t", 1)
        local = TREE / path
        if not local.is_file() or _blob_sha(local) != sha:
            differing.append(path)
    assert not differing


def test_the_pins_agree():
    """The header, the watch and FINOS's _config.yml name one edition and one commit."""
    header = _schema()
    commit = header["annotations"]["upstream_commit"]
    assert commit == _watch().PINNED_COMMIT
    assert header["source"].endswith(f"/tree/{commit}")
    assert header["version"] == _config()["version"] == _watch().PINNED_EDITION
    assert header["annotations"]["upstream_release_date"] == str(
        _config()["release-date"]
    )
    assert header["annotations"]["upstream_license"] == "CC-BY-4.0"
    assert "PackageLicenseDeclared: CC-BY-4.0" in (TREE / "LICENSE.spdx").read_text(
        encoding="utf-8"
    )


@pytest.mark.parametrize("class_name", ["AigfRisk", "AigfMitigation", "AigfUseCase"])
def test_every_page_validates(class_name):
    """Each page's front matter validates once its keys are renamed."""
    builder = _builder()
    pages = builder.pages(class_name)
    assert pages
    for path, matter in pages:
        record = builder.page_record(_schema(), class_name, path, matter)
        assert not _errors(record, class_name), path.name


@pytest.mark.parametrize("class_name", ["AigfRisk", "AigfMitigation", "AigfUseCase"])
def test_the_renaming_is_one_to_one(class_name):
    """A record gives back FINOS's front matter exactly: no two keys fold into one,
    and each key the page writes is kept, under the slot that lists it."""
    builder = _builder()
    table = builder.renames(_schema(), class_name)
    back = {slot: key for key, slot in table.items()}
    assert len(back) == len(table)
    slots = set(builder.class_slots(_schema(), class_name))
    for path, matter in builder.pages(class_name):
        record = builder.page_record(_schema(), class_name, path, matter)
        added = {
            "item_id": record.pop("item_id"),
            "source_file": record.pop("source_file"),
        }
        assert set(record) <= slots, path.name
        assert {back.get(k, k): v for k, v in record.items()} == matter, path.name
        assert added["source_file"] == path.relative_to(TREE).as_posix()


def test_a_key_outside_the_schema_fails_rather_than_passing():
    """Front matter with no renaming fails, so the closed classes are doing their work."""
    builder = _builder()
    path, matter = builder.pages("AigfRisk")[0]
    assert _errors(matter, "AigfRisk"), path.name


@pytest.mark.parametrize(
    "stem", sorted(p.stem for p in (DOCS / "_data/references").glob("*.yml"))
)
def test_every_reference_file_validates_unchanged(stem):
    """A reference file needs no renaming: FINOS's keys are the schema's."""
    reference = _builder().reference_files()[stem]
    assert not _errors(reference, "AigfReferenceFile"), stem
    assert not reference_file_faults(stem, reference)


def test_finos_own_reference_check_passes():
    """scripts/validate-references.py, which FINOS's workflow runs, agrees."""
    result = subprocess.run(
        [sys.executable, str(TREE / "scripts" / "validate-references.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout


def test_every_reference_file_has_a_citation_slot_and_every_slot_a_file():
    stems = set(_builder().reference_files())
    slots = _schema()["classes"]["AigfReferenceCitations"]["slots"]
    assert {citation_slot(stem) for stem in stems} == set(slots)
    for stem in stems:
        slot = _schema()["slots"][citation_slot(stem)]
        assert slot["description"] == f"Keys of docs/_data/references/{stem}.yml."


def test_every_page_of_the_collections_is_read():
    """A page with no front matter is only the taxonomy's prose, uc-index.md."""
    builder = _builder()
    for class_name, folder in builder.COLLECTIONS.items():
        named = {p.name for p, _ in builder.pages(class_name)}
        others = {p.name for p in (DOCS / folder).glob("*.md")} - named
        assert others == ({"uc-index.md"} if class_name == "AigfUseCase" else set())


def test_the_catalogue_breaks_no_rule():
    catalogue = _catalogue()
    assert not page_faults(catalogue)
    assert not cross_reference_faults(catalogue)
    assert not citation_faults(catalogue)
    assert not use_case_faults(catalogue)


def test_every_risk_has_a_mitigation():
    """A risk lists no mitigations of its own, so the mitigations must reach each one."""
    catalogue = _catalogue()
    reached = {r for m in catalogue["mitigations"] for r in m["mitigates"]}
    assert {r["item_id"] for r in catalogue["risks"]} == reached


def test_the_departures_are_listed():
    """FINOS's files depart from FINOS's statements in the places listed, and no others."""
    departures = yaml.safe_load(DEPARTURES.read_text(encoding="utf-8"))
    listed = set(_config()["usecase_categories"])
    categories = {
        item["item_id"]: item["category"]
        for item in _catalogue()["use_cases"]
        if item["category"] not in listed
    }
    assert categories == departures["category_not_listed"]
    superseded = {}
    for stem, reference in _builder().reference_files().items():
        for item in items(_catalogue()):
            cited = [
                key
                for key in item.get(citation_slot(stem)) or []
                if "superseded_by" in reference["entries"][key]
            ]
            if cited:
                superseded.setdefault(item["item_id"], {})[stem] = cited
    assert superseded == departures["superseded_citations"]


def _labels(enum):
    return {
        name: (value or {}).get("title")
        for name, value in _schema()["enums"][enum]["permissible_values"].items()
    }


@pytest.mark.parametrize(
    ("enum", "key"),
    [
        ("AigfRiskType", "risk_type_labels"),
        ("AigfMitigationType", "mitigation_type_labels"),
        ("AigfRiskDomain", "risk_domain_labels"),
        ("AigfMitigationDomain", "mitigation_domain_labels"),
    ],
)
def test_the_label_enums_are_the_config(enum, key):
    assert _labels(enum) == _config()[key]


def test_the_status_enum_is_the_config():
    values = _schema()["enums"]["AigfDocumentStatus"]["permissible_values"]
    assert {k: v["description"] for k, v in values.items()} == {
        s["name"]: s["description"] for s in _config()["document_status"]
    }


def test_the_category_enum_is_the_config_and_the_listed_departures():
    departures = yaml.safe_load(DEPARTURES.read_text(encoding="utf-8"))
    assert set(_labels("AigfUseCaseCategory")) == set(
        _config()["usecase_categories"]
    ) | set(departures["category_not_listed"].values())


def test_the_lens_enum_is_the_config():
    values = _schema()["enums"]["AigfLens"]["permissible_values"]
    assert {k: v["description"] for k, v in values.items()} == {
        k: v["question"] for k, v in _config()["reference_lenses"].items()
    }


def test_the_sensitivity_enum_is_the_data():
    values = set(_schema()["enums"]["AigfSensitivity"]["permissible_values"])
    assert values == {
        c["sensitivity"] for c in _catalogue()["financial_data_classification"]
    }


def test_the_data_handling_enum_is_the_axis():
    axis = next(
        a
        for a in _catalogue()["ai_deployment_model_taxonomy"]
        if a["name"] == "data_handling"
    )
    assert set(_schema()["enums"]["AigfDataHandling"]["permissible_values"]) == {
        o["name"] for o in axis["options"]
    }


def test_each_booklet_abbreviation_is_one_config_lists():
    known = set(_config()["ffiec_itbooklet_abbreviations"].values())
    entries = _builder().reference_files()["ffiec-itbooklets"]["entries"]
    assert {e["booklet_abbrev"] for e in entries.values()} <= known


def test_the_data_files_lose_nothing():
    """The two taxonomies' records give back FINOS's nested mappings."""
    builder = _builder()
    catalogue = _catalogue()
    assert [
        {d["name"]: [{a["name"]: a["use_case_names"]} for a in d["use_case_areas"]]}
        for d in catalogue["ai_use_cases"]
    ] == builder.read_yaml(DOCS / "_data" / "ai_use_cases.yml")["AI_use_cases"]
    original = builder.read_yaml(DOCS / "_data" / "ai_deployment_model.yml")
    assert [
        {
            a["name"]: [
                {o["name"]: {"description": o["description"]}} for o in a["options"]
            ]
        }
        for a in catalogue["ai_deployment_model_taxonomy"]
    ] == [
        {
            axis: [
                {name: {"description": value["description"].strip()}}
                for option in options
                for name, value in option.items()
            ]
        }
        for entry in original["ai_deployment_model_taxonomy"]
        for axis, options in entry.items()
    ]
