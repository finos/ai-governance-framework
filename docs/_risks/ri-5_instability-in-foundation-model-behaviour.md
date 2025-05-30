---
sequence: 5
title: Instability in Foundation Model Behaviour
layout: risk
doc-status: Draft
type: OP
external_risks:
  - NIST-600_2024_2-08    # NIST 600.1: Information Integrity
  - OWASP-LLM_2025_LLM01  # OWASP LLM: Prompt Injection
  - OWASP-LLM_2025_LLM03  # OWASP LLM: Supply Chain
  - OWASP-LLM_2025_LLM09  # OWASP LLM: Misinformation
  - OWASP-ML_2023_ML01    # OWASP ML: Input Manipulation Attack
  - OWASP-ML_2023_ML08    # OWASP ML: Model Skewing
ffiec_references:
  - ffiec_ots_risk-management
  - ffiec_dam_vii-maintenance
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai_references:
  - eu-ai_c3-s2-a9  # III.S2.A9 Risk Management System
  - eu-ai_c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - eu-ai_c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

When we talk about instability in foundation model behaviour, we are referring to the tendency to produce different outputs for the same set of inputs in successive calls to the model. To a degree, this is a core quality of generative AI technology, with the degree of creativity exhibited by the model often controllable by its temperature.

This can be an issue where model outputs differ quantitatively (i.e. they draw different factual conclusions over time) and your business process depends on the output to make decisions. Unhelpful variations in model output can also be caused by adversarial users crafting malicious prompts or skewing data distributions in continuous learning models.

A significant factor contributing to behavioural instability arises from reliance on third-party model providers. If an institution depends heavily on the provider for model evaluation and validation, particularly for models that are frequently updated (such as code generation models which can change multiple times a day), it effectively transfers responsibility for the stability and suitability of that model component to the provider. This reliance becomes a risk if the provider's update and versioning practices are not transparent or robust.

Instability can manifest if the model provider alters the underlying model without explicit notification to its consumers, or if their version control is not rigorous. Even when a specific model version is "pinned" by the consuming institution, inherent non-determinism in the model's architecture can still lead to variations in output. These changes, whether intentional or emergent, can disrupt business processes that depend on consistent model behaviour, potentially leading to operational failures, incorrect decisions, or regulatory breaches if the model's responses deviate from tested and approved parameters.

Furthermore, the risk of instability is amplified by the potential for adversarial attacks. Malicious actors may use techniques like prompt perturbations – subtle alterations to input prompts – to deliberately induce erratic or unintended model behaviour. Such attacks can compromise the model's grounding in factual information or bypass safety mechanisms, leading to the generation of inaccurate, inappropriate, or harmful content, thereby weakening system defences and posing a direct threat to information integrity.

#### Links

* [Surprisingly Fragile: Assessing and Addressing Prompt Instability in Multimodal Foundation Models](https://www.arxiv.org/abs/2408.14595)
* [DPD error caused chatbot to swear at customer](https://www.bbc.co.uk/news/technology-68025677)
