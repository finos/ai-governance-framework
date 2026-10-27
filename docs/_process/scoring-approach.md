# Scoring Approach

How inherent risk, control effectiveness, residual risk, and the deployment gate are calculated.

## Inherent Risk = Likelihood x Impact

Inherent risk is the exposure before mitigating controls are credited. Score Likelihood and Impact independently on the 1-5 anchors below, then multiply. The product ranges from 1 to 25 and maps to a four-tier rating band.

### Likelihood
| Level | Rating | Description |
|---|---|---|
| 1 | Rare | May occur only in exceptional circumstances, no known occurrence in similar systems. |
| 2 | Unlikely | Could occur but not expected, isolated instances of precedence in the industry. |
| 3 | Possible | Might occur at some point, has happened in similar AI deployments. |
| 4 | Likely | Expected to occur in most circumstances within the assessment period. |
| 5 | High Probability (Certainty) | Expected to occur frequently / continuously when there is not addressed. |

### Impact
| Level | Rating | Description |
|---|---|---|
| 1 | Insignificant | Negligible effect, no customer harm, no regulatory interest, easily absorbed. |
| 2 | Minor | Limited, contained harm, minor remediation, no reportable breach. |
| 3 | Moderate | Noticeable customer / operational harm, possible regulatory attention, manageable cost. |
| 4 | Major | Significant harm, financial loss, or compliance breach, senior escalation, reportable. |
| 5 | Severe | Systemic harm, large fines, license / reputational damage, or safety impact at scale. |

### Rating Bands
| Range | Rating | Governance Consideration |
|---|---|---|
| 1 – 4 | Low | Acceptable with baseline controls and routine oversight. |
| 5 – 9 | Moderate | Acceptable with standard guardrails, monitoring, and periodic review. |
| 10 – 15 | High | Deploy only with mandatory controls, approval gates, and active monitoring. |
| 16 – 25 | Critical | Do not deploy as-is, redesign to reduce exposure or require human-in-the-loop. Go-no-go. (if deployed - Kill) |

## Control Effectiveness and Residual Risk

Rate the effectiveness of existing controls on a 1-5 scale (1 = Ineffective through 5 = Fully effective). reduces exposure 

Residual Score = Inherent Score × Mitigation Factor, where the increase in controls reduce exposure.

Governance forum reviews and escalates/makes decision on residual risk.

| Level | Effectiveness | Implication | Mitigation Factor | Residual = Inherent x Factor |
|---|---|---|---|---|
| 1 | Ineffective | Controls absent or untested | 1.00 | 100% |
| 2 | Limited | Partial / ad-hoc controls | 0.80 | 80% |
| 3 | Moderate | Standard controls, some gaps | 0.60 | 60% |
| 4 |  Strong | Robust, tested controls | 0.40 | 40% |
| 5 |  Fully effective | Comprehensive, continuously assured | 0.25 | 25% |

## Risk Tolerance Deployment Gate (Go / No-Go)

| Residual Rating | Tolerance Stance | Rating | Gate Decision | Required Sign-off |
|---|---|---|---|---|
| Low | Accept | PASS | Proceed | Product / risk owner |
| Moderate | Accept w/ monitoring | PASS | Proceed with conditions | AI governance lead |
| High | Mitigate before deploy | CONDITIONAL | Controls must close gap | Governance forum / CRO delegate |
| Critical | Avoid / redesign | FAIL | Block deployment/Kill | Governance forum + accountable executive |
