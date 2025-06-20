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

#### A. Protecting AI Session Data (Especially with Third-Party Services)
The use of TSPs for cutting-edge LLMs is often compelling due to proprietary model access, specialized GPU compute requirements, and scalability needs. However, this necessitates rigorous controls:

* **Secure Communication Channels:**
    * **Action:** Mandate and verify the use of strong, industry-best-practice encryption protocols (e.g., TLS 1.3+) for all data in transit when interacting with TSPs or any external AI service endpoint.
    * **Rationale:** Protects against network taps and Man-In-The-Middle (MITM) attacks.
* **Secure Network Architectures:**
    * **Action:** Where feasible, prefer architectural patterns where the TSP hosts their service within the institution's secure cloud tenant (e.g., using private endpoints, dedicated clusters) to minimize data transmission outside of controlled system boundaries.
    * **Rationale:** Reduces exposure to public internet threats.
* **Control over Data Persistence by Third Parties:**
    * **Action:** Contractually require and, where possible, technically verify that TSPs default to "zero persistence" or minimal, time-bound persistence of logs, session data (prompts/responses), and temporary files (e.g., core dumps), unless explicitly agreed in writing for specific, justified purposes (e.g., audit, support) and with robust safeguards.
    * **Rationale:** Minimizes the data footprint at the TSP, reducing the window of opportunity for leakage from their systems.
* **Secure Data Disposal by Third Parties:**
    * **Action:** Ensure that vendor contracts include commitments to Data Lifecycle Management best practices, compatible with the institution's standards, particularly concerning the secure and certified disposal of storage media.
    * **Rationale:** Prevents data recovery from improperly decommissioned hardware.
* **Scrutiny of Multi-Tenant Architectures:**
    * **Action:** For multi-tenant AI services, the institution's security design and vendor risk management teams should thoroughly review the TSP's system architecture documentation, security certifications (e.g., SOC 2 Type II), and penetration test results to assess the adequacy of logical tenant isolation and controls preventing cross-tenant data leakage.
    * **Rationale:** Ensures one tenant's data is not inadvertently exposed to another.
* **Contractual Prohibitions on Unauthorized Data Use (e.g., Model Training):**
    * **Action:** Legal agreements with AI providers (especially for API-based access to foundational models) must explicitly state that proprietary API inputs/outputs (session data) will **not** be used for training their general-purpose models or for any other purpose outside the direct provision of the contracted service, without the institution's explicit, informed consent. (Addresses "Memorization" risk).
    * **Rationale:** Prevents institutional data from becoming embedded in publicly accessible or other clients' models.
* **Transparency and Control over Performance Optimizations (e.g., Caching):**
    * **Action:** Given the high computational cost of LLMs, TSPs may implement caching mechanisms (e.g., for token activations or common prompt prefixes) to reduce redundancy and improve performance. Require TSPs to provide clear information about any such optimizations.
    * **Review:** The institution's ML and security teams should review these practices for potential risks of data remnants or unintended information exposure through shared cache elements.
    * **Rationale:** Ensures performance optimizations do not inadvertently create new data leakage vectors.

#### B. Protecting AI Training Data
* **Robust Access Controls and Secure Storage:** Implement strict access controls (e.g., Role-Based Access Control), strong encryption at rest, and secure, isolated storage environments for all proprietary datasets used for training or fine-tuning AI models.
* **Guardrails Against Extraction via Prompts:** For models fine-tuned with proprietary data, the institution or its AI provider must implement and continuously evaluate input/output filtering mechanisms ("guardrails"). These are designed to detect and block attempts by users to extract significant portions of the training data through carefully crafted prompts. This requires ongoing monitoring and adaptation by ML and security teams.

#### C. Protecting AI Model Intellectual Property (e.g., Weights, Architecture)
* **Secure Model Storage and Access Control:** Treat trained model weights, configurations, and proprietary architectures as highly sensitive intellectual property. Store them in secure, access-controlled repositories with strong encryption.
* **Prevent Unauthorized Distribution and Replication:** Implement technical controls (e.g., digital rights management, if applicable) and contractual obligations to prevent unauthorized copying, transfer, or distribution of model artifacts.

### II. Detective Measures: Identifying Data Leakage

#### A. Detecting Session Data Leakage (Especially with External AI Services)
* **Canary Tokens ("Honey Tokens"):**
    * **Concept:** Embed uniquely identifiable, non-sensitive markers (e.g., unique strings, fictitious identifiers, GUIDs) – "canaries" – within data streams, prompts, or queries sent to external or internal AI models. These canaries have no legitimate business value but are designed to be easily detectable if they appear in unauthorized locations.
    * **Implementation:** Strategically place canary tokens in representative samples of data. Continuously monitor public internet sources (e.g., code repositories, forums, paste sites), dark web locations, and potentially even unexpected internal systems for the appearance of these canaries.
* **Data Fingerprinting:**
    * **Concept:** Generate unique cryptographic hashes or more sophisticated signatures ("fingerprints") of sensitive data segments or entire documents before they are processed by an AI system, particularly if sent to an external provider.
    * **Implementation:** Monitor for the appearance of these exact fingerprints in unauthorized locations. This is most effective for detecting leakage of static, well-defined data elements.
* **Integration into AI Interaction Points:**
    * **Action:** Where feasible, integrate canary token generation and fingerprinting mechanisms at key data touchpoints within the AI system's architecture, such as API gateways, data ingestion pipelines, or custom plugins for LLM interactions. This facilitates systematic and continuous monitoring.
* **Automated Detection and Incident Response Workflow:**
    * **Action:** Develop or utilize automated systems to continuously scan for exposed canaries or fingerprints across relevant environments.
    * **Response:** Upon detection of a canary or fingerprint in an unauthorized location, the system must trigger an immediate alert to the Security Operations Center (SOC) or designated incident response team. This initiates a predefined incident response process, including:
        * Identifying the likely source and vector of the breach.
        * Determining the scope and potential impact of the leakage.
        * Implementing containment and remediation actions (e.g., isolating the affected service, notifying the third-party provider, revoking credentials, invoking contractual clauses for breach).

#### B. Detecting Unauthorized Training Data Extraction
* **Monitoring Guardrail Effectiveness:** Continuously monitor the performance and logs of input/output guardrails designed to prevent training data extraction. Investigate suspicious prompt patterns or model outputs that might indicate attempts to circumvent these protective measures.

#### C. Detecting AI Model Weight Leakage
* **Emerging Techniques:** Stay informed about and evaluate emerging research techniques for "fingerprinting" or watermarking AI models (e.g., knowledge injection methods like "Instructional Fingerprinting"). While many of these are still in the research phase, they may offer future capabilities for detecting unauthorized copies or uses of proprietary models if they are found in the wild.

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
