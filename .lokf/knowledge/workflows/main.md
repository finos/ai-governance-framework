---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The test workflow on each pull request and on `main`: on five Python versions in `linkml/`, it runs `just test`, and on one it runs the lint and the adapt check."
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Build and test (main.yaml)

The job installs from `linkml/uv.lock` with `uv sync --locked`, and runs `just lint` and `just lokf-adapt-check` on Python 3.13 alone.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml
