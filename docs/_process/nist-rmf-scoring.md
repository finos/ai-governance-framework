# NIST RMF Scoring

Crosswalks the register's existing Likelihood x Impact model onto NIST's risk-assessment and risk-management framework terminology covering NIST SP 800-30 Rev. 1 (Guide for Conducting Risk Assessments), NIST SP 800-37 Rev. 2 (Risk Management Framework for Information Systems and Organizations), FIPS PUB 199, and NIST SP 800-53 Rev. 5, so the register can be read against federal/NIST-aligned risk taxonomy alongside the CVSS and FINOS AIGF framing already provided. See [nist-rmf-mapping.md](nist-rmf-mapping.md) for the resulting per-risk crosswalk. This is a first attempt and requires additional work. Markdown aligned with work originally done on a spreadsheet hence some residual references may remain - read accordingly.

## NIST RMF — Seven-Step Process and Where This Register Fits

| Step | RMF Step Name | NIST Activity | Where It Lives |
|---|---|---|---|
| 1 | Prepare | Establish context, roles, and organizational risk tolerance before assessing individual risks. | Scoring Approach Section (Rating Bands, Risk Tolerance Deployment Gate); Assumptions & Considerations tab. |
| 2 | Categorize | Determine the potential impact level of the system/information (FIPS 199: Low/Moderate/High) based on worst-case harm to confidentiality, integrity, or availability. | NIST RMF Mapping — FIPS 199 Impact Category column, derived from each risk's Impact rating. |
| 3 | Select | Choose the security and privacy controls (NIST SP 800-53 Rev. 5 control families) needed to address the categorized risk. | NIST RMF Mapping — Primary NIST 800-53 Control Family column (illustrative starting point). |
| 4 | Implement | Deploy the selected controls and document how they are implemented. | Risk Register Section  — Existing Controls column. |
| 5 | Assess | Evaluate whether the implemented controls are operating effectively. | Risk Register Section — Ctrl Effectiveness column; Scoring Approach tab — effectiveness scale. |
| 6 | Authorize | A designated Authorizing Official weighs residual risk and issues a risk-acceptance decision. | Scoring Approach Section  — Risk Tolerance Deployment Gate; crosswalked below to NIST authorization outcomes. |
| 7 | Monitor | Continuously track control effectiveness and risk posture, and reassess on a defined cadence or triggering event. | Risk Register tab — Status column; Lifecycle Triggers Section. |

## Likelihood Crosswalk — Register (1-5) to NIST SP 800-30 Rev. 1

| Register Level | Register Rating | NIST Qualitative Value | NIST Semi-Quantitative Range (0-100) | Semi-Quant Midpoint (used here) |
|---|---|---|---|---|
| 1 | Rare | Very Low | 0 - 4 | 2 |
| 2 | Unlikely | Low | 5 - 20 | 12.5 |
| 3 | Possible | Moderate | 21 - 79 | 50 |
| 4 | Likely | High | 80 - 95 | 87.5 |
| 5 | High Probability (Certainty) | Very High | 96 - 100 | 98 |

*Source: NIST SP 800-30 Rev. 1, Guide for Conducting Risk Assessments, Appendix G (Assessment Scales — Likelihood of Threat Event Initiation/Occurrence), semi-quantitative values. Register levels are mapped 1:1 onto NIST's five qualitative bands in ascending order.*

## Impact Crosswalk — Register (1-5) to NIST SP 800-30 Rev. 1 and FIPS 199

| Register Level | Register Rating | NIST Qualitative Value | NIST Semi-Quant Range | Midpoint | FIPS 199 Potential Impact Category |
|---|---|---|---|---|---|
| 1 | Insignificant | Very Low | 0 - 4 | 2 | Low |
| 2 | Minor | Low | 5 - 20 | 12.5 | Low |
| 3 | Moderate | Moderate | 21 - 79 | 50 | Moderate |
| 4 | Major | High | 80 - 95 | 87.5 | High |
| 5 | Severe | Very High | 96 - 100 | 98 | High |

*FIPS PUB 199 (Standards for Security Categorization of Federal Information and Information Systems) defines only three potential-impact levels based on worst-case effect on confidentiality, integrity, or availability: Low = limited adverse effect; Moderate = serious adverse effect; High = severe or catastrophic adverse effect (including loss of life or serious life-threatening injury). The register's five-level Impact scale is collapsed onto these three for Categorize-step reporting.*

## Deriving an Overall NIST-Style Risk Score and Level

NIST SP 800-30 Rev. 1 does not publish one fixed, universal combination table; it directs organizations to define and document a risk-level matrix appropriate to their assessment (Section 3.7.1 approach of the original SP 800-30, carried forward as the semi-quantitative method in Rev. 1 Appendix I). This file applies NIST's own semi-quantitative bins consistently across Likelihood, Impact, and combined Risk so the result is fully auditable from [nist-rmf-mapping.md](nist-rmf-mapping.md).

| Metric | Formula | Note |
|---|---|---|
| NIST Semi-Quantitative Risk Score | `ROUND(Likelihood Score x Impact Score / 100, 1)` | Mirrors NIST's likelihood-probability x impact-value approach (SP 800-30 original Table 3-6), rescaled to stay on the 0-100 semi-quantitative range |
| NIST Risk Level | Banded on the same Very Low (0-4) / Low (5-20) / Moderate (21-79) / High (80-95) / Very High (96-100) scale used for Likelihood and Impact | Applied to both the Inherent score and the Residual (control-adjusted) score |
| NIST Residual Score | `ROUND(NIST Inherent Score x Mitigation Factor, 1)` | Mirrors the register's own Residual = Inherent x Mitigation Factor logic |

### NIST Risk Bands (applied to Likelihood, Impact, and combined Risk Score)

| Range | Rating | Note |
|---|---|---|
| 0 - 4 | Very Low | Negligible; routine monitoring only. |
| 5 - 20 | Low | Acceptable with baseline controls. |
| 21 - 79 | Moderate | Acceptable with standard guardrails and monitoring. |
| 80 - 95 | High | Deploy only with mandatory controls and active monitoring. |
| 96 - 100 | Very High | Do not deploy as-is; redesign, add human-in-the-loop, or escalate for authorization decision. |

## Authorization Decision Crosswalk (RMF Step 6 — Authorize)

| Register Gate Decision | Register Sign-off | NIST RMF Authorization Outcome | Typical NIST Authorizing Role |
|---|---|---|---|
| Proceed | Product / risk owner | Authorization to Operate (ATO) | Authorizing Official (AO) |
| Proceed with conditions | AI governance lead | ATO with conditions (POA&M tracked) | AO or AO-designated representative |
| Controls must close gap | Governance forum / CRO delegate | Interim Authorization to Test/Operate (IATT/IATO), pending POA&M closure | AO |
| Block deployment/Kill | Governance forum + accountable executive | Denial of Authorization to Operate (Denial of ATO) | AO / senior accountable official |

## NIST SP 800-53 Rev. 5 Control Families (reference for RMF Select step)

| Code | Control Family |
|---|---|
| AC | Access Control |
| AT | Awareness and Training |
| AU | Audit and Accountability |
| CA | Assessment, Authorization, and Monitoring |
| CM | Configuration Management |
| CP | Contingency Planning |
| IA | Identification and Authentication |
| IR | Incident Response |
| MA | Maintenance |
| MP | Media Protection |
| PE | Physical and Environmental Protection |
| PL | Planning |
| PM | Program Management |
| PS | Personnel Security |
| PT | PII Processing and Transparency |
| RA | Risk Assessment |
| SA | System and Services Acquisition |
| SC | System and Communications Protection |
| SI | System and Information Integrity |
| SR | Supply Chain Risk Management |

*The Primary Control Family assigned to each risk in [nist-rmf-mapping.md](nist-rmf-mapping.md) is an illustrative starting point for the RMF Select step, reflecting the risk's dominant control need. Most risks implicate more than one family in practice (e.g., RA and CA together); treat the single family shown as a pointer for control selection, not a compliance determination.*

## References

- NIST SP 800-30 Rev. 1 — https://doi.org/10.6028/NIST.SP.800-30r1
- NIST SP 800-37 Rev. 2 — https://doi.org/10.6028/NIST.SP.800-37r2
- FIPS PUB 199 - https://doi.org/10.6028/NIST.FIPS.199
- NIST SP 800-53 Rev. 5 - https://doi.org/10.6028/NIST.SP.800-53r5
