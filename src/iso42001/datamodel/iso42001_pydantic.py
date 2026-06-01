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


metamodel_version = "1.11.0"
version = "1.0.0"


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


linkml_meta = LinkMLMeta({'annotations': {'amendment_reference': {'tag': 'amendment_reference',
                                             'value': 'Forward-compatibility '
                                                      'placeholder for tracking '
                                                      'amendments (AMD) and '
                                                      'technical corrigenda (Cor) '
                                                      'to ISO/IEC 42001:2023. '
                                                      'Update when ISO/IEC '
                                                      'publishes amendments to the '
                                                      'base edition.'},
                     'developing_committee': {'tag': 'developing_committee',
                                              'value': 'ISO/IEC JTC 1/SC 42 '
                                                       '(Artificial Intelligence)'},
                     'harmonized_structure': {'tag': 'harmonized_structure',
                                              'value': True},
                     'normative_reference': {'tag': 'normative_reference',
                                             'value': 'ISO/IEC 22989:2022 (AI '
                                                      'concepts and terminology)'},
                     'related_standards': {'tag': 'related_standards',
                                           'value': 'ISO/IEC 23894 (AI risk '
                                                    'management guidance); ISO/IEC '
                                                    '38507 (Governance of IT - AI '
                                                    'governance implications); '
                                                    'ISO/IEC 5259 (Data quality '
                                                    'for analytics and ML); '
                                                    'ISO/IEC 5338 (AI system life '
                                                    'cycle process); ISO/IEC 27001 '
                                                    '(Information security '
                                                    'management); ISO/IEC 27701 '
                                                    '(Privacy information '
                                                    'management); ISO 9001 '
                                                    '(Quality management); ISO '
                                                    '31000 (Risk management)'},
                     'rights_notice': {'tag': 'rights_notice',
                                       'value': 'This project is licensed under '
                                                'Apache-2.0 for original schema '
                                                'structure and descriptions. '
                                                'ISO/IEC standards text is owned '
                                                'by ISO/IEC and is not reproduced '
                                                'verbatim by this project.'},
                     'schema_maintainer': {'tag': 'schema_maintainer',
                                           'value': 'noel.mcloughlin@gmail.com'},
                     'schema_status': {'tag': 'schema_status', 'value': 'stable'},
                     'standard_date': {'tag': 'standard_date', 'value': '2023-12'},
                     'standard_edition': {'tag': 'standard_edition',
                                          'value': 'First edition'},
                     'standard_reference': {'tag': 'standard_reference',
                                            'value': 'ISO/IEC 42001:2023(E)'},
                     'standard_title': {'tag': 'standard_title',
                                        'value': 'Information technology - '
                                                 'Artificial intelligence - '
                                                 'Management system'}},
     'default_prefix': 'iso42001',
     'default_range': 'string',
     'description': 'A comprehensive LinkML schema modeling AI Management System '
                    '(AIMS) entities, workflows, and traceability links aligned to '
                    'ISO/IEC 42001:2023 clause and Annex references. Designed for '
                    'open data publication, automated validation, and integration '
                    'with AI governance, risk, and compliance platforms.\n'
                    'This schema captures: - AIMS lifecycle (establish, implement, '
                    'maintain, improve) - AI risk assessment, treatment, and AI '
                    'system impact assessment (Clause 6.1) - Annex A reference '
                    'control catalog (A.2-A.10) for responsible AI - Audit, '
                    'measurement, and continual improvement artifacts - Data '
                    'resources, tooling, computing, and human resources for AI '
                    'systems - Third-party, supplier, and customer relationships '
                    'across the AI life cycle',
     'id': 'https://w3id.org/lmodel/iso42001',
     'imports': ['linkml:types'],
     'license': 'https://www.apache.org/licenses/LICENSE-2.0',
     'name': 'iso42001',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'iso22989': {'prefix_prefix': 'iso22989',
                               'prefix_reference': 'https://w3id.org/lmodel/iso22989/'},
                  'iso23894': {'prefix_prefix': 'iso23894',
                               'prefix_reference': 'https://w3id.org/lmodel/iso23894/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'iso42001': {'prefix_prefix': 'iso42001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso42001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_100_1': {'prefix_prefix': 'nist_ai_100_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'nist_ai_600_1': {'prefix_prefix': 'nist_ai_600_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-600-1/'},
                  'nist_ai_rmf': {'prefix_prefix': 'nist_ai_rmf',
                                  'prefix_reference': 'https://www.nist.gov/itl/ai-risk-management-framework/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'}},
     'see_also': ['https://lmodel.github.io/iso42001',
                  'https://www.iso.org/standard/81230.html'],
     'source_file': 'src/iso42001/schema/iso42001.yaml',
     'subsets': {'ai_data_management': {'description': 'Elements covering data '
                                                       'resources, data '
                                                       'acquisition, data quality, '
                                                       'data provenance, and data '
                                                       'preparation for AI systems '
                                                       'per A.7.',
                                        'from_schema': 'https://w3id.org/lmodel/iso42001',
                                        'name': 'ai_data_management'},
                 'ai_risk_management': {'description': 'Elements supporting AI '
                                                       'risk assessment (6.1.2), '
                                                       'AI risk treatment (6.1.3), '
                                                       'and AI system impact '
                                                       'assessment (6.1.4). '
                                                       'Aligned with ISO '
                                                       '31000:2018 and ISO/IEC '
                                                       '23894 guidance.',
                                        'from_schema': 'https://w3id.org/lmodel/iso42001',
                                        'name': 'ai_risk_management'},
                 'ai_system_lifecycle': {'description': 'Classes representing the '
                                                        'AI system life cycle '
                                                        'stages (design, '
                                                        'development, '
                                                        'verification, deployment, '
                                                        'operation, monitoring, '
                                                        'decommissioning) '
                                                        'referenced in Annex A.6.',
                                         'from_schema': 'https://w3id.org/lmodel/iso42001',
                                         'name': 'ai_system_lifecycle'},
                 'aims_core': {'comments': ['Mandatory for any ISO/IEC 42001 '
                                            'conformance dataset',
                                            'Maps to requirement statements in the '
                                            'standard'],
                               'description': 'Core AIMS structural elements '
                                              'required for conformity with '
                                              'Clauses 4-10 of ISO/IEC 42001:2023. '
                                              'These classes represent the minimum '
                                              'viable data model for AIMS '
                                              'documentation.',
                               'from_schema': 'https://w3id.org/lmodel/iso42001',
                               'name': 'aims_core'},
                 'annex_a_controls': {'description': 'Classes and enumerations '
                                                     'representing the reference '
                                                     'controls in Annex A of '
                                                     'ISO/IEC 42001:2023, grouped '
                                                     'into nine control families '
                                                     '(A.2 through A.10). '
                                                     'Implementation guidance is '
                                                     'provided in Annex B.',
                                      'from_schema': 'https://w3id.org/lmodel/iso42001',
                                      'name': 'annex_a_controls'},
                 'continual_improvement': {'description': 'Elements for '
                                                          'nonconformity '
                                                          'management, corrective '
                                                          'actions, and '
                                                          'improvement tracking '
                                                          'per Clause 10.',
                                           'from_schema': 'https://w3id.org/lmodel/iso42001',
                                           'name': 'continual_improvement'},
                 'documented_information': {'description': 'Classes representing '
                                                           'required documented '
                                                           'information per Clause '
                                                           '7.5. Supports document '
                                                           'control and retention '
                                                           'requirements.',
                                            'from_schema': 'https://w3id.org/lmodel/iso42001',
                                            'name': 'documented_information'},
                 'performance_evaluation': {'description': 'Classes for '
                                                           'monitoring, '
                                                           'measurement, internal '
                                                           'audit, and management '
                                                           'review per Clauses '
                                                           '9.1-9.3.',
                                            'from_schema': 'https://w3id.org/lmodel/iso42001',
                                            'name': 'performance_evaluation'},
                 'third_party_management': {'description': 'Classes covering '
                                                           'allocation of '
                                                           'responsibilities to '
                                                           'partners, suppliers, '
                                                           'and customers across '
                                                           'the AI system life '
                                                           'cycle per A.10.',
                                            'from_schema': 'https://w3id.org/lmodel/iso42001',
                                            'name': 'third_party_management'}},
     'title': 'ISO 42001 / AIMS: LinkML Schema',
     'types': {'duration type': {'base': 'str',
                                 'description': 'ISO 8601 duration value such as '
                                                'P1Y, P30D, or PT4H',
                                 'from_schema': 'https://w3id.org/lmodel/iso42001',
                                 'name': 'duration type',
                                 'uri': 'xsd:duration'},
               'positive integer type': {'base': 'int',
                                         'description': 'integer greater than '
                                                        'zero; natural number '
                                                        'explicitly excluding zero',
                                         'exact_mappings': ['wikidata:Q28920044'],
                                         'from_schema': 'https://w3id.org/lmodel/iso42001',
                                         'name': 'positive integer type',
                                         'uri': 'xsd:positiveInteger'},
               'unsigned short type': {'base': 'int',
                                       'description': 'data type for non-negative '
                                                      'integers that can be '
                                                      'represented with 16 bits',
                                       'exact_mappings': ['wikidata:Q110650833'],
                                       'from_schema': 'https://w3id.org/lmodel/iso42001',
                                       'name': 'unsigned short type',
                                       'uri': 'xsd:unsignedShort'}}} )

class AIControlFamily(str, Enum):
    """
    The reference control families in Annex A of ISO/IEC 42001:2023.
    """
    ai_policies = "ai_policies"
    """
    Policies related to AI (Annex A.2) - management direction and support for AI systems according to business requirements.
    """
    internal_organization = "internal_organization"
    """
    Internal organization (Annex A.3) - accountability for responsible implementation, operation, and management of AI systems.
    """
    ai_resources = "ai_resources"
    """
    Resources for AI systems (Annex A.4) - documentation of data, tooling, system/computing, and human resources for AI systems.
    """
    impact_assessment = "impact_assessment"
    """
    Assessing impacts of AI systems (Annex A.5) - evaluation of consequences for individuals, groups, and societies across the AI system life cycle.
    """
    ai_system_lifecycle = "ai_system_lifecycle"
    """
    AI system life cycle (Annex A.6) - responsible design, development, verification, deployment, operation, and technical documentation.
    """
    data_for_ai = "data_for_ai"
    """
    Data for AI systems (Annex A.7) - data management, acquisition, quality, provenance, and preparation for AI.
    """
    information_for_parties = "information_for_parties"
    """
    Information for interested parties (Annex A.8) - system documentation for users, external reporting, and incident communications.
    """
    use_of_ai = "use_of_ai"
    """
    Use of AI systems (Annex A.9) - responsible-use processes, objectives, and intended-use enforcement.
    """
    third_party_relationships = "third_party_relationships"
    """
    Third-party and customer relationships (Annex A.10) - allocating responsibilities, supplier management, and customer expectations.
    """


class ImplementationStatus(str, Enum):
    """
    Lifecycle status of a reference control, used in the AIMS Statement of Applicability and control tracking.
    """
    not_started = "not_started"
    """
    Control identified but no implementation activities begun.
    """
    planned = "planned"
    """
    Control scheduled for implementation with defined timeline.
    """
    in_progress = "in_progress"
    """
    Implementation actively underway but not yet complete.
    """
    implemented = "implemented"
    """
    Control fully implemented and operational.
    """
    not_applicable = "not_applicable"
    """
    Control excluded from scope with documented justification per Clause 6.1.3 f).
    """


class RiskTreatmentOption(str, Enum):
    """
    Standard risk treatment options drawn from ISO 31000 and adapted for AI risk treatment per Clause 6.1.3.
    """
    modify = "modify"
    """
    Apply controls to change the AI risk level (reduce likelihood or consequence).
    """
    accept = "accept"
    """
    Accept the residual AI risk without further treatment, within risk appetite, with designated management approval.
    """
    avoid = "avoid"
    """
    Eliminate the AI risk by not undertaking the activity that creates it (for example, not deploying a high-risk AI use case).
    """
    share = "share"
    """
    Transfer or share the AI risk with external parties (e.g., insurance, contractual transfer to a supplier or partner).
    """


class RiskLevel(str, Enum):
    """
    Qualitative AI risk rating derived from likelihood and consequence analysis.
    """
    very_low = "very_low"
    """
    Negligible AI risk requiring no immediate action.
    """
    low = "low"
    """
    Minor AI risk manageable through routine procedures.
    """
    medium = "medium"
    """
    Moderate AI risk requiring management attention and planned controls.
    """
    high = "high"
    """
    Significant AI risk requiring priority treatment and escalation.
    """
    critical = "critical"
    """
    Severe AI risk threatening organizational objectives, individuals, or societies; requires immediate executive action.
    """


class LikelihoodRating(str, Enum):
    """
    Qualitative likelihood scale for AI risk assessment.
    """
    rare = "rare"
    """
    Highly unlikely to occur (< 5% probability).
    """
    unlikely = "unlikely"
    """
    Not expected but possible (5-20% probability).
    """
    possible = "possible"
    """
    May occur at some point (20-50% probability).
    """
    likely = "likely"
    """
    Probably will occur (50-80% probability).
    """
    almost_certain = "almost_certain"
    """
    Expected to occur in most circumstances (> 80% probability).
    """


class ImpactRating(str, Enum):
    """
    Qualitative consequence scale for AI risk assessment, covering impact on the organization, individuals, groups, and societies.
    """
    negligible = "negligible"
    """
    No significant impact on operations, individuals, or society.
    """
    minor = "minor"
    """
    Limited impact, easily absorbed by normal operations.
    """
    moderate = "moderate"
    """
    Noticeable impact requiring management intervention.
    """
    major = "major"
    """
    Serious impact on objectives, reputation, compliance, or identifiable groups of individuals.
    """
    severe = "severe"
    """
    Catastrophic impact threatening organizational viability, broad societal harm, or fundamental rights of affected individuals.
    """


class AISystemLifecycleStage(str, Enum):
    """
    Stages of the AI system life cycle referenced throughout Annex A.6 and defined in ISO/IEC 5338 / ISO/IEC 22989.
    """
    inception = "inception"
    """
    Initial conception, feasibility, and use-case definition.
    """
    design = "design"
    """
    AI system design including requirements and architecture.
    """
    data_collection_and_preparation = "data_collection_and_preparation"
    """
    Acquiring, labelling, and preparing data resources.
    """
    development = "development"
    """
    Model and AI system development and training.
    """
    verification_and_validation = "verification_and_validation"
    """
    Verification and validation of the AI system.
    """
    deployment = "deployment"
    """
    Release and integration into the production environment.
    """
    operation_and_monitoring = "operation_and_monitoring"
    """
    Ongoing operation, monitoring, and support.
    """
    continuous_validation = "continuous_validation"
    """
    Continuous validation, including drift detection and re-training triggers.
    """
    re_evaluation = "re_evaluation"
    """
    Re-evaluation following significant changes or new evidence.
    """
    decommissioning = "decommissioning"
    """
    Retirement, disposal, and post-decommissioning obligations.
    """


class AIOrganizationalRole(str, Enum):
    """
    Roles an organization may take with respect to an AI system, paraphrased from the role taxonomy referenced in ISO/IEC 22989 and the NIST AI RMF.
    """
    ai_provider = "ai_provider"
    """
    Organization providing AI platforms, products, or services to others.
    """
    ai_producer = "ai_producer"
    """
    Organization or actor that develops, designs, operates, tests, evaluates, deploys, or governs AI systems.
    """
    ai_customer = "ai_customer"
    """
    Organization or individual that uses an AI product or service.
    """
    ai_partner = "ai_partner"
    """
    System integrators and data providers for AI systems.
    """
    ai_subject = "ai_subject"
    """
    Individuals or groups whose data or interests are affected by an AI system (e.g., data subjects).
    """
    relevant_authority = "relevant_authority"
    """
    Policymakers, regulators, and other oversight bodies.
    """


class DataResourceCategory(str, Enum):
    """
    Categories of data resources documented for AI systems per A.7 (Data for AI systems).
    """
    training = "training"
    """
    Data used to train machine learning models.
    """
    validation = "validation"
    """
    Data used for model selection and hyperparameter tuning.
    """
    test = "test"
    """
    Data used to evaluate model performance prior to deployment.
    """
    production = "production"
    """
    Live operational data processed by the deployed AI system.
    """
    reference = "reference"
    """
    Reference datasets used for benchmarking or comparison.
    """


class AIObjectiveCategory(str, Enum):
    """
    Categories of organizational objectives associated with responsible development and use of AI systems, paraphrased from Annex C of ISO/IEC 42001:2023.
    """
    accountability = "accountability"
    """
    Clear allocation of responsibility for AI-supported decisions.
    """
    ai_expertise = "ai_expertise"
    """
    Availability of interdisciplinary expertise for AI activities.
    """
    data_quality = "data_quality"
    """
    Adequate quality of training, validation, and test data.
    """
    environmental_impact = "environmental_impact"
    """
    Management of positive and negative environmental effects.
    """
    fairness = "fairness"
    """
    Avoiding inappropriate or unfair outcomes for individuals or groups.
    """
    maintainability = "maintainability"
    """
    Ability to correct defects and accommodate new requirements.
    """
    privacy = "privacy"
    """
    Protection of personal and sensitive data processed by AI systems.
    """
    robustness = "robustness"
    """
    Comparable performance on new and operational data.
    """
    safety = "safety"
    """
    Avoidance of harm to life, health, property, or the environment.
    """
    security = "security"
    """
    Protection from AI-specific and conventional security threats.
    """
    transparency = "transparency"
    """
    Visibility into organizational AI practices and AI system behaviour.
    """
    explainability = "explainability"
    """
    Comprehensible explanations of important factors driving AI outputs.
    """
    reliability = "reliability"
    """
    Consistent performance under defined conditions.
    """
    accessibility = "accessibility"
    """
    Usability of AI systems by people with diverse abilities.
    """
    availability_of_training_data = "availability_of_training_data"
    """
    Sufficient availability and quality of training, validation, and test data needed to train and verify AI systems (Annex C.2.3).
    """


class AIRiskSourceCategory(str, Enum):
    """
    Categories of AI risk sources, paraphrased from Annex C of ISO/IEC 42001:2023.
    """
    complexity_of_environment = "complexity_of_environment"
    """
    Performance uncertainty in complex or open operational environments (e.g., autonomous systems).
    """
    lack_of_transparency_or_explainability = "lack_of_transparency_or_explainability"
    """
    Inability to provide adequate information to interested parties, affecting trustworthiness and accountability.
    """
    level_of_automation = "level_of_automation"
    """
    Effects of automation on safety, fairness, security, or human oversight.
    """
    machine_learning_specific = "machine_learning_specific"
    """
    Risks tied to data collection, data quality, and ML-specific phenomena such as data poisoning.
    """
    hardware = "hardware"
    """
    Hardware errors or behavioural differences when transferring trained models between systems.
    """
    lifecycle = "lifecycle"
    """
    Risks introduced at any AI system life cycle stage, including design flaws, deployment issues, or decommissioning gaps.
    """
    technology_readiness = "technology_readiness"
    """
    Risks from immature technology with unknown limitations as well as mature technology subject to technology complacency.
    """


class DocumentType(str, Enum):
    """
    Categories of documented information referenced in or required by ISO/IEC 42001:2023.
    """
    policy = "policy"
    """
    High-level statement of intent and direction (e.g., AI policy per 5.2).
    """
    procedure = "procedure"
    """
    Documented steps for performing AIMS activities consistently.
    """
    standard = "standard"
    """
    Mandatory requirements for specific AI technologies or processes.
    """
    guideline = "guideline"
    """
    Recommended practices that support AI-related policies.
    """
    record = "record"
    """
    Evidence of AIMS activities performed or results achieved.
    """
    plan = "plan"
    """
    Documented approach for achieving objectives (e.g., AI risk treatment plan, deployment plan).
    """
    report = "report"
    """
    Formal output of assessment, audit, impact assessment, or review activities.
    """
    technical_documentation = "technical_documentation"
    """
    AI system technical documentation provided to users, partners, supervisory authorities, and other interested parties per A.6.2.7 and A.8.2.
    """


class AuditFindingType(str, Enum):
    """
    Classification of internal audit findings for the AIMS.
    """
    major_nonconformity = "major_nonconformity"
    """
    Significant failure to fulfill a requirement that affects the AIMS ability to achieve its intended outcomes.
    """
    minor_nonconformity = "minor_nonconformity"
    """
    Isolated lapse that does not significantly affect AIMS effectiveness.
    """
    observation = "observation"
    """
    Noted condition that could lead to a nonconformity if not addressed.
    """
    positive_finding = "positive_finding"
    """
    Evidence of effective implementation exceeding requirements.
    """


class ImpactAssessmentDimension(str, Enum):
    """
    Dimensions evaluated during an AI system impact assessment per Clause 6.1.4. Combines individual/group impacts (Annex A.5.4 / Annex B.5.4) with societal-scope impacts (Annex A.5.5 / Annex B.5.5).
    """
    individual = "individual"
    """
    Consequences for individual persons interacting with or affected by the AI system.
    """
    group = "group"
    """
    Consequences for identifiable groups of individuals.
    """
    societal = "societal"
    """
    Broader societal consequences.
    """
    fairness = "fairness"
    """
    Fair and non-discriminatory treatment of affected individuals and groups (B.5.4).
    """
    transparency = "transparency"
    """
    Transparency of organizational AI practices and AI system behaviour (B.5.4).
    """
    explainability = "explainability"
    """
    Comprehensibility of important factors driving AI outputs (B.5.4).
    """
    accountability = "accountability"
    """
    Clear allocation of accountability for AI-supported decisions (B.5.4).
    """
    accessibility = "accessibility"
    """
    Accessibility of the AI system for people with diverse abilities (B.5.4).
    """
    human_rights = "human_rights"
    """
    Effects on fundamental human rights (B.5.4).
    """
    financial = "financial"
    """
    Financial consequences for affected individuals or organizations (B.5.4).
    """
    health = "health"
    """
    Effects on physical or mental health (B.5.4).
    """
    environmental = "environmental"
    """
    Environmental consequences attributable to the AI system (B.5.5).
    """
    economic = "economic"
    """
    Wider economic consequences (B.5.5).
    """
    government = "government"
    """
    Consequences for democratic processes, governance, or rule of law (B.5.5).
    """
    cultural_norms = "cultural_norms"
    """
    Consequences for cultural norms, traditions, or values (B.5.5).
    """
    safety = "safety"
    """
    Safety-related consequences in the deployment context.
    """
    privacy = "privacy"
    """
    Privacy-related consequences for data subjects.
    """
    security = "security"
    """
    Information security consequences attributable to the AI system.
    """


class AnnexAControlId(str, Enum):
    """
    Normative reference control identifiers from Annex A of ISO/IEC 42001:2023 (38 controls across nine families A.2-A.10). Permissible value names use underscores in place of dots; the `meaning` slot preserves the Annex A dotted form. Control titles are paraphrased.
    """
    a_2_2 = "a_2_2"
    """
    AI policy - document a policy governing AI system development or use.
    """
    a_2_3 = "a_2_3"
    """
    Alignment with other organizational policies - reconcile AI objectives with related policies.
    """
    a_2_4 = "a_2_4"
    """
    Review of the AI policy - planned and event-driven policy review for suitability and effectiveness.
    """
    a_3_2 = "a_3_2"
    """
    AI roles and responsibilities - define and allocate AI-related roles per organizational needs.
    """
    a_3_3 = "a_3_3"
    """
    Reporting of concerns - process for raising concerns about the organization's role with respect to AI.
    """
    a_4_2 = "a_4_2"
    """
    Resource documentation - identify and document resources used at each AI lifecycle stage.
    """
    a_4_3 = "a_4_3"
    """
    Data resources - document data resources used by the AI system.
    """
    a_4_4 = "a_4_4"
    """
    Tooling resources - document tooling resources used by the AI system.
    """
    a_4_5 = "a_4_5"
    """
    System and computing resources - document system and computing resources used by the AI system.
    """
    a_4_6 = "a_4_6"
    """
    Human resources - document human resources and competences across the AI lifecycle.
    """
    a_5_2 = "a_5_2"
    """
    AI system impact assessment process - establish a process to assess consequences across the lifecycle.
    """
    a_5_3 = "a_5_3"
    """
    Documentation of AI system impact assessments - record and retain assessment results.
    """
    a_5_4 = "a_5_4"
    """
    Assessing AI system impact on individuals or groups - evaluate and document impacts to individuals.
    """
    a_5_5 = "a_5_5"
    """
    Assessing societal impacts of AI systems - evaluate and document broader societal impacts.
    """
    a_6_1_2 = "a_6_1_2"
    """
    Objectives for responsible development - identify objectives that guide responsible AI development.
    """
    a_6_1_3 = "a_6_1_3"
    """
    Processes for responsible AI system design and development - document the design and development processes.
    """
    a_6_2_2 = "a_6_2_2"
    """
    AI system requirements and specification - specify requirements for new or enhanced AI systems.
    """
    a_6_2_3 = "a_6_2_3"
    """
    Documentation of AI system design and development - document design and development against requirements.
    """
    a_6_2_4 = "a_6_2_4"
    """
    AI system verification and validation - define and document V&V measures and criteria.
    """
    a_6_2_5 = "a_6_2_5"
    """
    AI system deployment - document a deployment plan and verify pre-deployment requirements.
    """
    a_6_2_6 = "a_6_2_6"
    """
    AI system operation and monitoring - document operational and performance monitoring, repairs, updates, and support.
    """
    a_6_2_7 = "a_6_2_7"
    """
    AI system technical documentation - provide technical documentation tailored to each interested party.
    """
    a_6_2_8 = "a_6_2_8"
    """
    AI system recording of event logs - enable event log recording across relevant lifecycle phases.
    """
    a_7_2 = "a_7_2"
    """
    Data for development and enhancement - define and implement data management processes for AI development.
    """
    a_7_3 = "a_7_3"
    """
    Acquisition of data - document acquisition and selection details for data used in AI systems.
    """
    a_7_4 = "a_7_4"
    """
    Quality of data for AI systems - define and meet data quality requirements.
    """
    a_7_5 = "a_7_5"
    """
    Data provenance - record data provenance across the data and AI system life cycles.
    """
    a_7_6 = "a_7_6"
    """
    Data preparation - document criteria and methods used for data preparation.
    """
    a_8_2 = "a_8_2"
    """
    System documentation and information for users - provide information needed by AI system users.
    """
    a_8_3 = "a_8_3"
    """
    External reporting - enable interested parties to report adverse impacts.
    """
    a_8_4 = "a_8_4"
    """
    Communication of incidents - document a plan for communicating incidents to users.
    """
    a_8_5 = "a_8_5"
    """
    Information for interested parties - document obligations to report AI system information to interested parties.
    """
    a_9_2 = "a_9_2"
    """
    Processes for responsible use of AI systems - define and document responsible use processes.
    """
    a_9_3 = "a_9_3"
    """
    Objectives for responsible use of AI system - identify and document responsible-use objectives.
    """
    a_9_4 = "a_9_4"
    """
    Intended use of the AI system - ensure use aligns with the documented intended use.
    """
    a_10_2 = "a_10_2"
    """
    Allocating responsibilities - allocate AI lifecycle responsibilities across organization, partners, suppliers, customers, third parties.
    """
    a_10_3 = "a_10_3"
    """
    Suppliers - ensure supplier-provided services, products, and materials align with the organization's responsible AI approach.
    """
    a_10_4 = "a_10_4"
    """
    Customers - account for customer expectations and needs in the organization's responsible AI approach.
    """


class SectorDomain(str, Enum):
    """
    Application sectors referenced in Annex D of ISO/IEC 42001:2023 in which the AIMS can be deployed jointly with sector-specific management system standards (e.g., ISO 13485, ISO 22000, IEC 62304).
    """
    health = "health"
    """
    Health, medical devices, and healthcare delivery contexts.
    """
    defence = "defence"
    """
    Defence, security, and dual-use technology contexts.
    """
    transport = "transport"
    """
    Transport, mobility, and autonomous vehicle contexts.
    """
    finance = "finance"
    """
    Financial services, banking, insurance, and capital markets.
    """
    employment = "employment"
    """
    Hiring, workforce management, and employee evaluation.
    """
    energy = "energy"
    """
    Energy production, distribution, and grid management.
    """
    public_sector = "public_sector"
    """
    Government, public administration, and public-service delivery.
    """
    education = "education"
    """
    Education, training, and academic assessment contexts.
    """
    manufacturing = "manufacturing"
    """
    Industrial and manufacturing automation.
    """
    agriculture = "agriculture"
    """
    Agricultural production and food-supply contexts.
    """
    telecommunications = "telecommunications"
    """
    Telecommunications and network operations.
    """
    retail = "retail"
    """
    Retail, e-commerce, and consumer products.
    """
    other = "other"
    """
    Other sector not enumerated above.
    """


class LearningParadigm(str, Enum):
    """
    Learning paradigm of an AI system, informing risk considerations related to data provenance, drift, and behavioural change over time (see ISO/IEC 42001:2023 Introduction and Annex C.3.4).
    """
    static = "static"
    """
    Trained once and deployed without further learning during operation.
    """
    periodic_retraining = "periodic_retraining"
    """
    Retrained on a defined cadence with controlled release cycles.
    """
    continuous_learning = "continuous_learning"
    """
    Updates its behaviour during operation based on new data or feedback.
    """
    online_learning = "online_learning"
    """
    Continuously updates parameters from a stream of data.
    """
    transfer_learning = "transfer_learning"
    """
    Adapted from a pre-trained model to a new task or domain.
    """
    reinforcement_learning = "reinforcement_learning"
    """
    Learns a policy through interaction with an environment and reward signals.
    """
    hybrid = "hybrid"
    """
    Combines multiple learning paradigms (e.g., supervised plus reinforcement).
    """
    not_applicable = "not_applicable"
    """
    AI system that is not based on machine learning (e.g., rule-based).
    """


class AIIncidentCategory(str, Enum):
    """
    AI-specific incident categories supplementing classical information security incident classes. Supports incident triage and communication per Annex A.8.3 (External reporting) and A.8.4 (Communication of incidents).
    """
    data_poisoning = "data_poisoning"
    """
    Training or production data manipulated to compromise model behaviour.
    """
    model_stealing = "model_stealing"
    """
    Unauthorized extraction or reconstruction of a deployed model.
    """
    model_inversion = "model_inversion"
    """
    Reconstruction of sensitive training data via model queries.
    """
    membership_inference = "membership_inference"
    """
    Inference of whether a record was part of the training set.
    """
    prompt_injection = "prompt_injection"
    """
    Adversarial inputs causing the model to deviate from intended behaviour.
    """
    hallucination = "hallucination"
    """
    Confidently incorrect or fabricated outputs causing material harm.
    """
    model_drift = "model_drift"
    """
    Performance or behaviour degradation due to distribution shift.
    """
    bias_incident = "bias_incident"
    """
    Unfair or discriminatory outcomes affecting individuals or groups.
    """
    safety_incident = "safety_incident"
    """
    Harm to life, health, property, or the environment from AI behaviour.
    """
    privacy_breach = "privacy_breach"
    """
    Unauthorized disclosure of personal data via the AI system.
    """
    security_breach = "security_breach"
    """
    Compromise of confidentiality, integrity, or availability of the AI system.
    """
    misuse = "misuse"
    """
    Use of the AI system outside its documented intended use.
    """
    adverse_societal_impact = "adverse_societal_impact"
    """
    Broader societal harm reported by external interested parties.
    """
    other = "other"
    """
    Other AI incident category not enumerated above.
    """


class AuditType(str, Enum):
    """
    Type of audit conducted against the AIMS per Clause 9.2 and the ISO 19011 audit taxonomy.
    """
    internal = "internal"
    """
    First-party audit conducted by the organization itself or on its behalf.
    """
    external_second_party = "external_second_party"
    """
    Second-party audit conducted by an interested party (e.g., customer).
    """
    external_third_party = "external_third_party"
    """
    Third-party audit conducted by an independent certification body.
    """
    surveillance = "surveillance"
    """
    Ongoing surveillance audit during the certification cycle.
    """
    recertification = "recertification"
    """
    Audit performed to renew certification.
    """
    combined = "combined"
    """
    Combined audit covering two or more management system disciplines.
    """


class MLApproach(str, Enum):
    """
    Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in B.6.2.3. Distinct from `LearningParadigm`, which describes how often the model updates.
    """
    supervised = "supervised"
    """
    Learns from labelled examples.
    """
    unsupervised = "unsupervised"
    """
    Discovers structure in unlabelled data.
    """
    semi_supervised = "semi_supervised"
    """
    Combines a small labelled set with a larger unlabelled set.
    """
    self_supervised = "self_supervised"
    """
    Generates supervisory signals from the data itself.
    """
    reinforcement = "reinforcement"
    """
    Learns a policy through interaction with an environment and reward signals.
    """
    transfer = "transfer"
    """
    Adapts a pre-trained model to a new task or domain.
    """
    federated = "federated"
    """
    Trains across distributed data holders without centralizing raw data.
    """
    generative = "generative"
    """
    Generative modelling approach (e.g., LLMs, diffusion models).
    """
    symbolic = "symbolic"
    """
    Rule-based or symbolic reasoning, not statistical ML.
    """
    hybrid = "hybrid"
    """
    Combines multiple ML approaches.
    """
    not_applicable = "not_applicable"
    """
    AI system not based on machine learning.
    """


class DataPreparationMethod(str, Enum):
    """
    Common data preparation and transformation methods documented per Annex A.7.6 and Annex B.7.6.
    """
    statistical_exploration = "statistical_exploration"
    """
    Distribution, mean, median, standard deviation, range, stratification, sampling.
    """
    cleaning = "cleaning"
    """
    Correcting entries and handling malformed records.
    """
    imputation = "imputation"
    """
    Filling in missing entries.
    """
    normalization = "normalization"
    """
    Re-scaling values to a common range or distribution.
    """
    scaling = "scaling"
    """
    Multiplicative re-scaling of feature values.
    """
    labelling = "labelling"
    """
    Assigning target labels to records.
    """
    encoding = "encoding"
    """
    Converting categorical variables to numeric representations.
    """
    augmentation = "augmentation"
    """
    Synthesising additional training samples from existing data.
    """
    deduplication = "deduplication"
    """
    Removing duplicate records.
    """
    anonymization = "anonymization"
    """
    Removing or transforming personally identifying information.
    """
    other = "other"
    """
    Other preparation method not enumerated above.
    """


class RelatedManagementSystem(str, Enum):
    """
    Related management-system standards with which the AIMS may be jointly implemented, per the Introduction (Compatibility with other management system standards) and Annex D.
    """
    iso_iec_27001 = "iso_iec_27001"
    """
    Information security management systems.
    """
    iso_iec_27701 = "iso_iec_27701"
    """
    Privacy information management.
    """
    iso_9001 = "iso_9001"
    """
    Quality management systems.
    """
    iso_22000 = "iso_22000"
    """
    Food safety management systems.
    """
    iso_13485 = "iso_13485"
    """
    Medical-device quality management systems.
    """
    iec_62304 = "iec_62304"
    """
    Medical device software life cycle processes.
    """
    iso_iec_5338 = "iso_iec_5338"
    """
    AI system life cycle process.
    """
    iso_iec_5259 = "iso_iec_5259"
    """
    Data quality for analytics and ML.
    """
    iso_iec_22989 = "iso_iec_22989"
    """
    AI concepts and terminology (normative reference).
    """
    iso_iec_23894 = "iso_iec_23894"
    """
    AI risk management guidance.
    """
    iso_iec_38507 = "iso_iec_38507"
    """
    Governance of IT - AI governance implications.
    """
    iso_iec_27000 = "iso_iec_27000"
    """
    Information security management - overview and vocabulary.
    """
    iso_iec_29100 = "iso_iec_29100"
    """
    Privacy framework.
    """
    iso_31000 = "iso_31000"
    """
    Risk management guidelines.
    """
    iso_iec_25024 = "iso_iec_25024"
    """
    Measurement of data quality.
    """
    iso_iec_25059 = "iso_iec_25059"
    """
    Quality model for AI systems.
    """
    iso_19011 = "iso_19011"
    """
    Guidelines for auditing management systems.
    """
    iso_37002 = "iso_37002"
    """
    Whistleblowing management systems (informs A.3.3 concern reporting).
    """
    other = "other"
    """
    Other management system standard not enumerated above.
    """


class GovernanceRoleType(str, Enum):
    """
    Governance role types within the AIMS, paraphrased from Clause 3.3 (top management), Clause 3.22 (governing body), Clause 5.3, and Annex A.3.2. Use this enum on `role_type` for normative governance positions; free-form strings remain accepted for organization-defined roles.
    """
    governing_body = "governing_body"
    """
    Board, trustees, or other body accountable for organizational performance (3.22).
    """
    top_management = "top_management"
    """
    Person or group directing and controlling the organization at the highest level (3.3).
    """
    designated_management = "designated_management"
    """
    Management designated to approve AI risk treatment plans and residual-risk acceptance (6.1.3).
    """
    chief_ai_officer = "chief_ai_officer"
    """
    Senior executive accountable for the AIMS.
    """
    ai_risk_owner = "ai_risk_owner"
    """
    Person accountable for managing a specific AI risk (6.1.2).
    """
    ai_policy_owner = "ai_policy_owner"
    """
    Role accountable for AI policy development and review (A.2.4).
    """
    ai_oversight_committee = "ai_oversight_committee"
    """
    Cross-functional committee providing oversight of AI systems.
    """
    data_steward = "data_steward"
    """
    Role accountable for data resources used by AI systems (A.4.3, A.7).
    """
    model_validator = "model_validator"
    """
    Role responsible for verification and validation of AI models (A.6.2.4).
    """
    human_oversight_reviewer = "human_oversight_reviewer"
    """
    Role performing human-in-the-loop review of AI outputs (B.9.3).
    """
    ai_developer = "ai_developer"
    """
    Role developing AI systems or components.
    """
    ai_operator = "ai_operator"
    """
    Role operating and monitoring AI systems in production.
    """
    ai_impact_assessor = "ai_impact_assessor"
    """
    Role conducting AI system impact assessments (6.1.4).
    """
    auditor = "auditor"
    """
    Internal or external auditor of the AIMS (9.2).
    """
    other = "other"
    """
    Other governance role not enumerated above.
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'comments': ['All concrete classes should inherit from this or a subclass'],
         'exact_mappings': ['iso27001:NamedEntity'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'slot_usage': {'id': {'description': 'Unique identifier for this entity '
                                              'instance.',
                               'identifier': True,
                               'name': 'id',
                               'required': True}}})

    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class DocumentedInformation(NamedEntity):
    """
    Abstract class for documented information per Clause 7.5. Captures metadata required for document control under the AIMS.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.5'}},
         'close_mappings': ['nist_ai_100_1:PlaybookEntry'],
         'comments': ['Captures Clause 7.5 metadata needed for document control, '
                      'review, and retention',
                      'Sub-classes inherit document_type, owner, approval, and '
                      'review-date slots'],
         'exact_mappings': ['iso27001:DocumentedInformation'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['documented_information']})

    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIManagementSystem(NamedEntity):
    """
    Top-level container representing an organization's complete AI Management System (AIMS) per ISO/IEC 42001:2023. Aggregates all components required to support the AIMS lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.4'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'close_mappings': ['iso27001:InformationSecurityManagementSystem',
                            'nist_ai_100_1:AiRmfFramework'],
         'comments': ['Root entity for any ISO/IEC 42001 conformance dataset',
                      'Reference: ISO/IEC 42001:2023 Clause 4.4. ISO/IEC standards '
                      'text is copyright ISO/IEC - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'related_mappings': ['iso29100:PrivacyFramework', 'nist_ai_600_1:GaiProfile']})

    organization: Optional[str] = Field(default=None, description="""Reference to the organization operating the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:organization']} })
    scope_statement: Optional[str] = Field(default=None, description="""Documented statement of AIMS scope per Clause 4.3.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.3'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:scope_statement']} })
    scope_boundaries: Optional[list[str]] = Field(default=None, description="""Defined boundaries of the AIMS scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:scope_boundaries']} })
    scope_exclusions: Optional[list[str]] = Field(default=None, description="""Any exclusions from scope with justification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:scope_exclusions']} })
    context_internal_issues: Optional[list[str]] = Field(default=None, description="""Internal issues relevant to the AIMS per Clause 4.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:context_internal_issues']} })
    context_external_issues: Optional[list[str]] = Field(default=None, description="""External issues relevant to the AIMS per Clause 4.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:context_external_issues']} })
    organizational_roles_with_ai: Optional[list[AIOrganizationalRole]] = Field(default=None, description="""Documented set of roles the organization plays in the AI ecosystem within the AIMS scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    integrated_management_systems: Optional[list[RelatedManagementSystem]] = Field(default=None, description="""Related management-system standards with which the AIMS is jointly implemented or aligned (Introduction - Compatibility with other management system standards, Annex D).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:integrated_management_systems']} })
    top_management: Optional[str] = Field(default=None, description="""Reference to the person or group exercising top management direction and control over the AIMS (Clause 3.3, 5.1).""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '3.3'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:top_management']} })
    governing_body: Optional[str] = Field(default=None, description="""Reference to the governing body to which top management is accountable (Clause 3.22).""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '3.22'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:governing_body']} })
    leadership_commitment_evidence: Optional[list[str]] = Field(default=None, description="""Records or references demonstrating top-management leadership and commitment to the AIMS per Clause 5.1.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.1'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:leadership_commitment_evidence']} })
    planned_changes: Optional[list[str]] = Field(default=None, description="""Records of planned changes to the AIMS, including purpose, consequences, resource implications, and responsibilities per Clause 6.3.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '6.3'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:planned_changes']} })
    interested_parties: Optional[list[str]] = Field(default=None, description="""Stakeholders relevant to the AIMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.2'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:interested_parties']} })
    ai_policy: Optional[str] = Field(default=None, description="""Reference to the AI policy.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'close_mappings': ['iso27001:information_security_policy'],
         'domain_of': ['AIManagementSystem']} })
    ai_objectives: Optional[list[str]] = Field(default=None, description="""AI objectives established by the organization.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:objectives'], 'domain_of': ['AIManagementSystem']} })
    ai_risk_assessment_process: Optional[str] = Field(default=None, description="""Reference to the AI risk assessment process.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:risk_assessment_process'],
         'domain_of': ['AIManagementSystem']} })
    ai_risk_treatment_process: Optional[str] = Field(default=None, description="""Reference to the AI risk treatment process.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:risk_treatment_process'],
         'domain_of': ['AIManagementSystem']} })
    ai_system_impact_assessment_process: Optional[str] = Field(default=None, description="""Reference to the AI system impact assessment process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    statement_of_applicability: Optional[str] = Field(default=None, description="""Reference to the AIMS Statement of Applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:statement_of_applicability']} })
    reference_controls: Optional[list[str]] = Field(default=None, description="""AI reference controls applied within the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    ai_systems: Optional[list[str]] = Field(default=None, description="""AI systems within the AIMS scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    roles: Optional[list[str]] = Field(default=None, description="""AI-related roles defined in the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    resources: Optional[list[str]] = Field(default=None, description="""Resources provided for the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'], 'exact_mappings': ['iso27001:resources']} })
    competence_records: Optional[list[str]] = Field(default=None, description="""Competence records for personnel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:competence_records']} })
    awareness_program: Optional[str] = Field(default=None, description="""Reference to the awareness program.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:awareness_program']} })
    communication_plan: Optional[str] = Field(default=None, description="""Reference to the communication plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem', 'AIIncident'],
         'exact_mappings': ['iso27001:communication_plan']} })
    documented_information_register: Optional[list[str]] = Field(default=None, description="""Register of all documented information.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.5'}},
         'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:documented_information_register']} })
    operational_procedures: Optional[list[str]] = Field(default=None, description="""Operational procedures of the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:operational_procedures']} })
    ai_risk_assessments: Optional[list[str]] = Field(default=None, description="""AI risk assessment instances.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:risk_assessments'],
         'domain_of': ['AIManagementSystem']} })
    ai_risk_treatment_plans: Optional[list[str]] = Field(default=None, description="""AI risk treatment plans.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:risk_treatment_plans'],
         'domain_of': ['AIManagementSystem']} })
    ai_system_impact_assessments: Optional[list[str]] = Field(default=None, description="""AI system impact assessment instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    monitoring_program: Optional[str] = Field(default=None, description="""Reference to the monitoring program.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:monitoring_program']} })
    internal_audits: Optional[list[str]] = Field(default=None, description="""Internal audits conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:internal_audits']} })
    management_reviews: Optional[list[str]] = Field(default=None, description="""Management reviews of the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:management_reviews']} })
    nonconformities: Optional[list[str]] = Field(default=None, description="""Nonconformities identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:nonconformities']} })
    corrective_actions: Optional[list[str]] = Field(default=None, description="""Corrective actions taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:corrective_actions']} })
    improvements: Optional[list[str]] = Field(default=None, description="""Improvement opportunities being tracked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:improvements']} })
    third_party_relationships: Optional[list[str]] = Field(default=None, description="""Third-party relationships within the AIMS scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem']} })
    certification_status: Optional[str] = Field(default=None, description="""Current certification status of the AIMS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:certification_status']} })
    certification_body: Optional[str] = Field(default=None, description="""Body that issued the certification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:certification_body']} })
    certification_date: Optional[date] = Field(default=None, description="""Date the AIMS was certified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:certification_date']} })
    recertification_date: Optional[date] = Field(default=None, description="""Date when recertification is due.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem'],
         'exact_mappings': ['iso27001:recertification_date']} })
    ai_system_events: Optional[list[str]] = Field(default=None, description="""AI system events recorded under the AIMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.6.2.8'}},
         'domain_of': ['AIManagementSystem'],
         'related_mappings': ['nist_ai_100_1:harms']} })
    ai_incidents: Optional[list[str]] = Field(default=None, description="""AI incidents managed under the AIMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.8.4'}},
         'domain_of': ['AIManagementSystem']} })
    concern_reports: Optional[list[str]] = Field(default=None, description="""Concern reports raised and managed under the AIMS per A.3.3.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.3.3'}},
         'domain_of': ['AIManagementSystem']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Organization(NamedEntity):
    """
    The organization establishing and operating the AIMS. Captures the context required by Clause 4.1, including the organization's role(s) with respect to AI systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'close_mappings': ['iso29100:PIIController', 'nist_ai_100_1:AiActor'],
         'comments': ['Captures the organizational context required by Clause 4.1',
                      'AI roles determine the applicability scope of Annex A controls'],
         'exact_mappings': ['iso27001:Organization', 'iso22989:organization'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'related_mappings': ['iso29100:PIIProcessor']})

    legal_name: Optional[str] = Field(default=None, description="""Legal registered name of the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    trading_names: Optional[list[str]] = Field(default=None, description="""Names under which the organization conducts business.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    organization_type: Optional[str] = Field(default=None, description="""Type of organization (e.g., corporation, government, nonprofit).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    industry_sector: Optional[str] = Field(default=None, description="""Primary industry sector of the organization (free-form label).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization'],
         'examples': [{'value': 'Financial Services'},
                      {'value': 'Healthcare'},
                      {'value': 'Public Sector'}]} })
    sector_domains: Optional[list[SectorDomain]] = Field(default=None, description="""Application sectors in which the organization deploys AI systems, drawn from the Annex D examples; supports identification of sector- specific management system standards that integrate with the AIMS.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': 'Annex D'}},
         'domain_of': ['Organization']} })
    size_category: Optional[str] = Field(default=None, description="""Organization size classification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization'],
         'examples': [{'value': 'SME'}, {'value': 'Enterprise'}]} })
    employee_count: Optional[int] = Field(default=None, description="""Approximate number of employees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    geographic_locations: Optional[list[str]] = Field(default=None, description="""Countries or regions where the organization operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    regulatory_jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions whose regulations apply to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    parent_organization: Optional[str] = Field(default=None, description="""Parent organization if applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    subsidiaries: Optional[list[str]] = Field(default=None, description="""Subsidiary organizations if applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    ai_roles: Optional[list[AIOrganizationalRole]] = Field(default=None, description="""Roles the organization takes with respect to AI systems (provider, producer, customer, partner, subject, authority).""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'close_mappings': ['iso27001:roles'],
         'domain_of': ['Organization']} })
    climate_change_relevant: Optional[bool] = Field(default=None, description="""Whether climate change has been determined to be a relevant issue for the organization's context per Clause 4.1.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['Organization'],
         'exact_mappings': ['iso27001:climate_change_relevant']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class InterestedParty(NamedEntity):
    """
    A stakeholder whose needs and expectations are relevant to the AIMS per Clause 4.2. Includes internal and external parties such as users, regulators, partners, suppliers, customers, AI subjects, and relevant authorities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.2'}},
         'close_mappings': ['iso29100:PrivacyStakeholder', 'nist_ai_100_1:AiActor'],
         'comments': ['Drives the requirements analysis required by Clause 4.2',
                      'Includes AI subjects and relevant authorities, not only '
                      'customers/suppliers'],
         'exact_mappings': ['iso27001:InterestedParty', 'iso22989:interested_party'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    party_type: Optional[str] = Field(default=None, description="""Category of party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty', 'ThirdPartyRelationship'],
         'examples': [{'value': 'internal'},
                      {'value': 'external'},
                      {'value': 'regulatory'},
                      {'value': 'ai_subject'},
                      {'value': 'supplier'},
                      {'value': 'customer'}]} })
    relationship: Optional[str] = Field(default=None, description="""Nature of the relationship with the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    requirements: Optional[list[str]] = Field(default=None, description="""Requirements of the interested party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    communication_needs: Optional[str] = Field(default=None, description="""Communication requirements for this party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    contact_information: Optional[str] = Field(default=None, description="""Contact details for the party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIPolicy(DocumentedInformation):
    """
    The AI policy established by top management per Clause 5.2. Provides a framework for setting AI objectives and demonstrates commitment to responsible AI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'close_mappings': ['iso27001:InformationSecurityPolicy',
                            'iso29100:PrivacyPolicy'],
         'comments': ['Top-management AI policy per Clause 5.2; framework for AI '
                      'objectives',
                      'Reviewed at planned intervals per Annex A.2.4'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'documented_information']})

    policy_statement: Optional[str] = Field(default=None, description="""The core policy statement text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy']} })
    policy_objectives_framework: Optional[str] = Field(default=None, description="""Framework for setting AI objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy']} })
    commitment_statements: Optional[list[str]] = Field(default=None, description="""Statements of commitment included in the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy']} })
    applicability_statement: Optional[str] = Field(default=None, description="""Statement of policy applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy']} })
    communication_date: Optional[date] = Field(default=None, description="""Date when the policy was communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy']} })
    acknowledgment_required: Optional[bool] = Field(default=None, description="""Whether acknowledgment is required from personnel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy']} })
    related_topic_policies: Optional[list[str]] = Field(default=None, description="""Topic-specific policies supporting this policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPolicy'],
         'exact_mappings': ['iso27001:related_topic_policies']} })
    last_policy_review_date: Optional[date] = Field(default=None, description="""Date of the most recent AI policy review.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.2.4'}},
         'domain_of': ['AIPolicy'],
         'exact_mappings': ['iso27001:last_policy_review_date']} })
    next_policy_review_date: Optional[date] = Field(default=None, description="""Planned date of the next AI policy review.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.2.4'}},
         'domain_of': ['AIPolicy'],
         'exact_mappings': ['iso27001:next_policy_review_date']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class TopicSpecificPolicy(DocumentedInformation):
    """
    A topic-specific policy supporting the overarching AI policy, for example covering data governance, fairness, transparency, supplier use, or human oversight of AI systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.2'}},
         'comments': ['Supports the overarching AI policy with topic-specific guidance '
                      '(data, fairness, oversight)',
                      'Typical topics: data governance, transparency, human oversight, '
                      'supplier use'],
         'exact_mappings': ['iso27001:TopicSpecificPolicy'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['documented_information']})

    topic_area: Optional[str] = Field(default=None, description="""The specific topic addressed by the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy'],
         'examples': [{'value': 'Data Governance'},
                      {'value': 'Human Oversight'},
                      {'value': 'Model Validation'},
                      {'value': 'Transparency'}]} })
    parent_policy: Optional[str] = Field(default=None, description="""The parent AI policy this topic-specific policy supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy']} })
    applicable_controls: Optional[list[str]] = Field(default=None, description="""Reference controls related to this policy or AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'AISystem']} })
    target_audience: Optional[str] = Field(default=None, description="""Intended audience for the policy or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'AwarenessProgram']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Role(NamedEntity):
    """
    An AI-related role with defined responsibilities and authorities per Clause 5.3 and Annex A.3.2.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.3.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.3'}},
         'close_mappings': ['nist_ai_100_1:AiActorTask'],
         'comments': ['AI-related role per Clause 5.3 and Annex A.3.2',
                      'Roles should be allocated according to organizational needs, '
                      'with clear authorities and reporting lines'],
         'exact_mappings': ['iso27001:Role'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    role_type: Optional[Union[GovernanceRoleType, str]] = Field(default=None, description="""Category of the role. Use a `GovernanceRoleType` value for the normative AIMS governance positions; free-form strings remain accepted for organization-defined roles.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'GovernanceRoleType'}, {'range': 'string'}],
         'domain_of': ['Role'],
         'examples': [{'value': 'top_management'},
                      {'value': 'governing_body'},
                      {'value': 'ai_risk_owner'},
                      {'value': 'Chief AI Officer'},
                      {'value': 'Model Validator'}]} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Responsibilities assigned to the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    authorities: Optional[list[str]] = Field(default=None, description="""Authorities granted to the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    accountability: Optional[str] = Field(default=None, description="""What the role is accountable for.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_ai_100_1:TrustworthinessCharacteristic'],
         'domain_of': ['Role'],
         'exact_mappings': ['iso29100:accountability']} })
    assigned_to: Optional[list[str]] = Field(default=None, description="""Person(s) assigned to this role or resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'HumanResource']} })
    delegation_rules: Optional[str] = Field(default=None, description="""Rules for delegating responsibilities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    reporting_line: Optional[str] = Field(default=None, description="""To whom this role reports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIObjective(NamedEntity):
    """
    A measurable AI objective per Clause 6.2, established at relevant functions and levels and aligned with the AI policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '6.2'}},
         'close_mappings': ['iso27001:InformationSecurityObjective'],
         'comments': ['Measurable AI objective per Clause 6.2, consistent with the AI '
                      'policy',
                      'Examples align with Annex C objective categories (fairness, '
                      'transparency, robustness, etc.)'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    objective_statement: Optional[str] = Field(default=None, description="""Clear statement of the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    objective_category: Optional[AIObjectiveCategory] = Field(default=None, description="""Category of AI objective (e.g., fairness, transparency, robustness).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    target_value: Optional[str] = Field(default=None, description="""Target value for the objective metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    current_value: Optional[str] = Field(default=None, description="""Current measured value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'MonitoringItem']} })
    metric_definition: Optional[str] = Field(default=None, description="""Definition of how the objective is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used to measure the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'MonitoringItem']} })
    measurement_frequency: Optional[str] = Field(default=None, description="""How often measurement is performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'MonitoringItem']} })
    responsible_role: Optional[str] = Field(default=None, description="""Role responsible for the objective or control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'SoAEntry']} })
    resources_required: Optional[str] = Field(default=None, description="""Resources required for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'AIRiskTreatmentPlan', 'CorrectiveAction']} })
    target_date: Optional[date] = Field(default=None, description="""Target date for achieving the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'ImprovementOpportunity']} })
    achievement_status: Optional[str] = Field(default=None, description="""Current status of objective achievement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    related_risks: Optional[list[str]] = Field(default=None, description="""Associated AI risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Other reference controls related to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'AIReferenceControl', 'OperationalProcedure']} })
    action_plan: Optional[str] = Field(default=None, description="""Plan for achieving the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIRiskAssessmentProcess(DocumentedInformation):
    """
    The documented AI risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analysing, and evaluating AI risks. Aligned with ISO/IEC 23894.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'close_mappings': ['iso27001:RiskAssessmentProcess', 'nist_ai_100_1:Function'],
         'comments': ['Defines methodology for AI risk identification, analysis, and '
                      'evaluation per Clause 6.1.2',
                      'Aligned with ISO/IEC 23894 risk-management guidance'],
         'exact_mappings': ['iso23894:risk_management_process',
                            'iso27001:risk_assessment_process'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management', 'documented_information']})

    risk_acceptance_criteria: Optional[str] = Field(default=None, description="""Criteria for accepting AI risks.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.1'}},
         'domain_of': ['AIRiskAssessmentProcess']} })
    assessment_criteria: Optional[str] = Field(default=None, description="""Criteria for performing AI risk or impact assessments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    assessment_methodology: Optional[str] = Field(default=None, description="""Methodology used for assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    likelihood_scale: Optional[str] = Field(default=None, description="""Scale used for likelihood rating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess']} })
    impact_scale: Optional[str] = Field(default=None, description="""Scale used for impact rating.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess']} })
    risk_matrix: Optional[str] = Field(default=None, description="""Risk matrix or calculation method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess']} })
    assessment_frequency: Optional[str] = Field(default=None, description="""Planned frequency of assessments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    trigger_events: Optional[list[str]] = Field(default=None, description="""Events that trigger an assessment outside the planned schedule.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 8.2 / 8.4 when significant changes are proposed or occur'],
         'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    alignment_with_ai_policy: Optional[str] = Field(default=None, description="""Statement of how the process aligns with the AI policy.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2 a)'}},
         'domain_of': ['AIRiskAssessmentProcess']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIRiskAssessment(DocumentedInformation):
    """
    An instance of AI risk assessment performed per Clause 8.2, identifying and evaluating AI risks at planned intervals or following significant change.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.2'}},
         'close_mappings': ['iso27001:RiskAssessment'],
         'comments': ['Instance of an AI risk assessment per Clause 8.2',
                      'Performed at planned intervals or on significant change'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management']})

    assessment_scope: Optional[str] = Field(default=None, description="""Scope of the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    ai_systems_assessed: Optional[list[str]] = Field(default=None, description="""AI systems covered by this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    assessment_date: Optional[date] = Field(default=None, description="""Date the assessment was conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    assessor: Optional[str] = Field(default=None, description="""Person or team who conducted the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    methodology_used: Optional[str] = Field(default=None, description="""Specific methodology applied in this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment']} })
    risks_identified: Optional[list[str]] = Field(default=None, description="""Risks identified in this assessment.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso29100:privacy_risks', 'nist_ai_100_1:risks'],
         'domain_of': ['AIRiskAssessment']} })
    linked_impact_assessment: Optional[str] = Field(default=None, description="""AI system impact assessment linked to this risk assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment']} })
    summary_findings: Optional[str] = Field(default=None, description="""Summary of assessment findings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment']} })
    recommendations: Optional[list[str]] = Field(default=None, description="""Recommendations from the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment']} })
    next_assessment_date: Optional[date] = Field(default=None, description="""Planned date for next assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIRisk(NamedEntity):
    """
    An identified AI risk that may affect achievement of AI objectives, individuals, groups, or societies within the AIMS scope.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2'}},
         'close_mappings': ['iso27001:Risk',
                            'nist_ai_100_1:Risk',
                            'nist_ai_600_1:GaiRisk'],
         'comments': ['Risk source categories drawn from Annex C',
                      'Affects organization, individuals, groups, or societies per '
                      'Clause 6.1.2 d) 1)'],
         'exact_mappings': ['iso23894:risk', 'iso27001:Risk'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management'],
         'narrow_mappings': ['nist_ai_100_1:AiSpecificRisk', 'nist_ai_600_1:GaiRisk'],
         'related_mappings': ['iso29100:PrivacyRisk']})

    risk_source_category: Optional[AIRiskSourceCategory] = Field(default=None, description="""Category of AI risk source per Annex C.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    risk_source_description: Optional[str] = Field(default=None, description="""Description of the specific source of risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    affected_ai_systems: Optional[list[str]] = Field(default=None, description="""AI systems affected by this risk.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:affected_assets'],
         'domain_of': ['AIRisk', 'AISystemEvent', 'AIIncident'],
         'related_mappings': ['nist_ai_600_1:risk_scope']} })
    affected_dimensions: Optional[list[ImpactAssessmentDimension]] = Field(default=None, description="""Dimensions of impact affected by the risk (individual, group, societal, safety, privacy, security, environmental).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk', 'AIIncident']} })
    risk_owner: Optional[str] = Field(default=None, description="""Person accountable for managing the AI risk.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2'}},
         'close_mappings': ['iso29100:pii_controller'],
         'domain_of': ['AIRisk']} })
    likelihood: Optional[LikelihoodRating] = Field(default=None, description="""Assessed likelihood of risk occurrence.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2 d) 2)'}},
         'domain_of': ['AIRisk']} })
    impact: Optional[ImpactRating] = Field(default=None, description="""Assessed consequence if the risk materializes.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2 d) 1)'}},
         'domain_of': ['AIRisk']} })
    inherent_risk_level: Optional[RiskLevel] = Field(default=None, description="""Risk level before controls are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    existing_controls: Optional[list[str]] = Field(default=None, description="""Controls currently in place affecting this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    residual_risk_level: Optional[RiskLevel] = Field(default=None, description="""Risk level after controls are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    risk_treatment_option: Optional[RiskTreatmentOption] = Field(default=None, description="""Selected treatment option for the AI risk.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_ai_100_1:risk_response'], 'domain_of': ['AIRisk']} })
    treatment_priority: Optional[str] = Field(default=None, description="""Priority for treating this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    related_treatment_plan: Optional[str] = Field(default=None, description="""Risk treatment plan addressing this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    related_impact_assessment: Optional[str] = Field(default=None, description="""AI system impact assessment associated with this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIRiskTreatmentProcess(DocumentedInformation):
    """
    The documented AI risk treatment process per Clause 6.1.3, defining how treatment options are selected, how Annex A controls are considered, and how the Statement of Applicability is produced.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'close_mappings': ['iso27001:RiskTreatmentProcess'],
         'comments': ['Defines treatment-option selection and SoA production per '
                      'Clause 6.1.3',
                      'Annex A controls must be considered before custom controls are '
                      'added'],
         'exact_mappings': ['iso23894:risk_treatment_process',
                            'iso27001:risk_treatment_process'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management', 'documented_information']})

    treatment_options_guidance: Optional[str] = Field(default=None, description="""Guidance on selecting AI risk treatment options.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentProcess']} })
    control_selection_criteria: Optional[str] = Field(default=None, description="""Criteria for selecting Annex A controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentProcess']} })
    soa_template: Optional[str] = Field(default=None, description="""Template used for the Statement of Applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentProcess']} })
    approval_workflow: Optional[str] = Field(default=None, description="""Workflow for approving AI risk treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentProcess']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIRiskTreatmentPlan(DocumentedInformation):
    """
    A plan documenting planned actions to address identified AI risks through selected controls. Requires approval by designated management per Clause 6.1.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['iso27001:RiskTreatmentPlan'],
         'comments': ['Requires approval by designated management and acceptance of '
                      'residual risk per Clause 6.1.3',
                      'Tracks controls, owners, timelines, and implementation status'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management', 'documented_information'],
         'related_mappings': ['iso29100:PrivacySafeguardingRequirement',
                              'nist_ai_100_1:RiskTolerance',
                              'nist_ai_600_1:SuggestedAction']})

    plan_scope: Optional[str] = Field(default=None, description="""Scope of the treatment plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    risks_addressed: Optional[list[str]] = Field(default=None, description="""Risks addressed by this plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    treatment_actions: Optional[list[str]] = Field(default=None, description="""Actions to be taken for treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    controls_to_implement: Optional[list[str]] = Field(default=None, description="""Controls to be implemented as part of treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    resources_required: Optional[str] = Field(default=None, description="""Resources required for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'AIRiskTreatmentPlan', 'CorrectiveAction']} })
    responsible_parties: Optional[list[str]] = Field(default=None, description="""Parties responsible for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    implementation_timeline: Optional[str] = Field(default=None, description="""Timeline for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    risk_owner_approval: Optional[str] = Field(default=None, description="""Risk owner who approved the plan.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'domain_of': ['AIRiskTreatmentPlan']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    residual_risk_acceptance: Optional[str] = Field(default=None, description="""Documentation of residual AI risk acceptance.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['nist_ai_100_1:residual_risk'],
         'domain_of': ['AIRiskTreatmentPlan']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Current implementation status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan', 'SoAEntry', 'AIReferenceControl']} })
    completion_date: Optional[date] = Field(default=None, description="""Date when implementation was completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AISystemImpactAssessmentProcess(DocumentedInformation):
    """
    The documented process for assessing the potential consequences for individuals, groups, and societies arising from the development, provision, or use of AI systems per Clause 6.1.4.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.5.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'comments': ['Documented process per Clause 6.1.4 and Annex A.5.2',
                      'Outputs feed back into AI risk assessment per Clause 6.1.4'],
         'exact_mappings': ['iso23894:impact_assessment_process'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management', 'documented_information'],
         'related_mappings': ['iso27001:RiskAssessmentProcess']})

    assessment_criteria: Optional[str] = Field(default=None, description="""Criteria for performing AI risk or impact assessments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    assessment_methodology: Optional[str] = Field(default=None, description="""Methodology used for assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    dimensions_in_scope: Optional[list[ImpactAssessmentDimension]] = Field(default=None, description="""Impact dimensions evaluated by the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessmentProcess']} })
    assessment_frequency: Optional[str] = Field(default=None, description="""Planned frequency of assessments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    trigger_events: Optional[list[str]] = Field(default=None, description="""Events that trigger an assessment outside the planned schedule.""", json_schema_extra = { "linkml_meta": {'comments': ['Per 8.2 / 8.4 when significant changes are proposed or occur'],
         'domain_of': ['AIRiskAssessmentProcess', 'AISystemImpactAssessmentProcess']} })
    linkage_to_risk_assessment: Optional[str] = Field(default=None, description="""Description of how impact assessment results feed into AI risk assessment per Clause 6.1.4.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessmentProcess']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AISystemImpactAssessment(DocumentedInformation):
    """
    An instance of an AI system impact assessment performed per Clause 6.1.4 and Clause 8.4. Documents consequences of deployment, intended use, and foreseeable misuse on individuals, groups, and societies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.5'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'close_mappings': ['iso29100:PrivacyImpactAssessment',
                            'nist_ai_100_1:Impact',
                            'nist_ai_600_1:PrimaryGaiConsideration'],
         'comments': ['Instance assessing consequences for individuals, groups, and '
                      'societies per Clause 8.4',
                      'Considers deployment context, intended use, and reasonably '
                      'foreseeable misuse'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_risk_management', 'documented_information'],
         'related_mappings': ['iso27001:RiskAssessment']})

    assessment_scope: Optional[str] = Field(default=None, description="""Scope of the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    ai_systems_assessed: Optional[list[str]] = Field(default=None, description="""AI systems covered by this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    assessment_date: Optional[date] = Field(default=None, description="""Date the assessment was conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    assessor: Optional[str] = Field(default=None, description="""Person or team who conducted the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    technical_context: Optional[str] = Field(default=None, description="""Specific technical context in which the AI system is deployed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    societal_context: Optional[str] = Field(default=None, description="""Societal context relevant to the impact assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    applicable_jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions relevant to the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    dimensions_assessed: Optional[list[ImpactAssessmentDimension]] = Field(default=None, description="""Impact dimensions actually assessed in this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    identified_consequences: Optional[list[str]] = Field(default=None, description="""Identified positive or negative consequences.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    mitigations: Optional[list[str]] = Field(default=None, description="""Mitigations to address identified consequences.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    shared_with_parties: Optional[list[str]] = Field(default=None, description="""Interested parties with whom the results have been shared.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemImpactAssessment']} })
    next_assessment_date: Optional[date] = Field(default=None, description="""Planned date for next assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskAssessment', 'AISystemImpactAssessment']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class StatementOfApplicability(DocumentedInformation):
    """
    The Statement of Applicability (SoA) for the AIMS recording which Annex A controls apply, justification for inclusion or exclusion, and current implementation state per Clause 6.1.3 f).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3 f)'},
                         'mandatory': {'tag': 'mandatory', 'value': 'true'}},
         'comments': ['Records applicability, justification, and implementation status '
                      'per Clause 6.1.3 f)',
                      'Equivalent role to ISO/IEC 27001:2022 SoA'],
         'exact_mappings': ['iso27001:StatementOfApplicability'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'annex_a_controls', 'documented_information']})

    soa_entries: Optional[list[SoAEntry]] = Field(default=None, description="""Individual control entries in the SoA.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    total_controls: Optional[int] = Field(default=None, description="""Total number of controls in scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    implemented_count: Optional[int] = Field(default=None, description="""Number of implemented controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    planned_count: Optional[int] = Field(default=None, description="""Number of controls planned for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    not_applicable_count: Optional[int] = Field(default=None, description="""Number of controls marked not applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    last_review_date: Optional[date] = Field(default=None, description="""Date of last review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatementOfApplicability']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class SoAEntry(ConfiguredBaseModel):
    """
    A single entry in the AIMS Statement of Applicability documenting the applicability and implementation status of one reference control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['One row of the SoA: links a control to applicability, '
                      'justification, and status',
                      'Exclusion justifications should reference risk assessment '
                      'outputs or external requirements'],
         'exact_mappings': ['iso27001:SoAEntry'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['annex_a_controls']})

    control_reference: Optional[str] = Field(default=None, description="""Reference to an Annex A control (e.g., A.6.2.4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry', 'AuditFinding']} })
    is_applicable: Optional[bool] = Field(default=None, description="""Whether the control is applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry']} })
    inclusion_justification: Optional[str] = Field(default=None, description="""Justification for including the control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3 f)'}},
         'domain_of': ['SoAEntry']} })
    exclusion_justification: Optional[str] = Field(default=None, description="""Justification for excluding the control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3 f)'}},
         'domain_of': ['SoAEntry']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Current implementation status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan', 'SoAEntry', 'AIReferenceControl']} })
    implementation_evidence: Optional[str] = Field(default=None, description="""Evidence of control implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry']} })
    responsible_role: Optional[str] = Field(default=None, description="""Role responsible for the objective or control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'SoAEntry']} })
    target_implementation_date: Optional[date] = Field(default=None, description="""Target date for implementing the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry']} })


class AIReferenceControl(NamedEntity):
    """
    A reference control from Annex A of ISO/IEC 42001:2023. Controls are grouped into nine families (A.2 through A.10) and supported by implementation guidance in Annex B.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_reference': {'tag': 'annex_reference',
                                             'value': 'Annex A'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['iso27001:SecurityControl',
                            'iso29100:PrivacyControl',
                            'nist_ai_100_1:Subcategory'],
         'comments': ['Reference: ISO/IEC 42001:2023 Annex A and Annex B. ISO/IEC '
                      'standards text is copyright ISO/IEC - not reproduced here.',
                      'The control_text slot must contain organization-authored '
                      'content only, not ISO/IEC standards text.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['annex_a_controls'],
         'related_mappings': ['nist_ai_600_1:SuggestedAction']})

    control_id: Optional[Union[AnnexAControlId, str]] = Field(default=None, description="""Control identifier from Annex A (e.g., A.6.2.4). Accepts either an enumerated normative `AnnexAControlId` value or a free-form string for organization-defined controls beyond Annex A.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'AnnexAControlId'}, {'range': 'string'}],
         'comments': ['Format matches Annex A numbering '
                      '(A.<family>[.<subclause>][.<control>])',
                      'Use AnnexAControlId for the 38 normative Annex A controls; use '
                      'string for org-defined controls.'],
         'domain_of': ['AIReferenceControl']} })
    control_title: Optional[str] = Field(default=None, description="""Title of the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    control_family: Optional[AIControlFamily] = Field(default=None, description="""Family of the Annex A control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    control_text: Optional[str] = Field(default=None, description="""Organization-authored control statement or external control summary. Do not include verbatim ISO/IEC standards text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    implementation_guidance: Optional[str] = Field(default=None, description="""Organization-authored implementation notes for the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Other reference controls related to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'AIReferenceControl', 'OperationalProcedure']} })
    applicable_risk_sources: Optional[list[AIRiskSourceCategory]] = Field(default=None, description="""Categories of AI risk source this control addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    applicable_objectives: Optional[list[AIObjectiveCategory]] = Field(default=None, description="""AI objective categories this control supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    control_owner: Optional[str] = Field(default=None, description="""Person responsible for the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Current implementation status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRiskTreatmentPlan', 'SoAEntry', 'AIReferenceControl']} })
    implementation_date: Optional[date] = Field(default=None, description="""Date the control was implemented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    effectiveness_rating: Optional[str] = Field(default=None, description="""Rating of control effectiveness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    last_test_date: Optional[date] = Field(default=None, description="""Date the control was last tested.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    evidence_references: Optional[list[str]] = Field(default=None, description="""References to evidence of implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIReferenceControl']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })

    @field_validator('control_id')
    def pattern_control_id(cls, v):
        pattern=re.compile(r"^A\.[0-9]{1,2}(\.[0-9]{1,2})*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid control_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid control_id format: {v}"
            raise ValueError(err_msg)
        return v


class AISystem(NamedEntity):
    """
    An AI system within the AIMS scope. Captures life cycle stage, intended use, applicable domains, and references to data and tooling resources, technical documentation, and impact assessments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.6'}},
         'comments': ['Captures life cycle stage, intended use, foreseeable misuse, '
                      'and resource references per Annex A.6',
                      'AI systems are the primary unit to which impact assessments and '
                      'incidents attach'],
         'exact_mappings': ['iso22989:ai_system', 'nist_ai_100_1:AiSystem'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_system_lifecycle'],
         'related_mappings': ['iso27001:Asset', 'nist_ai_600_1:GaiProfile']})

    ai_system_purpose: Optional[str] = Field(default=None, description="""Purpose of the AI system.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_ai_100_1:application_domain'],
         'domain_of': ['AISystem']} })
    intended_uses: Optional[list[str]] = Field(default=None, description="""Documented intended uses of the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.9.4'}},
         'close_mappings': ['nist_ai_100_1:intended_use'],
         'domain_of': ['AISystem']} })
    foreseeable_misuse: Optional[list[str]] = Field(default=None, description="""Reasonably foreseeable misuse of the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.5'}},
         'close_mappings': ['nist_ai_100_1:potential_misuse'],
         'domain_of': ['AISystem']} })
    application_domain: Optional[str] = Field(default=None, description="""Domain in which the AI system is applied (e.g., health, finance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    deployment_context: Optional[str] = Field(default=None, description="""Operational context in which the AI system is deployed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    lifecycle_stage: Optional[AISystemLifecycleStage] = Field(default=None, description="""Current life cycle stage of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem'], 'exact_mappings': ['nist_ai_100_1:lifecycle_stage']} })
    organization_role: Optional[AIOrganizationalRole] = Field(default=None, description="""The organization's role with respect to this AI system (provider, producer, customer, partner).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    autonomy_level: Optional[str] = Field(default=None, description="""Description of the level of autonomy and human oversight required for this AI system. Free-form text complements `human_oversight_required` and `human_oversight_description`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    ml_approach: Optional[MLApproach] = Field(default=None, description="""Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in Annex B.6.2.3.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.6.2.3'}},
         'domain_of': ['AISystem']} })
    human_oversight_required: Optional[bool] = Field(default=None, description="""Whether human oversight is required for outputs of the AI system (Annex A.9, Annex B.9.3).""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.9'}},
         'close_mappings': ['nist_ai_100_1:human_ai_configuration'],
         'domain_of': ['AISystem']} })
    human_oversight_description: Optional[str] = Field(default=None, description="""Description of human-oversight arrangements, including review points, escalation paths, and oversight authority (Annex B.9.3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    human_oversight_stages: Optional[list[AISystemLifecycleStage]] = Field(default=None, description="""AI system life cycle stages at which human oversight applies (Annex B.9.3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    learning_mode: Optional[LearningParadigm] = Field(default=None, description="""Learning paradigm of the AI system (informs Clause 6.1 risk and Annex A.6.2.6 monitoring considerations).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    data_resources: Optional[list[str]] = Field(default=None, description="""Data resources used by the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.3'}},
         'domain_of': ['AISystem']} })
    tooling_resources: Optional[list[str]] = Field(default=None, description="""Tooling resources used by the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.4'}},
         'domain_of': ['AISystem']} })
    computing_resources: Optional[list[str]] = Field(default=None, description="""System and computing resources used by the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.5'}},
         'domain_of': ['AISystem']} })
    human_resources: Optional[list[str]] = Field(default=None, description="""Human resources involved with the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.6'}},
         'domain_of': ['AISystem']} })
    technical_documentation: Optional[list[str]] = Field(default=None, description="""Reference to AI system technical documentation.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.6.2.7'}},
         'domain_of': ['AISystem']} })
    event_log_policy: Optional[str] = Field(default=None, description="""Policy for AI system event log recording across life cycle phases.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.6.2.8'}},
         'domain_of': ['AISystem']} })
    applicable_controls: Optional[list[str]] = Field(default=None, description="""Reference controls related to this policy or AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'AISystem']} })
    related_impact_assessments: Optional[list[str]] = Field(default=None, description="""Impact assessments related to this AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    supplier_relationships: Optional[list[str]] = Field(default=None, description="""Supplier relationships relevant to this AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    customer_relationships: Optional[list[str]] = Field(default=None, description="""Customer relationships relevant to this AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class DataResource(NamedEntity):
    """
    A data resource used by an AI system per Annex A.7. Includes data acquisition, quality, provenance, and preparation metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.7'}},
         'close_mappings': ['iso29100:PersonallyIdentifiableInformation'],
         'comments': ['Data resource documentation per Annex A.4.3 and A.7',
                      'Captures acquisition, quality, provenance, preparation, and '
                      'known bias issues'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_data_management'],
         'narrow_mappings': ['iso27001:Asset']})

    data_resource_category: Optional[DataResourceCategory] = Field(default=None, description="""Category of data resource (training, validation, test, production).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    source: Optional[str] = Field(default=None, description="""Source from which the data was obtained.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    acquisition_method: Optional[str] = Field(default=None, description="""How the data was acquired (e.g., collected, purchased, synthetic).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    data_quality_requirements: Optional[list[str]] = Field(default=None, description="""Documented data quality requirements for the AI system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.7.4'}},
         'domain_of': ['DataResource']} })
    data_quality_metrics: Optional[list[str]] = Field(default=None, description="""Measured data quality metrics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    data_provenance: Optional[str] = Field(default=None, description="""Provenance information for the data resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.7.5'}},
         'domain_of': ['DataResource']} })
    labelling_process: Optional[str] = Field(default=None, description="""Description of the data labelling process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    data_preparation_methods: Optional[list[DataPreparationMethod]] = Field(default=None, description="""Data preparation methods used (e.g., scaling, encoding, cleaning) per Annex A.7.6.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.7.6'}},
         'domain_of': ['DataResource']} })
    last_updated_date: Optional[date] = Field(default=None, description="""Date the data was last updated or modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    known_bias_issues: Optional[list[str]] = Field(default=None, description="""Known or potential bias issues in the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    retention_policy: Optional[str] = Field(default=None, description="""Retention and disposal policy applicable to the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    data_classification: Optional[str] = Field(default=None, description="""Classification of the data resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataResource']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ToolingResource(NamedEntity):
    """
    A tooling resource (algorithm, framework, model, library) used in an AI system per A.4.4.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.4'}},
         'comments': ['Algorithm, framework, model, or library used by the AI system '
                      'per Annex A.4.4',
                      'Track vendor, version, and license terms to support third-party '
                      'assurance'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_data_management', 'ai_system_lifecycle'],
         'narrow_mappings': ['iso27001:Asset']})

    tool_category: Optional[str] = Field(default=None, description="""Category of tooling resource (algorithm, framework, model, library).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolingResource']} })
    tool_version: Optional[str] = Field(default=None, description="""Version identifier for the tooling resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolingResource']} })
    vendor: Optional[str] = Field(default=None, description="""Vendor or origin of the tooling resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolingResource']} })
    license_terms: Optional[str] = Field(default=None, description="""License terms applicable to the tooling resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolingResource']} })
    usage_purpose: Optional[str] = Field(default=None, description="""Purpose for which the tooling resource is used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ToolingResource']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ComputingResource(NamedEntity):
    """
    A system or computing resource used in the development or operation of an AI system per A.4.5.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.5'}},
         'comments': ['System and computing resource per Annex A.4.5',
                      'Examples include GPU clusters, edge devices, cloud regions, and '
                      'on-prem environments'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_system_lifecycle'],
         'narrow_mappings': ['iso27001:Asset']})

    resource_class: Optional[str] = Field(default=None, description="""Class of computing resource (e.g., GPU cluster, edge device).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource']} })
    quantity: Optional[str] = Field(default=None, description="""Quantity of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource', 'Resource']} })
    location: Optional[str] = Field(default=None, description="""Physical or logical location of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource']} })
    environment_type: Optional[str] = Field(default=None, description="""Type of environment (development, staging, production).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource']} })
    cost: Optional[str] = Field(default=None, description="""Cost of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource', 'Resource']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class HumanResource(NamedEntity):
    """
    A human resource (role, expertise area) involved in development, deployment, operation, maintenance, or oversight of an AI system per A.4.6.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4.6'}},
         'comments': ['Human-resource record per Annex A.4.6 covering competences and '
                      'lifecycle responsibilities',
                      'Supports Clause 7.2 competence determination'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['ai_system_lifecycle'],
         'narrow_mappings': ['iso27001:Asset']})

    required_competencies: Optional[list[str]] = Field(default=None, description="""Competencies required for the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanResource', 'CompetenceRecord']} })
    assigned_to: Optional[list[str]] = Field(default=None, description="""Person(s) assigned to this role or resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'HumanResource']} })
    lifecycle_responsibilities: Optional[list[str]] = Field(default=None, description="""Life cycle responsibilities allocated to this human resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanResource']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Resource(NamedEntity):
    """
    A resource provided for the AIMS per Clause 7.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.4'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.1'}},
         'comments': ['Generic AIMS resource record per Clause 7.1',
                      'Use specialized DataResource / ToolingResource / '
                      'ComputingResource / HumanResource where applicable'],
         'exact_mappings': ['iso27001:Resource'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    resource_type: Optional[str] = Field(default=None, description="""Type of resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource'],
         'examples': [{'value': 'personnel'},
                      {'value': 'technology'},
                      {'value': 'budget'},
                      {'value': 'infrastructure'},
                      {'value': 'data'},
                      {'value': 'tooling'}]} })
    quantity: Optional[str] = Field(default=None, description="""Quantity of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource', 'Resource']} })
    allocation_date: Optional[date] = Field(default=None, description="""Date the resource was allocated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    allocated_to: Optional[str] = Field(default=None, description="""What the resource is allocated to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    cost: Optional[str] = Field(default=None, description="""Cost of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputingResource', 'Resource']} })
    availability_status: Optional[str] = Field(default=None, description="""Current availability of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CompetenceRecord(DocumentedInformation):
    """
    Evidence of competence for personnel affecting AIMS performance per Clause 7.2.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.2'}},
         'comments': ['Evidence of competence per Clause 7.2',
                      'Captures education, training, experience, and identified '
                      'competency gaps'],
         'exact_mappings': ['iso27001:CompetenceRecord'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'documented_information']})

    person_name: Optional[str] = Field(default=None, description="""Name of the person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    person_role: Optional[str] = Field(default=None, description="""Role of the person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    required_competencies: Optional[list[str]] = Field(default=None, description="""Competencies required for the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanResource', 'CompetenceRecord']} })
    education_records: Optional[list[str]] = Field(default=None, description="""Education qualifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    training_records: Optional[list[str]] = Field(default=None, description="""Training completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    experience_records: Optional[list[str]] = Field(default=None, description="""Relevant experience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    competency_assessment_date: Optional[date] = Field(default=None, description="""Date of last competency assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    competency_gaps: Optional[list[str]] = Field(default=None, description="""Identified competency gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    development_actions: Optional[list[str]] = Field(default=None, description="""Actions to address competency gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompetenceRecord']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AwarenessProgram(DocumentedInformation):
    """
    The awareness program ensuring personnel understand their AI-related responsibilities per Clause 7.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.3'}},
         'comments': ['Personnel awareness of AI policy and AIMS contributions per '
                      'Clause 7.3',
                      'Tracks topics, audiences, frequency, and effectiveness '
                      'measures'],
         'exact_mappings': ['iso27001:AwarenessProgram'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    awareness_topics: Optional[list[str]] = Field(default=None, description="""Topics covered in the awareness program.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    delivery_methods: Optional[list[str]] = Field(default=None, description="""Methods used to deliver awareness content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    target_audience: Optional[str] = Field(default=None, description="""Intended audience for the policy or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TopicSpecificPolicy', 'AwarenessProgram']} })
    frequency: Optional[str] = Field(default=None, description="""Frequency of the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram', 'CommunicationItem']} })
    completion_tracking: Optional[str] = Field(default=None, description="""How completion is tracked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    effectiveness_measures: Optional[str] = Field(default=None, description="""How effectiveness is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CommunicationPlan(DocumentedInformation):
    """
    Plan for internal and external communications relevant to the AIMS per Clause 7.4.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.4'}},
         'comments': ['Internal and external communication plan per Clause 7.4',
                      'Aggregates individual CommunicationItem records'],
         'exact_mappings': ['iso27001:CommunicationPlan'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'documented_information']})

    communication_items: Optional[list[CommunicationItem]] = Field(default=None, description="""Communication items in the plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationPlan']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CommunicationItem(ConfiguredBaseModel):
    """
    A single communication requirement within the AIMS communication plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.4'}},
         'comments': ['One row of the communication plan per Clause 7.4',
                      'Captures what, when, with whom, and how to communicate'],
         'exact_mappings': ['iso27001:CommunicationItem'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    subject: Optional[str] = Field(default=None, description="""Subject of the communication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    purpose: Optional[str] = Field(default=None, description="""Purpose of the communication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    audience: Optional[str] = Field(default=None, description="""Target audience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    frequency: Optional[str] = Field(default=None, description="""Frequency of the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AwarenessProgram', 'CommunicationItem']} })
    method: Optional[str] = Field(default=None, description="""Method of communication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    records_required: Optional[str] = Field(default=None, description="""Records required to evidence the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem']} })


class OperationalProcedure(DocumentedInformation):
    """
    A documented procedure for operational planning and control of AIMS processes per Clause 8.1, including AI system life cycle related controls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.1'}},
         'comments': ['Operational planning and control per Clause 8.1',
                      'Should cover AI life-cycle controls implemented via 6.1.3'],
         'exact_mappings': ['iso27001:OperationalProcedure'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['documented_information'],
         'related_mappings': ['iso29100:PIIProcessingActivity']})

    procedure_scope: Optional[str] = Field(default=None, description="""Scope of the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    process_criteria: Optional[str] = Field(default=None, description="""Criteria for the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    control_measures: Optional[list[str]] = Field(default=None, description="""Control measures applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    responsible_roles: Optional[list[str]] = Field(default=None, description="""Roles responsible for the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Other reference controls related to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'AIReferenceControl', 'OperationalProcedure']} })
    change_control_requirements: Optional[str] = Field(default=None, description="""Requirements for controlling changes to the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalProcedure']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class MonitoringProgram(DocumentedInformation):
    """
    The program for monitoring, measurement, analysis, and evaluation of AIMS performance per Clause 9.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.1'}},
         'comments': ['Defines what is monitored, how, and how often per Clause 9.1',
                      'Aggregates individual MonitoringItem records'],
         'exact_mappings': ['iso27001:MonitoringProgram'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    monitoring_items: Optional[list[MonitoringItem]] = Field(default=None, description="""Items to be monitored.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringProgram']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class MonitoringItem(ConfiguredBaseModel):
    """
    A single item to be monitored and measured per Clause 9.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.1'}},
         'comments': ['One metric monitored under Clause 9.1',
                      'Thresholds and trends support performance evaluation and '
                      'improvement triggers'],
         'exact_mappings': ['iso27001:MonitoringItem'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation']})

    metric_name: Optional[str] = Field(default=None, description="""Name of the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    metric_description: Optional[str] = Field(default=None, description="""Description of the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used to measure the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'MonitoringItem']} })
    measurement_frequency: Optional[str] = Field(default=None, description="""How often measurement is performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'MonitoringItem']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    analysis_frequency: Optional[str] = Field(default=None, description="""Frequency of analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    analyst: Optional[str] = Field(default=None, description="""Person performing the analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    target_threshold: Optional[str] = Field(default=None, description="""Target threshold for the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    alert_threshold: Optional[str] = Field(default=None, description="""Threshold that triggers an alert.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })
    current_value: Optional[str] = Field(default=None, description="""Current measured value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'MonitoringItem']} })
    trend: Optional[str] = Field(default=None, description="""Observed trend in the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonitoringItem']} })


class InternalAudit(DocumentedInformation):
    """
    An internal audit instance per Clause 9.2 assessing AIMS conformance and effectiveness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.2'}},
         'comments': ['Internal audit instance per Clause 9.2',
                      'Audit type aligned with ISO 19011 (first-, second-, '
                      'third-party, surveillance, recertification)'],
         'exact_mappings': ['iso27001:InternalAudit'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    audit_reference: Optional[str] = Field(default=None, description="""Unique reference identifier for the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_type: Optional[AuditType] = Field(default=None, description="""Type of audit (internal, external second-party, external third-party, surveillance, recertification, combined).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_scope: Optional[str] = Field(default=None, description="""Scope of the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_criteria: Optional[str] = Field(default=None, description="""Criteria used for the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_objectives: Optional[str] = Field(default=None, description="""Objectives of the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_period_start: Optional[date] = Field(default=None, description="""Start date of the audit period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_period_end: Optional[date] = Field(default=None, description="""End date of the audit period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    lead_auditor: Optional[str] = Field(default=None, description="""Lead auditor for the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_team: Optional[list[str]] = Field(default=None, description="""Members of the audit team.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    auditee_representatives: Optional[list[str]] = Field(default=None, description="""Representatives of the auditee.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_plan: Optional[str] = Field(default=None, description="""Reference to the audit plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    findings: Optional[list[str]] = Field(default=None, description="""Findings from the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    positive_observations: Optional[list[str]] = Field(default=None, description="""Positive observations from the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    audit_conclusion: Optional[str] = Field(default=None, description="""Overall conclusion of the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    report_date: Optional[date] = Field(default=None, description="""Date the audit report was issued.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    report_distribution: Optional[list[str]] = Field(default=None, description="""Distribution list for the audit report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InternalAudit']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AuditProgramme(DocumentedInformation):
    """
    The internal audit programme per Clause 9.2.2, planning AIMS audit activities over a defined period.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.2.2'}},
         'comments': ['Audit programme per Clause 9.2.2',
                      'Frequency rationale should reflect process importance and prior '
                      'audit results'],
         'exact_mappings': ['iso27001:AuditProgramme'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    programme_period: Optional[str] = Field(default=None, description="""Period covered by the audit programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    planned_audits: Optional[list[str]] = Field(default=None, description="""Audits planned within the programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    audit_frequency_rationale: Optional[str] = Field(default=None, description="""Rationale for the audit cadence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    resource_requirements: Optional[str] = Field(default=None, description="""Resources required for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    auditor_qualifications: Optional[str] = Field(default=None, description="""Required auditor qualifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    programme_status: Optional[str] = Field(default=None, description="""Status of the audit programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditProgramme']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AuditFinding(NamedEntity):
    """
    A finding from an AIMS internal audit, including nonconformities, observations, and positive findings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.2'}},
         'comments': ['Finding from an internal audit per Clause 9.2',
                      'Findings may be major or minor nonconformities, observations, '
                      'or positive findings'],
         'exact_mappings': ['iso27001:AuditFinding'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation']})

    finding_type: Optional[AuditFindingType] = Field(default=None, description="""Type of audit finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 42001 clause referenced by the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    control_reference: Optional[str] = Field(default=None, description="""Reference to an Annex A control (e.g., A.6.2.4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoAEntry', 'AuditFinding']} })
    finding_description: Optional[str] = Field(default=None, description="""Description of the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    objective_evidence: Optional[str] = Field(default=None, description="""Objective evidence supporting the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    root_cause_analysis: Optional[str] = Field(default=None, description="""Analysis of the root cause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    risk_implication: Optional[str] = Field(default=None, description="""AI risk implication of the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    recommended_action: Optional[str] = Field(default=None, description="""Recommended action to address the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    auditee_response: Optional[str] = Field(default=None, description="""Auditee's response to the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    linked_corrective_action: Optional[str] = Field(default=None, description="""Linked corrective action addressing the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    closure_status: Optional[str] = Field(default=None, description="""Closure status of the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding']} })
    closure_date: Optional[date] = Field(default=None, description="""Date when the item was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding', 'Nonconformity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ManagementReview(DocumentedInformation):
    """
    A management review per Clause 9.3, conducted by top management to evaluate ongoing AIMS suitability, adequacy, and effectiveness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.3'}},
         'comments': ['Top-management review per Clause 9.3 to ensure ongoing '
                      'suitability, adequacy, effectiveness',
                      'Required inputs include nonconformities, monitoring, audits, '
                      'and interested-party changes'],
         'exact_mappings': ['iso27001:ManagementReview'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation', 'documented_information']})

    review_date: Optional[date] = Field(default=None, description="""Date when the document is due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'ManagementReview']} })
    attendees: Optional[list[str]] = Field(default=None, description="""Attendees of the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    previous_actions_status: Optional[str] = Field(default=None, description="""Status of actions from previous reviews.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    context_changes: Optional[list[str]] = Field(default=None, description="""Changes in external or internal context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    interested_party_changes: Optional[list[str]] = Field(default=None, description="""Changes in interested party needs and expectations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    performance_trends: Optional[str] = Field(default=None, description="""Trends in AIMS performance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    audit_results_summary: Optional[str] = Field(default=None, description="""Summary of audit results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    risk_assessment_results: Optional[str] = Field(default=None, description="""Summary of AI risk assessment results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    impact_assessment_results: Optional[str] = Field(default=None, description="""Summary of AI system impact assessment results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    improvement_opportunities: Optional[list[str]] = Field(default=None, description="""Improvement opportunities identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    decisions: Optional[list[str]] = Field(default=None, description="""Decisions made during the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    action_items: Optional[list[str]] = Field(default=None, description="""Action items resulting from the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    next_review_date: Optional[date] = Field(default=None, description="""Date of the next review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManagementReview']} })
    document_type: Optional[DocumentType] = Field(default=None, description="""Classification of the documented information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'in_subset': ['documented_information']} })
    document_reference: Optional[str] = Field(default=None, description="""Unique reference number for document control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'AIMS-POL-001'}, {'value': 'AISIA-2025-003'}]} })
    author: Optional[str] = Field(default=None, description="""Person who created the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    owner: Optional[str] = Field(default=None, description="""Person accountable for the document content and maintenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    approved_by: Optional[str] = Field(default=None, description="""Person who approved the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'StatementOfApplicability']} })
    approved_date: Optional[date] = Field(default=None, description="""Date when the document was approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation', 'AIRiskTreatmentPlan']} })
    effective_date: Optional[date] = Field(default=None, description="""Date when the document becomes effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    classification: Optional[str] = Field(default=None, description="""Information classification level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentedInformation'],
         'examples': [{'value': 'confidential'},
                      {'value': 'internal'},
                      {'value': 'public'}]} })
    retention_period: Optional[str] = Field(default=None, description="""Duration for which the document is retained.""", json_schema_extra = { "linkml_meta": {'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['DocumentedInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class Nonconformity(NamedEntity):
    """
    A nonconformity identified per Clause 10.2 representing failure to fulfill an AIMS requirement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.2'}},
         'comments': ['Nonconformity per Clause 10.2; triggers corrective-action '
                      'workflow',
                      'Equivalent in structure to ISO/IEC 27001:2022 Nonconformity'],
         'exact_mappings': ['iso27001:Nonconformity'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['continual_improvement']})

    nonconformity_source: Optional[str] = Field(default=None, description="""Source from which the nonconformity was identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    detection_date: Optional[date] = Field(default=None, description="""Date the nonconformity was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    detected_by: Optional[str] = Field(default=None, description="""Person or process that detected the nonconformity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    requirement_violated: Optional[str] = Field(default=None, description="""Requirement that was violated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    nonconformity_description: Optional[str] = Field(default=None, description="""Description of the nonconformity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    immediate_actions: Optional[list[str]] = Field(default=None, description="""Immediate actions taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    consequences_addressed: Optional[str] = Field(default=None, description="""How consequences were addressed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    root_cause: Optional[str] = Field(default=None, description="""Identified root cause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity', 'AIIncident']} })
    similar_nonconformities_check: Optional[str] = Field(default=None, description="""Check for similar nonconformities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    linked_corrective_actions: Optional[list[str]] = Field(default=None, description="""Linked corrective actions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity', 'AIIncident']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    closure_date: Optional[date] = Field(default=None, description="""Date when the item was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditFinding', 'Nonconformity']} })
    closure_evidence: Optional[str] = Field(default=None, description="""Evidence of closure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CorrectiveAction(NamedEntity):
    """
    A corrective action per Clause 10.2 to address the root cause of an AIMS nonconformity and reduce the likelihood of recurrence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.2'}},
         'close_mappings': ['nist_ai_600_1:SuggestedAction'],
         'comments': ['Corrective action per Clause 10.2 addressing the root cause of '
                      'a nonconformity',
                      'Effectiveness must be reviewed and any required AIMS changes '
                      'recorded'],
         'exact_mappings': ['iso27001:CorrectiveAction'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['continual_improvement']})

    linked_nonconformity: Optional[str] = Field(default=None, description="""Linked nonconformity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    action_description: Optional[str] = Field(default=None, description="""Description of the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    root_cause_addressed: Optional[str] = Field(default=None, description="""Root cause addressed by the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    target_completion_date: Optional[date] = Field(default=None, description="""Target completion date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    actual_completion_date: Optional[date] = Field(default=None, description="""Actual completion date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction', 'ImprovementOpportunity']} })
    resources_required: Optional[str] = Field(default=None, description="""Resources required for implementation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'AIRiskTreatmentPlan', 'CorrectiveAction']} })
    effectiveness_criteria: Optional[str] = Field(default=None, description="""Criteria for assessing effectiveness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    effectiveness_review_date: Optional[date] = Field(default=None, description="""Date when effectiveness was reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    effectiveness_verified: Optional[bool] = Field(default=None, description="""Whether effectiveness was verified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction']} })
    aims_changes_required: Optional[bool] = Field(default=None, description="""Whether AIMS changes are required as a result of the action.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:isms_changes_required'],
         'domain_of': ['CorrectiveAction']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ImprovementOpportunity(NamedEntity):
    """
    An opportunity for continual improvement of the AIMS per Clause 10.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.1'}},
         'comments': ['Continual improvement opportunity per Clause 10.1',
                      'May originate from audit, review, monitoring, or '
                      'interested-party feedback'],
         'exact_mappings': ['iso27001:ImprovementOpportunity'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['continual_improvement']})

    improvement_source: Optional[str] = Field(default=None, description="""Source of the improvement opportunity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    identification_date: Optional[date] = Field(default=None, description="""Date the improvement opportunity was identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    identified_by: Optional[str] = Field(default=None, description="""Person who identified the improvement opportunity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    improvement_description: Optional[str] = Field(default=None, description="""Description of the improvement opportunity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    expected_benefit: Optional[str] = Field(default=None, description="""Expected benefit of the improvement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    priority: Optional[RiskLevel] = Field(default=None, description="""Priority assigned (qualitative level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    implementation_plan: Optional[str] = Field(default=None, description="""Plan for implementing the improvement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    responsible_party: Optional[str] = Field(default=None, description="""Party responsible for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommunicationItem',
                       'MonitoringItem',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    target_date: Optional[date] = Field(default=None, description="""Target date for achieving the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIObjective', 'ImprovementOpportunity']} })
    actual_completion_date: Optional[date] = Field(default=None, description="""Actual completion date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrectiveAction', 'ImprovementOpportunity']} })
    outcome_assessment: Optional[str] = Field(default=None, description="""Assessment of the outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImprovementOpportunity']} })
    status: Optional[str] = Field(default=None, description="""Current status of the document or entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples include draft, approved, active, superseded, archived'],
         'domain_of': ['DocumentedInformation',
                       'Nonconformity',
                       'CorrectiveAction',
                       'ImprovementOpportunity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ThirdPartyRelationship(NamedEntity):
    """
    A documented relationship with a third party (supplier, partner, or customer) involved in the AI system life cycle per A.10.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10'}},
         'comments': ['Documented relationship per Annex A.10 capturing responsibility '
                      'allocation',
                      'Specialized into SupplierRelationship and CustomerRelationship'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['third_party_management'],
         'related_mappings': ['iso27001:InterestedParty']})

    party_type: Optional[str] = Field(default=None, description="""Category of party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty', 'ThirdPartyRelationship'],
         'examples': [{'value': 'internal'},
                      {'value': 'external'},
                      {'value': 'regulatory'},
                      {'value': 'ai_subject'},
                      {'value': 'supplier'},
                      {'value': 'customer'}]} })
    party_name: Optional[str] = Field(default=None, description="""Name of the third party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    contractual_basis: Optional[str] = Field(default=None, description="""Contractual basis of the relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    allocated_responsibilities: Optional[list[str]] = Field(default=None, description="""Responsibilities allocated to the third party.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.2'}},
         'domain_of': ['ThirdPartyRelationship']} })
    data_processing_role: Optional[str] = Field(default=None, description="""Role of the third party in data processing (e.g., PII controller, PII processor).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    ai_systems_involved: Optional[list[str]] = Field(default=None, description="""AI systems involved in the third-party relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    lifecycle_stages_involved: Optional[list[AISystemLifecycleStage]] = Field(default=None, description="""AI life cycle stages where the third party is involved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    assurance_evidence: Optional[list[str]] = Field(default=None, description="""Evidence of assurance over the third party's conformance with the organization's responsible AI approach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    review_frequency: Optional[str] = Field(default=None, description="""Frequency at which the relationship is reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class SupplierRelationship(ThirdPartyRelationship):
    """
    A supplier relationship covering services, products, or materials (e.g., datasets, models, libraries, full AI systems) provided to the organization per A.10.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.3'}},
         'comments': ['Supplier relationship per Annex A.10.3',
                      'Includes assessment criteria, monitoring method, and corrective '
                      'actions required'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['third_party_management'],
         'related_mappings': ['iso27001:InterestedParty']})

    supplier_assessment_criteria: Optional[list[str]] = Field(default=None, description="""Criteria for assessing the supplier.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.3'}},
         'domain_of': ['SupplierRelationship']} })
    monitoring_method: Optional[str] = Field(default=None, description="""How the supplier or customer relationship is monitored.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SupplierRelationship']} })
    corrective_actions_required: Optional[list[str]] = Field(default=None, description="""Corrective actions required of the supplier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SupplierRelationship']} })
    party_type: Optional[str] = Field(default=None, description="""Category of party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty', 'ThirdPartyRelationship'],
         'examples': [{'value': 'internal'},
                      {'value': 'external'},
                      {'value': 'regulatory'},
                      {'value': 'ai_subject'},
                      {'value': 'supplier'},
                      {'value': 'customer'}]} })
    party_name: Optional[str] = Field(default=None, description="""Name of the third party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    contractual_basis: Optional[str] = Field(default=None, description="""Contractual basis of the relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    allocated_responsibilities: Optional[list[str]] = Field(default=None, description="""Responsibilities allocated to the third party.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.2'}},
         'domain_of': ['ThirdPartyRelationship']} })
    data_processing_role: Optional[str] = Field(default=None, description="""Role of the third party in data processing (e.g., PII controller, PII processor).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    ai_systems_involved: Optional[list[str]] = Field(default=None, description="""AI systems involved in the third-party relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    lifecycle_stages_involved: Optional[list[AISystemLifecycleStage]] = Field(default=None, description="""AI life cycle stages where the third party is involved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    assurance_evidence: Optional[list[str]] = Field(default=None, description="""Evidence of assurance over the third party's conformance with the organization's responsible AI approach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    review_frequency: Optional[str] = Field(default=None, description="""Frequency at which the relationship is reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class CustomerRelationship(ThirdPartyRelationship):
    """
    A customer relationship for an AI product or service supplied by the organization per A.10.4.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.4'}},
         'comments': ['Customer relationship per Annex A.10.4',
                      'Captures customer expectations and communicated AI system '
                      'limitations'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['third_party_management'],
         'related_mappings': ['iso27001:InterestedParty']})

    customer_expectations: Optional[list[str]] = Field(default=None, description="""Documented customer expectations and needs.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.4'}},
         'domain_of': ['CustomerRelationship']} })
    usage_agreement_reference: Optional[str] = Field(default=None, description="""Reference to the usage agreement with the customer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CustomerRelationship']} })
    communicated_limitations: Optional[list[str]] = Field(default=None, description="""Limitations of the AI system that are communicated to the customer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CustomerRelationship']} })
    party_type: Optional[str] = Field(default=None, description="""Category of party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InterestedParty', 'ThirdPartyRelationship'],
         'examples': [{'value': 'internal'},
                      {'value': 'external'},
                      {'value': 'regulatory'},
                      {'value': 'ai_subject'},
                      {'value': 'supplier'},
                      {'value': 'customer'}]} })
    party_name: Optional[str] = Field(default=None, description="""Name of the third party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    contractual_basis: Optional[str] = Field(default=None, description="""Contractual basis of the relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    allocated_responsibilities: Optional[list[str]] = Field(default=None, description="""Responsibilities allocated to the third party.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.10.2'}},
         'domain_of': ['ThirdPartyRelationship']} })
    data_processing_role: Optional[str] = Field(default=None, description="""Role of the third party in data processing (e.g., PII controller, PII processor).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    ai_systems_involved: Optional[list[str]] = Field(default=None, description="""AI systems involved in the third-party relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    lifecycle_stages_involved: Optional[list[AISystemLifecycleStage]] = Field(default=None, description="""AI life cycle stages where the third party is involved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    assurance_evidence: Optional[list[str]] = Field(default=None, description="""Evidence of assurance over the third party's conformance with the organization's responsible AI approach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    review_frequency: Optional[str] = Field(default=None, description="""Frequency at which the relationship is reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdPartyRelationship']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AISystemEvent(NamedEntity):
    """
    An AI system event detected by monitoring, users, or external reporting channels. Events may or may not be subsequently classified as incidents. Supports A.6.2.8 event log capture and A.8.3 external reporting workflows.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.6.2.8, A.8.3'}},
         'close_mappings': ['iso27001:InformationSecurityEvent'],
         'comments': ['First-class entity allowing event records to attach to A.6.2.8 '
                      'logs and A.8.3 reports',
                      'Reference: ISO/IEC 42001:2023 Annex A controls A.6.2.8, A.8.3. '
                      'ISO/IEC standards text is copyright ISO/IEC - not reproduced '
                      'here.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation', 'annex_a_controls']})

    event_datetime: Optional[datetime ] = Field(default=None, description="""Date and time the event was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent']} })
    reporter: Optional[str] = Field(default=None, description="""Identifier or description of the person or system that reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent', 'ConcernReport']} })
    reporter_party_type: Optional[str] = Field(default=None, description="""Type of party that reported the event (internal user, external interested party, monitoring system, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent', 'ConcernReport']} })
    event_source: Optional[str] = Field(default=None, description="""Source channel through which the event was raised (monitoring, user report, external report, audit).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent']} })
    event_description: Optional[str] = Field(default=None, description="""Free-text description of the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent']} })
    affected_ai_systems: Optional[list[str]] = Field(default=None, description="""AI systems affected by this risk.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:affected_assets'],
         'domain_of': ['AIRisk', 'AISystemEvent', 'AIIncident'],
         'related_mappings': ['nist_ai_600_1:risk_scope']} })
    initial_assessment: Optional[str] = Field(default=None, description="""Initial triage assessment of the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent']} })
    categorized_as_incident: Optional[bool] = Field(default=None, description="""Whether the event has been categorized as an incident requiring response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent']} })
    linked_incident: Optional[str] = Field(default=None, description="""AI incident linked to the originating event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class AIIncident(NamedEntity):
    """
    An AI incident, i.e., an AI system event determined to require response, escalation, or external communication. Captures triage, response lifecycle, and communications to users and other interested parties per A.8.4 and A.8.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.8.3, A.8.4'}},
         'close_mappings': ['iso27001:InformationSecurityIncident',
                            'iso29100:PrivacyBreach',
                            'nist_ai_100_1:Harm',
                            'nist_ai_600_1:GaiRisk'],
         'comments': ['Provides the entity to which A.8.4 communication plans and '
                      'A.8.3 external reports attach',
                      'AI-specific categories (data poisoning, model stealing, prompt '
                      'injection, etc.) supplement classical infosec incident classes',
                      'Reference: ISO/IEC 42001:2023 Annex A controls A.8.3, A.8.4. '
                      'ISO/IEC standards text is copyright ISO/IEC - not reproduced '
                      'here.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['performance_evaluation',
                       'annex_a_controls',
                       'continual_improvement']})

    incident_datetime: Optional[datetime ] = Field(default=None, description="""Date and time the incident was declared or detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    incident_category: Optional[AIIncidentCategory] = Field(default=None, description="""AI-specific category of the incident.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.8.4'}},
         'domain_of': ['AIIncident']} })
    severity: Optional[RiskLevel] = Field(default=None, description="""Severity rating of the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident', 'ConcernReport']} })
    affected_ai_systems: Optional[list[str]] = Field(default=None, description="""AI systems affected by this risk.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:affected_assets'],
         'domain_of': ['AIRisk', 'AISystemEvent', 'AIIncident'],
         'related_mappings': ['nist_ai_600_1:risk_scope']} })
    affected_dimensions: Optional[list[ImpactAssessmentDimension]] = Field(default=None, description="""Dimensions of impact affected by the risk (individual, group, societal, safety, privacy, security, environmental).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIRisk', 'AIIncident']} })
    incident_description: Optional[str] = Field(default=None, description="""Free-text description of the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    detection_method: Optional[str] = Field(default=None, description="""How the incident was detected (monitoring alert, user report, external report).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    response_actions: Optional[list[str]] = Field(default=None, description="""Response actions taken for the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    containment_actions: Optional[list[str]] = Field(default=None, description="""Containment actions taken to limit incident impact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    recovery_actions: Optional[list[str]] = Field(default=None, description="""Recovery actions taken to restore normal AI system operation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    root_cause: Optional[str] = Field(default=None, description="""Identified root cause.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity', 'AIIncident']} })
    lessons_learned: Optional[list[str]] = Field(default=None, description="""Lessons learned recorded after incident closure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    evidence_collected: Optional[list[str]] = Field(default=None, description="""References to evidence collected during incident response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    notification_required: Optional[bool] = Field(default=None, description="""Whether notification to interested parties or authorities is required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    notifications_made: Optional[list[str]] = Field(default=None, description="""Notifications actually made (user communications, regulator filings).""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.8.4'}},
         'domain_of': ['AIIncident']} })
    external_reports: Optional[list[str]] = Field(default=None, description="""External reports received or filed regarding the incident.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.8.3'}},
         'domain_of': ['AIIncident']} })
    communication_plan: Optional[str] = Field(default=None, description="""Reference to the communication plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIManagementSystem', 'AIIncident'],
         'exact_mappings': ['iso27001:communication_plan']} })
    linked_corrective_actions: Optional[list[str]] = Field(default=None, description="""Linked corrective actions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Nonconformity', 'AIIncident']} })
    closure_datetime: Optional[datetime ] = Field(default=None, description="""Date and time the incident was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident', 'ConcernReport']} })
    post_incident_review: Optional[str] = Field(default=None, description="""Reference to the post-incident review record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


class ConcernReport(NamedEntity):
    """
    A concern raised by employees, contractors, users, or other interested parties about the organization's role with respect to an AI system. Operationalises Annex A.3.3 (Reporting of concerns). Confidentiality, anonymity, anti-reprisal protection, escalation, and timely response are core attributes; informed by ISO 37002.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_reference': {'tag': 'annex_a_reference',
                                               'value': 'A.3.3'}},
         'comments': ['First-class entity supporting A.3.3 concern-reporting workflows '
                      'distinct from AIIncident',
                      'Anonymity and anti-reprisal protections are required even when '
                      'reporter identity is captured',
                      'Reference: ISO/IEC 42001:2023 Annex A.3.3 (paraphrased); '
                      'related guidance ISO 37002. ISO standards text is copyright '
                      'ISO/IEC - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['annex_a_controls', 'performance_evaluation'],
         'related_mappings': ['iso27001:Nonconformity',
                              'nist_ai_100_1:Harm',
                              'nist_ai_600_1:StructuredPublicFeedback']})

    reported_date: Optional[date] = Field(default=None, description="""Date the concern was reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    reporter: Optional[str] = Field(default=None, description="""Identifier or description of the person or system that reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent', 'ConcernReport']} })
    reporter_party_type: Optional[str] = Field(default=None, description="""Type of party that reported the event (internal user, external interested party, monitoring system, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystemEvent', 'ConcernReport']} })
    reporter_anonymous: Optional[bool] = Field(default=None, description="""Whether the reporter chose to remain anonymous.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    confidentiality_level: Optional[str] = Field(default=None, description="""Confidentiality classification applied to the concern record (e.g., confidential, restricted, internal).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    reporting_channel: Optional[str] = Field(default=None, description="""Channel through which the concern was reported (e.g., hotline, web form, manager, ombudsperson, external auditor).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    concern_description: Optional[str] = Field(default=None, description="""Paraphrased summary of the concern raised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    concern_ai_systems: Optional[list[str]] = Field(default=None, description="""AI systems referenced in the concern report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    concern_lifecycle_stage: Optional[list[AISystemLifecycleStage]] = Field(default=None, description="""AI system life cycle stage(s) at which the concern arose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    severity: Optional[RiskLevel] = Field(default=None, description="""Severity rating of the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident', 'ConcernReport']} })
    investigator: Optional[str] = Field(default=None, description="""Identifier or description of the investigator assigned to the concern.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    investigation_status: Optional[str] = Field(default=None, description="""Status of the investigation (e.g., opened, in_progress, closed, escalated, referred_external).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    investigation_findings: Optional[str] = Field(default=None, description="""Paraphrased summary of investigation findings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    escalation_status: Optional[str] = Field(default=None, description="""Whether and how the concern was escalated (internal management, governing body, external authority).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    response_due_date: Optional[date] = Field(default=None, description="""Target date by which a response is owed to the reporter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    response_provided_date: Optional[date] = Field(default=None, description="""Date a response was provided to the reporter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    resolution: Optional[str] = Field(default=None, description="""Paraphrased description of the resolution provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    reprisal_protection_actions: Optional[list[str]] = Field(default=None, description="""Actions taken to protect the reporter from reprisals or detriment (informed by ISO 37002).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    related_incidents: Optional[list[str]] = Field(default=None, description="""AI incidents linked to this concern report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    related_nonconformities: Optional[list[str]] = Field(default=None, description="""Nonconformities linked to this concern report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConcernReport']} })
    closure_datetime: Optional[datetime ] = Field(default=None, description="""Date and time the incident was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIIncident', 'ConcernReport']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:id'],
         'examples': [{'value': 'iso42001:ai-risk-001'},
                      {'value': 'iso42001:control-A.6.2.4'}]} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:name']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'exact_mappings': ['iso27001:description']} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    version: Optional[str] = Field(default=None, description="""Version identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['iso27001:version'],
         'examples': [{'value': '1.0'}, {'value': '2.3.1'}]} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
DocumentedInformation.model_rebuild()
AIManagementSystem.model_rebuild()
Organization.model_rebuild()
InterestedParty.model_rebuild()
AIPolicy.model_rebuild()
TopicSpecificPolicy.model_rebuild()
Role.model_rebuild()
AIObjective.model_rebuild()
AIRiskAssessmentProcess.model_rebuild()
AIRiskAssessment.model_rebuild()
AIRisk.model_rebuild()
AIRiskTreatmentProcess.model_rebuild()
AIRiskTreatmentPlan.model_rebuild()
AISystemImpactAssessmentProcess.model_rebuild()
AISystemImpactAssessment.model_rebuild()
StatementOfApplicability.model_rebuild()
SoAEntry.model_rebuild()
AIReferenceControl.model_rebuild()
AISystem.model_rebuild()
DataResource.model_rebuild()
ToolingResource.model_rebuild()
ComputingResource.model_rebuild()
HumanResource.model_rebuild()
Resource.model_rebuild()
CompetenceRecord.model_rebuild()
AwarenessProgram.model_rebuild()
CommunicationPlan.model_rebuild()
CommunicationItem.model_rebuild()
OperationalProcedure.model_rebuild()
MonitoringProgram.model_rebuild()
MonitoringItem.model_rebuild()
InternalAudit.model_rebuild()
AuditProgramme.model_rebuild()
AuditFinding.model_rebuild()
ManagementReview.model_rebuild()
Nonconformity.model_rebuild()
CorrectiveAction.model_rebuild()
ImprovementOpportunity.model_rebuild()
ThirdPartyRelationship.model_rebuild()
SupplierRelationship.model_rebuild()
CustomerRelationship.model_rebuild()
AISystemEvent.model_rebuild()
AIIncident.model_rebuild()
ConcernReport.model_rebuild()
