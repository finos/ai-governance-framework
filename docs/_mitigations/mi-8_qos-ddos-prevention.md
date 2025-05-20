---
sequence: 8
title: QoS/DDoS Prevention
layout: mitigation
doc-status: Draft
type: PREV
mitigates:
- ri-7
---

### Overview
Controls should be in place to ensure single or few users don't starve finite resources and interfere with the availability of AI systems.

### Description
The rapid integration of artificial intelligence into applications, notably through Generative AI, RAG and Agentic workflows, presents significant risks. Such risks include potential disruption in service availability, performance degradation, and fairness in service delivery. Prioritizing Quality of Service (QoS) and preventing DDoS attacks are vital to securing these systems.  AI systems exposed through APIs or public interfaces are susceptible to QoS degradation by volumetric attacks, prompt flooding, and inference spam, all of which can exhaust compute resources, induce latency, or disrupt legitimate access. 

### Objectives

The QoS and DDoS prevention controls aim to:

- Prevent resource exhaustion from high-volume or malicious requests.
- Maintain predictable performance under load.
- Detect and mitigate adversarial traffic patterns targeting AI infrastructure.
- Prioritize access based on user roles, service tiers, or business-critical workflows


### Implementation Guidance
- **Rate Limiting**: Enforce per-user or per-API-key request quotas to prevent abuse or to avoid monopolization of AI system resources.
- **Traffic Shaping**: Use dynamic throttling to control bursts of traffic and maintain steady system load. 
- **Traffic Filtering and Validation**: Employ anomaly detection to identify unusual traffic patterns indicative of DDoS or abuse. Enforce rigorous validation of all incoming data to filter out malformed or resource-intensive inputs.
- **Load Balancing and Redundancy**: Employ Dynamic Load Balancing to distribute traffic intelligently across instances and zones to prevent localized overload. Create redundant infrastructure for failover and redundancy, ensuring maximum uptime during high-load scenarios or targeted attacks.
- **Edge Protection**: Integrate with network-level DDoS protection services.
- **Prioritization Policies**: Implement QoS tiers to ensure critical operations receive priority during congestion.
- **Monitoring and Anomaly Detection**: Track performance metrics and traffic volume in real-time to detect anomalies early. Leverage ML-based detection systems to spot patterns indicative of low-and-slow DDoS attacks or prompt-based abuse.
- **Resource Isolation**: Use container-level isolation to protect core inference or decision systems from being impacted by overloaded upstream components.

### Additional Consideration - Prompt Filtering/Firewall
Simple static filters may not suffice against evolving prompt injection attacks. Dynamic, adaptive approaches are needed to handle adversarial attempts that circumvent fixed rule sets.  Use fixed rules as a first filter, not the sole protection mechanism. Combine with adaptive systems that learn from traffic patterns. This aligns with broader AI firewall strategies to secure input validation and filtering at multiple layers.

### Reference implementation

A common approach is to deploy an API gateway and generate API keys specific to each use case. The assignments of keys allows:
  1. Revocation of keys on a per use case basis to block misbehaving applications
  2. Attribution of cost at the use case level to ensure shared infrastructure receives necessary funding and to allow ROI to be measured
  3. Priortizing access of LLM requests when capacity has been saturated and SLAs across all consumers cannot be satisfied

### Further reading
- ri-7 Availability of foundational model
- CT-9 Alerting / DoW spend alert
- CT-17 AI firewall
