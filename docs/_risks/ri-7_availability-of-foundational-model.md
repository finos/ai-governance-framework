---
sequence: 7
title: Availability of Foundational Model
layout: risk
doc-status: Draft
type: OP
owasp-llm_references:
  - llm10-2025  # OWASP LLM: Unbounded Consumption
ffiec_references:
  - bcm-4
  - bcm-5
  - ots-2
  - aio-6
eu-ai-act_references:
  - c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - c3-s3-a26  # III.S3.A26 Obligations of Deployers of High-Risk AI Systems
  - c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

## Summary

Foundation models often rely on GPU-heavy infrastructure hosted by third-party providers, introducing risks related to service availability and performance. Key threats include Denial of Wallet (excessive usage leading to cost spikes or throttling), outages from immature Technology Service Providers, and VRAM exhaustion due to memory leaks or configuration changes. These issues can disrupt operations, limit failover options, and undermine the reliability of LLM-based applications.

## Description

Many high-performing LLMs require access to GPU-accelerated infrastructure to meet acceptable responsiveness and throughput standards. Because of this, and the proprietary nature of several leading models, many implementations rely on external Technology Service Providers (TSPs) to host and serve the models.

One key availability risk is **Denial of Wallet (DoW)**—a situation where usage patterns inadvertently lead to excessive costs, throttling, or service disruptions. For example, overly long prompts—due to large document chunking or the inclusion of multiple documents—can exhaust token limits or drive up usage charges. These effects may be magnified when systems work with multimedia content or fall victim to token-expensive attacks (e.g., adversarial queries designed to extract training data). In other scenarios, poorly throttled scripts or agentic systems may generate excessive or unexpected API calls, overwhelming available resources and bypassing original capacity planning assumptions.

Another risk is **TSP outage or degradation**, which may occur when providers lack the operational maturity to maintain stable service levels. Some models may go offline unexpectedly or become temporarily degraded under load. A particular concern arises when an LLM implementation is tightly coupled to a specific proprietary provider, limiting the ability to fail over to alternative services. This lack of redundancy can violate business continuity expectations and has been highlighted in regulatory guidance such as the FFIEC Appendix J on third-party resilience.

A further concern is **VRAM exhaustion** on the serving infrastructure, which can result from several factors. These include memory leaks introduced by updates to model-serving libraries, the adoption of caching strategies that trade VRAM for throughput, or configuration changes such as increased context length. Each of these can compromise model responsiveness or trigger crashes, reducing system availability during critical usage periods.

These availability-related risks underscore the importance of robust capacity planning, usage monitoring, and fallback strategies when integrating foundation models into operational systems.

## Links

- [Denial of Wallet (Dow) Attack on GenAI Apps](https://www.prompt.security/blog/denial-of-wallet-on-genai-apps-ddow)
- [FFIEC IT Handbook](https://ithandbook.ffiec.gov/)

