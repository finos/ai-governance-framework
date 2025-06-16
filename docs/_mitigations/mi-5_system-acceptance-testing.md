---
sequence: 5
title: System Acceptance Testing
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-6-2-4  # ISO 42001: AI system verification and validation
  - A-6-2-5  # ISO 42001: AI system deployment
mitigates:
  - ri-4  # Hallucination and Inaccurate Outputs
  - ri-5  # Foundation Model Versioning
  - ri-6  # Non-Deterministic Behaviour
related_mitigations:
  - mi-15  # Using Large Language Models for Automated Evaluation LLM as a Judge
  - mi-11  # Human Feedback Loop for AI Systems
  - mi-10  # AI Model Version Pinning
---

## Purpose

System Acceptance Testing (SAT) for AI systems is a crucial validation phase within a financial institution. Its primary goal is to **confirm that a developed AI solution rigorously meets all agreed-upon business and user requirements**, functions as intended from an end-user perspective, and is **fit for its designated purpose before being deployed** into any live operational environment. This testing focuses on the user's viewpoint and verifies the system's overall operational readiness, including its alignment with risk and compliance standards.

---

## Key Principles

System Acceptance Testing for AI systems shares similarities with traditional software testing but includes unique considerations:

1. **Variability in AI Outputs:** LLM-based applications exhibit variability in their output, where the same response could be phrased differently despite exactly the same preconditions. The acceptance criteria needs to accommodate this variability, using techniques to validate a given response contains (or excludes) certain information, rather than expecting an exact match.

2. **Quality Thresholds vs. Binary Pass/Fail:** For non-AI systems often the goal is to achieve a 100% pass rate for test cases. Whereas for LLM-based applications, it is likely that lower pass rate is acceptable. The overall quality of the system is considered a sliding scale rather than a fixed bar.

---

## Implementation Guidance

Effective System Acceptance Testing for AI systems in the financial services sector should be a structured process that includes the following key activities:

### 1. Establishing Clear and Comprehensive Acceptance Criteria
* **Action:** Before testing begins, collaborate with all relevant stakeholders – including business owners, end-users, AI development teams, operations, risk management, compliance, and information security – to define, document, and agree upon clear, measurable, and testable acceptance criteria.
* **Considerations for Criteria:**
    * **Functional Integrity:** Does the AI system accurately and reliably perform the specific tasks and functions it was designed for? (e.g., verify accuracy rates for fraud detection models, precision in credit risk assessments, or effectiveness in customer query resolution).
    * **Performance and Scalability:** Does the system operate efficiently within defined performance benchmarks (e.g., processing speed, response times, resource utilization) and can it scale as anticipated?
    * **Security and Access Control:** Are data protection measures robust, access controls correctly implemented according to the principle of least privilege, and are audit trails comprehensive and accurate?
    * **Ethical AI Principles & Responsible AI:** For AI systems, especially those influencing critical decisions or customer interactions, do the outputs align with the institution's commitment to fairness, transparency, and explainability? This includes verifying bias detection and mitigation measures and ensuring outcomes are justifiable.
    * **Usability and User Experience (UX):** Is the system intuitive, accessible, and easy for the intended users to operate effectively and efficiently?
    * **Regulatory Compliance and Policy Adherence:** Does the system's operation and data handling comply with all relevant financial regulations (e.g., data privacy, consumer protection) and internal governance policies?
    * **Resilience and Error Handling:** How does the system behave under stress, with invalid inputs, or in failure scenarios? Are error messages clear and actionable?

### 2. Preparing a Representative Test Environment and Data
* **Action:** Conduct SAT in a dedicated test environment that mirrors the intended production environment as closely as possible in terms of infrastructure, configurations, and dependencies.
* **Test Data:** Utilize comprehensive, high-quality test datasets that are representative of the data the AI system will encounter in real-world operations. This should include:
    * Normal operational scenarios.
    * Boundary conditions and edge cases.
    * Diverse demographic data to test for fairness and bias, where applicable.
    * Potentially, sanitized or synthetic data that mimics production characteristics for specific security or adversarial testing scenarios.

### 3. Ensuring Active User Involvement
* **Action:** Actively involve actual end-users, or designated representatives who understand the business processes, in the execution of test cases and the validation of results.
* **Rationale:** Their hands-on participation and feedback are paramount to confirming that the system genuinely meets practical business needs and usability expectations.

### 4. Systematic Test Execution and Rigorous Documentation
* **Action:** Execute test cases methodically according to a predefined test plan, ensuring all acceptance criteria are covered.
* **Documentation:** Maintain meticulous records of all testing activities:
    * Test cases executed with their respective outcomes (pass/fail).
    * Detailed evidence for each test (e.g., screenshots, logs, output files).
    * Any deviations from expected results or issues encountered.
    * Clear traceability linking requirements to test cases and their results.

### 5. Managing Issues and Validating Resolutions
* **Action:** Implement a formal process for reporting, prioritizing, tracking, and resolving any defects, gaps, or issues identified during SAT.
* **Resolution:** Ensure that all critical and high-priority issues are satisfactorily addressed, re-tested, and validated before granting system acceptance.

### 6. Obtaining Formal Acceptance and Sign-off
* **Action:** Secure a formal, documented sign-off from the designated business owner(s) and other key stakeholders (e.g., Head of Risk, CISO delegate where appropriate).
* **Significance:** This sign-off confirms that the AI system has successfully met all acceptance criteria and is approved for deployment, acknowledging any accepted risks or limitations.

---
## Example: RAG-based Chat Application Testing

For example, a test harness for a RAG-based chat application would likely require a test data store which contains known 'facts'. The test suite would comprise a number of test cases covering a wide variety of questions and responses, where the test framework asserts the factual accuracy of the response from the system under test. The suite should also include test cases that explore the various failure modes of this system, exploring bias, prompt injection, hallucination and more.

System Acceptance Testing is a highly effective control for understanding the overall quality of an LLM-based application. While the system is under development it quantifies quality, allowing for more effective and efficient development. And when the system becomes ready for production it allows risks to be quantified.

---

## Importance and Benefits

System Acceptance Testing provides critical value for financial institutions:

* **Risk Mitigation:** Identifies and mitigates operational and reputational risks before deployment
* **Compliance Assurance:** Provides documented evidence of thorough vetting for regulatory requirements
* **User Confidence:** Builds trust through stakeholder involvement in validation processes
* **Cost Prevention:** Prevents expensive post-deployment failures and remediation efforts
* **Quality Assurance:** Ensures AI systems meet business objectives and performance standards

---

## Additional Resources

* [GitHub - openai/evals: Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks.](https://github.com/openai/evals)
* [Evaluation / LangChain](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/)
* [Promptfoo](https://www.promptfoo.dev/)
* [Inspect](https://inspect.ai-safety-institute.org.uk/)
