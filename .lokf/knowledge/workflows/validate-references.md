---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/validate-references
genre: reference
title: Validate references (validate-references.yml)
description: "FINOS's own workflow, which stays as FINOS writes it: it runs `scripts/validate-references.py` when a reference file changes."
resource: .github/workflows/validate-references.yml
sources:
  - id: validate-references.yml
    resource: .github/workflows/validate-references.yml
  - id: test_upstream_tree.py
    resource: linkml/tests/test_upstream_tree.py
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Validate references (validate-references.yml)

The workflow runs on a push or a pull request that touches `docs/_data/references/` or the script.[^validate-references.yml] `linkml/tests/test_upstream_tree.py` also runs the script.[^test_upstream_tree.py]

[^validate-references.yml]: .github/workflows/validate-references.yml
[^test_upstream_tree.py]: linkml/tests/test_upstream_tree.py
