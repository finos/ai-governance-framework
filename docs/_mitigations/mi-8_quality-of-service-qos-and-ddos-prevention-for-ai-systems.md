---
sequence: 8
title: Quality of Service (QoS) and DDoS Prevention for AI Systems
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-6-2-6  # ISO 42001: AI system operation and monitoring
  - A-4-5    # ISO 42001: System and computing resources
nist-sp-800-53r5_references:
  - sc-5  # SC-5 Denial-of-service Protection
  - sc-6  # SC-6 Resource Availability
  - sc-7  # SC-7 Boundary Protection
  - si-4  # SI-4 System Monitoring
  - si-10  # SI-10 Information Input Validation
  - si-13  # SI-13 Predictable Failure Prevention
  - ir-4  # IR-4 Incident Handling
  - ca-7  # CA-7 Authorization
mitigates:
  - ri-7  # Availability of Foundational Model
related_mitigations:
  - mi-9   # AI System Alerting and Denial of Wallet DoW Spend Monitoring
  - mi-17  # AI Firewall Implementation and Management
  - mi-4   # AI System Observability
---

## Purpose

The increasing integration of Artificial Intelligence (AI) into financial applications, particularly through Generative AI, Retrieval Augmented Generation (RAG), and Agentic workflows, introduces significant operational risks. These include potential disruptions in service availability, degradation of performance, and inequities in service delivery. This control addresses the critical need to **ensure Quality of Service (QoS) and implement robust Distributed Denial of Service (DDoS) prevention measures** for AI systems.

AI systems, especially those exposed via APIs or public interfaces, are susceptible to various attacks that can impact QoS. These include volumetric attacks (overwhelming the system with traffic), prompt flooding (sending a high volume of complex queries), and inference spam (repeated, resource-intensive model calls). Such activities can exhaust computational resources, induce unacceptable latency, or deny legitimate users access to critical AI-driven services. This control aims to maintain system resilience, ensure fair access, and protect against malicious attempts to disrupt AI operations.

---

## Key Principles

Controls should be in place to ensure single or few users don't starve finite resources and interfere with the availability of AI systems.

The primary objectives of implementing QoS and DDoS prevention for AI systems are to:

* **Maintain Availability:** Ensure AI systems remain accessible to legitimate users and dependent processes by preventing resource exhaustion from high-volume, abusive, or malicious requests.
* **Ensure Predictable Performance:** Maintain consistent and acceptable performance levels (e.g., response times, throughput) even under varying loads.
* **Detect and Mitigate Malicious Traffic:** Identify and neutralize adversarial traffic patterns specifically targeting AI infrastructure, including those exploiting the unique characteristics of AI workloads.
* **Fair Resource Allocation:** Implement mechanisms to prioritize access and allocate resources effectively, especially during periods of congestion, based on user roles, service tiers, or business-critical workflows.

---

## Implementation Guidance

To effectively ensure QoS and protect AI systems from DDoS attacks, consider the following implementation measures:

* **Rate Limiting**: Enforce per-user or per-API-key request quotas to prevent abuse or to avoid monopolization of AI system resources.
* **Traffic Shaping**: Use dynamic throttling to control bursts of traffic and maintain steady system load. 
* **Traffic Filtering and Validation**: Employ anomaly detection to identify unusual traffic patterns indicative of DDoS or abuse. Enforce rigorous validation of all incoming data to filter out malformed or resource-intensive inputs.
* **Load Balancing and Redundancy**: Employ Dynamic Load Balancing to distribute traffic intelligently across instances and zones to prevent localized overload. Create redundant infrastructure for failover and redundancy, ensuring maximum uptime during high-load scenarios or targeted attacks.
* **Edge Protection**: Integrate with network-level DDoS protection services.
* **Prioritization Policies**: Implement QoS tiers to ensure critical operations receive priority during congestion.
* **Monitoring and Anomaly Detection**: Track performance metrics and traffic volume in real-time to detect anomalies early. Leverage ML-based detection systems to spot patterns indicative of low-and-slow DDoS attacks or prompt-based abuse.
* **Resource Isolation**: Use container-level isolation to protect core inference or decision systems from being impacted by overloaded upstream components.

### Additional Consideration - Prompt Filtering/Firewall
Simple static filters may not suffice against evolving prompt injection attacks. Dynamic, adaptive approaches are needed to handle adversarial attempts that circumvent fixed rule sets.  Use fixed rules as a first filter, not the sole protection mechanism. Combine with adaptive systems that learn from traffic patterns. This aligns with broader AI firewall strategies to secure input validation and filtering at multiple layers.

### Reference Implementation

A common approach is to deploy an API gateway and generate API keys specific to each use case. The assignments of keys allows:
  1. Revocation of keys on a per use case basis to block misbehaving applications
  2. Attribution of cost at the use case level to ensure shared infrastructure receives necessary funding and to allow ROI to be measured
  3. Prioritizing access of LLM requests when capacity has been saturated and SLAs across all consumers cannot be satisfied

---

## Importance and Benefits

Implementing robust QoS and DDoS prevention measures for AI systems provides several key benefits for financial institutions:

* **Service Availability:** Protects critical AI-driven services from disruption, ensuring business continuity for legitimate users
* **Performance Maintenance:** Prevents degradation of AI system performance, ensuring timely responses and positive user experience
* **Financial Protection:** Mitigates costs from service downtime, resource abuse, and reputational damage
* **Reputation Safeguarding:** Demonstrates reliability and security, preserving customer trust
* **Fair Access:** Enables equitable distribution of AI resources, preventing monopolization during peak loads
* **Operational Stability:** Contributes to overall stability and predictability of IT operations
