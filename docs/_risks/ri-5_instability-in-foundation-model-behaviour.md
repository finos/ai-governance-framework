---
sequence: 5
title: Instability in Foundation Model Behaviour
layout: risk
doc-status: Draft
type: OP
owasp-llm_references:
  - llm09-2025  # OWASP LLM: Misinformation
nist-ai-600-1_references:
  - 2-8    # NIST AI 600.1: Information Integrity
ffiec_references:
  - ffiec_ots_risk-management
  - ffiec_dam_vii-maintenance
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai-act_references:
  - c3-s2-a9  # III.S2.A9 Risk Management System
  - c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

## Summary

Foundation model instability refers to unpredictable changes in model behaviour over time, even when given identical prompts. This can result from version updates, internal system prompt changes, non-deterministic generation, or unannounced modifications by the provider. Such variability can undermine testing, reliability, and trust in systems built on top of these models, particularly when no version control or change notification mechanisms are in place.

## Description

Instability in foundation model behaviour may manifest as deviations in output (i.e., during inferencing) when the same prompt is supplied. This can affect reliability, reproducibility, and downstream decision-making in systems built on top of these models.

There are several ways in which foundation model behaviour may change:

* **Version Updates**: Model providers frequently improve and update their foundation models, which may involve retraining, fine-tuning, or architecture changes. These updates, if applied without explicit notification or without allowing version pinning, can lead to shifts in behaviour even when inputs remain unchanged.

* **System Prompt Modifications**: Many models operate with a hidden or implicit *system prompt*—a predefined set of instructions that guides the model’s tone, formatting, or safety behaviour. Changes to this internal prompt (e.g., for improved safety or compliance) can alter model outputs subtly or significantly, even if user inputs remain identical.

* **Non-Determinism in Generation**: LLMs and other generative models inherently involve stochastic processes—especially when parameters like `temperature` or `top-p` sampling are non-zero. Even without external changes, this randomness can cause variability in the outputs across repeated runs.

* **Context Window Effects**: Model behaviour may vary depending on the total length and structure of input context, including position in the token window. Outputs can shift when prompts are rephrased, rearranged, or extended—even if core semantics are preserved.

* **Deployment Environment or API Changes**: Changes in model deployment infrastructure (e.g., hardware, quantization, tokenization behaviour) or API defaults can also affect behaviour, particularly for latency-sensitive or performance-critical applications.

Relying entirely on the model provider for evaluation—particularly for fast-evolving model types such as code generation—places the burden of behavioural consistency entirely on that provider. Any change introduced upstream, whether explicitly versioned or not, can impact downstream system reliability.

If the foundation model behaviour changes over time—due to lack of version pinning, absence of rigorous provider-side version control, or silent model updates—it can compromise system testing and reproducibility. This, in turn, may affect critical business operations and decisions taken on the basis of model output.

The model provider may alter the model or its configuration without explicit customer notification. Such silent changes can result in outputs that deviate from tested expectations. Even when mechanisms for version pinning are offered, the inherent non-determinism of these systems means that output variability remains a risk.

Another source of instability is **prompt perturbation**. Recent research highlights how even minor variations in phrasing can significantly impact output, and in some cases, be exploited to attack model grounding or circumvent safeguards—thereby introducing further unpredictability and risk.

## Links

* [Surprisingly Fragile: Assessing and Addressing Prompt Instability in Multimodal Foundation Models](https://www.arxiv.org/abs/2408.14595)
* [DPD error caused chatbot to swear at customer](https://www.bbc.co.uk/news/technology-68025677)
* [Prompt Perturbation in Retrieval-Augmented Generation Based Large Language Models](https://arxiv.org/abs/2402.07179)
