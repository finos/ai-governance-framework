---
sequence: 24
title: Agent Action Authorization Bypass
layout: risk
doc-status: Approved-Specification
type: SEC
owasp-llm_references:
  - llm06-2025  # LLM06:2025 Excessive Agency
related_risks:
  - ri-10  # Prompt Injection
  - ri-18  # Model Overreach / Expanded Use
  - ri-22  # Regulatory Compliance and Oversight
---

## Summary

Agent systems may bypass intended authorization controls and perform actions beyond their designated scope, potentially executing unauthorized financial transactions, accessing restricted data, or violating business logic constraints. This occurs when agents exploit API vulnerabilities, escalate privileges through tool chains, or circumvent approval workflows designed to maintain segregation of duties and regulatory compliance.

## Description

Agentic AI systems in financial services may operate with significantly more autonomy than traditional RAG-based implementations, capable of making decisions and executing actions through various APIs and tools. This autonomy introduces a critical security risk: **Agent Action Authorization Bypass**, where agents perform operations outside their intended authorization boundaries.

Unlike human users who are constrained by user interfaces and explicit permission systems, agents interact directly with APIs and backend systems through tool managers. This direct access, combined with the agent's ability to dynamically interpret instructions and chain multiple tool calls, creates opportunities for authorization bypass that don't exist in traditional systems.

### Core Authorization Bypass Mechanisms

* **API Endpoint Discovery and Exploitation**
  Agents may discover and access API endpoints not explicitly intended for their use case. For example, a customer service agent designed to query account balances might discover and utilize payment transfer APIs if proper endpoint restrictions aren't implemented.

* **Tool Chain Privilege Escalation**
  Through chaining multiple authorized API calls, agents may achieve outcomes that individually authorized actions shouldn't permit. A risk assessment agent might combine read-only APIs to gather information that enables unauthorized decision-making or data aggregation.

* **Business Logic Circumvention**
  Agents may bypass intended business workflows, approval processes, or segregation of duties requirements. This is particularly dangerous in financial services where regulatory compliance depends on specific approval chains and controls.

* **Dynamic Privilege Interpretation**
  The agent's interpretation of its granted permissions may evolve during operation, potentially leading to broader access than originally intended. This "permission creep" can occur without explicit reconfiguration.

### Financial Services Impact Scenarios

* **Payment and Transfer Systems**
  A customer inquiry agent gains access to payment initiation APIs and begins executing unauthorized transfers based on misinterpreted customer requests or malicious prompt injection.

* **Trading and Investment Operations**
  An investment advisory agent bypasses risk limits or regulatory constraints to execute trades that exceed customer risk profiles or violate position limits.

* **Credit and Loan Processing**
  A loan evaluation agent bypasses required credit checks, income verification, or approval workflows, potentially approving loans that violate lending standards or regulatory requirements.

* **Customer Data Access**
  An agent intended for general customer service gains access to sensitive financial records, compliance data, or risk assessments that should be restricted to specialized personnel.

### Consequences

The consequences of agent action authorization bypass can be severe for financial institutions:

* **Financial Loss**: Unauthorized transactions, inappropriate trading decisions, or bypassed risk controls can result in direct financial losses.
* **Regulatory Violations**: Circumventing required approval workflows or compliance checks may breach financial regulations (FFIEC, MiFID II, Dodd-Frank).
* **Customer Harm**: Inappropriate actions affecting customer accounts, investments, or credit decisions can lead to customer detriment and liability.
* **Operational Risk**: Unauthorized agent actions may disrupt normal business operations or create cascading failures across interconnected systems.
* **Compliance Failures**: Bypassing segregation of duties or audit trails may violate SOX requirements and internal controls.

### Key Risk Factors

- **Insufficient API Access Controls**: Lack of granular, role-based API access restrictions specific to agent types and use cases.
- **Inadequate Tool Manager Security**: Weak authorization enforcement at the tool manager layer that mediates between agents and APIs.
- **Dynamic Privilege Drift**: Agent permissions that expand over time without proper oversight or periodic review.
- **Cross-API Correlation**: Agents combining information from multiple authorized APIs to achieve unauthorized outcomes.
- **Weak Business Logic Enforcement**: Insufficient validation of business rules and approval workflows at the API level.

## Links

- [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm06-excessive-agency/)
- [FFIEC IT Handbook - Information Security](https://ithandbook.ffiec.gov/it-booklets/information-security.aspx)