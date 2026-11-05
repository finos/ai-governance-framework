---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge registrar (knowledge-registrar.yaml)
description: "The gate on the bundle: it validates the bundle and runs the conventions script on each pull request that touches `.lokf/`, and checks the provenance of a person's confirmation."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
dependsOn:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/adapt-copy
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Knowledge registrar (knowledge-registrar.yaml)

The workflow is a copy of the KTL template.[^knowledge-registrar.yaml]

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml
