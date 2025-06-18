---
sequence: 19
title: Data Quality and Drift
layout: risk
doc-status: Approved-Specification
type: OP
nist-ai-600-1_references:
  - 2-8  # 2.8. Information Integrity
ffiec-itbooklets_references:
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
  - dam-7  # DAM: VII Maintenance
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10: Data and Data Governance
  - c3-s2-a9   # III.S2.A9: Risk Management System
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
related_risks:
  - ri-4   # Hallucination and Inaccurate Outputs
  - ri-16  # Bias and Discrimination
  - ri-9   # Data Poisoning
---

## Summary

Generative AI systems rely heavily on the quality and freshness of their training data, and outdated or poor-quality data can lead to inaccurate, biased, or irrelevant outputs. In fast-moving sectors like financial services, stale models may miss market changes or regulatory updates, resulting in flawed risk assessments or compliance failures. Ongoing data integrity and retraining efforts are essential to ensure models remain accurate, relevant, and aligned with current conditions.

## Description

The effectiveness of generative AI models is highly dependent on the quality, completeness, and recency of the data used during training or fine-tuning. If the underlying data is inaccurate, outdated, or biased, the model’s outputs are likely to reflect and potentially amplify these issues. Poor-quality data can lead to unreliable, misleading, or irrelevant responses, especially when the AI is used in decision-making, client interactions, or risk analysis.

AI models can become "stale" if not regularly updated with current information. This "data drift" or "concept drift" occurs when statistical properties of input data change over time, causing predictive power to decline. In fast-moving financial markets, reliance on stale models can lead to flawed risk assessments, suboptimal investment decisions, and critical compliance failures when models fail to recognize emerging market shifts, new regulatory requirements, or evolving customer behaviors.

For instance, a generative AI system trained prior to recent regulatory changes might suggest outdated documentation practices or miss new compliance requirements. Similarly, an AI model used in credit scoring could provide flawed recommendations if it relies on obsolete economic indicators or no longer-representative borrower behaviour patterns.

In addition, errors or embedded biases in historical training data can propagate into the model and be magnified at scale, especially in generative systems that synthesise or infer new content from noisy inputs. This not only undermines performance and trust, but can also introduce legal and reputational risks if decisions are made based on inaccurate or biased outputs.

Maintaining data integrity, accuracy, and relevance is therefore an ongoing operational challenge. It requires continuous monitoring, data validation processes, and governance to ensure that models remain aligned with current realities and organisational objectives.
