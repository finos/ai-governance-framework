# Benchmarks — Define, Measure, Reassess

A benchmark is a target threshold for a section (domain) or a lifecycle stage. Set the target, record the current measured value, and the Status auto-flags whether it is Met or a Gap. Reassess on the stated cadence.

1. Define a measurable target per section and per stage (e.g. 'avg residual ≤ 8', 'gate pass-rate ≥ 90%').   2. Record the current value from the register or your monitoring.   3. Status compares the two against the target direction.   4. Reassess each benchmark on its cadence, and whenever a lifecycle trigger fires. Benchmarks are versioned — capture the baseline date so drift in the benchmark itself is visible.

## Section Benchmarks (per domain)

| Section / Domain | Benchmark Metric | Target | Current | Status | Reassess Cadence | Owner |
|---|---|---|---|---|---|---|
| Operational | Avg residual score ≤ target | 8 |  |  | Quarterly | Head of AI Governance |
| Security | Avg residual score ≤ target | 8 |  |  | Quarterly | CISO |
| Regulatory | Avg residual score ≤ target | 7 |  |  | On reg change | Chief Compliance Officer |
| Agent Operations | Avg residual score ≤ target | 8 |  |  | Monthly | Head of AI Governance |
| Infrastructure & Supply | Avg residual score ≤ target | 8 |  |  | Quarterly | Chief Technology Officer |
| Data Pipeline | Avg residual score ≤ target | 7 |  |  | Monthly | Head of Data Governance |

## Business Outcome

| All sections | Open FINOS gaps not yet reviewed = target |  |  |  | Continuous | Head of AI Governance |

## STAGE BENCHMARKS  (per lifecycle stage)

| Lifecycle Stage | Benchmark Metric | Target | Status | Reassess Cadence | Owner |
| --- | --- | --- | --- | --- | --- |
| Onboarding / Intake | % new use cases with completed intake assessment | 100% | Pending | Per intake | AI Governance |
| Design / Build | % designs with controls mapped to identified risks | 100% | Pending | Per build | ML Platform Lead |
| Pre-Deployment Gate | Gate pass-rate at first submission | 90% | Pending | Per release | Governance forum |
| Pre-Deployment Gate | % connected-agent chains with rollback + kill-switch tested | 100% | Pending | Per release | Head of AI Governance |
| Production / Operate | % systems within drift threshold | 95% | Pending | Monthly | ML Platform Lead |
| Production / Operate | Mean time to detect outcome deviation (hrs) | 24 | Pending | Monthly | ML Platform Lead |
| Incident-Triggered Review | % incidents with register re-scored within SLA | 100% | Pending | Per incident | AI Governance |

Current

## Periodic Review

Decommission  % retirements with data deletion + access revocation verified  100%  Pending  Per retirement  CISO

Target and Current cells contents are inputs (targets and current measured values). 'Current' for section benchmarks is pulled live from the register; for stage benchmarks, enter the measured value from process metrics.