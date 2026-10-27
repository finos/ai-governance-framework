# Addressing the Risk & Acceptance Criteria

How each register risk is treated, and the explicit criteria for mitigating, removing, or accepting it.

## Options to Address

| Option | What it Means | When to Choose It |
|---|---|---|
| Mitigate / Reduce | Apply or strengthen controls to lower likelihood and/or impact until residual risk is within tolerance. | Default for most High/Critical risks where the use case has clear business value and controls can close the gap. |
| Transfer | Shift exposure to a third party — contractual indemnity, insurance, or vendor-assumed liability. | Where another party is better positioned to bear or control the risk (e.g. model provider indemnity for IP). |
| Avoid / Remove | Eliminate the exposure by removing the capability, decommissioning the model/agent, or not deploying. | Where residual risk stays Critical after mitigation, or cost/effort outweighs value. Triggers removal criteria below. |
| Accept | Formally accept the residual risk with documented sign-off and ongoing monitoring. | Where residual risk is within tolerance and meets the acceptance criteria below. |

## Acceptance Criteria (all must hold to accept)

- Residual rating is within the organization's stated tolerance for the use-case tier (typically Low or Moderate).
- All credible mitigations have been applied or consciously deferred with rationale, no quick win is left undone.
- An accountable owner is named, and the required sign-off level (per the deployment gate) has been obtained.
- Monitoring and trigger conditions are defined so the acceptance is revisited if exposure changes.
- A review/expiry date is set — acceptance is time-bound, not permanent.
- Acceptance is documented in the register (Address Risk = Accept, Status = Accepted) with date and approver.

## Risk Removal / Avoidance Criteria (any one may trigger removal)

- Residual rating remains Critical after all reasonable mitigation, and human-in-the-loop cannot reduce it.
- The risk cannot be detected or rolled back reliably (e.g. cascading multi-agent deviation with no recovery path).
- Mitigation cost or operational drag outweighs the use case's business value.
- A legal, regulatory, or ethical constraint prohibits the capability as designed.
- Acceptance criteria cannot be met and no owner will accept the residual risk.

## Kill-Switch / Complete Termination (control of last resort)

A kill-switch is a pre-defined, tested mechanism to immediately halt an AI system or agent — pausing a single agent, breaking a connected-agent chain, or fully terminating the deployment — and fail to a safe, known state. It is a required control for any system rated High or Critical residual, for all autonomous-action agents, and for all connected-agent chains. It must be tested before release and exercised periodically.

### Possible Approach

| Invocation Trigger | Scope of Action | Owner / Authority |
|---|---|---|
| Out-of-mandate autonomous action detected | Pause the offending agent, revoke action privileges | On-call governance / SecOps |
| Outcome deviation breaches threshold | Auto-pause agent, route to human, freeze outputs | Automated + ML Platform Lead |
| Repeated low-confidence or fabricated outputs | Halt agent, force fail-safe/abstain, alert | Automated + AI Governance |
| Cascading deviation across connected agents | Break the chain at circuit-breaker, isolate state, roll back to checkpoint | Automated + Governance forum |
| Corrupt input crossing agent trust boundary | Quarantine payload, suspend dependent agents | SecOps |
| Security incident (injection, poisoning, credential) | Terminate affected agents, revoke credentials | CISO / SecOps |
| Regulatory or legal direction to stop | Complete termination of the deployment | Accountable executive |
