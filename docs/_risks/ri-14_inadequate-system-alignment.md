---
sequence: 14
title: Inadequate System Alignment
layout: risk
doc-status: Draft
type: OP
ffiec_references:
  - ffiec_dam_iii-risk-management-of-development-acquisition-and-maintenance
  - ffiec_dam_v-development
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai_references:
  - eu-ai_c2-a5  # II.A5 Prohibited AI Practices
  - eu-ai_c3-s2-a9  # III.S2.A9 Risk Management System
  - eu-ai_c3-s2-a14  # III.S2.A14 Human Oversight
related_risks:
  - ri-4  # Hallucination and Inaccurate Outputs
  - ri-6  # Non-Deterministic Behaviour
external_risks:
  - OWASP-LLM_2025_LLM07  # OWASP LLM: System Prompt Leakage
  - OWASP-ML_2023_ML01 # OWASP ML Input Manipulation
  - OWASP-ML_2023_ML02 # Data Poisoning Attack
  - OWASP-ML_2023_ML08 # Model Skewing
  - OWASP-ML_2023_ML10 # Model Poisoning
---

Inadequate system alignment occurs when an AI system's behaviour deviates from the intended goals, operational requirements, ethical guidelines, or regulatory obligations defined by the institution. This misalignment can arise even if the system appears to perform adequately on individual queries or tasks in the short term.

The consequences of such misalignment in a financial services context can be severe. For instance:

  * Suboptimal or Harmful Business Outcomes: An AI system designed to optimize profitability might inadvertently recommend strategies that exploit regulatory ambiguities, compromise customer best interests (e.g., by promoting unsuitable financial products), or disregard the institution's social responsibilities and long-term reputational integrity.
  * Bias and Unfair Treatment: AI models used in critical processes like credit assessment, fraud detection, or even recruitment, if misaligned, may perpetuate or amplify existing biases. This can lead to discriminatory outcomes against certain customer demographics or applicant groups, resulting in regulatory breaches (e.g., fair lending violations) and significant reputational damage.
  * Erosion of Accountability and Oversight: The automation of complex processes by AI systems, if not properly aligned with human oversight mechanisms, can lead to a diffusion of responsibility. If the system behaves unexpectedly or causes harm, the lack of clarity regarding human accountability can hinder remediation and erode trust.
  * Compromised Decision-Making: Misalignment can be exacerbated by issues such as hallucinations (ri-4) where the model generates plausible but incorrect information, or by the inherent instability and non-deterministic behaviour (ri-5) of foundation models. These factors can lead to unreliable outputs that underpin critical financial decisions.
  * An AI system that is adequately aligned at its initial deployment may drift towards misalignment over time. This can be due to several factors, including updates to the underlying model by third-party providers (see ri-11: Third-Party Model Versioning), changes in the data it processes (e.g., through Retrieval Augmented Generation databases), shifts in the operational environment, or the model's own learning and adaptation if continuous learning is enabled.

Ultimately, a misaligned AI system may optimize for its programmed objectives in a manner that produces unintended, detrimental side effects for the institution, its customers, or the broader financial system. Ensuring and maintaining alignment requires a robust governance framework encompassing design, development, testing, deployment, and ongoing monitoring, guided by the principles of responsible AI to ensure safety, fairness, transparency, and accountability.

#### Links


* AI vendor providers
  * [AWS - Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
  * [Microsoft - Responsible AI with Azure](https://azure.microsoft.com/en-us/solutions/ai/responsible-ai-with-azure)
  * [Google - Responsibility and Safety](https://deepmind.google/about/responsibility-safety/)
  * [OpenAI - A hazard analysis framework for code synthesis large language models](https://openai.com/research/a-hazard-analysis-framework-for-code-synthesis-large-language-models) 
* Research
  * [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://arxiv.org/abs/2402.18540)
  * [SoFA: Shielded On-the-fly Alignment via Priority Rule Following](https://arxiv.org/abs/2402.17358)
