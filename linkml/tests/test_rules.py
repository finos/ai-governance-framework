"""Each rule in tests/aigf_rules.py finds a planted fault."""

import copy

import pytest
from aigf_rules import (
    citation_faults,
    cross_reference_faults,
    page_faults,
    reference_file_faults,
    use_case_faults,
)

BASE = {
    "reference_indexes": [
        {"reference_file": "owasp-llm", "lens": "threat", "entry_keys": ["llm01-2026"]}
    ],
    "financial_data_classification": [{"name": "Customer_PII_Data"}],
    "ai_deployment_model_taxonomy": [
        {"name": "data_handling", "options": [{"name": "Centralized"}]}
    ],
    "risks": [
        {
            "item_id": "ri-1",
            "sequence": 1,
            "source_file": "docs/_risks/ri-1_a.md",
            "related_risks": [],
            "owasp_llm_references": ["llm01-2026"],
        },
        {"item_id": "ri-2", "sequence": 2, "source_file": "docs/_risks/ri-2_b.md"},
    ],
    "mitigations": [
        {
            "item_id": "mi-1",
            "sequence": 1,
            "source_file": "docs/_mitigations/mi-1_a.md",
            "mitigates": ["ri-1"],
        }
    ],
    "use_cases": [
        {
            "item_id": "uc-1",
            "sequence": 1,
            "source_file": "docs/_usecases/uc-1_a.md",
            "data_classifications": [{"name": "Customer_PII_Data"}],
            "data_handling_aspects": ["Centralized"],
        }
    ],
}


def test_the_base_breaks_no_rule():
    for rule in (page_faults, cross_reference_faults, citation_faults, use_case_faults):
        assert rule(BASE) == []


def _planted(section, index, key, value):
    planted = copy.deepcopy(BASE)
    planted[section][index][key] = value
    return planted


@pytest.mark.parametrize(
    ("rule", "section", "key", "value"),
    [
        (page_faults, "risks", "sequence", 7),
        (page_faults, "risks", "source_file", "docs/_risks/ri-9_a.md"),
        (page_faults, "risks", "owasp_llm_references", ["llm01-2026", "llm01-2026"]),
        (page_faults, "risks", "item_id", "ri-2"),
        (cross_reference_faults, "risks", "related_risks", ["ri-99"]),
        (cross_reference_faults, "risks", "related_risks", ["ri-1"]),
        (cross_reference_faults, "mitigations", "mitigates", ["mi-1"]),
        (cross_reference_faults, "mitigations", "related_mitigations", ["mi-99"]),
        (citation_faults, "risks", "owasp_llm_references", ["llm99-2026"]),
        (use_case_faults, "use_cases", "data_classifications", [{"name": "Other"}]),
        (use_case_faults, "use_cases", "data_handling_aspects", ["Other"]),
    ],
)
def test_a_rule_finds_a_planted_fault(rule, section, key, value):
    assert rule(_planted(section, 0, key, value))


@pytest.mark.parametrize(
    "reference",
    [
        {"entries": {}},
        {"entries": {"a key": {"title": "T", "url": "https://example.org"}}},
        {
            "entries": {
                "a": {"title": "T", "url": "https://x.org", "superseded_by": "b"}
            }
        },
    ],
)
def test_a_reference_file_rule_finds_a_planted_fault(reference):
    assert reference_file_faults("x", reference)


def test_a_good_reference_file_breaks_no_rule():
    entries = {
        "a": {"title": "T", "url": "https://example.org", "superseded_by": "b"},
        "b": {"title": "U", "url": "https://example.org"},
    }
    assert reference_file_faults("x", {"entries": entries}) == []
