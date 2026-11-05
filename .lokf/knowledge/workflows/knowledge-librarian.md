---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge librarian (knowledge-librarian.yaml)
description: The sidecar's scheduled agent run that keeps the bundle in step with its sources and opens a pull request. It stays inert until the repository variable `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/playbooks/knowledge-sources
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Knowledge librarian (knowledge-librarian.yaml)

The workflow is a copy of the KTL template, with the skills pin at v0.61.0.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml
