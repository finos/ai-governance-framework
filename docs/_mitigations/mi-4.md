---
layout: mitigation
doc-status: Draft
sequence: 4
type:
  - Detective
mitigates:
  - ri-1
  - ri-2
  - ri-3
  - ri-5
  - ri-6
  - ri-7
  - ri-8
  - ri-10
  - ri-13
title: System observability
---

#### What to log/monitor

When talking about observability, these are the main things to log and monitor:

- Inputs from the user
- Output from the model
- APIs calls
- Information crossing trust boundaries

It is always good to log and monitor all, or as much as possible. But when there are limitations because of the bandwidth of the ingested data, consider at least the previous sources. Every application using the models should be included.

Consider employing a solution for horizontal monitoring, across several inputs/outputs at the same time for the whole architecture.


#### Why

The following reasons explain why we want to log and monitor, and what threats we tackle or how we benefit from it:

- Anomaly detection, something that other controls are not explicitly looking into.
- Audit and compliance. Although we are not aware of current regulation that requires it, it could become mandatory in the future.
- Version control drift from changes, including model, system architecture, and data. Detecting performance degradation that can affect the stability and safety of the whole system.
  
- Set clear SLA for availability and performance metrics, specially when multiple tenants are involved. This and cost monitoring is related to security because of [denial of wallet](#ri-7), for that we look into API calls, CPU-lock/scale out, front-end DOS. Once we monitor it, we can rate limit or throttle when reaching limits (Finops), and alerting as described in [CT-9	-	Alerting / DoW spend alert](#CT-9).

- The recommendation to capture inputs including user prompt, can be used to discover external misuse of your system, even if individually blocked, by individuals or organized campaigns that may require severe measures to completely block while maintaining stability.

- Being able to detect data bleeding (information from a user in a session being available for other users/session), and data persistence (information from one finished session being available into another session). Also known as data pollution, related [CT-3 - User/app/model firewalling/filtering](#CT-3), [CT-1 - Draft	Data Leakage Prevention and Detection](#CT-1), [CT-2 - Draft	Data filtering from Confluence into the samples](#CT-2).

- Assurances that responsible AI metrics are met, need logging, monitoring and processing of the whole system behavior against the specific metrics for this topic. 

- When in the future you are experiencing security issues, you need to have started collecting information in the past for a full fledged analysis and troubleshooting.
