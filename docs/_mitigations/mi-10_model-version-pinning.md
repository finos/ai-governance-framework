---
sequence: 10
title: AI Model Version Pinning
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-6-2-3 # Documentation of AI system design and development
  - A-6-2-5 # AI system deployment
  - A-6-2-6 # AI system operation and monitoring
  - A-4-4   # Tooling resources
mitigates:
  - ri-5   # Instability in Foundation Model Behaviour
  - ri-6   # Non-Deterministic Behaviour
  - ri-11  # Lack of Foundation Model Versioning
---

## Purpose

Model Version Pinning is the deliberate practice of selecting and using a specific, fixed version of an Artificial Intelligence (AI) model within a production environment, rather than automatically adopting the latest available version. This is particularly crucial when utilizing externally sourced models, such as foundation models provided by third-party vendors. The primary goal of model version pinning is to **ensure operational stability, maintain predictable AI system behavior, and enable a controlled, risk-managed approach to adopting model updates.** This practice helps prevent unexpected disruptions, performance degradation, or the introduction of new vulnerabilities that might arise from unvetted changes in newer model versions.

---
## Key Principles

The implementation of model version pinning is guided by the following core principles:

* **Stability and Predictability:** Pinned model versions provide a consistent and known performance baseline. This is paramount for critical financial applications where unexpected shifts in AI behavior can have significant operational, financial, or reputational consequences (mitigating `ri-5`, `ri-6`).
* **Controlled Change Management:** Model pinning facilitates a deliberate and structured update strategy. It is not about indefinitely avoiding model upgrades but about enabling a rigorous process for evaluating, testing, and approving new versions before they are deployed into production (aligns with ISO 42001 A.6.2.6).
* **Risk Mitigation:** This practice prevents automatic exposure to potential regressions in performance, new or altered biases, increased non-deterministic behavior, or security vulnerabilities that might be present in newer, unvetted model versions (mitigating `ri-11`).
* **Supplier Accountability and Collaboration:** Effective model version pinning relies on AI model suppliers offering robust versioning support and clear communication. The organization must actively manage these supplier relationships to understand and plan for model updates.

---
## Implementation Guidance

Effective model version pinning involves both managing expectations with suppliers and establishing robust internal organizational practices:

### 1. Establishing Expectations with AI Model Suppliers
During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following:

* **Clear Versioning Scheme and Detailed Release Notes:**
    * **Requirement:** Suppliers must implement and communicate a clear, consistent versioning system (e.g., semantic versioning like MAJOR.MINOR.PATCH).
    * **Details:** Each new version should be accompanied by comprehensive release notes detailing changes in model architecture, training data, performance characteristics (e.g., accuracy, latency), known issues, potential behavioral shifts, and any deprecated features.
* **Advance Notification of New Versions and Deprecation:**
    * **Requirement:** Suppliers should provide proactive and sufficient advance notification regarding new model releases, planned timelines for deprecating older versions, and any critical security advisories or patches related to specific versions.
* **API Flexibility for Version Selection and Backward Compatibility:**
    * **Requirement:** For models accessed via APIs, suppliers must provide mechanisms that allow the institution to explicitly select and "pin" to a specific model version.
    * **Support:** Ensure options for backward compatibility or clearly defined migration paths, allowing the institution to continue using a pinned version for a reasonable period until it is ready to migrate. Production systems should not be forcibly updated by the supplier.
* **Support for Testing New Versions:**
    * **Requirement:** Ideally, suppliers should offer sandbox environments, trial access, or other mechanisms enabling the institution to thoroughly test new model versions with its own specific use cases, data, and integrations before committing to a production upgrade.
* **Transparency into Supplier's Testing Practices:**
    * **Due Diligence:** Inquire about the supplier's internal testing, validation, and quality assurance processes for new model releases to gauge their rigor.
* **Feedback Mechanisms:**
    * **Requirement:** Establish clear channels for providing feedback to the supplier on model performance, including any regressions, unexpected behaviors, or issues encountered with specific versions.

### 2. Internal Organizational Practices for Model Version Management
The institution must implement its own controls and procedures for managing AI model versions:

* **Explicit Version Selection and Pinning:**
    * **Action:** Formally decide, document, and implement the specific version of each AI model to be used in each production application or system. This "pinned" version becomes the approved baseline. (Supports ISO 42001 A.6.2.3, A.6.2.5)
* **Develop a Version Upgrade Strategy and Process:**
    * **Action:** Establish a structured internal process for the evaluation, testing, risk assessment, and approval of new AI model versions before they replace a currently pinned version. (Supports ISO 42001 A.6.2.6)
    * **Testing Scope:** This internal validation should include performance testing against established baselines, bias and fairness assessments, security reviews (for new vulnerabilities), integration testing, and user acceptance testing (UAT) where applicable.
* **Implement Controlled Deployment and Rollback Procedures:**
    * **Action:** Utilize robust deployment practices (e.g., blue/green deployments, canary releases) for introducing new model versions into production.
    * **Rollback Plan:** Always have a well-tested rollback plan to quickly revert to the previously pinned stable version if significant issues arise post-deployment of a new version. (Supports ISO 42001 A.6.2.5)
* **Continuous Monitoring of Pinned Models:**
    * **Action:** Monitor the performance, behavior, and security posture of pinned models in production. This includes tracking for:
        * Performance degradation or "drift" (which can occur even without a model change if input data characteristics evolve).
        * Newly discovered vulnerabilities or ethical concerns associated with the pinned version, based on ongoing threat intelligence and research.
* **Maintain an Inventory and Conduct Regular Audits:**
    * **Action:** Keep an up-to-date inventory of all deployed AI models, their specific pinned versions, and their business owners/applications.
    * **Audits:** Conduct regular audits to verify that production systems are consistently using the approved, pinned model versions.
* **Ensure Traceability and Comprehensive Logging:**
    * **Action:** Implement logging mechanisms to record which AI model version was used for any given transaction, decision, or output. This is crucial for debugging, incident analysis, and auditability.
    * **Metadata:** Where feasible, model outputs should include metadata indicating the model version used. (Supports ISO 42001 A.6.2.3)
* **Thorough Documentation:**
    * **Action:** Document the rationale for selecting a specific pinned version, the results of its initial validation testing, any subsequent evaluations of that version, and the strategic plan for future reviews or upgrades. (Supports ISO 42001 A.6.2.3) Also document tooling used in managing these versions (aligns with ISO 42001 A.4.4).

---
## Importance and Benefits

Adopting AI model version pinning offers significant advantages for financial institutions:

* **Enhanced Operational Stability:** Prevents unexpected disruptions and ensures consistent AI system behavior by isolating production environments from unvetted changes in upstream model provider updates (addresses `ri-5`, `ri-6`).
* **Predictable and Reliable Performance:** Guarantees that AI systems perform as expected based on previously tested and validated model versions, which is critical for user trust and dependable business processes.
* **Proactive Risk Management:** Allows for thorough assessment and mitigation of risks (e.g., new flaws, biases, security vulnerabilities, performance regressions) associated with new model versions before they impact production.
* **Structured Change Control:** Facilitates a systematic, auditable, and governed change management process for AI model updates, aligning with broader IT and enterprise risk management frameworks.
* **Improved Compliance and Auditability:** Provides clear documentation and traceability of which model version was active at any point in time, supporting regulatory inquiries, internal audits, and demonstrating control over AI systems (addresses `ri-11`).
* **Effective Incident Response:** Simplifies troubleshooting, root cause analysis, and incident response by providing a stable, known baseline for AI model behavior and allowing for quicker isolation of issues related to model changes.
