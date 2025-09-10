---
sequence: 25
title: Tool Chain Manipulation and Injection
layout: risk
doc-status: Draft
type: SEC
owasp-llm_references:
  - llm01-2025  # LLM01:2025 Prompt Injection
related_risks:
  - ri-10  # Prompt Injection
  - ri-24  # Agent Action Authorization Bypass
  - ri-4   # Hallucination and Inaccurate Outputs
---

## Summary

Malicious inputs manipulate agents into selecting inappropriate tools, executing dangerous API call sequences, or injecting malicious parameters into legitimate API calls. This extends beyond traditional prompt injection by targeting the agent's tool selection and execution logic, potentially causing financial transactions, data exposure, or system compromise through carefully crafted tool chain attacks.

## Description

**Tool Chain Manipulation and Injection** represents an evolution of prompt injection attacks specifically targeting agentic AI systems. While traditional prompt injection focuses on manipulating text outputs, tool chain attacks target the agent's decision-making process for selecting and executing tools, APIs, and system actions.

In agentic systems, the LLM doesn't just generate text responses—it makes decisions about which tools to use, what parameters to pass, and how to sequence multiple API calls to achieve complex objectives. This decision-making process becomes a critical attack surface that adversaries can exploit to cause real-world harm beyond generating inappropriate text.

### Attack Vectors and Mechanisms

* **Tool Selection Manipulation**
  Attackers craft inputs that cause the agent to select inappropriate tools for the given task. For example, an agent intended to check account balances might be manipulated into selecting payment transfer tools instead.

* **API Parameter Injection**
  Malicious inputs influence the parameters the agent passes to legitimate API calls. An attacker might manipulate an agent to pass malicious account numbers, amounts, or authorization codes to financial APIs.

* **Tool Chain Sequencing Attacks**
  Adversaries manipulate the sequence in which the agent executes multiple tools, creating dangerous combinations of otherwise safe individual operations. For instance, combining data gathering tools with action-taking tools in ways that weren't intended.

* **Tool State Corruption**
  Attacks that corrupt the agent's understanding of tool states, capabilities, or relationships, leading to inappropriate tool usage or dangerous tool combinations.

* **Cross-Tool Data Injection**
  Using outputs from one tool to inject malicious data into subsequent tool calls, creating a chain of compromised operations.

### Financial Services Attack Scenarios

* **Payment Redirection Attacks**
  An attacker submits a customer service request that manipulates the agent into using payment tools with modified beneficiary details, redirecting legitimate payments to attacker-controlled accounts.

* **Trading Manipulation**
  Market analysis requests are crafted to manipulate trading agents into executing unauthorized trades, potentially involving insider information or market manipulation schemes.

* **Data Exfiltration Through Tool Chains**
  Combining read-only tools in sequences that extract sensitive customer data, financial records, or proprietary trading algorithms through multi-step information gathering.

* **Compliance Bypass Operations**
  Manipulating compliance checking agents to skip required verification steps or approve transactions that should be flagged for manual review.

* **Risk Assessment Corruption**
  Injecting parameters into risk calculation APIs that produce artificially low risk scores, enabling inappropriate loan approvals or investment recommendations.

### Technical Exploitation Methods

* **Contextual Prompt Injection**: Embedding malicious instructions within legitimate-appearing data that influences tool selection when processed by the agent.

* **Parameter Substitution**: Crafting inputs that cause the agent to substitute attacker-controlled values for legitimate parameters in API calls.

* **Tool Function Confusion**: Exploiting similarities between tool names or descriptions to trick agents into using wrong tools for specific tasks.

* **State Machine Manipulation**: Interfering with the agent's understanding of current state or context to induce inappropriate tool selection decisions.

### Consequences

Tool chain manipulation attacks can result in severe consequences for financial institutions:

* **Financial Fraud**: Direct financial loss through unauthorized transactions, payment redirections, or trading manipulation.
* **Data Breach**: Exfiltration of sensitive customer data, financial records, or proprietary information through manipulated tool chains.
* **Regulatory Violations**: Bypassing compliance checks or audit trails may violate financial regulations and reporting requirements.
* **Market Manipulation**: Inappropriate trading actions could constitute market manipulation with severe regulatory and legal consequences.
* **Operational Disruption**: Corrupted tool chains may cause system failures, processing delays, or require expensive remediation efforts.
* **Customer Harm**: Inappropriate actions affecting customer accounts, investments, or financial standing.

### Key Risk Factors

- **Insufficient Tool Selection Validation**: Lack of verification that selected tools are appropriate for the given task and context.
- **Weak API Parameter Sanitization**: Inadequate validation and sanitization of parameters passed to APIs through agent tool calls.
- **Tool Chain Logic Vulnerabilities**: Flaws in the logic governing how agents sequence and combine multiple tool calls.
- **Cross-Tool State Management**: Poor isolation between tool calls allowing corruption to propagate through tool chains.
- **Inadequate Tool Access Controls**: Overly broad tool access permissions enabling inappropriate tool selection.

## Links

- [OWASP LLM01: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [MITRE ATT&CK: Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/)