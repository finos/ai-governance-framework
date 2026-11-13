---
sequence: 33
title: Adversarial Adaptation and Control-Evasion Drift
layout: risk
doc-status: Draft
type: SEC
domain: accuracy
owasp-ml_references:
  - ml01-2023  # ML01:2023 Input Manipulation Attack
  - ml08-2023  # ML08:2023 Model Skewing
eu-ai-act_references:
  - c3-s2-a9   # III.S2.A9: Risk Management System
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
related_risks:
  - ri-9   # Data Poisoning
  - ri-16  # Bias and Discrimination
  - ri-19  # Data Quality and Drift
---

## Summary

Models and rules that decide who gets blocked, reviewed or paid (fraud scoring, transaction monitoring, onboarding
checks, scam warnings) face an opponent who watches the outcome and changes behaviour to get past them. The model
does not just go stale. It is actively worked around, and the loss can grow while the usual quality measures still
look healthy.

## Description

Ordinary drift (see RI-19) happens because the world changes on its own. Adversarial adaptation happens because
people who gain from a control failing learn how it behaves and respond. In fraud and financial crime this is the
normal operating condition, not an edge case.

How the adaptation happens:

- **Probing.** Attackers send small or cheap test actions to learn what is allowed: low-value payments, repeated
  login attempts, throwaway accounts, slightly altered documents. Each test teaches them where the line is.
- **Learning from the response.** Block messages, step-up prompts, delays and approvals all leak information about
  the control. Even a plain "approved" or "declined" is a label the attacker can collect.
- **Moving to the gap.** Once one route is closed, activity shifts to the route that is not watched: another
  payment rail, another channel, another account type, another time of day, another stage of the customer journey.
- **Sharing and scaling.** Working methods are traded and copied, so a weakness found by one person is used by many
  within days. Generative AI tools lower the cost of making new variations (new text, images, voices and documents)
  faster than a review team can write new rules.
- **Mimicking good behaviour.** Attackers copy the features that the model treats as safe, such as account age,
  normal-looking transaction sizes and device history, so the legitimate-looking population and the attacking
  population move closer together.

Why standard monitoring can miss it:

- **Late labels.** Confirmed fraud often arrives weeks or months after the event (chargebacks, returns, customer
  reports, investigations). Recent performance looks better than it is, because the bad outcomes have not been
  labelled yet.
- **Selection effects.** What the control blocks is never confirmed as fraud or not, so the training data reflects
  only what the old control let through. Retraining on that data can lock in the old blind spots.
- **Averages hide the targeted slice.** Overall accuracy or alert volume can stay flat while one product, rail or
  customer segment is being exploited.
- **Fixes teach the attacker.** A visible change to a rule or model is itself a signal that tells the attacker what
  was detected, and the next variation arrives shortly after.
- **Feedback loops.** If model decisions shape the data used to retrain it, an attacker (or a gap in coverage) can
  steer the next version. This is related to model skewing and, in some cases, to data poisoning.

### Financial Services Impact Scenarios

- A card or payments fraud model keeps its overall catch rate while losses concentrate in a new payment method that
  the model has little history on.
- Small test transfers to a new recipient become routine for attackers because the model scores them as harmless.
  The first large transfer then arrives from an account with a clean-looking history.
- A scam-warning or customer-friction control works for a few weeks, then attackers coach victims to answer the
  warning prompts the way a genuine customer would.
- Synthetic or AI-assisted identity documents pass an onboarding model that was validated on last year's fakes.
- An AI system that proposes new detection rules is trained on the cases analysts already confirmed, so it learns
  yesterday's pattern and misses the variation that has already moved on.

### Consequences

- Fraud and financial-crime losses rise while headline model metrics appear stable.
- Late discovery, because the labels that would reveal the problem arrive after the damage.
- Customer harm from over-correction: after a loss event, a rushed tightening raises false declines and friction
  for legitimate customers.
- Regulatory and supervisory exposure where an institution must show that its models are monitored and still
  effective against current threats.
- Wasted analyst time as teams chase each new variation one rule at a time.

### Key Risk Factors

- **Single control, single point of failure.** One model or rule set does all the detecting, so one successful
  evasion method works everywhere.
- **Slow or unmeasured label delay.** The institution does not track how long confirmed outcomes take to arrive,
  so recent performance is read as final.
- **No tracking of attacker behaviour.** Metrics describe the model (accuracy, alert rate) but not the opponent
  (new test patterns, shifts between channels, repeat probing).
- **Predictable responses.** Block and challenge outcomes are consistent and observable, and customer-facing
  messages explain exactly why an action was stopped.
- **Retraining only on confirmed outcomes.** Blocked cases are excluded or mislabelled, so the next model inherits
  the previous model's blind spots.
- **Infrequent adversarial testing.** Controls are validated on historical data but not tested against deliberate
  attempts to get around them.

## Links

- [OWASP ML01:2023 Input Manipulation Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML01_2023-Input_Manipulation_Attack.html)
- [OWASP ML08:2023 Model Skewing](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML08_2023-Model_Skewing.html)
- [NIST AI 100-2 E2025, Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://doi.org/10.6028/NIST.AI.100-2e2025)
- [MITRE Fight Fraud Framework (F3)](https://ctid.mitre.org/fightfraud/): a catalogue of the behaviours fraud actors use,
  useful for listing the evasion behaviours a control should be tested against
