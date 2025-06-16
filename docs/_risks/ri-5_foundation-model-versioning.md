---
sequence: 5
title: Foundation Model Versioning
layout: risk
doc-status: Draft
type: OP
related_risks:
  - ri-7  # Availability of Foundational Model
  - ri-8  # Tampering With the Foundational Model
owasp-llm_references:
  - llm09-2025  # LLM09:2025 Misinformation
nist-ai-600-1_references:
  - 2-8  # 2.8. Information Integrity
ffiec-itbooklets_references:
  - ots-2  # OTS: Risk Management
  - dam-7  # DAM: VII Maintenance
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s2-a9   # III.S2.A9: Risk Management System
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
  - c5-s2-a53  # V.S2.A53: Obligations for Providers of General-Purpose AI Models
---

## Summary

Foundation model instability refers to unpredictable changes in model behavior over time due to external factors like version updates, system prompt modifications, or provider changes. Unlike inherent non-determinism (ri-6), this instability stems from upstream modifications that alter the model's fundamental behavior patterns. Such variability can undermine testing, reliability, and trust when no version control or change notification mechanisms are in place.

## Description

Model providers frequently improve and update their foundation models, which may involve retraining, fine-tuning, or architecture changes. These updates, if applied without explicit notification or without allowing version pinning, can lead to shifts in behaviour even when inputs remain unchanged.

* **System Prompt Modifications**: Many models operate with a hidden or implicit *system prompt*—a predefined set of instructions that guides the model's tone, formatting, or safety behaviour. Changes to this internal prompt (e.g., for improved safety or compliance) can alter model outputs subtly or significantly, even if user inputs remain identical.

* **Context Window Effects**: Model behaviour may vary depending on the total length and structure of input context, including position in the token window. Outputs can shift when prompts are rephrased, rearranged, or extended—even if core semantics are preserved.

* **Deployment Environment or API Changes**: Changes in model deployment infrastructure (e.g., hardware, quantization, tokenization behaviour) or API defaults can also affect behaviour, particularly for latency-sensitive or performance-critical applications.

### Versioning Challenges

LLM versioning is uniquely difficult due to:

* **Scale and Complexity**: Massive parameter counts make tracking changes challenging
* **Dynamic Updates**: Continuous learning and fine-tuning blur discrete version boundaries  
* **Multidimensional Changes**: Updates span architecture, training data, and inference parameters
* **Resource Constraints**: Running multiple versions simultaneously strains infrastructure
* **No Standards**: Lack of accepted versioning practices across organizations

Relying entirely on the model provider for evaluation—particularly for fast-evolving model types such as code generation—places the burden of behavioural consistency entirely on that provider. Any change introduced upstream, whether explicitly versioned or not, can impact downstream system reliability.

If the foundation model behaviour changes over time—due to lack of version pinning, absence of rigorous provider-side version control, or silent model updates—it can compromise system testing and reproducibility. This, in turn, may affect critical business operations and decisions taken on the basis of model output.

The model provider may alter the model or its configuration without explicit customer notification. Such silent changes can result in outputs that deviate from tested expectations. Even when mechanisms for version pinning are offered, the inherent non-determinism of these systems means that output variability remains a risk.

Another source of instability is **prompt perturbation**. Recent research highlights how even minor variations in phrasing can significantly impact output, and in some cases, be exploited to attack model grounding or circumvent safeguards—thereby introducing further unpredictability and risk.

### Impact of Inadequate Versioning

Poor versioning practices exacerbate instability risks and create additional operational challenges:

* **Inconsistent Output**: Models may produce different responses to identical prompts, leading to inconsistent user experiences and unreliable decision-making
* **Reproducibility Issues**: Inability to replicate or trace past outputs complicates testing, debugging, and audit requirements
* **Performance Variability**: Unexpected changes in model performance, potentially introducing regressions or new biases, while making it difficult to assess improvements
* **Compliance and Auditing**: Inability to track and explain model changes creates compliance problems and difficulties in auditing AI-driven decisions
* **Integration Challenges**: Other systems that depend on specific model behaviors may break when models are updated without proper versioning
* **Security and Privacy**: Difficulty tracking security vulnerabilities or privacy issues, with new problems potentially introduced during updates

## Links

* [Surprisingly Fragile: Assessing and Addressing Prompt Instability in Multimodal Foundation Models](https://www.arxiv.org/abs/2408.14595)
* [DPD error caused chatbot to swear at customer](https://www.bbc.co.uk/news/technology-68025677)
* [Prompt Perturbation in Retrieval-Augmented Generation Based Large Language Models](https://arxiv.org/abs/2402.07179)
