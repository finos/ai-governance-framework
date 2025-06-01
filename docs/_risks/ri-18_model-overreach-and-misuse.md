---
sequence: 18
title: Model Overreach and Misuse
layout: risk
doc-status: Draft
type: OP
owasp-llm_references:
  - llm06-2025  # LLM06:2025 Excessive Agency
ffiec_references:
  - mgt-1  # MGT: I   Governance
  - mgt-2  # MGT: II Risk Management
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s1-a6   # III.S1.A6: Classification Rules for High-Risk AI Systems
  - c3-s2-a14  # III.S2.A14: Human Oversight
  - c3-s3-a26  # III.S3.A26: Obligations of Deployers of High-Risk AI Systems
---

## Summary

Model overreach occurs when AI systems are used beyond their intended purpose, often due to overconfidence in their capabilities. This can lead to poor-quality, non-compliant, or misleading outputs, especially when users apply AI to high-stakes tasks without proper validation or oversight. Overreliance and misplaced trust—such as treating AI as a human expert—can result in operational errors and regulatory breaches.#

## Description

The impressive capabilities of generative AI (GenAI) can create a false sense of reliability, leading users to overestimate what the model is capable of. This can result in staff using AI systems well beyond their intended scope or original design. For instance, a model fine-tuned to draft marketing emails might be repurposed—without validation—for high-stakes tasks such as providing legal advice or making investment recommendations.

Such misuse can lead to poor-quality, non-compliant, or even harmful outputs, especially when the AI operates in domains that require domain-specific expertise or regulatory oversight. Overreliance on AI, particularly by users who do not fully understand the model's limitations, can introduce operational errors and expose the organisation to legal or reputational risk.

A further concern is the anthropomorphising of AI systems—treating them as if they possess human judgment or authority. When users place excessive trust in AI-generated recommendations, they may accept incorrect, biased, or incomplete outputs without sufficient scrutiny. This increases the likelihood of errors, inappropriate actions, and decisions that may not align with business policy or regulatory requirements.

## Examples

* **Improper Use for Investment Advice**:
  An LLM initially deployed to assist with client communications is later used to generate investment advice. Because the model lacks formal training in financial regulation and risk analysis, it may suggest unsuitable or non-compliant investment strategies, potentially breaching financial conduct rules.

* **Inappropriate Legal Document Drafting**:
  A generative AI tool trained for internal report summarisation is misapplied to draft legally binding loan agreements or regulatory filings. This could result in missing key clauses or regulatory language, exposing the firm to legal risk or compliance violations.

* **Anthropomorphism in Client Advisory**:
  Relationship managers begin to rely heavily on AI-generated summaries or recommendations during client meetings, assuming the model's outputs are authoritative. This misplaced trust may lead to inaccurate advice being passed to clients, harming customer outcomes and increasing liability.

