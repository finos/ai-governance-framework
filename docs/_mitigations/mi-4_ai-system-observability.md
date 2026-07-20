---
sequence: 4
title: AI System Observability
layout: mitigation
doc-status: Approved-Specification
type: DET
iso-42001_references:
  - A-6-2-6  # ISO 42001: AI system operation and monitoring
  - A-6-2-8  # ISO 42001: AI system recording of event logs
nist-sp-800-53r5_references:
  - ac-2   # AC-2 Account Management
  - au-2   # AU-2 Event Logging
  - au-3   # AU-3 Content Of Audit Records
  - au-6   # AU-6 Audit Record Review, Analysis, And Reporting
  - au-11  # AU-11 Audit Record Retention
  - au-12  # AU-12 Audit Record Generation
  - ca-7   # CA-7 Authorization
  - ir-4   # IR-4 Incident Handling
  - ir-5   # IR-5 Incident Monitoring
  - ra-10  # RA-10 Threat Hunting
  - si-4   # SI-4 System Monitoring
  - si-7   # SI-7 Software, Firmware, And Information Integrity
mitigates:
  - ri-1   # Information Leaked To Hosted Model
  - ri-5   # Foundation Model Versioning
  - ri-6   # Non-Deterministic Behaviour
  - ri-7   # Availability of Foundational Model
  - ri-14  # Inadequate System Alignment
  - ri-18  # Model Overreach / Expanded Use
  - ri-19  # Data Quality and Drift
  - ri-24  # Agent Action Authorization Bypass
  - ri-25  # Tool Chain Manipulation and Injection
  - ri-26  # MCP Server Supply Chain Compromise
  - ri-27  # Agent State Persistence Poisoning
  - ri-28  # Multi-Agent Trust Boundary Violations
  - ri-29  # Agent-Mediated Credential Discovery and Harvesting
related_mitigations:
  - mi-9   # AI System Alerting and Denial of Wallet (DoW) / Spend Monitoring
  - mi-11  # Human Feedback Loop for AI Systems
  - mi-1   # AI Data Leakage Prevention and Detection
iosco-supervisory-toolkit_references:
  - t2-recordkeeping  # Table 2: Recordkeeping & Audit Trail
  - t6-1              # Table 6.1: Documentation of AI Lifecycle Oversight
  - t6-3              # Table 6.3: Documentation of AI-Generated Outcomes
  - t6-5              # Table 6.5: Records on Incidents Relating to AI Products or Services
  - t7-adoption       # Table 7: AI Adoption Indicators
  - t7-nature         # Table 7: Nature and Use Cases of AI Systems
  - t7-performance    # Table 7: AI System Performance Indicators
---

## Purpose

AI System Observability encompasses the comprehensive collection, analysis, and monitoring of data about AI system behavior, performance, interactions, and outcomes. This control is essential for maintaining operational awareness, detecting anomalies, ensuring performance standards, and supporting incident response for AI-driven applications and services within a financial institution.

The goal is to provide deep visibility into all aspects of AI system operations—from user interactions and model behavior to resource utilization and security events—enabling proactive management, rapid issue resolution, and continuous improvement.

---

## Key Principles

Effective observability for AI systems should encompass multiple data types and monitoring layers:

* **Logging and Audit Trails:** Comprehensive capture of system events, user interactions, and operational data (as per ISO 42001 A.6.2.8).
* **Performance Monitoring:** Real-time tracking of system health, response times, throughput, and resource utilization.
* **Model Behavior Analysis:** Monitoring of AI model outputs, accuracy trends, and behavioral patterns.
* **Security Event Detection:** Identification of potential threats, unauthorized access attempts, and policy violations.
* **User Interaction Tracking:** Analysis of how users interact with AI systems and the quality of their experience.

---

## Implementation Guidance

Implementing a robust observability framework for AI systems involves several key steps:

### 1. Establish an Observability Strategy
* **Define Objectives:** Clearly articulate the goals for AI system observability based on business requirements, specific AI risks (e.g., fairness, security, operational resilience), compliance obligations, and operational support needs.
* **Identify Stakeholders:** Determine who needs access to observability data and insights (e.g., MLOps teams, data scientists, security analysts, risk managers, compliance officers) and their specific information requirements.

### 2. Identify Key Data Points for Logging and Monitoring
Comprehensive logging is fundamental (as per ISO 42001 A.6.2.8). Consider the following critical data points, ensuring collection respects data privacy and minimization principles:

* **User Interactions and Inputs:**
    * Complete user inputs (e.g., prompts, queries, uploaded files/data), where permissible and necessary for analysis.
    * System-generated queries to internal/external data sources (e.g., RAG database queries).
* **AI Model Behavior and Outputs:**
    * AI model outputs (e.g., predictions, classifications, generated text/images, decisions).
    * Associated confidence scores, uncertainty measures, or explainability data (if the model provides these).
    * Potentially key intermediate calculations or feature values, especially during debugging or fine-grained analysis of complex models.
* **API Traffic and System Interactions:**
    * All API calls related to the AI system (to and from the model, between microservices), including request/response payloads (or sanitized summaries), status codes, latencies, and authentication details.
    * Data flows and interactions crossing trust boundaries (e.g., with external data sources, third-party AI services, or different internal security zones).
* **Model Performance Metrics (as per ISO 42001 A.6.2.6):**
    * Task-specific accuracy metrics (e.g., precision, recall, F1-score, AUC for classification; MAE, RMSE for regression).
    * Model prediction drift, concept drift, and data drift indicators.
    * Inference latency, throughput (queries per second).
    * Error rates and types.
* **Resource Utilization and System Health:**
    * Consumption of computational resources (CPU, GPU, memory, disk I/O).
    * Network bandwidth utilization and latency.
    * Health status and operational logs from underlying infrastructure (servers, containers, orchestrators).
* **Security-Specific Events:**
    * Authentication and authorization events (both successes and failures).
    * Alerts and events from integrated security tools (e.g., AI Firewall, Data Leakage Prevention systems, intrusion detection systems).
    * Detected access control policy violations or attempts.
* **Versioning Information:**
    * Log the versions of AI models, datasets, key software libraries, and system components active during any given operation or event. This is crucial for diagnosing version-specific issues and understanding behavioral changes (e.g., model drift due to an update).

### 3. Implement Appropriate Tooling and Architecture
* **Logging Frameworks & Libraries:** Utilize robust logging libraries within AI applications and infrastructure components to generate structured and informative log data.
* **Centralized Log Management:** Aggregate logs from all components into a centralized system (e.g., SIEM, specialized log management platforms) to facilitate efficient searching, analysis, correlation, and long-term retention.
* **Monitoring and Visualization Platforms:** Employ dashboards and visualization tools to display key metrics, operational trends, system health, and security events in real-time or near real-time.
* **Alerting Mechanisms:** Configure automated alerts based on predefined thresholds, significant deviations from baselines, critical errors, or specific security event signatures (linking to concepts such as [MI-9 Alerting / DoW spend alert](#mi-9)).
* **Distributed Tracing:** For complex AI systems composed of multiple interacting microservices, implement distributed tracing capabilities to map end-to-end request flows, identify performance bottlenecks, and understand component dependencies.
* **Horizontal Monitoring Solutions:** Consider solutions that enable monitoring and correlation of activities across various inputs, outputs, and components simultaneously to achieve a holistic architectural view.

### 4. Establish Baselines and Implement Anomaly Detection
* **Baseline Definition:** Collect observability data over a sufficient period under normal operating conditions to establish baselines for key performance, behavioral, and resource utilization metrics.
* **Anomaly Detection Techniques:** Implement methods (ranging from statistical approaches to machine learning-based techniques) to automatically detect significant deviations from these established baselines. Anomalies can indicate performance issues, emerging security threats, data drift, or unexpected model behavior.

### 5. Define Data Retention and Archival Policies
* Formulate and implement clear policies for the retention and secure archival of observability data, balancing operational needs (e.g., troubleshooting, trend analysis), regulatory requirements (e.g., audit trails), and storage cost considerations.

### 6. Ensure Regular Review and Iteration
* Periodically review the effectiveness of the observability strategy, the relevance of data points being collected, the accuracy of alerting thresholds, and the utility of dashboards. Adapt and refine the observability setup as the AI system evolves, new risks are identified, or business and compliance requirements change.

### 7. Standardize Agent Telemetry on an Open Semantic Convention
The data points identified above are more portable and machine-comparable when emitted against a common, well-defined schema. Proprietary or per-vendor formats fragment agent telemetry, complicating cross-system correlation, migration, and independent review. Financial institutions should standardize agent telemetry on an open, vendor-neutral semantic convention. The OpenTelemetry GenAI semantic conventions, currently at `Development` status, are one recommended, non-mandatory baseline; an equivalent open convention is acceptable. Standardized telemetry is a detection and correlation *substrate*: it strengthens, but does not replace, the authoritative and durable audit record maintained under [MI-21 Agent Decision Audit and Explainability](#mi-21). A semantic convention defines what telemetry means and is distinct from the wire protocol used to transport it, such as OTLP.

* **Agent and Tool-Call Spans:**
    * **Action:** Instrument each logical agent invocation, model inference request, and agent tool execution using the applicable span convention, avoiding duplicate spans where another instrumentation covers the operation. Correlate spans in one trace where context can be propagated, or use span links or correlation identifiers for asynchronous work. Populate applicable attributes such as `gen_ai.operation.name`, `gen_ai.provider.name`, model and token-usage attributes, `gen_ai.tool.name`, and `gen_ai.tool.call.id` rather than relying solely on free-text logs.
    * **Rationale:** Correlated agent, inference, and tool-execution spans organize the "API Traffic and System Interactions" telemetry identified above into a queryable execution graph. Stable identifiers can join that graph to separately governed authorization and decision records maintained under [MI-21](#mi-21). These signals support detection and investigation of agent action authorization bypass (`ri-24`) and tool chain manipulation or injection (`ri-25`), but are not sufficient by themselves.
    * **Considerations:** Record available tool-execution context, including tool identity, call identifier, and applicable MCP, server, and network attributes. Correlate this telemetry with approved inventories and independent provenance or attestation data; a trace alone does not establish that supply-chain compromise (`ri-26`) or a multi-agent trust-boundary violation (`ri-28`) occurred.

* **Planning as a First-Class Operation:**
    * **Action:** Where instrumentation can reliably distinguish planning or task decomposition from generic reasoning or inference, emit an `INTERNAL` span with `gen_ai.operation.name` set to `plan`. Record the model call that generates the plan as its child; tool or task spans are typically correlated sibling operations under the enclosing `invoke_agent` span.
    * **Rationale:** A structural `plan` span records that a distinguishable planning phase occurred and situates it within the execution flow. It does not encode planned steps, map them to tool calls, or explain why the agent acted. Reconstructing why requires governed opt-in content on the relevant model span or separately maintained decision records correlated under [MI-21](#mi-21).
    * **Considerations:** Where planned-step content is captured or referenced under MI-21, compare it with executed actions over time; structural telemetry alone cannot perform this comparison. Correlate deviations with persistent-state or memory read/write telemetry as investigative signals for agent state persistence poisoning (`ri-27`) and model overreach or expanded use (`ri-18`).

* **Opt-In Content Attributes for Content-Free-by-Default Logging:**
    * **Action:** Adopt the schema's separation of structural telemetry (operations, token counts, latencies, tool identities, and status) from message content, treating the capture of prompts, completions, and tool arguments as an explicit, configurable opt-in rather than a default.
    * **Rationale:** This separation preserves structural traceability and supports content-independent anomaly detection while reducing default exposure of message and tool content. It supports balancing ISO 42001 A.6.2.8 against applicable data-minimization obligations, but institutions must still classify, minimize, redact, restrict, and govern all emitted attributes.
    * **Considerations:** Content-free telemetry does not provide complete detection coverage: detections that inspect prompt, output, tool-argument, or tool-result content require governed access to that content. Provide it only where justified, either through applicable opt-in attributes or a separately controlled store referenced from the trace, under [MI-21](#mi-21) access and retention controls.

* **Portable Export for Cross-Vendor Incident Forensics:**
    * **Action:** Export traces using an open protocol such as OTLP, distinct from the semantic convention, and propagate trace context or explicit correlation identifiers across participating components. Together, these controls allow compatible telemetry to be aggregated, correlated, and retained within institution-controlled systems.
    * **Rationale:** Portable export and institution-controlled retention reduce vendor dependency and support incident investigation after providers or tooling change. When correlated with records governed by [MI-21](#mi-21), traces can support cross-system investigation and evidence export. They provide signals relevant to credential discovery and harvesting (`ri-29`) only when the necessary tool, resource, content, and security telemetry is available.
    * **Considerations:** Apply the retention and secure-archival policies in Section 5, together with applicable integrity and access controls under [MI-21](#mi-21), to exported traces. Monitor export health and treat loss of required telemetry as a control failure.

* **Schema Versioning and Governance:**
    * **Action:** Pin a published release of the adopted convention or an immutable revision where no release exists. While OpenTelemetry GenAI remains `Development`, follow its upstream production-use guidance; any exception should require documented institutional risk acceptance, conformance testing, and change monitoring before deployment.
    * **Rationale:** The OpenTelemetry GenAI conventions are actively evolving and currently have `Development` status; attributes and operations may change. Recording the adopted revision makes historical telemetry interpretable, while comparability across revisions requires version-aware queries or tested migrations. This versioning governs telemetry and does not make it the authoritative audit record maintained under MI-21.
    * **Considerations:** Treat schema adoption as a living control—periodically reassess newly defined agent operations and attributes for inclusion, consistent with the review cadence in Section 6.

---
## Importance and Benefits

Comprehensive AI system observability provides numerous critical benefits for a financial institution:

* **Early Anomaly and Threat Detection:** Enables the proactive identification of unusual system behaviors, performance degradation, data drift, potential security breaches (e.g., unauthorized access, prompt injection attempts), or misuse that other specific controls might not explicitly cover.
* **Enhanced Security Incident Response:**  Provides vital data for thoroughly investigating security incidents, understanding attack vectors, assessing the scope and impact, performing root cause analysis, and informing remediation efforts.
* **Support for Audit, Compliance, and Regulatory Reporting:**  Generates essential, auditable records to demonstrate operational integrity, adherence to internal policies, and compliance with external regulatory requirements (e.g., event logging for accountability). 
* **Effective Performance Management and Optimization:**  Allows for continuous tracking of AI model performance (e.g., accuracy, latency, throughput) and resource utilization, facilitating the identification of bottlenecks and opportunities for optimization.
* **Proactive Management of Model and System Drift:**  Helps detect and diagnose changes in model behavior or overall system performance that may occur due to updates in models, system architecture, or shifts in underlying data distributions.
* **Improved SLA Adherence and Cost Control (FinOps):**  Provides the necessary data to monitor Service Level Agreement (SLA) compliance for AI services. Monitoring API call volumes, resource consumption (CPU, GPU), and frontend activity is crucial for managing operational costs and preventing "Denial of Wallet" attacks (`ri-7`). Alerts can be configured for when usage approaches predefined limits.
* **Detection and Understanding of System Misuse:**  Capturing inputs, including user prompts (while respecting privacy), can help identify patterns of external misuse, such as individuals or coordinated campaigns attempting to exploit the system or bypass established guardrails, even if individual attempts are initially blocked. 
* **Identification of Data Integrity and Leakage Issues:**  Aids in detecting potential data integrity problems, such as "data bleeding" (unintended information leakage between different user sessions) or unintended data persistence across sessions ("data pollution"). 
* **Crucial Support for Responsible AI Implementation:**  Logging and monitoring AI system behavior against specific metrics (e.g., related to fairness, bias, transparency, explainability) is necessary to provide ongoing assurance that responsible AI principles are being effectively implemented and maintained in practice. 
* **Informed Troubleshooting and Debugging:**  Offers deep insights into system operations and interactions, facilitating faster diagnosis and resolution of both technical and model-related issues.
* **Increased Trust and Transparency:**  Demonstrates robust control, understanding, and transparent operation of AI systems, fostering trust among users, stakeholders, and regulatory bodies.
