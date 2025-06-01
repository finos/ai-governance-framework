---
sequence: 16
title: Bias and Discrimination
layout: risk
doc-status: Pre-Draft
type: OP
nist-ai-600-1_references:
  - 2-6    # NIST AI 600.1: Harmful Bias and Homogenization
ffiec_references:
  - mgt-2
  - dam-3
  - aud-4
eu-ai-act_references:
  - c2-a5  # II.A5 Prohibited AI Practices
  - c3-s2-a9  # III.S2.A9 Risk Management System
  - c3-s2-a14  # III.S2.A14 Human Oversight
---

## Summary

AI systems risk perpetuating bias and discrimination when trained on historical or internet-based data that reflect societal inequalities. This can lead to unfair outcomes such as biased credit scoring, discriminatory loan approvals, or unequal access to financial products. These effects may be subtle and difficult to detect, but can result in regulatory, ethical, and reputational consequences if left unaddressed.

## Description

Foundational models are typically trained on large-scale datasets collected from the internet, historical records, or other broad text corpora. These data sources often reflect the biases, stereotypes, and inequalities present in the societies from which they were drawn. As a result, the models may internalize and reproduce these patterns in their outputs, even when those outcomes are unintentional or socially harmful.

When used in decision-making systems, these biases can translate into discriminatory outcomes. For example, AI models used in credit scoring might assign lower creditworthiness to certain demographic groups based on historical lending patterns. In pricing algorithms, the model might recommend higher prices to individuals from specific geographic or socioeconomic backgrounds. In recruitment or admissions systems, underrepresented groups may be ranked lower due to skewed training data or biased evaluation criteria.

These issues are often invisible or hard to detect, particularly when models operate as part of complex or opaque workflows. Even when explicit demographic data is excluded from training, proxy variables—such as postal codes, language style, or purchase history—can reintroduce discriminatory patterns.

Bias and discrimination risks are compounded when models are retrained on real-world feedback, potentially reinforcing unjust patterns over time. Without regular auditing, fairness assessments, and transparent governance, these systems may systematically disadvantage certain individuals or groups, resulting in reputational damage, regulatory violations, or ethical harm.

## Examples

* **Biased Credit Scoring**:
  An AI model trained on historical lending data may learn patterns that reflect past discriminatory practices—such as granting loans disproportionately to individuals from certain zip codes, employment types, or educational backgrounds. This can result in lower credit scores for minority applicants or applicants from underserved communities, even if their actual financial behaviour is comparable to others.

* **Unfair Loan Approval Recommendations**:
  An LLM-powered decision support tool might assist underwriters by summarizing borrower applications. If trained on biased documentation or internal guidance, the system might consistently recommend rejection for certain profiles (e.g., single parents, freelancers), reinforcing systemic exclusion and contributing to disparate impact under fair lending laws.

* **Discriminatory Insurance Premium Calculations**:
  Insurance pricing algorithms that use AI may rely on features like occupation, home location, or education level—attributes that correlate with socioeconomic status or race. This can lead to higher premiums for certain demographic groups without a justifiable basis in actual risk, potentially violating fairness or equal treatment regulations.

* **Disparate Marketing Practices**:
  AI systems used for personalized financial product recommendations or targeted advertising might exclude certain users from seeing offers—such as mortgage refinancing or investment services—based on income, browsing behaviour, or inferred demographics. This results in unequal access to financial opportunities and can perpetuate wealth gaps.

* **Customer Service Disparities**:
  Foundational models used in customer support chatbots may respond differently based on linguistic patterns or perceived socioeconomic cues. For example, customers writing in non-standard English or with certain accents (in voice-based systems) might receive lower-quality or less helpful responses, affecting service equity.


