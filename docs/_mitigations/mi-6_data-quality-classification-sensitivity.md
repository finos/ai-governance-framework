---
sequence: 6
title: Data Quality & Classification/Sensitivity
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-7-4  # ISO 42001: Quality of data for AI systems
  - A-7-2  # ISO 42001: Data for development and enhancement of AI system
  - A-4-3  # ISO 42001: Data resources
nist-sp-800-53r5_references:
  - ac-1  # AC-1 Policy And Procedures
  - ac-4  # AC-4 Information Flow Enforcement
  - ac-16  # AC-16 Security And Privacy Attributes
  - at-2  # AT-2 Literacy Training And Awareness
  - at-3  # AT-3 Role-based Training
  - ca-7  # CA-7 Authorization
  - cm-13  # CM-13 Data Action Mapping
  - pm-11  # PM-11 Mission And Business Process Definition
  - pm-22  # PM-22 Personally Identifiable Information Quality Management
  - pm-23  # PM-23 Data Governance Body
  - ra-2  # RA-2 Security Categorization
  - si-7  # SI-7 Software, Firmware, And Information Integrity
  - si-10  # SI-10 Information Input Validation
  - si-12  # SI-12 Information Management And Retention
  - si-18  # SI-18 Personally Identifiable Information Quality Operations
mitigates:
  - ri-1   # Information Leaked To Hosted Model
  - ri-2   # Information Leaked to Vector Store
  - ri-4   # Hallucination and Inaccurate Outputs
  - ri-16  # Bias and Discrimination
  - ri-22  # Regulatory Compliance and Oversight
  - ri-23  # Intellectual Property (IP) and Copyright
related_mitigations:
  - mi-2   # Data Filtering From External Knowledge Bases
  - mi-12  # Role Based Access Control for AI Data
  - mi-14  # Encryption of AI Data at Rest
---

## Purpose

The integrity, security, and effectiveness of any AI system deployed within a financial institution are fundamentally dependent on the quality and appropriate handling of the data it uses. This control establishes the necessity for robust processes to:

1.  **Ensure Data Quality:** Verify that data used for training, testing, and operating AI systems is accurate, complete, relevant, timely, and fit for its intended purpose.
2.  **Implement Data Classification:** Systematically categorize data based on its sensitivity (e.g., public, internal, confidential, restricted) to dictate appropriate security measures, access controls, and handling procedures throughout the AI lifecycle.

Adherence to these practices is critical for building trustworthy AI, minimizing risks, and meeting regulatory obligations.

---

## Key Principles

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
    * Provide regular training to all personnel involved in data management, AI development, and AI operations on the institution's data classification policies, data quality standards, ethical data use, and secure data handling procedures.

---

## Importance and Benefits

Implementing robust data quality assurance and sensitivity classification for AI systems yields significant benefits:

* **Data Protection:** Accurate classification protects sensitive information and mitigates unauthorized access risks
* **Model Performance:** High-quality data ensures accurate, robust, and dependable AI model outputs
* **Bias Mitigation:** Rigorous data quality practices support ethical, fair, and unbiased AI outcomes
* **Regulatory Compliance:** Provides framework for meeting data protection regulations and audit requirements
* **Stakeholder Trust:** Demonstrates strong governance practices that build confidence in AI systems
* **Operational Efficiency:** Prevents wasted resources from data-related issues and rework
