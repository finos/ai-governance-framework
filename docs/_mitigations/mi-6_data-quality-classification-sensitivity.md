---
sequence: 6
title: Data Quality & Classification/Sensitivity
layout: mitigation
doc-status: Pre-Draft
type: PREV
mitigates:
  - ri-1  # Information Leaked To Hosted Model
  - ri-2  # Information Leaked to Vector Store
---

Mitigating data sensitivity risks when using AI/ML and GenAI in the financial sector, especially under regulations such as the GDPR, EU AI Act, and similar global frameworks (e.g., UK Data Protection Act, CCPA, FRTB, Basel III, etc.), requires a multi-layered approach.

- Data is classified within the Confluence data store, and filtered prior to ingestion
- Manual quality assurance on the data at the necessary scale? Can this be automated?
- Data governance for source data? Scope and context for input data?



