---
sequence: 1
title: AI Data Leakage Prevention and Detection
layout: mitigation
doc-status: Approved-Specification
type: DET
iso-42001_references:
  - A-7-2    # ISO 42001: Data for development and enhancement of AI system
  - A-6-2-6  # ISO 42001: AI system operation and monitoring
  - A-5-2    # ISO 42001: AI system impact assessment process
nist-sp-800-53r5_references:
  - ac-4  # AC-4 Information Flow Enforcement
  - ac-20  # AC-20 Use Of External Systems
  - au-13  # AU-13 Monitoring For Information Disclosure
  - ca-3  # CA-3 Information Exchange
  - ca-7  # CA-7 Authorization
  - ir-4  # IR-4 Incident Handling
  - ir-9  # IR-9 Information Spillage Response
  - mp-6  # MP-6 Media Sanitization
  - sa-9  # SA-9 External System Services
  - sc-7  # SC-7 Boundary Protection
  - sc-8  # SC-8 Transmission Confidentiality And Integrity
  - sc-28  # SC-28 Protection Of Information AT Rest
  - si-4  # SI-4 System Monitoring
  - si-20  # SI-20 Tainting
mitigates:
  - ri-1  # Information Leaked To Hosted Model
related_mitigations:
  - mi-2   # Data Filtering From External Knowledge Bases
  - mi-4   # AI System Observability
  - mi-14  # Encryption of AI Data at Rest
---

## Purpose

Data Leakage Prevention and Detection (DLP&D) for Artificial Intelligence (AI) systems encompasses a combination of proactive measures to **prevent sensitive data from unauthorized egress or exposure** through these systems, and detective measures to **identify such incidents promptly if they occur.** This control is critical for safeguarding various types of information associated with AI, including:
* **Session Data:** Information exchanged during interactions with AI models (e.g., user prompts, model responses, intermediate data).
* **Training Data:** Proprietary or sensitive datasets used to train or fine-tune AI models.
* **Model Intellectual Property:** The AI models themselves (weights, architecture) which represent significant intellectual property.

This control applies to both internally developed AI systems and, crucially, to scenarios involving Third-Party Service Providers (TSPs) for LLM-powered services or raw model endpoints, where data may cross organizational boundaries.

---

## Key Principles

Effective DLP&D for AI systems is built upon these fundamental strategies:

* **Defense in Depth:** Employ multiple layers of controls—technical, contractual, and procedural—to create a robust defense against data leakage.
* **Data Minimization and De-identification:** Only collect, process, and transmit sensitive data that is strictly necessary for the AI system's function. Utilize anonymization, pseudonymization, or data masking techniques wherever feasible.
* **Secure Data Handling Across the Lifecycle:** Integrate DLP&D considerations into all stages of the AI system lifecycle, from data sourcing and preparation through development, deployment, operation, monitoring, and decommissioning (aligns with ISO 42001 A.7.2).
* **Continuous Monitoring and Vigilance:** Implement ongoing monitoring of data flows, system logs, and external environments to detect anomalies or direct indicators of potential data leakage (aligns with ISO 42001 A.6.2.6).
* **Third-Party Risk Management:** Conduct thorough due diligence and establish strong contractual safeguards defining data handling, persistence, and security obligations when using third-party AI services or data providers.
* **"Assume Breach" for Detection:** Design detective mechanisms with the understanding that preventative controls, despite best efforts, might eventually be bypassed.
* **Incident Response Preparedness:** Develop and maintain a well-defined incident response plan to address detected data leakage events swiftly and effectively.
* **Impact-Driven Prioritization:** Understand the potential consequences of various data leakage scenarios (as per ISO 42001 A.5.2) to prioritize preventative and detective efforts on the most critical data assets and AI systems.

---
## Implementation Guidance

This section outlines specific measures for both preventing and detecting data leakage in AI systems.

### I. Proactive Measures: Preventing Data Leakage

#### A. Protecting AI Session Data with Third-Party Services

The use of TSPs for cutting-edge LLMs is often compelling due to proprietary model access, specialized GPU compute requirements, and scalability needs. However, this necessitates rigorous controls across several domains:

##### 1. Secure Data Transmission and Architecture
*   **Secure Communication Channels:** Mandate and verify the use of strong, industry-best-practice encryption protocols (e.g., TLS 1.3+) for all data in transit.
*   **Secure Network Architectures:** Where feasible, prefer architectural patterns like private endpoints or dedicated clusters within the institution's secure cloud tenant to minimize data transmission over the public internet.

##### 2. Data Handling and Persistence by Third Parties
*   **Control over Data Persistence:** Contractually require and technically verify that TSPs default to "zero persistence" or minimal, time-bound persistence of logs and session data.
*   **Secure Data Disposal:** Ensure vendor contracts include commitments to secure and certified disposal of storage media.
*   **Scrutiny of Multi-Tenant Architectures:** Thoroughly review the TSP's architecture, security certifications (e.g., SOC 2 Type II), and penetration test results to assess the adequacy of logical tenant isolation.

##### 3. Contractual and Policy Safeguards
*   **Prohibition on Unauthorized Data Use:** Legal agreements must explicitly prohibit AI providers from using proprietary data for training their general-purpose models without explicit consent.
*   **Transparency in Performance Optimizations:** Require TSPs to provide clear information about caching or other performance optimizations that might create new data leakage vectors.

#### B. Protecting AI Training Data
*   **Robust Access Controls and Secure Storage:** Implement strict access controls (e.g., Role-Based Access Control), strong encryption at rest, and secure, isolated storage environments for all proprietary datasets.
*   **Guardrails Against Extraction via Prompts:** Implement and continuously evaluate input/output filtering mechanisms ("guardrails") to detect and block attempts by users to extract training data through crafted prompts.

#### C. Protecting AI Model Intellectual Property
*   **Secure Model Storage and Access Control:** Treat trained model weights and configurations as highly sensitive intellectual property, storing them in secure, access-controlled repositories with strong encryption.
*   **Prevent Unauthorized Distribution:** Implement technical and contractual controls to prevent unauthorized copying or transfer of model artifacts.

### II. Detective Measures: Identifying Data Leakage

#### A. Detecting Session Data Leakage from External Services

##### 1. Deception-Based Detection
*   **Canary Tokens ("Honey Tokens"):** Embed uniquely identifiable, non-sensitive markers ("canaries") within data streams sent to AI models. Continuously monitor public and dark web sources for the appearance of these canaries.
*   **Data Fingerprinting:** Generate unique cryptographic hashes ("fingerprints") of sensitive data before it is processed by an AI system. Monitor for the appearance of these fingerprints in unauthorized locations.

##### 2. Automated Monitoring and Response
*   **Integration into AI Interaction Points:** Integrate canary token generation and fingerprinting at key data touchpoints like API gateways or data ingestion pipelines.
*   **Automated Detection and Incident Response:** Develop automated systems to scan for exposed canaries or fingerprints. Upon detection, trigger an immediate alert to the security operations team to initiate a predefined incident response plan.

#### B. Detecting Unauthorized Training Data Extraction
*   **Monitoring Guardrail Effectiveness:** Continuously monitor the performance and logs of input/output guardrails. Investigate suspicious prompt patterns that might indicate attempts to circumvent these protections.

#### C. Detecting AI Model Weight Leakage
*   **Emerging Techniques:** Stay informed about and evaluate emerging research for "fingerprinting" or watermarking AI models (e.g., "Instructional Fingerprinting") to detect unauthorized copies of proprietary models.

---
## Importance and Benefits

Implementing comprehensive Data Leakage Prevention and Detection controls for AI systems is vital for financial institutions due to:

* **Protection of Highly Sensitive Information:** Safeguards customer Personally Identifiable Information (PII), confidential corporate data, financial records, and strategic information that may be processed by or embedded within AI systems.
* **Preservation of Valuable Intellectual Property:** Protects proprietary AI models, unique training datasets, and related innovations from theft, unauthorized use, or competitive disadvantage.
* **Adherence to Regulatory Compliance:** Helps meet stringent obligations under various data protection laws (e.g., GDPR, CCPA, GLBA) and industry-specific regulations which mandate the security of sensitive data and often carry severe penalties for breaches.
* **Maintaining Customer and Stakeholder Trust:** Prevents data breaches and unauthorized disclosures that can severely damage customer trust, institutional reputation, and investor confidence.
* **Mitigating Financial and Operational Loss:** Avoids direct financial costs associated with data leakage incidents (e.g., fines, legal fees, incident response costs) and indirect costs from business disruption or loss of competitive edge.
* **Enabling Safe Innovation with Third-Party AI:** Provides crucial mechanisms to reduce and monitor risks when leveraging external AI services and foundational models, allowing the institution to innovate confidently while managing data exposure.
* **Early Warning System:** Detective controls act as an early warning system, enabling rapid response to contain leaks and minimize their impact before they escalate.
