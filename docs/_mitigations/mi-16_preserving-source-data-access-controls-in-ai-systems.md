---
sequence: 16
title: Preserving Source Data Access Controls in AI Systems
layout: mitigation
doc-status: Draft
type: DET
iso-42001_references:
  - A-7-2  # ISO 42001: Data for development and enhancement of AI system
  - A-7-3  # ISO 42001: Acquisition of data
  - A-9-2  # ISO 42001: Processes for responsible use of AI systems
mitigates:
  - ri-2   # Information Leaked to Vector Store
  - ri-22  # Regulatory Compliance and Oversight
---

## Purpose

This control addresses the critical requirement that when an Artificial Intelligence (AI) system—particularly one employing Retrieval Augmented Generation (RAG) or similar techniques—ingests data from various internal or external sources, the **original access control permissions, restrictions, and entitlements associated with that source data must be understood, preserved, and effectively enforced** when the AI system subsequently uses or presents information derived from that data.

While the *implementation* of mechanisms to preserve these controls is preventative, this control also has a significant **detective aspect**. This involves the ongoing verification, auditing, and monitoring to ensure that these access controls are correctly mapped, consistently maintained within the AI ecosystem, and are not being inadvertently or maliciously bypassed. Detecting deviations or failures in preserving source access controls is paramount to preventing unauthorized data exposure through the AI system.

---
## Key Principles

The preservation of source data access controls within AI systems should be guided by these fundamental principles:

* **Fidelity of Control Replication:** The primary goal is to replicate the intent and effect of original source data access permissions as faithfully as possible within the AI system's environment. (Supports ISO 42001 A.7.2, A.7.3).
* **Principle of Least Privilege (Extended to AI):** The AI system, and users interacting through it, should only be able to access or derive insights from data segments for which appropriate authorization exists, mirroring the principle of least privilege from the source systems.
* **Data-Aware AI Design:** AI systems must be architected with an intrinsic understanding that ingested data carries varying levels of sensitivity and access restrictions. This understanding must inform how data is processed, stored, retrieved, and presented.
* **Continuous Verification and Auditability:** The mapping and enforcement of access controls within the AI system must be regularly audited, tested, and verified to ensure ongoing effectiveness and to detect any drift, misconfiguration, or bypass attempts.
* **Transparency of Access Logic:** The mechanisms by which the AI system determines and enforces access based on preserved source controls should be documented, understandable, and transparent to relevant stakeholders (e.g., security teams, auditors). (Supports ISO 42001 A.9.2).

---

## Implementation Guidance

Implementing and verifying the preservation of source access controls is a complex task, particularly for RAG systems. It requires a multi-faceted approach:

### 1. Understanding and Documenting Source Access Controls
* **Discovery and Analysis:** Before or during data ingestion, thoroughly identify, analyze, and document the existing access control lists (ACLs), roles, permissions, and any other entitlement mechanisms associated with all source data repositories (e.g., file shares, databases, document management systems like Confluence).
* **Mapping Entitlements:** Understand how these source permissions translate to user identities or groups within the organization's identity management system.

### 2. Strategies for Preserving and Enforcing Access Controls in AI Systems

* **A. Leveraging Native Access Controls in AI Data Stores (e.g., Vector Databases):**
    * **Assessment:** Evaluate whether the target data stores used by the AI system (e.g., vector databases, graph databases, knowledge graphs) offer granular, attribute-based, or role-based access control features at the document, record, or sub-document (chunk) level.
    * **Configuration:** If such features exist, meticulously map and configure these native controls to replicate the original source data permissions. For example, tag ingested data chunks with their original access permissions and configure the vector database to filter search results based on the querying user's entitlements matching these tags. This is often the most integrated approach if supported robustly by the technology.
* **B. Data Segregation and Siloing Based on Access Domains:**
    * **Strategy:** If fine-grained controls within a single AI data store are insufficient or technically infeasible, segregate ingested data into different physical or logical data stores (e.g., separate vector database instances, distinct indexes, or collections) based on clearly defined access level boundaries derived from the source systems.
    * **Access Provisioning:** Grant AI system components, or end-users interacting with the AI, access only to the specific segregated RAG instances or data stores that correspond to their authorized access domain.
    * **Consolidation of Granular Permissions:** If source systems have extremely granular and numerous distinct access levels, a pragmatic approach might involve consolidating these into a smaller set of broader access tiers within the AI system, provided this consolidation still upholds the fundamental security restrictions and risk appetite. This requires careful analysis and risk assessment.
* **C. Application-Layer Access Control Enforcement:**
    * **Mechanism:** Implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer would:
        1. Authenticate the user and retrieve their identity and associated entitlements from the corporate Identity Provider (IdP).
        2. Intercept the user's query to the AI.
        3. Before passing the query to the RAG system or LLM, modify it or constrain its scope to ensure that any data retrieval or processing only targets data segments the user is authorized to access (based on their entitlements and the preserved source permissions metadata).
        4. Filter the AI's response to redact or remove any information derived from data sources the user is not permitted to see.
    * **Complexity:** This approach can be complex to implement and maintain but offers flexibility when underlying data stores lack sufficient native access control capabilities.
* **D. Metadata-Driven Access Control at Query Time:**
    * **Ingestion Enrichment:** During the data ingestion process, enrich the data chunks or their corresponding metadata entries in the vector store with explicit tags, labels, or attributes representing the original source permissions, sensitivity levels, or authorized user groups/roles.
    * **Query-Time Filtering:** At query time, the RAG system (or an intermediary access control service) uses this metadata to filter the retrieved document chunks *before* they are passed to the LLM for synthesis. The system ensures that only chunks matching the querying user's entitlements are considered for generating the response.

### 3. Avoiding Insecure "Shortcuts"
* **System Prompt-Based Access Control (Strongly Discouraged):** Attempting to enforce access controls by merely instructing an LLM via its system prompt (e.g., "Only show data from 'Department X' to users in 'Group Y'") is **highly unreliable, inefficient, and proven to be easily bypassable** through adversarial prompting. This method should **not** be considered a secure mechanism for preserving access controls and must be avoided.

### 4. Verification, Auditing, and Monitoring (The Detective Aspect)
* **Regular Configuration Audits:** Periodically audit the configuration of access controls in source systems and, critically, how these are mapped and implemented within the AI data stores, RAG pipelines, and any application-layer enforcement points.
* **Penetration Testing and Red Teaming:** Conduct targeted security testing, including penetration tests and red teaming exercises, specifically designed to attempt to bypass the preserved access controls and access unauthorized data through the AI system.
* **Access Log Monitoring:** Implement comprehensive logging of user queries, data retrieval actions within the RAG system, and the final responses generated by the AI. Monitor these logs for:
    * Anomalous access patterns.
    * Attempts to query or access data beyond a user's expected scope.
    * Discrepancies between a user's known entitlements and the data sources apparently used to generate their responses.
* **Entitlement Reconciliation Reviews:** Periodically reconcile the list of users and their permissions for accessing the AI system (or specific RAG interfaces) against the access controls defined on the data ingested into those systems. The goal is to ensure there are no exfiltration paths where users might gain access to information they shouldn't, due to misconfiguration or aggregation effects. 
* **Data Lineage and Provenance Tracking:** To the extent possible, maintain lineage information that tracks which source documents (and their original permissions) contributed to specific AI-generated outputs. This aids in investigations if a potential access control violation is suspected.

---

## Challenges and Considerations

Implementing and maintaining the preservation of source access controls in AI systems is a significant technical and governance challenge:

* **Complexity of Mapping:** Translating diverse and often complex permission models from numerous source systems (each potentially with its own ACL structure, role definitions, etc.) into a consistent and enforceable model within the AI ecosystem is highly complex.
* **Granularity Mismatch:** Source systems may have very fine-grained permissions (e.g., cell-level in a database, paragraph-level in a document) that are difficult to replicate perfectly in current vector databases or RAG chunking strategies.
* **Scalability:** For organizations with vast numbers of data sources and highly granular access controls, segregating data into numerous distinct RAG instances can become unmanageable and resource-intensive.
* **Performance Overhead:** Implementing real-time, query-level access control checks (especially in the application layer or via complex metadata filtering) can introduce latency and impact the performance of the AI system.
* **Dynamic Nature of Permissions:** Access controls in source systems can change frequently. Ensuring these changes are promptly and accurately propagated to the AI system's access control mechanisms is a continuous challenge.
* **AI's Synthesis Capability:** A core challenge is when an AI synthesizes information from multiple retrieved chunks, some of which a user might be authorized to see, and some not. Preventing the AI from inadvertently revealing restricted information through such synthesis, while still providing a useful summary, is non-trivial.
* **Maturity of Tooling:** While improving, native access control features in some newer AI-specific data stores (like many vector databases) may not yet be as mature or granular as those in traditional enterprise data systems.

---

## Importance and Benefits

Despite the challenges, striving to preserve source data access controls within AI systems is crucial:

* **Unauthorized Access Prevention:** Prevents AI systems from becoming unintentional backdoors for accessing restricted data
* **Data Confidentiality Maintenance:** Upholds intended security posture and confidentiality requirements of source data
* **Regulatory Compliance:** Essential for adhering to data protection regulations and internal governance policies
* **Insider Risk Reduction:** Limits accessible data scope to only what user roles permit
* **Trust Building:** Assures stakeholders that AI systems respect and enforce established data access policies
* **Audit and Detection Support:** Enables identification and investigation of misconfigurations and policy violations
* **Responsible AI Deployment:** Ensures AI systems operate within established data governance frameworks
