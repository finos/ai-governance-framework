---
sequence: 19
title: Data Quality and Drift
layout: risk
doc-status: Draft
type: OP
nist-ai-600-1_references:
  - 2-8    # NIST AI 600.1: Information Integrity
ffiec_references:
  - ffiec_dam_iii-risk-management-of-development-acquisition-and-maintenance
  - ffiec_dam_vii-maintenance
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10 Data and Data Governance
  - c3-s2-a9  # III.S2.A9 Risk Management System
  - c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
---

## Summary

Generative AI systems rely heavily on the quality and freshness of their training data, and outdated or poor-quality data can lead to inaccurate, biased, or irrelevant outputs. In fast-moving sectors like financial services, stale models may miss market changes or regulatory updates, resulting in flawed risk assessments or compliance failures. Ongoing data integrity and retraining efforts are essential to ensure models remain accurate, relevant, and aligned with current conditions.

## Description

The effectiveness of generative AI models is highly dependent on the quality, completeness, and recency of the data used during training or fine-tuning. If the underlying data is inaccurate, outdated, or biased, the model’s outputs are likely to reflect and potentially amplify these issues. Poor-quality data can lead to unreliable, misleading, or irrelevant responses, especially when the AI is used in decision-making, client interactions, or risk analysis.

Over time, models trained on static datasets can become stale—failing to reflect new developments in market dynamics, regulations, or customer behaviour. Without mechanisms for periodic retraining or updates, these models are prone to data drift, where the input data they encounter in production no longer resembles the data used to train them. This is particularly problematic in financial services, where fast-paced environments demand up-to-date information to ensure accurate forecasting, risk assessment, and compliance monitoring.

For instance, a generative AI system trained prior to recent regulatory changes might suggest outdated documentation practices or miss new compliance requirements. Similarly, an AI model used in credit scoring could provide flawed recommendations if it relies on obsolete economic indicators or no longer-representative borrower behaviour patterns.

In addition, errors or embedded biases in historical training data can propagate into the model and be magnified at scale, especially in generative systems that synthesise or infer new content from noisy inputs. This not only undermines performance and trust, but can also introduce legal and reputational risks if decisions are made based on inaccurate or biased outputs.

Maintaining data integrity, accuracy, and relevance is therefore an ongoing operational challenge. It requires continuous monitoring, data validation processes, and governance to ensure that models remain aligned with current realities and organisational objectives.
