# CVSS-Style Mapping — Domain-Recalibrated

Rescales the register's Likelihood x Impact scoring onto the open CVSS v3.1 0-10 scale (FIRST.org CVSS v3.1 Specification), then recalibrates that mapping per AI governance risk domain, because CVSS was designed to score a technical vulnerability's exploitability and impact — a concept that fits some AI governance domains far better than others.
Left in at this time as this addresses vulnerability aspects. NIST-RMF scoring used and a mapping created in addition to address overall risks from industry standards perspective.

## How the recalibration works

1) Every risk still gets a raw CVSS Base Score from its Likelihood x Impact (unchanged formula from the prior version).
2) Each risk's Domain is looked up in the table below to get a default CVSS Applicability (Applicable / Partially Applicable / Not Applicable) and a Domain Weight.
3) An analyst can override that default for an individual risk in the blue Applicability Override column, e.g. where one risk in an otherwise-technical domain is really a business or compliance risk.
4) The recalibrated score = raw CVSS Base Score x effective weight — or "N/A" if the risk is Not Applicable, in which case the Recommended Scoring Adjustment column states how to score it instead.
5) The same recalibration is applied to the residual (control-adjusted) score.

## Formulas

| Metric | Formula | Notes |
|---|---|---|
| CVSS Base Score (raw) | ROUND( (Likelihood x Impact) / 25 x 10 , 1 ) | Unchanged linear rescale of Inherent Score (1-25) onto CVSS's 0-10 range. |
| Effective Applicability | Applicability Override, if set; otherwise the risk's Domain default | Lets an analyst override the domain default for one risk without changing the whole domain. |
| Effective Weight | 1.0 if Applicable; Domain Weight if Partially Applicable; N/A (no score) if Not Applicable | The recalibration factor actually applied to the raw CVSS score. |
| Recalibrated CVSS Base | IF(Effective Applicability = Not Applicable, "N/A", ROUND(CVSS Base Score (raw) x Effective Weight , 1)) | The domain- and risk-aware CVSS-style score; this is the number to report, not the raw score. |
| Recalibrated CVSS-Adjusted | IF(Effective Applicability = Not Applicable, "N/A", ROUND(Recalibrated CVSS Base x Mitigation Factor , 1)) | Mirrors the register's Residual = Inherent x Mitigation Factor logic, applied to the recalibrated base. |

Severity bands (official, unchanged): None = 0.0, Low = 0.1-3.9, Medium = 4.0-6.9, High = 7.0-8.9, Critical = 9.0-10.0. Source: FIRST.org CVSS v3.1 Specification, Table 14. "N/A" is not a CVSS band — it flags a risk this scoring system should not be used for.

## AI Governance Domain → CVSS Applicability Lookup

| Domain | CVSS Applicability | Weight | Rationale | Recommended Scoring Adjustment |
|---|---|---|---|---|
| Operational | Partially Applicable | 0.7 | Failure modes like hallucination, model-version drift, or degraded output quality usually have no discrete attacker — CVSS's exploitability metrics (attack vector, complexity, privileges, user interaction) assume one. The impact side (integrity/availability of correct output) still translates. | Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure. |
| Security | Applicable | 1 | Prompt injection, jailbreaks, data poisoning, and similar risks are adversarial exploitation of a defined technical flaw against a defined attack surface — exactly what CVSS was built to score. | None needed; the CVSS mapping applies directly. |
| Regulatory | Not Applicable | N/A | Regulatory / compliance failure is a legal and process risk. There is no attacker, no attack vector, and no technical flaw being exploited, so a CVSS-style exploitability score is meaningless here. | Do not report a CVSS-equivalent score. Score and report on the register's native Likelihood x Impact scale only, anchoring Impact to regulatory/legal consequence (fines, license loss, reportability). |
| Agent Operations | Applicable | 1 | Authorization bypass, tool-chain manipulation, MCP supply-chain compromise, and credential harvesting are technical exploits against a defined agentic attack surface, directly analogous to CVSS's targets. | None needed; the CVSS mapping applies directly. |
| Infrastructure & Supply | Partially Applicable | 0.6 | Availability/DR failures (node failure, network partition) translate reasonably to CVSS's Availability impact metric. But cost overrun (FinOps) and vendor lock-in in this domain are business/financial exposure with no technical exploit surface at all. | Apply the domain weight for availability/resilience risks. For risks that are purely business/financial exposure (see per-risk override below), treat as Not Applicable and score on native Likelihood x Impact only. |
| Data Pipeline | Partially Applicable | 0.9 | Training-serving skew, feature drift, and lineage/provenance gaps are technical data-integrity failures with a definable failure surface, reasonably CVSS-analogous on Integrity — but they are not always attacker-driven, so a small down-weight is applied. | CVSS mapping applies with light down-weighting; native score remains the reference figure for lineage-specific audit findings. |
| Business Outcome | Not Applicable | N/A | Strategic misalignment and failed ROI are business-strategy risk with no technical exploit surface, no attacker, and no confidentiality/integrity/availability dimension. | Do not report a CVSS-equivalent score. Score and report on the register's native Likelihood x Impact scale only, and route to business/portfolio governance rather than a security forum. |

## Control Effectiveness → Mitigation Factor

| Ctrl Effectiveness | Mitigation Factor |
|---|---|
| 1 | 1 |
| 2 | 0.8 |
| 3 | 0.6 |
| 4 | 0.4 |
| 5 | 0.25 |

## Risk-Level CVSS Mapping (domain-recalibrated)

Core figures per risk. Where Effective Applicability is not "Applicable", the CVSS-equivalent score is N/A by design — see the Recommended Scoring Adjustment notes that follow the table.

| ID | Domain | Risk | Likelihood | Impact | Inherent | CVSS Base (raw) | Effective Applicability | Effective Weight | Recal. Base | Base Severity | Recal. Adjusted | Adjusted Severity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Operational | Hallucination & Inaccurate Outputs | 3 | 5 | 15 | 6 | Partially Applicable | 0.7 | 4.2 | Medium | 2.5 | Low |
| R-02 | Operational | Foundation Model Versioning | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-03 | Operational | Non-Deterministic Behavior | 3 | 3 | 9 | 3.6 | Partially Applicable | 0.7 | 2.5 | Low | 1.5 | Low |
| R-04 | Operational | Availability of Foundation Model | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-05 | Operational | Inadequate System Alignment | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-06 | Operational | Bias & Discrimination | 3 | 5 | 15 | 6 | Partially Applicable | 0.7 | 4.2 | Medium | 2.5 | Low |
| R-07 | Operational | Lack of Explainability | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-08 | Operational | Model Overreach / Expanded Use | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-09 | Operational | Data Quality & Drift | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-10 | Operational | Reputational Risk | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.7 | 3.4 | Low | 2 | Low |
| R-11 | Operational | Multi-Agent Trust Boundary Violations | 2 | 5 | 10 | 4 | Partially Applicable | 0.7 | 2.8 | Low | 2.2 | Low |
| R-12 | Security | Information Leaked to Hosted Model | 4 | 5 | 20 | 8 | Applicable | 1 | 8 | High | 4.8 | Medium |
| R-13 | Security | Information Leaked to Vector Store | 3 | 4 | 12 | 4.8 | Applicable | 1 | 4.8 | Medium | 2.9 | Low |
| R-14 | Security | Tampering with the Foundation Model | 2 | 5 | 10 | 4 | Applicable | 1 | 4 | Medium | 3.2 | Low |
| R-15 | Security | Data Poisoning | 2 | 5 | 10 | 4 | Applicable | 1 | 4 | Medium | 3.2 | Low |
| R-16 | Security | Prompt Injection | 4 | 4 | 16 | 6.4 | Applicable | 1 | 6.4 | Medium | 3.8 | Low |
| R-17 | Security | Agent Action Authorization Bypass | 3 | 5 | 15 | 6 | Applicable | 1 | 6 | Medium | 4.8 | Medium |
| R-18 | Security | Tool Chain Manipulation & Injection | 3 | 5 | 15 | 6 | Applicable | 1 | 6 | Medium | 4.8 | Medium |
| R-19 | Security | MCP Server Supply Chain Compromise | 3 | 5 | 15 | 6 | Applicable | 1 | 6 | Medium | 4.8 | Medium |
| R-20 | Security | Agent State Persistence Poisoning | 2 | 5 | 10 | 4 | Applicable | 1 | 4 | Medium | 3.2 | Low |
| R-21 | Security | Agent-Mediated Credential Harvesting | 2 | 5 | 10 | 4 | Applicable | 1 | 4 | Medium | 3.2 | Low |
| R-22 | Regulatory | Regulatory Compliance & Oversight | 3 | 5 | 15 | 6 | Not Applicable | N/A | N/A | N/A | N/A | N/A |
| R-23 | Regulatory | Intellectual Property & Copyright | 3 | 4 | 12 | 4.8 | Not Applicable | N/A | N/A | N/A | N/A | N/A |
| R-24 | Regulatory | Information Leaked To Hosted Model - Data Protection & Privacy Compliance | 3 | 5 | 15 | 6 | Not Applicable | N/A | N/A | N/A | N/A | N/A |
| R-25 | Agent Operations | Model Overreach / Expanded Use - Autonomous Decision-Making Beyond Mandate | 3 | 5 | 15 | 6 | Applicable | 1 | 6 | Medium | 4.8 | Medium |
| R-26 | Agent Operations | Outcome Deviation & Detection Gap | 3 | 4 | 12 | 4.8 | Applicable | 1 | 4.8 | Medium | 3.8 | Low |
| R-27 | Agent Operations | DQ issues/non-deterministic behavior. Pattern-Shift Rejected as Anomaly | 3 | 4 | 12 | 4.8 | Applicable | 1 | 4.8 | Medium | 3.8 | Low |
| R-28 | Agent Operations | hallucination/inadequate system alignment, Fabricated Outcome Under Inability to Respond | 4 | 5 | 20 | 8 | Applicable | 1 | 8 | High | 6.4 | Medium |
| R-29 | Agent Operations | Toolchain / injection/boundary violations Cascading Deviation in Connected Agents (No Rollback) | 3 | 5 | 15 | 6 | Applicable | 1 | 6 | Medium | 4.8 | Medium |
| R-30 | Agent Operations | non-deterministic behavior/boundary violations/Result Skew from Upstream Agent Non-Response | 3 | 4 | 12 | 4.8 | Applicable | 1 | 4.8 | Medium | 3.8 | Low |
| R-31 | Agent Operations | Agent state persistence posioningCorrupt-Input Propagation Across Agent Trust Boundary | 2 | 5 | 10 | 4 | Applicable | 1 | 4 | Medium | 3.2 | Low |
| R-32 | Infrastructure & Supply | Compute Supply Chain & Concentration | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.6 | 2.9 | Low | 2.3 | Low |
| R-33 | Infrastructure & Supply | Infrastructure Resilience & DR Gap | 2 | 4 | 8 | 3.2 | Partially Applicable | 0.6 | 1.9 | Low | 1.5 | Low |
| R-34 | Infrastructure & Supply | Cloud Cost Overrun & FinOps Gap (Denial-of-Wallet) | 4 | 3 | 12 | 4.8 | Not Applicable | N/A | N/A | N/A | N/A | N/A |
| R-35 | Infrastructure & Supply | Vendor Lock-in & Concentration | 3 | 3 | 9 | 3.6 | Not Applicable | N/A | N/A | N/A | N/A | N/A |
| R-36 | Data Pipeline | Data drift/Training-Serving Skew & Feature Pipeline Drift | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.9 | 4.3 | Medium | 3.4 | Low |
| R-37 | Data Pipeline | Data Lineage & Provenance Gap | 3 | 4 | 12 | 4.8 | Partially Applicable | 0.9 | 4.3 | Medium | 3.4 | Low |
| R-38 | Business Outcome | Strategic Misalignment & Failed ROI | 3 | 4 | 12 | 4.8 | Not Applicable | N/A | N/A | N/A | N/A | N/A |


### Recommended Scoring Adjustments (risks not fully CVSS-applicable)

- **R-01** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-02** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-03** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-04** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-05** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-06** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-07** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-08** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-09** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-10** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-11** (Operational): Report the register's native Likelihood x Impact score as the primary figure. Treat the recalibrated CVSS-equivalent as directional security-framing context only, not a compliance-grade figure.
- **R-22** (Regulatory): Do not report a CVSS-equivalent score. Score and report on the register's native Likelihood x Impact scale only, anchoring Impact to regulatory/legal consequence (fines, license loss, reportability).
- **R-23** (Regulatory): Do not report a CVSS-equivalent score. Score and report on the register's native Likelihood x Impact scale only, anchoring Impact to regulatory/legal consequence (fines, license loss, reportability).
- **R-24** (Regulatory): Do not report a CVSS-equivalent score. Score and report on the register's native Likelihood x Impact scale only, anchoring Impact to regulatory/legal consequence (fines, license loss, reportability).
- **R-32** (Infrastructure & Supply): Apply the domain weight for availability/resilience risks. For risks that are purely business/financial exposure (see per-risk override below), treat as Not Applicable and score on native Likelihood x Impact only.
- **R-33** (Infrastructure & Supply): Apply the domain weight for availability/resilience risks. For risks that are purely business/financial exposure (see per-risk override below), treat as Not Applicable and score on native Likelihood x Impact only.
- **R-34** (Infrastructure & Supply (per-risk override)): Cost/FinOps exposure has no attacker or technical flaw. Score on native Likelihood x Impact only.
- **R-35** (Infrastructure & Supply (per-risk override)): Vendor concentration is commercial exposure, not an exploitable vulnerability. Score on native Likelihood x Impact only.
- **R-36** (Data Pipeline): CVSS mapping applies with light down-weighting; native score remains the reference figure for lineage-specific audit findings.
- **R-37** (Data Pipeline): CVSS mapping applies with light down-weighting; native score remains the reference figure for lineage-specific audit findings.
- **R-38** (Business Outcome): Do not report a CVSS-equivalent score. Score and report on the register's native Likelihood x Impact scale only, and route to business/portfolio governance rather than a security forum.

## Heat Map by AI Governance Domain (recalibrated, control-adjusted)

Counts each domain's 38 risks by their recalibrated CVSS-Adjusted severity. Domains scored Not Applicable show entirely in the N/A column by design — that is the correct, honest read for a domain this scoring system was never meant to grade, not a data gap.

| Domain | Domain-Default Applicability | Risks | Avg Recal. Adjusted Score | None | Low | Medium | High | Critical | N/A |
|---|---|---|---|---|---|---|---|---|---|
| Operational | Partially Applicable | 11 | 2.1 | 0 | 11 | 0 | 0 | 0 | 0 |
| Security | Applicable | 10 | 3.9 | 0 | 6 | 4 | 0 | 0 | 0 |
| Regulatory | Not Applicable | 3 | N/A | 0 | 0 | 0 | 0 | 0 | 3 |
| Agent Operations | Applicable | 7 | 4.4 | 0 | 4 | 3 | 0 | 0 | 0 |
| Infrastructure & Supply | Partially Applicable | 4 | 1.9 | 0 | 2 | 0 | 0 | 0 | 2 |
| Data Pipeline | Partially Applicable | 2 | 3.4 | 0 | 2 | 0 | 0 | 0 | 0 |
| Business Outcome | Not Applicable | 1 | N/A | 0 | 0 | 0 | 0 | 0 | 1 |
| Total |  | 38 |  | 0 | 25 | 7 | 0 | 0 | 6 |
