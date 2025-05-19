---
sequence: 17
title: Ai Firewall
layout: mitigation
doc-status: Pre-Draft
type: PREV
mitigates:
- ri-7
- ri-10
- ri-15
related_mitigations:
- mi-8
- mi-9
- mi-12
---

An AI firewall would inspect and block user prompts when it detects it may lead to data leakage, making the system unstable, or exahusting resources (number of tokens).

### Further reading
- CT-8 QoS/DDoS prevention
- CT-9 Alerting / DoW spend alert
- CT-12 Role-based data access
