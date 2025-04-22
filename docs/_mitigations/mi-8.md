---
layout: mitigation
doc-status: Pre-Draft
sequence: 8
type:
 - Preventative
mitigates:
 - ri-7
title: QoS/DDoS prevention
---

Controls should be in place to ensure single or few users don't starve finite resources and interfere with the availability of AI systems.

### API authentication

LLM endpoints should require authentication to ensure that only approved use cases can access the LLM. 

### Monitoring model usage

LLM endpoints should have usage being monitored, per application / use case.

Observed metrics should be compared with expected utilization.

### API throttling

Throttle API calls on a per use case basis depending on priority to fit the assigned capacity.

### Reference implementation

A common approach is to deploy an API gateway and generate API keys specific to each use case. The assignments of keys allows:
  1. Revocation of keys on a per use case basis to block misbehaving applications
  2. Attribution of cost at the use case level to ensure shared infrastructure receives necessary funding and to allow ROI to be measured
  3. Priortizing access of LLM requests when capacity has been saturated and SLAs across all consumers cannot be satisfied

### Further reading
- ri-7 Availability of foundational model
- CT-9 Alerting / DoW spend alert
- CT-17 AI firewall
