---
type: Explanation
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/explanations/modelling-choices
genre: explanation
title: Modelling choices
description: "The choices behind the schema: its own classes rather than IBM AI Atlas Nexus, an identifier taken from a page's file name, a category FINOS's config does not list, and an SSSOM row that is a citation."
resource: linkml/docs/about.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
sources:
  - id: about.md
    resource: linkml/docs/about.md
    title: Choices worth knowing
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Modelling choices

An earlier schema of this fork imported a patched copy of IBM's AI Atlas Nexus and held FINOS's v2 as data under it. FINOS's v3 changed the identifiers and added the lenses, so the schema now declares its own classes, and Nexus is a mapping target.[^about.md]

FINOS's front matter holds `sequence` and no identifier, so the catalogue adds `item_id` from the file's name.[^about.md]

The category enum holds `Risk_and_Compliance`, which uc-3 and uc-4 write, and its description says that `docs/_config.yml` does not list it.[^about.md]

[^about.md]: linkml/docs/about.md, Choices worth knowing
