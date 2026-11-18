# Gap Register — Risks Not Addressed by FINOS AIGF

| Gap ID | Gap / Missing Risk | How Surfaced | Why FINOS Doesn't Cover It | Disposition | Register ID | Date Added | Reassess |
|---|---|---|---|---|---|---|---|
| G-01 | Pattern-Shift Rejected as Anomaly | Benchmark review — drift metric flagged sustained 'anomaly' clusters | FINOS r-19 covers drift/decay but not the agent actively rejecting a legitimate new-normal as an outlier and failing to adapt. | Added to register | R-27 | 2026-06-30 | Quarterly |
| G-02 | Fabricated Outcome Under Inability to Respond | Incident review — agent returned confident output despite tool failure | FINOS r-4 covers hallucination generally, this is the specific fail-open behavior of guessing instead of abstaining/escalating when unable to answer. | Added to register | R-28 | 2026-06-30 | Quarterly |
| G-03 | Corrupt-Input Propagation Across Agent Trust Boundary | Pre-release review of a connected-agent chain | FINOS r-27 / OP-028 address state poisoning and multi-agent boundaries, this captures a dependent agent implicitly trusting upstream output and skipping revalidation. | Added to register | R-31 | 2026-06-30 | Per release |
| G-04 | Compute Supply Chain & Concentration | Stack-coverage validation (L1) | FINOS scope is model/data/agent, not hardware-layer GPU supply or vendor concentration. | Added to register | R-32 | 2026-06-30 | Quarterly |
| G-05 | Infrastructure Resilience & DR Gap | Stack-coverage validation (L2) | No FINOS risk covers GPU node failure, network partition, or AI-platform disaster recovery. | Added to register | R-33 | 2026-06-30 | Quarterly |
| G-06 |  |  |  |  |  |  |  |
| G-07 | Data Lineage, Skew & Strategic ROI | Stack-coverage validation (L5, L10) | Training-serving skew, lineage/provenance, and business-outcome/ROI risk extend beyond FINOS's model-centric catalogue. | Added to register | R-36, R-37, R-38 | 2026-06-30 | Quarterly |


Refer to #296 for Stack coverage https://github.com/finos/ai-governance-framework/issues/296
