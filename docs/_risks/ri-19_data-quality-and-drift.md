---
sequence: 19
title: Data Quality and Drift
layout: risk
doc-status: Pre-Draft
type: OP
external_risks:
  - NIST-600_2024_2-08  # NIST 600.1: Information Integrity
  - OWASP-LLM_2025_LLM04  # OWASP LLM: Data and Model Poisoning
  - OWASP-LLM_2025_LLM08  # OWASP LLM: Vector and Embedding Weaknesses
  - OWASP-ML_2023_ML02 # OWASP ML Data Poisoning Attack
  - OWASP-ML_2023_ML08 # OWASP ML Model Skewing
  
ffiec_references:
  - ffiec_dam_iii-risk-management-of-development-acquisition-and-maintenance
  - ffiec_dam_vii-maintenance
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai_references:
  - eu-ai_c3-s2-a10  # III.S2.A10 Data and Data Governance
  - eu-ai_c3-s2-a9  # III.S2.A9 Risk Management System
  - eu-ai_c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
---

The reliability and accuracy of Generative AI outputs are fundamentally dependent on the quality, relevance, and recency of the data upon which they are trained and operate. The use of poor-quality, biased, incomplete, or outdated data can significantly degrade model performance, leading to unreliable, irrelevant, or potentially harmful results.

AI models, particularly those operating in dynamic environments like financial markets, can become "stale" if not regularly updated or retrained with current information. This "data drift" or "concept drift" occurs when the statistical properties of the input data change over time, causing the model's predictive power to decline. A lack of updated training data may result in the AI failing to recognize emerging market shifts, new regulatory requirements, or evolving customer behaviours. In the context of fast-moving financial markets, reliance on stale models can lead to flawed risk assessments, suboptimal investment decisions, and critical compliance failures.

Furthermore, errors, inaccuracies, or inherent biases present in the training data can be learned, reflected, and in some cases, amplified by AI systems. If data used for training or fine-tuning contains skewed representations or historical prejudices, the AI model is likely to perpetuate these issues in its outputs, potentially leading to discriminatory outcomes or unfair treatment.

Maintaining data integrity, ensuring data quality, and managing data drift are continuous and significant operational challenges for financial institutions deploying AI. This requires robust data governance practices, ongoing monitoring of data pipelines, and mechanisms for regular model retraining and validation to ensure sustained accuracy and relevance.
