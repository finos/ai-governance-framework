---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/departures
genre: reference
title: Departures from FINOS's own statements
description: "`linkml/tests/departures.yaml`: where FINOS's files break a statement of FINOS's own: a use case category `docs/_config.yml` does not list, and a citation of a superseded entry. A new departure fails a test."
resource: linkml/tests/departures.yaml
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
sources:
  - id: departures.yaml
    resource: linkml/tests/departures.yaml
  - id: test_upstream_tree.py
    resource: linkml/tests/test_upstream_tree.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Departures from FINOS's own statements

uc-3 and uc-4 write the category `Risk_and_Compliance`, which `usecase_categories` does not list. ri-30 cites `llm03-2025` and `llm06-2025`, which carry `superseded_by`.[^departures.yaml]

`linkml/tests/test_upstream_tree.py` holds the list to the tree, so a new departure fails and a fixed one must leave it.[^test_upstream_tree.py]

[^departures.yaml]: linkml/tests/departures.yaml
[^test_upstream_tree.py]: linkml/tests/test_upstream_tree.py
