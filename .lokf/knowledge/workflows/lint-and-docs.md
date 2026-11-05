---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/lint-and-docs
genre: reference
title: Lint and docs (lint-and-docs.yaml)
description: "The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, word budgets, markdownlint, lychee and codespell, over this project's files and never FINOS's."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/explanations/fork-layout
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Lint and docs (lint-and-docs.yaml)

The shell check ignores FINOS's folders, and the Markdown, link and spelling checks name this project's paths.[^lint-and-docs.yaml] The word budgets hold `linkml/CONTRIBUTING.md` to 1000 words and `.github/SECURITY.md` to 900.[^lint-and-docs.yaml]

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml
