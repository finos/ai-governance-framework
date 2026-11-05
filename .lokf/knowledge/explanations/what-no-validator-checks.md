---
type: Explanation
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/explanations/what-no-validator-checks
genre: explanation
title: What no validator checks
description: The rules the generated JSON Schema cannot state, such as a citation resolving in its reference file, which `linkml/tests/aigf_rules.py` holds, and why validation uses the JSON Schema rather than the generated Python models.
resource: linkml/tests/aigf_rules.py
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
sources:
  - id: index.md
    resource: linkml/docs/index.md
    title: What the validator does not check
  - resource: linkml/tests/test_rules.py
  - resource: linkml/tests/test_upstream_tree.py
  - resource: linkml/tests/conftest.py
  - resource: linkml/tests/test_data.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# What no validator checks

JSON Schema looks at one value at a time. It does not check that a citation resolves, that a related risk exists, or that `sequence` equals the number in the identifier.[^index.md]

`linkml/tests/aigf_rules.py` states those rules, `linkml/tests/test_upstream_tree.py` runs them over FINOS's files, and `linkml/tests/test_rules.py` shows that each one finds a planted fault.[^index.md]

[^index.md]: linkml/docs/index.md, What the validator does not check
