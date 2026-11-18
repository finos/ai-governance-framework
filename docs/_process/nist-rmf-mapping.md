# NIST RMF Mapping — AI Risk Register (SP 800-30 Rev. 1 / SP 800-37 Rev. 2 Crosswalk)

Crosswalks every risk's native Likelihood x Impact score onto NIST SP 800-30 Rev. 1's semi-quantitative scale, derives a NIST-style risk level for Inherent and Residual risk, and maps the register's deployment gate onto NIST SP 800-37 Rev. 2's Authorize-step outcomes. See [nist-rmf-scoring.md](nist-rmf-scoring.md) for full definitions, sourcing, and methodology. This is an initial attempt that is currently under review and will be finalized. At this time the approach is to create a crosswalk, eventually this will be part of the risk register for easier implementation and potentially an application will be made available to create and manage the risk register for an enterprise. Some random scores are inserted (generated) to illustrate how the scoring will appear.

## How This Mapping Works

1. Each risk's Likelihood and Impact (1-5, from the Risk Register) are looked up against the NIST semi-quantitative scale (Very Low-Very High, scored 0-100) — see [nist-rmf-scoring.md](nist-rmf-scoring.md) for full sourcing.
2. Impact is also collapsed to a FIPS 199 potential-impact category (Low/Moderate/High).
3. A NIST semi-quantitative risk score is derived as `(Likelihood Score x Impact Score) / 100`, then banded on the same Very Low-Very High scale, for both Inherent and Residual (control-adjusted) risk.
4. The register's Residual Rating and Deployment Gate are crosswalked to RMF Authorize-step outcomes (ATO / ATO with conditions / Interim Authorization / Denial of ATO).
5. A primary NIST SP 800-53 Rev. 5 control family is suggested per risk as an illustrative starting point for the RMF Select step.

## Formulas

| Metric | Formula | Note |
|---|---|---|
| NIST Likelihood / Impact Score | Lookup against the NIST semi-quantitative scale, keyed on the 1-5 register level | Midpoints per NIST SP 800-30 Rev. 1 Appendix G |
| NIST Semi-Quant Risk Score (Inherent) | `ROUND(Likelihood Score x Impact Score / 100, 1)` | Rescaled to stay on the 0-100 semi-quantitative range |
| NIST Risk Level | Banded via Very Low (0-4) / Low (5-20) / Moderate (21-79) / High (80-95) / Very High (96-100) | Same bands used for Likelihood, Impact, Inherent, and Residual |
| NIST Semi-Quant Risk Score (Residual) | `ROUND(NIST Inherent Score x Mitigation Factor, 1)` | Mitigation Factor from Ctrl Effectiveness (1=1.00, 2=0.80, 3=0.60, 4=0.40, 5=0.25) |

**NIST risk bands** (semi-quantitative, SP 800-30 Rev. 1 Appendix G/I bins): Very Low = 0-4, Low = 5-20, Moderate = 21-79, High = 80-95, Very High = 96-100.

## Risk-Level NIST RMF Mapping

| ID | Domain | Risk | Likelihood (1-5) | NIST Likelihood Level | NIST Likelihood Score | Impact (1-5) | NIST Impact Level | NIST Impact Score | FIPS 199 Impact Category | NIST Risk Score (Inherent) | NIST Risk Level (Inherent) | Ctrl Effectiveness | Mitigation Factor | NIST Risk Score (Residual) | NIST Risk Level (Residual) | Residual Rating (register) | RMF Authorization Recommendation | Primary NIST 800-53 Control Family |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Operational | Hallucination & Inaccurate Outputs | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 3 | 0.6 | 29.4 | Moderate | Moderate | ATO with conditions (POA&M tracked) | SI - System and Information Integrity |
| R-02 | Operational | Foundation Model Versioning | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | CM - Configuration Management |
| R-03 | Operational | Non-Deterministic Behavior | 3 | Moderate | 50 | 3 | Moderate | 50 | Moderate | 25 | Moderate | 3 | 0.6 | 15 | Low | Moderate | ATO with conditions (POA&M tracked) | SI - System and Information Integrity |
| R-04 | Operational | Availability of Foundation Model | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | CP - Contingency Planning |
| R-05 | Operational | Inadequate System Alignment | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | RA - Risk Assessment |
| R-06 | Operational | Bias & Discrimination | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 3 | 0.6 | 29.4 | Moderate | Moderate | ATO with conditions (POA&M tracked) | RA - Risk Assessment |
| R-07 | Operational | Lack of Explainability | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | RA - Risk Assessment |
| R-08 | Operational | Model Overreach / Expanded Use | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | AC - Access Control |
| R-09 | Operational | Data Quality & Drift | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | SI - System and Information Integrity |
| R-10 | Operational | Reputational Risk | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | PM - Program Management |
| R-11 | Operational | Multi-Agent Trust Boundary Violations | 2 | Low | 12.5 | 5 | Very High | 98 | High | 12.3 | Low | 2 | 0.8 | 9.8 | Low | Moderate | ATO with conditions (POA&M tracked) | AC - Access Control |
| R-12 | Security | Information Leaked to Hosted Model | 4 | High | 87.5 | 5 | Very High | 98 | High | 85.8 | High | 3 | 0.6 | 51.5 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SC - System and Communications Protection |
| R-13 | Security | Information Leaked to Vector Store | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | SC - System and Communications Protection |
| R-14 | Security | Tampering with the Foundation Model | 2 | Low | 12.5 | 5 | Very High | 98 | High | 12.3 | Low | 2 | 0.8 | 9.8 | Low | Moderate | ATO with conditions (POA&M tracked) | SI - System and Information Integrity |
| R-15 | Security | Data Poisoning | 2 | Low | 12.5 | 5 | Very High | 98 | High | 12.3 | Low | 2 | 0.8 | 9.8 | Low | Moderate | ATO with conditions (POA&M tracked) | SI - System and Information Integrity |
| R-16 | Security | Prompt Injection | 4 | High | 87.5 | 4 | High | 87.5 | High | 76.6 | Moderate | 3 | 0.6 | 46 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SI - System and Information Integrity |
| R-17 | Security | Agent Action Authorization Bypass | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 2 | 0.8 | 39.2 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | AC - Access Control |
| R-18 | Security | Tool Chain Manipulation & Injection | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 2 | 0.8 | 39.2 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SR - Supply Chain Risk Management |
| R-19 | Security | MCP Server Supply Chain Compromise | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 2 | 0.8 | 39.2 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SR - Supply Chain Risk Management |
| R-20 | Security | Agent State Persistence Poisoning | 2 | Low | 12.5 | 5 | Very High | 98 | High | 12.3 | Low | 2 | 0.8 | 9.8 | Low | Moderate | ATO with conditions (POA&M tracked) | SI - System and Information Integrity |
| R-21 | Security | Agent-Mediated Credential Harvesting | 2 | Low | 12.5 | 5 | Very High | 98 | High | 12.3 | Low | 2 | 0.8 | 9.8 | Low | Moderate | ATO with conditions (POA&M tracked) | IA - Identification and Authentication |
| R-22 | Regulatory | Regulatory Compliance & Oversight | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 3 | 0.6 | 29.4 | Moderate | Moderate | ATO with conditions (POA&M tracked) | CA - Assessment, Authorization, and Monitoring |
| R-23 | Regulatory | Intellectual Property & Copyright | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | PL - Planning |
| R-24 | Regulatory | Information Leaked To Hosted Model - Data Protection & Privacy Compliance | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 3 | 0.6 | 29.4 | Moderate | Moderate | ATO with conditions (POA&M tracked) | PT - PII Processing and Transparency |
| R-25 | Agent Operations | Model Overreach / Expanded Use - Autonomous Decision-Making Beyond Mandate | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 2 | 0.8 | 39.2 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | AC - Access Control |
| R-26 | Agent Operations | Outcome Deviation & Detection Gap | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | AU - Audit and Accountability |
| R-27 | Agent Operations | DQ issues/non-deterministic behavior. Pattern-Shift Rejected as Anomaly | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | AU - Audit and Accountability |
| R-28 | Agent Operations | hallucination/inadequate system alignment, Fabricated Outcome Under Inability to Respond | 4 | High | 87.5 | 5 | Very High | 98 | High | 85.8 | High | 2 | 0.8 | 68.6 | Moderate | Critical | Denial of Authorization to Operate | SI - System and Information Integrity |
| R-29 | Agent Operations | Toolchain / injection/boundary violations Cascading Deviation in Connected Agents (No Rollback) | 3 | Moderate | 50 | 5 | Very High | 98 | High | 49 | Moderate | 2 | 0.8 | 39.2 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | CP - Contingency Planning |
| R-30 | Agent Operations | non-deterministic behavior/boundary violations/Result Skew from Upstream Agent Non-Response | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SI - System and Information Integrity |
| R-31 | Agent Operations | Agent state persistence posioningCorrupt-Input Propagation Across Agent Trust Boundary | 2 | Low | 12.5 | 5 | Very High | 98 | High | 12.3 | Low | 2 | 0.8 | 9.8 | Low | Moderate | ATO with conditions (POA&M tracked) | SC - System and Communications Protection |
| R-32 | Infrastructure & Supply | Compute Supply Chain & Concentration | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SR - Supply Chain Risk Management |
| R-33 | Infrastructure & Supply | Infrastructure Resilience & DR Gap | 2 | Low | 12.5 | 4 | High | 87.5 | High | 10.9 | Low | 2 | 0.8 | 8.7 | Low | Moderate | ATO with conditions (POA&M tracked) | CP - Contingency Planning |
| R-34 | Infrastructure & Supply | Cloud Cost Overrun & FinOps Gap (Denial-of-Wallet) | 4 | High | 87.5 | 3 | Moderate | 50 | Moderate | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | PM - Program Management |
| R-35 | Infrastructure & Supply | Vendor Lock-in & Concentration | 3 | Moderate | 50 | 3 | Moderate | 50 | Moderate | 25 | Moderate | 2 | 0.8 | 20 | Low | Moderate | ATO with conditions (POA&M tracked) | SR - Supply Chain Risk Management |
| R-36 | Data Pipeline | Data drift/Training-Serving Skew & Feature Pipeline Drift | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | SI - System and Information Integrity |
| R-37 | Data Pipeline | Data Lineage & Provenance Gap | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 2 | 0.8 | 35 | Moderate | High | Interim Authorization to Test/Operate (IATT/IATO) | CM - Configuration Management |
| R-38 | Business Outcome | Strategic Misalignment & Failed ROI | 3 | Moderate | 50 | 4 | High | 87.5 | High | 43.8 | Moderate | 3 | 0.6 | 26.3 | Moderate | Moderate | ATO with conditions (POA&M tracked) | PM - Program Management |

## NIST Risk Level Distribution (Inherent vs Residual)

| NIST Risk Level | Inherent Count | Residual Count |
|---|---|---|
| Very Low | 0 | 0 |
| Low | 7 | 9 |
| Moderate | 29 | 29 |
| High | 2 | 0 |
| Very High | 0 | 0 |
| **Total** | **38** | **38** |
