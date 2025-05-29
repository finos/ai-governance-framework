---
sequence: 7
title: Legal and Contractual Frameworks for AI Systems
layout: mitigation
doc-status: Draft
type: PREV
external_risks:
  - ISO-42001_2023_A-2-3   # Alignment with other organizational policies
  - ISO-42001_2023_A-10-2  # Allocating responsibilities
  - ISO-42001_2023_A-10-3  # Suppliers
  - ISO-42001_2023_A-8-5   # Information for interested parties
mitigates:
  - ri-1  # Information Leaked To Hosted Model
  - ri-20 # Reputational Risk
  - ri-22 # Regulatory Compliance and Oversight
  - ri-23 # Intellectual Property (IP) and Copyright

---

## Purpose

Robust legal and contractual agreements are essential for governing the development, procurement, deployment, and use of AI systems within a financial institution. This control ensures that comprehensive frameworks are established and maintained to manage risks, define responsibilities, protect data, and ensure compliance with legal and regulatory obligations when engaging with AI technology vendors, data providers, partners, and even in defining terms for end-users. These agreements must be thoroughly understood and actively managed to ensure adherence to all stipulated requirements.

---
## Scope of Legal and Contractual Agreements for AI

Legal and contractual considerations for AI systems extend across various relationships and arrangements, including but not limited to:

* **AI Technology Vendors:** Agreements with providers of AI platforms, models (including foundational models), tools, and related services (e.g., SaaS providers for inference, MLOps platforms).
* **Data Providers:** Contracts for acquiring or accessing external datasets used for training, testing, or operating AI systems.
* **Development Partners & Consultants:** Agreements with third parties involved in the custom development, integration, or enhancement of AI systems.
* **Cloud Service Providers (CSPs):** Terms governing the infrastructure and platform services used to host and operate AI systems.
* **Customers and End-Users:** Terms of service, privacy policies, and consent mechanisms related to the institution's AI-driven products and services.
* **Open Source Software (OSS):** Understanding and complying with licensing terms for any OSS components used within AI systems.

---
## Key Contractual Provisions and Considerations

When establishing legal agreements related to AI systems, financial institutions should ensure the following critical areas are addressed:

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

### 6. Data Sovereignty and Cross-Border Data Flows
* **Jurisdictional Requirements:** Ensure the vendor can meet any data sovereignty requirements (e.g., storing and processing EU citizen data within the EU).
* **Legal Data Transfers:** If data is transferred across borders, stipulate the legal mechanisms that will be used (e.g., Standard Contractual Clauses, adequacy decisions).

### 7. Audit, Compliance Verification, and Reporting
* **Right to Audit:** Secure rights to audit the vendor's compliance with contractual obligations, security controls, and regulatory requirements, or to receive third-party audit reports (e.g., SOC 2).
* **Compliance with Institutional Standards:** Ensure vendors can conform to the institution's tools, testing requirements, and standards for responsible and compliant AI.
* **Information for Interested Parties:** Define any obligations for the vendor to provide information necessary for the institution to meet its own reporting duties to regulators or other interested parties (as per ISO 42001 A.8.5).

### 8. Business Continuity, Disaster Recovery, and Exit Strategy
* **BCP/DR:** Ensure the vendor has adequate business continuity and disaster recovery plans for the AI services provided.
* **Termination and Data Retrieval/Deletion:** Clearly outline procedures for contract termination, including secure retrieval or certified deletion of institutional data, and any transition support.

---
## Internal Governance and Processes

Effective management of legal and contractual agreements for AI requires robust internal processes:

* **Cross-functional Collaboration:** Legal teams must work closely with procurement, information security, risk management, AI governance bodies, ethics committees, and relevant business units to identify requirements and assess risks.
* **Defining Requirements:** Internal stakeholders (e.g., Legal, AI Governance, Ethics Committee) must define the institution's requirements for data governance, privacy, security, explainability, and responsible AI, which then inform contractual negotiations.
* **Standardized Checklists and Templates:** Develop and use standardized checklists or contract templates for AI-related agreements to ensure key provisions are consistently addressed.
* **Review and Approval:** Implement a formal review and approval process for all AI-related contracts, involving all necessary stakeholders.
* **Contract Lifecycle Management:** Maintain a central repository of AI-related agreements and track key dates, obligations, and renewal/termination options.
* **Ongoing Monitoring:** Continuously monitor vendor compliance with contractual terms and periodically review the adequacy of existing agreements in light of evolving AI technologies, regulatory landscapes, and business needs.

---
## Importance and Benefits

* **Risk Mitigation:** Well-drafted contracts are crucial for mitigating legal, financial, operational, and reputational risks associated with AI systems, including data breaches (`ri-1`), IP infringement (`ri-23`), and regulatory non-compliance (`ri-22`).
* **Clear Accountability:** Establishes clear lines of responsibility between the institution and third parties, reducing ambiguity and potential for disputes.
* **Protection of Assets:** Safeguards the institution's data, intellectual property, and other assets.
* **Ensuring Compliance:** Helps ensure that the development and use of AI systems align with legal, regulatory, and ethical obligations.
* **Supporting Responsible AI:** Contractual requirements can mandate practices that support the responsible development and use of AI, aligning with the institution's values and policies.
* **Facilitating Trustworthy Partnerships:** Transparent and comprehensive agreements form the basis of strong, trustworthy relationships with AI vendors and partners.
