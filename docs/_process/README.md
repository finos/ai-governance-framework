# AI Governance Risk Register — Process Documentation

Converted from `AI_Risk_Register_-_Draft_V3_CVSS_Recalibrated.xlsx`. Reusable, vendor-agnostic risk register
and scoring methodology for AI/agentic systems, referenced against the
[FINOS AI Governance Framework (AIGF)](https://github.com/finos/ai-governance-framework/tree/main/docs/_risks).
Each Markdown file corresponds to a worksheet/tab from the original Excel workbook. During conversion, formatting and structure were adjusted where necessary to make the content more suitable for Markdown and Git-based collaboration. Some editorial modifications were also made to improve consistency and readability.
The underlying risk content and intent have been retained.


## Contents

| File | Covers |
|---|---|
| [assumptions-and-considerations.md](assumptions-and-considerations.md) | Key assumptions and open considerations behind the register |
| [scoring-approach.md](scoring-approach.md) | The 5x5 Likelihood x Impact model, rating bands, control-effectiveness scale, and the residual-risk / deployment-gate logic |
| [cvss-mapping.md](cvss-mapping.md) | Domain-recalibrated mapping of the register's scoring onto the open CVSS v3.1 standard, with a per-domain applicability lookup, per-risk overrides, and a heat map by domain |
| [scoring-matrix.md](scoring-matrix.md) | Visual 5x5 heat map and descriptor anchors for each Likelihood/Impact level |
| [risk-register.md](risk-register.md) | The core register — 38 risks across Operational, Security, Regulatory, Agent Operations, Infrastructure & Supply, Data Pipeline, and Business Outcome domains, each with inherent & residual scoring, owner, controls, and status |
| [address-the-risk.md](address-the-risk.md) | Options to address risk (mitigate/transfer/remove/accept), acceptance & removal criteria, and the kill-switch / termination control |
| [illustrative-benchmark.md](illustrative-benchmark.md) | Per-domain and per-stage benchmark targets, current values, and reassessment cadence |
| [gap-register.md](gap-register.md) | Risks identified that FINOS AIGF doesn't cover, and how each was closed |
| [lifecycle-triggers.md](lifecycle-triggers.md) | Events that require a (re)assessment, mapped to lifecycle stage and the risks each event most affects |
| [stack-coverage.md](stack-coverage.md) | Validation of the register against the 10-layer AI stack / parallel business architecture |
| [terminology-mapping.md](terminology-mapping.md) | Shared glossary reconciling register terms with FINOS / NIST / EU AI Act / OWASP language |
| [assessment-summary.md](assessment-summary.md) | Placeholder — rollup of counts/averages by domain and rating (not yet built in the source workbook) |


## Notes
## Risk Identifiers

The original risk identifiers from the source workbook have been preserved wherever possible to maintain traceability back to the source material.

Where FINOS identifiers already existed, those identifiers have also been retained or mapped to the corresponding risks.

Additional identifiers have been introduced where necessary to support risks, controls, or records that did not have an existing FINOS identifier. These mappings are intended to allow the material to be reconciled and progressively merged with the broader FINOS AI Governance Framework as part of the ongoing development exercise.

## Risk Scoring

The original risk scoring has been retained to preserve the assessment and prioritization represented in the source workbook.

Where applicable, the original scoring has also been mapped to the Common Vulnerability Scoring System (CVSS) to provide a standardized vulnerability-oriented reference point.

The original scoring model is intentionally retained because it considers dimensions of AI and enterprise risk that extend beyond the scope of CVSS. CVSS primarily addresses the severity of technical vulnerabilities and does not fully represent several governance, operational, model, regulatory, data, ethical, and business-impact considerations relevant to AI risk management.

Accordingly, at this time the CVSS will be treated as a complementary mapping rather than a replacement for the original AI risk scoring methodology - will work on convert this to a clear industry standard methodology. 

## Ongoing Integration

These files represent working material intended to support the continuing evolution of the FINOS AI Governance Framework.

Identifier normalization, scoring alignment, terminology, risk consolidation, and integration with other FINOS framework components may continue to evolve as the material is reviewed and merged.

## Additional Notes

- More detailed than originally intended — still evolving; this reflects the first draft and may be simplified.
- Some AI was used to accelerate curating/merging content.
- Tables adapted from the source spreadsheet's cached values at the time of conversion (2026-07-20); the workbook
  reflects anything computed by formula - additional changes made to markdowns may not be reflected in the original version of workbook.
