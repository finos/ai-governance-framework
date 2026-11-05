---
type: Playbook
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/playbooks/take-a-new-finos-edition
genre: how-to
title: Take a new edition from FINOS
description: "How to follow FINOS's main when the watch opens an issue: merge `upstream/main` on a branch, rewrite the list of files, move the pins, follow the changes, regenerate, and merge with a merge commit."
resource: linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
sources:
  - id: contributing.md
    resource: linkml/CONTRIBUTING.md
    title: Taking a new edition from FINOS
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Take a new edition from FINOS

The weekly watch opens an issue when FINOS's main changes a file the schema reads.[^contributing.md]

1. On a branch, merge `upstream/main`.[^contributing.md]
2. Rewrite `linkml/tests/upstream_tree.tsv` from `git ls-tree -r`.[^contributing.md]
3. Move the pin in `linkml/scripts/check_upstream_release.py` and the schema's header.[^contributing.md]
4. Follow the changes, and regenerate.[^contributing.md]
5. Merge with a merge commit.[^contributing.md]

A merge of FINOS's main is a release of this repository when one of FINOS's commits carries a releasing type, so write its changelog entry in the same pull request.[^semantic-release.yml]

[^contributing.md]: linkml/CONTRIBUTING.md, Taking a new edition from FINOS
[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header
