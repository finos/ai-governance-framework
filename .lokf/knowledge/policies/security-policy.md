---
type: Policy
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/policies/security-policy
title: Security policy
description: How to report a vulnerability, what this repository releases, what executes here and what holds each surface, in `.github/SECURITY.md`.
resource: .github/SECURITY.md
sources:
  - id: security.md
    resource: .github/SECURITY.md
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/policies/ai-covenant
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/main
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Security policy

Report through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

FINOS's Jekyll site and scripts sit at the root, unchanged. No workflow here builds or runs them, apart from FINOS's own `validate-references.yml` and a test that runs `scripts/validate-references.py`.[^security.md]

[^security.md]: .github/SECURITY.md
