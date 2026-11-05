---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/adapt-copy
genre: reference
title: The adapt copy
description: "`.lokf/ai-governance-framework.yaml`, the copy `lokf adapt` writes from the schema: it re-roots `AigfItem` and `AigfDataClassification` on `Concept`, and renames `version`, `name`, `url`, `source` and `references` with an `aigf_` prefix."
resource: .lokf/ai-governance-framework.yaml
derivedFrom:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
sources:
  - id: project.justfile
    resource: linkml/project.justfile
    title: the adapt recipes
  - id: linkml-readme.md
    resource: linkml/README.md
    title: Knowledge Trust Ladder
  - id: test_schema_rules.py
    resource: linkml/tests/test_schema_rules.py
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: .lokf/lokf.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# The adapt copy

`just lokf-adapt`, run from `linkml/`, rewrites the copy, and `just lokf-adapt-check` fails when it is stale.[^project.justfile] A release attaches it as `schema-<tag>-ai-governance-framework.yaml`.[^linkml-readme.md]

`linkml/tests/test_schema_rules.py` holds its names apart from LOKF's and from the neighbours' copies, and lists the keys it shares with them.[^test_schema_rules.py]

[^project.justfile]: linkml/project.justfile, the adapt recipes
[^linkml-readme.md]: linkml/README.md, Knowledge Trust Ladder
[^test_schema_rules.py]: linkml/tests/test_schema_rules.py
