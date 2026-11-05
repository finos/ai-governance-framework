---
type: Playbook
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/playbooks/rebuild-the-catalogue
genre: how-to
title: Rebuild the catalogue and the SSSOM sets
description: How to rewrite the catalogue and the SSSOM sets from FINOS's files, with `just build-catalogue` and `just build-mappings`, and how to check them with `just check-catalogue` and `just check-mappings`.
resource: linkml/project.justfile
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/catalogue
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/sssom-sets
sources:
  - id: project.justfile
    resource: linkml/project.justfile
    title: the catalogue and the SSSOM sets
  - id: build_catalogue.py
    resource: linkml/scripts/build_catalogue.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Rebuild the catalogue and the SSSOM sets

From `linkml/`, run `just build-catalogue` and then `just build-mappings`.[^project.justfile] Run `just check-catalogue` and `just check-mappings` to fail on a difference.[^project.justfile]

Neither builder takes input of its own: each reads FINOS's files and the schema, so a difference means one of those changed.[^build_catalogue.py]

[^project.justfile]: linkml/project.justfile, the catalogue and the SSSOM sets
[^build_catalogue.py]: linkml/scripts/build_catalogue.py, the docstring
