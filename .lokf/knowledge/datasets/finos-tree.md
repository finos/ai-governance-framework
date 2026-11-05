---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
genre: reference
title: FINOS's tree
description: "Every file FINOS's commit holds, unchanged at the repository's root: the pages under `docs/_risks/`, `docs/_mitigations/` and `docs/_usecases/`, the data under `docs/_data/`, the Jekyll site, and FINOS's scripts and governance files."
resource: docs
isPartOf:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/references/finos-ai-governance-framework
sources:
  - id: test_upstream_tree.py
    resource: linkml/tests/test_upstream_tree.py
    title: the docstring
  - id: conventions.md
    resource: CONVENTIONS.md
  - id: references-readme.md
    resource: docs/_data/references/README.md
  - id: mi-template.md
    resource: templates-for-ri-md/mi-template.md
  - resource: docs/_risks
  - resource: docs/_mitigations
  - resource: docs/_usecases
  - resource: docs/_data
  - resource: docs/_config.yml
  - resource: docs/adr
  - resource: scripts
  - resource: scripts_docs
  - resource: diagrams
  - resource: DEVELOPMENT.md
  - resource: GOVERNANCE.md
  - resource: MAINTAINERS.md
  - resource: CONTRIBUTING.md
  - resource: README.md
  - resource: NOTICE
  - resource: LICENSE
  - resource: LICENSE.spdx
  - resource: .gitattributes
  - resource: .gitignore
  - resource: .pre-commit-config.yaml
  - resource: .github/CODE_OF_CONDUCT.md
  - resource: .github/ISSUE_TEMPLATE
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# FINOS's tree

This project reads FINOS's files and changes none of them. `linkml/tests/upstream_tree.tsv` lists each file of the pinned commit with its git object hash, and `linkml/tests/test_upstream_tree.py` holds the tree to it byte for byte.[^test_upstream_tree.py]

`CONVENTIONS.md` states the front matter keys, the file names and the one-way link from a mitigation to its risks.[^conventions.md] `docs/_data/references/README.md` states the reference files' shape and lenses.[^references-readme.md] `templates-for-ri-md/mi-template.md` is FINOS's template for a mitigation.[^mi-template.md]

[^test_upstream_tree.py]: linkml/tests/test_upstream_tree.py, the docstring
[^conventions.md]: CONVENTIONS.md
[^references-readme.md]: docs/_data/references/README.md
[^mi-template.md]: templates-for-ri-md/mi-template.md
