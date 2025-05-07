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

| **Level** | **Scope**       | **Control**                                                                                                                | **Pros**                                | **Cons / Residual Risk**          |
| --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | --------------------------------- |
| **0**     | Org-wide        | **Enterprise spending cap** (configured accounting/controlling; enforced via payment provider)                             | Bullet-proof stop-loss; zero code       | Binary outage if mis-sized; blunt |
| **1**     | Org-wide        | **Real-time budget alerts** (configured in model hosting infra, hyperscaler)                                               | 2-min setup; low friction               | Reactive; alert fatigue           |
| **2**     | Billing account | **Daily/Weekly/monthly spend limits** enforced by FinOps                                                                   | Aligns to GL codes & POs                | Coarse; slow to amend             |
| **3**     | Project / env   | **IaC quota policy** (`quota <= $X/day` in ex. terraform / ansible configs)                                                | Declarative, auditable                  | Requires IaC discipline           |
| **4**     | API key / team  | **Token & request quotas** in central API Gateway, Proxy middleware                                                        | Fine-grained; supports charge-back      | Custom code; state mgmt           |
| **5**     | Session         | **Adaptive & Semantic rate-limit** (LLM: Prompt & Semantic Policy. ML: risk-score × spend velocity  )                      | Graceful degradation; Semantic Anomoly Detections stops misuse fast | Experimental, Needs ML baseline & tuning |
