---
sequence: 2
title: Data Filtering From External Knowledge Bases
layout: mitigation
doc-status: Approved-Specification
type: PREV
iso-42001_references:
  - A-7-2  # ISO 42001: Data for development and enhancement of AI system
  - A-7-3  # ISO 42001: Acquisition of data
  - A-7-4  # ISO 42001: Quality of data for AI systems
  - A-7-6  # ISO 42001: Data preparation
nist-sp-800-53r5_references:
  - ac-4  # AC-4 Information Flow Enforcement
  - ac-22  # AC-22 Publicly Accessible Content
  - mp-6  # MP-6 Media Sanitization
  - pt-2  # PT-2 Authority To Process Personally Identifiable Information
  - si-4  # SI-4 System Monitoring
  - si-12  # SI-12 Information Management And Retention
  - si-15  # SI-15 Information Output Filtering
  - si-19  # SI-19 De-identification
mitigates:
  - ri-1  # Information Leaked To Hosted Model
related_mitigations:
  - mi-1   # AI Data Leakage Prevention and Detection
  - mi-6   # Data Quality Classification Sensitivity
  - mi-16  # Preserving Source Data Access Controls in AI Systems
---

## Purpose

This control addresses the critical need to **sanitize, filter, and appropriately manage sensitive information** when AI systems ingest data from internal knowledge sources such as wikis, document management systems, databases, or collaboration platforms (e.g., Confluence, SharePoint, internal websites). The primary objective is to **prevent the inadvertent exposure, leakage, or manipulation of confidential organizational knowledge** when this data is processed by AI models, converted into embeddings for vector databases, or used in Retrieval Augmented Generation (RAG) systems.

Given that many AI applications, particularly RAG systems, rely on internal knowledge bases to provide contextually relevant and organization-specific responses, ensuring that sensitive information within these sources is appropriately handled is paramount for maintaining data confidentiality and preventing unauthorized access.

---
## Key Principles

Effective data filtering from external knowledge bases should be guided by these core principles:

* **Proactive Data Sanitization:** Apply filtering and anonymization techniques **before** data enters the AI processing pipeline, vector databases, or any external service endpoints (aligns with ISO 42001 A.7.6).
* **Data Classification Awareness:** Understand and respect the sensitivity levels and access controls associated with source data when determining appropriate filtering strategies (supports ISO 42001 A.7.4).
* **Principle of Least Exposure:** Only include data in AI systems that is necessary for the intended business function, and ensure that even this data is appropriately de-identified or masked when possible.
* **Defense in Depth:** Implement multiple layers of filtering—at data ingestion, during processing, and at output generation—to create robust protection against data leakage.
* **Auditability and Transparency:** Maintain clear documentation and audit trails of what data filtering processes have been applied and why (supports ISO 42001 A.7.2).

---

## Implementation Guidance

### 1. Rigorous Data Cleansing and Anonymization at Ingestion

* **Pre-Processing Review and Cleansing:**
    * **Process:** Before any information from internal knowledge sources is ingested by an AI system (whether for training, vector database population, or real-time retrieval), it must undergo a thorough review and cleansing process.
    * **Objective:** Identify and remove or appropriately anonymize sensitive details to ensure that data fed into the AI system is free from information that could pose a security or privacy risk if inadvertently exposed.

* **Categories of Data to Target for Filtering:**
    * **Personally Identifiable Information (PII):** Names, contact details, financial account numbers, employee IDs, social security numbers, addresses, and other personal identifiers.
    * **Proprietary Business Information:** Trade secrets, intellectual property, unreleased financial results, strategic plans, merger and acquisition details, customer lists, pricing strategies, and competitive intelligence.
    * **Sensitive Internal Operational Data:** Security configurations, system architecture details, access credentials, internal process documentation not intended for broader access, incident reports, and audit findings.
    * **Confidential Customer Data:** Account information, transaction details, credit scores, loan applications, investment portfolios, and personal financial information.
    * **Regulatory or Compliance-Sensitive Information:** Legal advice, regulatory correspondence, compliance violations, investigation details, and privileged communications.

* **Filtering and Anonymization Methods:**
    * **Data Masking:** Replace sensitive data fields with anonymized equivalents (e.g., "Employee12345" instead of "John Smith").
    * **Redaction:** Remove entire sections of documents that contain sensitive information.
    * **Generalization:** Replace specific information with more general categories (e.g., "Major metropolitan area" instead of "New York City").
    * **Tokenization:** Replace sensitive data with non-sensitive tokens that can be mapped back to the original data only through a secure, separate system.
    * **Synthetic Data Generation:** For training purposes, generate synthetic data that maintains statistical properties of the original data without exposing actual sensitive information.

### 2. Segregation for Highly Sensitive Data

* **Isolated AI Systems for Critical Data:**
    * **Concept:** For datasets or knowledge sources containing exceptionally sensitive information that cannot be adequately protected through standard cleansing or anonymization techniques, implement separate, isolated AI systems or environments.
    * **Implementation:** Create distinct AI models and associated data stores (e.g., separate vector databases for RAG systems) with much stricter access controls, enhanced encryption, and limited network connectivity.
    * **Benefit:** Ensures that only explicitly authorized personnel or tightly controlled AI processes can interact with highly sensitive data, minimizing the risk of broader exposure.

* **Access Domain-Based Segregation:**
    * **Strategy:** Segment data and AI system access based on clearly defined access domains that mirror the organization's existing data classification and access control structures.
    * **Implementation:** Different user groups or business units may have access only to AI instances that contain data appropriate to their clearance level and business need.

### 3. Filtering AI System Outputs (Secondary Defense)

* **Response Filtering and Validation:**
    * **Rationale:** As an additional layer of defense, responses and information generated by the AI system should be monitored and filtered before being presented to users or integrated into other systems.
    * **Function:** Acts as a crucial safety net to detect and remove any sensitive data that might have inadvertently bypassed the initial input cleansing stages or was unexpectedly reconstructed or inferred by the AI model during its processing.
    * **Scope:** Output filtering should apply the same principles and rules used for sanitizing input data, checking for PII, proprietary information, and other sensitive content.

* **Contextual Output Analysis:**
    * **Dynamic Filtering:** Implement intelligent filtering that considers the context of the user's query and their authorization level to determine what information should be included in the response.
    * **Confidence Scoring:** Where technically feasible, implement systems that assess the confidence level of the AI's output and flag responses that may contain uncertain or potentially sensitive information for human review.

### 4. Integration with Source System Access Controls

* **Respect Original Permissions:** When possible, design the AI system to respect and replicate the original access control permissions from source systems (see [MI-16 Preserving Access Controls](#mi-16)).
* **Dynamic Source Querying:** For real-time RAG systems, consider querying source systems dynamically while respecting user permissions, rather than pre-processing all data indiscriminately.

### 5. Monitoring and Continuous Improvement

* **Regular Review of Filtering Effectiveness:** Periodically audit the effectiveness of data filtering processes by sampling processed data and checking for any sensitive information that may have been missed.
* **Feedback Loop Integration:** Establish mechanisms for users and reviewers to report instances where sensitive information may have been inappropriately exposed, using this feedback to improve filtering algorithms and processes.
* **Threat Intelligence Integration:** Stay informed about new types of data leakage vectors and attack techniques that might affect AI systems, and update filtering strategies accordingly.

---
## Challenges and Considerations

* **Balancing Utility and Security:** Over-aggressive filtering may remove so much information that the AI system becomes less useful for legitimate business purposes. Finding the right balance requires careful consideration of business needs and risk tolerance.
* **Contextual Sensitivity:** Some information may be sensitive in certain contexts but not others. Developing filtering rules that understand context can be complex.
* **False Positives and Negatives:** Filtering systems may incorrectly identify non-sensitive information as sensitive (false positives) or miss actual sensitive information (false negatives). Regular calibration and human oversight are essential.
* **Evolving Data Landscape:** As organizational data and business processes evolve, filtering rules and strategies must be updated accordingly.
* **Performance Impact:** Comprehensive data filtering can introduce latency in AI system responses, particularly for real-time applications.

---
## Importance and Benefits

Implementing robust data filtering from external knowledge bases is a critical preventative measure that provides significant benefits:

* **Prevention of Data Leakage:** Significantly reduces the risk of sensitive organizational information being inadvertently exposed through AI system outputs or stored in less secure external services.
* **Regulatory Compliance:** Helps meet requirements under data protection regulations (e.g., GDPR, CCPA, GLBA) that mandate the protection of personal and sensitive business information.
* **Intellectual Property Protection:** Safeguards valuable trade secrets, strategic information, and proprietary data from unauthorized disclosure or competitive exposure.
* **Reduced Attack Surface:** By controlling the information that enters AI operational environments, organizations minimize the potential impact of AI-specific attacks like prompt injection or data extraction attempts.
* **Enhanced Trust and Confidence:** Builds stakeholder confidence in AI systems by demonstrating rigorous data protection practices.
* **Compliance with Internal Data Governance:** Supports adherence to internal data classification and handling policies within AI contexts.
* **Mitigation of Insider Risk:** Reduces the risk of sensitive information being accessed by unauthorized internal users through AI interfaces.

This control is particularly important given the evolving nature of AI technologies and the sophisticated ways they interact with and process large volumes of organizational information. A proactive approach to data sanitization helps maintain confidentiality, integrity, and compliance while enabling the organization to benefit from AI capabilities.
