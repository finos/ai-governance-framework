---
sequence: 29
title: Agent-Mediated Credential Discovery and Harvesting
layout: risk
doc-status: Approved-Specification
type: SEC
owasp-llm_references:
  - llm01-2025  # LLM01:2025 Prompt Injection
  - llm06-2025  # LLM06:2025 Excessive Agency
related_risks:
  - ri-10  # Prompt Injection
  - ri-24  # Agent Action Authorization Bypass
  - ri-25  # Tool Chain Manipulation and Injection
  - ri-26  # MCP Server Supply Chain Compromise
---

## Summary

Agents are manipulated or exploited to systematically discover, access, and exfiltrate authentication credentials, API keys, secrets, and other sensitive authentication materials from systems, applications, and data stores. This risk extends beyond traditional credential theft by leveraging agents' autonomous tool selection capabilities and legitimate system access to conduct systematic credential harvesting operations that can compromise entire infrastructure and enable widespread lateral movement.

## Description

**Agent-Mediated Credential Discovery and Harvesting** represents a sophisticated attack vector that exploits agentic AI systems' unique combination of autonomous decision-making, legitimate tool access, and systematic data processing capabilities to conduct large-scale credential harvesting operations. Unlike traditional credential theft that targets specific systems or requires manual reconnaissance, this risk leverages agents' ability to autonomously explore systems, process large volumes of data, and make intelligent decisions about which resources to target for credential extraction.

Agentic systems in financial services typically have broad access to files, databases, APIs, configuration systems, and cloud resources as part of their legitimate operations. This extensive access, combined with their ability to process and analyze data at scale, makes them powerful tools for credential discovery when compromised or manipulated by malicious actors.

The systematic nature of agent-mediated credential harvesting makes it particularly dangerous, as agents can autonomously identify patterns, correlate information across multiple systems, and optimize their harvesting strategies based on discovered information. This creates a force multiplication effect where a single compromised agent can potentially discover and exfiltrate credentials from dozens or hundreds of systems.

### Credential Discovery Attack Vectors

* **Tool Chain Credential Enumeration**
  Agents are manipulated to use legitimate file access, database query, or API tools to systematically search for credentials in predictable locations such as configuration files, environment variables, application logs, and source code repositories.

* **Memory and Process Credential Extraction**
  Compromised agents use system access tools to extract credentials from running process memory, swap files, core dumps, or temporary storage where credentials may be cached or inadvertently stored.

* **Database and Storage System Credential Mining**
  Agents exploit their database access to search for credentials stored in user tables, configuration tables, or other database locations where passwords, API keys, or authentication tokens may be stored.

* **Cloud and Infrastructure Credential Harvesting**
  Agents leverage cloud management APIs and infrastructure tools to discover credentials in cloud key vaults, secret stores, instance metadata, or infrastructure-as-code configurations.

* **Cross-System Credential Correlation**
  Agents use their ability to access multiple systems to correlate partial credential information, reconstruct full credentials from fragments, or identify credential reuse patterns across systems.

### Financial Services Exploitation Scenarios

* **Trading System Credential Compromise**
  An agent manipulated to harvest trading platform credentials, market data API keys, or brokerage system authentication tokens, enabling unauthorized trading operations or market data manipulation.

* **Banking Core System Access**
  Agents extract credentials for core banking systems, payment processors, or SWIFT networks, providing attackers with access to critical financial infrastructure and transaction systems.

* **Customer Data System Credentials**
  Systematic harvesting of credentials for customer relationship management systems, loan origination platforms, or identity verification services, enabling large-scale customer data breaches.

* **Regulatory Reporting System Access**
  Extraction of credentials for regulatory reporting systems, compliance databases, or audit platforms, potentially enabling manipulation of regulatory submissions or compliance data.

* **Cloud Infrastructure Credential Theft**
  Harvesting of cloud service credentials, container registry keys, or infrastructure management tokens that provide broad access to financial institution's cloud infrastructure and data stores.

### Advanced Credential Harvesting Techniques

* **Intelligent Credential Pattern Recognition**
  Agents use pattern recognition capabilities to identify credentials that don't match obvious formats, such as custom authentication schemes or encoded credential formats.

* **Credential Validation and Testing**
  Compromised agents automatically test discovered credentials against multiple systems to determine their scope and validity, maximizing the value of harvested materials.

* **Lateral Movement Credential Chaining**
  Agents use initially discovered credentials to access additional systems and harvest more credentials, creating a cascading compromise effect across interconnected systems.

* **Time-Based Credential Harvesting**
  Agents conduct harvesting operations over extended periods to avoid detection, systematically building comprehensive credential databases while maintaining operational stealth.

### Attack Propagation and Amplification

* **Multi-Agent Credential Sharing**
  In multi-agent environments, compromised agents share discovered credentials with other agents, amplifying the scope of compromise across the entire agent ecosystem.

* **Persistent Credential Collection**
  Agents maintain persistent credential collection operations across multiple sessions, building comprehensive credential databases over time.

* **Automated Credential Updates**
  Compromised agents monitor for credential changes and automatically update their harvested credential stores when credentials are rotated or updated.

### Consequences

Agent-mediated credential harvesting can result in catastrophic security consequences:

* **Infrastructure-Wide Compromise**: Harvested credentials can provide attackers with broad access to financial institution's entire technology infrastructure.
* **Customer Data Breach**: Access to customer system credentials enables large-scale data breaches affecting thousands or millions of customers.
* **Financial System Manipulation**: Trading, payment, and core banking system credentials enable direct financial fraud and market manipulation.
* **Regulatory System Access**: Compromise of regulatory reporting and compliance systems can enable manipulation of regulatory submissions and audit data.
* **Long-term Persistent Access**: Comprehensive credential harvesting provides attackers with multiple access points that persist even after initial compromise vectors are discovered.
* **Supply Chain Compromise**: Harvested vendor or partner credentials can extend compromise beyond the primary target to interconnected organizations.

### Key Risk Factors

- **Excessive Agent System Access**: Agents with broad access to files, databases, and system resources without appropriate credential isolation.
- **Inadequate Credential Segmentation**: Failure to properly isolate credentials from agent execution environments and accessible data stores.
- **Weak Agent Tool Restrictions**: Insufficient restrictions on agent tool usage, particularly for system administration and data access tools.
- **Poor Credential Storage Practices**: Storing credentials in locations accessible to agent operations such as configuration files, environment variables, or shared databases.
- **Insufficient Credential Monitoring**: Lack of monitoring for unusual credential access patterns or systematic credential discovery activities.
- **Agent Memory and State Persistence**: Agent persistent memory or state storage that could retain discovered credentials across sessions.

## Links

- [OWASP LLM01: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm06-excessive-agency/)
- [MITRE ATT&CK: Credential Access](https://attack.mitre.org/tactics/TA0006/)
- [NIST SP 800-63B - Authentication and Lifecycle Management](https://pages.nist.gov/800-63-3/sp800-63b.html)