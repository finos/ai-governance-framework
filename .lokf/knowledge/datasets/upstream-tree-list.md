---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/upstream-tree-list
genre: reference
title: List of FINOS's files
description: "`linkml/tests/upstream_tree.tsv`: each of the 153 files of FINOS's pinned commit, with its git object hash, which the tests and the weekly watch compare."
resource: linkml/tests/upstream_tree.tsv
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
sources:
  - id: test_upstream_tree.py
    resource: linkml/tests/test_upstream_tree.py
  - id: check_upstream_release.py
    resource: linkml/scripts/check_upstream_release.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# List of FINOS's files

`linkml/tests/test_upstream_tree.py` compares the list with the repository's files, offline.[^test_upstream_tree.py] `linkml/scripts/check_upstream_release.py` compares it with FINOS's main.[^check_upstream_release.py]

[^test_upstream_tree.py]: linkml/tests/test_upstream_tree.py
[^check_upstream_release.py]: linkml/scripts/check_upstream_release.py, the docstring
