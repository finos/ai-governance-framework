---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow builds. It shows `linkml/README.md`, `linkml/docs/`, the changelog, the schema's pages and the bundle, and leaves FINOS's own site alone.
resource: website
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
  - resource: website/README.md
  - resource: website/NOTICE
dependsOn:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Documentation site

`website/site.config.mjs` names what the site shows. The home page is `linkml/README.md`, the docs are `linkml/docs/`, and the changelog is `linkml/CHANGELOG.md`.[^site.config.mjs]

The site's schema pages come from `just --justfile linkml/justfile gen-doc`.[^site.config.mjs] FINOS's Jekyll `docs/` stays out.[^site.config.mjs]

[^site.config.mjs]: website/site.config.mjs
