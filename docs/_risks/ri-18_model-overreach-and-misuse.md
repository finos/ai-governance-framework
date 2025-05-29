---
sequence: 18
title: Model Overreach and Misuse
layout: risk
doc-status: Pre-Draft
type: OP
external_risks:
  - OWASP-LLM_2025_LLM06  # OWASP LLM: Excessive Agency
ffiec_references:
  - ffiec_mgt_i-governance
  - ffiec_mgt_ii-risk-management
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai_references:
  - eu-ai_c3-s1-a6  # III.S1.A6 Classification Rules for High-Risk AI Systems
  - eu-ai_c3-s2-a14  # III.S2.A14 Human Oversight
  - eu-ai_c3-s3-a26  # III.S3.A26 Obligations of Deployers of High-Risk AI Systems
---

-he advanced capabilities demonstrated by Generative AI (GenAI) can inadvertently lead to an overestimation of its actual abilities and an underappreciation of its inherent limitations. This perception gap creates a risk of "model overreach," where personnel may be tempted to utilize AI systems beyond their validated and intended operational scope.

For instance, an AI model specifically trained and tested for a relatively low-risk task, such as drafting marketing emails, might be inappropriately repurposed by staff for significantly higher-risk applications, such as generating investment advice, preparing legal documents, or making credit decisions. Such misuse can lead to the generation of poor-quality, inaccurate, or non-compliant outcomes, as the model lacks the specific training, knowledge, and safeguards required for these more sensitive functions.

Overreliance on AI without a thorough understanding of its boundaries and potential failure points can result in critical operational mistakes and flawed decision-making. If AI systems are applied to tasks for which they are not suited or in ways that contravene regulatory requirements or ethical guidelines, significant compliance breaches can occur.

A contributing factor to this risk is the tendency towards anthropomorphism—attributing human-like understanding or expertise to AI. This can foster misplaced trust, leading users to accept AI-generated outputs or recommendations too readily, without sufficient critical review or human oversight. Consequently, errors or biases in the AI's output may go undetected, potentially leading to financial losses, customer detriment, or reputational damage for the institution.
