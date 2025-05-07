---
sequence: 9
title: Alerting / DoW Spend Alert
layout: mitigation
doc-status: Pre-Draft
type:
  - Detective
mitigates:
  - ri-7
---

Detective & Preventive controls: 
- L0 hard spend cap 
- L1 vendor side alerts; 
- L2 FinOps enforced hourly/weekly/monthly limits; 
- L3 Finegrained API key /proxy token/request quotas;
- L4 adaptive rate‑limit. Add semantic, context level/response token caps with semantic anomaly detector, credits are offset normalized by use case.
