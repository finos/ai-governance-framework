---
sequence: 4
title: Hallucination and Inaccurate Outputs
layout: risk
doc-status: Draft
type: OP
owasp-llm_references:
  - llm09-2025  # LLM09:2025 Misinformation
owasp-ml_references:
  - ml09-2023  # ML09:2023 Output Integrity Attack
nist-ai-600-1_references:
  - 2-2  # 2.2. Confabulation
  - 2-8  # 2.8. Information Integrity
ffiec-itbooklets_references:
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
  - mgt-2  # MGT: II Risk Management
eu-ai-act_references:
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
  - c3-s2-a13  # III.S2.A13: Transparency and Provision of Information to Deployers
  - c3-s2-a9   # III.S2.A9: Risk Management System
related_risks:
  - ri-14  # Inadequate System Alignment
  - ri-6   # Non-Deterministic Behaviour
  - ri-19  # Data Quality and Drift
---

## Summary

LLM hallucinations occur when a model generates confident but incorrect or fabricated information due to its reliance on statistical patterns rather than factual understanding. Techniques like Retrieval-Augmented Generation can reduce hallucinations by providing factual context, but they cannot fully prevent the model from introducing errors or mixing in inaccurate internal knowledge. As there is no guaranteed way to constrain outputs to verified facts, hallucinations remain a persistent and unresolved challenge in LLM applications.

## Description

LLM hallucinations refer to instances when a Large Language Model (LLM) generates incorrect or nonsensical information that seems plausible but is not based on factual data or reality. These "hallucinations" occur because the model generates text based on patterns in its training data rather than true understanding or access to current, verified information.

The likelihood of hallucination can be minimised by techniques such as Retrieval Augmented Generation (RAG), providing the LLM with facts directly via the prompt. However, the response provided by the model is a synthesis of the information within the input prompt and information retained within the model. There is no reliable way to ensure the response is restricted to the facts provided via the prompt, and as such, RAG-based applications still hallucinate.

There is currently no reliable method for removing hallucinations, with this being an active area of research.

## Contributing Factors

Several factors increase the risk of hallucination:

 - **Lack of Ground Truth:** The model cannot distinguish between accurate and inaccurate data in its training corpus.
 - **Ambiguous or Incomplete Prompts:** When input prompts lack clarity or precision, the model is more likely to fabricate plausible-sounding but incorrect details.
 - **Confidence Mismatch:** LLMs often present hallucinated information with high fluency and syntactic confidence, making it difficult for users to recognize inaccuracies.
 - **Fine-Tuning or Prompt Bias:** Instructions or training intended to improve helpfulness or creativity can inadvertently increase the tendency to generate unsupported statements.

## Example hallucinations

Below are a few illustrative cases of LLM hallucination.

1. **Cited Sources That Don't Exist**
   An LLM asked to summarize academic work may invent references, complete with plausible authors, titles, and journal names, that are entirely fictional.

2. **Fabricated Legal or Medical Advice**
   When prompted for legal precedents or medical diagnoses, LLMs may provide entirely fabricated cases or treatments that sound convincing but have no basis in reality.

3. **Incorrect Product or API Descriptions**
   Given prompts about software tools or APIs, the model may hallucinate methods, parameters, or features that are not part of the actual documentation.

4. **False Historical or Scientific Claims**
   LLMs have been known to invent historical facts (e.g., attributing events to the wrong year or country) or scientific findings (e.g., claiming a drug is approved for a condition it is not).

5. **Contradictory Reasoning**
   In some cases, LLMs produce internally inconsistent outputs—for example, simultaneously asserting and denying the same fact in the same answer, or offering logically incompatible reasoning steps.

## Links

* [WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia](https://arxiv.org/abs/2305.14292) - “WikiChat achieves 97.9% factual accuracy in conversations with human users about recent topics, 55.0% better than GPT-4, while receiving significantly higher user ratings and more favorable comments.”
* [Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/abs/2401.11817)
