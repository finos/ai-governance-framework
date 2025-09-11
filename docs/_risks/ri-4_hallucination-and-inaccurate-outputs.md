---
sequence: 4
title: Hallucination and Inaccurate Outputs
layout: risk
doc-status: Approved-Specification
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

## Example Financial Services Hallucinations

Below are a few illustrative, hypothetical cases of LLM hallucination tailored to the financial services industry.

1. **Fabricated Financial News or Analysis**
   An LLM-powered market analysis tool incorrectly reports that 'Fictional Bank Corp' has missed its quarterly earnings target based on a non-existent press release, causing a temporary dip in its stock price.

2. **Incorrect Regulatory Interpretations**
   A compliance chatbot, when asked about anti-money laundering (AML) requirements, confidently states that a specific low-risk transaction type is exempt from reporting, citing a non-existent clause in the Bank Secrecy Act.

3. **Hallucinated Customer Information**
   When a customer asks a banking chatbot for their last five transactions, the LLM hallucinates a plausible-sounding but entirely fictional transaction, such as a payment to a non-existent online merchant.

4. **False Information in Loan Adjudication**
   An AI-powered loan processing system summarizes a loan application and incorrectly states the applicant has a prior bankruptcy, a detail fabricated by the model, leading to an unfair loan denial.

5. **Generating Flawed Code for Financial Models**
   A developer asks an LLM to generate Python code for calculating Value at Risk (VaR). The model provides code that uses a non-existent function from a popular financial library, which would cause the risk calculation to fail or produce incorrect values if not caught.

## Links

* [WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia](https://arxiv.org/abs/2305.14292) - “WikiChat achieves 97.9% factual accuracy in conversations with human users about recent topics, 55.0% better than GPT-4, while receiving significantly higher user ratings and more favorable comments.”
* [Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/abs/2401.11817)
