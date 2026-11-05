# ai-governance-framework

This project is a LinkML model of the AI Governance Framework that FINOS publishes for financial services, at v3 of 26 October 2026. It holds the framework's facts as records, and each record keeps FINOS's keys and values.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together, where each part comes from and what the model leaves out
- [`ai_governance_framework.yaml`](schema/ai_governance_framework.yaml): the schema

## Validating

The catalogue:

```bash
uv run linkml-validate -s src/ai_governance_framework/schema/ai_governance_framework.yaml -C AigfCatalogue src/ai_governance_framework/data/aigf-v3.yaml
```

One of FINOS's reference files, unchanged:

```bash
uv run linkml-validate -s src/ai_governance_framework/schema/ai_governance_framework.yaml -C AigfReferenceFile ../docs/_data/references/owasp-llm.yml
```

`project/jsonschema/ai_governance_framework.schema.json` is the same schema for anyone without LinkML.

## What the catalogue holds

| Part | Records |
| --- | --- |
| Risks | 24 |
| Mitigations | 25 |
| Worked use cases | 4 |
| Reference files, by their keys | 13 |
| Lenses | 3 |
| Classes of financial data | 11 |
| Top levels of the use case taxonomy | 5 |
| Cross-cutting capabilities | 5 |
| Axes of the deployment model | 9 |

`tests/test_catalogue.py` holds these counts, validates the file with the committed JSON Schema, and loads it into the generated dataclasses and Pydantic models.

## What the validator does not check

JSON Schema looks at one value at a time. It does not check that a citation resolves in its reference file, that a page's related risk exists, or that `sequence` equals the number in the page's identifier. `tests/aigf_rules.py` states these rules, `tests/test_upstream_tree.py` runs them over FINOS's files, and `tests/test_rules.py` shows that each one finds a planted fault.

The generated Python models hold the same classes and leave out what the validator leaves out. They also do not check the patterns a slot carries through `slot_usage`, so validate with the JSON Schema or `linkml-validate`.
