---
layout: risk
doc-status: Draft
sequence: 5
type: OP
title: Instability in foundation model behaviour
external_risks:
  - LLM09
---

Instability in foundation model behaviour would manifest itself as deviations in the output (i.e during inferencing), when supplied with the same prompt.

If you completely rely on the model provider for its evaluation, for example because it’s of a kind that changes very quickly, like a code generation model (that can change several times a day), you have to acknowledge that you are putting all the responsibility on the outcome of the architecture on that provider, and you trust what it does whenever the model version is changed.

If you need to implement strict tests on your whole architecture, the foundation model behaviour may change over time if the third-party doesn't have rigorous version control (covered in Threat 11), you don’t pin the version you are using, or they silently change model versions without notifying the consumer. This can lead to instability in the model's behaviour, which may impact on the client's business operations and actions taken upon model output.

The provider may change the model without explicit customer knowledge. This could lead to unexpected response from the model that it has not been tested for by the corporation.
The provider might also provide a mechanism to pin the model version. In both cases non-determinism can lead to instability in model behaviour.

Another mechanism to induce instability is around perturbations. There is recent research into using prompt perturbations to attack grounding and hence weaken system defences against malicious attacks.

#### Links

* [Surprisingly Fragile: Assessing and Addressing Prompt Instability in Multimodal Foundation Models](https://www.arxiv.org/abs/2408.14595)
* [DPD error caused chatbot to swear at customer](https://www.bbc.co.uk/news/technology-68025677)
