---
sequence: 3
title: User/App/Model Firewalling/Filtering
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-6-1-3  # ISO 42001: Processes for responsible AI system design and development
  - A-6-2-2  # ISO 42001: AI system requirements and specification
  - A-9-2    # ISO 42001: Processes for responsible use of AI systems
mitigates:
  - ri-7   # Availability of Foundational Model
  - ri-10  # Prompt Injection
---

Effective security for AI systems involves monitoring and filtering interactions at multiple points: between the AI model and its users, between different application components, and between the model and its various data sources (e.g., Retrieval Augmented Generation (RAG) databases).

A helpful analogy is a Web Application Firewall (WAF) which inspects incoming web traffic for known attack patterns (like malicious URLs targeting server vulnerabilities) and filters outgoing responses to prevent issues like malicious JavaScript injection. Similarly, for AI systems, we must inspect and control data flows to and from the model.

Beyond filtering direct user inputs and model outputs, careful attention must be given to data handling in associated components, such as RAG databases. When internal company information is used to enrich a RAG database – especially if this involves processing by external services (e.g., a Software-as-a-Service (SaaS) LLM platform for converting text into specialized data formats called 'embeddings') – this data and the external communication pathways must be carefully managed and secured. Any proprietary or sensitive information sent to an external service for such processing requires rigorous filtering *before* transmission to prevent data leakage.

---
#### Key Areas for Monitoring and Filtering

Implementing monitoring and filtering capabilities allows for the detection and blocking of undesired behaviors and potential threats. Key areas include:

* **RAG Data Ingestion:**
    * **Control:** Before transmitting internal information to an external service (e.g., an embeddings endpoint of a SaaS LLM provider) for processing and inclusion in a RAG system, meticulously filter out any sensitive or private data that should not be disclosed or processed externally.
* **User Input to the AI Model:**
    * **Threat Mitigation:** Detect and block malicious or abusive user inputs, such as [Prompt Injection attacks](#ri-10) designed to manipulate the LLM.
    * **Data Protection:** Identify and filter (or anonymize) any potentially private or sensitive information that users might inadvertently or intentionally include in queries to an AI model, especially if the model is hosted externally (e.g., as a SaaS offering).
* **AI Model Output (LLM Responses):**
    * **Integrity and Availability:** Detect responses that are excessively long, potentially indicative of a user tricking the LLM to cause a [Denial of Service](#ri-7) or to induce erratic behavior that might lead to information disclosure.
    * **Format Conformance:** Verify that the model's output adheres to expected formats (e.g., structured JSON). Deviations, such as responses in an unexpected language, can be an indicator of compromise or manipulation.
    * **Evasion Detection:** Identify known patterns that indicate the LLM is resisting malicious inputs or attempted abuse. Such patterns, even if input filtering was partially bypassed, can signal an ongoing attack probing for vulnerabilities in the system's protective measures (guardrails).
    * **Data Leakage Prevention:** Scrutinize outputs for any unintended disclosure of private information originating from the RAG database or the model's underlying training data.
    * **Reputational Protection:** Detect and block inappropriate or offensive language that an attacker might have forced the LLM to generate, thereby safeguarding the organization's reputation.
    * **Secure Data Handling:** Ensure that data anonymized for processing (e.g., user queries) is not inadvertently re-identified in the output in a way that exposes sensitive information. If re-identification is a necessary function, it must be handled securely.

These filtering mechanisms can be enhanced by monitoring the size of queries and responses, as detailed in [CT-8 QoS/Firewall/DDoS prevention](#CT-8). Unusually large data packets could be part of a [Denial of Wallet attack](#ri-7) (excessive resource consumption) or an attempt to destabilize the LLM to expose private training data.

Ideally, all interactions between AI system components—not just user and LLM communications—should be monitored, logged, and subject to automated safety mechanisms. A key principle is to implement filtering at information boundaries, especially where data crosses trust zones or system components.

---
#### Challenges in Implementation

* **RAG Database Security:**
    * While it's often more practical to pre-process and filter data for RAG systems before sending it for external embedding creation, organizations might also consider in-line filters for real-time checks.
    * **Consideration:** Once internal information is converted into specialized 'embedding' formats (numerical representations of text) and stored in AI-optimized 'vector databases' for rapid retrieval, the data becomes largely opaque to traditional security tools. It's challenging to directly inspect this embedded data, apply retroactive filters, or implement granular access controls within the vector database itself in the same way one might with standard databases. This inherent characteristic underscores the critical need for thorough data filtering and sanitization *before* the information is transformed into embeddings and ingested into such systems.
* **Filtering Efficacy:**
    * Static filters (e.g., based on regular expressions or keyword blocklists) are effective for well-defined patterns like email addresses, specific company terms, or known malicious code signatures. However, they are less effective at identifying more nuanced issues such as generic private information, subtle [Prompt Injection attacks](#ri-10) (which are designed to evade detection), or sophisticated offensive language. This limitation often leads to the use of more advanced techniques, such as an "LLM as a judge" (explained below).
* **Streaming Outputs:**
    * Streaming responses (where the AI model delivers output word-by-word) significantly improves user experience by providing immediate feedback.
    * **Trade-off:** However, implementing output filtering can be challenging with streaming. To comprehensively filter a response, the entire output often needs to be assembled first. This can negate the benefits of streaming or, if filtering is done on partial streams, risk exposing unfiltered sensitive information before it's detected and redacted.
    * **Alternative:** An approach is to stream the response while performing on-the-fly detection. If an issue is found, the streamed output is immediately cancelled and removed. This requires careful risk assessment based on the sensitivity of the information and the user base, as there's a brief window of potential exposure.

---
#### Remediation Techniques

* **Basic Filters:** Simple static checks using blocklists (denylists) and regular expressions can detect rudimentary attacks or policy violations.
* **System Prompts (Caution Advised):** While system prompts can instruct an LLM on what to avoid, they are generally not a robust security control. Attackers can often bypass these instructions or even trick the LLM into revealing the prompt itself, thereby exposing the filtering logic.
* **LLM as a Judge:**
    * A more advanced and increasingly common technique involves using a secondary, specialized LLM (an "LLM judge") to analyze user queries and the primary LLM's responses. This judge model is specifically trained to categorize inputs/outputs for various risks (e.g., prompt injection, abuse, hate speech, data leakage) rather than to generate user-facing answers.
    * This can be implemented using a SaaS product or a locally hosted model, though the latter incurs computational costs for each evaluation.
    * For highly sensitive or organization-specific information, consider training a custom LLM judge tailored to recognize proprietary data types or unique risk categories.
* **Human Feedback Loop:** Implementing a system where users can easily report problematic AI responses provides a valuable complementary control. This feedback helps verify the effectiveness of automated guardrails and identify new evasion techniques.

---
#### Additional Considerations

* **API Security and Observability:** Implementing a comprehensive API monitoring and security solution offers benefits beyond AI-specific threats, enhancing overall system security. For example, a security proxy can enforce encrypted communication (e.g., TLS) between all AI system components.
* **Logging and Analysis:** Detailed logging of interactions (queries, responses, filter actions) is essential. It aids in understanding user behavior, system performance, and allows for the detection of sophisticated attacks or anomalies that may only be apparent through statistical analysis of logged data (e.g., coordinated denial-of-service attempts).

---
#### Links

* Tooling
    * [LLM Guard](https://github.com/protectai/llm-guard): Open source LLM filter for sanitization, detection of harmful language, prevention of data leakage, and resistance against prompt injection attacks.
    * [deberta-v3-base-prompt-injection-v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2): Open source LLM model, a fine-tuned version of microsoft/deberta-v3-base specifically developed to detect and classify prompt injection attacks which can manipulate language models into producing unintended outputs.
    * [ShieldLM](https://github.com/thu-coai/ShieldLM): open source bilingual (Chinese and English) safety detector that mainly aims to help to detect safety issues in LLMs' generations.
