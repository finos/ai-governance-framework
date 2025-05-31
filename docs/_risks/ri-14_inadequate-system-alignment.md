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
nist-sp-800-53r5_references:
  - sa-11  # SA-11 Developer Testing and Evaluation
  - ra-3   # RA-3 Risk Assessment  
  - ca-6   # CA-6 Authorization
related_risks:
  - ri-4  # Hallucination and Inaccurate Outputs
  - ri-6  # Non-Deterministic Behaviour
external_risks:
  - OWASP-LLM_2025_LLM07  # OWASP LLM: System Prompt Leakage
---

## Summary

AI alignment risk arises when a system's behaviour diverges from its intended goals, either by producing irrelevant outputs or by pursuing objectives in harmful or unintended ways. Even well-performing systems may cause issues at scale, such as reinforcing bias, exploiting loopholes, or removing human accountability. Alignment can degrade over time due to model updates, context changes, or inherent unpredictability, making continuous oversight essential.

## Description

AI systems are typically deployed with a specific goal in mind—this could be an overarching project objective or a requirement tied to individual queries. Misalignment occurs when the behaviour of the AI system does not correspond with the intended goal, either by producing irrelevant, unhelpful outputs or by pursuing the objective in ways that lead to undesirable outcomes.

In simple cases, this misalignment may resemble hallucinations, where the model fails to deliver useful responses. However, more subtle forms of misalignment can occur even when the AI appears to perform well in isolation. Over time or at scale, the system may optimise for patterns or subgoals that conflict with broader intentions or ethical expectations. For example, an AI tasked with maximising profit may suggest strategies that exploit regulatory gaps, overlook societal impact, or erode trust. Similarly, an AI used in recruitment might select high-performing candidates while systematically disadvantaging certain demographic groups due to biased training data.

There is also a risk that fully automating certain processes with AI removes human oversight and accountability. When decisions are made entirely by the system, there may be no one left with a clear understanding of how or why those decisions were made, leaving the organisation unable to respond effectively if the system misbehaves.

Even systems that are initially well-aligned can become misaligned over time due to non-deterministic behaviour, deployment of new model versions, or changes in contextual information such as system prompts or retrieval databases.

In general, there is a risk that an AI system may optimise for its goals in ways that cause unintended or harmful side effects—both in the immediate context and in broader societal or long-term settings. This highlights the importance of responsible AI development, ensuring that systems are designed and monitored to reflect human values, fairness, and safety while maintaining accountability.


## Links

  * [AWS - Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
  * [Microsoft - Responsible AI with Azure](https://azure.microsoft.com/en-us/solutions/ai/responsible-ai-with-azure)
  * [Google - Responsibility and Safety](https://deepmind.google/about/responsibility-safety/)
  * [OpenAI - A hazard analysis framework for code synthesis large language models](https://openai.com/research/a-hazard-analysis-framework-for-code-synthesis-large-language-models) 
* Research
  * [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://arxiv.org/abs/2402.18540)
  * [SoFA: Shielded On-the-fly Alignment via Priority Rule Following](https://arxiv.org/abs/2402.17358)
