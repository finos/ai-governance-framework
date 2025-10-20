# FINOS AI Governance Framework

This document contains the atomized controls for the FINOS AI Governance Framework (AIGF).

## FINOS-PREV-002-001: Including Necessary Data for Business Function

**Section:** Key Principles

**Responsible Party:** System Owners

**Control Text:** System owners must include only the data necessary for the intended business function in AI systems for effective data filtering from external knowledge bases.

**Source Text:** Principle of Least Exposure: Only include data in AI systems that is necessary for the intended business function, and ensure that even this data is appropriately de-identified or masked when possible.

---

## FINOS-PREV-002-002: Ensuring Data De-identification or Masking

**Section:** Key Principles

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that data included in AI systems for the intended business function is appropriately de-identified or masked when possible for effective data filtering from external knowledge bases.

**Source Text:** Principle of Least Exposure: Only include data in AI systems that is necessary for the intended business function, and ensure that even this data is appropriately de-identified or masked when possible.

---

## FINOS-PREV-002-003: Maintaining Documentation and Audit Trails for Data Filtering

**Section:** Key Principles

**Responsible Party:** System Owners

**Control Text:** System owners must maintain clear documentation and audit trails of what data filtering from external knowledge bases processes have been applied and why. 

**Source Text:** Auditability and Transparency: Maintain clear documentation and audit trails of what data filtering processes have been applied and why (supports ISO 42001 A.7.2).

---

## FINOS-PREV-002-004: Reviewing and Cleansing Internal Information Prior to Ingestion

**Section:** Implementation Guidance

**Subsection:** Pre-Processing Review and Cleansing 

**Responsible Party:** System Owners

**Control Text:** System owners must put any information from internal knowledge sources through a thorough review and cleansing process before it is ingested by an AI system (whether for training, vector database population, or real-time retrieval). 

**Source Text:** Process: Before any information from internal knowledge sources is ingested by an AI system (whether for training, vector database population, or real-time retrieval), it must undergo a thorough review and cleansing process.

---

## FINOS-PREV-002-005: Identifying and Removing or Anonymizing Senstive Details

**Section:** Implementation Guidance

**Subsection:** Pre-Processing Review and Cleansing

**Responsible Party:** System Owners

**Control Text:** System owners must identify and remove or appropriately anonymize sensitive details to ensure that data fed into the AI system is free from information that could pose a security or privacy risk if inadvertently exposed.

**Source Text:** Objective: Identify and remove or appropriately anonymize sensitive details to ensure that data fed into the AI system is free from information that could pose a security or privacy risk if inadvertently exposed.

---

## FINOS-PREV-002-006: Filtering PII

**Section:** Implementation Guidance

**Subsection:** Categories of Data to Target for Filtering

**Responsible Party:** System Owners

**Control Text:** System owners must target for filtering personal identifiable information (PII) from internal knowledge sources before ingestion, including names, contact details, financial account numbers, employee IDs, social security numbers, addresses, and other personal identifiers.

**Source Text:** Personally Identifiable Information (PII): Names, contact details, financial account numbers, employee IDs, social security numbers, addresses, and other personal identifiers.

---

## FINOS-PREV-002-007: Filtering Proprietary Business Information

**Section:** Implementation Guidance

**Subsection:** Categories of Data to Target for Filtering

**Responsible Party:** System Owners

**Control Text:** System owners must target for filtering proprietary business information from internal knowledge sources before ingestion, including trade secrets, intellectual property, unreleased financial results, strategic plans, merger and acquisition details, customer lists, pricing strategies, and competitive intelligence.

**Source Text:** Proprietary Business Information: Trade secrets, intellectual property, unreleased financial results, strategic plans, merger and acquisition details, customer lists, pricing strategies, and competitive intelligence.

---

## FINOS-PREV-002-008: Filtering Sensitive Internal Operational Data

**Section:** Implementation Guidance

**Subsection:** Categories of Data to Target for Filtering

**Responsible Party:** System Owners

**Control Text:** System owners must target for filtering sensitive internal operational data from internal knowledge sources before ingestion, security configurations, system architecture details, access credentials, internal process documentation not intended for broader access, incident reports, and audit findings.

**Source Text:** Sensitive Internal Operational Data: Security configurations, system architecture details, access credentials, internal process documentation not intended for broader access, incident reports, and audit findings.

---

## FINOS-PREV-002-009: Filtering Confidential Customer Data

**Section:** Implementation Guidance

**Subsection:** Categories of Data to Target for Filtering 

**Responsible Party:** System Owners

**Control Text:** System owners must target for filtering confidential customer data from internal knowledge sources before ingestion, including account information, transaction details, credit scores, loan applications, investment portfolios, and personal financial information. 

**Source Text:** Confidential Customer Data: Account information, transaction details, credit scores, loan applications, investment portfolios, and personal financial information.

---

## FINOS-PREV-002-010: Filtering Regulator or Compliance-sensitive Information

**Section:** Implementation Guidance

**Subsection:** Categories of Data to Target for Filtering 

**Responsible Party:** System Owners

**Control Text:** System owners must target for filtering regulatory or compliance-sensitive information from internal knowledge sources before ingestion, including legal advice, regulatory correspondence, compliance violations, investigation details, and privileged communications. 

**Source Text:** Regulatory or Compliance-Sensitive Information: Legal advice, regulatory correspondence, compliance violations, investigation details, and privileged communications.

---

## FINOS-PREV-002-011: Data Masking Before Ingestion

**Section:** Implementation Guidance

**Subsection:** Filtering and Anonymization Methods 

**Responsible Party:** System Owners

**Control Text:** System owners must filter and anonymize internal knowledge sources before ingestion, including data masking by replacing sensitive data fields with anonymized equivalents (e.g., “Employee12345” instead of “John Smith”).

**Source Text:** Data Masking: Replace sensitive data fields with anonymized equivalents (e.g., “Employee12345” instead of “John Smith”).

---

## FINOS-PREV-002-012: Redacting Sensitive Data Before Ingestion

**Section:** Implementation Guidance

**Subsection:** Filtering and Anonymization Methods 

**Responsible Party:** System Owners

**Control Text:** System owners must filter and anonymize internal knowledge sources before ingestion, including redaction by removing entire sections of documents that contain sensitive information.

**Source Text:** Redaction: Remove entire sections of documents that contain sensitive information.

---

## FINOS-PREV-002-013: Generalizing Specific Information Before Ingestion

**Section:** Implementation Guidance

**Subsection:** Filtering and Anonymization Methods 

**Responsible Party:** System Owners

**Control Text:** System owners must filter and anonymize internal knowledge sources before ingestion, including generalization by replacing specific information with more general categories (e.g. "Major metropolitian area" instead of "New York City").

**Source Text:** Generalization: Replace specific information with more general categories (e.g., “Major metropolitan area” instead of “New York City”).

---

## FINOS-PREV-002-014: Tokenizing Sensitive Data Before Ingestion

**Section:** Implementation Guidance

**Subsection:** Filtering and Anonymization Methods 

**Responsible Party:** System Owners

**Control Text:** System owners must filter and anonymize internal knowledge sources before ingestion, including tokenization by replacing sensitive data with non-sensitive tokens that can be mapped back to the original data only through a secure, seperate system. 

**Source Text:** Tokenization: Replace sensitive data with non-sensitive tokens that can be mapped back to the original data only through a secure, separate system.

---

## FINOS-PREV-002-015: Generating Synthetic Data 

**Section:** Implementation Guidance

**Subsection:** Filtering and Anonymization Methods 

**Responsible Party:** System Owners

**Control Text:** System owners must filter and anonymize internal knowledge sources before ingestion, including synthetic data generation by generating synthentic data for training purposes that maintains statistical properties of the original data without exposing actual senstive information.

**Source Text:** Synthetic Data Generation: For training purposes, generate synthetic data that maintains statistical properties of the original data without exposing actual sensitive information.

---

## FINOS-PREV-002-016: Implementing Isolated Systems or Environments for Sensitive Resources 

**Section:** Implementation Guidance

**Subsection:** Isolated AI Systems for Critical Data

**Responsible Party:** System Owners

**Control Text:** System owners must implement separate, isolated AI systems or environments for datasets or knowledge sources containing exceptionally sensitive information that cannot be adequately protected through standard cleansing or anonymization techniques.

**Source Text:** Concept: For datasets or knowledge sources containing exceptionally sensitive information that cannot be adequately protected through standard cleansing or anonymization techniques, implement separate, isolated AI systems or environments.

---

## FINOS-PREV-002-017: Creating Isolated AI Models and Data Stores for Exceptionally Sensitive Information

**Section:** Implementation Guidance

**Subsection:** Isolated AI Systems for Critical Data

**Responsible Party:** System Owners

**Control Text:** System owners must create distinct AI models and associated data stores (e.g., separate vector databases for RAG systems) with much stricter access controls, enhanced encryption, and limited network connectivity for datasets or knowledge sources containing exceptionally sensitive information that cannot be adequately protected through standard cleansing or anonymization techniques.

**Source Text:** Implementation: Create distinct AI models and associated data stores (e.g., separate vector databases for RAG systems) with much stricter access controls, enhanced encryption, and limited network connectivity.

---

## FINOS-PREV-002-018: Restricting Access to Highly Sensitive Data and Processes

**Section:** Implementation Guidance

**Subsection:** Isolated AI Systems for Critical Data

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that only explicitly authorized personnel or tightly controlled AI processes can interact with highly sensitive data, minimizing the risk of broader exposure for datasets or knowledge sources containing exceptionally sensitive information that cannot be adequately protected through standard cleansing or anonymization techniques.

**Source Text:** Benefit: Ensures that only explicitly authorized personnel or tightly controlled AI processes can interact with highly sensitive data, minimizing the risk of broader exposure.

---

## FINOS-PREV-002-019: Segmenting Data and System Access by Defined Access Domains

**Section:** Implementation Guidance

**Subsection:** Access Domain-Based Segregation

**Responsible Party:** System Owners

**Control Text:** System owners must segment data and AI system access based on clearly defined access domains that mirror the organization's existing data classification and access control structures. 

**Source Text:** Strategy: Segment data and AI system access based on clearly defined access domains that mirror the organization’s existing data classification and access control structures.

---

## FINOS-PREV-002-020: Restricting AI System Access by User Group or Business Unit

**Section:** Implementation Guidance

**Subsection:** Access Domain-Based Segregation

**Responsible Party:** System Owners

**Control Text:** System owners must segment data and AI system access such that different user groups or business units have access only to AI instances that contain data appropriate to their clearance level and business need.

**Source Text:** Implementation: Different user groups or business units may have access only to AI instances that contain data appropriate to their clearance level and business need.

---

## FINOS-PREV-002-021: Monitoring and Filtering AI System Outputs

**Section:** Implementation Guidance

**Subsection:** Response Filtering and Validation

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that responses and information generated by the AI system are monitored and filtered before being presented to users or integrated into other systems as an additional layer of defense.

**Source Text:** Rationale: As an additional layer of defense, responses and information generated by the AI system should be monitored and filtered before being presented to users or integrated into other systems.

---

## FINOS-PREV-002-022: Detecting and Removing Sensitive Data from AI Outputs

**Section:** Implementation Guidance

**Subsection:** Response Filtering and Validation

**Responsible Party:** System Owners

**Control Text:** System owners must detect and remove any sensitive data that might have inadvertently bypassed the initial input cleansing stages or was unexpectedly reconstructed or inferred by the AI model during its processing.

**Source Text:** Function: Acts as a crucial safety net to detect and remove any sensitive data that might have inadvertently bypassed the initial input cleansing stages or was unexpectedly reconstructed or inferred by the AI model during its processing.

---

## FINOS-PREV-002-023: Applying Consistent Filtering Rules to AI Outputs

**Section:** Implementation Guidance

**Subsection:** Response Filtering and Validation

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that output filtering applies the same principles and rules used for sanitizing input data, checking for PII, propreitaty information, and other sensitive content. 

**Source Text:** Scope: Output filtering should apply the same principles and rules used for sanitizing input data, checking for PII, proprietary information, and other sensitive content.

---

## FINOS-PREV-002-024: Implementing Output Filtering Based on Context and Authorization

**Section:** Implementation Guidance

**Subsection:** Contextual Output Analysis

**Responsible Party:** System Owners

**Control Text:** System owners must implement intelligent filtering that considers the context of the user’s query and their authorization level to determine what information should be included in the response.

**Source Text:** Dynamic Filtering: Implement intelligent filtering that considers the context of the user’s query and their authorization level to determine what information should be included in the response.

---

## FINOS-PREV-002-025: Assessing and Flagging Uncertain or Sensitive AI Outputs for Human Review

**Section:** Implementation Guidance

**Subsection:** Contextual Output Analysis

**Responsible Party:** System Owners

**Control Text:** System owners must implement systems that assess the confidence level of the AI’s output and flag responses that may contain uncertain or potentially sensitive information for human review, where technically feasible.

**Source Text:** Confidence Scoring: Where technically feasible, implement systems that assess the confidence level of the AI’s output and flag responses that may contain uncertain or potentially sensitive information for human review.

---

## FINOS-PREV-002-026: Preserving and Replicating Source System Access Controls

**Section:** Implementation Guidance

**Subsection:** Integration with Source System Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners must design the AI system to respect and replicate the original access control permissions from source systems, when possible. 

**Source Text:** Respect Original Permissions: When possible, design the AI system to respect and replicate the original access control permissions from source systems (see MI-16 Preserving Access Controls).

---

## FINOS-PREV-002-027: Querying Source Systems Dynamically in Real-Time RAG Systems

**Section:** Implementation Guidance

**Subsection:** Integration with Source System Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners using real-time RAG systems may consider querying source systems dynamically while respecting user permissions, rather than pre-processing all data indiscriminately.

**Source Text:** Dynamic Source Querying: For real-time RAG systems, consider querying source systems dynamically while respecting user permissions, rather than pre-processing all data indiscriminately.

---

## FINOS-PREV-002-028: Auditing Effectiveness of Data Filtering Processes

**Section:** Implementation Guidance

**Subsection:** Monitoring and Continuous Improvement

**Responsible Party:** System Owners

**Control Text:** System owners must periodically audit the effectiveness of data filtering processes by sampling processed data and checking for any sensitive information that may have been missed.

**Source Text:** Regular Review of Filtering Effectiveness: Periodically audit the effectiveness of data filtering processes by sampling processed data and checking for any sensitive information that may have been missed.

---

## FINOS-PREV-002-029: Establishing Feedback Mechanisms for Reporting Data Exposure

**Section:** Implementation Guidance

**Subsection:** Monitoring and Continuous Improvement

**Responsible Party:** System Owners

**Control Text:** System owners must establish mechanisms for users and reviewers to report instances where sensitive information may have been inappropriately exposed, using this feedback to improve filtering algorithms and processes.

**Source Text:** Feedback Loop Integration: Establish mechanisms for users and reviewers to report instances where sensitive information may have been inappropriately exposed, using this feedback to improve filtering algorithms and processes.

---

## FINOS-PREV-002-030: Updating Filtering Strategies Against Emerging Data Leakage Vectors

**Section:** Implementation Guidance

**Subsection:** Monitoring and Continuous Improvement

**Responsible Party:** System Owners

**Control Text:** System owners must stay informed about new types of data leakage vectors and attack techniques that might affect AI systems, and update filtering strategies accordingly.

**Source Text:** Threat Intelligence Integration: Stay informed about new types of data leakage vectors and attack techniques that might affect AI systems, and update filtering strategies accordingly.

---

## FINOS-PREV-003-001: Verifying Model Output Format 

**Section:** Key Principles

**Subsection:** AI Model Output (LLM Responses)

**Responsible Party:** System Owners

**Control Text:** System owners must verify that the model’s outputs conform to expected formats (e.g., structured JSON) to detect and block undesired behaviors or potential threats, including deviations that may indicate compromise or manipulation.

**Source Text:** Format Conformance: Verify that the model’s output adheres to expected formats (e.g., structured JSON). Deviations, such as responses in an unexpected language, can be an indicator of compromise or manipulation.

---

## FINOS-PREV-003-002: Identifying Patterns of Malicious Input Resistance

**Section:** Key Principles

**Subsection:** AI Model Output (LLM Responses)

**Responsible Party:** System Owners

**Control Text:** System owners must identify known patterns in model behavior that indicate the LLM is resisting malicious inputs or attempted abuse, as such patterns can signal an ongoing attack probing for vulnerabilities in the system’s protective measures (guardrails).

**Source Text:** Evasion Detection: Identify known patterns that indicate the LLM is resisting malicious inputs or attempted abuse. Such patterns, even if input filtering was partially bypassed, can signal an ongoing attack probing for vulnerabilities in the system’s protective measures (guardrails).

---

## FINOS-PREV-003-003: Preventing Re-identification of Anonymized Data in Outputs

**Section:** Key Principles

**Subsection:** AI Model Output (LLM Responses)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that data anonymized for processing (e.g., user queries) is not inadvertently re-identified in the output in a way that exposes sensitive information. 

**Source Text:** Secure Data Handling: Ensure that data anonymized for processing (e.g., user queries) is not inadvertently re-identified in the output in a way that exposes sensitive information. If re-identification is a necessary function, it must be handled securely.

---

## FINOS-PREV-003-004: Securing Re-identification Processes for Sensitive Data

**Section:** Key Principles

**Subsection:** AI Model Output (LLM Responses)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that data anonymized for processing is handled securely in the event that re-identification in the output is done so securely to prevent exposure of sensitive information. 

**Source Text:** Secure Data Handling: Ensure that data anonymized for processing (e.g., user queries) is not inadvertently re-identified in the output in a way that exposes sensitive information. If re-identification is a necessary function, it must be handled securely.

---

## FINOS-PREV-003-005: Pre-processing and Filtering Data for RAG Embedding Creation

**Section:** Implementation Guidance

**Subsection:** Key Areas for Monitoring and Filtering

**Responsible Party:** System Owners

**Control Text:** System owners using RAG may often find it more practical to pre-process and filter data for RAG systems before sending it for external embedding creation, though they may also consider in-line filters for real-time checks.

**Source Text:** RAG Database Security:
While it’s often more practical to pre-process and filter data for RAG systems before sending it for external embedding creation, organizations might also consider in-line filters for real-time checks.

---

## FINOS-PREV-003-006: Implementing Data Filtering and Sanitization Before Embedding and Storing Data 

**Section:** Implementation Guidance

**Subsection:** Key Areas for Monitoring and Filtering

**Responsible Party:** System Owners

**Control Text:** System owners must implement thorough data filtering and sanitization before internal information is transformed into specialized “embedding” formats (numerical representations of text) and stored in AI-optimized “vector databases” for rapid retrieval, to mitigate the loss of visibility and control associated with inspecting or managing embedded data using traditional security tools.

**Source Text:** Consideration: Once internal information is converted into specialized ‘embedding’ formats (numerical representations of text) and stored in AI-optimized ‘vector databases’ for rapid retrieval, the data becomes largely opaque to traditional security tools. It’s challenging to directly inspect this embedded data, apply retroactive filters, or implement granular access controls within the vector database itself in the same way one might with standard databases. This inherent characteristic underscores the critical need for thorough data filtering and sanitization before the information is transformed into embeddings and ingested into such systems.

---

## FINOS-PREV-003-007: Enhancing Filtering with Static and Advanced LLM-based Techniques

**Section:** Implementation Guidance

**Subsection:** Key Areas for Monitoring and Filtering

**Responsible Party:** System Owners

**Control Text:** System owners may augment static filters (e.g., those based on regular expressions or keyword blocklists) that identify well-defined patterns such as email addresses, specific company terms, or known malicious code signatures with more advanced techniques, such as using an "LLM as a judge," to detect nuanced issues including generic private information, subtle prompt injection attacks designed to evade detection, or sophisticated offensive language.

**Source Text:** Filtering Efficacy:
Static filters (e.g., based on regular expressions or keyword blocklists) are effective for well-defined patterns like email addresses, specific company terms, or known malicious code signatures. However, they are less effective at identifying more nuanced issues such as generic private information, subtle Prompt Injection attacks (which are designed to evade detection), or sophisticated offensive language. This limitation often leads to the use of more advanced techniques, such as an “LLM as a judge” (explained below).

---

## FINOS-PREV-003-008: Monitoring and Filtering for Streaming Responses

**Section:** Implementation Guidance

**Subsection:** Key Areas for Monitoring and Filtering

**Responsible Party:** System Owners

**Control Text:** System owners must implement monitoring and filtering mechanisms for AI models that deliver streaming responses (where the model outputs content word-by-word) to improve user experience through immediate feedback.

**Source Text:** Streaming Outputs: Streaming responses (where the AI model delivers output word-by-word) significantly improves user experience by providing immediate feedback.

---

## FINOS-PREV-003-009: Assessing Risks of Output Filtering in Streaming Responses

**Section:** Implementation Guidance

**Subsection:** Key Areas for Monitoring and Filtering

**Responsible Party:** System Owners

**Control Text:** System owners using streaming outputs must consider that implementing output filtering can be challenging with streaming. To comprehensively filter a response, the entire output often needs to be assembled first. This can negate the benefits of streaming or, if filtering is done on partial streams, risk exposing unfiltered sensitive information before it’s detected and redacted.

**Source Text:** Trade-off: However, implementing output filtering can be challenging with streaming. To comprehensively filter a response, the entire output often needs to be assembled first. This can negate the benefits of streaming or, if filtering is done on partial streams, risk exposing unfiltered sensitive information before it’s detected and redacted.

---

## FINOS-PREV-003-010: Implementing On-the-Fly Detection and Cancellation for Streaming Outputs

**Section:** Implementation Guidance

**Subsection:** Key Areas for Monitoring and Filtering

**Responsible Party:** System Owners

**Control Text:** System owners using streaming outputs may use an approach to stream the response while performing on-the-fly detection. If an issue is found, the streamed output is immediately cancelled and removed. This requires careful risk assessment based on the sensitivity of the information and the user base, as there’s a brief window of potential exposure.

**Source Text:** Alternative: An approach is to stream the response while performing on-the-fly detection. If an issue is found, the streamed output is immediately cancelled and removed. This requires careful risk assessment based on the sensitivity of the information and the user base, as there’s a brief window of potential exposure.

---

## FINOS-PREV-003-011: Applying Basic Static Filtering 

**Section:** Implementation Guidance

**Subsection:** Remediation Techniques

**Responsible Party:** System Owners

**Control Text:** System owners must implement basic filtering mechanisms, including simple static checks that use blocklists (denylists) and regular expressions to detect rudimentary attacks or policy violations.

**Source Text:** Basic Filters: Simple static checks using blocklists (denylists) and regular expressions can detect rudimentary attacks or policy violations.

---

## FINOS-PREV-003-012: Understanding Limitations of System Prompts as Security Controls

**Section:** Implementation Guidance

**Subsection:** Remediation Techniques

**Responsible Party:** System Owners

**Control Text:** System owners using system prompts must be cautioned that while system prompts can instruct an LLM on what to avoid, they are generally not a robust security control. Attackers can often bypass these instructions or even trick the LLM into revealing the prompt itself, thereby exposing the filtering logic. 

**Source Text:** System Prompts (Caution Advised): While system prompts can instruct an LLM on what to avoid, they are generally not a robust security control. Attackers can often bypass these instructions or even trick the LLM into revealing the prompt itself, thereby exposing the filtering logic.

---

## FINOS-PREV-003-013: Using LLM Judges for Risk Analysis and Filtering

**Section:** Implementation Guidance

**Subsection:** Remediation Techniques

**Responsible Party:** System Owners

**Control Text:** System owners may implement an "LLM judge" to analyze user queries and the primary LLM's responses risks such as prompt injection, abuse, hate speech, or data leakage, using a SaaS product or locally hosted model. 



**Source Text:** LLM as a Judge:
A more advanced and increasingly common technique involves using a secondary, specialized LLM (an “LLM judge”) to analyze user queries and the primary LLM’s responses. This judge model is specifically trained to categorize inputs/outputs for various risks (e.g., prompt injection, abuse, hate speech, data leakage) rather than to generate user-facing answers.
This can be implemented using a SaaS product or a locally hosted model, though the latter incurs computational costs for each evaluation.
For highly sensitive or organization-specific information, consider training a custom LLM judge tailored to recognize proprietary data types or unique risk categories.

---

## FINOS-PREV-003-014: Using Custom LLM Judges for Sensitive Information

**Section:** Implementation Guidance

**Subsection:** Remediation Techniques

**Responsible Party:** System Owners

**Control Text:** System owners may train a custom LLM judge tailored to recognize proprietary data types or unique risk categories for highly sensitive or organization-specific information. 


**Source Text:** LLM as a Judge:
A more advanced and increasingly common technique involves using a secondary, specialized LLM (an “LLM judge”) to analyze user queries and the primary LLM’s responses. This judge model is specifically trained to categorize inputs/outputs for various risks (e.g., prompt injection, abuse, hate speech, data leakage) rather than to generate user-facing answers.
This can be implemented using a SaaS product or a locally hosted model, though the latter incurs computational costs for each evaluation.
For highly sensitive or organization-specific information, consider training a custom LLM judge tailored to recognize proprietary data types or unique risk categories.

---

## FINOS-PREV-003-015: Implementing User Reporting Mechanisms for Problematic AI Responses

**Section:** Implementation Guidance

**Subsection:** Remediation Techniques

**Responsible Party:** System Owners

**Control Text:** System owners must implement a system that allows users to easily report problematic AI responses, providing a valuable complementary control to verify the effectiveness of automated guardrails and identify new evasion techniques.

**Source Text:** Human Feedback Loop: Implementing a system where users can easily report problematic AI responses provides a valuable complementary control. This feedback helps verify the effectiveness of automated guardrails and identify new evasion techniques.

---

## FINOS-PREV-003-016: Implementing API Monitoring and Security Solutions

**Section:** Implementation Guidance

**Subsection:** Additional Considerations

**Responsible Party:** System Owners

**Control Text:** System owners must implement a comprehensive API monitoring and security solution to enhance overall system security, such as a security proxy to enforce encrypted communication (e.g., TLS) between all AI system components.

**Source Text:** API Security and Observability: Implementing a comprehensive API monitoring and security solution offers benefits beyond AI-specific threats, enhancing overall system security. For example, a security proxy can enforce encrypted communication (e.g., TLS) between all AI system components.

---

## FINOS-PREV-003-017: Maintaining Logs for Behavior and Anomaly Detection

**Section:** Implementation Guidance

**Subsection:** Additional Considerations

**Responsible Party:** System Owners

**Control Text:** System owners must maintain detailed logs of interactions (queries, responses, filter actions) to aid in understanding user behavior, system performance, and to allow for the detection of sophisticated attacks or anomalies that may only be apparent through statistical analysis of logged data (e.g., coordinated denial-of-service attempts).

**Source Text:** Logging and Analysis: Detailed logging of interactions (queries, responses, filter actions) is essential. It aids in understanding user behavior, system performance, and allows for the detection of sophisticated attacks or anomalies that may only be apparent through statistical analysis of logged data (e.g., coordinated denial-of-service attempts).

---

## FINOS-PREV-005-001: Collaborating with Stakeholders to Define and Document Acceptance Criteria

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must collaborate with all relevant stakeholders – including business owners, end-users, AI development teams, operations, risk management, compliance, and information security – to define, document, and agree upon clear, measurable, and testable acceptance criteria, before testing begins. 

**Source Text:** Action: Before testing begins, collaborate with all relevant stakeholders – including business owners, end-users, AI development teams, operations, risk management, compliance, and information security – to define, document, and agree upon clear, measurable, and testable acceptance criteria.

---

## FINOS-PREV-005-002: Ensuring Accurate and Reliable Performance

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that the AI system accurately and reliably performs the specific tasks and functions it was designed for (e.g., verifying accuracy rates for fraud detection models, precision in credit risk assessments, or effectiveness in customer query resolution) to maintain functional integrity.

**Source Text:** Functional Integrity: Does the AI system accurately and reliably perform the specific tasks and functions it was designed for? (e.g., verify accuracy rates for fraud detection models, precision in credit risk assessments, or effectiveness in customer query resolution).

---

## FINOS-PREV-005-003: Ensuring Operational Efficiency and Scalability 

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that the system operates efficiently within defined performance benchmarks (e.g., processing speed, response times, resource utilization) and can scale as anticipated to maintain functional integrity.

**Source Text:** Performance and Scalability: Does the system operate efficiently within defined performance benchmarks (e.g., processing speed, response times, resource utilization) and can it scale as anticipated?

---

## FINOS-PREV-005-004: Ensuring Robust Data Protections and Access Controls

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that robust data protection measures and access controls are implemented according to the principle of least privilege.

**Source Text:** Security and Access Control: Are data protection measures robust, access controls correctly implemented according to the principle of least privilege, and are audit trails comprehensive and accurate?

---

## nan: Ensuring Accurate Audit Trails

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure audit trails are comprehensive and accurate to maintain functional integrity.

**Source Text:** Security and Access Control: Are data protection measures robust, access controls correctly implemented according to the principle of least privilege, and are audit trails comprehensive and accurate?

---

## FINOS-PREV-005-005: Ensuring Fiar, Transparent, and Explainable Outputs 

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that AI system outputs influencing critical decisions or customer interactions align with the institution’s commitment to fairness, transparency, and explainability by verifying bias detection and mitigation measures and ensuring that outcomes are justifiable.

**Source Text:** Ethical AI Principles & Responsible AI: For AI systems, especially those influencing critical decisions or customer interactions, do the outputs align with the institution’s commitment to fairness, transparency, and explainability? This includes verifying bias detection and mitigation measures and ensuring outcomes are justifiable.

---

## FINOS-PREV-005-006: Ensuring Operational Accessbility for Users

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure the system is intuitive, accessible, and easy for the intended users to oeprate effectively and efficiently. 

**Source Text:** Usability and User Experience (UX): Is the system intuitive, accessible, and easy for the intended users to operate effectively and efficiently?

---

## FINOS-PREV-005-007: Ensuring Regulatory Compliance 

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure the system's operation and data handling complies with all relevation financial regulations (e.g., data privacy, consumer protection) and internal governance policies. 

**Source Text:** Regulatory Compliance and Policy Adherence: Does the system’s operation and data handling comply with all relevant financial regulations (e.g., data privacy, consumer protection) and internal governance policies?

---

## FINOS-PREV-005-008: Ensuring Resilient Behavior 

**Section:** Implementation Guidance

**Subsection:** Establishing Clear and Comprehensive Acceptance Criteria: Considerations for Criteria

**Responsible Party:** System Owners

**Control Text:** System owners must ensure the system exhibits resilient behavior under stress, with invalid inputs, or in failure scenarios, such as by providing clear and actionable error messages.

**Source Text:** Resilience and Error Handling: How does the system behave under stress, with invalid inputs, or in failure scenarios? Are error messages clear and actionable?

---

## FINOS-PREV-005-009: Conducting SAT in Dedicated Test Environments

**Section:** Implementation Guidance

**Subsection:** Preparing a Representative Test Environment and Data

**Responsible Party:** System Owners

**Control Text:** System owners must conduct SAT in a dedicated test environment that mirrors the intended production environment as closely as possinle in terms of infrastructure, configurations, and dependencies. 

**Source Text:** Action: Conduct SAT in a dedicated test environment that mirrors the intended production environment as closely as possible in terms of infrastructure, configurations, and dependencies.

---

## FINOS-PREV-005-010: Utilizing Comprehensive and Representative Test Datasets

**Section:** Implementation Guidance

**Subsection:** Preparing a Representative Test Environment and Data

**Responsible Party:** System Owners

**Control Text:** System owners must utilize comprehensive, high-quality test datasets that are representative of the data the AI system will encounter in real-world operations, including normal operational scenarios, boundary conditions and edge cases, diverse demographic data to test for fairness and bias, where applicable, and potentially, sanitized or synthetic data that mimics production characteristics for specific security or adversarial testing scenarios.

**Source Text:** Test Data: Utilize comprehensive, high-quality test datasets that are representative of the data the AI system will encounter in real-world operations. This should include:
-Normal operational scenarios.
-Boundary conditions and edge cases.
-Diverse demographic data to test for fairness and bias, where applicable.
-Potentially, sanitized or synthetic data that mimics production characteristics for specific security or adversarial testing scenarios.

---

## FINOS-PREV-005-011: Involving End-Users in Test Execution and Validation

**Section:** Implementation Guidance

**Subsection:** Ensuring Active User Involvement

**Responsible Party:** System Owners

**Control Text:** System owners must actively involve actual end-users, or designated representatives who understand the business processes, in the execution of test cases and the validation of results to confirm that the system genuinely meets practical business needs and usability expectations.

**Source Text:** Action: Actively involve actual end-users, or designated representatives who understand the business processes, in the execution of test cases and the validation of results.

---

## FINOS-PREV-005-012: Incorporating User Feedback to Confirm Practical Usability

**Section:** Implementation Guidance

**Subsection:** Ensuring Active User Involvement

**Responsible Party:** System Owners

**Control Text:** System owners may consider tha their hands-on partipation and feedback are paramount to confirming that the system genuinly meets practical business needs and usability expectations.

**Source Text:** Rationale: Their hands-on participation and feedback are paramount to confirming that the system genuinely meets practical business needs and usability expectations.

---

## FINOS-PREV-005-013: Executing Test Cases

**Section:** Implementation Guidance

**Subsection:** Systematic Test Execution and Rigorous Documentation

**Responsible Party:** System Owners

**Control Text:** System owners must execute test cases methodically according to a predefined test plan, ensuring all acceptance criteria are covered.

**Source Text:** Action: Execute test cases methodically according to a predefined test plan, ensuring all acceptance criteria are covered.

---

## FINOS-PREV-005-014: Maintaining Records of Testing Activities

**Section:** Implementation Guidance

**Subsection:** Systematic Test Execution and Rigorous Documentation

**Responsible Party:** System Owners

**Control Text:** System owners must maintain meticulous records of all testing activities, including test cases executed with their respective outcomes (pass/fail), detailed evidence for each test (e.g., screenshots, logs, output files), any deviations from expected results or issues encountered, and clear traceability linking requirements to test cases and their results.

**Source Text:** Documentation: Maintain meticulous records of all testing activities:
Test cases executed with their respective outcomes (pass/fail).
Detailed evidence for each test (e.g., screenshots, logs, output files).
Any deviations from expected results or issues encountered.
Clear traceability linking requirements to test cases and their results.

---

## FINOS-PREV-005-015: Reporting and Resolving Issues Identified During SAT

**Section:** Implementation Guidance

**Subsection:** Managing Issues and Validating Resolutions

**Responsible Party:** System Owners

**Control Text:** System owners must implement a formal process for reporting, prioritizing, tracking, and resolving any defects, gaps, or issues identified during SAT.

**Source Text:** Action: Implement a formal process for reporting, prioritizing, tracking, and resolving any defects, gaps, or issues identified during SAT.

---

## FINOS-PREV-005-016: Addressing and Validating Critical Issues Before Acceptance

**Section:** Implementation Guidance

**Subsection:** Managing Issues and Validating Resolutions

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that all critical and high-priority issues are satisfactorily addressed, re-tested, and validated before granting system acceptance.

**Source Text:** Resolution: Ensure that all critical and high-priority issues are satisfactorily addressed, re-tested, and validated before granting system acceptance.

---

## FINOS-PREV-005-017: Securing Formal Sign-Off for System Acceptance and Deployment

**Section:** Implementation Guidance

**Subsection:** Obtaining Formal Acceptance and Sign-off

**Responsible Party:** System Owners

**Control Text:** System owners must secure a formal, documented sign-off from the designated business owner(s) and other key stakeholders (e.g., Head of Risk, CISO delegate where appropriate) to confirm that the AI system has successfully met all acceptance criteria and is approved for deployment, acknowledging any accepted risks or limitations. 

**Source Text:** Action: Secure a formal, documented sign-off from the designated business owner(s) and other key stakeholders (e.g., Head of Risk, CISO delegate where appropriate).

---

## FINOS-PREV-005-018: Confirming Acceptance and Acknowledged Risks Through Formal Sign-Off

**Section:** Implementation Guidance

**Subsection:** Obtaining Formal Acceptance and Sign-off

**Responsible Party:** System Owners

**Control Text:** System owners may consider that this sign-off confirms that the AI system has successfully met all acceptance criteria and is approved for deployment, acknowledging any accepted risks or limitations.

**Source Text:** Significance: This sign-off confirms that the AI system has successfully met all acceptance criteria and is approved for deployment, acknowledging any accepted risks or limitations.

---

## FINOS-PREV-006-001: Establishing and Maintaining an AI Data Governance Framework

**Section:** Key Principles

**Subsection:** Comprehensive Data Governance for AI


**Responsible Party:** System Owners

**Control Text:** System owners must establish and maintain a clear data governance framework that specifically addresses the lifecycle of data used in AI systems, including defined roles and responsibilities for data stewardship, quality assurance, and classification.

**Source Text:** Framework: Establish and maintain a clear data governance framework that specifically addresses the lifecycle of data used in AI systems. This includes defining roles and responsibilities for data stewardship, quality assurance, and classification.

---

## FINOS-PREV-006-002: Developing and Enforcing Data Handling and Quality Policies

**Section:** Key Principles

**Subsection:** Comprehensive Data Governance for AI


**Responsible Party:** System Owners

**Control Text:** System owners must develop and enforce policies for data handling, data quality standards, and data classification that are understood and actionable by relevant personnel.

**Source Text:** Policies: Develop and enforce policies for data handling, data quality standards, and data classification that are understood and actionable by relevant personnel.

---

## FINOS-PREV-006-003: Maintaining Comprehensive Data Lineage and Metadata Management

**Section:** Key Principles

**Subsection:** Comprehensive Data Governance for AI


**Responsible Party:** System Owners

**Control Text:** System owners must maintain robust data lineage documentation (tracing data origins, transformations, and usage) and comprehensive metadata management to ensure transparency and understanding of data context.

**Source Text:** Lineage and Metadata: Maintain robust data lineage documentation (tracing data origins, transformations, and usage) and comprehensive metadata management to ensure transparency and understanding of data context.

---

## FINOS-PREV-006-004: Assessing Origin and Reliability of New Data Sources

**Section:** Implementation Guidance

**Subsection:** Data Source Vetting

**Responsible Party:** System Owners

**Control Text:** System owners must, before incorporating any new data source, conduct a thorough assessment of the data source’s origin, reliability, existing quality controls, and the accuracy of any pre-existing classifications, prioritizing the use of well-governed and trusted internal data sources.

**Source Text:** Before incorporating any new data source, conduct a thorough assessment of its origin, reliability, existing quality controls, and the accuracy of any pre-existing classifications. Prioritize the use of well-governed, trusted internal data sources.

---

## FINOS-PREV-006-005: Leveraging Automated Tools for Data Discovery and Classification

**Section:** Implementation Guidance

**Subsection:** Automated Tools (Where Feasible)

**Responsible Party:** System Owners

**Control Text:** System owners must leverage automated tools for data discovery, profiling (to understand quality characteristics), and classification (e.g., using pattern matching, metadata analysis, or ML-based classifiers) to manage the volume and velocity of data (“at the necessary scale”).

**Source Text:** Leverage automated tools for data discovery, profiling (to understand quality characteristics), and classification (e.g., using pattern matching, metadata analysis, or ML-based classifiers). Automation is crucial for managing the volume and velocity of data (“at the necessary scale”).

---

## FINOS-PREV-006-006: Implementing Automated Data Quality Checks and Validation Rules

**Section:** Implementation Guidance

**Subsection:** Automated Tools (Where Feasible)

**Responsible Party:** System Owners

**Control Text:** System owners must implement automated data quality checks and validation rules within data pipelines to continuously monitor and flag issues.

**Source Text:** Implement automated data quality checks and validation rules within data pipelines to continuously monitor and flag issues.

---

## FINOS-PREV-006-007: Conducting Manual Reviews for Sensitive or Critical Data

**Section:** Implementation Guidance

**Subsection:** Manual Oversight and QA

**Responsible Party:** System Owners

**Control Text:** System owners must supplement automated processes with targeted manual reviews and quality assurance procedures, particularly for highly sensitive data, data used in critical AI applications (e.g., those impacting financial decisions, regulatory reporting, or customer treatment), and validation of automated classification and quality assessment results.

**Source Text:** Supplement automated processes with targeted manual reviews and quality assurance procedures, particularly for:
-Highly sensitive data.
-Data used in critical AI applications (e.g., those impacting financial decisions, regulatory reporting, or customer treatment).
-Validation of automated classification and quality assessment results.

---

## FINOS-PREV-006-008: Applying Technical Controls to Filter and Restrict Data Based on Sensitivity

**Section:** Implementation Guidance

**Subsection:** Filtering and Control Based on Classification/Quality

**Responsible Party:** System Owners

**Control Text:** System owners must implement technical controls to filter, segregate, or restrict data from AI ingestion pipelines based on its sensitivity classification and data quality metrics. 

**Source Text:** Implement technical controls to filter, segregate, or restrict data from AI ingestion pipelines based on its sensitivity classification and data quality metrics. For example, prevent highly confidential data from being used in a general-purpose AI development sandbox unless explicitly authorized and with appropriate safeguards.

---

## FINOS-PREV-006-009: Triggering Alerts for Data Quality Issues Below Acceptable Thresholds

**Section:** Implementation Guidance

**Subsection:** Filtering and Control Based on Classification/Quality

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that data quality issues below a certain threshold trigger alerts or prevent data from being used by the AI model until remediated.

**Source Text:** Ensure that data quality issues below a certain threshold trigger alerts or prevent data from being used by the AI model until remediated.

---

## FINOS-PREV-006-010: Implementing Data Pre-Processing Techniques to Address Quality Issues

**Section:** Implementation Guidance

**Subsection:** Data Pre-processing for Quality Enhancement

**Responsible Party:** System Owners

**Control Text:** System owners must document and implement appropriate data pre-processing techniques to address identified quality issues, including handling missing values, correcting inaccuracies, standardizing formats, normalizing data, and removing duplicates, to maintain data lineage.

**Source Text:** Employ appropriate data pre-processing techniques to address identified quality issues. This may include handling missing values, correcting inaccuracies, standardizing formats, normalizing data, and removing duplicates. All such transformations should be documented to maintain lineage.

---

## FINOS-PREV-006-011: Auditing Data Classification Accuracy and Quality Management Processes

**Section:** Implementation Guidance

**Subsection:** Regular Audits and Continuous Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners must conduct periodic audits of data classification accuracy across key repositories and assess the effectiveness of data quality management processes for AI data sources.

**Source Text:** Conduct periodic audits of data classification accuracy across key repositories and assess the effectiveness of data quality management processes for AI data sources.

---

## FINOS-PREV-006-012: Monitoring Data Pipelines for Drift and Quality Degradation

**Section:** Implementation Guidance

**Subsection:** Regular Audits and Continuous Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners must continuously monitor data pipelines for significant drifts in data distributions or degradation in quality, as these can adversely impact AI model performance, fairness, and reliability.

**Source Text:** Continuously monitor data pipelines for significant drifts in data distributions or degradation in quality, as these can adversely impact AI model performance, fairness, and reliability.

---

## FINOS-PREV-006-013: Providing Regular Training to Personnel

**Section:** Implementation Guidance

**Subsection:** Training and Awareness Programs

**Responsible Party:** System Owners

**Control Text:** System owners must provide regular training to all personnel involved in data management, AI development, and AI operations on the institution’s data classification policies, data quality standards, ethical data use, and secure data handling procedures.

**Source Text:** Provide regular training to all personnel involved in data management, AI development, and AI operations on the institution’s data classification policies, data quality standards, ethical data use, and secure data handling procedures.

---

## FINOS-PREV-007-001: Ensuring SaaS Providers Comply with Data Sovereignty Requirements

**Section:** Key Principles

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers specify the provider’s ability to honor data sovereignty requirements of different jurisdictions.  

**Source Text:** Does the provider have the ability to honor data sovereignty requirements of different jurisdictions? For example, if EU client/user data should be stored in EU.

---

## FINOS-PREV-007-002: Defining Data Usage and Retention Terms in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Data Governance, Privacy, and Security

**Responsible Party:** System Owners

**Control Text:** System owners must clearly define in legal agreements with the SaaS inference provider how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected, including whether the vendor persists or logs prompts, inputs, and outputs, for how long, and for what purposes.

**Source Text:** Data Usage and Processing: Clearly define how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected. Specifically clarify:
Does the vendor persist or log prompts, inputs, and outputs? If so, for how long and for what purposes?

---

## FINOS-PREV-007-003: Defining Data Protection and Privacy Safeguards in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Data Governance, Privacy, and Security

**Responsible Party:** System Owners

**Control Text:** System owners must clearly define in legal agreements with the SaaS inference provider how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected, including how the data is safeguarded (encryption, access controls, segregation) and how its privacy is preserved. 

**Source Text:** Data Usage and Processing: Clearly define how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected. Specifically clarify: How is data safeguarded (encryption, access controls, segregation)? How is its privacy preserved?

---

## FINOS-PREV-007-004: Defining Data Use for Vendor Model Training in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Data Governance, Privacy, and Security

**Responsible Party:** System Owners

**Control Text:** System owners must clearly define in legal agreements with the SaaS inference provider how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected, including whether the data is used for further training of the vendor's models or for any other purposes. 

**Source Text:** Data Usage and Processing: Clearly define how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected. Specifically clarify: Is the data used for further training of the vendor’s models or for any other purposes?

---

## FINOS-PREV-007-005: Defining Data Sharing Conditions with Third Parties in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Data Governance, Privacy, and Security

**Responsible Party:** System Owners

**Control Text:** System owners must clearly define in legal agreements with the SaaS inference provider how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected, including whether the data is shared with any other third parties and under what conditions.

**Source Text:** Data Usage and Processing: Clearly define how any data provided to or processed by a third party (e.g., prompts, proprietary datasets, customer information) will be used, processed, stored, and protected. Specifically clarify: Is data shared with any other third parties? Under what conditions?

---

## FINOS-PREV-007-006: Mandating Compliance with Data Protection and Privacy Regulations

**Section:** Implementation Guidance

**Subsection:** Data Governance, Privacy, and Security

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with the SaaS inference provider mandate compliance with all applicable data protection and privacy regulations (e.g., GDPR, CCPA), addressing requirements for lawful basis for processing, data subject rights management, and consent mechanisms (how consent is obtained, recorded, and managed from users, if applicable).

**Source Text:** Regulatory Compliance: Ensure the agreement mandates compliance with all applicable data protection and privacy regulations (e.g., GDPR, CCPA). Address requirements for:
Lawful basis for processing.
Data subject rights management.
Consent mechanisms (how consent is obtained, recorded, and managed from users, if applicable).

---

## FINOS-PREV-007-007: Specifying Information Security Standards and Breach Notification Procedures

**Section:** Implementation Guidance

**Subsection:** Data Governance, Privacy, and Security

**Responsible Party:** System Owners

**Control Text:** System owners must stipulate required information security standards, controls, and certifications in legal agreements with the SaaS inference provider, including clear procedures and timelines for notifying the institution in the event of a data breach or security incident.

**Source Text:** Security Standards and Breach Notification: Stipulate required information security standards, controls, and certifications. Include clear procedures and timelines for notifying the institution in the event of a data breach or security incident.

---

## FINOS-PREV-007-008: Addressing Training Data and Third-Party IP in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Intellectual Property (IP) Rights and Indemnification

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with the SaaS inference provider includes information regarding the data used for training, particulatly concerning third-party IP, if the vendor provides pre-trained models. 

**Source Text:** Training Data Provenance: If the vendor provides pre-trained models, seek information regarding the data used for training, particularly concerning third-party IP.

---

## FINOS-PREV-007-009: Requiring Indemnification for IP Infringement in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Intellectual Property (IP) Rights and Indemnification

**Responsible Party:** System Owners

**Control Text:** System owners must ensure in legal agreements with the SaaS inference provider that the vendor provides indemnifications against claims of IP infringement (e.g., if copyrighted materials were used without authorization in model training).

**Source Text:** Indemnity Protections: Does the vendor provide indemnification against claims of IP infringement (e.g., if copyrighted materials were used without authorization in model training)?

---

## FINOS-PREV-007-010: Defining Ownership of AI Outputs and Derived IP

**Section:** Implementation Guidance

**Subsection:** Intellectual Property (IP) Rights and Indemnification

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers clearly define ownership of AI model outputs, any new intellectual property created (e.g., custom models developed using vendor tools), and data derivatives.

**Source Text:** Ownership of Outputs and Derivatives: Clearly define ownership of AI model outputs, any new IP created (e.g., custom models developed using vendor tools), and data derivatives.

---

## FINOS-PREV-007-011: Clarifying Licensing Terms for AI Models and Tools

**Section:** Implementation Guidance

**Subsection:** Intellectual Property (IP) Rights and Indemnification

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers provide clarity on licensing terms for AI models, software, and tools, including scope of use, restrictions, and any dependencies.


**Source Text:** Licensing Terms: Ensure clarity on licensing terms for AI models, software, and tools, including scope of use, restrictions, and any dependencies.

---

## FINOS-PREV-007-012: Allocating Responsibilities Across the AI System Lifecycle

**Section:** Implementation Guidance

**Subsection:** Allocation of Responsibilities, Liabilities, and Risk

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers explicitly allocate responsibilities for the AI system’s lifecycle (development, deployment, operation, maintenance, decommissioning) between the institution and the third party (as per ISO 42001 A.10.2, A.10.3).

**Source Text:** Clearly Defined Roles: Explicitly allocate responsibilities for the AI system’s lifecycle (development, deployment, operation, maintenance, decommissioning) between the institution and the third party (as per ISO 42001 A.10.2, A.10.3).

---

## FINOS-PREV-007-013: Addressing Liability, Warranties, and Disclaimers in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Allocation of Responsibilities, Liabilities, and Risk

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers address limitations of liability, warranties (e.g., regarding performance and accuracy), and any disclaimers, and that these provisions are appropriate for the risk level of the AI application.

**Source Text:** Liability and Warranties: Address limitations of liability, warranties (e.g., regarding performance, accuracy), and any disclaimers. Ensure these are appropriate for the risk level of the AI application.

---

## FINOS-PREV-007-014: Seeking Transparency into Vendor Model Architecture and Methodologies

**Section:** Implementation Guidance

**Subsection:** Model Transparency, Explainability, and Data Provenance

**Responsible Party:** System Owners

**Control Text:** System owners entering legal agreements with SaaS inference providers must seek rights to understand the AI model’s general architecture, methodologies, and key operational parameters, to the extent feasible and permissible.

**Source Text:** Transparency into Model Operation: To the extent feasible and permissible, seek rights to understand the AI model’s general architecture, methodologies, and key operational parameters.

---

## FINOS-PREV-007-015: Ensuring Explainability Support in SaaS Provider Agreements

**Section:** Implementation Guidance

**Subsection:** Model Transparency, Explainability, and Data Provenance

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that the legal aggreemtns with SaaS inference providers support the institution’s explainability requirements if the AI system is used for decisions impacting customers or for regulatory purposes.

**Source Text:** Explainability Support: If the AI system is used for decisions impacting customers or for regulatory purposes, ensure the contract supports the institution’s explainability requirements.

---

## FINOS-PREV-007-016: Requesting Information on Training Data Sources and Characteristics

**Section:** Implementation Guidance

**Subsection:** Model Transparency, Explainability, and Data Provenance

**Responsible Party:** System Owners

**Control Text:** System owners entering legal agreements with SaaS inference providers must seek information on the characteristics and sources of data used to train models provided by vendors, as appropriate.

**Source Text:** Information on Training Data: As appropriate, seek information on the characteristics and sources of data used to train models provided by vendors.

---

## FINOS-PREV-007-017: Defining SLAs for Availability, Performance, and Support in SaaS Agreements

**Section:** Implementation Guidance

**Subsection:** Service Levels, Performance, and Model Management

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers define clear SLAs for AI system availability, performance metrics (e.g., response times, accuracy levels), and support responsiveness.

**Source Text:** Service Level Agreements (SLAs): Define clear SLAs for AI system availability, performance metrics (e.g., response times, accuracy levels), and support responsiveness.

---

## FINOS-PREV-007-018: Specifying Model Versioning and Update Notification Requirements

**Section:** Implementation Guidance

**Subsection:** Service Levels, Performance, and Model Management

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers specify the vendor’s policy on model versioning, updates, and changes, and require timely notification of any modifications that could impact model performance, behavior (“drift”), or compliance to allow the institution to re-validate.

**Source Text:** Model Versioning and Change Management: The contract should specify the vendor’s policy on model versioning, updates, and changes. Ensure timely notification of any changes that could impact model performance, behavior (“drift”), or compliance, allowing the institution to re-validate.

---

## FINOS-PREV-007-019: Outlining Maintenance and Technical Support Provisions

**Section:** Implementation Guidance

**Subsection:** Service Levels, Performance, and Model Management

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with SaaS inference providers outline provisions for ongoing maintenance, technical support, and updates.

**Source Text:** Maintenance and Support: Outline provisions for ongoing maintenance, technical support, and updates.

---

## FINOS-PREV-008-001: Enforcing Per-User and Per-API-Key Request Quotas

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must enforce per-user or per-API-key request quotas to prevent absuse or to avoid monopolization of AI system resources.

**Source Text:** Rate Limiting: Enforce per-user or per-API-key request quotas to prevent abuse or to avoid monopolization of AI system resources.

---

## FINOS-PREV-008-002: Implementing Dynamic Throttling for Traffic Management

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must use dynamic throttling to control bursts of traffic and maintain steady system load.

**Source Text:** Traffic Shaping: Use dynamic throttling to control bursts of traffic and maintain steady system load.

---

## FINOS-PREV-008-003: Employing Anomaly Detection for DDoS and Abuse Prevention

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must employ anomaly detection to identify unusual traffic patterns indicative of distributed denial-of-service (DDoS) attacks or abuse and enforce rigorous validation of all incoming data to filter out malformed or resource-intensive inputs.

**Source Text:** Traffic Filtering and Validation: Employ anomaly detection to identify unusual traffic patterns indicative of DDoS or abuse. Enforce rigorous validation of all incoming data to filter out malformed or resource-intensive inputs.

---

## FINOS-PREV-008-004: Using Dynamic Load Balancing and Redundant Infrastructure for Resilience

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must employ dynamic load balancing to distribute traffic intelligently across instances and zones to prevent localized overload and establish redundant infrastructure for failover to ensure maximum uptime during high-load scenarios or targeted attacks.

**Source Text:** Load Balancing and Redundancy: Employ Dynamic Load Balancing to distribute traffic intelligently across instances and zones to prevent localized overload. Create redundant infrastructure for failover and redundancy, ensuring maximum uptime during high-load scenarios or targeted attacks.

---

## FINOS-PREV-008-005: Integrating Network-Level DDoS Protection Services

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must integrate with network-level DDoD protection services. 

**Source Text:** Edge Protection: Integrate with network-level DDoS protection services.

---

## FINOS-PREV-008-006: Implementing QoS Tiers for Critical Operations

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must implement QoS tiers to ensure that critical operations recieve priority during congestion. 

**Source Text:** Prioritization Policies: Implement QoS tiers to ensure critical operations receive priority during congestion.

---

## FINOS-PREV-008-007: Monitoring Performance and Traffic with ML-Based Anomaly Detection

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must track performance metrics and traffic volume in real-time to detect anomalies early and leverage ML-based detection systems to spot patterns indicative of low-and-slow DDoS attacks or prompt-based abuse.

**Source Text:** Monitoring and Anomaly Detection: Track performance metrics and traffic volume in real-time to detect anomalies early. Leverage ML-based detection systems to spot patterns indicative of low-and-slow DDoS attacks or prompt-based abuse.

---

## FINOS-PREV-008-008: Using Container-Level Isolation for Inference System Protection

**Section:** Implementation Guidance

**Subsection:** Measures to ensure QoS and protect AI systems from DDoS attacks

**Responsible Party:** System Owners

**Control Text:** System owners must use container-level isolation to protect core inference or decision systems from being impacted by overloaded upstream components.

**Source Text:** Resource Isolation: Use container-level isolation to protect core inference or decision systems from being impacted by overloaded upstream components.

---

## FINOS-PREV-008-009: Combining Static and Adaptive Filters for Secure Input Validation

**Section:** Implementation Guidance

**Subsection:** Reference Implementation

**Responsible Party:** System Owners

**Control Text:** System owners must combine simple static filters with adaptive systems that learn from traffic patterns to secure input validation and filtering at mulitple layers, including deploying an API gateaway and generating API keys specific to each use case. 

**Source Text:** A common approach is to deploy an API gateway and generate API keys specific to each use case. The assignments of keys allows:
Revocation of keys on a per use case basis to block misbehaving applications
Attribution of cost at the use case level to ensure shared infrastructure receives necessary funding and to allow ROI to be measured
Prioritizing access of LLM requests when capacity has been saturated and SLAs across all consumers cannot be satisfied

---

## FINOS-PREV-010-001: Ensuring Clear Versioning Schemes and Release Notes in Supplier Agreements

**Section:** Implementation Guidance

**Subsection:** Establishing Expectations with AI Model Suppliers

**Responsible Party:** System Owners

**Control Text:** The institution must seek and contractually ensure a clear versioning scheme and detailed release notes during procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs). Suppliers must implement and communicate a clear, consistent versioning system (e.g., semantic versioning like MAJOR.MINOR.PATCH). Each new version should be accompanied by comprehensive release notes detailing changes in model architecture, training data, performance characteristics (e.g., accuracy, latency), known issues, potential behavioral shifts, and any deprecated features.

**Source Text:** During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following: Clear Versioning Scheme and Detailed Release Notes:
Requirement: Suppliers must implement and communicate a clear, consistent versioning system (e.g., semantic versioning like MAJOR.MINOR.PATCH).
Details: Each new version should be accompanied by comprehensive release notes detailing changes in model architecture, training data, performance characteristics (e.g., accuracy, latency), known issues, potential behavioral shifts, and any deprecated features.

---

## FINOS-PREV-010-002: Ensuring Advance Notification of New Versions and Deprecations

**Section:** Implementation Guidance

**Subsection:** Establishing Expectations with AI Model Suppliers

**Responsible Party:** System Owners

**Control Text:** The institution must seek and contractually ensure an advance notification of new versions and deprecations during procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs). Suppliers must provide proactive and sufficient advance notification regarding new model releases, planned timelines for deprecating older versions, and any critical security advisories or patches related to specific versions.

**Source Text:** During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following: Advance Notification of New Versions and Deprecation:
Requirement: Suppliers should provide proactive and sufficient advance notification regarding new model releases, planned timelines for deprecating older versions, and any critical security advisories or patches related to specific versions.

---

## FINOS-PREV-010-003: Ensuring API Flexibility for Version Selection and Backward Compatibility

**Section:** Implementation Guidance

**Subsection:** Establishing Expectations with AI Model Suppliers

**Responsible Party:** System Owners

**Control Text:** The institution must seek and contractually ensure API flexibility for version selection and backward compatibility during procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs). Suppliers must provide mechanisms that allow the institution to explicitly select and "pin" to a specific model version for models accessed via APIs. System owners must ensure options for backward compatibility or clearly defined migration paths, allowing the institution to continue using a pinned version for a reasonable period until it is ready to migrate. Production systems should not be forcibly updated by the supplier.


**Source Text:** During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following: API Flexibility for Version Selection and Backward Compatibility:
Requirement: For models accessed via APIs, suppliers must provide mechanisms that allow the institution to explicitly select and “pin” to a specific model version.
Support: Ensure options for backward compatibility or clearly defined migration paths, allowing the institution to continue using a pinned version for a reasonable period until it is ready to migrate. Production systems should not be forcibly updated by the supplier.

---

## FINOS-PREV-010-004: Ensuring Support for Testing New Model Versions

**Section:** Implementation Guidance

**Subsection:** Establishing Expectations with AI Model Suppliers

**Responsible Party:** System Owners

**Control Text:** The institution must seek and contractually ensure support for testing new versions during procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs). Suppliers must offer sandbox environments, trial access, or other mechanisms enabling the institution to thoroughly test new model versions with its own specific use cases, data, and integrations before committing to a production upgrade.

**Source Text:** During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following: Support for Testing New Versions:
Requirement: Ideally, suppliers should offer sandbox environments, trial access, or other mechanisms enabling the institution to thoroughly test new model versions with its own specific use cases, data, and integrations before committing to a production upgrade.

---

## FINOS-PREV-010-005: Ensuring Transparency into Supplier Testing and Validation Practices

**Section:** Implementation Guidance

**Subsection:** Establishing Expectations with AI Model Suppliers

**Responsible Party:** System Owners

**Control Text:** The institution must seek and contractually ensure transparency into supplier's testing practices during procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs). System owners must inquire about the supplier’s internal testing, validation, and quality assurance processes for new model releases to gauge their rigor.

**Source Text:** During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following: Transparency into Supplier’s Testing Practices:
Due Diligence: Inquire about the supplier’s internal testing, validation, and quality assurance processes for new model releases to gauge their rigor.

---

## FINOS-PREV-010-006: Establishing Feedback Mechanisms with AI Model Suppliers

**Section:** Implementation Guidance

**Subsection:** Establishing Expectations with AI Model Suppliers

**Responsible Party:** System Owners

**Control Text:** The institution must seek and contractually ensure feedback mechanisms during procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs). They must establish clear channels for providing feedback to the supplier on model performance, including any regressions, unexpected behaviors, or issues encountered with specific versions.

**Source Text:** During procurement, due diligence, and ongoing relationship management with AI model suppliers (especially for foundational models or models accessed via APIs), the institution should seek and contractually ensure the following: Feedback Mechanisms:
Requirement: Establish clear channels for providing feedback to the supplier on model performance, including any regressions, unexpected behaviors, or issues encountered with specific versions.

---

## FINOS-PREV-010-009: Documenting and Implementing Approved Pinned Model Versions

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must formally decide, document, and implement the specific version of each AI model to be used in each production application or system. This “pinned” version becomes the approved baseline. (Supports ISO 42001 A.6.2.3, A.6.2.5)

**Source Text:** Explicit Version Selection and Pinning:
Action: Formally decide, document, and implement the specific version of each AI model to be used in each production application or system. This “pinned” version becomes the approved baseline. (Supports ISO 42001 A.6.2.3, A.6.2.5)

---

## FINOS-PREV-010-010: Establishing Processes for Evaluating and Approving New Model Versions

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must establish a structured internal process for the evaluation, testing, risk assessment, and approval of new AI model versions before they replace a currently pinned version (Supports ISO 42001 A.6.2.6). This process must include performance testing against established baselines, bias and fairness assessments, security reviews (for new vulnerabilities), integration testing, and user acceptance testing (UAT) where applicable.

**Source Text:** Develop a Version Upgrade Strategy and Process:
Action: Establish a structured internal process for the evaluation, testing, risk assessment, and approval of new AI model versions before they replace a currently pinned version. (Supports ISO 42001 A.6.2.6)
Testing Scope: This internal validation should include performance testing against established baselines, bias and fairness assessments, security reviews (for new vulnerabilities), integration testing, and user acceptance testing (UAT) where applicable.

---

## FINOS-PREV-010-011: Utilizing Deployment Practices for New Model Versions

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must utilize robust deployment practices (e.g., blue/green deployments, canary releases) for introducing new model versions into production.

**Source Text:** Implement Controlled Deployment and Rollback Procedures:
Action: Utilize robust deployment practices (e.g., blue/green deployments, canary releases) for introducing new model versions into production.

---

## FINOS-PREV-010-012: Maintaining Tested Rollback Plans for Reverting Model Versions

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must maintain a well-tested rollback plan to quickly revert to the previously pinned stable version if significant issues arise post-deployment of a new version. (Supports ISO 42001 A.6.2.5)

**Source Text:** Implement Controlled Deployment and Rollback Procedures: Rollback Plan: Always have a well-tested rollback plan to quickly revert to the previously pinned stable version if significant issues arise post-deployment of a new version. (Supports ISO 42001 A.6.2.5)

---

## FINOS-PREV-010-013: Monitoring Performance and Security of Pinned Models in Production

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must monitor the performance, behavior, and security posture of pinned models in production. This includes tracking for performance degradation or “drift” (which can occur even without a model change if input data characteristics evolve), and newly discovered vulnerabilities or ethical concerns associated with the pinned version, based on ongoing threat intelligence and research.

**Source Text:** Continuous Monitoring of Pinned Models:
Action: Monitor the performance, behavior, and security posture of pinned models in production. This includes tracking for:
Performance degradation or “drift” (which can occur even without a model change if input data characteristics evolve).
Newly discovered vulnerabilities or ethical concerns associated with the pinned version, based on ongoing threat intelligence and research.

---

## FINOS-PREV-010-014: Maintaining an Deployed Model Inventory 

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must keep an up-to-date inventory of all deployed AI models, their specific pinned versions, and their business owners/applications.

**Source Text:** Maintain an Inventory and Conduct Regular Audits:
Action: Keep an up-to-date inventory of all deployed AI models, their specific pinned versions, and their business owners/applications.

---

## FINOS-PREV-010-015: Verifying Use of Approved Model Versions in Production

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must conduct regular audits to verify that production systems are consistently using the approved, pinned model versions.

**Source Text:** Maintain an Inventory and Conduct Regular Audits:Audits: Conduct regular audits to verify that production systems are consistently using the approved, pinned model versions.

---

## FINOS-PREV-010-016: Implementing Model Version Logging

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must implement logging mechanisms to record which AI model version was used for any given transaction, decision, or output. This is crucial for debugging, incident analysis, and auditability.

**Source Text:** Ensure Traceability and Comprehensive Logging:
Action: Implement logging mechanisms to record which AI model version was used for any given transaction, decision, or output. This is crucial for debugging, incident analysis, and auditability.

---

## FINOS-PREV-010-017: Including Model Version Metadata in AI Outputs

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that model outputs include metadata indicating the model version used, when feasible (supports ISO 42001 A.6.2.3).

**Source Text:** Ensure Traceability and Comprehensive Logging: Metadata: Where feasible, model outputs should include metadata indicating the model version used. (Supports ISO 42001 A.6.2.3)

---

## FINOS-PREV-010-018: Documenting Rationale and Validation for Pinned Model Versions

**Section:** Implementation Guidance

**Subsection:** Internal Organizational Practices for Model Version Management

**Responsible Party:** System Owners

**Control Text:** System owners must document the rationale for selecting a specific pinned version, the results of its initial validation testing, any subsequent evaluations of that version, and the strategic plan for future reviews or upgrades (Supports ISO 42001 A.6.2.3). Also, document the tooling used in managing these versions (aligns with ISO 42001 A.4.4).

**Source Text:** Thorough Documentation:
Action: Document the rationale for selecting a specific pinned version, the results of its initial validation testing, any subsequent evaluations of that version, and the strategic plan for future reviews or upgrades. (Supports ISO 42001 A.6.2.3) Also document tooling used in managing these versions (aligns with ISO 42001 A.4.4).

---

## FINOS-PREV-012-001: Identifying Human and Non-Human Entities Requiring Data Access

**Section:** Implementation Guidance

**Subsection:** Define Roles and Responsibilities for AI Data Access

**Responsible Party:** System Owners

**Control Text:** System owners must systematically identify all human roles and non-human entities (e.g., AI models, MLOps pipelines, service accounts) that require access to data used by, or generated from, AI systems.

**Source Text:** Identify Entities: Systematically identify all human roles and non-human entities (e.g., AI models, MLOps pipelines, service accounts) that require access to data used by, or generated from, AI systems.

---

## FINOS-PREV-012-002: Documenting Data Access Requirements Across the AI Lifecycle

**Section:** Implementation Guidance

**Subsection:** Define Roles and Responsibilities for AI Data Access

**Responsible Party:** System Owners

**Control Text:** System owners must meticulously document the specific data access requirements (e.g., read, write, modify, delete, execute) based on their tasks and responsibilities across the different phases of the AI lifecycle (e.g., data collection, annotation, model training, validation, inference, monitoring) for each identified role/entity, (Aligns with ISO 42001 A.3.2)


**Source Text:** Document Access Needs: For each identified role/entity, meticulously document the specific data access requirements (e.g., read, write, modify, delete, execute) based on their tasks and responsibilities across the different phases of the AI lifecycle (e.g., data collection, annotation, model training, validation, inference, monitoring). (Aligns with ISO 42001 A.3.2)

---

## FINOS-PREV-012-003: Maintaining an Inventory of Data Assets Relevant to AI Systems

**Section:** Implementation Guidance

**Subsection:** Data Discovery, Classification, and Inventory

**Responsible Party:** System Owners

**Control Text:** System owners must maintain a comprehensive inventory of all data assets relevant to AI systems, including datasets, databases, data streams, model artifacts, and configuration files.

**Source Text:** Data Asset Inventory: Maintain a comprehensive inventory of all data assets relevant to AI systems, including datasets, databases, data streams, model artifacts, and configuration files.

---

## FINOS-PREV-012-004: Classifying Data According to Sensitivity Levels

**Section:** Implementation Guidance

**Subsection:** Data Discovery, Classification, and Inventory

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that all data is classified according to the institution’s data sensitivity scheme (e.g., Public, Internal, Confidential, Highly Restricted). This classification is fundamental to determining appropriate access controls. (Aligns with ISO 42001 A.7.2)

**Source Text:** Data Classification: Ensure all data is classified according to the institution’s data sensitivity scheme (e.g., Public, Internal, Confidential, Highly Restricted). This classification is fundamental to determining appropriate access controls. (Aligns with ISO 42001 A.7.2)

---

## FINOS-PREV-012-005: Creating and Updating Access Control Matrices for AI Data

**Section:** Implementation Guidance

**Subsection:** Develop and Maintain an Access Control Matrix

**Responsible Party:** System Owners

**Control Text:** System owners must create and regularly update an access control matrix (or equivalent policy documentation) that clearly maps the defined roles to specific data categories/assets and the corresponding permitted access levels. This matrix serves as the blueprint for configuring technical controls.

**Source Text:** Mapping Roles to Data: Create and regularly update an access control matrix (or equivalent policy documentation) that clearly maps the defined roles to specific data categories/assets and the corresponding permitted access levels. This matrix serves as the blueprint for configuring technical controls.

---

## FINOS-PREV-012-006: Enforcing Role-Based Access Controls Across AI System Layers

**Section:** Implementation Guidance

**Subsection:** Implement Technical Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners must enforce RBAC policies at all relevant layers where AI data is stored, processed, transmitted, or accessed.

**Source Text:** Multi-Layered Enforcement: Enforce RBAC policies at all relevant layers where AI data is stored, processed, transmitted, or accessed

---

## FINOS-PREV-012-007: Applying RBAC to Databases and File Storage Systems

**Section:** Implementation Guidance

**Subsection:** Implement Technical Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners must apply RBAC to databases, data lakes, data warehouses, document management systems (e.g., ensuring data accessed from sources like Confluence is aligned with the end-user’s or system’s role), and file storage.

**Source Text:** Data Repositories: Apply RBAC to databases, data lakes, data warehouses, document management systems (e.g., ensuring data accessed from sources like Confluence is aligned with the end-user’s or system’s role), and file storage.

---

## FINOS-PREV-012-008: Configuring Role-Based Access in AI and MLOps Platforms

**Section:** Implementation Guidance

**Subsection:** Implement Technical Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners must configure access controls within AI/ML development platforms, MLOps tools, and modeling environments to restrict access to projects, experiments, datasets, models, and features based on roles.

**Source Text:** AI/ML Platforms & Tools: Configure access controls within AI/ML development platforms, MLOps tools, and modeling environments to restrict access to projects, experiments, datasets, models, and features based on roles.

---

## FINOS-PREV-012-009: Securing APIs with Role-Based Authorization Controls

**Section:** Implementation Guidance

**Subsection:** Implement Technical Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners must secure APIs that provide access to data or AI model functionalities using role-based authorization.

**Source Text:** APIs: Secure APIs that provide access to data or AI model functionalities using role-based authorization.

---

## FINOS-PREV-012-010: Integrating RBAC into End-User Applications Consuming AI Services

**Section:** Implementation Guidance

**Subsection:** Implement Technical Access Controls

**Responsible Party:** System Owners

**Control Text:** System owners must integrate RBAC into end-user applications that consume AI services or present AI-generated data, ensuring users only see data they are authorized to view.

**Source Text:** Applications: Integrate RBAC into end-user applications that consume AI services or present AI-generated data, ensuring users only see data they are authorized to view.

---

## FINOS-PREV-012-011: Mandating Strong Authentication for Human and Non-Human Entities

**Section:** Implementation Guidance

**Subsection:** Employ Strong Authentication and Authorization Mechanisms

**Responsible Party:** System Owners

**Control Text:** System owners must mandate strong authentication methods for all entities accessing AI data. This includes multi-factor authentication (MFA) for human users and robust, managed credentials (e.g., certificates, API keys, service principals) for applications, AI models, and system accounts.

**Source Text:** Authentication: Mandate strong authentication methods for all entities accessing AI data. This includes multi-factor authentication (MFA) for human users and robust, managed credentials (e.g., certificates, API keys, service principals) for applications, AI models, and system accounts.

---

## FINOS-PREV-012-012: Implementing Authorization Checks Against Access Control Matrices

**Section:** Implementation Guidance

**Subsection:** Employ Strong Authentication and Authorization Mechanisms

**Responsible Party:** System Owners

**Control Text:** System owners must implement rigorous authorization mechanisms that verify an authenticated identity’s permissions against the defined access control matrix before granting access to specific data or functions.

**Source Text:** Authorization: Implement rigorous authorization mechanisms that verify an authenticated identity’s permissions against the defined access control matrix before granting access to specific data or functions.

---

## FINOS-PREV-012-013: Requiring Attestation for Identity and Authorization Verification

**Section:** Implementation Guidance

**Subsection:** Employ Strong Authentication and Authorization Mechanisms

**Responsible Party:** System Owners

**Control Text:** System owners must consider requiring systems (including AI models or processing components) to prove their identity and authorization status through robust attestation mechanisms (hardware-based or software-based) before they can process, train with, or retrieve data for critical systems or sensitive data access (e.g., data stored in encrypted file systems or specialized AI data stores).

**Source Text:** Attestation for Systems: For critical systems or sensitive data access (e.g., data stored in encrypted file systems or specialized AI data stores), consider requiring systems (including AI models or processing components) to prove their identity and authorization status through robust attestation mechanisms (hardware-based or software-based) before they can process, train with, or retrieve data.

---

## FINOS-PREV-012-014: Establishing Processes for Periodic Access Review and Recertification

**Section:** Implementation Guidance

**Subsection:** Conduct Regular Access Reviews and Recertification

**Responsible Party:** System Owners

**Control Text:** System owners must establish a formal process for periodic review (e.g., quarterly, semi-annually) and recertification of all access rights by data owners, business managers, or system owners.

**Source Text:** Periodic Reviews: Establish a formal process for periodic review (e.g., quarterly, semi-annually) and recertification of all access rights by data owners, business managers, or system owners.

---

## FINOS-PREV-012-015: Updating or Revoking Access Permissions Upon Role or System Changes

**Section:** Implementation Guidance

**Subsection:** Conduct Regular Access Reviews and Recertification

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that access permissions are promptly updated or revoked when an individual’s role changes, they leave the organization, or a system’s function is modified or decommissioned.


**Source Text:** Timely Adjustments: Ensure that access permissions are promptly updated or revoked when an individual’s role changes, they leave the organization, or a system’s function is modified or decommissioned.

---

## FINOS-PREV-012-016: Assigning Roles and Minimal Permissions to Non-Human Identities

**Section:** Implementation Guidance

**Subsection:** Manage Access for Non-Human Identities

**Responsible Party:** System Owners

**Control Text:** System owners must treat AI models, MLOps pipelines, automation scripts, and other non-human entities as distinct identities. System owners must assign them specific roles and grant them only the minimum necessary permissions to perform their automated tasks.

**Source Text:** Principle of Least Privilege for Systems: Treat AI models, MLOps pipelines, automation scripts, and other non-human entities as distinct identities. Assign them specific roles and grant them only the minimum necessary permissions to perform their automated tasks.

---

## FINOS-PREV-012-017: Managing Credential Lifecycles for Non-Human Identities Securely

**Section:** Implementation Guidance

**Subsection:** Manage Access for Non-Human Identities

**Responsible Party:** System Owners

**Control Text:** System owners must implement secure practices for managing the lifecycle of credentials (e.g., secrets management, regular rotation) used by these non-human identities.

**Source Text:** Secure Credential Management: Implement secure practices for managing the lifecycle of credentials (e.g., secrets management, regular rotation) used by these non-human identities.

---

## FINOS-PREV-012-018: Implementing Comprehensive Logging of Data Access Attempts

**Section:** Implementation Guidance

**Subsection:** Log and Monitor Data Access

**Responsible Party:** System Owners

**Control Text:** System owners must implement detailed logging of all data access attempts, including successful accesses and denied attempts. Logs should record the identity, data accessed, type of access, and timestamp.

**Source Text:** Comprehensive Logging: Implement detailed logging of all data access attempts, including successful accesses and denied attempts. Logs should record the identity, data accessed, type of access, and timestamp.

---

## FINOS-PREV-012-019: Monitoring Access Logs for Anomalies and Unauthorized Activities

**Section:** Implementation Guidance

**Subsection:** Log and Monitor Data Access

**Responsible Party:** System Owners

**Control Text:** System owners must regularly monitor access logs for anomalous activities, patterns of unauthorized access attempts, or other potential security policy violations.


**Source Text:** Security Monitoring: Regularly monitor access logs for anomalous activities, patterns of unauthorized access attempts, or other potential security policy violations.


---

## FINOS-PREV-014-001: Establishing Policies and Standards for Data Encryption at Rest

**Section:** Implementation Guidance

**Subsection:** Define Policies and Standards

**Responsible Party:** System Owners

**Control Text:** System owners must establish clear organizational policies and standards for data encryption at rest. These should specify approved encryption algorithms (e.g., AES-256), key lengths, modes of operation, and mandatory key management procedures. (Aligns with ISO 42001 A.7.2 regarding data management processes).


**Source Text:** Establish clear organizational policies and standards for data encryption at rest. These should specify approved encryption algorithms (e.g., AES-256), key lengths, modes of operation, and mandatory key management procedures. (Aligns with ISO 42001 A.7.2 regarding data management processes).


---

## FINOS-PREV-014-002: Implementing Storage-Level Encryption for Data Protection

**Section:** Implementation Guidance

**Subsection:** Select Appropriate Encryption Mechanisms

**Responsible Party:** System Owners

**Control Text:** System owners must implement storage-level encryption, which may be full-disk encryption (FDE) which encrypts entire physical or virtual disks, file-system level encryption which encrypts individual files or directories, or database encryption where many database systems (SQL, NoSQL) offer built-in encryption capabilities like Transparent Data Encryption (TDE), which encrypts data files, log files, and backups.

**Source Text:** Storage-Level Encryption:
Full-Disk Encryption (FDE): Encrypts entire physical or virtual disks.
File System-Level Encryption: Encrypts individual files or directories.
Database Encryption: Many database systems (SQL, NoSQL) offer built-in encryption capabilities like Transparent Data Encryption (TDE), which encrypts data files, log files, and backups.

---

## FINOS-PREV-014-003: Encrypting Data at the Application Layer Before Storage

**Section:** Implementation Guidance

**Subsection:** Select Appropriate Encryption Mechanisms

**Responsible Party:** System Owners

**Control Text:** System owners must ensure data is encrypted by the application before being written to any storage medium. This provides granular control but requires careful implementation within the AI applications or data pipelines.

**Source Text:** Application-Level Encryption: Data is encrypted by the application before being written to any storage medium. This provides granular control but requires careful implementation within the AI applications or data pipelines.

---

## FINOS-PREV-014-004: Utilizing Dedicated Key Management Systems for Encryption Keys

**Section:** Implementation Guidance

**Subsection:** Implement Robust Key Management

**Responsible Party:** System Owners

**Control Text:** System owners must utilize a dedicated, hardened Key Management System (KMS) for the secure lifecycle management of encryption keys (generation, storage, distribution, rotation, backup, and revocation).

**Source Text:** Utilize a dedicated, hardened Key Management System (KMS) for the secure lifecycle management of encryption keys (generation, storage, distribution, rotation, backup, and revocation).

---

## FINOS-PREV-014-005: Enforcing Access Controls and Separation of Duties for Encryption Keys

**Section:** Implementation Guidance

**Subsection:** Implement Robust Key Management

**Responsible Party:** System Owners

**Control Text:** System owners must enforce strict access controls to encryption keys based on the principle of least privilege and separation of duties.

**Source Text:** Enforce strict access controls to encryption keys based on the principle of least privilege and separation of duties.

---

## FINOS-PREV-014-006: Rotating Encryption Keys Regularly per Policy

**Section:** Implementation Guidance

**Subsection:** Implement Robust Key Management

**Responsible Party:** System Owners

**Control Text:** System owners must regularly rotate encryption keys according to policy and best practices.

**Source Text:** Regularly rotate encryption keys according to policy and best practices.

---

## FINOS-PREV-014-007: Verifying Encryption Support and Configuration in Vector Databases

**Section:** Implementation Guidance

**Subsection:** Specific Considerations for AI Components and New Technologies


**Responsible Party:** System Owners

**Control Text:** System owners may use criticality for vector databases, given that vector databases are a relatively recent technology area central to many modern AI applications (e.g., RAG systems). It’s crucial to verify and ensure they support robust encryption at rest and that this feature is enabled and correctly configured. Default security postures may vary significantly between different vector database solutions.

**Source Text:** Criticality: Given that vector databases are a relatively recent technology area central to many modern AI applications (e.g., RAG systems), it’s crucial to verify and ensure they support robust encryption at rest and that this feature is enabled and correctly configured. Default security postures may vary significantly between different vector database solutions.

---

## FINOS-PREV-014-008: Leveraging Cloud-Native Vector Stores with Customer-Managed Keys

**Section:** Implementation Guidance

**Subsection:** Specific Considerations for AI Components and New Technologies


**Responsible Party:** System Owners

**Control Text:** System owners may use cloud-native vector stores for vector databases when using services like Azure AI Search or AWS OpenSearch Service, to leverage their integrated encryption at rest features. System owners must ensure these are configured to meet institutional security standards, including options for customer-managed encryption keys (CMEK) if available and required.

**Source Text:** Cloud-Native Vector Stores: When using services like Azure AI Search or AWS OpenSearch Service, leverage their integrated encryption at rest features. Ensure these are configured to meet institutional security standards, including options for customer-managed encryption keys (CMEK) if available and required.

---

## FINOS-PREV-014-009: Reviewing Security and Encryption Practices of Managed SaaS Vector Databases

**Section:** Implementation Guidance

**Subsection:** Specific Considerations for AI Components and New Technologies


**Responsible Party:** System Owners

**Control Text:** System owners may use Managed SaaS Vector Databases for third-party managed services (e.g., Pinecone), where they will carefully review their security documentation and contractual agreements regarding their data encryption practices, key management responsibilities, and compliance certifications. In such cases, securing API access to the service becomes paramount.

**Source Text:** Managed SaaS Vector Databases: For third-party managed services (e.g., Pinecone), carefully review their security documentation and contractual agreements regarding their data encryption practices, key management responsibilities, and compliance certifications. In such cases, securing API access to the service becomes paramount.

---

## FINOS-PREV-014-010: Using Self-Hosted Vector Databases with Institution-Managed Encryption

**Section:** Implementation Guidance

**Subsection:** Specific Considerations for AI Components and New Technologies


**Responsible Party:** System Owners

**Control Text:** System owners may use Self-Hosted Vector Databases if deploying self-hosted vector databases (e.g., using Redis with vector capabilities, or FAISS with persistent storage). In this case, the institution bears full responsibility for implementing and managing encryption at rest for the underlying storage infrastructure, securing the host servers, and managing the encryption keys. This approach requires significant in-house security expertise.

**Source Text:** Self-Hosted Vector Databases: If deploying self-hosted vector databases (e.g., using Redis with vector capabilities, or FAISS with persistent storage), the institution bears full responsibility for implementing and managing encryption at rest for the underlying storage infrastructure, securing the host servers, and managing the encryption keys. This approach requires significant in-house security expertise.

---

## FINOS-PREV-014-011: Protecting In-Memory Data Processing and Persistent Storage Encryption

**Section:** Implementation Guidance

**Subsection:** Specific Considerations for AI Components and New Technologies


**Responsible Party:** System Owners using in-memory data processing

**Control Text:** System owners using in-memory data processing (e.g. FAISS) must remember that primarily operating in-memory (like some configurations of FAISS) can reduce risks associated with persistent storage breaches during runtime. However, system owners must realize that any data loaded into memory must be protected while in transit and sourced from securely encrypted storage, and that if any data or index from such in-memory tools is persisted to disk (e.g., for saving, backup, or sharing), that persisted data must be encrypted. Relying solely on in-memory operation is not a substitute for encryption if data touches persistent storage at any point.

**Source Text:** In-Memory Data Processing (e.g., FAISS):
While primarily operating in-memory (like some configurations of FAISS) can reduce risks associated with persistent storage breaches during runtime, it’s vital to remember that:
Any data loaded into memory must be protected while in transit and sourced from securely encrypted storage.
If any data or index from such in-memory tools is persisted to disk (e.g., for saving, backup, or sharing), that persisted data must be encrypted. Relying solely on in-memory operation is not a substitute for encryption if data touches persistent storage at any point.

---

## FINOS-PREV-014-012: Verifying Implementation and Effectiveness of Encryption Controls

**Section:** Implementation Guidance

**Subsection:** Regular Verification and Audit

**Responsible Party:** System Owners

**Control Text:** System owners must periodically verify that encryption controls are correctly implemented, active, and effective across all relevant AI data storage systems.

**Source Text:** Periodically verify that encryption controls are correctly implemented, active, and effective across all relevant AI data storage systems.

---

## FINOS-PREV-014-013: Including Encryption and Key Management in Security Audits

**Section:** Implementation Guidance

**Subsection:** Regular Verification and Audit

**Responsible Party:** System Owners

**Control Text:** System owners must include encryption at rest configurations and key management practices as part of regular information security audits and assessments.

**Source Text:** Include encryption at rest configurations and key management practices as part of regular information security audits and assessments.

---

## nan: Enforcing Rules and Policies for AI Agent Interactions

**Section:** Key Principles

**Subsection:** Behavioral Policy Enforcement for AI Agents:

**Responsible Party:** System Owners

**Control Text:** System owners using AI agents that can interact with other tools and systems must enforce predefined rules or policies on permissible actions, tool usage, and data access to prevent abuse or unintended consequences.

**Source Text:** In systems involving AI agents that can interact with other tools and systems, enforce predefined rules or policies on permissible actions, tool usage, and data access to prevent abuse or unintended consequences.

---

## FINOS-PREV-017-001: Defining Policies for Acceptable AI Inputs, Outputs, and Behaviors

**Section:** Implementation Guidance

**Subsection:** Policy Definition

**Responsible Party:** System Owners/Organizations

**Control Text:** System owners may choose to define their policies. In that case, organizations must first define clear policies regarding what constitutes acceptable and unacceptable inputs/outputs, data sensitivity rules, and permissible AI agent behaviors. These policies will drive the firewall's configuration.

**Source Text:** Policy Definition: Crucially, organizations must first define clear policies regarding what constitutes acceptable and unacceptable inputs/outputs, data sensitivity rules, and permissible AI agent behaviors. These policies will drive the firewall’s configuration.

---

## FINOS-PREV-017-002: Specializing AI Security Gateways or Proxies for Firewalls

**Section:** Implementation Guidance

**Subsection:** Technological Approaches

**Responsible Party:** System Owners

**Control Text:** System owners may choose to specialize AI security gateways/proxies for their firewalls. This technological approach entails dedicated appliances or software that sit on front of AI models to inspect traffic.

**Source Text:** Specialized AI Security Gateways/Proxies: Dedicated appliances or software that sit in front of AI models to inspect traffic.

---

## FINOS-PREV-017-003: Enhancing Web Application Firewalls with AI-Specific Capabilities

**Section:** Implementation Guidance

**Subsection:** Technological Approaches

**Responsible Party:** System Owners

**Control Text:** System owners may choose to enhance web application firewalls (WAFs), which means that existing WAFs may evolve or offer add-ons with AI-specific rule sets and inspection capabilities. 

**Source Text:** Enhanced Web Application Firewalls (WAFs): Existing WAFs may evolve or offer add-ons with AI-specific rule sets and inspection capabilities.

---

## FINOS-PREV-017-004: Applying API Security Solutions for AI Interactions

**Section:** Implementation Guidance

**Subsection:** Technological Approaches

**Responsible Party:** System Owners

**Control Text:** System owners may choose to use API security solutions for their firewalls because many AI interactions occur via APIs. This technological appraoch includes API security tools with deep payload inspection and behavioral analysis that are relevant.  

**Source Text:** API Security Solutions: Many AI interactions occur via APIs; API security tools with deep payload inspection and behavioral analysis are relevant.

---

## FINOS-PREV-017-005: Using Guardian AI Models for Prompt and Response Evaluation

**Section:** Implementation Guidance

**Subsection:** Technological Approaches

**Responsible Party:** System Owners

**Control Text:** System owners may choose to use "guardian" AI models for their firewalls. This technological approach entails utilizing secondary AI models (sometimes called "LLM judges" or "safety models") specifically trained to evaluate the safety, security, and appropriateness of prompts and responses. 

**Source Text:** “Guardian” AI Models: Utilizing secondary AI models (sometimes called “LLM judges” or “safety models”) specifically trained to evaluate the safety, security, and appropriateness of prompts and responses.

---

## FINOS-PREV-017-006: Determining Optimal Architectural Placement for AI Firewalls

**Section:** Implementation Guidance

**Subsection:** Architectual Placement

**Responsible Party:** System Owners

**Control Text:** System owners may choose to use architectual placement in their firewalls, which would determine the optimal points for inspection (e.g., at the edge, at API gateways, between application components and AI models, or within agentic frameworks).

**Source Text:** Architectural Placement: Determine the optimal points for inspection (e.g., at the edge, at API gateways, between application components and AI models, or within agentic frameworks).

---

## FINOS-PREV-017-007: Balancing Performance Impact and Security in AI Firewalls

**Section:** Implementation Guidance

**Subsection:** Performance Impact

**Responsible Party:** System Owners

**Control Text:** System owners may choose to use performance impacy in their firewalls, which entails deep inspection of AI payloads (which can be large and complex) to introduce latency. The performance overhead must be carefully balanced against security benefits.

**Source Text:** Performance Impact: Deep inspection of AI payloads (which can be large and complex) can introduce latency. The performance overhead must be carefully balanced against security benefits.

---

## FINOS-PREV-017-008: Implementing Adaptability and Continuous Learning in AI Firewalls

**Section:** Implementation Guidance

**Subsection:** Adaptability and Continuous Learning

**Responsible Party:** System Owners

**Control Text:** System owners may choose to use adaptability and continuous learning in their firewalls, which means that an AI Firewall should ideally be adaptive, capable of being updated frequently with new threat signatures, patterns, and potentially using machine learning to detect novel attacks-given the rapidly evolving nature of AI threats.

**Source Text:** Adaptability and Continuous Learning: Given the rapidly evolving nature of AI threats, an AI Firewall should ideally be adaptive, capable of being updated frequently with new threat signatures, patterns, and potentially using machine learning to detect novel attacks.

---

## FINOS-PREV-017-009: Integrating AI Firewalls with the Broader Security Ecosystem

**Section:** Implementation Guidance

**Subsection:** Integration with Security Ecosystem

**Responsible Party:** System Owners

**Control Text:** System owners may choose to use integration with security ecosystem in their firewalls, which would ensure the AI Firewall can integrate with existing security infrastructure, such as Security Information and Event Management (SIEM) systems for log correlation and alerting, Security Orchestration, Automation and Response (SOAR) platforms for automated incident response, and threat intelligence platforms.

**Source Text:** Integration with Security Ecosystem: Ensure the AI Firewall can integrate with existing security infrastructure, such as Security Information and Event Management (SIEM) systems for log correlation and alerting, Security Orchestration, Automation and Response (SOAR) platforms for automated incident response, and threat intelligence platforms.

---

## FINOS-DET-001-001: Mandating Strong Encryption Protocols for Data in Transit

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must mandate and verify the use of strong, industry-best-practice encryption protocols (e.g., TLS 1.3+) for all data in transit when interacting with TSPs or any external AI service endpoint. This process protects against network taps and Man-In-The-Middle (MITM) attacks.

**Source Text:** Secure Communication Channels:
Action: Mandate and verify the use of strong, industry-best-practice encryption protocols (e.g., TLS 1.3+) for all data in transit when interacting with TSPs or any external AI service endpoint.
Rationale: Protects against network taps and Man-In-The-Middle (MITM) attacks.

---

## FINOS-DET-001-002: Preferring Secure Architectural Patterns Within Institutional Cloud Tenants

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must prefer architectural patterns where the TSP hosts their service within the institution’s secure cloud tenant (e.g., using private endpoints, dedicated clusters) to minimize data transmission outside of controlled system boundaries, where feasible. This process reduces exposure to public internet threats.

**Source Text:** Secure Network Architectures:
Action: Where feasible, prefer architectural patterns where the TSP hosts their service within the institution’s secure cloud tenant (e.g., using private endpoints, dedicated clusters) to minimize data transmission outside of controlled system boundaries.
Rationale: Reduces exposure to public internet threats.

---

## FINOS-DET-001-003: Requiring Zero or Time-Bound Data Persistence from TSPs

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must contractually require and, where possible, technically verify that TSPs default to “zero persistence” or minimal, time-bound persistence of logs, session data (prompts/responses), and temporary files (e.g., core dumps), unless explicitly agreed in writing for specific, justified purposes (e.g., audit, support) and with robust safeguards. This process minimizes the data footprint at the TSP, reducing the window of opportunity for leakage from their systems.


**Source Text:** Control over Data Persistence by Third Parties:
Action: Contractually require and, where possible, technically verify that TSPs default to “zero persistence” or minimal, time-bound persistence of logs, session data (prompts/responses), and temporary files (e.g., core dumps), unless explicitly agreed in writing for specific, justified purposes (e.g., audit, support) and with robust safeguards.
Rationale: Minimizes the data footprint at the TSP, reducing the window of opportunity for leakage from their systems.

---

## FINOS-DET-001-004: Ensuring Vendor Compliance with Data Lifecycle Management Standards

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that vendor contracts include commitments to Data Lifecycle Management best practices, compatible with the institution’s standards, particularly concerning the secure and certified disposal of storage media. This process prevents data recovery from improperly decommissioned hardware.


**Source Text:** Secure Data Disposal by Third Parties:
Action: Ensure that vendor contracts include commitments to Data Lifecycle Management best practices, compatible with the institution’s standards, particularly concerning the secure and certified disposal of storage media.
Rationale: Prevents data recovery from improperly decommissioned hardware.

---

## FINOS-DET-001-005: Reviewing TSP Architecture and Certifications for Tenant Isolation

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must confirm that the institution's security design and vendor risk management teams thoroughly review the TSP’s system architecture documentation, security certifications (e.g., SOC 2 Type II), and penetration test results to assess the adequacy of logical tenant isolation and controls preventing cross-tenant data leakage, for multi-tenant AI services. This process ensures one tenant’s data is not inadvertently exposed to another.

**Source Text:** Scrutiny of Multi-Tenant Architectures:
Action: For multi-tenant AI services, the institution’s security design and vendor risk management teams should thoroughly review the TSP’s system architecture documentation, security certifications (e.g., SOC 2 Type II), and penetration test results to assess the adequacy of logical tenant isolation and controls preventing cross-tenant data leakage.
Rationale: Ensures one tenant’s data is not inadvertently exposed to another.

---

## FINOS-DET-001-006: Prohibiting Use of Proprietary Data for Vendor Model Training

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that legal agreements with AI providers (especially for API-based access to foundational models) explicitly state that proprietary API inputs/outputs (session data) will not be used for training their general-purpose models or for any other purpose outside the direct provision of the contracted service, without the institution’s explicit, informed consent. (Addresses “Memorization” risk). This process prevents institutional data from becoming embedded in publicly accessible or other clients’ models.

**Source Text:** Contractual Prohibitions on Unauthorized Data Use (e.g., Model Training):
Action: Legal agreements with AI providers (especially for API-based access to foundational models) must explicitly state that proprietary API inputs/outputs (session data) will not be used for training their general-purpose models or for any other purpose outside the direct provision of the contracted service, without the institution’s explicit, informed consent. (Addresses “Memorization” risk).
Rationale: Prevents institutional data from becoming embedded in publicly accessible or other clients’ models.

---

## FINOS-DET-001-007: Implementing Caching Mechanisms for Performance Optimization with TSPs

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners with TSPs

**Control Text:** System owners with TSPs may implement caching mechanisms (e.g., for token activations or common prompt prefixes) to reduce redundancy and improve performance, given the high computational cost of LLMs. They must require TSPs to provide clear information about any such optimizations.


**Source Text:** Transparency and Control over Performance Optimizations (e.g., Caching):
Action: Given the high computational cost of LLMs, TSPs may implement caching mechanisms (e.g., for token activations or common prompt prefixes) to reduce redundancy and improve performance. Require TSPs to provide clear information about any such optimizations.


---

## FINOS-DET-001-008: Reviewing Caching Practices for Data Leakage and Residual Risk

**Section:** Implementation Guidance

**Subsection:** Protecting AI Session Data (Especially with Third-Party Services)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that the institution's ML and security teams review the caching mechanism practices for potential risks of data remnants or unintended information exposure through shared cache elements. This process ensures that performance optimizations do not inadvertently create new data leakage vectors. 

**Source Text:** Transparency and Control over Performance Optimizations (e.g., Caching):
Review: The institution’s ML and security teams should review these practices for potential risks of data remnants or unintended information exposure through shared cache elements.
Rationale: Ensures performance optimizations do not inadvertently create new data leakage vectors.

---

## FINOS-DET-001-009: Securing Proprietary Training and Fine-Tuning Datasets

**Section:** Implementation Guidance

**Subsection:** Protecting AI Training Data

**Responsible Party:** System Owners

**Control Text:** System owners must implement strict access controls (e.g., Role-Based Access Control), strong encryption at rest, and secure, isolated storage environments for all proprietary datasets used for training or fine-tuning AI models.

**Source Text:** Robust Access Controls and Secure Storage: Implement strict access controls (e.g., Role-Based Access Control), strong encryption at rest, and secure, isolated storage environments for all proprietary datasets used for training or fine-tuning AI models.

---

## FINOS-DET-001-010: Implementing Guardrails for Models Fine-Tuned with Proprietary Data

**Section:** Implementation Guidance

**Subsection:** Protecting AI Training Data

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that the institution or its AI provider implements and continuously evaluates input/output filtering mechanisms (“guardrails”) for models that are fine-tuned with proprietary data. These are designed to detect and block attempts by users to extract significant portions of the training data through carefully crafted prompts. This requires ongoing monitoring and adaptation by ML and security teams.

**Source Text:** Guardrails Against Extraction via Prompts: For models fine-tuned with proprietary data, the institution or its AI provider must implement and continuously evaluate input/output filtering mechanisms (“guardrails”). These are designed to detect and block attempts by users to extract significant portions of the training data through carefully crafted prompts. This requires ongoing monitoring and adaptation by ML and security teams.

---

## FINOS-DET-001-011: Protecting Trained Model Weights and Architectures as Intellectual Property

**Section:** Implementation Guidance

**Subsection:** Protecting AI Model Intellectual Property (e.g., Weights, Architecture)


**Responsible Party:** System Owners

**Control Text:** System owners must treat trained model weights, configurations, and proprietary architectures as highly sensitive intellectual property. They must store them in secure, access-controlled repositories with strong encryption.

**Source Text:** Secure Model Storage and Access Control: Treat trained model weights, configurations, and proprietary architectures as highly sensitive intellectual property. Store them in secure, access-controlled repositories with strong encryption.

---

## FINOS-DET-001-012: Preventing Unauthorized Copying or Distribution of Model Artifacts

**Section:** Implementation Guidance

**Subsection:** Protecting AI Model Intellectual Property (e.g., Weights, Architecture)

**Responsible Party:** System Owners

**Control Text:** System owners must implement technical controls (e.g., digital rights management, if applicable) and contractual obligations to prevent unauthorized copying, transfer, or distribution of model artifacts.

**Source Text:** Prevent Unauthorized Distribution and Replication: Implement technical controls (e.g., digital rights management, if applicable) and contractual obligations to prevent unauthorized copying, transfer, or distribution of model artifacts.

---

## FINOS-DET-001-013: Embedding Canary Tokens to Detect Unauthorized Data Exposure

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners must embed uniquely identifiable, non-sensitive markers (e.g., unique strings, fictitious identifiers, GUIDs) – “canaries” – within data streams, prompts, or queries sent to external or internal AI models. These canaries have no legitimate business value but are designed to be easily detectable if they appear in unauthorized locations.

**Source Text:** Canary Tokens (“Honey Tokens”):
Concept: Embed uniquely identifiable, non-sensitive markers (e.g., unique strings, fictitious identifiers, GUIDs) – “canaries” – within data streams, prompts, or queries sent to external or internal AI models. These canaries have no legitimate business value but are designed to be easily detectable if they appear in unauthorized locations.

---

## FINOS-DET-001-014: Monitoring for Canary Tokens Across Internal and External Sources

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners must strategically place canary tokens in representative samples of data, and continuously monitor public internet sources (e.g., code repositories, forums, paste sites), dark web locations, and potentially even unexpected internal systems for the appearance of these canaries.

**Source Text:** Canary Tokens ("Honey Tokens"): Implementation: Strategically place canary tokens in representative samples of data. Continuously monitor public internet sources (e.g., code repositories, forums, paste sites), dark web locations, and potentially even unexpected internal systems for the appearance of these canaries.

---

## FINOS-DET-001-015: Generating Cryptographic Fingerprints of Sensitive Data Segments

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners must generate unique cryptographic hashes or more sophisticated signatures (“fingerprints”) of sensitive data segments or entire documents before they are processed by an AI system, particularly if sent to an external provider.

**Source Text:** Data Fingerprinting:
Concept: Generate unique cryptographic hashes or more sophisticated signatures (“fingerprints”) of sensitive data segments or entire documents before they are processed by an AI system, particularly if sent to an external provider.

---

## FINOS-DET-001-016: Monitoring for Fingerprint Appearances in Unauthorized Locations

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners must monitor the appearance of these exact fingerprints in unauthorized locations. This is most effective for detecting leakage of static, well-defined data elements.


**Source Text:** Data Fingerprinting:
Implementation: Monitor for the appearance of these exact fingerprints in unauthorized locations. This is most effective for detecting leakage of static, well-defined data elements.

---

## FINOS-DET-001-017: Integrating Canary and Fingerprinting Mechanisms at Key Data Touchpoints

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners must integrate canary token generation and fingerprinting mechanisms at key data touchpoints within the AI system’s architecture, such as API gateways, data ingestion pipelines, or custom plugins for LLM interactions, where feasible. This facilitates systematic and continuous monitoring.


**Source Text:** Integration into AI Interaction Points:
Action: Where feasible, integrate canary token generation and fingerprinting mechanisms at key data touchpoints within the AI system’s architecture, such as API gateways, data ingestion pipelines, or custom plugins for LLM interactions. This facilitates systematic and continuous monitoring.


---

## FINOS-DET-001-018: Automating Scans for Exposed Canaries and Fingerprints

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners must develop or utilize automated systems to continuously scan for exposed canaries or fingerprints across relevant environments.

**Source Text:** Automated Detection and Incident Response Workflow:
Action: Develop or utilize automated systems to continuously scan for exposed canaries or fingerprints across relevant environments.

---

## FINOS-DET-001-019: Triggering Incident Response Upon Detection of Canary or Fingerprint Leakage

**Section:** Implementation Guidance

**Subsection:** Detecting Session Data Leakage (Especially with External AI Services)

**Responsible Party:** System Owners

**Control Text:** System owners who detect a canary or fingerprint in an unauthorized location must make sure that the system triggers an immediate alert to the Security Operations Center (SOC) or designated incident response team. This initiates a predefined incident response process, including identifying the likely source and vector of the breach, determining the scope and potential impact of the leakage, and implementing containment and remediation actions (e.g., isolating the affected service, notifying the third-party provider, revoking credentials, invoking contractual clauses for breach).

**Source Text:** Automated Detection and Incident Response Workflow: Response: Upon detection of a canary or fingerprint in an unauthorized location, the system must trigger an immediate alert to the Security Operations Center (SOC) or designated incident response team. This initiates a predefined incident response process, including:
Identifying the likely source and vector of the breach.
Determining the scope and potential impact of the leakage.
Implementing containment and remediation actions (e.g., isolating the affected service, notifying the third-party provider, revoking credentials, invoking contractual clauses for breach).

---

## FINOS-DET-001-020: Monitoring Guardrail Performance and Detecting Circumvention Attempts

**Section:** Implementation Guidance

**Subsection:** Detecting Unauthorized Training Data Extraction

**Responsible Party:** System Owners

**Control Text:** System owners must continuously monitor the performance and logs of input/output guardrails designed to prevent training data extraction. They must investigate suspicious prompt patterns or model outputs that might indicate attempts to circumvent these protective measures.

**Source Text:** Monitoring Guardrail Effectiveness: Continuously monitor the performance and logs of input/output guardrails designed to prevent training data extraction. Investigate suspicious prompt patterns or model outputs that might indicate attempts to circumvent these protective measures.

---

## FINOS-DET-001-021: Evaluating Emerging Techniques for AI Model Fingerprinting and Watermarking

**Section:** Implementation Guidance

**Subsection:** Detecting AI Model Weight Leakage

**Responsible Party:** System Owners

**Control Text:** System owners must stay informed about and evaluate emerging research techniques for “fingerprinting” or watermarking AI models (e.g., knowledge injection methods like “Instructional Fingerprinting”). While many of these are still in the research phase, they may offer future capabilities for detecting unauthorized copies or uses of proprietary models if they are found in the wild.

**Source Text:** Emerging Techniques: Stay informed about and evaluate emerging research techniques for “fingerprinting” or watermarking AI models (e.g., knowledge injection methods like “Instructional Fingerprinting”). While many of these are still in the research phase, they may offer future capabilities for detecting unauthorized copies or uses of proprietary models if they are found in the wild.

---

## FINOS-DET-004-001: Defining Goals for AI System Observability

**Section:** Implementation Guidance

**Subsection:** Establish an Observability Strategy

**Responsible Party:** System Owners

**Control Text:** System owners must clearly articulate the goals for AI system observability based on business requirements, specific AI risks (e.g., fairness, security, operational resilience), compliance obligations, and operational support needs.

**Source Text:** Define Objectives: Clearly articulate the goals for AI system observability based on business requirements, specific AI risks (e.g., fairness, security, operational resilience), compliance obligations, and operational support needs.

---

## FINOS-DET-004-002: Determining Access Requirements for Observability Data and Insights

**Section:** Implementation Guidance

**Subsection:** Establish an Observability Strategy

**Responsible Party:** System Owners

**Control Text:** System owners must determine who needs access to observability data and insights (e.g., MLOps teams, data scientists, security analysts, risk managers, compliance officers) and their specific information requirements.


**Source Text:** Identify Stakeholders: Determine who needs access to observability data and insights (e.g., MLOps teams, data scientists, security analysts, risk managers, compliance officers) and their specific information requirements.

---

## FINOS-DET-004-003: Logging and Monitoring User Interactions and Outputs

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use user interactions and output for logging and monitoring, which would complete user inputs (e.g., prompts, queries, uploaded files/data), where permissible and necessary for analysis. This includes system-generated queries to internal/external data sources (e.g., RAG database queries).

**Source Text:** User Interactions and Inputs:
Complete user inputs (e.g., prompts, queries, uploaded files/data), where permissible and necessary for analysis.
System-generated queries to internal/external data sources (e.g., RAG database queries).

---

## FINOS-DET-004-004: Logging and Monitoring AI Model Behavior and Outputs

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use AI Model Behavior and Outputs for logging and monitoring (e.g., predictions, classifications, generated text/images, decisions), which has associated confidence scores, uncertainty measures, or explainability data (if the model provides these). This process includes potentially key intermediate calculations or feature values, especially during debugging or fine-grained analysis of complex models.

**Source Text:** AI Model Behavior and Outputs:
AI model outputs (e.g., predictions, classifications, generated text/images, decisions).
Associated confidence scores, uncertainty measures, or explainability data (if the model provides these).
Potentially key intermediate calculations or feature values, especially during debugging or fine-grained analysis of complex models.

---

## FINOS-DET-004-005: Logging and Monitoring API Traffic and System Interactions

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use API Traffic and System Interactions for logging and monitoring, which includes all API calls related to the AI system (to and from the model, between microservices), including request/response payloads (or sanitized summaries), status codes, latencies, and authentication details. This process also includes data flows and interactions crossing trust boundaries (e.g., with external data sources, third-party AI services, or different internal security zones).

**Source Text:** API Traffic and System Interactions:
All API calls related to the AI system (to and from the model, between microservices), including request/response payloads (or sanitized summaries), status codes, latencies, and authentication details.
Data flows and interactions crossing trust boundaries (e.g., with external data sources, third-party AI services, or different internal security zones).

---

## FINOS-DET-004-006: Tracking Model Performance Metrics for Monitoring and Drift Detection

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use Model Performance Metrics (as per ISO 42001 A.6.2.6) for logging and monitoring, which entails task-specific accuracy metrics (e.g., precision, recall, F1-score, AUC for classification; MAE, RMSE for regression). With this process, it is also important to consider: model prediction drift, concept drift, and data drift indicators; inference latency, throughput (queries per second); error rates and types.

**Source Text:** Model Performance Metrics (as per ISO 42001 A.6.2.6):
Task-specific accuracy metrics (e.g., precision, recall, F1-score, AUC for classification; MAE, RMSE for regression).
Model prediction drift, concept drift, and data drift indicators.
Inference latency, throughput (queries per second).
Error rates and types.

---

## FINOS-DET-004-007: Monitoring Resource Utilization and System Health

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use Resource Utilization and System Health for logging and monitoring, which entails consumption of computational resources (CPU, GPU, memory, disk I/O), network bandwidth utilization and latency, and health status and operational logs from underlying infrastructure (servers, containers, orchestrators).

**Source Text:** Resource Utilization and System Health:
Consumption of computational resources (CPU, GPU, memory, disk I/O).
Network bandwidth utilization and latency.
Health status and operational logs from underlying infrastructure (servers, containers, orchestrators).

---

## FINOS-DET-004-008: Monitoring Security-Specific Events and Access Control Violations

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use Security-Specific Events for logging and monitoring, which includes authentication and authorization events (both successes and failures), alerts and events from integrated security tools (e.g., AI Firewall, Data Leakage Prevention systems, intrusion detection systems), and detected access control policy violations or attempts.

**Source Text:** Security-Specific Events:
Authentication and authorization events (both successes and failures).
Alerts and events from integrated security tools (e.g., AI Firewall, Data Leakage Prevention systems, intrusion detection systems).
Detected access control policy violations or attempts.

---

## FINOS-DET-004-009: Logging Versioning Information for AI Models and System Components

**Section:** Implementation Guidance

**Subsection:** Identify Key Data Points for Logging and Monitoring

**Responsible Party:** System Owners

**Control Text:** System owners may use Versioning Information for logging and monitoring, which means that they must log the versions of AI models, datasets, key software libraries, and system components active during any given operation or event. This is crucial for diagnosing version-specific issues and understanding behavioral changes (e.g., model drift due to an update).

**Source Text:** Versioning Information:
Log the versions of AI models, datasets, key software libraries, and system components active during any given operation or event. This is crucial for diagnosing version-specific issues and understanding behavioral changes (e.g., model drift due to an update).

---

## FINOS-DET-004-010: Using Robust Logging Libraries for Structured Log Generation

**Section:** Implementation Guidance

**Subsection:** Implement Appropriate Tooling and Architecture

**Responsible Party:** System Owners

**Control Text:** System owners must utilize robust logging libraries within AI applications and infrastructure components to generate structured and informative log data.

**Source Text:** Logging Frameworks & Libraries: Utilize robust logging libraries within AI applications and infrastructure components to generate structured and informative log data.

---

## FINOS-DET-004-011: Centralizing Log Aggregation for Analysis and Retention

**Section:** Implementation Guidance

**Subsection:** Implement Appropriate Tooling and Architecture

**Responsible Party:** System Owners

**Control Text:** System owners must aggregate logs from all components into a centralized system (e.g., SIEM, specialized log management platforms) to facilitate efficient searching, analysis, correlation, and long-term retention.

**Source Text:** Centralized Log Management: Aggregate logs from all components into a centralized system (e.g., SIEM, specialized log management platforms) to facilitate efficient searching, analysis, correlation, and long-term retention.

---

## FINOS-DET-004-012: Visualizing Metrics and Events Through Dashboards and Monitoring Tools

**Section:** Implementation Guidance

**Subsection:** Implement Appropriate Tooling and Architecture

**Responsible Party:** System Owners

**Control Text:** System owners must employ dashboards and visualization tools to display key metrics, operational trends, system health, and security events in real-time or near real-time.

**Source Text:** Monitoring and Visualization Platforms: Employ dashboards and visualization tools to display key metrics, operational trends, system health, and security events in real-time or near real-time.

---

## FINOS-DET-004-013: Configuring Automated Alerts for Critical Events and Deviations

**Section:** Implementation Guidance

**Subsection:** Implement Appropriate Tooling and Architecture

**Responsible Party:** System Owners

**Control Text:** System owners must configure automated alerts based on predefined thresholds, significant deviations from baselines, critical errors, or specific security event signatures (linking to concepts such as MI-9 Alerting / DoW spend alert).

**Source Text:** Alerting Mechanisms: Configure automated alerts based on predefined thresholds, significant deviations from baselines, critical errors, or specific security event signatures (linking to concepts such as MI-9 Alerting / DoW spend alert).

---

## FINOS-DET-004-014: Implementing Distributed Tracing for Complex AI Systems

**Section:** Implementation Guidance

**Subsection:** Implement Appropriate Tooling and Architecture

**Responsible Party:** System Owners

**Control Text:** System owners must implement distributed tracing capabilities to map end-to-end request flows, identify performance bottlenecks, and understand component dependencies, for complex AI systems composed of multiple interacting microservices.

**Source Text:** Distributed Tracing: For complex AI systems composed of multiple interacting microservices, implement distributed tracing capabilities to map end-to-end request flows, identify performance bottlenecks, and understand component dependencies.

---

## FINOS-DET-004-015: Achieving Holistic Monitoring Across AI System Components

**Section:** Implementation Guidance

**Subsection:** Implement Appropriate Tooling and Architecture

**Responsible Party:** System Owners

**Control Text:** System owners must consider solutions that enable monitoring and correlation of activities across various inputs, outputs, and components simultaneously to achieve a holistic architectural view.


**Source Text:** Horizontal Monitoring Solutions: Consider solutions that enable monitoring and correlation of activities across various inputs, outputs, and components simultaneously to achieve a holistic architectural view.


---

## FINOS-DET-004-016: Establishing Baselines for Performance and Resource Utilization Metrics

**Section:** Implementation Guidance

**Subsection:** Establish Baselines and Implement Anomaly Detection

**Responsible Party:** System Owners

**Control Text:** System owners must collect observability data over a sufficient period under normal operating conditions to establish baselines for key performance, behavioral, and resource utilization metrics.

**Source Text:** Baseline Definition: Collect observability data over a sufficient period under normal operating conditions to establish baselines for key performance, behavioral, and resource utilization metrics.

---

## FINOS-DET-004-017: Detecting Anomalies Through Statistical or Machine Learning Techniques

**Section:** Implementation Guidance

**Subsection:** Establish Baselines and Implement Anomaly Detection

**Responsible Party:** System Owners

**Control Text:** System owners must implement methods (ranging from statistical approaches to machine learning-based techniques) to automatically detect significant deviations from these established baselines. Anomalies can indicate performance issues, emerging security threats, data drift, or unexpected model behavior.

**Source Text:** Anomaly Detection Techniques: Implement methods (ranging from statistical approaches to machine learning-based techniques) to automatically detect significant deviations from these established baselines. Anomalies can indicate performance issues, emerging security threats, data drift, or unexpected model behavior.

---

## FINOS-DET-004-018: Defining Policies for Retention and Archival of Observability Data

**Section:** Implementation Guidance

**Subsection:** Define Data Retention and Archival Policies

**Responsible Party:** System Owners

**Control Text:** System owners must formulate and implement clear policies for the retention and secure archival of observability data, balancing operational needs (e.g., troubleshooting, trend analysis), regulatory requirements (e.g., audit trails), and storage cost considerations.


**Source Text:** Formulate and implement clear policies for the retention and secure archival of observability data, balancing operational needs (e.g., troubleshooting, trend analysis), regulatory requirements (e.g., audit trails), and storage cost considerations.


---

## FINOS-DET-004-019: Reviewing and Refining the Observability Strategy Periodically

**Section:** Implementation Guidance

**Subsection:** Ensure Regular Review and Iteration


**Responsible Party:** System Owners

**Control Text:** System owners must periodically review the effectiveness of the observability strategy, the relevance of data points being collected, the accuracy of alerting thresholds, and the utility of dashboards. Adapt and refine the observability setup as the AI system evolves, new risks are identified, or business and compliance requirements change.

**Source Text:** Periodically review the effectiveness of the observability strategy, the relevance of data points being collected, the accuracy of alerting thresholds, and the utility of dashboards. Adapt and refine the observability setup as the AI system evolves, new risks are identified, or business and compliance requirements change.

---

## FINOS-DET-009-001: Implementing Hard Spending Limits for Cloud and AI Service Usage

**Section:** Implementation Guidance

**Subsection:** Establish Financial Guardrails

**Responsible Party:** System Owners

**Control Text:** System owners must implement hard spending limits at the organizational level through payment providers or cloud service billing controls as an ultimate failsafe.

**Source Text:** Enterprise-Level Caps: Implement hard spending limits at the organizational level through payment providers or cloud service billing controls as an ultimate failsafe.

---

## FINOS-DET-009-002: Setting Cascading Budget Limits Across Organizational Levels

**Section:** Implementation Guidance

**Subsection:** Establish Financial Guardrails

**Responsible Party:** System Owners

**Control Text:** System owners must set up cascading budget limits from enterprise → department → project → individual user/API key levels.

**Source Text:** Hierarchical Budget Controls: Set up cascading budget limits from enterprise → department → project → individual user/API key levels.

---

## FINOS-DET-009-003: Configuring Automatic Suspension or Throttling at Spending Thresholds

**Section:** Implementation Guidance

**Subsection:** Establish Financial Guardrails


**Responsible Party:** System Owners

**Control Text:** System owners must configure automatic service suspension or throttling when predefined spending thresholds are reached.

**Source Text:** Automated Spend Cutoffs: Configure automatic service suspension or throttling when predefined spending thresholds are reached.

---

## FINOS-DET-009-004: Monitoring AI Service Consumption Costs in Real Time

**Section:** Implementation Guidance

**Subsection:** Real-time Monitoring and Alerting

**Responsible Party:** System Owners

**Control Text:** System owners must implement real-time monitoring of AI service consumption costs across all services, projects, and users.

**Source Text:** Cost Tracking: Implement real-time monitoring of AI service consumption costs across all services, projects, and users.

---

## FINOS-DET-009-005: Configuring Multi-Level Spending Alerts with Escalation Procedures

**Section:** Implementation Guidance

**Subsection:** Real-time Monitoring and Alerting

**Responsible Party:** System Owners

**Control Text:** System owners must configure alerts at multiple spending levels (e.g., 50%, 75%, 90%, 100% of budget) with escalating notification procedures.

**Source Text:** Multi-Threshold Alerts: Configure alerts at multiple spending levels (e.g., 50%, 75%, 90%, 100% of budget) with escalating notification procedures.

---

## FINOS-DET-009-006: Detecting Unusual Spending Patterns and Malicious Activity

**Section:** Implementation Guidance

**Subsection:** Real-time Monitoring and Alerting

**Responsible Party:** System Owners

**Control Text:** System owners must deploy systems to detect unusual spending patterns that might indicate malicious activity or system malfunction.

**Source Text:** Anomaly Detection: Deploy systems to detect unusual spending patterns that might indicate malicious activity or system malfunction.

---

## FINOS-DET-009-007: Implementing Per-Key Quotas and Resource Limits via API Gateways

**Section:** Implementation Guidance

**Subsection:** Granular Resource Controls

**Responsible Party:** System Owners

**Control Text:** System owners must use API gateways to implement per-key quotas for request rate limits (requests per minute/hour), token consumption limits (for LLM services), and compute resource consumption caps.

**Source Text:** API Key Management: Use API gateways to implement per-key quotas for:
Request rate limits (requests per minute/hour)
Token consumption limits (for LLM services)
Compute resource consumption caps

---

## FINOS-DET-009-008: Setting Individual User Spending and Usage Limits by Role

**Section:** Implementation Guidance

**Subsection:** Granular Resource Controls

**Responsible Party:** System Owners

**Control Text:** System owners must implement individual user spending and usage limits based on roles and business needs.

**Source Text:** User-Based Quotas: Implement individual user spending and usage limits based on roles and business needs.

---

## FINOS-DET-009-009: Defining Project-Level Resource Quotas to Prevent Overconsumption

**Section:** Implementation Guidance

**Subsection:** Granular Resource Controls

**Responsible Party:** System Owners

**Control Text:** System owners must set resource quotas at the project or environment level to prevent any single initiative from consuming excessive resources.

**Source Text:** Project-Level Controls: Set resource quotas at the project or environment level to prevent any single initiative from consuming excessive resources.

---

## FINOS-DET-009-010: Attributing AI Resource Usage to Business Units and Cost Centers

**Section:** Implementation Guidance

**Subsection:** Usage Attribution and Accountability

**Responsible Party:** System Owners

**Control Text:** System owners must ensure all AI resource consumption can be attributed to specific business units or cost centers, projects or applications, individual users or service accounts, and specific use cases or workloads.

**Source Text:** Cost Attribution: Ensure all AI resource consumption can be attributed to specific:
Business units or cost centers
Projects or applications
Individual users or service accounts
Specific use cases or workloads

---

## FINOS-DET-009-011: Implementing Internal Chargeback Systems for AI Costs

**Section:** Implementation Guidance

**Subsection:** Usage Attribution and Accountability

**Responsible Party:** System Owners

**Control Text:** System owners must implement internal chargeback systems to allocate AI costs to the appropriate business units.

**Source Text:** Chargeback Mechanisms: Implement internal chargeback systems to allocate AI costs to the appropriate business units.

---

## FINOS-DET-009-012: Analyzing Spending Patterns for Optimization and Forecasting

**Section:** Implementation Guidance

**Subsection:** Proactive Management and Optimization

**Responsible Party:** System Owners

**Control Text:** System owners must regularly analyze spending patterns to identify optimization opportunities and predict future resource needs.

**Source Text:** Usage Analytics: Regularly analyze spending patterns to identify optimization opportunities and predict future resource needs.

---

## FINOS-DET-009-013: Evaluating Alignment of AI Resource Allocations with Business Needs

**Section:** Implementation Guidance

**Subsection:** Proactive Management and Optimization

**Responsible Party:** System Owners

**Control Text:** System owners must continuously evaluate whether AI resource allocations match actual business requirements.

**Source Text:** Right-sizing: Continuously evaluate whether AI resource allocations match actual business requirements.

---

## FINOS-DET-009-014: Optimizing Pricing and Contract Terms with AI Service Providers

**Section:** Implementation Guidance

**Subsection:** Proactive Management and Optimization

**Responsible Party:** System Owners

**Control Text:** System owners must monitor and negotiate with AI service providers to optimize pricing and contract terms.

**Source Text:** Vendor Management: Monitor and negotiate with AI service providers to optimize pricing and contract terms.

---

## FINOS-DET-011-001: Documenting Intended Uses of Collected Feedback Data

**Section:** Implementation Guidance

**Subsection:** Designing the Feedback Mechanism

**Responsible Party:** System Owners

**Control Text:** System owners must clearly document how feedback data will be utilized, such as for prompt fine-tuning, RAG document updates, model/data drift detection, or more advanced uses like Reinforcement Learning from Human Feedback (RLHF).

**Source Text:** Objectives: Clearly document how feedback data will be utilized, such as for prompt fine-tuning, RAG document updates, model/data drift detection, or more advanced uses like Reinforcement Learning from Human Feedback (RLHF).

---

## FINOS-DET-011-002: Designing Feedback Questions Aligned with Key Performance Indicators

**Section:** Implementation Guidance

**Subsection:** Designing the Feedback Mechanism

**Responsible Party:** System Owners

**Control Text:** System owners must design feedback questions and metrics to align with the solution’s key performance indicators (KPIs). For example, if accuracy is a KPI, feedback might involve users or SMEs annotating if an answer was correct.

**Source Text:** KPI Alignment: Design feedback questions and metrics to align with the solution’s key performance indicators (KPIs). For example, if accuracy is a KPI, feedback might involve users or SMEs annotating if an answer was correct.

---

## FINOS-DET-011-003: Ensuring Feedback Mechanisms Are Simple and Non-Disruptive

**Section:** Implementation Guidance

**Subsection:** Designing the Feedback Mechanism

**Responsible Party:** System Owners

**Control Text:** System owners must ensure the feedback mechanism (e.g., buttons, forms, comment boxes) is simple, intuitive, and does not significantly hamper the user’s primary task.

**Source Text:** Ease of Use: Ensure the feedback mechanism (e.g., buttons, forms, comment boxes) is simple, intuitive, and does not significantly hamper the user’s primary task.

---

## FINOS-DET-011-004: Assessing User Willingness and Effort Required to Provide Feedback

**Section:** Implementation Guidance

**Subsection:** Designing the Feedback Mechanism

**Responsible Party:** System Owners

**Control Text:** System owners must gauge the target audience’s willingness to provide feedback; make it optional and low-effort where possible.

**Source Text:** Willingness to Participate: Gauge the target audience’s willingness to provide feedback; make it optional and low-effort where possible.

---

## FINOS-DET-011-005: Collecting Broad User Feedback for General Insights

**Section:** Implementation Guidance

**Subsection:** Designing the Feedback Mechanism

**Responsible Party:** System Owners

**Control Text:** System owners must collect feedback from the general user base, and it must be suitable for broad insights and identifying common issues.

**Source Text:** Wide Feedback: Collect feedback from the general user base. Suitable for broad insights and identifying common issues.

---

## FINOS-DET-011-006: Engaging Expert Testers or SMEs for Specialized Feedback

**Section:** Implementation Guidance

**Subsection:** Designing the Feedback Mechanism

**Responsible Party:** System Owners

**Control Text:** System owners must create a smaller, dedicated group of expert testers or SMEs for scenarios where general user feedback might be disruptive or if highly specialized input is needed. These SMEs can provide continuous, detailed feedback directly to development teams.

**Source Text:** Narrow Feedback: For scenarios where general user feedback might be disruptive or if highly specialized input is needed, create a smaller, dedicated group of expert testers or SMEs. These SMEs can provide continuous, detailed feedback directly to development teams.

---

## FINOS-DET-011-007: Collecting Structured Quantitative Feedback for Performance Measurement

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Quantitative Feedback

**Control Text:** System owners that use quatitative feedback must collect structured responses that can be easily aggregated and measured, such as numerical ratings (e.g., “Rate this response on a scale of 1-5 for helpfulness”), categorical choices (e.g., “Was this answer: Correct/Incorrect/Partially Correct”), or binary responses (e.g., thumbs up/down).

**Source Text:** Description: Involves collecting structured responses that can be easily aggregated and measured, such as numerical ratings (e.g., “Rate this response on a scale of 1-5 for helpfulness”), categorical choices (e.g., “Was this answer: Correct/Incorrect/Partially Correct”), or binary responses (e.g., thumbs up/down).

---

## FINOS-DET-011-008: Using Quantitative Feedback to Track Trends and KPI Alignment

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Quantitative Feedback

**Control Text:** System owners that use quatitative feedback must realize that it's use is effective for tracking trends, measuring against KPIs, and quickly identifying areas of high or low performance.

**Source Text:** Use Cases: Effective for tracking trends, measuring against KPIs, and quickly identifying areas of high or low performance.

---

## FINOS-DET-011-009: Enabling Qualitative Feedback for Detailed User Insights

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Qualitative Feedback

**Control Text:** System owners that use qualitative feedback must ensure that this method consists of open-ended, free-form text responses where users can provide detailed comments, explanations, or describe nuanced issues not captured by quantitative metrics.

**Source Text:** Description: Consists of open-ended, free-form text responses where users can provide detailed comments, explanations, or describe nuanced issues not captured by quantitative metrics.

---

## FINOS-DET-011-010: Using Qualitative Feedback to Identify Issues and Analyze AI Behavior

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Qualitative Feedback

**Control Text:** System owners that use qualitative feedback must realize that it's use offers rich insights into user reasoning, identifies novel problems, and provides specific examples of AI behavior. Natural Language Processing (NLP) techniques or even other LLMs can be employed to analyze and categorize this textual feedback at scale.

**Source Text:** Use Cases: Offers rich insights into user reasoning, identifies novel problems, and provides specific examples of AI behavior. Natural Language Processing (NLP) techniques or even other LLMs can be employed to analyze and categorize this textual feedback at scale.

---

## FINOS-DET-011-011: Collecting and Analyzing Implicit Feedback from User Interactions

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Implicit Feedback

**Control Text:** System owners that use implicit feedback must ensure that its derived indirectly from user actions rather than explicit submissions, e.g., whether a user accepts or ignores an AI suggestion, time spent on an AI-generated summary, or if a user immediately rephrases a query after an unsatisfactory response.

**Source Text:** Description: Derived indirectly from user actions rather than explicit submissions, e.g., whether a user accepts or ignores an AI suggestion, time spent on an AI-generated summary, or if a user immediately rephrases a query after an unsatisfactory response.

---

## FINOS-DET-011-012: Leveraging Implicit Feedback to Measure User Satisfaction at Scale

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Implicit Feedback

**Control Text:** System owners that use implicit feedback must realize that it's use can provide large-scale, less biased indicators of user satisfaction or task success.

**Source Text:** Use Cases: Can provide large-scale, less biased indicators of user satisfaction or task success.

---

## FINOS-DET-011-013: Establishing Multiple Channels for Feedback Collection

**Section:** Implementation Guidance

**Subsection:** Types of Feedback and Collection Methods

**Responsible Party:** System Owners that use Channels for Collection

**Control Text:** System owners that use channels for collection must ensure that it in-application widgets (e.g., rating buttons, feedback forms), dedicated reporting channels or email addresses, user surveys, facilitated feedback sessions with SMEs or user groups, and mechanisms for users to report concerns about adverse impacts or ethical issues (aligns with ISO 42001 A.8.3, A.3.3).
 

**Source Text:** Channels for Collection:
In-application widgets (e.g., rating buttons, feedback forms).
Dedicated reporting channels or email addresses.
User surveys.
Facilitated feedback sessions with SMEs or user groups.
Mechanisms for users to report concerns about adverse impacts or ethical issues (aligns with ISO 42001 A.8.3, A.3.3).


---

## FINOS-DET-011-014: Aggregating and Analyzing Quantitative and Qualitative Feedback Regularly

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must implement processes for regularly collecting, aggregating, and analyzing both quantitative and qualitative feedback.


**Source Text:** Systematic Analysis: Implement processes for regularly collecting, aggregating, and analyzing both quantitative and qualitative feedback.


---

## FINOS-DET-011-015: Refining Prompts Based on Feedback from LLM Responses

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must use feedback on LLM responses to identify weaknesses in prompts and iteratively refine them to improve clarity, relevance, and safety.

**Source Text:** Prompt Engineering and Fine-tuning: Use feedback on LLM responses to identify weaknesses in prompts and iteratively refine them to improve clarity, relevance, and safety.

---

## FINOS-DET-011-016: Identifying Knowledge Base Deficiencies Through RAG Feedback

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must examine low-rated responses from RAG systems to pinpoint deficiencies in the underlying knowledge base, signaling opportunities for content updates, corrections, or additions.

**Source Text:** RAG System Improvement: Examine low-rated responses from RAG systems to pinpoint deficiencies in the underlying knowledge base, signaling opportunities for content updates, corrections, or additions.

---

## FINOS-DET-011-017: Tracking Feedback Metrics to Detect Model or Data Drift

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must track feedback metrics over time to quantitatively detect degradation in model performance or shifts in output quality that might indicate model drift (due to changes in the foundational model version - addresses ri-11) or data drift (due to changes in input data characteristics).

**Source Text:** Model and Data Drift Detection: Track feedback metrics over time to quantitatively detect degradation in model performance or shifts in output quality that might indicate model drift (due to changes in the foundational model version - addresses ri-11) or data drift (due to changes in input data characteristics).

---

## FINOS-DET-011-018: Using Feedback to Detect Security Issues and Prompt Injection Attempts

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that user feedback can be an invaluable source for detecting instances where AI systems have been successfully manipulated (e.g., prompt injection), have leaked sensitive information, or exhibit other security flaws.

**Source Text:** Identifying Security Vulnerabilities: User feedback can be an invaluable source for detecting instances where AI systems have been successfully manipulated (e.g., prompt injection), have leaked sensitive information, or exhibit other security flaws.

---

## FINOS-DET-011-019: Providing Channels for Reporting Biased or Unethical AI Outputs

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must provide a channel for users to report outputs they perceive as biased, unfair, inappropriate, or ethically problematic.

**Source Text:** Highlighting Ethical Concerns and Bias: Provide a channel for users to report outputs they perceive as biased, unfair, inappropriate, or ethically problematic.

---

## FINOS-DET-011-020: Using Feedback to Improve User Guidance and System Documentation

**Section:** Implementation Guidance

**Subsection:** Processing and Utilizing Feedback

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that feedback can highlight areas where user guidance or system documentation (as per ISO 42001 A.8.2) needs improvement.

**Source Text:** Improving User Documentation and Training: Feedback can highlight areas where user guidance or system documentation (as per ISO 42001 A.8.2) needs improvement.

---

## FINOS-DET-011-021: Understanding Reinforcement Learning from Human Feedback (RLHF) Techniques

**Section:** Implementation Guidance

**Subsection:** Advanced Feedback Integration: Reinforcement Learning from Human Feedback (RLHF)

**Responsible Party:** System Owners using RLHF

**Control Text:** System owners using RLHF must know that it is an advanced machine learning technique where AI models, particularly LLMs, are further refined using direct human judgments on their outputs, instead of solely relying on pre-existing data, human evaluators assess model responses (e.g., rating helpfulness, correctness, safety, adherence to instructions). This feedback must then be used to systematically adjust the model’s internal decision-making processes, effectively “rewarding” desired behaviors and “penalizing” undesired ones. 

**Source Text:** Conceptual Overview for Risk Audience: RLHF is an advanced machine learning technique where AI models, particularly LLMs, are further refined using direct human judgments on their outputs. Instead of solely relying on pre-existing data, human evaluators assess model responses (e.g., rating helpfulness, correctness, safety, adherence to instructions). This feedback is then used to systematically adjust the model’s internal decision-making processes, effectively “rewarding” desired behaviors and “penalizing” undesired ones.

---

## FINOS-DET-011-022: Aligning AI Model Behavior with Human Preferences and Ethics

**Section:** Implementation Guidance

**Subsection:** Advanced Feedback Integration: Reinforcement Learning from Human Feedback (RLHF)

**Responsible Party:** System Owners using RLHF

**Control Text:** System owners using RLHF must realize that the primary goal of RLHF is to better align the AI model’s behavior with human goals, nuanced preferences, ethical considerations, and complex instructions that are hard to specify in traditional training datasets.

**Source Text:** Key Objective: The primary goal of RLHF is to better align the AI model’s behavior with human goals, nuanced preferences, ethical considerations, and complex instructions that are hard to specify in traditional training datasets.

---

## FINOS-DET-011-023: Collecting Human Evaluations to Train Reward Models

**Section:** Implementation Guidance

**Subsection:** Advanced Feedback Integration: Reinforcement Learning from Human Feedback (RLHF)

**Responsible Party:** System Owners

**Control Text:** System owners must systematically gather human evaluations on model outputs for a diverse set of inputs. This feedback is often used to train a separate “reward model” that learns to predict human preferences.

**Source Text:** Feedback Collection: Systematically gather human evaluations on model outputs for a diverse set of inputs. Reward Modeling: This feedback is often used to train a separate “reward model” that learns to predict human preferences.

---

## FINOS-DET-011-024: Fine-Tuning AI Models Using Reinforcement Learning Guided by Reward Models

**Section:** Implementation Guidance

**Subsection:** Advanced Feedback Integration: Reinforcement Learning from Human Feedback (RLHF)

**Responsible Party:** System Owners

**Control Text:** System owners must make sure that the primary AI model is then fine-tuned using reinforcement learning techniques, with the reward model providing signals to guide its learning towards generating more highly-rated outputs

**Source Text:** Policy Optimization: The primary AI model is then fine-tuned using reinforcement learning techniques, with the reward model providing signals to guide its learning towards generating more highly-rated outputs

---

## FINOS-DET-011-025: Improving Model Safety and Instruction Adherence Through RLHF

**Section:** Implementation Guidance

**Subsection:** Advanced Feedback Integration: Reinforcement Learning from Human Feedback (RLHF)

**Responsible Party:** System Owners

**Control Text:** System owners using RLHF must recognize that it can significantly improve model safety, reduce the generation of harmful or biased content, and enhance the model’s ability to follow instructions faithfully.

**Source Text:** Benefits for Control: RLHF can significantly improve model safety, reduce the generation of harmful or biased content, and enhance the model’s ability to follow instructions faithfully.

---

## FINOS-DET-011-026: Maintaining Human Feedback Loops Alongside LLM-as-a-Judge Systems

**Section:** Implementation Guidance

**Subsection:** Integration with “LLM-as-a-Judge” Concepts

**Responsible Party:** System Owners

**Control Text:** System owners may acknowledge that as organizations explore using LLMs to evaluate the outputs of other LLMs (“LLM-as-a-Judge” - see CT-15), human feedback loops remain essential.

**Source Text:** Context: As organizations explore using LLMs to evaluate the outputs of other LLMs (“LLM-as-a-Judge” - see CT-15), human feedback loops remain essential.

---

## FINOS-DET-011-027: Collecting and Comparing Human and LLM Judge Feedback for Calibration

**Section:** Implementation Guidance

**Subsection:** Integration with “LLM-as-a-Judge” Concepts

**Responsible Party:** System Owners

**Control Text:** System owners must implement mechanisms for humans (especially SMEs) to provide quantitative and qualitative feedback on the judgments made by these LLM judges. This allows for comparison of feedback quality and consistency between human SMEs and LLM judges, calibration and evaluation of the LLM-as-a-Judge system’s effectiveness and reliability, and targeted human review (narrow feedback) on a sample of LLM-as-a-Judge results, with sample size and methodology dependent on the use-case criticality.


**Source Text:** Application: Implement mechanisms for humans (especially SMEs) to provide quantitative and qualitative feedback on the judgments made by these LLM judges.

---

## FINOS-DET-011-029: Defining Roles and Responsibilities for Feedback Management

**Section:** Implementation Guidance

**Subsection:** Feedback Review, Actioning, and Governance Process

**Responsible Party:** System Owners

**Control Text:** System owners must assign clear roles and responsibilities for collecting, reviewing, triaging, and actioning feedback (e.g., product owners, MLOps teams, data science teams, AI governance committees).

**Source Text:** Defined Responsibilities: Assign clear roles and responsibilities for collecting, reviewing, triaging, and actioning feedback (e.g., product owners, MLOps teams, data science teams, AI governance committees).

---

## FINOS-DET-011-030: Prioritizing Feedback Based on Severity and Strategic Impact

**Section:** Implementation Guidance

**Subsection:** Feedback Review, Actioning, and Governance Process

**Responsible Party:** System Owners

**Control Text:** System owners must establish a process to categorize and prioritize incoming feedback based on severity, frequency, potential impact, and alignment with strategic goals.

**Source Text:** Triage and Prioritization: Establish a process to categorize and prioritize incoming feedback based on severity, frequency, potential impact, and alignment with strategic goals.

---

## FINOS-DET-011-031: Tracking Feedback Actions and Outcomes

**Section:** Implementation Guidance

**Subsection:** Feedback Review, Actioning, and Governance Process

**Responsible Party:** System Owners

**Control Text:** System owners must implement a system to track feedback items, the actions taken in response, and their outcomes.

**Source Text:** Tracking and Resolution: Implement a system to track feedback items, the actions taken in response, and their outcomes.

---

## FINOS-DET-011-032: Communicating Feedback Utilization and Resulting Improvements to Users

**Section:** Implementation Guidance

**Subsection:** Feedback Review, Actioning, and Governance Process

**Responsible Party:** System Owners

**Control Text:** System owners must inform users or feedback providers about how their input has been used or what changes have been made, fostering a sense of engagement, when appropriate and feasible. (Supports ISO 42001 A.6.2.6 for repairs/updates based on feedback).

**Source Text:** Closing the Loop: Where appropriate and feasible, inform users or feedback providers about how their input has been used or what changes have been made, fostering a sense of engagement. (Supports ISO 42001 A.6.2.6 for repairs/updates based on feedback).

---

## FINOS-DET-013-001: Maintaining Traceable Links Between Retrieved Chunks and Generated Outputs

**Section:** Implementation Guidance

**Subsection:** Designing AI Systems for Citability (Especially RAG Systems)

**Responsible Party:** System Owners with RAG

**Control Text:** System owners with RAG systems must ensure that the pipeline maintains a robust and auditable link between the specific “chunks” of text retrieved from knowledge bases and the segments of the generated output that are based on those chunks. This linkage is fundamental for accurate citation.

**Source Text:** Source Tracking in RAG Pipelines: For RAG systems, it is essential that the pipeline maintains a robust and auditable link between the specific “chunks” of text retrieved from knowledge bases and the segments of the generated output that are based on those chunks. This linkage is fundamental for accurate citation.

---

## FINOS-DET-013-002: Developing Strategies for Document Chunking and Unique Identification

**Section:** Implementation Guidance

**Subsection:** Designing AI Systems for Citability (Especially RAG Systems)

**Responsible Party:** System Owners

**Control Text:** System owners must develop and implement appropriate strategies for breaking down source documents into smaller, uniquely identifiable, and addressable “chunks” that can be precisely referenced in citations.

**Source Text:** Optimal Content Chunking Strategies: Develop and implement appropriate strategies for breaking down source documents into smaller, uniquely identifiable, and addressable “chunks” that can be precisely referenced in citations.

---

## FINOS-DET-013-003: Preserving Source Metadata for Accurate and Meaningful Citations

**Section:** Implementation Guidance

**Subsection:** Designing AI Systems for Citability (Especially RAG Systems)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that relevant metadata from source documents (e.g., document titles, authors, original URLs, document IDs, page numbers, section headers, last updated dates) is ingested, preserved, and made available for constructing meaningful citations.

**Source Text:** Preservation and Use of Metadata: Ensure that relevant metadata from source documents (e.g., document titles, authors, original URLs, document IDs, page numbers, section headers, last updated dates) is ingested, preserved, and made available for constructing meaningful citations.

---

## FINOS-DET-013-004: Ensuring Stable Identifiers for Internal Source Content

**Section:** Implementation Guidance

**Subsection:** Designing AI Systems for Citability (Especially RAG Systems)

**Responsible Party:** System Owners

**Control Text:** System owners must ensure these systems have stable, persistent identifiers for content that can be reliably used in citations, when using internal data sources (e.g., company wikis, document management systems, databases).

**Source Text:** Internal Knowledge Base Integration: When using internal data sources (e.g., company wikis, document management systems, databases), ensure these systems have stable, persistent identifiers for content that can be reliably used in citations.

---

## FINOS-DET-013-005: Designing Clear Visual Indicators for Cited Information in the UI

**Section:** Implementation Guidance

**Subsection:** Presentation of Citations to Users

**Responsible Party:** System Owners

**Control Text:** System owners must implement clear and intuitive visual cues within the user interface to indicate that a piece of information is cited (e.g., footnotes, endnotes, inline numerical references, highlighted text with hover-over citation details, clickable icons or links).

**Source Text:** Clear Visual Indicators: Implement clear and intuitive visual cues within the user interface to indicate that a piece of information is cited (e.g., footnotes, endnotes, inline numerical references, highlighted text with hover-over citation details, clickable icons or links).

---

## FINOS-DET-013-006: Providing Users with Accessible Full Source Information for Citations

**Section:** Implementation Guidance

**Subsection:** Presentation of Citations to Users

**Responsible Party:** System Owners

**Control Text:** System owners must provide users with easy mechanisms to access the full source information corresponding to a citation. This might involve direct links to source documents (if hosted and accessible), display of relevant text snippets from the source within the UI, or clear references to find the source material offline.

**Source Text:** Accessible Source Information: Provide users with easy mechanisms to access the full source information corresponding to a citation. This might involve direct links to source documents (if hosted and accessible), display of relevant text snippets from the source within the UI, or clear references to find the source material offline.

---

## FINOS-DET-013-007: Displaying Relevant Source Snippets Alongside Citations

**Section:** Implementation Guidance

**Subsection:** Presentation of Citations to Users

**Responsible Party:** System Owners

**Control Text:** System owners must consider displaying a brief, relevant snippet of the cited source text directly alongside the citation. This can give users immediate context for the AI’s claim without requiring them to open and search the full source document.

**Source Text:** Contextual Snippets (Optional but Recommended): Consider displaying a brief, relevant snippet of the cited source text directly alongside the citation. This can give users immediate context for the AI’s claim without requiring them to open and search the full source document.

---

## FINOS-DET-013-008: Curating Reliable and Authoritative Sources for RAG Knowledge Bases

**Section:** Implementation Guidance

**Subsection:** Quality, Relevance, and Limitations of Citations

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that curation processes for RAG sources should aim to include reliable and appropriate materials. This is because, while the AI system provides the citation, the quality and authoritativeness of the underlying knowledge base are critical. 

**Source Text:** Source Vetting (Upstream Process): While the AI system provides the citation, the quality and authoritativeness of the underlying knowledge base are critical. Curation processes for RAG sources should aim to include reliable and appropriate materials.

---

## FINOS-DET-013-009: Indicating When Parametric or Synthesized Knowledge Is Used Instead of Direct Citations

**Section:** Implementation Guidance

**Subsection:** Quality, Relevance, and Limitations of Citations

**Responsible Party:** System Owners

**Control Text:** System owners must ensure that the system clearly indicates when a direct document-level citation is not applicable, if the AI generates content based on its general parametric knowledge (i.e., knowledge learned during its foundational training, not from a specific retrieved document) or if it highly synthesizes information from multiple sources in an abstractive manner. They must also avoid generating misleading or fabricated citations.

**Source Text:** Handling Uncitable or Abstractive Content: If the AI generates content based on its general parametric knowledge (i.e., knowledge learned during its foundational training, not from a specific retrieved document) or if it highly synthesizes information from multiple sources in an abstractive manner, the system should clearly indicate when a direct document-level citation is not applicable. Avoid generating misleading or fabricated citations.

---

## FINOS-DET-013-010: Evaluating Semantic Relevance and Confidence of Cited Sources

**Section:** Implementation Guidance

**Subsection:** Quality, Relevance, and Limitations of Citations

**Responsible Party:** System Owners

**Control Text:** System owners must implement mechanisms (potentially AI-assisted) to evaluate the semantic relevance of the specific cited source segment to the precise claim being made in the generated output, where technically feasible. They must also flag or provide confidence scores for citations where relevance might be lower.

**Source Text:** Assessing Citation Relevance: Where technically feasible, implement mechanisms (potentially AI-assisted) to evaluate the semantic relevance of the specific cited source segment to the precise claim being made in the generated output. Flag or provide confidence scores for citations where relevance might be lower.

---

## FINOS-DET-013-011: Monitoring and Managing Link Rot in Cited References

**Section:** Implementation Guidance

**Subsection:** Maintaining Citation Integrity Over Time

**Responsible Party:** System Owners

**Control Text:** System owners must implement strategies to monitor for and manage “link rot” (links becoming broken or leading to changed content) for citations that are URLs to external web pages or internal documents. 

**Source Text:** Managing “Link Rot”: For citations that are URLs to external web pages or internal documents, implement strategies to monitor for and manage “link rot” (links becoming broken or leading to changed content). This might involve periodic link checking, caching key cited public web content, or prioritizing the use of persistent identifiers like Digital Object Identifiers (DOIs) where available.

---

## FINOS-DET-013-012: Managing Link Rot Through Link Checking, Caching, and Persistent Identifiers

**Section:** Implementation Guidance

**Subsection:** Maintaining Citation Integrity Over Time

**Responsible Party:** System Owners

**Control Text:** System owners must complete periodic link checking, caching key cited public web content, or prioritizing the use of persistent identifiers like Digital Object Identifiers (DOIs) where available in order to manage "link rot" for citations that are URLs to external web pages or internal documents. 

**Source Text:** Managing “Link Rot”: For citations that are URLs to external web pages or internal documents, implement strategies to monitor for and manage “link rot” (links becoming broken or leading to changed content). This might involve periodic link checking, caching key cited public web content, or prioritizing the use of persistent identifiers like Digital Object Identifiers (DOIs) where available.

---

## FINOS-DET-013-013: Defining Citation Behavior for Updated or Versioned Source Documents

**Section:** Implementation Guidance

**Subsection:** Maintaining Citation Integrity Over Time

**Responsible Party:** System Owners

**Control Text:** System owners must establish a clear strategy for how citations will behave if the underlying source documents are updated, versioned, or archived. System owners must make sure that citations point to the specific version of the source material used at the time the AI generated the information, or at least clearly indicate if a source has been updated since citation.

**Source Text:** Versioning of Source Documents: Establish a clear strategy for how citations will behave if the underlying source documents are updated, versioned, or archived. Ideally, citations should point to the specific version of the source material used at the time the AI generated the information, or at least clearly indicate if a source has been updated since citation.

---

## FINOS-DET-013-014: Providing User Guidance on Citation Generation and Interpretation

**Section:** Implementation Guidance

**Subsection:** User Education and Guidance (as per ISO 42001 A.8.2)

**Responsible Party:** System Owners

**Control Text:** System owners must provide users with clear, accessible information and guidance on; how the AI system generates and presents citations, how to interpret and use citations to verify information, and the limitations of citations (e.g., a citation indicates the source of a statement, not necessarily a validation of the source’s absolute truth, quality, or currentness).

**Source Text:** Provide users with clear, accessible information and guidance on:
How the AI system generates and presents citations.
How to interpret and use citations to verify information.
The limitations of citations (e.g., a citation indicates the source of a statement, not necessarily a validation of the source’s absolute truth, quality, or currentness).

---

## FINOS-DET-013-015: Documenting Citation Mechanisms, Source Types, and Known Limitations

**Section:** Implementation Guidance

**Subsection:** Technical Documentation (as per ISO 42001 A.6.2.7)

**Responsible Party:** Internal technical teams, auditors, or regulators

**Control Text:** Internal technical teams, auditors, or regulators, must ensure that AI system documentation clearly describes; the citation generation mechanism and its logic, the types of sources included in the knowledge base and how they are referenced, and any known limitations or potential inaccuracies in the citation process.

**Source Text:** For internal technical teams, auditors, or regulators, ensure that AI system documentation clearly describes:
The citation generation mechanism and its logic.
The types of sources included in the knowledge base and how they are referenced.
Any known limitations or potential inaccuracies in the citation process.

---

## FINOS-DET-015-001: Defining Evaluation Criteria for Primary AI Outputs

**Section:** Implementation Guidance

**Subsection:** Defining the Evaluation Task and Criteria

**Responsible Party:** System Owners 

**Control Text:** System owners must clearly articulate what aspects of the primary AI’s output needs to be evaluated (e.g., is it about factual correctness in a RAG system, adherence to safety guidelines, stylistic consistency, absence of PII?).

**Source Text:** Specify Evaluation Goals: Clearly articulate what aspects of the primary AI’s output need to be evaluated (e.g., is it about factual correctness in a RAG system, adherence to safety guidelines, stylistic consistency, absence of PII?).

---

## FINOS-DET-015-002: Creating Detailed Rubrics and Constitutions for Judge LLMs

**Section:** Implementation Guidance

**Subsection:** Defining the Evaluation Task and Criteria

**Responsible Party:** System Owners 

**Control Text:** System owners must create precise instructions, rubrics, or “constitutions” for the “judge” LLM. For example, in a RAG use case, an evaluator LLM might be presented with a source document, a user’s question, the primary RAG system’s answer, and then asked to assess if the answer is factually consistent with the source document and to explain its reasoning.

**Source Text:** Develop Detailed Rubrics/Guidelines: Create precise instructions, rubrics, or “constitutions” for the “judge” LLM. For example, in a RAG use case, an evaluator LLM might be presented with a source document, a user’s question, the primary RAG system’s answer, and then asked to assess if the answer is factually consistent with the source document and to explain its reasoning.

---

## FINOS-DET-015-003: Specifying Output Formats for Judge LLM Evaluations

**Section:** Implementation Guidance

**Subsection:** Defining the Evaluation Task and Criteria

**Responsible Party:** System Owners 

**Control Text:** System owners must specify the desired output format from the “judge” LLM (e.g., a numerical score, a categorical label like “Compliant/Non-compliant,” a binary “True/False,” and/or a textual explanation).

**Source Text:** Define Output Format: Specify the desired output format from the “judge” LLM (e.g., a numerical score, a categorical label like “Compliant/Non-compliant,” a binary “True/False,” and/or a textual explanation).

---

## FINOS-DET-015-004: Selecting General-Purpose Foundation Models as Judge LLMs

**Section:** Implementation Guidance

**Subsection:** Selecting or Configuring the “Judge” LLM

**Responsible Party:** System Owners 

**Control Text:** System owners must choose or configure their system's "Judge" LLM. They may choose a mdoel to use powerful, general-purpose foundation models (e.g., GPT-4, Claude series) and configure them with carefully crafted prompts that encapsulate the evaluation criteria. Research suggests these can perform well as generalized and fair evaluators.


**Source Text:** Choice of Model: Options include:
Using powerful, general-purpose foundation models (e.g., GPT-4, Claude series) and configuring them with carefully crafted prompts that encapsulate the evaluation criteria. Research suggests these can perform well as generalized and fair evaluators.
Fine-tuning a smaller, more specialized LLM for specific, repetitive evaluation tasks if cost or latency is a major concern (though this may sacrifice some generality).

---

## FINOS-DET-015-005: Fine-Tuning Specialized Judge LLMs for Targeted Evaluation Tasks

**Section:** Implementation Guidance

**Subsection:** Selecting or Configuring the “Judge” LLM

**Responsible Party:** System Owners 

**Control Text:** System owners must choose or confirgure their system's "Judge" LLM. They may choose a model to fine-tune a smaller, more specialized LLM for specific, repetitive evaluation tasks if cost or latency is a major concern (though this may sacrifice some generality).

**Source Text:** Choice of Model: Options include:
Using powerful, general-purpose foundation models (e.g., GPT-4, Claude series) and configuring them with carefully crafted prompts that encapsulate the evaluation criteria. Research suggests these can perform well as generalized and fair evaluators.
Fine-tuning a smaller, more specialized LLM for specific, repetitive evaluation tasks if cost or latency is a major concern (though this may sacrifice some generality).

---

## FINOS-DET-015-006: Developing Clear and Unambiguous Prompts for Judge LLMs

**Section:** Implementation Guidance

**Subsection:** Selecting or Configuring the “Judge” LLM

**Responsible Party:** System Owners 

**Control Text:** System owners must develop robust and unambiguous prompts that clearly instruct the “judge” LLM on its task, the criteria to use, and the format of its output.

**Source Text:** Prompt Engineering for the “Judge”: Develop robust and unambiguous prompts that clearly instruct the “judge” LLM on its task, the criteria to use, and the format of its output.

---

## FINOS-DET-015-007: Structuring Inputs and Context for Judge LLM Evaluations

**Section:** Implementation Guidance

**Subsection:** Designing and Executing the Evaluation Process


**Responsible Party:** System Owners 

**Control Text:** System owners must structure the input to the “judge” LLM, which includes: the output from the primary AI system that needs evaluation, the original input/prompt given to the primary AI, any relevant context (e.g., source documents for RAG, user persona, task instructions), and the evaluation criteria or rubric.

**Source Text:** Input Preparation: Structure the input to the “judge” LLM, which typically includes:
The output from the primary AI system that needs evaluation.
The original input/prompt given to the primary AI.
Any relevant context (e.g., source documents for RAG, user persona, task instructions).
The evaluation criteria or rubric.

---

## FINOS-DET-015-008: Determining Evaluation Frequency and Mode for Judge LLM Assessments

**Section:** Implementation Guidance

**Subsection:** Designing and Executing the Evaluation Process


**Responsible Party:** System Owners 

**Control Text:** System owners must decide whether evaluations will be done in batches (e.g., for testing sets or periodic sampling of production data) or in near real-time for ongoing monitoring (though this has higher cost and latency implications).

**Source Text:** Batch vs. Real-time Evaluation: Decide whether evaluations will be done in batches (e.g., for testing sets or periodic sampling of production data) or in near real-time for ongoing monitoring (though this has higher cost and latency implications).

---

## FINOS-DET-015-009: Measuring Judge LLM Performance Against Human SME Evaluations

**Section:** Implementation Guidance

**Subsection:** Evaluating and Calibrating the “Judge” LLM’s Performance

**Responsible Party:** System Owners 

**Control Text:** System owners must measure the "judge" LLM's performance against evaluations conducted by human Subject Matter Experts (SMEs) on a representative set of the primary AI’s outputs.


**Source Text:** Benchmarking Against Human Evaluation: The crucial step is to measure the “judge” LLM’s performance against evaluations conducted by human Subject Matter Experts (SMEs) on a representative set of the primary AI’s outputs.


---

## FINOS-DET-015-010: Using Classification Metrics to Assess Judge LLM Agreement with Humans

**Section:** Implementation Guidance

**Subsection:** Evaluating and Calibrating the “Judge” LLM’s Performance

**Responsible Party:** System Owners 

**Control Text:** System owners must use metrics like Accuracy, Precision, Recall, and F1-score to assess agreement with human labels if the judge provides categorical outputs (e.g., “Pass/Fail,” “Toxic/Non-toxic”). Analyzing the confusion matrix can reveal systematic errors or biases of the “judge.”

**Source Text:** Metrics for Judge Performance:
Classification Metrics: If the judge provides categorical outputs (e.g., “Pass/Fail,” “Toxic/Non-toxic”), use metrics like Accuracy, Precision, Recall, and F1-score to assess agreement with human labels. Analyzing the confusion matrix can reveal systematic errors or biases of the “judge.”

---

## FINOS-DET-015-011: Assessing Correlation Between Judge LLM and Human Scoring

**Section:** Implementation Guidance

**Subsection:** Evaluating and Calibrating the “Judge” LLM’s Performance

**Responsible Party:** System Owners 

**Control Text:** System owners must assess the correlation (e.g., Pearson, Spearman) between its scores and human-assigned scores if the judge provides numerical scores.

**Source Text:** Metrics for Judge Performance: Correlation Metrics: If the judge provides numerical scores, assess the correlation (e.g., Pearson, Spearman) between its scores and human-assigned scores.

---

## FINOS-DET-015-012: Refining and Calibrating Judge LLMs for Improved Alignment

**Section:** Implementation Guidance

**Subsection:** Evaluating and Calibrating the “Judge” LLM’s Performance

**Responsible Party:** System Owners 

**Control Text:** System owners must refine the “judge’s” prompts, adjust its configuration, or even consider a different “judge” model to improve its alignment with human judgments, based on the "Judge" LLMs calibration.

**Source Text:** Iterative Refinement: Based on this calibration, refine the “judge’s” prompts, adjust its configuration, or even consider a different “judge” model to improve its alignment with human judgments.

---

## FINOS-DET-015-013: Using Judge LLMs to Automate Testing and Regression Analysis

**Section:** Implementation Guidance

**Subsection:** Integrating “LLM-as-a-Judge” into AI System Lifecycles


**Responsible Party:** System Owners 

**Control Text:** System owners must use LLM-as-a-Judge to automate parts of model testing, compare different model versions or prompts, and identify regressions during development (supports ISO 42001 A.6.2.4).

**Source Text:** Development and Testing: Use LLM-as-a-Judge to automate parts of model testing, compare different model versions or prompts, and identify regressions during development (supports ISO 42001 A.6.2.4).

---

## FINOS-DET-015-014: Applying Judge LLMs to Monitor Live Production Outputs

**Section:** Implementation Guidance

**Subsection:** Integrating “LLM-as-a-Judge” into AI System Lifecycles


**Responsible Party:** System Owners 

**Control Text:** System owners must apply LLM-as-a-Judge to a sample of live production outputs to monitor for degradation in quality, emerging safety issues, or deviations from expected behavior over time (supports ISO 42001 A.6.2.6).

**Source Text:** Continuous Monitoring in Production: Apply LLM-as-a-Judge to a sample of live production outputs to monitor for degradation in quality, emerging safety issues, or deviations from expected behavior over time (supports ISO 42001 A.6.2.6).

---

## FINOS-DET-015-015: Leveraging Judge LLM Evaluations for Scalable Model Improvement

**Section:** Implementation Guidance

**Subsection:** Integrating “LLM-as-a-Judge” into AI System Lifecycles


**Responsible Party:** System Owners 

**Control Text:** System owners must acknowledge that the evaluations from the “judge” LLM can provide scalable feedback signals to help identify areas where the primary AI model or its surrounding application logic needs improvement.

**Source Text:** Feedback Loop for Primary Model Improvement: The evaluations from the “judge” LLM can provide scalable feedback signals to help identify areas where the primary AI model or its surrounding application logic needs improvement.

---

## FINOS-DET-015-016: Establishing Human Review Processes for Judge LLM Evaluations

**Section:** Implementation Guidance

**Subsection:** Ensuring Human Review and Escalation Pathways

**Responsible Party:** System Owners 

**Control Text:** System owners must establish clear processes for human review of the “judge” LLM’s evaluations, especially for:
outputs flagged as high-risk or problematic by the “judge", cases where the “judge” expresses low confidence in its own evaluation, and a random sample of “passed” evaluations to check for false negatives.

**Source Text:** Human-in-the-Loop: Establish clear processes for human review of the “judge” LLM’s evaluations, especially for:
Outputs flagged as high-risk or problematic by the “judge.”
Cases where the “judge” expresses low confidence in its own evaluation.
A random sample of “passed” evaluations to check for false negatives.

---

## FINOS-DET-015-017: Defining Escalation Pathways for Critical Issues Identified by Judge LLMs

**Section:** Implementation Guidance

**Subsection:** Ensuring Human Review and Escalation Pathways

**Responsible Party:** System Owners 

**Control Text:** System owners must define clear pathways for escalating critical issues identified by the “judge” (and confirmed by human review) to relevant teams (e.g., MLOps, security, legal, compliance).

**Source Text:** Escalation Procedures: Define clear pathways for escalating critical issues identified by the “judge” (and confirmed by human review) to relevant teams (e.g., MLOps, security, legal, compliance).

---

## FINOS-DET-016-001: Identifying and Documenting Source Data Access Controls and Permissions

**Section:** Implementation Guidance

**Subsection:** Understanding and Documenting Source Access Controls

**Responsible Party:** System Owners 

**Control Text:** System owners must ensure that before or during data ingestion, they are thoroughly identifying, analyzing, and documenting the existing access control lists (ACLs), roles, permissions, and any other entitlement mechanisms associated with all source data repositories (e.g., file shares, databases, document management systems like Confluence).

**Source Text:** Discovery and Analysis: Before or during data ingestion, thoroughly identify, analyze, and document the existing access control lists (ACLs), roles, permissions, and any other entitlement mechanisms associated with all source data repositories (e.g., file shares, databases, document management systems like Confluence).

---

## FINOS-DET-016-002: Understanding Mapping of Source Permissions to Organizational Identities

**Section:** Implementation Guidance

**Subsection:** Understanding and Documenting Source Access Controls

**Responsible Party:** System Owners 

**Control Text:** System owners must understand how these source permissions translate to user identities or groups within the organization’s identity management system.

**Source Text:** Mapping Entitlements: Understand how these source permissions translate to user identities or groups within the organization’s identity management system.

---

## FINOS-DET-016-003: Evaluating Access Control Capabilities of Target AI Data Stores

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must evaluate whether the target data stores used by the AI system (e.g., vector databases, graph databases, knowledge graphs) offer granular, attribute-based, or role-based access control features at the document, record, or sub-document (chunk) level.

**Source Text:** Leveraging Native Access Controls in AI Data Stores (e.g., Vector Databases):
Assessment: Evaluate whether the target data stores used by the AI system (e.g., vector databases, graph databases, knowledge graphs) offer granular, attribute-based, or role-based access control features at the document, record, or sub-document (chunk) level.

---

## FINOS-DET-016-004: Mapping and Configuring Controls to Replicate Source Data Permissions

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must meticulously map and configure these native controls to replicate the original source data permissions, if such features exist. For example, tag ingested data chunks with their original access permissions and configure the vector database to filter search results based on the querying user’s entitlements matching these tags. This is often the most integrated approach if supported robustly by the technology.

**Source Text:** Leveraging Native Access Controls in AI Data Stores (e.g., Vector Databases): Configuration: If such features exist, meticulously map and configure these native controls to replicate the original source data permissions. For example, tag ingested data chunks with their original access permissions and configure the vector database to filter search results based on the querying user’s entitlements matching these tags. This is often the most integrated approach if supported robustly by the technology.

---

## FINOS-DET-016-005: Segregating Data Stores Based on Access Level Boundaries

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must segregate ingested data into different physical or logical data stores (e.g., separate vector database instances, distinct indexes, or collections) based on clearly defined access level boundaries derived from the source systems, if fine-grained controls within a single AI data store are insufficient or technically infeasible.

**Source Text:** Data Segregation and Siloing Based on Access Domains:
Strategy: If fine-grained controls within a single AI data store are insufficient or technically infeasible, segregate ingested data into different physical or logical data stores (e.g., separate vector database instances, distinct indexes, or collections) based on clearly defined access level boundaries derived from the source systems.

---

## FINOS-DET-016-006: Granting Access Only to Authorized RAG Instances or Data Stores

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must grant AI system components, or end-users interacting with the AI, access only to the specific segregated RAG instances or data stores that correspond to their authorized access domain.

**Source Text:** Data Segregation and Siloing Based on Access Domains: Access Provisioning: Grant AI system components, or end-users interacting with the AI, access only to the specific segregated RAG instances or data stores that correspond to their authorized access domain.

---

## FINOS-DET-016-007: Consolidating Granular Access Levels into Broader Authorized Tiers

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System owners with extremely granular and numerous distinct access levels

**Control Text:** System owners with extremely granular and numerous distinct access levels may consolidate these into a smaller set of broader access tiers within the AI system, provided this consolidation still upholds the fundamental security restrictions and risk appetite. This requires careful analysis and risk assessment.

**Source Text:** Data Segregation and Siloing Based on Access Domains: Consolidation of Granular Permissions: If source systems have extremely granular and numerous distinct access levels, a pragmatic approach might involve consolidating these into a smaller set of broader access tiers within the AI system, provided this consolidation still upholds the fundamental security restrictions and risk appetite. This requires careful analysis and risk assessment.

---

## FINOS-DET-016-008: Implementing Application-Layer Authentication and Entitlement Retrieval

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer will authenticate the user and retrieve their identity and associated entitlements from the corporate Identity Provider (IdP).

**Source Text:** Application-Layer Access Control Enforcement:
Mechanism: Implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer would: Authenticate the user and retrieve their identity and associated entitlements from the corporate Identity Provider (IdP).

---

## FINOS-DET-016-009: Intercepting and Constraining User Queries Based on Access Permissions

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer will intercept the user’s query to the AI.

**Source Text:** Application-Layer Access Control Enforcement:
Mechanism: Implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer would: Intercept the user’s query to the AI.

---

## FINOS-DET-016-010: Filtering AI Responses to Enforce Data Access Restrictions

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer will modify it or constrain its scope before passing the query to the RAG system or LLM, in order to ensure that any data retrieval or processing only targets data segments the user is authorized to access (based on their entitlements and the preserved source permissions metadata).

**Source Text:** Application-Layer Access Control Enforcement:
Mechanism: Implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer would: Before passing the query to the RAG system or LLM, modify it or constrain its scope to ensure that any data retrieval or processing only targets data segments the user is authorized to access (based on their entitlements and the preserved source permissions metadata).

---

## FINOS-DET-016-011: Filtering AI Responses to Enforce Access Restrictions

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer will filter the AI’s response to redact or remove any information derived from data sources the user is not permitted to see.

**Source Text:** Application-Layer Access Control Enforcement:
Mechanism: Implement access control logic within the application layer that serves as the interface to the AI model or RAG system. This intermediary layer would: Filter the AI’s response to redact or remove any information derived from data sources the user is not permitted to see.

---

## FINOS-DET-016-012: Recognizing Complexity and Flexibility of Application-Layer Access Control

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must realize that this approach can be complex to implement and maintain but offers flexibility when underlying data stores lack sufficient native access control capabilities.

**Source Text:** Complexity: This approach can be complex to implement and maintain but offers flexibility when underlying data stores lack sufficient native access control capabilities.

---

## FINOS-DET-016-013: Tagging Data Chunks with Source Permissions and Sensitivity Metadata

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must enrich the data chunks or their corresponding metadata entries in the vector store with explicit tags, labels, or attributes representing the original source permissions, sensitivity levels, or authorized user groups/roles, during the data ingestion process.

**Source Text:** D. Metadata-Driven Access Control at Query Time:
Ingestion Enrichment: During the data ingestion process, enrich the data chunks or their corresponding metadata entries in the vector store with explicit tags, labels, or attributes representing the original source permissions, sensitivity levels, or authorized user groups/roles.

---

## FINOS-DET-016-014: Filtering Retrieved Chunks at Query Time Based on User Entitlements

**Section:** Implementation Guidance

**Subsection:** Strategies for Preserving and Enforcing Access Controls in AI Systems

**Responsible Party:** System Owners 

**Control Text:** System owners must, at query time, ensure that the RAG system (or an intermediary access control service) uses this metadata to filter the retrieved document chunks before they are passed to the LLM for synthesis. The system ensures that only chunks matching the querying user’s entitlements are considered for generating the response.

**Source Text:** D. Metadata-Driven Access Control at Query Time: Query-Time Filtering: At query time, the RAG system (or an intermediary access control service) uses this metadata to filter the retrieved document chunks before they are passed to the LLM for synthesis. The system ensures that only chunks matching the querying user’s entitlements are considered for generating the response.

---

## FINOS-DET-016-015: Avoiding System Prompt–Based Access Control Methods

**Section:** Implementation Guidance

**Subsection:** Avoiding Insecure “Shortcuts”

**Responsible Party:** System Owners using System Prompt-Based Access Control

**Control Text:** System owners using System Prompt-Based Access Control must acknowledge that attempting to enforce access controls by merely instructing an LLM via its system prompt (e.g., “Only show data from ‘Department X’ to users in ‘Group Y’”) is highly unreliable, inefficient, and proven to be easily bypassable through adversarial prompting. This method should not be considered a secure mechanism for preserving access controls and must be avoided.

**Source Text:** System Prompt-Based Access Control (Strongly Discouraged): Attempting to enforce access controls by merely instructing an LLM via its system prompt (e.g., “Only show data from ‘Department X’ to users in ‘Group Y’”) is highly unreliable, inefficient, and proven to be easily bypassable through adversarial prompting. This method should not be considered a secure mechanism for preserving access controls and must be avoided.

---

## FINOS-DET-016-016: Auditing Access Control Configurations and Mappings Periodically

**Section:** Implementation Guidance

**Subsection:** Verification, Auditing, and Monitoring (The Detective Aspect)

**Responsible Party:** System Owners 

**Control Text:** System owners must periodically audit the configuration of access controls in source systems and how these are mapped and implemented within the AI data stores, RAG pipelines, and any application-layer enforcement points.

**Source Text:** Regular Configuration Audits: Periodically audit the configuration of access controls in source systems and, critically, how these are mapped and implemented within the AI data stores, RAG pipelines, and any application-layer enforcement points.

---

## FINOS-DET-016-017: Conducting Security Testing to Identify Access Control Weaknesses

**Section:** Implementation Guidance

**Subsection:** Verification, Auditing, and Monitoring (The Detective Aspect)

**Responsible Party:** System Owners 

**Control Text:** System owners must conduct targeted security testing, including penetration tests and red teaming exercises, specifically designed to attempt to bypass the preserved access controls and access unauthorized data through the AI system.

**Source Text:** Penetration Testing and Red Teaming: Conduct targeted security testing, including penetration tests and red teaming exercises, specifically designed to attempt to bypass the preserved access controls and access unauthorized data through the AI system.

---

## FINOS-DET-016-018: Logging User Queries and Data Retrieval Activities

**Section:** Implementation Guidance

**Subsection:** Verification, Auditing, and Monitoring (The Detective Aspect)

**Responsible Party:** System Owners 

**Control Text:** System owners must implement comprehensive logging of user queries, data retrieval actions within the RAG system, and the final responses generated by the AI.

**Source Text:** Access Log Monitoring: Implement comprehensive logging of user queries, data retrieval actions within the RAG system, and the final responses generated by the AI. Monitor these logs for:
Anomalous access patterns.
Attempts to query or access data beyond a user’s expected scope.
Discrepancies between a user’s known entitlements and the data sources apparently used to generate their responses.

---

## FINOS-DET-016-019: Monitoring Access Logs for Anomalous or Unauthorized Patterns

**Section:** Implementation Guidance

**Subsection:** Verification, Auditing, and Monitoring (The Detective Aspect)

**Responsible Party:** System Owners 

**Control Text:** System owners must monitor these access logs for anomalous access patterns, attempts to query or access data beyond a user’s expected scope, and discrepancies between a user’s known entitlements and the data sources apparently used to generate their responses.

**Source Text:** Access Log Monitoring: Implement comprehensive logging of user queries, data retrieval actions within the RAG system, and the final responses generated by the AI. Monitor these logs for:
Anomalous access patterns.
Attempts to query or access data beyond a user’s expected scope.
Discrepancies between a user’s known entitlements and the data sources apparently used to generate their responses.

---

## FINOS-DET-016-020: Reconciling User Permissions with Ingested Data Access Controls

**Section:** Implementation Guidance

**Subsection:** Verification, Auditing, and Monitoring (The Detective Aspect)

**Responsible Party:** System Owners 

**Control Text:** System owners must periodically reconcile the list of users and their permissions for accessing the AI system (or specific RAG interfaces) against the access controls defined on the data ingested into those systems. The goal is to ensure there are no exfiltration paths where users might gain access to information they shouldn’t, due to misconfiguration or aggregation effects.

**Source Text:** Entitlement Reconciliation Reviews: Periodically reconcile the list of users and their permissions for accessing the AI system (or specific RAG interfaces) against the access controls defined on the data ingested into those systems. The goal is to ensure there are no exfiltration paths where users might gain access to information they shouldn’t, due to misconfiguration or aggregation effects.

---

## FINOS-DET-016-021: Maintaining Lineage of Source Documents and Permissions in AI Outputs

**Section:** Implementation Guidance

**Subsection:** Verification, Auditing, and Monitoring (The Detective Aspect)

**Responsible Party:** System Owners 

**Control Text:** System owners must maintain lineage information that tracks which source documents (and their original permissions) contributed to specific AI-generated outputs, to the extent possible. This aids in investigations if a potential access control violation is suspected.

**Source Text:** Data Lineage and Provenance Tracking: To the extent possible, maintain lineage information that tracks which source documents (and their original permissions) contributed to specific AI-generated outputs. This aids in investigations if a potential access control violation is suspected.

---

