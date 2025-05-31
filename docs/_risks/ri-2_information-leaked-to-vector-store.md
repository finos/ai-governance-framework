---
sequence: 2
title: Information Leaked to Vector Store
layout: risk
doc-status: Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM06  # OWASP LLM: Excessive Agency
  - OWASP-LLM_2025_LLM08  # OWASP LLM: Vector and Embedding Weaknesses
nist-ai-600-1_references:
  - 2-4    # NIST AI 600.1: Data Privacy
  - 2-9    # NIST AI 600.1: Information Security
ffiec_references:
  - ffiec_sec_iii-security-operations
  - ffiec_sec_iv-information-security-program-effectiveness
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10 Data and Data Governance
  - c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - c3-s3-a16  # III.S3.A16 Obligations of Providers of High-Risk AI Systems
---

## Summary

LLM applications pose data leakage risks not only through vector stores but across all components handling derived data, such as embeddings, prompt logs, and caches. These representations, while not directly human-readable, can still expose sensitive information via inversion or inference attacks, especially when security controls like access management, encryption, and auditing are lacking. To mitigate these risks, robust enterprise-grade security measures must be applied consistently across all parts of the LLM pipeline.

## Description

Vector stores are specialized databases designed to store and manage 'vector embeddings'—dense numerical representations of data such as text, images, or other complex data types. According to [OpenAI](https://platform.openai.com/docs/guides/embeddings), *"An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness."* These embeddings capture the semantic meaning of the input data, enabling advanced operations like semantic search, similarity comparisons, and clustering.

In the context of [Retrieval-Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) models, vector stores play a critical role. When a user query is received, it's converted into an embedding, and the vector store is queried to find the most semantically similar embeddings, which correspond to relevant pieces of data or documents. These retrieved data are then used to generate responses using Large Language Models (LLMs).

### Threat Description

In a typical RAG architecture which relies on a vector store to retrieve relevant organizational knowledge (e.g., from Confluence), the immaturity of current vector store technologies poses significant confidentiality and integrity risks. Vector stores, which hold embeddings of sensitive internal data, may lack enterprise-grade security controls such as robust access control mechanisms, encryption at rest, and audit logging. Misconfigurations or incomplete implementations can lead to unauthorized access to sensitive embeddings, enabling data tampering, theft, or unintentional disclosure.

While embeddings are not directly interpretable by humans, recent research has demonstrated that embeddings can reveal substantial information about the original data. For instance, embedding inversion attacks can reconstruct sensitive information from embeddings, potentially exposing proprietary or personally identifiable information (PII). The paper ["Text Embeddings Reveal (Almost) as Much as Text"](https://arxiv.org/abs/2310.06816) illustrates this very point, discussing how embeddings can be used to recover the content of the original text with high fidelity. If you are interested in learning more about how an embedding inversion attack works in practice, check-out the corresponding [GitHub repository](https://github.com/jxmorris12/vec2text) related to the above paper.

Moreover, embeddings can be subject to membership inference attacks, where an adversary determines whether a particular piece of data is included in the embedding store. This is particularly problematic in sensitive domains where the mere presence of certain information (e.g., confidential business transactions or properitary data) is sensitive. For example, if embeddings are created over a document repository for investment bankers, an adversary could generate various embeddings corresponding to speculative or confidential scenarios like *"Company A to acquire Company B."* By probing the vector store to see how many documents are similar to that embedding, they could infer whether such a transaction is being discussed internally, effectively uncovering confidential corporate activities.

As related to insufficient access control, one of the primary threats involves data poisoning, where an attacker with access to the vector store injects malicious or misleading embeddings into the system (see: [PoisonedRag](https://arxiv.org/html/2402.07867v1) for a related example). Compromised embeddings could degrade the quality or accuracy of the LLM's responses, leading to integrity issues that are difficult to detect. Since embeddings are dense numerical representations, spotting malicious alterations is not as straightforward as with traditional data.

Given the nascent nature of vector store products, they may not adhere to enterprise security standards, leaving gaps that could be exploited by malicious actors or internal users. For example:

- **Misconfigured Access Controls**: Lack of role-based access control (RBAC) or overly permissive settings may allow unauthorized internal or external users to retrieve sensitive embeddings, bypassing intended security measures.
- **Encryption Failures**: Without encryption at rest, embeddings that contain sensitive or proprietary information may be exposed to anyone with access to the storage layer, leading to data breaches or tampering.
- **Audit Deficiencies**: The absence of robust audit logging makes it difficult to detect unauthorized access, modifications, or data exfiltration, allowing breaches to go unnoticed for extended periods.

## Links

* [OpenAI – Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
* [AWS – What is Retrieval-Augmented Generation (RAG)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
* [Text Embeddings Reveal (Almost) as Much as Text – arXiv](https://arxiv.org/abs/2310.06816)
* [vec2text – GitHub Repository](https://github.com/jxmorris12/vec2text)
* [PoisonedRAG – arXiv](https://arxiv.org/html/2402.07867v1)
