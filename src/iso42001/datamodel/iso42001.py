# Auto generated from iso42001.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-01T16:09:22
# Schema: iso42001
#
# id: https://w3id.org/lmodel/iso42001
# description: A comprehensive LinkML schema modeling AI Management System (AIMS) entities, workflows, and traceability links aligned to ISO/IEC 42001:2023 clause and Annex references. Designed for open data publication, automated validation, and integration with AI governance, risk, and compliance platforms.
#   This schema captures: - AIMS lifecycle (establish, implement, maintain, improve) - AI risk assessment, treatment, and AI system impact assessment (Clause 6.1) - Annex A reference control catalog (A.2-A.10) for responsible AI - Audit, measurement, and continual improvement artifacts - Data resources, tooling, computing, and human resources for AI systems - Third-party, supplier, and customer relationships across the AI life cycle
# license: https://www.apache.org/licenses/LICENSE-2.0

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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
ISO22989 = CurieNamespace('iso22989', 'https://w3id.org/lmodel/iso22989/')
ISO23894 = CurieNamespace('iso23894', 'https://w3id.org/lmodel/iso23894/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
ISO42001 = CurieNamespace('iso42001', 'https://w3id.org/lmodel/iso42001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_100_1 = CurieNamespace('nist_ai_100_1', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_AI_600_1 = CurieNamespace('nist_ai_600_1', 'https://w3id.org/lmodel/nist-ai-600-1/')
NIST_AI_RMF = CurieNamespace('nist_ai_rmf', 'https://www.nist.gov/itl/ai-risk-management-framework/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO42001


# Types
class PositiveIntegerType(int):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer type"
    type_model_uri = ISO42001.PositiveIntegerType


class UnsignedShortType(int):
    """ data type for non-negative integers that can be represented with 16 bits """
    type_class_uri = XSD["unsignedShort"]
    type_class_curie = "xsd:unsignedShort"
    type_name = "unsigned short type"
    type_model_uri = ISO42001.UnsignedShortType


class DurationType(str):
    """ ISO 8601 duration value such as P1Y, P30D, or PT4H """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration type"
    type_model_uri = ISO42001.DurationType


# Class references
class NamedEntityId(URIorCURIE):
    pass


class DocumentedInformationId(NamedEntityId):
    pass


class AIManagementSystemId(NamedEntityId):
    pass


class OrganizationId(NamedEntityId):
    pass


class InterestedPartyId(NamedEntityId):
    pass


class AIPolicyId(DocumentedInformationId):
    pass


class TopicSpecificPolicyId(DocumentedInformationId):
    pass


class RoleId(NamedEntityId):
    pass


class AIObjectiveId(NamedEntityId):
    pass


class AIRiskAssessmentProcessId(DocumentedInformationId):
    pass


class AIRiskAssessmentId(DocumentedInformationId):
    pass


class AIRiskId(NamedEntityId):
    pass


class AIRiskTreatmentProcessId(DocumentedInformationId):
    pass


class AIRiskTreatmentPlanId(DocumentedInformationId):
    pass


class AISystemImpactAssessmentProcessId(DocumentedInformationId):
    pass


class AISystemImpactAssessmentId(DocumentedInformationId):
    pass


class StatementOfApplicabilityId(DocumentedInformationId):
    pass


class AIReferenceControlId(NamedEntityId):
    pass


class AISystemId(NamedEntityId):
    pass


class DataResourceId(NamedEntityId):
    pass


class ToolingResourceId(NamedEntityId):
    pass


class ComputingResourceId(NamedEntityId):
    pass


class HumanResourceId(NamedEntityId):
    pass


class ResourceId(NamedEntityId):
    pass


class CompetenceRecordId(DocumentedInformationId):
    pass


class AwarenessProgramId(DocumentedInformationId):
    pass


class CommunicationPlanId(DocumentedInformationId):
    pass


class OperationalProcedureId(DocumentedInformationId):
    pass


class MonitoringProgramId(DocumentedInformationId):
    pass


class InternalAuditId(DocumentedInformationId):
    pass


class AuditProgrammeId(DocumentedInformationId):
    pass


class AuditFindingId(NamedEntityId):
    pass


class ManagementReviewId(DocumentedInformationId):
    pass


class NonconformityId(NamedEntityId):
    pass


class CorrectiveActionId(NamedEntityId):
    pass


class ImprovementOpportunityId(NamedEntityId):
    pass


class ThirdPartyRelationshipId(NamedEntityId):
    pass


class SupplierRelationshipId(ThirdPartyRelationshipId):
    pass


class CustomerRelationshipId(ThirdPartyRelationshipId):
    pass


class AISystemEventId(NamedEntityId):
    pass


class AIIncidentId(NamedEntityId):
    pass


class ConcernReportId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Abstract base class for all entities with an identifier, name, and description. Provides common identification and
    documentation slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["NamedEntity"]
    class_class_curie: ClassVar[str] = "iso42001:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = ISO42001.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: str = None
    description: Optional[str] = None
    created_date: Optional[Union[str, XSDDate]] = None
    modified_date: Optional[Union[str, XSDDate]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.created_date is not None and not isinstance(self.created_date, XSDDate):
            self.created_date = XSDDate(self.created_date)

        if self.modified_date is not None and not isinstance(self.modified_date, XSDDate):
            self.modified_date = XSDDate(self.modified_date)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentedInformation(NamedEntity):
    """
    Abstract class for documented information per Clause 7.5. Captures metadata required for document control under
    the AIMS.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["DocumentedInformation"]
    class_class_curie: ClassVar[str] = "iso42001:DocumentedInformation"
    class_name: ClassVar[str] = "DocumentedInformation"
    class_model_uri: ClassVar[URIRef] = ISO42001.DocumentedInformation

    id: Union[str, DocumentedInformationId] = None
    name: str = None
    document_type: Optional[Union[str, "DocumentType"]] = None
    document_reference: Optional[str] = None
    author: Optional[str] = None
    owner: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[Union[str, XSDDate]] = None
    effective_date: Optional[Union[str, XSDDate]] = None
    review_date: Optional[Union[str, XSDDate]] = None
    status: Optional[str] = None
    classification: Optional[str] = None
    retention_period: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.document_type is not None and not isinstance(self.document_type, DocumentType):
            self.document_type = DocumentType(self.document_type)

        if self.document_reference is not None and not isinstance(self.document_reference, str):
            self.document_reference = str(self.document_reference)

        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.owner is not None and not isinstance(self.owner, str):
            self.owner = str(self.owner)

        if self.approved_by is not None and not isinstance(self.approved_by, str):
            self.approved_by = str(self.approved_by)

        if self.approved_date is not None and not isinstance(self.approved_date, XSDDate):
            self.approved_date = XSDDate(self.approved_date)

        if self.effective_date is not None and not isinstance(self.effective_date, XSDDate):
            self.effective_date = XSDDate(self.effective_date)

        if self.review_date is not None and not isinstance(self.review_date, XSDDate):
            self.review_date = XSDDate(self.review_date)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        if self.retention_period is not None and not isinstance(self.retention_period, str):
            self.retention_period = str(self.retention_period)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIManagementSystem(NamedEntity):
    """
    Top-level container representing an organization's complete AI Management System (AIMS) per ISO/IEC 42001:2023.
    Aggregates all components required to support the AIMS lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIManagementSystem"]
    class_class_curie: ClassVar[str] = "iso42001:AIManagementSystem"
    class_name: ClassVar[str] = "AIManagementSystem"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIManagementSystem

    id: Union[str, AIManagementSystemId] = None
    name: str = None
    organization: Optional[Union[str, OrganizationId]] = None
    scope_statement: Optional[str] = None
    scope_boundaries: Optional[Union[str, list[str]]] = empty_list()
    scope_exclusions: Optional[Union[str, list[str]]] = empty_list()
    context_internal_issues: Optional[Union[str, list[str]]] = empty_list()
    context_external_issues: Optional[Union[str, list[str]]] = empty_list()
    organizational_roles_with_ai: Optional[Union[Union[str, "AIOrganizationalRole"], list[Union[str, "AIOrganizationalRole"]]]] = empty_list()
    integrated_management_systems: Optional[Union[Union[str, "RelatedManagementSystem"], list[Union[str, "RelatedManagementSystem"]]]] = empty_list()
    top_management: Optional[str] = None
    governing_body: Optional[str] = None
    leadership_commitment_evidence: Optional[Union[str, list[str]]] = empty_list()
    planned_changes: Optional[Union[str, list[str]]] = empty_list()
    interested_parties: Optional[Union[Union[str, InterestedPartyId], list[Union[str, InterestedPartyId]]]] = empty_list()
    ai_policy: Optional[Union[str, AIPolicyId]] = None
    ai_objectives: Optional[Union[Union[str, AIObjectiveId], list[Union[str, AIObjectiveId]]]] = empty_list()
    ai_risk_assessment_process: Optional[Union[str, AIRiskAssessmentProcessId]] = None
    ai_risk_treatment_process: Optional[Union[str, AIRiskTreatmentProcessId]] = None
    ai_system_impact_assessment_process: Optional[Union[str, AISystemImpactAssessmentProcessId]] = None
    statement_of_applicability: Optional[Union[str, StatementOfApplicabilityId]] = None
    reference_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    ai_systems: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    roles: Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]] = empty_list()
    resources: Optional[Union[Union[str, ResourceId], list[Union[str, ResourceId]]]] = empty_list()
    competence_records: Optional[Union[Union[str, CompetenceRecordId], list[Union[str, CompetenceRecordId]]]] = empty_list()
    awareness_program: Optional[Union[str, AwarenessProgramId]] = None
    communication_plan: Optional[Union[str, CommunicationPlanId]] = None
    documented_information_register: Optional[Union[Union[str, DocumentedInformationId], list[Union[str, DocumentedInformationId]]]] = empty_list()
    operational_procedures: Optional[Union[Union[str, OperationalProcedureId], list[Union[str, OperationalProcedureId]]]] = empty_list()
    ai_risk_assessments: Optional[Union[Union[str, AIRiskAssessmentId], list[Union[str, AIRiskAssessmentId]]]] = empty_list()
    ai_risk_treatment_plans: Optional[Union[Union[str, AIRiskTreatmentPlanId], list[Union[str, AIRiskTreatmentPlanId]]]] = empty_list()
    ai_system_impact_assessments: Optional[Union[Union[str, AISystemImpactAssessmentId], list[Union[str, AISystemImpactAssessmentId]]]] = empty_list()
    monitoring_program: Optional[Union[str, MonitoringProgramId]] = None
    internal_audits: Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]] = empty_list()
    management_reviews: Optional[Union[Union[str, ManagementReviewId], list[Union[str, ManagementReviewId]]]] = empty_list()
    nonconformities: Optional[Union[Union[str, NonconformityId], list[Union[str, NonconformityId]]]] = empty_list()
    corrective_actions: Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]] = empty_list()
    improvements: Optional[Union[Union[str, ImprovementOpportunityId], list[Union[str, ImprovementOpportunityId]]]] = empty_list()
    third_party_relationships: Optional[Union[Union[str, ThirdPartyRelationshipId], list[Union[str, ThirdPartyRelationshipId]]]] = empty_list()
    certification_status: Optional[str] = None
    certification_body: Optional[str] = None
    certification_date: Optional[Union[str, XSDDate]] = None
    recertification_date: Optional[Union[str, XSDDate]] = None
    ai_system_events: Optional[Union[Union[str, AISystemEventId], list[Union[str, AISystemEventId]]]] = empty_list()
    ai_incidents: Optional[Union[Union[str, AIIncidentId], list[Union[str, AIIncidentId]]]] = empty_list()
    concern_reports: Optional[Union[Union[str, ConcernReportId], list[Union[str, ConcernReportId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIManagementSystemId):
            self.id = AIManagementSystemId(self.id)

        if self.organization is not None and not isinstance(self.organization, OrganizationId):
            self.organization = OrganizationId(self.organization)

        if self.scope_statement is not None and not isinstance(self.scope_statement, str):
            self.scope_statement = str(self.scope_statement)

        if not isinstance(self.scope_boundaries, list):
            self.scope_boundaries = [self.scope_boundaries] if self.scope_boundaries is not None else []
        self.scope_boundaries = [v if isinstance(v, str) else str(v) for v in self.scope_boundaries]

        if not isinstance(self.scope_exclusions, list):
            self.scope_exclusions = [self.scope_exclusions] if self.scope_exclusions is not None else []
        self.scope_exclusions = [v if isinstance(v, str) else str(v) for v in self.scope_exclusions]

        if not isinstance(self.context_internal_issues, list):
            self.context_internal_issues = [self.context_internal_issues] if self.context_internal_issues is not None else []
        self.context_internal_issues = [v if isinstance(v, str) else str(v) for v in self.context_internal_issues]

        if not isinstance(self.context_external_issues, list):
            self.context_external_issues = [self.context_external_issues] if self.context_external_issues is not None else []
        self.context_external_issues = [v if isinstance(v, str) else str(v) for v in self.context_external_issues]

        if not isinstance(self.organizational_roles_with_ai, list):
            self.organizational_roles_with_ai = [self.organizational_roles_with_ai] if self.organizational_roles_with_ai is not None else []
        self.organizational_roles_with_ai = [v if isinstance(v, AIOrganizationalRole) else AIOrganizationalRole(v) for v in self.organizational_roles_with_ai]

        if not isinstance(self.integrated_management_systems, list):
            self.integrated_management_systems = [self.integrated_management_systems] if self.integrated_management_systems is not None else []
        self.integrated_management_systems = [v if isinstance(v, RelatedManagementSystem) else RelatedManagementSystem(v) for v in self.integrated_management_systems]

        if self.top_management is not None and not isinstance(self.top_management, str):
            self.top_management = str(self.top_management)

        if self.governing_body is not None and not isinstance(self.governing_body, str):
            self.governing_body = str(self.governing_body)

        if not isinstance(self.leadership_commitment_evidence, list):
            self.leadership_commitment_evidence = [self.leadership_commitment_evidence] if self.leadership_commitment_evidence is not None else []
        self.leadership_commitment_evidence = [v if isinstance(v, str) else str(v) for v in self.leadership_commitment_evidence]

        if not isinstance(self.planned_changes, list):
            self.planned_changes = [self.planned_changes] if self.planned_changes is not None else []
        self.planned_changes = [v if isinstance(v, str) else str(v) for v in self.planned_changes]

        if not isinstance(self.interested_parties, list):
            self.interested_parties = [self.interested_parties] if self.interested_parties is not None else []
        self.interested_parties = [v if isinstance(v, InterestedPartyId) else InterestedPartyId(v) for v in self.interested_parties]

        if self.ai_policy is not None and not isinstance(self.ai_policy, AIPolicyId):
            self.ai_policy = AIPolicyId(self.ai_policy)

        if not isinstance(self.ai_objectives, list):
            self.ai_objectives = [self.ai_objectives] if self.ai_objectives is not None else []
        self.ai_objectives = [v if isinstance(v, AIObjectiveId) else AIObjectiveId(v) for v in self.ai_objectives]

        if self.ai_risk_assessment_process is not None and not isinstance(self.ai_risk_assessment_process, AIRiskAssessmentProcessId):
            self.ai_risk_assessment_process = AIRiskAssessmentProcessId(self.ai_risk_assessment_process)

        if self.ai_risk_treatment_process is not None and not isinstance(self.ai_risk_treatment_process, AIRiskTreatmentProcessId):
            self.ai_risk_treatment_process = AIRiskTreatmentProcessId(self.ai_risk_treatment_process)

        if self.ai_system_impact_assessment_process is not None and not isinstance(self.ai_system_impact_assessment_process, AISystemImpactAssessmentProcessId):
            self.ai_system_impact_assessment_process = AISystemImpactAssessmentProcessId(self.ai_system_impact_assessment_process)

        if self.statement_of_applicability is not None and not isinstance(self.statement_of_applicability, StatementOfApplicabilityId):
            self.statement_of_applicability = StatementOfApplicabilityId(self.statement_of_applicability)

        if not isinstance(self.reference_controls, list):
            self.reference_controls = [self.reference_controls] if self.reference_controls is not None else []
        self.reference_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.reference_controls]

        if not isinstance(self.ai_systems, list):
            self.ai_systems = [self.ai_systems] if self.ai_systems is not None else []
        self.ai_systems = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.ai_systems]

        if not isinstance(self.roles, list):
            self.roles = [self.roles] if self.roles is not None else []
        self.roles = [v if isinstance(v, RoleId) else RoleId(v) for v in self.roles]

        if not isinstance(self.resources, list):
            self.resources = [self.resources] if self.resources is not None else []
        self.resources = [v if isinstance(v, ResourceId) else ResourceId(v) for v in self.resources]

        if not isinstance(self.competence_records, list):
            self.competence_records = [self.competence_records] if self.competence_records is not None else []
        self.competence_records = [v if isinstance(v, CompetenceRecordId) else CompetenceRecordId(v) for v in self.competence_records]

        if self.awareness_program is not None and not isinstance(self.awareness_program, AwarenessProgramId):
            self.awareness_program = AwarenessProgramId(self.awareness_program)

        if self.communication_plan is not None and not isinstance(self.communication_plan, CommunicationPlanId):
            self.communication_plan = CommunicationPlanId(self.communication_plan)

        if not isinstance(self.documented_information_register, list):
            self.documented_information_register = [self.documented_information_register] if self.documented_information_register is not None else []
        self.documented_information_register = [v if isinstance(v, DocumentedInformationId) else DocumentedInformationId(v) for v in self.documented_information_register]

        if not isinstance(self.operational_procedures, list):
            self.operational_procedures = [self.operational_procedures] if self.operational_procedures is not None else []
        self.operational_procedures = [v if isinstance(v, OperationalProcedureId) else OperationalProcedureId(v) for v in self.operational_procedures]

        if not isinstance(self.ai_risk_assessments, list):
            self.ai_risk_assessments = [self.ai_risk_assessments] if self.ai_risk_assessments is not None else []
        self.ai_risk_assessments = [v if isinstance(v, AIRiskAssessmentId) else AIRiskAssessmentId(v) for v in self.ai_risk_assessments]

        if not isinstance(self.ai_risk_treatment_plans, list):
            self.ai_risk_treatment_plans = [self.ai_risk_treatment_plans] if self.ai_risk_treatment_plans is not None else []
        self.ai_risk_treatment_plans = [v if isinstance(v, AIRiskTreatmentPlanId) else AIRiskTreatmentPlanId(v) for v in self.ai_risk_treatment_plans]

        if not isinstance(self.ai_system_impact_assessments, list):
            self.ai_system_impact_assessments = [self.ai_system_impact_assessments] if self.ai_system_impact_assessments is not None else []
        self.ai_system_impact_assessments = [v if isinstance(v, AISystemImpactAssessmentId) else AISystemImpactAssessmentId(v) for v in self.ai_system_impact_assessments]

        if self.monitoring_program is not None and not isinstance(self.monitoring_program, MonitoringProgramId):
            self.monitoring_program = MonitoringProgramId(self.monitoring_program)

        if not isinstance(self.internal_audits, list):
            self.internal_audits = [self.internal_audits] if self.internal_audits is not None else []
        self.internal_audits = [v if isinstance(v, InternalAuditId) else InternalAuditId(v) for v in self.internal_audits]

        if not isinstance(self.management_reviews, list):
            self.management_reviews = [self.management_reviews] if self.management_reviews is not None else []
        self.management_reviews = [v if isinstance(v, ManagementReviewId) else ManagementReviewId(v) for v in self.management_reviews]

        if not isinstance(self.nonconformities, list):
            self.nonconformities = [self.nonconformities] if self.nonconformities is not None else []
        self.nonconformities = [v if isinstance(v, NonconformityId) else NonconformityId(v) for v in self.nonconformities]

        if not isinstance(self.corrective_actions, list):
            self.corrective_actions = [self.corrective_actions] if self.corrective_actions is not None else []
        self.corrective_actions = [v if isinstance(v, CorrectiveActionId) else CorrectiveActionId(v) for v in self.corrective_actions]

        if not isinstance(self.improvements, list):
            self.improvements = [self.improvements] if self.improvements is not None else []
        self.improvements = [v if isinstance(v, ImprovementOpportunityId) else ImprovementOpportunityId(v) for v in self.improvements]

        if not isinstance(self.third_party_relationships, list):
            self.third_party_relationships = [self.third_party_relationships] if self.third_party_relationships is not None else []
        self.third_party_relationships = [v if isinstance(v, ThirdPartyRelationshipId) else ThirdPartyRelationshipId(v) for v in self.third_party_relationships]

        if self.certification_status is not None and not isinstance(self.certification_status, str):
            self.certification_status = str(self.certification_status)

        if self.certification_body is not None and not isinstance(self.certification_body, str):
            self.certification_body = str(self.certification_body)

        if self.certification_date is not None and not isinstance(self.certification_date, XSDDate):
            self.certification_date = XSDDate(self.certification_date)

        if self.recertification_date is not None and not isinstance(self.recertification_date, XSDDate):
            self.recertification_date = XSDDate(self.recertification_date)

        if not isinstance(self.ai_system_events, list):
            self.ai_system_events = [self.ai_system_events] if self.ai_system_events is not None else []
        self.ai_system_events = [v if isinstance(v, AISystemEventId) else AISystemEventId(v) for v in self.ai_system_events]

        if not isinstance(self.ai_incidents, list):
            self.ai_incidents = [self.ai_incidents] if self.ai_incidents is not None else []
        self.ai_incidents = [v if isinstance(v, AIIncidentId) else AIIncidentId(v) for v in self.ai_incidents]

        if not isinstance(self.concern_reports, list):
            self.concern_reports = [self.concern_reports] if self.concern_reports is not None else []
        self.concern_reports = [v if isinstance(v, ConcernReportId) else ConcernReportId(v) for v in self.concern_reports]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(NamedEntity):
    """
    The organization establishing and operating the AIMS. Captures the context required by Clause 4.1, including the
    organization's role(s) with respect to AI systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["Organization"]
    class_class_curie: ClassVar[str] = "iso42001:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ISO42001.Organization

    id: Union[str, OrganizationId] = None
    name: str = None
    legal_name: Optional[str] = None
    trading_names: Optional[Union[str, list[str]]] = empty_list()
    organization_type: Optional[str] = None
    industry_sector: Optional[str] = None
    sector_domains: Optional[Union[Union[str, "SectorDomain"], list[Union[str, "SectorDomain"]]]] = empty_list()
    size_category: Optional[str] = None
    employee_count: Optional[int] = None
    geographic_locations: Optional[Union[str, list[str]]] = empty_list()
    regulatory_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    parent_organization: Optional[str] = None
    subsidiaries: Optional[Union[str, list[str]]] = empty_list()
    ai_roles: Optional[Union[Union[str, "AIOrganizationalRole"], list[Union[str, "AIOrganizationalRole"]]]] = empty_list()
    climate_change_relevant: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.legal_name is not None and not isinstance(self.legal_name, str):
            self.legal_name = str(self.legal_name)

        if not isinstance(self.trading_names, list):
            self.trading_names = [self.trading_names] if self.trading_names is not None else []
        self.trading_names = [v if isinstance(v, str) else str(v) for v in self.trading_names]

        if self.organization_type is not None and not isinstance(self.organization_type, str):
            self.organization_type = str(self.organization_type)

        if self.industry_sector is not None and not isinstance(self.industry_sector, str):
            self.industry_sector = str(self.industry_sector)

        if not isinstance(self.sector_domains, list):
            self.sector_domains = [self.sector_domains] if self.sector_domains is not None else []
        self.sector_domains = [v if isinstance(v, SectorDomain) else SectorDomain(v) for v in self.sector_domains]

        if self.size_category is not None and not isinstance(self.size_category, str):
            self.size_category = str(self.size_category)

        if self.employee_count is not None and not isinstance(self.employee_count, int):
            self.employee_count = int(self.employee_count)

        if not isinstance(self.geographic_locations, list):
            self.geographic_locations = [self.geographic_locations] if self.geographic_locations is not None else []
        self.geographic_locations = [v if isinstance(v, str) else str(v) for v in self.geographic_locations]

        if not isinstance(self.regulatory_jurisdictions, list):
            self.regulatory_jurisdictions = [self.regulatory_jurisdictions] if self.regulatory_jurisdictions is not None else []
        self.regulatory_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.regulatory_jurisdictions]

        if self.parent_organization is not None and not isinstance(self.parent_organization, str):
            self.parent_organization = str(self.parent_organization)

        if not isinstance(self.subsidiaries, list):
            self.subsidiaries = [self.subsidiaries] if self.subsidiaries is not None else []
        self.subsidiaries = [v if isinstance(v, str) else str(v) for v in self.subsidiaries]

        if not isinstance(self.ai_roles, list):
            self.ai_roles = [self.ai_roles] if self.ai_roles is not None else []
        self.ai_roles = [v if isinstance(v, AIOrganizationalRole) else AIOrganizationalRole(v) for v in self.ai_roles]

        if self.climate_change_relevant is not None and not isinstance(self.climate_change_relevant, Bool):
            self.climate_change_relevant = Bool(self.climate_change_relevant)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterestedParty(NamedEntity):
    """
    A stakeholder whose needs and expectations are relevant to the AIMS per Clause 4.2. Includes internal and external
    parties such as users, regulators, partners, suppliers, customers, AI subjects, and relevant authorities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["InterestedParty"]
    class_class_curie: ClassVar[str] = "iso42001:InterestedParty"
    class_name: ClassVar[str] = "InterestedParty"
    class_model_uri: ClassVar[URIRef] = ISO42001.InterestedParty

    id: Union[str, InterestedPartyId] = None
    name: str = None
    party_type: Optional[str] = None
    relationship: Optional[str] = None
    requirements: Optional[Union[str, list[str]]] = empty_list()
    communication_needs: Optional[str] = None
    contact_information: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InterestedPartyId):
            self.id = InterestedPartyId(self.id)

        if self.party_type is not None and not isinstance(self.party_type, str):
            self.party_type = str(self.party_type)

        if self.relationship is not None and not isinstance(self.relationship, str):
            self.relationship = str(self.relationship)

        if not isinstance(self.requirements, list):
            self.requirements = [self.requirements] if self.requirements is not None else []
        self.requirements = [v if isinstance(v, str) else str(v) for v in self.requirements]

        if self.communication_needs is not None and not isinstance(self.communication_needs, str):
            self.communication_needs = str(self.communication_needs)

        if self.contact_information is not None and not isinstance(self.contact_information, str):
            self.contact_information = str(self.contact_information)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIPolicy(DocumentedInformation):
    """
    The AI policy established by top management per Clause 5.2. Provides a framework for setting AI objectives and
    demonstrates commitment to responsible AI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIPolicy"]
    class_class_curie: ClassVar[str] = "iso42001:AIPolicy"
    class_name: ClassVar[str] = "AIPolicy"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIPolicy

    id: Union[str, AIPolicyId] = None
    name: str = None
    policy_statement: Optional[str] = None
    policy_objectives_framework: Optional[str] = None
    commitment_statements: Optional[Union[str, list[str]]] = empty_list()
    applicability_statement: Optional[str] = None
    communication_date: Optional[Union[str, XSDDate]] = None
    acknowledgment_required: Optional[Union[bool, Bool]] = None
    related_topic_policies: Optional[Union[Union[str, TopicSpecificPolicyId], list[Union[str, TopicSpecificPolicyId]]]] = empty_list()
    last_policy_review_date: Optional[Union[str, XSDDate]] = None
    next_policy_review_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIPolicyId):
            self.id = AIPolicyId(self.id)

        if self.policy_statement is not None and not isinstance(self.policy_statement, str):
            self.policy_statement = str(self.policy_statement)

        if self.policy_objectives_framework is not None and not isinstance(self.policy_objectives_framework, str):
            self.policy_objectives_framework = str(self.policy_objectives_framework)

        if not isinstance(self.commitment_statements, list):
            self.commitment_statements = [self.commitment_statements] if self.commitment_statements is not None else []
        self.commitment_statements = [v if isinstance(v, str) else str(v) for v in self.commitment_statements]

        if self.applicability_statement is not None and not isinstance(self.applicability_statement, str):
            self.applicability_statement = str(self.applicability_statement)

        if self.communication_date is not None and not isinstance(self.communication_date, XSDDate):
            self.communication_date = XSDDate(self.communication_date)

        if self.acknowledgment_required is not None and not isinstance(self.acknowledgment_required, Bool):
            self.acknowledgment_required = Bool(self.acknowledgment_required)

        if not isinstance(self.related_topic_policies, list):
            self.related_topic_policies = [self.related_topic_policies] if self.related_topic_policies is not None else []
        self.related_topic_policies = [v if isinstance(v, TopicSpecificPolicyId) else TopicSpecificPolicyId(v) for v in self.related_topic_policies]

        if self.last_policy_review_date is not None and not isinstance(self.last_policy_review_date, XSDDate):
            self.last_policy_review_date = XSDDate(self.last_policy_review_date)

        if self.next_policy_review_date is not None and not isinstance(self.next_policy_review_date, XSDDate):
            self.next_policy_review_date = XSDDate(self.next_policy_review_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TopicSpecificPolicy(DocumentedInformation):
    """
    A topic-specific policy supporting the overarching AI policy, for example covering data governance, fairness,
    transparency, supplier use, or human oversight of AI systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["TopicSpecificPolicy"]
    class_class_curie: ClassVar[str] = "iso42001:TopicSpecificPolicy"
    class_name: ClassVar[str] = "TopicSpecificPolicy"
    class_model_uri: ClassVar[URIRef] = ISO42001.TopicSpecificPolicy

    id: Union[str, TopicSpecificPolicyId] = None
    name: str = None
    topic_area: Optional[str] = None
    parent_policy: Optional[Union[str, AIPolicyId]] = None
    applicable_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    target_audience: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TopicSpecificPolicyId):
            self.id = TopicSpecificPolicyId(self.id)

        if self.topic_area is not None and not isinstance(self.topic_area, str):
            self.topic_area = str(self.topic_area)

        if self.parent_policy is not None and not isinstance(self.parent_policy, AIPolicyId):
            self.parent_policy = AIPolicyId(self.parent_policy)

        if not isinstance(self.applicable_controls, list):
            self.applicable_controls = [self.applicable_controls] if self.applicable_controls is not None else []
        self.applicable_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.applicable_controls]

        if self.target_audience is not None and not isinstance(self.target_audience, str):
            self.target_audience = str(self.target_audience)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(NamedEntity):
    """
    An AI-related role with defined responsibilities and authorities per Clause 5.3 and Annex A.3.2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["Role"]
    class_class_curie: ClassVar[str] = "iso42001:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = ISO42001.Role

    id: Union[str, RoleId] = None
    name: str = None
    role_type: Optional[str] = None
    responsibilities: Optional[Union[str, list[str]]] = empty_list()
    authorities: Optional[Union[str, list[str]]] = empty_list()
    accountability: Optional[str] = None
    assigned_to: Optional[Union[str, list[str]]] = empty_list()
    delegation_rules: Optional[str] = None
    reporting_line: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RoleId):
            self.id = RoleId(self.id)

        if self.role_type is not None and not isinstance(self.role_type, str):
            self.role_type = str(self.role_type)

        if not isinstance(self.responsibilities, list):
            self.responsibilities = [self.responsibilities] if self.responsibilities is not None else []
        self.responsibilities = [v if isinstance(v, str) else str(v) for v in self.responsibilities]

        if not isinstance(self.authorities, list):
            self.authorities = [self.authorities] if self.authorities is not None else []
        self.authorities = [v if isinstance(v, str) else str(v) for v in self.authorities]

        if self.accountability is not None and not isinstance(self.accountability, str):
            self.accountability = str(self.accountability)

        if not isinstance(self.assigned_to, list):
            self.assigned_to = [self.assigned_to] if self.assigned_to is not None else []
        self.assigned_to = [v if isinstance(v, str) else str(v) for v in self.assigned_to]

        if self.delegation_rules is not None and not isinstance(self.delegation_rules, str):
            self.delegation_rules = str(self.delegation_rules)

        if self.reporting_line is not None and not isinstance(self.reporting_line, str):
            self.reporting_line = str(self.reporting_line)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIObjective(NamedEntity):
    """
    A measurable AI objective per Clause 6.2, established at relevant functions and levels and aligned with the AI
    policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIObjective"]
    class_class_curie: ClassVar[str] = "iso42001:AIObjective"
    class_name: ClassVar[str] = "AIObjective"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIObjective

    id: Union[str, AIObjectiveId] = None
    name: str = None
    objective_statement: Optional[str] = None
    objective_category: Optional[Union[str, "AIObjectiveCategory"]] = None
    target_value: Optional[str] = None
    current_value: Optional[str] = None
    metric_definition: Optional[str] = None
    measurement_method: Optional[str] = None
    measurement_frequency: Optional[str] = None
    responsible_role: Optional[Union[str, RoleId]] = None
    resources_required: Optional[str] = None
    target_date: Optional[Union[str, XSDDate]] = None
    achievement_status: Optional[str] = None
    related_risks: Optional[Union[Union[str, AIRiskId], list[Union[str, AIRiskId]]]] = empty_list()
    related_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    action_plan: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIObjectiveId):
            self.id = AIObjectiveId(self.id)

        if self.objective_statement is not None and not isinstance(self.objective_statement, str):
            self.objective_statement = str(self.objective_statement)

        if self.objective_category is not None and not isinstance(self.objective_category, AIObjectiveCategory):
            self.objective_category = AIObjectiveCategory(self.objective_category)

        if self.target_value is not None and not isinstance(self.target_value, str):
            self.target_value = str(self.target_value)

        if self.current_value is not None and not isinstance(self.current_value, str):
            self.current_value = str(self.current_value)

        if self.metric_definition is not None and not isinstance(self.metric_definition, str):
            self.metric_definition = str(self.metric_definition)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_frequency is not None and not isinstance(self.measurement_frequency, str):
            self.measurement_frequency = str(self.measurement_frequency)

        if self.responsible_role is not None and not isinstance(self.responsible_role, RoleId):
            self.responsible_role = RoleId(self.responsible_role)

        if self.resources_required is not None and not isinstance(self.resources_required, str):
            self.resources_required = str(self.resources_required)

        if self.target_date is not None and not isinstance(self.target_date, XSDDate):
            self.target_date = XSDDate(self.target_date)

        if self.achievement_status is not None and not isinstance(self.achievement_status, str):
            self.achievement_status = str(self.achievement_status)

        if not isinstance(self.related_risks, list):
            self.related_risks = [self.related_risks] if self.related_risks is not None else []
        self.related_risks = [v if isinstance(v, AIRiskId) else AIRiskId(v) for v in self.related_risks]

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.related_controls]

        if self.action_plan is not None and not isinstance(self.action_plan, str):
            self.action_plan = str(self.action_plan)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIRiskAssessmentProcess(DocumentedInformation):
    """
    The documented AI risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying,
    analysing, and evaluating AI risks. Aligned with ISO/IEC 23894.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIRiskAssessmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AIRiskAssessmentProcess"
    class_name: ClassVar[str] = "AIRiskAssessmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIRiskAssessmentProcess

    id: Union[str, AIRiskAssessmentProcessId] = None
    name: str = None
    risk_acceptance_criteria: Optional[str] = None
    assessment_criteria: Optional[str] = None
    assessment_methodology: Optional[str] = None
    likelihood_scale: Optional[str] = None
    impact_scale: Optional[str] = None
    risk_matrix: Optional[str] = None
    assessment_frequency: Optional[str] = None
    trigger_events: Optional[Union[str, list[str]]] = empty_list()
    alignment_with_ai_policy: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIRiskAssessmentProcessId):
            self.id = AIRiskAssessmentProcessId(self.id)

        if self.risk_acceptance_criteria is not None and not isinstance(self.risk_acceptance_criteria, str):
            self.risk_acceptance_criteria = str(self.risk_acceptance_criteria)

        if self.assessment_criteria is not None and not isinstance(self.assessment_criteria, str):
            self.assessment_criteria = str(self.assessment_criteria)

        if self.assessment_methodology is not None and not isinstance(self.assessment_methodology, str):
            self.assessment_methodology = str(self.assessment_methodology)

        if self.likelihood_scale is not None and not isinstance(self.likelihood_scale, str):
            self.likelihood_scale = str(self.likelihood_scale)

        if self.impact_scale is not None and not isinstance(self.impact_scale, str):
            self.impact_scale = str(self.impact_scale)

        if self.risk_matrix is not None and not isinstance(self.risk_matrix, str):
            self.risk_matrix = str(self.risk_matrix)

        if self.assessment_frequency is not None and not isinstance(self.assessment_frequency, str):
            self.assessment_frequency = str(self.assessment_frequency)

        if not isinstance(self.trigger_events, list):
            self.trigger_events = [self.trigger_events] if self.trigger_events is not None else []
        self.trigger_events = [v if isinstance(v, str) else str(v) for v in self.trigger_events]

        if self.alignment_with_ai_policy is not None and not isinstance(self.alignment_with_ai_policy, str):
            self.alignment_with_ai_policy = str(self.alignment_with_ai_policy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIRiskAssessment(DocumentedInformation):
    """
    An instance of AI risk assessment performed per Clause 8.2, identifying and evaluating AI risks at planned
    intervals or following significant change.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIRiskAssessment"]
    class_class_curie: ClassVar[str] = "iso42001:AIRiskAssessment"
    class_name: ClassVar[str] = "AIRiskAssessment"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIRiskAssessment

    id: Union[str, AIRiskAssessmentId] = None
    name: str = None
    assessment_scope: Optional[str] = None
    ai_systems_assessed: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    assessment_date: Optional[Union[str, XSDDate]] = None
    assessor: Optional[str] = None
    methodology_used: Optional[str] = None
    risks_identified: Optional[Union[Union[str, AIRiskId], list[Union[str, AIRiskId]]]] = empty_list()
    linked_impact_assessment: Optional[Union[str, AISystemImpactAssessmentId]] = None
    summary_findings: Optional[str] = None
    recommendations: Optional[Union[str, list[str]]] = empty_list()
    next_assessment_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIRiskAssessmentId):
            self.id = AIRiskAssessmentId(self.id)

        if self.assessment_scope is not None and not isinstance(self.assessment_scope, str):
            self.assessment_scope = str(self.assessment_scope)

        if not isinstance(self.ai_systems_assessed, list):
            self.ai_systems_assessed = [self.ai_systems_assessed] if self.ai_systems_assessed is not None else []
        self.ai_systems_assessed = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.ai_systems_assessed]

        if self.assessment_date is not None and not isinstance(self.assessment_date, XSDDate):
            self.assessment_date = XSDDate(self.assessment_date)

        if self.assessor is not None and not isinstance(self.assessor, str):
            self.assessor = str(self.assessor)

        if self.methodology_used is not None and not isinstance(self.methodology_used, str):
            self.methodology_used = str(self.methodology_used)

        if not isinstance(self.risks_identified, list):
            self.risks_identified = [self.risks_identified] if self.risks_identified is not None else []
        self.risks_identified = [v if isinstance(v, AIRiskId) else AIRiskId(v) for v in self.risks_identified]

        if self.linked_impact_assessment is not None and not isinstance(self.linked_impact_assessment, AISystemImpactAssessmentId):
            self.linked_impact_assessment = AISystemImpactAssessmentId(self.linked_impact_assessment)

        if self.summary_findings is not None and not isinstance(self.summary_findings, str):
            self.summary_findings = str(self.summary_findings)

        if not isinstance(self.recommendations, list):
            self.recommendations = [self.recommendations] if self.recommendations is not None else []
        self.recommendations = [v if isinstance(v, str) else str(v) for v in self.recommendations]

        if self.next_assessment_date is not None and not isinstance(self.next_assessment_date, XSDDate):
            self.next_assessment_date = XSDDate(self.next_assessment_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIRisk(NamedEntity):
    """
    An identified AI risk that may affect achievement of AI objectives, individuals, groups, or societies within the
    AIMS scope.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIRisk"]
    class_class_curie: ClassVar[str] = "iso42001:AIRisk"
    class_name: ClassVar[str] = "AIRisk"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIRisk

    id: Union[str, AIRiskId] = None
    name: str = None
    risk_source_category: Optional[Union[str, "AIRiskSourceCategory"]] = None
    risk_source_description: Optional[str] = None
    affected_ai_systems: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    affected_dimensions: Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]] = empty_list()
    risk_owner: Optional[str] = None
    likelihood: Optional[Union[str, "LikelihoodRating"]] = None
    impact: Optional[Union[str, "ImpactRating"]] = None
    inherent_risk_level: Optional[Union[str, "RiskLevel"]] = None
    existing_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    residual_risk_level: Optional[Union[str, "RiskLevel"]] = None
    risk_treatment_option: Optional[Union[str, "RiskTreatmentOption"]] = None
    treatment_priority: Optional[str] = None
    related_treatment_plan: Optional[Union[str, AIRiskTreatmentPlanId]] = None
    related_impact_assessment: Optional[Union[str, AISystemImpactAssessmentId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIRiskId):
            self.id = AIRiskId(self.id)

        if self.risk_source_category is not None and not isinstance(self.risk_source_category, AIRiskSourceCategory):
            self.risk_source_category = AIRiskSourceCategory(self.risk_source_category)

        if self.risk_source_description is not None and not isinstance(self.risk_source_description, str):
            self.risk_source_description = str(self.risk_source_description)

        if not isinstance(self.affected_ai_systems, list):
            self.affected_ai_systems = [self.affected_ai_systems] if self.affected_ai_systems is not None else []
        self.affected_ai_systems = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.affected_ai_systems]

        if not isinstance(self.affected_dimensions, list):
            self.affected_dimensions = [self.affected_dimensions] if self.affected_dimensions is not None else []
        self.affected_dimensions = [v if isinstance(v, ImpactAssessmentDimension) else ImpactAssessmentDimension(v) for v in self.affected_dimensions]

        if self.risk_owner is not None and not isinstance(self.risk_owner, str):
            self.risk_owner = str(self.risk_owner)

        if self.likelihood is not None and not isinstance(self.likelihood, LikelihoodRating):
            self.likelihood = LikelihoodRating(self.likelihood)

        if self.impact is not None and not isinstance(self.impact, ImpactRating):
            self.impact = ImpactRating(self.impact)

        if self.inherent_risk_level is not None and not isinstance(self.inherent_risk_level, RiskLevel):
            self.inherent_risk_level = RiskLevel(self.inherent_risk_level)

        if not isinstance(self.existing_controls, list):
            self.existing_controls = [self.existing_controls] if self.existing_controls is not None else []
        self.existing_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.existing_controls]

        if self.residual_risk_level is not None and not isinstance(self.residual_risk_level, RiskLevel):
            self.residual_risk_level = RiskLevel(self.residual_risk_level)

        if self.risk_treatment_option is not None and not isinstance(self.risk_treatment_option, RiskTreatmentOption):
            self.risk_treatment_option = RiskTreatmentOption(self.risk_treatment_option)

        if self.treatment_priority is not None and not isinstance(self.treatment_priority, str):
            self.treatment_priority = str(self.treatment_priority)

        if self.related_treatment_plan is not None and not isinstance(self.related_treatment_plan, AIRiskTreatmentPlanId):
            self.related_treatment_plan = AIRiskTreatmentPlanId(self.related_treatment_plan)

        if self.related_impact_assessment is not None and not isinstance(self.related_impact_assessment, AISystemImpactAssessmentId):
            self.related_impact_assessment = AISystemImpactAssessmentId(self.related_impact_assessment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIRiskTreatmentProcess(DocumentedInformation):
    """
    The documented AI risk treatment process per Clause 6.1.3, defining how treatment options are selected, how Annex
    A controls are considered, and how the Statement of Applicability is produced.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIRiskTreatmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AIRiskTreatmentProcess"
    class_name: ClassVar[str] = "AIRiskTreatmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIRiskTreatmentProcess

    id: Union[str, AIRiskTreatmentProcessId] = None
    name: str = None
    treatment_options_guidance: Optional[str] = None
    control_selection_criteria: Optional[str] = None
    soa_template: Optional[str] = None
    approval_workflow: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIRiskTreatmentProcessId):
            self.id = AIRiskTreatmentProcessId(self.id)

        if self.treatment_options_guidance is not None and not isinstance(self.treatment_options_guidance, str):
            self.treatment_options_guidance = str(self.treatment_options_guidance)

        if self.control_selection_criteria is not None and not isinstance(self.control_selection_criteria, str):
            self.control_selection_criteria = str(self.control_selection_criteria)

        if self.soa_template is not None and not isinstance(self.soa_template, str):
            self.soa_template = str(self.soa_template)

        if self.approval_workflow is not None and not isinstance(self.approval_workflow, str):
            self.approval_workflow = str(self.approval_workflow)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIRiskTreatmentPlan(DocumentedInformation):
    """
    A plan documenting planned actions to address identified AI risks through selected controls. Requires approval by
    designated management per Clause 6.1.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIRiskTreatmentPlan"]
    class_class_curie: ClassVar[str] = "iso42001:AIRiskTreatmentPlan"
    class_name: ClassVar[str] = "AIRiskTreatmentPlan"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIRiskTreatmentPlan

    id: Union[str, AIRiskTreatmentPlanId] = None
    name: str = None
    plan_scope: Optional[str] = None
    risks_addressed: Optional[Union[Union[str, AIRiskId], list[Union[str, AIRiskId]]]] = empty_list()
    treatment_actions: Optional[Union[str, list[str]]] = empty_list()
    controls_to_implement: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    resources_required: Optional[str] = None
    responsible_parties: Optional[Union[str, list[str]]] = empty_list()
    implementation_timeline: Optional[str] = None
    risk_owner_approval: Optional[str] = None
    approved_date: Optional[Union[str, XSDDate]] = None
    residual_risk_acceptance: Optional[str] = None
    implementation_status: Optional[Union[str, "ImplementationStatus"]] = None
    completion_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIRiskTreatmentPlanId):
            self.id = AIRiskTreatmentPlanId(self.id)

        if self.plan_scope is not None and not isinstance(self.plan_scope, str):
            self.plan_scope = str(self.plan_scope)

        if not isinstance(self.risks_addressed, list):
            self.risks_addressed = [self.risks_addressed] if self.risks_addressed is not None else []
        self.risks_addressed = [v if isinstance(v, AIRiskId) else AIRiskId(v) for v in self.risks_addressed]

        if not isinstance(self.treatment_actions, list):
            self.treatment_actions = [self.treatment_actions] if self.treatment_actions is not None else []
        self.treatment_actions = [v if isinstance(v, str) else str(v) for v in self.treatment_actions]

        if not isinstance(self.controls_to_implement, list):
            self.controls_to_implement = [self.controls_to_implement] if self.controls_to_implement is not None else []
        self.controls_to_implement = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.controls_to_implement]

        if self.resources_required is not None and not isinstance(self.resources_required, str):
            self.resources_required = str(self.resources_required)

        if not isinstance(self.responsible_parties, list):
            self.responsible_parties = [self.responsible_parties] if self.responsible_parties is not None else []
        self.responsible_parties = [v if isinstance(v, str) else str(v) for v in self.responsible_parties]

        if self.implementation_timeline is not None and not isinstance(self.implementation_timeline, str):
            self.implementation_timeline = str(self.implementation_timeline)

        if self.risk_owner_approval is not None and not isinstance(self.risk_owner_approval, str):
            self.risk_owner_approval = str(self.risk_owner_approval)

        if self.approved_date is not None and not isinstance(self.approved_date, XSDDate):
            self.approved_date = XSDDate(self.approved_date)

        if self.residual_risk_acceptance is not None and not isinstance(self.residual_risk_acceptance, str):
            self.residual_risk_acceptance = str(self.residual_risk_acceptance)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(self.implementation_status)

        if self.completion_date is not None and not isinstance(self.completion_date, XSDDate):
            self.completion_date = XSDDate(self.completion_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISystemImpactAssessmentProcess(DocumentedInformation):
    """
    The documented process for assessing the potential consequences for individuals, groups, and societies arising
    from the development, provision, or use of AI systems per Clause 6.1.4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AISystemImpactAssessmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AISystemImpactAssessmentProcess"
    class_name: ClassVar[str] = "AISystemImpactAssessmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AISystemImpactAssessmentProcess

    id: Union[str, AISystemImpactAssessmentProcessId] = None
    name: str = None
    assessment_criteria: Optional[str] = None
    assessment_methodology: Optional[str] = None
    dimensions_in_scope: Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]] = empty_list()
    assessment_frequency: Optional[str] = None
    trigger_events: Optional[Union[str, list[str]]] = empty_list()
    linkage_to_risk_assessment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISystemImpactAssessmentProcessId):
            self.id = AISystemImpactAssessmentProcessId(self.id)

        if self.assessment_criteria is not None and not isinstance(self.assessment_criteria, str):
            self.assessment_criteria = str(self.assessment_criteria)

        if self.assessment_methodology is not None and not isinstance(self.assessment_methodology, str):
            self.assessment_methodology = str(self.assessment_methodology)

        if not isinstance(self.dimensions_in_scope, list):
            self.dimensions_in_scope = [self.dimensions_in_scope] if self.dimensions_in_scope is not None else []
        self.dimensions_in_scope = [v if isinstance(v, ImpactAssessmentDimension) else ImpactAssessmentDimension(v) for v in self.dimensions_in_scope]

        if self.assessment_frequency is not None and not isinstance(self.assessment_frequency, str):
            self.assessment_frequency = str(self.assessment_frequency)

        if not isinstance(self.trigger_events, list):
            self.trigger_events = [self.trigger_events] if self.trigger_events is not None else []
        self.trigger_events = [v if isinstance(v, str) else str(v) for v in self.trigger_events]

        if self.linkage_to_risk_assessment is not None and not isinstance(self.linkage_to_risk_assessment, str):
            self.linkage_to_risk_assessment = str(self.linkage_to_risk_assessment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISystemImpactAssessment(DocumentedInformation):
    """
    An instance of an AI system impact assessment performed per Clause 6.1.4 and Clause 8.4. Documents consequences of
    deployment, intended use, and foreseeable misuse on individuals, groups, and societies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AISystemImpactAssessment"]
    class_class_curie: ClassVar[str] = "iso42001:AISystemImpactAssessment"
    class_name: ClassVar[str] = "AISystemImpactAssessment"
    class_model_uri: ClassVar[URIRef] = ISO42001.AISystemImpactAssessment

    id: Union[str, AISystemImpactAssessmentId] = None
    name: str = None
    assessment_scope: Optional[str] = None
    ai_systems_assessed: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    assessment_date: Optional[Union[str, XSDDate]] = None
    assessor: Optional[str] = None
    technical_context: Optional[str] = None
    societal_context: Optional[str] = None
    applicable_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    dimensions_assessed: Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]] = empty_list()
    identified_consequences: Optional[Union[str, list[str]]] = empty_list()
    mitigations: Optional[Union[str, list[str]]] = empty_list()
    shared_with_parties: Optional[Union[str, list[str]]] = empty_list()
    next_assessment_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISystemImpactAssessmentId):
            self.id = AISystemImpactAssessmentId(self.id)

        if self.assessment_scope is not None and not isinstance(self.assessment_scope, str):
            self.assessment_scope = str(self.assessment_scope)

        if not isinstance(self.ai_systems_assessed, list):
            self.ai_systems_assessed = [self.ai_systems_assessed] if self.ai_systems_assessed is not None else []
        self.ai_systems_assessed = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.ai_systems_assessed]

        if self.assessment_date is not None and not isinstance(self.assessment_date, XSDDate):
            self.assessment_date = XSDDate(self.assessment_date)

        if self.assessor is not None and not isinstance(self.assessor, str):
            self.assessor = str(self.assessor)

        if self.technical_context is not None and not isinstance(self.technical_context, str):
            self.technical_context = str(self.technical_context)

        if self.societal_context is not None and not isinstance(self.societal_context, str):
            self.societal_context = str(self.societal_context)

        if not isinstance(self.applicable_jurisdictions, list):
            self.applicable_jurisdictions = [self.applicable_jurisdictions] if self.applicable_jurisdictions is not None else []
        self.applicable_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.applicable_jurisdictions]

        if not isinstance(self.dimensions_assessed, list):
            self.dimensions_assessed = [self.dimensions_assessed] if self.dimensions_assessed is not None else []
        self.dimensions_assessed = [v if isinstance(v, ImpactAssessmentDimension) else ImpactAssessmentDimension(v) for v in self.dimensions_assessed]

        if not isinstance(self.identified_consequences, list):
            self.identified_consequences = [self.identified_consequences] if self.identified_consequences is not None else []
        self.identified_consequences = [v if isinstance(v, str) else str(v) for v in self.identified_consequences]

        if not isinstance(self.mitigations, list):
            self.mitigations = [self.mitigations] if self.mitigations is not None else []
        self.mitigations = [v if isinstance(v, str) else str(v) for v in self.mitigations]

        if not isinstance(self.shared_with_parties, list):
            self.shared_with_parties = [self.shared_with_parties] if self.shared_with_parties is not None else []
        self.shared_with_parties = [v if isinstance(v, str) else str(v) for v in self.shared_with_parties]

        if self.next_assessment_date is not None and not isinstance(self.next_assessment_date, XSDDate):
            self.next_assessment_date = XSDDate(self.next_assessment_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatementOfApplicability(DocumentedInformation):
    """
    The Statement of Applicability (SoA) for the AIMS recording which Annex A controls apply, justification for
    inclusion or exclusion, and current implementation state per Clause 6.1.3 f).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["StatementOfApplicability"]
    class_class_curie: ClassVar[str] = "iso42001:StatementOfApplicability"
    class_name: ClassVar[str] = "StatementOfApplicability"
    class_model_uri: ClassVar[URIRef] = ISO42001.StatementOfApplicability

    id: Union[str, StatementOfApplicabilityId] = None
    name: str = None
    soa_entries: Optional[Union[Union[dict, "SoAEntry"], list[Union[dict, "SoAEntry"]]]] = empty_list()
    total_controls: Optional[int] = None
    implemented_count: Optional[int] = None
    planned_count: Optional[int] = None
    not_applicable_count: Optional[int] = None
    last_review_date: Optional[Union[str, XSDDate]] = None
    approved_by: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatementOfApplicabilityId):
            self.id = StatementOfApplicabilityId(self.id)

        if not isinstance(self.soa_entries, list):
            self.soa_entries = [self.soa_entries] if self.soa_entries is not None else []
        self.soa_entries = [v if isinstance(v, SoAEntry) else SoAEntry(**as_dict(v)) for v in self.soa_entries]

        if self.total_controls is not None and not isinstance(self.total_controls, int):
            self.total_controls = int(self.total_controls)

        if self.implemented_count is not None and not isinstance(self.implemented_count, int):
            self.implemented_count = int(self.implemented_count)

        if self.planned_count is not None and not isinstance(self.planned_count, int):
            self.planned_count = int(self.planned_count)

        if self.not_applicable_count is not None and not isinstance(self.not_applicable_count, int):
            self.not_applicable_count = int(self.not_applicable_count)

        if self.last_review_date is not None and not isinstance(self.last_review_date, XSDDate):
            self.last_review_date = XSDDate(self.last_review_date)

        if self.approved_by is not None and not isinstance(self.approved_by, str):
            self.approved_by = str(self.approved_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoAEntry(YAMLRoot):
    """
    A single entry in the AIMS Statement of Applicability documenting the applicability and implementation status of
    one reference control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["SoAEntry"]
    class_class_curie: ClassVar[str] = "iso42001:SoAEntry"
    class_name: ClassVar[str] = "SoAEntry"
    class_model_uri: ClassVar[URIRef] = ISO42001.SoAEntry

    control_reference: Optional[Union[str, AIReferenceControlId]] = None
    is_applicable: Optional[Union[bool, Bool]] = None
    inclusion_justification: Optional[str] = None
    exclusion_justification: Optional[str] = None
    implementation_status: Optional[Union[str, "ImplementationStatus"]] = None
    implementation_evidence: Optional[str] = None
    responsible_role: Optional[Union[str, RoleId]] = None
    target_implementation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.control_reference is not None and not isinstance(self.control_reference, AIReferenceControlId):
            self.control_reference = AIReferenceControlId(self.control_reference)

        if self.is_applicable is not None and not isinstance(self.is_applicable, Bool):
            self.is_applicable = Bool(self.is_applicable)

        if self.inclusion_justification is not None and not isinstance(self.inclusion_justification, str):
            self.inclusion_justification = str(self.inclusion_justification)

        if self.exclusion_justification is not None and not isinstance(self.exclusion_justification, str):
            self.exclusion_justification = str(self.exclusion_justification)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(self.implementation_status)

        if self.implementation_evidence is not None and not isinstance(self.implementation_evidence, str):
            self.implementation_evidence = str(self.implementation_evidence)

        if self.responsible_role is not None and not isinstance(self.responsible_role, RoleId):
            self.responsible_role = RoleId(self.responsible_role)

        if self.target_implementation_date is not None and not isinstance(self.target_implementation_date, XSDDate):
            self.target_implementation_date = XSDDate(self.target_implementation_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIReferenceControl(NamedEntity):
    """
    A reference control from Annex A of ISO/IEC 42001:2023. Controls are grouped into nine families (A.2 through A.10)
    and supported by implementation guidance in Annex B.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIReferenceControl"]
    class_class_curie: ClassVar[str] = "iso42001:AIReferenceControl"
    class_name: ClassVar[str] = "AIReferenceControl"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIReferenceControl

    id: Union[str, AIReferenceControlId] = None
    name: str = None
    control_id: Optional[str] = None
    control_title: Optional[str] = None
    control_family: Optional[Union[str, "AIControlFamily"]] = None
    control_text: Optional[str] = None
    implementation_guidance: Optional[str] = None
    related_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    applicable_risk_sources: Optional[Union[Union[str, "AIRiskSourceCategory"], list[Union[str, "AIRiskSourceCategory"]]]] = empty_list()
    applicable_objectives: Optional[Union[Union[str, "AIObjectiveCategory"], list[Union[str, "AIObjectiveCategory"]]]] = empty_list()
    control_owner: Optional[str] = None
    implementation_status: Optional[Union[str, "ImplementationStatus"]] = None
    implementation_date: Optional[Union[str, XSDDate]] = None
    effectiveness_rating: Optional[str] = None
    last_test_date: Optional[Union[str, XSDDate]] = None
    evidence_references: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIReferenceControlId):
            self.id = AIReferenceControlId(self.id)

        if self.control_id is not None and not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if self.control_title is not None and not isinstance(self.control_title, str):
            self.control_title = str(self.control_title)

        if self.control_family is not None and not isinstance(self.control_family, AIControlFamily):
            self.control_family = AIControlFamily(self.control_family)

        if self.control_text is not None and not isinstance(self.control_text, str):
            self.control_text = str(self.control_text)

        if self.implementation_guidance is not None and not isinstance(self.implementation_guidance, str):
            self.implementation_guidance = str(self.implementation_guidance)

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.related_controls]

        if not isinstance(self.applicable_risk_sources, list):
            self.applicable_risk_sources = [self.applicable_risk_sources] if self.applicable_risk_sources is not None else []
        self.applicable_risk_sources = [v if isinstance(v, AIRiskSourceCategory) else AIRiskSourceCategory(v) for v in self.applicable_risk_sources]

        if not isinstance(self.applicable_objectives, list):
            self.applicable_objectives = [self.applicable_objectives] if self.applicable_objectives is not None else []
        self.applicable_objectives = [v if isinstance(v, AIObjectiveCategory) else AIObjectiveCategory(v) for v in self.applicable_objectives]

        if self.control_owner is not None and not isinstance(self.control_owner, str):
            self.control_owner = str(self.control_owner)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(self.implementation_status)

        if self.implementation_date is not None and not isinstance(self.implementation_date, XSDDate):
            self.implementation_date = XSDDate(self.implementation_date)

        if self.effectiveness_rating is not None and not isinstance(self.effectiveness_rating, str):
            self.effectiveness_rating = str(self.effectiveness_rating)

        if self.last_test_date is not None and not isinstance(self.last_test_date, XSDDate):
            self.last_test_date = XSDDate(self.last_test_date)

        if not isinstance(self.evidence_references, list):
            self.evidence_references = [self.evidence_references] if self.evidence_references is not None else []
        self.evidence_references = [v if isinstance(v, str) else str(v) for v in self.evidence_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISystem(NamedEntity):
    """
    An AI system within the AIMS scope. Captures life cycle stage, intended use, applicable domains, and references to
    data and tooling resources, technical documentation, and impact assessments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AISystem"]
    class_class_curie: ClassVar[str] = "iso42001:AISystem"
    class_name: ClassVar[str] = "AISystem"
    class_model_uri: ClassVar[URIRef] = ISO42001.AISystem

    id: Union[str, AISystemId] = None
    name: str = None
    ai_system_purpose: Optional[str] = None
    intended_uses: Optional[Union[str, list[str]]] = empty_list()
    foreseeable_misuse: Optional[Union[str, list[str]]] = empty_list()
    application_domain: Optional[str] = None
    deployment_context: Optional[str] = None
    lifecycle_stage: Optional[Union[str, "AISystemLifecycleStage"]] = None
    organization_role: Optional[Union[str, "AIOrganizationalRole"]] = None
    autonomy_level: Optional[str] = None
    ml_approach: Optional[Union[str, "MLApproach"]] = None
    human_oversight_required: Optional[Union[bool, Bool]] = None
    human_oversight_description: Optional[str] = None
    human_oversight_stages: Optional[Union[Union[str, "AISystemLifecycleStage"], list[Union[str, "AISystemLifecycleStage"]]]] = empty_list()
    learning_mode: Optional[Union[str, "LearningParadigm"]] = None
    data_resources: Optional[Union[Union[str, DataResourceId], list[Union[str, DataResourceId]]]] = empty_list()
    tooling_resources: Optional[Union[Union[str, ToolingResourceId], list[Union[str, ToolingResourceId]]]] = empty_list()
    computing_resources: Optional[Union[Union[str, ComputingResourceId], list[Union[str, ComputingResourceId]]]] = empty_list()
    human_resources: Optional[Union[Union[str, HumanResourceId], list[Union[str, HumanResourceId]]]] = empty_list()
    technical_documentation: Optional[Union[str, list[str]]] = empty_list()
    event_log_policy: Optional[str] = None
    applicable_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    related_impact_assessments: Optional[Union[Union[str, AISystemImpactAssessmentId], list[Union[str, AISystemImpactAssessmentId]]]] = empty_list()
    supplier_relationships: Optional[Union[Union[str, SupplierRelationshipId], list[Union[str, SupplierRelationshipId]]]] = empty_list()
    customer_relationships: Optional[Union[Union[str, CustomerRelationshipId], list[Union[str, CustomerRelationshipId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISystemId):
            self.id = AISystemId(self.id)

        if self.ai_system_purpose is not None and not isinstance(self.ai_system_purpose, str):
            self.ai_system_purpose = str(self.ai_system_purpose)

        if not isinstance(self.intended_uses, list):
            self.intended_uses = [self.intended_uses] if self.intended_uses is not None else []
        self.intended_uses = [v if isinstance(v, str) else str(v) for v in self.intended_uses]

        if not isinstance(self.foreseeable_misuse, list):
            self.foreseeable_misuse = [self.foreseeable_misuse] if self.foreseeable_misuse is not None else []
        self.foreseeable_misuse = [v if isinstance(v, str) else str(v) for v in self.foreseeable_misuse]

        if self.application_domain is not None and not isinstance(self.application_domain, str):
            self.application_domain = str(self.application_domain)

        if self.deployment_context is not None and not isinstance(self.deployment_context, str):
            self.deployment_context = str(self.deployment_context)

        if self.lifecycle_stage is not None and not isinstance(self.lifecycle_stage, AISystemLifecycleStage):
            self.lifecycle_stage = AISystemLifecycleStage(self.lifecycle_stage)

        if self.organization_role is not None and not isinstance(self.organization_role, AIOrganizationalRole):
            self.organization_role = AIOrganizationalRole(self.organization_role)

        if self.autonomy_level is not None and not isinstance(self.autonomy_level, str):
            self.autonomy_level = str(self.autonomy_level)

        if self.ml_approach is not None and not isinstance(self.ml_approach, MLApproach):
            self.ml_approach = MLApproach(self.ml_approach)

        if self.human_oversight_required is not None and not isinstance(self.human_oversight_required, Bool):
            self.human_oversight_required = Bool(self.human_oversight_required)

        if self.human_oversight_description is not None and not isinstance(self.human_oversight_description, str):
            self.human_oversight_description = str(self.human_oversight_description)

        if not isinstance(self.human_oversight_stages, list):
            self.human_oversight_stages = [self.human_oversight_stages] if self.human_oversight_stages is not None else []
        self.human_oversight_stages = [v if isinstance(v, AISystemLifecycleStage) else AISystemLifecycleStage(v) for v in self.human_oversight_stages]

        if self.learning_mode is not None and not isinstance(self.learning_mode, LearningParadigm):
            self.learning_mode = LearningParadigm(self.learning_mode)

        if not isinstance(self.data_resources, list):
            self.data_resources = [self.data_resources] if self.data_resources is not None else []
        self.data_resources = [v if isinstance(v, DataResourceId) else DataResourceId(v) for v in self.data_resources]

        if not isinstance(self.tooling_resources, list):
            self.tooling_resources = [self.tooling_resources] if self.tooling_resources is not None else []
        self.tooling_resources = [v if isinstance(v, ToolingResourceId) else ToolingResourceId(v) for v in self.tooling_resources]

        if not isinstance(self.computing_resources, list):
            self.computing_resources = [self.computing_resources] if self.computing_resources is not None else []
        self.computing_resources = [v if isinstance(v, ComputingResourceId) else ComputingResourceId(v) for v in self.computing_resources]

        if not isinstance(self.human_resources, list):
            self.human_resources = [self.human_resources] if self.human_resources is not None else []
        self.human_resources = [v if isinstance(v, HumanResourceId) else HumanResourceId(v) for v in self.human_resources]

        if not isinstance(self.technical_documentation, list):
            self.technical_documentation = [self.technical_documentation] if self.technical_documentation is not None else []
        self.technical_documentation = [v if isinstance(v, str) else str(v) for v in self.technical_documentation]

        if self.event_log_policy is not None and not isinstance(self.event_log_policy, str):
            self.event_log_policy = str(self.event_log_policy)

        if not isinstance(self.applicable_controls, list):
            self.applicable_controls = [self.applicable_controls] if self.applicable_controls is not None else []
        self.applicable_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.applicable_controls]

        if not isinstance(self.related_impact_assessments, list):
            self.related_impact_assessments = [self.related_impact_assessments] if self.related_impact_assessments is not None else []
        self.related_impact_assessments = [v if isinstance(v, AISystemImpactAssessmentId) else AISystemImpactAssessmentId(v) for v in self.related_impact_assessments]

        if not isinstance(self.supplier_relationships, list):
            self.supplier_relationships = [self.supplier_relationships] if self.supplier_relationships is not None else []
        self.supplier_relationships = [v if isinstance(v, SupplierRelationshipId) else SupplierRelationshipId(v) for v in self.supplier_relationships]

        if not isinstance(self.customer_relationships, list):
            self.customer_relationships = [self.customer_relationships] if self.customer_relationships is not None else []
        self.customer_relationships = [v if isinstance(v, CustomerRelationshipId) else CustomerRelationshipId(v) for v in self.customer_relationships]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataResource(NamedEntity):
    """
    A data resource used by an AI system per Annex A.7. Includes data acquisition, quality, provenance, and
    preparation metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["DataResource"]
    class_class_curie: ClassVar[str] = "iso42001:DataResource"
    class_name: ClassVar[str] = "DataResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.DataResource

    id: Union[str, DataResourceId] = None
    name: str = None
    data_resource_category: Optional[Union[str, "DataResourceCategory"]] = None
    source: Optional[str] = None
    acquisition_method: Optional[str] = None
    data_quality_requirements: Optional[Union[str, list[str]]] = empty_list()
    data_quality_metrics: Optional[Union[str, list[str]]] = empty_list()
    data_provenance: Optional[str] = None
    labelling_process: Optional[str] = None
    data_preparation_methods: Optional[Union[Union[str, "DataPreparationMethod"], list[Union[str, "DataPreparationMethod"]]]] = empty_list()
    last_updated_date: Optional[Union[str, XSDDate]] = None
    known_bias_issues: Optional[Union[str, list[str]]] = empty_list()
    retention_policy: Optional[str] = None
    data_classification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataResourceId):
            self.id = DataResourceId(self.id)

        if self.data_resource_category is not None and not isinstance(self.data_resource_category, DataResourceCategory):
            self.data_resource_category = DataResourceCategory(self.data_resource_category)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.acquisition_method is not None and not isinstance(self.acquisition_method, str):
            self.acquisition_method = str(self.acquisition_method)

        if not isinstance(self.data_quality_requirements, list):
            self.data_quality_requirements = [self.data_quality_requirements] if self.data_quality_requirements is not None else []
        self.data_quality_requirements = [v if isinstance(v, str) else str(v) for v in self.data_quality_requirements]

        if not isinstance(self.data_quality_metrics, list):
            self.data_quality_metrics = [self.data_quality_metrics] if self.data_quality_metrics is not None else []
        self.data_quality_metrics = [v if isinstance(v, str) else str(v) for v in self.data_quality_metrics]

        if self.data_provenance is not None and not isinstance(self.data_provenance, str):
            self.data_provenance = str(self.data_provenance)

        if self.labelling_process is not None and not isinstance(self.labelling_process, str):
            self.labelling_process = str(self.labelling_process)

        if not isinstance(self.data_preparation_methods, list):
            self.data_preparation_methods = [self.data_preparation_methods] if self.data_preparation_methods is not None else []
        self.data_preparation_methods = [v if isinstance(v, DataPreparationMethod) else DataPreparationMethod(v) for v in self.data_preparation_methods]

        if self.last_updated_date is not None and not isinstance(self.last_updated_date, XSDDate):
            self.last_updated_date = XSDDate(self.last_updated_date)

        if not isinstance(self.known_bias_issues, list):
            self.known_bias_issues = [self.known_bias_issues] if self.known_bias_issues is not None else []
        self.known_bias_issues = [v if isinstance(v, str) else str(v) for v in self.known_bias_issues]

        if self.retention_policy is not None and not isinstance(self.retention_policy, str):
            self.retention_policy = str(self.retention_policy)

        if self.data_classification is not None and not isinstance(self.data_classification, str):
            self.data_classification = str(self.data_classification)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolingResource(NamedEntity):
    """
    A tooling resource (algorithm, framework, model, library) used in an AI system per A.4.4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["ToolingResource"]
    class_class_curie: ClassVar[str] = "iso42001:ToolingResource"
    class_name: ClassVar[str] = "ToolingResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.ToolingResource

    id: Union[str, ToolingResourceId] = None
    name: str = None
    tool_category: Optional[str] = None
    tool_version: Optional[str] = None
    vendor: Optional[str] = None
    license_terms: Optional[str] = None
    usage_purpose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToolingResourceId):
            self.id = ToolingResourceId(self.id)

        if self.tool_category is not None and not isinstance(self.tool_category, str):
            self.tool_category = str(self.tool_category)

        if self.tool_version is not None and not isinstance(self.tool_version, str):
            self.tool_version = str(self.tool_version)

        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.license_terms is not None and not isinstance(self.license_terms, str):
            self.license_terms = str(self.license_terms)

        if self.usage_purpose is not None and not isinstance(self.usage_purpose, str):
            self.usage_purpose = str(self.usage_purpose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputingResource(NamedEntity):
    """
    A system or computing resource used in the development or operation of an AI system per A.4.5.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["ComputingResource"]
    class_class_curie: ClassVar[str] = "iso42001:ComputingResource"
    class_name: ClassVar[str] = "ComputingResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.ComputingResource

    id: Union[str, ComputingResourceId] = None
    name: str = None
    resource_class: Optional[str] = None
    quantity: Optional[str] = None
    location: Optional[str] = None
    environment_type: Optional[str] = None
    cost: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputingResourceId):
            self.id = ComputingResourceId(self.id)

        if self.resource_class is not None and not isinstance(self.resource_class, str):
            self.resource_class = str(self.resource_class)

        if self.quantity is not None and not isinstance(self.quantity, str):
            self.quantity = str(self.quantity)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.environment_type is not None and not isinstance(self.environment_type, str):
            self.environment_type = str(self.environment_type)

        if self.cost is not None and not isinstance(self.cost, str):
            self.cost = str(self.cost)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanResource(NamedEntity):
    """
    A human resource (role, expertise area) involved in development, deployment, operation, maintenance, or oversight
    of an AI system per A.4.6.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["HumanResource"]
    class_class_curie: ClassVar[str] = "iso42001:HumanResource"
    class_name: ClassVar[str] = "HumanResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.HumanResource

    id: Union[str, HumanResourceId] = None
    name: str = None
    required_competencies: Optional[Union[str, list[str]]] = empty_list()
    assigned_to: Optional[Union[str, list[str]]] = empty_list()
    lifecycle_responsibilities: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanResourceId):
            self.id = HumanResourceId(self.id)

        if not isinstance(self.required_competencies, list):
            self.required_competencies = [self.required_competencies] if self.required_competencies is not None else []
        self.required_competencies = [v if isinstance(v, str) else str(v) for v in self.required_competencies]

        if not isinstance(self.assigned_to, list):
            self.assigned_to = [self.assigned_to] if self.assigned_to is not None else []
        self.assigned_to = [v if isinstance(v, str) else str(v) for v in self.assigned_to]

        if not isinstance(self.lifecycle_responsibilities, list):
            self.lifecycle_responsibilities = [self.lifecycle_responsibilities] if self.lifecycle_responsibilities is not None else []
        self.lifecycle_responsibilities = [v if isinstance(v, str) else str(v) for v in self.lifecycle_responsibilities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(NamedEntity):
    """
    A resource provided for the AIMS per Clause 7.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["Resource"]
    class_class_curie: ClassVar[str] = "iso42001:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = ISO42001.Resource

    id: Union[str, ResourceId] = None
    name: str = None
    resource_type: Optional[str] = None
    quantity: Optional[str] = None
    allocation_date: Optional[Union[str, XSDDate]] = None
    allocated_to: Optional[str] = None
    cost: Optional[str] = None
    availability_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.resource_type is not None and not isinstance(self.resource_type, str):
            self.resource_type = str(self.resource_type)

        if self.quantity is not None and not isinstance(self.quantity, str):
            self.quantity = str(self.quantity)

        if self.allocation_date is not None and not isinstance(self.allocation_date, XSDDate):
            self.allocation_date = XSDDate(self.allocation_date)

        if self.allocated_to is not None and not isinstance(self.allocated_to, str):
            self.allocated_to = str(self.allocated_to)

        if self.cost is not None and not isinstance(self.cost, str):
            self.cost = str(self.cost)

        if self.availability_status is not None and not isinstance(self.availability_status, str):
            self.availability_status = str(self.availability_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompetenceRecord(DocumentedInformation):
    """
    Evidence of competence for personnel affecting AIMS performance per Clause 7.2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["CompetenceRecord"]
    class_class_curie: ClassVar[str] = "iso42001:CompetenceRecord"
    class_name: ClassVar[str] = "CompetenceRecord"
    class_model_uri: ClassVar[URIRef] = ISO42001.CompetenceRecord

    id: Union[str, CompetenceRecordId] = None
    name: str = None
    person_name: Optional[str] = None
    person_role: Optional[str] = None
    required_competencies: Optional[Union[str, list[str]]] = empty_list()
    education_records: Optional[Union[str, list[str]]] = empty_list()
    training_records: Optional[Union[str, list[str]]] = empty_list()
    experience_records: Optional[Union[str, list[str]]] = empty_list()
    competency_assessment_date: Optional[Union[str, XSDDate]] = None
    competency_gaps: Optional[Union[str, list[str]]] = empty_list()
    development_actions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompetenceRecordId):
            self.id = CompetenceRecordId(self.id)

        if self.person_name is not None and not isinstance(self.person_name, str):
            self.person_name = str(self.person_name)

        if self.person_role is not None and not isinstance(self.person_role, str):
            self.person_role = str(self.person_role)

        if not isinstance(self.required_competencies, list):
            self.required_competencies = [self.required_competencies] if self.required_competencies is not None else []
        self.required_competencies = [v if isinstance(v, str) else str(v) for v in self.required_competencies]

        if not isinstance(self.education_records, list):
            self.education_records = [self.education_records] if self.education_records is not None else []
        self.education_records = [v if isinstance(v, str) else str(v) for v in self.education_records]

        if not isinstance(self.training_records, list):
            self.training_records = [self.training_records] if self.training_records is not None else []
        self.training_records = [v if isinstance(v, str) else str(v) for v in self.training_records]

        if not isinstance(self.experience_records, list):
            self.experience_records = [self.experience_records] if self.experience_records is not None else []
        self.experience_records = [v if isinstance(v, str) else str(v) for v in self.experience_records]

        if self.competency_assessment_date is not None and not isinstance(self.competency_assessment_date, XSDDate):
            self.competency_assessment_date = XSDDate(self.competency_assessment_date)

        if not isinstance(self.competency_gaps, list):
            self.competency_gaps = [self.competency_gaps] if self.competency_gaps is not None else []
        self.competency_gaps = [v if isinstance(v, str) else str(v) for v in self.competency_gaps]

        if not isinstance(self.development_actions, list):
            self.development_actions = [self.development_actions] if self.development_actions is not None else []
        self.development_actions = [v if isinstance(v, str) else str(v) for v in self.development_actions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AwarenessProgram(DocumentedInformation):
    """
    The awareness program ensuring personnel understand their AI-related responsibilities per Clause 7.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AwarenessProgram"]
    class_class_curie: ClassVar[str] = "iso42001:AwarenessProgram"
    class_name: ClassVar[str] = "AwarenessProgram"
    class_model_uri: ClassVar[URIRef] = ISO42001.AwarenessProgram

    id: Union[str, AwarenessProgramId] = None
    name: str = None
    awareness_topics: Optional[Union[str, list[str]]] = empty_list()
    delivery_methods: Optional[Union[str, list[str]]] = empty_list()
    target_audience: Optional[str] = None
    frequency: Optional[str] = None
    completion_tracking: Optional[str] = None
    effectiveness_measures: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AwarenessProgramId):
            self.id = AwarenessProgramId(self.id)

        if not isinstance(self.awareness_topics, list):
            self.awareness_topics = [self.awareness_topics] if self.awareness_topics is not None else []
        self.awareness_topics = [v if isinstance(v, str) else str(v) for v in self.awareness_topics]

        if not isinstance(self.delivery_methods, list):
            self.delivery_methods = [self.delivery_methods] if self.delivery_methods is not None else []
        self.delivery_methods = [v if isinstance(v, str) else str(v) for v in self.delivery_methods]

        if self.target_audience is not None and not isinstance(self.target_audience, str):
            self.target_audience = str(self.target_audience)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.completion_tracking is not None and not isinstance(self.completion_tracking, str):
            self.completion_tracking = str(self.completion_tracking)

        if self.effectiveness_measures is not None and not isinstance(self.effectiveness_measures, str):
            self.effectiveness_measures = str(self.effectiveness_measures)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunicationPlan(DocumentedInformation):
    """
    Plan for internal and external communications relevant to the AIMS per Clause 7.4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["CommunicationPlan"]
    class_class_curie: ClassVar[str] = "iso42001:CommunicationPlan"
    class_name: ClassVar[str] = "CommunicationPlan"
    class_model_uri: ClassVar[URIRef] = ISO42001.CommunicationPlan

    id: Union[str, CommunicationPlanId] = None
    name: str = None
    communication_items: Optional[Union[Union[dict, "CommunicationItem"], list[Union[dict, "CommunicationItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommunicationPlanId):
            self.id = CommunicationPlanId(self.id)

        if not isinstance(self.communication_items, list):
            self.communication_items = [self.communication_items] if self.communication_items is not None else []
        self.communication_items = [v if isinstance(v, CommunicationItem) else CommunicationItem(**as_dict(v)) for v in self.communication_items]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunicationItem(YAMLRoot):
    """
    A single communication requirement within the AIMS communication plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["CommunicationItem"]
    class_class_curie: ClassVar[str] = "iso42001:CommunicationItem"
    class_name: ClassVar[str] = "CommunicationItem"
    class_model_uri: ClassVar[URIRef] = ISO42001.CommunicationItem

    subject: Optional[str] = None
    purpose: Optional[str] = None
    audience: Optional[str] = None
    frequency: Optional[str] = None
    method: Optional[str] = None
    responsible_party: Optional[str] = None
    records_required: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.records_required is not None and not isinstance(self.records_required, str):
            self.records_required = str(self.records_required)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OperationalProcedure(DocumentedInformation):
    """
    A documented procedure for operational planning and control of AIMS processes per Clause 8.1, including AI system
    life cycle related controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["OperationalProcedure"]
    class_class_curie: ClassVar[str] = "iso42001:OperationalProcedure"
    class_name: ClassVar[str] = "OperationalProcedure"
    class_model_uri: ClassVar[URIRef] = ISO42001.OperationalProcedure

    id: Union[str, OperationalProcedureId] = None
    name: str = None
    procedure_scope: Optional[str] = None
    process_criteria: Optional[str] = None
    control_measures: Optional[Union[str, list[str]]] = empty_list()
    responsible_roles: Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]] = empty_list()
    related_controls: Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]] = empty_list()
    change_control_requirements: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalProcedureId):
            self.id = OperationalProcedureId(self.id)

        if self.procedure_scope is not None and not isinstance(self.procedure_scope, str):
            self.procedure_scope = str(self.procedure_scope)

        if self.process_criteria is not None and not isinstance(self.process_criteria, str):
            self.process_criteria = str(self.process_criteria)

        if not isinstance(self.control_measures, list):
            self.control_measures = [self.control_measures] if self.control_measures is not None else []
        self.control_measures = [v if isinstance(v, str) else str(v) for v in self.control_measures]

        if not isinstance(self.responsible_roles, list):
            self.responsible_roles = [self.responsible_roles] if self.responsible_roles is not None else []
        self.responsible_roles = [v if isinstance(v, RoleId) else RoleId(v) for v in self.responsible_roles]

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, AIReferenceControlId) else AIReferenceControlId(v) for v in self.related_controls]

        if self.change_control_requirements is not None and not isinstance(self.change_control_requirements, str):
            self.change_control_requirements = str(self.change_control_requirements)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonitoringProgram(DocumentedInformation):
    """
    The program for monitoring, measurement, analysis, and evaluation of AIMS performance per Clause 9.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["MonitoringProgram"]
    class_class_curie: ClassVar[str] = "iso42001:MonitoringProgram"
    class_name: ClassVar[str] = "MonitoringProgram"
    class_model_uri: ClassVar[URIRef] = ISO42001.MonitoringProgram

    id: Union[str, MonitoringProgramId] = None
    name: str = None
    monitoring_items: Optional[Union[Union[dict, "MonitoringItem"], list[Union[dict, "MonitoringItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonitoringProgramId):
            self.id = MonitoringProgramId(self.id)

        if not isinstance(self.monitoring_items, list):
            self.monitoring_items = [self.monitoring_items] if self.monitoring_items is not None else []
        self.monitoring_items = [v if isinstance(v, MonitoringItem) else MonitoringItem(**as_dict(v)) for v in self.monitoring_items]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonitoringItem(YAMLRoot):
    """
    A single item to be monitored and measured per Clause 9.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["MonitoringItem"]
    class_class_curie: ClassVar[str] = "iso42001:MonitoringItem"
    class_name: ClassVar[str] = "MonitoringItem"
    class_model_uri: ClassVar[URIRef] = ISO42001.MonitoringItem

    metric_name: Optional[str] = None
    metric_description: Optional[str] = None
    measurement_method: Optional[str] = None
    measurement_frequency: Optional[str] = None
    responsible_party: Optional[str] = None
    analysis_frequency: Optional[str] = None
    analyst: Optional[str] = None
    target_threshold: Optional[str] = None
    alert_threshold: Optional[str] = None
    current_value: Optional[str] = None
    trend: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.metric_name is not None and not isinstance(self.metric_name, str):
            self.metric_name = str(self.metric_name)

        if self.metric_description is not None and not isinstance(self.metric_description, str):
            self.metric_description = str(self.metric_description)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_frequency is not None and not isinstance(self.measurement_frequency, str):
            self.measurement_frequency = str(self.measurement_frequency)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.analysis_frequency is not None and not isinstance(self.analysis_frequency, str):
            self.analysis_frequency = str(self.analysis_frequency)

        if self.analyst is not None and not isinstance(self.analyst, str):
            self.analyst = str(self.analyst)

        if self.target_threshold is not None and not isinstance(self.target_threshold, str):
            self.target_threshold = str(self.target_threshold)

        if self.alert_threshold is not None and not isinstance(self.alert_threshold, str):
            self.alert_threshold = str(self.alert_threshold)

        if self.current_value is not None and not isinstance(self.current_value, str):
            self.current_value = str(self.current_value)

        if self.trend is not None and not isinstance(self.trend, str):
            self.trend = str(self.trend)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternalAudit(DocumentedInformation):
    """
    An internal audit instance per Clause 9.2 assessing AIMS conformance and effectiveness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["InternalAudit"]
    class_class_curie: ClassVar[str] = "iso42001:InternalAudit"
    class_name: ClassVar[str] = "InternalAudit"
    class_model_uri: ClassVar[URIRef] = ISO42001.InternalAudit

    id: Union[str, InternalAuditId] = None
    name: str = None
    audit_reference: Optional[str] = None
    audit_type: Optional[Union[str, "AuditType"]] = None
    audit_scope: Optional[str] = None
    audit_criteria: Optional[str] = None
    audit_objectives: Optional[str] = None
    audit_period_start: Optional[Union[str, XSDDate]] = None
    audit_period_end: Optional[Union[str, XSDDate]] = None
    lead_auditor: Optional[str] = None
    audit_team: Optional[Union[str, list[str]]] = empty_list()
    auditee_representatives: Optional[Union[str, list[str]]] = empty_list()
    audit_plan: Optional[str] = None
    findings: Optional[Union[Union[str, AuditFindingId], list[Union[str, AuditFindingId]]]] = empty_list()
    positive_observations: Optional[Union[str, list[str]]] = empty_list()
    audit_conclusion: Optional[str] = None
    report_date: Optional[Union[str, XSDDate]] = None
    report_distribution: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternalAuditId):
            self.id = InternalAuditId(self.id)

        if self.audit_reference is not None and not isinstance(self.audit_reference, str):
            self.audit_reference = str(self.audit_reference)

        if self.audit_type is not None and not isinstance(self.audit_type, AuditType):
            self.audit_type = AuditType(self.audit_type)

        if self.audit_scope is not None and not isinstance(self.audit_scope, str):
            self.audit_scope = str(self.audit_scope)

        if self.audit_criteria is not None and not isinstance(self.audit_criteria, str):
            self.audit_criteria = str(self.audit_criteria)

        if self.audit_objectives is not None and not isinstance(self.audit_objectives, str):
            self.audit_objectives = str(self.audit_objectives)

        if self.audit_period_start is not None and not isinstance(self.audit_period_start, XSDDate):
            self.audit_period_start = XSDDate(self.audit_period_start)

        if self.audit_period_end is not None and not isinstance(self.audit_period_end, XSDDate):
            self.audit_period_end = XSDDate(self.audit_period_end)

        if self.lead_auditor is not None and not isinstance(self.lead_auditor, str):
            self.lead_auditor = str(self.lead_auditor)

        if not isinstance(self.audit_team, list):
            self.audit_team = [self.audit_team] if self.audit_team is not None else []
        self.audit_team = [v if isinstance(v, str) else str(v) for v in self.audit_team]

        if not isinstance(self.auditee_representatives, list):
            self.auditee_representatives = [self.auditee_representatives] if self.auditee_representatives is not None else []
        self.auditee_representatives = [v if isinstance(v, str) else str(v) for v in self.auditee_representatives]

        if self.audit_plan is not None and not isinstance(self.audit_plan, str):
            self.audit_plan = str(self.audit_plan)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, AuditFindingId) else AuditFindingId(v) for v in self.findings]

        if not isinstance(self.positive_observations, list):
            self.positive_observations = [self.positive_observations] if self.positive_observations is not None else []
        self.positive_observations = [v if isinstance(v, str) else str(v) for v in self.positive_observations]

        if self.audit_conclusion is not None and not isinstance(self.audit_conclusion, str):
            self.audit_conclusion = str(self.audit_conclusion)

        if self.report_date is not None and not isinstance(self.report_date, XSDDate):
            self.report_date = XSDDate(self.report_date)

        if not isinstance(self.report_distribution, list):
            self.report_distribution = [self.report_distribution] if self.report_distribution is not None else []
        self.report_distribution = [v if isinstance(v, str) else str(v) for v in self.report_distribution]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditProgramme(DocumentedInformation):
    """
    The internal audit programme per Clause 9.2.2, planning AIMS audit activities over a defined period.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AuditProgramme"]
    class_class_curie: ClassVar[str] = "iso42001:AuditProgramme"
    class_name: ClassVar[str] = "AuditProgramme"
    class_model_uri: ClassVar[URIRef] = ISO42001.AuditProgramme

    id: Union[str, AuditProgrammeId] = None
    name: str = None
    programme_period: Optional[str] = None
    planned_audits: Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]] = empty_list()
    audit_frequency_rationale: Optional[str] = None
    resource_requirements: Optional[str] = None
    auditor_qualifications: Optional[str] = None
    programme_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditProgrammeId):
            self.id = AuditProgrammeId(self.id)

        if self.programme_period is not None and not isinstance(self.programme_period, str):
            self.programme_period = str(self.programme_period)

        if not isinstance(self.planned_audits, list):
            self.planned_audits = [self.planned_audits] if self.planned_audits is not None else []
        self.planned_audits = [v if isinstance(v, InternalAuditId) else InternalAuditId(v) for v in self.planned_audits]

        if self.audit_frequency_rationale is not None and not isinstance(self.audit_frequency_rationale, str):
            self.audit_frequency_rationale = str(self.audit_frequency_rationale)

        if self.resource_requirements is not None and not isinstance(self.resource_requirements, str):
            self.resource_requirements = str(self.resource_requirements)

        if self.auditor_qualifications is not None and not isinstance(self.auditor_qualifications, str):
            self.auditor_qualifications = str(self.auditor_qualifications)

        if self.programme_status is not None and not isinstance(self.programme_status, str):
            self.programme_status = str(self.programme_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditFinding(NamedEntity):
    """
    A finding from an AIMS internal audit, including nonconformities, observations, and positive findings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AuditFinding"]
    class_class_curie: ClassVar[str] = "iso42001:AuditFinding"
    class_name: ClassVar[str] = "AuditFinding"
    class_model_uri: ClassVar[URIRef] = ISO42001.AuditFinding

    id: Union[str, AuditFindingId] = None
    name: str = None
    finding_type: Optional[Union[str, "AuditFindingType"]] = None
    clause_reference: Optional[str] = None
    control_reference: Optional[Union[str, AIReferenceControlId]] = None
    finding_description: Optional[str] = None
    objective_evidence: Optional[str] = None
    root_cause_analysis: Optional[str] = None
    risk_implication: Optional[str] = None
    recommended_action: Optional[str] = None
    auditee_response: Optional[str] = None
    linked_corrective_action: Optional[Union[str, CorrectiveActionId]] = None
    closure_status: Optional[str] = None
    closure_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditFindingId):
            self.id = AuditFindingId(self.id)

        if self.finding_type is not None and not isinstance(self.finding_type, AuditFindingType):
            self.finding_type = AuditFindingType(self.finding_type)

        if self.clause_reference is not None and not isinstance(self.clause_reference, str):
            self.clause_reference = str(self.clause_reference)

        if self.control_reference is not None and not isinstance(self.control_reference, AIReferenceControlId):
            self.control_reference = AIReferenceControlId(self.control_reference)

        if self.finding_description is not None and not isinstance(self.finding_description, str):
            self.finding_description = str(self.finding_description)

        if self.objective_evidence is not None and not isinstance(self.objective_evidence, str):
            self.objective_evidence = str(self.objective_evidence)

        if self.root_cause_analysis is not None and not isinstance(self.root_cause_analysis, str):
            self.root_cause_analysis = str(self.root_cause_analysis)

        if self.risk_implication is not None and not isinstance(self.risk_implication, str):
            self.risk_implication = str(self.risk_implication)

        if self.recommended_action is not None and not isinstance(self.recommended_action, str):
            self.recommended_action = str(self.recommended_action)

        if self.auditee_response is not None and not isinstance(self.auditee_response, str):
            self.auditee_response = str(self.auditee_response)

        if self.linked_corrective_action is not None and not isinstance(self.linked_corrective_action, CorrectiveActionId):
            self.linked_corrective_action = CorrectiveActionId(self.linked_corrective_action)

        if self.closure_status is not None and not isinstance(self.closure_status, str):
            self.closure_status = str(self.closure_status)

        if self.closure_date is not None and not isinstance(self.closure_date, XSDDate):
            self.closure_date = XSDDate(self.closure_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ManagementReview(DocumentedInformation):
    """
    A management review per Clause 9.3, conducted by top management to evaluate ongoing AIMS suitability, adequacy,
    and effectiveness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["ManagementReview"]
    class_class_curie: ClassVar[str] = "iso42001:ManagementReview"
    class_name: ClassVar[str] = "ManagementReview"
    class_model_uri: ClassVar[URIRef] = ISO42001.ManagementReview

    id: Union[str, ManagementReviewId] = None
    name: str = None
    review_date: Optional[Union[str, XSDDate]] = None
    attendees: Optional[Union[str, list[str]]] = empty_list()
    previous_actions_status: Optional[str] = None
    context_changes: Optional[Union[str, list[str]]] = empty_list()
    interested_party_changes: Optional[Union[str, list[str]]] = empty_list()
    performance_trends: Optional[str] = None
    audit_results_summary: Optional[str] = None
    risk_assessment_results: Optional[str] = None
    impact_assessment_results: Optional[str] = None
    improvement_opportunities: Optional[Union[Union[str, ImprovementOpportunityId], list[Union[str, ImprovementOpportunityId]]]] = empty_list()
    decisions: Optional[Union[str, list[str]]] = empty_list()
    action_items: Optional[Union[str, list[str]]] = empty_list()
    next_review_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManagementReviewId):
            self.id = ManagementReviewId(self.id)

        if self.review_date is not None and not isinstance(self.review_date, XSDDate):
            self.review_date = XSDDate(self.review_date)

        if not isinstance(self.attendees, list):
            self.attendees = [self.attendees] if self.attendees is not None else []
        self.attendees = [v if isinstance(v, str) else str(v) for v in self.attendees]

        if self.previous_actions_status is not None and not isinstance(self.previous_actions_status, str):
            self.previous_actions_status = str(self.previous_actions_status)

        if not isinstance(self.context_changes, list):
            self.context_changes = [self.context_changes] if self.context_changes is not None else []
        self.context_changes = [v if isinstance(v, str) else str(v) for v in self.context_changes]

        if not isinstance(self.interested_party_changes, list):
            self.interested_party_changes = [self.interested_party_changes] if self.interested_party_changes is not None else []
        self.interested_party_changes = [v if isinstance(v, str) else str(v) for v in self.interested_party_changes]

        if self.performance_trends is not None and not isinstance(self.performance_trends, str):
            self.performance_trends = str(self.performance_trends)

        if self.audit_results_summary is not None and not isinstance(self.audit_results_summary, str):
            self.audit_results_summary = str(self.audit_results_summary)

        if self.risk_assessment_results is not None and not isinstance(self.risk_assessment_results, str):
            self.risk_assessment_results = str(self.risk_assessment_results)

        if self.impact_assessment_results is not None and not isinstance(self.impact_assessment_results, str):
            self.impact_assessment_results = str(self.impact_assessment_results)

        if not isinstance(self.improvement_opportunities, list):
            self.improvement_opportunities = [self.improvement_opportunities] if self.improvement_opportunities is not None else []
        self.improvement_opportunities = [v if isinstance(v, ImprovementOpportunityId) else ImprovementOpportunityId(v) for v in self.improvement_opportunities]

        if not isinstance(self.decisions, list):
            self.decisions = [self.decisions] if self.decisions is not None else []
        self.decisions = [v if isinstance(v, str) else str(v) for v in self.decisions]

        if not isinstance(self.action_items, list):
            self.action_items = [self.action_items] if self.action_items is not None else []
        self.action_items = [v if isinstance(v, str) else str(v) for v in self.action_items]

        if self.next_review_date is not None and not isinstance(self.next_review_date, XSDDate):
            self.next_review_date = XSDDate(self.next_review_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Nonconformity(NamedEntity):
    """
    A nonconformity identified per Clause 10.2 representing failure to fulfill an AIMS requirement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["Nonconformity"]
    class_class_curie: ClassVar[str] = "iso42001:Nonconformity"
    class_name: ClassVar[str] = "Nonconformity"
    class_model_uri: ClassVar[URIRef] = ISO42001.Nonconformity

    id: Union[str, NonconformityId] = None
    name: str = None
    nonconformity_source: Optional[str] = None
    detection_date: Optional[Union[str, XSDDate]] = None
    detected_by: Optional[str] = None
    requirement_violated: Optional[str] = None
    nonconformity_description: Optional[str] = None
    immediate_actions: Optional[Union[str, list[str]]] = empty_list()
    consequences_addressed: Optional[str] = None
    root_cause: Optional[str] = None
    similar_nonconformities_check: Optional[str] = None
    linked_corrective_actions: Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]] = empty_list()
    status: Optional[str] = None
    closure_date: Optional[Union[str, XSDDate]] = None
    closure_evidence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonconformityId):
            self.id = NonconformityId(self.id)

        if self.nonconformity_source is not None and not isinstance(self.nonconformity_source, str):
            self.nonconformity_source = str(self.nonconformity_source)

        if self.detection_date is not None and not isinstance(self.detection_date, XSDDate):
            self.detection_date = XSDDate(self.detection_date)

        if self.detected_by is not None and not isinstance(self.detected_by, str):
            self.detected_by = str(self.detected_by)

        if self.requirement_violated is not None and not isinstance(self.requirement_violated, str):
            self.requirement_violated = str(self.requirement_violated)

        if self.nonconformity_description is not None and not isinstance(self.nonconformity_description, str):
            self.nonconformity_description = str(self.nonconformity_description)

        if not isinstance(self.immediate_actions, list):
            self.immediate_actions = [self.immediate_actions] if self.immediate_actions is not None else []
        self.immediate_actions = [v if isinstance(v, str) else str(v) for v in self.immediate_actions]

        if self.consequences_addressed is not None and not isinstance(self.consequences_addressed, str):
            self.consequences_addressed = str(self.consequences_addressed)

        if self.root_cause is not None and not isinstance(self.root_cause, str):
            self.root_cause = str(self.root_cause)

        if self.similar_nonconformities_check is not None and not isinstance(self.similar_nonconformities_check, str):
            self.similar_nonconformities_check = str(self.similar_nonconformities_check)

        if not isinstance(self.linked_corrective_actions, list):
            self.linked_corrective_actions = [self.linked_corrective_actions] if self.linked_corrective_actions is not None else []
        self.linked_corrective_actions = [v if isinstance(v, CorrectiveActionId) else CorrectiveActionId(v) for v in self.linked_corrective_actions]

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.closure_date is not None and not isinstance(self.closure_date, XSDDate):
            self.closure_date = XSDDate(self.closure_date)

        if self.closure_evidence is not None and not isinstance(self.closure_evidence, str):
            self.closure_evidence = str(self.closure_evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectiveAction(NamedEntity):
    """
    A corrective action per Clause 10.2 to address the root cause of an AIMS nonconformity and reduce the likelihood
    of recurrence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["CorrectiveAction"]
    class_class_curie: ClassVar[str] = "iso42001:CorrectiveAction"
    class_name: ClassVar[str] = "CorrectiveAction"
    class_model_uri: ClassVar[URIRef] = ISO42001.CorrectiveAction

    id: Union[str, CorrectiveActionId] = None
    name: str = None
    linked_nonconformity: Optional[Union[str, NonconformityId]] = None
    action_description: Optional[str] = None
    root_cause_addressed: Optional[str] = None
    responsible_party: Optional[str] = None
    target_completion_date: Optional[Union[str, XSDDate]] = None
    actual_completion_date: Optional[Union[str, XSDDate]] = None
    resources_required: Optional[str] = None
    effectiveness_criteria: Optional[str] = None
    effectiveness_review_date: Optional[Union[str, XSDDate]] = None
    effectiveness_verified: Optional[Union[bool, Bool]] = None
    aims_changes_required: Optional[Union[bool, Bool]] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CorrectiveActionId):
            self.id = CorrectiveActionId(self.id)

        if self.linked_nonconformity is not None and not isinstance(self.linked_nonconformity, NonconformityId):
            self.linked_nonconformity = NonconformityId(self.linked_nonconformity)

        if self.action_description is not None and not isinstance(self.action_description, str):
            self.action_description = str(self.action_description)

        if self.root_cause_addressed is not None and not isinstance(self.root_cause_addressed, str):
            self.root_cause_addressed = str(self.root_cause_addressed)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.target_completion_date is not None and not isinstance(self.target_completion_date, XSDDate):
            self.target_completion_date = XSDDate(self.target_completion_date)

        if self.actual_completion_date is not None and not isinstance(self.actual_completion_date, XSDDate):
            self.actual_completion_date = XSDDate(self.actual_completion_date)

        if self.resources_required is not None and not isinstance(self.resources_required, str):
            self.resources_required = str(self.resources_required)

        if self.effectiveness_criteria is not None and not isinstance(self.effectiveness_criteria, str):
            self.effectiveness_criteria = str(self.effectiveness_criteria)

        if self.effectiveness_review_date is not None and not isinstance(self.effectiveness_review_date, XSDDate):
            self.effectiveness_review_date = XSDDate(self.effectiveness_review_date)

        if self.effectiveness_verified is not None and not isinstance(self.effectiveness_verified, Bool):
            self.effectiveness_verified = Bool(self.effectiveness_verified)

        if self.aims_changes_required is not None and not isinstance(self.aims_changes_required, Bool):
            self.aims_changes_required = Bool(self.aims_changes_required)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImprovementOpportunity(NamedEntity):
    """
    An opportunity for continual improvement of the AIMS per Clause 10.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["ImprovementOpportunity"]
    class_class_curie: ClassVar[str] = "iso42001:ImprovementOpportunity"
    class_name: ClassVar[str] = "ImprovementOpportunity"
    class_model_uri: ClassVar[URIRef] = ISO42001.ImprovementOpportunity

    id: Union[str, ImprovementOpportunityId] = None
    name: str = None
    improvement_source: Optional[str] = None
    identification_date: Optional[Union[str, XSDDate]] = None
    identified_by: Optional[str] = None
    improvement_description: Optional[str] = None
    expected_benefit: Optional[str] = None
    priority: Optional[Union[str, "RiskLevel"]] = None
    implementation_plan: Optional[str] = None
    responsible_party: Optional[str] = None
    target_date: Optional[Union[str, XSDDate]] = None
    actual_completion_date: Optional[Union[str, XSDDate]] = None
    outcome_assessment: Optional[str] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImprovementOpportunityId):
            self.id = ImprovementOpportunityId(self.id)

        if self.improvement_source is not None and not isinstance(self.improvement_source, str):
            self.improvement_source = str(self.improvement_source)

        if self.identification_date is not None and not isinstance(self.identification_date, XSDDate):
            self.identification_date = XSDDate(self.identification_date)

        if self.identified_by is not None and not isinstance(self.identified_by, str):
            self.identified_by = str(self.identified_by)

        if self.improvement_description is not None and not isinstance(self.improvement_description, str):
            self.improvement_description = str(self.improvement_description)

        if self.expected_benefit is not None and not isinstance(self.expected_benefit, str):
            self.expected_benefit = str(self.expected_benefit)

        if self.priority is not None and not isinstance(self.priority, RiskLevel):
            self.priority = RiskLevel(self.priority)

        if self.implementation_plan is not None and not isinstance(self.implementation_plan, str):
            self.implementation_plan = str(self.implementation_plan)

        if self.responsible_party is not None and not isinstance(self.responsible_party, str):
            self.responsible_party = str(self.responsible_party)

        if self.target_date is not None and not isinstance(self.target_date, XSDDate):
            self.target_date = XSDDate(self.target_date)

        if self.actual_completion_date is not None and not isinstance(self.actual_completion_date, XSDDate):
            self.actual_completion_date = XSDDate(self.actual_completion_date)

        if self.outcome_assessment is not None and not isinstance(self.outcome_assessment, str):
            self.outcome_assessment = str(self.outcome_assessment)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdPartyRelationship(NamedEntity):
    """
    A documented relationship with a third party (supplier, partner, or customer) involved in the AI system life cycle
    per A.10.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["ThirdPartyRelationship"]
    class_class_curie: ClassVar[str] = "iso42001:ThirdPartyRelationship"
    class_name: ClassVar[str] = "ThirdPartyRelationship"
    class_model_uri: ClassVar[URIRef] = ISO42001.ThirdPartyRelationship

    id: Union[str, ThirdPartyRelationshipId] = None
    name: str = None
    party_type: Optional[str] = None
    party_name: Optional[str] = None
    contractual_basis: Optional[str] = None
    allocated_responsibilities: Optional[Union[str, list[str]]] = empty_list()
    data_processing_role: Optional[str] = None
    ai_systems_involved: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    lifecycle_stages_involved: Optional[Union[Union[str, "AISystemLifecycleStage"], list[Union[str, "AISystemLifecycleStage"]]]] = empty_list()
    assurance_evidence: Optional[Union[str, list[str]]] = empty_list()
    review_frequency: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartyRelationshipId):
            self.id = ThirdPartyRelationshipId(self.id)

        if self.party_type is not None and not isinstance(self.party_type, str):
            self.party_type = str(self.party_type)

        if self.party_name is not None and not isinstance(self.party_name, str):
            self.party_name = str(self.party_name)

        if self.contractual_basis is not None and not isinstance(self.contractual_basis, str):
            self.contractual_basis = str(self.contractual_basis)

        if not isinstance(self.allocated_responsibilities, list):
            self.allocated_responsibilities = [self.allocated_responsibilities] if self.allocated_responsibilities is not None else []
        self.allocated_responsibilities = [v if isinstance(v, str) else str(v) for v in self.allocated_responsibilities]

        if self.data_processing_role is not None and not isinstance(self.data_processing_role, str):
            self.data_processing_role = str(self.data_processing_role)

        if not isinstance(self.ai_systems_involved, list):
            self.ai_systems_involved = [self.ai_systems_involved] if self.ai_systems_involved is not None else []
        self.ai_systems_involved = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.ai_systems_involved]

        if not isinstance(self.lifecycle_stages_involved, list):
            self.lifecycle_stages_involved = [self.lifecycle_stages_involved] if self.lifecycle_stages_involved is not None else []
        self.lifecycle_stages_involved = [v if isinstance(v, AISystemLifecycleStage) else AISystemLifecycleStage(v) for v in self.lifecycle_stages_involved]

        if not isinstance(self.assurance_evidence, list):
            self.assurance_evidence = [self.assurance_evidence] if self.assurance_evidence is not None else []
        self.assurance_evidence = [v if isinstance(v, str) else str(v) for v in self.assurance_evidence]

        if self.review_frequency is not None and not isinstance(self.review_frequency, str):
            self.review_frequency = str(self.review_frequency)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupplierRelationship(ThirdPartyRelationship):
    """
    A supplier relationship covering services, products, or materials (e.g., datasets, models, libraries, full AI
    systems) provided to the organization per A.10.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["SupplierRelationship"]
    class_class_curie: ClassVar[str] = "iso42001:SupplierRelationship"
    class_name: ClassVar[str] = "SupplierRelationship"
    class_model_uri: ClassVar[URIRef] = ISO42001.SupplierRelationship

    id: Union[str, SupplierRelationshipId] = None
    name: str = None
    supplier_assessment_criteria: Optional[Union[str, list[str]]] = empty_list()
    monitoring_method: Optional[str] = None
    corrective_actions_required: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupplierRelationshipId):
            self.id = SupplierRelationshipId(self.id)

        if not isinstance(self.supplier_assessment_criteria, list):
            self.supplier_assessment_criteria = [self.supplier_assessment_criteria] if self.supplier_assessment_criteria is not None else []
        self.supplier_assessment_criteria = [v if isinstance(v, str) else str(v) for v in self.supplier_assessment_criteria]

        if self.monitoring_method is not None and not isinstance(self.monitoring_method, str):
            self.monitoring_method = str(self.monitoring_method)

        if not isinstance(self.corrective_actions_required, list):
            self.corrective_actions_required = [self.corrective_actions_required] if self.corrective_actions_required is not None else []
        self.corrective_actions_required = [v if isinstance(v, str) else str(v) for v in self.corrective_actions_required]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerRelationship(ThirdPartyRelationship):
    """
    A customer relationship for an AI product or service supplied by the organization per A.10.4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["CustomerRelationship"]
    class_class_curie: ClassVar[str] = "iso42001:CustomerRelationship"
    class_name: ClassVar[str] = "CustomerRelationship"
    class_model_uri: ClassVar[URIRef] = ISO42001.CustomerRelationship

    id: Union[str, CustomerRelationshipId] = None
    name: str = None
    customer_expectations: Optional[Union[str, list[str]]] = empty_list()
    usage_agreement_reference: Optional[str] = None
    communicated_limitations: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerRelationshipId):
            self.id = CustomerRelationshipId(self.id)

        if not isinstance(self.customer_expectations, list):
            self.customer_expectations = [self.customer_expectations] if self.customer_expectations is not None else []
        self.customer_expectations = [v if isinstance(v, str) else str(v) for v in self.customer_expectations]

        if self.usage_agreement_reference is not None and not isinstance(self.usage_agreement_reference, str):
            self.usage_agreement_reference = str(self.usage_agreement_reference)

        if not isinstance(self.communicated_limitations, list):
            self.communicated_limitations = [self.communicated_limitations] if self.communicated_limitations is not None else []
        self.communicated_limitations = [v if isinstance(v, str) else str(v) for v in self.communicated_limitations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISystemEvent(NamedEntity):
    """
    An AI system event detected by monitoring, users, or external reporting channels. Events may or may not be
    subsequently classified as incidents. Supports A.6.2.8 event log capture and A.8.3 external reporting workflows.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AISystemEvent"]
    class_class_curie: ClassVar[str] = "iso42001:AISystemEvent"
    class_name: ClassVar[str] = "AISystemEvent"
    class_model_uri: ClassVar[URIRef] = ISO42001.AISystemEvent

    id: Union[str, AISystemEventId] = None
    name: str = None
    event_datetime: Optional[Union[str, XSDDateTime]] = None
    reporter: Optional[str] = None
    reporter_party_type: Optional[str] = None
    event_source: Optional[str] = None
    event_description: Optional[str] = None
    affected_ai_systems: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    initial_assessment: Optional[str] = None
    categorized_as_incident: Optional[Union[bool, Bool]] = None
    linked_incident: Optional[Union[str, AIIncidentId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISystemEventId):
            self.id = AISystemEventId(self.id)

        if self.event_datetime is not None and not isinstance(self.event_datetime, XSDDateTime):
            self.event_datetime = XSDDateTime(self.event_datetime)

        if self.reporter is not None and not isinstance(self.reporter, str):
            self.reporter = str(self.reporter)

        if self.reporter_party_type is not None and not isinstance(self.reporter_party_type, str):
            self.reporter_party_type = str(self.reporter_party_type)

        if self.event_source is not None and not isinstance(self.event_source, str):
            self.event_source = str(self.event_source)

        if self.event_description is not None and not isinstance(self.event_description, str):
            self.event_description = str(self.event_description)

        if not isinstance(self.affected_ai_systems, list):
            self.affected_ai_systems = [self.affected_ai_systems] if self.affected_ai_systems is not None else []
        self.affected_ai_systems = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.affected_ai_systems]

        if self.initial_assessment is not None and not isinstance(self.initial_assessment, str):
            self.initial_assessment = str(self.initial_assessment)

        if self.categorized_as_incident is not None and not isinstance(self.categorized_as_incident, Bool):
            self.categorized_as_incident = Bool(self.categorized_as_incident)

        if self.linked_incident is not None and not isinstance(self.linked_incident, AIIncidentId):
            self.linked_incident = AIIncidentId(self.linked_incident)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIIncident(NamedEntity):
    """
    An AI incident, i.e., an AI system event determined to require response, escalation, or external communication.
    Captures triage, response lifecycle, and communications to users and other interested parties per A.8.4 and A.8.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AIIncident"]
    class_class_curie: ClassVar[str] = "iso42001:AIIncident"
    class_name: ClassVar[str] = "AIIncident"
    class_model_uri: ClassVar[URIRef] = ISO42001.AIIncident

    id: Union[str, AIIncidentId] = None
    name: str = None
    incident_datetime: Optional[Union[str, XSDDateTime]] = None
    incident_category: Optional[Union[str, "AIIncidentCategory"]] = None
    severity: Optional[Union[str, "RiskLevel"]] = None
    affected_ai_systems: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    affected_dimensions: Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]] = empty_list()
    incident_description: Optional[str] = None
    detection_method: Optional[str] = None
    response_actions: Optional[Union[str, list[str]]] = empty_list()
    containment_actions: Optional[Union[str, list[str]]] = empty_list()
    recovery_actions: Optional[Union[str, list[str]]] = empty_list()
    root_cause: Optional[str] = None
    lessons_learned: Optional[Union[str, list[str]]] = empty_list()
    evidence_collected: Optional[Union[str, list[str]]] = empty_list()
    notification_required: Optional[Union[bool, Bool]] = None
    notifications_made: Optional[Union[str, list[str]]] = empty_list()
    external_reports: Optional[Union[str, list[str]]] = empty_list()
    communication_plan: Optional[Union[str, CommunicationPlanId]] = None
    linked_corrective_actions: Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]] = empty_list()
    closure_datetime: Optional[Union[str, XSDDateTime]] = None
    post_incident_review: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIIncidentId):
            self.id = AIIncidentId(self.id)

        if self.incident_datetime is not None and not isinstance(self.incident_datetime, XSDDateTime):
            self.incident_datetime = XSDDateTime(self.incident_datetime)

        if self.incident_category is not None and not isinstance(self.incident_category, AIIncidentCategory):
            self.incident_category = AIIncidentCategory(self.incident_category)

        if self.severity is not None and not isinstance(self.severity, RiskLevel):
            self.severity = RiskLevel(self.severity)

        if not isinstance(self.affected_ai_systems, list):
            self.affected_ai_systems = [self.affected_ai_systems] if self.affected_ai_systems is not None else []
        self.affected_ai_systems = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.affected_ai_systems]

        if not isinstance(self.affected_dimensions, list):
            self.affected_dimensions = [self.affected_dimensions] if self.affected_dimensions is not None else []
        self.affected_dimensions = [v if isinstance(v, ImpactAssessmentDimension) else ImpactAssessmentDimension(v) for v in self.affected_dimensions]

        if self.incident_description is not None and not isinstance(self.incident_description, str):
            self.incident_description = str(self.incident_description)

        if self.detection_method is not None and not isinstance(self.detection_method, str):
            self.detection_method = str(self.detection_method)

        if not isinstance(self.response_actions, list):
            self.response_actions = [self.response_actions] if self.response_actions is not None else []
        self.response_actions = [v if isinstance(v, str) else str(v) for v in self.response_actions]

        if not isinstance(self.containment_actions, list):
            self.containment_actions = [self.containment_actions] if self.containment_actions is not None else []
        self.containment_actions = [v if isinstance(v, str) else str(v) for v in self.containment_actions]

        if not isinstance(self.recovery_actions, list):
            self.recovery_actions = [self.recovery_actions] if self.recovery_actions is not None else []
        self.recovery_actions = [v if isinstance(v, str) else str(v) for v in self.recovery_actions]

        if self.root_cause is not None and not isinstance(self.root_cause, str):
            self.root_cause = str(self.root_cause)

        if not isinstance(self.lessons_learned, list):
            self.lessons_learned = [self.lessons_learned] if self.lessons_learned is not None else []
        self.lessons_learned = [v if isinstance(v, str) else str(v) for v in self.lessons_learned]

        if not isinstance(self.evidence_collected, list):
            self.evidence_collected = [self.evidence_collected] if self.evidence_collected is not None else []
        self.evidence_collected = [v if isinstance(v, str) else str(v) for v in self.evidence_collected]

        if self.notification_required is not None and not isinstance(self.notification_required, Bool):
            self.notification_required = Bool(self.notification_required)

        if not isinstance(self.notifications_made, list):
            self.notifications_made = [self.notifications_made] if self.notifications_made is not None else []
        self.notifications_made = [v if isinstance(v, str) else str(v) for v in self.notifications_made]

        if not isinstance(self.external_reports, list):
            self.external_reports = [self.external_reports] if self.external_reports is not None else []
        self.external_reports = [v if isinstance(v, str) else str(v) for v in self.external_reports]

        if self.communication_plan is not None and not isinstance(self.communication_plan, CommunicationPlanId):
            self.communication_plan = CommunicationPlanId(self.communication_plan)

        if not isinstance(self.linked_corrective_actions, list):
            self.linked_corrective_actions = [self.linked_corrective_actions] if self.linked_corrective_actions is not None else []
        self.linked_corrective_actions = [v if isinstance(v, CorrectiveActionId) else CorrectiveActionId(v) for v in self.linked_corrective_actions]

        if self.closure_datetime is not None and not isinstance(self.closure_datetime, XSDDateTime):
            self.closure_datetime = XSDDateTime(self.closure_datetime)

        if self.post_incident_review is not None and not isinstance(self.post_incident_review, str):
            self.post_incident_review = str(self.post_incident_review)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConcernReport(NamedEntity):
    """
    A concern raised by employees, contractors, users, or other interested parties about the organization's role with
    respect to an AI system. Operationalises Annex A.3.3 (Reporting of concerns). Confidentiality, anonymity,
    anti-reprisal protection, escalation, and timely response are core attributes; informed by ISO 37002.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["ConcernReport"]
    class_class_curie: ClassVar[str] = "iso42001:ConcernReport"
    class_name: ClassVar[str] = "ConcernReport"
    class_model_uri: ClassVar[URIRef] = ISO42001.ConcernReport

    id: Union[str, ConcernReportId] = None
    name: str = None
    reported_date: Optional[Union[str, XSDDate]] = None
    reporter: Optional[str] = None
    reporter_party_type: Optional[str] = None
    reporter_anonymous: Optional[Union[bool, Bool]] = None
    confidentiality_level: Optional[str] = None
    reporting_channel: Optional[str] = None
    concern_description: Optional[str] = None
    concern_ai_systems: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    concern_lifecycle_stage: Optional[Union[Union[str, "AISystemLifecycleStage"], list[Union[str, "AISystemLifecycleStage"]]]] = empty_list()
    severity: Optional[Union[str, "RiskLevel"]] = None
    investigator: Optional[str] = None
    investigation_status: Optional[str] = None
    investigation_findings: Optional[str] = None
    escalation_status: Optional[str] = None
    response_due_date: Optional[Union[str, XSDDate]] = None
    response_provided_date: Optional[Union[str, XSDDate]] = None
    resolution: Optional[str] = None
    reprisal_protection_actions: Optional[Union[str, list[str]]] = empty_list()
    related_incidents: Optional[Union[Union[str, AIIncidentId], list[Union[str, AIIncidentId]]]] = empty_list()
    related_nonconformities: Optional[Union[Union[str, NonconformityId], list[Union[str, NonconformityId]]]] = empty_list()
    closure_datetime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConcernReportId):
            self.id = ConcernReportId(self.id)

        if self.reported_date is not None and not isinstance(self.reported_date, XSDDate):
            self.reported_date = XSDDate(self.reported_date)

        if self.reporter is not None and not isinstance(self.reporter, str):
            self.reporter = str(self.reporter)

        if self.reporter_party_type is not None and not isinstance(self.reporter_party_type, str):
            self.reporter_party_type = str(self.reporter_party_type)

        if self.reporter_anonymous is not None and not isinstance(self.reporter_anonymous, Bool):
            self.reporter_anonymous = Bool(self.reporter_anonymous)

        if self.confidentiality_level is not None and not isinstance(self.confidentiality_level, str):
            self.confidentiality_level = str(self.confidentiality_level)

        if self.reporting_channel is not None and not isinstance(self.reporting_channel, str):
            self.reporting_channel = str(self.reporting_channel)

        if self.concern_description is not None and not isinstance(self.concern_description, str):
            self.concern_description = str(self.concern_description)

        if not isinstance(self.concern_ai_systems, list):
            self.concern_ai_systems = [self.concern_ai_systems] if self.concern_ai_systems is not None else []
        self.concern_ai_systems = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.concern_ai_systems]

        if not isinstance(self.concern_lifecycle_stage, list):
            self.concern_lifecycle_stage = [self.concern_lifecycle_stage] if self.concern_lifecycle_stage is not None else []
        self.concern_lifecycle_stage = [v if isinstance(v, AISystemLifecycleStage) else AISystemLifecycleStage(v) for v in self.concern_lifecycle_stage]

        if self.severity is not None and not isinstance(self.severity, RiskLevel):
            self.severity = RiskLevel(self.severity)

        if self.investigator is not None and not isinstance(self.investigator, str):
            self.investigator = str(self.investigator)

        if self.investigation_status is not None and not isinstance(self.investigation_status, str):
            self.investigation_status = str(self.investigation_status)

        if self.investigation_findings is not None and not isinstance(self.investigation_findings, str):
            self.investigation_findings = str(self.investigation_findings)

        if self.escalation_status is not None and not isinstance(self.escalation_status, str):
            self.escalation_status = str(self.escalation_status)

        if self.response_due_date is not None and not isinstance(self.response_due_date, XSDDate):
            self.response_due_date = XSDDate(self.response_due_date)

        if self.response_provided_date is not None and not isinstance(self.response_provided_date, XSDDate):
            self.response_provided_date = XSDDate(self.response_provided_date)

        if self.resolution is not None and not isinstance(self.resolution, str):
            self.resolution = str(self.resolution)

        if not isinstance(self.reprisal_protection_actions, list):
            self.reprisal_protection_actions = [self.reprisal_protection_actions] if self.reprisal_protection_actions is not None else []
        self.reprisal_protection_actions = [v if isinstance(v, str) else str(v) for v in self.reprisal_protection_actions]

        if not isinstance(self.related_incidents, list):
            self.related_incidents = [self.related_incidents] if self.related_incidents is not None else []
        self.related_incidents = [v if isinstance(v, AIIncidentId) else AIIncidentId(v) for v in self.related_incidents]

        if not isinstance(self.related_nonconformities, list):
            self.related_nonconformities = [self.related_nonconformities] if self.related_nonconformities is not None else []
        self.related_nonconformities = [v if isinstance(v, NonconformityId) else NonconformityId(v) for v in self.related_nonconformities]

        if self.closure_datetime is not None and not isinstance(self.closure_datetime, XSDDateTime):
            self.closure_datetime = XSDDateTime(self.closure_datetime)

        super().__post_init__(**kwargs)


# Enumerations
class AIControlFamily(EnumDefinitionImpl):
    """
    The reference control families in Annex A of ISO/IEC 42001:2023.
    """
    ai_policies = PermissibleValue(
        text="ai_policies",
        description="""Policies related to AI (Annex A.2) - management direction and support for AI systems according to business requirements.""")
    internal_organization = PermissibleValue(
        text="internal_organization",
        description="""Internal organization (Annex A.3) - accountability for responsible implementation, operation, and management of AI systems.""")
    ai_resources = PermissibleValue(
        text="ai_resources",
        description="""Resources for AI systems (Annex A.4) - documentation of data, tooling, system/computing, and human resources for AI systems.""")
    impact_assessment = PermissibleValue(
        text="impact_assessment",
        description="""Assessing impacts of AI systems (Annex A.5) - evaluation of consequences for individuals, groups, and societies across the AI system life cycle.""")
    ai_system_lifecycle = PermissibleValue(
        text="ai_system_lifecycle",
        description="""AI system life cycle (Annex A.6) - responsible design, development, verification, deployment, operation, and technical documentation.""")
    data_for_ai = PermissibleValue(
        text="data_for_ai",
        description="""Data for AI systems (Annex A.7) - data management, acquisition, quality, provenance, and preparation for AI.""")
    information_for_parties = PermissibleValue(
        text="information_for_parties",
        description="""Information for interested parties (Annex A.8) - system documentation for users, external reporting, and incident communications.""")
    use_of_ai = PermissibleValue(
        text="use_of_ai",
        description="""Use of AI systems (Annex A.9) - responsible-use processes, objectives, and intended-use enforcement.""")
    third_party_relationships = PermissibleValue(
        text="third_party_relationships",
        description="""Third-party and customer relationships (Annex A.10) - allocating responsibilities, supplier management, and customer expectations.""")

    _defn = EnumDefinition(
        name="AIControlFamily",
        description="The reference control families in Annex A of ISO/IEC 42001:2023.",
    )

class ImplementationStatus(EnumDefinitionImpl):
    """
    Lifecycle status of a reference control, used in the AIMS Statement of Applicability and control tracking.
    """
    not_started = PermissibleValue(
        text="not_started",
        description="Control identified but no implementation activities begun.")
    planned = PermissibleValue(
        text="planned",
        description="Control scheduled for implementation with defined timeline.")
    in_progress = PermissibleValue(
        text="in_progress",
        description="Implementation actively underway but not yet complete.")
    implemented = PermissibleValue(
        text="implemented",
        description="Control fully implemented and operational.")
    not_applicable = PermissibleValue(
        text="not_applicable",
        description="Control excluded from scope with documented justification per Clause 6.1.3 f).")

    _defn = EnumDefinition(
        name="ImplementationStatus",
        description="""Lifecycle status of a reference control, used in the AIMS Statement of Applicability and control tracking.""",
    )

class RiskTreatmentOption(EnumDefinitionImpl):
    """
    Standard risk treatment options drawn from ISO 31000 and adapted for AI risk treatment per Clause 6.1.3.
    """
    modify = PermissibleValue(
        text="modify",
        description="Apply controls to change the AI risk level (reduce likelihood or consequence).")
    accept = PermissibleValue(
        text="accept",
        description="""Accept the residual AI risk without further treatment, within risk appetite, with designated management approval.""")
    avoid = PermissibleValue(
        text="avoid",
        description="""Eliminate the AI risk by not undertaking the activity that creates it (for example, not deploying a high-risk AI use case).""")
    share = PermissibleValue(
        text="share",
        description="""Transfer or share the AI risk with external parties (e.g., insurance, contractual transfer to a supplier or partner).""")

    _defn = EnumDefinition(
        name="RiskTreatmentOption",
        description="""Standard risk treatment options drawn from ISO 31000 and adapted for AI risk treatment per Clause 6.1.3.""",
    )

class RiskLevel(EnumDefinitionImpl):
    """
    Qualitative AI risk rating derived from likelihood and consequence analysis.
    """
    very_low = PermissibleValue(
        text="very_low",
        description="Negligible AI risk requiring no immediate action.")
    low = PermissibleValue(
        text="low",
        description="Minor AI risk manageable through routine procedures.")
    medium = PermissibleValue(
        text="medium",
        description="Moderate AI risk requiring management attention and planned controls.")
    high = PermissibleValue(
        text="high",
        description="Significant AI risk requiring priority treatment and escalation.")
    critical = PermissibleValue(
        text="critical",
        description="""Severe AI risk threatening organizational objectives, individuals, or societies; requires immediate executive action.""")

    _defn = EnumDefinition(
        name="RiskLevel",
        description="Qualitative AI risk rating derived from likelihood and consequence analysis.",
    )

class LikelihoodRating(EnumDefinitionImpl):
    """
    Qualitative likelihood scale for AI risk assessment.
    """
    rare = PermissibleValue(
        text="rare",
        description="Highly unlikely to occur (< 5% probability).")
    unlikely = PermissibleValue(
        text="unlikely",
        description="Not expected but possible (5-20% probability).")
    possible = PermissibleValue(
        text="possible",
        description="May occur at some point (20-50% probability).")
    likely = PermissibleValue(
        text="likely",
        description="Probably will occur (50-80% probability).")
    almost_certain = PermissibleValue(
        text="almost_certain",
        description="Expected to occur in most circumstances (> 80% probability).")

    _defn = EnumDefinition(
        name="LikelihoodRating",
        description="Qualitative likelihood scale for AI risk assessment.",
    )

class ImpactRating(EnumDefinitionImpl):
    """
    Qualitative consequence scale for AI risk assessment, covering impact on the organization, individuals, groups,
    and societies.
    """
    negligible = PermissibleValue(
        text="negligible",
        description="No significant impact on operations, individuals, or society.")
    minor = PermissibleValue(
        text="minor",
        description="Limited impact, easily absorbed by normal operations.")
    moderate = PermissibleValue(
        text="moderate",
        description="Noticeable impact requiring management intervention.")
    major = PermissibleValue(
        text="major",
        description="Serious impact on objectives, reputation, compliance, or identifiable groups of individuals.")
    severe = PermissibleValue(
        text="severe",
        description="""Catastrophic impact threatening organizational viability, broad societal harm, or fundamental rights of affected individuals.""")

    _defn = EnumDefinition(
        name="ImpactRating",
        description="""Qualitative consequence scale for AI risk assessment, covering impact on the organization, individuals, groups, and societies.""",
    )

class AISystemLifecycleStage(EnumDefinitionImpl):
    """
    Stages of the AI system life cycle referenced throughout Annex A.6 and defined in ISO/IEC 5338 / ISO/IEC 22989.
    """
    inception = PermissibleValue(
        text="inception",
        description="Initial conception, feasibility, and use-case definition.")
    design = PermissibleValue(
        text="design",
        description="AI system design including requirements and architecture.")
    data_collection_and_preparation = PermissibleValue(
        text="data_collection_and_preparation",
        description="Acquiring, labelling, and preparing data resources.")
    development = PermissibleValue(
        text="development",
        description="Model and AI system development and training.")
    verification_and_validation = PermissibleValue(
        text="verification_and_validation",
        description="Verification and validation of the AI system.")
    deployment = PermissibleValue(
        text="deployment",
        description="Release and integration into the production environment.")
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        description="Ongoing operation, monitoring, and support.")
    continuous_validation = PermissibleValue(
        text="continuous_validation",
        description="Continuous validation, including drift detection and re-training triggers.")
    re_evaluation = PermissibleValue(
        text="re_evaluation",
        description="Re-evaluation following significant changes or new evidence.")
    decommissioning = PermissibleValue(
        text="decommissioning",
        description="Retirement, disposal, and post-decommissioning obligations.")

    _defn = EnumDefinition(
        name="AISystemLifecycleStage",
        description="""Stages of the AI system life cycle referenced throughout Annex A.6 and defined in ISO/IEC 5338 / ISO/IEC 22989.""",
    )

class AIOrganizationalRole(EnumDefinitionImpl):
    """
    Roles an organization may take with respect to an AI system, paraphrased from the role taxonomy referenced in
    ISO/IEC 22989 and the NIST AI RMF.
    """
    ai_provider = PermissibleValue(
        text="ai_provider",
        description="Organization providing AI platforms, products, or services to others.")
    ai_producer = PermissibleValue(
        text="ai_producer",
        description="""Organization or actor that develops, designs, operates, tests, evaluates, deploys, or governs AI systems.""")
    ai_customer = PermissibleValue(
        text="ai_customer",
        description="Organization or individual that uses an AI product or service.")
    ai_partner = PermissibleValue(
        text="ai_partner",
        description="System integrators and data providers for AI systems.")
    ai_subject = PermissibleValue(
        text="ai_subject",
        description="""Individuals or groups whose data or interests are affected by an AI system (e.g., data subjects).""")
    relevant_authority = PermissibleValue(
        text="relevant_authority",
        description="Policymakers, regulators, and other oversight bodies.")

    _defn = EnumDefinition(
        name="AIOrganizationalRole",
        description="""Roles an organization may take with respect to an AI system, paraphrased from the role taxonomy referenced in ISO/IEC 22989 and the NIST AI RMF.""",
    )

class DataResourceCategory(EnumDefinitionImpl):
    """
    Categories of data resources documented for AI systems per A.7 (Data for AI systems).
    """
    training = PermissibleValue(
        text="training",
        description="Data used to train machine learning models.")
    validation = PermissibleValue(
        text="validation",
        description="Data used for model selection and hyperparameter tuning.")
    test = PermissibleValue(
        text="test",
        description="Data used to evaluate model performance prior to deployment.")
    production = PermissibleValue(
        text="production",
        description="Live operational data processed by the deployed AI system.")
    reference = PermissibleValue(
        text="reference",
        description="Reference datasets used for benchmarking or comparison.")

    _defn = EnumDefinition(
        name="DataResourceCategory",
        description="Categories of data resources documented for AI systems per A.7 (Data for AI systems).",
    )

class AIObjectiveCategory(EnumDefinitionImpl):
    """
    Categories of organizational objectives associated with responsible development and use of AI systems, paraphrased
    from Annex C of ISO/IEC 42001:2023.
    """
    accountability = PermissibleValue(
        text="accountability",
        description="Clear allocation of responsibility for AI-supported decisions.")
    ai_expertise = PermissibleValue(
        text="ai_expertise",
        description="Availability of interdisciplinary expertise for AI activities.")
    data_quality = PermissibleValue(
        text="data_quality",
        description="Adequate quality of training, validation, and test data.")
    environmental_impact = PermissibleValue(
        text="environmental_impact",
        description="Management of positive and negative environmental effects.")
    fairness = PermissibleValue(
        text="fairness",
        description="Avoiding inappropriate or unfair outcomes for individuals or groups.")
    maintainability = PermissibleValue(
        text="maintainability",
        description="Ability to correct defects and accommodate new requirements.")
    privacy = PermissibleValue(
        text="privacy",
        description="Protection of personal and sensitive data processed by AI systems.")
    robustness = PermissibleValue(
        text="robustness",
        description="Comparable performance on new and operational data.")
    safety = PermissibleValue(
        text="safety",
        description="Avoidance of harm to life, health, property, or the environment.")
    security = PermissibleValue(
        text="security",
        description="Protection from AI-specific and conventional security threats.")
    transparency = PermissibleValue(
        text="transparency",
        description="Visibility into organizational AI practices and AI system behaviour.")
    explainability = PermissibleValue(
        text="explainability",
        description="Comprehensible explanations of important factors driving AI outputs.")
    reliability = PermissibleValue(
        text="reliability",
        description="Consistent performance under defined conditions.")
    accessibility = PermissibleValue(
        text="accessibility",
        description="Usability of AI systems by people with diverse abilities.")
    availability_of_training_data = PermissibleValue(
        text="availability_of_training_data",
        description="""Sufficient availability and quality of training, validation, and test data needed to train and verify AI systems (Annex C.2.3).""")

    _defn = EnumDefinition(
        name="AIObjectiveCategory",
        description="""Categories of organizational objectives associated with responsible development and use of AI systems, paraphrased from Annex C of ISO/IEC 42001:2023.""",
    )

class AIRiskSourceCategory(EnumDefinitionImpl):
    """
    Categories of AI risk sources, paraphrased from Annex C of ISO/IEC 42001:2023.
    """
    complexity_of_environment = PermissibleValue(
        text="complexity_of_environment",
        description="""Performance uncertainty in complex or open operational environments (e.g., autonomous systems).""")
    lack_of_transparency_or_explainability = PermissibleValue(
        text="lack_of_transparency_or_explainability",
        description="""Inability to provide adequate information to interested parties, affecting trustworthiness and accountability.""")
    level_of_automation = PermissibleValue(
        text="level_of_automation",
        description="Effects of automation on safety, fairness, security, or human oversight.")
    machine_learning_specific = PermissibleValue(
        text="machine_learning_specific",
        description="Risks tied to data collection, data quality, and ML-specific phenomena such as data poisoning.")
    hardware = PermissibleValue(
        text="hardware",
        description="Hardware errors or behavioural differences when transferring trained models between systems.")
    lifecycle = PermissibleValue(
        text="lifecycle",
        description="""Risks introduced at any AI system life cycle stage, including design flaws, deployment issues, or decommissioning gaps.""")
    technology_readiness = PermissibleValue(
        text="technology_readiness",
        description="""Risks from immature technology with unknown limitations as well as mature technology subject to technology complacency.""")

    _defn = EnumDefinition(
        name="AIRiskSourceCategory",
        description="Categories of AI risk sources, paraphrased from Annex C of ISO/IEC 42001:2023.",
    )

class DocumentType(EnumDefinitionImpl):
    """
    Categories of documented information referenced in or required by ISO/IEC 42001:2023.
    """
    policy = PermissibleValue(
        text="policy",
        description="High-level statement of intent and direction (e.g., AI policy per 5.2).")
    procedure = PermissibleValue(
        text="procedure",
        description="Documented steps for performing AIMS activities consistently.")
    standard = PermissibleValue(
        text="standard",
        description="Mandatory requirements for specific AI technologies or processes.")
    guideline = PermissibleValue(
        text="guideline",
        description="Recommended practices that support AI-related policies.")
    record = PermissibleValue(
        text="record",
        description="Evidence of AIMS activities performed or results achieved.")
    plan = PermissibleValue(
        text="plan",
        description="Documented approach for achieving objectives (e.g., AI risk treatment plan, deployment plan).")
    report = PermissibleValue(
        text="report",
        description="Formal output of assessment, audit, impact assessment, or review activities.")
    technical_documentation = PermissibleValue(
        text="technical_documentation",
        description="""AI system technical documentation provided to users, partners, supervisory authorities, and other interested parties per A.6.2.7 and A.8.2.""")

    _defn = EnumDefinition(
        name="DocumentType",
        description="Categories of documented information referenced in or required by ISO/IEC 42001:2023.",
    )

class AuditFindingType(EnumDefinitionImpl):
    """
    Classification of internal audit findings for the AIMS.
    """
    major_nonconformity = PermissibleValue(
        text="major_nonconformity",
        description="""Significant failure to fulfill a requirement that affects the AIMS ability to achieve its intended outcomes.""")
    minor_nonconformity = PermissibleValue(
        text="minor_nonconformity",
        description="Isolated lapse that does not significantly affect AIMS effectiveness.")
    observation = PermissibleValue(
        text="observation",
        description="Noted condition that could lead to a nonconformity if not addressed.")
    positive_finding = PermissibleValue(
        text="positive_finding",
        description="Evidence of effective implementation exceeding requirements.")

    _defn = EnumDefinition(
        name="AuditFindingType",
        description="Classification of internal audit findings for the AIMS.",
    )

class ImpactAssessmentDimension(EnumDefinitionImpl):
    """
    Dimensions evaluated during an AI system impact assessment per Clause 6.1.4. Combines individual/group impacts
    (Annex A.5.4 / Annex B.5.4) with societal-scope impacts (Annex A.5.5 / Annex B.5.5).
    """
    individual = PermissibleValue(
        text="individual",
        description="Consequences for individual persons interacting with or affected by the AI system.")
    group = PermissibleValue(
        text="group",
        description="Consequences for identifiable groups of individuals.")
    societal = PermissibleValue(
        text="societal",
        description="Broader societal consequences.")
    fairness = PermissibleValue(
        text="fairness",
        description="Fair and non-discriminatory treatment of affected individuals and groups (B.5.4).")
    transparency = PermissibleValue(
        text="transparency",
        description="Transparency of organizational AI practices and AI system behaviour (B.5.4).")
    explainability = PermissibleValue(
        text="explainability",
        description="Comprehensibility of important factors driving AI outputs (B.5.4).")
    accountability = PermissibleValue(
        text="accountability",
        description="Clear allocation of accountability for AI-supported decisions (B.5.4).")
    accessibility = PermissibleValue(
        text="accessibility",
        description="Accessibility of the AI system for people with diverse abilities (B.5.4).")
    human_rights = PermissibleValue(
        text="human_rights",
        description="Effects on fundamental human rights (B.5.4).")
    financial = PermissibleValue(
        text="financial",
        description="Financial consequences for affected individuals or organizations (B.5.4).")
    health = PermissibleValue(
        text="health",
        description="Effects on physical or mental health (B.5.4).")
    environmental = PermissibleValue(
        text="environmental",
        description="Environmental consequences attributable to the AI system (B.5.5).")
    economic = PermissibleValue(
        text="economic",
        description="Wider economic consequences (B.5.5).")
    government = PermissibleValue(
        text="government",
        description="Consequences for democratic processes, governance, or rule of law (B.5.5).")
    cultural_norms = PermissibleValue(
        text="cultural_norms",
        description="Consequences for cultural norms, traditions, or values (B.5.5).")
    safety = PermissibleValue(
        text="safety",
        description="Safety-related consequences in the deployment context.")
    privacy = PermissibleValue(
        text="privacy",
        description="Privacy-related consequences for data subjects.")
    security = PermissibleValue(
        text="security",
        description="Information security consequences attributable to the AI system.")

    _defn = EnumDefinition(
        name="ImpactAssessmentDimension",
        description="""Dimensions evaluated during an AI system impact assessment per Clause 6.1.4. Combines individual/group impacts (Annex A.5.4 / Annex B.5.4) with societal-scope impacts (Annex A.5.5 / Annex B.5.5).""",
    )

class AnnexAControlId(EnumDefinitionImpl):
    """
    Normative reference control identifiers from Annex A of ISO/IEC 42001:2023 (38 controls across nine families
    A.2-A.10). Permissible value names use underscores in place of dots; the `meaning` slot preserves the Annex A
    dotted form. Control titles are paraphrased.
    """
    a_2_2 = PermissibleValue(
        text="a_2_2",
        description="AI policy - document a policy governing AI system development or use.")
    a_2_3 = PermissibleValue(
        text="a_2_3",
        description="Alignment with other organizational policies - reconcile AI objectives with related policies.")
    a_2_4 = PermissibleValue(
        text="a_2_4",
        description="""Review of the AI policy - planned and event-driven policy review for suitability and effectiveness.""")
    a_3_2 = PermissibleValue(
        text="a_3_2",
        description="AI roles and responsibilities - define and allocate AI-related roles per organizational needs.")
    a_3_3 = PermissibleValue(
        text="a_3_3",
        description="""Reporting of concerns - process for raising concerns about the organization's role with respect to AI.""")
    a_4_2 = PermissibleValue(
        text="a_4_2",
        description="Resource documentation - identify and document resources used at each AI lifecycle stage.")
    a_4_3 = PermissibleValue(
        text="a_4_3",
        description="Data resources - document data resources used by the AI system.")
    a_4_4 = PermissibleValue(
        text="a_4_4",
        description="Tooling resources - document tooling resources used by the AI system.")
    a_4_5 = PermissibleValue(
        text="a_4_5",
        description="""System and computing resources - document system and computing resources used by the AI system.""")
    a_4_6 = PermissibleValue(
        text="a_4_6",
        description="Human resources - document human resources and competences across the AI lifecycle.")
    a_5_2 = PermissibleValue(
        text="a_5_2",
        description="""AI system impact assessment process - establish a process to assess consequences across the lifecycle.""")
    a_5_3 = PermissibleValue(
        text="a_5_3",
        description="Documentation of AI system impact assessments - record and retain assessment results.")
    a_5_4 = PermissibleValue(
        text="a_5_4",
        description="""Assessing AI system impact on individuals or groups - evaluate and document impacts to individuals.""")
    a_5_5 = PermissibleValue(
        text="a_5_5",
        description="Assessing societal impacts of AI systems - evaluate and document broader societal impacts.")
    a_6_1_2 = PermissibleValue(
        text="a_6_1_2",
        description="""Objectives for responsible development - identify objectives that guide responsible AI development.""")
    a_6_1_3 = PermissibleValue(
        text="a_6_1_3",
        description="""Processes for responsible AI system design and development - document the design and development processes.""")
    a_6_2_2 = PermissibleValue(
        text="a_6_2_2",
        description="""AI system requirements and specification - specify requirements for new or enhanced AI systems.""")
    a_6_2_3 = PermissibleValue(
        text="a_6_2_3",
        description="""Documentation of AI system design and development - document design and development against requirements.""")
    a_6_2_4 = PermissibleValue(
        text="a_6_2_4",
        description="AI system verification and validation - define and document V&V measures and criteria.")
    a_6_2_5 = PermissibleValue(
        text="a_6_2_5",
        description="AI system deployment - document a deployment plan and verify pre-deployment requirements.")
    a_6_2_6 = PermissibleValue(
        text="a_6_2_6",
        description="""AI system operation and monitoring - document operational and performance monitoring, repairs, updates, and support.""")
    a_6_2_7 = PermissibleValue(
        text="a_6_2_7",
        description="""AI system technical documentation - provide technical documentation tailored to each interested party.""")
    a_6_2_8 = PermissibleValue(
        text="a_6_2_8",
        description="""AI system recording of event logs - enable event log recording across relevant lifecycle phases.""")
    a_7_2 = PermissibleValue(
        text="a_7_2",
        description="""Data for development and enhancement - define and implement data management processes for AI development.""")
    a_7_3 = PermissibleValue(
        text="a_7_3",
        description="Acquisition of data - document acquisition and selection details for data used in AI systems.")
    a_7_4 = PermissibleValue(
        text="a_7_4",
        description="Quality of data for AI systems - define and meet data quality requirements.")
    a_7_5 = PermissibleValue(
        text="a_7_5",
        description="Data provenance - record data provenance across the data and AI system life cycles.")
    a_7_6 = PermissibleValue(
        text="a_7_6",
        description="Data preparation - document criteria and methods used for data preparation.")
    a_8_2 = PermissibleValue(
        text="a_8_2",
        description="""System documentation and information for users - provide information needed by AI system users.""")
    a_8_3 = PermissibleValue(
        text="a_8_3",
        description="External reporting - enable interested parties to report adverse impacts.")
    a_8_4 = PermissibleValue(
        text="a_8_4",
        description="Communication of incidents - document a plan for communicating incidents to users.")
    a_8_5 = PermissibleValue(
        text="a_8_5",
        description="""Information for interested parties - document obligations to report AI system information to interested parties.""")
    a_9_2 = PermissibleValue(
        text="a_9_2",
        description="Processes for responsible use of AI systems - define and document responsible use processes.")
    a_9_3 = PermissibleValue(
        text="a_9_3",
        description="""Objectives for responsible use of AI system - identify and document responsible-use objectives.""")
    a_9_4 = PermissibleValue(
        text="a_9_4",
        description="Intended use of the AI system - ensure use aligns with the documented intended use.")
    a_10_2 = PermissibleValue(
        text="a_10_2",
        description="""Allocating responsibilities - allocate AI lifecycle responsibilities across organization, partners, suppliers, customers, third parties.""")
    a_10_3 = PermissibleValue(
        text="a_10_3",
        description="""Suppliers - ensure supplier-provided services, products, and materials align with the organization's responsible AI approach.""")
    a_10_4 = PermissibleValue(
        text="a_10_4",
        description="""Customers - account for customer expectations and needs in the organization's responsible AI approach.""")

    _defn = EnumDefinition(
        name="AnnexAControlId",
        description="""Normative reference control identifiers from Annex A of ISO/IEC 42001:2023 (38 controls across nine families A.2-A.10). Permissible value names use underscores in place of dots; the `meaning` slot preserves the Annex A dotted form. Control titles are paraphrased.""",
    )

class SectorDomain(EnumDefinitionImpl):
    """
    Application sectors referenced in Annex D of ISO/IEC 42001:2023 in which the AIMS can be deployed jointly with
    sector-specific management system standards (e.g., ISO 13485, ISO 22000, IEC 62304).
    """
    health = PermissibleValue(
        text="health",
        description="Health, medical devices, and healthcare delivery contexts.")
    defence = PermissibleValue(
        text="defence",
        description="Defence, security, and dual-use technology contexts.")
    transport = PermissibleValue(
        text="transport",
        description="Transport, mobility, and autonomous vehicle contexts.")
    finance = PermissibleValue(
        text="finance",
        description="Financial services, banking, insurance, and capital markets.")
    employment = PermissibleValue(
        text="employment",
        description="Hiring, workforce management, and employee evaluation.")
    energy = PermissibleValue(
        text="energy",
        description="Energy production, distribution, and grid management.")
    public_sector = PermissibleValue(
        text="public_sector",
        description="Government, public administration, and public-service delivery.")
    education = PermissibleValue(
        text="education",
        description="Education, training, and academic assessment contexts.")
    manufacturing = PermissibleValue(
        text="manufacturing",
        description="Industrial and manufacturing automation.")
    agriculture = PermissibleValue(
        text="agriculture",
        description="Agricultural production and food-supply contexts.")
    telecommunications = PermissibleValue(
        text="telecommunications",
        description="Telecommunications and network operations.")
    retail = PermissibleValue(
        text="retail",
        description="Retail, e-commerce, and consumer products.")
    other = PermissibleValue(
        text="other",
        description="Other sector not enumerated above.")

    _defn = EnumDefinition(
        name="SectorDomain",
        description="""Application sectors referenced in Annex D of ISO/IEC 42001:2023 in which the AIMS can be deployed jointly with sector-specific management system standards (e.g., ISO 13485, ISO 22000, IEC 62304).""",
    )

class LearningParadigm(EnumDefinitionImpl):
    """
    Learning paradigm of an AI system, informing risk considerations related to data provenance, drift, and
    behavioural change over time (see ISO/IEC 42001:2023 Introduction and Annex C.3.4).
    """
    static = PermissibleValue(
        text="static",
        description="Trained once and deployed without further learning during operation.")
    periodic_retraining = PermissibleValue(
        text="periodic_retraining",
        description="Retrained on a defined cadence with controlled release cycles.")
    continuous_learning = PermissibleValue(
        text="continuous_learning",
        description="Updates its behaviour during operation based on new data or feedback.")
    online_learning = PermissibleValue(
        text="online_learning",
        description="Continuously updates parameters from a stream of data.")
    transfer_learning = PermissibleValue(
        text="transfer_learning",
        description="Adapted from a pre-trained model to a new task or domain.")
    reinforcement_learning = PermissibleValue(
        text="reinforcement_learning",
        description="Learns a policy through interaction with an environment and reward signals.")
    hybrid = PermissibleValue(
        text="hybrid",
        description="Combines multiple learning paradigms (e.g., supervised plus reinforcement).")
    not_applicable = PermissibleValue(
        text="not_applicable",
        description="AI system that is not based on machine learning (e.g., rule-based).")

    _defn = EnumDefinition(
        name="LearningParadigm",
        description="""Learning paradigm of an AI system, informing risk considerations related to data provenance, drift, and behavioural change over time (see ISO/IEC 42001:2023 Introduction and Annex C.3.4).""",
    )

class AIIncidentCategory(EnumDefinitionImpl):
    """
    AI-specific incident categories supplementing classical information security incident classes. Supports incident
    triage and communication per Annex A.8.3 (External reporting) and A.8.4 (Communication of incidents).
    """
    data_poisoning = PermissibleValue(
        text="data_poisoning",
        description="Training or production data manipulated to compromise model behaviour.")
    model_stealing = PermissibleValue(
        text="model_stealing",
        description="Unauthorized extraction or reconstruction of a deployed model.")
    model_inversion = PermissibleValue(
        text="model_inversion",
        description="Reconstruction of sensitive training data via model queries.")
    membership_inference = PermissibleValue(
        text="membership_inference",
        description="Inference of whether a record was part of the training set.")
    prompt_injection = PermissibleValue(
        text="prompt_injection",
        description="Adversarial inputs causing the model to deviate from intended behaviour.")
    hallucination = PermissibleValue(
        text="hallucination",
        description="Confidently incorrect or fabricated outputs causing material harm.")
    model_drift = PermissibleValue(
        text="model_drift",
        description="Performance or behaviour degradation due to distribution shift.")
    bias_incident = PermissibleValue(
        text="bias_incident",
        description="Unfair or discriminatory outcomes affecting individuals or groups.")
    safety_incident = PermissibleValue(
        text="safety_incident",
        description="Harm to life, health, property, or the environment from AI behaviour.")
    privacy_breach = PermissibleValue(
        text="privacy_breach",
        description="Unauthorized disclosure of personal data via the AI system.")
    security_breach = PermissibleValue(
        text="security_breach",
        description="Compromise of confidentiality, integrity, or availability of the AI system.")
    misuse = PermissibleValue(
        text="misuse",
        description="Use of the AI system outside its documented intended use.")
    adverse_societal_impact = PermissibleValue(
        text="adverse_societal_impact",
        description="Broader societal harm reported by external interested parties.")
    other = PermissibleValue(
        text="other",
        description="Other AI incident category not enumerated above.")

    _defn = EnumDefinition(
        name="AIIncidentCategory",
        description="""AI-specific incident categories supplementing classical information security incident classes. Supports incident triage and communication per Annex A.8.3 (External reporting) and A.8.4 (Communication of incidents).""",
    )

class AuditType(EnumDefinitionImpl):
    """
    Type of audit conducted against the AIMS per Clause 9.2 and the ISO 19011 audit taxonomy.
    """
    internal = PermissibleValue(
        text="internal",
        description="First-party audit conducted by the organization itself or on its behalf.")
    external_second_party = PermissibleValue(
        text="external_second_party",
        description="Second-party audit conducted by an interested party (e.g., customer).")
    external_third_party = PermissibleValue(
        text="external_third_party",
        description="Third-party audit conducted by an independent certification body.")
    surveillance = PermissibleValue(
        text="surveillance",
        description="Ongoing surveillance audit during the certification cycle.")
    recertification = PermissibleValue(
        text="recertification",
        description="Audit performed to renew certification.")
    combined = PermissibleValue(
        text="combined",
        description="Combined audit covering two or more management system disciplines.")

    _defn = EnumDefinition(
        name="AuditType",
        description="Type of audit conducted against the AIMS per Clause 9.2 and the ISO 19011 audit taxonomy.",
    )

class MLApproach(EnumDefinitionImpl):
    """
    Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in B.6.2.3.
    Distinct from `LearningParadigm`, which describes how often the model updates.
    """
    supervised = PermissibleValue(
        text="supervised",
        description="Learns from labelled examples.")
    unsupervised = PermissibleValue(
        text="unsupervised",
        description="Discovers structure in unlabelled data.")
    semi_supervised = PermissibleValue(
        text="semi_supervised",
        description="Combines a small labelled set with a larger unlabelled set.")
    self_supervised = PermissibleValue(
        text="self_supervised",
        description="Generates supervisory signals from the data itself.")
    reinforcement = PermissibleValue(
        text="reinforcement",
        description="Learns a policy through interaction with an environment and reward signals.")
    transfer = PermissibleValue(
        text="transfer",
        description="Adapts a pre-trained model to a new task or domain.")
    federated = PermissibleValue(
        text="federated",
        description="Trains across distributed data holders without centralizing raw data.")
    generative = PermissibleValue(
        text="generative",
        description="Generative modelling approach (e.g., LLMs, diffusion models).")
    symbolic = PermissibleValue(
        text="symbolic",
        description="Rule-based or symbolic reasoning, not statistical ML.")
    hybrid = PermissibleValue(
        text="hybrid",
        description="Combines multiple ML approaches.")
    not_applicable = PermissibleValue(
        text="not_applicable",
        description="AI system not based on machine learning.")

    _defn = EnumDefinition(
        name="MLApproach",
        description="""Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in B.6.2.3. Distinct from `LearningParadigm`, which describes how often the model updates.""",
    )

class DataPreparationMethod(EnumDefinitionImpl):
    """
    Common data preparation and transformation methods documented per Annex A.7.6 and Annex B.7.6.
    """
    statistical_exploration = PermissibleValue(
        text="statistical_exploration",
        description="Distribution, mean, median, standard deviation, range, stratification, sampling.")
    cleaning = PermissibleValue(
        text="cleaning",
        description="Correcting entries and handling malformed records.")
    imputation = PermissibleValue(
        text="imputation",
        description="Filling in missing entries.")
    normalization = PermissibleValue(
        text="normalization",
        description="Re-scaling values to a common range or distribution.")
    scaling = PermissibleValue(
        text="scaling",
        description="Multiplicative re-scaling of feature values.")
    labelling = PermissibleValue(
        text="labelling",
        description="Assigning target labels to records.")
    encoding = PermissibleValue(
        text="encoding",
        description="Converting categorical variables to numeric representations.")
    augmentation = PermissibleValue(
        text="augmentation",
        description="Synthesising additional training samples from existing data.")
    deduplication = PermissibleValue(
        text="deduplication",
        description="Removing duplicate records.")
    anonymization = PermissibleValue(
        text="anonymization",
        description="Removing or transforming personally identifying information.")
    other = PermissibleValue(
        text="other",
        description="Other preparation method not enumerated above.")

    _defn = EnumDefinition(
        name="DataPreparationMethod",
        description="Common data preparation and transformation methods documented per Annex A.7.6 and Annex B.7.6.",
    )

class RelatedManagementSystem(EnumDefinitionImpl):
    """
    Related management-system standards with which the AIMS may be jointly implemented, per the Introduction
    (Compatibility with other management system standards) and Annex D.
    """
    iso_iec_27001 = PermissibleValue(
        text="iso_iec_27001",
        description="Information security management systems.")
    iso_iec_27701 = PermissibleValue(
        text="iso_iec_27701",
        description="Privacy information management.")
    iso_9001 = PermissibleValue(
        text="iso_9001",
        description="Quality management systems.")
    iso_22000 = PermissibleValue(
        text="iso_22000",
        description="Food safety management systems.")
    iso_13485 = PermissibleValue(
        text="iso_13485",
        description="Medical-device quality management systems.")
    iec_62304 = PermissibleValue(
        text="iec_62304",
        description="Medical device software life cycle processes.")
    iso_iec_5338 = PermissibleValue(
        text="iso_iec_5338",
        description="AI system life cycle process.")
    iso_iec_5259 = PermissibleValue(
        text="iso_iec_5259",
        description="Data quality for analytics and ML.")
    iso_iec_22989 = PermissibleValue(
        text="iso_iec_22989",
        description="AI concepts and terminology (normative reference).")
    iso_iec_23894 = PermissibleValue(
        text="iso_iec_23894",
        description="AI risk management guidance.")
    iso_iec_38507 = PermissibleValue(
        text="iso_iec_38507",
        description="Governance of IT - AI governance implications.")
    iso_iec_27000 = PermissibleValue(
        text="iso_iec_27000",
        description="Information security management - overview and vocabulary.")
    iso_iec_29100 = PermissibleValue(
        text="iso_iec_29100",
        description="Privacy framework.")
    iso_31000 = PermissibleValue(
        text="iso_31000",
        description="Risk management guidelines.")
    iso_iec_25024 = PermissibleValue(
        text="iso_iec_25024",
        description="Measurement of data quality.")
    iso_iec_25059 = PermissibleValue(
        text="iso_iec_25059",
        description="Quality model for AI systems.")
    iso_19011 = PermissibleValue(
        text="iso_19011",
        description="Guidelines for auditing management systems.")
    iso_37002 = PermissibleValue(
        text="iso_37002",
        description="Whistleblowing management systems (informs A.3.3 concern reporting).")
    other = PermissibleValue(
        text="other",
        description="Other management system standard not enumerated above.")

    _defn = EnumDefinition(
        name="RelatedManagementSystem",
        description="""Related management-system standards with which the AIMS may be jointly implemented, per the Introduction (Compatibility with other management system standards) and Annex D.""",
    )

class GovernanceRoleType(EnumDefinitionImpl):
    """
    Governance role types within the AIMS, paraphrased from Clause 3.3 (top management), Clause 3.22 (governing body),
    Clause 5.3, and Annex A.3.2. Use this enum on `role_type` for normative governance positions; free-form strings
    remain accepted for organization-defined roles.
    """
    governing_body = PermissibleValue(
        text="governing_body",
        description="Board, trustees, or other body accountable for organizational performance (3.22).")
    top_management = PermissibleValue(
        text="top_management",
        description="Person or group directing and controlling the organization at the highest level (3.3).")
    designated_management = PermissibleValue(
        text="designated_management",
        description="Management designated to approve AI risk treatment plans and residual-risk acceptance (6.1.3).")
    chief_ai_officer = PermissibleValue(
        text="chief_ai_officer",
        description="Senior executive accountable for the AIMS.")
    ai_risk_owner = PermissibleValue(
        text="ai_risk_owner",
        description="Person accountable for managing a specific AI risk (6.1.2).")
    ai_policy_owner = PermissibleValue(
        text="ai_policy_owner",
        description="Role accountable for AI policy development and review (A.2.4).")
    ai_oversight_committee = PermissibleValue(
        text="ai_oversight_committee",
        description="Cross-functional committee providing oversight of AI systems.")
    data_steward = PermissibleValue(
        text="data_steward",
        description="Role accountable for data resources used by AI systems (A.4.3, A.7).")
    model_validator = PermissibleValue(
        text="model_validator",
        description="Role responsible for verification and validation of AI models (A.6.2.4).")
    human_oversight_reviewer = PermissibleValue(
        text="human_oversight_reviewer",
        description="Role performing human-in-the-loop review of AI outputs (B.9.3).")
    ai_developer = PermissibleValue(
        text="ai_developer",
        description="Role developing AI systems or components.")
    ai_operator = PermissibleValue(
        text="ai_operator",
        description="Role operating and monitoring AI systems in production.")
    ai_impact_assessor = PermissibleValue(
        text="ai_impact_assessor",
        description="Role conducting AI system impact assessments (6.1.4).")
    auditor = PermissibleValue(
        text="auditor",
        description="Internal or external auditor of the AIMS (9.2).")
    other = PermissibleValue(
        text="other",
        description="Other governance role not enumerated above.")

    _defn = EnumDefinition(
        name="GovernanceRoleType",
        description="""Governance role types within the AIMS, paraphrased from Clause 3.3 (top management), Clause 3.22 (governing body), Clause 5.3, and Annex A.3.2. Use this enum on `role_type` for normative governance positions; free-form strings remain accepted for organization-defined roles.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=ISO42001.id, name="id", curie=ISO42001.curie('id'),
                   model_uri=ISO42001.id, domain=None, range=URIRef)

slots.name = Slot(uri=ISO42001.name, name="name", curie=ISO42001.curie('name'),
                   model_uri=ISO42001.name, domain=None, range=str)

slots.description = Slot(uri=ISO42001.description, name="description", curie=ISO42001.curie('description'),
                   model_uri=ISO42001.description, domain=None, range=Optional[str])

slots.version = Slot(uri=ISO42001.version, name="version", curie=ISO42001.curie('version'),
                   model_uri=ISO42001.version, domain=None, range=Optional[str])

slots.created_date = Slot(uri=ISO42001.created_date, name="created_date", curie=ISO42001.curie('created_date'),
                   model_uri=ISO42001.created_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.modified_date = Slot(uri=ISO42001.modified_date, name="modified_date", curie=ISO42001.curie('modified_date'),
                   model_uri=ISO42001.modified_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.document_type = Slot(uri=ISO42001.document_type, name="document_type", curie=ISO42001.curie('document_type'),
                   model_uri=ISO42001.document_type, domain=None, range=Optional[Union[str, "DocumentType"]])

slots.document_reference = Slot(uri=ISO42001.document_reference, name="document_reference", curie=ISO42001.curie('document_reference'),
                   model_uri=ISO42001.document_reference, domain=None, range=Optional[str])

slots.author = Slot(uri=ISO42001.author, name="author", curie=ISO42001.curie('author'),
                   model_uri=ISO42001.author, domain=None, range=Optional[str])

slots.owner = Slot(uri=ISO42001.owner, name="owner", curie=ISO42001.curie('owner'),
                   model_uri=ISO42001.owner, domain=None, range=Optional[str])

slots.approved_by = Slot(uri=ISO42001.approved_by, name="approved_by", curie=ISO42001.curie('approved_by'),
                   model_uri=ISO42001.approved_by, domain=None, range=Optional[str])

slots.approved_date = Slot(uri=ISO42001.approved_date, name="approved_date", curie=ISO42001.curie('approved_date'),
                   model_uri=ISO42001.approved_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effective_date = Slot(uri=ISO42001.effective_date, name="effective_date", curie=ISO42001.curie('effective_date'),
                   model_uri=ISO42001.effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.review_date = Slot(uri=ISO42001.review_date, name="review_date", curie=ISO42001.curie('review_date'),
                   model_uri=ISO42001.review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.status = Slot(uri=ISO42001.status, name="status", curie=ISO42001.curie('status'),
                   model_uri=ISO42001.status, domain=None, range=Optional[str])

slots.classification = Slot(uri=ISO42001.classification, name="classification", curie=ISO42001.curie('classification'),
                   model_uri=ISO42001.classification, domain=None, range=Optional[str])

slots.retention_period = Slot(uri=ISO42001.retention_period, name="retention_period", curie=ISO42001.curie('retention_period'),
                   model_uri=ISO42001.retention_period, domain=None, range=Optional[str])

slots.organization = Slot(uri=ISO42001.organization, name="organization", curie=ISO42001.curie('organization'),
                   model_uri=ISO42001.organization, domain=None, range=Optional[Union[str, OrganizationId]])

slots.legal_name = Slot(uri=ISO42001.legal_name, name="legal_name", curie=ISO42001.curie('legal_name'),
                   model_uri=ISO42001.legal_name, domain=None, range=Optional[str])

slots.trading_names = Slot(uri=ISO42001.trading_names, name="trading_names", curie=ISO42001.curie('trading_names'),
                   model_uri=ISO42001.trading_names, domain=None, range=Optional[Union[str, list[str]]])

slots.organization_type = Slot(uri=ISO42001.organization_type, name="organization_type", curie=ISO42001.curie('organization_type'),
                   model_uri=ISO42001.organization_type, domain=None, range=Optional[str])

slots.industry_sector = Slot(uri=ISO42001.industry_sector, name="industry_sector", curie=ISO42001.curie('industry_sector'),
                   model_uri=ISO42001.industry_sector, domain=None, range=Optional[str])

slots.sector_domains = Slot(uri=ISO42001.sector_domains, name="sector_domains", curie=ISO42001.curie('sector_domains'),
                   model_uri=ISO42001.sector_domains, domain=None, range=Optional[Union[Union[str, "SectorDomain"], list[Union[str, "SectorDomain"]]]])

slots.size_category = Slot(uri=ISO42001.size_category, name="size_category", curie=ISO42001.curie('size_category'),
                   model_uri=ISO42001.size_category, domain=None, range=Optional[str])

slots.employee_count = Slot(uri=ISO42001.employee_count, name="employee_count", curie=ISO42001.curie('employee_count'),
                   model_uri=ISO42001.employee_count, domain=None, range=Optional[int])

slots.geographic_locations = Slot(uri=ISO42001.geographic_locations, name="geographic_locations", curie=ISO42001.curie('geographic_locations'),
                   model_uri=ISO42001.geographic_locations, domain=None, range=Optional[Union[str, list[str]]])

slots.regulatory_jurisdictions = Slot(uri=ISO42001.regulatory_jurisdictions, name="regulatory_jurisdictions", curie=ISO42001.curie('regulatory_jurisdictions'),
                   model_uri=ISO42001.regulatory_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.parent_organization = Slot(uri=ISO42001.parent_organization, name="parent_organization", curie=ISO42001.curie('parent_organization'),
                   model_uri=ISO42001.parent_organization, domain=None, range=Optional[str])

slots.subsidiaries = Slot(uri=ISO42001.subsidiaries, name="subsidiaries", curie=ISO42001.curie('subsidiaries'),
                   model_uri=ISO42001.subsidiaries, domain=None, range=Optional[Union[str, list[str]]])

slots.ai_roles = Slot(uri=ISO42001.ai_roles, name="ai_roles", curie=ISO42001.curie('ai_roles'),
                   model_uri=ISO42001.ai_roles, domain=None, range=Optional[Union[Union[str, "AIOrganizationalRole"], list[Union[str, "AIOrganizationalRole"]]]])

slots.organizational_roles_with_ai = Slot(uri=ISO42001.organizational_roles_with_ai, name="organizational_roles_with_ai", curie=ISO42001.curie('organizational_roles_with_ai'),
                   model_uri=ISO42001.organizational_roles_with_ai, domain=None, range=Optional[Union[Union[str, "AIOrganizationalRole"], list[Union[str, "AIOrganizationalRole"]]]])

slots.scope_statement = Slot(uri=ISO42001.scope_statement, name="scope_statement", curie=ISO42001.curie('scope_statement'),
                   model_uri=ISO42001.scope_statement, domain=None, range=Optional[str])

slots.scope_boundaries = Slot(uri=ISO42001.scope_boundaries, name="scope_boundaries", curie=ISO42001.curie('scope_boundaries'),
                   model_uri=ISO42001.scope_boundaries, domain=None, range=Optional[Union[str, list[str]]])

slots.scope_exclusions = Slot(uri=ISO42001.scope_exclusions, name="scope_exclusions", curie=ISO42001.curie('scope_exclusions'),
                   model_uri=ISO42001.scope_exclusions, domain=None, range=Optional[Union[str, list[str]]])

slots.context_internal_issues = Slot(uri=ISO42001.context_internal_issues, name="context_internal_issues", curie=ISO42001.curie('context_internal_issues'),
                   model_uri=ISO42001.context_internal_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.context_external_issues = Slot(uri=ISO42001.context_external_issues, name="context_external_issues", curie=ISO42001.curie('context_external_issues'),
                   model_uri=ISO42001.context_external_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.climate_change_relevant = Slot(uri=ISO42001.climate_change_relevant, name="climate_change_relevant", curie=ISO42001.curie('climate_change_relevant'),
                   model_uri=ISO42001.climate_change_relevant, domain=None, range=Optional[Union[bool, Bool]])

slots.interested_parties = Slot(uri=ISO42001.interested_parties, name="interested_parties", curie=ISO42001.curie('interested_parties'),
                   model_uri=ISO42001.interested_parties, domain=None, range=Optional[Union[Union[str, InterestedPartyId], list[Union[str, InterestedPartyId]]]])

slots.party_type = Slot(uri=ISO42001.party_type, name="party_type", curie=ISO42001.curie('party_type'),
                   model_uri=ISO42001.party_type, domain=None, range=Optional[str])

slots.relationship = Slot(uri=ISO42001.relationship, name="relationship", curie=ISO42001.curie('relationship'),
                   model_uri=ISO42001.relationship, domain=None, range=Optional[str])

slots.requirements = Slot(uri=ISO42001.requirements, name="requirements", curie=ISO42001.curie('requirements'),
                   model_uri=ISO42001.requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.communication_needs = Slot(uri=ISO42001.communication_needs, name="communication_needs", curie=ISO42001.curie('communication_needs'),
                   model_uri=ISO42001.communication_needs, domain=None, range=Optional[str])

slots.contact_information = Slot(uri=ISO42001.contact_information, name="contact_information", curie=ISO42001.curie('contact_information'),
                   model_uri=ISO42001.contact_information, domain=None, range=Optional[str])

slots.ai_policy = Slot(uri=ISO42001.ai_policy, name="ai_policy", curie=ISO42001.curie('ai_policy'),
                   model_uri=ISO42001.ai_policy, domain=None, range=Optional[Union[str, AIPolicyId]])

slots.policy_statement = Slot(uri=ISO42001.policy_statement, name="policy_statement", curie=ISO42001.curie('policy_statement'),
                   model_uri=ISO42001.policy_statement, domain=None, range=Optional[str])

slots.policy_objectives_framework = Slot(uri=ISO42001.policy_objectives_framework, name="policy_objectives_framework", curie=ISO42001.curie('policy_objectives_framework'),
                   model_uri=ISO42001.policy_objectives_framework, domain=None, range=Optional[str])

slots.commitment_statements = Slot(uri=ISO42001.commitment_statements, name="commitment_statements", curie=ISO42001.curie('commitment_statements'),
                   model_uri=ISO42001.commitment_statements, domain=None, range=Optional[Union[str, list[str]]])

slots.applicability_statement = Slot(uri=ISO42001.applicability_statement, name="applicability_statement", curie=ISO42001.curie('applicability_statement'),
                   model_uri=ISO42001.applicability_statement, domain=None, range=Optional[str])

slots.communication_date = Slot(uri=ISO42001.communication_date, name="communication_date", curie=ISO42001.curie('communication_date'),
                   model_uri=ISO42001.communication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.acknowledgment_required = Slot(uri=ISO42001.acknowledgment_required, name="acknowledgment_required", curie=ISO42001.curie('acknowledgment_required'),
                   model_uri=ISO42001.acknowledgment_required, domain=None, range=Optional[Union[bool, Bool]])

slots.related_topic_policies = Slot(uri=ISO42001.related_topic_policies, name="related_topic_policies", curie=ISO42001.curie('related_topic_policies'),
                   model_uri=ISO42001.related_topic_policies, domain=None, range=Optional[Union[Union[str, TopicSpecificPolicyId], list[Union[str, TopicSpecificPolicyId]]]])

slots.last_policy_review_date = Slot(uri=ISO42001.last_policy_review_date, name="last_policy_review_date", curie=ISO42001.curie('last_policy_review_date'),
                   model_uri=ISO42001.last_policy_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.next_policy_review_date = Slot(uri=ISO42001.next_policy_review_date, name="next_policy_review_date", curie=ISO42001.curie('next_policy_review_date'),
                   model_uri=ISO42001.next_policy_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.topic_area = Slot(uri=ISO42001.topic_area, name="topic_area", curie=ISO42001.curie('topic_area'),
                   model_uri=ISO42001.topic_area, domain=None, range=Optional[str])

slots.parent_policy = Slot(uri=ISO42001.parent_policy, name="parent_policy", curie=ISO42001.curie('parent_policy'),
                   model_uri=ISO42001.parent_policy, domain=None, range=Optional[Union[str, AIPolicyId]])

slots.applicable_controls = Slot(uri=ISO42001.applicable_controls, name="applicable_controls", curie=ISO42001.curie('applicable_controls'),
                   model_uri=ISO42001.applicable_controls, domain=None, range=Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]])

slots.target_audience = Slot(uri=ISO42001.target_audience, name="target_audience", curie=ISO42001.curie('target_audience'),
                   model_uri=ISO42001.target_audience, domain=None, range=Optional[str])

slots.roles = Slot(uri=ISO42001.roles, name="roles", curie=ISO42001.curie('roles'),
                   model_uri=ISO42001.roles, domain=None, range=Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]])

slots.role_type = Slot(uri=ISO42001.role_type, name="role_type", curie=ISO42001.curie('role_type'),
                   model_uri=ISO42001.role_type, domain=None, range=Optional[str])

slots.responsibilities = Slot(uri=ISO42001.responsibilities, name="responsibilities", curie=ISO42001.curie('responsibilities'),
                   model_uri=ISO42001.responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.authorities = Slot(uri=ISO42001.authorities, name="authorities", curie=ISO42001.curie('authorities'),
                   model_uri=ISO42001.authorities, domain=None, range=Optional[Union[str, list[str]]])

slots.accountability = Slot(uri=ISO42001.accountability, name="accountability", curie=ISO42001.curie('accountability'),
                   model_uri=ISO42001.accountability, domain=None, range=Optional[str])

slots.assigned_to = Slot(uri=ISO42001.assigned_to, name="assigned_to", curie=ISO42001.curie('assigned_to'),
                   model_uri=ISO42001.assigned_to, domain=None, range=Optional[Union[str, list[str]]])

slots.delegation_rules = Slot(uri=ISO42001.delegation_rules, name="delegation_rules", curie=ISO42001.curie('delegation_rules'),
                   model_uri=ISO42001.delegation_rules, domain=None, range=Optional[str])

slots.reporting_line = Slot(uri=ISO42001.reporting_line, name="reporting_line", curie=ISO42001.curie('reporting_line'),
                   model_uri=ISO42001.reporting_line, domain=None, range=Optional[str])

slots.ai_objectives = Slot(uri=ISO42001.ai_objectives, name="ai_objectives", curie=ISO42001.curie('ai_objectives'),
                   model_uri=ISO42001.ai_objectives, domain=None, range=Optional[Union[Union[str, AIObjectiveId], list[Union[str, AIObjectiveId]]]])

slots.objective_statement = Slot(uri=ISO42001.objective_statement, name="objective_statement", curie=ISO42001.curie('objective_statement'),
                   model_uri=ISO42001.objective_statement, domain=None, range=Optional[str])

slots.objective_category = Slot(uri=ISO42001.objective_category, name="objective_category", curie=ISO42001.curie('objective_category'),
                   model_uri=ISO42001.objective_category, domain=None, range=Optional[Union[str, "AIObjectiveCategory"]])

slots.target_value = Slot(uri=ISO42001.target_value, name="target_value", curie=ISO42001.curie('target_value'),
                   model_uri=ISO42001.target_value, domain=None, range=Optional[str])

slots.current_value = Slot(uri=ISO42001.current_value, name="current_value", curie=ISO42001.curie('current_value'),
                   model_uri=ISO42001.current_value, domain=None, range=Optional[str])

slots.metric_definition = Slot(uri=ISO42001.metric_definition, name="metric_definition", curie=ISO42001.curie('metric_definition'),
                   model_uri=ISO42001.metric_definition, domain=None, range=Optional[str])

slots.measurement_method = Slot(uri=ISO42001.measurement_method, name="measurement_method", curie=ISO42001.curie('measurement_method'),
                   model_uri=ISO42001.measurement_method, domain=None, range=Optional[str])

slots.measurement_frequency = Slot(uri=ISO42001.measurement_frequency, name="measurement_frequency", curie=ISO42001.curie('measurement_frequency'),
                   model_uri=ISO42001.measurement_frequency, domain=None, range=Optional[str])

slots.responsible_role = Slot(uri=ISO42001.responsible_role, name="responsible_role", curie=ISO42001.curie('responsible_role'),
                   model_uri=ISO42001.responsible_role, domain=None, range=Optional[Union[str, RoleId]])

slots.target_date = Slot(uri=ISO42001.target_date, name="target_date", curie=ISO42001.curie('target_date'),
                   model_uri=ISO42001.target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.achievement_status = Slot(uri=ISO42001.achievement_status, name="achievement_status", curie=ISO42001.curie('achievement_status'),
                   model_uri=ISO42001.achievement_status, domain=None, range=Optional[str])

slots.action_plan = Slot(uri=ISO42001.action_plan, name="action_plan", curie=ISO42001.curie('action_plan'),
                   model_uri=ISO42001.action_plan, domain=None, range=Optional[str])

slots.ai_risk_assessment_process = Slot(uri=ISO42001.ai_risk_assessment_process, name="ai_risk_assessment_process", curie=ISO42001.curie('ai_risk_assessment_process'),
                   model_uri=ISO42001.ai_risk_assessment_process, domain=None, range=Optional[Union[str, AIRiskAssessmentProcessId]])

slots.alignment_with_ai_policy = Slot(uri=ISO42001.alignment_with_ai_policy, name="alignment_with_ai_policy", curie=ISO42001.curie('alignment_with_ai_policy'),
                   model_uri=ISO42001.alignment_with_ai_policy, domain=None, range=Optional[str])

slots.risk_acceptance_criteria = Slot(uri=ISO42001.risk_acceptance_criteria, name="risk_acceptance_criteria", curie=ISO42001.curie('risk_acceptance_criteria'),
                   model_uri=ISO42001.risk_acceptance_criteria, domain=None, range=Optional[str])

slots.assessment_criteria = Slot(uri=ISO42001.assessment_criteria, name="assessment_criteria", curie=ISO42001.curie('assessment_criteria'),
                   model_uri=ISO42001.assessment_criteria, domain=None, range=Optional[str])

slots.assessment_methodology = Slot(uri=ISO42001.assessment_methodology, name="assessment_methodology", curie=ISO42001.curie('assessment_methodology'),
                   model_uri=ISO42001.assessment_methodology, domain=None, range=Optional[str])

slots.likelihood_scale = Slot(uri=ISO42001.likelihood_scale, name="likelihood_scale", curie=ISO42001.curie('likelihood_scale'),
                   model_uri=ISO42001.likelihood_scale, domain=None, range=Optional[str])

slots.impact_scale = Slot(uri=ISO42001.impact_scale, name="impact_scale", curie=ISO42001.curie('impact_scale'),
                   model_uri=ISO42001.impact_scale, domain=None, range=Optional[str])

slots.risk_matrix = Slot(uri=ISO42001.risk_matrix, name="risk_matrix", curie=ISO42001.curie('risk_matrix'),
                   model_uri=ISO42001.risk_matrix, domain=None, range=Optional[str])

slots.assessment_frequency = Slot(uri=ISO42001.assessment_frequency, name="assessment_frequency", curie=ISO42001.curie('assessment_frequency'),
                   model_uri=ISO42001.assessment_frequency, domain=None, range=Optional[str])

slots.trigger_events = Slot(uri=ISO42001.trigger_events, name="trigger_events", curie=ISO42001.curie('trigger_events'),
                   model_uri=ISO42001.trigger_events, domain=None, range=Optional[Union[str, list[str]]])

slots.ai_risk_assessments = Slot(uri=ISO42001.ai_risk_assessments, name="ai_risk_assessments", curie=ISO42001.curie('ai_risk_assessments'),
                   model_uri=ISO42001.ai_risk_assessments, domain=None, range=Optional[Union[Union[str, AIRiskAssessmentId], list[Union[str, AIRiskAssessmentId]]]])

slots.assessment_scope = Slot(uri=ISO42001.assessment_scope, name="assessment_scope", curie=ISO42001.curie('assessment_scope'),
                   model_uri=ISO42001.assessment_scope, domain=None, range=Optional[str])

slots.ai_systems_assessed = Slot(uri=ISO42001.ai_systems_assessed, name="ai_systems_assessed", curie=ISO42001.curie('ai_systems_assessed'),
                   model_uri=ISO42001.ai_systems_assessed, domain=None, range=Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]])

slots.assessment_date = Slot(uri=ISO42001.assessment_date, name="assessment_date", curie=ISO42001.curie('assessment_date'),
                   model_uri=ISO42001.assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.assessor = Slot(uri=ISO42001.assessor, name="assessor", curie=ISO42001.curie('assessor'),
                   model_uri=ISO42001.assessor, domain=None, range=Optional[str])

slots.methodology_used = Slot(uri=ISO42001.methodology_used, name="methodology_used", curie=ISO42001.curie('methodology_used'),
                   model_uri=ISO42001.methodology_used, domain=None, range=Optional[str])

slots.risks_identified = Slot(uri=ISO42001.risks_identified, name="risks_identified", curie=ISO42001.curie('risks_identified'),
                   model_uri=ISO42001.risks_identified, domain=None, range=Optional[Union[Union[str, AIRiskId], list[Union[str, AIRiskId]]]])

slots.linked_impact_assessment = Slot(uri=ISO42001.linked_impact_assessment, name="linked_impact_assessment", curie=ISO42001.curie('linked_impact_assessment'),
                   model_uri=ISO42001.linked_impact_assessment, domain=None, range=Optional[Union[str, AISystemImpactAssessmentId]])

slots.summary_findings = Slot(uri=ISO42001.summary_findings, name="summary_findings", curie=ISO42001.curie('summary_findings'),
                   model_uri=ISO42001.summary_findings, domain=None, range=Optional[str])

slots.recommendations = Slot(uri=ISO42001.recommendations, name="recommendations", curie=ISO42001.curie('recommendations'),
                   model_uri=ISO42001.recommendations, domain=None, range=Optional[Union[str, list[str]]])

slots.next_assessment_date = Slot(uri=ISO42001.next_assessment_date, name="next_assessment_date", curie=ISO42001.curie('next_assessment_date'),
                   model_uri=ISO42001.next_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.related_risks = Slot(uri=ISO42001.related_risks, name="related_risks", curie=ISO42001.curie('related_risks'),
                   model_uri=ISO42001.related_risks, domain=None, range=Optional[Union[Union[str, AIRiskId], list[Union[str, AIRiskId]]]])

slots.risk_source_category = Slot(uri=ISO42001.risk_source_category, name="risk_source_category", curie=ISO42001.curie('risk_source_category'),
                   model_uri=ISO42001.risk_source_category, domain=None, range=Optional[Union[str, "AIRiskSourceCategory"]])

slots.risk_source_description = Slot(uri=ISO42001.risk_source_description, name="risk_source_description", curie=ISO42001.curie('risk_source_description'),
                   model_uri=ISO42001.risk_source_description, domain=None, range=Optional[str])

slots.affected_ai_systems = Slot(uri=ISO42001.affected_ai_systems, name="affected_ai_systems", curie=ISO42001.curie('affected_ai_systems'),
                   model_uri=ISO42001.affected_ai_systems, domain=None, range=Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]])

slots.affected_dimensions = Slot(uri=ISO42001.affected_dimensions, name="affected_dimensions", curie=ISO42001.curie('affected_dimensions'),
                   model_uri=ISO42001.affected_dimensions, domain=None, range=Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]])

slots.risk_owner = Slot(uri=ISO42001.risk_owner, name="risk_owner", curie=ISO42001.curie('risk_owner'),
                   model_uri=ISO42001.risk_owner, domain=None, range=Optional[str])

slots.likelihood = Slot(uri=ISO42001.likelihood, name="likelihood", curie=ISO42001.curie('likelihood'),
                   model_uri=ISO42001.likelihood, domain=None, range=Optional[Union[str, "LikelihoodRating"]])

slots.impact = Slot(uri=ISO42001.impact, name="impact", curie=ISO42001.curie('impact'),
                   model_uri=ISO42001.impact, domain=None, range=Optional[Union[str, "ImpactRating"]])

slots.inherent_risk_level = Slot(uri=ISO42001.inherent_risk_level, name="inherent_risk_level", curie=ISO42001.curie('inherent_risk_level'),
                   model_uri=ISO42001.inherent_risk_level, domain=None, range=Optional[Union[str, "RiskLevel"]])

slots.existing_controls = Slot(uri=ISO42001.existing_controls, name="existing_controls", curie=ISO42001.curie('existing_controls'),
                   model_uri=ISO42001.existing_controls, domain=None, range=Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]])

slots.residual_risk_level = Slot(uri=ISO42001.residual_risk_level, name="residual_risk_level", curie=ISO42001.curie('residual_risk_level'),
                   model_uri=ISO42001.residual_risk_level, domain=None, range=Optional[Union[str, "RiskLevel"]])

slots.risk_treatment_option = Slot(uri=ISO42001.risk_treatment_option, name="risk_treatment_option", curie=ISO42001.curie('risk_treatment_option'),
                   model_uri=ISO42001.risk_treatment_option, domain=None, range=Optional[Union[str, "RiskTreatmentOption"]])

slots.treatment_priority = Slot(uri=ISO42001.treatment_priority, name="treatment_priority", curie=ISO42001.curie('treatment_priority'),
                   model_uri=ISO42001.treatment_priority, domain=None, range=Optional[str])

slots.related_treatment_plan = Slot(uri=ISO42001.related_treatment_plan, name="related_treatment_plan", curie=ISO42001.curie('related_treatment_plan'),
                   model_uri=ISO42001.related_treatment_plan, domain=None, range=Optional[Union[str, AIRiskTreatmentPlanId]])

slots.related_impact_assessment = Slot(uri=ISO42001.related_impact_assessment, name="related_impact_assessment", curie=ISO42001.curie('related_impact_assessment'),
                   model_uri=ISO42001.related_impact_assessment, domain=None, range=Optional[Union[str, AISystemImpactAssessmentId]])

slots.ai_risk_treatment_process = Slot(uri=ISO42001.ai_risk_treatment_process, name="ai_risk_treatment_process", curie=ISO42001.curie('ai_risk_treatment_process'),
                   model_uri=ISO42001.ai_risk_treatment_process, domain=None, range=Optional[Union[str, AIRiskTreatmentProcessId]])

slots.treatment_options_guidance = Slot(uri=ISO42001.treatment_options_guidance, name="treatment_options_guidance", curie=ISO42001.curie('treatment_options_guidance'),
                   model_uri=ISO42001.treatment_options_guidance, domain=None, range=Optional[str])

slots.control_selection_criteria = Slot(uri=ISO42001.control_selection_criteria, name="control_selection_criteria", curie=ISO42001.curie('control_selection_criteria'),
                   model_uri=ISO42001.control_selection_criteria, domain=None, range=Optional[str])

slots.soa_template = Slot(uri=ISO42001.soa_template, name="soa_template", curie=ISO42001.curie('soa_template'),
                   model_uri=ISO42001.soa_template, domain=None, range=Optional[str])

slots.approval_workflow = Slot(uri=ISO42001.approval_workflow, name="approval_workflow", curie=ISO42001.curie('approval_workflow'),
                   model_uri=ISO42001.approval_workflow, domain=None, range=Optional[str])

slots.ai_risk_treatment_plans = Slot(uri=ISO42001.ai_risk_treatment_plans, name="ai_risk_treatment_plans", curie=ISO42001.curie('ai_risk_treatment_plans'),
                   model_uri=ISO42001.ai_risk_treatment_plans, domain=None, range=Optional[Union[Union[str, AIRiskTreatmentPlanId], list[Union[str, AIRiskTreatmentPlanId]]]])

slots.plan_scope = Slot(uri=ISO42001.plan_scope, name="plan_scope", curie=ISO42001.curie('plan_scope'),
                   model_uri=ISO42001.plan_scope, domain=None, range=Optional[str])

slots.risks_addressed = Slot(uri=ISO42001.risks_addressed, name="risks_addressed", curie=ISO42001.curie('risks_addressed'),
                   model_uri=ISO42001.risks_addressed, domain=None, range=Optional[Union[Union[str, AIRiskId], list[Union[str, AIRiskId]]]])

slots.treatment_actions = Slot(uri=ISO42001.treatment_actions, name="treatment_actions", curie=ISO42001.curie('treatment_actions'),
                   model_uri=ISO42001.treatment_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.controls_to_implement = Slot(uri=ISO42001.controls_to_implement, name="controls_to_implement", curie=ISO42001.curie('controls_to_implement'),
                   model_uri=ISO42001.controls_to_implement, domain=None, range=Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]])

slots.resources_required = Slot(uri=ISO42001.resources_required, name="resources_required", curie=ISO42001.curie('resources_required'),
                   model_uri=ISO42001.resources_required, domain=None, range=Optional[str])

slots.responsible_parties = Slot(uri=ISO42001.responsible_parties, name="responsible_parties", curie=ISO42001.curie('responsible_parties'),
                   model_uri=ISO42001.responsible_parties, domain=None, range=Optional[Union[str, list[str]]])

slots.implementation_timeline = Slot(uri=ISO42001.implementation_timeline, name="implementation_timeline", curie=ISO42001.curie('implementation_timeline'),
                   model_uri=ISO42001.implementation_timeline, domain=None, range=Optional[str])

slots.risk_owner_approval = Slot(uri=ISO42001.risk_owner_approval, name="risk_owner_approval", curie=ISO42001.curie('risk_owner_approval'),
                   model_uri=ISO42001.risk_owner_approval, domain=None, range=Optional[str])

slots.residual_risk_acceptance = Slot(uri=ISO42001.residual_risk_acceptance, name="residual_risk_acceptance", curie=ISO42001.curie('residual_risk_acceptance'),
                   model_uri=ISO42001.residual_risk_acceptance, domain=None, range=Optional[str])

slots.implementation_status = Slot(uri=ISO42001.implementation_status, name="implementation_status", curie=ISO42001.curie('implementation_status'),
                   model_uri=ISO42001.implementation_status, domain=None, range=Optional[Union[str, "ImplementationStatus"]])

slots.completion_date = Slot(uri=ISO42001.completion_date, name="completion_date", curie=ISO42001.curie('completion_date'),
                   model_uri=ISO42001.completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ai_system_impact_assessment_process = Slot(uri=ISO42001.ai_system_impact_assessment_process, name="ai_system_impact_assessment_process", curie=ISO42001.curie('ai_system_impact_assessment_process'),
                   model_uri=ISO42001.ai_system_impact_assessment_process, domain=None, range=Optional[Union[str, AISystemImpactAssessmentProcessId]])

slots.ai_system_impact_assessments = Slot(uri=ISO42001.ai_system_impact_assessments, name="ai_system_impact_assessments", curie=ISO42001.curie('ai_system_impact_assessments'),
                   model_uri=ISO42001.ai_system_impact_assessments, domain=None, range=Optional[Union[Union[str, AISystemImpactAssessmentId], list[Union[str, AISystemImpactAssessmentId]]]])

slots.dimensions_in_scope = Slot(uri=ISO42001.dimensions_in_scope, name="dimensions_in_scope", curie=ISO42001.curie('dimensions_in_scope'),
                   model_uri=ISO42001.dimensions_in_scope, domain=None, range=Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]])

slots.linkage_to_risk_assessment = Slot(uri=ISO42001.linkage_to_risk_assessment, name="linkage_to_risk_assessment", curie=ISO42001.curie('linkage_to_risk_assessment'),
                   model_uri=ISO42001.linkage_to_risk_assessment, domain=None, range=Optional[str])

slots.technical_context = Slot(uri=ISO42001.technical_context, name="technical_context", curie=ISO42001.curie('technical_context'),
                   model_uri=ISO42001.technical_context, domain=None, range=Optional[str])

slots.societal_context = Slot(uri=ISO42001.societal_context, name="societal_context", curie=ISO42001.curie('societal_context'),
                   model_uri=ISO42001.societal_context, domain=None, range=Optional[str])

slots.applicable_jurisdictions = Slot(uri=ISO42001.applicable_jurisdictions, name="applicable_jurisdictions", curie=ISO42001.curie('applicable_jurisdictions'),
                   model_uri=ISO42001.applicable_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensions_assessed = Slot(uri=ISO42001.dimensions_assessed, name="dimensions_assessed", curie=ISO42001.curie('dimensions_assessed'),
                   model_uri=ISO42001.dimensions_assessed, domain=None, range=Optional[Union[Union[str, "ImpactAssessmentDimension"], list[Union[str, "ImpactAssessmentDimension"]]]])

slots.identified_consequences = Slot(uri=ISO42001.identified_consequences, name="identified_consequences", curie=ISO42001.curie('identified_consequences'),
                   model_uri=ISO42001.identified_consequences, domain=None, range=Optional[Union[str, list[str]]])

slots.mitigations = Slot(uri=ISO42001.mitigations, name="mitigations", curie=ISO42001.curie('mitigations'),
                   model_uri=ISO42001.mitigations, domain=None, range=Optional[Union[str, list[str]]])

slots.shared_with_parties = Slot(uri=ISO42001.shared_with_parties, name="shared_with_parties", curie=ISO42001.curie('shared_with_parties'),
                   model_uri=ISO42001.shared_with_parties, domain=None, range=Optional[Union[str, list[str]]])

slots.statement_of_applicability = Slot(uri=ISO42001.statement_of_applicability, name="statement_of_applicability", curie=ISO42001.curie('statement_of_applicability'),
                   model_uri=ISO42001.statement_of_applicability, domain=None, range=Optional[Union[str, StatementOfApplicabilityId]])

slots.soa_entries = Slot(uri=ISO42001.soa_entries, name="soa_entries", curie=ISO42001.curie('soa_entries'),
                   model_uri=ISO42001.soa_entries, domain=None, range=Optional[Union[Union[dict, SoAEntry], list[Union[dict, SoAEntry]]]])

slots.total_controls = Slot(uri=ISO42001.total_controls, name="total_controls", curie=ISO42001.curie('total_controls'),
                   model_uri=ISO42001.total_controls, domain=None, range=Optional[int])

slots.implemented_count = Slot(uri=ISO42001.implemented_count, name="implemented_count", curie=ISO42001.curie('implemented_count'),
                   model_uri=ISO42001.implemented_count, domain=None, range=Optional[int])

slots.planned_count = Slot(uri=ISO42001.planned_count, name="planned_count", curie=ISO42001.curie('planned_count'),
                   model_uri=ISO42001.planned_count, domain=None, range=Optional[int])

slots.not_applicable_count = Slot(uri=ISO42001.not_applicable_count, name="not_applicable_count", curie=ISO42001.curie('not_applicable_count'),
                   model_uri=ISO42001.not_applicable_count, domain=None, range=Optional[int])

slots.last_review_date = Slot(uri=ISO42001.last_review_date, name="last_review_date", curie=ISO42001.curie('last_review_date'),
                   model_uri=ISO42001.last_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.control_reference = Slot(uri=ISO42001.control_reference, name="control_reference", curie=ISO42001.curie('control_reference'),
                   model_uri=ISO42001.control_reference, domain=None, range=Optional[Union[str, AIReferenceControlId]])

slots.is_applicable = Slot(uri=ISO42001.is_applicable, name="is_applicable", curie=ISO42001.curie('is_applicable'),
                   model_uri=ISO42001.is_applicable, domain=None, range=Optional[Union[bool, Bool]])

slots.inclusion_justification = Slot(uri=ISO42001.inclusion_justification, name="inclusion_justification", curie=ISO42001.curie('inclusion_justification'),
                   model_uri=ISO42001.inclusion_justification, domain=None, range=Optional[str])

slots.exclusion_justification = Slot(uri=ISO42001.exclusion_justification, name="exclusion_justification", curie=ISO42001.curie('exclusion_justification'),
                   model_uri=ISO42001.exclusion_justification, domain=None, range=Optional[str])

slots.implementation_evidence = Slot(uri=ISO42001.implementation_evidence, name="implementation_evidence", curie=ISO42001.curie('implementation_evidence'),
                   model_uri=ISO42001.implementation_evidence, domain=None, range=Optional[str])

slots.target_implementation_date = Slot(uri=ISO42001.target_implementation_date, name="target_implementation_date", curie=ISO42001.curie('target_implementation_date'),
                   model_uri=ISO42001.target_implementation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.reference_controls = Slot(uri=ISO42001.reference_controls, name="reference_controls", curie=ISO42001.curie('reference_controls'),
                   model_uri=ISO42001.reference_controls, domain=None, range=Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]])

slots.control_id = Slot(uri=ISO42001.control_id, name="control_id", curie=ISO42001.curie('control_id'),
                   model_uri=ISO42001.control_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^A\.[0-9]{1,2}(\.[0-9]{1,2})*$'))

slots.control_title = Slot(uri=ISO42001.control_title, name="control_title", curie=ISO42001.curie('control_title'),
                   model_uri=ISO42001.control_title, domain=None, range=Optional[str])

slots.control_family = Slot(uri=ISO42001.control_family, name="control_family", curie=ISO42001.curie('control_family'),
                   model_uri=ISO42001.control_family, domain=None, range=Optional[Union[str, "AIControlFamily"]])

slots.control_text = Slot(uri=ISO42001.control_text, name="control_text", curie=ISO42001.curie('control_text'),
                   model_uri=ISO42001.control_text, domain=None, range=Optional[str])

slots.implementation_guidance = Slot(uri=ISO42001.implementation_guidance, name="implementation_guidance", curie=ISO42001.curie('implementation_guidance'),
                   model_uri=ISO42001.implementation_guidance, domain=None, range=Optional[str])

slots.related_controls = Slot(uri=ISO42001.related_controls, name="related_controls", curie=ISO42001.curie('related_controls'),
                   model_uri=ISO42001.related_controls, domain=None, range=Optional[Union[Union[str, AIReferenceControlId], list[Union[str, AIReferenceControlId]]]])

slots.applicable_risk_sources = Slot(uri=ISO42001.applicable_risk_sources, name="applicable_risk_sources", curie=ISO42001.curie('applicable_risk_sources'),
                   model_uri=ISO42001.applicable_risk_sources, domain=None, range=Optional[Union[Union[str, "AIRiskSourceCategory"], list[Union[str, "AIRiskSourceCategory"]]]])

slots.applicable_objectives = Slot(uri=ISO42001.applicable_objectives, name="applicable_objectives", curie=ISO42001.curie('applicable_objectives'),
                   model_uri=ISO42001.applicable_objectives, domain=None, range=Optional[Union[Union[str, "AIObjectiveCategory"], list[Union[str, "AIObjectiveCategory"]]]])

slots.control_owner = Slot(uri=ISO42001.control_owner, name="control_owner", curie=ISO42001.curie('control_owner'),
                   model_uri=ISO42001.control_owner, domain=None, range=Optional[str])

slots.implementation_date = Slot(uri=ISO42001.implementation_date, name="implementation_date", curie=ISO42001.curie('implementation_date'),
                   model_uri=ISO42001.implementation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effectiveness_rating = Slot(uri=ISO42001.effectiveness_rating, name="effectiveness_rating", curie=ISO42001.curie('effectiveness_rating'),
                   model_uri=ISO42001.effectiveness_rating, domain=None, range=Optional[str])

slots.last_test_date = Slot(uri=ISO42001.last_test_date, name="last_test_date", curie=ISO42001.curie('last_test_date'),
                   model_uri=ISO42001.last_test_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.evidence_references = Slot(uri=ISO42001.evidence_references, name="evidence_references", curie=ISO42001.curie('evidence_references'),
                   model_uri=ISO42001.evidence_references, domain=None, range=Optional[Union[str, list[str]]])

slots.ai_systems = Slot(uri=ISO42001.ai_systems, name="ai_systems", curie=ISO42001.curie('ai_systems'),
                   model_uri=ISO42001.ai_systems, domain=None, range=Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]])

slots.ai_system_purpose = Slot(uri=ISO42001.ai_system_purpose, name="ai_system_purpose", curie=ISO42001.curie('ai_system_purpose'),
                   model_uri=ISO42001.ai_system_purpose, domain=None, range=Optional[str])

slots.intended_uses = Slot(uri=ISO42001.intended_uses, name="intended_uses", curie=ISO42001.curie('intended_uses'),
                   model_uri=ISO42001.intended_uses, domain=None, range=Optional[Union[str, list[str]]])

slots.foreseeable_misuse = Slot(uri=ISO42001.foreseeable_misuse, name="foreseeable_misuse", curie=ISO42001.curie('foreseeable_misuse'),
                   model_uri=ISO42001.foreseeable_misuse, domain=None, range=Optional[Union[str, list[str]]])

slots.application_domain = Slot(uri=ISO42001.application_domain, name="application_domain", curie=ISO42001.curie('application_domain'),
                   model_uri=ISO42001.application_domain, domain=None, range=Optional[str])

slots.deployment_context = Slot(uri=ISO42001.deployment_context, name="deployment_context", curie=ISO42001.curie('deployment_context'),
                   model_uri=ISO42001.deployment_context, domain=None, range=Optional[str])

slots.lifecycle_stage = Slot(uri=ISO42001.lifecycle_stage, name="lifecycle_stage", curie=ISO42001.curie('lifecycle_stage'),
                   model_uri=ISO42001.lifecycle_stage, domain=None, range=Optional[Union[str, "AISystemLifecycleStage"]])

slots.organization_role = Slot(uri=ISO42001.organization_role, name="organization_role", curie=ISO42001.curie('organization_role'),
                   model_uri=ISO42001.organization_role, domain=None, range=Optional[Union[str, "AIOrganizationalRole"]])

slots.autonomy_level = Slot(uri=ISO42001.autonomy_level, name="autonomy_level", curie=ISO42001.curie('autonomy_level'),
                   model_uri=ISO42001.autonomy_level, domain=None, range=Optional[str])

slots.learning_mode = Slot(uri=ISO42001.learning_mode, name="learning_mode", curie=ISO42001.curie('learning_mode'),
                   model_uri=ISO42001.learning_mode, domain=None, range=Optional[Union[str, "LearningParadigm"]])

slots.data_resources = Slot(uri=ISO42001.data_resources, name="data_resources", curie=ISO42001.curie('data_resources'),
                   model_uri=ISO42001.data_resources, domain=None, range=Optional[Union[Union[str, DataResourceId], list[Union[str, DataResourceId]]]])

slots.tooling_resources = Slot(uri=ISO42001.tooling_resources, name="tooling_resources", curie=ISO42001.curie('tooling_resources'),
                   model_uri=ISO42001.tooling_resources, domain=None, range=Optional[Union[Union[str, ToolingResourceId], list[Union[str, ToolingResourceId]]]])

slots.computing_resources = Slot(uri=ISO42001.computing_resources, name="computing_resources", curie=ISO42001.curie('computing_resources'),
                   model_uri=ISO42001.computing_resources, domain=None, range=Optional[Union[Union[str, ComputingResourceId], list[Union[str, ComputingResourceId]]]])

slots.human_resources = Slot(uri=ISO42001.human_resources, name="human_resources", curie=ISO42001.curie('human_resources'),
                   model_uri=ISO42001.human_resources, domain=None, range=Optional[Union[Union[str, HumanResourceId], list[Union[str, HumanResourceId]]]])

slots.technical_documentation = Slot(uri=ISO42001.technical_documentation, name="technical_documentation", curie=ISO42001.curie('technical_documentation'),
                   model_uri=ISO42001.technical_documentation, domain=None, range=Optional[Union[str, list[str]]])

slots.event_log_policy = Slot(uri=ISO42001.event_log_policy, name="event_log_policy", curie=ISO42001.curie('event_log_policy'),
                   model_uri=ISO42001.event_log_policy, domain=None, range=Optional[str])

slots.related_impact_assessments = Slot(uri=ISO42001.related_impact_assessments, name="related_impact_assessments", curie=ISO42001.curie('related_impact_assessments'),
                   model_uri=ISO42001.related_impact_assessments, domain=None, range=Optional[Union[Union[str, AISystemImpactAssessmentId], list[Union[str, AISystemImpactAssessmentId]]]])

slots.supplier_relationships = Slot(uri=ISO42001.supplier_relationships, name="supplier_relationships", curie=ISO42001.curie('supplier_relationships'),
                   model_uri=ISO42001.supplier_relationships, domain=None, range=Optional[Union[Union[str, SupplierRelationshipId], list[Union[str, SupplierRelationshipId]]]])

slots.customer_relationships = Slot(uri=ISO42001.customer_relationships, name="customer_relationships", curie=ISO42001.curie('customer_relationships'),
                   model_uri=ISO42001.customer_relationships, domain=None, range=Optional[Union[Union[str, CustomerRelationshipId], list[Union[str, CustomerRelationshipId]]]])

slots.data_resource_category = Slot(uri=ISO42001.data_resource_category, name="data_resource_category", curie=ISO42001.curie('data_resource_category'),
                   model_uri=ISO42001.data_resource_category, domain=None, range=Optional[Union[str, "DataResourceCategory"]])

slots.source = Slot(uri=ISO42001.source, name="source", curie=ISO42001.curie('source'),
                   model_uri=ISO42001.source, domain=None, range=Optional[str])

slots.acquisition_method = Slot(uri=ISO42001.acquisition_method, name="acquisition_method", curie=ISO42001.curie('acquisition_method'),
                   model_uri=ISO42001.acquisition_method, domain=None, range=Optional[str])

slots.data_quality_requirements = Slot(uri=ISO42001.data_quality_requirements, name="data_quality_requirements", curie=ISO42001.curie('data_quality_requirements'),
                   model_uri=ISO42001.data_quality_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.data_quality_metrics = Slot(uri=ISO42001.data_quality_metrics, name="data_quality_metrics", curie=ISO42001.curie('data_quality_metrics'),
                   model_uri=ISO42001.data_quality_metrics, domain=None, range=Optional[Union[str, list[str]]])

slots.data_provenance = Slot(uri=ISO42001.data_provenance, name="data_provenance", curie=ISO42001.curie('data_provenance'),
                   model_uri=ISO42001.data_provenance, domain=None, range=Optional[str])

slots.labelling_process = Slot(uri=ISO42001.labelling_process, name="labelling_process", curie=ISO42001.curie('labelling_process'),
                   model_uri=ISO42001.labelling_process, domain=None, range=Optional[str])

slots.data_preparation_methods = Slot(uri=ISO42001.data_preparation_methods, name="data_preparation_methods", curie=ISO42001.curie('data_preparation_methods'),
                   model_uri=ISO42001.data_preparation_methods, domain=None, range=Optional[Union[Union[str, "DataPreparationMethod"], list[Union[str, "DataPreparationMethod"]]]])

slots.last_updated_date = Slot(uri=ISO42001.last_updated_date, name="last_updated_date", curie=ISO42001.curie('last_updated_date'),
                   model_uri=ISO42001.last_updated_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.known_bias_issues = Slot(uri=ISO42001.known_bias_issues, name="known_bias_issues", curie=ISO42001.curie('known_bias_issues'),
                   model_uri=ISO42001.known_bias_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.retention_policy = Slot(uri=ISO42001.retention_policy, name="retention_policy", curie=ISO42001.curie('retention_policy'),
                   model_uri=ISO42001.retention_policy, domain=None, range=Optional[str])

slots.data_classification = Slot(uri=ISO42001.data_classification, name="data_classification", curie=ISO42001.curie('data_classification'),
                   model_uri=ISO42001.data_classification, domain=None, range=Optional[str])

slots.tool_category = Slot(uri=ISO42001.tool_category, name="tool_category", curie=ISO42001.curie('tool_category'),
                   model_uri=ISO42001.tool_category, domain=None, range=Optional[str])

slots.tool_version = Slot(uri=ISO42001.tool_version, name="tool_version", curie=ISO42001.curie('tool_version'),
                   model_uri=ISO42001.tool_version, domain=None, range=Optional[str])

slots.vendor = Slot(uri=ISO42001.vendor, name="vendor", curie=ISO42001.curie('vendor'),
                   model_uri=ISO42001.vendor, domain=None, range=Optional[str])

slots.license_terms = Slot(uri=ISO42001.license_terms, name="license_terms", curie=ISO42001.curie('license_terms'),
                   model_uri=ISO42001.license_terms, domain=None, range=Optional[str])

slots.usage_purpose = Slot(uri=ISO42001.usage_purpose, name="usage_purpose", curie=ISO42001.curie('usage_purpose'),
                   model_uri=ISO42001.usage_purpose, domain=None, range=Optional[str])

slots.resource_class = Slot(uri=ISO42001.resource_class, name="resource_class", curie=ISO42001.curie('resource_class'),
                   model_uri=ISO42001.resource_class, domain=None, range=Optional[str])

slots.location = Slot(uri=ISO42001.location, name="location", curie=ISO42001.curie('location'),
                   model_uri=ISO42001.location, domain=None, range=Optional[str])

slots.environment_type = Slot(uri=ISO42001.environment_type, name="environment_type", curie=ISO42001.curie('environment_type'),
                   model_uri=ISO42001.environment_type, domain=None, range=Optional[str])

slots.lifecycle_responsibilities = Slot(uri=ISO42001.lifecycle_responsibilities, name="lifecycle_responsibilities", curie=ISO42001.curie('lifecycle_responsibilities'),
                   model_uri=ISO42001.lifecycle_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.resources = Slot(uri=ISO42001.resources, name="resources", curie=ISO42001.curie('resources'),
                   model_uri=ISO42001.resources, domain=None, range=Optional[Union[Union[str, ResourceId], list[Union[str, ResourceId]]]])

slots.resource_type = Slot(uri=ISO42001.resource_type, name="resource_type", curie=ISO42001.curie('resource_type'),
                   model_uri=ISO42001.resource_type, domain=None, range=Optional[str])

slots.quantity = Slot(uri=ISO42001.quantity, name="quantity", curie=ISO42001.curie('quantity'),
                   model_uri=ISO42001.quantity, domain=None, range=Optional[str])

slots.allocation_date = Slot(uri=ISO42001.allocation_date, name="allocation_date", curie=ISO42001.curie('allocation_date'),
                   model_uri=ISO42001.allocation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.allocated_to = Slot(uri=ISO42001.allocated_to, name="allocated_to", curie=ISO42001.curie('allocated_to'),
                   model_uri=ISO42001.allocated_to, domain=None, range=Optional[str])

slots.cost = Slot(uri=ISO42001.cost, name="cost", curie=ISO42001.curie('cost'),
                   model_uri=ISO42001.cost, domain=None, range=Optional[str])

slots.availability_status = Slot(uri=ISO42001.availability_status, name="availability_status", curie=ISO42001.curie('availability_status'),
                   model_uri=ISO42001.availability_status, domain=None, range=Optional[str])

slots.competence_records = Slot(uri=ISO42001.competence_records, name="competence_records", curie=ISO42001.curie('competence_records'),
                   model_uri=ISO42001.competence_records, domain=None, range=Optional[Union[Union[str, CompetenceRecordId], list[Union[str, CompetenceRecordId]]]])

slots.person_name = Slot(uri=ISO42001.person_name, name="person_name", curie=ISO42001.curie('person_name'),
                   model_uri=ISO42001.person_name, domain=None, range=Optional[str])

slots.person_role = Slot(uri=ISO42001.person_role, name="person_role", curie=ISO42001.curie('person_role'),
                   model_uri=ISO42001.person_role, domain=None, range=Optional[str])

slots.required_competencies = Slot(uri=ISO42001.required_competencies, name="required_competencies", curie=ISO42001.curie('required_competencies'),
                   model_uri=ISO42001.required_competencies, domain=None, range=Optional[Union[str, list[str]]])

slots.education_records = Slot(uri=ISO42001.education_records, name="education_records", curie=ISO42001.curie('education_records'),
                   model_uri=ISO42001.education_records, domain=None, range=Optional[Union[str, list[str]]])

slots.training_records = Slot(uri=ISO42001.training_records, name="training_records", curie=ISO42001.curie('training_records'),
                   model_uri=ISO42001.training_records, domain=None, range=Optional[Union[str, list[str]]])

slots.experience_records = Slot(uri=ISO42001.experience_records, name="experience_records", curie=ISO42001.curie('experience_records'),
                   model_uri=ISO42001.experience_records, domain=None, range=Optional[Union[str, list[str]]])

slots.competency_assessment_date = Slot(uri=ISO42001.competency_assessment_date, name="competency_assessment_date", curie=ISO42001.curie('competency_assessment_date'),
                   model_uri=ISO42001.competency_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.competency_gaps = Slot(uri=ISO42001.competency_gaps, name="competency_gaps", curie=ISO42001.curie('competency_gaps'),
                   model_uri=ISO42001.competency_gaps, domain=None, range=Optional[Union[str, list[str]]])

slots.development_actions = Slot(uri=ISO42001.development_actions, name="development_actions", curie=ISO42001.curie('development_actions'),
                   model_uri=ISO42001.development_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.awareness_program = Slot(uri=ISO42001.awareness_program, name="awareness_program", curie=ISO42001.curie('awareness_program'),
                   model_uri=ISO42001.awareness_program, domain=None, range=Optional[Union[str, AwarenessProgramId]])

slots.awareness_topics = Slot(uri=ISO42001.awareness_topics, name="awareness_topics", curie=ISO42001.curie('awareness_topics'),
                   model_uri=ISO42001.awareness_topics, domain=None, range=Optional[Union[str, list[str]]])

slots.delivery_methods = Slot(uri=ISO42001.delivery_methods, name="delivery_methods", curie=ISO42001.curie('delivery_methods'),
                   model_uri=ISO42001.delivery_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.frequency = Slot(uri=ISO42001.frequency, name="frequency", curie=ISO42001.curie('frequency'),
                   model_uri=ISO42001.frequency, domain=None, range=Optional[str])

slots.completion_tracking = Slot(uri=ISO42001.completion_tracking, name="completion_tracking", curie=ISO42001.curie('completion_tracking'),
                   model_uri=ISO42001.completion_tracking, domain=None, range=Optional[str])

slots.effectiveness_measures = Slot(uri=ISO42001.effectiveness_measures, name="effectiveness_measures", curie=ISO42001.curie('effectiveness_measures'),
                   model_uri=ISO42001.effectiveness_measures, domain=None, range=Optional[str])

slots.communication_plan = Slot(uri=ISO42001.communication_plan, name="communication_plan", curie=ISO42001.curie('communication_plan'),
                   model_uri=ISO42001.communication_plan, domain=None, range=Optional[Union[str, CommunicationPlanId]])

slots.communication_items = Slot(uri=ISO42001.communication_items, name="communication_items", curie=ISO42001.curie('communication_items'),
                   model_uri=ISO42001.communication_items, domain=None, range=Optional[Union[Union[dict, CommunicationItem], list[Union[dict, CommunicationItem]]]])

slots.subject = Slot(uri=ISO42001.subject, name="subject", curie=ISO42001.curie('subject'),
                   model_uri=ISO42001.subject, domain=None, range=Optional[str])

slots.purpose = Slot(uri=ISO42001.purpose, name="purpose", curie=ISO42001.curie('purpose'),
                   model_uri=ISO42001.purpose, domain=None, range=Optional[str])

slots.audience = Slot(uri=ISO42001.audience, name="audience", curie=ISO42001.curie('audience'),
                   model_uri=ISO42001.audience, domain=None, range=Optional[str])

slots.method = Slot(uri=ISO42001.method, name="method", curie=ISO42001.curie('method'),
                   model_uri=ISO42001.method, domain=None, range=Optional[str])

slots.responsible_party = Slot(uri=ISO42001.responsible_party, name="responsible_party", curie=ISO42001.curie('responsible_party'),
                   model_uri=ISO42001.responsible_party, domain=None, range=Optional[str])

slots.records_required = Slot(uri=ISO42001.records_required, name="records_required", curie=ISO42001.curie('records_required'),
                   model_uri=ISO42001.records_required, domain=None, range=Optional[str])

slots.documented_information_register = Slot(uri=ISO42001.documented_information_register, name="documented_information_register", curie=ISO42001.curie('documented_information_register'),
                   model_uri=ISO42001.documented_information_register, domain=None, range=Optional[Union[Union[str, DocumentedInformationId], list[Union[str, DocumentedInformationId]]]])

slots.operational_procedures = Slot(uri=ISO42001.operational_procedures, name="operational_procedures", curie=ISO42001.curie('operational_procedures'),
                   model_uri=ISO42001.operational_procedures, domain=None, range=Optional[Union[Union[str, OperationalProcedureId], list[Union[str, OperationalProcedureId]]]])

slots.procedure_scope = Slot(uri=ISO42001.procedure_scope, name="procedure_scope", curie=ISO42001.curie('procedure_scope'),
                   model_uri=ISO42001.procedure_scope, domain=None, range=Optional[str])

slots.process_criteria = Slot(uri=ISO42001.process_criteria, name="process_criteria", curie=ISO42001.curie('process_criteria'),
                   model_uri=ISO42001.process_criteria, domain=None, range=Optional[str])

slots.control_measures = Slot(uri=ISO42001.control_measures, name="control_measures", curie=ISO42001.curie('control_measures'),
                   model_uri=ISO42001.control_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.responsible_roles = Slot(uri=ISO42001.responsible_roles, name="responsible_roles", curie=ISO42001.curie('responsible_roles'),
                   model_uri=ISO42001.responsible_roles, domain=None, range=Optional[Union[Union[str, RoleId], list[Union[str, RoleId]]]])

slots.change_control_requirements = Slot(uri=ISO42001.change_control_requirements, name="change_control_requirements", curie=ISO42001.curie('change_control_requirements'),
                   model_uri=ISO42001.change_control_requirements, domain=None, range=Optional[str])

slots.monitoring_program = Slot(uri=ISO42001.monitoring_program, name="monitoring_program", curie=ISO42001.curie('monitoring_program'),
                   model_uri=ISO42001.monitoring_program, domain=None, range=Optional[Union[str, MonitoringProgramId]])

slots.monitoring_items = Slot(uri=ISO42001.monitoring_items, name="monitoring_items", curie=ISO42001.curie('monitoring_items'),
                   model_uri=ISO42001.monitoring_items, domain=None, range=Optional[Union[Union[dict, MonitoringItem], list[Union[dict, MonitoringItem]]]])

slots.metric_name = Slot(uri=ISO42001.metric_name, name="metric_name", curie=ISO42001.curie('metric_name'),
                   model_uri=ISO42001.metric_name, domain=None, range=Optional[str])

slots.metric_description = Slot(uri=ISO42001.metric_description, name="metric_description", curie=ISO42001.curie('metric_description'),
                   model_uri=ISO42001.metric_description, domain=None, range=Optional[str])

slots.analysis_frequency = Slot(uri=ISO42001.analysis_frequency, name="analysis_frequency", curie=ISO42001.curie('analysis_frequency'),
                   model_uri=ISO42001.analysis_frequency, domain=None, range=Optional[str])

slots.analyst = Slot(uri=ISO42001.analyst, name="analyst", curie=ISO42001.curie('analyst'),
                   model_uri=ISO42001.analyst, domain=None, range=Optional[str])

slots.target_threshold = Slot(uri=ISO42001.target_threshold, name="target_threshold", curie=ISO42001.curie('target_threshold'),
                   model_uri=ISO42001.target_threshold, domain=None, range=Optional[str])

slots.alert_threshold = Slot(uri=ISO42001.alert_threshold, name="alert_threshold", curie=ISO42001.curie('alert_threshold'),
                   model_uri=ISO42001.alert_threshold, domain=None, range=Optional[str])

slots.trend = Slot(uri=ISO42001.trend, name="trend", curie=ISO42001.curie('trend'),
                   model_uri=ISO42001.trend, domain=None, range=Optional[str])

slots.internal_audits = Slot(uri=ISO42001.internal_audits, name="internal_audits", curie=ISO42001.curie('internal_audits'),
                   model_uri=ISO42001.internal_audits, domain=None, range=Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]])

slots.audit_reference = Slot(uri=ISO42001.audit_reference, name="audit_reference", curie=ISO42001.curie('audit_reference'),
                   model_uri=ISO42001.audit_reference, domain=None, range=Optional[str])

slots.audit_type = Slot(uri=ISO42001.audit_type, name="audit_type", curie=ISO42001.curie('audit_type'),
                   model_uri=ISO42001.audit_type, domain=None, range=Optional[Union[str, "AuditType"]])

slots.audit_scope = Slot(uri=ISO42001.audit_scope, name="audit_scope", curie=ISO42001.curie('audit_scope'),
                   model_uri=ISO42001.audit_scope, domain=None, range=Optional[str])

slots.audit_criteria = Slot(uri=ISO42001.audit_criteria, name="audit_criteria", curie=ISO42001.curie('audit_criteria'),
                   model_uri=ISO42001.audit_criteria, domain=None, range=Optional[str])

slots.audit_objectives = Slot(uri=ISO42001.audit_objectives, name="audit_objectives", curie=ISO42001.curie('audit_objectives'),
                   model_uri=ISO42001.audit_objectives, domain=None, range=Optional[str])

slots.audit_period_start = Slot(uri=ISO42001.audit_period_start, name="audit_period_start", curie=ISO42001.curie('audit_period_start'),
                   model_uri=ISO42001.audit_period_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.audit_period_end = Slot(uri=ISO42001.audit_period_end, name="audit_period_end", curie=ISO42001.curie('audit_period_end'),
                   model_uri=ISO42001.audit_period_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.lead_auditor = Slot(uri=ISO42001.lead_auditor, name="lead_auditor", curie=ISO42001.curie('lead_auditor'),
                   model_uri=ISO42001.lead_auditor, domain=None, range=Optional[str])

slots.audit_team = Slot(uri=ISO42001.audit_team, name="audit_team", curie=ISO42001.curie('audit_team'),
                   model_uri=ISO42001.audit_team, domain=None, range=Optional[Union[str, list[str]]])

slots.auditee_representatives = Slot(uri=ISO42001.auditee_representatives, name="auditee_representatives", curie=ISO42001.curie('auditee_representatives'),
                   model_uri=ISO42001.auditee_representatives, domain=None, range=Optional[Union[str, list[str]]])

slots.audit_plan = Slot(uri=ISO42001.audit_plan, name="audit_plan", curie=ISO42001.curie('audit_plan'),
                   model_uri=ISO42001.audit_plan, domain=None, range=Optional[str])

slots.findings = Slot(uri=ISO42001.findings, name="findings", curie=ISO42001.curie('findings'),
                   model_uri=ISO42001.findings, domain=None, range=Optional[Union[Union[str, AuditFindingId], list[Union[str, AuditFindingId]]]])

slots.positive_observations = Slot(uri=ISO42001.positive_observations, name="positive_observations", curie=ISO42001.curie('positive_observations'),
                   model_uri=ISO42001.positive_observations, domain=None, range=Optional[Union[str, list[str]]])

slots.audit_conclusion = Slot(uri=ISO42001.audit_conclusion, name="audit_conclusion", curie=ISO42001.curie('audit_conclusion'),
                   model_uri=ISO42001.audit_conclusion, domain=None, range=Optional[str])

slots.report_date = Slot(uri=ISO42001.report_date, name="report_date", curie=ISO42001.curie('report_date'),
                   model_uri=ISO42001.report_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.report_distribution = Slot(uri=ISO42001.report_distribution, name="report_distribution", curie=ISO42001.curie('report_distribution'),
                   model_uri=ISO42001.report_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.programme_period = Slot(uri=ISO42001.programme_period, name="programme_period", curie=ISO42001.curie('programme_period'),
                   model_uri=ISO42001.programme_period, domain=None, range=Optional[str])

slots.planned_audits = Slot(uri=ISO42001.planned_audits, name="planned_audits", curie=ISO42001.curie('planned_audits'),
                   model_uri=ISO42001.planned_audits, domain=None, range=Optional[Union[Union[str, InternalAuditId], list[Union[str, InternalAuditId]]]])

slots.audit_frequency_rationale = Slot(uri=ISO42001.audit_frequency_rationale, name="audit_frequency_rationale", curie=ISO42001.curie('audit_frequency_rationale'),
                   model_uri=ISO42001.audit_frequency_rationale, domain=None, range=Optional[str])

slots.resource_requirements = Slot(uri=ISO42001.resource_requirements, name="resource_requirements", curie=ISO42001.curie('resource_requirements'),
                   model_uri=ISO42001.resource_requirements, domain=None, range=Optional[str])

slots.auditor_qualifications = Slot(uri=ISO42001.auditor_qualifications, name="auditor_qualifications", curie=ISO42001.curie('auditor_qualifications'),
                   model_uri=ISO42001.auditor_qualifications, domain=None, range=Optional[str])

slots.programme_status = Slot(uri=ISO42001.programme_status, name="programme_status", curie=ISO42001.curie('programme_status'),
                   model_uri=ISO42001.programme_status, domain=None, range=Optional[str])

slots.finding_type = Slot(uri=ISO42001.finding_type, name="finding_type", curie=ISO42001.curie('finding_type'),
                   model_uri=ISO42001.finding_type, domain=None, range=Optional[Union[str, "AuditFindingType"]])

slots.clause_reference = Slot(uri=ISO42001.clause_reference, name="clause_reference", curie=ISO42001.curie('clause_reference'),
                   model_uri=ISO42001.clause_reference, domain=None, range=Optional[str])

slots.finding_description = Slot(uri=ISO42001.finding_description, name="finding_description", curie=ISO42001.curie('finding_description'),
                   model_uri=ISO42001.finding_description, domain=None, range=Optional[str])

slots.objective_evidence = Slot(uri=ISO42001.objective_evidence, name="objective_evidence", curie=ISO42001.curie('objective_evidence'),
                   model_uri=ISO42001.objective_evidence, domain=None, range=Optional[str])

slots.root_cause_analysis = Slot(uri=ISO42001.root_cause_analysis, name="root_cause_analysis", curie=ISO42001.curie('root_cause_analysis'),
                   model_uri=ISO42001.root_cause_analysis, domain=None, range=Optional[str])

slots.risk_implication = Slot(uri=ISO42001.risk_implication, name="risk_implication", curie=ISO42001.curie('risk_implication'),
                   model_uri=ISO42001.risk_implication, domain=None, range=Optional[str])

slots.recommended_action = Slot(uri=ISO42001.recommended_action, name="recommended_action", curie=ISO42001.curie('recommended_action'),
                   model_uri=ISO42001.recommended_action, domain=None, range=Optional[str])

slots.auditee_response = Slot(uri=ISO42001.auditee_response, name="auditee_response", curie=ISO42001.curie('auditee_response'),
                   model_uri=ISO42001.auditee_response, domain=None, range=Optional[str])

slots.linked_corrective_action = Slot(uri=ISO42001.linked_corrective_action, name="linked_corrective_action", curie=ISO42001.curie('linked_corrective_action'),
                   model_uri=ISO42001.linked_corrective_action, domain=None, range=Optional[Union[str, CorrectiveActionId]])

slots.closure_status = Slot(uri=ISO42001.closure_status, name="closure_status", curie=ISO42001.curie('closure_status'),
                   model_uri=ISO42001.closure_status, domain=None, range=Optional[str])

slots.closure_date = Slot(uri=ISO42001.closure_date, name="closure_date", curie=ISO42001.curie('closure_date'),
                   model_uri=ISO42001.closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.management_reviews = Slot(uri=ISO42001.management_reviews, name="management_reviews", curie=ISO42001.curie('management_reviews'),
                   model_uri=ISO42001.management_reviews, domain=None, range=Optional[Union[Union[str, ManagementReviewId], list[Union[str, ManagementReviewId]]]])

slots.attendees = Slot(uri=ISO42001.attendees, name="attendees", curie=ISO42001.curie('attendees'),
                   model_uri=ISO42001.attendees, domain=None, range=Optional[Union[str, list[str]]])

slots.previous_actions_status = Slot(uri=ISO42001.previous_actions_status, name="previous_actions_status", curie=ISO42001.curie('previous_actions_status'),
                   model_uri=ISO42001.previous_actions_status, domain=None, range=Optional[str])

slots.context_changes = Slot(uri=ISO42001.context_changes, name="context_changes", curie=ISO42001.curie('context_changes'),
                   model_uri=ISO42001.context_changes, domain=None, range=Optional[Union[str, list[str]]])

slots.interested_party_changes = Slot(uri=ISO42001.interested_party_changes, name="interested_party_changes", curie=ISO42001.curie('interested_party_changes'),
                   model_uri=ISO42001.interested_party_changes, domain=None, range=Optional[Union[str, list[str]]])

slots.performance_trends = Slot(uri=ISO42001.performance_trends, name="performance_trends", curie=ISO42001.curie('performance_trends'),
                   model_uri=ISO42001.performance_trends, domain=None, range=Optional[str])

slots.audit_results_summary = Slot(uri=ISO42001.audit_results_summary, name="audit_results_summary", curie=ISO42001.curie('audit_results_summary'),
                   model_uri=ISO42001.audit_results_summary, domain=None, range=Optional[str])

slots.risk_assessment_results = Slot(uri=ISO42001.risk_assessment_results, name="risk_assessment_results", curie=ISO42001.curie('risk_assessment_results'),
                   model_uri=ISO42001.risk_assessment_results, domain=None, range=Optional[str])

slots.impact_assessment_results = Slot(uri=ISO42001.impact_assessment_results, name="impact_assessment_results", curie=ISO42001.curie('impact_assessment_results'),
                   model_uri=ISO42001.impact_assessment_results, domain=None, range=Optional[str])

slots.improvement_opportunities = Slot(uri=ISO42001.improvement_opportunities, name="improvement_opportunities", curie=ISO42001.curie('improvement_opportunities'),
                   model_uri=ISO42001.improvement_opportunities, domain=None, range=Optional[Union[Union[str, ImprovementOpportunityId], list[Union[str, ImprovementOpportunityId]]]])

slots.decisions = Slot(uri=ISO42001.decisions, name="decisions", curie=ISO42001.curie('decisions'),
                   model_uri=ISO42001.decisions, domain=None, range=Optional[Union[str, list[str]]])

slots.action_items = Slot(uri=ISO42001.action_items, name="action_items", curie=ISO42001.curie('action_items'),
                   model_uri=ISO42001.action_items, domain=None, range=Optional[Union[str, list[str]]])

slots.next_review_date = Slot(uri=ISO42001.next_review_date, name="next_review_date", curie=ISO42001.curie('next_review_date'),
                   model_uri=ISO42001.next_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.nonconformities = Slot(uri=ISO42001.nonconformities, name="nonconformities", curie=ISO42001.curie('nonconformities'),
                   model_uri=ISO42001.nonconformities, domain=None, range=Optional[Union[Union[str, NonconformityId], list[Union[str, NonconformityId]]]])

slots.nonconformity_source = Slot(uri=ISO42001.nonconformity_source, name="nonconformity_source", curie=ISO42001.curie('nonconformity_source'),
                   model_uri=ISO42001.nonconformity_source, domain=None, range=Optional[str])

slots.detection_date = Slot(uri=ISO42001.detection_date, name="detection_date", curie=ISO42001.curie('detection_date'),
                   model_uri=ISO42001.detection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.detected_by = Slot(uri=ISO42001.detected_by, name="detected_by", curie=ISO42001.curie('detected_by'),
                   model_uri=ISO42001.detected_by, domain=None, range=Optional[str])

slots.requirement_violated = Slot(uri=ISO42001.requirement_violated, name="requirement_violated", curie=ISO42001.curie('requirement_violated'),
                   model_uri=ISO42001.requirement_violated, domain=None, range=Optional[str])

slots.nonconformity_description = Slot(uri=ISO42001.nonconformity_description, name="nonconformity_description", curie=ISO42001.curie('nonconformity_description'),
                   model_uri=ISO42001.nonconformity_description, domain=None, range=Optional[str])

slots.immediate_actions = Slot(uri=ISO42001.immediate_actions, name="immediate_actions", curie=ISO42001.curie('immediate_actions'),
                   model_uri=ISO42001.immediate_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.consequences_addressed = Slot(uri=ISO42001.consequences_addressed, name="consequences_addressed", curie=ISO42001.curie('consequences_addressed'),
                   model_uri=ISO42001.consequences_addressed, domain=None, range=Optional[str])

slots.root_cause = Slot(uri=ISO42001.root_cause, name="root_cause", curie=ISO42001.curie('root_cause'),
                   model_uri=ISO42001.root_cause, domain=None, range=Optional[str])

slots.similar_nonconformities_check = Slot(uri=ISO42001.similar_nonconformities_check, name="similar_nonconformities_check", curie=ISO42001.curie('similar_nonconformities_check'),
                   model_uri=ISO42001.similar_nonconformities_check, domain=None, range=Optional[str])

slots.linked_corrective_actions = Slot(uri=ISO42001.linked_corrective_actions, name="linked_corrective_actions", curie=ISO42001.curie('linked_corrective_actions'),
                   model_uri=ISO42001.linked_corrective_actions, domain=None, range=Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]])

slots.closure_evidence = Slot(uri=ISO42001.closure_evidence, name="closure_evidence", curie=ISO42001.curie('closure_evidence'),
                   model_uri=ISO42001.closure_evidence, domain=None, range=Optional[str])

slots.corrective_actions = Slot(uri=ISO42001.corrective_actions, name="corrective_actions", curie=ISO42001.curie('corrective_actions'),
                   model_uri=ISO42001.corrective_actions, domain=None, range=Optional[Union[Union[str, CorrectiveActionId], list[Union[str, CorrectiveActionId]]]])

slots.linked_nonconformity = Slot(uri=ISO42001.linked_nonconformity, name="linked_nonconformity", curie=ISO42001.curie('linked_nonconformity'),
                   model_uri=ISO42001.linked_nonconformity, domain=None, range=Optional[Union[str, NonconformityId]])

slots.action_description = Slot(uri=ISO42001.action_description, name="action_description", curie=ISO42001.curie('action_description'),
                   model_uri=ISO42001.action_description, domain=None, range=Optional[str])

slots.root_cause_addressed = Slot(uri=ISO42001.root_cause_addressed, name="root_cause_addressed", curie=ISO42001.curie('root_cause_addressed'),
                   model_uri=ISO42001.root_cause_addressed, domain=None, range=Optional[str])

slots.target_completion_date = Slot(uri=ISO42001.target_completion_date, name="target_completion_date", curie=ISO42001.curie('target_completion_date'),
                   model_uri=ISO42001.target_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.actual_completion_date = Slot(uri=ISO42001.actual_completion_date, name="actual_completion_date", curie=ISO42001.curie('actual_completion_date'),
                   model_uri=ISO42001.actual_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effectiveness_criteria = Slot(uri=ISO42001.effectiveness_criteria, name="effectiveness_criteria", curie=ISO42001.curie('effectiveness_criteria'),
                   model_uri=ISO42001.effectiveness_criteria, domain=None, range=Optional[str])

slots.effectiveness_review_date = Slot(uri=ISO42001.effectiveness_review_date, name="effectiveness_review_date", curie=ISO42001.curie('effectiveness_review_date'),
                   model_uri=ISO42001.effectiveness_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.effectiveness_verified = Slot(uri=ISO42001.effectiveness_verified, name="effectiveness_verified", curie=ISO42001.curie('effectiveness_verified'),
                   model_uri=ISO42001.effectiveness_verified, domain=None, range=Optional[Union[bool, Bool]])

slots.aims_changes_required = Slot(uri=ISO42001.aims_changes_required, name="aims_changes_required", curie=ISO42001.curie('aims_changes_required'),
                   model_uri=ISO42001.aims_changes_required, domain=None, range=Optional[Union[bool, Bool]])

slots.improvements = Slot(uri=ISO42001.improvements, name="improvements", curie=ISO42001.curie('improvements'),
                   model_uri=ISO42001.improvements, domain=None, range=Optional[Union[Union[str, ImprovementOpportunityId], list[Union[str, ImprovementOpportunityId]]]])

slots.improvement_source = Slot(uri=ISO42001.improvement_source, name="improvement_source", curie=ISO42001.curie('improvement_source'),
                   model_uri=ISO42001.improvement_source, domain=None, range=Optional[str])

slots.identification_date = Slot(uri=ISO42001.identification_date, name="identification_date", curie=ISO42001.curie('identification_date'),
                   model_uri=ISO42001.identification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.identified_by = Slot(uri=ISO42001.identified_by, name="identified_by", curie=ISO42001.curie('identified_by'),
                   model_uri=ISO42001.identified_by, domain=None, range=Optional[str])

slots.improvement_description = Slot(uri=ISO42001.improvement_description, name="improvement_description", curie=ISO42001.curie('improvement_description'),
                   model_uri=ISO42001.improvement_description, domain=None, range=Optional[str])

slots.expected_benefit = Slot(uri=ISO42001.expected_benefit, name="expected_benefit", curie=ISO42001.curie('expected_benefit'),
                   model_uri=ISO42001.expected_benefit, domain=None, range=Optional[str])

slots.priority = Slot(uri=ISO42001.priority, name="priority", curie=ISO42001.curie('priority'),
                   model_uri=ISO42001.priority, domain=None, range=Optional[Union[str, "RiskLevel"]])

slots.implementation_plan = Slot(uri=ISO42001.implementation_plan, name="implementation_plan", curie=ISO42001.curie('implementation_plan'),
                   model_uri=ISO42001.implementation_plan, domain=None, range=Optional[str])

slots.outcome_assessment = Slot(uri=ISO42001.outcome_assessment, name="outcome_assessment", curie=ISO42001.curie('outcome_assessment'),
                   model_uri=ISO42001.outcome_assessment, domain=None, range=Optional[str])

slots.third_party_relationships = Slot(uri=ISO42001.third_party_relationships, name="third_party_relationships", curie=ISO42001.curie('third_party_relationships'),
                   model_uri=ISO42001.third_party_relationships, domain=None, range=Optional[Union[Union[str, ThirdPartyRelationshipId], list[Union[str, ThirdPartyRelationshipId]]]])

slots.party_name = Slot(uri=ISO42001.party_name, name="party_name", curie=ISO42001.curie('party_name'),
                   model_uri=ISO42001.party_name, domain=None, range=Optional[str])

slots.contractual_basis = Slot(uri=ISO42001.contractual_basis, name="contractual_basis", curie=ISO42001.curie('contractual_basis'),
                   model_uri=ISO42001.contractual_basis, domain=None, range=Optional[str])

slots.allocated_responsibilities = Slot(uri=ISO42001.allocated_responsibilities, name="allocated_responsibilities", curie=ISO42001.curie('allocated_responsibilities'),
                   model_uri=ISO42001.allocated_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.data_processing_role = Slot(uri=ISO42001.data_processing_role, name="data_processing_role", curie=ISO42001.curie('data_processing_role'),
                   model_uri=ISO42001.data_processing_role, domain=None, range=Optional[str])

slots.ai_systems_involved = Slot(uri=ISO42001.ai_systems_involved, name="ai_systems_involved", curie=ISO42001.curie('ai_systems_involved'),
                   model_uri=ISO42001.ai_systems_involved, domain=None, range=Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]])

slots.lifecycle_stages_involved = Slot(uri=ISO42001.lifecycle_stages_involved, name="lifecycle_stages_involved", curie=ISO42001.curie('lifecycle_stages_involved'),
                   model_uri=ISO42001.lifecycle_stages_involved, domain=None, range=Optional[Union[Union[str, "AISystemLifecycleStage"], list[Union[str, "AISystemLifecycleStage"]]]])

slots.assurance_evidence = Slot(uri=ISO42001.assurance_evidence, name="assurance_evidence", curie=ISO42001.curie('assurance_evidence'),
                   model_uri=ISO42001.assurance_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.review_frequency = Slot(uri=ISO42001.review_frequency, name="review_frequency", curie=ISO42001.curie('review_frequency'),
                   model_uri=ISO42001.review_frequency, domain=None, range=Optional[str])

slots.supplier_assessment_criteria = Slot(uri=ISO42001.supplier_assessment_criteria, name="supplier_assessment_criteria", curie=ISO42001.curie('supplier_assessment_criteria'),
                   model_uri=ISO42001.supplier_assessment_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.monitoring_method = Slot(uri=ISO42001.monitoring_method, name="monitoring_method", curie=ISO42001.curie('monitoring_method'),
                   model_uri=ISO42001.monitoring_method, domain=None, range=Optional[str])

slots.corrective_actions_required = Slot(uri=ISO42001.corrective_actions_required, name="corrective_actions_required", curie=ISO42001.curie('corrective_actions_required'),
                   model_uri=ISO42001.corrective_actions_required, domain=None, range=Optional[Union[str, list[str]]])

slots.customer_expectations = Slot(uri=ISO42001.customer_expectations, name="customer_expectations", curie=ISO42001.curie('customer_expectations'),
                   model_uri=ISO42001.customer_expectations, domain=None, range=Optional[Union[str, list[str]]])

slots.usage_agreement_reference = Slot(uri=ISO42001.usage_agreement_reference, name="usage_agreement_reference", curie=ISO42001.curie('usage_agreement_reference'),
                   model_uri=ISO42001.usage_agreement_reference, domain=None, range=Optional[str])

slots.communicated_limitations = Slot(uri=ISO42001.communicated_limitations, name="communicated_limitations", curie=ISO42001.curie('communicated_limitations'),
                   model_uri=ISO42001.communicated_limitations, domain=None, range=Optional[Union[str, list[str]]])

slots.certification_status = Slot(uri=ISO42001.certification_status, name="certification_status", curie=ISO42001.curie('certification_status'),
                   model_uri=ISO42001.certification_status, domain=None, range=Optional[str])

slots.certification_body = Slot(uri=ISO42001.certification_body, name="certification_body", curie=ISO42001.curie('certification_body'),
                   model_uri=ISO42001.certification_body, domain=None, range=Optional[str])

slots.certification_date = Slot(uri=ISO42001.certification_date, name="certification_date", curie=ISO42001.curie('certification_date'),
                   model_uri=ISO42001.certification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.recertification_date = Slot(uri=ISO42001.recertification_date, name="recertification_date", curie=ISO42001.curie('recertification_date'),
                   model_uri=ISO42001.recertification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.ai_system_events = Slot(uri=ISO42001.ai_system_events, name="ai_system_events", curie=ISO42001.curie('ai_system_events'),
                   model_uri=ISO42001.ai_system_events, domain=None, range=Optional[Union[Union[str, AISystemEventId], list[Union[str, AISystemEventId]]]])

slots.ai_incidents = Slot(uri=ISO42001.ai_incidents, name="ai_incidents", curie=ISO42001.curie('ai_incidents'),
                   model_uri=ISO42001.ai_incidents, domain=None, range=Optional[Union[Union[str, AIIncidentId], list[Union[str, AIIncidentId]]]])

slots.event_datetime = Slot(uri=ISO42001.event_datetime, name="event_datetime", curie=ISO42001.curie('event_datetime'),
                   model_uri=ISO42001.event_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.reporter = Slot(uri=ISO42001.reporter, name="reporter", curie=ISO42001.curie('reporter'),
                   model_uri=ISO42001.reporter, domain=None, range=Optional[str])

slots.reporter_party_type = Slot(uri=ISO42001.reporter_party_type, name="reporter_party_type", curie=ISO42001.curie('reporter_party_type'),
                   model_uri=ISO42001.reporter_party_type, domain=None, range=Optional[str])

slots.event_source = Slot(uri=ISO42001.event_source, name="event_source", curie=ISO42001.curie('event_source'),
                   model_uri=ISO42001.event_source, domain=None, range=Optional[str])

slots.event_description = Slot(uri=ISO42001.event_description, name="event_description", curie=ISO42001.curie('event_description'),
                   model_uri=ISO42001.event_description, domain=None, range=Optional[str])

slots.initial_assessment = Slot(uri=ISO42001.initial_assessment, name="initial_assessment", curie=ISO42001.curie('initial_assessment'),
                   model_uri=ISO42001.initial_assessment, domain=None, range=Optional[str])

slots.categorized_as_incident = Slot(uri=ISO42001.categorized_as_incident, name="categorized_as_incident", curie=ISO42001.curie('categorized_as_incident'),
                   model_uri=ISO42001.categorized_as_incident, domain=None, range=Optional[Union[bool, Bool]])

slots.linked_incident = Slot(uri=ISO42001.linked_incident, name="linked_incident", curie=ISO42001.curie('linked_incident'),
                   model_uri=ISO42001.linked_incident, domain=None, range=Optional[Union[str, AIIncidentId]])

slots.incident_datetime = Slot(uri=ISO42001.incident_datetime, name="incident_datetime", curie=ISO42001.curie('incident_datetime'),
                   model_uri=ISO42001.incident_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.incident_category = Slot(uri=ISO42001.incident_category, name="incident_category", curie=ISO42001.curie('incident_category'),
                   model_uri=ISO42001.incident_category, domain=None, range=Optional[Union[str, "AIIncidentCategory"]])

slots.severity = Slot(uri=ISO42001.severity, name="severity", curie=ISO42001.curie('severity'),
                   model_uri=ISO42001.severity, domain=None, range=Optional[Union[str, "RiskLevel"]])

slots.incident_description = Slot(uri=ISO42001.incident_description, name="incident_description", curie=ISO42001.curie('incident_description'),
                   model_uri=ISO42001.incident_description, domain=None, range=Optional[str])

slots.detection_method = Slot(uri=ISO42001.detection_method, name="detection_method", curie=ISO42001.curie('detection_method'),
                   model_uri=ISO42001.detection_method, domain=None, range=Optional[str])

slots.response_actions = Slot(uri=ISO42001.response_actions, name="response_actions", curie=ISO42001.curie('response_actions'),
                   model_uri=ISO42001.response_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.containment_actions = Slot(uri=ISO42001.containment_actions, name="containment_actions", curie=ISO42001.curie('containment_actions'),
                   model_uri=ISO42001.containment_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.recovery_actions = Slot(uri=ISO42001.recovery_actions, name="recovery_actions", curie=ISO42001.curie('recovery_actions'),
                   model_uri=ISO42001.recovery_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.lessons_learned = Slot(uri=ISO42001.lessons_learned, name="lessons_learned", curie=ISO42001.curie('lessons_learned'),
                   model_uri=ISO42001.lessons_learned, domain=None, range=Optional[Union[str, list[str]]])

slots.evidence_collected = Slot(uri=ISO42001.evidence_collected, name="evidence_collected", curie=ISO42001.curie('evidence_collected'),
                   model_uri=ISO42001.evidence_collected, domain=None, range=Optional[Union[str, list[str]]])

slots.notification_required = Slot(uri=ISO42001.notification_required, name="notification_required", curie=ISO42001.curie('notification_required'),
                   model_uri=ISO42001.notification_required, domain=None, range=Optional[Union[bool, Bool]])

slots.notifications_made = Slot(uri=ISO42001.notifications_made, name="notifications_made", curie=ISO42001.curie('notifications_made'),
                   model_uri=ISO42001.notifications_made, domain=None, range=Optional[Union[str, list[str]]])

slots.external_reports = Slot(uri=ISO42001.external_reports, name="external_reports", curie=ISO42001.curie('external_reports'),
                   model_uri=ISO42001.external_reports, domain=None, range=Optional[Union[str, list[str]]])

slots.closure_datetime = Slot(uri=ISO42001.closure_datetime, name="closure_datetime", curie=ISO42001.curie('closure_datetime'),
                   model_uri=ISO42001.closure_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.post_incident_review = Slot(uri=ISO42001.post_incident_review, name="post_incident_review", curie=ISO42001.curie('post_incident_review'),
                   model_uri=ISO42001.post_incident_review, domain=None, range=Optional[str])

slots.integrated_management_systems = Slot(uri=ISO42001.integrated_management_systems, name="integrated_management_systems", curie=ISO42001.curie('integrated_management_systems'),
                   model_uri=ISO42001.integrated_management_systems, domain=None, range=Optional[Union[Union[str, "RelatedManagementSystem"], list[Union[str, "RelatedManagementSystem"]]]])

slots.top_management = Slot(uri=ISO42001.top_management, name="top_management", curie=ISO42001.curie('top_management'),
                   model_uri=ISO42001.top_management, domain=None, range=Optional[str])

slots.governing_body = Slot(uri=ISO42001.governing_body, name="governing_body", curie=ISO42001.curie('governing_body'),
                   model_uri=ISO42001.governing_body, domain=None, range=Optional[str])

slots.leadership_commitment_evidence = Slot(uri=ISO42001.leadership_commitment_evidence, name="leadership_commitment_evidence", curie=ISO42001.curie('leadership_commitment_evidence'),
                   model_uri=ISO42001.leadership_commitment_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.planned_changes = Slot(uri=ISO42001.planned_changes, name="planned_changes", curie=ISO42001.curie('planned_changes'),
                   model_uri=ISO42001.planned_changes, domain=None, range=Optional[Union[str, list[str]]])

slots.ml_approach = Slot(uri=ISO42001.ml_approach, name="ml_approach", curie=ISO42001.curie('ml_approach'),
                   model_uri=ISO42001.ml_approach, domain=None, range=Optional[Union[str, "MLApproach"]])

slots.human_oversight_required = Slot(uri=ISO42001.human_oversight_required, name="human_oversight_required", curie=ISO42001.curie('human_oversight_required'),
                   model_uri=ISO42001.human_oversight_required, domain=None, range=Optional[Union[bool, Bool]])

slots.human_oversight_description = Slot(uri=ISO42001.human_oversight_description, name="human_oversight_description", curie=ISO42001.curie('human_oversight_description'),
                   model_uri=ISO42001.human_oversight_description, domain=None, range=Optional[str])

slots.human_oversight_stages = Slot(uri=ISO42001.human_oversight_stages, name="human_oversight_stages", curie=ISO42001.curie('human_oversight_stages'),
                   model_uri=ISO42001.human_oversight_stages, domain=None, range=Optional[Union[Union[str, "AISystemLifecycleStage"], list[Union[str, "AISystemLifecycleStage"]]]])

slots.concern_reports = Slot(uri=ISO42001.concern_reports, name="concern_reports", curie=ISO42001.curie('concern_reports'),
                   model_uri=ISO42001.concern_reports, domain=None, range=Optional[Union[Union[str, ConcernReportId], list[Union[str, ConcernReportId]]]])

slots.reported_date = Slot(uri=ISO42001.reported_date, name="reported_date", curie=ISO42001.curie('reported_date'),
                   model_uri=ISO42001.reported_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.reporter_anonymous = Slot(uri=ISO42001.reporter_anonymous, name="reporter_anonymous", curie=ISO42001.curie('reporter_anonymous'),
                   model_uri=ISO42001.reporter_anonymous, domain=None, range=Optional[Union[bool, Bool]])

slots.confidentiality_level = Slot(uri=ISO42001.confidentiality_level, name="confidentiality_level", curie=ISO42001.curie('confidentiality_level'),
                   model_uri=ISO42001.confidentiality_level, domain=None, range=Optional[str])

slots.reporting_channel = Slot(uri=ISO42001.reporting_channel, name="reporting_channel", curie=ISO42001.curie('reporting_channel'),
                   model_uri=ISO42001.reporting_channel, domain=None, range=Optional[str])

slots.concern_description = Slot(uri=ISO42001.concern_description, name="concern_description", curie=ISO42001.curie('concern_description'),
                   model_uri=ISO42001.concern_description, domain=None, range=Optional[str])

slots.concern_ai_systems = Slot(uri=ISO42001.concern_ai_systems, name="concern_ai_systems", curie=ISO42001.curie('concern_ai_systems'),
                   model_uri=ISO42001.concern_ai_systems, domain=None, range=Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]])

slots.concern_lifecycle_stage = Slot(uri=ISO42001.concern_lifecycle_stage, name="concern_lifecycle_stage", curie=ISO42001.curie('concern_lifecycle_stage'),
                   model_uri=ISO42001.concern_lifecycle_stage, domain=None, range=Optional[Union[Union[str, "AISystemLifecycleStage"], list[Union[str, "AISystemLifecycleStage"]]]])

slots.investigator = Slot(uri=ISO42001.investigator, name="investigator", curie=ISO42001.curie('investigator'),
                   model_uri=ISO42001.investigator, domain=None, range=Optional[str])

slots.investigation_status = Slot(uri=ISO42001.investigation_status, name="investigation_status", curie=ISO42001.curie('investigation_status'),
                   model_uri=ISO42001.investigation_status, domain=None, range=Optional[str])

slots.investigation_findings = Slot(uri=ISO42001.investigation_findings, name="investigation_findings", curie=ISO42001.curie('investigation_findings'),
                   model_uri=ISO42001.investigation_findings, domain=None, range=Optional[str])

slots.escalation_status = Slot(uri=ISO42001.escalation_status, name="escalation_status", curie=ISO42001.curie('escalation_status'),
                   model_uri=ISO42001.escalation_status, domain=None, range=Optional[str])

slots.response_due_date = Slot(uri=ISO42001.response_due_date, name="response_due_date", curie=ISO42001.curie('response_due_date'),
                   model_uri=ISO42001.response_due_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.response_provided_date = Slot(uri=ISO42001.response_provided_date, name="response_provided_date", curie=ISO42001.curie('response_provided_date'),
                   model_uri=ISO42001.response_provided_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.resolution = Slot(uri=ISO42001.resolution, name="resolution", curie=ISO42001.curie('resolution'),
                   model_uri=ISO42001.resolution, domain=None, range=Optional[str])

slots.reprisal_protection_actions = Slot(uri=ISO42001.reprisal_protection_actions, name="reprisal_protection_actions", curie=ISO42001.curie('reprisal_protection_actions'),
                   model_uri=ISO42001.reprisal_protection_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.related_incidents = Slot(uri=ISO42001.related_incidents, name="related_incidents", curie=ISO42001.curie('related_incidents'),
                   model_uri=ISO42001.related_incidents, domain=None, range=Optional[Union[Union[str, AIIncidentId], list[Union[str, AIIncidentId]]]])

slots.related_nonconformities = Slot(uri=ISO42001.related_nonconformities, name="related_nonconformities", curie=ISO42001.curie('related_nonconformities'),
                   model_uri=ISO42001.related_nonconformities, domain=None, range=Optional[Union[Union[str, NonconformityId], list[Union[str, NonconformityId]]]])

slots.NamedEntity_id = Slot(uri=ISO42001.id, name="NamedEntity_id", curie=ISO42001.curie('id'),
                   model_uri=ISO42001.NamedEntity_id, domain=NamedEntity, range=Union[str, NamedEntityId])
