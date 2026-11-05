---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: The workflow that builds `website/` on each pull request that touches its inputs and weekly, and deploys to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/services/documentation-site
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Knowledge website (knowledge-website.yaml)

The workflow is a copy of the KTL template. Its path filter names the root `README.md` and `docs/`, which are FINOS's, and `linkml/README.md` is not among them, so a change there reaches the site on the weekly rebuild or a manual run.[^knowledge-website.yaml]

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml
