---
sequence: 11
title: Lack of Foundation Model Versioning
layout: risk
doc-status: Draft
type: OP
external_risks:
ffiec_references:
  - ffiec_dam_vii-maintenance
  - ffiec_ots_risk-management
  - ffiec_dam_ii-governance-of-development-acquisition-and-maintenance
eu-ai_references:
  - eu-ai_c3-s2-a11  # III.S2.A11 Technical Documentation
  - eu-ai_c3-s2-a12  # III.S2.A12 Record-Keeping
  - eu-ai_c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

Inadequate or unpublished API versioning and/or model version control may result in response instability, due to changes in the foundation model and the client's absence of opportunity to benchmark and test the new model.

This can lead to instability in the model's behaviour, which may impact on the client's business operations.

#### Challenges with versioning

There are unique challenges to versioning large language models (LLMs) and consequently, the APIs that provide LLM capabilities. Unlike traditional software, where versioning is tracking changes in source code, version LLMs must account for a range of factors such as model behavior, training data, architecture, and computational requirements. Some key challenges include:
1. Model size and complexity: 
   - Models are incredibly large, comprising of a large number of parameters. Managing and tracking changes and their impacts across such massive models can be very complex. It is also challenging to quantify or summarize changes in a meaningful way.
2. Dynamic nature of LLMs
   - Some LLMs are designed to learn and adapt over time, while others are updated through fine-tuning and customizations. This makes it difficult to keep track of changes or define discrete versions, as the model is constantly being updated.
3. Non-deterministic behavior:
   - LLMs can produce different outputs for the same input due to factors like temperature settings, making it difficult to define a "new version". 
4. Multidimensional changes:
   - Updates to LLMs might involve changes to the model architecture, training data, fine-tuning process, and inference parameters. Capturing all these dimensions in a version number or identifier is challenging.
   - Changes to LLMs can range from minor tweaks (e.g., adjusting hyperparaemters) to significant changes (e.g., retraining with new data), making it challenging to define the proper granularity of versioning.
5. Training data versioning:
   - LLMs are trained on massive amounts of data, making it difficult to track and manage changes in the training corpus.
6. Resource management: 
   - Running multiple versions of LLMs simultaneously can strain computational resources and challenge infrastructure.
7. Lack of standardization: 
   - There are no widely accepted standard for versioning LLMs, leading to inconsistent practices across different organizations.

#### Problems caused by inadequate versioning:

1. Inconsistent output
   - LLM may product different responses to the same prompt, leading to inconsistent user experiences or decision-making
2. Reproducibility/Traceability
   - Inability to replicate or trace past outputs, which may be required in some business context or during testing and debugging
3. Performance variability: 
   - Unexpected changes in model performance, even introducing regression in some areas (e.g., more bias)
   - Assessing improvements or regression becomes challenging
4. Compliance and auditing:
   - Inability to track and explain model changes can lead to compliance problems and difficulty in auditing decisions
5. Integration and compatibility/backward compatibility:
   - Other systems or APIs may depend on specific behaviors of an LLM
6. Testing and quality assurance:
   - Difficulty in identifying root cause of errors or bugs
   - Inability to replicate issues or isolate model changes that are causing issues
7. Security and privacy:
   - Difficult to track security vulnerabilities or privacy issues
   - New security or privacy issues may be introduced
