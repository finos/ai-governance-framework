---
sequence: 7
title: Legal and Contractual Frameworks for AI Systems
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-2-3   # ISO 42001: Alignment with other organizational policies
  - A-10-2  # ISO 42001: Allocating responsibilities
  - A-10-3  # ISO 42001: Suppliers
  - A-8-5   # ISO 42001: Information for interested parties
nist-sp-800-53r5_references:
  - ac-20  # AC-20 Use Of External Systems
  - ca-3  # CA-3 Information Exchange
  - ir-6  # IR-6 Incident Reporting
  - pm-30  # PM-30 Supply Chain Risk Management Strategy
  - ps-7  # PS-7 External Personnel Security
  - sa-4  # SA-4 Acquisition Process
  - sa-9  # SA-9 External System Services
  - sr-2  # SR-2 Supply Chain Risk Management Plan
  - sr-3  # SR-3 Supply Chain Controls And Processes
  - sr-5  # SR-5 Acquisition Strategies, Tools, And Methods
  - sr-8  # SR-8 Notification Agreements
mitigates:
  - ri-1   # Information Leaked To Hosted Model
  - ri-20  # Reputational Risk
  - ri-22  # Regulatory Compliance and Oversight
  - ri-23  # Intellectual Property (IP) and Copyright
related_mitigations:
  - mi-1   # AI Data Leakage Prevention and Detection
  - mi-10  # AI Model Version Pinning
  - mi-6   # Data Quality Classification Sensitivity
---

## Purpose

Robust legal and contractual agreements are essential for governing the development, procurement, deployment, and use of AI systems within a financial institution. This control ensures that comprehensive frameworks are established and maintained to manage risks, define responsibilities, protect data, and ensure compliance with legal and regulatory obligations when engaging with AI technology vendors, data providers, partners, and even in defining terms for end-users. These agreements must be thoroughly understood and actively managed to ensure adherence to all stipulated requirements.

---

## Key Principles

This control is about legal agreements between the SaaS inference provider and the organization. Those legal agreements not only have to exist, but have to be understood by the organization to make sure they comply with all requirements.

Requirements may include:
- Legal department would specify data governance, privacy and related requirements.
- Guidance from your AI governance body and ethics committee.
- Explainability requirements
- Conforming to tools and test requirements for addressing responsible and compliant AI.

Legal agreement should explain these questions:
- Can the SaaS vendor provide information on what data was used to train the models.
  - Indemnity protections: Does provider guarantee any indemnity protections, for example if copyrighted materials were used to train the models.
- Understand contractually what the SaaS provider does with any data you send them. The following are questions to consider:
  - Does SaaS provider persist prompts/completions? If they do persist, for how much time?
  - How data is safeguarded in that case? How is its privacy preserved?
  - How are they used? Are they used to further train models?
  - Is this data being shared with others? In what ways?
  - Does the provider have the ability to honor data sovereignty requirements of different jurisdictions? For example, if EU client/user data should be stored in EU.
- Privacy policy: Legal contract should clearly state how in what form data sent and prompts are used by the provider.
  - Does the usage of data meet regulatory requirements, like GDPR? What kind of consent is required? How consent is obtained and stored from users?
- Legal contract should state the policy about model versioning and changes, and inform clients to ensure that foundational models don't drift or change in unexpected ways.

---

## Implementation Guidance

### 1. Data Governance, Privacy, and Security
* **Data Usage and Processing:** Clearly define how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected. Specifically clarify:
    * Does the vendor persist or log prompts, inputs, and outputs? If so, for how long and for what purposes?
    * How is data safeguarded (encryption, access controls, segregation)? How is its privacy preserved?
    * Is the data used for further training of the vendor's models or for any other purposes?
    * Is data shared with any other third parties? Under what conditions?
* **Regulatory Compliance:** Ensure the agreement mandates compliance with all applicable data protection and privacy regulations (e.g., GDPR, CCPA). Address requirements for:
    * Lawful basis for processing.
    * Data subject rights management.
    * Consent mechanisms (how consent is obtained, recorded, and managed from users, if applicable).
* **Security Standards and Breach Notification:** Stipulate required information security standards, controls, and certifications. Include clear procedures and timelines for notifying the institution in the event of a data breach or security incident.

### 2. Intellectual Property (IP) Rights and Indemnification
* **Training Data Provenance:** If the vendor provides pre-trained models, seek information regarding the data used for training, particularly concerning third-party IP.
* **Indemnity Protections:** Does the vendor provide indemnification against claims of IP infringement (e.g., if copyrighted materials were used without authorization in model training)?
* **Ownership of Outputs and Derivatives:** Clearly define ownership of AI model outputs, any new IP created (e.g., custom models developed using vendor tools), and data derivatives.
* **Licensing Terms:** Ensure clarity on licensing terms for AI models, software, and tools, including scope of use, restrictions, and any dependencies.

### 3. Allocation of Responsibilities, Liabilities, and Risk
* **Clearly Defined Roles:** Explicitly allocate responsibilities for the AI system's lifecycle (development, deployment, operation, maintenance, decommissioning) between the institution and the third party (as per ISO 42001 A.10.2, A.10.3).
* **Liability and Warranties:** Address limitations of liability, warranties (e.g., regarding performance, accuracy), and any disclaimers. Ensure these are appropriate for the risk level of the AI application.

### 4. Model Transparency, Explainability, and Data Provenance
* **Transparency into Model Operation:** To the extent feasible and permissible, seek rights to understand the AI model's general architecture, methodologies, and key operational parameters.
* **Explainability Support:** If the AI system is used for decisions impacting customers or for regulatory purposes, ensure the contract supports the institution's explainability requirements.
* **Information on Training Data:** As appropriate, seek information on the characteristics and sources of data used to train models provided by vendors.

### 5. Service Levels, Performance, and Model Management
* **Service Level Agreements (SLAs):** Define clear SLAs for AI system availability, performance metrics (e.g., response times, accuracy levels), and support responsiveness.
* **Model Versioning and Change Management:** The contract should specify the vendor's policy on model versioning, updates, and changes. Ensure timely notification of any changes that could impact model performance, behavior ("drift"), or compliance, allowing the institution to re-validate.
* **Maintenance and Support:** Outline provisions for ongoing maintenance, technical support, and updates.

---

## Importance and Benefits

* **Risk Mitigation:** Well-drafted contracts mitigate legal, financial, operational, and reputational risks associated with AI systems
* **Clear Accountability:** Establishes clear lines of responsibility between the institution and third parties
* **Asset Protection:** Safeguards the institution's data, intellectual property, and other assets
* **Compliance Assurance:** Ensures AI system development and use align with legal, regulatory, and ethical obligations
* **Responsible AI Support:** Contractual requirements mandate practices supporting responsible AI development
* **Partnership Foundation:** Transparent agreements form the basis of trustworthy relationships with AI vendors
