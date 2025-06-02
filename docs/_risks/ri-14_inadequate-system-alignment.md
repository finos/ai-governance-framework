---
sequence: 14
title: Inadequate System Alignment
layout: risk
doc-status: Draft
type: OP
ffiec-itbooklets_references:
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
  - dam-5  # DAM: V Development
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c2-a5      # II.A5 Prohibited AI Practices
  - c3-s2-a9   # III.S2.A9: Risk Management System
  - c3-s2-a14  # III.S2.A14: Human Oversight
nist-sp-800-53r5_references:
  - sa-11  # SA-11 Developer Testing And Evaluation
  - ra-3   # RA-3 Risk Assessment
  - ca-6   # CA-6 Authorization
related_risks:
  - ri-4  # Hallucination and Inaccurate Outputs
  - ri-6  # Non-Deterministic Behaviour
owasp-llm_references:
  - llm07-2025  # LLM07:2025 System Prompt Leakage
owasp-ml_references:
  - ml08-2023  # ML08:2023 Model Skewing
---

## Summary

AI alignment risk arises when a system's behaviour diverges from its intended goals, either by producing irrelevant outputs or by pursuing objectives in harmful or unintended ways. Even well-performing systems may cause issues at scale, such as reinforcing bias, exploiting loopholes, or removing human accountability. Alignment can degrade over time due to model updates, context changes, or inherent unpredictability, making continuous oversight essential.

## Description

AI systems are typically deployed with a specific goal in mind—this could be an overarching project objective or a requirement tied to individual queries. Misalignment occurs when the behaviour of the AI system does not correspond with the intended goal, either by producing irrelevant, unhelpful outputs or by pursuing the objective in ways that lead to undesirable outcomes.

In simple cases, this misalignment may resemble hallucinations, where the model fails to deliver useful responses. However, more subtle forms of misalignment can occur even when the AI appears to perform well in isolation. Over time or at scale, the system may optimise for patterns or subgoals that conflict with broader intentions or ethical expectations. For example, an AI tasked with maximising profit may suggest strategies that exploit regulatory gaps, overlook societal impact, or erode trust. Similarly, an AI used in recruitment might select high-performing candidates while systematically disadvantaging certain demographic groups due to biased training data.

There is also a risk that fully automating certain processes with AI removes human oversight and accountability. When decisions are made entirely by the system, there may be no one left with a clear understanding of how or why those decisions were made, leaving the organisation unable to respond effectively if the system misbehaves.

Even systems that are initially well-aligned can become misaligned over time due to non-deterministic behaviour, deployment of new model versions, or changes in contextual information such as system prompts or retrieval databases.

### Financial Services Impact

The consequences of such misalignment in a financial services context can be severe:

* **Suboptimal or Harmful Business Outcomes**: An AI system designed to optimize profitability might inadvertently recommend strategies that exploit regulatory ambiguities, compromise customer best interests (e.g., by promoting unsuitable financial products), or disregard the institution's social responsibilities and long-term reputational integrity.

* **Bias and Unfair Treatment**: AI models used in critical processes like credit assessment, fraud detection, or even recruitment, if misaligned, may perpetuate or amplify existing biases. This can lead to discriminatory outcomes against certain customer demographics or applicant groups, resulting in regulatory breaches (e.g., fair lending violations) and significant reputational damage.

* **Erosion of Accountability and Oversight**: The automation of complex processes by AI systems, if not properly aligned with human oversight mechanisms, can lead to a diffusion of responsibility. If the system behaves unexpectedly or causes harm, the lack of clarity regarding human accountability can hinder remediation and erode trust.

* **Compromised Decision-Making**: Misalignment can be exacerbated by issues such as hallucinations (ri-4) where the model generates plausible but incorrect information, or by the inherent instability and non-deterministic behaviour (ri-5) of foundation models. These factors can lead to unreliable outputs that underpin critical financial decisions.

An AI system that is adequately aligned at its initial deployment may drift towards misalignment over time. This can be due to several factors, including updates to the underlying model by third-party providers, changes in the data it processes (e.g., through Retrieval Augmented Generation databases), shifts in the operational environment, or the model's own learning and adaptation if continuous learning is enabled.

Ultimately, a misaligned AI system may optimize for its programmed objectives in a manner that produces unintended, detrimental side effects for the institution, its customers, or the broader financial system. Ensuring and maintaining alignment requires a robust governance framework encompassing design, development, testing, deployment, and ongoing monitoring, guided by the principles of responsible AI to ensure safety, fairness, transparency, and accountability.


## Links

  * [AWS - Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
  * [Microsoft - Responsible AI with Azure](https://azure.microsoft.com/en-us/solutions/ai/responsible-ai-with-azure)
  * [Google - Responsibility and Safety](https://deepmind.google/about/responsibility-safety/)
  * [OpenAI - A hazard analysis framework for code synthesis large language models](https://openai.com/research/a-hazard-analysis-framework-for-code-synthesis-large-language-models) 
* Research
  * [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://arxiv.org/abs/2402.18540)
  * [SoFA: Shielded On-the-fly Alignment via Priority Rule Following](https://arxiv.org/abs/2402.17358)
