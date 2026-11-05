# Auto generated from ai_governance_framework.yaml by pythongen.py version: 0.0.1
# Schema: ai_governance_framework
#
# id: https://w3id.org/lmodel/ai-governance-framework
# description: A LinkML model of the FINOS AI Governance Framework: its risks, mitigations and use cases, the reference files they cite, and the data files beside them. Each class keeps FINOS's keys and values, so FINOS's files are the test data.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.12.0"
version = "v3"

# Namespaces
AI_GOVERNANCE_FRAMEWORK = CurieNamespace('ai_governance_framework', 'https://w3id.org/lmodel/ai-governance-framework/')
AIRO = CurieNamespace('airo', 'https://w3id.org/airo#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NEXUS = CurieNamespace('nexus', 'https://w3id.org/ai-atlas-nexus/')
NIST_AI_600_1 = CurieNamespace('nist_ai_600_1', 'https://w3id.org/lmodel/nist-ai-600-1/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = AI_GOVERNANCE_FRAMEWORK


# Types

# Class references
class AigfItemItemId(extended_str):
    pass


class AigfRiskItemId(AigfItemItemId):
    pass


class AigfMitigationItemId(AigfItemItemId):
    pass


class AigfUseCaseItemId(AigfItemItemId):
    pass


class AigfReferenceEntryReferenceKey(extended_str):
    pass


@dataclass(repr=False)
class AigfCatalogue(YAMLRoot):
    """
    One edition of the framework, as the facts FINOS's front matter and data files state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfCatalogue"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfCatalogue"
    class_name: ClassVar[str] = "AigfCatalogue"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfCatalogue

    title: str = None
    version: str = None
    release_date: Union[str, XSDDate] = None
    source_commit: str = None
    risks: Union[dict[Union[str, AigfRiskItemId], Union[dict, "AigfRisk"]], list[Union[dict, "AigfRisk"]]] = empty_dict()
    mitigations: Union[dict[Union[str, AigfMitigationItemId], Union[dict, "AigfMitigation"]], list[Union[dict, "AigfMitigation"]]] = empty_dict()
    reference_lenses: Optional[Union[Union[dict, "AigfReferenceLens"], list[Union[dict, "AigfReferenceLens"]]]] = empty_list()
    reference_indexes: Optional[Union[Union[dict, "AigfReferenceIndex"], list[Union[dict, "AigfReferenceIndex"]]]] = empty_list()
    use_cases: Optional[Union[dict[Union[str, AigfUseCaseItemId], Union[dict, "AigfUseCase"]], list[Union[dict, "AigfUseCase"]]]] = empty_dict()
    financial_data_classification: Optional[Union[Union[dict, "AigfDataClassification"], list[Union[dict, "AigfDataClassification"]]]] = empty_list()
    ai_use_cases: Optional[Union[Union[dict, "AigfUseCaseDomain"], list[Union[dict, "AigfUseCaseDomain"]]]] = empty_list()
    cross_cutting_capabilities: Optional[Union[str, list[str]]] = empty_list()
    ai_deployment_model_taxonomy: Optional[Union[Union[dict, "AigfDeploymentAxis"], list[Union[dict, "AigfDeploymentAxis"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.release_date):
            self.MissingRequiredField("release_date")
        if not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self._is_empty(self.source_commit):
            self.MissingRequiredField("source_commit")
        if not isinstance(self.source_commit, str):
            self.source_commit = str(self.source_commit)

        if self._is_empty(self.risks):
            self.MissingRequiredField("risks")
        self._normalize_inlined_as_list(slot_name="risks", slot_type=AigfRisk, key_name="item_id", keyed=True)

        if self._is_empty(self.mitigations):
            self.MissingRequiredField("mitigations")
        self._normalize_inlined_as_list(slot_name="mitigations", slot_type=AigfMitigation, key_name="item_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="reference_lenses", slot_type=AigfReferenceLens, key_name="lens", keyed=False)

        self._normalize_inlined_as_list(slot_name="reference_indexes", slot_type=AigfReferenceIndex, key_name="reference_file", keyed=False)

        self._normalize_inlined_as_list(slot_name="use_cases", slot_type=AigfUseCase, key_name="item_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="financial_data_classification", slot_type=AigfDataClassification, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_use_cases", slot_type=AigfUseCaseDomain, key_name="name", keyed=False)

        if not isinstance(self.cross_cutting_capabilities, list):
            self.cross_cutting_capabilities = [self.cross_cutting_capabilities] if self.cross_cutting_capabilities is not None else []
        self.cross_cutting_capabilities = [v if isinstance(v, str) else str(v) for v in self.cross_cutting_capabilities]

        self._normalize_inlined_as_list(slot_name="ai_deployment_model_taxonomy", slot_type=AigfDeploymentAxis, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfItem(YAMLRoot):
    """
    A page of the framework that its front matter describes and that others cite by identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfItem"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfItem"
    class_name: ClassVar[str] = "AigfItem"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfItem

    item_id: Union[str, AigfItemItemId] = None
    sequence: int = None
    title: str = None
    layout: str = None
    doc_status: Union[str, "AigfDocumentStatus"] = None
    source_file: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.item_id):
            self.MissingRequiredField("item_id")
        if not isinstance(self.item_id, AigfItemItemId):
            self.item_id = AigfItemItemId(self.item_id)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, int):
            self.sequence = int(self.sequence)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.layout):
            self.MissingRequiredField("layout")
        if not isinstance(self.layout, str):
            self.layout = str(self.layout)

        if self._is_empty(self.doc_status):
            self.MissingRequiredField("doc_status")
        if not isinstance(self.doc_status, AigfDocumentStatus):
            self.doc_status = AigfDocumentStatus(self.doc_status)

        if self._is_empty(self.source_file):
            self.MissingRequiredField("source_file")
        if not isinstance(self.source_file, str):
            self.source_file = str(self.source_file)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfReferenceCitations(YAMLRoot):
    """
    The entries of FINOS's reference files that a page cites, one list for each file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfReferenceCitations"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfReferenceCitations"
    class_name: ClassVar[str] = "AigfReferenceCitations"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfReferenceCitations

    atr_references: Optional[Union[str, list[str]]] = empty_list()
    canada_regulations_references: Optional[Union[str, list[str]]] = empty_list()
    eu_ai_act_references: Optional[Union[str, list[str]]] = empty_list()
    ffiec_itbooklets_references: Optional[Union[str, list[str]]] = empty_list()
    iosco_supervisory_toolkit_references: Optional[Union[str, list[str]]] = empty_list()
    iso_42001_references: Optional[Union[str, list[str]]] = empty_list()
    nist_ai_600_1_references: Optional[Union[str, list[str]]] = empty_list()
    nist_sp_800_53r5_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_asi_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_llm_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_ml_references: Optional[Union[str, list[str]]] = empty_list()
    sr11_7_references: Optional[Union[str, list[str]]] = empty_list()
    uk_regulations_references: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.atr_references, list):
            self.atr_references = [self.atr_references] if self.atr_references is not None else []
        self.atr_references = [v if isinstance(v, str) else str(v) for v in self.atr_references]

        if not isinstance(self.canada_regulations_references, list):
            self.canada_regulations_references = [self.canada_regulations_references] if self.canada_regulations_references is not None else []
        self.canada_regulations_references = [v if isinstance(v, str) else str(v) for v in self.canada_regulations_references]

        if not isinstance(self.eu_ai_act_references, list):
            self.eu_ai_act_references = [self.eu_ai_act_references] if self.eu_ai_act_references is not None else []
        self.eu_ai_act_references = [v if isinstance(v, str) else str(v) for v in self.eu_ai_act_references]

        if not isinstance(self.ffiec_itbooklets_references, list):
            self.ffiec_itbooklets_references = [self.ffiec_itbooklets_references] if self.ffiec_itbooklets_references is not None else []
        self.ffiec_itbooklets_references = [v if isinstance(v, str) else str(v) for v in self.ffiec_itbooklets_references]

        if not isinstance(self.iosco_supervisory_toolkit_references, list):
            self.iosco_supervisory_toolkit_references = [self.iosco_supervisory_toolkit_references] if self.iosco_supervisory_toolkit_references is not None else []
        self.iosco_supervisory_toolkit_references = [v if isinstance(v, str) else str(v) for v in self.iosco_supervisory_toolkit_references]

        if not isinstance(self.iso_42001_references, list):
            self.iso_42001_references = [self.iso_42001_references] if self.iso_42001_references is not None else []
        self.iso_42001_references = [v if isinstance(v, str) else str(v) for v in self.iso_42001_references]

        if not isinstance(self.nist_ai_600_1_references, list):
            self.nist_ai_600_1_references = [self.nist_ai_600_1_references] if self.nist_ai_600_1_references is not None else []
        self.nist_ai_600_1_references = [v if isinstance(v, str) else str(v) for v in self.nist_ai_600_1_references]

        if not isinstance(self.nist_sp_800_53r5_references, list):
            self.nist_sp_800_53r5_references = [self.nist_sp_800_53r5_references] if self.nist_sp_800_53r5_references is not None else []
        self.nist_sp_800_53r5_references = [v if isinstance(v, str) else str(v) for v in self.nist_sp_800_53r5_references]

        if not isinstance(self.owasp_asi_references, list):
            self.owasp_asi_references = [self.owasp_asi_references] if self.owasp_asi_references is not None else []
        self.owasp_asi_references = [v if isinstance(v, str) else str(v) for v in self.owasp_asi_references]

        if not isinstance(self.owasp_llm_references, list):
            self.owasp_llm_references = [self.owasp_llm_references] if self.owasp_llm_references is not None else []
        self.owasp_llm_references = [v if isinstance(v, str) else str(v) for v in self.owasp_llm_references]

        if not isinstance(self.owasp_ml_references, list):
            self.owasp_ml_references = [self.owasp_ml_references] if self.owasp_ml_references is not None else []
        self.owasp_ml_references = [v if isinstance(v, str) else str(v) for v in self.owasp_ml_references]

        if not isinstance(self.sr11_7_references, list):
            self.sr11_7_references = [self.sr11_7_references] if self.sr11_7_references is not None else []
        self.sr11_7_references = [v if isinstance(v, str) else str(v) for v in self.sr11_7_references]

        if not isinstance(self.uk_regulations_references, list):
            self.uk_regulations_references = [self.uk_regulations_references] if self.uk_regulations_references is not None else []
        self.uk_regulations_references = [v if isinstance(v, str) else str(v) for v in self.uk_regulations_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfRisk(AigfItem):
    """
    A risk the framework names, from a file under docs/_risks/.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfRisk"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfRisk"
    class_name: ClassVar[str] = "AigfRisk"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfRisk

    item_id: Union[str, AigfRiskItemId] = None
    sequence: int = None
    title: str = None
    doc_status: Union[str, "AigfDocumentStatus"] = None
    risk_type: Union[str, "AigfRiskType"] = None
    risk_domain: Union[str, "AigfRiskDomain"] = None
    layout: str = None
    source_file: str = None
    related_risks: Optional[Union[Union[str, AigfRiskItemId], list[Union[str, AigfRiskItemId]]]] = empty_list()
    atr_references: Optional[Union[str, list[str]]] = empty_list()
    canada_regulations_references: Optional[Union[str, list[str]]] = empty_list()
    eu_ai_act_references: Optional[Union[str, list[str]]] = empty_list()
    ffiec_itbooklets_references: Optional[Union[str, list[str]]] = empty_list()
    iosco_supervisory_toolkit_references: Optional[Union[str, list[str]]] = empty_list()
    iso_42001_references: Optional[Union[str, list[str]]] = empty_list()
    nist_ai_600_1_references: Optional[Union[str, list[str]]] = empty_list()
    nist_sp_800_53r5_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_asi_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_llm_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_ml_references: Optional[Union[str, list[str]]] = empty_list()
    sr11_7_references: Optional[Union[str, list[str]]] = empty_list()
    uk_regulations_references: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.item_id):
            self.MissingRequiredField("item_id")
        if not isinstance(self.item_id, AigfRiskItemId):
            self.item_id = AigfRiskItemId(self.item_id)

        if self._is_empty(self.risk_type):
            self.MissingRequiredField("risk_type")
        if not isinstance(self.risk_type, AigfRiskType):
            self.risk_type = AigfRiskType(self.risk_type)

        if self._is_empty(self.risk_domain):
            self.MissingRequiredField("risk_domain")
        if not isinstance(self.risk_domain, AigfRiskDomain):
            self.risk_domain = AigfRiskDomain(self.risk_domain)

        if self._is_empty(self.layout):
            self.MissingRequiredField("layout")
        if not isinstance(self.layout, str):
            self.layout = str(self.layout)

        if self._is_empty(self.source_file):
            self.MissingRequiredField("source_file")
        if not isinstance(self.source_file, str):
            self.source_file = str(self.source_file)

        if not isinstance(self.related_risks, list):
            self.related_risks = [self.related_risks] if self.related_risks is not None else []
        self.related_risks = [v if isinstance(v, AigfRiskItemId) else AigfRiskItemId(v) for v in self.related_risks]

        if not isinstance(self.atr_references, list):
            self.atr_references = [self.atr_references] if self.atr_references is not None else []
        self.atr_references = [v if isinstance(v, str) else str(v) for v in self.atr_references]

        if not isinstance(self.canada_regulations_references, list):
            self.canada_regulations_references = [self.canada_regulations_references] if self.canada_regulations_references is not None else []
        self.canada_regulations_references = [v if isinstance(v, str) else str(v) for v in self.canada_regulations_references]

        if not isinstance(self.eu_ai_act_references, list):
            self.eu_ai_act_references = [self.eu_ai_act_references] if self.eu_ai_act_references is not None else []
        self.eu_ai_act_references = [v if isinstance(v, str) else str(v) for v in self.eu_ai_act_references]

        if not isinstance(self.ffiec_itbooklets_references, list):
            self.ffiec_itbooklets_references = [self.ffiec_itbooklets_references] if self.ffiec_itbooklets_references is not None else []
        self.ffiec_itbooklets_references = [v if isinstance(v, str) else str(v) for v in self.ffiec_itbooklets_references]

        if not isinstance(self.iosco_supervisory_toolkit_references, list):
            self.iosco_supervisory_toolkit_references = [self.iosco_supervisory_toolkit_references] if self.iosco_supervisory_toolkit_references is not None else []
        self.iosco_supervisory_toolkit_references = [v if isinstance(v, str) else str(v) for v in self.iosco_supervisory_toolkit_references]

        if not isinstance(self.iso_42001_references, list):
            self.iso_42001_references = [self.iso_42001_references] if self.iso_42001_references is not None else []
        self.iso_42001_references = [v if isinstance(v, str) else str(v) for v in self.iso_42001_references]

        if not isinstance(self.nist_ai_600_1_references, list):
            self.nist_ai_600_1_references = [self.nist_ai_600_1_references] if self.nist_ai_600_1_references is not None else []
        self.nist_ai_600_1_references = [v if isinstance(v, str) else str(v) for v in self.nist_ai_600_1_references]

        if not isinstance(self.nist_sp_800_53r5_references, list):
            self.nist_sp_800_53r5_references = [self.nist_sp_800_53r5_references] if self.nist_sp_800_53r5_references is not None else []
        self.nist_sp_800_53r5_references = [v if isinstance(v, str) else str(v) for v in self.nist_sp_800_53r5_references]

        if not isinstance(self.owasp_asi_references, list):
            self.owasp_asi_references = [self.owasp_asi_references] if self.owasp_asi_references is not None else []
        self.owasp_asi_references = [v if isinstance(v, str) else str(v) for v in self.owasp_asi_references]

        if not isinstance(self.owasp_llm_references, list):
            self.owasp_llm_references = [self.owasp_llm_references] if self.owasp_llm_references is not None else []
        self.owasp_llm_references = [v if isinstance(v, str) else str(v) for v in self.owasp_llm_references]

        if not isinstance(self.owasp_ml_references, list):
            self.owasp_ml_references = [self.owasp_ml_references] if self.owasp_ml_references is not None else []
        self.owasp_ml_references = [v if isinstance(v, str) else str(v) for v in self.owasp_ml_references]

        if not isinstance(self.sr11_7_references, list):
            self.sr11_7_references = [self.sr11_7_references] if self.sr11_7_references is not None else []
        self.sr11_7_references = [v if isinstance(v, str) else str(v) for v in self.sr11_7_references]

        if not isinstance(self.uk_regulations_references, list):
            self.uk_regulations_references = [self.uk_regulations_references] if self.uk_regulations_references is not None else []
        self.uk_regulations_references = [v if isinstance(v, str) else str(v) for v in self.uk_regulations_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfMitigation(AigfItem):
    """
    A mitigation the framework names, from a file under docs/_mitigations/.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfMitigation"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfMitigation"
    class_name: ClassVar[str] = "AigfMitigation"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfMitigation

    item_id: Union[str, AigfMitigationItemId] = None
    sequence: int = None
    title: str = None
    doc_status: Union[str, "AigfDocumentStatus"] = None
    mitigation_type: Union[str, "AigfMitigationType"] = None
    mitigation_domain: Union[str, "AigfMitigationDomain"] = None
    mitigates: Union[Union[str, AigfRiskItemId], list[Union[str, AigfRiskItemId]]] = None
    layout: str = None
    source_file: str = None
    related_mitigations: Optional[Union[Union[str, AigfMitigationItemId], list[Union[str, AigfMitigationItemId]]]] = empty_list()
    atr_references: Optional[Union[str, list[str]]] = empty_list()
    canada_regulations_references: Optional[Union[str, list[str]]] = empty_list()
    eu_ai_act_references: Optional[Union[str, list[str]]] = empty_list()
    ffiec_itbooklets_references: Optional[Union[str, list[str]]] = empty_list()
    iosco_supervisory_toolkit_references: Optional[Union[str, list[str]]] = empty_list()
    iso_42001_references: Optional[Union[str, list[str]]] = empty_list()
    nist_ai_600_1_references: Optional[Union[str, list[str]]] = empty_list()
    nist_sp_800_53r5_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_asi_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_llm_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_ml_references: Optional[Union[str, list[str]]] = empty_list()
    sr11_7_references: Optional[Union[str, list[str]]] = empty_list()
    uk_regulations_references: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.item_id):
            self.MissingRequiredField("item_id")
        if not isinstance(self.item_id, AigfMitigationItemId):
            self.item_id = AigfMitigationItemId(self.item_id)

        if self._is_empty(self.mitigation_type):
            self.MissingRequiredField("mitigation_type")
        if not isinstance(self.mitigation_type, AigfMitigationType):
            self.mitigation_type = AigfMitigationType(self.mitigation_type)

        if self._is_empty(self.mitigation_domain):
            self.MissingRequiredField("mitigation_domain")
        if not isinstance(self.mitigation_domain, AigfMitigationDomain):
            self.mitigation_domain = AigfMitigationDomain(self.mitigation_domain)

        if self._is_empty(self.mitigates):
            self.MissingRequiredField("mitigates")
        if not isinstance(self.mitigates, list):
            self.mitigates = [self.mitigates] if self.mitigates is not None else []
        self.mitigates = [v if isinstance(v, AigfRiskItemId) else AigfRiskItemId(v) for v in self.mitigates]

        if self._is_empty(self.layout):
            self.MissingRequiredField("layout")
        if not isinstance(self.layout, str):
            self.layout = str(self.layout)

        if self._is_empty(self.source_file):
            self.MissingRequiredField("source_file")
        if not isinstance(self.source_file, str):
            self.source_file = str(self.source_file)

        if not isinstance(self.related_mitigations, list):
            self.related_mitigations = [self.related_mitigations] if self.related_mitigations is not None else []
        self.related_mitigations = [v if isinstance(v, AigfMitigationItemId) else AigfMitigationItemId(v) for v in self.related_mitigations]

        if not isinstance(self.atr_references, list):
            self.atr_references = [self.atr_references] if self.atr_references is not None else []
        self.atr_references = [v if isinstance(v, str) else str(v) for v in self.atr_references]

        if not isinstance(self.canada_regulations_references, list):
            self.canada_regulations_references = [self.canada_regulations_references] if self.canada_regulations_references is not None else []
        self.canada_regulations_references = [v if isinstance(v, str) else str(v) for v in self.canada_regulations_references]

        if not isinstance(self.eu_ai_act_references, list):
            self.eu_ai_act_references = [self.eu_ai_act_references] if self.eu_ai_act_references is not None else []
        self.eu_ai_act_references = [v if isinstance(v, str) else str(v) for v in self.eu_ai_act_references]

        if not isinstance(self.ffiec_itbooklets_references, list):
            self.ffiec_itbooklets_references = [self.ffiec_itbooklets_references] if self.ffiec_itbooklets_references is not None else []
        self.ffiec_itbooklets_references = [v if isinstance(v, str) else str(v) for v in self.ffiec_itbooklets_references]

        if not isinstance(self.iosco_supervisory_toolkit_references, list):
            self.iosco_supervisory_toolkit_references = [self.iosco_supervisory_toolkit_references] if self.iosco_supervisory_toolkit_references is not None else []
        self.iosco_supervisory_toolkit_references = [v if isinstance(v, str) else str(v) for v in self.iosco_supervisory_toolkit_references]

        if not isinstance(self.iso_42001_references, list):
            self.iso_42001_references = [self.iso_42001_references] if self.iso_42001_references is not None else []
        self.iso_42001_references = [v if isinstance(v, str) else str(v) for v in self.iso_42001_references]

        if not isinstance(self.nist_ai_600_1_references, list):
            self.nist_ai_600_1_references = [self.nist_ai_600_1_references] if self.nist_ai_600_1_references is not None else []
        self.nist_ai_600_1_references = [v if isinstance(v, str) else str(v) for v in self.nist_ai_600_1_references]

        if not isinstance(self.nist_sp_800_53r5_references, list):
            self.nist_sp_800_53r5_references = [self.nist_sp_800_53r5_references] if self.nist_sp_800_53r5_references is not None else []
        self.nist_sp_800_53r5_references = [v if isinstance(v, str) else str(v) for v in self.nist_sp_800_53r5_references]

        if not isinstance(self.owasp_asi_references, list):
            self.owasp_asi_references = [self.owasp_asi_references] if self.owasp_asi_references is not None else []
        self.owasp_asi_references = [v if isinstance(v, str) else str(v) for v in self.owasp_asi_references]

        if not isinstance(self.owasp_llm_references, list):
            self.owasp_llm_references = [self.owasp_llm_references] if self.owasp_llm_references is not None else []
        self.owasp_llm_references = [v if isinstance(v, str) else str(v) for v in self.owasp_llm_references]

        if not isinstance(self.owasp_ml_references, list):
            self.owasp_ml_references = [self.owasp_ml_references] if self.owasp_ml_references is not None else []
        self.owasp_ml_references = [v if isinstance(v, str) else str(v) for v in self.owasp_ml_references]

        if not isinstance(self.sr11_7_references, list):
            self.sr11_7_references = [self.sr11_7_references] if self.sr11_7_references is not None else []
        self.sr11_7_references = [v if isinstance(v, str) else str(v) for v in self.sr11_7_references]

        if not isinstance(self.uk_regulations_references, list):
            self.uk_regulations_references = [self.uk_regulations_references] if self.uk_regulations_references is not None else []
        self.uk_regulations_references = [v if isinstance(v, str) else str(v) for v in self.uk_regulations_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfUseCase(AigfItem):
    """
    A worked use case with its risks, mitigations and data, from a file under docs/_usecases/.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfUseCase"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfUseCase"
    class_name: ClassVar[str] = "AigfUseCase"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfUseCase

    item_id: Union[str, AigfUseCaseItemId] = None
    sequence: int = None
    title: str = None
    doc_status: Union[str, "AigfDocumentStatus"] = None
    category: Union[str, "AigfUseCaseCategory"] = None
    description: str = None
    layout: str = None
    source_file: str = None
    end_user: Optional[str] = None
    business_value: Optional[str] = None
    related_risks: Optional[Union[Union[str, AigfRiskItemId], list[Union[str, AigfRiskItemId]]]] = empty_list()
    related_mitigations: Optional[Union[Union[str, AigfMitigationItemId], list[Union[str, AigfMitigationItemId]]]] = empty_list()
    data_classifications: Optional[Union[Union[dict, "AigfDataClassificationUse"], list[Union[dict, "AigfDataClassificationUse"]]]] = empty_list()
    data_handling_aspects: Optional[Union[Union[str, "AigfDataHandling"], list[Union[str, "AigfDataHandling"]]]] = empty_list()
    regulatory_concerns: Optional[Union[Union[dict, "AigfRegulatoryReference"], list[Union[dict, "AigfRegulatoryReference"]]]] = empty_list()
    further_reading: Optional[Union[Union[dict, "AigfFurtherReading"], list[Union[dict, "AigfFurtherReading"]]]] = empty_list()
    atr_references: Optional[Union[str, list[str]]] = empty_list()
    canada_regulations_references: Optional[Union[str, list[str]]] = empty_list()
    eu_ai_act_references: Optional[Union[str, list[str]]] = empty_list()
    ffiec_itbooklets_references: Optional[Union[str, list[str]]] = empty_list()
    iosco_supervisory_toolkit_references: Optional[Union[str, list[str]]] = empty_list()
    iso_42001_references: Optional[Union[str, list[str]]] = empty_list()
    nist_ai_600_1_references: Optional[Union[str, list[str]]] = empty_list()
    nist_sp_800_53r5_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_asi_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_llm_references: Optional[Union[str, list[str]]] = empty_list()
    owasp_ml_references: Optional[Union[str, list[str]]] = empty_list()
    sr11_7_references: Optional[Union[str, list[str]]] = empty_list()
    uk_regulations_references: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.item_id):
            self.MissingRequiredField("item_id")
        if not isinstance(self.item_id, AigfUseCaseItemId):
            self.item_id = AigfUseCaseItemId(self.item_id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, AigfUseCaseCategory):
            self.category = AigfUseCaseCategory(self.category)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.layout):
            self.MissingRequiredField("layout")
        if not isinstance(self.layout, str):
            self.layout = str(self.layout)

        if self._is_empty(self.source_file):
            self.MissingRequiredField("source_file")
        if not isinstance(self.source_file, str):
            self.source_file = str(self.source_file)

        if self.end_user is not None and not isinstance(self.end_user, str):
            self.end_user = str(self.end_user)

        if self.business_value is not None and not isinstance(self.business_value, str):
            self.business_value = str(self.business_value)

        if not isinstance(self.related_risks, list):
            self.related_risks = [self.related_risks] if self.related_risks is not None else []
        self.related_risks = [v if isinstance(v, AigfRiskItemId) else AigfRiskItemId(v) for v in self.related_risks]

        if not isinstance(self.related_mitigations, list):
            self.related_mitigations = [self.related_mitigations] if self.related_mitigations is not None else []
        self.related_mitigations = [v if isinstance(v, AigfMitigationItemId) else AigfMitigationItemId(v) for v in self.related_mitigations]

        self._normalize_inlined_as_list(slot_name="data_classifications", slot_type=AigfDataClassificationUse, key_name="name", keyed=False)

        if not isinstance(self.data_handling_aspects, list):
            self.data_handling_aspects = [self.data_handling_aspects] if self.data_handling_aspects is not None else []
        self.data_handling_aspects = [v if isinstance(v, AigfDataHandling) else AigfDataHandling(v) for v in self.data_handling_aspects]

        self._normalize_inlined_as_list(slot_name="regulatory_concerns", slot_type=AigfRegulatoryReference, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="further_reading", slot_type=AigfFurtherReading, key_name="name", keyed=False)

        if not isinstance(self.atr_references, list):
            self.atr_references = [self.atr_references] if self.atr_references is not None else []
        self.atr_references = [v if isinstance(v, str) else str(v) for v in self.atr_references]

        if not isinstance(self.canada_regulations_references, list):
            self.canada_regulations_references = [self.canada_regulations_references] if self.canada_regulations_references is not None else []
        self.canada_regulations_references = [v if isinstance(v, str) else str(v) for v in self.canada_regulations_references]

        if not isinstance(self.eu_ai_act_references, list):
            self.eu_ai_act_references = [self.eu_ai_act_references] if self.eu_ai_act_references is not None else []
        self.eu_ai_act_references = [v if isinstance(v, str) else str(v) for v in self.eu_ai_act_references]

        if not isinstance(self.ffiec_itbooklets_references, list):
            self.ffiec_itbooklets_references = [self.ffiec_itbooklets_references] if self.ffiec_itbooklets_references is not None else []
        self.ffiec_itbooklets_references = [v if isinstance(v, str) else str(v) for v in self.ffiec_itbooklets_references]

        if not isinstance(self.iosco_supervisory_toolkit_references, list):
            self.iosco_supervisory_toolkit_references = [self.iosco_supervisory_toolkit_references] if self.iosco_supervisory_toolkit_references is not None else []
        self.iosco_supervisory_toolkit_references = [v if isinstance(v, str) else str(v) for v in self.iosco_supervisory_toolkit_references]

        if not isinstance(self.iso_42001_references, list):
            self.iso_42001_references = [self.iso_42001_references] if self.iso_42001_references is not None else []
        self.iso_42001_references = [v if isinstance(v, str) else str(v) for v in self.iso_42001_references]

        if not isinstance(self.nist_ai_600_1_references, list):
            self.nist_ai_600_1_references = [self.nist_ai_600_1_references] if self.nist_ai_600_1_references is not None else []
        self.nist_ai_600_1_references = [v if isinstance(v, str) else str(v) for v in self.nist_ai_600_1_references]

        if not isinstance(self.nist_sp_800_53r5_references, list):
            self.nist_sp_800_53r5_references = [self.nist_sp_800_53r5_references] if self.nist_sp_800_53r5_references is not None else []
        self.nist_sp_800_53r5_references = [v if isinstance(v, str) else str(v) for v in self.nist_sp_800_53r5_references]

        if not isinstance(self.owasp_asi_references, list):
            self.owasp_asi_references = [self.owasp_asi_references] if self.owasp_asi_references is not None else []
        self.owasp_asi_references = [v if isinstance(v, str) else str(v) for v in self.owasp_asi_references]

        if not isinstance(self.owasp_llm_references, list):
            self.owasp_llm_references = [self.owasp_llm_references] if self.owasp_llm_references is not None else []
        self.owasp_llm_references = [v if isinstance(v, str) else str(v) for v in self.owasp_llm_references]

        if not isinstance(self.owasp_ml_references, list):
            self.owasp_ml_references = [self.owasp_ml_references] if self.owasp_ml_references is not None else []
        self.owasp_ml_references = [v if isinstance(v, str) else str(v) for v in self.owasp_ml_references]

        if not isinstance(self.sr11_7_references, list):
            self.sr11_7_references = [self.sr11_7_references] if self.sr11_7_references is not None else []
        self.sr11_7_references = [v if isinstance(v, str) else str(v) for v in self.sr11_7_references]

        if not isinstance(self.uk_regulations_references, list):
            self.uk_regulations_references = [self.uk_regulations_references] if self.uk_regulations_references is not None else []
        self.uk_regulations_references = [v if isinstance(v, str) else str(v) for v in self.uk_regulations_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfDataClassificationUse(YAMLRoot):
    """
    A data classification a use case handles, with the kinds of data it holds under it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfDataClassificationUse"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfDataClassificationUse"
    class_name: ClassVar[str] = "AigfDataClassificationUse"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfDataClassificationUse

    name: str = None
    data_types: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.data_types, list):
            self.data_types = [self.data_types] if self.data_types is not None else []
        self.data_types = [v if isinstance(v, str) else str(v) for v in self.data_types]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfRegulatoryReference(YAMLRoot):
    """
    A regulation or guideline named by its title and address, with where it applies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfRegulatoryReference"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfRegulatoryReference"
    class_name: ClassVar[str] = "AigfRegulatoryReference"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfRegulatoryReference

    name: str = None
    url: Optional[str] = None
    jurisdiction: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.jurisdiction is not None and not isinstance(self.jurisdiction, str):
            self.jurisdiction = str(self.jurisdiction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfFurtherReading(YAMLRoot):
    """
    A paper or article a use case points to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfFurtherReading"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfFurtherReading"
    class_name: ClassVar[str] = "AigfFurtherReading"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfFurtherReading

    name: str = None
    url: Optional[str] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfDataClassification(YAMLRoot):
    """
    A class of financial data with its sensitivity and its handling, from docs/_data/data_classification.yml.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfDataClassification"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfDataClassification"
    class_name: ClassVar[str] = "AigfDataClassification"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfDataClassification

    name: str = None
    sensitivity: Union[str, "AigfSensitivity"] = None
    description: str = None
    examples: Optional[Union[str, list[str]]] = empty_list()
    storage_location: Optional[str] = None
    regulations: Optional[str] = None
    references: Optional[Union[Union[dict, AigfRegulatoryReference], list[Union[dict, AigfRegulatoryReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.sensitivity):
            self.MissingRequiredField("sensitivity")
        if not isinstance(self.sensitivity, AigfSensitivity):
            self.sensitivity = AigfSensitivity(self.sensitivity)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        if self.storage_location is not None and not isinstance(self.storage_location, str):
            self.storage_location = str(self.storage_location)

        if self.regulations is not None and not isinstance(self.regulations, str):
            self.regulations = str(self.regulations)

        self._normalize_inlined_as_list(slot_name="references", slot_type=AigfRegulatoryReference, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfReferenceLens(YAMLRoot):
    """
    How the site presents the reference files of one lens, from reference_lenses in docs/_config.yml.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfReferenceLens"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfReferenceLens"
    class_name: ClassVar[str] = "AigfReferenceLens"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfReferenceLens

    lens: Union[str, "AigfLens"] = None
    label: str = None
    question: str = None
    icon: Optional[str] = None
    color: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lens):
            self.MissingRequiredField("lens")
        if not isinstance(self.lens, AigfLens):
            self.lens = AigfLens(self.lens)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.question):
            self.MissingRequiredField("question")
        if not isinstance(self.question, str):
            self.question = str(self.question)

        if self.icon is not None and not isinstance(self.icon, str):
            self.icon = str(self.icon)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfReferenceFile(YAMLRoot):
    """
    One file under docs/_data/references/, which lists the citable entries of one regulation, framework or standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfReferenceFile"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfReferenceFile"
    class_name: ClassVar[str] = "AigfReferenceFile"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfReferenceFile

    title: str = None
    description: str = None
    lens: Union[str, "AigfLens"] = None
    entries: Union[dict[Union[str, AigfReferenceEntryReferenceKey], Union[dict, "AigfReferenceEntry"]], list[Union[dict, "AigfReferenceEntry"]]] = empty_dict()
    source_url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.lens):
            self.MissingRequiredField("lens")
        if not isinstance(self.lens, AigfLens):
            self.lens = AigfLens(self.lens)

        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=AigfReferenceEntry, key_name="reference_key", keyed=True)

        if self.source_url is not None and not isinstance(self.source_url, str):
            self.source_url = str(self.source_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfReferenceEntry(YAMLRoot):
    """
    One citable item of a reference file, under the key a page cites it by.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfReferenceEntry"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfReferenceEntry"
    class_name: ClassVar[str] = "AigfReferenceEntry"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfReferenceEntry

    reference_key: Union[str, AigfReferenceEntryReferenceKey] = None
    title: str = None
    url: str = None
    description: Optional[str] = None
    issuer: Optional[str] = None
    booklet_abbrev: Optional[str] = None
    superseded_by: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_key):
            self.MissingRequiredField("reference_key")
        if not isinstance(self.reference_key, AigfReferenceEntryReferenceKey):
            self.reference_key = AigfReferenceEntryReferenceKey(self.reference_key)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.issuer is not None and not isinstance(self.issuer, str):
            self.issuer = str(self.issuer)

        if self.booklet_abbrev is not None and not isinstance(self.booklet_abbrev, str):
            self.booklet_abbrev = str(self.booklet_abbrev)

        if self.superseded_by is not None and not isinstance(self.superseded_by, str):
            self.superseded_by = str(self.superseded_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfReferenceIndex(YAMLRoot):
    """
    The keys one reference file holds, so that a catalogue's citations resolve within it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfReferenceIndex"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfReferenceIndex"
    class_name: ClassVar[str] = "AigfReferenceIndex"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfReferenceIndex

    reference_file: str = None
    lens: Union[str, "AigfLens"] = None
    entry_keys: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_file):
            self.MissingRequiredField("reference_file")
        if not isinstance(self.reference_file, str):
            self.reference_file = str(self.reference_file)

        if self._is_empty(self.lens):
            self.MissingRequiredField("lens")
        if not isinstance(self.lens, AigfLens):
            self.lens = AigfLens(self.lens)

        if not isinstance(self.entry_keys, list):
            self.entry_keys = [self.entry_keys] if self.entry_keys is not None else []
        self.entry_keys = [v if isinstance(v, str) else str(v) for v in self.entry_keys]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfUseCaseDomain(YAMLRoot):
    """
    A top level of the use case taxonomy in docs/_data/ai_use_cases.yml.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfUseCaseDomain"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfUseCaseDomain"
    class_name: ClassVar[str] = "AigfUseCaseDomain"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfUseCaseDomain

    name: str = None
    use_case_areas: Optional[Union[Union[dict, "AigfUseCaseArea"], list[Union[dict, "AigfUseCaseArea"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="use_case_areas", slot_type=AigfUseCaseArea, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfUseCaseArea(YAMLRoot):
    """
    A second level of the use case taxonomy, with the use cases under it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfUseCaseArea"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfUseCaseArea"
    class_name: ClassVar[str] = "AigfUseCaseArea"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfUseCaseArea

    name: str = None
    use_case_names: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.use_case_names, list):
            self.use_case_names = [self.use_case_names] if self.use_case_names is not None else []
        self.use_case_names = [v if isinstance(v, str) else str(v) for v in self.use_case_names]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfDeploymentAxis(YAMLRoot):
    """
    One axis of the deployment model taxonomy in docs/_data/ai_deployment_model.yml.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfDeploymentAxis"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfDeploymentAxis"
    class_name: ClassVar[str] = "AigfDeploymentAxis"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfDeploymentAxis

    name: str = None
    options: Optional[Union[Union[dict, "AigfDeploymentOption"], list[Union[dict, "AigfDeploymentOption"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="options", slot_type=AigfDeploymentOption, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AigfDeploymentOption(YAMLRoot):
    """
    One option on an axis of the deployment model taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK["AigfDeploymentOption"]
    class_class_curie: ClassVar[str] = "ai_governance_framework:AigfDeploymentOption"
    class_name: ClassVar[str] = "AigfDeploymentOption"
    class_model_uri: ClassVar[URIRef] = AI_GOVERNANCE_FRAMEWORK.AigfDeploymentOption

    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class AigfDocumentStatus(EnumDefinitionImpl):
    """
    How far a page has been approved, from document_status in docs/_config.yml.
    """
    Draft = PermissibleValue(
        text="Draft",
        description="""The document is in the early stages of development, with content being written and structured but not yet polished.""")

    _defn = EnumDefinition(
        name="AigfDocumentStatus",
        description="How far a page has been approved, from document_status in docs/_config.yml.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Pre-Draft",
            PermissibleValue(
                text="Pre-Draft",
                description="""Initial brainstorming or collection of ideas, notes, and outlines. The document is not yet formally written."""))
        setattr(cls, "Working-Group-Approved",
            PermissibleValue(
                text="Working-Group-Approved",
                description="The document is in its final form and has been approved by the AIGF team."))
        setattr(cls, "Approved-Specification",
            PermissibleValue(
                text="Approved-Specification",
                description="The publication of an Approved Specification in a publicly accessible manner."))

class AigfRiskType(EnumDefinitionImpl):
    """
    A risk's group, from risk_type_labels in docs/_config.yml.
    """
    RC = PermissibleValue(
        text="RC",
        title="Regulatory and Compliance")
    OP = PermissibleValue(
        text="OP",
        title="Operational")
    SEC = PermissibleValue(
        text="SEC",
        title="Security")

    _defn = EnumDefinition(
        name="AigfRiskType",
        description="A risk's group, from risk_type_labels in docs/_config.yml.",
    )

class AigfMitigationType(EnumDefinitionImpl):
    """
    A mitigation's group, from mitigation_type_labels in docs/_config.yml.
    """
    PREV = PermissibleValue(
        text="PREV",
        title="Preventative")
    DET = PermissibleValue(
        text="DET",
        title="Detective")

    _defn = EnumDefinition(
        name="AigfMitigationType",
        description="A mitigation's group, from mitigation_type_labels in docs/_config.yml.",
    )

class AigfRiskDomain(EnumDefinitionImpl):
    """
    A risk's domain, from risk_domain_labels in docs/_config.yml.
    """
    components = PermissibleValue(
        text="components",
        title="Components")
    inputs = PermissibleValue(
        text="inputs",
        title="Inputs")
    leakage = PermissibleValue(
        text="leakage",
        title="Leakage")
    accuracy = PermissibleValue(
        text="accuracy",
        title="Accuracy")
    alignment = PermissibleValue(
        text="alignment",
        title="Alignment")
    agency = PermissibleValue(
        text="agency",
        title="Agency")
    vendor = PermissibleValue(
        text="vendor",
        title="Vendor")
    liability = PermissibleValue(
        text="liability",
        title="Liability")

    _defn = EnumDefinition(
        name="AigfRiskDomain",
        description="A risk's domain, from risk_domain_labels in docs/_config.yml.",
    )

class AigfMitigationDomain(EnumDefinitionImpl):
    """
    A mitigation's domain, from mitigation_domain_labels in docs/_config.yml.
    """
    sourcing = PermissibleValue(
        text="sourcing",
        title="Sourcing")
    filtering = PermissibleValue(
        text="filtering",
        title="Filtering")
    data = PermissibleValue(
        text="data",
        title="Data")
    access = PermissibleValue(
        text="access",
        title="Access")
    evaluation = PermissibleValue(
        text="evaluation",
        title="Evaluation")
    oversight = PermissibleValue(
        text="oversight",
        title="Oversight")
    monitoring = PermissibleValue(
        text="monitoring",
        title="Monitoring")

    _defn = EnumDefinition(
        name="AigfMitigationDomain",
        description="A mitigation's domain, from mitigation_domain_labels in docs/_config.yml.",
    )

class AigfUseCaseCategory(EnumDefinitionImpl):
    """
    A use case's category, from usecase_categories in docs/_config.yml.
    """
    Customer_Experience_and_Engagement = PermissibleValue(
        text="Customer_Experience_and_Engagement",
        title="Customer Experience and Engagement")
    Risk_Management_and_Compliance = PermissibleValue(
        text="Risk_Management_and_Compliance",
        title="Risk Management and Compliance")
    Operations_and_Process_Optimization = PermissibleValue(
        text="Operations_and_Process_Optimization",
        title="Operations and Process Optimization")
    Trading_and_Investment = PermissibleValue(
        text="Trading_and_Investment",
        title="Trading and Investment")
    Data_Intelligence_and_Analytics = PermissibleValue(
        text="Data_Intelligence_and_Analytics",
        title="Data Intelligence and Analytics")
    Fraud_Detection_and_Security = PermissibleValue(
        text="Fraud_Detection_and_Security",
        title="Fraud Detection and Security")
    Risk_and_Compliance = PermissibleValue(
        text="Risk_and_Compliance",
        title="Risk and Compliance",
        description="""A category uc-3 and uc-4 use. docs/_config.yml does not list it, though docs/_data/ai_use_cases.yml has a domain of this name.""")

    _defn = EnumDefinition(
        name="AigfUseCaseCategory",
        description="A use case's category, from usecase_categories in docs/_config.yml.",
    )

class AigfSensitivity(EnumDefinitionImpl):
    """
    How sensitive a class of data is, as docs/_data/data_classification.yml grades it.
    """
    Low = PermissibleValue(text="Low")
    Medium = PermissibleValue(text="Medium")
    High = PermissibleValue(text="High")
    Critical = PermissibleValue(text="Critical")

    _defn = EnumDefinition(
        name="AigfSensitivity",
        description="How sensitive a class of data is, as docs/_data/data_classification.yml grades it.",
    )

class AigfLens(EnumDefinitionImpl):
    """
    The question a reference file answers, from docs/_data/references/README.md.
    """
    threat = PermissibleValue(
        text="threat",
        description="What is this called elsewhere?")
    obligation = PermissibleValue(
        text="obligation",
        description="Which rule requires me to address it?")
    control = PermissibleValue(
        text="control",
        description="How do I implement and evidence it?")

    _defn = EnumDefinition(
        name="AigfLens",
        description="The question a reference file answers, from docs/_data/references/README.md.",
    )

class AigfDataHandling(EnumDefinitionImpl):
    """
    The options of the deployment model's data_handling axis.
    """
    Centralized = PermissibleValue(text="Centralized")
    Federated = PermissibleValue(text="Federated")
    Synthetic_Data = PermissibleValue(text="Synthetic_Data")
    Privacy_Preserving = PermissibleValue(text="Privacy_Preserving")

    _defn = EnumDefinition(
        name="AigfDataHandling",
        description="The options of the deployment model's data_handling axis.",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.description, domain=None, range=Optional[str])

slots.version = Slot(uri=AI_GOVERNANCE_FRAMEWORK.version, name="version", curie=AI_GOVERNANCE_FRAMEWORK.curie('version'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.version, domain=None, range=Optional[str])

slots.release_date = Slot(uri=AI_GOVERNANCE_FRAMEWORK.release_date, name="release_date", curie=AI_GOVERNANCE_FRAMEWORK.curie('release_date'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.release_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.source_commit = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_commit, name="source_commit", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_commit'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.source_commit, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9a-f]{40}$'))

slots.reference_lenses = Slot(uri=AI_GOVERNANCE_FRAMEWORK.reference_lenses, name="reference_lenses", curie=AI_GOVERNANCE_FRAMEWORK.curie('reference_lenses'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.reference_lenses, domain=None, range=Optional[Union[Union[dict, AigfReferenceLens], list[Union[dict, AigfReferenceLens]]]])

slots.reference_indexes = Slot(uri=AI_GOVERNANCE_FRAMEWORK.reference_indexes, name="reference_indexes", curie=AI_GOVERNANCE_FRAMEWORK.curie('reference_indexes'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.reference_indexes, domain=None, range=Optional[Union[Union[dict, AigfReferenceIndex], list[Union[dict, AigfReferenceIndex]]]])

slots.risks = Slot(uri=AI_GOVERNANCE_FRAMEWORK.risks, name="risks", curie=AI_GOVERNANCE_FRAMEWORK.curie('risks'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.risks, domain=None, range=Optional[Union[dict[Union[str, AigfRiskItemId], Union[dict, AigfRisk]], list[Union[dict, AigfRisk]]]])

slots.mitigations = Slot(uri=AI_GOVERNANCE_FRAMEWORK.mitigations, name="mitigations", curie=AI_GOVERNANCE_FRAMEWORK.curie('mitigations'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.mitigations, domain=None, range=Optional[Union[dict[Union[str, AigfMitigationItemId], Union[dict, AigfMitigation]], list[Union[dict, AigfMitigation]]]])

slots.use_cases = Slot(uri=AI_GOVERNANCE_FRAMEWORK.use_cases, name="use_cases", curie=AI_GOVERNANCE_FRAMEWORK.curie('use_cases'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.use_cases, domain=None, range=Optional[Union[dict[Union[str, AigfUseCaseItemId], Union[dict, AigfUseCase]], list[Union[dict, AigfUseCase]]]])

slots.financial_data_classification = Slot(uri=AI_GOVERNANCE_FRAMEWORK.financial_data_classification, name="financial_data_classification", curie=AI_GOVERNANCE_FRAMEWORK.curie('financial_data_classification'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.financial_data_classification, domain=None, range=Optional[Union[Union[dict, AigfDataClassification], list[Union[dict, AigfDataClassification]]]])

slots.ai_use_cases = Slot(uri=AI_GOVERNANCE_FRAMEWORK.ai_use_cases, name="ai_use_cases", curie=AI_GOVERNANCE_FRAMEWORK.curie('ai_use_cases'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.ai_use_cases, domain=None, range=Optional[Union[Union[dict, AigfUseCaseDomain], list[Union[dict, AigfUseCaseDomain]]]])

slots.cross_cutting_capabilities = Slot(uri=AI_GOVERNANCE_FRAMEWORK.cross_cutting_capabilities, name="cross_cutting_capabilities", curie=AI_GOVERNANCE_FRAMEWORK.curie('cross_cutting_capabilities'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.cross_cutting_capabilities, domain=None, range=Optional[Union[str, list[str]]])

slots.ai_deployment_model_taxonomy = Slot(uri=AI_GOVERNANCE_FRAMEWORK.ai_deployment_model_taxonomy, name="ai_deployment_model_taxonomy", curie=AI_GOVERNANCE_FRAMEWORK.curie('ai_deployment_model_taxonomy'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.ai_deployment_model_taxonomy, domain=None, range=Optional[Union[Union[dict, AigfDeploymentAxis], list[Union[dict, AigfDeploymentAxis]]]])

slots.item_id = Slot(uri=AI_GOVERNANCE_FRAMEWORK.item_id, name="item_id", curie=AI_GOVERNANCE_FRAMEWORK.curie('item_id'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.item_id, domain=None, range=URIRef)

slots.sequence = Slot(uri=AI_GOVERNANCE_FRAMEWORK.sequence, name="sequence", curie=AI_GOVERNANCE_FRAMEWORK.curie('sequence'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.sequence, domain=None, range=int)

slots.layout = Slot(uri=AI_GOVERNANCE_FRAMEWORK.layout, name="layout", curie=AI_GOVERNANCE_FRAMEWORK.curie('layout'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.layout, domain=None, range=str)

slots.doc_status = Slot(uri=AI_GOVERNANCE_FRAMEWORK.doc_status, name="doc_status", curie=AI_GOVERNANCE_FRAMEWORK.curie('doc_status'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.doc_status, domain=None, range=Union[str, "AigfDocumentStatus"])

slots.source_file = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_file, name="source_file", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_file'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.source_file, domain=None, range=str)

slots.risk_type = Slot(uri=AI_GOVERNANCE_FRAMEWORK.risk_type, name="risk_type", curie=AI_GOVERNANCE_FRAMEWORK.curie('risk_type'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.risk_type, domain=None, range=Union[str, "AigfRiskType"])

slots.risk_domain = Slot(uri=AI_GOVERNANCE_FRAMEWORK.risk_domain, name="risk_domain", curie=AI_GOVERNANCE_FRAMEWORK.curie('risk_domain'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.risk_domain, domain=None, range=Union[str, "AigfRiskDomain"])

slots.mitigation_type = Slot(uri=AI_GOVERNANCE_FRAMEWORK.mitigation_type, name="mitigation_type", curie=AI_GOVERNANCE_FRAMEWORK.curie('mitigation_type'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.mitigation_type, domain=None, range=Union[str, "AigfMitigationType"])

slots.mitigation_domain = Slot(uri=AI_GOVERNANCE_FRAMEWORK.mitigation_domain, name="mitigation_domain", curie=AI_GOVERNANCE_FRAMEWORK.curie('mitigation_domain'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.mitigation_domain, domain=None, range=Union[str, "AigfMitigationDomain"])

slots.related_risks = Slot(uri=AI_GOVERNANCE_FRAMEWORK.related_risks, name="related_risks", curie=AI_GOVERNANCE_FRAMEWORK.curie('related_risks'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.related_risks, domain=None, range=Optional[Union[Union[str, AigfRiskItemId], list[Union[str, AigfRiskItemId]]]])

slots.related_mitigations = Slot(uri=AI_GOVERNANCE_FRAMEWORK.related_mitigations, name="related_mitigations", curie=AI_GOVERNANCE_FRAMEWORK.curie('related_mitigations'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.related_mitigations, domain=None, range=Optional[Union[Union[str, AigfMitigationItemId], list[Union[str, AigfMitigationItemId]]]])

slots.mitigates = Slot(uri=AI_GOVERNANCE_FRAMEWORK.mitigates, name="mitigates", curie=AI_GOVERNANCE_FRAMEWORK.curie('mitigates'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.mitigates, domain=None, range=Union[Union[str, AigfRiskItemId], list[Union[str, AigfRiskItemId]]])

slots.category = Slot(uri=AI_GOVERNANCE_FRAMEWORK.category, name="category", curie=AI_GOVERNANCE_FRAMEWORK.curie('category'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.category, domain=None, range=Union[str, "AigfUseCaseCategory"])

slots.end_user = Slot(uri=AI_GOVERNANCE_FRAMEWORK.end_user, name="end_user", curie=AI_GOVERNANCE_FRAMEWORK.curie('end_user'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.end_user, domain=None, range=Optional[str])

slots.business_value = Slot(uri=AI_GOVERNANCE_FRAMEWORK.business_value, name="business_value", curie=AI_GOVERNANCE_FRAMEWORK.curie('business_value'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.business_value, domain=None, range=Optional[str])

slots.data_classifications = Slot(uri=AI_GOVERNANCE_FRAMEWORK.data_classifications, name="data_classifications", curie=AI_GOVERNANCE_FRAMEWORK.curie('data_classifications'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.data_classifications, domain=None, range=Optional[Union[Union[dict, AigfDataClassificationUse], list[Union[dict, AigfDataClassificationUse]]]])

slots.data_types = Slot(uri=AI_GOVERNANCE_FRAMEWORK.data_types, name="data_types", curie=AI_GOVERNANCE_FRAMEWORK.curie('data_types'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.data_types, domain=None, range=Optional[Union[str, list[str]]])

slots.data_handling_aspects = Slot(uri=AI_GOVERNANCE_FRAMEWORK.data_handling_aspects, name="data_handling_aspects", curie=AI_GOVERNANCE_FRAMEWORK.curie('data_handling_aspects'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.data_handling_aspects, domain=None, range=Optional[Union[Union[str, "AigfDataHandling"], list[Union[str, "AigfDataHandling"]]]])

slots.regulatory_concerns = Slot(uri=AI_GOVERNANCE_FRAMEWORK.regulatory_concerns, name="regulatory_concerns", curie=AI_GOVERNANCE_FRAMEWORK.curie('regulatory_concerns'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.regulatory_concerns, domain=None, range=Optional[Union[Union[dict, AigfRegulatoryReference], list[Union[dict, AigfRegulatoryReference]]]])

slots.further_reading = Slot(uri=AI_GOVERNANCE_FRAMEWORK.further_reading, name="further_reading", curie=AI_GOVERNANCE_FRAMEWORK.curie('further_reading'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.further_reading, domain=None, range=Optional[Union[Union[dict, AigfFurtherReading], list[Union[dict, AigfFurtherReading]]]])

slots.atr_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.atr_references, name="atr_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('atr_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.atr_references, domain=None, range=Optional[Union[str, list[str]]])

slots.canada_regulations_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.canada_regulations_references, name="canada_regulations_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('canada_regulations_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.canada_regulations_references, domain=None, range=Optional[Union[str, list[str]]])

slots.eu_ai_act_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.eu_ai_act_references, name="eu_ai_act_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('eu_ai_act_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.eu_ai_act_references, domain=None, range=Optional[Union[str, list[str]]])

slots.ffiec_itbooklets_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.ffiec_itbooklets_references, name="ffiec_itbooklets_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('ffiec_itbooklets_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.ffiec_itbooklets_references, domain=None, range=Optional[Union[str, list[str]]])

slots.iosco_supervisory_toolkit_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.iosco_supervisory_toolkit_references, name="iosco_supervisory_toolkit_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('iosco_supervisory_toolkit_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.iosco_supervisory_toolkit_references, domain=None, range=Optional[Union[str, list[str]]])

slots.iso_42001_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.iso_42001_references, name="iso_42001_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('iso_42001_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.iso_42001_references, domain=None, range=Optional[Union[str, list[str]]])

slots.nist_ai_600_1_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.nist_ai_600_1_references, name="nist_ai_600_1_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('nist_ai_600_1_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.nist_ai_600_1_references, domain=None, range=Optional[Union[str, list[str]]])

slots.nist_sp_800_53r5_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.nist_sp_800_53r5_references, name="nist_sp_800_53r5_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('nist_sp_800_53r5_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.nist_sp_800_53r5_references, domain=None, range=Optional[Union[str, list[str]]])

slots.owasp_asi_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.owasp_asi_references, name="owasp_asi_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('owasp_asi_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.owasp_asi_references, domain=None, range=Optional[Union[str, list[str]]])

slots.owasp_llm_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.owasp_llm_references, name="owasp_llm_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('owasp_llm_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.owasp_llm_references, domain=None, range=Optional[Union[str, list[str]]])

slots.owasp_ml_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.owasp_ml_references, name="owasp_ml_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('owasp_ml_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.owasp_ml_references, domain=None, range=Optional[Union[str, list[str]]])

slots.sr11_7_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.sr11_7_references, name="sr11_7_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('sr11_7_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.sr11_7_references, domain=None, range=Optional[Union[str, list[str]]])

slots.uk_regulations_references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.uk_regulations_references, name="uk_regulations_references", curie=AI_GOVERNANCE_FRAMEWORK.curie('uk_regulations_references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.uk_regulations_references, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=AI_GOVERNANCE_FRAMEWORK.name, name="name", curie=AI_GOVERNANCE_FRAMEWORK.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.name, domain=None, range=str)

slots.url = Slot(uri=AI_GOVERNANCE_FRAMEWORK.url, name="url", curie=AI_GOVERNANCE_FRAMEWORK.curie('url'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.url, domain=None, range=Optional[str],
                   pattern=re.compile(r'^http'))

slots.jurisdiction = Slot(uri=AI_GOVERNANCE_FRAMEWORK.jurisdiction, name="jurisdiction", curie=AI_GOVERNANCE_FRAMEWORK.curie('jurisdiction'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.jurisdiction, domain=None, range=Optional[str])

slots.source = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source, name="source", curie=AI_GOVERNANCE_FRAMEWORK.curie('source'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.source, domain=None, range=Optional[str])

slots.sensitivity = Slot(uri=AI_GOVERNANCE_FRAMEWORK.sensitivity, name="sensitivity", curie=AI_GOVERNANCE_FRAMEWORK.curie('sensitivity'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.sensitivity, domain=None, range=Optional[Union[str, "AigfSensitivity"]])

slots.examples = Slot(uri=AI_GOVERNANCE_FRAMEWORK.examples, name="examples", curie=AI_GOVERNANCE_FRAMEWORK.curie('examples'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.examples, domain=None, range=Optional[Union[str, list[str]]])

slots.storage_location = Slot(uri=AI_GOVERNANCE_FRAMEWORK.storage_location, name="storage_location", curie=AI_GOVERNANCE_FRAMEWORK.curie('storage_location'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.storage_location, domain=None, range=Optional[str])

slots.regulations = Slot(uri=AI_GOVERNANCE_FRAMEWORK.regulations, name="regulations", curie=AI_GOVERNANCE_FRAMEWORK.curie('regulations'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.regulations, domain=None, range=Optional[str])

slots.references = Slot(uri=AI_GOVERNANCE_FRAMEWORK.references, name="references", curie=AI_GOVERNANCE_FRAMEWORK.curie('references'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.references, domain=None, range=Optional[Union[Union[dict, AigfRegulatoryReference], list[Union[dict, AigfRegulatoryReference]]]])

slots.lens = Slot(uri=AI_GOVERNANCE_FRAMEWORK.lens, name="lens", curie=AI_GOVERNANCE_FRAMEWORK.curie('lens'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.lens, domain=None, range=Optional[Union[str, "AigfLens"]])

slots.label = Slot(uri=AI_GOVERNANCE_FRAMEWORK.label, name="label", curie=AI_GOVERNANCE_FRAMEWORK.curie('label'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.label, domain=None, range=Optional[str])

slots.question = Slot(uri=AI_GOVERNANCE_FRAMEWORK.question, name="question", curie=AI_GOVERNANCE_FRAMEWORK.curie('question'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.question, domain=None, range=Optional[str])

slots.icon = Slot(uri=AI_GOVERNANCE_FRAMEWORK.icon, name="icon", curie=AI_GOVERNANCE_FRAMEWORK.curie('icon'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.icon, domain=None, range=Optional[str])

slots.color = Slot(uri=AI_GOVERNANCE_FRAMEWORK.color, name="color", curie=AI_GOVERNANCE_FRAMEWORK.curie('color'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.color, domain=None, range=Optional[str])

slots.source_url = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_url, name="source_url", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_url'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.source_url, domain=None, range=Optional[str])

slots.entries = Slot(uri=AI_GOVERNANCE_FRAMEWORK.entries, name="entries", curie=AI_GOVERNANCE_FRAMEWORK.curie('entries'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.entries, domain=None, range=Optional[Union[dict[Union[str, AigfReferenceEntryReferenceKey], Union[dict, AigfReferenceEntry]], list[Union[dict, AigfReferenceEntry]]]])

slots.reference_key = Slot(uri=AI_GOVERNANCE_FRAMEWORK.reference_key, name="reference_key", curie=AI_GOVERNANCE_FRAMEWORK.curie('reference_key'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.reference_key, domain=None, range=URIRef)

slots.issuer = Slot(uri=AI_GOVERNANCE_FRAMEWORK.issuer, name="issuer", curie=AI_GOVERNANCE_FRAMEWORK.curie('issuer'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.issuer, domain=None, range=Optional[str])

slots.booklet_abbrev = Slot(uri=AI_GOVERNANCE_FRAMEWORK.booklet_abbrev, name="booklet_abbrev", curie=AI_GOVERNANCE_FRAMEWORK.curie('booklet_abbrev'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.booklet_abbrev, domain=None, range=Optional[str])

slots.superseded_by = Slot(uri=AI_GOVERNANCE_FRAMEWORK.superseded_by, name="superseded_by", curie=AI_GOVERNANCE_FRAMEWORK.curie('superseded_by'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.superseded_by, domain=None, range=Optional[str])

slots.reference_file = Slot(uri=AI_GOVERNANCE_FRAMEWORK.reference_file, name="reference_file", curie=AI_GOVERNANCE_FRAMEWORK.curie('reference_file'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.reference_file, domain=None, range=str)

slots.entry_keys = Slot(uri=AI_GOVERNANCE_FRAMEWORK.entry_keys, name="entry_keys", curie=AI_GOVERNANCE_FRAMEWORK.curie('entry_keys'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.entry_keys, domain=None, range=Optional[Union[str, list[str]]])

slots.use_case_areas = Slot(uri=AI_GOVERNANCE_FRAMEWORK.use_case_areas, name="use_case_areas", curie=AI_GOVERNANCE_FRAMEWORK.curie('use_case_areas'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.use_case_areas, domain=None, range=Optional[Union[Union[dict, AigfUseCaseArea], list[Union[dict, AigfUseCaseArea]]]])

slots.use_case_names = Slot(uri=AI_GOVERNANCE_FRAMEWORK.use_case_names, name="use_case_names", curie=AI_GOVERNANCE_FRAMEWORK.curie('use_case_names'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.use_case_names, domain=None, range=Optional[Union[str, list[str]]])

slots.options = Slot(uri=AI_GOVERNANCE_FRAMEWORK.options, name="options", curie=AI_GOVERNANCE_FRAMEWORK.curie('options'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.options, domain=None, range=Optional[Union[Union[dict, AigfDeploymentOption], list[Union[dict, AigfDeploymentOption]]]])

slots.AigfCatalogue_title = Slot(uri=SCHEMA.name, name="AigfCatalogue_title", curie=SCHEMA.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfCatalogue_title, domain=AigfCatalogue, range=str)

slots.AigfCatalogue_version = Slot(uri=AI_GOVERNANCE_FRAMEWORK.version, name="AigfCatalogue_version", curie=AI_GOVERNANCE_FRAMEWORK.curie('version'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfCatalogue_version, domain=AigfCatalogue, range=str)

slots.AigfCatalogue_release_date = Slot(uri=AI_GOVERNANCE_FRAMEWORK.release_date, name="AigfCatalogue_release_date", curie=AI_GOVERNANCE_FRAMEWORK.curie('release_date'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfCatalogue_release_date, domain=AigfCatalogue, range=Union[str, XSDDate])

slots.AigfCatalogue_source_commit = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_commit, name="AigfCatalogue_source_commit", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_commit'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfCatalogue_source_commit, domain=AigfCatalogue, range=str,
                   pattern=re.compile(r'^[0-9a-f]{40}$'))

slots.AigfCatalogue_risks = Slot(uri=AI_GOVERNANCE_FRAMEWORK.risks, name="AigfCatalogue_risks", curie=AI_GOVERNANCE_FRAMEWORK.curie('risks'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfCatalogue_risks, domain=AigfCatalogue, range=Union[dict[Union[str, AigfRiskItemId], Union[dict, "AigfRisk"]], list[Union[dict, "AigfRisk"]]])

slots.AigfCatalogue_mitigations = Slot(uri=AI_GOVERNANCE_FRAMEWORK.mitigations, name="AigfCatalogue_mitigations", curie=AI_GOVERNANCE_FRAMEWORK.curie('mitigations'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfCatalogue_mitigations, domain=AigfCatalogue, range=Union[dict[Union[str, AigfMitigationItemId], Union[dict, "AigfMitigation"]], list[Union[dict, "AigfMitigation"]]])

slots.AigfItem_title = Slot(uri=SCHEMA.name, name="AigfItem_title", curie=SCHEMA.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfItem_title, domain=AigfItem, range=str)

slots.AigfRisk_item_id = Slot(uri=AI_GOVERNANCE_FRAMEWORK.item_id, name="AigfRisk_item_id", curie=AI_GOVERNANCE_FRAMEWORK.curie('item_id'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfRisk_item_id, domain=AigfRisk, range=Union[str, AigfRiskItemId],
                   pattern=re.compile(r'^ri-[1-9][0-9]*$'))

slots.AigfRisk_layout = Slot(uri=AI_GOVERNANCE_FRAMEWORK.layout, name="AigfRisk_layout", curie=AI_GOVERNANCE_FRAMEWORK.curie('layout'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfRisk_layout, domain=AigfRisk, range=str)

slots.AigfRisk_source_file = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_file, name="AigfRisk_source_file", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_file'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfRisk_source_file, domain=AigfRisk, range=str,
                   pattern=re.compile(r'^docs/_risks/ri-[1-9][0-9]*_[a-z0-9-]+[.]md$'))

slots.AigfMitigation_item_id = Slot(uri=AI_GOVERNANCE_FRAMEWORK.item_id, name="AigfMitigation_item_id", curie=AI_GOVERNANCE_FRAMEWORK.curie('item_id'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfMitigation_item_id, domain=AigfMitigation, range=Union[str, AigfMitigationItemId],
                   pattern=re.compile(r'^mi-[1-9][0-9]*$'))

slots.AigfMitigation_layout = Slot(uri=AI_GOVERNANCE_FRAMEWORK.layout, name="AigfMitigation_layout", curie=AI_GOVERNANCE_FRAMEWORK.curie('layout'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfMitigation_layout, domain=AigfMitigation, range=str)

slots.AigfMitigation_source_file = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_file, name="AigfMitigation_source_file", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_file'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfMitigation_source_file, domain=AigfMitigation, range=str,
                   pattern=re.compile(r'^docs/_mitigations/mi-[1-9][0-9]*_[a-z0-9-]+[.]md$'))

slots.AigfUseCase_item_id = Slot(uri=AI_GOVERNANCE_FRAMEWORK.item_id, name="AigfUseCase_item_id", curie=AI_GOVERNANCE_FRAMEWORK.curie('item_id'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfUseCase_item_id, domain=AigfUseCase, range=Union[str, AigfUseCaseItemId],
                   pattern=re.compile(r'^uc-[1-9][0-9]*$'))

slots.AigfUseCase_layout = Slot(uri=AI_GOVERNANCE_FRAMEWORK.layout, name="AigfUseCase_layout", curie=AI_GOVERNANCE_FRAMEWORK.curie('layout'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfUseCase_layout, domain=AigfUseCase, range=str)

slots.AigfUseCase_source_file = Slot(uri=AI_GOVERNANCE_FRAMEWORK.source_file, name="AigfUseCase_source_file", curie=AI_GOVERNANCE_FRAMEWORK.curie('source_file'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfUseCase_source_file, domain=AigfUseCase, range=str,
                   pattern=re.compile(r'^docs/_usecases/uc-[1-9][0-9]*_[a-z0-9-]+[.]md$'))

slots.AigfUseCase_description = Slot(uri=SCHEMA.description, name="AigfUseCase_description", curie=SCHEMA.curie('description'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfUseCase_description, domain=AigfUseCase, range=str)

slots.AigfDataClassificationUse_name = Slot(uri=AI_GOVERNANCE_FRAMEWORK.name, name="AigfDataClassificationUse_name", curie=AI_GOVERNANCE_FRAMEWORK.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfDataClassificationUse_name, domain=AigfDataClassificationUse, range=str)

slots.AigfDataClassification_sensitivity = Slot(uri=AI_GOVERNANCE_FRAMEWORK.sensitivity, name="AigfDataClassification_sensitivity", curie=AI_GOVERNANCE_FRAMEWORK.curie('sensitivity'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfDataClassification_sensitivity, domain=AigfDataClassification, range=Union[str, "AigfSensitivity"])

slots.AigfDataClassification_description = Slot(uri=SCHEMA.description, name="AigfDataClassification_description", curie=SCHEMA.curie('description'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfDataClassification_description, domain=AigfDataClassification, range=str)

slots.AigfReferenceLens_lens = Slot(uri=AI_GOVERNANCE_FRAMEWORK.lens, name="AigfReferenceLens_lens", curie=AI_GOVERNANCE_FRAMEWORK.curie('lens'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceLens_lens, domain=AigfReferenceLens, range=Union[str, "AigfLens"])

slots.AigfReferenceLens_label = Slot(uri=AI_GOVERNANCE_FRAMEWORK.label, name="AigfReferenceLens_label", curie=AI_GOVERNANCE_FRAMEWORK.curie('label'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceLens_label, domain=AigfReferenceLens, range=str)

slots.AigfReferenceLens_question = Slot(uri=AI_GOVERNANCE_FRAMEWORK.question, name="AigfReferenceLens_question", curie=AI_GOVERNANCE_FRAMEWORK.curie('question'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceLens_question, domain=AigfReferenceLens, range=str)

slots.AigfReferenceFile_title = Slot(uri=SCHEMA.name, name="AigfReferenceFile_title", curie=SCHEMA.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceFile_title, domain=AigfReferenceFile, range=str)

slots.AigfReferenceFile_description = Slot(uri=SCHEMA.description, name="AigfReferenceFile_description", curie=SCHEMA.curie('description'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceFile_description, domain=AigfReferenceFile, range=str)

slots.AigfReferenceFile_lens = Slot(uri=AI_GOVERNANCE_FRAMEWORK.lens, name="AigfReferenceFile_lens", curie=AI_GOVERNANCE_FRAMEWORK.curie('lens'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceFile_lens, domain=AigfReferenceFile, range=Union[str, "AigfLens"])

slots.AigfReferenceFile_entries = Slot(uri=AI_GOVERNANCE_FRAMEWORK.entries, name="AigfReferenceFile_entries", curie=AI_GOVERNANCE_FRAMEWORK.curie('entries'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceFile_entries, domain=AigfReferenceFile, range=Union[dict[Union[str, AigfReferenceEntryReferenceKey], Union[dict, "AigfReferenceEntry"]], list[Union[dict, "AigfReferenceEntry"]]])

slots.AigfReferenceEntry_title = Slot(uri=SCHEMA.name, name="AigfReferenceEntry_title", curie=SCHEMA.curie('name'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceEntry_title, domain=AigfReferenceEntry, range=str)

slots.AigfReferenceEntry_url = Slot(uri=AI_GOVERNANCE_FRAMEWORK.url, name="AigfReferenceEntry_url", curie=AI_GOVERNANCE_FRAMEWORK.curie('url'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceEntry_url, domain=AigfReferenceEntry, range=str,
                   pattern=re.compile(r'^http'))

slots.AigfReferenceIndex_lens = Slot(uri=AI_GOVERNANCE_FRAMEWORK.lens, name="AigfReferenceIndex_lens", curie=AI_GOVERNANCE_FRAMEWORK.curie('lens'),
                   model_uri=AI_GOVERNANCE_FRAMEWORK.AigfReferenceIndex_lens, domain=AigfReferenceIndex, range=Union[str, "AigfLens"])
