---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the projections in `linkml/project/`, the Python models in `linkml/src/ai_governance_framework/datamodel/` and the schema's copy in `linkml/docs/schema/`."
resource: linkml/project
derivedFrom:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
sources:
  - id: contributing.md
    resource: linkml/CONTRIBUTING.md
    title: What this project is
  - id: config.public.mk
    resource: linkml/config.public.mk
  - resource: linkml/.linkml/generators.yaml
  - resource: linkml/src/ai_governance_framework/datamodel
  - resource: linkml/docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Generated artefacts

The recipes write these files, and they are never edited by hand.[^contributing.md] `linkml/.linkml/generators.yaml` holds the generators' settings.[^config.public.mk]

[^contributing.md]: linkml/CONTRIBUTING.md, What this project is
[^config.public.mk]: linkml/config.public.mk
