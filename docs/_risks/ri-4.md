---
layout: risk
doc-status: Draft
sequence: 4
type: OP
title: Hallucination and Inaccurate Outputs
external_risks:
  - LLM08
  - LLM09
---

LLM hallucinations refer to instances when a large language model (LLM) generates incorrect or nonsensical information that seems plausible but is not based on factual data or reality. These "hallucinations" occur because the model generates text based on patterns in its training data rather than true understanding or access to current, verified information.

The likelihood of hallucination can be minimised by using Retrieval Augmented Generation (RAG) techniques, providing the LLM with facts directly via the prompt. However, the response provided by the model is a synthesis of the information within the input prompt and information retained within the model. There is no reliable way to ensure the response is restricted to the facts provided via the prompt, and as such, RAG-based applications still hallucinate.

There is currently no reliable method for removing hallucinations, with this being an active area of research.

#### Links

* [WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia](https://arxiv.org/abs/2305.14292) - “WikiChat achieves 97.9% factual accuracy in conversations with human users about recent topics, 55.0% better than GPT-4, while receiving significantly higher user ratings and more favorable comments.”
* [Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/abs/2401.11817)
