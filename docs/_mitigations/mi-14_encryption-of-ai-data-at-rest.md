---
sequence: 14
title: Encryption of AI Data at Rest
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-7-2  # ISO 42001: Data for development and enhancement of AI system
mitigates:
  - ri-2   # Information Leaked to Vector Store
  - ri-22  # Regulatory Compliance and Oversight
---

## Purpose

Encryption of data at rest is a fundamental security control that involves **transforming stored information into a cryptographically secured format using robust encryption algorithms.** This process renders the data unintelligible and inaccessible to unauthorized parties unless they possess the corresponding decryption key. The primary objective is to **protect the confidentiality and integrity of sensitive data** associated with AI systems, even if the underlying storage medium (e.g., disks, servers, backup tapes) is physically or logically compromised. While considered a standard security practice across IT, its diligent application to all components of AI systems, including newer technologies like vector databases, is critical.

---
## Key Principles

The implementation of encryption at rest for AI data should adhere to these core principles:

* **Defense in Depth:** Encryption at rest serves as an essential layer in a multi-layered security strategy, complementing other controls like access controls and network security.
* **Comprehensive Data Protection:** All sensitive data associated with the AI lifecycle that is stored persistently—regardless of the storage medium or location—should be subject to encryption.
* **Alignment with Data Classification:** The strength of encryption and key management practices should align with the sensitivity level of the data, as defined by the institution's data classification policy.
* **Robust Key Management:** The security of encrypted data is entirely dependent on the security of the encryption keys. Therefore, secure key generation, storage, access control, rotation, and lifecycle management are paramount.
* **Default Security Posture:** Encryption at rest should be a default configuration for all new storage solutions and data repositories used for AI systems, rather than an optional add-on.

---
## Scope of Data Requiring Encryption at Rest for AI Systems

Within the context of AI systems, encryption at rest should be applied to a wide range of data types, including but not limited to:

* **Training, Validation, and Testing Datasets:** Raw and processed datasets containing potentially sensitive or proprietary information used to build and evaluate AI models.
* **Intermediate Data Artifacts:** Sensitive intermediate data generated during AI development and pre-processing, such as feature sets, serialized data objects, or temporary files.
* **Embeddings and Vector Representations:** Numerical representations of data (e.g., text, images) stored in vector databases for use in RAG systems or similarity searches.
* **AI Model Artifacts:** The trained model files themselves, which constitute valuable intellectual property and may inadvertently contain or reveal sensitive information from training data.
* **Log Files:** System and application logs from AI platforms and applications, which may capture sensitive input data, model outputs, or user activity.
* **Configuration Files:** Files containing sensitive parameters such as API keys, database credentials, or other secrets (though these are ideally managed via dedicated secrets management systems).
* **Backups and Archives:** All backups and archival copies of the aforementioned data types.

---
## Implementation Guidance

Effective implementation of data at rest encryption for AI systems involves the following:

### 1. Define Policies and Standards
* Establish clear organizational policies and standards for data encryption at rest. These should specify approved encryption algorithms (e.g., AES-256), key lengths, modes of operation, and mandatory key management procedures. (Aligns with ISO 42001 A.7.2 regarding data management processes).

### 2. Select Appropriate Encryption Mechanisms
* **Storage-Level Encryption:**
    * **Full-Disk Encryption (FDE):** Encrypts entire physical or virtual disks.
    * **File System-Level Encryption:** Encrypts individual files or directories.
    * **Database Encryption:** Many database systems (SQL, NoSQL) offer built-in encryption capabilities like Transparent Data Encryption (TDE), which encrypts data files, log files, and backups.
* **Application-Level Encryption:** Data is encrypted by the application before being written to any storage medium. This provides granular control but requires careful implementation within the AI applications or data pipelines.

### 3. Implement Robust Key Management
* Utilize a dedicated, hardened Key Management System (KMS) for the secure lifecycle management of encryption keys (generation, storage, distribution, rotation, backup, and revocation).
* Enforce strict access controls to encryption keys based on the principle of least privilege and separation of duties.
* Regularly rotate encryption keys according to policy and best practices.

### 4. Specific Considerations for AI Components and New Technologies
* **Vector Databases:**
    * **Criticality:** Given that vector databases are a relatively recent technology area central to many modern AI applications (e.g., RAG systems), it's crucial to verify and ensure they support robust encryption at rest and that this feature is enabled and correctly configured. Default security postures may vary significantly between different vector database solutions.
    * **Cloud-Native Vector Stores:** When using services like Azure AI Search or AWS OpenSearch Service, leverage their integrated encryption at rest features. Ensure these are configured to meet institutional security standards, including options for customer-managed encryption keys (CMEK) if available and required.
    * **Managed SaaS Vector Databases:** For third-party managed services (e.g., Pinecone), carefully review their security documentation and contractual agreements regarding their data encryption practices, key management responsibilities, and compliance certifications. In such cases, securing API access to the service becomes paramount.
    * **Self-Hosted Vector Databases:** If deploying self-hosted vector databases (e.g., using Redis with vector capabilities, or FAISS with persistent storage), the institution bears full responsibility for implementing and managing encryption at rest for the underlying storage infrastructure, securing the host servers, and managing the encryption keys. This approach requires significant in-house security expertise.
* **In-Memory Data Processing (e.g., FAISS):**
    * While primarily operating in-memory (like some configurations of FAISS) can reduce risks associated with persistent storage breaches during runtime, it's vital to remember that:
        * Any data loaded into memory must be protected while in transit and sourced from securely encrypted storage.
        * If any data or index from such in-memory tools is persisted to disk (e.g., for saving, backup, or sharing), that persisted data *must* be encrypted. Relying solely on in-memory operation is not a substitute for encryption if data touches persistent storage at any point.

### 5. Regular Verification and Audit
* Periodically verify that encryption controls are correctly implemented, active, and effective across all relevant AI data storage systems.
* Include encryption at rest configurations and key management practices as part of regular information security audits and assessments.

---
## Importance and Benefits

Implementing strong encryption for AI data at rest provides crucial benefits to financial institutions:

* **Enhanced Data Confidentiality:** 🛡️ Protects sensitive corporate, customer, and AI model data from unauthorized disclosure if storage media is lost, stolen, physically accessed by unauthorized individuals, or if other security layers are breached.
* **Reduced Impact of Data Breaches:** 📉 In the event of a security breach that compromises storage systems, properly encrypted data remains unintelligible and unusable to attackers without the decryption keys, significantly mitigating the impact.
* **Support for Regulatory Compliance:** 📜 Helps meet the stringent data protection requirements mandated by various regulations (e.g., GDPR, GLBA, NYDFS Cybersecurity Regulation, PCI DSS), many of which require or strongly recommend encryption for sensitive data.
* **Protection of Intellectual Property:** 💡 AI models and proprietary datasets represent valuable intellectual property. Encryption at rest helps protect these assets from theft, unauthorized copying, or reverse engineering.
* **Increased Trust and Confidence:** 🤝 Demonstrates a strong commitment to data security, thereby building and maintaining trust with customers, partners, regulators, and other stakeholders.
* **Alignment with Security Best Practices:** Adheres to widely recognized information security standards and best practices, strengthening the institution's overall security posture.
