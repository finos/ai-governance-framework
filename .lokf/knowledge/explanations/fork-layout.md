---
type: Explanation
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/explanations/fork-layout
genre: explanation
title: Why FINOS's tree stays at the root
description: "This repository is a fork: FINOS's tree sits unchanged at the root, and the schema project, the bundle and the website sit beside it. What keeps them apart, and why a merge from FINOS must stay a merge commit."
resource: linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
sources:
  - id: notice
    resource: linkml/NOTICE
  - id: contributing.md
    resource: linkml/CONTRIBUTING.md
    title: Before opening a pull request; Taking a new edition from FINOS
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Why FINOS's tree stays at the root

The fork holds two licences by path: the schema project under Apache-2.0, and FINOS's files under CC-BY-4.0.[^notice] A change to one of FINOS's files goes to FINOS, and a test fails on an edit here.[^contributing.md]

The checks in `lint-and-docs.yaml` read this project's files and leave FINOS's out.[^lint-and-docs.yaml]

A new edition arrives by merging FINOS's main on a branch. That branch is merged with a merge commit, because a squash loses FINOS's history and the next merge then conflicts on every file.[^contributing.md]

[^notice]: linkml/NOTICE
[^contributing.md]: linkml/CONTRIBUTING.md, Before opening a pull request; Taking a new edition from FINOS
[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header
