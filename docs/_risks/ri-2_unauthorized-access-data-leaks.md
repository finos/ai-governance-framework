---
sequence: 2
title: Unauthorized Access & Data Leaks
layout: risk
doc-status: Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM01  # OWASP LLM: Prompt Injection
  - OWASP-LLM_2025_LLM02  # OWASP LLM: Sensitive Information Disclosure
  - OWASP-LLM_2025_LLM07  # OWASP LLM: System Prompt Leakage
  - OWASP-LLM_2025_LLM08  # OWASP LLM: Vector and Embedding Weaknesses
  - OWASP-ML_2023_ML03    # OWASP ML Model Inversion Attack
  - OWASP-ML_2023_ML04    # OWASP ML Membership Inference Attack
  - OWASP-ML_2023_ML05    # OWASP ML Model Theft
  - NIST-600_2024_2-04    # NIST 600.1: Data Privacy
  - NIST-600_2024_2-09    # NIST 600.1: Information Security
ffiec_references:
  - ffiec_sec_iii-security-operations
  - ffiec_sec_iv-information-security-program-effectiveness
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai_references:
  - eu-ai_c3-s2-a10  # III.S2.A10 Data and Data Governance
  - eu-ai_c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - eu-ai_c3-s3-a16  # III.S3.A16 Obligations of Providers of High-Risk AI Systems
---

Modern AI systems often rely on specialized repositories to store and manage complex data representations. These representations, frequently numerical in nature (sometimes referred to as 'embeddings'), aim to capture the underlying meaning or key features of diverse data types such as text, images, or other complex information. The principle is that the closer these numerical representations are to each other, the more related the original data items are considered. This capability allows AI to perform sophisticated operations, such as searching for information based on its semantic meaning rather than just keywords.

Many advanced AI models, particularly those designed to generate informed and context-aware responses (a technique sometimes known as Retrieval-Augmented Generation or RAG), use these specialized data repositories as a core component. When a user query is received, the AI typically converts it into a similar numerical format and then searches the repository for the most semantically relevant stored data. This retrieved information is then used by the AI to help formulate a more accurate, relevant, and contextually appropriate response.

Threat Description

When AI systems utilize these specialized data repositories to access and retrieve organizational knowledge (e.g., from internal documentation, databases, or other knowledge sources), the evolving nature of the technologies underpinning these repositories can introduce significant risks to data confidentiality, integrity, and availability.

If these repositories store sensitive internal information in these AI-readable formats, they may lack mature, enterprise-grade security controls. This can manifest as:

  * Weaknesses in managing and enforcing who can access the data (access control).
  * Insufficient encryption of the stored data representations, both at rest and in transit.
  * Inadequate logging and monitoring of activities within and around these repositories.

Such shortcomings, whether due to misconfiguration, the inherent immaturity of current technologies, or oversight during implementation, can lead to unauthorized access to sensitive data representations. This could potentially result in data tampering, theft, or accidental disclosure of confidential information.

Although these AI-readable data representations are not directly understandable by humans in the same way as the original data, research has demonstrated that they can still reveal significant information about the source material. Sophisticated techniques, sometimes called 'inversion attacks,' may allow adversaries to reconstruct or infer sensitive details from these representations. This could lead to the exposure of proprietary business information or personally identifiable information (PII), even if the original data was thought to be adequately protected by its conversion into this AI-specific format. The risk is that these abstract representations may not sufficiently anonymize or obscure the underlying sensitive content.

Furthermore, these AI data repositories can be vulnerable to 'membership inference attacks.' In such an attack, an adversary attempts to determine if a specific piece of information is present within the repository by strategically probing the system with queries related to that information and observing the AI's responses or system behavior. This is a serious concern in contexts where even the knowledge that certain data exists within the system is sensitive. For example, if an AI's knowledge base includes confidential business strategy documents, an attacker might craft queries related to hypothetical scenarios (e.g., a potential merger or acquisition). By analyzing system responses, the attacker might infer whether such information is indeed part of the AI's knowledge base, thereby uncovering confidential corporate activities.

Insufficient access controls to these data repositories also create opportunities for 'data poisoning' attacks. An attacker who gains unauthorized access could inject malicious, misleading, or biased data representations into the system. These compromised representations can then corrupt the information the AI relies on, leading to a degradation in the quality, accuracy, or fairness of the AI's outputs. Detecting such manipulations can be particularly challenging because these data representations are often complex and not easily inspected for subtle, malicious alterations, unlike traditional data records.

Because the technologies for managing these AI-specific data repositories are still maturing, they may not yet fully incorporate or adhere to established enterprise security standards. This can leave exploitable gaps, for example:

  * Misconfigured or Inadequate Access Controls: Systems may lack fine-grained, role-based access controls (RBAC), or may be deployed with overly permissive settings. This could allow unauthorized users (both internal and external) to access or modify sensitive data representations, bypassing intended security measures.
  *  Insufficient Data Encryption: If the AI-readable data representations are not strongly encrypted while stored or when being transmitted, they could be exposed to anyone who gains unauthorized access to the underlying storage systems or network traffic, leading to data breaches or unauthorized modifications.
  * Limited Audit Capabilities: A lack of comprehensive and detailed audit logs detailing access patterns, data modifications, and system queries makes it difficult to detect, investigate, and respond to security incidents or unauthorized activities in a timely and effective manner. This can allow breaches or misuse to go unnoticed for extended periods.

These vulnerabilities collectively increase the risk of sensitive information disclosure, data integrity compromises, and potential system manipulation. These concerns align with issues highlighted by established security frameworks, such as the OWASP Top 10 for Large Language Model Applications (e.g., LLM06: Sensitive Information Disclosure and LLM04: Model Data Poisoning), which address the dangers of exposing proprietary data or PII and corrupting data through AI systems.
