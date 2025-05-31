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

#### Alignment

There is a specific goal you want to achieve when using an AI system in a successful way. It may be an overarching project goal, or a specific requirement for single queries to the AI system. 

This risk describes when the AI system behaves in a way that doesn't align with the intended goal.


#### What can go wrong

In the more basic instance, it already has been described when we talked about [hallucinations](#TR-14) that the model may not be giving useful output to queries. But even when the model does seem to be performing well in the short term for individual queries, it may be putting the emphasis on a specific topic that, when using the AI model on scale, will in turn have undesirable consequences.

For example, an AI with a goal to maximize a company's profit could suggest exploiting regulatory loopholes or ignoring the social responsibility for the impact of implementing its solutions on population. In another example, an AI tasked with selecting candidates for jobs positions may be choosing people that perform quite well in the roles, but may be biased against specific kind of population in an unfair way. You could even think that making some processes completely AI automated could pose a risk, for removing completely responsibility about something from humans may end up making nobody knowing anything at all about the automated task, having no accountability or responsibility when it misbehaves.

Also an AI system that is aligned at first may become misaligned in future situations given its [non-deterministic behavior](#TR-6), when [new versions of the model](#TR-11) are deployed, or it uses different contextual information (system prompt, RAG database, etc).

In general we can summarize that the **AI system may optimize for a goal in a way that causes unintended or harmful side effects**, not only for its immediate goals, but for society in general and the long term.

#### Responsible AI

The concept of **responsible AI** defines the practice of developing and deploying AI systems in a way that we make sure they are aligned with human values, ensure safety, fairness, and accountability while minimizing risks and unintended consequences.

#### Links


* AI vendor providers
  * [AWS - Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
  * [Microsoft - Responsible AI with Azure](https://azure.microsoft.com/en-us/solutions/ai/responsible-ai-with-azure)
  * [Google - Responsibility and Safety](https://deepmind.google/about/responsibility-safety/)
  * [OpenAI - A hazard analysis framework for code synthesis large language models](https://openai.com/research/a-hazard-analysis-framework-for-code-synthesis-large-language-models) 
* Research
  * [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://arxiv.org/abs/2402.18540)
  * [SoFA: Shielded On-the-fly Alignment via Priority Rule Following](https://arxiv.org/abs/2402.17358)
