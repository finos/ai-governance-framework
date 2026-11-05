---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
genre: reference
title: ai-governance-framework LinkML schema
description: "The LinkML model of FINOS's framework, `linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml`: `Aigf` classes for the risks, mitigations and use cases, the reference files and the other data files, at FINOS's v3."
resource: linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml
derivedFrom:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/references/finos-ai-governance-framework
sources:
  - id: ai_governance_framework.yaml
    resource: linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml
    title: the header comments
  - id: about.md
    resource: linkml/docs/about.md
    title: How the classes fit together
  - resource: linkml/src/ai_governance_framework/schema/README.md
  - resource: linkml/.linkmllint.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# ai-governance-framework LinkML schema

The schema is one file that imports only `linkml:types`. Its header carries FINOS's edition in `version` and the pinned commit in `source`.[^ai_governance_framework.yaml]

`AigfCatalogue` holds one edition. `AigfRisk`, `AigfMitigation` and `AigfUseCase` are the three kinds of page, under the abstract `AigfItem`. `AigfReferenceCitations` is a mixin of thirteen lists, one per reference file.[^about.md]

Each class keeps FINOS's keys and values. A slot that spells a key otherwise lists FINOS's key under `aliases`.[^ai_governance_framework.yaml]

[^ai_governance_framework.yaml]: linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml, the header comments
[^about.md]: linkml/docs/about.md, How the classes fit together
