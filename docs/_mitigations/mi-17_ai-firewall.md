---
sequence: 17
title: Ai Firewall
layout: mitigation
doc-status: Pre-Draft
type: PREV
mitigates:
- ri-10
---

### Description
The rapid and widespread integration of generative AI into application workflows, either through direct API calls, agentic workflows, or the client-server concept of the Model Context Protocol (MCP), brings forth emerging risks. These risks include model inversion, prompt injection, and data exfiltration or leakage. Given these threats, there is a growing necessity for a security system like an AI firewall. Such a firewall would intercept and analyze communication between user and agent, agent and tools, and even inter-agent communication. Its functions should include, but not be limited to, threat detection, monitoring, alerting, blocking, reporting, and implementing guardrails to preserve Personally Identifiable Information (PII) and the confidentiality of sensitive data.


### Key Risks

- **Risk 1**: Data poisoning, a method where the AI's training data is manipulated by an adversary, can impact its decision-making process. This risk is present across the AI agentic workflow, even during stages like fine-tuning and Retriever-Augmented Generation (RAG), potentially leading to skewed or inaccurate results.

- **Risk 2**: Data exfiltration and leakage refer to unauthorized transfer or disclosure of sensitive information from a system. They pose serious risks in the AI agentic workflow, potentially compromising the integrity of the system and violating privacy regulations.

- **Risk 3**: AI agent compromise, which refers to the scenario where an adversary gains unauthorized access or control over an AI system, which can manipulate its functions and outputs, posing a significant threat to the integrity and reliability of the AI agentic workflow.

- **Risk 4**: Tool abuse, refers to the misuse of agent tools and its resources, usually involving the use of such tools for unauthorized purposes. This can lead to harmful consequences, ranging from data breaches to the production of misleading or harmful outputs.

- **Risk 5**: Resource exhaustion through DoS attacks, on the other hand, involves overloading an AI system with excessive requests, aiming to overwhelm the system and render it unable to function properly. This form of cyberattack can severely affect the performance of the AI system, and in extreme cases, can cause the system to shut down entirely.

- **Risk 6**: Lack of transparency can obscure who is accessing what tools or data, and whether these activities are authorized or potentially malicious and this can pose significant security risks.

- **Risk 7**: Absence of an input filter, the system is vulnerable to malicious data or commands. This could lead to a variety of issues like system corruption, manipulated outputs, or the execution of unauthorized actions.

- **Risk 8**: Absence of an output filter, which may result in the disclosure of sensitive information, violation of privacy regulations, or the production of harmful or inappropriate responses. Output filters are crucial to ensure the AI system's responses align with ethical guidelines and do not inadvertently harm the user or the system's reputation.

### Technical Background (Optional)
<Include any technical details, references, or context that help explain the risk.>

### Challenges
<Highlight specific challenges or complexities associated with this risk.>

### Mitigation Strategies
- **Strategy 1**: <Description of the first mitigation strategy.>
- **Strategy 2**: <Description of the second mitigation strategy.>
- ...

### Regulatory References
- [Link 1](#)
- [Link 2](#)

### Standards References
- [Link 1](#)
- [Link 2](#)

### Technical References
- [Link 1](#)
- [Link 2](#)
- 

An AI firewall would inspect and block user prompts when it detects it may lead to data leakage, making the system unstable, or exahusting resources (number of tokens).

### Further reading
- ri-7 Availability of foundational model
- ri-10 Prompt injection
- ri-15 Data leakage
- CT-8 QoS/DDoS prevention
- CT-9 Alerting / DoW spend alert
- CT-12 Role-based data access
