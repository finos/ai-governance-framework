---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: "`linkml/tests/neighbours/`: the adapt copies of 27 released lmodel repositories, each the schema asset of a release and pinned by its checksum, so that tests can hold this schema's names and mappings to them."
resource: linkml/tests/neighbours
sources:
  - id: test_schema_rules.py
    resource: linkml/tests/test_schema_rules.py
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/adapt-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Neighbours' adapt copies

`linkml/tests/test_schema_rules.py` pins each copy by SHA-256, with its repository and release in a comment.[^test_schema_rules.py]

The test checks that no class, enum, type or subset name is shared, and that the keys shared are the listed ones. It checks that each mapping to `nist_ai_600_1` and `nist_sp_800_53` names a class of that copy.[^test_schema_rules.py]

[^test_schema_rules.py]: linkml/tests/test_schema_rules.py
