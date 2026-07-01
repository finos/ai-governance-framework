---
sequence: 17
title: Lack of Explainability
layout: risk
doc-status: Approved-Specification
type: OP
ffiec-itbooklets_references:
  - mgt-2  # MGT: II Risk Management
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
eu-ai-act_references:
  - c3-s2-a13  # III.S2.A13: Transparency and Provision of Information to Deployers
  - c3-s2-a14  # III.S2.A14: Human Oversight
  - c4-a50     # IV.A50 Transparency Obligations for Providers and Deployers of Certain AI Systems
  - c9-s4-a86  # IX.S4.A86: Right to Explanation of Individual Decision-Making
canada-regulations_references:
  # Reasonable-basis doctrine (functional explainability)
  - csa-sn-11-348          # CSA SN 11-348: explainability/governance expectations for AI
  - ni-31-103-s13-3        # s. 13.3 reasonable basis — must articulate why a recommendation is suitable
  - ni-31-103-s13-2-1      # s. 13.2.1 KYP — understanding the product (incl. AI-driven products)
  - ni-31-103-s14-2        # s. 14.2 relationship disclosure information — must disclose AI use to clients
  - csa-ciro-sn-31-368     # Joint CFR review — supervisory benchmark for demonstrating reasonable basis
  - csa-sn-31-342          # Online advice — AR must remain decision-maker for registerable activities
  # Supervision and oversight
  - ciro-rules-phase-4     # Proposed Rule 3900 — supervisors must understand automated tasks
  - ciro-idpc-rule-3900    # Operative Rule 3900 (supervision) — understanding processes being supervised
  # Investment funds
  - ni-81-102              # Offering document disclosure must clearly articulate how AI is used
  # Statutory explanation right
  - qc-p39-s12-1           # Quebec Law 25 s. 12.1 — only Canadian private-sector ADM explanation right
  # Tier 3 benchmarks
  - osfi-e23-2027          # OSFI E-23 — model documentation/validation (FRFIs, 2027)
  - qc-amf-ai-guideline    # AMF AI Guideline — lifecycle controls imply explainability (QC FIs, 2027)
  - iosco-fr-02-2026       # IOSCO Toolkit — disclosure / AI transparency
related_risks:
  - ri-22  # Regulatory Compliance and Oversight
  - ri-16  # Bias and Discrimination
  - ri-18  # Model Overreach / Expanded Use
iosco-supervisory-toolkit_references:
  - t2-disclosure  # Table 2: Disclosure & Transparency
  - t5-1           # Table 5.1: Disclosure of AI Use in Products and Services to End-Users
  - t6-4           # Table 6.4: Documentation of Explainability of AI Outputs
  - t3-7           # Table 3.7: Controls and Human Oversight of AI Systems
  - t4-2           # Table 4.2: Transparency Measures
---

## Summary

AI systems, particularly those using complex foundation models, often lack transparency, making it difficult to interpret how decisions are made. This limits firms’ ability to explain outcomes to regulators, stakeholders, or customers, raising trust and compliance concerns. Without explainability, errors and biases can go undetected, increasing the risk of inappropriate use, regulatory scrutiny, and undiagnosed failures.

## Description

A key challenge in deploying AI systems—particularly those based on complex foundation models—is the difficulty of interpreting and understanding how decisions are made. These models often operate as "black boxes," producing outputs without a clear, traceable rationale. This lack of transparency in decision-making can make it challenging for firms to explain or justify AI-driven outcomes to internal stakeholders, regulators, or affected customers.

The opaque nature of these models makes it hard for firms to articulate the rationale behind AI-driven decisions to stakeholders, including customers, regulators, and internal oversight bodies. This can heighten regulatory scrutiny and diminish consumer trust, as the basis for outcomes (e.g., loan approvals, investment recommendations, fraud alerts) cannot be clearly explained.

Furthermore, the inability to peer inside the model can conceal underlying errors, embedded biases, or vulnerabilities that were not apparent during initial development or testing. This opacity complicates the assessment of model soundness and reliability, a critical aspect of risk management in financial services. Without a clear understanding of how a model arrives at its conclusions, firms risk deploying AI systems that they do not fully comprehend.

This can lead to inappropriate application, undiagnosed failures in specific scenarios, or an inability to adapt the model effectively to changing market conditions or regulatory requirements. Traditional validation and testing methodologies may prove insufficient for these complex, non-linear models, making it difficult to ensure they are functioning as intended and in alignment with the institution's ethical guidelines and risk appetite.

Transparency and accountability are paramount in financial services; the lack of explainability directly undermines these principles, potentially exposing firms to operational, reputational, and compliance risks. Therefore, establishing robust governance and oversight mechanisms is essential to mitigate the risks associated with opaque AI systems.

## Links

* [Large language models don't behave like people, even though we may expect them to](https://techxplore.com/news/2024-07-large-language-dont-people.html)
