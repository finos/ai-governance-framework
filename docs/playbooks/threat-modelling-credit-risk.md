---
layout: default
title: Worked example — threat modelling with AIGF (credit-risk assistive system)
doc-status: Draft
---

# Worked example: threat modelling with the FINOS AI Governance Framework

> **Purpose.** Answer the consumer question in [#351](https://github.com/finos/ai-governance-framework/issues/351): *show me how a firm would actually use AIGF with related FINOS artefacts*, starting from the lowest-hanging path maintainers identified — **threat modelling** — without inventing new doctrine.
>
> **Status.** Draft community documentation. This is **not** an Approved-Specification risk/mitigation file. It links existing catalogue entries.
>
> **Non-goals.** This page does not define a mandatory left-to-right operating model, does not require CALM as the only architecture language, and does not claim certification or regulatory safe harbour.

## What is already canonical

| Artefact | Role in this example |
|---|---|
| [Heuristic assessment](/heuristic-assessment.html) | Guided questions to surface GenAI risks for a use case |
| [Use case: Credit Risk Analysis](/usecase/uc-1_credit-risk-analysis/) (`uc-1`) | Draft worked use case with related risks/mitigations |
| Risk catalogue (`docs/_risks/`) | e.g. `ri-1`, `ri-4`, `ri-16`, `ri-17`, `ri-19` |
| Mitigation catalogue (`docs/_mitigations/`) | e.g. `mi-1`, `mi-4`, `mi-5`, `mi-13` |
| [CALM governance learning path](https://calm.finos.org/learn/journeys/governance) | Optional architecture-as-code journey (pluggable — firms may use other AaC) |
| CC4AI / provider attestations | Inform technical control mapping; they do **not** replace institution-owned evidence |

The July 2026 working-session notes captured on #351 still apply: the end-to-end diagram in that issue is a **target state**; adoption is tailored; threat modelling is the practical on-ramp.

## Scenario (assistive only)

Assume an **assistive** credit-risk helper aligned with `uc-1`:

- Reads application documents and internal lending policy.
- Produces a score with source-linked reasons.
- A **loan officer** decides. The system may **not** approve, decline, price, or communicate the credit decision.

If autonomy later increases to agentic decisioning, that is a **new approval cycle**, not a config tweak.

## Five steps (threat-modelling on-ramp)

### 1. Describe and version the system

Record, as governed artefacts owned by named roles:

- Business purpose and end users (`uc-1` front matter is a starting template).
- Autonomy level: **assistive**.
- Provider, model, policy, code, and data versions.
- Human-review step and permitted / forbidden actions.

This description drives which AIGF risks are in scope. It is not only a tech spec.

### 2. Assess applicable risks (catalogue, then judgement)

Start from `uc-1` related risks, then **add** what the use case implies:

| Risk ID | Title (short) | Why it appears here |
|---|---|---|
| [ri-1](/risks/ri-1_information-leaked-to-hosted-model/) | Information leaked to hosted model | Application packs may leave the firm boundary |
| [ri-4](/risks/ri-4_hallucination-and-inaccurate-outputs/) | Hallucination / inaccurate outputs | Score reasons may invent support |
| [ri-16](/risks/ri-16_bias-and-discrimination/) | Bias and discrimination | Credit context — do not treat `uc-1` mapping as exhaustive |
| [ri-17](/risks/ri-17_lack-of-explainability/) | Lack of explainability | Officer must see source-linked reasons |
| [ri-19](/risks/ri-19_data-quality-and-drift/) | Data quality and drift | Statements and bureau feeds change |

Use the [heuristic assessment](/heuristic-assessment.html) questions to challenge gaps (data, decision impact, regulatory mapping, security).

### 3. Map risks → mitigations → owners → evidence

Example thread for **inaccurate output** (`ri-4`):

| Element | Example (illustrative) |
|---|---|
| Mitigation | [mi-13](/mitigations/mi-13_providing-citations-and-source-traceability-for-ai-generated-information/) citations / source traceability; [mi-5](/mitigations/mi-5_system-acceptance-testing/) acceptance testing |
| Observability | [mi-4](/mitigations/mi-4_ai-system-observability/) |
| Owner | Model risk / credit policy (firm-defined) |
| Evidence | Versioned test set that reasons cite supporting passages; logs that the assistive boundary held |

Where CCC/CC4AI control definitions exist, they may **inform** the technical mapping. Provider attestations are inputs; they cannot prove performance on *this* lender’s population.

### 4. Attach controls to architecture (pluggable)

Represent each selected control on the component or data flow that must enforce it (entitlement service, document store, model gateway, UI that forbids “Approve”).

- [CALM](https://calm.finos.org/) is one FINOS-native option (`hub.calm.finos.org` includes AI GF controls in CALM formatting).
- Institutions may use other architecture-as-code preferences. The requirement is **traceability**, not a single vendor language.

When a component is replaced, the control attachment should make that a visible governance event.

### 5. Decide, record, re-check

Agree **before** testing what stops a trial (e.g. missing source links; evaluation not reproducible; automated credit decision observed). Accountable credit owner signs off against a specific version of description + mapping + evidence.

Reassess on events, not only calendars: model/provider/data/policy/architecture/autonomy change, or monitoring breach. Calendar review is the backstop.

## What this does *not* claim

- That following these steps equals regulatory compliance or FINOS certification.
- That CC4AI / OSCAL packs replace firm evidence.
- That one playbook fits Cyber, AppDev, MRM, and Risk equally — other stakeholder playbooks can be added later (#351 / #353 / #251).

## See also

- Issue discussion: [#351](https://github.com/finos/ai-governance-framework/issues/351)
- Related lifecycle proposal: [#353](https://github.com/finos/ai-governance-framework/issues/353)
- Adopter one-pagers: [#251](https://github.com/finos/ai-governance-framework/issues/251)
- Heuristic assessment: [heuristic-assessment](/heuristic-assessment.html)
- Use case index: [uc-index](/usecase/uc-index/)
