---
type: GlossaryTerm
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/adapt-copy
title: Adapt copy
description: "An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`."
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/adapt-copy
sources:
  - id: project.justfile
    resource: linkml/project.justfile
    title: the comment above the recipes
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Adapt copy

`lokf adapt` copies a schema so that a bundle can use its classes as concept types. It re-roots the classes named with `--root` on LOKF's `Concept`.[^project.justfile]

[^project.justfile]: linkml/project.justfile, the comment above the recipes
