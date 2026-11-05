# Auto generated from iso42001.yaml by pythongen.py version: 0.0.1
# Schema: iso42001
#
# id: https://w3id.org/lmodel/iso42001
# description: A LinkML model of the records an organization keeps to run an artificial intelligence (AI) management system under ISO/IEC 42001:2023. The records cover its context, leadership, planning and support, how it weighs and treats AI risks, and what its AI systems may do to people and society. They also cover those systems with their resources, data and documents, its audits and reviews, and what it corrects and improves. The reference controls of Annex A appear by number, with titles of this project's own.
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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.12.0"
version = "2023"

# Namespaces
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO42001 = CurieNamespace('iso42001', 'https://w3id.org/lmodel/iso42001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPDX_CORE = CurieNamespace('spdx_core', 'https://spdx.org/rdf/3.0.1/terms/Core/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO42001


# Types
class AimsDuration(String):
    """ A length of time as ISO 8601 writes it, such as P7Y for seven years or P30D for thirty days. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "aims_duration"
    type_model_uri = ISO42001.AimsDuration


# Class references
class AimsRecordMixinAimsId(URIorCURIE):
    pass


class AimsManagementSystemAimsId(URIorCURIE):
    pass


class AimsOrganizationAimsId(URIorCURIE):
    pass


class AimsInterestedPartyAimsId(URIorCURIE):
    pass


class AimsPolicyAimsId(URIorCURIE):
    pass


class AimsTopicSpecificPolicyAimsId(URIorCURIE):
    pass


class AimsRoleAimsId(URIorCURIE):
    pass


class AimsObjectiveAimsId(URIorCURIE):
    pass


class AimsPlannedActionAimsId(URIorCURIE):
    pass


class AimsRiskAssessmentProcessAimsId(URIorCURIE):
    pass


class AimsRiskAssessmentAimsId(URIorCURIE):
    pass


class AimsRiskAimsId(URIorCURIE):
    pass


class AimsRiskTreatmentProcessAimsId(URIorCURIE):
    pass


class AimsRiskTreatmentPlanAimsId(URIorCURIE):
    pass


class AimsImpactAssessmentProcessAimsId(URIorCURIE):
    pass


class AimsImpactAssessmentAimsId(URIorCURIE):
    pass


class AimsStatementOfApplicabilityAimsId(URIorCURIE):
    pass


class AimsControlAimsId(URIorCURIE):
    pass


class AimsAiSystemAimsId(URIorCURIE):
    pass


class AimsSystemResourceAimsId(URIorCURIE):
    pass


class AimsComponentResourceAimsId(AimsSystemResourceAimsId):
    pass


class AimsDataResourceAimsId(AimsSystemResourceAimsId):
    pass


class AimsToolingResourceAimsId(AimsSystemResourceAimsId):
    pass


class AimsComputingResourceAimsId(AimsSystemResourceAimsId):
    pass


class AimsHumanResourceAimsId(AimsSystemResourceAimsId):
    pass


class AimsDevelopmentProcessAimsId(URIorCURIE):
    pass


class AimsResponsibleUseProcessAimsId(URIorCURIE):
    pass


class AimsTechnicalDocumentationAimsId(URIorCURIE):
    pass


class AimsUserInformationAimsId(URIorCURIE):
    pass


class AimsIncidentCommunicationPlanAimsId(URIorCURIE):
    pass


class AimsReportingObligationAimsId(URIorCURIE):
    pass


class AimsResourceAimsId(URIorCURIE):
    pass


class AimsCompetenceRecordAimsId(URIorCURIE):
    pass


class AimsAwarenessProgrammeAimsId(URIorCURIE):
    pass


class AimsCommunicationPlanAimsId(URIorCURIE):
    pass


class AimsDocumentedInformationAimsId(URIorCURIE):
    pass


class AimsOperationalProcedureAimsId(URIorCURIE):
    pass


class AimsMonitoringProgrammeAimsId(URIorCURIE):
    pass


class AimsAuditProgrammeAimsId(URIorCURIE):
    pass


class AimsAuditAimsId(URIorCURIE):
    pass


class AimsAuditFindingAimsId(URIorCURIE):
    pass


class AimsManagementReviewAimsId(URIorCURIE):
    pass


class AimsNonconformityAimsId(URIorCURIE):
    pass


class AimsCorrectiveActionAimsId(URIorCURIE):
    pass


class AimsImprovementOpportunityAimsId(URIorCURIE):
    pass


class AimsThirdPartyRelationshipAimsId(URIorCURIE):
    pass


class AimsSupplierRelationshipAimsId(AimsThirdPartyRelationshipAimsId):
    pass


class AimsCustomerRelationshipAimsId(AimsThirdPartyRelationshipAimsId):
    pass


class AimsSystemEventAimsId(URIorCURIE):
    pass


class AimsIncidentAimsId(AimsSystemEventAimsId):
    pass


class AimsConcernReportingProcessAimsId(URIorCURIE):
    pass


class AimsConcernReportAimsId(URIorCURIE):
    pass


@dataclass(repr=False)
class AimsRecordMixin(YAMLRoot):
    """
    What every record of the system has, so that other records can refer to it: an identifier, a title and a
    description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRecordMixin"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRecordMixin"
    class_name: ClassVar[str] = "AimsRecordMixin"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRecordMixin

    aims_id: Union[str, AimsRecordMixinAimsId] = None
    title: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRecordMixinAimsId):
            self.aims_id = AimsRecordMixinAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsDocumentControlMixin(YAMLRoot):
    """
    The control that documented information is kept under: who wrote, owns and approved it, its format and medium,
    when it takes effect and is looked at again, how it is classified, handed out, stored and changed, how long it is
    kept, and whether it came from outside.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsDocumentControlMixin"]
    class_class_curie: ClassVar[str] = "iso42001:AimsDocumentControlMixin"
    class_name: ClassVar[str] = "AimsDocumentControlMixin"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsDocumentControlMixin

    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsManagementSystem(YAMLRoot):
    """
    One organization's management system for AI: its scope and context, and every record it keeps, each kind in a list
    of its own.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsManagementSystem"]
    class_class_curie: ClassVar[str] = "iso42001:AimsManagementSystem"
    class_name: ClassVar[str] = "AimsManagementSystem"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsManagementSystem

    aims_id: Union[str, AimsManagementSystemAimsId] = None
    title: str = None
    aims_organization: Optional[Union[dict, "AimsOrganization"]] = None
    aims_top_management: Optional[str] = None
    aims_governing_body: Optional[str] = None
    aims_leadership_evidence: Optional[Union[str, list[str]]] = empty_list()
    aims_scope: Optional[str] = None
    aims_scope_boundaries: Optional[Union[str, list[str]]] = empty_list()
    aims_scope_applicability: Optional[Union[str, list[str]]] = empty_list()
    aims_processes: Optional[str] = None
    aims_internal_issues: Optional[Union[str, list[str]]] = empty_list()
    aims_external_issues: Optional[Union[str, list[str]]] = empty_list()
    aims_planned_changes: Optional[Union[str, list[str]]] = empty_list()
    aims_external_services: Optional[Union[str, list[str]]] = empty_list()
    aims_integrated_standards: Optional[Union[Union[str, "AimsManagementSystemStandard"], list[Union[str, "AimsManagementSystemStandard"]]]] = empty_list()
    aims_certification_status: Optional[str] = None
    aims_certification_body: Optional[str] = None
    aims_certification_date: Optional[Union[str, XSDDate]] = None
    aims_recertification_date: Optional[Union[str, XSDDate]] = None
    aims_interested_parties: Optional[Union[dict[Union[str, AimsInterestedPartyAimsId], Union[dict, "AimsInterestedParty"]], list[Union[dict, "AimsInterestedParty"]]]] = empty_dict()
    aims_policy: Optional[Union[dict, "AimsPolicy"]] = None
    aims_topic_specific_policies: Optional[Union[dict[Union[str, AimsTopicSpecificPolicyAimsId], Union[dict, "AimsTopicSpecificPolicy"]], list[Union[dict, "AimsTopicSpecificPolicy"]]]] = empty_dict()
    aims_roles: Optional[Union[dict[Union[str, AimsRoleAimsId], Union[dict, "AimsRole"]], list[Union[dict, "AimsRole"]]]] = empty_dict()
    aims_objectives: Optional[Union[dict[Union[str, AimsObjectiveAimsId], Union[dict, "AimsObjective"]], list[Union[dict, "AimsObjective"]]]] = empty_dict()
    aims_planned_actions: Optional[Union[dict[Union[str, AimsPlannedActionAimsId], Union[dict, "AimsPlannedAction"]], list[Union[dict, "AimsPlannedAction"]]]] = empty_dict()
    aims_risk_assessment_process: Optional[Union[dict, "AimsRiskAssessmentProcess"]] = None
    aims_risk_treatment_process: Optional[Union[dict, "AimsRiskTreatmentProcess"]] = None
    aims_impact_assessment_process: Optional[Union[dict, "AimsImpactAssessmentProcess"]] = None
    aims_risk_assessments: Optional[Union[dict[Union[str, AimsRiskAssessmentAimsId], Union[dict, "AimsRiskAssessment"]], list[Union[dict, "AimsRiskAssessment"]]]] = empty_dict()
    aims_risks: Optional[Union[dict[Union[str, AimsRiskAimsId], Union[dict, "AimsRisk"]], list[Union[dict, "AimsRisk"]]]] = empty_dict()
    aims_risk_treatment_plans: Optional[Union[dict[Union[str, AimsRiskTreatmentPlanAimsId], Union[dict, "AimsRiskTreatmentPlan"]], list[Union[dict, "AimsRiskTreatmentPlan"]]]] = empty_dict()
    aims_impact_assessments: Optional[Union[dict[Union[str, AimsImpactAssessmentAimsId], Union[dict, "AimsImpactAssessment"]], list[Union[dict, "AimsImpactAssessment"]]]] = empty_dict()
    aims_statement_of_applicability: Optional[Union[dict, "AimsStatementOfApplicability"]] = None
    aims_controls: Optional[Union[dict[Union[str, AimsControlAimsId], Union[dict, "AimsControl"]], list[Union[dict, "AimsControl"]]]] = empty_dict()
    aims_systems: Optional[Union[dict[Union[str, AimsAiSystemAimsId], Union[dict, "AimsAiSystem"]], list[Union[dict, "AimsAiSystem"]]]] = empty_dict()
    aims_system_resources: Optional[Union[dict[Union[str, AimsSystemResourceAimsId], Union[dict, "AimsSystemResource"]], list[Union[dict, "AimsSystemResource"]]]] = empty_dict()
    aims_development_processes: Optional[Union[dict[Union[str, AimsDevelopmentProcessAimsId], Union[dict, "AimsDevelopmentProcess"]], list[Union[dict, "AimsDevelopmentProcess"]]]] = empty_dict()
    aims_use_processes: Optional[Union[dict[Union[str, AimsResponsibleUseProcessAimsId], Union[dict, "AimsResponsibleUseProcess"]], list[Union[dict, "AimsResponsibleUseProcess"]]]] = empty_dict()
    aims_technical_documentation: Optional[Union[dict[Union[str, AimsTechnicalDocumentationAimsId], Union[dict, "AimsTechnicalDocumentation"]], list[Union[dict, "AimsTechnicalDocumentation"]]]] = empty_dict()
    aims_user_information: Optional[Union[dict[Union[str, AimsUserInformationAimsId], Union[dict, "AimsUserInformation"]], list[Union[dict, "AimsUserInformation"]]]] = empty_dict()
    aims_incident_communication_plans: Optional[Union[dict[Union[str, AimsIncidentCommunicationPlanAimsId], Union[dict, "AimsIncidentCommunicationPlan"]], list[Union[dict, "AimsIncidentCommunicationPlan"]]]] = empty_dict()
    aims_reporting_obligations: Optional[Union[dict[Union[str, AimsReportingObligationAimsId], Union[dict, "AimsReportingObligation"]], list[Union[dict, "AimsReportingObligation"]]]] = empty_dict()
    aims_third_party_relationships: Optional[Union[dict[Union[str, AimsThirdPartyRelationshipAimsId], Union[dict, "AimsThirdPartyRelationship"]], list[Union[dict, "AimsThirdPartyRelationship"]]]] = empty_dict()
    aims_resources: Optional[Union[dict[Union[str, AimsResourceAimsId], Union[dict, "AimsResource"]], list[Union[dict, "AimsResource"]]]] = empty_dict()
    aims_competence_records: Optional[Union[dict[Union[str, AimsCompetenceRecordAimsId], Union[dict, "AimsCompetenceRecord"]], list[Union[dict, "AimsCompetenceRecord"]]]] = empty_dict()
    aims_awareness_programme: Optional[Union[dict, "AimsAwarenessProgramme"]] = None
    aims_communication_plan: Optional[Union[dict, "AimsCommunicationPlan"]] = None
    aims_documented_information: Optional[Union[dict[Union[str, AimsDocumentedInformationAimsId], Union[dict, "AimsDocumentedInformation"]], list[Union[dict, "AimsDocumentedInformation"]]]] = empty_dict()
    aims_operational_procedures: Optional[Union[dict[Union[str, AimsOperationalProcedureAimsId], Union[dict, "AimsOperationalProcedure"]], list[Union[dict, "AimsOperationalProcedure"]]]] = empty_dict()
    aims_monitoring_programme: Optional[Union[dict, "AimsMonitoringProgramme"]] = None
    aims_audit_programmes: Optional[Union[dict[Union[str, AimsAuditProgrammeAimsId], Union[dict, "AimsAuditProgramme"]], list[Union[dict, "AimsAuditProgramme"]]]] = empty_dict()
    aims_audits: Optional[Union[dict[Union[str, AimsAuditAimsId], Union[dict, "AimsAudit"]], list[Union[dict, "AimsAudit"]]]] = empty_dict()
    aims_management_reviews: Optional[Union[dict[Union[str, AimsManagementReviewAimsId], Union[dict, "AimsManagementReview"]], list[Union[dict, "AimsManagementReview"]]]] = empty_dict()
    aims_nonconformities: Optional[Union[dict[Union[str, AimsNonconformityAimsId], Union[dict, "AimsNonconformity"]], list[Union[dict, "AimsNonconformity"]]]] = empty_dict()
    aims_corrective_actions: Optional[Union[dict[Union[str, AimsCorrectiveActionAimsId], Union[dict, "AimsCorrectiveAction"]], list[Union[dict, "AimsCorrectiveAction"]]]] = empty_dict()
    aims_improvements: Optional[Union[dict[Union[str, AimsImprovementOpportunityAimsId], Union[dict, "AimsImprovementOpportunity"]], list[Union[dict, "AimsImprovementOpportunity"]]]] = empty_dict()
    aims_system_events: Optional[Union[dict[Union[str, AimsSystemEventAimsId], Union[dict, "AimsSystemEvent"]], list[Union[dict, "AimsSystemEvent"]]]] = empty_dict()
    aims_concern_reporting_process: Optional[Union[dict, "AimsConcernReportingProcess"]] = None
    aims_concern_reports: Optional[Union[dict[Union[str, AimsConcernReportAimsId], Union[dict, "AimsConcernReport"]], list[Union[dict, "AimsConcernReport"]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsManagementSystemAimsId):
            self.aims_id = AimsManagementSystemAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_organization is not None and not isinstance(self.aims_organization, AimsOrganization):
            self.aims_organization = AimsOrganization(**as_dict(self.aims_organization))

        if self.aims_top_management is not None and not isinstance(self.aims_top_management, str):
            self.aims_top_management = str(self.aims_top_management)

        if self.aims_governing_body is not None and not isinstance(self.aims_governing_body, str):
            self.aims_governing_body = str(self.aims_governing_body)

        if not isinstance(self.aims_leadership_evidence, list):
            self.aims_leadership_evidence = [self.aims_leadership_evidence] if self.aims_leadership_evidence is not None else []
        self.aims_leadership_evidence = [v if isinstance(v, str) else str(v) for v in self.aims_leadership_evidence]

        if self.aims_scope is not None and not isinstance(self.aims_scope, str):
            self.aims_scope = str(self.aims_scope)

        if not isinstance(self.aims_scope_boundaries, list):
            self.aims_scope_boundaries = [self.aims_scope_boundaries] if self.aims_scope_boundaries is not None else []
        self.aims_scope_boundaries = [v if isinstance(v, str) else str(v) for v in self.aims_scope_boundaries]

        if not isinstance(self.aims_scope_applicability, list):
            self.aims_scope_applicability = [self.aims_scope_applicability] if self.aims_scope_applicability is not None else []
        self.aims_scope_applicability = [v if isinstance(v, str) else str(v) for v in self.aims_scope_applicability]

        if self.aims_processes is not None and not isinstance(self.aims_processes, str):
            self.aims_processes = str(self.aims_processes)

        if not isinstance(self.aims_internal_issues, list):
            self.aims_internal_issues = [self.aims_internal_issues] if self.aims_internal_issues is not None else []
        self.aims_internal_issues = [v if isinstance(v, str) else str(v) for v in self.aims_internal_issues]

        if not isinstance(self.aims_external_issues, list):
            self.aims_external_issues = [self.aims_external_issues] if self.aims_external_issues is not None else []
        self.aims_external_issues = [v if isinstance(v, str) else str(v) for v in self.aims_external_issues]

        if not isinstance(self.aims_planned_changes, list):
            self.aims_planned_changes = [self.aims_planned_changes] if self.aims_planned_changes is not None else []
        self.aims_planned_changes = [v if isinstance(v, str) else str(v) for v in self.aims_planned_changes]

        if not isinstance(self.aims_external_services, list):
            self.aims_external_services = [self.aims_external_services] if self.aims_external_services is not None else []
        self.aims_external_services = [v if isinstance(v, str) else str(v) for v in self.aims_external_services]

        if not isinstance(self.aims_integrated_standards, list):
            self.aims_integrated_standards = [self.aims_integrated_standards] if self.aims_integrated_standards is not None else []
        self.aims_integrated_standards = [v if isinstance(v, AimsManagementSystemStandard) else AimsManagementSystemStandard(v) for v in self.aims_integrated_standards]

        if self.aims_certification_status is not None and not isinstance(self.aims_certification_status, str):
            self.aims_certification_status = str(self.aims_certification_status)

        if self.aims_certification_body is not None and not isinstance(self.aims_certification_body, str):
            self.aims_certification_body = str(self.aims_certification_body)

        if self.aims_certification_date is not None and not isinstance(self.aims_certification_date, XSDDate):
            self.aims_certification_date = XSDDate(self.aims_certification_date)

        if self.aims_recertification_date is not None and not isinstance(self.aims_recertification_date, XSDDate):
            self.aims_recertification_date = XSDDate(self.aims_recertification_date)

        self._normalize_inlined_as_list(slot_name="aims_interested_parties", slot_type=AimsInterestedParty, key_name="aims_id", keyed=True)

        if self.aims_policy is not None and not isinstance(self.aims_policy, AimsPolicy):
            self.aims_policy = AimsPolicy(**as_dict(self.aims_policy))

        self._normalize_inlined_as_list(slot_name="aims_topic_specific_policies", slot_type=AimsTopicSpecificPolicy, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_roles", slot_type=AimsRole, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_objectives", slot_type=AimsObjective, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_planned_actions", slot_type=AimsPlannedAction, key_name="aims_id", keyed=True)

        if self.aims_risk_assessment_process is not None and not isinstance(self.aims_risk_assessment_process, AimsRiskAssessmentProcess):
            self.aims_risk_assessment_process = AimsRiskAssessmentProcess(**as_dict(self.aims_risk_assessment_process))

        if self.aims_risk_treatment_process is not None and not isinstance(self.aims_risk_treatment_process, AimsRiskTreatmentProcess):
            self.aims_risk_treatment_process = AimsRiskTreatmentProcess(**as_dict(self.aims_risk_treatment_process))

        if self.aims_impact_assessment_process is not None and not isinstance(self.aims_impact_assessment_process, AimsImpactAssessmentProcess):
            self.aims_impact_assessment_process = AimsImpactAssessmentProcess(**as_dict(self.aims_impact_assessment_process))

        self._normalize_inlined_as_list(slot_name="aims_risk_assessments", slot_type=AimsRiskAssessment, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_risks", slot_type=AimsRisk, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_risk_treatment_plans", slot_type=AimsRiskTreatmentPlan, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_impact_assessments", slot_type=AimsImpactAssessment, key_name="aims_id", keyed=True)

        if self.aims_statement_of_applicability is not None and not isinstance(self.aims_statement_of_applicability, AimsStatementOfApplicability):
            self.aims_statement_of_applicability = AimsStatementOfApplicability(**as_dict(self.aims_statement_of_applicability))

        self._normalize_inlined_as_list(slot_name="aims_controls", slot_type=AimsControl, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_systems", slot_type=AimsAiSystem, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_system_resources", slot_type=AimsSystemResource, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_development_processes", slot_type=AimsDevelopmentProcess, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_use_processes", slot_type=AimsResponsibleUseProcess, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_technical_documentation", slot_type=AimsTechnicalDocumentation, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_user_information", slot_type=AimsUserInformation, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_incident_communication_plans", slot_type=AimsIncidentCommunicationPlan, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_reporting_obligations", slot_type=AimsReportingObligation, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_third_party_relationships", slot_type=AimsThirdPartyRelationship, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_resources", slot_type=AimsResource, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_competence_records", slot_type=AimsCompetenceRecord, key_name="aims_id", keyed=True)

        if self.aims_awareness_programme is not None and not isinstance(self.aims_awareness_programme, AimsAwarenessProgramme):
            self.aims_awareness_programme = AimsAwarenessProgramme(**as_dict(self.aims_awareness_programme))

        if self.aims_communication_plan is not None and not isinstance(self.aims_communication_plan, AimsCommunicationPlan):
            self.aims_communication_plan = AimsCommunicationPlan(**as_dict(self.aims_communication_plan))

        self._normalize_inlined_as_list(slot_name="aims_documented_information", slot_type=AimsDocumentedInformation, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_operational_procedures", slot_type=AimsOperationalProcedure, key_name="aims_id", keyed=True)

        if self.aims_monitoring_programme is not None and not isinstance(self.aims_monitoring_programme, AimsMonitoringProgramme):
            self.aims_monitoring_programme = AimsMonitoringProgramme(**as_dict(self.aims_monitoring_programme))

        self._normalize_inlined_as_list(slot_name="aims_audit_programmes", slot_type=AimsAuditProgramme, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_audits", slot_type=AimsAudit, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_management_reviews", slot_type=AimsManagementReview, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_nonconformities", slot_type=AimsNonconformity, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_corrective_actions", slot_type=AimsCorrectiveAction, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_improvements", slot_type=AimsImprovementOpportunity, key_name="aims_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aims_system_events", slot_type=AimsSystemEvent, key_name="aims_id", keyed=True)

        if self.aims_concern_reporting_process is not None and not isinstance(self.aims_concern_reporting_process, AimsConcernReportingProcess):
            self.aims_concern_reporting_process = AimsConcernReportingProcess(**as_dict(self.aims_concern_reporting_process))

        self._normalize_inlined_as_list(slot_name="aims_concern_reports", slot_type=AimsConcernReport, key_name="aims_id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsOrganization(YAMLRoot):
    """
    The organization that runs the system, with what it needs to know about itself to understand its context and the
    parts it plays with AI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsOrganization"]
    class_class_curie: ClassVar[str] = "iso42001:AimsOrganization"
    class_name: ClassVar[str] = "AimsOrganization"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsOrganization

    aims_id: Union[str, AimsOrganizationAimsId] = None
    title: str = None
    aims_organization_legal_name: Optional[str] = None
    aims_organization_trading_names: Optional[Union[str, list[str]]] = empty_list()
    aims_organization_kind: Optional[str] = None
    aims_organization_sectors: Optional[Union[str, list[str]]] = empty_list()
    aims_organization_size: Optional[str] = None
    aims_organization_employee_count: Optional[int] = None
    aims_organization_locations: Optional[Union[str, list[str]]] = empty_list()
    aims_organization_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    aims_organization_parent: Optional[str] = None
    aims_organization_subsidiaries: Optional[Union[str, list[str]]] = empty_list()
    aims_organization_ai_roles: Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]] = empty_list()
    aims_organization_pii_roles: Optional[Union[Union[str, "AimsPiiRole"], list[Union[str, "AimsPiiRole"]]]] = empty_list()
    aims_organization_climate_change_relevant: Optional[Union[bool, Bool]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsOrganizationAimsId):
            self.aims_id = AimsOrganizationAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_organization_legal_name is not None and not isinstance(self.aims_organization_legal_name, str):
            self.aims_organization_legal_name = str(self.aims_organization_legal_name)

        if not isinstance(self.aims_organization_trading_names, list):
            self.aims_organization_trading_names = [self.aims_organization_trading_names] if self.aims_organization_trading_names is not None else []
        self.aims_organization_trading_names = [v if isinstance(v, str) else str(v) for v in self.aims_organization_trading_names]

        if self.aims_organization_kind is not None and not isinstance(self.aims_organization_kind, str):
            self.aims_organization_kind = str(self.aims_organization_kind)

        if not isinstance(self.aims_organization_sectors, list):
            self.aims_organization_sectors = [self.aims_organization_sectors] if self.aims_organization_sectors is not None else []
        self.aims_organization_sectors = [v if isinstance(v, str) else str(v) for v in self.aims_organization_sectors]

        if self.aims_organization_size is not None and not isinstance(self.aims_organization_size, str):
            self.aims_organization_size = str(self.aims_organization_size)

        if self.aims_organization_employee_count is not None and not isinstance(self.aims_organization_employee_count, int):
            self.aims_organization_employee_count = int(self.aims_organization_employee_count)

        if not isinstance(self.aims_organization_locations, list):
            self.aims_organization_locations = [self.aims_organization_locations] if self.aims_organization_locations is not None else []
        self.aims_organization_locations = [v if isinstance(v, str) else str(v) for v in self.aims_organization_locations]

        if not isinstance(self.aims_organization_jurisdictions, list):
            self.aims_organization_jurisdictions = [self.aims_organization_jurisdictions] if self.aims_organization_jurisdictions is not None else []
        self.aims_organization_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.aims_organization_jurisdictions]

        if self.aims_organization_parent is not None and not isinstance(self.aims_organization_parent, str):
            self.aims_organization_parent = str(self.aims_organization_parent)

        if not isinstance(self.aims_organization_subsidiaries, list):
            self.aims_organization_subsidiaries = [self.aims_organization_subsidiaries] if self.aims_organization_subsidiaries is not None else []
        self.aims_organization_subsidiaries = [v if isinstance(v, str) else str(v) for v in self.aims_organization_subsidiaries]

        if not isinstance(self.aims_organization_ai_roles, list):
            self.aims_organization_ai_roles = [self.aims_organization_ai_roles] if self.aims_organization_ai_roles is not None else []
        self.aims_organization_ai_roles = [v if isinstance(v, AimsAiRole) else AimsAiRole(v) for v in self.aims_organization_ai_roles]

        if not isinstance(self.aims_organization_pii_roles, list):
            self.aims_organization_pii_roles = [self.aims_organization_pii_roles] if self.aims_organization_pii_roles is not None else []
        self.aims_organization_pii_roles = [v if isinstance(v, AimsPiiRole) else AimsPiiRole(v) for v in self.aims_organization_pii_roles]

        if self.aims_organization_climate_change_relevant is not None and not isinstance(self.aims_organization_climate_change_relevant, Bool):
            self.aims_organization_climate_change_relevant = Bool(self.aims_organization_climate_change_relevant)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsInterestedParty(YAMLRoot):
    """
    A person or organization whose needs and expectations bear on the system, or who may feel its decisions, inside
    the organization or outside it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsInterestedParty"]
    class_class_curie: ClassVar[str] = "iso42001:AimsInterestedParty"
    class_name: ClassVar[str] = "AimsInterestedParty"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsInterestedParty

    aims_id: Union[str, AimsInterestedPartyAimsId] = None
    title: str = None
    aims_party_category: Optional[str] = None
    aims_party_ai_roles: Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]] = empty_list()
    aims_party_relationship: Optional[str] = None
    aims_party_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_party_addressed_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_party_climate_change_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_party_communication_needs: Optional[str] = None
    aims_party_contact: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsInterestedPartyAimsId):
            self.aims_id = AimsInterestedPartyAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_party_category is not None and not isinstance(self.aims_party_category, str):
            self.aims_party_category = str(self.aims_party_category)

        if not isinstance(self.aims_party_ai_roles, list):
            self.aims_party_ai_roles = [self.aims_party_ai_roles] if self.aims_party_ai_roles is not None else []
        self.aims_party_ai_roles = [v if isinstance(v, AimsAiRole) else AimsAiRole(v) for v in self.aims_party_ai_roles]

        if self.aims_party_relationship is not None and not isinstance(self.aims_party_relationship, str):
            self.aims_party_relationship = str(self.aims_party_relationship)

        if not isinstance(self.aims_party_requirements, list):
            self.aims_party_requirements = [self.aims_party_requirements] if self.aims_party_requirements is not None else []
        self.aims_party_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_party_requirements]

        if not isinstance(self.aims_party_addressed_requirements, list):
            self.aims_party_addressed_requirements = [self.aims_party_addressed_requirements] if self.aims_party_addressed_requirements is not None else []
        self.aims_party_addressed_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_party_addressed_requirements]

        if not isinstance(self.aims_party_climate_change_requirements, list):
            self.aims_party_climate_change_requirements = [self.aims_party_climate_change_requirements] if self.aims_party_climate_change_requirements is not None else []
        self.aims_party_climate_change_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_party_climate_change_requirements]

        if self.aims_party_communication_needs is not None and not isinstance(self.aims_party_communication_needs, str):
            self.aims_party_communication_needs = str(self.aims_party_communication_needs)

        if self.aims_party_contact is not None and not isinstance(self.aims_party_contact, str):
            self.aims_party_contact = str(self.aims_party_contact)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsPolicy(YAMLRoot):
    """
    The AI policy that top management sets: the organization's commitments and the frame for its AI objectives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsPolicy"]
    class_class_curie: ClassVar[str] = "iso42001:AimsPolicy"
    class_name: ClassVar[str] = "AimsPolicy"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsPolicy

    aims_id: Union[str, AimsPolicyAimsId] = None
    title: str = None
    aims_cited_clauses: Optional[Union[Union[str, "AimsClause"], list[Union[str, "AimsClause"]]]] = empty_list()
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    aims_policy_statement: Optional[str] = None
    aims_policy_objectives_framework: Optional[str] = None
    aims_policy_commitments: Optional[Union[str, list[str]]] = empty_list()
    aims_policy_principles: Optional[Union[str, list[str]]] = empty_list()
    aims_policy_exceptions_process: Optional[str] = None
    aims_policy_influences: Optional[Union[str, list[str]]] = empty_list()
    aims_policy_related_policies: Optional[Union[str, list[str]]] = empty_list()
    aims_policy_communication_date: Optional[Union[str, XSDDate]] = None
    aims_policy_availability: Optional[str] = None
    aims_policy_review_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_policy_review_interval: Optional[Union[str, AimsDuration]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsPolicyAimsId):
            self.aims_id = AimsPolicyAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_cited_clauses, list):
            self.aims_cited_clauses = [self.aims_cited_clauses] if self.aims_cited_clauses is not None else []
        self.aims_cited_clauses = [v if isinstance(v, AimsClause) else AimsClause(v) for v in self.aims_cited_clauses]

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if self.aims_policy_statement is not None and not isinstance(self.aims_policy_statement, str):
            self.aims_policy_statement = str(self.aims_policy_statement)

        if self.aims_policy_objectives_framework is not None and not isinstance(self.aims_policy_objectives_framework, str):
            self.aims_policy_objectives_framework = str(self.aims_policy_objectives_framework)

        if not isinstance(self.aims_policy_commitments, list):
            self.aims_policy_commitments = [self.aims_policy_commitments] if self.aims_policy_commitments is not None else []
        self.aims_policy_commitments = [v if isinstance(v, str) else str(v) for v in self.aims_policy_commitments]

        if not isinstance(self.aims_policy_principles, list):
            self.aims_policy_principles = [self.aims_policy_principles] if self.aims_policy_principles is not None else []
        self.aims_policy_principles = [v if isinstance(v, str) else str(v) for v in self.aims_policy_principles]

        if self.aims_policy_exceptions_process is not None and not isinstance(self.aims_policy_exceptions_process, str):
            self.aims_policy_exceptions_process = str(self.aims_policy_exceptions_process)

        if not isinstance(self.aims_policy_influences, list):
            self.aims_policy_influences = [self.aims_policy_influences] if self.aims_policy_influences is not None else []
        self.aims_policy_influences = [v if isinstance(v, str) else str(v) for v in self.aims_policy_influences]

        if not isinstance(self.aims_policy_related_policies, list):
            self.aims_policy_related_policies = [self.aims_policy_related_policies] if self.aims_policy_related_policies is not None else []
        self.aims_policy_related_policies = [v if isinstance(v, str) else str(v) for v in self.aims_policy_related_policies]

        if self.aims_policy_communication_date is not None and not isinstance(self.aims_policy_communication_date, XSDDate):
            self.aims_policy_communication_date = XSDDate(self.aims_policy_communication_date)

        if self.aims_policy_availability is not None and not isinstance(self.aims_policy_availability, str):
            self.aims_policy_availability = str(self.aims_policy_availability)

        if self.aims_policy_review_role is not None and not isinstance(self.aims_policy_review_role, AimsRoleAimsId):
            self.aims_policy_review_role = AimsRoleAimsId(self.aims_policy_review_role)

        if self.aims_policy_review_interval is not None and not isinstance(self.aims_policy_review_interval, AimsDuration):
            self.aims_policy_review_interval = AimsDuration(self.aims_policy_review_interval)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsTopicSpecificPolicy(YAMLRoot):
    """
    A policy on one topic that gives more guidance under the AI policy, such as assessing impacts or building systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsTopicSpecificPolicy"]
    class_class_curie: ClassVar[str] = "iso42001:AimsTopicSpecificPolicy"
    class_name: ClassVar[str] = "AimsTopicSpecificPolicy"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsTopicSpecificPolicy

    aims_id: Union[str, AimsTopicSpecificPolicyAimsId] = None
    title: str = None
    aims_relevant_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    aims_topic_policy_topic: Optional[str] = None
    aims_topic_policy_parent: Optional[Union[str, AimsPolicyAimsId]] = None
    aims_topic_policy_audience: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsTopicSpecificPolicyAimsId):
            self.aims_id = AimsTopicSpecificPolicyAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_relevant_controls, list):
            self.aims_relevant_controls = [self.aims_relevant_controls] if self.aims_relevant_controls is not None else []
        self.aims_relevant_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_relevant_controls]

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if self.aims_topic_policy_topic is not None and not isinstance(self.aims_topic_policy_topic, str):
            self.aims_topic_policy_topic = str(self.aims_topic_policy_topic)

        if self.aims_topic_policy_parent is not None and not isinstance(self.aims_topic_policy_parent, AimsPolicyAimsId):
            self.aims_topic_policy_parent = AimsPolicyAimsId(self.aims_topic_policy_parent)

        if self.aims_topic_policy_audience is not None and not isinstance(self.aims_topic_policy_audience, str):
            self.aims_topic_policy_audience = str(self.aims_topic_policy_audience)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsRole(YAMLRoot):
    """
    A role in the system, with the duties and powers it carries and who holds it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRole"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRole"
    class_name: ClassVar[str] = "AimsRole"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRole

    aims_id: Union[str, AimsRoleAimsId] = None
    title: str = None
    aims_role_category: Optional[str] = None
    aims_role_areas: Optional[Union[str, list[str]]] = empty_list()
    aims_role_responsibilities: Optional[Union[str, list[str]]] = empty_list()
    aims_role_authorities: Optional[Union[str, list[str]]] = empty_list()
    aims_role_ensures_conformity: Optional[Union[bool, Bool]] = None
    aims_role_reports_performance: Optional[Union[bool, Bool]] = None
    aims_role_accountability: Optional[str] = None
    aims_role_holders: Optional[Union[str, list[str]]] = empty_list()
    aims_role_delegation: Optional[str] = None
    aims_role_reports_to: Optional[Union[str, AimsRoleAimsId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRoleAimsId):
            self.aims_id = AimsRoleAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_role_category is not None and not isinstance(self.aims_role_category, str):
            self.aims_role_category = str(self.aims_role_category)

        if not isinstance(self.aims_role_areas, list):
            self.aims_role_areas = [self.aims_role_areas] if self.aims_role_areas is not None else []
        self.aims_role_areas = [v if isinstance(v, str) else str(v) for v in self.aims_role_areas]

        if not isinstance(self.aims_role_responsibilities, list):
            self.aims_role_responsibilities = [self.aims_role_responsibilities] if self.aims_role_responsibilities is not None else []
        self.aims_role_responsibilities = [v if isinstance(v, str) else str(v) for v in self.aims_role_responsibilities]

        if not isinstance(self.aims_role_authorities, list):
            self.aims_role_authorities = [self.aims_role_authorities] if self.aims_role_authorities is not None else []
        self.aims_role_authorities = [v if isinstance(v, str) else str(v) for v in self.aims_role_authorities]

        if self.aims_role_ensures_conformity is not None and not isinstance(self.aims_role_ensures_conformity, Bool):
            self.aims_role_ensures_conformity = Bool(self.aims_role_ensures_conformity)

        if self.aims_role_reports_performance is not None and not isinstance(self.aims_role_reports_performance, Bool):
            self.aims_role_reports_performance = Bool(self.aims_role_reports_performance)

        if self.aims_role_accountability is not None and not isinstance(self.aims_role_accountability, str):
            self.aims_role_accountability = str(self.aims_role_accountability)

        if not isinstance(self.aims_role_holders, list):
            self.aims_role_holders = [self.aims_role_holders] if self.aims_role_holders is not None else []
        self.aims_role_holders = [v if isinstance(v, str) else str(v) for v in self.aims_role_holders]

        if self.aims_role_delegation is not None and not isinstance(self.aims_role_delegation, str):
            self.aims_role_delegation = str(self.aims_role_delegation)

        if self.aims_role_reports_to is not None and not isinstance(self.aims_role_reports_to, AimsRoleAimsId):
            self.aims_role_reports_to = AimsRoleAimsId(self.aims_role_reports_to)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsObjective(YAMLRoot):
    """
    An AI objective: a result the organization aims for, with how it plans to reach it and how it judges progress.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsObjective"]
    class_class_curie: ClassVar[str] = "iso42001:AimsObjective"
    class_name: ClassVar[str] = "AimsObjective"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsObjective

    aims_id: Union[str, AimsObjectiveAimsId] = None
    title: str = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_relevant_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_objective_categories: Optional[Union[Union[str, "AimsObjectiveCategory"], list[Union[str, "AimsObjectiveCategory"]]]] = empty_list()
    aims_objective_purpose: Optional[Union[str, "AimsObjectivePurpose"]] = None
    aims_objective_statement: Optional[str] = None
    aims_objective_target: Optional[str] = None
    aims_objective_current_value: Optional[str] = None
    aims_objective_metric: Optional[str] = None
    aims_objective_measurement_method: Optional[str] = None
    aims_objective_measurement_frequency: Optional[str] = None
    aims_objective_target_date: Optional[Union[str, XSDDate]] = None
    aims_objective_achievement: Optional[str] = None
    aims_objective_risks: Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]] = empty_list()
    aims_objective_action_plan: Optional[str] = None
    aims_objective_resources: Optional[str] = None
    aims_objective_evaluation: Optional[str] = None
    aims_objective_communication: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsObjectiveAimsId):
            self.aims_id = AimsObjectiveAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if not isinstance(self.aims_relevant_controls, list):
            self.aims_relevant_controls = [self.aims_relevant_controls] if self.aims_relevant_controls is not None else []
        self.aims_relevant_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_relevant_controls]

        if not isinstance(self.aims_objective_categories, list):
            self.aims_objective_categories = [self.aims_objective_categories] if self.aims_objective_categories is not None else []
        self.aims_objective_categories = [v if isinstance(v, AimsObjectiveCategory) else AimsObjectiveCategory(v) for v in self.aims_objective_categories]

        if self.aims_objective_purpose is not None and not isinstance(self.aims_objective_purpose, AimsObjectivePurpose):
            self.aims_objective_purpose = AimsObjectivePurpose(self.aims_objective_purpose)

        if self.aims_objective_statement is not None and not isinstance(self.aims_objective_statement, str):
            self.aims_objective_statement = str(self.aims_objective_statement)

        if self.aims_objective_target is not None and not isinstance(self.aims_objective_target, str):
            self.aims_objective_target = str(self.aims_objective_target)

        if self.aims_objective_current_value is not None and not isinstance(self.aims_objective_current_value, str):
            self.aims_objective_current_value = str(self.aims_objective_current_value)

        if self.aims_objective_metric is not None and not isinstance(self.aims_objective_metric, str):
            self.aims_objective_metric = str(self.aims_objective_metric)

        if self.aims_objective_measurement_method is not None and not isinstance(self.aims_objective_measurement_method, str):
            self.aims_objective_measurement_method = str(self.aims_objective_measurement_method)

        if self.aims_objective_measurement_frequency is not None and not isinstance(self.aims_objective_measurement_frequency, str):
            self.aims_objective_measurement_frequency = str(self.aims_objective_measurement_frequency)

        if self.aims_objective_target_date is not None and not isinstance(self.aims_objective_target_date, XSDDate):
            self.aims_objective_target_date = XSDDate(self.aims_objective_target_date)

        if self.aims_objective_achievement is not None and not isinstance(self.aims_objective_achievement, str):
            self.aims_objective_achievement = str(self.aims_objective_achievement)

        if not isinstance(self.aims_objective_risks, list):
            self.aims_objective_risks = [self.aims_objective_risks] if self.aims_objective_risks is not None else []
        self.aims_objective_risks = [v if isinstance(v, AimsRiskAimsId) else AimsRiskAimsId(v) for v in self.aims_objective_risks]

        if self.aims_objective_action_plan is not None and not isinstance(self.aims_objective_action_plan, str):
            self.aims_objective_action_plan = str(self.aims_objective_action_plan)

        if self.aims_objective_resources is not None and not isinstance(self.aims_objective_resources, str):
            self.aims_objective_resources = str(self.aims_objective_resources)

        if self.aims_objective_evaluation is not None and not isinstance(self.aims_objective_evaluation, str):
            self.aims_objective_evaluation = str(self.aims_objective_evaluation)

        if self.aims_objective_communication is not None and not isinstance(self.aims_objective_communication, str):
            self.aims_objective_communication = str(self.aims_objective_communication)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsPlannedAction(YAMLRoot):
    """
    An action planned on a risk or an opportunity the system faces, with how it fits the system's processes and how
    its effect will be judged.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsPlannedAction"]
    class_class_curie: ClassVar[str] = "iso42001:AimsPlannedAction"
    class_name: ClassVar[str] = "AimsPlannedAction"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsPlannedAction

    aims_id: Union[str, AimsPlannedActionAimsId] = None
    title: str = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_planned_action_risks: Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]] = empty_list()
    aims_planned_action_opportunities: Optional[Union[str, list[str]]] = empty_list()
    aims_planned_action_integration: Optional[str] = None
    aims_planned_action_effectiveness: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsPlannedActionAimsId):
            self.aims_id = AimsPlannedActionAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_planned_action_risks, list):
            self.aims_planned_action_risks = [self.aims_planned_action_risks] if self.aims_planned_action_risks is not None else []
        self.aims_planned_action_risks = [v if isinstance(v, AimsRiskAimsId) else AimsRiskAimsId(v) for v in self.aims_planned_action_risks]

        if not isinstance(self.aims_planned_action_opportunities, list):
            self.aims_planned_action_opportunities = [self.aims_planned_action_opportunities] if self.aims_planned_action_opportunities is not None else []
        self.aims_planned_action_opportunities = [v if isinstance(v, str) else str(v) for v in self.aims_planned_action_opportunities]

        if self.aims_planned_action_integration is not None and not isinstance(self.aims_planned_action_integration, str):
            self.aims_planned_action_integration = str(self.aims_planned_action_integration)

        if self.aims_planned_action_effectiveness is not None and not isinstance(self.aims_planned_action_effectiveness, str):
            self.aims_planned_action_effectiveness = str(self.aims_planned_action_effectiveness)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsRiskAssessmentProcess(YAMLRoot):
    """
    The organization's process for assessing AI risks: its criteria, scales and method, and when it runs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRiskAssessmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRiskAssessmentProcess"
    class_name: ClassVar[str] = "AimsRiskAssessmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRiskAssessmentProcess

    aims_id: Union[str, AimsRiskAssessmentProcessAimsId] = None
    title: str = None
    aims_risk_criteria: Optional[Union[str, list[str]]] = empty_list()
    aims_risk_policy_alignment: Optional[str] = None
    aims_risk_comparability: Optional[str] = None
    aims_risk_method: Optional[str] = None
    aims_risk_likelihood_scale: Optional[str] = None
    aims_risk_consequence_scale: Optional[str] = None
    aims_risk_matrix: Optional[str] = None
    aims_risk_prioritization: Optional[str] = None
    aims_risk_assessment_interval: Optional[Union[str, AimsDuration]] = None
    aims_risk_assessment_triggers: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRiskAssessmentProcessAimsId):
            self.aims_id = AimsRiskAssessmentProcessAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_risk_criteria, list):
            self.aims_risk_criteria = [self.aims_risk_criteria] if self.aims_risk_criteria is not None else []
        self.aims_risk_criteria = [v if isinstance(v, str) else str(v) for v in self.aims_risk_criteria]

        if self.aims_risk_policy_alignment is not None and not isinstance(self.aims_risk_policy_alignment, str):
            self.aims_risk_policy_alignment = str(self.aims_risk_policy_alignment)

        if self.aims_risk_comparability is not None and not isinstance(self.aims_risk_comparability, str):
            self.aims_risk_comparability = str(self.aims_risk_comparability)

        if self.aims_risk_method is not None and not isinstance(self.aims_risk_method, str):
            self.aims_risk_method = str(self.aims_risk_method)

        if self.aims_risk_likelihood_scale is not None and not isinstance(self.aims_risk_likelihood_scale, str):
            self.aims_risk_likelihood_scale = str(self.aims_risk_likelihood_scale)

        if self.aims_risk_consequence_scale is not None and not isinstance(self.aims_risk_consequence_scale, str):
            self.aims_risk_consequence_scale = str(self.aims_risk_consequence_scale)

        if self.aims_risk_matrix is not None and not isinstance(self.aims_risk_matrix, str):
            self.aims_risk_matrix = str(self.aims_risk_matrix)

        if self.aims_risk_prioritization is not None and not isinstance(self.aims_risk_prioritization, str):
            self.aims_risk_prioritization = str(self.aims_risk_prioritization)

        if self.aims_risk_assessment_interval is not None and not isinstance(self.aims_risk_assessment_interval, AimsDuration):
            self.aims_risk_assessment_interval = AimsDuration(self.aims_risk_assessment_interval)

        if not isinstance(self.aims_risk_assessment_triggers, list):
            self.aims_risk_assessment_triggers = [self.aims_risk_assessment_triggers] if self.aims_risk_assessment_triggers is not None else []
        self.aims_risk_assessment_triggers = [v if isinstance(v, str) else str(v) for v in self.aims_risk_assessment_triggers]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsRiskAssessment(YAMLRoot):
    """
    One risk assessment carried out under the process, and what it found.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRiskAssessment"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRiskAssessment"
    class_name: ClassVar[str] = "AimsRiskAssessment"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRiskAssessment

    aims_id: Union[str, AimsRiskAssessmentAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_assessment_scope: Optional[str] = None
    aims_assessment_date: Optional[Union[str, XSDDate]] = None
    aims_assessment_assessor: Optional[str] = None
    aims_assessment_method_used: Optional[str] = None
    aims_assessment_risks: Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]] = empty_list()
    aims_assessment_impact_assessments: Optional[Union[Union[str, AimsImpactAssessmentAimsId], list[Union[str, AimsImpactAssessmentAimsId]]]] = empty_list()
    aims_assessment_summary: Optional[str] = None
    aims_assessment_recommendations: Optional[Union[str, list[str]]] = empty_list()
    aims_assessment_next_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRiskAssessmentAimsId):
            self.aims_id = AimsRiskAssessmentAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if self.aims_assessment_scope is not None and not isinstance(self.aims_assessment_scope, str):
            self.aims_assessment_scope = str(self.aims_assessment_scope)

        if self.aims_assessment_date is not None and not isinstance(self.aims_assessment_date, XSDDate):
            self.aims_assessment_date = XSDDate(self.aims_assessment_date)

        if self.aims_assessment_assessor is not None and not isinstance(self.aims_assessment_assessor, str):
            self.aims_assessment_assessor = str(self.aims_assessment_assessor)

        if self.aims_assessment_method_used is not None and not isinstance(self.aims_assessment_method_used, str):
            self.aims_assessment_method_used = str(self.aims_assessment_method_used)

        if not isinstance(self.aims_assessment_risks, list):
            self.aims_assessment_risks = [self.aims_assessment_risks] if self.aims_assessment_risks is not None else []
        self.aims_assessment_risks = [v if isinstance(v, AimsRiskAimsId) else AimsRiskAimsId(v) for v in self.aims_assessment_risks]

        if not isinstance(self.aims_assessment_impact_assessments, list):
            self.aims_assessment_impact_assessments = [self.aims_assessment_impact_assessments] if self.aims_assessment_impact_assessments is not None else []
        self.aims_assessment_impact_assessments = [v if isinstance(v, AimsImpactAssessmentAimsId) else AimsImpactAssessmentAimsId(v) for v in self.aims_assessment_impact_assessments]

        if self.aims_assessment_summary is not None and not isinstance(self.aims_assessment_summary, str):
            self.aims_assessment_summary = str(self.aims_assessment_summary)

        if not isinstance(self.aims_assessment_recommendations, list):
            self.aims_assessment_recommendations = [self.aims_assessment_recommendations] if self.aims_assessment_recommendations is not None else []
        self.aims_assessment_recommendations = [v if isinstance(v, str) else str(v) for v in self.aims_assessment_recommendations]

        if self.aims_assessment_next_date is not None and not isinstance(self.aims_assessment_next_date, XSDDate):
            self.aims_assessment_next_date = XSDDate(self.aims_assessment_next_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsRisk(YAMLRoot):
    """
    An AI risk in the risk register: where it comes from, which objectives it helps or hinders, who could feel its
    consequences, how it is rated and how it is treated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRisk"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRisk"
    class_name: ClassVar[str] = "AimsRisk"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRisk

    aims_id: Union[str, AimsRiskAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_risk_source_categories: Optional[Union[Union[str, "AimsRiskSourceCategory"], list[Union[str, "AimsRiskSourceCategory"]]]] = empty_list()
    aims_risk_source: Optional[str] = None
    aims_risk_objectives: Optional[Union[Union[str, AimsObjectiveAimsId], list[Union[str, AimsObjectiveAimsId]]]] = empty_list()
    aims_risk_consequences_for_organization: Optional[str] = None
    aims_risk_consequences_for_individuals: Optional[str] = None
    aims_risk_consequences_for_societies: Optional[str] = None
    aims_risk_owner: Optional[str] = None
    aims_risk_likelihood: Optional[Union[str, "AimsLikelihood"]] = None
    aims_risk_consequence: Optional[Union[str, "AimsConsequence"]] = None
    aims_risk_inherent_level: Optional[Union[str, "AimsRiskLevel"]] = None
    aims_risk_existing_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_risk_residual_level: Optional[Union[str, "AimsRiskLevel"]] = None
    aims_risk_acceptable: Optional[Union[bool, Bool]] = None
    aims_risk_treatment_option: Optional[Union[str, "AimsRiskTreatmentOption"]] = None
    aims_risk_treatment_priority: Optional[str] = None
    aims_risk_impact_assessments: Optional[Union[Union[str, AimsImpactAssessmentAimsId], list[Union[str, AimsImpactAssessmentAimsId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRiskAimsId):
            self.aims_id = AimsRiskAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_risk_source_categories, list):
            self.aims_risk_source_categories = [self.aims_risk_source_categories] if self.aims_risk_source_categories is not None else []
        self.aims_risk_source_categories = [v if isinstance(v, AimsRiskSourceCategory) else AimsRiskSourceCategory(v) for v in self.aims_risk_source_categories]

        if self.aims_risk_source is not None and not isinstance(self.aims_risk_source, str):
            self.aims_risk_source = str(self.aims_risk_source)

        if not isinstance(self.aims_risk_objectives, list):
            self.aims_risk_objectives = [self.aims_risk_objectives] if self.aims_risk_objectives is not None else []
        self.aims_risk_objectives = [v if isinstance(v, AimsObjectiveAimsId) else AimsObjectiveAimsId(v) for v in self.aims_risk_objectives]

        if self.aims_risk_consequences_for_organization is not None and not isinstance(self.aims_risk_consequences_for_organization, str):
            self.aims_risk_consequences_for_organization = str(self.aims_risk_consequences_for_organization)

        if self.aims_risk_consequences_for_individuals is not None and not isinstance(self.aims_risk_consequences_for_individuals, str):
            self.aims_risk_consequences_for_individuals = str(self.aims_risk_consequences_for_individuals)

        if self.aims_risk_consequences_for_societies is not None and not isinstance(self.aims_risk_consequences_for_societies, str):
            self.aims_risk_consequences_for_societies = str(self.aims_risk_consequences_for_societies)

        if self.aims_risk_owner is not None and not isinstance(self.aims_risk_owner, str):
            self.aims_risk_owner = str(self.aims_risk_owner)

        if self.aims_risk_likelihood is not None and not isinstance(self.aims_risk_likelihood, AimsLikelihood):
            self.aims_risk_likelihood = AimsLikelihood(self.aims_risk_likelihood)

        if self.aims_risk_consequence is not None and not isinstance(self.aims_risk_consequence, AimsConsequence):
            self.aims_risk_consequence = AimsConsequence(self.aims_risk_consequence)

        if self.aims_risk_inherent_level is not None and not isinstance(self.aims_risk_inherent_level, AimsRiskLevel):
            self.aims_risk_inherent_level = AimsRiskLevel(self.aims_risk_inherent_level)

        if not isinstance(self.aims_risk_existing_controls, list):
            self.aims_risk_existing_controls = [self.aims_risk_existing_controls] if self.aims_risk_existing_controls is not None else []
        self.aims_risk_existing_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_risk_existing_controls]

        if self.aims_risk_residual_level is not None and not isinstance(self.aims_risk_residual_level, AimsRiskLevel):
            self.aims_risk_residual_level = AimsRiskLevel(self.aims_risk_residual_level)

        if self.aims_risk_acceptable is not None and not isinstance(self.aims_risk_acceptable, Bool):
            self.aims_risk_acceptable = Bool(self.aims_risk_acceptable)

        if self.aims_risk_treatment_option is not None and not isinstance(self.aims_risk_treatment_option, AimsRiskTreatmentOption):
            self.aims_risk_treatment_option = AimsRiskTreatmentOption(self.aims_risk_treatment_option)

        if self.aims_risk_treatment_priority is not None and not isinstance(self.aims_risk_treatment_priority, str):
            self.aims_risk_treatment_priority = str(self.aims_risk_treatment_priority)

        if not isinstance(self.aims_risk_impact_assessments, list):
            self.aims_risk_impact_assessments = [self.aims_risk_impact_assessments] if self.aims_risk_impact_assessments is not None else []
        self.aims_risk_impact_assessments = [v if isinstance(v, AimsImpactAssessmentAimsId) else AimsImpactAssessmentAimsId(v) for v in self.aims_risk_impact_assessments]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsRiskTreatmentProcess(YAMLRoot):
    """
    The organization's process for treating AI risks: how it chooses options and controls, checks them against Annex A
    and produces the Statement of Applicability and the plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRiskTreatmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRiskTreatmentProcess"
    class_name: ClassVar[str] = "AimsRiskTreatmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRiskTreatmentProcess

    aims_id: Union[str, AimsRiskTreatmentProcessAimsId] = None
    title: str = None
    aims_treatment_options_guidance: Optional[str] = None
    aims_treatment_control_selection: Optional[str] = None
    aims_treatment_annex_a_comparison: Optional[str] = None
    aims_treatment_additional_controls: Optional[str] = None
    aims_treatment_annex_b_use: Optional[str] = None
    aims_treatment_soa_template: Optional[str] = None
    aims_treatment_approval_workflow: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRiskTreatmentProcessAimsId):
            self.aims_id = AimsRiskTreatmentProcessAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_treatment_options_guidance is not None and not isinstance(self.aims_treatment_options_guidance, str):
            self.aims_treatment_options_guidance = str(self.aims_treatment_options_guidance)

        if self.aims_treatment_control_selection is not None and not isinstance(self.aims_treatment_control_selection, str):
            self.aims_treatment_control_selection = str(self.aims_treatment_control_selection)

        if self.aims_treatment_annex_a_comparison is not None and not isinstance(self.aims_treatment_annex_a_comparison, str):
            self.aims_treatment_annex_a_comparison = str(self.aims_treatment_annex_a_comparison)

        if self.aims_treatment_additional_controls is not None and not isinstance(self.aims_treatment_additional_controls, str):
            self.aims_treatment_additional_controls = str(self.aims_treatment_additional_controls)

        if self.aims_treatment_annex_b_use is not None and not isinstance(self.aims_treatment_annex_b_use, str):
            self.aims_treatment_annex_b_use = str(self.aims_treatment_annex_b_use)

        if self.aims_treatment_soa_template is not None and not isinstance(self.aims_treatment_soa_template, str):
            self.aims_treatment_soa_template = str(self.aims_treatment_soa_template)

        if self.aims_treatment_approval_workflow is not None and not isinstance(self.aims_treatment_approval_workflow, str):
            self.aims_treatment_approval_workflow = str(self.aims_treatment_approval_workflow)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsRiskTreatmentPlan(YAMLRoot):
    """
    A plan to treat one or more risks: the actions and controls, who carries them out and when, and designated
    management's approval of the plan and of the risk left over.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsRiskTreatmentPlan"]
    class_class_curie: ClassVar[str] = "iso42001:AimsRiskTreatmentPlan"
    class_name: ClassVar[str] = "AimsRiskTreatmentPlan"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsRiskTreatmentPlan

    aims_id: Union[str, AimsRiskTreatmentPlanAimsId] = None
    title: str = None
    aims_implementation_state: Optional[Union[str, "AimsImplementationStatus"]] = None
    aims_plan_scope: Optional[str] = None
    aims_plan_risks: Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]] = empty_list()
    aims_plan_actions: Optional[Union[str, list[str]]] = empty_list()
    aims_plan_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_plan_resources: Optional[str] = None
    aims_plan_responsible_parties: Optional[Union[str, list[str]]] = empty_list()
    aims_plan_timeline: Optional[str] = None
    aims_plan_approver: Optional[str] = None
    aims_plan_residual_risk_acceptance: Optional[str] = None
    aims_plan_effectiveness: Optional[str] = None
    aims_plan_revalidation: Optional[str] = None
    aims_plan_completion_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsRiskTreatmentPlanAimsId):
            self.aims_id = AimsRiskTreatmentPlanAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_implementation_state is not None and not isinstance(self.aims_implementation_state, AimsImplementationStatus):
            self.aims_implementation_state = AimsImplementationStatus(self.aims_implementation_state)

        if self.aims_plan_scope is not None and not isinstance(self.aims_plan_scope, str):
            self.aims_plan_scope = str(self.aims_plan_scope)

        if not isinstance(self.aims_plan_risks, list):
            self.aims_plan_risks = [self.aims_plan_risks] if self.aims_plan_risks is not None else []
        self.aims_plan_risks = [v if isinstance(v, AimsRiskAimsId) else AimsRiskAimsId(v) for v in self.aims_plan_risks]

        if not isinstance(self.aims_plan_actions, list):
            self.aims_plan_actions = [self.aims_plan_actions] if self.aims_plan_actions is not None else []
        self.aims_plan_actions = [v if isinstance(v, str) else str(v) for v in self.aims_plan_actions]

        if not isinstance(self.aims_plan_controls, list):
            self.aims_plan_controls = [self.aims_plan_controls] if self.aims_plan_controls is not None else []
        self.aims_plan_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_plan_controls]

        if self.aims_plan_resources is not None and not isinstance(self.aims_plan_resources, str):
            self.aims_plan_resources = str(self.aims_plan_resources)

        if not isinstance(self.aims_plan_responsible_parties, list):
            self.aims_plan_responsible_parties = [self.aims_plan_responsible_parties] if self.aims_plan_responsible_parties is not None else []
        self.aims_plan_responsible_parties = [v if isinstance(v, str) else str(v) for v in self.aims_plan_responsible_parties]

        if self.aims_plan_timeline is not None and not isinstance(self.aims_plan_timeline, str):
            self.aims_plan_timeline = str(self.aims_plan_timeline)

        if self.aims_plan_approver is not None and not isinstance(self.aims_plan_approver, str):
            self.aims_plan_approver = str(self.aims_plan_approver)

        if self.aims_plan_residual_risk_acceptance is not None and not isinstance(self.aims_plan_residual_risk_acceptance, str):
            self.aims_plan_residual_risk_acceptance = str(self.aims_plan_residual_risk_acceptance)

        if self.aims_plan_effectiveness is not None and not isinstance(self.aims_plan_effectiveness, str):
            self.aims_plan_effectiveness = str(self.aims_plan_effectiveness)

        if self.aims_plan_revalidation is not None and not isinstance(self.aims_plan_revalidation, str):
            self.aims_plan_revalidation = str(self.aims_plan_revalidation)

        if self.aims_plan_completion_date is not None and not isinstance(self.aims_plan_completion_date, XSDDate):
            self.aims_plan_completion_date = XSDDate(self.aims_plan_completion_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsImpactAssessmentProcess(YAMLRoot):
    """
    The process for working out what AI systems may do to people and society: when it applies, what it takes in, who
    runs it and how the results are used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsImpactAssessmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AimsImpactAssessmentProcess"
    class_name: ClassVar[str] = "AimsImpactAssessmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsImpactAssessmentProcess

    aims_id: Union[str, AimsImpactAssessmentProcessAimsId] = None
    title: str = None
    aims_impact_process_triggers: Optional[Union[str, list[str]]] = empty_list()
    aims_impact_process_interval: Optional[Union[str, AimsDuration]] = None
    aims_impact_process_steps: Optional[Union[str, list[str]]] = empty_list()
    aims_impact_process_assessors: Optional[str] = None
    aims_impact_process_use: Optional[str] = None
    aims_impact_process_subjects: Optional[Union[Union[str, "AimsImpactSubject"], list[Union[str, "AimsImpactSubject"]]]] = empty_list()
    aims_impact_process_areas: Optional[Union[Union[str, "AimsImpactArea"], list[Union[str, "AimsImpactArea"]]]] = empty_list()
    aims_impact_process_retention: Optional[Union[str, AimsDuration]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsImpactAssessmentProcessAimsId):
            self.aims_id = AimsImpactAssessmentProcessAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_impact_process_triggers, list):
            self.aims_impact_process_triggers = [self.aims_impact_process_triggers] if self.aims_impact_process_triggers is not None else []
        self.aims_impact_process_triggers = [v if isinstance(v, str) else str(v) for v in self.aims_impact_process_triggers]

        if self.aims_impact_process_interval is not None and not isinstance(self.aims_impact_process_interval, AimsDuration):
            self.aims_impact_process_interval = AimsDuration(self.aims_impact_process_interval)

        if not isinstance(self.aims_impact_process_steps, list):
            self.aims_impact_process_steps = [self.aims_impact_process_steps] if self.aims_impact_process_steps is not None else []
        self.aims_impact_process_steps = [v if isinstance(v, str) else str(v) for v in self.aims_impact_process_steps]

        if self.aims_impact_process_assessors is not None and not isinstance(self.aims_impact_process_assessors, str):
            self.aims_impact_process_assessors = str(self.aims_impact_process_assessors)

        if self.aims_impact_process_use is not None and not isinstance(self.aims_impact_process_use, str):
            self.aims_impact_process_use = str(self.aims_impact_process_use)

        if not isinstance(self.aims_impact_process_subjects, list):
            self.aims_impact_process_subjects = [self.aims_impact_process_subjects] if self.aims_impact_process_subjects is not None else []
        self.aims_impact_process_subjects = [v if isinstance(v, AimsImpactSubject) else AimsImpactSubject(v) for v in self.aims_impact_process_subjects]

        if not isinstance(self.aims_impact_process_areas, list):
            self.aims_impact_process_areas = [self.aims_impact_process_areas] if self.aims_impact_process_areas is not None else []
        self.aims_impact_process_areas = [v if isinstance(v, AimsImpactArea) else AimsImpactArea(v) for v in self.aims_impact_process_areas]

        if self.aims_impact_process_retention is not None and not isinstance(self.aims_impact_process_retention, AimsDuration):
            self.aims_impact_process_retention = AimsDuration(self.aims_impact_process_retention)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsImpactAssessment(YAMLRoot):
    """
    One impact assessment carried out under the process: the systems and the setting it looked at, and each impact it
    found.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsImpactAssessment"]
    class_class_curie: ClassVar[str] = "iso42001:AimsImpactAssessment"
    class_name: ClassVar[str] = "AimsImpactAssessment"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsImpactAssessment

    aims_id: Union[str, AimsImpactAssessmentAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_impact_scope: Optional[str] = None
    aims_impact_discipline: Optional[str] = None
    aims_impact_date: Optional[Union[str, XSDDate]] = None
    aims_impact_assessor: Optional[str] = None
    aims_impact_intended_use: Optional[str] = None
    aims_impact_foreseeable_misuse: Optional[str] = None
    aims_impact_technical_context: Optional[str] = None
    aims_impact_societal_context: Optional[str] = None
    aims_impact_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    aims_impact_demographic_groups: Optional[Union[str, list[str]]] = empty_list()
    aims_impact_system_complexity: Optional[str] = None
    aims_impact_human_role: Optional[str] = None
    aims_impact_failures: Optional[Union[str, list[str]]] = empty_list()
    aims_impact_workforce: Optional[str] = None
    aims_impact_findings: Optional[Union[Union[dict, "AimsIdentifiedImpact"], list[Union[dict, "AimsIdentifiedImpact"]]]] = empty_list()
    aims_impact_shared_with: Optional[Union[Union[str, AimsInterestedPartyAimsId], list[Union[str, AimsInterestedPartyAimsId]]]] = empty_list()
    aims_impact_next_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsImpactAssessmentAimsId):
            self.aims_id = AimsImpactAssessmentAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if self.aims_impact_scope is not None and not isinstance(self.aims_impact_scope, str):
            self.aims_impact_scope = str(self.aims_impact_scope)

        if self.aims_impact_discipline is not None and not isinstance(self.aims_impact_discipline, str):
            self.aims_impact_discipline = str(self.aims_impact_discipline)

        if self.aims_impact_date is not None and not isinstance(self.aims_impact_date, XSDDate):
            self.aims_impact_date = XSDDate(self.aims_impact_date)

        if self.aims_impact_assessor is not None and not isinstance(self.aims_impact_assessor, str):
            self.aims_impact_assessor = str(self.aims_impact_assessor)

        if self.aims_impact_intended_use is not None and not isinstance(self.aims_impact_intended_use, str):
            self.aims_impact_intended_use = str(self.aims_impact_intended_use)

        if self.aims_impact_foreseeable_misuse is not None and not isinstance(self.aims_impact_foreseeable_misuse, str):
            self.aims_impact_foreseeable_misuse = str(self.aims_impact_foreseeable_misuse)

        if self.aims_impact_technical_context is not None and not isinstance(self.aims_impact_technical_context, str):
            self.aims_impact_technical_context = str(self.aims_impact_technical_context)

        if self.aims_impact_societal_context is not None and not isinstance(self.aims_impact_societal_context, str):
            self.aims_impact_societal_context = str(self.aims_impact_societal_context)

        if not isinstance(self.aims_impact_jurisdictions, list):
            self.aims_impact_jurisdictions = [self.aims_impact_jurisdictions] if self.aims_impact_jurisdictions is not None else []
        self.aims_impact_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.aims_impact_jurisdictions]

        if not isinstance(self.aims_impact_demographic_groups, list):
            self.aims_impact_demographic_groups = [self.aims_impact_demographic_groups] if self.aims_impact_demographic_groups is not None else []
        self.aims_impact_demographic_groups = [v if isinstance(v, str) else str(v) for v in self.aims_impact_demographic_groups]

        if self.aims_impact_system_complexity is not None and not isinstance(self.aims_impact_system_complexity, str):
            self.aims_impact_system_complexity = str(self.aims_impact_system_complexity)

        if self.aims_impact_human_role is not None and not isinstance(self.aims_impact_human_role, str):
            self.aims_impact_human_role = str(self.aims_impact_human_role)

        if not isinstance(self.aims_impact_failures, list):
            self.aims_impact_failures = [self.aims_impact_failures] if self.aims_impact_failures is not None else []
        self.aims_impact_failures = [v if isinstance(v, str) else str(v) for v in self.aims_impact_failures]

        if self.aims_impact_workforce is not None and not isinstance(self.aims_impact_workforce, str):
            self.aims_impact_workforce = str(self.aims_impact_workforce)

        self._normalize_inlined_as_list(slot_name="aims_impact_findings", slot_type=AimsIdentifiedImpact, key_name="aims_identified_impact_subject", keyed=False)

        if not isinstance(self.aims_impact_shared_with, list):
            self.aims_impact_shared_with = [self.aims_impact_shared_with] if self.aims_impact_shared_with is not None else []
        self.aims_impact_shared_with = [v if isinstance(v, AimsInterestedPartyAimsId) else AimsInterestedPartyAimsId(v) for v in self.aims_impact_shared_with]

        if self.aims_impact_next_date is not None and not isinstance(self.aims_impact_next_date, XSDDate):
            self.aims_impact_next_date = XSDDate(self.aims_impact_next_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsIdentifiedImpact(YAMLRoot):
    """
    One impact an assessment found: on whom it falls, in what area, whether it helps or harms, and what limits the
    harm.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsIdentifiedImpact"]
    class_class_curie: ClassVar[str] = "iso42001:AimsIdentifiedImpact"
    class_name: ClassVar[str] = "AimsIdentifiedImpact"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsIdentifiedImpact

    aims_identified_impact_subject: Union[str, "AimsImpactSubject"] = None
    aims_identified_impact_text: str = None
    aims_identified_impact_area: Optional[Union[str, "AimsImpactArea"]] = None
    aims_identified_impact_direction: Optional[Union[str, "AimsImpactDirection"]] = None
    aims_identified_impact_mitigation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_identified_impact_subject):
            self.MissingRequiredField("aims_identified_impact_subject")
        if not isinstance(self.aims_identified_impact_subject, AimsImpactSubject):
            self.aims_identified_impact_subject = AimsImpactSubject(self.aims_identified_impact_subject)

        if self._is_empty(self.aims_identified_impact_text):
            self.MissingRequiredField("aims_identified_impact_text")
        if not isinstance(self.aims_identified_impact_text, str):
            self.aims_identified_impact_text = str(self.aims_identified_impact_text)

        if self.aims_identified_impact_area is not None and not isinstance(self.aims_identified_impact_area, AimsImpactArea):
            self.aims_identified_impact_area = AimsImpactArea(self.aims_identified_impact_area)

        if self.aims_identified_impact_direction is not None and not isinstance(self.aims_identified_impact_direction, AimsImpactDirection):
            self.aims_identified_impact_direction = AimsImpactDirection(self.aims_identified_impact_direction)

        if not isinstance(self.aims_identified_impact_mitigation, list):
            self.aims_identified_impact_mitigation = [self.aims_identified_impact_mitigation] if self.aims_identified_impact_mitigation is not None else []
        self.aims_identified_impact_mitigation = [v if isinstance(v, str) else str(v) for v in self.aims_identified_impact_mitigation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsStatementOfApplicability(YAMLRoot):
    """
    The Statement of Applicability: each control the organization needs, with why it is included and whether it is in
    place, and each control it leaves out, with why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsStatementOfApplicability"]
    class_class_curie: ClassVar[str] = "iso42001:AimsStatementOfApplicability"
    class_name: ClassVar[str] = "AimsStatementOfApplicability"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsStatementOfApplicability

    aims_id: Union[str, AimsStatementOfApplicabilityAimsId] = None
    title: str = None
    aims_soa_entries: Optional[Union[Union[dict, "AimsApplicabilityEntry"], list[Union[dict, "AimsApplicabilityEntry"]]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsStatementOfApplicabilityAimsId):
            self.aims_id = AimsStatementOfApplicabilityAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="aims_soa_entries", slot_type=AimsApplicabilityEntry, key_name="aims_entry_justification", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsApplicabilityEntry(YAMLRoot):
    """
    One entry of the Statement of Applicability, which either includes a control or leaves one out, and says why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsApplicabilityEntry"]
    class_class_curie: ClassVar[str] = "iso42001:AimsApplicabilityEntry"
    class_name: ClassVar[str] = "AimsApplicabilityEntry"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsApplicabilityEntry

    aims_entry_justification: str = None
    aims_entry_annex_a_control: Optional[Union[str, "AimsAnnexAControl"]] = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_entry_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_entry_justification):
            self.MissingRequiredField("aims_entry_justification")
        if not isinstance(self.aims_entry_justification, str):
            self.aims_entry_justification = str(self.aims_entry_justification)

        if self.aims_entry_annex_a_control is not None and not isinstance(self.aims_entry_annex_a_control, AimsAnnexAControl):
            self.aims_entry_annex_a_control = AimsAnnexAControl(self.aims_entry_annex_a_control)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        self.aims_entry_type = str(self.class_name)

        super().__post_init__(**kwargs)
        self.unknown_aims_entry_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "aims_entry_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AimsIncludedControl(AimsApplicabilityEntry):
    """
    An entry that includes a control the organization needs, from Annex A or from elsewhere, says which risks call for
    it and whether it is in place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsIncludedControl"]
    class_class_curie: ClassVar[str] = "iso42001:AimsIncludedControl"
    class_name: ClassVar[str] = "AimsIncludedControl"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsIncludedControl

    aims_entry_justification: str = None
    aims_implementation_state: Union[str, "AimsImplementationStatus"] = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_included_control: Optional[Union[str, AimsControlAimsId]] = None
    aims_included_risks: Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]] = empty_list()
    aims_included_evidence: Optional[str] = None
    aims_included_target_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_implementation_state):
            self.MissingRequiredField("aims_implementation_state")
        if not isinstance(self.aims_implementation_state, AimsImplementationStatus):
            self.aims_implementation_state = AimsImplementationStatus(self.aims_implementation_state)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if self.aims_included_control is not None and not isinstance(self.aims_included_control, AimsControlAimsId):
            self.aims_included_control = AimsControlAimsId(self.aims_included_control)

        if not isinstance(self.aims_included_risks, list):
            self.aims_included_risks = [self.aims_included_risks] if self.aims_included_risks is not None else []
        self.aims_included_risks = [v if isinstance(v, AimsRiskAimsId) else AimsRiskAimsId(v) for v in self.aims_included_risks]

        if self.aims_included_evidence is not None and not isinstance(self.aims_included_evidence, str):
            self.aims_included_evidence = str(self.aims_included_evidence)

        if self.aims_included_target_date is not None and not isinstance(self.aims_included_target_date, XSDDate):
            self.aims_included_target_date = XSDDate(self.aims_included_target_date)

        super().__post_init__(**kwargs)
        self.unknown_aims_entry_type = str(self.class_name)


@dataclass(repr=False)
class AimsExcludedControl(AimsApplicabilityEntry):
    """
    An entry that leaves out an Annex A control the organization does not need, and says why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsExcludedControl"]
    class_class_curie: ClassVar[str] = "iso42001:AimsExcludedControl"
    class_name: ClassVar[str] = "AimsExcludedControl"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsExcludedControl

    aims_entry_justification: str = None
    aims_entry_annex_a_control: Union[str, "AimsAnnexAControl"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_entry_annex_a_control):
            self.MissingRequiredField("aims_entry_annex_a_control")
        if not isinstance(self.aims_entry_annex_a_control, AimsAnnexAControl):
            self.aims_entry_annex_a_control = AimsAnnexAControl(self.aims_entry_annex_a_control)

        super().__post_init__(**kwargs)
        self.unknown_aims_entry_type = str(self.class_name)


@dataclass(repr=False)
class AimsControl(YAMLRoot):
    """
    A control the organization has found it needs to treat its risks: what it does in the organization's words, which
    Annex A controls it answers to, who owns it, how far it is in place and how well it works.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsControl"]
    class_class_curie: ClassVar[str] = "iso42001:AimsControl"
    class_name: ClassVar[str] = "AimsControl"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsControl

    aims_id: Union[str, AimsControlAimsId] = None
    title: str = None
    aims_relevant_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_implementation_state: Optional[Union[str, "AimsImplementationStatus"]] = None
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_objective_categories: Optional[Union[Union[str, "AimsObjectiveCategory"], list[Union[str, "AimsObjectiveCategory"]]]] = empty_list()
    aims_risk_source_categories: Optional[Union[Union[str, "AimsRiskSourceCategory"], list[Union[str, "AimsRiskSourceCategory"]]]] = empty_list()
    aims_control_area: Optional[Union[str, "AimsControlArea"]] = None
    aims_control_text: Optional[str] = None
    aims_control_guidance: Optional[str] = None
    aims_control_owner: Optional[str] = None
    aims_control_implementation_date: Optional[Union[str, XSDDate]] = None
    aims_control_effectiveness: Optional[str] = None
    aims_control_last_tested: Optional[Union[str, XSDDate]] = None
    aims_control_evidence: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsControlAimsId):
            self.aims_id = AimsControlAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_relevant_controls, list):
            self.aims_relevant_controls = [self.aims_relevant_controls] if self.aims_relevant_controls is not None else []
        self.aims_relevant_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_relevant_controls]

        if self.aims_implementation_state is not None and not isinstance(self.aims_implementation_state, AimsImplementationStatus):
            self.aims_implementation_state = AimsImplementationStatus(self.aims_implementation_state)

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_objective_categories, list):
            self.aims_objective_categories = [self.aims_objective_categories] if self.aims_objective_categories is not None else []
        self.aims_objective_categories = [v if isinstance(v, AimsObjectiveCategory) else AimsObjectiveCategory(v) for v in self.aims_objective_categories]

        if not isinstance(self.aims_risk_source_categories, list):
            self.aims_risk_source_categories = [self.aims_risk_source_categories] if self.aims_risk_source_categories is not None else []
        self.aims_risk_source_categories = [v if isinstance(v, AimsRiskSourceCategory) else AimsRiskSourceCategory(v) for v in self.aims_risk_source_categories]

        if self.aims_control_area is not None and not isinstance(self.aims_control_area, AimsControlArea):
            self.aims_control_area = AimsControlArea(self.aims_control_area)

        if self.aims_control_text is not None and not isinstance(self.aims_control_text, str):
            self.aims_control_text = str(self.aims_control_text)

        if self.aims_control_guidance is not None and not isinstance(self.aims_control_guidance, str):
            self.aims_control_guidance = str(self.aims_control_guidance)

        if self.aims_control_owner is not None and not isinstance(self.aims_control_owner, str):
            self.aims_control_owner = str(self.aims_control_owner)

        if self.aims_control_implementation_date is not None and not isinstance(self.aims_control_implementation_date, XSDDate):
            self.aims_control_implementation_date = XSDDate(self.aims_control_implementation_date)

        if self.aims_control_effectiveness is not None and not isinstance(self.aims_control_effectiveness, str):
            self.aims_control_effectiveness = str(self.aims_control_effectiveness)

        if self.aims_control_last_tested is not None and not isinstance(self.aims_control_last_tested, XSDDate):
            self.aims_control_last_tested = XSDDate(self.aims_control_last_tested)

        if not isinstance(self.aims_control_evidence, list):
            self.aims_control_evidence = [self.aims_control_evidence] if self.aims_control_evidence is not None else []
        self.aims_control_evidence = [v if isinstance(v, str) else str(v) for v in self.aims_control_evidence]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsAiSystem(YAMLRoot):
    """
    One AI system under the management system: what it is for, how it is built, run and overseen, what it draws on,
    and what is kept about it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsAiSystem"]
    class_class_curie: ClassVar[str] = "iso42001:AimsAiSystem"
    class_name: ClassVar[str] = "AimsAiSystem"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsAiSystem

    aims_id: Union[str, AimsAiSystemAimsId] = None
    title: str = None
    aims_relevant_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_system_intended_purpose: Optional[str] = None
    aims_system_intended_uses: Optional[Union[str, list[str]]] = empty_list()
    aims_system_foreseeable_misuse: Optional[Union[str, list[str]]] = empty_list()
    aims_system_domain: Optional[str] = None
    aims_system_deployment_context: Optional[str] = None
    aims_system_life_cycle_stage: Optional[Union[str, "AimsLifecycleStage"]] = None
    aims_system_organization_roles: Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]] = empty_list()
    aims_system_pii_roles: Optional[Union[Union[str, "AimsPiiRole"], list[Union[str, "AimsPiiRole"]]]] = empty_list()
    aims_system_rationale: Optional[str] = None
    aims_system_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_system_ml_approach: Optional[str] = None
    aims_system_model_types: Optional[Union[str, list[str]]] = empty_list()
    aims_system_continuous_learning: Optional[Union[bool, Bool]] = None
    aims_system_automation_level: Optional[str] = None
    aims_system_threats: Optional[Union[Union[str, "AimsAiThreat"], list[Union[str, "AimsAiThreat"]]]] = empty_list()
    aims_system_verification_measures: Optional[Union[str, list[str]]] = empty_list()
    aims_system_evaluation_criteria: Optional[Union[str, list[str]]] = empty_list()
    aims_system_release_criteria: Optional[Union[str, list[str]]] = empty_list()
    aims_system_deployment_plan: Optional[Union[str, AimsDocumentedInformationAimsId]] = None
    aims_system_operation_elements: Optional[Union[str, list[str]]] = empty_list()
    aims_system_performance_metrics: Optional[Union[str, list[str]]] = empty_list()
    aims_system_log_stages: Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]] = empty_list()
    aims_system_log_contents: Optional[Union[str, list[str]]] = empty_list()
    aims_system_log_retention: Optional[Union[str, AimsDuration]] = None
    aims_system_human_oversight_required: Optional[Union[bool, Bool]] = None
    aims_system_human_oversight: Optional[str] = None
    aims_system_human_oversight_stages: Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]] = empty_list()
    aims_system_resources_used: Optional[Union[Union[str, AimsSystemResourceAimsId], list[Union[str, AimsSystemResourceAimsId]]]] = empty_list()
    aims_system_technical_documents: Optional[Union[Union[str, AimsTechnicalDocumentationAimsId], list[Union[str, AimsTechnicalDocumentationAimsId]]]] = empty_list()
    aims_system_impact_assessments: Optional[Union[Union[str, AimsImpactAssessmentAimsId], list[Union[str, AimsImpactAssessmentAimsId]]]] = empty_list()
    aims_system_relationships: Optional[Union[Union[str, AimsThirdPartyRelationshipAimsId], list[Union[str, AimsThirdPartyRelationshipAimsId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsAiSystemAimsId):
            self.aims_id = AimsAiSystemAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_relevant_controls, list):
            self.aims_relevant_controls = [self.aims_relevant_controls] if self.aims_relevant_controls is not None else []
        self.aims_relevant_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_relevant_controls]

        if self.aims_system_intended_purpose is not None and not isinstance(self.aims_system_intended_purpose, str):
            self.aims_system_intended_purpose = str(self.aims_system_intended_purpose)

        if not isinstance(self.aims_system_intended_uses, list):
            self.aims_system_intended_uses = [self.aims_system_intended_uses] if self.aims_system_intended_uses is not None else []
        self.aims_system_intended_uses = [v if isinstance(v, str) else str(v) for v in self.aims_system_intended_uses]

        if not isinstance(self.aims_system_foreseeable_misuse, list):
            self.aims_system_foreseeable_misuse = [self.aims_system_foreseeable_misuse] if self.aims_system_foreseeable_misuse is not None else []
        self.aims_system_foreseeable_misuse = [v if isinstance(v, str) else str(v) for v in self.aims_system_foreseeable_misuse]

        if self.aims_system_domain is not None and not isinstance(self.aims_system_domain, str):
            self.aims_system_domain = str(self.aims_system_domain)

        if self.aims_system_deployment_context is not None and not isinstance(self.aims_system_deployment_context, str):
            self.aims_system_deployment_context = str(self.aims_system_deployment_context)

        if self.aims_system_life_cycle_stage is not None and not isinstance(self.aims_system_life_cycle_stage, AimsLifecycleStage):
            self.aims_system_life_cycle_stage = AimsLifecycleStage(self.aims_system_life_cycle_stage)

        if not isinstance(self.aims_system_organization_roles, list):
            self.aims_system_organization_roles = [self.aims_system_organization_roles] if self.aims_system_organization_roles is not None else []
        self.aims_system_organization_roles = [v if isinstance(v, AimsAiRole) else AimsAiRole(v) for v in self.aims_system_organization_roles]

        if not isinstance(self.aims_system_pii_roles, list):
            self.aims_system_pii_roles = [self.aims_system_pii_roles] if self.aims_system_pii_roles is not None else []
        self.aims_system_pii_roles = [v if isinstance(v, AimsPiiRole) else AimsPiiRole(v) for v in self.aims_system_pii_roles]

        if self.aims_system_rationale is not None and not isinstance(self.aims_system_rationale, str):
            self.aims_system_rationale = str(self.aims_system_rationale)

        if not isinstance(self.aims_system_requirements, list):
            self.aims_system_requirements = [self.aims_system_requirements] if self.aims_system_requirements is not None else []
        self.aims_system_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_system_requirements]

        if self.aims_system_ml_approach is not None and not isinstance(self.aims_system_ml_approach, str):
            self.aims_system_ml_approach = str(self.aims_system_ml_approach)

        if not isinstance(self.aims_system_model_types, list):
            self.aims_system_model_types = [self.aims_system_model_types] if self.aims_system_model_types is not None else []
        self.aims_system_model_types = [v if isinstance(v, str) else str(v) for v in self.aims_system_model_types]

        if self.aims_system_continuous_learning is not None and not isinstance(self.aims_system_continuous_learning, Bool):
            self.aims_system_continuous_learning = Bool(self.aims_system_continuous_learning)

        if self.aims_system_automation_level is not None and not isinstance(self.aims_system_automation_level, str):
            self.aims_system_automation_level = str(self.aims_system_automation_level)

        if not isinstance(self.aims_system_threats, list):
            self.aims_system_threats = [self.aims_system_threats] if self.aims_system_threats is not None else []
        self.aims_system_threats = [v if isinstance(v, AimsAiThreat) else AimsAiThreat(v) for v in self.aims_system_threats]

        if not isinstance(self.aims_system_verification_measures, list):
            self.aims_system_verification_measures = [self.aims_system_verification_measures] if self.aims_system_verification_measures is not None else []
        self.aims_system_verification_measures = [v if isinstance(v, str) else str(v) for v in self.aims_system_verification_measures]

        if not isinstance(self.aims_system_evaluation_criteria, list):
            self.aims_system_evaluation_criteria = [self.aims_system_evaluation_criteria] if self.aims_system_evaluation_criteria is not None else []
        self.aims_system_evaluation_criteria = [v if isinstance(v, str) else str(v) for v in self.aims_system_evaluation_criteria]

        if not isinstance(self.aims_system_release_criteria, list):
            self.aims_system_release_criteria = [self.aims_system_release_criteria] if self.aims_system_release_criteria is not None else []
        self.aims_system_release_criteria = [v if isinstance(v, str) else str(v) for v in self.aims_system_release_criteria]

        if self.aims_system_deployment_plan is not None and not isinstance(self.aims_system_deployment_plan, AimsDocumentedInformationAimsId):
            self.aims_system_deployment_plan = AimsDocumentedInformationAimsId(self.aims_system_deployment_plan)

        if not isinstance(self.aims_system_operation_elements, list):
            self.aims_system_operation_elements = [self.aims_system_operation_elements] if self.aims_system_operation_elements is not None else []
        self.aims_system_operation_elements = [v if isinstance(v, str) else str(v) for v in self.aims_system_operation_elements]

        if not isinstance(self.aims_system_performance_metrics, list):
            self.aims_system_performance_metrics = [self.aims_system_performance_metrics] if self.aims_system_performance_metrics is not None else []
        self.aims_system_performance_metrics = [v if isinstance(v, str) else str(v) for v in self.aims_system_performance_metrics]

        if not isinstance(self.aims_system_log_stages, list):
            self.aims_system_log_stages = [self.aims_system_log_stages] if self.aims_system_log_stages is not None else []
        self.aims_system_log_stages = [v if isinstance(v, AimsLifecycleStage) else AimsLifecycleStage(v) for v in self.aims_system_log_stages]

        if not isinstance(self.aims_system_log_contents, list):
            self.aims_system_log_contents = [self.aims_system_log_contents] if self.aims_system_log_contents is not None else []
        self.aims_system_log_contents = [v if isinstance(v, str) else str(v) for v in self.aims_system_log_contents]

        if self.aims_system_log_retention is not None and not isinstance(self.aims_system_log_retention, AimsDuration):
            self.aims_system_log_retention = AimsDuration(self.aims_system_log_retention)

        if self.aims_system_human_oversight_required is not None and not isinstance(self.aims_system_human_oversight_required, Bool):
            self.aims_system_human_oversight_required = Bool(self.aims_system_human_oversight_required)

        if self.aims_system_human_oversight is not None and not isinstance(self.aims_system_human_oversight, str):
            self.aims_system_human_oversight = str(self.aims_system_human_oversight)

        if not isinstance(self.aims_system_human_oversight_stages, list):
            self.aims_system_human_oversight_stages = [self.aims_system_human_oversight_stages] if self.aims_system_human_oversight_stages is not None else []
        self.aims_system_human_oversight_stages = [v if isinstance(v, AimsLifecycleStage) else AimsLifecycleStage(v) for v in self.aims_system_human_oversight_stages]

        if not isinstance(self.aims_system_resources_used, list):
            self.aims_system_resources_used = [self.aims_system_resources_used] if self.aims_system_resources_used is not None else []
        self.aims_system_resources_used = [v if isinstance(v, AimsSystemResourceAimsId) else AimsSystemResourceAimsId(v) for v in self.aims_system_resources_used]

        if not isinstance(self.aims_system_technical_documents, list):
            self.aims_system_technical_documents = [self.aims_system_technical_documents] if self.aims_system_technical_documents is not None else []
        self.aims_system_technical_documents = [v if isinstance(v, AimsTechnicalDocumentationAimsId) else AimsTechnicalDocumentationAimsId(v) for v in self.aims_system_technical_documents]

        if not isinstance(self.aims_system_impact_assessments, list):
            self.aims_system_impact_assessments = [self.aims_system_impact_assessments] if self.aims_system_impact_assessments is not None else []
        self.aims_system_impact_assessments = [v if isinstance(v, AimsImpactAssessmentAimsId) else AimsImpactAssessmentAimsId(v) for v in self.aims_system_impact_assessments]

        if not isinstance(self.aims_system_relationships, list):
            self.aims_system_relationships = [self.aims_system_relationships] if self.aims_system_relationships is not None else []
        self.aims_system_relationships = [v if isinstance(v, AimsThirdPartyRelationshipAimsId) else AimsThirdPartyRelationshipAimsId(v) for v in self.aims_system_relationships]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsSystemResource(YAMLRoot):
    """
    Something an AI system draws on, told apart by its type, with the stages of the system's life that need it and who
    provides it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsSystemResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsSystemResource"
    class_name: ClassVar[str] = "AimsSystemResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsSystemResource

    aims_id: Union[str, AimsSystemResourceAimsId] = None
    aims_resource_type: str = None
    title: str = None
    aims_life_cycle_stages: Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]] = empty_list()
    aims_resource_provider: Optional[Union[str, "AimsResourceProvider"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)

        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsSystemResourceAimsId):
            self.aims_id = AimsSystemResourceAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_life_cycle_stages, list):
            self.aims_life_cycle_stages = [self.aims_life_cycle_stages] if self.aims_life_cycle_stages is not None else []
        self.aims_life_cycle_stages = [v if isinstance(v, AimsLifecycleStage) else AimsLifecycleStage(v) for v in self.aims_life_cycle_stages]

        if self.aims_resource_provider is not None and not isinstance(self.aims_resource_provider, AimsResourceProvider):
            self.aims_resource_provider = AimsResourceProvider(self.aims_resource_provider)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "aims_resource_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AimsComponentResource(AimsSystemResource):
    """
    A part of a system, and how it is joined to the rest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsComponentResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsComponentResource"
    class_name: ClassVar[str] = "AimsComponentResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsComponentResource

    aims_id: Union[str, AimsComponentResourceAimsId] = None
    aims_resource_type: str = None
    title: str = None
    aims_component_kind: Optional[str] = None
    aims_component_integration: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsComponentResourceAimsId):
            self.aims_id = AimsComponentResourceAimsId(self.aims_id)

        if self.aims_component_kind is not None and not isinstance(self.aims_component_kind, str):
            self.aims_component_kind = str(self.aims_component_kind)

        if self.aims_component_integration is not None and not isinstance(self.aims_component_integration, str):
            self.aims_component_integration = str(self.aims_component_integration)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)


@dataclass(repr=False)
class AimsDataResource(AimsSystemResource):
    """
    Data an AI system draws on: where it came from, what part it plays, how it was obtained, made ready and judged
    fit, and how long it is kept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsDataResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsDataResource"
    class_name: ClassVar[str] = "AimsDataResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsDataResource

    aims_id: Union[str, AimsDataResourceAimsId] = None
    aims_resource_type: str = None
    title: str = None
    aims_data_categories: Optional[Union[Union[str, "AimsDataCategory"], list[Union[str, "AimsDataCategory"]]]] = empty_list()
    aims_data_kinds: Optional[Union[str, list[str]]] = empty_list()
    aims_data_intended_use: Optional[str] = None
    aims_data_quantity: Optional[str] = None
    aims_data_sources: Optional[Union[str, list[str]]] = empty_list()
    aims_data_source_characteristics: Optional[Union[str, list[str]]] = empty_list()
    aims_data_subject_demographics: Optional[Union[str, list[str]]] = empty_list()
    aims_data_prior_handling: Optional[str] = None
    aims_data_rights: Optional[Union[str, list[str]]] = empty_list()
    aims_data_metadata: Optional[Union[str, list[str]]] = empty_list()
    aims_data_provenance: Optional[str] = None
    aims_data_provenance_verification: Optional[str] = None
    aims_data_quality_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_data_quality_results: Optional[Union[str, list[str]]] = empty_list()
    aims_data_bias_issues: Optional[Union[str, list[str]]] = empty_list()
    aims_data_representativeness: Optional[str] = None
    aims_data_labelling_process: Optional[str] = None
    aims_data_preparation_criteria: Optional[str] = None
    aims_data_preparation_methods: Optional[Union[Union[str, "AimsDataPreparationMethod"], list[Union[str, "AimsDataPreparationMethod"]]]] = empty_list()
    aims_data_last_updated: Optional[Union[str, XSDDate]] = None
    aims_data_retention: Optional[str] = None
    aims_data_classification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsDataResourceAimsId):
            self.aims_id = AimsDataResourceAimsId(self.aims_id)

        if not isinstance(self.aims_data_categories, list):
            self.aims_data_categories = [self.aims_data_categories] if self.aims_data_categories is not None else []
        self.aims_data_categories = [v if isinstance(v, AimsDataCategory) else AimsDataCategory(v) for v in self.aims_data_categories]

        if not isinstance(self.aims_data_kinds, list):
            self.aims_data_kinds = [self.aims_data_kinds] if self.aims_data_kinds is not None else []
        self.aims_data_kinds = [v if isinstance(v, str) else str(v) for v in self.aims_data_kinds]

        if self.aims_data_intended_use is not None and not isinstance(self.aims_data_intended_use, str):
            self.aims_data_intended_use = str(self.aims_data_intended_use)

        if self.aims_data_quantity is not None and not isinstance(self.aims_data_quantity, str):
            self.aims_data_quantity = str(self.aims_data_quantity)

        if not isinstance(self.aims_data_sources, list):
            self.aims_data_sources = [self.aims_data_sources] if self.aims_data_sources is not None else []
        self.aims_data_sources = [v if isinstance(v, str) else str(v) for v in self.aims_data_sources]

        if not isinstance(self.aims_data_source_characteristics, list):
            self.aims_data_source_characteristics = [self.aims_data_source_characteristics] if self.aims_data_source_characteristics is not None else []
        self.aims_data_source_characteristics = [v if isinstance(v, str) else str(v) for v in self.aims_data_source_characteristics]

        if not isinstance(self.aims_data_subject_demographics, list):
            self.aims_data_subject_demographics = [self.aims_data_subject_demographics] if self.aims_data_subject_demographics is not None else []
        self.aims_data_subject_demographics = [v if isinstance(v, str) else str(v) for v in self.aims_data_subject_demographics]

        if self.aims_data_prior_handling is not None and not isinstance(self.aims_data_prior_handling, str):
            self.aims_data_prior_handling = str(self.aims_data_prior_handling)

        if not isinstance(self.aims_data_rights, list):
            self.aims_data_rights = [self.aims_data_rights] if self.aims_data_rights is not None else []
        self.aims_data_rights = [v if isinstance(v, str) else str(v) for v in self.aims_data_rights]

        if not isinstance(self.aims_data_metadata, list):
            self.aims_data_metadata = [self.aims_data_metadata] if self.aims_data_metadata is not None else []
        self.aims_data_metadata = [v if isinstance(v, str) else str(v) for v in self.aims_data_metadata]

        if self.aims_data_provenance is not None and not isinstance(self.aims_data_provenance, str):
            self.aims_data_provenance = str(self.aims_data_provenance)

        if self.aims_data_provenance_verification is not None and not isinstance(self.aims_data_provenance_verification, str):
            self.aims_data_provenance_verification = str(self.aims_data_provenance_verification)

        if not isinstance(self.aims_data_quality_requirements, list):
            self.aims_data_quality_requirements = [self.aims_data_quality_requirements] if self.aims_data_quality_requirements is not None else []
        self.aims_data_quality_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_data_quality_requirements]

        if not isinstance(self.aims_data_quality_results, list):
            self.aims_data_quality_results = [self.aims_data_quality_results] if self.aims_data_quality_results is not None else []
        self.aims_data_quality_results = [v if isinstance(v, str) else str(v) for v in self.aims_data_quality_results]

        if not isinstance(self.aims_data_bias_issues, list):
            self.aims_data_bias_issues = [self.aims_data_bias_issues] if self.aims_data_bias_issues is not None else []
        self.aims_data_bias_issues = [v if isinstance(v, str) else str(v) for v in self.aims_data_bias_issues]

        if self.aims_data_representativeness is not None and not isinstance(self.aims_data_representativeness, str):
            self.aims_data_representativeness = str(self.aims_data_representativeness)

        if self.aims_data_labelling_process is not None and not isinstance(self.aims_data_labelling_process, str):
            self.aims_data_labelling_process = str(self.aims_data_labelling_process)

        if self.aims_data_preparation_criteria is not None and not isinstance(self.aims_data_preparation_criteria, str):
            self.aims_data_preparation_criteria = str(self.aims_data_preparation_criteria)

        if not isinstance(self.aims_data_preparation_methods, list):
            self.aims_data_preparation_methods = [self.aims_data_preparation_methods] if self.aims_data_preparation_methods is not None else []
        self.aims_data_preparation_methods = [v if isinstance(v, AimsDataPreparationMethod) else AimsDataPreparationMethod(v) for v in self.aims_data_preparation_methods]

        if self.aims_data_last_updated is not None and not isinstance(self.aims_data_last_updated, XSDDate):
            self.aims_data_last_updated = XSDDate(self.aims_data_last_updated)

        if self.aims_data_retention is not None and not isinstance(self.aims_data_retention, str):
            self.aims_data_retention = str(self.aims_data_retention)

        if self.aims_data_classification is not None and not isinstance(self.aims_data_classification, str):
            self.aims_data_classification = str(self.aims_data_classification)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)


@dataclass(repr=False)
class AimsToolingResource(AimsSystemResource):
    """
    A tool an AI system draws on, such as an algorithm, a model or a development tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsToolingResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsToolingResource"
    class_name: ClassVar[str] = "AimsToolingResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsToolingResource

    aims_id: Union[str, AimsToolingResourceAimsId] = None
    aims_resource_type: str = None
    title: str = None
    aims_tool_category: Optional[str] = None
    aims_tool_version: Optional[str] = None
    aims_tool_vendor: Optional[str] = None
    aims_tool_licence: Optional[str] = None
    aims_tool_purpose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsToolingResourceAimsId):
            self.aims_id = AimsToolingResourceAimsId(self.aims_id)

        if self.aims_tool_category is not None and not isinstance(self.aims_tool_category, str):
            self.aims_tool_category = str(self.aims_tool_category)

        if self.aims_tool_version is not None and not isinstance(self.aims_tool_version, str):
            self.aims_tool_version = str(self.aims_tool_version)

        if self.aims_tool_vendor is not None and not isinstance(self.aims_tool_vendor, str):
            self.aims_tool_vendor = str(self.aims_tool_vendor)

        if self.aims_tool_licence is not None and not isinstance(self.aims_tool_licence, str):
            self.aims_tool_licence = str(self.aims_tool_licence)

        if self.aims_tool_purpose is not None and not isinstance(self.aims_tool_purpose, str):
            self.aims_tool_purpose = str(self.aims_tool_purpose)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)


@dataclass(repr=False)
class AimsComputingResource(AimsSystemResource):
    """
    Hardware or computing an AI system draws on: what it needs, where it runs and what the hardware costs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsComputingResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsComputingResource"
    class_name: ClassVar[str] = "AimsComputingResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsComputingResource

    aims_id: Union[str, AimsComputingResourceAimsId] = None
    aims_resource_type: str = None
    title: str = None
    aims_computing_requirements: Optional[str] = None
    aims_computing_location: Optional[str] = None
    aims_computing_processing: Optional[str] = None
    aims_computing_hardware_impact: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsComputingResourceAimsId):
            self.aims_id = AimsComputingResourceAimsId(self.aims_id)

        if self.aims_computing_requirements is not None and not isinstance(self.aims_computing_requirements, str):
            self.aims_computing_requirements = str(self.aims_computing_requirements)

        if self.aims_computing_location is not None and not isinstance(self.aims_computing_location, str):
            self.aims_computing_location = str(self.aims_computing_location)

        if self.aims_computing_processing is not None and not isinstance(self.aims_computing_processing, str):
            self.aims_computing_processing = str(self.aims_computing_processing)

        if self.aims_computing_hardware_impact is not None and not isinstance(self.aims_computing_hardware_impact, str):
            self.aims_computing_hardware_impact = str(self.aims_computing_hardware_impact)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)


@dataclass(repr=False)
class AimsHumanResource(AimsSystemResource):
    """
    People an AI system draws on: their skills and the work they do on it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsHumanResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsHumanResource"
    class_name: ClassVar[str] = "AimsHumanResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsHumanResource

    aims_id: Union[str, AimsHumanResourceAimsId] = None
    aims_resource_type: str = None
    title: str = None
    aims_human_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_human_competences: Optional[Union[str, list[str]]] = empty_list()
    aims_human_activities: Optional[Union[str, list[str]]] = empty_list()
    aims_human_diversity: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsHumanResourceAimsId):
            self.aims_id = AimsHumanResourceAimsId(self.aims_id)

        if self.aims_human_role is not None and not isinstance(self.aims_human_role, AimsRoleAimsId):
            self.aims_human_role = AimsRoleAimsId(self.aims_human_role)

        if not isinstance(self.aims_human_competences, list):
            self.aims_human_competences = [self.aims_human_competences] if self.aims_human_competences is not None else []
        self.aims_human_competences = [v if isinstance(v, str) else str(v) for v in self.aims_human_competences]

        if not isinstance(self.aims_human_activities, list):
            self.aims_human_activities = [self.aims_human_activities] if self.aims_human_activities is not None else []
        self.aims_human_activities = [v if isinstance(v, str) else str(v) for v in self.aims_human_activities]

        if self.aims_human_diversity is not None and not isinstance(self.aims_human_diversity, str):
            self.aims_human_diversity = str(self.aims_human_diversity)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aims_resource_type):
            self.MissingRequiredField("aims_resource_type")
        self.aims_resource_type = str(self.class_name)


@dataclass(repr=False)
class AimsDevelopmentProcess(YAMLRoot):
    """
    A process for designing and building an AI system responsibly: the life cycle it follows, and what it asks of
    testing, oversight, data and approvals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsDevelopmentProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AimsDevelopmentProcess"
    class_name: ClassVar[str] = "AimsDevelopmentProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsDevelopmentProcess

    aims_id: Union[str, AimsDevelopmentProcessAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_development_life_cycle_model: Optional[str] = None
    aims_development_testing: Optional[str] = None
    aims_development_human_oversight: Optional[str] = None
    aims_development_impact_assessment_stages: Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]] = empty_list()
    aims_development_training_data_rules: Optional[str] = None
    aims_development_expertise: Optional[str] = None
    aims_development_release_criteria: Optional[Union[str, list[str]]] = empty_list()
    aims_development_approvals: Optional[Union[str, list[str]]] = empty_list()
    aims_development_change_control: Optional[str] = None
    aims_development_usability: Optional[str] = None
    aims_development_party_engagement: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsDevelopmentProcessAimsId):
            self.aims_id = AimsDevelopmentProcessAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if self.aims_development_life_cycle_model is not None and not isinstance(self.aims_development_life_cycle_model, str):
            self.aims_development_life_cycle_model = str(self.aims_development_life_cycle_model)

        if self.aims_development_testing is not None and not isinstance(self.aims_development_testing, str):
            self.aims_development_testing = str(self.aims_development_testing)

        if self.aims_development_human_oversight is not None and not isinstance(self.aims_development_human_oversight, str):
            self.aims_development_human_oversight = str(self.aims_development_human_oversight)

        if not isinstance(self.aims_development_impact_assessment_stages, list):
            self.aims_development_impact_assessment_stages = [self.aims_development_impact_assessment_stages] if self.aims_development_impact_assessment_stages is not None else []
        self.aims_development_impact_assessment_stages = [v if isinstance(v, AimsLifecycleStage) else AimsLifecycleStage(v) for v in self.aims_development_impact_assessment_stages]

        if self.aims_development_training_data_rules is not None and not isinstance(self.aims_development_training_data_rules, str):
            self.aims_development_training_data_rules = str(self.aims_development_training_data_rules)

        if self.aims_development_expertise is not None and not isinstance(self.aims_development_expertise, str):
            self.aims_development_expertise = str(self.aims_development_expertise)

        if not isinstance(self.aims_development_release_criteria, list):
            self.aims_development_release_criteria = [self.aims_development_release_criteria] if self.aims_development_release_criteria is not None else []
        self.aims_development_release_criteria = [v if isinstance(v, str) else str(v) for v in self.aims_development_release_criteria]

        if not isinstance(self.aims_development_approvals, list):
            self.aims_development_approvals = [self.aims_development_approvals] if self.aims_development_approvals is not None else []
        self.aims_development_approvals = [v if isinstance(v, str) else str(v) for v in self.aims_development_approvals]

        if self.aims_development_change_control is not None and not isinstance(self.aims_development_change_control, str):
            self.aims_development_change_control = str(self.aims_development_change_control)

        if self.aims_development_usability is not None and not isinstance(self.aims_development_usability, str):
            self.aims_development_usability = str(self.aims_development_usability)

        if self.aims_development_party_engagement is not None and not isinstance(self.aims_development_party_engagement, str):
            self.aims_development_party_engagement = str(self.aims_development_party_engagement)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsResponsibleUseProcess(YAMLRoot):
    """
    A process for using AI systems responsibly: what decides if a system may be used, built in-house or brought in.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsResponsibleUseProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AimsResponsibleUseProcess"
    class_name: ClassVar[str] = "AimsResponsibleUseProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsResponsibleUseProcess

    aims_id: Union[str, AimsResponsibleUseProcessAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_use_approvals: Optional[Union[str, list[str]]] = empty_list()
    aims_use_costs: Optional[str] = None
    aims_use_sourcing_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_use_legal_requirements: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsResponsibleUseProcessAimsId):
            self.aims_id = AimsResponsibleUseProcessAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_use_approvals, list):
            self.aims_use_approvals = [self.aims_use_approvals] if self.aims_use_approvals is not None else []
        self.aims_use_approvals = [v if isinstance(v, str) else str(v) for v in self.aims_use_approvals]

        if self.aims_use_costs is not None and not isinstance(self.aims_use_costs, str):
            self.aims_use_costs = str(self.aims_use_costs)

        if not isinstance(self.aims_use_sourcing_requirements, list):
            self.aims_use_sourcing_requirements = [self.aims_use_sourcing_requirements] if self.aims_use_sourcing_requirements is not None else []
        self.aims_use_sourcing_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_use_sourcing_requirements]

        if not isinstance(self.aims_use_legal_requirements, list):
            self.aims_use_legal_requirements = [self.aims_use_legal_requirements] if self.aims_use_legal_requirements is not None else []
        self.aims_use_legal_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_use_legal_requirements]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsTechnicalDocumentation(YAMLRoot):
    """
    Technical documents about an AI system for one kind of reader: what they hold, and the form they take.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsTechnicalDocumentation"]
    class_class_curie: ClassVar[str] = "iso42001:AimsTechnicalDocumentation"
    class_name: ClassVar[str] = "AimsTechnicalDocumentation"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsTechnicalDocumentation

    aims_id: Union[str, AimsTechnicalDocumentationAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_technical_doc_audiences: Optional[Union[str, list[str]]] = empty_list()
    aims_technical_doc_form: Optional[str] = None
    aims_technical_doc_contents: Optional[Union[str, list[str]]] = empty_list()
    aims_technical_doc_failure_plan: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsTechnicalDocumentationAimsId):
            self.aims_id = AimsTechnicalDocumentationAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_technical_doc_audiences, list):
            self.aims_technical_doc_audiences = [self.aims_technical_doc_audiences] if self.aims_technical_doc_audiences is not None else []
        self.aims_technical_doc_audiences = [v if isinstance(v, str) else str(v) for v in self.aims_technical_doc_audiences]

        if self.aims_technical_doc_form is not None and not isinstance(self.aims_technical_doc_form, str):
            self.aims_technical_doc_form = str(self.aims_technical_doc_form)

        if not isinstance(self.aims_technical_doc_contents, list):
            self.aims_technical_doc_contents = [self.aims_technical_doc_contents] if self.aims_technical_doc_contents is not None else []
        self.aims_technical_doc_contents = [v if isinstance(v, str) else str(v) for v in self.aims_technical_doc_contents]

        if self.aims_technical_doc_failure_plan is not None and not isinstance(self.aims_technical_doc_failure_plan, str):
            self.aims_technical_doc_failure_plan = str(self.aims_technical_doc_failure_plan)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsUserInformation(YAMLRoot):
    """
    What those who use a system are told: the contents, how it reaches them, what decided it, and the check that they
    got it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsUserInformation"]
    class_class_curie: ClassVar[str] = "iso42001:AimsUserInformation"
    class_name: ClassVar[str] = "AimsUserInformation"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsUserInformation

    aims_id: Union[str, AimsUserInformationAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_user_information_contents: Optional[Union[str, list[str]]] = empty_list()
    aims_user_information_channels: Optional[Union[str, list[str]]] = empty_list()
    aims_user_information_criteria: Optional[Union[str, list[str]]] = empty_list()
    aims_user_information_validated: Optional[Union[bool, Bool]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsUserInformationAimsId):
            self.aims_id = AimsUserInformationAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_user_information_contents, list):
            self.aims_user_information_contents = [self.aims_user_information_contents] if self.aims_user_information_contents is not None else []
        self.aims_user_information_contents = [v if isinstance(v, str) else str(v) for v in self.aims_user_information_contents]

        if not isinstance(self.aims_user_information_channels, list):
            self.aims_user_information_channels = [self.aims_user_information_channels] if self.aims_user_information_channels is not None else []
        self.aims_user_information_channels = [v if isinstance(v, str) else str(v) for v in self.aims_user_information_channels]

        if not isinstance(self.aims_user_information_criteria, list):
            self.aims_user_information_criteria = [self.aims_user_information_criteria] if self.aims_user_information_criteria is not None else []
        self.aims_user_information_criteria = [v if isinstance(v, str) else str(v) for v in self.aims_user_information_criteria]

        if self.aims_user_information_validated is not None and not isinstance(self.aims_user_information_validated, Bool):
            self.aims_user_information_validated = Bool(self.aims_user_information_validated)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsIncidentCommunicationPlan(YAMLRoot):
    """
    The plan for telling users when a system goes wrong: which incidents, how soon, to which authorities, and with
    what details.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsIncidentCommunicationPlan"]
    class_class_curie: ClassVar[str] = "iso42001:AimsIncidentCommunicationPlan"
    class_name: ClassVar[str] = "AimsIncidentCommunicationPlan"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsIncidentCommunicationPlan

    aims_id: Union[str, AimsIncidentCommunicationPlanAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_incident_plan_categories: Optional[Union[Union[str, "AimsIncidentCategory"], list[Union[str, "AimsIncidentCategory"]]]] = empty_list()
    aims_incident_plan_timeline: Optional[str] = None
    aims_incident_plan_authorities: Optional[Union[str, list[str]]] = empty_list()
    aims_incident_plan_details: Optional[Union[str, list[str]]] = empty_list()
    aims_incident_plan_integration: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsIncidentCommunicationPlanAimsId):
            self.aims_id = AimsIncidentCommunicationPlanAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_incident_plan_categories, list):
            self.aims_incident_plan_categories = [self.aims_incident_plan_categories] if self.aims_incident_plan_categories is not None else []
        self.aims_incident_plan_categories = [v if isinstance(v, AimsIncidentCategory) else AimsIncidentCategory(v) for v in self.aims_incident_plan_categories]

        if self.aims_incident_plan_timeline is not None and not isinstance(self.aims_incident_plan_timeline, str):
            self.aims_incident_plan_timeline = str(self.aims_incident_plan_timeline)

        if not isinstance(self.aims_incident_plan_authorities, list):
            self.aims_incident_plan_authorities = [self.aims_incident_plan_authorities] if self.aims_incident_plan_authorities is not None else []
        self.aims_incident_plan_authorities = [v if isinstance(v, str) else str(v) for v in self.aims_incident_plan_authorities]

        if not isinstance(self.aims_incident_plan_details, list):
            self.aims_incident_plan_details = [self.aims_incident_plan_details] if self.aims_incident_plan_details is not None else []
        self.aims_incident_plan_details = [v if isinstance(v, str) else str(v) for v in self.aims_incident_plan_details]

        if self.aims_incident_plan_integration is not None and not isinstance(self.aims_incident_plan_integration, str):
            self.aims_incident_plan_integration = str(self.aims_incident_plan_integration)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsReportingObligation(YAMLRoot):
    """
    Something the organization must report about a system to an interested party: to whom, under what rule, what and
    how soon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsReportingObligation"]
    class_class_curie: ClassVar[str] = "iso42001:AimsReportingObligation"
    class_name: ClassVar[str] = "AimsReportingObligation"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsReportingObligation

    aims_id: Union[str, AimsReportingObligationAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_obligation_parties: Optional[Union[Union[str, AimsInterestedPartyAimsId], list[Union[str, AimsInterestedPartyAimsId]]]] = empty_list()
    aims_obligation_basis: Optional[str] = None
    aims_obligation_jurisdiction: Optional[str] = None
    aims_obligation_contents: Optional[Union[str, list[str]]] = empty_list()
    aims_obligation_timeframe: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsReportingObligationAimsId):
            self.aims_id = AimsReportingObligationAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_obligation_parties, list):
            self.aims_obligation_parties = [self.aims_obligation_parties] if self.aims_obligation_parties is not None else []
        self.aims_obligation_parties = [v if isinstance(v, AimsInterestedPartyAimsId) else AimsInterestedPartyAimsId(v) for v in self.aims_obligation_parties]

        if self.aims_obligation_basis is not None and not isinstance(self.aims_obligation_basis, str):
            self.aims_obligation_basis = str(self.aims_obligation_basis)

        if self.aims_obligation_jurisdiction is not None and not isinstance(self.aims_obligation_jurisdiction, str):
            self.aims_obligation_jurisdiction = str(self.aims_obligation_jurisdiction)

        if not isinstance(self.aims_obligation_contents, list):
            self.aims_obligation_contents = [self.aims_obligation_contents] if self.aims_obligation_contents is not None else []
        self.aims_obligation_contents = [v if isinstance(v, str) else str(v) for v in self.aims_obligation_contents]

        if self.aims_obligation_timeframe is not None and not isinstance(self.aims_obligation_timeframe, str):
            self.aims_obligation_timeframe = str(self.aims_obligation_timeframe)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsResource(YAMLRoot):
    """
    A resource provided for the management system itself, such as people, time, tools or budget. What an AI system
    draws on is an AimsSystemResource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsResource"]
    class_class_curie: ClassVar[str] = "iso42001:AimsResource"
    class_name: ClassVar[str] = "AimsResource"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsResource

    aims_id: Union[str, AimsResourceAimsId] = None
    title: str = None
    aims_support_category: Optional[str] = None
    aims_support_quantity: Optional[str] = None
    aims_support_allocation_date: Optional[Union[str, XSDDate]] = None
    aims_support_allocated_to: Optional[str] = None
    aims_support_cost: Optional[str] = None
    aims_support_availability: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsResourceAimsId):
            self.aims_id = AimsResourceAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_support_category is not None and not isinstance(self.aims_support_category, str):
            self.aims_support_category = str(self.aims_support_category)

        if self.aims_support_quantity is not None and not isinstance(self.aims_support_quantity, str):
            self.aims_support_quantity = str(self.aims_support_quantity)

        if self.aims_support_allocation_date is not None and not isinstance(self.aims_support_allocation_date, XSDDate):
            self.aims_support_allocation_date = XSDDate(self.aims_support_allocation_date)

        if self.aims_support_allocated_to is not None and not isinstance(self.aims_support_allocated_to, str):
            self.aims_support_allocated_to = str(self.aims_support_allocated_to)

        if self.aims_support_cost is not None and not isinstance(self.aims_support_cost, str):
            self.aims_support_cost = str(self.aims_support_cost)

        if self.aims_support_availability is not None and not isinstance(self.aims_support_availability, str):
            self.aims_support_availability = str(self.aims_support_availability)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsCompetenceRecord(YAMLRoot):
    """
    The evidence of one person's competence for work that affects AI performance, and what is done to close any gap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsCompetenceRecord"]
    class_class_curie: ClassVar[str] = "iso42001:AimsCompetenceRecord"
    class_name: ClassVar[str] = "AimsCompetenceRecord"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsCompetenceRecord

    aims_id: Union[str, AimsCompetenceRecordAimsId] = None
    title: str = None
    aims_competence_person: Optional[str] = None
    aims_competence_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_competence_required: Optional[Union[str, list[str]]] = empty_list()
    aims_competence_education: Optional[Union[str, list[str]]] = empty_list()
    aims_competence_training: Optional[Union[str, list[str]]] = empty_list()
    aims_competence_experience: Optional[Union[str, list[str]]] = empty_list()
    aims_competence_assessment_date: Optional[Union[str, XSDDate]] = None
    aims_competence_gaps: Optional[Union[str, list[str]]] = empty_list()
    aims_competence_actions: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsCompetenceRecordAimsId):
            self.aims_id = AimsCompetenceRecordAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_competence_person is not None and not isinstance(self.aims_competence_person, str):
            self.aims_competence_person = str(self.aims_competence_person)

        if self.aims_competence_role is not None and not isinstance(self.aims_competence_role, AimsRoleAimsId):
            self.aims_competence_role = AimsRoleAimsId(self.aims_competence_role)

        if not isinstance(self.aims_competence_required, list):
            self.aims_competence_required = [self.aims_competence_required] if self.aims_competence_required is not None else []
        self.aims_competence_required = [v if isinstance(v, str) else str(v) for v in self.aims_competence_required]

        if not isinstance(self.aims_competence_education, list):
            self.aims_competence_education = [self.aims_competence_education] if self.aims_competence_education is not None else []
        self.aims_competence_education = [v if isinstance(v, str) else str(v) for v in self.aims_competence_education]

        if not isinstance(self.aims_competence_training, list):
            self.aims_competence_training = [self.aims_competence_training] if self.aims_competence_training is not None else []
        self.aims_competence_training = [v if isinstance(v, str) else str(v) for v in self.aims_competence_training]

        if not isinstance(self.aims_competence_experience, list):
            self.aims_competence_experience = [self.aims_competence_experience] if self.aims_competence_experience is not None else []
        self.aims_competence_experience = [v if isinstance(v, str) else str(v) for v in self.aims_competence_experience]

        if self.aims_competence_assessment_date is not None and not isinstance(self.aims_competence_assessment_date, XSDDate):
            self.aims_competence_assessment_date = XSDDate(self.aims_competence_assessment_date)

        if not isinstance(self.aims_competence_gaps, list):
            self.aims_competence_gaps = [self.aims_competence_gaps] if self.aims_competence_gaps is not None else []
        self.aims_competence_gaps = [v if isinstance(v, str) else str(v) for v in self.aims_competence_gaps]

        if not isinstance(self.aims_competence_actions, list):
            self.aims_competence_actions = [self.aims_competence_actions] if self.aims_competence_actions is not None else []
        self.aims_competence_actions = [v if isinstance(v, str) else str(v) for v in self.aims_competence_actions]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsAwarenessProgramme(YAMLRoot):
    """
    The programme that tells people working for the organization about the AI policy, their part in the system and
    what failing it would mean.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsAwarenessProgramme"]
    class_class_curie: ClassVar[str] = "iso42001:AimsAwarenessProgramme"
    class_name: ClassVar[str] = "AimsAwarenessProgramme"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsAwarenessProgramme

    aims_id: Union[str, AimsAwarenessProgrammeAimsId] = None
    title: str = None
    aims_awareness_topics: Optional[Union[str, list[str]]] = empty_list()
    aims_awareness_methods: Optional[Union[str, list[str]]] = empty_list()
    aims_awareness_audience: Optional[str] = None
    aims_awareness_frequency: Optional[str] = None
    aims_awareness_completion_tracking: Optional[str] = None
    aims_awareness_effectiveness: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsAwarenessProgrammeAimsId):
            self.aims_id = AimsAwarenessProgrammeAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_awareness_topics, list):
            self.aims_awareness_topics = [self.aims_awareness_topics] if self.aims_awareness_topics is not None else []
        self.aims_awareness_topics = [v if isinstance(v, str) else str(v) for v in self.aims_awareness_topics]

        if not isinstance(self.aims_awareness_methods, list):
            self.aims_awareness_methods = [self.aims_awareness_methods] if self.aims_awareness_methods is not None else []
        self.aims_awareness_methods = [v if isinstance(v, str) else str(v) for v in self.aims_awareness_methods]

        if self.aims_awareness_audience is not None and not isinstance(self.aims_awareness_audience, str):
            self.aims_awareness_audience = str(self.aims_awareness_audience)

        if self.aims_awareness_frequency is not None and not isinstance(self.aims_awareness_frequency, str):
            self.aims_awareness_frequency = str(self.aims_awareness_frequency)

        if self.aims_awareness_completion_tracking is not None and not isinstance(self.aims_awareness_completion_tracking, str):
            self.aims_awareness_completion_tracking = str(self.aims_awareness_completion_tracking)

        if self.aims_awareness_effectiveness is not None and not isinstance(self.aims_awareness_effectiveness, str):
            self.aims_awareness_effectiveness = str(self.aims_awareness_effectiveness)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsCommunicationPlan(YAMLRoot):
    """
    The plan for communication about the system, inside the organization and outside it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsCommunicationPlan"]
    class_class_curie: ClassVar[str] = "iso42001:AimsCommunicationPlan"
    class_name: ClassVar[str] = "AimsCommunicationPlan"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsCommunicationPlan

    aims_id: Union[str, AimsCommunicationPlanAimsId] = None
    title: str = None
    aims_communication_items: Optional[Union[Union[dict, "AimsCommunication"], list[Union[dict, "AimsCommunication"]]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsCommunicationPlanAimsId):
            self.aims_id = AimsCommunicationPlanAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="aims_communication_items", slot_type=AimsCommunication, key_name="aims_communication_subject", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsCommunication(YAMLRoot):
    """
    One communication the plan provides for: what about, to whom, when, how, and who communicates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsCommunication"]
    class_class_curie: ClassVar[str] = "iso42001:AimsCommunication"
    class_name: ClassVar[str] = "AimsCommunication"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsCommunication

    aims_communication_subject: str = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_communication_purpose: Optional[str] = None
    aims_communication_audience: Optional[str] = None
    aims_communication_external: Optional[Union[bool, Bool]] = None
    aims_communication_timing: Optional[str] = None
    aims_communication_method: Optional[str] = None
    aims_communication_records_required: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_communication_subject):
            self.MissingRequiredField("aims_communication_subject")
        if not isinstance(self.aims_communication_subject, str):
            self.aims_communication_subject = str(self.aims_communication_subject)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if self.aims_communication_purpose is not None and not isinstance(self.aims_communication_purpose, str):
            self.aims_communication_purpose = str(self.aims_communication_purpose)

        if self.aims_communication_audience is not None and not isinstance(self.aims_communication_audience, str):
            self.aims_communication_audience = str(self.aims_communication_audience)

        if self.aims_communication_external is not None and not isinstance(self.aims_communication_external, Bool):
            self.aims_communication_external = Bool(self.aims_communication_external)

        if self.aims_communication_timing is not None and not isinstance(self.aims_communication_timing, str):
            self.aims_communication_timing = str(self.aims_communication_timing)

        if self.aims_communication_method is not None and not isinstance(self.aims_communication_method, str):
            self.aims_communication_method = str(self.aims_communication_method)

        if self.aims_communication_records_required is not None and not isinstance(self.aims_communication_records_required, Bool):
            self.aims_communication_records_required = Bool(self.aims_communication_records_required)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsDocumentedInformation(YAMLRoot):
    """
    A document or record the system keeps under control that no more specific record describes, such as a procedure, a
    plan or a report.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsDocumentedInformation"]
    class_class_curie: ClassVar[str] = "iso42001:AimsDocumentedInformation"
    class_name: ClassVar[str] = "AimsDocumentedInformation"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsDocumentedInformation

    aims_id: Union[str, AimsDocumentedInformationAimsId] = None
    aims_document_kind: Union[str, "AimsDocumentKind"] = None
    title: str = None
    aims_cited_clauses: Optional[Union[Union[str, "AimsClause"], list[Union[str, "AimsClause"]]]] = empty_list()
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsDocumentedInformationAimsId):
            self.aims_id = AimsDocumentedInformationAimsId(self.aims_id)

        if self._is_empty(self.aims_document_kind):
            self.MissingRequiredField("aims_document_kind")
        if not isinstance(self.aims_document_kind, AimsDocumentKind):
            self.aims_document_kind = AimsDocumentKind(self.aims_document_kind)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_cited_clauses, list):
            self.aims_cited_clauses = [self.aims_cited_clauses] if self.aims_cited_clauses is not None else []
        self.aims_cited_clauses = [v if isinstance(v, AimsClause) else AimsClause(v) for v in self.aims_cited_clauses]

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsOperationalProcedure(YAMLRoot):
    """
    A procedure by which the organization plans and controls the processes that meet its requirements, such as
    managing data for building or vetting suppliers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsOperationalProcedure"]
    class_class_curie: ClassVar[str] = "iso42001:AimsOperationalProcedure"
    class_name: ClassVar[str] = "AimsOperationalProcedure"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsOperationalProcedure

    aims_id: Union[str, AimsOperationalProcedureAimsId] = None
    title: str = None
    aims_relevant_controls: Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]] = empty_list()
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    aims_procedure_scope: Optional[str] = None
    aims_procedure_criteria: Optional[str] = None
    aims_procedure_control_measures: Optional[Union[str, list[str]]] = empty_list()
    aims_procedure_roles: Optional[Union[Union[str, AimsRoleAimsId], list[Union[str, AimsRoleAimsId]]]] = empty_list()
    aims_procedure_change_control: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsOperationalProcedureAimsId):
            self.aims_id = AimsOperationalProcedureAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_relevant_controls, list):
            self.aims_relevant_controls = [self.aims_relevant_controls] if self.aims_relevant_controls is not None else []
        self.aims_relevant_controls = [v if isinstance(v, AimsControlAimsId) else AimsControlAimsId(v) for v in self.aims_relevant_controls]

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if self.aims_procedure_scope is not None and not isinstance(self.aims_procedure_scope, str):
            self.aims_procedure_scope = str(self.aims_procedure_scope)

        if self.aims_procedure_criteria is not None and not isinstance(self.aims_procedure_criteria, str):
            self.aims_procedure_criteria = str(self.aims_procedure_criteria)

        if not isinstance(self.aims_procedure_control_measures, list):
            self.aims_procedure_control_measures = [self.aims_procedure_control_measures] if self.aims_procedure_control_measures is not None else []
        self.aims_procedure_control_measures = [v if isinstance(v, str) else str(v) for v in self.aims_procedure_control_measures]

        if not isinstance(self.aims_procedure_roles, list):
            self.aims_procedure_roles = [self.aims_procedure_roles] if self.aims_procedure_roles is not None else []
        self.aims_procedure_roles = [v if isinstance(v, AimsRoleAimsId) else AimsRoleAimsId(v) for v in self.aims_procedure_roles]

        if self.aims_procedure_change_control is not None and not isinstance(self.aims_procedure_change_control, str):
            self.aims_procedure_change_control = str(self.aims_procedure_change_control)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsMonitoringProgramme(YAMLRoot):
    """
    The programme that watches, measures, analyses and judges how well the system does and how well it works.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsMonitoringProgramme"]
    class_class_curie: ClassVar[str] = "iso42001:AimsMonitoringProgramme"
    class_name: ClassVar[str] = "AimsMonitoringProgramme"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsMonitoringProgramme

    aims_id: Union[str, AimsMonitoringProgrammeAimsId] = None
    title: str = None
    aims_monitoring_items: Optional[Union[Union[dict, "AimsMonitoringItem"], list[Union[dict, "AimsMonitoringItem"]]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsMonitoringProgrammeAimsId):
            self.aims_id = AimsMonitoringProgrammeAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="aims_monitoring_items", slot_type=AimsMonitoringItem, key_name="aims_monitoring_metric", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsMonitoringItem(YAMLRoot):
    """
    One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and
    against what thresholds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsMonitoringItem"]
    class_class_curie: ClassVar[str] = "iso42001:AimsMonitoringItem"
    class_name: ClassVar[str] = "AimsMonitoringItem"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsMonitoringItem

    aims_monitoring_metric: str = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_monitoring_description: Optional[str] = None
    aims_monitoring_method: Optional[str] = None
    aims_monitoring_frequency: Optional[str] = None
    aims_monitoring_analysis_frequency: Optional[str] = None
    aims_monitoring_analyst: Optional[str] = None
    aims_monitoring_target: Optional[str] = None
    aims_monitoring_alert_threshold: Optional[str] = None
    aims_monitoring_current_value: Optional[str] = None
    aims_monitoring_trend: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_monitoring_metric):
            self.MissingRequiredField("aims_monitoring_metric")
        if not isinstance(self.aims_monitoring_metric, str):
            self.aims_monitoring_metric = str(self.aims_monitoring_metric)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if self.aims_monitoring_description is not None and not isinstance(self.aims_monitoring_description, str):
            self.aims_monitoring_description = str(self.aims_monitoring_description)

        if self.aims_monitoring_method is not None and not isinstance(self.aims_monitoring_method, str):
            self.aims_monitoring_method = str(self.aims_monitoring_method)

        if self.aims_monitoring_frequency is not None and not isinstance(self.aims_monitoring_frequency, str):
            self.aims_monitoring_frequency = str(self.aims_monitoring_frequency)

        if self.aims_monitoring_analysis_frequency is not None and not isinstance(self.aims_monitoring_analysis_frequency, str):
            self.aims_monitoring_analysis_frequency = str(self.aims_monitoring_analysis_frequency)

        if self.aims_monitoring_analyst is not None and not isinstance(self.aims_monitoring_analyst, str):
            self.aims_monitoring_analyst = str(self.aims_monitoring_analyst)

        if self.aims_monitoring_target is not None and not isinstance(self.aims_monitoring_target, str):
            self.aims_monitoring_target = str(self.aims_monitoring_target)

        if self.aims_monitoring_alert_threshold is not None and not isinstance(self.aims_monitoring_alert_threshold, str):
            self.aims_monitoring_alert_threshold = str(self.aims_monitoring_alert_threshold)

        if self.aims_monitoring_current_value is not None and not isinstance(self.aims_monitoring_current_value, str):
            self.aims_monitoring_current_value = str(self.aims_monitoring_current_value)

        if self.aims_monitoring_trend is not None and not isinstance(self.aims_monitoring_trend, str):
            self.aims_monitoring_trend = str(self.aims_monitoring_trend)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsAuditProgramme(YAMLRoot):
    """
    A programme of internal audits: the audits planned over a period, how often and why, and the resources and
    auditors they need.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsAuditProgramme"]
    class_class_curie: ClassVar[str] = "iso42001:AimsAuditProgramme"
    class_name: ClassVar[str] = "AimsAuditProgramme"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsAuditProgramme

    aims_id: Union[str, AimsAuditProgrammeAimsId] = None
    title: str = None
    aims_programme_period: Optional[str] = None
    aims_programme_audits: Optional[Union[Union[str, AimsAuditAimsId], list[Union[str, AimsAuditAimsId]]]] = empty_list()
    aims_programme_frequency_rationale: Optional[str] = None
    aims_programme_methods: Optional[str] = None
    aims_programme_responsibilities: Optional[Union[str, list[str]]] = empty_list()
    aims_programme_resources: Optional[str] = None
    aims_programme_auditor_selection: Optional[str] = None
    aims_programme_status: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsAuditProgrammeAimsId):
            self.aims_id = AimsAuditProgrammeAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_programme_period is not None and not isinstance(self.aims_programme_period, str):
            self.aims_programme_period = str(self.aims_programme_period)

        if not isinstance(self.aims_programme_audits, list):
            self.aims_programme_audits = [self.aims_programme_audits] if self.aims_programme_audits is not None else []
        self.aims_programme_audits = [v if isinstance(v, AimsAuditAimsId) else AimsAuditAimsId(v) for v in self.aims_programme_audits]

        if self.aims_programme_frequency_rationale is not None and not isinstance(self.aims_programme_frequency_rationale, str):
            self.aims_programme_frequency_rationale = str(self.aims_programme_frequency_rationale)

        if self.aims_programme_methods is not None and not isinstance(self.aims_programme_methods, str):
            self.aims_programme_methods = str(self.aims_programme_methods)

        if not isinstance(self.aims_programme_responsibilities, list):
            self.aims_programme_responsibilities = [self.aims_programme_responsibilities] if self.aims_programme_responsibilities is not None else []
        self.aims_programme_responsibilities = [v if isinstance(v, str) else str(v) for v in self.aims_programme_responsibilities]

        if self.aims_programme_resources is not None and not isinstance(self.aims_programme_resources, str):
            self.aims_programme_resources = str(self.aims_programme_resources)

        if self.aims_programme_auditor_selection is not None and not isinstance(self.aims_programme_auditor_selection, str):
            self.aims_programme_auditor_selection = str(self.aims_programme_auditor_selection)

        if self.aims_programme_status is not None and not isinstance(self.aims_programme_status, str):
            self.aims_programme_status = str(self.aims_programme_status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsAudit(YAMLRoot):
    """
    An audit of the system: an internal audit, or one by a customer or a certification body, with its scope, criteria,
    team, findings and conclusion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsAudit"]
    class_class_curie: ClassVar[str] = "iso42001:AimsAudit"
    class_name: ClassVar[str] = "AimsAudit"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsAudit

    aims_id: Union[str, AimsAuditAimsId] = None
    aims_audit_type: Union[str, "AimsAuditType"] = None
    title: str = None
    aims_audit_standards: Optional[Union[Union[str, "AimsManagementSystemStandard"], list[Union[str, "AimsManagementSystemStandard"]]]] = empty_list()
    aims_audit_scope: Optional[str] = None
    aims_audit_criteria: Optional[Union[str, list[str]]] = empty_list()
    aims_audit_objectives: Optional[Union[str, list[str]]] = empty_list()
    aims_audit_period_start: Optional[Union[str, XSDDate]] = None
    aims_audit_period_end: Optional[Union[str, XSDDate]] = None
    aims_audit_lead: Optional[str] = None
    aims_audit_team: Optional[Union[str, list[str]]] = empty_list()
    aims_audit_auditees: Optional[Union[str, list[str]]] = empty_list()
    aims_audit_plan: Optional[Union[str, AimsDocumentedInformationAimsId]] = None
    aims_audit_findings: Optional[Union[dict[Union[str, AimsAuditFindingAimsId], Union[dict, "AimsAuditFinding"]], list[Union[dict, "AimsAuditFinding"]]]] = empty_dict()
    aims_audit_conclusion: Optional[str] = None
    aims_audit_report_date: Optional[Union[str, XSDDate]] = None
    aims_audit_report_distribution: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsAuditAimsId):
            self.aims_id = AimsAuditAimsId(self.aims_id)

        if self._is_empty(self.aims_audit_type):
            self.MissingRequiredField("aims_audit_type")
        if not isinstance(self.aims_audit_type, AimsAuditType):
            self.aims_audit_type = AimsAuditType(self.aims_audit_type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_audit_standards, list):
            self.aims_audit_standards = [self.aims_audit_standards] if self.aims_audit_standards is not None else []
        self.aims_audit_standards = [v if isinstance(v, AimsManagementSystemStandard) else AimsManagementSystemStandard(v) for v in self.aims_audit_standards]

        if self.aims_audit_scope is not None and not isinstance(self.aims_audit_scope, str):
            self.aims_audit_scope = str(self.aims_audit_scope)

        if not isinstance(self.aims_audit_criteria, list):
            self.aims_audit_criteria = [self.aims_audit_criteria] if self.aims_audit_criteria is not None else []
        self.aims_audit_criteria = [v if isinstance(v, str) else str(v) for v in self.aims_audit_criteria]

        if not isinstance(self.aims_audit_objectives, list):
            self.aims_audit_objectives = [self.aims_audit_objectives] if self.aims_audit_objectives is not None else []
        self.aims_audit_objectives = [v if isinstance(v, str) else str(v) for v in self.aims_audit_objectives]

        if self.aims_audit_period_start is not None and not isinstance(self.aims_audit_period_start, XSDDate):
            self.aims_audit_period_start = XSDDate(self.aims_audit_period_start)

        if self.aims_audit_period_end is not None and not isinstance(self.aims_audit_period_end, XSDDate):
            self.aims_audit_period_end = XSDDate(self.aims_audit_period_end)

        if self.aims_audit_lead is not None and not isinstance(self.aims_audit_lead, str):
            self.aims_audit_lead = str(self.aims_audit_lead)

        if not isinstance(self.aims_audit_team, list):
            self.aims_audit_team = [self.aims_audit_team] if self.aims_audit_team is not None else []
        self.aims_audit_team = [v if isinstance(v, str) else str(v) for v in self.aims_audit_team]

        if not isinstance(self.aims_audit_auditees, list):
            self.aims_audit_auditees = [self.aims_audit_auditees] if self.aims_audit_auditees is not None else []
        self.aims_audit_auditees = [v if isinstance(v, str) else str(v) for v in self.aims_audit_auditees]

        if self.aims_audit_plan is not None and not isinstance(self.aims_audit_plan, AimsDocumentedInformationAimsId):
            self.aims_audit_plan = AimsDocumentedInformationAimsId(self.aims_audit_plan)

        self._normalize_inlined_as_list(slot_name="aims_audit_findings", slot_type=AimsAuditFinding, key_name="aims_id", keyed=True)

        if self.aims_audit_conclusion is not None and not isinstance(self.aims_audit_conclusion, str):
            self.aims_audit_conclusion = str(self.aims_audit_conclusion)

        if self.aims_audit_report_date is not None and not isinstance(self.aims_audit_report_date, XSDDate):
            self.aims_audit_report_date = XSDDate(self.aims_audit_report_date)

        if not isinstance(self.aims_audit_report_distribution, list):
            self.aims_audit_report_distribution = [self.aims_audit_report_distribution] if self.aims_audit_report_distribution is not None else []
        self.aims_audit_report_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_audit_report_distribution]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsAuditFinding(YAMLRoot):
    """
    One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it
    concerns, its evidence and how it is closed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsAuditFinding"]
    class_class_curie: ClassVar[str] = "iso42001:AimsAuditFinding"
    class_name: ClassVar[str] = "AimsAuditFinding"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsAuditFinding

    aims_id: Union[str, AimsAuditFindingAimsId] = None
    aims_finding_type: Union[str, "AimsAuditFindingType"] = None
    title: str = None
    aims_cited_clauses: Optional[Union[Union[str, "AimsClause"], list[Union[str, "AimsClause"]]]] = empty_list()
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    aims_finding_control: Optional[Union[str, AimsControlAimsId]] = None
    aims_finding_evidence: Optional[str] = None
    aims_finding_root_cause: Optional[str] = None
    aims_finding_risk: Optional[str] = None
    aims_finding_recommendation: Optional[str] = None
    aims_finding_auditee_response: Optional[str] = None
    aims_finding_corrective_action: Optional[Union[str, AimsCorrectiveActionAimsId]] = None
    aims_finding_closure_status: Optional[str] = None
    aims_finding_closure_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsAuditFindingAimsId):
            self.aims_id = AimsAuditFindingAimsId(self.aims_id)

        if self._is_empty(self.aims_finding_type):
            self.MissingRequiredField("aims_finding_type")
        if not isinstance(self.aims_finding_type, AimsAuditFindingType):
            self.aims_finding_type = AimsAuditFindingType(self.aims_finding_type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_cited_clauses, list):
            self.aims_cited_clauses = [self.aims_cited_clauses] if self.aims_cited_clauses is not None else []
        self.aims_cited_clauses = [v if isinstance(v, AimsClause) else AimsClause(v) for v in self.aims_cited_clauses]

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if self.aims_finding_control is not None and not isinstance(self.aims_finding_control, AimsControlAimsId):
            self.aims_finding_control = AimsControlAimsId(self.aims_finding_control)

        if self.aims_finding_evidence is not None and not isinstance(self.aims_finding_evidence, str):
            self.aims_finding_evidence = str(self.aims_finding_evidence)

        if self.aims_finding_root_cause is not None and not isinstance(self.aims_finding_root_cause, str):
            self.aims_finding_root_cause = str(self.aims_finding_root_cause)

        if self.aims_finding_risk is not None and not isinstance(self.aims_finding_risk, str):
            self.aims_finding_risk = str(self.aims_finding_risk)

        if self.aims_finding_recommendation is not None and not isinstance(self.aims_finding_recommendation, str):
            self.aims_finding_recommendation = str(self.aims_finding_recommendation)

        if self.aims_finding_auditee_response is not None and not isinstance(self.aims_finding_auditee_response, str):
            self.aims_finding_auditee_response = str(self.aims_finding_auditee_response)

        if self.aims_finding_corrective_action is not None and not isinstance(self.aims_finding_corrective_action, AimsCorrectiveActionAimsId):
            self.aims_finding_corrective_action = AimsCorrectiveActionAimsId(self.aims_finding_corrective_action)

        if self.aims_finding_closure_status is not None and not isinstance(self.aims_finding_closure_status, str):
            self.aims_finding_closure_status = str(self.aims_finding_closure_status)

        if self.aims_finding_closure_date is not None and not isinstance(self.aims_finding_closure_date, XSDDate):
            self.aims_finding_closure_date = XSDDate(self.aims_finding_closure_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsManagementReview(YAMLRoot):
    """
    A review of the system by top management: what it took in, what it decided and what it asked to be done.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsManagementReview"]
    class_class_curie: ClassVar[str] = "iso42001:AimsManagementReview"
    class_name: ClassVar[str] = "AimsManagementReview"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsManagementReview

    aims_id: Union[str, AimsManagementReviewAimsId] = None
    aims_review_held_on: Union[str, XSDDate] = None
    title: str = None
    aims_review_attendees: Optional[Union[str, list[str]]] = empty_list()
    aims_review_previous_actions: Optional[str] = None
    aims_review_context_changes: Optional[str] = None
    aims_review_interested_party_changes: Optional[str] = None
    aims_review_nonconformity_trends: Optional[str] = None
    aims_review_monitoring_trends: Optional[str] = None
    aims_review_audit_trends: Optional[str] = None
    aims_review_improvement_opportunities: Optional[Union[str, list[str]]] = empty_list()
    aims_review_decisions: Optional[Union[str, list[str]]] = empty_list()
    aims_review_system_changes: Optional[Union[str, list[str]]] = empty_list()
    aims_review_actions: Optional[Union[str, list[str]]] = empty_list()
    aims_review_next_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsManagementReviewAimsId):
            self.aims_id = AimsManagementReviewAimsId(self.aims_id)

        if self._is_empty(self.aims_review_held_on):
            self.MissingRequiredField("aims_review_held_on")
        if not isinstance(self.aims_review_held_on, XSDDate):
            self.aims_review_held_on = XSDDate(self.aims_review_held_on)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_review_attendees, list):
            self.aims_review_attendees = [self.aims_review_attendees] if self.aims_review_attendees is not None else []
        self.aims_review_attendees = [v if isinstance(v, str) else str(v) for v in self.aims_review_attendees]

        if self.aims_review_previous_actions is not None and not isinstance(self.aims_review_previous_actions, str):
            self.aims_review_previous_actions = str(self.aims_review_previous_actions)

        if self.aims_review_context_changes is not None and not isinstance(self.aims_review_context_changes, str):
            self.aims_review_context_changes = str(self.aims_review_context_changes)

        if self.aims_review_interested_party_changes is not None and not isinstance(self.aims_review_interested_party_changes, str):
            self.aims_review_interested_party_changes = str(self.aims_review_interested_party_changes)

        if self.aims_review_nonconformity_trends is not None and not isinstance(self.aims_review_nonconformity_trends, str):
            self.aims_review_nonconformity_trends = str(self.aims_review_nonconformity_trends)

        if self.aims_review_monitoring_trends is not None and not isinstance(self.aims_review_monitoring_trends, str):
            self.aims_review_monitoring_trends = str(self.aims_review_monitoring_trends)

        if self.aims_review_audit_trends is not None and not isinstance(self.aims_review_audit_trends, str):
            self.aims_review_audit_trends = str(self.aims_review_audit_trends)

        if not isinstance(self.aims_review_improvement_opportunities, list):
            self.aims_review_improvement_opportunities = [self.aims_review_improvement_opportunities] if self.aims_review_improvement_opportunities is not None else []
        self.aims_review_improvement_opportunities = [v if isinstance(v, str) else str(v) for v in self.aims_review_improvement_opportunities]

        if not isinstance(self.aims_review_decisions, list):
            self.aims_review_decisions = [self.aims_review_decisions] if self.aims_review_decisions is not None else []
        self.aims_review_decisions = [v if isinstance(v, str) else str(v) for v in self.aims_review_decisions]

        if not isinstance(self.aims_review_system_changes, list):
            self.aims_review_system_changes = [self.aims_review_system_changes] if self.aims_review_system_changes is not None else []
        self.aims_review_system_changes = [v if isinstance(v, str) else str(v) for v in self.aims_review_system_changes]

        if not isinstance(self.aims_review_actions, list):
            self.aims_review_actions = [self.aims_review_actions] if self.aims_review_actions is not None else []
        self.aims_review_actions = [v if isinstance(v, str) else str(v) for v in self.aims_review_actions]

        if self.aims_review_next_date is not None and not isinstance(self.aims_review_next_date, XSDDate):
            self.aims_review_next_date = XSDDate(self.aims_review_next_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsNonconformity(YAMLRoot):
    """
    A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was
    closed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsNonconformity"]
    class_class_curie: ClassVar[str] = "iso42001:AimsNonconformity"
    class_name: ClassVar[str] = "AimsNonconformity"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsNonconformity

    aims_id: Union[str, AimsNonconformityAimsId] = None
    title: str = None
    aims_cited_clauses: Optional[Union[Union[str, "AimsClause"], list[Union[str, "AimsClause"]]]] = empty_list()
    aims_cited_annex_a_controls: Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]] = empty_list()
    aims_nonconformity_source: Optional[str] = None
    aims_nonconformity_detected_on: Optional[Union[str, XSDDate]] = None
    aims_nonconformity_detected_by: Optional[str] = None
    aims_nonconformity_requirement: Optional[str] = None
    aims_nonconformity_immediate_actions: Optional[Union[str, list[str]]] = empty_list()
    aims_nonconformity_consequences: Optional[str] = None
    aims_nonconformity_root_cause: Optional[str] = None
    aims_nonconformity_similar_check: Optional[str] = None
    aims_nonconformity_status: Optional[str] = None
    aims_nonconformity_closure_date: Optional[Union[str, XSDDate]] = None
    aims_nonconformity_closure_evidence: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsNonconformityAimsId):
            self.aims_id = AimsNonconformityAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_cited_clauses, list):
            self.aims_cited_clauses = [self.aims_cited_clauses] if self.aims_cited_clauses is not None else []
        self.aims_cited_clauses = [v if isinstance(v, AimsClause) else AimsClause(v) for v in self.aims_cited_clauses]

        if not isinstance(self.aims_cited_annex_a_controls, list):
            self.aims_cited_annex_a_controls = [self.aims_cited_annex_a_controls] if self.aims_cited_annex_a_controls is not None else []
        self.aims_cited_annex_a_controls = [v if isinstance(v, AimsAnnexAControl) else AimsAnnexAControl(v) for v in self.aims_cited_annex_a_controls]

        if self.aims_nonconformity_source is not None and not isinstance(self.aims_nonconformity_source, str):
            self.aims_nonconformity_source = str(self.aims_nonconformity_source)

        if self.aims_nonconformity_detected_on is not None and not isinstance(self.aims_nonconformity_detected_on, XSDDate):
            self.aims_nonconformity_detected_on = XSDDate(self.aims_nonconformity_detected_on)

        if self.aims_nonconformity_detected_by is not None and not isinstance(self.aims_nonconformity_detected_by, str):
            self.aims_nonconformity_detected_by = str(self.aims_nonconformity_detected_by)

        if self.aims_nonconformity_requirement is not None and not isinstance(self.aims_nonconformity_requirement, str):
            self.aims_nonconformity_requirement = str(self.aims_nonconformity_requirement)

        if not isinstance(self.aims_nonconformity_immediate_actions, list):
            self.aims_nonconformity_immediate_actions = [self.aims_nonconformity_immediate_actions] if self.aims_nonconformity_immediate_actions is not None else []
        self.aims_nonconformity_immediate_actions = [v if isinstance(v, str) else str(v) for v in self.aims_nonconformity_immediate_actions]

        if self.aims_nonconformity_consequences is not None and not isinstance(self.aims_nonconformity_consequences, str):
            self.aims_nonconformity_consequences = str(self.aims_nonconformity_consequences)

        if self.aims_nonconformity_root_cause is not None and not isinstance(self.aims_nonconformity_root_cause, str):
            self.aims_nonconformity_root_cause = str(self.aims_nonconformity_root_cause)

        if self.aims_nonconformity_similar_check is not None and not isinstance(self.aims_nonconformity_similar_check, str):
            self.aims_nonconformity_similar_check = str(self.aims_nonconformity_similar_check)

        if self.aims_nonconformity_status is not None and not isinstance(self.aims_nonconformity_status, str):
            self.aims_nonconformity_status = str(self.aims_nonconformity_status)

        if self.aims_nonconformity_closure_date is not None and not isinstance(self.aims_nonconformity_closure_date, XSDDate):
            self.aims_nonconformity_closure_date = XSDDate(self.aims_nonconformity_closure_date)

        if self.aims_nonconformity_closure_evidence is not None and not isinstance(self.aims_nonconformity_closure_evidence, str):
            self.aims_nonconformity_closure_evidence = str(self.aims_nonconformity_closure_evidence)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsCorrectiveAction(YAMLRoot):
    """
    An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it
    worked.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsCorrectiveAction"]
    class_class_curie: ClassVar[str] = "iso42001:AimsCorrectiveAction"
    class_name: ClassVar[str] = "AimsCorrectiveAction"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsCorrectiveAction

    aims_id: Union[str, AimsCorrectiveActionAimsId] = None
    title: str = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_action_nonconformities: Optional[Union[Union[str, AimsNonconformityAimsId], list[Union[str, AimsNonconformityAimsId]]]] = empty_list()
    aims_action_root_cause: Optional[str] = None
    aims_action_target_date: Optional[Union[str, XSDDate]] = None
    aims_action_completion_date: Optional[Union[str, XSDDate]] = None
    aims_action_resources: Optional[str] = None
    aims_action_effectiveness_criteria: Optional[str] = None
    aims_action_effectiveness_review_date: Optional[Union[str, XSDDate]] = None
    aims_action_effective: Optional[Union[bool, Bool]] = None
    aims_action_system_changes: Optional[str] = None
    aims_action_status: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsCorrectiveActionAimsId):
            self.aims_id = AimsCorrectiveActionAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if not isinstance(self.aims_action_nonconformities, list):
            self.aims_action_nonconformities = [self.aims_action_nonconformities] if self.aims_action_nonconformities is not None else []
        self.aims_action_nonconformities = [v if isinstance(v, AimsNonconformityAimsId) else AimsNonconformityAimsId(v) for v in self.aims_action_nonconformities]

        if self.aims_action_root_cause is not None and not isinstance(self.aims_action_root_cause, str):
            self.aims_action_root_cause = str(self.aims_action_root_cause)

        if self.aims_action_target_date is not None and not isinstance(self.aims_action_target_date, XSDDate):
            self.aims_action_target_date = XSDDate(self.aims_action_target_date)

        if self.aims_action_completion_date is not None and not isinstance(self.aims_action_completion_date, XSDDate):
            self.aims_action_completion_date = XSDDate(self.aims_action_completion_date)

        if self.aims_action_resources is not None and not isinstance(self.aims_action_resources, str):
            self.aims_action_resources = str(self.aims_action_resources)

        if self.aims_action_effectiveness_criteria is not None and not isinstance(self.aims_action_effectiveness_criteria, str):
            self.aims_action_effectiveness_criteria = str(self.aims_action_effectiveness_criteria)

        if self.aims_action_effectiveness_review_date is not None and not isinstance(self.aims_action_effectiveness_review_date, XSDDate):
            self.aims_action_effectiveness_review_date = XSDDate(self.aims_action_effectiveness_review_date)

        if self.aims_action_effective is not None and not isinstance(self.aims_action_effective, Bool):
            self.aims_action_effective = Bool(self.aims_action_effective)

        if self.aims_action_system_changes is not None and not isinstance(self.aims_action_system_changes, str):
            self.aims_action_system_changes = str(self.aims_action_system_changes)

        if self.aims_action_status is not None and not isinstance(self.aims_action_status, str):
            self.aims_action_status = str(self.aims_action_status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsImprovementOpportunity(YAMLRoot):
    """
    An opportunity to make the system more suitable, adequate or effective, and what came of it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsImprovementOpportunity"]
    class_class_curie: ClassVar[str] = "iso42001:AimsImprovementOpportunity"
    class_name: ClassVar[str] = "AimsImprovementOpportunity"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsImprovementOpportunity

    aims_id: Union[str, AimsImprovementOpportunityAimsId] = None
    title: str = None
    aims_responsible_role: Optional[Union[str, AimsRoleAimsId]] = None
    aims_improvement_source: Optional[str] = None
    aims_improvement_identified_on: Optional[Union[str, XSDDate]] = None
    aims_improvement_identified_by: Optional[str] = None
    aims_improvement_benefit: Optional[str] = None
    aims_improvement_priority: Optional[str] = None
    aims_improvement_plan: Optional[str] = None
    aims_improvement_target_date: Optional[Union[str, XSDDate]] = None
    aims_improvement_completion_date: Optional[Union[str, XSDDate]] = None
    aims_improvement_outcome: Optional[str] = None
    aims_improvement_status: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsImprovementOpportunityAimsId):
            self.aims_id = AimsImprovementOpportunityAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aims_responsible_role is not None and not isinstance(self.aims_responsible_role, AimsRoleAimsId):
            self.aims_responsible_role = AimsRoleAimsId(self.aims_responsible_role)

        if self.aims_improvement_source is not None and not isinstance(self.aims_improvement_source, str):
            self.aims_improvement_source = str(self.aims_improvement_source)

        if self.aims_improvement_identified_on is not None and not isinstance(self.aims_improvement_identified_on, XSDDate):
            self.aims_improvement_identified_on = XSDDate(self.aims_improvement_identified_on)

        if self.aims_improvement_identified_by is not None and not isinstance(self.aims_improvement_identified_by, str):
            self.aims_improvement_identified_by = str(self.aims_improvement_identified_by)

        if self.aims_improvement_benefit is not None and not isinstance(self.aims_improvement_benefit, str):
            self.aims_improvement_benefit = str(self.aims_improvement_benefit)

        if self.aims_improvement_priority is not None and not isinstance(self.aims_improvement_priority, str):
            self.aims_improvement_priority = str(self.aims_improvement_priority)

        if self.aims_improvement_plan is not None and not isinstance(self.aims_improvement_plan, str):
            self.aims_improvement_plan = str(self.aims_improvement_plan)

        if self.aims_improvement_target_date is not None and not isinstance(self.aims_improvement_target_date, XSDDate):
            self.aims_improvement_target_date = XSDDate(self.aims_improvement_target_date)

        if self.aims_improvement_completion_date is not None and not isinstance(self.aims_improvement_completion_date, XSDDate):
            self.aims_improvement_completion_date = XSDDate(self.aims_improvement_completion_date)

        if self.aims_improvement_outcome is not None and not isinstance(self.aims_improvement_outcome, str):
            self.aims_improvement_outcome = str(self.aims_improvement_outcome)

        if self.aims_improvement_status is not None and not isinstance(self.aims_improvement_status, str):
            self.aims_improvement_status = str(self.aims_improvement_status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsThirdPartyRelationship(YAMLRoot):
    """
    A relationship with another party in an AI system's life, such as a partner: who carries which duty, and what
    assures the organization of that.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsThirdPartyRelationship"]
    class_class_curie: ClassVar[str] = "iso42001:AimsThirdPartyRelationship"
    class_name: ClassVar[str] = "AimsThirdPartyRelationship"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsThirdPartyRelationship

    aims_id: Union[str, AimsThirdPartyRelationshipAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_life_cycle_stages: Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]] = empty_list()
    aims_relationship_type: Optional[str] = None
    aims_relationship_party: Optional[str] = None
    aims_relationship_party_roles: Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]] = empty_list()
    aims_relationship_contract: Optional[str] = None
    aims_relationship_responsibilities: Optional[Union[str, list[str]]] = empty_list()
    aims_relationship_pii_role: Optional[Union[str, "AimsPiiRole"]] = None
    aims_relationship_documentation: Optional[Union[str, list[str]]] = empty_list()
    aims_relationship_assurance_evidence: Optional[Union[str, list[str]]] = empty_list()
    aims_relationship_review_frequency: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsThirdPartyRelationshipAimsId):
            self.aims_id = AimsThirdPartyRelationshipAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if not isinstance(self.aims_life_cycle_stages, list):
            self.aims_life_cycle_stages = [self.aims_life_cycle_stages] if self.aims_life_cycle_stages is not None else []
        self.aims_life_cycle_stages = [v if isinstance(v, AimsLifecycleStage) else AimsLifecycleStage(v) for v in self.aims_life_cycle_stages]

        self.aims_relationship_type = str(self.class_name)

        if self.aims_relationship_party is not None and not isinstance(self.aims_relationship_party, str):
            self.aims_relationship_party = str(self.aims_relationship_party)

        if not isinstance(self.aims_relationship_party_roles, list):
            self.aims_relationship_party_roles = [self.aims_relationship_party_roles] if self.aims_relationship_party_roles is not None else []
        self.aims_relationship_party_roles = [v if isinstance(v, AimsAiRole) else AimsAiRole(v) for v in self.aims_relationship_party_roles]

        if self.aims_relationship_contract is not None and not isinstance(self.aims_relationship_contract, str):
            self.aims_relationship_contract = str(self.aims_relationship_contract)

        if not isinstance(self.aims_relationship_responsibilities, list):
            self.aims_relationship_responsibilities = [self.aims_relationship_responsibilities] if self.aims_relationship_responsibilities is not None else []
        self.aims_relationship_responsibilities = [v if isinstance(v, str) else str(v) for v in self.aims_relationship_responsibilities]

        if self.aims_relationship_pii_role is not None and not isinstance(self.aims_relationship_pii_role, AimsPiiRole):
            self.aims_relationship_pii_role = AimsPiiRole(self.aims_relationship_pii_role)

        if not isinstance(self.aims_relationship_documentation, list):
            self.aims_relationship_documentation = [self.aims_relationship_documentation] if self.aims_relationship_documentation is not None else []
        self.aims_relationship_documentation = [v if isinstance(v, str) else str(v) for v in self.aims_relationship_documentation]

        if not isinstance(self.aims_relationship_assurance_evidence, list):
            self.aims_relationship_assurance_evidence = [self.aims_relationship_assurance_evidence] if self.aims_relationship_assurance_evidence is not None else []
        self.aims_relationship_assurance_evidence = [v if isinstance(v, str) else str(v) for v in self.aims_relationship_assurance_evidence]

        if self.aims_relationship_review_frequency is not None and not isinstance(self.aims_relationship_review_frequency, str):
            self.aims_relationship_review_frequency = str(self.aims_relationship_review_frequency)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        self.unknown_aims_relationship_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "aims_relationship_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AimsSupplierRelationship(AimsThirdPartyRelationship):
    """
    A relationship with a supplier to the organization's AI work: what it provides, the risk that brings, and how it
    is held to the organization's approach.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsSupplierRelationship"]
    class_class_curie: ClassVar[str] = "iso42001:AimsSupplierRelationship"
    class_name: ClassVar[str] = "AimsSupplierRelationship"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsSupplierRelationship

    aims_id: Union[str, AimsSupplierRelationshipAimsId] = None
    title: str = None
    aims_supplier_provides: Optional[Union[str, list[str]]] = empty_list()
    aims_supplier_risk: Optional[Union[str, "AimsRiskLevel"]] = None
    aims_supplier_requirements: Optional[Union[str, list[str]]] = empty_list()
    aims_supplier_monitoring: Optional[str] = None
    aims_supplier_integration: Optional[str] = None
    aims_supplier_corrective_actions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsSupplierRelationshipAimsId):
            self.aims_id = AimsSupplierRelationshipAimsId(self.aims_id)

        if not isinstance(self.aims_supplier_provides, list):
            self.aims_supplier_provides = [self.aims_supplier_provides] if self.aims_supplier_provides is not None else []
        self.aims_supplier_provides = [v if isinstance(v, str) else str(v) for v in self.aims_supplier_provides]

        if self.aims_supplier_risk is not None and not isinstance(self.aims_supplier_risk, AimsRiskLevel):
            self.aims_supplier_risk = AimsRiskLevel(self.aims_supplier_risk)

        if not isinstance(self.aims_supplier_requirements, list):
            self.aims_supplier_requirements = [self.aims_supplier_requirements] if self.aims_supplier_requirements is not None else []
        self.aims_supplier_requirements = [v if isinstance(v, str) else str(v) for v in self.aims_supplier_requirements]

        if self.aims_supplier_monitoring is not None and not isinstance(self.aims_supplier_monitoring, str):
            self.aims_supplier_monitoring = str(self.aims_supplier_monitoring)

        if self.aims_supplier_integration is not None and not isinstance(self.aims_supplier_integration, str):
            self.aims_supplier_integration = str(self.aims_supplier_integration)

        if not isinstance(self.aims_supplier_corrective_actions, list):
            self.aims_supplier_corrective_actions = [self.aims_supplier_corrective_actions] if self.aims_supplier_corrective_actions is not None else []
        self.aims_supplier_corrective_actions = [v if isinstance(v, str) else str(v) for v in self.aims_supplier_corrective_actions]

        super().__post_init__(**kwargs)
        self.unknown_aims_relationship_type = str(self.class_name)


@dataclass(repr=False)
class AimsCustomerRelationship(AimsThirdPartyRelationship):
    """
    A relationship with a customer of the organization's AI work: what it expects, who answers for what, and which
    limits it was told of.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsCustomerRelationship"]
    class_class_curie: ClassVar[str] = "iso42001:AimsCustomerRelationship"
    class_name: ClassVar[str] = "AimsCustomerRelationship"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsCustomerRelationship

    aims_id: Union[str, AimsCustomerRelationshipAimsId] = None
    title: str = None
    aims_customer_expectations: Optional[Union[str, list[str]]] = empty_list()
    aims_customer_agreement: Optional[str] = None
    aims_customer_responsibility_split: Optional[str] = None
    aims_customer_communicated_limits: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsCustomerRelationshipAimsId):
            self.aims_id = AimsCustomerRelationshipAimsId(self.aims_id)

        if not isinstance(self.aims_customer_expectations, list):
            self.aims_customer_expectations = [self.aims_customer_expectations] if self.aims_customer_expectations is not None else []
        self.aims_customer_expectations = [v if isinstance(v, str) else str(v) for v in self.aims_customer_expectations]

        if self.aims_customer_agreement is not None and not isinstance(self.aims_customer_agreement, str):
            self.aims_customer_agreement = str(self.aims_customer_agreement)

        if self.aims_customer_responsibility_split is not None and not isinstance(self.aims_customer_responsibility_split, str):
            self.aims_customer_responsibility_split = str(self.aims_customer_responsibility_split)

        if not isinstance(self.aims_customer_communicated_limits, list):
            self.aims_customer_communicated_limits = [self.aims_customer_communicated_limits] if self.aims_customer_communicated_limits is not None else []
        self.aims_customer_communicated_limits = [v if isinstance(v, str) else str(v) for v in self.aims_customer_communicated_limits]

        super().__post_init__(**kwargs)
        self.unknown_aims_relationship_type = str(self.class_name)


@dataclass(repr=False)
class AimsSystemEvent(YAMLRoot):
    """
    Something that happened with a system and was reported, by monitoring, by a user or by someone outside, and the
    assessment of whether it is an incident. An event assessed as an incident is recorded as an AimsIncident.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsSystemEvent"]
    class_class_curie: ClassVar[str] = "iso42001:AimsSystemEvent"
    class_name: ClassVar[str] = "AimsSystemEvent"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsSystemEvent

    aims_id: Union[str, AimsSystemEventAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_event_type: Optional[str] = None
    aims_event_occurred_at: Optional[Union[str, XSDDateTime]] = None
    aims_event_reporter: Optional[str] = None
    aims_event_source: Optional[str] = None
    aims_event_adverse_impact: Optional[str] = None
    aims_event_assessment: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsSystemEventAimsId):
            self.aims_id = AimsSystemEventAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        self.aims_event_type = str(self.class_name)

        if self.aims_event_occurred_at is not None and not isinstance(self.aims_event_occurred_at, XSDDateTime):
            self.aims_event_occurred_at = XSDDateTime(self.aims_event_occurred_at)

        if self.aims_event_reporter is not None and not isinstance(self.aims_event_reporter, str):
            self.aims_event_reporter = str(self.aims_event_reporter)

        if self.aims_event_source is not None and not isinstance(self.aims_event_source, str):
            self.aims_event_source = str(self.aims_event_source)

        if self.aims_event_adverse_impact is not None and not isinstance(self.aims_event_adverse_impact, str):
            self.aims_event_adverse_impact = str(self.aims_event_adverse_impact)

        if self.aims_event_assessment is not None and not isinstance(self.aims_event_assessment, str):
            self.aims_event_assessment = str(self.aims_event_assessment)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        self.unknown_aims_event_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "aims_event_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AimsIncident(AimsSystemEvent):
    """
    An event assessed as an incident: what it concerns, how severe it is, what was done, who was told, and what was
    learned.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsIncident"]
    class_class_curie: ClassVar[str] = "iso42001:AimsIncident"
    class_name: ClassVar[str] = "AimsIncident"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsIncident

    aims_id: Union[str, AimsIncidentAimsId] = None
    title: str = None
    aims_incident_category: Optional[Union[str, "AimsIncidentCategory"]] = None
    aims_incident_threats: Optional[Union[Union[str, "AimsAiThreat"], list[Union[str, "AimsAiThreat"]]]] = empty_list()
    aims_incident_severity: Optional[Union[str, "AimsRiskLevel"]] = None
    aims_incident_impact_areas: Optional[Union[Union[str, "AimsImpactArea"], list[Union[str, "AimsImpactArea"]]]] = empty_list()
    aims_incident_detection_method: Optional[str] = None
    aims_incident_response_actions: Optional[Union[str, list[str]]] = empty_list()
    aims_incident_recovery_actions: Optional[Union[str, list[str]]] = empty_list()
    aims_incident_root_cause: Optional[str] = None
    aims_incident_lessons_learned: Optional[Union[str, list[str]]] = empty_list()
    aims_incident_notification_required: Optional[Union[bool, Bool]] = None
    aims_incident_notifications: Optional[Union[str, list[str]]] = empty_list()
    aims_incident_corrective_actions: Optional[Union[Union[str, AimsCorrectiveActionAimsId], list[Union[str, AimsCorrectiveActionAimsId]]]] = empty_list()
    aims_incident_closed_at: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsIncidentAimsId):
            self.aims_id = AimsIncidentAimsId(self.aims_id)

        if self.aims_incident_category is not None and not isinstance(self.aims_incident_category, AimsIncidentCategory):
            self.aims_incident_category = AimsIncidentCategory(self.aims_incident_category)

        if not isinstance(self.aims_incident_threats, list):
            self.aims_incident_threats = [self.aims_incident_threats] if self.aims_incident_threats is not None else []
        self.aims_incident_threats = [v if isinstance(v, AimsAiThreat) else AimsAiThreat(v) for v in self.aims_incident_threats]

        if self.aims_incident_severity is not None and not isinstance(self.aims_incident_severity, AimsRiskLevel):
            self.aims_incident_severity = AimsRiskLevel(self.aims_incident_severity)

        if not isinstance(self.aims_incident_impact_areas, list):
            self.aims_incident_impact_areas = [self.aims_incident_impact_areas] if self.aims_incident_impact_areas is not None else []
        self.aims_incident_impact_areas = [v if isinstance(v, AimsImpactArea) else AimsImpactArea(v) for v in self.aims_incident_impact_areas]

        if self.aims_incident_detection_method is not None and not isinstance(self.aims_incident_detection_method, str):
            self.aims_incident_detection_method = str(self.aims_incident_detection_method)

        if not isinstance(self.aims_incident_response_actions, list):
            self.aims_incident_response_actions = [self.aims_incident_response_actions] if self.aims_incident_response_actions is not None else []
        self.aims_incident_response_actions = [v if isinstance(v, str) else str(v) for v in self.aims_incident_response_actions]

        if not isinstance(self.aims_incident_recovery_actions, list):
            self.aims_incident_recovery_actions = [self.aims_incident_recovery_actions] if self.aims_incident_recovery_actions is not None else []
        self.aims_incident_recovery_actions = [v if isinstance(v, str) else str(v) for v in self.aims_incident_recovery_actions]

        if self.aims_incident_root_cause is not None and not isinstance(self.aims_incident_root_cause, str):
            self.aims_incident_root_cause = str(self.aims_incident_root_cause)

        if not isinstance(self.aims_incident_lessons_learned, list):
            self.aims_incident_lessons_learned = [self.aims_incident_lessons_learned] if self.aims_incident_lessons_learned is not None else []
        self.aims_incident_lessons_learned = [v if isinstance(v, str) else str(v) for v in self.aims_incident_lessons_learned]

        if self.aims_incident_notification_required is not None and not isinstance(self.aims_incident_notification_required, Bool):
            self.aims_incident_notification_required = Bool(self.aims_incident_notification_required)

        if not isinstance(self.aims_incident_notifications, list):
            self.aims_incident_notifications = [self.aims_incident_notifications] if self.aims_incident_notifications is not None else []
        self.aims_incident_notifications = [v if isinstance(v, str) else str(v) for v in self.aims_incident_notifications]

        if not isinstance(self.aims_incident_corrective_actions, list):
            self.aims_incident_corrective_actions = [self.aims_incident_corrective_actions] if self.aims_incident_corrective_actions is not None else []
        self.aims_incident_corrective_actions = [v if isinstance(v, AimsCorrectiveActionAimsId) else AimsCorrectiveActionAimsId(v) for v in self.aims_incident_corrective_actions]

        if self.aims_incident_closed_at is not None and not isinstance(self.aims_incident_closed_at, XSDDateTime):
            self.aims_incident_closed_at = XSDDateTime(self.aims_incident_closed_at)

        super().__post_init__(**kwargs)
        self.unknown_aims_event_type = str(self.class_name)


@dataclass(repr=False)
class AimsConcernReportingProcess(YAMLRoot):
    """
    The way people raise worries about the organization's part in a system: how it keeps them safe, who looks into a
    worry, and how fast it answers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsConcernReportingProcess"]
    class_class_curie: ClassVar[str] = "iso42001:AimsConcernReportingProcess"
    class_name: ClassVar[str] = "AimsConcernReportingProcess"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsConcernReportingProcess

    aims_id: Union[str, AimsConcernReportingProcessAimsId] = None
    title: str = None
    aims_concern_process_confidentiality: Optional[Union[str, list[str]]] = empty_list()
    aims_concern_process_audience: Optional[str] = None
    aims_concern_process_investigators: Optional[str] = None
    aims_concern_process_escalation: Optional[str] = None
    aims_concern_process_reprisal_protection: Optional[str] = None
    aims_concern_process_response_time: Optional[str] = None
    description: Optional[str] = None
    aims_document_reference: Optional[str] = None
    aims_document_version: Optional[str] = None
    aims_document_author: Optional[str] = None
    aims_document_owner: Optional[str] = None
    aims_document_format: Optional[str] = None
    aims_document_medium: Optional[str] = None
    aims_document_approver: Optional[str] = None
    aims_document_approval_date: Optional[Union[str, XSDDate]] = None
    aims_document_effective_date: Optional[Union[str, XSDDate]] = None
    aims_document_last_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_next_review_date: Optional[Union[str, XSDDate]] = None
    aims_document_status: Optional[str] = None
    aims_document_classification: Optional[str] = None
    aims_document_retention: Optional[Union[str, AimsDuration]] = None
    aims_document_disposition: Optional[str] = None
    aims_document_distribution: Optional[Union[str, list[str]]] = empty_list()
    aims_document_storage: Optional[str] = None
    aims_document_change_control: Optional[str] = None
    aims_document_external_origin: Optional[Union[bool, Bool]] = None
    aims_document_external_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsConcernReportingProcessAimsId):
            self.aims_id = AimsConcernReportingProcessAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_concern_process_confidentiality, list):
            self.aims_concern_process_confidentiality = [self.aims_concern_process_confidentiality] if self.aims_concern_process_confidentiality is not None else []
        self.aims_concern_process_confidentiality = [v if isinstance(v, str) else str(v) for v in self.aims_concern_process_confidentiality]

        if self.aims_concern_process_audience is not None and not isinstance(self.aims_concern_process_audience, str):
            self.aims_concern_process_audience = str(self.aims_concern_process_audience)

        if self.aims_concern_process_investigators is not None and not isinstance(self.aims_concern_process_investigators, str):
            self.aims_concern_process_investigators = str(self.aims_concern_process_investigators)

        if self.aims_concern_process_escalation is not None and not isinstance(self.aims_concern_process_escalation, str):
            self.aims_concern_process_escalation = str(self.aims_concern_process_escalation)

        if self.aims_concern_process_reprisal_protection is not None and not isinstance(self.aims_concern_process_reprisal_protection, str):
            self.aims_concern_process_reprisal_protection = str(self.aims_concern_process_reprisal_protection)

        if self.aims_concern_process_response_time is not None and not isinstance(self.aims_concern_process_response_time, str):
            self.aims_concern_process_response_time = str(self.aims_concern_process_response_time)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.aims_document_reference is not None and not isinstance(self.aims_document_reference, str):
            self.aims_document_reference = str(self.aims_document_reference)

        if self.aims_document_version is not None and not isinstance(self.aims_document_version, str):
            self.aims_document_version = str(self.aims_document_version)

        if self.aims_document_author is not None and not isinstance(self.aims_document_author, str):
            self.aims_document_author = str(self.aims_document_author)

        if self.aims_document_owner is not None and not isinstance(self.aims_document_owner, str):
            self.aims_document_owner = str(self.aims_document_owner)

        if self.aims_document_format is not None and not isinstance(self.aims_document_format, str):
            self.aims_document_format = str(self.aims_document_format)

        if self.aims_document_medium is not None and not isinstance(self.aims_document_medium, str):
            self.aims_document_medium = str(self.aims_document_medium)

        if self.aims_document_approver is not None and not isinstance(self.aims_document_approver, str):
            self.aims_document_approver = str(self.aims_document_approver)

        if self.aims_document_approval_date is not None and not isinstance(self.aims_document_approval_date, XSDDate):
            self.aims_document_approval_date = XSDDate(self.aims_document_approval_date)

        if self.aims_document_effective_date is not None and not isinstance(self.aims_document_effective_date, XSDDate):
            self.aims_document_effective_date = XSDDate(self.aims_document_effective_date)

        if self.aims_document_last_review_date is not None and not isinstance(self.aims_document_last_review_date, XSDDate):
            self.aims_document_last_review_date = XSDDate(self.aims_document_last_review_date)

        if self.aims_document_next_review_date is not None and not isinstance(self.aims_document_next_review_date, XSDDate):
            self.aims_document_next_review_date = XSDDate(self.aims_document_next_review_date)

        if self.aims_document_status is not None and not isinstance(self.aims_document_status, str):
            self.aims_document_status = str(self.aims_document_status)

        if self.aims_document_classification is not None and not isinstance(self.aims_document_classification, str):
            self.aims_document_classification = str(self.aims_document_classification)

        if self.aims_document_retention is not None and not isinstance(self.aims_document_retention, AimsDuration):
            self.aims_document_retention = AimsDuration(self.aims_document_retention)

        if self.aims_document_disposition is not None and not isinstance(self.aims_document_disposition, str):
            self.aims_document_disposition = str(self.aims_document_disposition)

        if not isinstance(self.aims_document_distribution, list):
            self.aims_document_distribution = [self.aims_document_distribution] if self.aims_document_distribution is not None else []
        self.aims_document_distribution = [v if isinstance(v, str) else str(v) for v in self.aims_document_distribution]

        if self.aims_document_storage is not None and not isinstance(self.aims_document_storage, str):
            self.aims_document_storage = str(self.aims_document_storage)

        if self.aims_document_change_control is not None and not isinstance(self.aims_document_change_control, str):
            self.aims_document_change_control = str(self.aims_document_change_control)

        if self.aims_document_external_origin is not None and not isinstance(self.aims_document_external_origin, Bool):
            self.aims_document_external_origin = Bool(self.aims_document_external_origin)

        if self.aims_document_external_source is not None and not isinstance(self.aims_document_external_source, str):
            self.aims_document_external_source = str(self.aims_document_external_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AimsConcernReport(YAMLRoot):
    """
    One worry someone raised about the organization's part in a system, and how it was looked into and settled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO42001["AimsConcernReport"]
    class_class_curie: ClassVar[str] = "iso42001:AimsConcernReport"
    class_name: ClassVar[str] = "AimsConcernReport"
    class_model_uri: ClassVar[URIRef] = ISO42001.AimsConcernReport

    aims_id: Union[str, AimsConcernReportAimsId] = None
    title: str = None
    aims_ai_systems: Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]] = empty_list()
    aims_concern_reported_on: Optional[Union[str, XSDDate]] = None
    aims_concern_reporter: Optional[str] = None
    aims_concern_anonymous: Optional[Union[bool, Bool]] = None
    aims_concern_channel: Optional[str] = None
    aims_concern_life_cycle_stage: Optional[Union[str, "AimsLifecycleStage"]] = None
    aims_concern_severity: Optional[Union[str, "AimsRiskLevel"]] = None
    aims_concern_investigator: Optional[str] = None
    aims_concern_investigation_status: Optional[str] = None
    aims_concern_findings: Optional[str] = None
    aims_concern_escalation: Optional[str] = None
    aims_concern_response_due: Optional[Union[str, XSDDate]] = None
    aims_concern_responded_on: Optional[Union[str, XSDDate]] = None
    aims_concern_resolution: Optional[str] = None
    aims_concern_reprisal_protection: Optional[str] = None
    aims_concern_incidents: Optional[Union[Union[str, AimsIncidentAimsId], list[Union[str, AimsIncidentAimsId]]]] = empty_list()
    aims_concern_nonconformities: Optional[Union[Union[str, AimsNonconformityAimsId], list[Union[str, AimsNonconformityAimsId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aims_id):
            self.MissingRequiredField("aims_id")
        if not isinstance(self.aims_id, AimsConcernReportAimsId):
            self.aims_id = AimsConcernReportAimsId(self.aims_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aims_ai_systems, list):
            self.aims_ai_systems = [self.aims_ai_systems] if self.aims_ai_systems is not None else []
        self.aims_ai_systems = [v if isinstance(v, AimsAiSystemAimsId) else AimsAiSystemAimsId(v) for v in self.aims_ai_systems]

        if self.aims_concern_reported_on is not None and not isinstance(self.aims_concern_reported_on, XSDDate):
            self.aims_concern_reported_on = XSDDate(self.aims_concern_reported_on)

        if self.aims_concern_reporter is not None and not isinstance(self.aims_concern_reporter, str):
            self.aims_concern_reporter = str(self.aims_concern_reporter)

        if self.aims_concern_anonymous is not None and not isinstance(self.aims_concern_anonymous, Bool):
            self.aims_concern_anonymous = Bool(self.aims_concern_anonymous)

        if self.aims_concern_channel is not None and not isinstance(self.aims_concern_channel, str):
            self.aims_concern_channel = str(self.aims_concern_channel)

        if self.aims_concern_life_cycle_stage is not None and not isinstance(self.aims_concern_life_cycle_stage, AimsLifecycleStage):
            self.aims_concern_life_cycle_stage = AimsLifecycleStage(self.aims_concern_life_cycle_stage)

        if self.aims_concern_severity is not None and not isinstance(self.aims_concern_severity, AimsRiskLevel):
            self.aims_concern_severity = AimsRiskLevel(self.aims_concern_severity)

        if self.aims_concern_investigator is not None and not isinstance(self.aims_concern_investigator, str):
            self.aims_concern_investigator = str(self.aims_concern_investigator)

        if self.aims_concern_investigation_status is not None and not isinstance(self.aims_concern_investigation_status, str):
            self.aims_concern_investigation_status = str(self.aims_concern_investigation_status)

        if self.aims_concern_findings is not None and not isinstance(self.aims_concern_findings, str):
            self.aims_concern_findings = str(self.aims_concern_findings)

        if self.aims_concern_escalation is not None and not isinstance(self.aims_concern_escalation, str):
            self.aims_concern_escalation = str(self.aims_concern_escalation)

        if self.aims_concern_response_due is not None and not isinstance(self.aims_concern_response_due, XSDDate):
            self.aims_concern_response_due = XSDDate(self.aims_concern_response_due)

        if self.aims_concern_responded_on is not None and not isinstance(self.aims_concern_responded_on, XSDDate):
            self.aims_concern_responded_on = XSDDate(self.aims_concern_responded_on)

        if self.aims_concern_resolution is not None and not isinstance(self.aims_concern_resolution, str):
            self.aims_concern_resolution = str(self.aims_concern_resolution)

        if self.aims_concern_reprisal_protection is not None and not isinstance(self.aims_concern_reprisal_protection, str):
            self.aims_concern_reprisal_protection = str(self.aims_concern_reprisal_protection)

        if not isinstance(self.aims_concern_incidents, list):
            self.aims_concern_incidents = [self.aims_concern_incidents] if self.aims_concern_incidents is not None else []
        self.aims_concern_incidents = [v if isinstance(v, AimsIncidentAimsId) else AimsIncidentAimsId(v) for v in self.aims_concern_incidents]

        if not isinstance(self.aims_concern_nonconformities, list):
            self.aims_concern_nonconformities = [self.aims_concern_nonconformities] if self.aims_concern_nonconformities is not None else []
        self.aims_concern_nonconformities = [v if isinstance(v, AimsNonconformityAimsId) else AimsNonconformityAimsId(v) for v in self.aims_concern_nonconformities]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class AimsClause(EnumDefinitionImpl):
    """
    The numbered clauses and subclauses of the standard from 4 to 10, by their numbers. A value's description is this
    project's own summary, and the clause headings and the requirements are ISO's.
    """
    clause_4 = PermissibleValue(
        text="clause_4",
        title="4",
        description="Why the system exists and what it reaches.")
    clause_4_1 = PermissibleValue(
        text="clause_4_1",
        title="4.1",
        description="""Matters inside and outside that bear on the system, climate among them, and the part the organization plays with AI.""")
    clause_4_2 = PermissibleValue(
        text="clause_4_2",
        title="4.2",
        description="Who has a stake in the system, and what they want from it.")
    clause_4_3 = PermissibleValue(
        text="clause_4_3",
        title="4.3",
        description="Where the system stops, stated in writing.")
    clause_4_4 = PermissibleValue(
        text="clause_4_4",
        title="4.4",
        description="Having the system and its processes in place, and keeping them up.")
    clause_5 = PermissibleValue(
        text="clause_5",
        title="5",
        description="What top management must do.")
    clause_5_1 = PermissibleValue(
        text="clause_5_1",
        title="5.1",
        description="How top management shows it leads and backs the system.")
    clause_5_2 = PermissibleValue(
        text="clause_5_2",
        title="5.2",
        description="Management's written direction on AI.")
    clause_5_3 = PermissibleValue(
        text="clause_5_3",
        title="5.3",
        description="""Who holds which duty and power, including who checks conformity and who reports on performance.""")
    clause_6 = PermissibleValue(
        text="clause_6",
        title="6",
        description="Deciding what to do before doing it.")
    clause_6_1 = PermissibleValue(
        text="clause_6_1",
        title="6.1",
        description="Dealing with what could go well or badly.")
    clause_6_1_1 = PermissibleValue(
        text="clause_6_1_1",
        title="6.1.1",
        description="Criteria for risk, and the actions planned on risks and opportunities.")
    clause_6_1_2 = PermissibleValue(
        text="clause_6_1_2",
        title="6.1.2",
        description="A repeatable way to find, analyse and rank AI risks.")
    clause_6_1_3 = PermissibleValue(
        text="clause_6_1_3",
        title="6.1.3",
        description="Choosing treatments and controls, with the Statement of Applicability and the plan.")
    clause_6_1_4 = PermissibleValue(
        text="clause_6_1_4",
        title="6.1.4",
        description="A way to work out what AI systems may do to people and society.")
    clause_6_2 = PermissibleValue(
        text="clause_6_2",
        title="6.2",
        description="Measurable aims for AI, and how each will be reached.")
    clause_6_3 = PermissibleValue(
        text="clause_6_3",
        title="6.3",
        description="Changing the system in an orderly way.")
    clause_7 = PermissibleValue(
        text="clause_7",
        title="7",
        description="What the system needs in order to run.")
    clause_7_1 = PermissibleValue(
        text="clause_7_1",
        title="7.1",
        description="Providing what the system needs.")
    clause_7_2 = PermissibleValue(
        text="clause_7_2",
        title="7.2",
        description="People's ability to do the work, and the evidence of it.")
    clause_7_3 = PermissibleValue(
        text="clause_7_3",
        title="7.3",
        description="What those who work for the organization must know.")
    clause_7_4 = PermissibleValue(
        text="clause_7_4",
        title="7.4",
        description="Who is told what, when and how.")
    clause_7_5 = PermissibleValue(
        text="clause_7_5",
        title="7.5",
        description="Keeping information under control.")
    clause_7_5_1 = PermissibleValue(
        text="clause_7_5_1",
        title="7.5.1",
        description="Which information the system holds.")
    clause_7_5_2 = PermissibleValue(
        text="clause_7_5_2",
        title="7.5.2",
        description="Naming, formatting, reviewing and approving it.")
    clause_7_5_3 = PermissibleValue(
        text="clause_7_5_3",
        title="7.5.3",
        description="Keeping it to hand and protected.")
    clause_8 = PermissibleValue(
        text="clause_8",
        title="8",
        description="Carrying out what was planned.")
    clause_8_1 = PermissibleValue(
        text="clause_8_1",
        title="8.1",
        description="Running and controlling the processes, including those from outside.")
    clause_8_2 = PermissibleValue(
        text="clause_8_2",
        title="8.2",
        description="Carrying out risk assessments, on schedule and when things change.")
    clause_8_3 = PermissibleValue(
        text="clause_8_3",
        title="8.3",
        description="Carrying out the treatment plan and checking that it works.")
    clause_8_4 = PermissibleValue(
        text="clause_8_4",
        title="8.4",
        description="Carrying out impact assessments, on schedule and when things change.")
    clause_9 = PermissibleValue(
        text="clause_9",
        title="9",
        description="Checking how the system is doing.")
    clause_9_1 = PermissibleValue(
        text="clause_9_1",
        title="9.1",
        description="What is measured, how and when, and what the results mean.")
    clause_9_2 = PermissibleValue(
        text="clause_9_2",
        title="9.2",
        description="Audits the organization runs on itself.")
    clause_9_2_1 = PermissibleValue(
        text="clause_9_2_1",
        title="9.2.1",
        description="What such an audit must establish, and how often.")
    clause_9_2_2 = PermissibleValue(
        text="clause_9_2_2",
        title="9.2.2",
        description="The plan for those audits, and how impartial they are.")
    clause_9_3 = PermissibleValue(
        text="clause_9_3",
        title="9.3",
        description="Top management's own look at the system.")
    clause_9_3_1 = PermissibleValue(
        text="clause_9_3_1",
        title="9.3.1",
        description="How often it looks, and to what end.")
    clause_9_3_2 = PermissibleValue(
        text="clause_9_3_2",
        title="9.3.2",
        description="What it must take in.")
    clause_9_3_3 = PermissibleValue(
        text="clause_9_3_3",
        title="9.3.3",
        description="What it must produce.")
    clause_10 = PermissibleValue(
        text="clause_10",
        title="10",
        description="Getting better and putting things right.")
    clause_10_1 = PermissibleValue(
        text="clause_10_1",
        title="10.1",
        description="Making the system better over time.")
    clause_10_2 = PermissibleValue(
        text="clause_10_2",
        title="10.2",
        description="Dealing with an unmet requirement and removing its cause.")

    _defn = EnumDefinition(
        name="AimsClause",
        description="""The numbered clauses and subclauses of the standard from 4 to 10, by their numbers. A value's description is this project's own summary, and the clause headings and the requirements are ISO's.""",
    )

class AimsControlArea(EnumDefinitionImpl):
    """
    The nine areas Annex A sorts its controls into, under names of this project's own. An area's number is its
    annotation.
    """
    policy_direction = PermissibleValue(
        text="policy_direction",
        title="A.2",
        description="Written direction from management on AI, and how it fits with other policies.")
    accountability = PermissibleValue(
        text="accountability",
        title="A.3",
        description="Who answers for AI within the organization's walls, and the way worries are raised.")
    system_resources = PermissibleValue(
        text="system_resources",
        title="A.4",
        description="What each AI system draws on: components, data, tools, computing and people.")
    impact_assessment = PermissibleValue(
        text="impact_assessment",
        title="A.5",
        description="Working out what AI systems may do to people and society.")
    system_life_cycle = PermissibleValue(
        text="system_life_cycle",
        title="A.6",
        description="Building and running AI systems, from the goals set for them to their logs.")
    data_management = PermissibleValue(
        text="data_management",
        title="A.7",
        description="The data AI systems use: how it is managed, obtained, kept fit, traced and readied.")
    stakeholder_information = PermissibleValue(
        text="stakeholder_information",
        title="A.8",
        description="What users and others are told about a system, and their way to report harm.")
    responsible_use = PermissibleValue(
        text="responsible_use",
        title="A.9",
        description="How AI systems are put to use, against the organization's goals and the systems' documents.")
    external_relationships = PermissibleValue(
        text="external_relationships",
        title="A.10",
        description="Duties shared with partners, suppliers and customers.")

    _defn = EnumDefinition(
        name="AimsControlArea",
        description="""The nine areas Annex A sorts its controls into, under names of this project's own. An area's number is its annotation.""",
    )

class AimsAnnexAControl(EnumDefinitionImpl):
    """
    The 38 reference controls of Annex A. A value's title holds the control's number and a name of this project's own,
    and its description says in this project's words what the control asks for. The headings and the control text are
    ISO's.
    """
    a_2_2 = PermissibleValue(
        text="a_2_2",
        title="A.2.2 Written direction on AI",
        description="Set down in writing how the organization means to treat AI systems.")
    a_2_3 = PermissibleValue(
        text="a_2_3",
        title="A.2.3 Fit with other policies",
        description="Find where the organization's other policies touch its aims for AI, in either direction.")
    a_2_4 = PermissibleValue(
        text="a_2_4",
        title="A.2.4 Regular policy check",
        description="""Look at the AI policy again on a schedule and whenever the need arises, to see that it still serves.""")
    a_3_2 = PermissibleValue(
        text="a_3_2",
        title="A.3.2 Who answers for what",
        description="Decide who carries which duty for AI, as the organization's needs dictate.")
    a_3_3 = PermissibleValue(
        text="a_3_3",
        title="A.3.3 A way to raise worries",
        description="""Give people a way to raise worries about the organization's part in a system, at any point in that system's life.""")
    a_4_2 = PermissibleValue(
        text="a_4_2",
        title="A.4.2 Inventory of what is needed",
        description="List what each stage of a system's life, and other AI work, draws on.")
    a_4_3 = PermissibleValue(
        text="a_4_3",
        title="A.4.3 Record of data used",
        description="Record facts about the data a system draws on.")
    a_4_4 = PermissibleValue(
        text="a_4_4",
        title="A.4.4 Record of tools used",
        description="Record facts about the tools a system draws on.")
    a_4_5 = PermissibleValue(
        text="a_4_5",
        title="A.4.5 Record of infrastructure used",
        description="Record facts about the hardware and computing a system draws on.")
    a_4_6 = PermissibleValue(
        text="a_4_6",
        title="A.4.6 Record of people used",
        description="Record who works on a system across its whole life, and what skills they bring.")
    a_5_2 = PermissibleValue(
        text="a_5_2",
        title="A.5.2 Method for weighing consequences",
        description="Set up a way to work out what a system could do to people and society over its life.")
    a_5_3 = PermissibleValue(
        text="a_5_3",
        title="A.5.3 Keeping assessment results",
        description="Write down what each impact assessment found, and hold on to it for a set time.")
    a_5_4 = PermissibleValue(
        text="a_5_4",
        title="A.5.4 Effects on people",
        description="""Work out and record how a system could affect single persons or particular groups over its life.""")
    a_5_5 = PermissibleValue(
        text="a_5_5",
        title="A.5.5 Effects on society",
        description="Work out and record how a system could affect society over its life.")
    a_6_1_2 = PermissibleValue(
        text="a_6_1_2",
        title="A.6.1.2 Goals for building",
        description="""Set goals that steer responsible building, and work measures for them into the development cycle.""")
    a_6_1_3 = PermissibleValue(
        text="a_6_1_3",
        title="A.6.1.3 Defined ways of building",
        description="Set down the particular processes for designing and building a system responsibly.")
    a_6_2_2 = PermissibleValue(
        text="a_6_2_2",
        title="A.6.2.2 What a system must do",
        description="Write down what a new system, or a large upgrade to one, must meet.")
    a_6_2_3 = PermissibleValue(
        text="a_6_2_3",
        title="A.6.2.3 Build records",
        description="Write down how a system was designed and built, against the goals and the requirements.")
    a_6_2_4 = PermissibleValue(
        text="a_6_2_4",
        title="A.6.2.4 Checks and their criteria",
        description="Set the checks that verify and validate a system, and say when each applies.")
    a_6_2_5 = PermissibleValue(
        text="a_6_2_5",
        title="A.6.2.5 Going live",
        description="Keep a plan for putting a system into service, and meet its conditions first.")
    a_6_2_6 = PermissibleValue(
        text="a_6_2_6",
        title="A.6.2.6 Running and watching",
        description="""Set down what keeping a system in service takes: at least watching it, fixing it, updating it and supporting it.""")
    a_6_2_7 = PermissibleValue(
        text="a_6_2_7",
        title="A.6.2.7 Documents per audience",
        description="""Decide what technical documents each kind of reader needs, and give them those documents in a suitable form.""")
    a_6_2_8 = PermissibleValue(
        text="a_6_2_8",
        title="A.6.2.8 Keeping logs",
        description="""Decide at which points in a system's life it keeps event logs, and keep them at least while it is in service.""")
    a_7_2 = PermissibleValue(
        text="a_7_2",
        title="A.7.2 Managing data for building",
        description="Set down and follow processes that manage the data used to build systems.")
    a_7_3 = PermissibleValue(
        text="a_7_3",
        title="A.7.3 Obtaining and choosing data",
        description="Record how the data a system uses was obtained and picked.")
    a_7_4 = PermissibleValue(
        text="a_7_4",
        title="A.7.4 Data fit for purpose",
        description="""State what quality data must have, and see that the data used to build and run a system has it.""")
    a_7_5 = PermissibleValue(
        text="a_7_5",
        title="A.7.5 Tracing where data came from",
        description="""Keep a process that records where data came from and what happened to it, while it and the system last.""")
    a_7_6 = PermissibleValue(
        text="a_7_6",
        title="A.7.6 Readying data",
        description="Set criteria for choosing how data is made ready, and name the methods to use.")
    a_8_2 = PermissibleValue(
        text="a_8_2",
        title="A.8.2 What users are told",
        description="Work out what those who use a system need to know, and tell them.")
    a_8_3 = PermissibleValue(
        text="a_8_3",
        title="A.8.3 Letting outsiders report harm",
        description="Give people outside the organization a way to report harm a system has done.")
    a_8_4 = PermissibleValue(
        text="a_8_4",
        title="A.8.4 Telling users about incidents",
        description="Keep a plan for telling those who use a system when something goes wrong.")
    a_8_5 = PermissibleValue(
        text="a_8_5",
        title="A.8.5 Duties to inform others",
        description="Work out what the organization owes others by way of reports about a system.")
    a_9_2 = PermissibleValue(
        text="a_9_2",
        title="A.9.2 Defined ways of using",
        description="Set down the processes for using AI systems responsibly.")
    a_9_3 = PermissibleValue(
        text="a_9_3",
        title="A.9.3 Goals for use",
        description="Set goals that steer how AI systems are used responsibly.")
    a_9_4 = PermissibleValue(
        text="a_9_4",
        title="A.9.4 Staying within documented use",
        description="See that a system is used only as intended and as its documents say.")
    a_10_2 = PermissibleValue(
        text="a_10_2",
        title="A.10.2 Sharing out duties",
        description="""Settle who carries which duty across a system's life, among the organization and those it deals with.""")
    a_10_3 = PermissibleValue(
        text="a_10_3",
        title="A.10.3 What is bought in",
        description="Keep a process that holds what suppliers provide to how the organization means to treat AI.")
    a_10_4 = PermissibleValue(
        text="a_10_4",
        title="A.10.4 Buyers' needs",
        description="See that how the organization treats AI takes account of what its customers expect and want.")

    _defn = EnumDefinition(
        name="AimsAnnexAControl",
        description="""The 38 reference controls of Annex A. A value's title holds the control's number and a name of this project's own, and its description says in this project's words what the control asks for. The headings and the control text are ISO's.""",
    )

class AimsLifecycleStage(EnumDefinitionImpl):
    """
    The eight stages of the generic life cycle model that ISO/IEC 22989:2022 gives, which ISO/IEC 42001 points to.
    """
    inception = PermissibleValue(
        text="inception",
        description="Someone sees a need, weighs whether to meet it, and sets goals.")
    design_and_development = PermissibleValue(
        text="design_and_development",
        description="The system is designed and built.")
    verification_and_validation = PermissibleValue(
        text="verification_and_validation",
        description="The system is checked against what was asked of it.")
    deployment = PermissibleValue(
        text="deployment",
        description="The system is put into service.")
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        description="The system runs and is watched.")
    continuous_validation = PermissibleValue(
        text="continuous_validation",
        description="A system that goes on learning is checked again as it changes.")
    re_evaluation = PermissibleValue(
        text="re_evaluation",
        description="The system's results are weighed against its goals afresh.")
    retirement = PermissibleValue(
        text="retirement",
        description="The system is taken out of service.")

    _defn = EnumDefinition(
        name="AimsLifecycleStage",
        description="""The eight stages of the generic life cycle model that ISO/IEC 22989:2022 gives, which ISO/IEC 42001 points to.""",
    )

class AimsAiRole(EnumDefinitionImpl):
    """
    The parts an organization or a person can play towards AI systems. The six families are those of ISO/IEC
    22989:2022, and each more specific role names its family in an annotation.
    """
    ai_provider = PermissibleValue(
        text="ai_provider",
        description="Offers AI systems or platforms to others.")
    ai_platform_provider = PermissibleValue(
        text="ai_platform_provider",
        description="Offers a platform that others build AI services on.")
    ai_product_or_service_provider = PermissibleValue(
        text="ai_product_or_service_provider",
        description="Offers goods or services that hold an AI system.")
    ai_producer = PermissibleValue(
        text="ai_producer",
        description="Makes AI systems.")
    ai_developer = PermissibleValue(
        text="ai_developer",
        description="Writes and trains what goes into a system.")
    ai_designer = PermissibleValue(
        text="ai_designer",
        description="Decides how a system should work.")
    ai_operator = PermissibleValue(
        text="ai_operator",
        description="Keeps a system running.")
    ai_tester_or_evaluator = PermissibleValue(
        text="ai_tester_or_evaluator",
        description="Checks how well a system does.")
    ai_deployer = PermissibleValue(
        text="ai_deployer",
        description="Puts a system into service.")
    ai_human_factor_professional = PermissibleValue(
        text="ai_human_factor_professional",
        description="Looks after how people and a system work together.")
    domain_expert = PermissibleValue(
        text="domain_expert",
        description="Knows the field a system is used in.")
    ai_impact_assessor = PermissibleValue(
        text="ai_impact_assessor",
        description="Weighs what a system may do to people and society.")
    procurer = PermissibleValue(
        text="procurer",
        description="Buys systems or their parts.")
    ai_governance_professional = PermissibleValue(
        text="ai_governance_professional",
        description="Oversees how AI is run and held to account.")
    ai_customer = PermissibleValue(
        text="ai_customer",
        description="Takes AI systems from a provider.")
    ai_user = PermissibleValue(
        text="ai_user",
        description="Works with a system directly.")
    ai_partner = PermissibleValue(
        text="ai_partner",
        description="Helps others make or run AI systems.")
    ai_system_integrator = PermissibleValue(
        text="ai_system_integrator",
        description="Joins a system to others.")
    data_provider = PermissibleValue(
        text="data_provider",
        description="Supplies data for a system.")
    ai_subject = PermissibleValue(
        text="ai_subject",
        description="Is affected by what a system decides or does.")
    data_subject = PermissibleValue(
        text="data_subject",
        description="Is someone a system's data is about.")
    other_subject = PermissibleValue(
        text="other_subject",
        description="Is affected in some other way.")
    relevant_authority = PermissibleValue(
        text="relevant_authority",
        description="Sets or enforces rules for AI.")
    policymaker = PermissibleValue(
        text="policymaker",
        description="Sets the rules.")
    regulator = PermissibleValue(
        text="regulator",
        description="Enforces the rules.")

    _defn = EnumDefinition(
        name="AimsAiRole",
        description="""The parts an organization or a person can play towards AI systems. The six families are those of ISO/IEC 22989:2022, and each more specific role names its family in an annotation.""",
    )

class AimsPiiRole(EnumDefinitionImpl):
    """
    The parts a party can play when personal data passes through AI, which ISO/IEC 29100 describes.
    """
    pii_controller = PermissibleValue(
        text="pii_controller",
        description="Decides why and how personal data is processed.")
    joint_pii_controller = PermissibleValue(
        text="joint_pii_controller",
        description="Makes those decisions together with another party.")
    pii_processor = PermissibleValue(
        text="pii_processor",
        description="Processes personal data on a controller's behalf.")

    _defn = EnumDefinition(
        name="AimsPiiRole",
        description="The parts a party can play when personal data passes through AI, which ISO/IEC 29100 describes.",
    )

class AimsObjectivePurpose(EnumDefinitionImpl):
    """
    What an AI objective is for. Clause 6.2 asks for objectives in general, and two Annex A controls ask for
    objectives of a narrower kind.
    """
    organizational = PermissibleValue(
        text="organizational",
        description="An objective for the whole system.")
    responsible_development = PermissibleValue(
        text="responsible_development",
        description="A goal that steers how systems are built.")
    responsible_use = PermissibleValue(
        text="responsible_use",
        description="A goal that steers how systems are used.")

    _defn = EnumDefinition(
        name="AimsObjectivePurpose",
        description="""What an AI objective is for. Clause 6.2 asks for objectives in general, and two Annex A controls ask for objectives of a narrower kind.""",
    )

class AimsObjectiveCategory(EnumDefinitionImpl):
    """
    Kinds of objective an organization may set for AI: those Annex C lists, two more from the guidance on responsible
    use, and other.
    """
    accountability = PermissibleValue(
        text="accountability",
        description="Someone stays answerable for what a system helps to do.")
    ai_expertise = PermissibleValue(
        text="ai_expertise",
        description="The organization has people with the skills AI calls for.")
    training_and_test_data = PermissibleValue(
        text="training_and_test_data",
        description="Good data to train and check a system is to hand.")
    environmental_impact = PermissibleValue(
        text="environmental_impact",
        description="A system's effect on the environment is kept in view.")
    fairness = PermissibleValue(
        text="fairness",
        description="Automated decisions do not wrong particular persons or groups.")
    maintainability = PermissibleValue(
        text="maintainability",
        description="Defects can be mended and new needs met.")
    privacy = PermissibleValue(
        text="privacy",
        description="Data about people, sensitive data above all, is neither misused nor exposed.")
    robustness = PermissibleValue(
        text="robustness",
        description="A system does as well on unseen data as on what it was trained on.")
    safety = PermissibleValue(
        text="safety",
        description="Nobody's life or health, and no property or part of nature, comes to harm.")
    security = PermissibleValue(
        text="security",
        description="Threats peculiar to AI are met, beyond the usual ones.")
    transparency_and_explainability = PermissibleValue(
        text="transparency_and_explainability",
        description="Those concerned can see how a system works and why it gave a result.")
    reliability = PermissibleValue(
        text="reliability",
        description="A system keeps doing what it is meant to.")
    accessibility = PermissibleValue(
        text="accessibility",
        description="A system can be used by people with differing abilities.")
    other = PermissibleValue(
        text="other",
        description="A kind of objective the organization sets for itself.")

    _defn = EnumDefinition(
        name="AimsObjectiveCategory",
        description="""Kinds of objective an organization may set for AI: those Annex C lists, two more from the guidance on responsible use, and other.""",
    )

class AimsRiskSourceCategory(EnumDefinitionImpl):
    """
    Kinds of source a risk from AI can come from: those Annex C lists, and other.
    """
    complex_environment = PermissibleValue(
        text="complex_environment",
        description="A system works where situations vary widely, so its results are less sure.")
    opaque_system = PermissibleValue(
        text="opaque_system",
        description="The organization cannot tell people enough about a system.")
    level_of_automation = PermissibleValue(
        text="level_of_automation",
        description="How much a system does alone, which bears on safety or fairness among others.")
    machine_learning = PermissibleValue(
        text="machine_learning",
        description="The data a model learns from, or how it was gathered, is flawed.")
    hardware = PermissibleValue(
        text="hardware",
        description="Faulty parts, or moving a trained model to other equipment.")
    life_cycle = PermissibleValue(
        text="life_cycle",
        description="Flaws anywhere in a system's life, from design to retirement.")
    technology_readiness = PermissibleValue(
        text="technology_readiness",
        description="A technology is too new to know well, or so old it breeds complacency.")
    other = PermissibleValue(
        text="other",
        description="A source the organization names for itself.")

    _defn = EnumDefinition(
        name="AimsRiskSourceCategory",
        description="Kinds of source a risk from AI can come from: those Annex C lists, and other.",
    )

class AimsImpactSubject(EnumDefinitionImpl):
    """
    Who an AI system's impact falls on.
    """
    individuals = PermissibleValue(
        text="individuals",
        description="Particular persons.")
    groups_of_individuals = PermissibleValue(
        text="groups_of_individuals",
        description="Groups of persons, such as children or workers.")
    societies = PermissibleValue(
        text="societies",
        description="Society at large.")

    _defn = EnumDefinition(
        name="AimsImpactSubject",
        description="Who an AI system's impact falls on.",
    )

class AimsImpactArea(EnumDefinitionImpl):
    """
    Areas where AI systems can touch people or society: those the guidance on impact assessment names as examples, and
    other.
    """
    fairness = PermissibleValue(
        text="fairness",
        description="Treating persons and groups even-handedly.")
    accountability = PermissibleValue(
        text="accountability",
        description="Someone staying answerable for the outcome.")
    transparency_and_explainability = PermissibleValue(
        text="transparency_and_explainability",
        description="Being able to see how a system works and why it gave a result.")
    security_and_privacy = PermissibleValue(
        text="security_and_privacy",
        description="Keeping people's information safe and private.")
    safety_and_health = PermissibleValue(
        text="safety_and_health",
        description="Physical and mental harm and wellbeing.")
    financial = PermissibleValue(
        text="financial",
        description="What people stand to gain or lose in money.")
    accessibility = PermissibleValue(
        text="accessibility",
        description="Whether people with differing abilities can use a system.")
    human_rights = PermissibleValue(
        text="human_rights",
        description="Rights everyone holds.")
    environmental_sustainability = PermissibleValue(
        text="environmental_sustainability",
        description="Natural resources and emissions.")
    economic = PermissibleValue(
        text="economic",
        description="Jobs, access to finance, taxes and trade.")
    government = PermissibleValue(
        text="government",
        description="Lawmaking, political falsehoods, defence of the state and the courts.")
    culture_and_values = PermissibleValue(
        text="culture_and_values",
        description="What a society holds to, and the biases a system can feed.")
    other = PermissibleValue(
        text="other",
        description="An area the organization names for itself.")

    _defn = EnumDefinition(
        name="AimsImpactArea",
        description="""Areas where AI systems can touch people or society: those the guidance on impact assessment names as examples, and other.""",
    )

class AimsImpactDirection(EnumDefinitionImpl):
    """
    Whether an impact helps or harms.
    """
    positive = PermissibleValue(
        text="positive",
        description="It helps.")
    negative = PermissibleValue(
        text="negative",
        description="It harms.")

    _defn = EnumDefinition(
        name="AimsImpactDirection",
        description="Whether an impact helps or harms.",
    )

class AimsResourceProvider(EnumDefinitionImpl):
    """
    Who provides a resource an AI system draws on.
    """
    organization = PermissibleValue(
        text="organization",
        description="The organization itself.")
    customer = PermissibleValue(
        text="customer",
        description="One of its customers.")
    third_party = PermissibleValue(
        text="third_party",
        description="Someone else.")

    _defn = EnumDefinition(
        name="AimsResourceProvider",
        description="Who provides a resource an AI system draws on.",
    )

class AimsDataCategory(EnumDefinitionImpl):
    """
    The parts data can play in machine learning.
    """
    training = PermissibleValue(
        text="training",
        description="Data a model learns from.")
    validation = PermissibleValue(
        text="validation",
        description="Data used to tune a model and compare versions of it.")
    test = PermissibleValue(
        text="test",
        description="Data held back to see how a finished model does.")
    production = PermissibleValue(
        text="production",
        description="Data a system meets in service.")

    _defn = EnumDefinition(
        name="AimsDataCategory",
        description="The parts data can play in machine learning.",
    )

class AimsDataPreparationMethod(EnumDefinitionImpl):
    """
    Common ways of making data ready for AI: those the guidance names, and other.
    """
    statistical_exploration = PermissibleValue(
        text="statistical_exploration",
        description="Looking at how the values are spread, and describing them.")
    cleaning = PermissibleValue(
        text="cleaning",
        description="Mending wrong values and dealing with gaps.")
    imputation = PermissibleValue(
        text="imputation",
        description="Filling gaps by a method.")
    normalization = PermissibleValue(
        text="normalization",
        description="Reshaping values to a common distribution or range.")
    scaling = PermissibleValue(
        text="scaling",
        description="Bringing values to comparable sizes.")
    labelling = PermissibleValue(
        text="labelling",
        description="Marking the values a model is to predict.")
    encoding = PermissibleValue(
        text="encoding",
        description="Turning categories into numbers.")
    other = PermissibleValue(
        text="other",
        description="A method the organization names for itself.")

    _defn = EnumDefinition(
        name="AimsDataPreparationMethod",
        description="Common ways of making data ready for AI: those the guidance names, and other.",
    )

class AimsAiThreat(EnumDefinitionImpl):
    """
    Threats to information security peculiar to AI: those the guidance names, and other.
    """
    data_poisoning = PermissibleValue(
        text="data_poisoning",
        description="Slipping bad data in to spoil what a model learns.")
    model_stealing = PermissibleValue(
        text="model_stealing",
        description="Copying a model by querying it or by taking it.")
    model_inversion = PermissibleValue(
        text="model_inversion",
        description="Working back from a model to the data it learned from.")
    other = PermissibleValue(
        text="other",
        description="A threat the organization names for itself.")

    _defn = EnumDefinition(
        name="AimsAiThreat",
        description="Threats to information security peculiar to AI: those the guidance names, and other.",
    )

class AimsImplementationStatus(EnumDefinitionImpl):
    """
    How far a control or a plan has been put into effect.
    """
    not_started = PermissibleValue(
        text="not_started",
        description="Nothing has been done yet.")
    planned = PermissibleValue(
        text="planned",
        description="The work is planned, with a timeline.")
    in_progress = PermissibleValue(
        text="in_progress",
        description="The work is under way.")
    implemented = PermissibleValue(
        text="implemented",
        description="The work is done and in operation.")

    _defn = EnumDefinition(
        name="AimsImplementationStatus",
        description="How far a control or a plan has been put into effect.",
    )

class AimsRiskTreatmentOption(EnumDefinitionImpl):
    """
    The ways of treating a risk, by the names ISO 31000 gives them.
    """
    modify = PermissibleValue(
        text="modify",
        description="Change the risk with controls that lower its likelihood or its consequences.")
    retain = PermissibleValue(
        text="retain",
        description="Keep the risk as it is, with management's approval.")
    avoid = PermissibleValue(
        text="avoid",
        description="Remove the risk by stopping or changing what gives rise to it.")
    share = PermissibleValue(
        text="share",
        description="Share the risk with another party, such as an insurer or a supplier.")

    _defn = EnumDefinition(
        name="AimsRiskTreatmentOption",
        description="The ways of treating a risk, by the names ISO 31000 gives them.",
    )

class AimsRiskLevel(EnumDefinitionImpl):
    """
    A five-point scale of risk level, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the
    organization.
    """
    very_low = PermissibleValue(
        text="very_low",
        description="Small enough to need no action.")
    low = PermissibleValue(
        text="low",
        description="Managed by routine procedures.")
    medium = PermissibleValue(
        text="medium",
        description="Needs management's attention and planned controls.")
    high = PermissibleValue(
        text="high",
        description="Needs treatment first and escalation.")
    critical = PermissibleValue(
        text="critical",
        description="Threatens the organization's objectives and needs action at once.")

    _defn = EnumDefinition(
        name="AimsRiskLevel",
        description="""A five-point scale of risk level, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.""",
    )

class AimsLikelihood(EnumDefinitionImpl):
    """
    A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the
    organization.
    """
    rare = PermissibleValue(
        text="rare",
        description="Not expected to happen.")
    unlikely = PermissibleValue(
        text="unlikely",
        description="Could happen, but is not expected to.")
    possible = PermissibleValue(
        text="possible",
        description="Might happen at some point.")
    likely = PermissibleValue(
        text="likely",
        description="Will probably happen.")
    almost_certain = PermissibleValue(
        text="almost_certain",
        description="Expected to happen.")

    _defn = EnumDefinition(
        name="AimsLikelihood",
        description="""A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.""",
    )

class AimsConsequence(EnumDefinitionImpl):
    """
    A five-point scale of consequence, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the
    organization.
    """
    negligible = PermissibleValue(
        text="negligible",
        description="No noticeable effect.")
    minor = PermissibleValue(
        text="minor",
        description="An effect normal operations absorb.")
    moderate = PermissibleValue(
        text="moderate",
        description="An effect that needs management to step in.")
    major = PermissibleValue(
        text="major",
        description="A serious effect on people, objectives or reputation.")
    severe = PermissibleValue(
        text="severe",
        description="An effect that threatens lives or the organization's survival.")

    _defn = EnumDefinition(
        name="AimsConsequence",
        description="""A five-point scale of consequence, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.""",
    )

class AimsDocumentKind(EnumDefinitionImpl):
    """
    The kinds of documented information an AimsDocumentedInformation record holds. Policies have records of their own.
    """
    procedure = PermissibleValue(
        text="procedure",
        description="The steps for carrying out an activity the same way each time.")
    standard = PermissibleValue(
        text="standard",
        description="Mandatory requirements for a technology or a process.")
    guideline = PermissibleValue(
        text="guideline",
        description="Recommended practice that supports a policy or a procedure.")
    record = PermissibleValue(
        text="record",
        description="Evidence of what was done or achieved.")
    plan = PermissibleValue(
        text="plan",
        description="How the organization means to reach an objective.")
    report = PermissibleValue(
        text="report",
        description="The formal output of an assessment, audit or review.")

    _defn = EnumDefinition(
        name="AimsDocumentKind",
        description="""The kinds of documented information an AimsDocumentedInformation record holds. Policies have records of their own.""",
    )

class AimsAuditType(EnumDefinitionImpl):
    """
    Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.
    """
    first_party = PermissibleValue(
        text="first_party",
        description="The organization audits itself, or someone audits it on its behalf.")
    second_party = PermissibleValue(
        text="second_party",
        description="A party with an interest in the organization audits it, such as a customer.")
    third_party = PermissibleValue(
        text="third_party",
        description="An independent body audits it, such as a certification body or a regulator.")

    _defn = EnumDefinition(
        name="AimsAuditType",
        description="Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.",
    )

class AimsAuditFindingType(EnumDefinitionImpl):
    """
    The kinds of audit finding.
    """
    major_nonconformity = PermissibleValue(
        text="major_nonconformity",
        description="A requirement not met in a way that puts the system's results in doubt.")
    minor_nonconformity = PermissibleValue(
        text="minor_nonconformity",
        description="A requirement not met in an isolated way that leaves its results in reach.")
    observation = PermissibleValue(
        text="observation",
        description="A condition that could lead to a nonconformity if left alone.")
    positive_finding = PermissibleValue(
        text="positive_finding",
        description="Evidence of practice that works well.")

    _defn = EnumDefinition(
        name="AimsAuditFindingType",
        description="The kinds of audit finding.",
    )

class AimsIncidentCategory(EnumDefinitionImpl):
    """
    What an incident involving an AI system concerns. ISO/IEC 42001 tells apart an incident of the system itself from
    one about security of information or about privacy.
    """
    ai_system = PermissibleValue(
        text="ai_system",
        description="The system itself misbehaved or failed.")
    information_security = PermissibleValue(
        text="information_security",
        description="Information was exposed, altered or made unavailable.")
    privacy = PermissibleValue(
        text="privacy",
        description="Personal data was exposed or misused.")
    safety = PermissibleValue(
        text="safety",
        description="Someone or something was put in danger.")
    other = PermissibleValue(
        text="other",
        description="Something the organization names for itself.")

    _defn = EnumDefinition(
        name="AimsIncidentCategory",
        description="""What an incident involving an AI system concerns. ISO/IEC 42001 tells apart an incident of the system itself from one about security of information or about privacy.""",
    )

class AimsManagementSystemStandard(EnumDefinitionImpl):
    """
    Management system standards Annex D names as ones to run this system beside, and other.
    """
    iso_iec_27001 = PermissibleValue(
        text="iso_iec_27001",
        description="Managing information security.")
    iso_iec_27701 = PermissibleValue(
        text="iso_iec_27701",
        description="Managing privacy of information.")
    iso_9001 = PermissibleValue(
        text="iso_9001",
        description="Managing quality.")
    iso_22000 = PermissibleValue(
        text="iso_22000",
        description="Managing food safety.")
    iso_13485 = PermissibleValue(
        text="iso_13485",
        description="Managing quality of medical devices.")
    other = PermissibleValue(
        text="other",
        description="Another management system standard, generic or for one sector.")

    _defn = EnumDefinition(
        name="AimsManagementSystemStandard",
        description="Management system standards Annex D names as ones to run this system beside, and other.",
    )

# Slots
class slots:
    pass

slots.aims_id = Slot(uri=ISO42001.aims_id, name="aims_id", curie=ISO42001.curie('aims_id'),
                   model_uri=ISO42001.aims_id, domain=None, range=URIRef)

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=ISO42001.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ISO42001.description, domain=None, range=Optional[str])

slots.aims_resource_type = Slot(uri=ISO42001.aims_resource_type, name="aims_resource_type", curie=ISO42001.curie('aims_resource_type'),
                   model_uri=ISO42001.aims_resource_type, domain=None, range=Optional[str])

slots.aims_responsible_role = Slot(uri=ISO42001.aims_responsible_role, name="aims_responsible_role", curie=ISO42001.curie('aims_responsible_role'),
                   model_uri=ISO42001.aims_responsible_role, domain=None, range=Optional[Union[str, AimsRoleAimsId]])

slots.aims_relevant_controls = Slot(uri=ISO42001.aims_relevant_controls, name="aims_relevant_controls", curie=ISO42001.curie('aims_relevant_controls'),
                   model_uri=ISO42001.aims_relevant_controls, domain=None, range=Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]])

slots.aims_ai_systems = Slot(uri=ISO42001.aims_ai_systems, name="aims_ai_systems", curie=ISO42001.curie('aims_ai_systems'),
                   model_uri=ISO42001.aims_ai_systems, domain=None, range=Optional[Union[Union[str, AimsAiSystemAimsId], list[Union[str, AimsAiSystemAimsId]]]])

slots.aims_implementation_state = Slot(uri=ISO42001.aims_implementation_state, name="aims_implementation_state", curie=ISO42001.curie('aims_implementation_state'),
                   model_uri=ISO42001.aims_implementation_state, domain=None, range=Optional[Union[str, "AimsImplementationStatus"]])

slots.aims_cited_clauses = Slot(uri=ISO42001.aims_cited_clauses, name="aims_cited_clauses", curie=ISO42001.curie('aims_cited_clauses'),
                   model_uri=ISO42001.aims_cited_clauses, domain=None, range=Optional[Union[Union[str, "AimsClause"], list[Union[str, "AimsClause"]]]])

slots.aims_cited_annex_a_controls = Slot(uri=ISO42001.aims_cited_annex_a_controls, name="aims_cited_annex_a_controls", curie=ISO42001.curie('aims_cited_annex_a_controls'),
                   model_uri=ISO42001.aims_cited_annex_a_controls, domain=None, range=Optional[Union[Union[str, "AimsAnnexAControl"], list[Union[str, "AimsAnnexAControl"]]]])

slots.aims_life_cycle_stages = Slot(uri=ISO42001.aims_life_cycle_stages, name="aims_life_cycle_stages", curie=ISO42001.curie('aims_life_cycle_stages'),
                   model_uri=ISO42001.aims_life_cycle_stages, domain=None, range=Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]])

slots.aims_entry_annex_a_control = Slot(uri=ISO42001.aims_entry_annex_a_control, name="aims_entry_annex_a_control", curie=ISO42001.curie('aims_entry_annex_a_control'),
                   model_uri=ISO42001.aims_entry_annex_a_control, domain=None, range=Optional[Union[str, "AimsAnnexAControl"]])

slots.aims_objective_categories = Slot(uri=ISO42001.aims_objective_categories, name="aims_objective_categories", curie=ISO42001.curie('aims_objective_categories'),
                   model_uri=ISO42001.aims_objective_categories, domain=None, range=Optional[Union[Union[str, "AimsObjectiveCategory"], list[Union[str, "AimsObjectiveCategory"]]]])

slots.aims_risk_source_categories = Slot(uri=ISO42001.aims_risk_source_categories, name="aims_risk_source_categories", curie=ISO42001.curie('aims_risk_source_categories'),
                   model_uri=ISO42001.aims_risk_source_categories, domain=None, range=Optional[Union[Union[str, "AimsRiskSourceCategory"], list[Union[str, "AimsRiskSourceCategory"]]]])

slots.aimsDocumentControlMixin__aims_document_reference = Slot(uri=ISO42001.aims_document_reference, name="aimsDocumentControlMixin__aims_document_reference", curie=ISO42001.curie('aims_document_reference'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_reference, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_version = Slot(uri=ISO42001.aims_document_version, name="aimsDocumentControlMixin__aims_document_version", curie=ISO42001.curie('aims_document_version'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_version, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_author = Slot(uri=ISO42001.aims_document_author, name="aimsDocumentControlMixin__aims_document_author", curie=ISO42001.curie('aims_document_author'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_author, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_owner = Slot(uri=ISO42001.aims_document_owner, name="aimsDocumentControlMixin__aims_document_owner", curie=ISO42001.curie('aims_document_owner'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_owner, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_format = Slot(uri=ISO42001.aims_document_format, name="aimsDocumentControlMixin__aims_document_format", curie=ISO42001.curie('aims_document_format'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_format, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_medium = Slot(uri=ISO42001.aims_document_medium, name="aimsDocumentControlMixin__aims_document_medium", curie=ISO42001.curie('aims_document_medium'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_medium, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_approver = Slot(uri=ISO42001.aims_document_approver, name="aimsDocumentControlMixin__aims_document_approver", curie=ISO42001.curie('aims_document_approver'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_approver, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_approval_date = Slot(uri=ISO42001.aims_document_approval_date, name="aimsDocumentControlMixin__aims_document_approval_date", curie=ISO42001.curie('aims_document_approval_date'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_approval_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsDocumentControlMixin__aims_document_effective_date = Slot(uri=ISO42001.aims_document_effective_date, name="aimsDocumentControlMixin__aims_document_effective_date", curie=ISO42001.curie('aims_document_effective_date'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsDocumentControlMixin__aims_document_last_review_date = Slot(uri=ISO42001.aims_document_last_review_date, name="aimsDocumentControlMixin__aims_document_last_review_date", curie=ISO42001.curie('aims_document_last_review_date'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_last_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsDocumentControlMixin__aims_document_next_review_date = Slot(uri=ISO42001.aims_document_next_review_date, name="aimsDocumentControlMixin__aims_document_next_review_date", curie=ISO42001.curie('aims_document_next_review_date'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_next_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsDocumentControlMixin__aims_document_status = Slot(uri=ISO42001.aims_document_status, name="aimsDocumentControlMixin__aims_document_status", curie=ISO42001.curie('aims_document_status'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_status, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_classification = Slot(uri=ISO42001.aims_document_classification, name="aimsDocumentControlMixin__aims_document_classification", curie=ISO42001.curie('aims_document_classification'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_classification, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_retention = Slot(uri=ISO42001.aims_document_retention, name="aimsDocumentControlMixin__aims_document_retention", curie=ISO42001.curie('aims_document_retention'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_retention, domain=None, range=Optional[Union[str, AimsDuration]])

slots.aimsDocumentControlMixin__aims_document_disposition = Slot(uri=ISO42001.aims_document_disposition, name="aimsDocumentControlMixin__aims_document_disposition", curie=ISO42001.curie('aims_document_disposition'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_disposition, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_distribution = Slot(uri=ISO42001.aims_document_distribution, name="aimsDocumentControlMixin__aims_document_distribution", curie=ISO42001.curie('aims_document_distribution'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDocumentControlMixin__aims_document_storage = Slot(uri=ISO42001.aims_document_storage, name="aimsDocumentControlMixin__aims_document_storage", curie=ISO42001.curie('aims_document_storage'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_storage, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_change_control = Slot(uri=ISO42001.aims_document_change_control, name="aimsDocumentControlMixin__aims_document_change_control", curie=ISO42001.curie('aims_document_change_control'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_change_control, domain=None, range=Optional[str])

slots.aimsDocumentControlMixin__aims_document_external_origin = Slot(uri=ISO42001.aims_document_external_origin, name="aimsDocumentControlMixin__aims_document_external_origin", curie=ISO42001.curie('aims_document_external_origin'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_external_origin, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsDocumentControlMixin__aims_document_external_source = Slot(uri=ISO42001.aims_document_external_source, name="aimsDocumentControlMixin__aims_document_external_source", curie=ISO42001.curie('aims_document_external_source'),
                   model_uri=ISO42001.aimsDocumentControlMixin__aims_document_external_source, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_organization = Slot(uri=ISO42001.aims_organization, name="aimsManagementSystem__aims_organization", curie=ISO42001.curie('aims_organization'),
                   model_uri=ISO42001.aimsManagementSystem__aims_organization, domain=None, range=Optional[Union[dict, AimsOrganization]])

slots.aimsManagementSystem__aims_top_management = Slot(uri=ISO42001.aims_top_management, name="aimsManagementSystem__aims_top_management", curie=ISO42001.curie('aims_top_management'),
                   model_uri=ISO42001.aimsManagementSystem__aims_top_management, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_governing_body = Slot(uri=ISO42001.aims_governing_body, name="aimsManagementSystem__aims_governing_body", curie=ISO42001.curie('aims_governing_body'),
                   model_uri=ISO42001.aimsManagementSystem__aims_governing_body, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_leadership_evidence = Slot(uri=ISO42001.aims_leadership_evidence, name="aimsManagementSystem__aims_leadership_evidence", curie=ISO42001.curie('aims_leadership_evidence'),
                   model_uri=ISO42001.aimsManagementSystem__aims_leadership_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_scope = Slot(uri=ISO42001.aims_scope, name="aimsManagementSystem__aims_scope", curie=ISO42001.curie('aims_scope'),
                   model_uri=ISO42001.aimsManagementSystem__aims_scope, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_scope_boundaries = Slot(uri=ISO42001.aims_scope_boundaries, name="aimsManagementSystem__aims_scope_boundaries", curie=ISO42001.curie('aims_scope_boundaries'),
                   model_uri=ISO42001.aimsManagementSystem__aims_scope_boundaries, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_scope_applicability = Slot(uri=ISO42001.aims_scope_applicability, name="aimsManagementSystem__aims_scope_applicability", curie=ISO42001.curie('aims_scope_applicability'),
                   model_uri=ISO42001.aimsManagementSystem__aims_scope_applicability, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_processes = Slot(uri=ISO42001.aims_processes, name="aimsManagementSystem__aims_processes", curie=ISO42001.curie('aims_processes'),
                   model_uri=ISO42001.aimsManagementSystem__aims_processes, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_internal_issues = Slot(uri=ISO42001.aims_internal_issues, name="aimsManagementSystem__aims_internal_issues", curie=ISO42001.curie('aims_internal_issues'),
                   model_uri=ISO42001.aimsManagementSystem__aims_internal_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_external_issues = Slot(uri=ISO42001.aims_external_issues, name="aimsManagementSystem__aims_external_issues", curie=ISO42001.curie('aims_external_issues'),
                   model_uri=ISO42001.aimsManagementSystem__aims_external_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_planned_changes = Slot(uri=ISO42001.aims_planned_changes, name="aimsManagementSystem__aims_planned_changes", curie=ISO42001.curie('aims_planned_changes'),
                   model_uri=ISO42001.aimsManagementSystem__aims_planned_changes, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_external_services = Slot(uri=ISO42001.aims_external_services, name="aimsManagementSystem__aims_external_services", curie=ISO42001.curie('aims_external_services'),
                   model_uri=ISO42001.aimsManagementSystem__aims_external_services, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementSystem__aims_integrated_standards = Slot(uri=ISO42001.aims_integrated_standards, name="aimsManagementSystem__aims_integrated_standards", curie=ISO42001.curie('aims_integrated_standards'),
                   model_uri=ISO42001.aimsManagementSystem__aims_integrated_standards, domain=None, range=Optional[Union[Union[str, "AimsManagementSystemStandard"], list[Union[str, "AimsManagementSystemStandard"]]]])

slots.aimsManagementSystem__aims_certification_status = Slot(uri=ISO42001.aims_certification_status, name="aimsManagementSystem__aims_certification_status", curie=ISO42001.curie('aims_certification_status'),
                   model_uri=ISO42001.aimsManagementSystem__aims_certification_status, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_certification_body = Slot(uri=ISO42001.aims_certification_body, name="aimsManagementSystem__aims_certification_body", curie=ISO42001.curie('aims_certification_body'),
                   model_uri=ISO42001.aimsManagementSystem__aims_certification_body, domain=None, range=Optional[str])

slots.aimsManagementSystem__aims_certification_date = Slot(uri=ISO42001.aims_certification_date, name="aimsManagementSystem__aims_certification_date", curie=ISO42001.curie('aims_certification_date'),
                   model_uri=ISO42001.aimsManagementSystem__aims_certification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsManagementSystem__aims_recertification_date = Slot(uri=ISO42001.aims_recertification_date, name="aimsManagementSystem__aims_recertification_date", curie=ISO42001.curie('aims_recertification_date'),
                   model_uri=ISO42001.aimsManagementSystem__aims_recertification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsManagementSystem__aims_interested_parties = Slot(uri=ISO42001.aims_interested_parties, name="aimsManagementSystem__aims_interested_parties", curie=ISO42001.curie('aims_interested_parties'),
                   model_uri=ISO42001.aimsManagementSystem__aims_interested_parties, domain=None, range=Optional[Union[dict[Union[str, AimsInterestedPartyAimsId], Union[dict, AimsInterestedParty]], list[Union[dict, AimsInterestedParty]]]])

slots.aimsManagementSystem__aims_policy = Slot(uri=ISO42001.aims_policy, name="aimsManagementSystem__aims_policy", curie=ISO42001.curie('aims_policy'),
                   model_uri=ISO42001.aimsManagementSystem__aims_policy, domain=None, range=Optional[Union[dict, AimsPolicy]])

slots.aimsManagementSystem__aims_topic_specific_policies = Slot(uri=ISO42001.aims_topic_specific_policies, name="aimsManagementSystem__aims_topic_specific_policies", curie=ISO42001.curie('aims_topic_specific_policies'),
                   model_uri=ISO42001.aimsManagementSystem__aims_topic_specific_policies, domain=None, range=Optional[Union[dict[Union[str, AimsTopicSpecificPolicyAimsId], Union[dict, AimsTopicSpecificPolicy]], list[Union[dict, AimsTopicSpecificPolicy]]]])

slots.aimsManagementSystem__aims_roles = Slot(uri=ISO42001.aims_roles, name="aimsManagementSystem__aims_roles", curie=ISO42001.curie('aims_roles'),
                   model_uri=ISO42001.aimsManagementSystem__aims_roles, domain=None, range=Optional[Union[dict[Union[str, AimsRoleAimsId], Union[dict, AimsRole]], list[Union[dict, AimsRole]]]])

slots.aimsManagementSystem__aims_objectives = Slot(uri=ISO42001.aims_objectives, name="aimsManagementSystem__aims_objectives", curie=ISO42001.curie('aims_objectives'),
                   model_uri=ISO42001.aimsManagementSystem__aims_objectives, domain=None, range=Optional[Union[dict[Union[str, AimsObjectiveAimsId], Union[dict, AimsObjective]], list[Union[dict, AimsObjective]]]])

slots.aimsManagementSystem__aims_planned_actions = Slot(uri=ISO42001.aims_planned_actions, name="aimsManagementSystem__aims_planned_actions", curie=ISO42001.curie('aims_planned_actions'),
                   model_uri=ISO42001.aimsManagementSystem__aims_planned_actions, domain=None, range=Optional[Union[dict[Union[str, AimsPlannedActionAimsId], Union[dict, AimsPlannedAction]], list[Union[dict, AimsPlannedAction]]]])

slots.aimsManagementSystem__aims_risk_assessment_process = Slot(uri=ISO42001.aims_risk_assessment_process, name="aimsManagementSystem__aims_risk_assessment_process", curie=ISO42001.curie('aims_risk_assessment_process'),
                   model_uri=ISO42001.aimsManagementSystem__aims_risk_assessment_process, domain=None, range=Optional[Union[dict, AimsRiskAssessmentProcess]])

slots.aimsManagementSystem__aims_risk_treatment_process = Slot(uri=ISO42001.aims_risk_treatment_process, name="aimsManagementSystem__aims_risk_treatment_process", curie=ISO42001.curie('aims_risk_treatment_process'),
                   model_uri=ISO42001.aimsManagementSystem__aims_risk_treatment_process, domain=None, range=Optional[Union[dict, AimsRiskTreatmentProcess]])

slots.aimsManagementSystem__aims_impact_assessment_process = Slot(uri=ISO42001.aims_impact_assessment_process, name="aimsManagementSystem__aims_impact_assessment_process", curie=ISO42001.curie('aims_impact_assessment_process'),
                   model_uri=ISO42001.aimsManagementSystem__aims_impact_assessment_process, domain=None, range=Optional[Union[dict, AimsImpactAssessmentProcess]])

slots.aimsManagementSystem__aims_risk_assessments = Slot(uri=ISO42001.aims_risk_assessments, name="aimsManagementSystem__aims_risk_assessments", curie=ISO42001.curie('aims_risk_assessments'),
                   model_uri=ISO42001.aimsManagementSystem__aims_risk_assessments, domain=None, range=Optional[Union[dict[Union[str, AimsRiskAssessmentAimsId], Union[dict, AimsRiskAssessment]], list[Union[dict, AimsRiskAssessment]]]])

slots.aimsManagementSystem__aims_risks = Slot(uri=ISO42001.aims_risks, name="aimsManagementSystem__aims_risks", curie=ISO42001.curie('aims_risks'),
                   model_uri=ISO42001.aimsManagementSystem__aims_risks, domain=None, range=Optional[Union[dict[Union[str, AimsRiskAimsId], Union[dict, AimsRisk]], list[Union[dict, AimsRisk]]]])

slots.aimsManagementSystem__aims_risk_treatment_plans = Slot(uri=ISO42001.aims_risk_treatment_plans, name="aimsManagementSystem__aims_risk_treatment_plans", curie=ISO42001.curie('aims_risk_treatment_plans'),
                   model_uri=ISO42001.aimsManagementSystem__aims_risk_treatment_plans, domain=None, range=Optional[Union[dict[Union[str, AimsRiskTreatmentPlanAimsId], Union[dict, AimsRiskTreatmentPlan]], list[Union[dict, AimsRiskTreatmentPlan]]]])

slots.aimsManagementSystem__aims_impact_assessments = Slot(uri=ISO42001.aims_impact_assessments, name="aimsManagementSystem__aims_impact_assessments", curie=ISO42001.curie('aims_impact_assessments'),
                   model_uri=ISO42001.aimsManagementSystem__aims_impact_assessments, domain=None, range=Optional[Union[dict[Union[str, AimsImpactAssessmentAimsId], Union[dict, AimsImpactAssessment]], list[Union[dict, AimsImpactAssessment]]]])

slots.aimsManagementSystem__aims_statement_of_applicability = Slot(uri=ISO42001.aims_statement_of_applicability, name="aimsManagementSystem__aims_statement_of_applicability", curie=ISO42001.curie('aims_statement_of_applicability'),
                   model_uri=ISO42001.aimsManagementSystem__aims_statement_of_applicability, domain=None, range=Optional[Union[dict, AimsStatementOfApplicability]])

slots.aimsManagementSystem__aims_controls = Slot(uri=ISO42001.aims_controls, name="aimsManagementSystem__aims_controls", curie=ISO42001.curie('aims_controls'),
                   model_uri=ISO42001.aimsManagementSystem__aims_controls, domain=None, range=Optional[Union[dict[Union[str, AimsControlAimsId], Union[dict, AimsControl]], list[Union[dict, AimsControl]]]])

slots.aimsManagementSystem__aims_systems = Slot(uri=ISO42001.aims_systems, name="aimsManagementSystem__aims_systems", curie=ISO42001.curie('aims_systems'),
                   model_uri=ISO42001.aimsManagementSystem__aims_systems, domain=None, range=Optional[Union[dict[Union[str, AimsAiSystemAimsId], Union[dict, AimsAiSystem]], list[Union[dict, AimsAiSystem]]]])

slots.aimsManagementSystem__aims_system_resources = Slot(uri=ISO42001.aims_system_resources, name="aimsManagementSystem__aims_system_resources", curie=ISO42001.curie('aims_system_resources'),
                   model_uri=ISO42001.aimsManagementSystem__aims_system_resources, domain=None, range=Optional[Union[dict[Union[str, AimsSystemResourceAimsId], Union[dict, AimsSystemResource]], list[Union[dict, AimsSystemResource]]]])

slots.aimsManagementSystem__aims_development_processes = Slot(uri=ISO42001.aims_development_processes, name="aimsManagementSystem__aims_development_processes", curie=ISO42001.curie('aims_development_processes'),
                   model_uri=ISO42001.aimsManagementSystem__aims_development_processes, domain=None, range=Optional[Union[dict[Union[str, AimsDevelopmentProcessAimsId], Union[dict, AimsDevelopmentProcess]], list[Union[dict, AimsDevelopmentProcess]]]])

slots.aimsManagementSystem__aims_use_processes = Slot(uri=ISO42001.aims_use_processes, name="aimsManagementSystem__aims_use_processes", curie=ISO42001.curie('aims_use_processes'),
                   model_uri=ISO42001.aimsManagementSystem__aims_use_processes, domain=None, range=Optional[Union[dict[Union[str, AimsResponsibleUseProcessAimsId], Union[dict, AimsResponsibleUseProcess]], list[Union[dict, AimsResponsibleUseProcess]]]])

slots.aimsManagementSystem__aims_technical_documentation = Slot(uri=ISO42001.aims_technical_documentation, name="aimsManagementSystem__aims_technical_documentation", curie=ISO42001.curie('aims_technical_documentation'),
                   model_uri=ISO42001.aimsManagementSystem__aims_technical_documentation, domain=None, range=Optional[Union[dict[Union[str, AimsTechnicalDocumentationAimsId], Union[dict, AimsTechnicalDocumentation]], list[Union[dict, AimsTechnicalDocumentation]]]])

slots.aimsManagementSystem__aims_user_information = Slot(uri=ISO42001.aims_user_information, name="aimsManagementSystem__aims_user_information", curie=ISO42001.curie('aims_user_information'),
                   model_uri=ISO42001.aimsManagementSystem__aims_user_information, domain=None, range=Optional[Union[dict[Union[str, AimsUserInformationAimsId], Union[dict, AimsUserInformation]], list[Union[dict, AimsUserInformation]]]])

slots.aimsManagementSystem__aims_incident_communication_plans = Slot(uri=ISO42001.aims_incident_communication_plans, name="aimsManagementSystem__aims_incident_communication_plans", curie=ISO42001.curie('aims_incident_communication_plans'),
                   model_uri=ISO42001.aimsManagementSystem__aims_incident_communication_plans, domain=None, range=Optional[Union[dict[Union[str, AimsIncidentCommunicationPlanAimsId], Union[dict, AimsIncidentCommunicationPlan]], list[Union[dict, AimsIncidentCommunicationPlan]]]])

slots.aimsManagementSystem__aims_reporting_obligations = Slot(uri=ISO42001.aims_reporting_obligations, name="aimsManagementSystem__aims_reporting_obligations", curie=ISO42001.curie('aims_reporting_obligations'),
                   model_uri=ISO42001.aimsManagementSystem__aims_reporting_obligations, domain=None, range=Optional[Union[dict[Union[str, AimsReportingObligationAimsId], Union[dict, AimsReportingObligation]], list[Union[dict, AimsReportingObligation]]]])

slots.aimsManagementSystem__aims_third_party_relationships = Slot(uri=ISO42001.aims_third_party_relationships, name="aimsManagementSystem__aims_third_party_relationships", curie=ISO42001.curie('aims_third_party_relationships'),
                   model_uri=ISO42001.aimsManagementSystem__aims_third_party_relationships, domain=None, range=Optional[Union[dict[Union[str, AimsThirdPartyRelationshipAimsId], Union[dict, AimsThirdPartyRelationship]], list[Union[dict, AimsThirdPartyRelationship]]]])

slots.aimsManagementSystem__aims_resources = Slot(uri=ISO42001.aims_resources, name="aimsManagementSystem__aims_resources", curie=ISO42001.curie('aims_resources'),
                   model_uri=ISO42001.aimsManagementSystem__aims_resources, domain=None, range=Optional[Union[dict[Union[str, AimsResourceAimsId], Union[dict, AimsResource]], list[Union[dict, AimsResource]]]])

slots.aimsManagementSystem__aims_competence_records = Slot(uri=ISO42001.aims_competence_records, name="aimsManagementSystem__aims_competence_records", curie=ISO42001.curie('aims_competence_records'),
                   model_uri=ISO42001.aimsManagementSystem__aims_competence_records, domain=None, range=Optional[Union[dict[Union[str, AimsCompetenceRecordAimsId], Union[dict, AimsCompetenceRecord]], list[Union[dict, AimsCompetenceRecord]]]])

slots.aimsManagementSystem__aims_awareness_programme = Slot(uri=ISO42001.aims_awareness_programme, name="aimsManagementSystem__aims_awareness_programme", curie=ISO42001.curie('aims_awareness_programme'),
                   model_uri=ISO42001.aimsManagementSystem__aims_awareness_programme, domain=None, range=Optional[Union[dict, AimsAwarenessProgramme]])

slots.aimsManagementSystem__aims_communication_plan = Slot(uri=ISO42001.aims_communication_plan, name="aimsManagementSystem__aims_communication_plan", curie=ISO42001.curie('aims_communication_plan'),
                   model_uri=ISO42001.aimsManagementSystem__aims_communication_plan, domain=None, range=Optional[Union[dict, AimsCommunicationPlan]])

slots.aimsManagementSystem__aims_documented_information = Slot(uri=ISO42001.aims_documented_information, name="aimsManagementSystem__aims_documented_information", curie=ISO42001.curie('aims_documented_information'),
                   model_uri=ISO42001.aimsManagementSystem__aims_documented_information, domain=None, range=Optional[Union[dict[Union[str, AimsDocumentedInformationAimsId], Union[dict, AimsDocumentedInformation]], list[Union[dict, AimsDocumentedInformation]]]])

slots.aimsManagementSystem__aims_operational_procedures = Slot(uri=ISO42001.aims_operational_procedures, name="aimsManagementSystem__aims_operational_procedures", curie=ISO42001.curie('aims_operational_procedures'),
                   model_uri=ISO42001.aimsManagementSystem__aims_operational_procedures, domain=None, range=Optional[Union[dict[Union[str, AimsOperationalProcedureAimsId], Union[dict, AimsOperationalProcedure]], list[Union[dict, AimsOperationalProcedure]]]])

slots.aimsManagementSystem__aims_monitoring_programme = Slot(uri=ISO42001.aims_monitoring_programme, name="aimsManagementSystem__aims_monitoring_programme", curie=ISO42001.curie('aims_monitoring_programme'),
                   model_uri=ISO42001.aimsManagementSystem__aims_monitoring_programme, domain=None, range=Optional[Union[dict, AimsMonitoringProgramme]])

slots.aimsManagementSystem__aims_audit_programmes = Slot(uri=ISO42001.aims_audit_programmes, name="aimsManagementSystem__aims_audit_programmes", curie=ISO42001.curie('aims_audit_programmes'),
                   model_uri=ISO42001.aimsManagementSystem__aims_audit_programmes, domain=None, range=Optional[Union[dict[Union[str, AimsAuditProgrammeAimsId], Union[dict, AimsAuditProgramme]], list[Union[dict, AimsAuditProgramme]]]])

slots.aimsManagementSystem__aims_audits = Slot(uri=ISO42001.aims_audits, name="aimsManagementSystem__aims_audits", curie=ISO42001.curie('aims_audits'),
                   model_uri=ISO42001.aimsManagementSystem__aims_audits, domain=None, range=Optional[Union[dict[Union[str, AimsAuditAimsId], Union[dict, AimsAudit]], list[Union[dict, AimsAudit]]]])

slots.aimsManagementSystem__aims_management_reviews = Slot(uri=ISO42001.aims_management_reviews, name="aimsManagementSystem__aims_management_reviews", curie=ISO42001.curie('aims_management_reviews'),
                   model_uri=ISO42001.aimsManagementSystem__aims_management_reviews, domain=None, range=Optional[Union[dict[Union[str, AimsManagementReviewAimsId], Union[dict, AimsManagementReview]], list[Union[dict, AimsManagementReview]]]])

slots.aimsManagementSystem__aims_nonconformities = Slot(uri=ISO42001.aims_nonconformities, name="aimsManagementSystem__aims_nonconformities", curie=ISO42001.curie('aims_nonconformities'),
                   model_uri=ISO42001.aimsManagementSystem__aims_nonconformities, domain=None, range=Optional[Union[dict[Union[str, AimsNonconformityAimsId], Union[dict, AimsNonconformity]], list[Union[dict, AimsNonconformity]]]])

slots.aimsManagementSystem__aims_corrective_actions = Slot(uri=ISO42001.aims_corrective_actions, name="aimsManagementSystem__aims_corrective_actions", curie=ISO42001.curie('aims_corrective_actions'),
                   model_uri=ISO42001.aimsManagementSystem__aims_corrective_actions, domain=None, range=Optional[Union[dict[Union[str, AimsCorrectiveActionAimsId], Union[dict, AimsCorrectiveAction]], list[Union[dict, AimsCorrectiveAction]]]])

slots.aimsManagementSystem__aims_improvements = Slot(uri=ISO42001.aims_improvements, name="aimsManagementSystem__aims_improvements", curie=ISO42001.curie('aims_improvements'),
                   model_uri=ISO42001.aimsManagementSystem__aims_improvements, domain=None, range=Optional[Union[dict[Union[str, AimsImprovementOpportunityAimsId], Union[dict, AimsImprovementOpportunity]], list[Union[dict, AimsImprovementOpportunity]]]])

slots.aimsManagementSystem__aims_system_events = Slot(uri=ISO42001.aims_system_events, name="aimsManagementSystem__aims_system_events", curie=ISO42001.curie('aims_system_events'),
                   model_uri=ISO42001.aimsManagementSystem__aims_system_events, domain=None, range=Optional[Union[dict[Union[str, AimsSystemEventAimsId], Union[dict, AimsSystemEvent]], list[Union[dict, AimsSystemEvent]]]])

slots.aimsManagementSystem__aims_concern_reporting_process = Slot(uri=ISO42001.aims_concern_reporting_process, name="aimsManagementSystem__aims_concern_reporting_process", curie=ISO42001.curie('aims_concern_reporting_process'),
                   model_uri=ISO42001.aimsManagementSystem__aims_concern_reporting_process, domain=None, range=Optional[Union[dict, AimsConcernReportingProcess]])

slots.aimsManagementSystem__aims_concern_reports = Slot(uri=ISO42001.aims_concern_reports, name="aimsManagementSystem__aims_concern_reports", curie=ISO42001.curie('aims_concern_reports'),
                   model_uri=ISO42001.aimsManagementSystem__aims_concern_reports, domain=None, range=Optional[Union[dict[Union[str, AimsConcernReportAimsId], Union[dict, AimsConcernReport]], list[Union[dict, AimsConcernReport]]]])

slots.aimsOrganization__aims_organization_legal_name = Slot(uri=ISO42001.aims_organization_legal_name, name="aimsOrganization__aims_organization_legal_name", curie=ISO42001.curie('aims_organization_legal_name'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_legal_name, domain=None, range=Optional[str])

slots.aimsOrganization__aims_organization_trading_names = Slot(uri=ISO42001.aims_organization_trading_names, name="aimsOrganization__aims_organization_trading_names", curie=ISO42001.curie('aims_organization_trading_names'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_trading_names, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsOrganization__aims_organization_kind = Slot(uri=ISO42001.aims_organization_kind, name="aimsOrganization__aims_organization_kind", curie=ISO42001.curie('aims_organization_kind'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_kind, domain=None, range=Optional[str])

slots.aimsOrganization__aims_organization_sectors = Slot(uri=ISO42001.aims_organization_sectors, name="aimsOrganization__aims_organization_sectors", curie=ISO42001.curie('aims_organization_sectors'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_sectors, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsOrganization__aims_organization_size = Slot(uri=ISO42001.aims_organization_size, name="aimsOrganization__aims_organization_size", curie=ISO42001.curie('aims_organization_size'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_size, domain=None, range=Optional[str])

slots.aimsOrganization__aims_organization_employee_count = Slot(uri=ISO42001.aims_organization_employee_count, name="aimsOrganization__aims_organization_employee_count", curie=ISO42001.curie('aims_organization_employee_count'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_employee_count, domain=None, range=Optional[int])

slots.aimsOrganization__aims_organization_locations = Slot(uri=ISO42001.aims_organization_locations, name="aimsOrganization__aims_organization_locations", curie=ISO42001.curie('aims_organization_locations'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_locations, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsOrganization__aims_organization_jurisdictions = Slot(uri=ISO42001.aims_organization_jurisdictions, name="aimsOrganization__aims_organization_jurisdictions", curie=ISO42001.curie('aims_organization_jurisdictions'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsOrganization__aims_organization_parent = Slot(uri=ISO42001.aims_organization_parent, name="aimsOrganization__aims_organization_parent", curie=ISO42001.curie('aims_organization_parent'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_parent, domain=None, range=Optional[str])

slots.aimsOrganization__aims_organization_subsidiaries = Slot(uri=ISO42001.aims_organization_subsidiaries, name="aimsOrganization__aims_organization_subsidiaries", curie=ISO42001.curie('aims_organization_subsidiaries'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_subsidiaries, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsOrganization__aims_organization_ai_roles = Slot(uri=ISO42001.aims_organization_ai_roles, name="aimsOrganization__aims_organization_ai_roles", curie=ISO42001.curie('aims_organization_ai_roles'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_ai_roles, domain=None, range=Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]])

slots.aimsOrganization__aims_organization_pii_roles = Slot(uri=ISO42001.aims_organization_pii_roles, name="aimsOrganization__aims_organization_pii_roles", curie=ISO42001.curie('aims_organization_pii_roles'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_pii_roles, domain=None, range=Optional[Union[Union[str, "AimsPiiRole"], list[Union[str, "AimsPiiRole"]]]])

slots.aimsOrganization__aims_organization_climate_change_relevant = Slot(uri=ISO42001.aims_organization_climate_change_relevant, name="aimsOrganization__aims_organization_climate_change_relevant", curie=ISO42001.curie('aims_organization_climate_change_relevant'),
                   model_uri=ISO42001.aimsOrganization__aims_organization_climate_change_relevant, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsInterestedParty__aims_party_category = Slot(uri=ISO42001.aims_party_category, name="aimsInterestedParty__aims_party_category", curie=ISO42001.curie('aims_party_category'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_category, domain=None, range=Optional[str])

slots.aimsInterestedParty__aims_party_ai_roles = Slot(uri=ISO42001.aims_party_ai_roles, name="aimsInterestedParty__aims_party_ai_roles", curie=ISO42001.curie('aims_party_ai_roles'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_ai_roles, domain=None, range=Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]])

slots.aimsInterestedParty__aims_party_relationship = Slot(uri=ISO42001.aims_party_relationship, name="aimsInterestedParty__aims_party_relationship", curie=ISO42001.curie('aims_party_relationship'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_relationship, domain=None, range=Optional[str])

slots.aimsInterestedParty__aims_party_requirements = Slot(uri=ISO42001.aims_party_requirements, name="aimsInterestedParty__aims_party_requirements", curie=ISO42001.curie('aims_party_requirements'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsInterestedParty__aims_party_addressed_requirements = Slot(uri=ISO42001.aims_party_addressed_requirements, name="aimsInterestedParty__aims_party_addressed_requirements", curie=ISO42001.curie('aims_party_addressed_requirements'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_addressed_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsInterestedParty__aims_party_climate_change_requirements = Slot(uri=ISO42001.aims_party_climate_change_requirements, name="aimsInterestedParty__aims_party_climate_change_requirements", curie=ISO42001.curie('aims_party_climate_change_requirements'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_climate_change_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsInterestedParty__aims_party_communication_needs = Slot(uri=ISO42001.aims_party_communication_needs, name="aimsInterestedParty__aims_party_communication_needs", curie=ISO42001.curie('aims_party_communication_needs'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_communication_needs, domain=None, range=Optional[str])

slots.aimsInterestedParty__aims_party_contact = Slot(uri=ISO42001.aims_party_contact, name="aimsInterestedParty__aims_party_contact", curie=ISO42001.curie('aims_party_contact'),
                   model_uri=ISO42001.aimsInterestedParty__aims_party_contact, domain=None, range=Optional[str])

slots.aimsPolicy__aims_policy_statement = Slot(uri=ISO42001.aims_policy_statement, name="aimsPolicy__aims_policy_statement", curie=ISO42001.curie('aims_policy_statement'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_statement, domain=None, range=Optional[str])

slots.aimsPolicy__aims_policy_objectives_framework = Slot(uri=ISO42001.aims_policy_objectives_framework, name="aimsPolicy__aims_policy_objectives_framework", curie=ISO42001.curie('aims_policy_objectives_framework'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_objectives_framework, domain=None, range=Optional[str])

slots.aimsPolicy__aims_policy_commitments = Slot(uri=ISO42001.aims_policy_commitments, name="aimsPolicy__aims_policy_commitments", curie=ISO42001.curie('aims_policy_commitments'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_commitments, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsPolicy__aims_policy_principles = Slot(uri=ISO42001.aims_policy_principles, name="aimsPolicy__aims_policy_principles", curie=ISO42001.curie('aims_policy_principles'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_principles, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsPolicy__aims_policy_exceptions_process = Slot(uri=ISO42001.aims_policy_exceptions_process, name="aimsPolicy__aims_policy_exceptions_process", curie=ISO42001.curie('aims_policy_exceptions_process'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_exceptions_process, domain=None, range=Optional[str])

slots.aimsPolicy__aims_policy_influences = Slot(uri=ISO42001.aims_policy_influences, name="aimsPolicy__aims_policy_influences", curie=ISO42001.curie('aims_policy_influences'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_influences, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsPolicy__aims_policy_related_policies = Slot(uri=ISO42001.aims_policy_related_policies, name="aimsPolicy__aims_policy_related_policies", curie=ISO42001.curie('aims_policy_related_policies'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_related_policies, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsPolicy__aims_policy_communication_date = Slot(uri=ISO42001.aims_policy_communication_date, name="aimsPolicy__aims_policy_communication_date", curie=ISO42001.curie('aims_policy_communication_date'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_communication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsPolicy__aims_policy_availability = Slot(uri=ISO42001.aims_policy_availability, name="aimsPolicy__aims_policy_availability", curie=ISO42001.curie('aims_policy_availability'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_availability, domain=None, range=Optional[str])

slots.aimsPolicy__aims_policy_review_role = Slot(uri=ISO42001.aims_policy_review_role, name="aimsPolicy__aims_policy_review_role", curie=ISO42001.curie('aims_policy_review_role'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_review_role, domain=None, range=Optional[Union[str, AimsRoleAimsId]])

slots.aimsPolicy__aims_policy_review_interval = Slot(uri=ISO42001.aims_policy_review_interval, name="aimsPolicy__aims_policy_review_interval", curie=ISO42001.curie('aims_policy_review_interval'),
                   model_uri=ISO42001.aimsPolicy__aims_policy_review_interval, domain=None, range=Optional[Union[str, AimsDuration]])

slots.aimsTopicSpecificPolicy__aims_topic_policy_topic = Slot(uri=ISO42001.aims_topic_policy_topic, name="aimsTopicSpecificPolicy__aims_topic_policy_topic", curie=ISO42001.curie('aims_topic_policy_topic'),
                   model_uri=ISO42001.aimsTopicSpecificPolicy__aims_topic_policy_topic, domain=None, range=Optional[str])

slots.aimsTopicSpecificPolicy__aims_topic_policy_parent = Slot(uri=ISO42001.aims_topic_policy_parent, name="aimsTopicSpecificPolicy__aims_topic_policy_parent", curie=ISO42001.curie('aims_topic_policy_parent'),
                   model_uri=ISO42001.aimsTopicSpecificPolicy__aims_topic_policy_parent, domain=None, range=Optional[Union[str, AimsPolicyAimsId]])

slots.aimsTopicSpecificPolicy__aims_topic_policy_audience = Slot(uri=ISO42001.aims_topic_policy_audience, name="aimsTopicSpecificPolicy__aims_topic_policy_audience", curie=ISO42001.curie('aims_topic_policy_audience'),
                   model_uri=ISO42001.aimsTopicSpecificPolicy__aims_topic_policy_audience, domain=None, range=Optional[str])

slots.aimsRole__aims_role_category = Slot(uri=ISO42001.aims_role_category, name="aimsRole__aims_role_category", curie=ISO42001.curie('aims_role_category'),
                   model_uri=ISO42001.aimsRole__aims_role_category, domain=None, range=Optional[str])

slots.aimsRole__aims_role_areas = Slot(uri=ISO42001.aims_role_areas, name="aimsRole__aims_role_areas", curie=ISO42001.curie('aims_role_areas'),
                   model_uri=ISO42001.aimsRole__aims_role_areas, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRole__aims_role_responsibilities = Slot(uri=ISO42001.aims_role_responsibilities, name="aimsRole__aims_role_responsibilities", curie=ISO42001.curie('aims_role_responsibilities'),
                   model_uri=ISO42001.aimsRole__aims_role_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRole__aims_role_authorities = Slot(uri=ISO42001.aims_role_authorities, name="aimsRole__aims_role_authorities", curie=ISO42001.curie('aims_role_authorities'),
                   model_uri=ISO42001.aimsRole__aims_role_authorities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRole__aims_role_ensures_conformity = Slot(uri=ISO42001.aims_role_ensures_conformity, name="aimsRole__aims_role_ensures_conformity", curie=ISO42001.curie('aims_role_ensures_conformity'),
                   model_uri=ISO42001.aimsRole__aims_role_ensures_conformity, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsRole__aims_role_reports_performance = Slot(uri=ISO42001.aims_role_reports_performance, name="aimsRole__aims_role_reports_performance", curie=ISO42001.curie('aims_role_reports_performance'),
                   model_uri=ISO42001.aimsRole__aims_role_reports_performance, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsRole__aims_role_accountability = Slot(uri=ISO42001.aims_role_accountability, name="aimsRole__aims_role_accountability", curie=ISO42001.curie('aims_role_accountability'),
                   model_uri=ISO42001.aimsRole__aims_role_accountability, domain=None, range=Optional[str])

slots.aimsRole__aims_role_holders = Slot(uri=ISO42001.aims_role_holders, name="aimsRole__aims_role_holders", curie=ISO42001.curie('aims_role_holders'),
                   model_uri=ISO42001.aimsRole__aims_role_holders, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRole__aims_role_delegation = Slot(uri=ISO42001.aims_role_delegation, name="aimsRole__aims_role_delegation", curie=ISO42001.curie('aims_role_delegation'),
                   model_uri=ISO42001.aimsRole__aims_role_delegation, domain=None, range=Optional[str])

slots.aimsRole__aims_role_reports_to = Slot(uri=ISO42001.aims_role_reports_to, name="aimsRole__aims_role_reports_to", curie=ISO42001.curie('aims_role_reports_to'),
                   model_uri=ISO42001.aimsRole__aims_role_reports_to, domain=None, range=Optional[Union[str, AimsRoleAimsId]])

slots.aimsObjective__aims_objective_purpose = Slot(uri=ISO42001.aims_objective_purpose, name="aimsObjective__aims_objective_purpose", curie=ISO42001.curie('aims_objective_purpose'),
                   model_uri=ISO42001.aimsObjective__aims_objective_purpose, domain=None, range=Optional[Union[str, "AimsObjectivePurpose"]])

slots.aimsObjective__aims_objective_statement = Slot(uri=ISO42001.aims_objective_statement, name="aimsObjective__aims_objective_statement", curie=ISO42001.curie('aims_objective_statement'),
                   model_uri=ISO42001.aimsObjective__aims_objective_statement, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_target = Slot(uri=ISO42001.aims_objective_target, name="aimsObjective__aims_objective_target", curie=ISO42001.curie('aims_objective_target'),
                   model_uri=ISO42001.aimsObjective__aims_objective_target, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_current_value = Slot(uri=ISO42001.aims_objective_current_value, name="aimsObjective__aims_objective_current_value", curie=ISO42001.curie('aims_objective_current_value'),
                   model_uri=ISO42001.aimsObjective__aims_objective_current_value, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_metric = Slot(uri=ISO42001.aims_objective_metric, name="aimsObjective__aims_objective_metric", curie=ISO42001.curie('aims_objective_metric'),
                   model_uri=ISO42001.aimsObjective__aims_objective_metric, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_measurement_method = Slot(uri=ISO42001.aims_objective_measurement_method, name="aimsObjective__aims_objective_measurement_method", curie=ISO42001.curie('aims_objective_measurement_method'),
                   model_uri=ISO42001.aimsObjective__aims_objective_measurement_method, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_measurement_frequency = Slot(uri=ISO42001.aims_objective_measurement_frequency, name="aimsObjective__aims_objective_measurement_frequency", curie=ISO42001.curie('aims_objective_measurement_frequency'),
                   model_uri=ISO42001.aimsObjective__aims_objective_measurement_frequency, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_target_date = Slot(uri=ISO42001.aims_objective_target_date, name="aimsObjective__aims_objective_target_date", curie=ISO42001.curie('aims_objective_target_date'),
                   model_uri=ISO42001.aimsObjective__aims_objective_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsObjective__aims_objective_achievement = Slot(uri=ISO42001.aims_objective_achievement, name="aimsObjective__aims_objective_achievement", curie=ISO42001.curie('aims_objective_achievement'),
                   model_uri=ISO42001.aimsObjective__aims_objective_achievement, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_risks = Slot(uri=ISO42001.aims_objective_risks, name="aimsObjective__aims_objective_risks", curie=ISO42001.curie('aims_objective_risks'),
                   model_uri=ISO42001.aimsObjective__aims_objective_risks, domain=None, range=Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]])

slots.aimsObjective__aims_objective_action_plan = Slot(uri=ISO42001.aims_objective_action_plan, name="aimsObjective__aims_objective_action_plan", curie=ISO42001.curie('aims_objective_action_plan'),
                   model_uri=ISO42001.aimsObjective__aims_objective_action_plan, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_resources = Slot(uri=ISO42001.aims_objective_resources, name="aimsObjective__aims_objective_resources", curie=ISO42001.curie('aims_objective_resources'),
                   model_uri=ISO42001.aimsObjective__aims_objective_resources, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_evaluation = Slot(uri=ISO42001.aims_objective_evaluation, name="aimsObjective__aims_objective_evaluation", curie=ISO42001.curie('aims_objective_evaluation'),
                   model_uri=ISO42001.aimsObjective__aims_objective_evaluation, domain=None, range=Optional[str])

slots.aimsObjective__aims_objective_communication = Slot(uri=ISO42001.aims_objective_communication, name="aimsObjective__aims_objective_communication", curie=ISO42001.curie('aims_objective_communication'),
                   model_uri=ISO42001.aimsObjective__aims_objective_communication, domain=None, range=Optional[str])

slots.aimsPlannedAction__aims_planned_action_risks = Slot(uri=ISO42001.aims_planned_action_risks, name="aimsPlannedAction__aims_planned_action_risks", curie=ISO42001.curie('aims_planned_action_risks'),
                   model_uri=ISO42001.aimsPlannedAction__aims_planned_action_risks, domain=None, range=Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]])

slots.aimsPlannedAction__aims_planned_action_opportunities = Slot(uri=ISO42001.aims_planned_action_opportunities, name="aimsPlannedAction__aims_planned_action_opportunities", curie=ISO42001.curie('aims_planned_action_opportunities'),
                   model_uri=ISO42001.aimsPlannedAction__aims_planned_action_opportunities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsPlannedAction__aims_planned_action_integration = Slot(uri=ISO42001.aims_planned_action_integration, name="aimsPlannedAction__aims_planned_action_integration", curie=ISO42001.curie('aims_planned_action_integration'),
                   model_uri=ISO42001.aimsPlannedAction__aims_planned_action_integration, domain=None, range=Optional[str])

slots.aimsPlannedAction__aims_planned_action_effectiveness = Slot(uri=ISO42001.aims_planned_action_effectiveness, name="aimsPlannedAction__aims_planned_action_effectiveness", curie=ISO42001.curie('aims_planned_action_effectiveness'),
                   model_uri=ISO42001.aimsPlannedAction__aims_planned_action_effectiveness, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_criteria = Slot(uri=ISO42001.aims_risk_criteria, name="aimsRiskAssessmentProcess__aims_risk_criteria", curie=ISO42001.curie('aims_risk_criteria'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRiskAssessmentProcess__aims_risk_policy_alignment = Slot(uri=ISO42001.aims_risk_policy_alignment, name="aimsRiskAssessmentProcess__aims_risk_policy_alignment", curie=ISO42001.curie('aims_risk_policy_alignment'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_policy_alignment, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_comparability = Slot(uri=ISO42001.aims_risk_comparability, name="aimsRiskAssessmentProcess__aims_risk_comparability", curie=ISO42001.curie('aims_risk_comparability'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_comparability, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_method = Slot(uri=ISO42001.aims_risk_method, name="aimsRiskAssessmentProcess__aims_risk_method", curie=ISO42001.curie('aims_risk_method'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_method, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_likelihood_scale = Slot(uri=ISO42001.aims_risk_likelihood_scale, name="aimsRiskAssessmentProcess__aims_risk_likelihood_scale", curie=ISO42001.curie('aims_risk_likelihood_scale'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_likelihood_scale, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_consequence_scale = Slot(uri=ISO42001.aims_risk_consequence_scale, name="aimsRiskAssessmentProcess__aims_risk_consequence_scale", curie=ISO42001.curie('aims_risk_consequence_scale'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_consequence_scale, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_matrix = Slot(uri=ISO42001.aims_risk_matrix, name="aimsRiskAssessmentProcess__aims_risk_matrix", curie=ISO42001.curie('aims_risk_matrix'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_matrix, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_prioritization = Slot(uri=ISO42001.aims_risk_prioritization, name="aimsRiskAssessmentProcess__aims_risk_prioritization", curie=ISO42001.curie('aims_risk_prioritization'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_prioritization, domain=None, range=Optional[str])

slots.aimsRiskAssessmentProcess__aims_risk_assessment_interval = Slot(uri=ISO42001.aims_risk_assessment_interval, name="aimsRiskAssessmentProcess__aims_risk_assessment_interval", curie=ISO42001.curie('aims_risk_assessment_interval'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_assessment_interval, domain=None, range=Optional[Union[str, AimsDuration]])

slots.aimsRiskAssessmentProcess__aims_risk_assessment_triggers = Slot(uri=ISO42001.aims_risk_assessment_triggers, name="aimsRiskAssessmentProcess__aims_risk_assessment_triggers", curie=ISO42001.curie('aims_risk_assessment_triggers'),
                   model_uri=ISO42001.aimsRiskAssessmentProcess__aims_risk_assessment_triggers, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRiskAssessment__aims_assessment_scope = Slot(uri=ISO42001.aims_assessment_scope, name="aimsRiskAssessment__aims_assessment_scope", curie=ISO42001.curie('aims_assessment_scope'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_scope, domain=None, range=Optional[str])

slots.aimsRiskAssessment__aims_assessment_date = Slot(uri=ISO42001.aims_assessment_date, name="aimsRiskAssessment__aims_assessment_date", curie=ISO42001.curie('aims_assessment_date'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsRiskAssessment__aims_assessment_assessor = Slot(uri=ISO42001.aims_assessment_assessor, name="aimsRiskAssessment__aims_assessment_assessor", curie=ISO42001.curie('aims_assessment_assessor'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_assessor, domain=None, range=Optional[str])

slots.aimsRiskAssessment__aims_assessment_method_used = Slot(uri=ISO42001.aims_assessment_method_used, name="aimsRiskAssessment__aims_assessment_method_used", curie=ISO42001.curie('aims_assessment_method_used'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_method_used, domain=None, range=Optional[str])

slots.aimsRiskAssessment__aims_assessment_risks = Slot(uri=ISO42001.aims_assessment_risks, name="aimsRiskAssessment__aims_assessment_risks", curie=ISO42001.curie('aims_assessment_risks'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_risks, domain=None, range=Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]])

slots.aimsRiskAssessment__aims_assessment_impact_assessments = Slot(uri=ISO42001.aims_assessment_impact_assessments, name="aimsRiskAssessment__aims_assessment_impact_assessments", curie=ISO42001.curie('aims_assessment_impact_assessments'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_impact_assessments, domain=None, range=Optional[Union[Union[str, AimsImpactAssessmentAimsId], list[Union[str, AimsImpactAssessmentAimsId]]]])

slots.aimsRiskAssessment__aims_assessment_summary = Slot(uri=ISO42001.aims_assessment_summary, name="aimsRiskAssessment__aims_assessment_summary", curie=ISO42001.curie('aims_assessment_summary'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_summary, domain=None, range=Optional[str])

slots.aimsRiskAssessment__aims_assessment_recommendations = Slot(uri=ISO42001.aims_assessment_recommendations, name="aimsRiskAssessment__aims_assessment_recommendations", curie=ISO42001.curie('aims_assessment_recommendations'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_recommendations, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRiskAssessment__aims_assessment_next_date = Slot(uri=ISO42001.aims_assessment_next_date, name="aimsRiskAssessment__aims_assessment_next_date", curie=ISO42001.curie('aims_assessment_next_date'),
                   model_uri=ISO42001.aimsRiskAssessment__aims_assessment_next_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsRisk__aims_risk_source = Slot(uri=ISO42001.aims_risk_source, name="aimsRisk__aims_risk_source", curie=ISO42001.curie('aims_risk_source'),
                   model_uri=ISO42001.aimsRisk__aims_risk_source, domain=None, range=Optional[str])

slots.aimsRisk__aims_risk_objectives = Slot(uri=ISO42001.aims_risk_objectives, name="aimsRisk__aims_risk_objectives", curie=ISO42001.curie('aims_risk_objectives'),
                   model_uri=ISO42001.aimsRisk__aims_risk_objectives, domain=None, range=Optional[Union[Union[str, AimsObjectiveAimsId], list[Union[str, AimsObjectiveAimsId]]]])

slots.aimsRisk__aims_risk_consequences_for_organization = Slot(uri=ISO42001.aims_risk_consequences_for_organization, name="aimsRisk__aims_risk_consequences_for_organization", curie=ISO42001.curie('aims_risk_consequences_for_organization'),
                   model_uri=ISO42001.aimsRisk__aims_risk_consequences_for_organization, domain=None, range=Optional[str])

slots.aimsRisk__aims_risk_consequences_for_individuals = Slot(uri=ISO42001.aims_risk_consequences_for_individuals, name="aimsRisk__aims_risk_consequences_for_individuals", curie=ISO42001.curie('aims_risk_consequences_for_individuals'),
                   model_uri=ISO42001.aimsRisk__aims_risk_consequences_for_individuals, domain=None, range=Optional[str])

slots.aimsRisk__aims_risk_consequences_for_societies = Slot(uri=ISO42001.aims_risk_consequences_for_societies, name="aimsRisk__aims_risk_consequences_for_societies", curie=ISO42001.curie('aims_risk_consequences_for_societies'),
                   model_uri=ISO42001.aimsRisk__aims_risk_consequences_for_societies, domain=None, range=Optional[str])

slots.aimsRisk__aims_risk_owner = Slot(uri=ISO42001.aims_risk_owner, name="aimsRisk__aims_risk_owner", curie=ISO42001.curie('aims_risk_owner'),
                   model_uri=ISO42001.aimsRisk__aims_risk_owner, domain=None, range=Optional[str])

slots.aimsRisk__aims_risk_likelihood = Slot(uri=ISO42001.aims_risk_likelihood, name="aimsRisk__aims_risk_likelihood", curie=ISO42001.curie('aims_risk_likelihood'),
                   model_uri=ISO42001.aimsRisk__aims_risk_likelihood, domain=None, range=Optional[Union[str, "AimsLikelihood"]])

slots.aimsRisk__aims_risk_consequence = Slot(uri=ISO42001.aims_risk_consequence, name="aimsRisk__aims_risk_consequence", curie=ISO42001.curie('aims_risk_consequence'),
                   model_uri=ISO42001.aimsRisk__aims_risk_consequence, domain=None, range=Optional[Union[str, "AimsConsequence"]])

slots.aimsRisk__aims_risk_inherent_level = Slot(uri=ISO42001.aims_risk_inherent_level, name="aimsRisk__aims_risk_inherent_level", curie=ISO42001.curie('aims_risk_inherent_level'),
                   model_uri=ISO42001.aimsRisk__aims_risk_inherent_level, domain=None, range=Optional[Union[str, "AimsRiskLevel"]])

slots.aimsRisk__aims_risk_existing_controls = Slot(uri=ISO42001.aims_risk_existing_controls, name="aimsRisk__aims_risk_existing_controls", curie=ISO42001.curie('aims_risk_existing_controls'),
                   model_uri=ISO42001.aimsRisk__aims_risk_existing_controls, domain=None, range=Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]])

slots.aimsRisk__aims_risk_residual_level = Slot(uri=ISO42001.aims_risk_residual_level, name="aimsRisk__aims_risk_residual_level", curie=ISO42001.curie('aims_risk_residual_level'),
                   model_uri=ISO42001.aimsRisk__aims_risk_residual_level, domain=None, range=Optional[Union[str, "AimsRiskLevel"]])

slots.aimsRisk__aims_risk_acceptable = Slot(uri=ISO42001.aims_risk_acceptable, name="aimsRisk__aims_risk_acceptable", curie=ISO42001.curie('aims_risk_acceptable'),
                   model_uri=ISO42001.aimsRisk__aims_risk_acceptable, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsRisk__aims_risk_treatment_option = Slot(uri=ISO42001.aims_risk_treatment_option, name="aimsRisk__aims_risk_treatment_option", curie=ISO42001.curie('aims_risk_treatment_option'),
                   model_uri=ISO42001.aimsRisk__aims_risk_treatment_option, domain=None, range=Optional[Union[str, "AimsRiskTreatmentOption"]])

slots.aimsRisk__aims_risk_treatment_priority = Slot(uri=ISO42001.aims_risk_treatment_priority, name="aimsRisk__aims_risk_treatment_priority", curie=ISO42001.curie('aims_risk_treatment_priority'),
                   model_uri=ISO42001.aimsRisk__aims_risk_treatment_priority, domain=None, range=Optional[str])

slots.aimsRisk__aims_risk_impact_assessments = Slot(uri=ISO42001.aims_risk_impact_assessments, name="aimsRisk__aims_risk_impact_assessments", curie=ISO42001.curie('aims_risk_impact_assessments'),
                   model_uri=ISO42001.aimsRisk__aims_risk_impact_assessments, domain=None, range=Optional[Union[Union[str, AimsImpactAssessmentAimsId], list[Union[str, AimsImpactAssessmentAimsId]]]])

slots.aimsRiskTreatmentProcess__aims_treatment_options_guidance = Slot(uri=ISO42001.aims_treatment_options_guidance, name="aimsRiskTreatmentProcess__aims_treatment_options_guidance", curie=ISO42001.curie('aims_treatment_options_guidance'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_options_guidance, domain=None, range=Optional[str])

slots.aimsRiskTreatmentProcess__aims_treatment_control_selection = Slot(uri=ISO42001.aims_treatment_control_selection, name="aimsRiskTreatmentProcess__aims_treatment_control_selection", curie=ISO42001.curie('aims_treatment_control_selection'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_control_selection, domain=None, range=Optional[str])

slots.aimsRiskTreatmentProcess__aims_treatment_annex_a_comparison = Slot(uri=ISO42001.aims_treatment_annex_a_comparison, name="aimsRiskTreatmentProcess__aims_treatment_annex_a_comparison", curie=ISO42001.curie('aims_treatment_annex_a_comparison'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_annex_a_comparison, domain=None, range=Optional[str])

slots.aimsRiskTreatmentProcess__aims_treatment_additional_controls = Slot(uri=ISO42001.aims_treatment_additional_controls, name="aimsRiskTreatmentProcess__aims_treatment_additional_controls", curie=ISO42001.curie('aims_treatment_additional_controls'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_additional_controls, domain=None, range=Optional[str])

slots.aimsRiskTreatmentProcess__aims_treatment_annex_b_use = Slot(uri=ISO42001.aims_treatment_annex_b_use, name="aimsRiskTreatmentProcess__aims_treatment_annex_b_use", curie=ISO42001.curie('aims_treatment_annex_b_use'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_annex_b_use, domain=None, range=Optional[str])

slots.aimsRiskTreatmentProcess__aims_treatment_soa_template = Slot(uri=ISO42001.aims_treatment_soa_template, name="aimsRiskTreatmentProcess__aims_treatment_soa_template", curie=ISO42001.curie('aims_treatment_soa_template'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_soa_template, domain=None, range=Optional[str])

slots.aimsRiskTreatmentProcess__aims_treatment_approval_workflow = Slot(uri=ISO42001.aims_treatment_approval_workflow, name="aimsRiskTreatmentProcess__aims_treatment_approval_workflow", curie=ISO42001.curie('aims_treatment_approval_workflow'),
                   model_uri=ISO42001.aimsRiskTreatmentProcess__aims_treatment_approval_workflow, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_scope = Slot(uri=ISO42001.aims_plan_scope, name="aimsRiskTreatmentPlan__aims_plan_scope", curie=ISO42001.curie('aims_plan_scope'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_scope, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_risks = Slot(uri=ISO42001.aims_plan_risks, name="aimsRiskTreatmentPlan__aims_plan_risks", curie=ISO42001.curie('aims_plan_risks'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_risks, domain=None, range=Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]])

slots.aimsRiskTreatmentPlan__aims_plan_actions = Slot(uri=ISO42001.aims_plan_actions, name="aimsRiskTreatmentPlan__aims_plan_actions", curie=ISO42001.curie('aims_plan_actions'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRiskTreatmentPlan__aims_plan_controls = Slot(uri=ISO42001.aims_plan_controls, name="aimsRiskTreatmentPlan__aims_plan_controls", curie=ISO42001.curie('aims_plan_controls'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_controls, domain=None, range=Optional[Union[Union[str, AimsControlAimsId], list[Union[str, AimsControlAimsId]]]])

slots.aimsRiskTreatmentPlan__aims_plan_resources = Slot(uri=ISO42001.aims_plan_resources, name="aimsRiskTreatmentPlan__aims_plan_resources", curie=ISO42001.curie('aims_plan_resources'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_resources, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_responsible_parties = Slot(uri=ISO42001.aims_plan_responsible_parties, name="aimsRiskTreatmentPlan__aims_plan_responsible_parties", curie=ISO42001.curie('aims_plan_responsible_parties'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_responsible_parties, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsRiskTreatmentPlan__aims_plan_timeline = Slot(uri=ISO42001.aims_plan_timeline, name="aimsRiskTreatmentPlan__aims_plan_timeline", curie=ISO42001.curie('aims_plan_timeline'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_timeline, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_approver = Slot(uri=ISO42001.aims_plan_approver, name="aimsRiskTreatmentPlan__aims_plan_approver", curie=ISO42001.curie('aims_plan_approver'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_approver, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_residual_risk_acceptance = Slot(uri=ISO42001.aims_plan_residual_risk_acceptance, name="aimsRiskTreatmentPlan__aims_plan_residual_risk_acceptance", curie=ISO42001.curie('aims_plan_residual_risk_acceptance'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_residual_risk_acceptance, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_effectiveness = Slot(uri=ISO42001.aims_plan_effectiveness, name="aimsRiskTreatmentPlan__aims_plan_effectiveness", curie=ISO42001.curie('aims_plan_effectiveness'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_effectiveness, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_revalidation = Slot(uri=ISO42001.aims_plan_revalidation, name="aimsRiskTreatmentPlan__aims_plan_revalidation", curie=ISO42001.curie('aims_plan_revalidation'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_revalidation, domain=None, range=Optional[str])

slots.aimsRiskTreatmentPlan__aims_plan_completion_date = Slot(uri=ISO42001.aims_plan_completion_date, name="aimsRiskTreatmentPlan__aims_plan_completion_date", curie=ISO42001.curie('aims_plan_completion_date'),
                   model_uri=ISO42001.aimsRiskTreatmentPlan__aims_plan_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsImpactAssessmentProcess__aims_impact_process_triggers = Slot(uri=ISO42001.aims_impact_process_triggers, name="aimsImpactAssessmentProcess__aims_impact_process_triggers", curie=ISO42001.curie('aims_impact_process_triggers'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_triggers, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsImpactAssessmentProcess__aims_impact_process_interval = Slot(uri=ISO42001.aims_impact_process_interval, name="aimsImpactAssessmentProcess__aims_impact_process_interval", curie=ISO42001.curie('aims_impact_process_interval'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_interval, domain=None, range=Optional[Union[str, AimsDuration]])

slots.aimsImpactAssessmentProcess__aims_impact_process_steps = Slot(uri=ISO42001.aims_impact_process_steps, name="aimsImpactAssessmentProcess__aims_impact_process_steps", curie=ISO42001.curie('aims_impact_process_steps'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_steps, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsImpactAssessmentProcess__aims_impact_process_assessors = Slot(uri=ISO42001.aims_impact_process_assessors, name="aimsImpactAssessmentProcess__aims_impact_process_assessors", curie=ISO42001.curie('aims_impact_process_assessors'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_assessors, domain=None, range=Optional[str])

slots.aimsImpactAssessmentProcess__aims_impact_process_use = Slot(uri=ISO42001.aims_impact_process_use, name="aimsImpactAssessmentProcess__aims_impact_process_use", curie=ISO42001.curie('aims_impact_process_use'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_use, domain=None, range=Optional[str])

slots.aimsImpactAssessmentProcess__aims_impact_process_subjects = Slot(uri=ISO42001.aims_impact_process_subjects, name="aimsImpactAssessmentProcess__aims_impact_process_subjects", curie=ISO42001.curie('aims_impact_process_subjects'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_subjects, domain=None, range=Optional[Union[Union[str, "AimsImpactSubject"], list[Union[str, "AimsImpactSubject"]]]])

slots.aimsImpactAssessmentProcess__aims_impact_process_areas = Slot(uri=ISO42001.aims_impact_process_areas, name="aimsImpactAssessmentProcess__aims_impact_process_areas", curie=ISO42001.curie('aims_impact_process_areas'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_areas, domain=None, range=Optional[Union[Union[str, "AimsImpactArea"], list[Union[str, "AimsImpactArea"]]]])

slots.aimsImpactAssessmentProcess__aims_impact_process_retention = Slot(uri=ISO42001.aims_impact_process_retention, name="aimsImpactAssessmentProcess__aims_impact_process_retention", curie=ISO42001.curie('aims_impact_process_retention'),
                   model_uri=ISO42001.aimsImpactAssessmentProcess__aims_impact_process_retention, domain=None, range=Optional[Union[str, AimsDuration]])

slots.aimsImpactAssessment__aims_impact_scope = Slot(uri=ISO42001.aims_impact_scope, name="aimsImpactAssessment__aims_impact_scope", curie=ISO42001.curie('aims_impact_scope'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_scope, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_discipline = Slot(uri=ISO42001.aims_impact_discipline, name="aimsImpactAssessment__aims_impact_discipline", curie=ISO42001.curie('aims_impact_discipline'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_discipline, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_date = Slot(uri=ISO42001.aims_impact_date, name="aimsImpactAssessment__aims_impact_date", curie=ISO42001.curie('aims_impact_date'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsImpactAssessment__aims_impact_assessor = Slot(uri=ISO42001.aims_impact_assessor, name="aimsImpactAssessment__aims_impact_assessor", curie=ISO42001.curie('aims_impact_assessor'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_assessor, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_intended_use = Slot(uri=ISO42001.aims_impact_intended_use, name="aimsImpactAssessment__aims_impact_intended_use", curie=ISO42001.curie('aims_impact_intended_use'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_intended_use, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_foreseeable_misuse = Slot(uri=ISO42001.aims_impact_foreseeable_misuse, name="aimsImpactAssessment__aims_impact_foreseeable_misuse", curie=ISO42001.curie('aims_impact_foreseeable_misuse'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_foreseeable_misuse, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_technical_context = Slot(uri=ISO42001.aims_impact_technical_context, name="aimsImpactAssessment__aims_impact_technical_context", curie=ISO42001.curie('aims_impact_technical_context'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_technical_context, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_societal_context = Slot(uri=ISO42001.aims_impact_societal_context, name="aimsImpactAssessment__aims_impact_societal_context", curie=ISO42001.curie('aims_impact_societal_context'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_societal_context, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_jurisdictions = Slot(uri=ISO42001.aims_impact_jurisdictions, name="aimsImpactAssessment__aims_impact_jurisdictions", curie=ISO42001.curie('aims_impact_jurisdictions'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsImpactAssessment__aims_impact_demographic_groups = Slot(uri=ISO42001.aims_impact_demographic_groups, name="aimsImpactAssessment__aims_impact_demographic_groups", curie=ISO42001.curie('aims_impact_demographic_groups'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_demographic_groups, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsImpactAssessment__aims_impact_system_complexity = Slot(uri=ISO42001.aims_impact_system_complexity, name="aimsImpactAssessment__aims_impact_system_complexity", curie=ISO42001.curie('aims_impact_system_complexity'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_system_complexity, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_human_role = Slot(uri=ISO42001.aims_impact_human_role, name="aimsImpactAssessment__aims_impact_human_role", curie=ISO42001.curie('aims_impact_human_role'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_human_role, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_failures = Slot(uri=ISO42001.aims_impact_failures, name="aimsImpactAssessment__aims_impact_failures", curie=ISO42001.curie('aims_impact_failures'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_failures, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsImpactAssessment__aims_impact_workforce = Slot(uri=ISO42001.aims_impact_workforce, name="aimsImpactAssessment__aims_impact_workforce", curie=ISO42001.curie('aims_impact_workforce'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_workforce, domain=None, range=Optional[str])

slots.aimsImpactAssessment__aims_impact_findings = Slot(uri=ISO42001.aims_impact_findings, name="aimsImpactAssessment__aims_impact_findings", curie=ISO42001.curie('aims_impact_findings'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_findings, domain=None, range=Optional[Union[Union[dict, AimsIdentifiedImpact], list[Union[dict, AimsIdentifiedImpact]]]])

slots.aimsImpactAssessment__aims_impact_shared_with = Slot(uri=ISO42001.aims_impact_shared_with, name="aimsImpactAssessment__aims_impact_shared_with", curie=ISO42001.curie('aims_impact_shared_with'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_shared_with, domain=None, range=Optional[Union[Union[str, AimsInterestedPartyAimsId], list[Union[str, AimsInterestedPartyAimsId]]]])

slots.aimsImpactAssessment__aims_impact_next_date = Slot(uri=ISO42001.aims_impact_next_date, name="aimsImpactAssessment__aims_impact_next_date", curie=ISO42001.curie('aims_impact_next_date'),
                   model_uri=ISO42001.aimsImpactAssessment__aims_impact_next_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsIdentifiedImpact__aims_identified_impact_subject = Slot(uri=ISO42001.aims_identified_impact_subject, name="aimsIdentifiedImpact__aims_identified_impact_subject", curie=ISO42001.curie('aims_identified_impact_subject'),
                   model_uri=ISO42001.aimsIdentifiedImpact__aims_identified_impact_subject, domain=None, range=Union[str, "AimsImpactSubject"])

slots.aimsIdentifiedImpact__aims_identified_impact_area = Slot(uri=ISO42001.aims_identified_impact_area, name="aimsIdentifiedImpact__aims_identified_impact_area", curie=ISO42001.curie('aims_identified_impact_area'),
                   model_uri=ISO42001.aimsIdentifiedImpact__aims_identified_impact_area, domain=None, range=Optional[Union[str, "AimsImpactArea"]])

slots.aimsIdentifiedImpact__aims_identified_impact_direction = Slot(uri=ISO42001.aims_identified_impact_direction, name="aimsIdentifiedImpact__aims_identified_impact_direction", curie=ISO42001.curie('aims_identified_impact_direction'),
                   model_uri=ISO42001.aimsIdentifiedImpact__aims_identified_impact_direction, domain=None, range=Optional[Union[str, "AimsImpactDirection"]])

slots.aimsIdentifiedImpact__aims_identified_impact_text = Slot(uri=ISO42001.aims_identified_impact_text, name="aimsIdentifiedImpact__aims_identified_impact_text", curie=ISO42001.curie('aims_identified_impact_text'),
                   model_uri=ISO42001.aimsIdentifiedImpact__aims_identified_impact_text, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.aimsIdentifiedImpact__aims_identified_impact_mitigation = Slot(uri=ISO42001.aims_identified_impact_mitigation, name="aimsIdentifiedImpact__aims_identified_impact_mitigation", curie=ISO42001.curie('aims_identified_impact_mitigation'),
                   model_uri=ISO42001.aimsIdentifiedImpact__aims_identified_impact_mitigation, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsStatementOfApplicability__aims_soa_entries = Slot(uri=ISO42001.aims_soa_entries, name="aimsStatementOfApplicability__aims_soa_entries", curie=ISO42001.curie('aims_soa_entries'),
                   model_uri=ISO42001.aimsStatementOfApplicability__aims_soa_entries, domain=None, range=Optional[Union[Union[dict, AimsApplicabilityEntry], list[Union[dict, AimsApplicabilityEntry]]]])

slots.aimsApplicabilityEntry__aims_entry_type = Slot(uri=ISO42001.aims_entry_type, name="aimsApplicabilityEntry__aims_entry_type", curie=ISO42001.curie('aims_entry_type'),
                   model_uri=ISO42001.aimsApplicabilityEntry__aims_entry_type, domain=None, range=Optional[str])

slots.aimsApplicabilityEntry__aims_entry_justification = Slot(uri=ISO42001.aims_entry_justification, name="aimsApplicabilityEntry__aims_entry_justification", curie=ISO42001.curie('aims_entry_justification'),
                   model_uri=ISO42001.aimsApplicabilityEntry__aims_entry_justification, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.aimsIncludedControl__aims_included_control = Slot(uri=ISO42001.aims_included_control, name="aimsIncludedControl__aims_included_control", curie=ISO42001.curie('aims_included_control'),
                   model_uri=ISO42001.aimsIncludedControl__aims_included_control, domain=None, range=Optional[Union[str, AimsControlAimsId]])

slots.aimsIncludedControl__aims_included_risks = Slot(uri=ISO42001.aims_included_risks, name="aimsIncludedControl__aims_included_risks", curie=ISO42001.curie('aims_included_risks'),
                   model_uri=ISO42001.aimsIncludedControl__aims_included_risks, domain=None, range=Optional[Union[Union[str, AimsRiskAimsId], list[Union[str, AimsRiskAimsId]]]])

slots.aimsIncludedControl__aims_included_evidence = Slot(uri=ISO42001.aims_included_evidence, name="aimsIncludedControl__aims_included_evidence", curie=ISO42001.curie('aims_included_evidence'),
                   model_uri=ISO42001.aimsIncludedControl__aims_included_evidence, domain=None, range=Optional[str])

slots.aimsIncludedControl__aims_included_target_date = Slot(uri=ISO42001.aims_included_target_date, name="aimsIncludedControl__aims_included_target_date", curie=ISO42001.curie('aims_included_target_date'),
                   model_uri=ISO42001.aimsIncludedControl__aims_included_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsControl__aims_control_area = Slot(uri=ISO42001.aims_control_area, name="aimsControl__aims_control_area", curie=ISO42001.curie('aims_control_area'),
                   model_uri=ISO42001.aimsControl__aims_control_area, domain=None, range=Optional[Union[str, "AimsControlArea"]])

slots.aimsControl__aims_control_text = Slot(uri=ISO42001.aims_control_text, name="aimsControl__aims_control_text", curie=ISO42001.curie('aims_control_text'),
                   model_uri=ISO42001.aimsControl__aims_control_text, domain=None, range=Optional[str])

slots.aimsControl__aims_control_guidance = Slot(uri=ISO42001.aims_control_guidance, name="aimsControl__aims_control_guidance", curie=ISO42001.curie('aims_control_guidance'),
                   model_uri=ISO42001.aimsControl__aims_control_guidance, domain=None, range=Optional[str])

slots.aimsControl__aims_control_owner = Slot(uri=ISO42001.aims_control_owner, name="aimsControl__aims_control_owner", curie=ISO42001.curie('aims_control_owner'),
                   model_uri=ISO42001.aimsControl__aims_control_owner, domain=None, range=Optional[str])

slots.aimsControl__aims_control_implementation_date = Slot(uri=ISO42001.aims_control_implementation_date, name="aimsControl__aims_control_implementation_date", curie=ISO42001.curie('aims_control_implementation_date'),
                   model_uri=ISO42001.aimsControl__aims_control_implementation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsControl__aims_control_effectiveness = Slot(uri=ISO42001.aims_control_effectiveness, name="aimsControl__aims_control_effectiveness", curie=ISO42001.curie('aims_control_effectiveness'),
                   model_uri=ISO42001.aimsControl__aims_control_effectiveness, domain=None, range=Optional[str])

slots.aimsControl__aims_control_last_tested = Slot(uri=ISO42001.aims_control_last_tested, name="aimsControl__aims_control_last_tested", curie=ISO42001.curie('aims_control_last_tested'),
                   model_uri=ISO42001.aimsControl__aims_control_last_tested, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsControl__aims_control_evidence = Slot(uri=ISO42001.aims_control_evidence, name="aimsControl__aims_control_evidence", curie=ISO42001.curie('aims_control_evidence'),
                   model_uri=ISO42001.aimsControl__aims_control_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_intended_purpose = Slot(uri=ISO42001.aims_system_intended_purpose, name="aimsAiSystem__aims_system_intended_purpose", curie=ISO42001.curie('aims_system_intended_purpose'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_intended_purpose, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_intended_uses = Slot(uri=ISO42001.aims_system_intended_uses, name="aimsAiSystem__aims_system_intended_uses", curie=ISO42001.curie('aims_system_intended_uses'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_intended_uses, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_foreseeable_misuse = Slot(uri=ISO42001.aims_system_foreseeable_misuse, name="aimsAiSystem__aims_system_foreseeable_misuse", curie=ISO42001.curie('aims_system_foreseeable_misuse'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_foreseeable_misuse, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_domain = Slot(uri=ISO42001.aims_system_domain, name="aimsAiSystem__aims_system_domain", curie=ISO42001.curie('aims_system_domain'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_domain, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_deployment_context = Slot(uri=ISO42001.aims_system_deployment_context, name="aimsAiSystem__aims_system_deployment_context", curie=ISO42001.curie('aims_system_deployment_context'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_deployment_context, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_life_cycle_stage = Slot(uri=ISO42001.aims_system_life_cycle_stage, name="aimsAiSystem__aims_system_life_cycle_stage", curie=ISO42001.curie('aims_system_life_cycle_stage'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_life_cycle_stage, domain=None, range=Optional[Union[str, "AimsLifecycleStage"]])

slots.aimsAiSystem__aims_system_organization_roles = Slot(uri=ISO42001.aims_system_organization_roles, name="aimsAiSystem__aims_system_organization_roles", curie=ISO42001.curie('aims_system_organization_roles'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_organization_roles, domain=None, range=Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]])

slots.aimsAiSystem__aims_system_pii_roles = Slot(uri=ISO42001.aims_system_pii_roles, name="aimsAiSystem__aims_system_pii_roles", curie=ISO42001.curie('aims_system_pii_roles'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_pii_roles, domain=None, range=Optional[Union[Union[str, "AimsPiiRole"], list[Union[str, "AimsPiiRole"]]]])

slots.aimsAiSystem__aims_system_rationale = Slot(uri=ISO42001.aims_system_rationale, name="aimsAiSystem__aims_system_rationale", curie=ISO42001.curie('aims_system_rationale'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_rationale, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_requirements = Slot(uri=ISO42001.aims_system_requirements, name="aimsAiSystem__aims_system_requirements", curie=ISO42001.curie('aims_system_requirements'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_ml_approach = Slot(uri=ISO42001.aims_system_ml_approach, name="aimsAiSystem__aims_system_ml_approach", curie=ISO42001.curie('aims_system_ml_approach'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_ml_approach, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_model_types = Slot(uri=ISO42001.aims_system_model_types, name="aimsAiSystem__aims_system_model_types", curie=ISO42001.curie('aims_system_model_types'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_model_types, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_continuous_learning = Slot(uri=ISO42001.aims_system_continuous_learning, name="aimsAiSystem__aims_system_continuous_learning", curie=ISO42001.curie('aims_system_continuous_learning'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_continuous_learning, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsAiSystem__aims_system_automation_level = Slot(uri=ISO42001.aims_system_automation_level, name="aimsAiSystem__aims_system_automation_level", curie=ISO42001.curie('aims_system_automation_level'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_automation_level, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_threats = Slot(uri=ISO42001.aims_system_threats, name="aimsAiSystem__aims_system_threats", curie=ISO42001.curie('aims_system_threats'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_threats, domain=None, range=Optional[Union[Union[str, "AimsAiThreat"], list[Union[str, "AimsAiThreat"]]]])

slots.aimsAiSystem__aims_system_verification_measures = Slot(uri=ISO42001.aims_system_verification_measures, name="aimsAiSystem__aims_system_verification_measures", curie=ISO42001.curie('aims_system_verification_measures'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_verification_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_evaluation_criteria = Slot(uri=ISO42001.aims_system_evaluation_criteria, name="aimsAiSystem__aims_system_evaluation_criteria", curie=ISO42001.curie('aims_system_evaluation_criteria'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_evaluation_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_release_criteria = Slot(uri=ISO42001.aims_system_release_criteria, name="aimsAiSystem__aims_system_release_criteria", curie=ISO42001.curie('aims_system_release_criteria'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_release_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_deployment_plan = Slot(uri=ISO42001.aims_system_deployment_plan, name="aimsAiSystem__aims_system_deployment_plan", curie=ISO42001.curie('aims_system_deployment_plan'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_deployment_plan, domain=None, range=Optional[Union[str, AimsDocumentedInformationAimsId]])

slots.aimsAiSystem__aims_system_operation_elements = Slot(uri=ISO42001.aims_system_operation_elements, name="aimsAiSystem__aims_system_operation_elements", curie=ISO42001.curie('aims_system_operation_elements'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_operation_elements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_performance_metrics = Slot(uri=ISO42001.aims_system_performance_metrics, name="aimsAiSystem__aims_system_performance_metrics", curie=ISO42001.curie('aims_system_performance_metrics'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_performance_metrics, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_log_stages = Slot(uri=ISO42001.aims_system_log_stages, name="aimsAiSystem__aims_system_log_stages", curie=ISO42001.curie('aims_system_log_stages'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_log_stages, domain=None, range=Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]])

slots.aimsAiSystem__aims_system_log_contents = Slot(uri=ISO42001.aims_system_log_contents, name="aimsAiSystem__aims_system_log_contents", curie=ISO42001.curie('aims_system_log_contents'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_log_contents, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAiSystem__aims_system_log_retention = Slot(uri=ISO42001.aims_system_log_retention, name="aimsAiSystem__aims_system_log_retention", curie=ISO42001.curie('aims_system_log_retention'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_log_retention, domain=None, range=Optional[Union[str, AimsDuration]])

slots.aimsAiSystem__aims_system_human_oversight_required = Slot(uri=ISO42001.aims_system_human_oversight_required, name="aimsAiSystem__aims_system_human_oversight_required", curie=ISO42001.curie('aims_system_human_oversight_required'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_human_oversight_required, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsAiSystem__aims_system_human_oversight = Slot(uri=ISO42001.aims_system_human_oversight, name="aimsAiSystem__aims_system_human_oversight", curie=ISO42001.curie('aims_system_human_oversight'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_human_oversight, domain=None, range=Optional[str])

slots.aimsAiSystem__aims_system_human_oversight_stages = Slot(uri=ISO42001.aims_system_human_oversight_stages, name="aimsAiSystem__aims_system_human_oversight_stages", curie=ISO42001.curie('aims_system_human_oversight_stages'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_human_oversight_stages, domain=None, range=Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]])

slots.aimsAiSystem__aims_system_resources_used = Slot(uri=ISO42001.aims_system_resources_used, name="aimsAiSystem__aims_system_resources_used", curie=ISO42001.curie('aims_system_resources_used'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_resources_used, domain=None, range=Optional[Union[Union[str, AimsSystemResourceAimsId], list[Union[str, AimsSystemResourceAimsId]]]])

slots.aimsAiSystem__aims_system_technical_documents = Slot(uri=ISO42001.aims_system_technical_documents, name="aimsAiSystem__aims_system_technical_documents", curie=ISO42001.curie('aims_system_technical_documents'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_technical_documents, domain=None, range=Optional[Union[Union[str, AimsTechnicalDocumentationAimsId], list[Union[str, AimsTechnicalDocumentationAimsId]]]])

slots.aimsAiSystem__aims_system_impact_assessments = Slot(uri=ISO42001.aims_system_impact_assessments, name="aimsAiSystem__aims_system_impact_assessments", curie=ISO42001.curie('aims_system_impact_assessments'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_impact_assessments, domain=None, range=Optional[Union[Union[str, AimsImpactAssessmentAimsId], list[Union[str, AimsImpactAssessmentAimsId]]]])

slots.aimsAiSystem__aims_system_relationships = Slot(uri=ISO42001.aims_system_relationships, name="aimsAiSystem__aims_system_relationships", curie=ISO42001.curie('aims_system_relationships'),
                   model_uri=ISO42001.aimsAiSystem__aims_system_relationships, domain=None, range=Optional[Union[Union[str, AimsThirdPartyRelationshipAimsId], list[Union[str, AimsThirdPartyRelationshipAimsId]]]])

slots.aimsSystemResource__aims_resource_provider = Slot(uri=ISO42001.aims_resource_provider, name="aimsSystemResource__aims_resource_provider", curie=ISO42001.curie('aims_resource_provider'),
                   model_uri=ISO42001.aimsSystemResource__aims_resource_provider, domain=None, range=Optional[Union[str, "AimsResourceProvider"]])

slots.aimsComponentResource__aims_component_kind = Slot(uri=ISO42001.aims_component_kind, name="aimsComponentResource__aims_component_kind", curie=ISO42001.curie('aims_component_kind'),
                   model_uri=ISO42001.aimsComponentResource__aims_component_kind, domain=None, range=Optional[str])

slots.aimsComponentResource__aims_component_integration = Slot(uri=ISO42001.aims_component_integration, name="aimsComponentResource__aims_component_integration", curie=ISO42001.curie('aims_component_integration'),
                   model_uri=ISO42001.aimsComponentResource__aims_component_integration, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_categories = Slot(uri=ISO42001.aims_data_categories, name="aimsDataResource__aims_data_categories", curie=ISO42001.curie('aims_data_categories'),
                   model_uri=ISO42001.aimsDataResource__aims_data_categories, domain=None, range=Optional[Union[Union[str, "AimsDataCategory"], list[Union[str, "AimsDataCategory"]]]])

slots.aimsDataResource__aims_data_kinds = Slot(uri=ISO42001.aims_data_kinds, name="aimsDataResource__aims_data_kinds", curie=ISO42001.curie('aims_data_kinds'),
                   model_uri=ISO42001.aimsDataResource__aims_data_kinds, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_intended_use = Slot(uri=ISO42001.aims_data_intended_use, name="aimsDataResource__aims_data_intended_use", curie=ISO42001.curie('aims_data_intended_use'),
                   model_uri=ISO42001.aimsDataResource__aims_data_intended_use, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_quantity = Slot(uri=ISO42001.aims_data_quantity, name="aimsDataResource__aims_data_quantity", curie=ISO42001.curie('aims_data_quantity'),
                   model_uri=ISO42001.aimsDataResource__aims_data_quantity, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_sources = Slot(uri=ISO42001.aims_data_sources, name="aimsDataResource__aims_data_sources", curie=ISO42001.curie('aims_data_sources'),
                   model_uri=ISO42001.aimsDataResource__aims_data_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_source_characteristics = Slot(uri=ISO42001.aims_data_source_characteristics, name="aimsDataResource__aims_data_source_characteristics", curie=ISO42001.curie('aims_data_source_characteristics'),
                   model_uri=ISO42001.aimsDataResource__aims_data_source_characteristics, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_subject_demographics = Slot(uri=ISO42001.aims_data_subject_demographics, name="aimsDataResource__aims_data_subject_demographics", curie=ISO42001.curie('aims_data_subject_demographics'),
                   model_uri=ISO42001.aimsDataResource__aims_data_subject_demographics, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_prior_handling = Slot(uri=ISO42001.aims_data_prior_handling, name="aimsDataResource__aims_data_prior_handling", curie=ISO42001.curie('aims_data_prior_handling'),
                   model_uri=ISO42001.aimsDataResource__aims_data_prior_handling, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_rights = Slot(uri=ISO42001.aims_data_rights, name="aimsDataResource__aims_data_rights", curie=ISO42001.curie('aims_data_rights'),
                   model_uri=ISO42001.aimsDataResource__aims_data_rights, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_metadata = Slot(uri=ISO42001.aims_data_metadata, name="aimsDataResource__aims_data_metadata", curie=ISO42001.curie('aims_data_metadata'),
                   model_uri=ISO42001.aimsDataResource__aims_data_metadata, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_provenance = Slot(uri=ISO42001.aims_data_provenance, name="aimsDataResource__aims_data_provenance", curie=ISO42001.curie('aims_data_provenance'),
                   model_uri=ISO42001.aimsDataResource__aims_data_provenance, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_provenance_verification = Slot(uri=ISO42001.aims_data_provenance_verification, name="aimsDataResource__aims_data_provenance_verification", curie=ISO42001.curie('aims_data_provenance_verification'),
                   model_uri=ISO42001.aimsDataResource__aims_data_provenance_verification, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_quality_requirements = Slot(uri=ISO42001.aims_data_quality_requirements, name="aimsDataResource__aims_data_quality_requirements", curie=ISO42001.curie('aims_data_quality_requirements'),
                   model_uri=ISO42001.aimsDataResource__aims_data_quality_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_quality_results = Slot(uri=ISO42001.aims_data_quality_results, name="aimsDataResource__aims_data_quality_results", curie=ISO42001.curie('aims_data_quality_results'),
                   model_uri=ISO42001.aimsDataResource__aims_data_quality_results, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_bias_issues = Slot(uri=ISO42001.aims_data_bias_issues, name="aimsDataResource__aims_data_bias_issues", curie=ISO42001.curie('aims_data_bias_issues'),
                   model_uri=ISO42001.aimsDataResource__aims_data_bias_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDataResource__aims_data_representativeness = Slot(uri=ISO42001.aims_data_representativeness, name="aimsDataResource__aims_data_representativeness", curie=ISO42001.curie('aims_data_representativeness'),
                   model_uri=ISO42001.aimsDataResource__aims_data_representativeness, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_labelling_process = Slot(uri=ISO42001.aims_data_labelling_process, name="aimsDataResource__aims_data_labelling_process", curie=ISO42001.curie('aims_data_labelling_process'),
                   model_uri=ISO42001.aimsDataResource__aims_data_labelling_process, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_preparation_criteria = Slot(uri=ISO42001.aims_data_preparation_criteria, name="aimsDataResource__aims_data_preparation_criteria", curie=ISO42001.curie('aims_data_preparation_criteria'),
                   model_uri=ISO42001.aimsDataResource__aims_data_preparation_criteria, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_preparation_methods = Slot(uri=ISO42001.aims_data_preparation_methods, name="aimsDataResource__aims_data_preparation_methods", curie=ISO42001.curie('aims_data_preparation_methods'),
                   model_uri=ISO42001.aimsDataResource__aims_data_preparation_methods, domain=None, range=Optional[Union[Union[str, "AimsDataPreparationMethod"], list[Union[str, "AimsDataPreparationMethod"]]]])

slots.aimsDataResource__aims_data_last_updated = Slot(uri=ISO42001.aims_data_last_updated, name="aimsDataResource__aims_data_last_updated", curie=ISO42001.curie('aims_data_last_updated'),
                   model_uri=ISO42001.aimsDataResource__aims_data_last_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsDataResource__aims_data_retention = Slot(uri=ISO42001.aims_data_retention, name="aimsDataResource__aims_data_retention", curie=ISO42001.curie('aims_data_retention'),
                   model_uri=ISO42001.aimsDataResource__aims_data_retention, domain=None, range=Optional[str])

slots.aimsDataResource__aims_data_classification = Slot(uri=ISO42001.aims_data_classification, name="aimsDataResource__aims_data_classification", curie=ISO42001.curie('aims_data_classification'),
                   model_uri=ISO42001.aimsDataResource__aims_data_classification, domain=None, range=Optional[str])

slots.aimsToolingResource__aims_tool_category = Slot(uri=ISO42001.aims_tool_category, name="aimsToolingResource__aims_tool_category", curie=ISO42001.curie('aims_tool_category'),
                   model_uri=ISO42001.aimsToolingResource__aims_tool_category, domain=None, range=Optional[str])

slots.aimsToolingResource__aims_tool_version = Slot(uri=ISO42001.aims_tool_version, name="aimsToolingResource__aims_tool_version", curie=ISO42001.curie('aims_tool_version'),
                   model_uri=ISO42001.aimsToolingResource__aims_tool_version, domain=None, range=Optional[str])

slots.aimsToolingResource__aims_tool_vendor = Slot(uri=ISO42001.aims_tool_vendor, name="aimsToolingResource__aims_tool_vendor", curie=ISO42001.curie('aims_tool_vendor'),
                   model_uri=ISO42001.aimsToolingResource__aims_tool_vendor, domain=None, range=Optional[str])

slots.aimsToolingResource__aims_tool_licence = Slot(uri=ISO42001.aims_tool_licence, name="aimsToolingResource__aims_tool_licence", curie=ISO42001.curie('aims_tool_licence'),
                   model_uri=ISO42001.aimsToolingResource__aims_tool_licence, domain=None, range=Optional[str])

slots.aimsToolingResource__aims_tool_purpose = Slot(uri=ISO42001.aims_tool_purpose, name="aimsToolingResource__aims_tool_purpose", curie=ISO42001.curie('aims_tool_purpose'),
                   model_uri=ISO42001.aimsToolingResource__aims_tool_purpose, domain=None, range=Optional[str])

slots.aimsComputingResource__aims_computing_requirements = Slot(uri=ISO42001.aims_computing_requirements, name="aimsComputingResource__aims_computing_requirements", curie=ISO42001.curie('aims_computing_requirements'),
                   model_uri=ISO42001.aimsComputingResource__aims_computing_requirements, domain=None, range=Optional[str])

slots.aimsComputingResource__aims_computing_location = Slot(uri=ISO42001.aims_computing_location, name="aimsComputingResource__aims_computing_location", curie=ISO42001.curie('aims_computing_location'),
                   model_uri=ISO42001.aimsComputingResource__aims_computing_location, domain=None, range=Optional[str])

slots.aimsComputingResource__aims_computing_processing = Slot(uri=ISO42001.aims_computing_processing, name="aimsComputingResource__aims_computing_processing", curie=ISO42001.curie('aims_computing_processing'),
                   model_uri=ISO42001.aimsComputingResource__aims_computing_processing, domain=None, range=Optional[str])

slots.aimsComputingResource__aims_computing_hardware_impact = Slot(uri=ISO42001.aims_computing_hardware_impact, name="aimsComputingResource__aims_computing_hardware_impact", curie=ISO42001.curie('aims_computing_hardware_impact'),
                   model_uri=ISO42001.aimsComputingResource__aims_computing_hardware_impact, domain=None, range=Optional[str])

slots.aimsHumanResource__aims_human_role = Slot(uri=ISO42001.aims_human_role, name="aimsHumanResource__aims_human_role", curie=ISO42001.curie('aims_human_role'),
                   model_uri=ISO42001.aimsHumanResource__aims_human_role, domain=None, range=Optional[Union[str, AimsRoleAimsId]])

slots.aimsHumanResource__aims_human_competences = Slot(uri=ISO42001.aims_human_competences, name="aimsHumanResource__aims_human_competences", curie=ISO42001.curie('aims_human_competences'),
                   model_uri=ISO42001.aimsHumanResource__aims_human_competences, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsHumanResource__aims_human_activities = Slot(uri=ISO42001.aims_human_activities, name="aimsHumanResource__aims_human_activities", curie=ISO42001.curie('aims_human_activities'),
                   model_uri=ISO42001.aimsHumanResource__aims_human_activities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsHumanResource__aims_human_diversity = Slot(uri=ISO42001.aims_human_diversity, name="aimsHumanResource__aims_human_diversity", curie=ISO42001.curie('aims_human_diversity'),
                   model_uri=ISO42001.aimsHumanResource__aims_human_diversity, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_life_cycle_model = Slot(uri=ISO42001.aims_development_life_cycle_model, name="aimsDevelopmentProcess__aims_development_life_cycle_model", curie=ISO42001.curie('aims_development_life_cycle_model'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_life_cycle_model, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_testing = Slot(uri=ISO42001.aims_development_testing, name="aimsDevelopmentProcess__aims_development_testing", curie=ISO42001.curie('aims_development_testing'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_testing, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_human_oversight = Slot(uri=ISO42001.aims_development_human_oversight, name="aimsDevelopmentProcess__aims_development_human_oversight", curie=ISO42001.curie('aims_development_human_oversight'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_human_oversight, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_impact_assessment_stages = Slot(uri=ISO42001.aims_development_impact_assessment_stages, name="aimsDevelopmentProcess__aims_development_impact_assessment_stages", curie=ISO42001.curie('aims_development_impact_assessment_stages'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_impact_assessment_stages, domain=None, range=Optional[Union[Union[str, "AimsLifecycleStage"], list[Union[str, "AimsLifecycleStage"]]]])

slots.aimsDevelopmentProcess__aims_development_training_data_rules = Slot(uri=ISO42001.aims_development_training_data_rules, name="aimsDevelopmentProcess__aims_development_training_data_rules", curie=ISO42001.curie('aims_development_training_data_rules'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_training_data_rules, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_expertise = Slot(uri=ISO42001.aims_development_expertise, name="aimsDevelopmentProcess__aims_development_expertise", curie=ISO42001.curie('aims_development_expertise'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_expertise, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_release_criteria = Slot(uri=ISO42001.aims_development_release_criteria, name="aimsDevelopmentProcess__aims_development_release_criteria", curie=ISO42001.curie('aims_development_release_criteria'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_release_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDevelopmentProcess__aims_development_approvals = Slot(uri=ISO42001.aims_development_approvals, name="aimsDevelopmentProcess__aims_development_approvals", curie=ISO42001.curie('aims_development_approvals'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_approvals, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsDevelopmentProcess__aims_development_change_control = Slot(uri=ISO42001.aims_development_change_control, name="aimsDevelopmentProcess__aims_development_change_control", curie=ISO42001.curie('aims_development_change_control'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_change_control, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_usability = Slot(uri=ISO42001.aims_development_usability, name="aimsDevelopmentProcess__aims_development_usability", curie=ISO42001.curie('aims_development_usability'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_usability, domain=None, range=Optional[str])

slots.aimsDevelopmentProcess__aims_development_party_engagement = Slot(uri=ISO42001.aims_development_party_engagement, name="aimsDevelopmentProcess__aims_development_party_engagement", curie=ISO42001.curie('aims_development_party_engagement'),
                   model_uri=ISO42001.aimsDevelopmentProcess__aims_development_party_engagement, domain=None, range=Optional[str])

slots.aimsResponsibleUseProcess__aims_use_approvals = Slot(uri=ISO42001.aims_use_approvals, name="aimsResponsibleUseProcess__aims_use_approvals", curie=ISO42001.curie('aims_use_approvals'),
                   model_uri=ISO42001.aimsResponsibleUseProcess__aims_use_approvals, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsResponsibleUseProcess__aims_use_costs = Slot(uri=ISO42001.aims_use_costs, name="aimsResponsibleUseProcess__aims_use_costs", curie=ISO42001.curie('aims_use_costs'),
                   model_uri=ISO42001.aimsResponsibleUseProcess__aims_use_costs, domain=None, range=Optional[str])

slots.aimsResponsibleUseProcess__aims_use_sourcing_requirements = Slot(uri=ISO42001.aims_use_sourcing_requirements, name="aimsResponsibleUseProcess__aims_use_sourcing_requirements", curie=ISO42001.curie('aims_use_sourcing_requirements'),
                   model_uri=ISO42001.aimsResponsibleUseProcess__aims_use_sourcing_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsResponsibleUseProcess__aims_use_legal_requirements = Slot(uri=ISO42001.aims_use_legal_requirements, name="aimsResponsibleUseProcess__aims_use_legal_requirements", curie=ISO42001.curie('aims_use_legal_requirements'),
                   model_uri=ISO42001.aimsResponsibleUseProcess__aims_use_legal_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsTechnicalDocumentation__aims_technical_doc_audiences = Slot(uri=ISO42001.aims_technical_doc_audiences, name="aimsTechnicalDocumentation__aims_technical_doc_audiences", curie=ISO42001.curie('aims_technical_doc_audiences'),
                   model_uri=ISO42001.aimsTechnicalDocumentation__aims_technical_doc_audiences, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsTechnicalDocumentation__aims_technical_doc_form = Slot(uri=ISO42001.aims_technical_doc_form, name="aimsTechnicalDocumentation__aims_technical_doc_form", curie=ISO42001.curie('aims_technical_doc_form'),
                   model_uri=ISO42001.aimsTechnicalDocumentation__aims_technical_doc_form, domain=None, range=Optional[str])

slots.aimsTechnicalDocumentation__aims_technical_doc_contents = Slot(uri=ISO42001.aims_technical_doc_contents, name="aimsTechnicalDocumentation__aims_technical_doc_contents", curie=ISO42001.curie('aims_technical_doc_contents'),
                   model_uri=ISO42001.aimsTechnicalDocumentation__aims_technical_doc_contents, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsTechnicalDocumentation__aims_technical_doc_failure_plan = Slot(uri=ISO42001.aims_technical_doc_failure_plan, name="aimsTechnicalDocumentation__aims_technical_doc_failure_plan", curie=ISO42001.curie('aims_technical_doc_failure_plan'),
                   model_uri=ISO42001.aimsTechnicalDocumentation__aims_technical_doc_failure_plan, domain=None, range=Optional[str])

slots.aimsUserInformation__aims_user_information_contents = Slot(uri=ISO42001.aims_user_information_contents, name="aimsUserInformation__aims_user_information_contents", curie=ISO42001.curie('aims_user_information_contents'),
                   model_uri=ISO42001.aimsUserInformation__aims_user_information_contents, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsUserInformation__aims_user_information_channels = Slot(uri=ISO42001.aims_user_information_channels, name="aimsUserInformation__aims_user_information_channels", curie=ISO42001.curie('aims_user_information_channels'),
                   model_uri=ISO42001.aimsUserInformation__aims_user_information_channels, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsUserInformation__aims_user_information_criteria = Slot(uri=ISO42001.aims_user_information_criteria, name="aimsUserInformation__aims_user_information_criteria", curie=ISO42001.curie('aims_user_information_criteria'),
                   model_uri=ISO42001.aimsUserInformation__aims_user_information_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsUserInformation__aims_user_information_validated = Slot(uri=ISO42001.aims_user_information_validated, name="aimsUserInformation__aims_user_information_validated", curie=ISO42001.curie('aims_user_information_validated'),
                   model_uri=ISO42001.aimsUserInformation__aims_user_information_validated, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsIncidentCommunicationPlan__aims_incident_plan_categories = Slot(uri=ISO42001.aims_incident_plan_categories, name="aimsIncidentCommunicationPlan__aims_incident_plan_categories", curie=ISO42001.curie('aims_incident_plan_categories'),
                   model_uri=ISO42001.aimsIncidentCommunicationPlan__aims_incident_plan_categories, domain=None, range=Optional[Union[Union[str, "AimsIncidentCategory"], list[Union[str, "AimsIncidentCategory"]]]])

slots.aimsIncidentCommunicationPlan__aims_incident_plan_timeline = Slot(uri=ISO42001.aims_incident_plan_timeline, name="aimsIncidentCommunicationPlan__aims_incident_plan_timeline", curie=ISO42001.curie('aims_incident_plan_timeline'),
                   model_uri=ISO42001.aimsIncidentCommunicationPlan__aims_incident_plan_timeline, domain=None, range=Optional[str])

slots.aimsIncidentCommunicationPlan__aims_incident_plan_authorities = Slot(uri=ISO42001.aims_incident_plan_authorities, name="aimsIncidentCommunicationPlan__aims_incident_plan_authorities", curie=ISO42001.curie('aims_incident_plan_authorities'),
                   model_uri=ISO42001.aimsIncidentCommunicationPlan__aims_incident_plan_authorities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsIncidentCommunicationPlan__aims_incident_plan_details = Slot(uri=ISO42001.aims_incident_plan_details, name="aimsIncidentCommunicationPlan__aims_incident_plan_details", curie=ISO42001.curie('aims_incident_plan_details'),
                   model_uri=ISO42001.aimsIncidentCommunicationPlan__aims_incident_plan_details, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsIncidentCommunicationPlan__aims_incident_plan_integration = Slot(uri=ISO42001.aims_incident_plan_integration, name="aimsIncidentCommunicationPlan__aims_incident_plan_integration", curie=ISO42001.curie('aims_incident_plan_integration'),
                   model_uri=ISO42001.aimsIncidentCommunicationPlan__aims_incident_plan_integration, domain=None, range=Optional[str])

slots.aimsReportingObligation__aims_obligation_parties = Slot(uri=ISO42001.aims_obligation_parties, name="aimsReportingObligation__aims_obligation_parties", curie=ISO42001.curie('aims_obligation_parties'),
                   model_uri=ISO42001.aimsReportingObligation__aims_obligation_parties, domain=None, range=Optional[Union[Union[str, AimsInterestedPartyAimsId], list[Union[str, AimsInterestedPartyAimsId]]]])

slots.aimsReportingObligation__aims_obligation_basis = Slot(uri=ISO42001.aims_obligation_basis, name="aimsReportingObligation__aims_obligation_basis", curie=ISO42001.curie('aims_obligation_basis'),
                   model_uri=ISO42001.aimsReportingObligation__aims_obligation_basis, domain=None, range=Optional[str])

slots.aimsReportingObligation__aims_obligation_jurisdiction = Slot(uri=ISO42001.aims_obligation_jurisdiction, name="aimsReportingObligation__aims_obligation_jurisdiction", curie=ISO42001.curie('aims_obligation_jurisdiction'),
                   model_uri=ISO42001.aimsReportingObligation__aims_obligation_jurisdiction, domain=None, range=Optional[str])

slots.aimsReportingObligation__aims_obligation_contents = Slot(uri=ISO42001.aims_obligation_contents, name="aimsReportingObligation__aims_obligation_contents", curie=ISO42001.curie('aims_obligation_contents'),
                   model_uri=ISO42001.aimsReportingObligation__aims_obligation_contents, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsReportingObligation__aims_obligation_timeframe = Slot(uri=ISO42001.aims_obligation_timeframe, name="aimsReportingObligation__aims_obligation_timeframe", curie=ISO42001.curie('aims_obligation_timeframe'),
                   model_uri=ISO42001.aimsReportingObligation__aims_obligation_timeframe, domain=None, range=Optional[str])

slots.aimsResource__aims_support_category = Slot(uri=ISO42001.aims_support_category, name="aimsResource__aims_support_category", curie=ISO42001.curie('aims_support_category'),
                   model_uri=ISO42001.aimsResource__aims_support_category, domain=None, range=Optional[str])

slots.aimsResource__aims_support_quantity = Slot(uri=ISO42001.aims_support_quantity, name="aimsResource__aims_support_quantity", curie=ISO42001.curie('aims_support_quantity'),
                   model_uri=ISO42001.aimsResource__aims_support_quantity, domain=None, range=Optional[str])

slots.aimsResource__aims_support_allocation_date = Slot(uri=ISO42001.aims_support_allocation_date, name="aimsResource__aims_support_allocation_date", curie=ISO42001.curie('aims_support_allocation_date'),
                   model_uri=ISO42001.aimsResource__aims_support_allocation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsResource__aims_support_allocated_to = Slot(uri=ISO42001.aims_support_allocated_to, name="aimsResource__aims_support_allocated_to", curie=ISO42001.curie('aims_support_allocated_to'),
                   model_uri=ISO42001.aimsResource__aims_support_allocated_to, domain=None, range=Optional[str])

slots.aimsResource__aims_support_cost = Slot(uri=ISO42001.aims_support_cost, name="aimsResource__aims_support_cost", curie=ISO42001.curie('aims_support_cost'),
                   model_uri=ISO42001.aimsResource__aims_support_cost, domain=None, range=Optional[str])

slots.aimsResource__aims_support_availability = Slot(uri=ISO42001.aims_support_availability, name="aimsResource__aims_support_availability", curie=ISO42001.curie('aims_support_availability'),
                   model_uri=ISO42001.aimsResource__aims_support_availability, domain=None, range=Optional[str])

slots.aimsCompetenceRecord__aims_competence_person = Slot(uri=ISO42001.aims_competence_person, name="aimsCompetenceRecord__aims_competence_person", curie=ISO42001.curie('aims_competence_person'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_person, domain=None, range=Optional[str])

slots.aimsCompetenceRecord__aims_competence_role = Slot(uri=ISO42001.aims_competence_role, name="aimsCompetenceRecord__aims_competence_role", curie=ISO42001.curie('aims_competence_role'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_role, domain=None, range=Optional[Union[str, AimsRoleAimsId]])

slots.aimsCompetenceRecord__aims_competence_required = Slot(uri=ISO42001.aims_competence_required, name="aimsCompetenceRecord__aims_competence_required", curie=ISO42001.curie('aims_competence_required'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_required, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCompetenceRecord__aims_competence_education = Slot(uri=ISO42001.aims_competence_education, name="aimsCompetenceRecord__aims_competence_education", curie=ISO42001.curie('aims_competence_education'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_education, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCompetenceRecord__aims_competence_training = Slot(uri=ISO42001.aims_competence_training, name="aimsCompetenceRecord__aims_competence_training", curie=ISO42001.curie('aims_competence_training'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_training, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCompetenceRecord__aims_competence_experience = Slot(uri=ISO42001.aims_competence_experience, name="aimsCompetenceRecord__aims_competence_experience", curie=ISO42001.curie('aims_competence_experience'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_experience, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCompetenceRecord__aims_competence_assessment_date = Slot(uri=ISO42001.aims_competence_assessment_date, name="aimsCompetenceRecord__aims_competence_assessment_date", curie=ISO42001.curie('aims_competence_assessment_date'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsCompetenceRecord__aims_competence_gaps = Slot(uri=ISO42001.aims_competence_gaps, name="aimsCompetenceRecord__aims_competence_gaps", curie=ISO42001.curie('aims_competence_gaps'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_gaps, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCompetenceRecord__aims_competence_actions = Slot(uri=ISO42001.aims_competence_actions, name="aimsCompetenceRecord__aims_competence_actions", curie=ISO42001.curie('aims_competence_actions'),
                   model_uri=ISO42001.aimsCompetenceRecord__aims_competence_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAwarenessProgramme__aims_awareness_topics = Slot(uri=ISO42001.aims_awareness_topics, name="aimsAwarenessProgramme__aims_awareness_topics", curie=ISO42001.curie('aims_awareness_topics'),
                   model_uri=ISO42001.aimsAwarenessProgramme__aims_awareness_topics, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAwarenessProgramme__aims_awareness_methods = Slot(uri=ISO42001.aims_awareness_methods, name="aimsAwarenessProgramme__aims_awareness_methods", curie=ISO42001.curie('aims_awareness_methods'),
                   model_uri=ISO42001.aimsAwarenessProgramme__aims_awareness_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAwarenessProgramme__aims_awareness_audience = Slot(uri=ISO42001.aims_awareness_audience, name="aimsAwarenessProgramme__aims_awareness_audience", curie=ISO42001.curie('aims_awareness_audience'),
                   model_uri=ISO42001.aimsAwarenessProgramme__aims_awareness_audience, domain=None, range=Optional[str])

slots.aimsAwarenessProgramme__aims_awareness_frequency = Slot(uri=ISO42001.aims_awareness_frequency, name="aimsAwarenessProgramme__aims_awareness_frequency", curie=ISO42001.curie('aims_awareness_frequency'),
                   model_uri=ISO42001.aimsAwarenessProgramme__aims_awareness_frequency, domain=None, range=Optional[str])

slots.aimsAwarenessProgramme__aims_awareness_completion_tracking = Slot(uri=ISO42001.aims_awareness_completion_tracking, name="aimsAwarenessProgramme__aims_awareness_completion_tracking", curie=ISO42001.curie('aims_awareness_completion_tracking'),
                   model_uri=ISO42001.aimsAwarenessProgramme__aims_awareness_completion_tracking, domain=None, range=Optional[str])

slots.aimsAwarenessProgramme__aims_awareness_effectiveness = Slot(uri=ISO42001.aims_awareness_effectiveness, name="aimsAwarenessProgramme__aims_awareness_effectiveness", curie=ISO42001.curie('aims_awareness_effectiveness'),
                   model_uri=ISO42001.aimsAwarenessProgramme__aims_awareness_effectiveness, domain=None, range=Optional[str])

slots.aimsCommunicationPlan__aims_communication_items = Slot(uri=ISO42001.aims_communication_items, name="aimsCommunicationPlan__aims_communication_items", curie=ISO42001.curie('aims_communication_items'),
                   model_uri=ISO42001.aimsCommunicationPlan__aims_communication_items, domain=None, range=Optional[Union[Union[dict, AimsCommunication], list[Union[dict, AimsCommunication]]]])

slots.aimsCommunication__aims_communication_subject = Slot(uri=ISO42001.aims_communication_subject, name="aimsCommunication__aims_communication_subject", curie=ISO42001.curie('aims_communication_subject'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_subject, domain=None, range=str)

slots.aimsCommunication__aims_communication_purpose = Slot(uri=ISO42001.aims_communication_purpose, name="aimsCommunication__aims_communication_purpose", curie=ISO42001.curie('aims_communication_purpose'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_purpose, domain=None, range=Optional[str])

slots.aimsCommunication__aims_communication_audience = Slot(uri=ISO42001.aims_communication_audience, name="aimsCommunication__aims_communication_audience", curie=ISO42001.curie('aims_communication_audience'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_audience, domain=None, range=Optional[str])

slots.aimsCommunication__aims_communication_external = Slot(uri=ISO42001.aims_communication_external, name="aimsCommunication__aims_communication_external", curie=ISO42001.curie('aims_communication_external'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_external, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsCommunication__aims_communication_timing = Slot(uri=ISO42001.aims_communication_timing, name="aimsCommunication__aims_communication_timing", curie=ISO42001.curie('aims_communication_timing'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_timing, domain=None, range=Optional[str])

slots.aimsCommunication__aims_communication_method = Slot(uri=ISO42001.aims_communication_method, name="aimsCommunication__aims_communication_method", curie=ISO42001.curie('aims_communication_method'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_method, domain=None, range=Optional[str])

slots.aimsCommunication__aims_communication_records_required = Slot(uri=ISO42001.aims_communication_records_required, name="aimsCommunication__aims_communication_records_required", curie=ISO42001.curie('aims_communication_records_required'),
                   model_uri=ISO42001.aimsCommunication__aims_communication_records_required, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsDocumentedInformation__aims_document_kind = Slot(uri=ISO42001.aims_document_kind, name="aimsDocumentedInformation__aims_document_kind", curie=ISO42001.curie('aims_document_kind'),
                   model_uri=ISO42001.aimsDocumentedInformation__aims_document_kind, domain=None, range=Union[str, "AimsDocumentKind"])

slots.aimsOperationalProcedure__aims_procedure_scope = Slot(uri=ISO42001.aims_procedure_scope, name="aimsOperationalProcedure__aims_procedure_scope", curie=ISO42001.curie('aims_procedure_scope'),
                   model_uri=ISO42001.aimsOperationalProcedure__aims_procedure_scope, domain=None, range=Optional[str])

slots.aimsOperationalProcedure__aims_procedure_criteria = Slot(uri=ISO42001.aims_procedure_criteria, name="aimsOperationalProcedure__aims_procedure_criteria", curie=ISO42001.curie('aims_procedure_criteria'),
                   model_uri=ISO42001.aimsOperationalProcedure__aims_procedure_criteria, domain=None, range=Optional[str])

slots.aimsOperationalProcedure__aims_procedure_control_measures = Slot(uri=ISO42001.aims_procedure_control_measures, name="aimsOperationalProcedure__aims_procedure_control_measures", curie=ISO42001.curie('aims_procedure_control_measures'),
                   model_uri=ISO42001.aimsOperationalProcedure__aims_procedure_control_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsOperationalProcedure__aims_procedure_roles = Slot(uri=ISO42001.aims_procedure_roles, name="aimsOperationalProcedure__aims_procedure_roles", curie=ISO42001.curie('aims_procedure_roles'),
                   model_uri=ISO42001.aimsOperationalProcedure__aims_procedure_roles, domain=None, range=Optional[Union[Union[str, AimsRoleAimsId], list[Union[str, AimsRoleAimsId]]]])

slots.aimsOperationalProcedure__aims_procedure_change_control = Slot(uri=ISO42001.aims_procedure_change_control, name="aimsOperationalProcedure__aims_procedure_change_control", curie=ISO42001.curie('aims_procedure_change_control'),
                   model_uri=ISO42001.aimsOperationalProcedure__aims_procedure_change_control, domain=None, range=Optional[str])

slots.aimsMonitoringProgramme__aims_monitoring_items = Slot(uri=ISO42001.aims_monitoring_items, name="aimsMonitoringProgramme__aims_monitoring_items", curie=ISO42001.curie('aims_monitoring_items'),
                   model_uri=ISO42001.aimsMonitoringProgramme__aims_monitoring_items, domain=None, range=Optional[Union[Union[dict, AimsMonitoringItem], list[Union[dict, AimsMonitoringItem]]]])

slots.aimsMonitoringItem__aims_monitoring_metric = Slot(uri=ISO42001.aims_monitoring_metric, name="aimsMonitoringItem__aims_monitoring_metric", curie=ISO42001.curie('aims_monitoring_metric'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_metric, domain=None, range=str)

slots.aimsMonitoringItem__aims_monitoring_description = Slot(uri=ISO42001.aims_monitoring_description, name="aimsMonitoringItem__aims_monitoring_description", curie=ISO42001.curie('aims_monitoring_description'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_description, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_method = Slot(uri=ISO42001.aims_monitoring_method, name="aimsMonitoringItem__aims_monitoring_method", curie=ISO42001.curie('aims_monitoring_method'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_method, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_frequency = Slot(uri=ISO42001.aims_monitoring_frequency, name="aimsMonitoringItem__aims_monitoring_frequency", curie=ISO42001.curie('aims_monitoring_frequency'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_frequency, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_analysis_frequency = Slot(uri=ISO42001.aims_monitoring_analysis_frequency, name="aimsMonitoringItem__aims_monitoring_analysis_frequency", curie=ISO42001.curie('aims_monitoring_analysis_frequency'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_analysis_frequency, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_analyst = Slot(uri=ISO42001.aims_monitoring_analyst, name="aimsMonitoringItem__aims_monitoring_analyst", curie=ISO42001.curie('aims_monitoring_analyst'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_analyst, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_target = Slot(uri=ISO42001.aims_monitoring_target, name="aimsMonitoringItem__aims_monitoring_target", curie=ISO42001.curie('aims_monitoring_target'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_target, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_alert_threshold = Slot(uri=ISO42001.aims_monitoring_alert_threshold, name="aimsMonitoringItem__aims_monitoring_alert_threshold", curie=ISO42001.curie('aims_monitoring_alert_threshold'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_alert_threshold, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_current_value = Slot(uri=ISO42001.aims_monitoring_current_value, name="aimsMonitoringItem__aims_monitoring_current_value", curie=ISO42001.curie('aims_monitoring_current_value'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_current_value, domain=None, range=Optional[str])

slots.aimsMonitoringItem__aims_monitoring_trend = Slot(uri=ISO42001.aims_monitoring_trend, name="aimsMonitoringItem__aims_monitoring_trend", curie=ISO42001.curie('aims_monitoring_trend'),
                   model_uri=ISO42001.aimsMonitoringItem__aims_monitoring_trend, domain=None, range=Optional[str])

slots.aimsAuditProgramme__aims_programme_period = Slot(uri=ISO42001.aims_programme_period, name="aimsAuditProgramme__aims_programme_period", curie=ISO42001.curie('aims_programme_period'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_period, domain=None, range=Optional[str])

slots.aimsAuditProgramme__aims_programme_audits = Slot(uri=ISO42001.aims_programme_audits, name="aimsAuditProgramme__aims_programme_audits", curie=ISO42001.curie('aims_programme_audits'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_audits, domain=None, range=Optional[Union[Union[str, AimsAuditAimsId], list[Union[str, AimsAuditAimsId]]]])

slots.aimsAuditProgramme__aims_programme_frequency_rationale = Slot(uri=ISO42001.aims_programme_frequency_rationale, name="aimsAuditProgramme__aims_programme_frequency_rationale", curie=ISO42001.curie('aims_programme_frequency_rationale'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_frequency_rationale, domain=None, range=Optional[str])

slots.aimsAuditProgramme__aims_programme_methods = Slot(uri=ISO42001.aims_programme_methods, name="aimsAuditProgramme__aims_programme_methods", curie=ISO42001.curie('aims_programme_methods'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_methods, domain=None, range=Optional[str])

slots.aimsAuditProgramme__aims_programme_responsibilities = Slot(uri=ISO42001.aims_programme_responsibilities, name="aimsAuditProgramme__aims_programme_responsibilities", curie=ISO42001.curie('aims_programme_responsibilities'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAuditProgramme__aims_programme_resources = Slot(uri=ISO42001.aims_programme_resources, name="aimsAuditProgramme__aims_programme_resources", curie=ISO42001.curie('aims_programme_resources'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_resources, domain=None, range=Optional[str])

slots.aimsAuditProgramme__aims_programme_auditor_selection = Slot(uri=ISO42001.aims_programme_auditor_selection, name="aimsAuditProgramme__aims_programme_auditor_selection", curie=ISO42001.curie('aims_programme_auditor_selection'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_auditor_selection, domain=None, range=Optional[str])

slots.aimsAuditProgramme__aims_programme_status = Slot(uri=ISO42001.aims_programme_status, name="aimsAuditProgramme__aims_programme_status", curie=ISO42001.curie('aims_programme_status'),
                   model_uri=ISO42001.aimsAuditProgramme__aims_programme_status, domain=None, range=Optional[str])

slots.aimsAudit__aims_audit_type = Slot(uri=ISO42001.aims_audit_type, name="aimsAudit__aims_audit_type", curie=ISO42001.curie('aims_audit_type'),
                   model_uri=ISO42001.aimsAudit__aims_audit_type, domain=None, range=Union[str, "AimsAuditType"])

slots.aimsAudit__aims_audit_standards = Slot(uri=ISO42001.aims_audit_standards, name="aimsAudit__aims_audit_standards", curie=ISO42001.curie('aims_audit_standards'),
                   model_uri=ISO42001.aimsAudit__aims_audit_standards, domain=None, range=Optional[Union[Union[str, "AimsManagementSystemStandard"], list[Union[str, "AimsManagementSystemStandard"]]]])

slots.aimsAudit__aims_audit_scope = Slot(uri=ISO42001.aims_audit_scope, name="aimsAudit__aims_audit_scope", curie=ISO42001.curie('aims_audit_scope'),
                   model_uri=ISO42001.aimsAudit__aims_audit_scope, domain=None, range=Optional[str])

slots.aimsAudit__aims_audit_criteria = Slot(uri=ISO42001.aims_audit_criteria, name="aimsAudit__aims_audit_criteria", curie=ISO42001.curie('aims_audit_criteria'),
                   model_uri=ISO42001.aimsAudit__aims_audit_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAudit__aims_audit_objectives = Slot(uri=ISO42001.aims_audit_objectives, name="aimsAudit__aims_audit_objectives", curie=ISO42001.curie('aims_audit_objectives'),
                   model_uri=ISO42001.aimsAudit__aims_audit_objectives, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAudit__aims_audit_period_start = Slot(uri=ISO42001.aims_audit_period_start, name="aimsAudit__aims_audit_period_start", curie=ISO42001.curie('aims_audit_period_start'),
                   model_uri=ISO42001.aimsAudit__aims_audit_period_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsAudit__aims_audit_period_end = Slot(uri=ISO42001.aims_audit_period_end, name="aimsAudit__aims_audit_period_end", curie=ISO42001.curie('aims_audit_period_end'),
                   model_uri=ISO42001.aimsAudit__aims_audit_period_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsAudit__aims_audit_lead = Slot(uri=ISO42001.aims_audit_lead, name="aimsAudit__aims_audit_lead", curie=ISO42001.curie('aims_audit_lead'),
                   model_uri=ISO42001.aimsAudit__aims_audit_lead, domain=None, range=Optional[str])

slots.aimsAudit__aims_audit_team = Slot(uri=ISO42001.aims_audit_team, name="aimsAudit__aims_audit_team", curie=ISO42001.curie('aims_audit_team'),
                   model_uri=ISO42001.aimsAudit__aims_audit_team, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAudit__aims_audit_auditees = Slot(uri=ISO42001.aims_audit_auditees, name="aimsAudit__aims_audit_auditees", curie=ISO42001.curie('aims_audit_auditees'),
                   model_uri=ISO42001.aimsAudit__aims_audit_auditees, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAudit__aims_audit_plan = Slot(uri=ISO42001.aims_audit_plan, name="aimsAudit__aims_audit_plan", curie=ISO42001.curie('aims_audit_plan'),
                   model_uri=ISO42001.aimsAudit__aims_audit_plan, domain=None, range=Optional[Union[str, AimsDocumentedInformationAimsId]])

slots.aimsAudit__aims_audit_findings = Slot(uri=ISO42001.aims_audit_findings, name="aimsAudit__aims_audit_findings", curie=ISO42001.curie('aims_audit_findings'),
                   model_uri=ISO42001.aimsAudit__aims_audit_findings, domain=None, range=Optional[Union[dict[Union[str, AimsAuditFindingAimsId], Union[dict, AimsAuditFinding]], list[Union[dict, AimsAuditFinding]]]])

slots.aimsAudit__aims_audit_conclusion = Slot(uri=ISO42001.aims_audit_conclusion, name="aimsAudit__aims_audit_conclusion", curie=ISO42001.curie('aims_audit_conclusion'),
                   model_uri=ISO42001.aimsAudit__aims_audit_conclusion, domain=None, range=Optional[str])

slots.aimsAudit__aims_audit_report_date = Slot(uri=ISO42001.aims_audit_report_date, name="aimsAudit__aims_audit_report_date", curie=ISO42001.curie('aims_audit_report_date'),
                   model_uri=ISO42001.aimsAudit__aims_audit_report_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsAudit__aims_audit_report_distribution = Slot(uri=ISO42001.aims_audit_report_distribution, name="aimsAudit__aims_audit_report_distribution", curie=ISO42001.curie('aims_audit_report_distribution'),
                   model_uri=ISO42001.aimsAudit__aims_audit_report_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsAuditFinding__aims_finding_type = Slot(uri=ISO42001.aims_finding_type, name="aimsAuditFinding__aims_finding_type", curie=ISO42001.curie('aims_finding_type'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_type, domain=None, range=Union[str, "AimsAuditFindingType"])

slots.aimsAuditFinding__aims_finding_control = Slot(uri=ISO42001.aims_finding_control, name="aimsAuditFinding__aims_finding_control", curie=ISO42001.curie('aims_finding_control'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_control, domain=None, range=Optional[Union[str, AimsControlAimsId]])

slots.aimsAuditFinding__aims_finding_evidence = Slot(uri=ISO42001.aims_finding_evidence, name="aimsAuditFinding__aims_finding_evidence", curie=ISO42001.curie('aims_finding_evidence'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_evidence, domain=None, range=Optional[str])

slots.aimsAuditFinding__aims_finding_root_cause = Slot(uri=ISO42001.aims_finding_root_cause, name="aimsAuditFinding__aims_finding_root_cause", curie=ISO42001.curie('aims_finding_root_cause'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_root_cause, domain=None, range=Optional[str])

slots.aimsAuditFinding__aims_finding_risk = Slot(uri=ISO42001.aims_finding_risk, name="aimsAuditFinding__aims_finding_risk", curie=ISO42001.curie('aims_finding_risk'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_risk, domain=None, range=Optional[str])

slots.aimsAuditFinding__aims_finding_recommendation = Slot(uri=ISO42001.aims_finding_recommendation, name="aimsAuditFinding__aims_finding_recommendation", curie=ISO42001.curie('aims_finding_recommendation'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_recommendation, domain=None, range=Optional[str])

slots.aimsAuditFinding__aims_finding_auditee_response = Slot(uri=ISO42001.aims_finding_auditee_response, name="aimsAuditFinding__aims_finding_auditee_response", curie=ISO42001.curie('aims_finding_auditee_response'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_auditee_response, domain=None, range=Optional[str])

slots.aimsAuditFinding__aims_finding_corrective_action = Slot(uri=ISO42001.aims_finding_corrective_action, name="aimsAuditFinding__aims_finding_corrective_action", curie=ISO42001.curie('aims_finding_corrective_action'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_corrective_action, domain=None, range=Optional[Union[str, AimsCorrectiveActionAimsId]])

slots.aimsAuditFinding__aims_finding_closure_status = Slot(uri=ISO42001.aims_finding_closure_status, name="aimsAuditFinding__aims_finding_closure_status", curie=ISO42001.curie('aims_finding_closure_status'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_closure_status, domain=None, range=Optional[str])

slots.aimsAuditFinding__aims_finding_closure_date = Slot(uri=ISO42001.aims_finding_closure_date, name="aimsAuditFinding__aims_finding_closure_date", curie=ISO42001.curie('aims_finding_closure_date'),
                   model_uri=ISO42001.aimsAuditFinding__aims_finding_closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsManagementReview__aims_review_held_on = Slot(uri=ISO42001.aims_review_held_on, name="aimsManagementReview__aims_review_held_on", curie=ISO42001.curie('aims_review_held_on'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_held_on, domain=None, range=Union[str, XSDDate])

slots.aimsManagementReview__aims_review_attendees = Slot(uri=ISO42001.aims_review_attendees, name="aimsManagementReview__aims_review_attendees", curie=ISO42001.curie('aims_review_attendees'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_attendees, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementReview__aims_review_previous_actions = Slot(uri=ISO42001.aims_review_previous_actions, name="aimsManagementReview__aims_review_previous_actions", curie=ISO42001.curie('aims_review_previous_actions'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_previous_actions, domain=None, range=Optional[str])

slots.aimsManagementReview__aims_review_context_changes = Slot(uri=ISO42001.aims_review_context_changes, name="aimsManagementReview__aims_review_context_changes", curie=ISO42001.curie('aims_review_context_changes'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_context_changes, domain=None, range=Optional[str])

slots.aimsManagementReview__aims_review_interested_party_changes = Slot(uri=ISO42001.aims_review_interested_party_changes, name="aimsManagementReview__aims_review_interested_party_changes", curie=ISO42001.curie('aims_review_interested_party_changes'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_interested_party_changes, domain=None, range=Optional[str])

slots.aimsManagementReview__aims_review_nonconformity_trends = Slot(uri=ISO42001.aims_review_nonconformity_trends, name="aimsManagementReview__aims_review_nonconformity_trends", curie=ISO42001.curie('aims_review_nonconformity_trends'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_nonconformity_trends, domain=None, range=Optional[str])

slots.aimsManagementReview__aims_review_monitoring_trends = Slot(uri=ISO42001.aims_review_monitoring_trends, name="aimsManagementReview__aims_review_monitoring_trends", curie=ISO42001.curie('aims_review_monitoring_trends'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_monitoring_trends, domain=None, range=Optional[str])

slots.aimsManagementReview__aims_review_audit_trends = Slot(uri=ISO42001.aims_review_audit_trends, name="aimsManagementReview__aims_review_audit_trends", curie=ISO42001.curie('aims_review_audit_trends'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_audit_trends, domain=None, range=Optional[str])

slots.aimsManagementReview__aims_review_improvement_opportunities = Slot(uri=ISO42001.aims_review_improvement_opportunities, name="aimsManagementReview__aims_review_improvement_opportunities", curie=ISO42001.curie('aims_review_improvement_opportunities'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_improvement_opportunities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementReview__aims_review_decisions = Slot(uri=ISO42001.aims_review_decisions, name="aimsManagementReview__aims_review_decisions", curie=ISO42001.curie('aims_review_decisions'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_decisions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementReview__aims_review_system_changes = Slot(uri=ISO42001.aims_review_system_changes, name="aimsManagementReview__aims_review_system_changes", curie=ISO42001.curie('aims_review_system_changes'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_system_changes, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementReview__aims_review_actions = Slot(uri=ISO42001.aims_review_actions, name="aimsManagementReview__aims_review_actions", curie=ISO42001.curie('aims_review_actions'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsManagementReview__aims_review_next_date = Slot(uri=ISO42001.aims_review_next_date, name="aimsManagementReview__aims_review_next_date", curie=ISO42001.curie('aims_review_next_date'),
                   model_uri=ISO42001.aimsManagementReview__aims_review_next_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsNonconformity__aims_nonconformity_source = Slot(uri=ISO42001.aims_nonconformity_source, name="aimsNonconformity__aims_nonconformity_source", curie=ISO42001.curie('aims_nonconformity_source'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_source, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_detected_on = Slot(uri=ISO42001.aims_nonconformity_detected_on, name="aimsNonconformity__aims_nonconformity_detected_on", curie=ISO42001.curie('aims_nonconformity_detected_on'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_detected_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsNonconformity__aims_nonconformity_detected_by = Slot(uri=ISO42001.aims_nonconformity_detected_by, name="aimsNonconformity__aims_nonconformity_detected_by", curie=ISO42001.curie('aims_nonconformity_detected_by'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_detected_by, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_requirement = Slot(uri=ISO42001.aims_nonconformity_requirement, name="aimsNonconformity__aims_nonconformity_requirement", curie=ISO42001.curie('aims_nonconformity_requirement'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_requirement, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_immediate_actions = Slot(uri=ISO42001.aims_nonconformity_immediate_actions, name="aimsNonconformity__aims_nonconformity_immediate_actions", curie=ISO42001.curie('aims_nonconformity_immediate_actions'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_immediate_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsNonconformity__aims_nonconformity_consequences = Slot(uri=ISO42001.aims_nonconformity_consequences, name="aimsNonconformity__aims_nonconformity_consequences", curie=ISO42001.curie('aims_nonconformity_consequences'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_consequences, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_root_cause = Slot(uri=ISO42001.aims_nonconformity_root_cause, name="aimsNonconformity__aims_nonconformity_root_cause", curie=ISO42001.curie('aims_nonconformity_root_cause'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_root_cause, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_similar_check = Slot(uri=ISO42001.aims_nonconformity_similar_check, name="aimsNonconformity__aims_nonconformity_similar_check", curie=ISO42001.curie('aims_nonconformity_similar_check'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_similar_check, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_status = Slot(uri=ISO42001.aims_nonconformity_status, name="aimsNonconformity__aims_nonconformity_status", curie=ISO42001.curie('aims_nonconformity_status'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_status, domain=None, range=Optional[str])

slots.aimsNonconformity__aims_nonconformity_closure_date = Slot(uri=ISO42001.aims_nonconformity_closure_date, name="aimsNonconformity__aims_nonconformity_closure_date", curie=ISO42001.curie('aims_nonconformity_closure_date'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsNonconformity__aims_nonconformity_closure_evidence = Slot(uri=ISO42001.aims_nonconformity_closure_evidence, name="aimsNonconformity__aims_nonconformity_closure_evidence", curie=ISO42001.curie('aims_nonconformity_closure_evidence'),
                   model_uri=ISO42001.aimsNonconformity__aims_nonconformity_closure_evidence, domain=None, range=Optional[str])

slots.aimsCorrectiveAction__aims_action_nonconformities = Slot(uri=ISO42001.aims_action_nonconformities, name="aimsCorrectiveAction__aims_action_nonconformities", curie=ISO42001.curie('aims_action_nonconformities'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_nonconformities, domain=None, range=Optional[Union[Union[str, AimsNonconformityAimsId], list[Union[str, AimsNonconformityAimsId]]]])

slots.aimsCorrectiveAction__aims_action_root_cause = Slot(uri=ISO42001.aims_action_root_cause, name="aimsCorrectiveAction__aims_action_root_cause", curie=ISO42001.curie('aims_action_root_cause'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_root_cause, domain=None, range=Optional[str])

slots.aimsCorrectiveAction__aims_action_target_date = Slot(uri=ISO42001.aims_action_target_date, name="aimsCorrectiveAction__aims_action_target_date", curie=ISO42001.curie('aims_action_target_date'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsCorrectiveAction__aims_action_completion_date = Slot(uri=ISO42001.aims_action_completion_date, name="aimsCorrectiveAction__aims_action_completion_date", curie=ISO42001.curie('aims_action_completion_date'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsCorrectiveAction__aims_action_resources = Slot(uri=ISO42001.aims_action_resources, name="aimsCorrectiveAction__aims_action_resources", curie=ISO42001.curie('aims_action_resources'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_resources, domain=None, range=Optional[str])

slots.aimsCorrectiveAction__aims_action_effectiveness_criteria = Slot(uri=ISO42001.aims_action_effectiveness_criteria, name="aimsCorrectiveAction__aims_action_effectiveness_criteria", curie=ISO42001.curie('aims_action_effectiveness_criteria'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_effectiveness_criteria, domain=None, range=Optional[str])

slots.aimsCorrectiveAction__aims_action_effectiveness_review_date = Slot(uri=ISO42001.aims_action_effectiveness_review_date, name="aimsCorrectiveAction__aims_action_effectiveness_review_date", curie=ISO42001.curie('aims_action_effectiveness_review_date'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_effectiveness_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsCorrectiveAction__aims_action_effective = Slot(uri=ISO42001.aims_action_effective, name="aimsCorrectiveAction__aims_action_effective", curie=ISO42001.curie('aims_action_effective'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_effective, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsCorrectiveAction__aims_action_system_changes = Slot(uri=ISO42001.aims_action_system_changes, name="aimsCorrectiveAction__aims_action_system_changes", curie=ISO42001.curie('aims_action_system_changes'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_system_changes, domain=None, range=Optional[str])

slots.aimsCorrectiveAction__aims_action_status = Slot(uri=ISO42001.aims_action_status, name="aimsCorrectiveAction__aims_action_status", curie=ISO42001.curie('aims_action_status'),
                   model_uri=ISO42001.aimsCorrectiveAction__aims_action_status, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_source = Slot(uri=ISO42001.aims_improvement_source, name="aimsImprovementOpportunity__aims_improvement_source", curie=ISO42001.curie('aims_improvement_source'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_source, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_identified_on = Slot(uri=ISO42001.aims_improvement_identified_on, name="aimsImprovementOpportunity__aims_improvement_identified_on", curie=ISO42001.curie('aims_improvement_identified_on'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_identified_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsImprovementOpportunity__aims_improvement_identified_by = Slot(uri=ISO42001.aims_improvement_identified_by, name="aimsImprovementOpportunity__aims_improvement_identified_by", curie=ISO42001.curie('aims_improvement_identified_by'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_identified_by, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_benefit = Slot(uri=ISO42001.aims_improvement_benefit, name="aimsImprovementOpportunity__aims_improvement_benefit", curie=ISO42001.curie('aims_improvement_benefit'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_benefit, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_priority = Slot(uri=ISO42001.aims_improvement_priority, name="aimsImprovementOpportunity__aims_improvement_priority", curie=ISO42001.curie('aims_improvement_priority'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_priority, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_plan = Slot(uri=ISO42001.aims_improvement_plan, name="aimsImprovementOpportunity__aims_improvement_plan", curie=ISO42001.curie('aims_improvement_plan'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_plan, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_target_date = Slot(uri=ISO42001.aims_improvement_target_date, name="aimsImprovementOpportunity__aims_improvement_target_date", curie=ISO42001.curie('aims_improvement_target_date'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_target_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsImprovementOpportunity__aims_improvement_completion_date = Slot(uri=ISO42001.aims_improvement_completion_date, name="aimsImprovementOpportunity__aims_improvement_completion_date", curie=ISO42001.curie('aims_improvement_completion_date'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_completion_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsImprovementOpportunity__aims_improvement_outcome = Slot(uri=ISO42001.aims_improvement_outcome, name="aimsImprovementOpportunity__aims_improvement_outcome", curie=ISO42001.curie('aims_improvement_outcome'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_outcome, domain=None, range=Optional[str])

slots.aimsImprovementOpportunity__aims_improvement_status = Slot(uri=ISO42001.aims_improvement_status, name="aimsImprovementOpportunity__aims_improvement_status", curie=ISO42001.curie('aims_improvement_status'),
                   model_uri=ISO42001.aimsImprovementOpportunity__aims_improvement_status, domain=None, range=Optional[str])

slots.aimsThirdPartyRelationship__aims_relationship_type = Slot(uri=ISO42001.aims_relationship_type, name="aimsThirdPartyRelationship__aims_relationship_type", curie=ISO42001.curie('aims_relationship_type'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_type, domain=None, range=Optional[str])

slots.aimsThirdPartyRelationship__aims_relationship_party = Slot(uri=ISO42001.aims_relationship_party, name="aimsThirdPartyRelationship__aims_relationship_party", curie=ISO42001.curie('aims_relationship_party'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_party, domain=None, range=Optional[str])

slots.aimsThirdPartyRelationship__aims_relationship_party_roles = Slot(uri=ISO42001.aims_relationship_party_roles, name="aimsThirdPartyRelationship__aims_relationship_party_roles", curie=ISO42001.curie('aims_relationship_party_roles'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_party_roles, domain=None, range=Optional[Union[Union[str, "AimsAiRole"], list[Union[str, "AimsAiRole"]]]])

slots.aimsThirdPartyRelationship__aims_relationship_contract = Slot(uri=ISO42001.aims_relationship_contract, name="aimsThirdPartyRelationship__aims_relationship_contract", curie=ISO42001.curie('aims_relationship_contract'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_contract, domain=None, range=Optional[str])

slots.aimsThirdPartyRelationship__aims_relationship_responsibilities = Slot(uri=ISO42001.aims_relationship_responsibilities, name="aimsThirdPartyRelationship__aims_relationship_responsibilities", curie=ISO42001.curie('aims_relationship_responsibilities'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsThirdPartyRelationship__aims_relationship_pii_role = Slot(uri=ISO42001.aims_relationship_pii_role, name="aimsThirdPartyRelationship__aims_relationship_pii_role", curie=ISO42001.curie('aims_relationship_pii_role'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_pii_role, domain=None, range=Optional[Union[str, "AimsPiiRole"]])

slots.aimsThirdPartyRelationship__aims_relationship_documentation = Slot(uri=ISO42001.aims_relationship_documentation, name="aimsThirdPartyRelationship__aims_relationship_documentation", curie=ISO42001.curie('aims_relationship_documentation'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_documentation, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsThirdPartyRelationship__aims_relationship_assurance_evidence = Slot(uri=ISO42001.aims_relationship_assurance_evidence, name="aimsThirdPartyRelationship__aims_relationship_assurance_evidence", curie=ISO42001.curie('aims_relationship_assurance_evidence'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_assurance_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsThirdPartyRelationship__aims_relationship_review_frequency = Slot(uri=ISO42001.aims_relationship_review_frequency, name="aimsThirdPartyRelationship__aims_relationship_review_frequency", curie=ISO42001.curie('aims_relationship_review_frequency'),
                   model_uri=ISO42001.aimsThirdPartyRelationship__aims_relationship_review_frequency, domain=None, range=Optional[str])

slots.aimsSupplierRelationship__aims_supplier_provides = Slot(uri=ISO42001.aims_supplier_provides, name="aimsSupplierRelationship__aims_supplier_provides", curie=ISO42001.curie('aims_supplier_provides'),
                   model_uri=ISO42001.aimsSupplierRelationship__aims_supplier_provides, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsSupplierRelationship__aims_supplier_risk = Slot(uri=ISO42001.aims_supplier_risk, name="aimsSupplierRelationship__aims_supplier_risk", curie=ISO42001.curie('aims_supplier_risk'),
                   model_uri=ISO42001.aimsSupplierRelationship__aims_supplier_risk, domain=None, range=Optional[Union[str, "AimsRiskLevel"]])

slots.aimsSupplierRelationship__aims_supplier_requirements = Slot(uri=ISO42001.aims_supplier_requirements, name="aimsSupplierRelationship__aims_supplier_requirements", curie=ISO42001.curie('aims_supplier_requirements'),
                   model_uri=ISO42001.aimsSupplierRelationship__aims_supplier_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsSupplierRelationship__aims_supplier_monitoring = Slot(uri=ISO42001.aims_supplier_monitoring, name="aimsSupplierRelationship__aims_supplier_monitoring", curie=ISO42001.curie('aims_supplier_monitoring'),
                   model_uri=ISO42001.aimsSupplierRelationship__aims_supplier_monitoring, domain=None, range=Optional[str])

slots.aimsSupplierRelationship__aims_supplier_integration = Slot(uri=ISO42001.aims_supplier_integration, name="aimsSupplierRelationship__aims_supplier_integration", curie=ISO42001.curie('aims_supplier_integration'),
                   model_uri=ISO42001.aimsSupplierRelationship__aims_supplier_integration, domain=None, range=Optional[str])

slots.aimsSupplierRelationship__aims_supplier_corrective_actions = Slot(uri=ISO42001.aims_supplier_corrective_actions, name="aimsSupplierRelationship__aims_supplier_corrective_actions", curie=ISO42001.curie('aims_supplier_corrective_actions'),
                   model_uri=ISO42001.aimsSupplierRelationship__aims_supplier_corrective_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCustomerRelationship__aims_customer_expectations = Slot(uri=ISO42001.aims_customer_expectations, name="aimsCustomerRelationship__aims_customer_expectations", curie=ISO42001.curie('aims_customer_expectations'),
                   model_uri=ISO42001.aimsCustomerRelationship__aims_customer_expectations, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsCustomerRelationship__aims_customer_agreement = Slot(uri=ISO42001.aims_customer_agreement, name="aimsCustomerRelationship__aims_customer_agreement", curie=ISO42001.curie('aims_customer_agreement'),
                   model_uri=ISO42001.aimsCustomerRelationship__aims_customer_agreement, domain=None, range=Optional[str])

slots.aimsCustomerRelationship__aims_customer_responsibility_split = Slot(uri=ISO42001.aims_customer_responsibility_split, name="aimsCustomerRelationship__aims_customer_responsibility_split", curie=ISO42001.curie('aims_customer_responsibility_split'),
                   model_uri=ISO42001.aimsCustomerRelationship__aims_customer_responsibility_split, domain=None, range=Optional[str])

slots.aimsCustomerRelationship__aims_customer_communicated_limits = Slot(uri=ISO42001.aims_customer_communicated_limits, name="aimsCustomerRelationship__aims_customer_communicated_limits", curie=ISO42001.curie('aims_customer_communicated_limits'),
                   model_uri=ISO42001.aimsCustomerRelationship__aims_customer_communicated_limits, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsSystemEvent__aims_event_type = Slot(uri=ISO42001.aims_event_type, name="aimsSystemEvent__aims_event_type", curie=ISO42001.curie('aims_event_type'),
                   model_uri=ISO42001.aimsSystemEvent__aims_event_type, domain=None, range=Optional[str])

slots.aimsSystemEvent__aims_event_occurred_at = Slot(uri=ISO42001.aims_event_occurred_at, name="aimsSystemEvent__aims_event_occurred_at", curie=ISO42001.curie('aims_event_occurred_at'),
                   model_uri=ISO42001.aimsSystemEvent__aims_event_occurred_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.aimsSystemEvent__aims_event_reporter = Slot(uri=ISO42001.aims_event_reporter, name="aimsSystemEvent__aims_event_reporter", curie=ISO42001.curie('aims_event_reporter'),
                   model_uri=ISO42001.aimsSystemEvent__aims_event_reporter, domain=None, range=Optional[str])

slots.aimsSystemEvent__aims_event_source = Slot(uri=ISO42001.aims_event_source, name="aimsSystemEvent__aims_event_source", curie=ISO42001.curie('aims_event_source'),
                   model_uri=ISO42001.aimsSystemEvent__aims_event_source, domain=None, range=Optional[str])

slots.aimsSystemEvent__aims_event_adverse_impact = Slot(uri=ISO42001.aims_event_adverse_impact, name="aimsSystemEvent__aims_event_adverse_impact", curie=ISO42001.curie('aims_event_adverse_impact'),
                   model_uri=ISO42001.aimsSystemEvent__aims_event_adverse_impact, domain=None, range=Optional[str])

slots.aimsSystemEvent__aims_event_assessment = Slot(uri=ISO42001.aims_event_assessment, name="aimsSystemEvent__aims_event_assessment", curie=ISO42001.curie('aims_event_assessment'),
                   model_uri=ISO42001.aimsSystemEvent__aims_event_assessment, domain=None, range=Optional[str])

slots.aimsIncident__aims_incident_category = Slot(uri=ISO42001.aims_incident_category, name="aimsIncident__aims_incident_category", curie=ISO42001.curie('aims_incident_category'),
                   model_uri=ISO42001.aimsIncident__aims_incident_category, domain=None, range=Optional[Union[str, "AimsIncidentCategory"]])

slots.aimsIncident__aims_incident_threats = Slot(uri=ISO42001.aims_incident_threats, name="aimsIncident__aims_incident_threats", curie=ISO42001.curie('aims_incident_threats'),
                   model_uri=ISO42001.aimsIncident__aims_incident_threats, domain=None, range=Optional[Union[Union[str, "AimsAiThreat"], list[Union[str, "AimsAiThreat"]]]])

slots.aimsIncident__aims_incident_severity = Slot(uri=ISO42001.aims_incident_severity, name="aimsIncident__aims_incident_severity", curie=ISO42001.curie('aims_incident_severity'),
                   model_uri=ISO42001.aimsIncident__aims_incident_severity, domain=None, range=Optional[Union[str, "AimsRiskLevel"]])

slots.aimsIncident__aims_incident_impact_areas = Slot(uri=ISO42001.aims_incident_impact_areas, name="aimsIncident__aims_incident_impact_areas", curie=ISO42001.curie('aims_incident_impact_areas'),
                   model_uri=ISO42001.aimsIncident__aims_incident_impact_areas, domain=None, range=Optional[Union[Union[str, "AimsImpactArea"], list[Union[str, "AimsImpactArea"]]]])

slots.aimsIncident__aims_incident_detection_method = Slot(uri=ISO42001.aims_incident_detection_method, name="aimsIncident__aims_incident_detection_method", curie=ISO42001.curie('aims_incident_detection_method'),
                   model_uri=ISO42001.aimsIncident__aims_incident_detection_method, domain=None, range=Optional[str])

slots.aimsIncident__aims_incident_response_actions = Slot(uri=ISO42001.aims_incident_response_actions, name="aimsIncident__aims_incident_response_actions", curie=ISO42001.curie('aims_incident_response_actions'),
                   model_uri=ISO42001.aimsIncident__aims_incident_response_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsIncident__aims_incident_recovery_actions = Slot(uri=ISO42001.aims_incident_recovery_actions, name="aimsIncident__aims_incident_recovery_actions", curie=ISO42001.curie('aims_incident_recovery_actions'),
                   model_uri=ISO42001.aimsIncident__aims_incident_recovery_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsIncident__aims_incident_root_cause = Slot(uri=ISO42001.aims_incident_root_cause, name="aimsIncident__aims_incident_root_cause", curie=ISO42001.curie('aims_incident_root_cause'),
                   model_uri=ISO42001.aimsIncident__aims_incident_root_cause, domain=None, range=Optional[str])

slots.aimsIncident__aims_incident_lessons_learned = Slot(uri=ISO42001.aims_incident_lessons_learned, name="aimsIncident__aims_incident_lessons_learned", curie=ISO42001.curie('aims_incident_lessons_learned'),
                   model_uri=ISO42001.aimsIncident__aims_incident_lessons_learned, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsIncident__aims_incident_notification_required = Slot(uri=ISO42001.aims_incident_notification_required, name="aimsIncident__aims_incident_notification_required", curie=ISO42001.curie('aims_incident_notification_required'),
                   model_uri=ISO42001.aimsIncident__aims_incident_notification_required, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsIncident__aims_incident_notifications = Slot(uri=ISO42001.aims_incident_notifications, name="aimsIncident__aims_incident_notifications", curie=ISO42001.curie('aims_incident_notifications'),
                   model_uri=ISO42001.aimsIncident__aims_incident_notifications, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsIncident__aims_incident_corrective_actions = Slot(uri=ISO42001.aims_incident_corrective_actions, name="aimsIncident__aims_incident_corrective_actions", curie=ISO42001.curie('aims_incident_corrective_actions'),
                   model_uri=ISO42001.aimsIncident__aims_incident_corrective_actions, domain=None, range=Optional[Union[Union[str, AimsCorrectiveActionAimsId], list[Union[str, AimsCorrectiveActionAimsId]]]])

slots.aimsIncident__aims_incident_closed_at = Slot(uri=ISO42001.aims_incident_closed_at, name="aimsIncident__aims_incident_closed_at", curie=ISO42001.curie('aims_incident_closed_at'),
                   model_uri=ISO42001.aimsIncident__aims_incident_closed_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.aimsConcernReportingProcess__aims_concern_process_confidentiality = Slot(uri=ISO42001.aims_concern_process_confidentiality, name="aimsConcernReportingProcess__aims_concern_process_confidentiality", curie=ISO42001.curie('aims_concern_process_confidentiality'),
                   model_uri=ISO42001.aimsConcernReportingProcess__aims_concern_process_confidentiality, domain=None, range=Optional[Union[str, list[str]]])

slots.aimsConcernReportingProcess__aims_concern_process_audience = Slot(uri=ISO42001.aims_concern_process_audience, name="aimsConcernReportingProcess__aims_concern_process_audience", curie=ISO42001.curie('aims_concern_process_audience'),
                   model_uri=ISO42001.aimsConcernReportingProcess__aims_concern_process_audience, domain=None, range=Optional[str])

slots.aimsConcernReportingProcess__aims_concern_process_investigators = Slot(uri=ISO42001.aims_concern_process_investigators, name="aimsConcernReportingProcess__aims_concern_process_investigators", curie=ISO42001.curie('aims_concern_process_investigators'),
                   model_uri=ISO42001.aimsConcernReportingProcess__aims_concern_process_investigators, domain=None, range=Optional[str])

slots.aimsConcernReportingProcess__aims_concern_process_escalation = Slot(uri=ISO42001.aims_concern_process_escalation, name="aimsConcernReportingProcess__aims_concern_process_escalation", curie=ISO42001.curie('aims_concern_process_escalation'),
                   model_uri=ISO42001.aimsConcernReportingProcess__aims_concern_process_escalation, domain=None, range=Optional[str])

slots.aimsConcernReportingProcess__aims_concern_process_reprisal_protection = Slot(uri=ISO42001.aims_concern_process_reprisal_protection, name="aimsConcernReportingProcess__aims_concern_process_reprisal_protection", curie=ISO42001.curie('aims_concern_process_reprisal_protection'),
                   model_uri=ISO42001.aimsConcernReportingProcess__aims_concern_process_reprisal_protection, domain=None, range=Optional[str])

slots.aimsConcernReportingProcess__aims_concern_process_response_time = Slot(uri=ISO42001.aims_concern_process_response_time, name="aimsConcernReportingProcess__aims_concern_process_response_time", curie=ISO42001.curie('aims_concern_process_response_time'),
                   model_uri=ISO42001.aimsConcernReportingProcess__aims_concern_process_response_time, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_reported_on = Slot(uri=ISO42001.aims_concern_reported_on, name="aimsConcernReport__aims_concern_reported_on", curie=ISO42001.curie('aims_concern_reported_on'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_reported_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsConcernReport__aims_concern_reporter = Slot(uri=ISO42001.aims_concern_reporter, name="aimsConcernReport__aims_concern_reporter", curie=ISO42001.curie('aims_concern_reporter'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_reporter, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_anonymous = Slot(uri=ISO42001.aims_concern_anonymous, name="aimsConcernReport__aims_concern_anonymous", curie=ISO42001.curie('aims_concern_anonymous'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_anonymous, domain=None, range=Optional[Union[bool, Bool]])

slots.aimsConcernReport__aims_concern_channel = Slot(uri=ISO42001.aims_concern_channel, name="aimsConcernReport__aims_concern_channel", curie=ISO42001.curie('aims_concern_channel'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_channel, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_life_cycle_stage = Slot(uri=ISO42001.aims_concern_life_cycle_stage, name="aimsConcernReport__aims_concern_life_cycle_stage", curie=ISO42001.curie('aims_concern_life_cycle_stage'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_life_cycle_stage, domain=None, range=Optional[Union[str, "AimsLifecycleStage"]])

slots.aimsConcernReport__aims_concern_severity = Slot(uri=ISO42001.aims_concern_severity, name="aimsConcernReport__aims_concern_severity", curie=ISO42001.curie('aims_concern_severity'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_severity, domain=None, range=Optional[Union[str, "AimsRiskLevel"]])

slots.aimsConcernReport__aims_concern_investigator = Slot(uri=ISO42001.aims_concern_investigator, name="aimsConcernReport__aims_concern_investigator", curie=ISO42001.curie('aims_concern_investigator'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_investigator, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_investigation_status = Slot(uri=ISO42001.aims_concern_investigation_status, name="aimsConcernReport__aims_concern_investigation_status", curie=ISO42001.curie('aims_concern_investigation_status'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_investigation_status, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_findings = Slot(uri=ISO42001.aims_concern_findings, name="aimsConcernReport__aims_concern_findings", curie=ISO42001.curie('aims_concern_findings'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_findings, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_escalation = Slot(uri=ISO42001.aims_concern_escalation, name="aimsConcernReport__aims_concern_escalation", curie=ISO42001.curie('aims_concern_escalation'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_escalation, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_response_due = Slot(uri=ISO42001.aims_concern_response_due, name="aimsConcernReport__aims_concern_response_due", curie=ISO42001.curie('aims_concern_response_due'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_response_due, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsConcernReport__aims_concern_responded_on = Slot(uri=ISO42001.aims_concern_responded_on, name="aimsConcernReport__aims_concern_responded_on", curie=ISO42001.curie('aims_concern_responded_on'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_responded_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.aimsConcernReport__aims_concern_resolution = Slot(uri=ISO42001.aims_concern_resolution, name="aimsConcernReport__aims_concern_resolution", curie=ISO42001.curie('aims_concern_resolution'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_resolution, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_reprisal_protection = Slot(uri=ISO42001.aims_concern_reprisal_protection, name="aimsConcernReport__aims_concern_reprisal_protection", curie=ISO42001.curie('aims_concern_reprisal_protection'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_reprisal_protection, domain=None, range=Optional[str])

slots.aimsConcernReport__aims_concern_incidents = Slot(uri=ISO42001.aims_concern_incidents, name="aimsConcernReport__aims_concern_incidents", curie=ISO42001.curie('aims_concern_incidents'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_incidents, domain=None, range=Optional[Union[Union[str, AimsIncidentAimsId], list[Union[str, AimsIncidentAimsId]]]])

slots.aimsConcernReport__aims_concern_nonconformities = Slot(uri=ISO42001.aims_concern_nonconformities, name="aimsConcernReport__aims_concern_nonconformities", curie=ISO42001.curie('aims_concern_nonconformities'),
                   model_uri=ISO42001.aimsConcernReport__aims_concern_nonconformities, domain=None, range=Optional[Union[Union[str, AimsNonconformityAimsId], list[Union[str, AimsNonconformityAimsId]]]])

slots.AimsRecordMixin_title = Slot(uri=SCHEMA.name, name="AimsRecordMixin_title", curie=SCHEMA.curie('name'),
                   model_uri=ISO42001.AimsRecordMixin_title, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AimsIncludedControl_aims_implementation_state = Slot(uri=ISO42001.aims_implementation_state, name="AimsIncludedControl_aims_implementation_state", curie=ISO42001.curie('aims_implementation_state'),
                   model_uri=ISO42001.AimsIncludedControl_aims_implementation_state, domain=AimsIncludedControl, range=Union[str, "AimsImplementationStatus"])

slots.AimsExcludedControl_aims_entry_annex_a_control = Slot(uri=ISO42001.aims_entry_annex_a_control, name="AimsExcludedControl_aims_entry_annex_a_control", curie=ISO42001.curie('aims_entry_annex_a_control'),
                   model_uri=ISO42001.AimsExcludedControl_aims_entry_annex_a_control, domain=AimsExcludedControl, range=Union[str, "AimsAnnexAControl"])

slots.AimsSystemResource_aims_resource_type = Slot(uri=ISO42001.aims_resource_type, name="AimsSystemResource_aims_resource_type", curie=ISO42001.curie('aims_resource_type'),
                   model_uri=ISO42001.AimsSystemResource_aims_resource_type, domain=AimsSystemResource, range=str)
