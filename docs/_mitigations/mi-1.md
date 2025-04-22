---
layout: mitigation
doc-status: Draft
sequence: 1
type:
  - Detective
mitigates:
  - ri-1
title: Data Leakage Prevention and Detection
---

#### Preventing Leakage of Session Data

The use of Third-Party Service Providers (TSPs) for LLM-powered
services and raw endpoints will be attractive for a variety of
reasons:

1. The best-peforming LLMs may be proprietary with model weights
   unavailable for local deployment.

2. GPU compute to power LLMs can require upgrades in data center power
   and cooling with long lead times.

3. GPUs are expensive and may be limited in supply. TSPs may be
   required for "burst capacity".


Given that leakage of session data may have adverse impact to clients
and risk fines from regulators, preventing leakage thereof is a
priority.  Traditional risks and mitigations include:

- Network Taps / Man-In-The-Middle Attacks

  - Ensure that communication with the TSP is encrypted following
    industry best practices.

  - Prefer architectures where the LLM provider hosts their service in
    your cloud tenant to avoid transmitting data outside your system
    boundaries.

- Filesystem

  - Ensure that the LLM provider defaults to "zero persistence" of
    logs, session data, and core dumps except where agreed upon in
    writing.

- Improper Disposal of Storage Medium

  - Ensure that the vendor follows Data Lifecycle Management best
    practices that are compatible with that of your organization.

- Multi-Tenant Architecture

  - Have your SecDesign team review the TSPs system architecture to
    ensure that no data can be leaked to other sessions / users.


LLM-specific attacks:

- Memorization

  - Verify that your legal agreement with the LLM provider explicitly
    states that no API inputs/outputs will be used for model training.

- LLM Caching

  - Given the high cost of GPUs, the TSP may be incentivized to reduce
    redundant computation through caching of activations /
    prefixes. Ensure that the TSP provides information about any such
    optimizations for your ML team to review.

    
#### Preventing Leakage of Training Data

If you have fine-tuned a model with proprietary data, there is the
potential for it to be extracted as described in:

- [Scalable Extraction of Training Data from (Production) Language
  Models](https://arxiv.org/abs/2311.17035)

Have your ML team ensure that there are guardrails in place to detect
attempts at training data extraction through prompting.


#### Detecting Leakage of Session Data

To address the potential for data leakage when proprietary information
is processed by an external LLM (typically a SaaS-based solution), a detective control
using [data leakage
canaries](https://www.ischool.berkeley.edu/projects/2023/llm-canary-open-source-security-benchmark-tool).

This technique aims to monitor and detect unauthorized disclosure of
sensitive information by embedding uniquely identifiable markers
(canaries) into the data streams or queries sent to the hosted model.

Key components of this control include:

- **Canary Data Injection**: Canary data consists of artificial or
  uniquely identifiable tokens embedded within the proprietary data
  sent to the hosted model. These tokens do not have legitimate
  business value but are crafted to detect leaks when exposed. For
  instance, queries containing unique strings can be planted during
  interactions with the LLM, and if these tokens appear in
  unauthorized contexts (e.g., responses from the model, external
  logs, or internet forums), it would indicate a potential breach.
  
- **Data Fingerprinting**: Proprietary data can be fingerprinted using
  cryptographic hashing techniques to create unique signatures. By
  monitoring the hosted service or conducting
  external reconnaissance, organizations can detect if these
  fingerprints appear in unauthorized locations, signaling a data
  breach or leakage.
  
- **Plugin Architecture Integration**: Implementing canary and
  fingerprint detection mechanisms into the plugin architecture of the
  SaaS-based LLM ensures that data leakage detection is embedded
  into the system at multiple touchpoints, providing continuous
  monitoring across interactions.
  
- **Detection and Response Workflow**: Once a canary token is detected
  in an unauthorized environment, the system triggers an immediate
  alert, initiating the incident response process. This includes
  identifying the source of the breach, determining the extent of the
  leakage, and implementing remedial actions, such as ceasing further
  interaction with the compromised model.

This control is particularly effective in detecting unauthorized use
or exposure of internal proprietary information processed by external
systems. By embedding canaries and fingerprints, organizations can
maintain a degree of oversight and control, even when data is
processed beyond their direct infrastructure.


#### Detecting Leakage of Model Weights

In situations where detecting leakage of model weights is necessary,
there are approaches to "fingerprinting" that are being explored in
the research community. On example based on knowledge-injection is:

- [Instructional Fingerprinting of Large Language Models](https://arxiv.org/abs/2401.12255)

