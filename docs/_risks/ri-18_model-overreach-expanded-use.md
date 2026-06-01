---
sequence: 18
title: Model Overreach / Expanded Use
layout: risk
doc-status: Approved-Specification
type: OP
owasp-llm_references:
  - llm06-2025  # LLM06:2025 Excessive Agency
ffiec-itbooklets_references:
  - mgt-1  # MGT: I   Governance
  - mgt-2  # MGT: II Risk Management
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s1-a6   # III.S1.A6: Classification Rules for High-Risk AI Systems
  - c3-s2-a14  # III.S2.A14: Human Oversight
  - c3-s3-a26  # III.S3.A26: Obligations of Deployers of High-Risk AI Systems
csa-ciro-canada_references:
  # Scope control and notification
  - csa-sn-11-348        # CSA SN 11-348: AI governance/scope expectations
  - ni-33-109-f5          # Form 33-109F5 — material business change notification
  - ni-81-102             # s. 5.1(1)(c) — AI as material strategy = fundamental change, securityholder approval
  - ni-81-106             # Part 11 material change reporting — AI scope expansion as a material change in fund operations
  # Supervision and human oversight
  - ciro-rules-phase-4    # Proposed Rules 3900/3907 — supervision of automated tasks
  - ciro-acr-2026         # CIRO 2026 Compliance Report — AI operational controls and scope
  - csa-sn-31-342         # AR must remain decision-maker — AI assists but cannot substitute
  # Outsourcing / third-party oversight
  - ni-31-103             # s. 11.1 — outsourcing obligations; registrant accountable for third-party AI scope
  - ni-31-103cp           # CP Part 11 — registerable-vs-support activity: AI may assist but not substitute
  - ciro-gn-2300-21-003   # Outsourcing Arrangements — monitoring for scope expansion by service providers
  # Tier 3 benchmarks
  - osfi-e-23-2027        # OSFI E-23 — model lifecycle monitoring catches scope drift (FRFIs, 2027)
  - osfi-b-10             # OSFI B-10 — third-party risk management and concentration (FRFIs)
related_risks:
  - ri-10  # Prompt Injection
  - ri-17  # Lack of Explainability
  - ri-22  # Regulatory Compliance and Oversight
---

## Summary

Model overreach occurs when AI systems are used beyond their intended purpose, often due to overconfidence in their capabilities. This can lead to poor-quality, non-compliant, or misleading outputs, especially when users apply AI to high-stakes tasks without proper validation or oversight. Overreliance and misplaced trust (such as treating AI as a human expert) can result in operational errors and regulatory breaches.

## Description

The impressive capabilities of generative AI (GenAI) can create a false sense of reliability, leading users to overestimate what the model is capable of. This can result in staff using AI systems well beyond their intended scope or original design. For instance, a model fine-tuned to draft marketing emails might be repurposed (without validation) for high-stakes tasks such as providing legal advice or making investment recommendations.

Such misuse can lead to poor-quality, non-compliant, or even harmful outputs, especially when the AI operates in domains that require domain-specific expertise or regulatory oversight. This perception gap creates a risk of "model overreach," where personnel may be tempted to utilize AI systems beyond their validated and intended operational scope.

A contributing factor to this risk is the tendency towards anthropomorphism — attributing human-like understanding or expertise to AI. This can foster misplaced trust, leading users to accept AI-generated outputs or recommendations too readily, without sufficient critical review or human oversight. Consequently, errors or biases in the AI's output may go undetected, potentially leading to financial losses, customer detriment, or reputational damage for the institution.

Overreliance on AI without a thorough understanding of its boundaries and potential failure points can result in critical operational mistakes and flawed decision-making. If AI systems are applied to tasks for which they are not suited or in ways that contravene regulatory requirements or ethical guidelines, significant compliance breaches can occur.

## Examples

* **Improper Use for Investment Advice**:
  An LLM initially deployed to assist with client communications is later used to generate investment advice. Because the model lacks formal training in financial regulation and risk analysis, it may suggest unsuitable or non-compliant investment strategies, potentially breaching financial conduct rules.

* **Inappropriate Legal Document Drafting**:
  A generative AI tool trained for internal report summarisation is misapplied to draft legally binding loan agreements or regulatory filings. This could result in missing key clauses or regulatory language, exposing the firm to legal risk or compliance violations.

* **Anthropomorphism in Client Advisory**:
  Relationship managers begin to rely heavily on AI-generated summaries or recommendations during client meetings, assuming the model's outputs are authoritative. This misplaced trust may lead to inaccurate advice being passed to clients, harming customer outcomes and increasing liability.

