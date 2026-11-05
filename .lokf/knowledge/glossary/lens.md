---
type: GlossaryTerm
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/lens
title: Lens
description: "A lens: what a reference file tells a reader about a risk or mitigation, one of `threat`, `obligation` or `control`, each answering one question, set by `lens` in the file and configured in `docs/_config.yml`."
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/reference-file
sources:
  - id: references-readme.md
    resource: docs/_data/references/README.md
    title: Lens
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Lens

Each reference file has one lens, which says which question the standard answers for a page.[^references-readme.md]

| Lens | Question |
| --- | --- |
| `threat` | What is this called elsewhere? |
| `obligation` | Which rule requires me to address it? |
| `control` | How do I implement and evidence it? |

[^references-readme.md]: docs/_data/references/README.md, Lens
