---
layout: mitigation
doc-status: Draft
sequence: 2
type:
  - Preventative
mitigates:
  - ri-1
title: Data filtering from Confluence into the samples
---

To mitigate the risk of sensitive data leakage and tampering in the vector store, the data filtering control ensures that sensitive information from internal knowledge sources, such as Confluence, is anonymized and/or entirely excluded before being processed by the model. This control aims to limit the exposure of sensitive organizational knowledge when creating embeddings that feed into the vector store, thus reducing the likelihood of confidential information being accessible or manipulated.

- **Anonymization and Data Sanitization**: Data extracted from Confluence or other internal knowledge repositories is filtered through anonymization and sanitization processes before it is converted into embeddings for the vector store. This prevents direct or identifiable sensitive data (e.g., PII, proprietary algorithms) from entering the model or vector store in the first place. Techniques could include, but are not limited to:
  - Masking personally identifiable information (PII).
  - Redacting sensitive financial or operational data.
  - Scrubbing proprietary corporate knowledge that may be exposed to unauthorized users or malicious actors.
- **Segregation of Sensitive Models**: For data that cannot be adequately sanitized, a separate model and vector store instance can be used to enforce stronger access controls. For example, highly sensitive data might be stored in a restricted vector store with more granular RBAC and encryption measures, ensuring only authorized users can query the sensitive data.
- **Response Filtering Based on Confluence Heuristics**: The model's responses are also filtered against the same heuristics used to sanitize the data at the ingestion point. This ensures that sensitive data that may have bypassed sanitization is detected and scrubbed before being returned to the user. Response filtering acts as a secondary layer of protection, preventing sensitive or proprietary data from leaking through model outputs.

This control emphasizes a preventive focus on the entry of sensitive information into the vector store, which minimizes the attack surface and significantly reduces the risk of unauthorized access or poisoning. This is especially important given the immaturity of vector store technologies.
