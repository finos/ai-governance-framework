---
sequence: 7
title: Availability of Foundational Model
layout: risk
doc-status: Approved-Specification
type: OP
owasp-llm_references:
  - llm10-2025  # LLM10:2025 Unbounded Consumption
ffiec-itbooklets_references:
  - bcm-4  # BCM: IV Business Continuity Strategies
  - bcm-5  # BCM: V Business Continuity Plan
  - ots-2  # OTS: Risk Management
  - aio-6  # AIO: VI Operations
eu-ai-act_references:
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
  - c3-s3-a26  # III.S3.A26: Obligations of Deployers of High-Risk AI Systems
  - c5-s2-a53  # V.S2.A53: Obligations for Providers of General-Purpose AI Models
related_risks:
  - ri-5   # Foundation Model Versioning
  - ri-8   # Tampering With the Foundational Model
---

## Summary

Foundation models often rely on GPU-heavy infrastructure hosted by third-party providers, introducing risks related to service availability and performance. Key threats include Denial of Wallet (excessive usage leading to cost spikes or throttling), outages from immature Technology Service Providers, and VRAM exhaustion due to memory leaks or configuration changes. These issues can disrupt operations, limit failover options, and undermine the reliability of LLM-based applications.

## Description

Many high-performing LLMs require access to GPU-accelerated infrastructure to meet acceptable responsiveness and throughput standards. Because of this, and the proprietary nature of several leading models, many implementations rely on external Technology Service Providers (TSPs) to host and serve the models.

Availability risks include:

**Denial of Wallet (DoW)**:
A situation where usage patterns inadvertently lead to excessive costs, throttling, or service disruptions. For example, overly long prompts—due to large document chunking or the inclusion of multiple documents—can exhaust token limits or drive up usage charges. These effects may be magnified when systems work with multimedia content or fall victim to token-expensive attacks (e.g., adversarial queries designed to extract training data). In other scenarios, poorly throttled scripts or agentic systems may generate excessive or unexpected API calls, overwhelming available resources and bypassing original capacity planning assumptions.

**TSP Outage or Degradation**:
External providers may lack the operational maturity to maintain stable service levels, leading to unexpected outages or performance degradation under load. A particular concern arises when an LLM implementation is tightly coupled to a specific proprietary provider, limiting the ability to fail over to alternative services. This lack of redundancy can violate business continuity expectations and has been highlighted in regulatory guidance such as the FFIEC Appendix J on third-party resilience. Mature TSPs may offer service level agreements (SLAs), but these do not guarantee uninterrupted service and may not compensate for business losses during an outage.

**VRAM Exhaustion**:
Video RAM (VRAM) exhaustion on the serving infrastructure can compromise model responsiveness or trigger crashes. This can result from several factors, including:
*   **Memory Leaks**: Bugs in model-serving libraries can lead to memory leaks, where VRAM is not properly released after use, eventually causing the system to crash.
*   **Caching Strategies**: Some strategies trade VRAM for throughput by caching model states or activations. While this can improve performance, it also increases VRAM consumption and the risk of exhaustion.
*   **Configuration Changes**: Increasing the context length or batch size can significantly increase VRAM requirements, potentially exceeding available resources.

These availability-related risks underscore the importance of robust capacity planning, usage monitoring, and fallback strategies when integrating foundation models into operational systems.

## Links

- [Denial of Wallet (Dow) Attack on GenAI Apps](https://www.prompt.security/blog/denial-of-wallet-on-genai-apps-ddow)
- [FFIEC IT Handbook](https://ithandbook.ffiec.gov/)

