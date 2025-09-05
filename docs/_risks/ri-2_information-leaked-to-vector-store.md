---
sequence: 2
title: Information Leaked to Vector Store
layout: risk
doc-status: Approved-Specification
type: SEC
owasp-llm_references:
  - llm02-2025  # LLM02:2025 Sensitive Information Disclosure
  - llm08-2025  # LLM08:2025 Vector and Embedding Weaknesses
nist-ai-600-1_references:
  - 2-4  # 2.4. Data Privacy
  - 2-9  # 2.9. Information Security
ffiec-itbooklets_references:
  - sec-3  # SEC: III Security Operations
  - sec-4  # SEC: IV Information Security Program Effectiveness
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10: Data and Data Governance
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
  - c3-s3-a16  # III.S3.A16: Obligations of Providers of High-Risk AI Systems
related_risks:
  - ri-1   # Information Leaked To Hosted Model
  - ri-9   # Data Poisoning
---

## Summary

LLM applications pose data leakage risks not only through vector stores but across all components handling derived data, such as embeddings, prompt logs, and caches. These representations, while not directly human-readable, can still expose sensitive information via inversion or inference attacks, especially when security controls like access management, encryption, and auditing are lacking. To mitigate these risks, robust enterprise-grade security measures must be applied consistently across all parts of the LLM pipeline.

## Description

Vector stores are specialized databases designed to store and manage 'vector embeddings'—dense numerical representations of data such as text, images, or other complex data types. According to [OpenAI](https://platform.openai.com/docs/guides/embeddings), *"An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness."* These embeddings capture the semantic meaning of the input data, enabling advanced operations like semantic search, similarity comparisons, and clustering.

In the context of [Retrieval-Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) models, vector stores play a critical role. When a user query is received, it's converted into an embedding, and the vector store is queried to find the most semantically similar embeddings, which correspond to relevant pieces of data or documents. These retrieved data are then used to generate responses using Large Language Models (LLMs).

### Threat Description

In a typical RAG architecture that relies on a vector store to retrieve organizational knowledge, the immaturity of current vector store technologies poses significant confidentiality and integrity risks.

#### Information Leakage from Embeddings
While embeddings are not directly human-readable, recent research demonstrates they can reveal substantial information about the original data.
*   **Embedding Inversion**: Attacks can reconstruct sensitive information from embeddings, potentially exposing proprietary or personally identifiable information (PII). The paper ["Text Embeddings Reveal (Almost) as Much as Text"](https://arxiv.org/abs/2310.06816) shows how embeddings can be used to recover original text with high fidelity. The corresponding [GitHub repository](https://github.com/jxmorris12/vec2text) provides a practical example.
*   **Membership Inference**: An adversary can determine if specific data is in the embedding store. This is problematic where the mere presence of information is sensitive. For example, an adversary could generate embeddings for *"Company A to acquire Company B"* and probe the vector store to infer if such a confidential transaction is being discussed internally.

#### Integrity and Security Risks
Vector stores holding embeddings of sensitive internal data may lack enterprise-grade security controls, leading to several risks:
*   **Data Poisoning**: An attacker with access could inject malicious or misleading embeddings, degrading the quality and accuracy of the LLM's responses. Since embeddings are dense numerical representations, spotting malicious alterations is difficult. The paper [PoisonedRAG](https://arxiv.org/abs/2402.07867) provides a relevant example.
*   **Misconfigured Access Controls**: A lack of role-based access control (RBAC) or overly permissive settings can allow unauthorized users to retrieve sensitive embeddings.
*   **Encryption Failures**: Without encryption at rest, embeddings containing sensitive information may be exposed to anyone with access to the storage layer.
*   **Audit Deficiencies**: The absence of robust audit logging makes it difficult to detect unauthorized access, modifications, or data exfiltration.

## Links
* [OpenAI – Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
* [AWS – What is Retrieval-Augmented Generation (RAG)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
* [Text Embeddings Reveal (Almost) as Much as Text – arXiv](https://arxiv.org/abs/2310.06816)
* [vec2text – GitHub Repository](https://github.com/jxmorris12/vec2text)
* [PoisonedRAG – arXiv](https://arxiv.org/abs/2402.07867)
