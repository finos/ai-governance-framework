"""Holds the committed catalogue to FINOS's files, the schema and the models."""

import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.loaders import yaml_loader

import ai_governance_framework.datamodel.ai_governance_framework as dataclasses_model
import ai_governance_framework.datamodel.ai_governance_framework_pydantic as pydantic_model

ROOT = Path(__file__).parent.parent
PACKAGE = ROOT / "src" / "ai_governance_framework"
CATALOGUE = PACKAGE / "data" / "aigf-v3.yaml"
SCHEMA = PACKAGE / "schema" / "ai_governance_framework.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "ai_governance_framework.schema.json"
BUILDER = ROOT / "scripts" / "build_catalogue.py"

# FINOS's counts at the pinned commit, which the site's own pages list.
COUNTS = {
    "risks": 24,
    "mitigations": 25,
    "use_cases": 4,
    "reference_indexes": 13,
    "reference_lenses": 3,
    "financial_data_classification": 11,
    "ai_use_cases": 5,
    "cross_cutting_capabilities": 5,
    "ai_deployment_model_taxonomy": 9,
}


@lru_cache(maxsize=1)
def _catalogue():
    return yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))


def _builder():
    spec = importlib.util.spec_from_file_location("build_catalogue_check", BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_the_catalogue_is_what_the_builder_writes():
    """The committed file equals what FINOS's files give, byte for byte."""
    assert _builder().main(["--check"]) == 0


def test_the_counts():
    for section, count in COUNTS.items():
        assert len(_catalogue()[section]) == count, section


def test_the_catalogue_passes_the_committed_json_schema():
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(_catalogue()))
    assert not errors, [e.message for e in errors[:5]]


def test_the_committed_json_schema_is_current():
    """The file the tests above read is what the schema generates."""
    generated = JsonSchemaGenerator(str(SCHEMA)).serialize()
    assert json.loads(generated) == json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))


def test_the_catalogue_holds_no_reference_entry_titles():
    """A reference entry appears by key alone, since a file's titles may be another
    publisher's headings."""
    for index in _catalogue()["reference_indexes"]:
        assert set(index) == {"reference_file", "lens", "entry_keys"}
        assert all(isinstance(key, str) for key in index["entry_keys"])


def test_the_dataclasses_load_the_catalogue():
    loaded = yaml_loader.load(
        str(CATALOGUE), target_class=dataclasses_model.AigfCatalogue
    )
    assert len(loaded.risks) == COUNTS["risks"]


def test_the_pydantic_models_load_the_catalogue():
    loaded = pydantic_model.AigfCatalogue.model_validate(_catalogue())
    assert len(loaded.mitigations) == COUNTS["mitigations"]
