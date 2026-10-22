---
sequence: 4
title: "Anti-Financial Crime Investigation"
layout: usecase
doc-status: Draft
category: Risk_Management_and_Compliance

description: "A GenAI assistant that supports L2 anti-financial-crime investigators across the AML investigation workflow, from alert triage and case enrichment through disposition to drafting the STR/SAR for MLRO/BSA officer review and filing."
end_user: "L2 AML investigator, financial crime analyst, MLRO/BSA officer"
business_value: "Reduces investigation handling time and alert backlog while improving narrative consistency, evidence traceability, and the defensibility of dispositions and STR/SAR filings."

related_risks:
  - ri-1
  - ri-2
  - ri-4
  - ri-10
  - ri-17
  - ri-18
  - ri-19
  - ri-22

related_mitigations:
  - mi-1
  - mi-4
  - mi-5
  - mi-11
  - mi-13
  - mi-14
  - mi-16
  - mi-17
  - mi-21

data_classifications:
  - name: Customer_PII_Data
    data_types:
      - KYC/CDD identity records and beneficial ownership information
      - Politically exposed person (PEP) status and sanctions/name-screening match details
      - Customer risk ratings and relationship history
  - name: Sensitive_Financial_Data
    data_types:
      - Individual transaction records and payment history for subjects and counterparties
      - Account balances and cross-border funds-flow data
      - AI-generated risk indicators and disposition recommendations
  - name: Confidential_Financial_Data
    data_types:
      - Draft and filed STR/SAR narratives and supporting case files
      - Internal watchlists and prior investigation outcomes
      - Law enforcement requests and regulator correspondence
  - name: Internal_Proprietary_Data
    data_types:
      - Transaction monitoring scenarios, thresholds, and alert logic
      - Money laundering typology libraries and red-flag indicators
      - Investigation procedures and disposition criteria

data_handling_aspects:
  - Centralized
  - Privacy_Preserving

eu-ai-act_references:
  - c3-s2-a10
  - c3-s2-a12
  - c3-s2-a13
  - c3-s2-a14

sr11-7_references:
  - overview
  - s2-use
  - s3
  - s3-monitoring
  - s4-inventory

regulatory_concerns:
  - name: "BSA / FinCEN Suspicious Activity Reporting (31 CFR § 1020.320)"
    url: "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320"
    jurisdiction: "US"
  - name: "EU Anti-Money Laundering Regulation (Regulation (EU) 2024/1624)"
    url: "https://eur-lex.europa.eu/eli/reg/2024/1624/oj"
    jurisdiction: "EU"
  - name: "Tipping-Off Prohibition (Directive (EU) 2015/849 Art. 39; Regulation (EU) 2024/1624 Art. 73)"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015L0849"
    jurisdiction: "EU"
  - name: "FATF Recommendations (R.20 Suspicious Transaction Reporting, R.21 Tipping-Off and Confidentiality)"
    url: "https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html"
    jurisdiction: "International"

further_reading:
  - name: "Opportunities and Challenges of New Technologies for AML/CFT"
    url: "https://www.fatf-gafi.org/en/publications/Digitaltransformation/Opportunities-challenges-new-technologies-for-aml-cft.html"
    source: "FATF"
  - name: "Principles for Using Artificial Intelligence and Machine Learning in Financial Crime Compliance"
    url: "https://www.wolfsberg-group.org/resources/innovation/93"
    source: "Wolfsberg Group"
  - name: "Project Aurora: The Power of Data, Technology and Collaboration to Combat Money Laundering Across Institutions and Borders"
    url: "https://www.bis.org/publ/othp66.htm"
    source: "BIS"
---

## Description

The Anti-Financial Crime Investigation use case applies GenAI as an assistant across the end-to-end AML investigation workflow, from alert triage through disposition to drafting the Suspicious Transaction Report (STR/SAR) for review and filing by the Money Laundering Reporting Officer (MLRO) or BSA officer (e.g. via goAML or FinCEN's BSA E-Filing). Enhanced (L2) investigators work alerts escalated from transaction monitoring, sanctions/name screening, or fraud detection; L2 denotes an alert-escalation tier, not a line of defense, and institutions house the workflow in the first or second line with the compliance function retaining second-line oversight.

GenAI drafts, summarizes, retrieves, and recommends; it never closes an alert, decides not to file, or submits a report autonomously. The investigator remains accountable for every disposition, the MLRO/BSA officer for every filing.

### Key Functions

- **Alert Triage**: Summarizes the alert, subject profile, and prior alerts, and recommends a priority.
- **Case Enrichment**: Consolidates Know Your Customer / Customer Due Diligence (KYC/CDD) records, beneficial ownership, transaction history, watchlists, and prior dispositions with source citations.
- **Adverse Media Screening**: Summarizes adverse media and external registries, linking each claim to its source.
- **Typology Matching**: Compares activity, funds flows, and counterparty patterns against the typology library and FATF-derived red-flag indicators.
- **Disposition Support**: Recommends close-as-false-positive or escalate, with an evidence-linked rationale.
- **Narrative Generation**: Drafts the investigation narrative grounded in the case file, with citations.
- **STR/SAR Drafting**: Pre-populates the filing narrative and structured fields in the format of the receiving Financial Intelligence Unit (FIU).
- **Audit Trail**: Records retrieved sources, model outputs, investigator edits, and approval steps.

## Business Value

AML investigation is labor-intensive: investigators spend most case-handling time gathering data and writing narratives rather than exercising judgment. GenAI automates the mechanical portions so investigator time concentrates on whether activity is genuinely suspicious.

**Key Benefits:**

- **Faster Case Handling**: Automates evidence gathering, summarization, and first-draft narratives, helping meet filing deadlines.
- **Consistent Narratives**: Standardized structure with citations improves filing quality and reduces FIU rejections.
- **Surge Resilience**: Absorbs alert spikes from new scenarios, sanctions events, or lookbacks.
- **Investigator Focus**: Shifts effort from data assembly to analysis and judgment.
- **Auditability**: Traceable records link alerts, evidence, AI drafts, decisions, and filings.

## End Users

- **Primary**: Enhanced (L2) AML investigators and financial crime analysts
- **Secondary**: MLRO/BSA officers, QA teams, and sanctions and fraud teams
- **Tertiary**: Model risk management, internal audit, FIUs, and supervisors

## Data Sensitivity

This use case concentrates **Customer PII Data**, **Sensitive Financial Data**, and **Confidential Financial Data**, including draft and filed STRs/SARs and the fact that a customer is under investigation. It also concentrates **Internal Proprietary Data** — transaction monitoring scenarios, thresholds, and typology libraries — whose leakage would enable launderers to evade detection, a harm distinct from any privacy breach.

Because STR/SAR confidentiality and tipping-off prohibitions apply, sending case content, draft narratives, or alert metadata to a third-party hosted model, or persisting it in shared vector stores or provider logs, must be treated as potential unlawful disclosure rather than a privacy incident. Controls should still allow the disclosures authorized under `31 CFR § 1020.320(e)`, such as sharing with FinCEN, law enforcement, examining authorities, and permitted intra-organizational recipients. Case data must remain in access-controlled, encrypted systems on a need-to-know basis, with retrieval preserving source-system access controls.

## Regulatory Concerns

- **BSA / FinCEN**: SAR filing obligation, 30-calendar-day timeframe from initial detection (60 where no suspect is identified), and SAR confidentiality (`31 CFR § 1020.320` for banks, with parallel sections for other institution types); FinCEN interprets initial detection as the point at which review determines the activity is suspicious, not the alert-generation date, a distinction that matters when AI compresses triage time
- **EU AML Package**: The AMLR (Regulation (EU) 2024/1624), applicable from 10 July 2027, harmonizes suspicious transaction reporting and carries the tipping-off prohibition forward from AMLD Article 39 (operative until then) as Article 73, per the correlation table in Annex VI AMLR; AMLA (Regulation (EU) 2024/1620) will select up to 40 high-risk cross-border institutions in 2027 and directly supervise them from 1 January 2028, including their governance of AI-assisted investigation and reporting
- **FATF Standards**: Recommendation 20 (prompt STR reporting) and Recommendation 21 (confidentiality and tipping-off)
- **EU AI Act**: Not a listed Annex III high-risk use; point 6 (law enforcement) covers systems used by or on behalf of law enforcement authorities as defined in Article 3(45), and an obliged entity meeting its own AML obligations acts on its own behalf; Articles 10, 12, 13, and 14 (data governance, record-keeping, transparency, human oversight) provide the internal benchmark
- **SR 11-7 / SR 26-2**: AML decision-support tools commonly meet the model definition and, where they do, require inventory, validation, and ongoing monitoring; the April 2021 interagency statement on model risk management for BSA/AML systems (SR 21-8) made the model-versus-tool determination bank-specific, and both SR 11-7 and SR 21-8 were superseded on 17 April 2026 by the revised interagency model risk management guidance (SR 26-2; OCC Bulletin 2026-13), which folds BSA/AML systems into the general framework

## AI Risks and Mitigations

**Information Leakage:** Sending case files, KYC records, or draft STR/SAR narratives to third-party models creates [Information Leaked To Hosted Model](/risks/ri-1_information-leaked-to-hosted-model/) risk; leakage revealing that a filing exists can itself breach SAR confidentiality and tipping-off prohibitions. Mitigations include self-hosted or contractually ring-fenced models, leakage prevention and detection, and strict data minimization.

**Vector Store Leakage:** Case enrichment retrieves KYC records, prior cases, watchlists, and historical narratives, creating [Information Leaked to Vector Store](/risks/ri-2_information-leaked-to-vector-store/) exposure; prior-case retrieval can reveal that a customer was previously the subject of an STR. Retrieval must enforce source-system access controls at query time, with encryption at rest and access logging.

**Hallucination and Inaccurate Outputs:** FIUs and law enforcement rely on STR/SAR narratives, so [Hallucination and Inaccurate Outputs](/risks/ri-4_hallucination-and-inaccurate-outputs/) such as a fabricated transaction or invented counterparty could corrupt a filing or wrongly implicate a customer. Generated statements should carry citations to source records, cross-checked against structured data and verified before filing.

**Prompt Injection:** Adverse media screening ingests untrusted web content, creating [Prompt Injection](/risks/ri-10_prompt-injection/) exposure such as planted content instructing the model to downplay findings or exfiltrate case details. External content should be treated as data, not instructions, filtered through an AI firewall, and segregated from internal evidence.

**Explainability:** Regulators and FIUs expect every closure and filing to rest on articulable, evidence-linked reasoning. [Lack of Explainability](/risks/ri-17_lack-of-explainability/) is mitigated by capturing the decision chain (alert, evidence, AI drafts, investigator edits, final human decision) as a reconstructable audit trail separating AI recommendation from human determination.

**Model Overreach:** Under volume pressure, investigators may accept [Model Overreach / Expanded Use](/risks/ri-18_model-overreach-expanded-use/) close recommendations without genuine review; systematically accepted false negatives are a failure-to-report pattern, while cheap drafting can drive defensive over-filing and boilerplate narratives that degrade intelligence value for FIUs. Mitigations include monitoring agreement rates, edit distance, escalation rates, and narrative similarity, with QA sampling weighted toward AI-recommended closures and QA outcomes fed back into the system through a structured human feedback loop.

**Data Quality and Drift:** Financial crime typologies evolve continuously as new laundering channels and evasion patterns emerge. [Data Quality and Drift](/risks/ri-19_data-quality-and-drift/) manifests as stale typology libraries, outdated KYC data, and degrading recommendations; mitigations include ongoing monitoring, typology refresh against FATF and FIU publications, and back-testing dispositions against QA outcomes.

**Regulatory Compliance and Oversight:** The workflow sits on statutory obligations with personal accountability for the MLRO/BSA officer, so [Regulatory Compliance and Oversight](/risks/ri-22_regulatory-compliance-and-oversight/) applies to the AI system itself, from missed filings to inability to evidence controls to examiners. Mitigations include advisory-only close recommendations, an MLRO/BSA approval gate outside the AI system's authority, and validation under model risk management.
