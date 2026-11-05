---
type: GlossaryTerm
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/reference-file
title: Reference file
description: "A reference file: a YAML file under `docs/_data/references/` that lists the citable entries of one regulation, framework or standard, each under a stable key a page cites it by."
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/lens
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/citation
sources:
  - id: references-readme.md
    resource: docs/_data/references/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Reference file

A reference file holds a title, a description, a lens, an optional source address and its entries. Each entry has a title and an address, under its key.[^references-readme.md]

When a framework publishes a new edition, the old keys stay, each marked `superseded_by` its successor.[^references-readme.md]

[^references-readme.md]: docs/_data/references/README.md
