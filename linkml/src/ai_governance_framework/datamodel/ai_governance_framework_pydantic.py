from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "v3"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'upstream_commit': {'tag': 'upstream_commit',
                                         'value': '67b8c3257695d5ede09d262798bf28a0e58d4740'},
                     'upstream_license': {'tag': 'upstream_license',
                                          'value': 'CC-BY-4.0'},
                     'upstream_release_date': {'tag': 'upstream_release_date',
                                               'value': '2026-10-26'}},
     'comments': ['FINOS tags no v3 release, so the version is the one '
                  'docs/_config.yml states and the source is the commit that '
                  'merged it. scripts/check_upstream_release.py reports a new tag, '
                  'or main changing a path this schema reads.',
                  'JSON Schema generation turns a hyphen in a slot name or an '
                  'alias into an underscore, so doc-status cannot be a key of the '
                  'generated schema, and a key named type would project as a false '
                  "rdf:type. Each slot that differs from FINOS's key lists that "
                  'key under aliases. scripts/build_catalogue.py renames by that '
                  "list and adds item_id and source_file, which FINOS's file name "
                  'states, and tests/test_upstream_tree.py shows that the renaming '
                  'is one to one. A reference file needs no renaming.'],
     'default_prefix': 'ai_governance_framework',
     'default_range': 'string',
     'description': 'A LinkML model of the FINOS AI Governance Framework: its '
                    'risks, mitigations and use cases, the reference files they '
                    'cite, and the data files beside them. Each class keeps '
                    "FINOS's keys and values, so FINOS's files are the test data.",
     'id': 'https://w3id.org/lmodel/ai-governance-framework',
     'imports': ['linkml:types'],
     'keywords': ['AI governance', 'AI risk', 'financial services', 'FINOS'],
     'license': 'Apache-2.0',
     'name': 'ai_governance_framework',
     'prefixes': {'ai_governance_framework': {'prefix_prefix': 'ai_governance_framework',
                                              'prefix_reference': 'https://w3id.org/lmodel/ai-governance-framework/'},
                  'airo': {'prefix_prefix': 'airo',
                           'prefix_reference': 'https://w3id.org/airo#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nexus': {'prefix_prefix': 'nexus',
                            'prefix_reference': 'https://w3id.org/ai-atlas-nexus/'},
                  'nist_ai_600_1': {'prefix_prefix': 'nist_ai_600_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-600-1/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://lmodel.github.io/ai-governance-framework',
                  'https://air-governance-framework.finos.org/',
                  'https://github.com/finos/ai-governance-framework'],
     'source': 'https://github.com/finos/ai-governance-framework/tree/67b8c3257695d5ede09d262798bf28a0e58d4740',
     'source_file': 'src/ai_governance_framework/schema/ai_governance_framework.yaml',
     'title': 'FINOS AI Governance Framework'} )

class AigfDocumentStatus(str, Enum):
    """
    How far a page has been approved, from document_status in docs/_config.yml.
    """
    Pre_Draft = "Pre-Draft"
    """
    Initial brainstorming or collection of ideas, notes, and outlines. The document is not yet formally written.
    """
    Draft = "Draft"
    """
    The document is in the early stages of development, with content being written and structured but not yet polished.
    """
    Working_Group_Approved = "Working-Group-Approved"
    """
    The document is in its final form and has been approved by the AIGF team.
    """
    Approved_Specification = "Approved-Specification"
    """
    The publication of an Approved Specification in a publicly accessible manner.
    """


class AigfRiskType(str, Enum):
    """
    A risk's group, from risk_type_labels in docs/_config.yml.
    """
    Regulatory_and_Compliance = "RC"
    Operational = "OP"
    Security = "SEC"


class AigfMitigationType(str, Enum):
    """
    A mitigation's group, from mitigation_type_labels in docs/_config.yml.
    """
    Preventative = "PREV"
    Detective = "DET"


class AigfRiskDomain(str, Enum):
    """
    A risk's domain, from risk_domain_labels in docs/_config.yml.
    """
    Components = "components"
    Inputs = "inputs"
    Leakage = "leakage"
    Accuracy = "accuracy"
    Alignment = "alignment"
    Agency = "agency"
    Vendor = "vendor"
    Liability = "liability"


class AigfMitigationDomain(str, Enum):
    """
    A mitigation's domain, from mitigation_domain_labels in docs/_config.yml.
    """
    Sourcing = "sourcing"
    Filtering = "filtering"
    Data = "data"
    Access = "access"
    Evaluation = "evaluation"
    Oversight = "oversight"
    Monitoring = "monitoring"


class AigfUseCaseCategory(str, Enum):
    """
    A use case's category, from usecase_categories in docs/_config.yml.
    """
    Customer_Experience_and_Engagement = "Customer_Experience_and_Engagement"
    Risk_Management_and_Compliance = "Risk_Management_and_Compliance"
    Operations_and_Process_Optimization = "Operations_and_Process_Optimization"
    Trading_and_Investment = "Trading_and_Investment"
    Data_Intelligence_and_Analytics = "Data_Intelligence_and_Analytics"
    Fraud_Detection_and_Security = "Fraud_Detection_and_Security"
    Risk_and_Compliance = "Risk_and_Compliance"
    """
    A category uc-3 and uc-4 use. docs/_config.yml does not list it, though docs/_data/ai_use_cases.yml has a domain of this name.
    """


class AigfSensitivity(str, Enum):
    """
    How sensitive a class of data is, as docs/_data/data_classification.yml grades it.
    """
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Critical = "Critical"


class AigfLens(str, Enum):
    """
    The question a reference file answers, from docs/_data/references/README.md.
    """
    threat = "threat"
    """
    What is this called elsewhere?
    """
    obligation = "obligation"
    """
    Which rule requires me to address it?
    """
    control = "control"
    """
    How do I implement and evidence it?
    """


class AigfDataHandling(str, Enum):
    """
    The options of the deployment model's data_handling axis.
    """
    Centralized = "Centralized"
    Federated = "Federated"
    Synthetic_Data = "Synthetic_Data"
    Privacy_Preserving = "Privacy_Preserving"



class AigfCatalogue(ConfiguredBaseModel):
    """
    One edition of the framework, as the facts FINOS's front matter and data files state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The bodies of the risk, mitigation and use case pages stay in '
                      "FINOS's files, which source_file names. The catalogue names "
                      "each reference file's entries by key and leaves their titles "
                      'there.'],
         'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'mitigations': {'name': 'mitigations', 'required': True},
                        'release_date': {'name': 'release_date', 'required': True},
                        'risks': {'name': 'risks', 'required': True},
                        'source_commit': {'name': 'source_commit', 'required': True},
                        'title': {'name': 'title', 'required': True},
                        'version': {'name': 'version', 'required': True}},
         'tree_root': True})

    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    version: str = Field(default=..., description="""The edition, as docs/_config.yml writes it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    release_date: date = Field(default=..., description="""The edition's date, as docs/_config.yml writes it.""", json_schema_extra = { "linkml_meta": {'aliases': ['release-date'], 'domain_of': ['AigfCatalogue']} })
    source_commit: str = Field(default=..., description="""The commit of FINOS's repository the catalogue was read from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    reference_lenses: Optional[list[AigfReferenceLens]] = Field(default=None, description="""The lenses docs/_config.yml configures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    reference_indexes: Optional[list[AigfReferenceIndex]] = Field(default=None, description="""The keys of each reference file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    risks: list[AigfRisk] = Field(default=..., description="""The risks of the edition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    mitigations: list[AigfMitigation] = Field(default=..., description="""The mitigations of the edition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    use_cases: Optional[list[AigfUseCase]] = Field(default=None, description="""The worked use cases of the edition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    financial_data_classification: Optional[list[AigfDataClassification]] = Field(default=None, description="""The classes of financial data docs/_data/data_classification.yml lists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    ai_use_cases: Optional[list[AigfUseCaseDomain]] = Field(default=None, description="""The use case taxonomy docs/_data/ai_use_cases.yml lists.""", json_schema_extra = { "linkml_meta": {'aliases': ['AI_use_cases'], 'domain_of': ['AigfCatalogue']} })
    cross_cutting_capabilities: Optional[list[str]] = Field(default=None, description="""The capabilities docs/_data/ai_use_cases.yml lists apart from the taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })
    ai_deployment_model_taxonomy: Optional[list[AigfDeploymentAxis]] = Field(default=None, description="""The axes docs/_data/ai_deployment_model.yml lists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue']} })

    @field_validator('source_commit')
    def pattern_source_commit(cls, v):
        pattern=re.compile(r"^[0-9a-f]{40}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid source_commit format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid source_commit format: {v}"
            raise ValueError(err_msg)
        return v


class AigfItem(ConfiguredBaseModel):
    """
    A page of the framework that its front matter describes and that others cite by identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    item_id: str = Field(default=..., description="""The page's identifier, which FINOS's file name starts with and other pages cite.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    sequence: int = Field(default=..., description="""The number in the page's identifier, which orders the pages.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    layout: str = Field(default=..., description="""The Jekyll layout that renders the page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    doc_status: AigfDocumentStatus = Field(default=..., description="""How far the page has been approved.""", json_schema_extra = { "linkml_meta": {'aliases': ['doc-status'], 'domain_of': ['AigfItem']} })
    source_file: str = Field(default=..., description="""The path of the page in FINOS's repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })


class AigfReferenceCitations(ConfiguredBaseModel):
    """
    The entries of FINOS's reference files that a page cites, one list for each file.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'mixin': True})

    atr_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/atr.yml.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceCitations']} })
    canada_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/canada-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['canada-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    eu_ai_act_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/eu-ai-act.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['eu-ai-act_references'], 'domain_of': ['AigfReferenceCitations']} })
    ffiec_itbooklets_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/ffiec-itbooklets.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['ffiec-itbooklets_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iosco_supervisory_toolkit_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iosco-supervisory-toolkit.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iosco-supervisory-toolkit_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iso_42001_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iso-42001.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iso-42001_references'], 'domain_of': ['AigfReferenceCitations']} })
    nist_ai_600_1_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-ai-600-1.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-ai-600-1_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_ai_600_1:Risk']} })
    nist_sp_800_53r5_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-sp-800-53r5.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-sp-800-53r5_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_sp_800_53:Control']} })
    owasp_asi_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-asi.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-asi_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_llm_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-llm.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-llm_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_ml_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-ml.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-ml_references'], 'domain_of': ['AigfReferenceCitations']} })
    sr11_7_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/sr11-7.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['sr11-7_references'], 'domain_of': ['AigfReferenceCitations']} })
    uk_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/uk-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['uk-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })


class AigfRisk(AigfReferenceCitations, AigfItem):
    """
    A risk the framework names, from a file under docs/_risks/.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['airo:Risk'],
         'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'mixins': ['AigfReferenceCitations'],
         'slot_usage': {'item_id': {'name': 'item_id', 'pattern': '^ri-[1-9][0-9]*$'},
                        'layout': {'equals_string': 'risk', 'name': 'layout'},
                        'source_file': {'name': 'source_file',
                                        'pattern': '^docs/_risks/ri-[1-9][0-9]*_[a-z0-9-]+[.]md$'}}})

    risk_type: AigfRiskType = Field(default=..., description="""The group a risk appears in.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'], 'domain_of': ['AigfRisk']} })
    risk_domain: AigfRiskDomain = Field(default=..., description="""The domain a risk belongs to.""", json_schema_extra = { "linkml_meta": {'aliases': ['domain'], 'domain_of': ['AigfRisk']} })
    related_risks: Optional[list[str]] = Field(default=None, description="""The risks a page relates to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfRisk', 'AigfUseCase']} })
    atr_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/atr.yml.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceCitations']} })
    canada_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/canada-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['canada-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    eu_ai_act_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/eu-ai-act.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['eu-ai-act_references'], 'domain_of': ['AigfReferenceCitations']} })
    ffiec_itbooklets_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/ffiec-itbooklets.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['ffiec-itbooklets_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iosco_supervisory_toolkit_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iosco-supervisory-toolkit.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iosco-supervisory-toolkit_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iso_42001_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iso-42001.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iso-42001_references'], 'domain_of': ['AigfReferenceCitations']} })
    nist_ai_600_1_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-ai-600-1.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-ai-600-1_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_ai_600_1:Risk']} })
    nist_sp_800_53r5_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-sp-800-53r5.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-sp-800-53r5_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_sp_800_53:Control']} })
    owasp_asi_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-asi.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-asi_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_llm_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-llm.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-llm_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_ml_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-ml.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-ml_references'], 'domain_of': ['AigfReferenceCitations']} })
    sr11_7_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/sr11-7.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['sr11-7_references'], 'domain_of': ['AigfReferenceCitations']} })
    uk_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/uk-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['uk-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    item_id: str = Field(default=..., description="""The page's identifier, which FINOS's file name starts with and other pages cite.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    sequence: int = Field(default=..., description="""The number in the page's identifier, which orders the pages.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    layout: Literal["risk"] = Field(default=..., description="""The Jekyll layout that renders the page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem'], 'equals_string': 'risk'} })
    doc_status: AigfDocumentStatus = Field(default=..., description="""How far the page has been approved.""", json_schema_extra = { "linkml_meta": {'aliases': ['doc-status'], 'domain_of': ['AigfItem']} })
    source_file: str = Field(default=..., description="""The path of the page in FINOS's repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })

    @field_validator('item_id')
    def pattern_item_id(cls, v):
        pattern=re.compile(r"^ri-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid item_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid item_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('source_file')
    def pattern_source_file(cls, v):
        pattern=re.compile(r"^docs/_risks/ri-[1-9][0-9]*_[a-z0-9-]+[.]md$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid source_file format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid source_file format: {v}"
            raise ValueError(err_msg)
        return v


class AigfMitigation(AigfReferenceCitations, AigfItem):
    """
    A mitigation the framework names, from a file under docs/_mitigations/.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['airo:RiskControl'],
         'comments': ['CONVENTIONS.md makes the link one way: a mitigation lists the '
                      'risks it mitigates, and a risk does not list its mitigations.'],
         'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'mixins': ['AigfReferenceCitations'],
         'related_mappings': ['nexus:Action'],
         'slot_usage': {'item_id': {'name': 'item_id', 'pattern': '^mi-[1-9][0-9]*$'},
                        'layout': {'equals_string': 'mitigation', 'name': 'layout'},
                        'source_file': {'name': 'source_file',
                                        'pattern': '^docs/_mitigations/mi-[1-9][0-9]*_[a-z0-9-]+[.]md$'}}})

    mitigation_type: AigfMitigationType = Field(default=..., description="""The group a mitigation appears in.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'], 'domain_of': ['AigfMitigation']} })
    mitigation_domain: AigfMitigationDomain = Field(default=..., description="""The domain a mitigation belongs to.""", json_schema_extra = { "linkml_meta": {'aliases': ['domain'], 'domain_of': ['AigfMitigation']} })
    mitigates: list[str] = Field(default=..., description="""The risks a mitigation addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfMitigation']} })
    related_mitigations: Optional[list[str]] = Field(default=None, description="""The mitigations a page relates to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfMitigation', 'AigfUseCase']} })
    atr_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/atr.yml.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceCitations']} })
    canada_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/canada-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['canada-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    eu_ai_act_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/eu-ai-act.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['eu-ai-act_references'], 'domain_of': ['AigfReferenceCitations']} })
    ffiec_itbooklets_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/ffiec-itbooklets.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['ffiec-itbooklets_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iosco_supervisory_toolkit_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iosco-supervisory-toolkit.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iosco-supervisory-toolkit_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iso_42001_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iso-42001.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iso-42001_references'], 'domain_of': ['AigfReferenceCitations']} })
    nist_ai_600_1_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-ai-600-1.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-ai-600-1_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_ai_600_1:Risk']} })
    nist_sp_800_53r5_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-sp-800-53r5.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-sp-800-53r5_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_sp_800_53:Control']} })
    owasp_asi_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-asi.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-asi_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_llm_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-llm.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-llm_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_ml_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-ml.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-ml_references'], 'domain_of': ['AigfReferenceCitations']} })
    sr11_7_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/sr11-7.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['sr11-7_references'], 'domain_of': ['AigfReferenceCitations']} })
    uk_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/uk-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['uk-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    item_id: str = Field(default=..., description="""The page's identifier, which FINOS's file name starts with and other pages cite.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    sequence: int = Field(default=..., description="""The number in the page's identifier, which orders the pages.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    layout: Literal["mitigation"] = Field(default=..., description="""The Jekyll layout that renders the page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem'], 'equals_string': 'mitigation'} })
    doc_status: AigfDocumentStatus = Field(default=..., description="""How far the page has been approved.""", json_schema_extra = { "linkml_meta": {'aliases': ['doc-status'], 'domain_of': ['AigfItem']} })
    source_file: str = Field(default=..., description="""The path of the page in FINOS's repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })

    @field_validator('item_id')
    def pattern_item_id(cls, v):
        pattern=re.compile(r"^mi-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid item_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid item_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('source_file')
    def pattern_source_file(cls, v):
        pattern=re.compile(r"^docs/_mitigations/mi-[1-9][0-9]*_[a-z0-9-]+[.]md$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid source_file format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid source_file format: {v}"
            raise ValueError(err_msg)
        return v


class AigfUseCase(AigfReferenceCitations, AigfItem):
    """
    A worked use case with its risks, mitigations and data, from a file under docs/_usecases/.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'mixins': ['AigfReferenceCitations'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'item_id': {'name': 'item_id', 'pattern': '^uc-[1-9][0-9]*$'},
                        'layout': {'equals_string': 'usecase', 'name': 'layout'},
                        'source_file': {'name': 'source_file',
                                        'pattern': '^docs/_usecases/uc-[1-9][0-9]*_[a-z0-9-]+[.]md$'}}})

    category: AigfUseCaseCategory = Field(default=..., description="""The category a use case is listed under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    description: str = Field(default=..., description="""FINOS's description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase',
                       'AigfDataClassification',
                       'AigfReferenceFile',
                       'AigfReferenceEntry',
                       'AigfDeploymentOption'],
         'slot_uri': 'schema:description'} })
    end_user: Optional[str] = Field(default=None, description="""Who uses the system the use case describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    business_value: Optional[str] = Field(default=None, description="""What the use case is worth to the business.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    related_risks: Optional[list[str]] = Field(default=None, description="""The risks a page relates to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfRisk', 'AigfUseCase']} })
    related_mitigations: Optional[list[str]] = Field(default=None, description="""The mitigations a page relates to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfMitigation', 'AigfUseCase']} })
    data_classifications: Optional[list[AigfDataClassificationUse]] = Field(default=None, description="""The data classifications a use case handles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    data_handling_aspects: Optional[list[AigfDataHandling]] = Field(default=None, description="""The options of the deployment model's data_handling axis a use case takes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    regulatory_concerns: Optional[list[AigfRegulatoryReference]] = Field(default=None, description="""The regulations a use case raises.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    further_reading: Optional[list[AigfFurtherReading]] = Field(default=None, description="""The papers and articles a use case points to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase']} })
    atr_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/atr.yml.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceCitations']} })
    canada_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/canada-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['canada-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    eu_ai_act_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/eu-ai-act.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['eu-ai-act_references'], 'domain_of': ['AigfReferenceCitations']} })
    ffiec_itbooklets_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/ffiec-itbooklets.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['ffiec-itbooklets_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iosco_supervisory_toolkit_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iosco-supervisory-toolkit.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iosco-supervisory-toolkit_references'],
         'domain_of': ['AigfReferenceCitations']} })
    iso_42001_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/iso-42001.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['iso-42001_references'], 'domain_of': ['AigfReferenceCitations']} })
    nist_ai_600_1_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-ai-600-1.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-ai-600-1_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_ai_600_1:Risk']} })
    nist_sp_800_53r5_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/nist-sp-800-53r5.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['nist-sp-800-53r5_references'],
         'domain_of': ['AigfReferenceCitations'],
         'related_mappings': ['nist_sp_800_53:Control']} })
    owasp_asi_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-asi.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-asi_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_llm_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-llm.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-llm_references'], 'domain_of': ['AigfReferenceCitations']} })
    owasp_ml_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/owasp-ml.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['owasp-ml_references'], 'domain_of': ['AigfReferenceCitations']} })
    sr11_7_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/sr11-7.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['sr11-7_references'], 'domain_of': ['AigfReferenceCitations']} })
    uk_regulations_references: Optional[list[str]] = Field(default=None, description="""Keys of docs/_data/references/uk-regulations.yml.""", json_schema_extra = { "linkml_meta": {'aliases': ['uk-regulations_references'],
         'domain_of': ['AigfReferenceCitations']} })
    item_id: str = Field(default=..., description="""The page's identifier, which FINOS's file name starts with and other pages cite.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    sequence: int = Field(default=..., description="""The number in the page's identifier, which orders the pages.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })
    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    layout: Literal["usecase"] = Field(default=..., description="""The Jekyll layout that renders the page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem'], 'equals_string': 'usecase'} })
    doc_status: AigfDocumentStatus = Field(default=..., description="""How far the page has been approved.""", json_schema_extra = { "linkml_meta": {'aliases': ['doc-status'], 'domain_of': ['AigfItem']} })
    source_file: str = Field(default=..., description="""The path of the page in FINOS's repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfItem']} })

    @field_validator('item_id')
    def pattern_item_id(cls, v):
        pattern=re.compile(r"^uc-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid item_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid item_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('source_file')
    def pattern_source_file(cls, v):
        pattern=re.compile(r"^docs/_usecases/uc-[1-9][0-9]*_[a-z0-9-]+[.]md$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid source_file format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid source_file format: {v}"
            raise ValueError(err_msg)
        return v


class AigfDataClassificationUse(ConfiguredBaseModel):
    """
    A data classification a use case handles, with the kinds of data it holds under it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'name': {'description': 'The name of a classification in '
                                                'docs/_data/data_classification.yml.',
                                 'name': 'name'}}})

    name: str = Field(default=..., description="""The name of a classification in docs/_data/data_classification.yml.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    data_types: Optional[list[str]] = Field(default=None, description="""The kinds of data a use case holds under one classification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse']} })


class AigfRegulatoryReference(ConfiguredBaseModel):
    """
    A regulation or guideline named by its title and address, with where it applies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework'})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    url: Optional[str] = Field(default=None, description="""The address of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfReferenceEntry']} })
    jurisdiction: Optional[str] = Field(default=None, description="""Where a regulation applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfRegulatoryReference']} })

    @field_validator('url')
    def pattern_url(cls, v):
        pattern=re.compile(r"^http")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid url format: {v}"
            raise ValueError(err_msg)
        return v


class AigfFurtherReading(ConfiguredBaseModel):
    """
    A paper or article a use case points to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework'})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    url: Optional[str] = Field(default=None, description="""The address of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfReferenceEntry']} })
    source: Optional[str] = Field(default=None, description="""Who published a paper or article.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfFurtherReading']} })

    @field_validator('url')
    def pattern_url(cls, v):
        pattern=re.compile(r"^http")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid url format: {v}"
            raise ValueError(err_msg)
        return v


class AigfDataClassification(ConfiguredBaseModel):
    """
    A class of financial data with its sensitivity and its handling, from docs/_data/data_classification.yml.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'sensitivity': {'name': 'sensitivity', 'required': True}}})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    sensitivity: AigfSensitivity = Field(default=..., description="""How sensitive a class of data is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassification']} })
    description: str = Field(default=..., description="""FINOS's description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase',
                       'AigfDataClassification',
                       'AigfReferenceFile',
                       'AigfReferenceEntry',
                       'AigfDeploymentOption'],
         'slot_uri': 'schema:description'} })
    examples: Optional[list[str]] = Field(default=None, description="""Kinds of data in a class.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassification']} })
    storage_location: Optional[str] = Field(default=None, description="""Where a class of data is held.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassification']} })
    regulations: Optional[str] = Field(default=None, description="""The regulations that apply to a class of data, written as FINOS writes them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassification']} })
    references: Optional[list[AigfRegulatoryReference]] = Field(default=None, description="""The regulations and guidelines a class of data cites.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassification']} })


class AigfReferenceLens(ConfiguredBaseModel):
    """
    How the site presents the reference files of one lens, from reference_lenses in docs/_config.yml.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'label': {'name': 'label', 'required': True},
                        'lens': {'name': 'lens', 'required': True},
                        'question': {'name': 'question', 'required': True}}})

    lens: AigfLens = Field(default=..., description="""Which question a reference file answers for a page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens', 'AigfReferenceFile', 'AigfReferenceIndex']} })
    label: str = Field(default=..., description="""The lens's display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens']} })
    question: str = Field(default=..., description="""The question the lens answers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens']} })
    icon: Optional[str] = Field(default=None, description="""The Bootstrap Icons class the site shows beside the lens.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens']} })
    color: Optional[str] = Field(default=None, description="""The Bootstrap theme colour the site gives the lens.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens']} })


class AigfReferenceFile(ConfiguredBaseModel):
    """
    One file under docs/_data/references/, which lists the citable entries of one regulation, framework or standard.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['These rules are the ones scripts/validate-references.py states, '
                      'except that superseded_by resolving within the file and entries '
                      'not being empty are held by tests/test_upstream_tree.py. No '
                      'generator writes either.'],
         'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'entries': {'name': 'entries', 'required': True},
                        'lens': {'name': 'lens', 'required': True},
                        'title': {'name': 'title', 'required': True}}})

    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., description="""FINOS's description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase',
                       'AigfDataClassification',
                       'AigfReferenceFile',
                       'AigfReferenceEntry',
                       'AigfDeploymentOption'],
         'slot_uri': 'schema:description'} })
    source_url: Optional[str] = Field(default=None, description="""The address the file was generated from, or a canonical index page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceFile']} })
    lens: AigfLens = Field(default=..., description="""Which question a reference file answers for a page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens', 'AigfReferenceFile', 'AigfReferenceIndex']} })
    entries: dict[str, AigfReferenceEntry] = Field(default=..., description="""The file's citable items, keyed by the key a page cites them by.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceFile']} })


class AigfReferenceEntry(ConfiguredBaseModel):
    """
    One citable item of a reference file, under the key a page cites it by.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'title': {'name': 'title', 'required': True},
                        'url': {'name': 'url', 'required': True}}})

    reference_key: str = Field(default=..., description="""The stable key a page cites the entry by.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceEntry']} })
    title: str = Field(default=..., description="""The name FINOS gives the page, file or framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfCatalogue',
                       'AigfItem',
                       'AigfReferenceFile',
                       'AigfReferenceEntry'],
         'slot_uri': 'schema:name'} })
    url: str = Field(default=..., description="""The address of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfReferenceEntry']} })
    description: Optional[str] = Field(default=None, description="""FINOS's description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase',
                       'AigfDataClassification',
                       'AigfReferenceFile',
                       'AigfReferenceEntry',
                       'AigfDeploymentOption'],
         'slot_uri': 'schema:description'} })
    issuer: Optional[str] = Field(default=None, description="""The body that issued the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceEntry']} })
    booklet_abbrev: Optional[str] = Field(default=None, description="""The abbreviation of the FFIEC booklet the entry belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceEntry']} })
    superseded_by: Optional[str] = Field(default=None, description="""The key of the entry in the same file that replaces this one in a newer edition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceEntry']} })

    @field_validator('url')
    def pattern_url(cls, v):
        pattern=re.compile(r"^http")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid url format: {v}"
            raise ValueError(err_msg)
        return v


class AigfReferenceIndex(ConfiguredBaseModel):
    """
    The keys one reference file holds, so that a catalogue's citations resolve within it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework',
         'slot_usage': {'lens': {'name': 'lens', 'required': True}}})

    reference_file: str = Field(default=..., description="""The reference file's stem.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceIndex']} })
    lens: AigfLens = Field(default=..., description="""Which question a reference file answers for a page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceLens', 'AigfReferenceFile', 'AigfReferenceIndex']} })
    entry_keys: Optional[list[str]] = Field(default=None, description="""The keys the reference file holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfReferenceIndex']} })


class AigfUseCaseDomain(ConfiguredBaseModel):
    """
    A top level of the use case taxonomy in docs/_data/ai_use_cases.yml.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework'})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    use_case_areas: Optional[list[AigfUseCaseArea]] = Field(default=None, description="""The areas under a domain.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCaseDomain']} })


class AigfUseCaseArea(ConfiguredBaseModel):
    """
    A second level of the use case taxonomy, with the use cases under it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework'})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    use_case_names: Optional[list[str]] = Field(default=None, description="""The use cases under an area, as the taxonomy names them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCaseArea']} })


class AigfDeploymentAxis(ConfiguredBaseModel):
    """
    One axis of the deployment model taxonomy in docs/_data/ai_deployment_model.yml.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework'})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    options: Optional[list[AigfDeploymentOption]] = Field(default=None, description="""The options on an axis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDeploymentAxis']} })


class AigfDeploymentOption(ConfiguredBaseModel):
    """
    One option on an axis of the deployment model taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/ai-governance-framework'})

    name: str = Field(default=..., description="""The name FINOS gives the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfDataClassificationUse',
                       'AigfRegulatoryReference',
                       'AigfFurtherReading',
                       'AigfDataClassification',
                       'AigfUseCaseDomain',
                       'AigfUseCaseArea',
                       'AigfDeploymentAxis',
                       'AigfDeploymentOption']} })
    description: Optional[str] = Field(default=None, description="""FINOS's description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AigfUseCase',
                       'AigfDataClassification',
                       'AigfReferenceFile',
                       'AigfReferenceEntry',
                       'AigfDeploymentOption'],
         'slot_uri': 'schema:description'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AigfCatalogue.model_rebuild()
AigfItem.model_rebuild()
AigfReferenceCitations.model_rebuild()
AigfRisk.model_rebuild()
AigfMitigation.model_rebuild()
AigfUseCase.model_rebuild()
AigfDataClassificationUse.model_rebuild()
AigfRegulatoryReference.model_rebuild()
AigfFurtherReading.model_rebuild()
AigfDataClassification.model_rebuild()
AigfReferenceLens.model_rebuild()
AigfReferenceFile.model_rebuild()
AigfReferenceEntry.model_rebuild()
AigfReferenceIndex.model_rebuild()
AigfUseCaseDomain.model_rebuild()
AigfUseCaseArea.model_rebuild()
AigfDeploymentAxis.model_rebuild()
AigfDeploymentOption.model_rebuild()
