# Stack Coverage Validation — Register vs Business / Technology Architecture

See mapping detail: https://github.com/finos/ai-governance-framework (issue #296) and https://github.com/user-attachments/files/28842813/AIGovernnaceFramework-FINOS-draft.pdf

Validates the risk register against the 10-layer AI stack and its parallel business architecture. For each layer: the business function, the technology layer, the layer-level risk the architecture asserts, the register risks that cover it, and a coverage determination. Gaps closed by new risks R-32 to R-38 are marked.

## Layer-by-Layer Coverage

| Layer | Business Function | Technology Layer | Architecture Risk (asserted) | Register Coverage | Coverage Determination | New Risk |
|---|---|---|---|---|---|---|
| L10 | Business outcome (revenue, NPS, ROI) | End user (chat, voice, API) | Reputational & strategic risk — brand, failed ROI, trust | R-10 Reputational (operational) | Partial → Closed | R-38 |
| L9 | Product & UX (features, journeys) | Application (app logic, UX shell) | UX & hallucination risk — harmful outputs, over-reliance, UI bias | R-01, R-05, R-06, R-27, R-29 | Covered | — |
| L8 | Integration & workflow (automation) | API & orchestration (RAG, agents) | Security & integration risk — prompt injection, API abuse, agent runaway | R-11, R-16-22, R-25, R-30-31 | Covered | — |
| L7 | AI capability (model selection) | Inference & serving (vLLM, KServe) | Model performance & bias risk — drift, accuracy decay, discriminatory output | R-03, R-06 | Covered | — |
| L6 | Governance & risk (ethics, audit) | Model layer (weights, fine-tuning) | Regulatory & compliance risk — EU AI Act, GDPR, explainability | R-02, R-07, R-08, R-14, R-22-23 | Covered | — |
| L5 | MLOps & delivery (lifecycle, CI/CD) | ML frameworks (PyTorch, JAX) | DATA RISK — training & pipeline: poisoned data, skew, stale labels, lineage gaps | R-09, R-13, R-15 | Partial → Closed | R-36, R-37 |
| L4 | Data strategy (products, contracts) | Acceleration libraries (CUDA, TensorRT) | DATA RISK — quality & privacy: PII leakage, consent gaps, contract breaches | R-12, R-24 | Covered | — |
| L3 | Cloud & platform (CapEx, OpEx, vendors) | OS & virtualization (Linux, K8s) | Operational & vendor risk — lock-in, cost overrun, SLA breach | R-04 (availability only) | Gap → Closed | R-34, R-35 |
| L2 | Infra operations (SRE, reliability) | Firmware & drivers (CUDA driver, ROCm) | Infrastructure & resilience risk — GPU failure, network partition, DR gaps | — (none) | Gap → Closed | R-33 |
| L1 | Compute investment (GPU, cloud spend) | Hardware (GPU, CPU, HBM) | Supply chain & concentration risk — GPU shortage, single-vendor, cost | R-19 (MCP supply only) | Gap → Closed | R-32 |

## Gap List — Exposures Now Closed

| New ID | Layer | Gap Closed | Why It Was Missing | Domain Added |
|---|---|---|---|---|
| R-32 | L1 | Compute supply chain & concentration | FINOS focuses on model/data/agent risk, not hardware-layer GPU supply or vendor concentration. | Infrastructure & Supply |
| R-33 | L2 | Infrastructure resilience & DR gap | No FINOS risk covers GPU node failure, network partition, or AI-platform DR. | Infrastructure & Supply |
| R-34 | L3 | Cloud cost overrun & FinOps (Denial-of-Wallet) | Cost/FinOps exposure sits outside FINOS, only availability (AIR-OP-007) is partial. | Infrastructure & Supply |
| R-35 | L3 | Vendor lock-in & concentration | Provider/cloud lock-in and portability not addressed as a discrete FINOS risk. | Infrastructure & Supply |
| R-36 | L5 | Training-serving skew & feature drift | FINOS AIR-OP-019 covers drift broadly, serving skew & feature-pipeline parity are specific extensions. | Data Pipeline |
| R-37 | L5 | Data lineage & provenance gap | Lineage/provenance as an auditable control is implied but not a discrete FINOS risk. | Data Pipeline |
| R-38 | L10 | Strategic misalignment & failed ROI | Business-outcome / ROI risk is above FINOS's model-centric scope. | Business Outcome |

## Layer Coverage Count (live from register Stack Layer column)

| Layer | # Risks |
|---|---|
| L1 | 2 |
| L2 | 1 |
| L3 | 3 |
| L4 | 2 |
| L5 | 6 |
| L6 | 6 |
| L7 | 2 |
| L8 | 10 |
| L9 | 4 |
| L10 | 2 |


Coverage Determination key:  Covered = adequately addressed by existing risks  |  Partial → Closed = thin coverage now reinforced  |  Gap → Closed = absent in register, new risk added.  Data-risk layers (L4-L5) shown in red per the architecture's elevated data-risk zone.
