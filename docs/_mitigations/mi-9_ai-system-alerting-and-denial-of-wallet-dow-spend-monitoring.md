---
sequence: 9
title: AI System Alerting and Denial of Wallet (DoW) / Spend Monitoring
layout: mitigation
doc-status: Draft
type: DET
iso-42001_references:
  - A-6-2-6  # ISO 42001: AI system operation and monitoring
  - A-4-2    # ISO 42001: Resource documentation
mitigates:
  - ri-7  # Availability of Foundational Model
---

## Purpose

The consumption-based pricing models common in AI services (especially cloud-hosted Large Language Models and compute-intensive AI workloads) create unique financial and operational risks. **"Denial of Wallet" (DoW)** attacks specifically target these cost structures by attempting to exhaust an organization's AI service budgets through excessive resource consumption, potentially leading to service suspension, degraded performance, or unexpected financial impact.

This control establishes comprehensive alerting and spend monitoring mechanisms to detect, prevent, and respond to both malicious and accidental overconsumption of AI resources, ensuring financial predictability and service availability.

---
## Multi-Layered Spend Control Framework

Effective DoW prevention requires implementing multiple layers of controls, each providing different levels of granularity and responsiveness:

| **Level** | **Scope**       | **Control**                                                                                                                | **Pros**                                | **Cons / Residual Risk**          |
| --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | --------------------------------- |
| **0**     | Org-wide        | **Enterprise spending cap** (configured accounting/controlling; enforced via payment provider)                             | Bullet-proof stop-loss; zero code       | Binary outage if mis-sized; blunt |
| **1**     | Org-wide        | **Real-time budget alerts** (configured in model hosting infra, hyperscaler)                                               | 2-min setup; low friction               | Reactive; alert fatigue           |
| **2**     | Billing account | **Daily/Weekly/monthly spend limits** enforced by FinOps                                                                   | Aligns to GL codes & POs                | Coarse; slow to amend             |
| **3**     | Project / env   | **IaC quota policy** (`quota <= $X/day` in ex. terraform / ansible configs)                                                | Declarative, auditable                  | Requires IaC discipline           |
| **4**     | API key / team  | **Token & request quotas** in central API Gateway, Proxy middleware                                                        | Fine-grained; immediate                  | Complex implementation             |

---
## Implementation Guidance

### 1. Establish Financial Guardrails
* **Enterprise-Level Caps:** Implement hard spending limits at the organizational level through payment providers or cloud service billing controls as an ultimate failsafe.
* **Hierarchical Budget Controls:** Set up cascading budget limits from enterprise → department → project → individual user/API key levels.
* **Automated Spend Cutoffs:** Configure automatic service suspension or throttling when predefined spending thresholds are reached.

### 2. Real-time Monitoring and Alerting
* **Cost Tracking:** Implement real-time monitoring of AI service consumption costs across all services, projects, and users.
* **Multi-Threshold Alerts:** Configure alerts at multiple spending levels (e.g., 50%, 75%, 90%, 100% of budget) with escalating notification procedures.
* **Anomaly Detection:** Deploy systems to detect unusual spending patterns that might indicate malicious activity or system malfunction.

### 3. Granular Resource Controls
* **API Key Management:** Use API gateways to implement per-key quotas for:
    * Request rate limits (requests per minute/hour)
    * Token consumption limits (for LLM services)
    * Compute resource consumption caps
* **User-Based Quotas:** Implement individual user spending and usage limits based on roles and business needs.
* **Project-Level Controls:** Set resource quotas at the project or environment level to prevent any single initiative from consuming excessive resources.

### 4. Usage Attribution and Accountability
* **Cost Attribution:** Ensure all AI resource consumption can be attributed to specific:
    * Business units or cost centers
    * Projects or applications
    * Individual users or service accounts
    * Specific use cases or workloads
* **Chargeback Mechanisms:** Implement internal chargeback systems to allocate AI costs to the appropriate business units.

### 5. Proactive Management and Optimization
* **Usage Analytics:** Regularly analyze spending patterns to identify optimization opportunities and predict future resource needs.
* **Right-sizing:** Continuously evaluate whether AI resource allocations match actual business requirements.
* **Vendor Management:** Monitor and negotiate with AI service providers to optimize pricing and contract terms.

---
## Alerting and Response Procedures

### Alert Types and Escalation
* **Budget Threshold Alerts:** Automated notifications when spending approaches defined limits
* **Anomaly Alerts:** Notifications for unusual spending patterns or consumption spikes
* **Service Interruption Alerts:** Immediate notifications if services are suspended due to spending limits
* **Security Alerts:** Alerts for suspected DoW attacks or unauthorized resource consumption

### Response Actions
* **Immediate Response:** Automatic throttling or suspension of non-critical AI services when hard limits are reached
* **Investigation:** Rapid assessment of spending anomalies to distinguish between legitimate use, misconfiguration, and attacks
* **Mitigation:** Quick implementation of additional controls or service adjustments to prevent further overconsumption
* **Communication:** Clear communication to affected users and stakeholders about spending issues and remediation steps

---
## Integration with Business Processes

### Financial Planning
* **Budget Forecasting:** Use historical AI spending data to improve budget planning and forecasting accuracy
* **Variance Analysis:** Regular comparison of actual vs. planned AI spending with root cause analysis for significant variances

### Procurement and Vendor Management
* **Contract Negotiations:** Use spending data to inform negotiations with AI service providers
* **Service Level Agreements:** Establish SLAs that account for spending limits and service availability requirements

### Risk Management
* **Risk Assessment:** Regular evaluation of DoW risks and the effectiveness of implemented controls
* **Incident Response:** Integration with broader cybersecurity incident response procedures for suspected attacks

---
## Importance and Benefits

Implementing comprehensive spend monitoring and DoW prevention provides critical advantages:

* **Financial Predictability:** Prevents unexpected AI service costs that could impact budget and financial planning
* **Service Availability:** Ensures AI services remain available by preventing budget exhaustion that could lead to service suspension
* **Resource Optimization:** Enables better understanding and optimization of AI resource consumption patterns
* **Security Protection:** Detects and mitigates attacks that attempt to exhaust AI service budgets
* **Operational Transparency:** Provides clear visibility into AI resource usage patterns and costs across the organization
* **Compliance Support:** Supports financial controls and audit requirements related to technology spending
* **Business Enablement:** Allows organizations to confidently deploy AI services knowing that costs are monitored and controlled
