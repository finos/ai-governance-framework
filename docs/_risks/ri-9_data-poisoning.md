---
sequence: 9
title: Data Poisoning
layout: risk
doc-status: Pre-Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM03
  - OWASP-LLM_2025_LLM05
  - OWASP-LLM_2025_LLM06
---

- Adversaries can tamper with AI training or fine-tuning data to introduce hidden patterns.  
- Fraudsters could inject fake data to manipulate AI decision-making (e.g., labeling fraudulent transactions as legitimate).  
- Data poisoning can bias models, such as skewing AI credit scoring to favor fraudulent profiles.  
- Risk is higher when AI models continuously learn from new data without strict validation.  
- Third-party data sources may be compromised, introducing hidden biases or vulnerabilities.  
- The effects of data poisoning may go unnoticed until a major failure occurs.