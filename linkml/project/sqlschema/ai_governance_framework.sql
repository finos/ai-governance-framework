-- # Class: AigfCatalogue Description: One edition of the framework, as the facts FINOS's front matter and data files state.
--     * Slot: id
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: version Description: The edition, as docs/_config.yml writes it.
--     * Slot: release_date Description: The edition's date, as docs/_config.yml writes it.
--     * Slot: source_commit Description: The commit of FINOS's repository the catalogue was read from.
-- # Abstract Class: AigfItem Description: A page of the framework that its front matter describes and that others cite by identifier.
--     * Slot: item_id Description: The page's identifier, which FINOS's file name starts with and other pages cite.
--     * Slot: sequence Description: The number in the page's identifier, which orders the pages.
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: layout Description: The Jekyll layout that renders the page.
--     * Slot: doc_status Description: How far the page has been approved.
--     * Slot: source_file Description: The path of the page in FINOS's repository.
-- # Class: AigfReferenceCitations Description: The entries of FINOS's reference files that a page cites, one list for each file.
--     * Slot: id
-- # Class: AigfRisk Description: A risk the framework names, from a file under docs/_risks/.
--     * Slot: risk_type Description: The group a risk appears in.
--     * Slot: risk_domain Description: The domain a risk belongs to.
--     * Slot: item_id Description: The page's identifier, which FINOS's file name starts with and other pages cite.
--     * Slot: sequence Description: The number in the page's identifier, which orders the pages.
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: layout Description: The Jekyll layout that renders the page.
--     * Slot: doc_status Description: How far the page has been approved.
--     * Slot: source_file Description: The path of the page in FINOS's repository.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfMitigation Description: A mitigation the framework names, from a file under docs/_mitigations/.
--     * Slot: mitigation_type Description: The group a mitigation appears in.
--     * Slot: mitigation_domain Description: The domain a mitigation belongs to.
--     * Slot: item_id Description: The page's identifier, which FINOS's file name starts with and other pages cite.
--     * Slot: sequence Description: The number in the page's identifier, which orders the pages.
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: layout Description: The Jekyll layout that renders the page.
--     * Slot: doc_status Description: How far the page has been approved.
--     * Slot: source_file Description: The path of the page in FINOS's repository.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfUseCase Description: A worked use case with its risks, mitigations and data, from a file under docs/_usecases/.
--     * Slot: category Description: The category a use case is listed under.
--     * Slot: description Description: FINOS's description of the element.
--     * Slot: end_user Description: Who uses the system the use case describes.
--     * Slot: business_value Description: What the use case is worth to the business.
--     * Slot: item_id Description: The page's identifier, which FINOS's file name starts with and other pages cite.
--     * Slot: sequence Description: The number in the page's identifier, which orders the pages.
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: layout Description: The Jekyll layout that renders the page.
--     * Slot: doc_status Description: How far the page has been approved.
--     * Slot: source_file Description: The path of the page in FINOS's repository.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfDataClassificationUse Description: A data classification a use case handles, with the kinds of data it holds under it.
--     * Slot: id
--     * Slot: name Description: The name of a classification in docs/_data/data_classification.yml.
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
-- # Class: AigfRegulatoryReference Description: A regulation or guideline named by its title and address, with where it applies.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: url Description: The address of the element.
--     * Slot: jurisdiction Description: Where a regulation applies.
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: AigfDataClassification_id Description: Autocreated FK slot
-- # Class: AigfFurtherReading Description: A paper or article a use case points to.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: url Description: The address of the element.
--     * Slot: source Description: Who published a paper or article.
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
-- # Class: AigfDataClassification Description: A class of financial data with its sensitivity and its handling, from docs/_data/data_classification.yml.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: sensitivity Description: How sensitive a class of data is.
--     * Slot: description Description: FINOS's description of the element.
--     * Slot: storage_location Description: Where a class of data is held.
--     * Slot: regulations Description: The regulations that apply to a class of data, written as FINOS writes them.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfReferenceLens Description: How the site presents the reference files of one lens, from reference_lenses in docs/_config.yml.
--     * Slot: id
--     * Slot: lens Description: Which question a reference file answers for a page.
--     * Slot: label Description: The lens's display name.
--     * Slot: question Description: The question the lens answers.
--     * Slot: icon Description: The Bootstrap Icons class the site shows beside the lens.
--     * Slot: color Description: The Bootstrap theme colour the site gives the lens.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfReferenceFile Description: One file under docs/_data/references/, which lists the citable entries of one regulation, framework or standard.
--     * Slot: id
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: description Description: FINOS's description of the element.
--     * Slot: source_url Description: The address the file was generated from, or a canonical index page.
--     * Slot: lens Description: Which question a reference file answers for a page.
-- # Class: AigfReferenceEntry Description: One citable item of a reference file, under the key a page cites it by.
--     * Slot: reference_key Description: The stable key a page cites the entry by.
--     * Slot: title Description: The name FINOS gives the page, file or framework.
--     * Slot: url Description: The address of the element.
--     * Slot: description Description: FINOS's description of the element.
--     * Slot: issuer Description: The body that issued the entry.
--     * Slot: booklet_abbrev Description: The abbreviation of the FFIEC booklet the entry belongs to.
--     * Slot: superseded_by Description: The key of the entry in the same file that replaces this one in a newer edition.
--     * Slot: AigfReferenceFile_id Description: Autocreated FK slot
-- # Class: AigfReferenceIndex Description: The keys one reference file holds, so that a catalogue's citations resolve within it.
--     * Slot: id
--     * Slot: reference_file Description: The reference file's stem.
--     * Slot: lens Description: Which question a reference file answers for a page.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfUseCaseDomain Description: A top level of the use case taxonomy in docs/_data/ai_use_cases.yml.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfUseCaseArea Description: A second level of the use case taxonomy, with the use cases under it.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: AigfUseCaseDomain_id Description: Autocreated FK slot
-- # Class: AigfDeploymentAxis Description: One axis of the deployment model taxonomy in docs/_data/ai_deployment_model.yml.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
-- # Class: AigfDeploymentOption Description: One option on an axis of the deployment model taxonomy.
--     * Slot: id
--     * Slot: name Description: The name FINOS gives the element.
--     * Slot: description Description: FINOS's description of the element.
--     * Slot: AigfDeploymentAxis_id Description: Autocreated FK slot
-- # Class: AigfCatalogue_cross_cutting_capabilities
--     * Slot: AigfCatalogue_id Description: Autocreated FK slot
--     * Slot: cross_cutting_capabilities Description: The capabilities docs/_data/ai_use_cases.yml lists apart from the taxonomy.
-- # Class: AigfReferenceCitations_atr_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: atr_references Description: Keys of docs/_data/references/atr.yml.
-- # Class: AigfReferenceCitations_canada_regulations_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: canada_regulations_references Description: Keys of docs/_data/references/canada-regulations.yml.
-- # Class: AigfReferenceCitations_eu_ai_act_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: eu_ai_act_references Description: Keys of docs/_data/references/eu-ai-act.yml.
-- # Class: AigfReferenceCitations_ffiec_itbooklets_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: ffiec_itbooklets_references Description: Keys of docs/_data/references/ffiec-itbooklets.yml.
-- # Class: AigfReferenceCitations_iosco_supervisory_toolkit_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: iosco_supervisory_toolkit_references Description: Keys of docs/_data/references/iosco-supervisory-toolkit.yml.
-- # Class: AigfReferenceCitations_iso_42001_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: iso_42001_references Description: Keys of docs/_data/references/iso-42001.yml.
-- # Class: AigfReferenceCitations_nist_ai_600_1_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: nist_ai_600_1_references Description: Keys of docs/_data/references/nist-ai-600-1.yml.
-- # Class: AigfReferenceCitations_nist_sp_800_53r5_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: nist_sp_800_53r5_references Description: Keys of docs/_data/references/nist-sp-800-53r5.yml.
-- # Class: AigfReferenceCitations_owasp_asi_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: owasp_asi_references Description: Keys of docs/_data/references/owasp-asi.yml.
-- # Class: AigfReferenceCitations_owasp_llm_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: owasp_llm_references Description: Keys of docs/_data/references/owasp-llm.yml.
-- # Class: AigfReferenceCitations_owasp_ml_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: owasp_ml_references Description: Keys of docs/_data/references/owasp-ml.yml.
-- # Class: AigfReferenceCitations_sr11_7_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: sr11_7_references Description: Keys of docs/_data/references/sr11-7.yml.
-- # Class: AigfReferenceCitations_uk_regulations_references
--     * Slot: AigfReferenceCitations_id Description: Autocreated FK slot
--     * Slot: uk_regulations_references Description: Keys of docs/_data/references/uk-regulations.yml.
-- # Class: AigfRisk_related_risks
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: related_risks_item_id Description: The risks a page relates to.
-- # Class: AigfRisk_atr_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: atr_references Description: Keys of docs/_data/references/atr.yml.
-- # Class: AigfRisk_canada_regulations_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: canada_regulations_references Description: Keys of docs/_data/references/canada-regulations.yml.
-- # Class: AigfRisk_eu_ai_act_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: eu_ai_act_references Description: Keys of docs/_data/references/eu-ai-act.yml.
-- # Class: AigfRisk_ffiec_itbooklets_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: ffiec_itbooklets_references Description: Keys of docs/_data/references/ffiec-itbooklets.yml.
-- # Class: AigfRisk_iosco_supervisory_toolkit_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: iosco_supervisory_toolkit_references Description: Keys of docs/_data/references/iosco-supervisory-toolkit.yml.
-- # Class: AigfRisk_iso_42001_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: iso_42001_references Description: Keys of docs/_data/references/iso-42001.yml.
-- # Class: AigfRisk_nist_ai_600_1_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: nist_ai_600_1_references Description: Keys of docs/_data/references/nist-ai-600-1.yml.
-- # Class: AigfRisk_nist_sp_800_53r5_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: nist_sp_800_53r5_references Description: Keys of docs/_data/references/nist-sp-800-53r5.yml.
-- # Class: AigfRisk_owasp_asi_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: owasp_asi_references Description: Keys of docs/_data/references/owasp-asi.yml.
-- # Class: AigfRisk_owasp_llm_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: owasp_llm_references Description: Keys of docs/_data/references/owasp-llm.yml.
-- # Class: AigfRisk_owasp_ml_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: owasp_ml_references Description: Keys of docs/_data/references/owasp-ml.yml.
-- # Class: AigfRisk_sr11_7_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: sr11_7_references Description: Keys of docs/_data/references/sr11-7.yml.
-- # Class: AigfRisk_uk_regulations_references
--     * Slot: AigfRisk_item_id Description: Autocreated FK slot
--     * Slot: uk_regulations_references Description: Keys of docs/_data/references/uk-regulations.yml.
-- # Class: AigfMitigation_mitigates
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: mitigates_item_id Description: The risks a mitigation addresses.
-- # Class: AigfMitigation_related_mitigations
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: related_mitigations_item_id Description: The mitigations a page relates to.
-- # Class: AigfMitigation_atr_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: atr_references Description: Keys of docs/_data/references/atr.yml.
-- # Class: AigfMitigation_canada_regulations_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: canada_regulations_references Description: Keys of docs/_data/references/canada-regulations.yml.
-- # Class: AigfMitigation_eu_ai_act_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: eu_ai_act_references Description: Keys of docs/_data/references/eu-ai-act.yml.
-- # Class: AigfMitigation_ffiec_itbooklets_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: ffiec_itbooklets_references Description: Keys of docs/_data/references/ffiec-itbooklets.yml.
-- # Class: AigfMitigation_iosco_supervisory_toolkit_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: iosco_supervisory_toolkit_references Description: Keys of docs/_data/references/iosco-supervisory-toolkit.yml.
-- # Class: AigfMitigation_iso_42001_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: iso_42001_references Description: Keys of docs/_data/references/iso-42001.yml.
-- # Class: AigfMitigation_nist_ai_600_1_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: nist_ai_600_1_references Description: Keys of docs/_data/references/nist-ai-600-1.yml.
-- # Class: AigfMitigation_nist_sp_800_53r5_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: nist_sp_800_53r5_references Description: Keys of docs/_data/references/nist-sp-800-53r5.yml.
-- # Class: AigfMitigation_owasp_asi_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: owasp_asi_references Description: Keys of docs/_data/references/owasp-asi.yml.
-- # Class: AigfMitigation_owasp_llm_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: owasp_llm_references Description: Keys of docs/_data/references/owasp-llm.yml.
-- # Class: AigfMitigation_owasp_ml_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: owasp_ml_references Description: Keys of docs/_data/references/owasp-ml.yml.
-- # Class: AigfMitigation_sr11_7_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: sr11_7_references Description: Keys of docs/_data/references/sr11-7.yml.
-- # Class: AigfMitigation_uk_regulations_references
--     * Slot: AigfMitigation_item_id Description: Autocreated FK slot
--     * Slot: uk_regulations_references Description: Keys of docs/_data/references/uk-regulations.yml.
-- # Class: AigfUseCase_related_risks
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: related_risks_item_id Description: The risks a page relates to.
-- # Class: AigfUseCase_related_mitigations
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: related_mitigations_item_id Description: The mitigations a page relates to.
-- # Class: AigfUseCase_data_handling_aspects
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: data_handling_aspects Description: The options of the deployment model's data_handling axis a use case takes.
-- # Class: AigfUseCase_atr_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: atr_references Description: Keys of docs/_data/references/atr.yml.
-- # Class: AigfUseCase_canada_regulations_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: canada_regulations_references Description: Keys of docs/_data/references/canada-regulations.yml.
-- # Class: AigfUseCase_eu_ai_act_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: eu_ai_act_references Description: Keys of docs/_data/references/eu-ai-act.yml.
-- # Class: AigfUseCase_ffiec_itbooklets_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: ffiec_itbooklets_references Description: Keys of docs/_data/references/ffiec-itbooklets.yml.
-- # Class: AigfUseCase_iosco_supervisory_toolkit_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: iosco_supervisory_toolkit_references Description: Keys of docs/_data/references/iosco-supervisory-toolkit.yml.
-- # Class: AigfUseCase_iso_42001_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: iso_42001_references Description: Keys of docs/_data/references/iso-42001.yml.
-- # Class: AigfUseCase_nist_ai_600_1_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: nist_ai_600_1_references Description: Keys of docs/_data/references/nist-ai-600-1.yml.
-- # Class: AigfUseCase_nist_sp_800_53r5_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: nist_sp_800_53r5_references Description: Keys of docs/_data/references/nist-sp-800-53r5.yml.
-- # Class: AigfUseCase_owasp_asi_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: owasp_asi_references Description: Keys of docs/_data/references/owasp-asi.yml.
-- # Class: AigfUseCase_owasp_llm_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: owasp_llm_references Description: Keys of docs/_data/references/owasp-llm.yml.
-- # Class: AigfUseCase_owasp_ml_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: owasp_ml_references Description: Keys of docs/_data/references/owasp-ml.yml.
-- # Class: AigfUseCase_sr11_7_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: sr11_7_references Description: Keys of docs/_data/references/sr11-7.yml.
-- # Class: AigfUseCase_uk_regulations_references
--     * Slot: AigfUseCase_item_id Description: Autocreated FK slot
--     * Slot: uk_regulations_references Description: Keys of docs/_data/references/uk-regulations.yml.
-- # Class: AigfDataClassificationUse_data_types
--     * Slot: AigfDataClassificationUse_id Description: Autocreated FK slot
--     * Slot: data_types Description: The kinds of data a use case holds under one classification.
-- # Class: AigfDataClassification_examples
--     * Slot: AigfDataClassification_id Description: Autocreated FK slot
--     * Slot: examples Description: Kinds of data in a class.
-- # Class: AigfReferenceIndex_entry_keys
--     * Slot: AigfReferenceIndex_id Description: Autocreated FK slot
--     * Slot: entry_keys Description: The keys the reference file holds.
-- # Class: AigfUseCaseArea_use_case_names
--     * Slot: AigfUseCaseArea_id Description: Autocreated FK slot
--     * Slot: use_case_names Description: The use cases under an area, as the taxonomy names them.

CREATE TABLE "AigfCatalogue" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	version TEXT NOT NULL,
	release_date DATE NOT NULL,
	source_commit TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AigfCatalogue_id" ON "AigfCatalogue" (id);

CREATE TABLE "AigfItem" (
	item_id TEXT NOT NULL,
	sequence INTEGER NOT NULL,
	title TEXT NOT NULL,
	layout TEXT NOT NULL,
	doc_status VARCHAR(22) NOT NULL,
	source_file TEXT NOT NULL,
	PRIMARY KEY (item_id)
);
CREATE INDEX "ix_AigfItem_item_id" ON "AigfItem" (item_id);

CREATE TABLE "AigfReferenceCitations" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AigfReferenceCitations_id" ON "AigfReferenceCitations" (id);

CREATE TABLE "AigfReferenceFile" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	source_url TEXT,
	lens VARCHAR(10) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AigfReferenceFile_id" ON "AigfReferenceFile" (id);

CREATE TABLE "AigfRisk" (
	risk_type VARCHAR(3) NOT NULL,
	risk_domain VARCHAR(10) NOT NULL,
	item_id TEXT NOT NULL,
	sequence INTEGER NOT NULL,
	title TEXT NOT NULL,
	layout TEXT NOT NULL,
	doc_status VARCHAR(22) NOT NULL,
	source_file TEXT NOT NULL,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (item_id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfRisk_item_id" ON "AigfRisk" (item_id);

CREATE TABLE "AigfMitigation" (
	mitigation_type VARCHAR(4) NOT NULL,
	mitigation_domain VARCHAR(10) NOT NULL,
	item_id TEXT NOT NULL,
	sequence INTEGER NOT NULL,
	title TEXT NOT NULL,
	layout TEXT NOT NULL,
	doc_status VARCHAR(22) NOT NULL,
	source_file TEXT NOT NULL,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (item_id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfMitigation_item_id" ON "AigfMitigation" (item_id);

CREATE TABLE "AigfUseCase" (
	category VARCHAR(35) NOT NULL,
	description TEXT NOT NULL,
	end_user TEXT,
	business_value TEXT,
	item_id TEXT NOT NULL,
	sequence INTEGER NOT NULL,
	title TEXT NOT NULL,
	layout TEXT NOT NULL,
	doc_status VARCHAR(22) NOT NULL,
	source_file TEXT NOT NULL,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (item_id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfUseCase_item_id" ON "AigfUseCase" (item_id);

CREATE TABLE "AigfDataClassification" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	sensitivity VARCHAR(8) NOT NULL,
	description TEXT NOT NULL,
	storage_location TEXT,
	regulations TEXT,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfDataClassification_id" ON "AigfDataClassification" (id);

CREATE TABLE "AigfReferenceLens" (
	id INTEGER NOT NULL,
	lens VARCHAR(10) NOT NULL,
	label TEXT NOT NULL,
	question TEXT NOT NULL,
	icon TEXT,
	color TEXT,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfReferenceLens_id" ON "AigfReferenceLens" (id);

CREATE TABLE "AigfReferenceEntry" (
	reference_key TEXT NOT NULL,
	title TEXT NOT NULL,
	url TEXT NOT NULL,
	description TEXT,
	issuer TEXT,
	booklet_abbrev TEXT,
	superseded_by TEXT,
	"AigfReferenceFile_id" INTEGER,
	PRIMARY KEY (reference_key, title, url, description, issuer, booklet_abbrev, superseded_by, "AigfReferenceFile_id"),
	UNIQUE ("AigfReferenceFile_id", reference_key),
	FOREIGN KEY("AigfReferenceFile_id") REFERENCES "AigfReferenceFile" (id)
);
CREATE INDEX "ix_AigfReferenceEntry_title" ON "AigfReferenceEntry" (title);
CREATE INDEX "ix_AigfReferenceEntry_issuer" ON "AigfReferenceEntry" (issuer);
CREATE INDEX "ix_AigfReferenceEntry_booklet_abbrev" ON "AigfReferenceEntry" (booklet_abbrev);
CREATE INDEX "ix_AigfReferenceEntry_description" ON "AigfReferenceEntry" (description);
CREATE INDEX "ix_AigfReferenceEntry_superseded_by" ON "AigfReferenceEntry" (superseded_by);
CREATE INDEX "AigfReferenceEntry_AigfReferenceFile_id_reference_key_idx" ON "AigfReferenceEntry" ("AigfReferenceFile_id", reference_key);
CREATE INDEX "ix_AigfReferenceEntry_AigfReferenceFile_id" ON "AigfReferenceEntry" ("AigfReferenceFile_id");
CREATE INDEX "ix_AigfReferenceEntry_url" ON "AigfReferenceEntry" (url);
CREATE INDEX "ix_AigfReferenceEntry_reference_key" ON "AigfReferenceEntry" (reference_key);

CREATE TABLE "AigfReferenceIndex" (
	id INTEGER NOT NULL,
	reference_file TEXT NOT NULL,
	lens VARCHAR(10) NOT NULL,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfReferenceIndex_id" ON "AigfReferenceIndex" (id);

CREATE TABLE "AigfUseCaseDomain" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfUseCaseDomain_id" ON "AigfUseCaseDomain" (id);

CREATE TABLE "AigfDeploymentAxis" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"AigfCatalogue_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfDeploymentAxis_id" ON "AigfDeploymentAxis" (id);

CREATE TABLE "AigfCatalogue_cross_cutting_capabilities" (
	"AigfCatalogue_id" INTEGER,
	cross_cutting_capabilities TEXT,
	PRIMARY KEY ("AigfCatalogue_id", cross_cutting_capabilities),
	FOREIGN KEY("AigfCatalogue_id") REFERENCES "AigfCatalogue" (id)
);
CREATE INDEX "ix_AigfCatalogue_cross_cutting_capabilities_AigfCatalogue_id" ON "AigfCatalogue_cross_cutting_capabilities" ("AigfCatalogue_id");
CREATE INDEX "ix_AigfCatalogue_cross_cutting_capabilities_cross_cutting_capabilities" ON "AigfCatalogue_cross_cutting_capabilities" (cross_cutting_capabilities);

CREATE TABLE "AigfReferenceCitations_atr_references" (
	"AigfReferenceCitations_id" INTEGER,
	atr_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", atr_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_atr_references_atr_references" ON "AigfReferenceCitations_atr_references" (atr_references);
CREATE INDEX "ix_AigfReferenceCitations_atr_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_atr_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_canada_regulations_references" (
	"AigfReferenceCitations_id" INTEGER,
	canada_regulations_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", canada_regulations_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_canada_regulations_references_canada_regulations_references" ON "AigfReferenceCitations_canada_regulations_references" (canada_regulations_references);
CREATE INDEX "ix_AigfReferenceCitations_canada_regulations_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_canada_regulations_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_eu_ai_act_references" (
	"AigfReferenceCitations_id" INTEGER,
	eu_ai_act_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", eu_ai_act_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_eu_ai_act_references_eu_ai_act_references" ON "AigfReferenceCitations_eu_ai_act_references" (eu_ai_act_references);
CREATE INDEX "ix_AigfReferenceCitations_eu_ai_act_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_eu_ai_act_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_ffiec_itbooklets_references" (
	"AigfReferenceCitations_id" INTEGER,
	ffiec_itbooklets_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", ffiec_itbooklets_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_ffiec_itbooklets_references_ffiec_itbooklets_references" ON "AigfReferenceCitations_ffiec_itbooklets_references" (ffiec_itbooklets_references);
CREATE INDEX "ix_AigfReferenceCitations_ffiec_itbooklets_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_ffiec_itbooklets_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_iosco_supervisory_toolkit_references" (
	"AigfReferenceCitations_id" INTEGER,
	iosco_supervisory_toolkit_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", iosco_supervisory_toolkit_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_iosco_supervisory_toolkit_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_iosco_supervisory_toolkit_references" ("AigfReferenceCitations_id");
CREATE INDEX "ix_AigfReferenceCitations_iosco_supervisory_toolkit_references_iosco_supervisory_toolkit_references" ON "AigfReferenceCitations_iosco_supervisory_toolkit_references" (iosco_supervisory_toolkit_references);

CREATE TABLE "AigfReferenceCitations_iso_42001_references" (
	"AigfReferenceCitations_id" INTEGER,
	iso_42001_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", iso_42001_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_iso_42001_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_iso_42001_references" ("AigfReferenceCitations_id");
CREATE INDEX "ix_AigfReferenceCitations_iso_42001_references_iso_42001_references" ON "AigfReferenceCitations_iso_42001_references" (iso_42001_references);

CREATE TABLE "AigfReferenceCitations_nist_ai_600_1_references" (
	"AigfReferenceCitations_id" INTEGER,
	nist_ai_600_1_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", nist_ai_600_1_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_nist_ai_600_1_references_nist_ai_600_1_references" ON "AigfReferenceCitations_nist_ai_600_1_references" (nist_ai_600_1_references);
CREATE INDEX "ix_AigfReferenceCitations_nist_ai_600_1_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_nist_ai_600_1_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_nist_sp_800_53r5_references" (
	"AigfReferenceCitations_id" INTEGER,
	nist_sp_800_53r5_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", nist_sp_800_53r5_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_nist_sp_800_53r5_references_nist_sp_800_53r5_references" ON "AigfReferenceCitations_nist_sp_800_53r5_references" (nist_sp_800_53r5_references);
CREATE INDEX "ix_AigfReferenceCitations_nist_sp_800_53r5_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_nist_sp_800_53r5_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_owasp_asi_references" (
	"AigfReferenceCitations_id" INTEGER,
	owasp_asi_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", owasp_asi_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_owasp_asi_references_owasp_asi_references" ON "AigfReferenceCitations_owasp_asi_references" (owasp_asi_references);
CREATE INDEX "ix_AigfReferenceCitations_owasp_asi_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_owasp_asi_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_owasp_llm_references" (
	"AigfReferenceCitations_id" INTEGER,
	owasp_llm_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", owasp_llm_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_owasp_llm_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_owasp_llm_references" ("AigfReferenceCitations_id");
CREATE INDEX "ix_AigfReferenceCitations_owasp_llm_references_owasp_llm_references" ON "AigfReferenceCitations_owasp_llm_references" (owasp_llm_references);

CREATE TABLE "AigfReferenceCitations_owasp_ml_references" (
	"AigfReferenceCitations_id" INTEGER,
	owasp_ml_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", owasp_ml_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_owasp_ml_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_owasp_ml_references" ("AigfReferenceCitations_id");
CREATE INDEX "ix_AigfReferenceCitations_owasp_ml_references_owasp_ml_references" ON "AigfReferenceCitations_owasp_ml_references" (owasp_ml_references);

CREATE TABLE "AigfReferenceCitations_sr11_7_references" (
	"AigfReferenceCitations_id" INTEGER,
	sr11_7_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", sr11_7_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_sr11_7_references_sr11_7_references" ON "AigfReferenceCitations_sr11_7_references" (sr11_7_references);
CREATE INDEX "ix_AigfReferenceCitations_sr11_7_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_sr11_7_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfReferenceCitations_uk_regulations_references" (
	"AigfReferenceCitations_id" INTEGER,
	uk_regulations_references TEXT,
	PRIMARY KEY ("AigfReferenceCitations_id", uk_regulations_references),
	FOREIGN KEY("AigfReferenceCitations_id") REFERENCES "AigfReferenceCitations" (id)
);
CREATE INDEX "ix_AigfReferenceCitations_uk_regulations_references_uk_regulations_references" ON "AigfReferenceCitations_uk_regulations_references" (uk_regulations_references);
CREATE INDEX "ix_AigfReferenceCitations_uk_regulations_references_AigfReferenceCitations_id" ON "AigfReferenceCitations_uk_regulations_references" ("AigfReferenceCitations_id");

CREATE TABLE "AigfDataClassificationUse" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"AigfUseCase_item_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfDataClassificationUse_id" ON "AigfDataClassificationUse" (id);

CREATE TABLE "AigfRegulatoryReference" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	url TEXT,
	jurisdiction TEXT,
	"AigfUseCase_item_id" TEXT,
	"AigfDataClassification_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id),
	FOREIGN KEY("AigfDataClassification_id") REFERENCES "AigfDataClassification" (id)
);
CREATE INDEX "ix_AigfRegulatoryReference_id" ON "AigfRegulatoryReference" (id);

CREATE TABLE "AigfFurtherReading" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	url TEXT,
	source TEXT,
	"AigfUseCase_item_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfFurtherReading_id" ON "AigfFurtherReading" (id);

CREATE TABLE "AigfUseCaseArea" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"AigfUseCaseDomain_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfUseCaseDomain_id") REFERENCES "AigfUseCaseDomain" (id)
);
CREATE INDEX "ix_AigfUseCaseArea_id" ON "AigfUseCaseArea" (id);

CREATE TABLE "AigfDeploymentOption" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	"AigfDeploymentAxis_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AigfDeploymentAxis_id") REFERENCES "AigfDeploymentAxis" (id)
);
CREATE INDEX "ix_AigfDeploymentOption_id" ON "AigfDeploymentOption" (id);

CREATE TABLE "AigfRisk_related_risks" (
	"AigfRisk_item_id" TEXT,
	related_risks_item_id TEXT,
	PRIMARY KEY ("AigfRisk_item_id", related_risks_item_id),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id),
	FOREIGN KEY(related_risks_item_id) REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_related_risks_related_risks_item_id" ON "AigfRisk_related_risks" (related_risks_item_id);
CREATE INDEX "ix_AigfRisk_related_risks_AigfRisk_item_id" ON "AigfRisk_related_risks" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_atr_references" (
	"AigfRisk_item_id" TEXT,
	atr_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", atr_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_atr_references_atr_references" ON "AigfRisk_atr_references" (atr_references);
CREATE INDEX "ix_AigfRisk_atr_references_AigfRisk_item_id" ON "AigfRisk_atr_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_canada_regulations_references" (
	"AigfRisk_item_id" TEXT,
	canada_regulations_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", canada_regulations_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_canada_regulations_references_canada_regulations_references" ON "AigfRisk_canada_regulations_references" (canada_regulations_references);
CREATE INDEX "ix_AigfRisk_canada_regulations_references_AigfRisk_item_id" ON "AigfRisk_canada_regulations_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_eu_ai_act_references" (
	"AigfRisk_item_id" TEXT,
	eu_ai_act_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", eu_ai_act_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_eu_ai_act_references_AigfRisk_item_id" ON "AigfRisk_eu_ai_act_references" ("AigfRisk_item_id");
CREATE INDEX "ix_AigfRisk_eu_ai_act_references_eu_ai_act_references" ON "AigfRisk_eu_ai_act_references" (eu_ai_act_references);

CREATE TABLE "AigfRisk_ffiec_itbooklets_references" (
	"AigfRisk_item_id" TEXT,
	ffiec_itbooklets_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", ffiec_itbooklets_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_ffiec_itbooklets_references_AigfRisk_item_id" ON "AigfRisk_ffiec_itbooklets_references" ("AigfRisk_item_id");
CREATE INDEX "ix_AigfRisk_ffiec_itbooklets_references_ffiec_itbooklets_references" ON "AigfRisk_ffiec_itbooklets_references" (ffiec_itbooklets_references);

CREATE TABLE "AigfRisk_iosco_supervisory_toolkit_references" (
	"AigfRisk_item_id" TEXT,
	iosco_supervisory_toolkit_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", iosco_supervisory_toolkit_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_iosco_supervisory_toolkit_references_AigfRisk_item_id" ON "AigfRisk_iosco_supervisory_toolkit_references" ("AigfRisk_item_id");
CREATE INDEX "ix_AigfRisk_iosco_supervisory_toolkit_references_iosco_supervisory_toolkit_references" ON "AigfRisk_iosco_supervisory_toolkit_references" (iosco_supervisory_toolkit_references);

CREATE TABLE "AigfRisk_iso_42001_references" (
	"AigfRisk_item_id" TEXT,
	iso_42001_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", iso_42001_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_iso_42001_references_iso_42001_references" ON "AigfRisk_iso_42001_references" (iso_42001_references);
CREATE INDEX "ix_AigfRisk_iso_42001_references_AigfRisk_item_id" ON "AigfRisk_iso_42001_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_nist_ai_600_1_references" (
	"AigfRisk_item_id" TEXT,
	nist_ai_600_1_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", nist_ai_600_1_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_nist_ai_600_1_references_nist_ai_600_1_references" ON "AigfRisk_nist_ai_600_1_references" (nist_ai_600_1_references);
CREATE INDEX "ix_AigfRisk_nist_ai_600_1_references_AigfRisk_item_id" ON "AigfRisk_nist_ai_600_1_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_nist_sp_800_53r5_references" (
	"AigfRisk_item_id" TEXT,
	nist_sp_800_53r5_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", nist_sp_800_53r5_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_nist_sp_800_53r5_references_AigfRisk_item_id" ON "AigfRisk_nist_sp_800_53r5_references" ("AigfRisk_item_id");
CREATE INDEX "ix_AigfRisk_nist_sp_800_53r5_references_nist_sp_800_53r5_references" ON "AigfRisk_nist_sp_800_53r5_references" (nist_sp_800_53r5_references);

CREATE TABLE "AigfRisk_owasp_asi_references" (
	"AigfRisk_item_id" TEXT,
	owasp_asi_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", owasp_asi_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_owasp_asi_references_AigfRisk_item_id" ON "AigfRisk_owasp_asi_references" ("AigfRisk_item_id");
CREATE INDEX "ix_AigfRisk_owasp_asi_references_owasp_asi_references" ON "AigfRisk_owasp_asi_references" (owasp_asi_references);

CREATE TABLE "AigfRisk_owasp_llm_references" (
	"AigfRisk_item_id" TEXT,
	owasp_llm_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", owasp_llm_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_owasp_llm_references_owasp_llm_references" ON "AigfRisk_owasp_llm_references" (owasp_llm_references);
CREATE INDEX "ix_AigfRisk_owasp_llm_references_AigfRisk_item_id" ON "AigfRisk_owasp_llm_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_owasp_ml_references" (
	"AigfRisk_item_id" TEXT,
	owasp_ml_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", owasp_ml_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_owasp_ml_references_owasp_ml_references" ON "AigfRisk_owasp_ml_references" (owasp_ml_references);
CREATE INDEX "ix_AigfRisk_owasp_ml_references_AigfRisk_item_id" ON "AigfRisk_owasp_ml_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_sr11_7_references" (
	"AigfRisk_item_id" TEXT,
	sr11_7_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", sr11_7_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_sr11_7_references_sr11_7_references" ON "AigfRisk_sr11_7_references" (sr11_7_references);
CREATE INDEX "ix_AigfRisk_sr11_7_references_AigfRisk_item_id" ON "AigfRisk_sr11_7_references" ("AigfRisk_item_id");

CREATE TABLE "AigfRisk_uk_regulations_references" (
	"AigfRisk_item_id" TEXT,
	uk_regulations_references TEXT,
	PRIMARY KEY ("AigfRisk_item_id", uk_regulations_references),
	FOREIGN KEY("AigfRisk_item_id") REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfRisk_uk_regulations_references_uk_regulations_references" ON "AigfRisk_uk_regulations_references" (uk_regulations_references);
CREATE INDEX "ix_AigfRisk_uk_regulations_references_AigfRisk_item_id" ON "AigfRisk_uk_regulations_references" ("AigfRisk_item_id");

CREATE TABLE "AigfMitigation_mitigates" (
	"AigfMitigation_item_id" TEXT,
	mitigates_item_id TEXT NOT NULL,
	PRIMARY KEY ("AigfMitigation_item_id", mitigates_item_id),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id),
	FOREIGN KEY(mitigates_item_id) REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfMitigation_mitigates_AigfMitigation_item_id" ON "AigfMitigation_mitigates" ("AigfMitigation_item_id");
CREATE INDEX "ix_AigfMitigation_mitigates_mitigates_item_id" ON "AigfMitigation_mitigates" (mitigates_item_id);

CREATE TABLE "AigfMitigation_related_mitigations" (
	"AigfMitigation_item_id" TEXT,
	related_mitigations_item_id TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", related_mitigations_item_id),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id),
	FOREIGN KEY(related_mitigations_item_id) REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_related_mitigations_related_mitigations_item_id" ON "AigfMitigation_related_mitigations" (related_mitigations_item_id);
CREATE INDEX "ix_AigfMitigation_related_mitigations_AigfMitigation_item_id" ON "AigfMitigation_related_mitigations" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_atr_references" (
	"AigfMitigation_item_id" TEXT,
	atr_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", atr_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_atr_references_atr_references" ON "AigfMitigation_atr_references" (atr_references);
CREATE INDEX "ix_AigfMitigation_atr_references_AigfMitigation_item_id" ON "AigfMitigation_atr_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_canada_regulations_references" (
	"AigfMitigation_item_id" TEXT,
	canada_regulations_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", canada_regulations_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_canada_regulations_references_canada_regulations_references" ON "AigfMitigation_canada_regulations_references" (canada_regulations_references);
CREATE INDEX "ix_AigfMitigation_canada_regulations_references_AigfMitigation_item_id" ON "AigfMitigation_canada_regulations_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_eu_ai_act_references" (
	"AigfMitigation_item_id" TEXT,
	eu_ai_act_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", eu_ai_act_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_eu_ai_act_references_eu_ai_act_references" ON "AigfMitigation_eu_ai_act_references" (eu_ai_act_references);
CREATE INDEX "ix_AigfMitigation_eu_ai_act_references_AigfMitigation_item_id" ON "AigfMitigation_eu_ai_act_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_ffiec_itbooklets_references" (
	"AigfMitigation_item_id" TEXT,
	ffiec_itbooklets_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", ffiec_itbooklets_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_ffiec_itbooklets_references_AigfMitigation_item_id" ON "AigfMitigation_ffiec_itbooklets_references" ("AigfMitigation_item_id");
CREATE INDEX "ix_AigfMitigation_ffiec_itbooklets_references_ffiec_itbooklets_references" ON "AigfMitigation_ffiec_itbooklets_references" (ffiec_itbooklets_references);

CREATE TABLE "AigfMitigation_iosco_supervisory_toolkit_references" (
	"AigfMitigation_item_id" TEXT,
	iosco_supervisory_toolkit_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", iosco_supervisory_toolkit_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_iosco_supervisory_toolkit_references_AigfMitigation_item_id" ON "AigfMitigation_iosco_supervisory_toolkit_references" ("AigfMitigation_item_id");
CREATE INDEX "ix_AigfMitigation_iosco_supervisory_toolkit_references_iosco_supervisory_toolkit_references" ON "AigfMitigation_iosco_supervisory_toolkit_references" (iosco_supervisory_toolkit_references);

CREATE TABLE "AigfMitigation_iso_42001_references" (
	"AigfMitigation_item_id" TEXT,
	iso_42001_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", iso_42001_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_iso_42001_references_AigfMitigation_item_id" ON "AigfMitigation_iso_42001_references" ("AigfMitigation_item_id");
CREATE INDEX "ix_AigfMitigation_iso_42001_references_iso_42001_references" ON "AigfMitigation_iso_42001_references" (iso_42001_references);

CREATE TABLE "AigfMitigation_nist_ai_600_1_references" (
	"AigfMitigation_item_id" TEXT,
	nist_ai_600_1_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", nist_ai_600_1_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_nist_ai_600_1_references_nist_ai_600_1_references" ON "AigfMitigation_nist_ai_600_1_references" (nist_ai_600_1_references);
CREATE INDEX "ix_AigfMitigation_nist_ai_600_1_references_AigfMitigation_item_id" ON "AigfMitigation_nist_ai_600_1_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_nist_sp_800_53r5_references" (
	"AigfMitigation_item_id" TEXT,
	nist_sp_800_53r5_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", nist_sp_800_53r5_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_nist_sp_800_53r5_references_AigfMitigation_item_id" ON "AigfMitigation_nist_sp_800_53r5_references" ("AigfMitigation_item_id");
CREATE INDEX "ix_AigfMitigation_nist_sp_800_53r5_references_nist_sp_800_53r5_references" ON "AigfMitigation_nist_sp_800_53r5_references" (nist_sp_800_53r5_references);

CREATE TABLE "AigfMitigation_owasp_asi_references" (
	"AigfMitigation_item_id" TEXT,
	owasp_asi_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", owasp_asi_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_owasp_asi_references_owasp_asi_references" ON "AigfMitigation_owasp_asi_references" (owasp_asi_references);
CREATE INDEX "ix_AigfMitigation_owasp_asi_references_AigfMitigation_item_id" ON "AigfMitigation_owasp_asi_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_owasp_llm_references" (
	"AigfMitigation_item_id" TEXT,
	owasp_llm_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", owasp_llm_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_owasp_llm_references_owasp_llm_references" ON "AigfMitigation_owasp_llm_references" (owasp_llm_references);
CREATE INDEX "ix_AigfMitigation_owasp_llm_references_AigfMitigation_item_id" ON "AigfMitigation_owasp_llm_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_owasp_ml_references" (
	"AigfMitigation_item_id" TEXT,
	owasp_ml_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", owasp_ml_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_owasp_ml_references_AigfMitigation_item_id" ON "AigfMitigation_owasp_ml_references" ("AigfMitigation_item_id");
CREATE INDEX "ix_AigfMitigation_owasp_ml_references_owasp_ml_references" ON "AigfMitigation_owasp_ml_references" (owasp_ml_references);

CREATE TABLE "AigfMitigation_sr11_7_references" (
	"AigfMitigation_item_id" TEXT,
	sr11_7_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", sr11_7_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_sr11_7_references_sr11_7_references" ON "AigfMitigation_sr11_7_references" (sr11_7_references);
CREATE INDEX "ix_AigfMitigation_sr11_7_references_AigfMitigation_item_id" ON "AigfMitigation_sr11_7_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfMitigation_uk_regulations_references" (
	"AigfMitigation_item_id" TEXT,
	uk_regulations_references TEXT,
	PRIMARY KEY ("AigfMitigation_item_id", uk_regulations_references),
	FOREIGN KEY("AigfMitigation_item_id") REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfMitigation_uk_regulations_references_uk_regulations_references" ON "AigfMitigation_uk_regulations_references" (uk_regulations_references);
CREATE INDEX "ix_AigfMitigation_uk_regulations_references_AigfMitigation_item_id" ON "AigfMitigation_uk_regulations_references" ("AigfMitigation_item_id");

CREATE TABLE "AigfUseCase_related_risks" (
	"AigfUseCase_item_id" TEXT,
	related_risks_item_id TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", related_risks_item_id),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id),
	FOREIGN KEY(related_risks_item_id) REFERENCES "AigfRisk" (item_id)
);
CREATE INDEX "ix_AigfUseCase_related_risks_related_risks_item_id" ON "AigfUseCase_related_risks" (related_risks_item_id);
CREATE INDEX "ix_AigfUseCase_related_risks_AigfUseCase_item_id" ON "AigfUseCase_related_risks" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_related_mitigations" (
	"AigfUseCase_item_id" TEXT,
	related_mitigations_item_id TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", related_mitigations_item_id),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id),
	FOREIGN KEY(related_mitigations_item_id) REFERENCES "AigfMitigation" (item_id)
);
CREATE INDEX "ix_AigfUseCase_related_mitigations_related_mitigations_item_id" ON "AigfUseCase_related_mitigations" (related_mitigations_item_id);
CREATE INDEX "ix_AigfUseCase_related_mitigations_AigfUseCase_item_id" ON "AigfUseCase_related_mitigations" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_data_handling_aspects" (
	"AigfUseCase_item_id" TEXT,
	data_handling_aspects VARCHAR(18),
	PRIMARY KEY ("AigfUseCase_item_id", data_handling_aspects),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_data_handling_aspects_data_handling_aspects" ON "AigfUseCase_data_handling_aspects" (data_handling_aspects);
CREATE INDEX "ix_AigfUseCase_data_handling_aspects_AigfUseCase_item_id" ON "AigfUseCase_data_handling_aspects" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_atr_references" (
	"AigfUseCase_item_id" TEXT,
	atr_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", atr_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_atr_references_AigfUseCase_item_id" ON "AigfUseCase_atr_references" ("AigfUseCase_item_id");
CREATE INDEX "ix_AigfUseCase_atr_references_atr_references" ON "AigfUseCase_atr_references" (atr_references);

CREATE TABLE "AigfUseCase_canada_regulations_references" (
	"AigfUseCase_item_id" TEXT,
	canada_regulations_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", canada_regulations_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_canada_regulations_references_canada_regulations_references" ON "AigfUseCase_canada_regulations_references" (canada_regulations_references);
CREATE INDEX "ix_AigfUseCase_canada_regulations_references_AigfUseCase_item_id" ON "AigfUseCase_canada_regulations_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_eu_ai_act_references" (
	"AigfUseCase_item_id" TEXT,
	eu_ai_act_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", eu_ai_act_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_eu_ai_act_references_AigfUseCase_item_id" ON "AigfUseCase_eu_ai_act_references" ("AigfUseCase_item_id");
CREATE INDEX "ix_AigfUseCase_eu_ai_act_references_eu_ai_act_references" ON "AigfUseCase_eu_ai_act_references" (eu_ai_act_references);

CREATE TABLE "AigfUseCase_ffiec_itbooklets_references" (
	"AigfUseCase_item_id" TEXT,
	ffiec_itbooklets_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", ffiec_itbooklets_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_ffiec_itbooklets_references_ffiec_itbooklets_references" ON "AigfUseCase_ffiec_itbooklets_references" (ffiec_itbooklets_references);
CREATE INDEX "ix_AigfUseCase_ffiec_itbooklets_references_AigfUseCase_item_id" ON "AigfUseCase_ffiec_itbooklets_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_iosco_supervisory_toolkit_references" (
	"AigfUseCase_item_id" TEXT,
	iosco_supervisory_toolkit_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", iosco_supervisory_toolkit_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_iosco_supervisory_toolkit_references_iosco_supervisory_toolkit_references" ON "AigfUseCase_iosco_supervisory_toolkit_references" (iosco_supervisory_toolkit_references);
CREATE INDEX "ix_AigfUseCase_iosco_supervisory_toolkit_references_AigfUseCase_item_id" ON "AigfUseCase_iosco_supervisory_toolkit_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_iso_42001_references" (
	"AigfUseCase_item_id" TEXT,
	iso_42001_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", iso_42001_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_iso_42001_references_AigfUseCase_item_id" ON "AigfUseCase_iso_42001_references" ("AigfUseCase_item_id");
CREATE INDEX "ix_AigfUseCase_iso_42001_references_iso_42001_references" ON "AigfUseCase_iso_42001_references" (iso_42001_references);

CREATE TABLE "AigfUseCase_nist_ai_600_1_references" (
	"AigfUseCase_item_id" TEXT,
	nist_ai_600_1_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", nist_ai_600_1_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_nist_ai_600_1_references_nist_ai_600_1_references" ON "AigfUseCase_nist_ai_600_1_references" (nist_ai_600_1_references);
CREATE INDEX "ix_AigfUseCase_nist_ai_600_1_references_AigfUseCase_item_id" ON "AigfUseCase_nist_ai_600_1_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_nist_sp_800_53r5_references" (
	"AigfUseCase_item_id" TEXT,
	nist_sp_800_53r5_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", nist_sp_800_53r5_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_nist_sp_800_53r5_references_nist_sp_800_53r5_references" ON "AigfUseCase_nist_sp_800_53r5_references" (nist_sp_800_53r5_references);
CREATE INDEX "ix_AigfUseCase_nist_sp_800_53r5_references_AigfUseCase_item_id" ON "AigfUseCase_nist_sp_800_53r5_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_owasp_asi_references" (
	"AigfUseCase_item_id" TEXT,
	owasp_asi_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", owasp_asi_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_owasp_asi_references_owasp_asi_references" ON "AigfUseCase_owasp_asi_references" (owasp_asi_references);
CREATE INDEX "ix_AigfUseCase_owasp_asi_references_AigfUseCase_item_id" ON "AigfUseCase_owasp_asi_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_owasp_llm_references" (
	"AigfUseCase_item_id" TEXT,
	owasp_llm_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", owasp_llm_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_owasp_llm_references_AigfUseCase_item_id" ON "AigfUseCase_owasp_llm_references" ("AigfUseCase_item_id");
CREATE INDEX "ix_AigfUseCase_owasp_llm_references_owasp_llm_references" ON "AigfUseCase_owasp_llm_references" (owasp_llm_references);

CREATE TABLE "AigfUseCase_owasp_ml_references" (
	"AigfUseCase_item_id" TEXT,
	owasp_ml_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", owasp_ml_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_owasp_ml_references_owasp_ml_references" ON "AigfUseCase_owasp_ml_references" (owasp_ml_references);
CREATE INDEX "ix_AigfUseCase_owasp_ml_references_AigfUseCase_item_id" ON "AigfUseCase_owasp_ml_references" ("AigfUseCase_item_id");

CREATE TABLE "AigfUseCase_sr11_7_references" (
	"AigfUseCase_item_id" TEXT,
	sr11_7_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", sr11_7_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_sr11_7_references_AigfUseCase_item_id" ON "AigfUseCase_sr11_7_references" ("AigfUseCase_item_id");
CREATE INDEX "ix_AigfUseCase_sr11_7_references_sr11_7_references" ON "AigfUseCase_sr11_7_references" (sr11_7_references);

CREATE TABLE "AigfUseCase_uk_regulations_references" (
	"AigfUseCase_item_id" TEXT,
	uk_regulations_references TEXT,
	PRIMARY KEY ("AigfUseCase_item_id", uk_regulations_references),
	FOREIGN KEY("AigfUseCase_item_id") REFERENCES "AigfUseCase" (item_id)
);
CREATE INDEX "ix_AigfUseCase_uk_regulations_references_AigfUseCase_item_id" ON "AigfUseCase_uk_regulations_references" ("AigfUseCase_item_id");
CREATE INDEX "ix_AigfUseCase_uk_regulations_references_uk_regulations_references" ON "AigfUseCase_uk_regulations_references" (uk_regulations_references);

CREATE TABLE "AigfDataClassification_examples" (
	"AigfDataClassification_id" INTEGER,
	examples TEXT,
	PRIMARY KEY ("AigfDataClassification_id", examples),
	FOREIGN KEY("AigfDataClassification_id") REFERENCES "AigfDataClassification" (id)
);
CREATE INDEX "ix_AigfDataClassification_examples_examples" ON "AigfDataClassification_examples" (examples);
CREATE INDEX "ix_AigfDataClassification_examples_AigfDataClassification_id" ON "AigfDataClassification_examples" ("AigfDataClassification_id");

CREATE TABLE "AigfReferenceIndex_entry_keys" (
	"AigfReferenceIndex_id" INTEGER,
	entry_keys TEXT,
	PRIMARY KEY ("AigfReferenceIndex_id", entry_keys),
	FOREIGN KEY("AigfReferenceIndex_id") REFERENCES "AigfReferenceIndex" (id)
);
CREATE INDEX "ix_AigfReferenceIndex_entry_keys_AigfReferenceIndex_id" ON "AigfReferenceIndex_entry_keys" ("AigfReferenceIndex_id");
CREATE INDEX "ix_AigfReferenceIndex_entry_keys_entry_keys" ON "AigfReferenceIndex_entry_keys" (entry_keys);

CREATE TABLE "AigfDataClassificationUse_data_types" (
	"AigfDataClassificationUse_id" INTEGER,
	data_types TEXT,
	PRIMARY KEY ("AigfDataClassificationUse_id", data_types),
	FOREIGN KEY("AigfDataClassificationUse_id") REFERENCES "AigfDataClassificationUse" (id)
);
CREATE INDEX "ix_AigfDataClassificationUse_data_types_AigfDataClassificationUse_id" ON "AigfDataClassificationUse_data_types" ("AigfDataClassificationUse_id");
CREATE INDEX "ix_AigfDataClassificationUse_data_types_data_types" ON "AigfDataClassificationUse_data_types" (data_types);

CREATE TABLE "AigfUseCaseArea_use_case_names" (
	"AigfUseCaseArea_id" INTEGER,
	use_case_names TEXT,
	PRIMARY KEY ("AigfUseCaseArea_id", use_case_names),
	FOREIGN KEY("AigfUseCaseArea_id") REFERENCES "AigfUseCaseArea" (id)
);
CREATE INDEX "ix_AigfUseCaseArea_use_case_names_AigfUseCaseArea_id" ON "AigfUseCaseArea_use_case_names" ("AigfUseCaseArea_id");
CREATE INDEX "ix_AigfUseCaseArea_use_case_names_use_case_names" ON "AigfUseCaseArea_use_case_names" (use_case_names);
