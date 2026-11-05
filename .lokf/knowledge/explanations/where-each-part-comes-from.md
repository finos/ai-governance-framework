---
type: Explanation
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/explanations/where-each-part-comes-from
genre: explanation
title: Where each part comes from
description: "Which of FINOS's files gives each part of the schema and the catalogue: the pages' front matter, `docs/_config.yml`, the reference files and the other data files."
resource: linkml/docs/about.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/catalogue
sources:
  - id: about.md
    resource: linkml/docs/about.md
    title: Where each part comes from
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Where each part comes from

Everything comes from FINOS's tree at the pinned commit.[^about.md]

- The pages' front matter gives each risk, mitigation and use case.[^about.md]
- `docs/_config.yml` gives the edition, the document statuses, the type and domain labels, the use case categories and the lens settings.[^about.md]
- `docs/_data/references/` gives the reference files.[^about.md]
- `docs/_data/` gives the other three data files, and the two nested taxonomies are written as lists of named records.[^about.md]

[^about.md]: linkml/docs/about.md, Where each part comes from
