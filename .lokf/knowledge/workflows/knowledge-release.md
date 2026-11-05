---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge release (knowledge-release.yaml)
description: The workflow that attaches the schema's adapt copy, the bundle zip and a Copilot skill zip to a release, each with a checksum and an attestation, when the bundle or the schema has changed.
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
dependsOn:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/adapt-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Knowledge release (knowledge-release.yaml)

The workflow is a copy of the KTL template. It runs when dispatched by hand, and on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml
