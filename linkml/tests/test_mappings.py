"""Holds the SSSOM sets to the citations in FINOS's front matter, both ways."""

import csv
import importlib.util
from functools import lru_cache
from pathlib import Path

import pytest
import yaml
from aigf_rules import citation_slot, items

ROOT = Path(__file__).parent.parent
MAPPINGS = ROOT / "src" / "ai_governance_framework" / "mappings"
SCRIPT = ROOT / "scripts" / "build_sssom_mappings.py"
CATALOGUE = ROOT / "src" / "ai_governance_framework" / "data" / "aigf-v3.yaml"


@lru_cache(maxsize=1)
def _script():
    spec = importlib.util.spec_from_file_location("build_sssom_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _catalogue():
    return yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _reference_files():
    return _script()._builder().reference_files()


STEMS = [
    i["reference_file"]
    for i in yaml.safe_load(CATALOGUE.read_text())["reference_indexes"]
]


def _set(stem):
    """A set's header, as parsed YAML, and its rows."""
    lines = _script().set_path(stem).read_text(encoding="utf-8").splitlines()
    header = yaml.safe_load("\n".join(x[2:] for x in lines if x.startswith("# ")))
    rows = list(
        csv.DictReader(
            [x for x in lines if not x.startswith("#")],
            delimiter="\t",
            quoting=csv.QUOTE_NONE,
        )
    )
    return header, rows


def test_the_sets_are_what_the_script_writes():
    assert _script().main(["--check"]) == 0


def test_there_is_one_set_for_each_reference_file():
    named = {p.name for p in MAPPINGS.glob("*.tsv")}
    assert named == {_script().set_path(stem).name for stem in STEMS}


@pytest.mark.parametrize("stem", STEMS)
def test_each_row_is_a_citation_and_each_citation_a_row(stem):
    _, rows = _set(stem)
    prefix = _script().object_prefix(stem)
    stated = {
        (f"ai_governance_framework:{item['item_id']}", f"{prefix}:{key}")
        for item in items(_catalogue())
        for key in item.get(citation_slot(stem)) or []
    }
    found = [(row["subject_id"], row["object_id"]) for row in rows]
    assert len(found) == len(set(found))
    assert set(found) == stated


@pytest.mark.parametrize("stem", STEMS)
def test_each_set_says_what_a_row_is(stem):
    header, rows = _set(stem)
    prefix = _script().object_prefix(stem)
    assert set(header["curie_map"]) == {
        "ai_governance_framework",
        prefix,
        "semapv",
        "skos",
    }
    assert (
        header["mapping_provider"] == "https://github.com/finos/ai-governance-framework"
    )
    assert {row["predicate_id"] for row in rows} == {"skos:relatedMatch"}
    assert {row["mapping_justification"] for row in rows} == {
        "semapv:ManualMappingCuration"
    }


def test_every_reference_file_has_a_label_position():
    """A set carries the entries' titles only where the builder records that the
    cited work's terms allow it, so a file FINOS adds is decided before its set is
    written, and the two decisions below hold."""
    assert set(STEMS) == set(_script().LABEL_POSITIONS)
    assert {
        stem for stem, position in _script().LABEL_POSITIONS.items() if position is None
    } == {"iso-42001", "iosco-supervisory-toolkit"}


@pytest.mark.parametrize("stem", STEMS)
def test_a_set_carries_a_label_only_where_its_position_allows(stem):
    _, rows = _set(stem)
    assert rows
    labelled = _script().LABEL_POSITIONS[stem] is not None
    assert ("object_label" in rows[0]) == labelled
    if labelled:
        assert all(row["object_label"] for row in rows)


@pytest.mark.parametrize("stem", STEMS)
def test_each_row_names_the_file_it_cites(stem):
    """object_source is the address the reference file was generated from, or
    empty when the file names none."""
    _, rows = _set(stem)
    source = _reference_files()[stem].get("source_url") or ""
    assert {row["object_source"] for row in rows} == {source}


def test_a_field_with_a_tab_is_refused():
    with pytest.raises(ValueError):
        _script().cell("a\tb")
    with pytest.raises(ValueError):
        _script().cell("a\nb")
    assert _script().cell("a b") == "a b"
