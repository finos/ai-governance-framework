"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

import ai_governance_framework.datamodel.ai_governance_framework

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))

SCHEMA = (
    Path(__file__).parent.parent
    / "src"
    / "ai_governance_framework"
    / "schema"
    / "ai_governance_framework.yaml"
)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        ai_governance_framework.datamodel.ai_governance_framework,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint (docs/index.md says what the generated models leave out), so each
# example is held to it: a valid one must pass, and a counter-example must fail.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text()),
        str(SCHEMA),
        Path(filepath).stem.split("-")[0],
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, so a file that starts failing for
    another reason fails this test."""
    text = Path(filepath).read_text()
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    report = validate(
        yaml.safe_load(text), str(SCHEMA), Path(filepath).stem.split("-")[0]
    )
    messages = [r.message for r in report.results]
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


def test_every_concept_class_has_an_example():
    """Each class a knowledge-bundle concept may name as its type, and each
    class those hold, has a valid example."""
    classes = {
        name
        for name, cls in SchemaView(str(SCHEMA)).all_classes().items()
        if not cls.abstract
    }
    examples = {Path(f).stem.split("-")[0] for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)
