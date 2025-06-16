---
sequence: 6
title: Non-Deterministic Behaviour
layout: risk
doc-status: Draft
type: OP
owasp-llm_references:
  - llm09-2025  # LLM09:2025 Misinformation
ffiec-itbooklets_references:
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s2-a9   # III.S2.A9: Risk Management System
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
  - c3-s2-a14  # III.S2.A14: Human Oversight
related_risks:
  - ri-4   # Hallucination and Inaccurate Outputs
  - ri-14  # Inadequate System Alignment
---

## Summary

LLMs exhibit non-deterministic behaviour, meaning they can generate different outputs for the same input due to probabilistic sampling and internal variability. This unpredictability can lead to inconsistent user experiences, undermine trust, and complicate testing, debugging, and performance evaluation. Inconsistent results may appear as varying answers to identical queries or fluctuating system performance across runs, posing significant challenges for reliable deployment and quality assurance.

## Description

LLMs may produce different outputs for identical inputs. This occurs because **models predict probability distributions over possible next tokens** and sample from these distributions at each step. Parameters like `temperature` (randomness level) and `top-p` sampling (nucleus sampling) may amplify this variability, even without external changes to the model itself.

Key sources of non-determinism include:

* **Probabilistic Sampling**: Models don't always choose the highest-probability token, introducing controlled randomness for more natural, varied outputs
* **Internal States**: Random seeds, GPU computation variations, or floating-point precision differences can affect results
* **Context Effects**: Model behavior varies based on prompt position within the token window or slight rephrasing
* **Temperature Settings**: Higher temperatures increase randomness; lower temperatures increase consistency but may reduce creativity

This unpredictability can undermine trust and complicate business processes that depend on consistent model behavior. Financial institutions may see varying risk assessments, inconsistent customer responses, or unreliable compliance checks from identical inputs.


## Examples of Non-Deterministic Behaviour

* **Customer Support Assistant**: A virtual assistant gives one user a definitive answer to a billing query and another user an ambiguous or conflicting response. The discrepancy leads to confusion and escalated support requests.

* **Code Generation Tool**: An LLM is used to generate Python scripts from natural language descriptions. On one attempt, the model writes clean, functional code; on another, it introduces subtle logic errors or omits key lines, despite identical prompts.

* **Knowledge Search System**: In a RAG pipeline, a user asks a compliance-related question. Depending on which documents are retrieved or how they’re synthesized into the prompt, the LLM may reference different regulations or misinterpret the intent.

* **Documentation Summarizer**: A tool designed to summarize technical documents produces varying summaries of the same document across multiple runs, shifting tone or omitting critical sections inconsistently.


## Testing and Evaluation Challenges

Non-determinism significantly complicates the testing, debugging, and evaluation of LLM-integrated systems. Reproducing prior model behaviour is often impossible without deterministic decoding and tightly controlled inputs. Bugs that surface intermittently due to randomness may evade diagnosis, or appear and disappear unpredictably across deployments. This makes regression testing unreliable, especially in continuous integration (CI) environments that assume consistency between test runs.

Quantitative evaluation is similarly affected: metrics such as accuracy, relevance, or coherence may vary across runs, obscuring whether changes in performance are due to real system modifications or natural model variability. This also limits confidence in A/B testing, user feedback loops, or fine-tuning efforts, as behavioural changes can’t be confidently attributed to specific inputs or parameters.

## Links

 - [The Non-determinism of ChatGPT in Code Generation](https://arxiv.org/abs/2308.02828)
