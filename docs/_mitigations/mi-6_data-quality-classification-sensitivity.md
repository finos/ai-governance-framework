---
sequence: 6
title: Data Quality & Classification/Sensitivity
layout: mitigation
doc-status: Draft
type: PREV
external_risks:
  - ISO-42001_2023_A-7-4 # Quality of data for AI systems
  - ISO-42001_2023_A-7-2 # Data for development and enhancement of AI system
  - ISO-42001_2023_A-4-3 # Data resources
mitigates:
  - ri-1  # Information Leaked To Hosted Model
  - ri-2  # Unauthorized Access & Data Leaks
  - ri-4  # Hallucination and Inaccurate Outputs
  - ri-16 # Bias and Discrimination
  - ri-22 # Intellectual Property (IP) and Copyright
  - ri-23 # Regulatory Compliance and Oversight
  
---

## Purpose

The integrity, security, and effectiveness of any AI system deployed within a financial institution are fundamentally dependent on the quality and appropriate handling of the data it uses. This control establishes the necessity for robust processes to:

1.  **Ensure Data Quality:** Verify that data used for training, testing, and operating AI systems is accurate, complete, relevant, timely, and fit for its intended purpose.
2.  **Implement Data Classification:** Systematically categorize data based on its sensitivity (e.g., public, internal, confidential, restricted) to dictate appropriate security measures, access controls, and handling procedures throughout the AI lifecycle.

Adherence to these practices is critical for building trustworthy AI, minimizing risks, and meeting regulatory obligations.

---
## Core Principles and Processes

A structured approach to data quality and classification for AI systems should be built upon the following principles:

### 1. Comprehensive Data Governance for AI
* **Framework:** Establish and maintain a clear data governance framework that specifically addresses the lifecycle of data used in AI systems. This includes defining roles and responsibilities for data stewardship, quality assurance, and classification.
* **Policies:** Develop and enforce policies for data handling, data quality standards, and data classification that are understood and actionable by relevant personnel.
* **Lineage and Metadata:** Maintain robust data lineage documentation (tracing data origins, transformations, and usage) and comprehensive metadata management to ensure transparency and understanding of data context.

### 2. Systematic Data Classification
* **Scheme:** Utilize the institution's established data classification scheme (e.g., Public, Internal Use Only, Confidential, Highly Restricted) and ensure it is consistently applied to all data sources intended for AI systems.
* **Application:** Classify data at its source or as early as possible in the data ingestion pipeline. For example, information within document repositories (like Confluence), databases, or other enterprise systems should have clear sensitivity labels.
* **Impact:** The classification level directly informs the security controls, access rights, encryption requirements, retention policies, and permissible uses of the data within AI development and operational environments.

### 3. Rigorous Data Quality Management
* **Defined Standards:** Define clear, measurable data quality dimensions and acceptable thresholds relevant to AI applications. Key dimensions include:
    * **Accuracy:** Freedom from error.
    * **Completeness:** Absence of missing data.
    * **Consistency:** Uniformity of data across systems and time.
    * **Timeliness:** Data being up-to-date for its intended use.
    * **Relevance:** Appropriateness of the data for the specific AI task.
    * **Representativeness:** Ensuring data accurately reflects the target population or phenomenon to avoid bias.
* **Assessment & Validation:** Implement processes to assess and validate data quality at various stages: during data acquisition, pre-processing, before model training, and through ongoing monitoring of data feeds.
* **Remediation:** Establish procedures for identifying, reporting, and remediating data quality issues, including data cleansing and transformation.

### 4. Understanding Data Scope and Context
* **Documentation:** For every data source feeding into an AI system, thoroughly document its scope (what it covers), intended use in the AI context, known limitations, and relevant business or operational context.
* **Fitness for Purpose:** Ensure that data selected for AI model training and operation is appropriate for the specific AI task. Critically evaluate whether its scope and context could introduce unintended biases, fairness issues, or operational risks.

---
## Implementation Guidance

To effectively manage data quality and classification for AI systems:

* **Data Source Vetting:** Before incorporating any new data source, conduct a thorough assessment of its origin, reliability, existing quality controls, and the accuracy of any pre-existing classifications. Prioritize the use of well-governed, trusted internal data sources.
* **Automated Tools (Where Feasible):**
    * Leverage automated tools for data discovery, profiling (to understand quality characteristics), and classification (e.g., using pattern matching, metadata analysis, or ML-based classifiers). Automation is crucial for managing the volume and velocity of data ("at the necessary scale").
    * Implement automated data quality checks and validation rules within data pipelines to continuously monitor and flag issues.
* **Manual Oversight and QA:** Supplement automated processes with targeted manual reviews and quality assurance procedures, particularly for:
    * Highly sensitive data.
    * Data used in critical AI applications (e.g., those impacting financial decisions, regulatory reporting, or customer treatment).
    * Validation of automated classification and quality assessment results.
* **Filtering and Control Based on Classification/Quality:**
    * Implement technical controls to filter, segregate, or restrict data from AI ingestion pipelines based on its sensitivity classification and data quality metrics. For example, prevent highly confidential data from being used in a general-purpose AI development sandbox unless explicitly authorized and with appropriate safeguards.
    * Ensure that data quality issues below a certain threshold trigger alerts or prevent data from being used by the AI model until remediated.
* **Data Pre-processing for Quality Enhancement:**
    * Employ appropriate data pre-processing techniques to address identified quality issues. This may include handling missing values, correcting inaccuracies, standardizing formats, normalizing data, and removing duplicates. All such transformations should be documented to maintain lineage.
* **Regular Audits and Continuous Monitoring:**
    * Conduct periodic audits of data classification accuracy across key repositories and assess the effectiveness of data quality management processes for AI data sources.
    * Continuously monitor data pipelines for significant drifts in data distributions or degradation in quality, as these can adversely impact AI model performance, fairness, and reliability.
* **Training and Awareness Programs:**
    * Provide regular training to all personnel involved in data management, AI development, and AI operations on the institution’s data classification policies, data quality standards, ethical data use, and secure data handling procedures.

---
## Importance and Benefits

Implementing robust data quality assurance and sensitivity classification for AI systems yields significant benefits:

* **Minimizes Data Leakage and Misuse:** Accurate classification is the first line of defense in protecting sensitive information, directly mitigating risks of unauthorized access and data breaches (as per `ri-1`, `ri-2`).
* **Enhances AI Model Performance and Reliability:** High-quality, relevant data is essential for training accurate, robust, and dependable AI models. Conversely, poor data quality can lead to flawed model outputs, poor decision-making, and operational failures.
* **Supports Ethical, Fair, and Unbiased AI:** Rigorous attention to data quality, including the representativeness of datasets, is crucial for identifying and mitigating biases, leading to fairer and more ethical AI outcomes.
* **Ensures Regulatory Compliance and Auditability:** Financial institutions are subject to stringent regulations regarding data protection (e.g., GDPR, CCPA) and data accuracy. This control provides a framework for compliance and facilitates easier audits.
* **Builds Stakeholder Trust:** Demonstrating strong data governance, including meticulous data quality and classification practices, increases trust and confidence in AI systems among customers, employees, regulators, and the public.
* **Improves Operational Efficiency:** Using high-quality data from the outset prevents wasted resources on developing and retraining AI models due to data-related issues, leading to more efficient AI development and deployment cycles.
