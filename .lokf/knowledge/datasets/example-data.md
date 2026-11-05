---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/example-data
genre: reference
title: Example data
description: "`linkml/tests/data/`: a valid example of each class that is not abstract, and a counter-example of each constraint, each naming the place it fails on its first line, which `linkml/tests/test_data.py` checks."
resource: linkml/tests/data
sources:
  - id: data-readme.md
    resource: linkml/tests/data/README.md
  - id: test_data.py
    resource: linkml/tests/test_data.py
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Example data

A file's name gives its class, as `ClassName-suffix.yaml`.[^data-readme.md] `linkml/tests/test_data.py` holds each valid example to both the generated dataclasses and the validator. It holds each counter-example to the JSON pointer its first line names.[^test_data.py]

[^data-readme.md]: linkml/tests/data/README.md
[^test_data.py]: linkml/tests/test_data.py
