---
type: Playbook
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test the schema
description: "How to change the schema: edit it, run `just gen-project`, `just gen-doc`, the two builders and `just lokf-adapt` from `linkml/`, then `just lint` and `just test`, and commit the output."
resource: linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
sources:
  - id: contributing.md
    resource: linkml/CONTRIBUTING.md
    title: Before opening a pull request
  - id: main.yaml
    resource: .github/workflows/main.yaml
  - resource: linkml/justfile
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Regenerate and test the schema

1. Edit `linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml`.
2. From `linkml/`, run `just gen-project`, `just gen-doc`, `just build-catalogue`, `just build-mappings` and `just lokf-adapt`, and commit the output.[^contributing.md]
3. Run `just test` from `linkml/`.[^contributing.md]

`just lint` runs `linkml-lint` under `linkml/.linkmllint.yaml`. `.github/workflows/main.yaml` runs the lint, the tests and the adapt check.[^main.yaml]

[^contributing.md]: linkml/CONTRIBUTING.md, Before opening a pull request
[^main.yaml]: .github/workflows/main.yaml
