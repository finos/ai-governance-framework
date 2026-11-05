export type AigfItemItemId = string;
export type AigfRiskItemId = string;
export type AigfMitigationItemId = string;
export type AigfUseCaseItemId = string;
export type AigfReferenceEntryReferenceKey = string;
/**
* How far a page has been approved, from document_status in docs/_config.yml.
*/
export enum AigfDocumentStatus {
    
    /** Initial brainstorming or collection of ideas, notes, and outlines. The document is not yet formally written. */
    Pre_Draft = "Pre-Draft",
    /** The document is in the early stages of development, with content being written and structured but not yet polished. */
    Draft = "Draft",
    /** The document is in its final form and has been approved by the AIGF team. */
    Working_Group_Approved = "Working-Group-Approved",
    /** The publication of an Approved Specification in a publicly accessible manner. */
    Approved_Specification = "Approved-Specification",
};
/**
* A risk's group, from risk_type_labels in docs/_config.yml.
*/
export enum AigfRiskType {
    
    Regulatory_and_Compliance = "RC",
    Operational = "OP",
    Security = "SEC",
};
/**
* A mitigation's group, from mitigation_type_labels in docs/_config.yml.
*/
export enum AigfMitigationType {
    
    Preventative = "PREV",
    Detective = "DET",
};
/**
* A risk's domain, from risk_domain_labels in docs/_config.yml.
*/
export enum AigfRiskDomain {
    
    Components = "components",
    Inputs = "inputs",
    Leakage = "leakage",
    Accuracy = "accuracy",
    Alignment = "alignment",
    Agency = "agency",
    Vendor = "vendor",
    Liability = "liability",
};
/**
* A mitigation's domain, from mitigation_domain_labels in docs/_config.yml.
*/
export enum AigfMitigationDomain {
    
    Sourcing = "sourcing",
    Filtering = "filtering",
    Data = "data",
    Access = "access",
    Evaluation = "evaluation",
    Oversight = "oversight",
    Monitoring = "monitoring",
};
/**
* A use case's category, from usecase_categories in docs/_config.yml.
*/
export enum AigfUseCaseCategory {
    
    Customer_Experience_and_Engagement = "Customer_Experience_and_Engagement",
    Risk_Management_and_Compliance = "Risk_Management_and_Compliance",
    Operations_and_Process_Optimization = "Operations_and_Process_Optimization",
    Trading_and_Investment = "Trading_and_Investment",
    Data_Intelligence_and_Analytics = "Data_Intelligence_and_Analytics",
    Fraud_Detection_and_Security = "Fraud_Detection_and_Security",
    /** A category uc-3 and uc-4 use. docs/_config.yml does not list it, though docs/_data/ai_use_cases.yml has a domain of this name. */
    Risk_and_Compliance = "Risk_and_Compliance",
};
/**
* How sensitive a class of data is, as docs/_data/data_classification.yml grades it.
*/
export enum AigfSensitivity {
    
    Low = "Low",
    Medium = "Medium",
    High = "High",
    Critical = "Critical",
};
/**
* The question a reference file answers, from docs/_data/references/README.md.
*/
export enum AigfLens {
    
    /** What is this called elsewhere? */
    threat = "threat",
    /** Which rule requires me to address it? */
    obligation = "obligation",
    /** How do I implement and evidence it? */
    control = "control",
};
/**
* The options of the deployment model's data_handling axis.
*/
export enum AigfDataHandling {
    
    Centralized = "Centralized",
    Federated = "Federated",
    Synthetic_Data = "Synthetic_Data",
    Privacy_Preserving = "Privacy_Preserving",
};


/**
 * One edition of the framework, as the facts FINOS's front matter and data files state.
 */
export interface AigfCatalogue {
    /** The name FINOS gives the page, file or framework. */
    title: string,
    /** The edition, as docs/_config.yml writes it. */
    version: string,
    /** The edition's date, as docs/_config.yml writes it. */
    release_date: date,
    /** The commit of FINOS's repository the catalogue was read from. */
    source_commit: string,
    /** The lenses docs/_config.yml configures. */
    reference_lenses?: AigfReferenceLens[],
    /** The keys of each reference file. */
    reference_indexes?: AigfReferenceIndex[],
    /** The risks of the edition. */
    risks: AigfRisk[],
    /** The mitigations of the edition. */
    mitigations: AigfMitigation[],
    /** The worked use cases of the edition. */
    use_cases?: AigfUseCase[],
    /** The classes of financial data docs/_data/data_classification.yml lists. */
    financial_data_classification?: AigfDataClassification[],
    /** The use case taxonomy docs/_data/ai_use_cases.yml lists. */
    ai_use_cases?: AigfUseCaseDomain[],
    /** The capabilities docs/_data/ai_use_cases.yml lists apart from the taxonomy. */
    cross_cutting_capabilities?: string[],
    /** The axes docs/_data/ai_deployment_model.yml lists. */
    ai_deployment_model_taxonomy?: AigfDeploymentAxis[],
}


/**
 * A page of the framework that its front matter describes and that others cite by identifier.
 */
export interface AigfItem {
    /** The page's identifier, which FINOS's file name starts with and other pages cite. */
    item_id: string,
    /** The number in the page's identifier, which orders the pages. */
    sequence: number,
    /** The name FINOS gives the page, file or framework. */
    title: string,
    /** The Jekyll layout that renders the page. */
    layout: string,
    /** How far the page has been approved. */
    doc_status: string,
    /** The path of the page in FINOS's repository. */
    source_file: string,
}


/**
 * The entries of FINOS's reference files that a page cites, one list for each file.
 */
export interface AigfReferenceCitations {
    /** Keys of docs/_data/references/atr.yml. */
    atr_references?: string[],
    /** Keys of docs/_data/references/canada-regulations.yml. */
    canada_regulations_references?: string[],
    /** Keys of docs/_data/references/eu-ai-act.yml. */
    eu_ai_act_references?: string[],
    /** Keys of docs/_data/references/ffiec-itbooklets.yml. */
    ffiec_itbooklets_references?: string[],
    /** Keys of docs/_data/references/iosco-supervisory-toolkit.yml. */
    iosco_supervisory_toolkit_references?: string[],
    /** Keys of docs/_data/references/iso-42001.yml. */
    iso_42001_references?: string[],
    /** Keys of docs/_data/references/nist-ai-600-1.yml. */
    nist_ai_600_1_references?: string[],
    /** Keys of docs/_data/references/nist-sp-800-53r5.yml. */
    nist_sp_800_53r5_references?: string[],
    /** Keys of docs/_data/references/owasp-asi.yml. */
    owasp_asi_references?: string[],
    /** Keys of docs/_data/references/owasp-llm.yml. */
    owasp_llm_references?: string[],
    /** Keys of docs/_data/references/owasp-ml.yml. */
    owasp_ml_references?: string[],
    /** Keys of docs/_data/references/sr11-7.yml. */
    sr11_7_references?: string[],
    /** Keys of docs/_data/references/uk-regulations.yml. */
    uk_regulations_references?: string[],
}


/**
 * A risk the framework names, from a file under docs/_risks/.
 */
export interface AigfRisk extends AigfItem, AigfReferenceCitations {
    /** The group a risk appears in. */
    risk_type: string,
    /** The domain a risk belongs to. */
    risk_domain: string,
    /** The risks a page relates to. */
    related_risks?: AigfRiskItemId[],
}


/**
 * A mitigation the framework names, from a file under docs/_mitigations/.
 */
export interface AigfMitigation extends AigfItem, AigfReferenceCitations {
    /** The group a mitigation appears in. */
    mitigation_type: string,
    /** The domain a mitigation belongs to. */
    mitigation_domain: string,
    /** The risks a mitigation addresses. */
    mitigates: AigfRiskItemId[],
    /** The mitigations a page relates to. */
    related_mitigations?: AigfMitigationItemId[],
}


/**
 * A worked use case with its risks, mitigations and data, from a file under docs/_usecases/.
 */
export interface AigfUseCase extends AigfItem, AigfReferenceCitations {
    /** The category a use case is listed under. */
    category: string,
    /** FINOS's description of the element. */
    description: string,
    /** Who uses the system the use case describes. */
    end_user?: string,
    /** What the use case is worth to the business. */
    business_value?: string,
    /** The risks a page relates to. */
    related_risks?: AigfRiskItemId[],
    /** The mitigations a page relates to. */
    related_mitigations?: AigfMitigationItemId[],
    /** The data classifications a use case handles. */
    data_classifications?: AigfDataClassificationUse[],
    /** The options of the deployment model's data_handling axis a use case takes. */
    data_handling_aspects?: string,
    /** The regulations a use case raises. */
    regulatory_concerns?: AigfRegulatoryReference[],
    /** The papers and articles a use case points to. */
    further_reading?: AigfFurtherReading[],
}


/**
 * A data classification a use case handles, with the kinds of data it holds under it.
 */
export interface AigfDataClassificationUse {
    /** The name of a classification in docs/_data/data_classification.yml. */
    name: string,
    /** The kinds of data a use case holds under one classification. */
    data_types?: string[],
}


/**
 * A regulation or guideline named by its title and address, with where it applies.
 */
export interface AigfRegulatoryReference {
    /** The name FINOS gives the element. */
    name: string,
    /** The address of the element. */
    url?: string,
    /** Where a regulation applies. */
    jurisdiction?: string,
}


/**
 * A paper or article a use case points to.
 */
export interface AigfFurtherReading {
    /** The name FINOS gives the element. */
    name: string,
    /** The address of the element. */
    url?: string,
    /** Who published a paper or article. */
    source?: string,
}


/**
 * A class of financial data with its sensitivity and its handling, from docs/_data/data_classification.yml.
 */
export interface AigfDataClassification {
    /** The name FINOS gives the element. */
    name: string,
    /** How sensitive a class of data is. */
    sensitivity: string,
    /** FINOS's description of the element. */
    description: string,
    /** Kinds of data in a class. */
    examples?: string[],
    /** Where a class of data is held. */
    storage_location?: string,
    /** The regulations that apply to a class of data, written as FINOS writes them. */
    regulations?: string,
    /** The regulations and guidelines a class of data cites. */
    references?: AigfRegulatoryReference[],
}


/**
 * How the site presents the reference files of one lens, from reference_lenses in docs/_config.yml.
 */
export interface AigfReferenceLens {
    /** Which question a reference file answers for a page. */
    lens: string,
    /** The lens's display name. */
    label: string,
    /** The question the lens answers. */
    question: string,
    /** The Bootstrap Icons class the site shows beside the lens. */
    icon?: string,
    /** The Bootstrap theme colour the site gives the lens. */
    color?: string,
}


/**
 * One file under docs/_data/references/, which lists the citable entries of one regulation, framework or standard.
 */
export interface AigfReferenceFile {
    /** The name FINOS gives the page, file or framework. */
    title: string,
    /** FINOS's description of the element. */
    description: string,
    /** The address the file was generated from, or a canonical index page. */
    source_url?: string,
    /** Which question a reference file answers for a page. */
    lens: string,
    /** The file's citable items, keyed by the key a page cites them by. */
    entries: {[index: AigfReferenceEntryReferenceKey]: AigfReferenceEntry },
}


/**
 * One citable item of a reference file, under the key a page cites it by.
 */
export interface AigfReferenceEntry {
    /** The stable key a page cites the entry by. */
    reference_key: string,
    /** The name FINOS gives the page, file or framework. */
    title: string,
    /** The address of the element. */
    url: string,
    /** FINOS's description of the element. */
    description?: string,
    /** The body that issued the entry. */
    issuer?: string,
    /** The abbreviation of the FFIEC booklet the entry belongs to. */
    booklet_abbrev?: string,
    /** The key of the entry in the same file that replaces this one in a newer edition. */
    superseded_by?: string,
}


/**
 * The keys one reference file holds, so that a catalogue's citations resolve within it.
 */
export interface AigfReferenceIndex {
    /** The reference file's stem. */
    reference_file: string,
    /** Which question a reference file answers for a page. */
    lens: string,
    /** The keys the reference file holds. */
    entry_keys?: string[],
}


/**
 * A top level of the use case taxonomy in docs/_data/ai_use_cases.yml.
 */
export interface AigfUseCaseDomain {
    /** The name FINOS gives the element. */
    name: string,
    /** The areas under a domain. */
    use_case_areas?: AigfUseCaseArea[],
}


/**
 * A second level of the use case taxonomy, with the use cases under it.
 */
export interface AigfUseCaseArea {
    /** The name FINOS gives the element. */
    name: string,
    /** The use cases under an area, as the taxonomy names them. */
    use_case_names?: string[],
}


/**
 * One axis of the deployment model taxonomy in docs/_data/ai_deployment_model.yml.
 */
export interface AigfDeploymentAxis {
    /** The name FINOS gives the element. */
    name: string,
    /** The options on an axis. */
    options?: AigfDeploymentOption[],
}


/**
 * One option on an axis of the deployment model taxonomy.
 */
export interface AigfDeploymentOption {
    /** The name FINOS gives the element. */
    name: string,
    /** FINOS's description of the element. */
    description?: string,
}



