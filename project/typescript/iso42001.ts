export type NamedEntityId = string;
export type DocumentedInformationId = string;
export type AIManagementSystemId = string;
export type OrganizationId = string;
export type InterestedPartyId = string;
export type AIPolicyId = string;
export type TopicSpecificPolicyId = string;
export type RoleId = string;
export type AIObjectiveId = string;
export type AIRiskAssessmentProcessId = string;
export type AIRiskAssessmentId = string;
export type AIRiskId = string;
export type AIRiskTreatmentProcessId = string;
export type AIRiskTreatmentPlanId = string;
export type AISystemImpactAssessmentProcessId = string;
export type AISystemImpactAssessmentId = string;
export type StatementOfApplicabilityId = string;
export type AIReferenceControlId = string;
export type AISystemId = string;
export type DataResourceId = string;
export type ToolingResourceId = string;
export type ComputingResourceId = string;
export type HumanResourceId = string;
export type ResourceId = string;
export type CompetenceRecordId = string;
export type AwarenessProgramId = string;
export type CommunicationPlanId = string;
export type OperationalProcedureId = string;
export type MonitoringProgramId = string;
export type InternalAuditId = string;
export type AuditProgrammeId = string;
export type AuditFindingId = string;
export type ManagementReviewId = string;
export type NonconformityId = string;
export type CorrectiveActionId = string;
export type ImprovementOpportunityId = string;
export type ThirdPartyRelationshipId = string;
export type SupplierRelationshipId = string;
export type CustomerRelationshipId = string;
export type AISystemEventId = string;
export type AIIncidentId = string;
export type ConcernReportId = string;
/**
* The reference control families in Annex A of ISO/IEC 42001:2023.
*/
export enum AIControlFamily {
    
    /** Policies related to AI (Annex A.2) - management direction and support for AI systems according to business requirements. */
    ai_policies = "ai_policies",
    /** Internal organization (Annex A.3) - accountability for responsible implementation, operation, and management of AI systems. */
    internal_organization = "internal_organization",
    /** Resources for AI systems (Annex A.4) - documentation of data, tooling, system/computing, and human resources for AI systems. */
    ai_resources = "ai_resources",
    /** Assessing impacts of AI systems (Annex A.5) - evaluation of consequences for individuals, groups, and societies across the AI system life cycle. */
    impact_assessment = "impact_assessment",
    /** AI system life cycle (Annex A.6) - responsible design, development, verification, deployment, operation, and technical documentation. */
    ai_system_lifecycle = "ai_system_lifecycle",
    /** Data for AI systems (Annex A.7) - data management, acquisition, quality, provenance, and preparation for AI. */
    data_for_ai = "data_for_ai",
    /** Information for interested parties (Annex A.8) - system documentation for users, external reporting, and incident communications. */
    information_for_parties = "information_for_parties",
    /** Use of AI systems (Annex A.9) - responsible-use processes, objectives, and intended-use enforcement. */
    use_of_ai = "use_of_ai",
    /** Third-party and customer relationships (Annex A.10) - allocating responsibilities, supplier management, and customer expectations. */
    third_party_relationships = "third_party_relationships",
};
/**
* Lifecycle status of a reference control, used in the AIMS Statement of Applicability and control tracking.
*/
export enum ImplementationStatus {
    
    /** Control identified but no implementation activities begun. */
    not_started = "not_started",
    /** Control scheduled for implementation with defined timeline. */
    planned = "planned",
    /** Implementation actively underway but not yet complete. */
    in_progress = "in_progress",
    /** Control fully implemented and operational. */
    implemented = "implemented",
    /** Control excluded from scope with documented justification per Clause 6.1.3 f). */
    not_applicable = "not_applicable",
};
/**
* Standard risk treatment options drawn from ISO 31000 and adapted for AI risk treatment per Clause 6.1.3.
*/
export enum RiskTreatmentOption {
    
    /** Apply controls to change the AI risk level (reduce likelihood or consequence). */
    modify = "modify",
    /** Accept the residual AI risk without further treatment, within risk appetite, with designated management approval. */
    accept = "accept",
    /** Eliminate the AI risk by not undertaking the activity that creates it (for example, not deploying a high-risk AI use case). */
    avoid = "avoid",
    /** Transfer or share the AI risk with external parties (e.g., insurance, contractual transfer to a supplier or partner). */
    share = "share",
};
/**
* Qualitative AI risk rating derived from likelihood and consequence analysis.
*/
export enum RiskLevel {
    
    /** Negligible AI risk requiring no immediate action. */
    very_low = "very_low",
    /** Minor AI risk manageable through routine procedures. */
    low = "low",
    /** Moderate AI risk requiring management attention and planned controls. */
    medium = "medium",
    /** Significant AI risk requiring priority treatment and escalation. */
    high = "high",
    /** Severe AI risk threatening organizational objectives, individuals, or societies; requires immediate executive action. */
    critical = "critical",
};
/**
* Qualitative likelihood scale for AI risk assessment.
*/
export enum LikelihoodRating {
    
    /** Highly unlikely to occur (< 5% probability). */
    rare = "rare",
    /** Not expected but possible (5-20% probability). */
    unlikely = "unlikely",
    /** May occur at some point (20-50% probability). */
    possible = "possible",
    /** Probably will occur (50-80% probability). */
    likely = "likely",
    /** Expected to occur in most circumstances (> 80% probability). */
    almost_certain = "almost_certain",
};
/**
* Qualitative consequence scale for AI risk assessment, covering impact on the organization, individuals, groups, and societies.
*/
export enum ImpactRating {
    
    /** No significant impact on operations, individuals, or society. */
    negligible = "negligible",
    /** Limited impact, easily absorbed by normal operations. */
    minor = "minor",
    /** Noticeable impact requiring management intervention. */
    moderate = "moderate",
    /** Serious impact on objectives, reputation, compliance, or identifiable groups of individuals. */
    major = "major",
    /** Catastrophic impact threatening organizational viability, broad societal harm, or fundamental rights of affected individuals. */
    severe = "severe",
};
/**
* Stages of the AI system life cycle referenced throughout Annex A.6 and defined in ISO/IEC 5338 / ISO/IEC 22989.
*/
export enum AISystemLifecycleStage {
    
    /** Initial conception, feasibility, and use-case definition. */
    inception = "inception",
    /** AI system design including requirements and architecture. */
    design = "design",
    /** Acquiring, labelling, and preparing data resources. */
    data_collection_and_preparation = "data_collection_and_preparation",
    /** Model and AI system development and training. */
    development = "development",
    /** Verification and validation of the AI system. */
    verification_and_validation = "verification_and_validation",
    /** Release and integration into the production environment. */
    deployment = "deployment",
    /** Ongoing operation, monitoring, and support. */
    operation_and_monitoring = "operation_and_monitoring",
    /** Continuous validation, including drift detection and re-training triggers. */
    continuous_validation = "continuous_validation",
    /** Re-evaluation following significant changes or new evidence. */
    re_evaluation = "re_evaluation",
    /** Retirement, disposal, and post-decommissioning obligations. */
    decommissioning = "decommissioning",
};
/**
* Roles an organization may take with respect to an AI system, paraphrased from the role taxonomy referenced in ISO/IEC 22989 and the NIST AI RMF.
*/
export enum AIOrganizationalRole {
    
    /** Organization providing AI platforms, products, or services to others. */
    ai_provider = "ai_provider",
    /** Organization or actor that develops, designs, operates, tests, evaluates, deploys, or governs AI systems. */
    ai_producer = "ai_producer",
    /** Organization or individual that uses an AI product or service. */
    ai_customer = "ai_customer",
    /** System integrators and data providers for AI systems. */
    ai_partner = "ai_partner",
    /** Individuals or groups whose data or interests are affected by an AI system (e.g., data subjects). */
    ai_subject = "ai_subject",
    /** Policymakers, regulators, and other oversight bodies. */
    relevant_authority = "relevant_authority",
};
/**
* Categories of data resources documented for AI systems per A.7 (Data for AI systems).
*/
export enum DataResourceCategory {
    
    /** Data used to train machine learning models. */
    training = "training",
    /** Data used for model selection and hyperparameter tuning. */
    validation = "validation",
    /** Data used to evaluate model performance prior to deployment. */
    test = "test",
    /** Live operational data processed by the deployed AI system. */
    production = "production",
    /** Reference datasets used for benchmarking or comparison. */
    reference = "reference",
};
/**
* Categories of organizational objectives associated with responsible development and use of AI systems, paraphrased from Annex C of ISO/IEC 42001:2023.
*/
export enum AIObjectiveCategory {
    
    /** Clear allocation of responsibility for AI-supported decisions. */
    accountability = "accountability",
    /** Availability of interdisciplinary expertise for AI activities. */
    ai_expertise = "ai_expertise",
    /** Adequate quality of training, validation, and test data. */
    data_quality = "data_quality",
    /** Management of positive and negative environmental effects. */
    environmental_impact = "environmental_impact",
    /** Avoiding inappropriate or unfair outcomes for individuals or groups. */
    fairness = "fairness",
    /** Ability to correct defects and accommodate new requirements. */
    maintainability = "maintainability",
    /** Protection of personal and sensitive data processed by AI systems. */
    privacy = "privacy",
    /** Comparable performance on new and operational data. */
    robustness = "robustness",
    /** Avoidance of harm to life, health, property, or the environment. */
    safety = "safety",
    /** Protection from AI-specific and conventional security threats. */
    security = "security",
    /** Visibility into organizational AI practices and AI system behaviour. */
    transparency = "transparency",
    /** Comprehensible explanations of important factors driving AI outputs. */
    explainability = "explainability",
    /** Consistent performance under defined conditions. */
    reliability = "reliability",
    /** Usability of AI systems by people with diverse abilities. */
    accessibility = "accessibility",
    /** Sufficient availability and quality of training, validation, and test data needed to train and verify AI systems (Annex C.2.3). */
    availability_of_training_data = "availability_of_training_data",
};
/**
* Categories of AI risk sources, paraphrased from Annex C of ISO/IEC 42001:2023.
*/
export enum AIRiskSourceCategory {
    
    /** Performance uncertainty in complex or open operational environments (e.g., autonomous systems). */
    complexity_of_environment = "complexity_of_environment",
    /** Inability to provide adequate information to interested parties, affecting trustworthiness and accountability. */
    lack_of_transparency_or_explainability = "lack_of_transparency_or_explainability",
    /** Effects of automation on safety, fairness, security, or human oversight. */
    level_of_automation = "level_of_automation",
    /** Risks tied to data collection, data quality, and ML-specific phenomena such as data poisoning. */
    machine_learning_specific = "machine_learning_specific",
    /** Hardware errors or behavioural differences when transferring trained models between systems. */
    hardware = "hardware",
    /** Risks introduced at any AI system life cycle stage, including design flaws, deployment issues, or decommissioning gaps. */
    lifecycle = "lifecycle",
    /** Risks from immature technology with unknown limitations as well as mature technology subject to technology complacency. */
    technology_readiness = "technology_readiness",
};
/**
* Categories of documented information referenced in or required by ISO/IEC 42001:2023.
*/
export enum DocumentType {
    
    /** High-level statement of intent and direction (e.g., AI policy per 5.2). */
    policy = "policy",
    /** Documented steps for performing AIMS activities consistently. */
    procedure = "procedure",
    /** Mandatory requirements for specific AI technologies or processes. */
    standard = "standard",
    /** Recommended practices that support AI-related policies. */
    guideline = "guideline",
    /** Evidence of AIMS activities performed or results achieved. */
    record = "record",
    /** Documented approach for achieving objectives (e.g., AI risk treatment plan, deployment plan). */
    plan = "plan",
    /** Formal output of assessment, audit, impact assessment, or review activities. */
    report = "report",
    /** AI system technical documentation provided to users, partners, supervisory authorities, and other interested parties per A.6.2.7 and A.8.2. */
    technical_documentation = "technical_documentation",
};
/**
* Classification of internal audit findings for the AIMS.
*/
export enum AuditFindingType {
    
    /** Significant failure to fulfill a requirement that affects the AIMS ability to achieve its intended outcomes. */
    major_nonconformity = "major_nonconformity",
    /** Isolated lapse that does not significantly affect AIMS effectiveness. */
    minor_nonconformity = "minor_nonconformity",
    /** Noted condition that could lead to a nonconformity if not addressed. */
    observation = "observation",
    /** Evidence of effective implementation exceeding requirements. */
    positive_finding = "positive_finding",
};
/**
* Dimensions evaluated during an AI system impact assessment per Clause 6.1.4. Combines individual/group impacts (Annex A.5.4 / Annex B.5.4) with societal-scope impacts (Annex A.5.5 / Annex B.5.5).
*/
export enum ImpactAssessmentDimension {
    
    /** Consequences for individual persons interacting with or affected by the AI system. */
    individual = "individual",
    /** Consequences for identifiable groups of individuals. */
    group = "group",
    /** Broader societal consequences. */
    societal = "societal",
    /** Fair and non-discriminatory treatment of affected individuals and groups (B.5.4). */
    fairness = "fairness",
    /** Transparency of organizational AI practices and AI system behaviour (B.5.4). */
    transparency = "transparency",
    /** Comprehensibility of important factors driving AI outputs (B.5.4). */
    explainability = "explainability",
    /** Clear allocation of accountability for AI-supported decisions (B.5.4). */
    accountability = "accountability",
    /** Accessibility of the AI system for people with diverse abilities (B.5.4). */
    accessibility = "accessibility",
    /** Effects on fundamental human rights (B.5.4). */
    human_rights = "human_rights",
    /** Financial consequences for affected individuals or organizations (B.5.4). */
    financial = "financial",
    /** Effects on physical or mental health (B.5.4). */
    health = "health",
    /** Environmental consequences attributable to the AI system (B.5.5). */
    environmental = "environmental",
    /** Wider economic consequences (B.5.5). */
    economic = "economic",
    /** Consequences for democratic processes, governance, or rule of law (B.5.5). */
    government = "government",
    /** Consequences for cultural norms, traditions, or values (B.5.5). */
    cultural_norms = "cultural_norms",
    /** Safety-related consequences in the deployment context. */
    safety = "safety",
    /** Privacy-related consequences for data subjects. */
    privacy = "privacy",
    /** Information security consequences attributable to the AI system. */
    security = "security",
};
/**
* Normative reference control identifiers from Annex A of ISO/IEC 42001:2023 (38 controls across nine families A.2-A.10). Permissible value names use underscores in place of dots; the `meaning` slot preserves the Annex A dotted form. Control titles are paraphrased.
*/
export enum AnnexAControlId {
    
    /** AI policy - document a policy governing AI system development or use. */
    a_2_2 = "a_2_2",
    /** Alignment with other organizational policies - reconcile AI objectives with related policies. */
    a_2_3 = "a_2_3",
    /** Review of the AI policy - planned and event-driven policy review for suitability and effectiveness. */
    a_2_4 = "a_2_4",
    /** AI roles and responsibilities - define and allocate AI-related roles per organizational needs. */
    a_3_2 = "a_3_2",
    /** Reporting of concerns - process for raising concerns about the organization's role with respect to AI. */
    a_3_3 = "a_3_3",
    /** Resource documentation - identify and document resources used at each AI lifecycle stage. */
    a_4_2 = "a_4_2",
    /** Data resources - document data resources used by the AI system. */
    a_4_3 = "a_4_3",
    /** Tooling resources - document tooling resources used by the AI system. */
    a_4_4 = "a_4_4",
    /** System and computing resources - document system and computing resources used by the AI system. */
    a_4_5 = "a_4_5",
    /** Human resources - document human resources and competences across the AI lifecycle. */
    a_4_6 = "a_4_6",
    /** AI system impact assessment process - establish a process to assess consequences across the lifecycle. */
    a_5_2 = "a_5_2",
    /** Documentation of AI system impact assessments - record and retain assessment results. */
    a_5_3 = "a_5_3",
    /** Assessing AI system impact on individuals or groups - evaluate and document impacts to individuals. */
    a_5_4 = "a_5_4",
    /** Assessing societal impacts of AI systems - evaluate and document broader societal impacts. */
    a_5_5 = "a_5_5",
    /** Objectives for responsible development - identify objectives that guide responsible AI development. */
    a_6_1_2 = "a_6_1_2",
    /** Processes for responsible AI system design and development - document the design and development processes. */
    a_6_1_3 = "a_6_1_3",
    /** AI system requirements and specification - specify requirements for new or enhanced AI systems. */
    a_6_2_2 = "a_6_2_2",
    /** Documentation of AI system design and development - document design and development against requirements. */
    a_6_2_3 = "a_6_2_3",
    /** AI system verification and validation - define and document V&V measures and criteria. */
    a_6_2_4 = "a_6_2_4",
    /** AI system deployment - document a deployment plan and verify pre-deployment requirements. */
    a_6_2_5 = "a_6_2_5",
    /** AI system operation and monitoring - document operational and performance monitoring, repairs, updates, and support. */
    a_6_2_6 = "a_6_2_6",
    /** AI system technical documentation - provide technical documentation tailored to each interested party. */
    a_6_2_7 = "a_6_2_7",
    /** AI system recording of event logs - enable event log recording across relevant lifecycle phases. */
    a_6_2_8 = "a_6_2_8",
    /** Data for development and enhancement - define and implement data management processes for AI development. */
    a_7_2 = "a_7_2",
    /** Acquisition of data - document acquisition and selection details for data used in AI systems. */
    a_7_3 = "a_7_3",
    /** Quality of data for AI systems - define and meet data quality requirements. */
    a_7_4 = "a_7_4",
    /** Data provenance - record data provenance across the data and AI system life cycles. */
    a_7_5 = "a_7_5",
    /** Data preparation - document criteria and methods used for data preparation. */
    a_7_6 = "a_7_6",
    /** System documentation and information for users - provide information needed by AI system users. */
    a_8_2 = "a_8_2",
    /** External reporting - enable interested parties to report adverse impacts. */
    a_8_3 = "a_8_3",
    /** Communication of incidents - document a plan for communicating incidents to users. */
    a_8_4 = "a_8_4",
    /** Information for interested parties - document obligations to report AI system information to interested parties. */
    a_8_5 = "a_8_5",
    /** Processes for responsible use of AI systems - define and document responsible use processes. */
    a_9_2 = "a_9_2",
    /** Objectives for responsible use of AI system - identify and document responsible-use objectives. */
    a_9_3 = "a_9_3",
    /** Intended use of the AI system - ensure use aligns with the documented intended use. */
    a_9_4 = "a_9_4",
    /** Allocating responsibilities - allocate AI lifecycle responsibilities across organization, partners, suppliers, customers, third parties. */
    a_10_2 = "a_10_2",
    /** Suppliers - ensure supplier-provided services, products, and materials align with the organization's responsible AI approach. */
    a_10_3 = "a_10_3",
    /** Customers - account for customer expectations and needs in the organization's responsible AI approach. */
    a_10_4 = "a_10_4",
};
/**
* Application sectors referenced in Annex D of ISO/IEC 42001:2023 in which the AIMS can be deployed jointly with sector-specific management system standards (e.g., ISO 13485, ISO 22000, IEC 62304).
*/
export enum SectorDomain {
    
    /** Health, medical devices, and healthcare delivery contexts. */
    health = "health",
    /** Defence, security, and dual-use technology contexts. */
    defence = "defence",
    /** Transport, mobility, and autonomous vehicle contexts. */
    transport = "transport",
    /** Financial services, banking, insurance, and capital markets. */
    finance = "finance",
    /** Hiring, workforce management, and employee evaluation. */
    employment = "employment",
    /** Energy production, distribution, and grid management. */
    energy = "energy",
    /** Government, public administration, and public-service delivery. */
    public_sector = "public_sector",
    /** Education, training, and academic assessment contexts. */
    education = "education",
    /** Industrial and manufacturing automation. */
    manufacturing = "manufacturing",
    /** Agricultural production and food-supply contexts. */
    agriculture = "agriculture",
    /** Telecommunications and network operations. */
    telecommunications = "telecommunications",
    /** Retail, e-commerce, and consumer products. */
    retail = "retail",
    /** Other sector not enumerated above. */
    other = "other",
};
/**
* Learning paradigm of an AI system, informing risk considerations related to data provenance, drift, and behavioural change over time (see ISO/IEC 42001:2023 Introduction and Annex C.3.4).
*/
export enum LearningParadigm {
    
    /** Trained once and deployed without further learning during operation. */
    static = "static",
    /** Retrained on a defined cadence with controlled release cycles. */
    periodic_retraining = "periodic_retraining",
    /** Updates its behaviour during operation based on new data or feedback. */
    continuous_learning = "continuous_learning",
    /** Continuously updates parameters from a stream of data. */
    online_learning = "online_learning",
    /** Adapted from a pre-trained model to a new task or domain. */
    transfer_learning = "transfer_learning",
    /** Learns a policy through interaction with an environment and reward signals. */
    reinforcement_learning = "reinforcement_learning",
    /** Combines multiple learning paradigms (e.g., supervised plus reinforcement). */
    hybrid = "hybrid",
    /** AI system that is not based on machine learning (e.g., rule-based). */
    not_applicable = "not_applicable",
};
/**
* AI-specific incident categories supplementing classical information security incident classes. Supports incident triage and communication per Annex A.8.3 (External reporting) and A.8.4 (Communication of incidents).
*/
export enum AIIncidentCategory {
    
    /** Training or production data manipulated to compromise model behaviour. */
    data_poisoning = "data_poisoning",
    /** Unauthorized extraction or reconstruction of a deployed model. */
    model_stealing = "model_stealing",
    /** Reconstruction of sensitive training data via model queries. */
    model_inversion = "model_inversion",
    /** Inference of whether a record was part of the training set. */
    membership_inference = "membership_inference",
    /** Adversarial inputs causing the model to deviate from intended behaviour. */
    prompt_injection = "prompt_injection",
    /** Confidently incorrect or fabricated outputs causing material harm. */
    hallucination = "hallucination",
    /** Performance or behaviour degradation due to distribution shift. */
    model_drift = "model_drift",
    /** Unfair or discriminatory outcomes affecting individuals or groups. */
    bias_incident = "bias_incident",
    /** Harm to life, health, property, or the environment from AI behaviour. */
    safety_incident = "safety_incident",
    /** Unauthorized disclosure of personal data via the AI system. */
    privacy_breach = "privacy_breach",
    /** Compromise of confidentiality, integrity, or availability of the AI system. */
    security_breach = "security_breach",
    /** Use of the AI system outside its documented intended use. */
    misuse = "misuse",
    /** Broader societal harm reported by external interested parties. */
    adverse_societal_impact = "adverse_societal_impact",
    /** Other AI incident category not enumerated above. */
    other = "other",
};
/**
* Type of audit conducted against the AIMS per Clause 9.2 and the ISO 19011 audit taxonomy.
*/
export enum AuditType {
    
    /** First-party audit conducted by the organization itself or on its behalf. */
    internal = "internal",
    /** Second-party audit conducted by an interested party (e.g., customer). */
    external_second_party = "external_second_party",
    /** Third-party audit conducted by an independent certification body. */
    external_third_party = "external_third_party",
    /** Ongoing surveillance audit during the certification cycle. */
    surveillance = "surveillance",
    /** Audit performed to renew certification. */
    recertification = "recertification",
    /** Combined audit covering two or more management system disciplines. */
    combined = "combined",
};
/**
* Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in B.6.2.3. Distinct from `LearningParadigm`, which describes how often the model updates.
*/
export enum MLApproach {
    
    /** Learns from labelled examples. */
    supervised = "supervised",
    /** Discovers structure in unlabelled data. */
    unsupervised = "unsupervised",
    /** Combines a small labelled set with a larger unlabelled set. */
    semi_supervised = "semi_supervised",
    /** Generates supervisory signals from the data itself. */
    self_supervised = "self_supervised",
    /** Learns a policy through interaction with an environment and reward signals. */
    reinforcement = "reinforcement",
    /** Adapts a pre-trained model to a new task or domain. */
    transfer = "transfer",
    /** Trains across distributed data holders without centralizing raw data. */
    federated = "federated",
    /** Generative modelling approach (e.g., LLMs, diffusion models). */
    generative = "generative",
    /** Rule-based or symbolic reasoning, not statistical ML. */
    symbolic = "symbolic",
    /** Combines multiple ML approaches. */
    hybrid = "hybrid",
    /** AI system not based on machine learning. */
    not_applicable = "not_applicable",
};
/**
* Common data preparation and transformation methods documented per Annex A.7.6 and Annex B.7.6.
*/
export enum DataPreparationMethod {
    
    /** Distribution, mean, median, standard deviation, range, stratification, sampling. */
    statistical_exploration = "statistical_exploration",
    /** Correcting entries and handling malformed records. */
    cleaning = "cleaning",
    /** Filling in missing entries. */
    imputation = "imputation",
    /** Re-scaling values to a common range or distribution. */
    normalization = "normalization",
    /** Multiplicative re-scaling of feature values. */
    scaling = "scaling",
    /** Assigning target labels to records. */
    labelling = "labelling",
    /** Converting categorical variables to numeric representations. */
    encoding = "encoding",
    /** Synthesising additional training samples from existing data. */
    augmentation = "augmentation",
    /** Removing duplicate records. */
    deduplication = "deduplication",
    /** Removing or transforming personally identifying information. */
    anonymization = "anonymization",
    /** Other preparation method not enumerated above. */
    other = "other",
};
/**
* Related management-system standards with which the AIMS may be jointly implemented, per the Introduction (Compatibility with other management system standards) and Annex D.
*/
export enum RelatedManagementSystem {
    
    /** Information security management systems. */
    iso_iec_27001 = "iso_iec_27001",
    /** Privacy information management. */
    iso_iec_27701 = "iso_iec_27701",
    /** Quality management systems. */
    iso_9001 = "iso_9001",
    /** Food safety management systems. */
    iso_22000 = "iso_22000",
    /** Medical-device quality management systems. */
    iso_13485 = "iso_13485",
    /** Medical device software life cycle processes. */
    iec_62304 = "iec_62304",
    /** AI system life cycle process. */
    iso_iec_5338 = "iso_iec_5338",
    /** Data quality for analytics and ML. */
    iso_iec_5259 = "iso_iec_5259",
    /** AI concepts and terminology (normative reference). */
    iso_iec_22989 = "iso_iec_22989",
    /** AI risk management guidance. */
    iso_iec_23894 = "iso_iec_23894",
    /** Governance of IT - AI governance implications. */
    iso_iec_38507 = "iso_iec_38507",
    /** Information security management - overview and vocabulary. */
    iso_iec_27000 = "iso_iec_27000",
    /** Privacy framework. */
    iso_iec_29100 = "iso_iec_29100",
    /** Risk management guidelines. */
    iso_31000 = "iso_31000",
    /** Measurement of data quality. */
    iso_iec_25024 = "iso_iec_25024",
    /** Quality model for AI systems. */
    iso_iec_25059 = "iso_iec_25059",
    /** Guidelines for auditing management systems. */
    iso_19011 = "iso_19011",
    /** Whistleblowing management systems (informs A.3.3 concern reporting). */
    iso_37002 = "iso_37002",
    /** Other management system standard not enumerated above. */
    other = "other",
};
/**
* Governance role types within the AIMS, paraphrased from Clause 3.3 (top management), Clause 3.22 (governing body), Clause 5.3, and Annex A.3.2. Use this enum on `role_type` for normative governance positions; free-form strings remain accepted for organization-defined roles.
*/
export enum GovernanceRoleType {
    
    /** Board, trustees, or other body accountable for organizational performance (3.22). */
    governing_body = "governing_body",
    /** Person or group directing and controlling the organization at the highest level (3.3). */
    top_management = "top_management",
    /** Management designated to approve AI risk treatment plans and residual-risk acceptance (6.1.3). */
    designated_management = "designated_management",
    /** Senior executive accountable for the AIMS. */
    chief_ai_officer = "chief_ai_officer",
    /** Person accountable for managing a specific AI risk (6.1.2). */
    ai_risk_owner = "ai_risk_owner",
    /** Role accountable for AI policy development and review (A.2.4). */
    ai_policy_owner = "ai_policy_owner",
    /** Cross-functional committee providing oversight of AI systems. */
    ai_oversight_committee = "ai_oversight_committee",
    /** Role accountable for data resources used by AI systems (A.4.3, A.7). */
    data_steward = "data_steward",
    /** Role responsible for verification and validation of AI models (A.6.2.4). */
    model_validator = "model_validator",
    /** Role performing human-in-the-loop review of AI outputs (B.9.3). */
    human_oversight_reviewer = "human_oversight_reviewer",
    /** Role developing AI systems or components. */
    ai_developer = "ai_developer",
    /** Role operating and monitoring AI systems in production. */
    ai_operator = "ai_operator",
    /** Role conducting AI system impact assessments (6.1.4). */
    ai_impact_assessor = "ai_impact_assessor",
    /** Internal or external auditor of the AIMS (9.2). */
    auditor = "auditor",
    /** Other governance role not enumerated above. */
    other = "other",
};


/**
 * Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
 */
export interface NamedEntity {
    /** Unique identifier for this entity instance. */
    id: string,
    /** Human-readable name or title. */
    name: string,
    /** Detailed description of the entity. */
    description?: string,
    /** Date when the entity was created. */
    created_date?: date,
    /** Date when the entity was last modified. */
    modified_date?: date,
    /** Version identifier for the entity. */
    version?: string,
}


/**
 * Abstract class for documented information per Clause 7.5. Captures metadata required for document control under the AIMS.
 */
export interface DocumentedInformation extends NamedEntity {
    /** Classification of the documented information. */
    document_type?: string,
    /** Unique reference number for document control. */
    document_reference?: string,
    /** Person who created the document. */
    author?: string,
    /** Person accountable for the document content and maintenance. */
    owner?: string,
    /** Person who approved the document. */
    approved_by?: string,
    /** Date when the document was approved. */
    approved_date?: date,
    /** Date when the document becomes effective. */
    effective_date?: date,
    /** Date when the document is due for review. */
    review_date?: date,
    /** Current status of the document or entity. */
    status?: string,
    /** Information classification level. */
    classification?: string,
    /** Duration for which the document is retained. */
    retention_period?: string,
}


/**
 * Top-level container representing an organization's complete AI Management System (AIMS) per ISO/IEC 42001:2023. Aggregates all components required to support the AIMS lifecycle.
 */
export interface AIManagementSystem extends NamedEntity {
    /** Reference to the organization operating the AIMS. */
    organization?: OrganizationId,
    /** Documented statement of AIMS scope per Clause 4.3. */
    scope_statement?: string,
    /** Defined boundaries of the AIMS scope. */
    scope_boundaries?: string[],
    /** Any exclusions from scope with justification. */
    scope_exclusions?: string[],
    /** Internal issues relevant to the AIMS per Clause 4.1. */
    context_internal_issues?: string[],
    /** External issues relevant to the AIMS per Clause 4.1. */
    context_external_issues?: string[],
    /** Documented set of roles the organization plays in the AI ecosystem within the AIMS scope. */
    organizational_roles_with_ai?: string,
    /** Related management-system standards with which the AIMS is jointly implemented or aligned (Introduction - Compatibility with other management system standards, Annex D). */
    integrated_management_systems?: string,
    /** Reference to the person or group exercising top management direction and control over the AIMS (Clause 3.3, 5.1). */
    top_management?: string,
    /** Reference to the governing body to which top management is accountable (Clause 3.22). */
    governing_body?: string,
    /** Records or references demonstrating top-management leadership and commitment to the AIMS per Clause 5.1. */
    leadership_commitment_evidence?: string[],
    /** Records of planned changes to the AIMS, including purpose, consequences, resource implications, and responsibilities per Clause 6.3. */
    planned_changes?: string[],
    /** Stakeholders relevant to the AIMS. */
    interested_parties?: InterestedPartyId[],
    /** Reference to the AI policy. */
    ai_policy?: AIPolicyId,
    /** AI objectives established by the organization. */
    ai_objectives?: AIObjectiveId[],
    /** Reference to the AI risk assessment process. */
    ai_risk_assessment_process?: AIRiskAssessmentProcessId,
    /** Reference to the AI risk treatment process. */
    ai_risk_treatment_process?: AIRiskTreatmentProcessId,
    /** Reference to the AI system impact assessment process. */
    ai_system_impact_assessment_process?: AISystemImpactAssessmentProcessId,
    /** Reference to the AIMS Statement of Applicability. */
    statement_of_applicability?: StatementOfApplicabilityId,
    /** AI reference controls applied within the AIMS. */
    reference_controls?: AIReferenceControlId[],
    /** AI systems within the AIMS scope. */
    ai_systems?: AISystemId[],
    /** AI-related roles defined in the AIMS. */
    roles?: RoleId[],
    /** Resources provided for the AIMS. */
    resources?: ResourceId[],
    /** Competence records for personnel. */
    competence_records?: CompetenceRecordId[],
    /** Reference to the awareness program. */
    awareness_program?: AwarenessProgramId,
    /** Reference to the communication plan. */
    communication_plan?: CommunicationPlanId,
    /** Register of all documented information. */
    documented_information_register?: DocumentedInformationId[],
    /** Operational procedures of the AIMS. */
    operational_procedures?: OperationalProcedureId[],
    /** AI risk assessment instances. */
    ai_risk_assessments?: AIRiskAssessmentId[],
    /** AI risk treatment plans. */
    ai_risk_treatment_plans?: AIRiskTreatmentPlanId[],
    /** AI system impact assessment instances. */
    ai_system_impact_assessments?: AISystemImpactAssessmentId[],
    /** Reference to the monitoring program. */
    monitoring_program?: MonitoringProgramId,
    /** Internal audits conducted. */
    internal_audits?: InternalAuditId[],
    /** Management reviews of the AIMS. */
    management_reviews?: ManagementReviewId[],
    /** Nonconformities identified. */
    nonconformities?: NonconformityId[],
    /** Corrective actions taken. */
    corrective_actions?: CorrectiveActionId[],
    /** Improvement opportunities being tracked. */
    improvements?: ImprovementOpportunityId[],
    /** Third-party relationships within the AIMS scope. */
    third_party_relationships?: ThirdPartyRelationshipId[],
    /** Current certification status of the AIMS. */
    certification_status?: string,
    /** Body that issued the certification. */
    certification_body?: string,
    /** Date the AIMS was certified. */
    certification_date?: date,
    /** Date when recertification is due. */
    recertification_date?: date,
    /** AI system events recorded under the AIMS. */
    ai_system_events?: AISystemEventId[],
    /** AI incidents managed under the AIMS. */
    ai_incidents?: AIIncidentId[],
    /** Concern reports raised and managed under the AIMS per A.3.3. */
    concern_reports?: ConcernReportId[],
}


/**
 * The organization establishing and operating the AIMS. Captures the context required by Clause 4.1, including the organization's role(s) with respect to AI systems.
 */
export interface Organization extends NamedEntity {
    /** Legal registered name of the organization. */
    legal_name?: string,
    /** Names under which the organization conducts business. */
    trading_names?: string[],
    /** Type of organization (e.g., corporation, government, nonprofit). */
    organization_type?: string,
    /** Primary industry sector of the organization (free-form label). */
    industry_sector?: string,
    /** Application sectors in which the organization deploys AI systems, drawn from the Annex D examples; supports identification of sector- specific management system standards that integrate with the AIMS. */
    sector_domains?: string,
    /** Organization size classification. */
    size_category?: string,
    /** Approximate number of employees. */
    employee_count?: number,
    /** Countries or regions where the organization operates. */
    geographic_locations?: string[],
    /** Jurisdictions whose regulations apply to the organization. */
    regulatory_jurisdictions?: string[],
    /** Parent organization if applicable. */
    parent_organization?: string,
    /** Subsidiary organizations if applicable. */
    subsidiaries?: string[],
    /** Roles the organization takes with respect to AI systems (provider, producer, customer, partner, subject, authority). */
    ai_roles?: string,
    /** Whether climate change has been determined to be a relevant issue for the organization's context per Clause 4.1. */
    climate_change_relevant?: boolean,
}


/**
 * A stakeholder whose needs and expectations are relevant to the AIMS per Clause 4.2. Includes internal and external parties such as users, regulators, partners, suppliers, customers, AI subjects, and relevant authorities.
 */
export interface InterestedParty extends NamedEntity {
    /** Category of party. */
    party_type?: string,
    /** Nature of the relationship with the organization. */
    relationship?: string,
    /** Requirements of the interested party. */
    requirements?: string[],
    /** Communication requirements for this party. */
    communication_needs?: string,
    /** Contact details for the party. */
    contact_information?: string,
}


/**
 * The AI policy established by top management per Clause 5.2. Provides a framework for setting AI objectives and demonstrates commitment to responsible AI.
 */
export interface AIPolicy extends DocumentedInformation {
    /** The core policy statement text. */
    policy_statement?: string,
    /** Framework for setting AI objectives. */
    policy_objectives_framework?: string,
    /** Statements of commitment included in the policy. */
    commitment_statements?: string[],
    /** Statement of policy applicability. */
    applicability_statement?: string,
    /** Date when the policy was communicated. */
    communication_date?: date,
    /** Whether acknowledgment is required from personnel. */
    acknowledgment_required?: boolean,
    /** Topic-specific policies supporting this policy. */
    related_topic_policies?: TopicSpecificPolicyId[],
    /** Date of the most recent AI policy review. */
    last_policy_review_date?: date,
    /** Planned date of the next AI policy review. */
    next_policy_review_date?: date,
}


/**
 * A topic-specific policy supporting the overarching AI policy, for example covering data governance, fairness, transparency, supplier use, or human oversight of AI systems.
 */
export interface TopicSpecificPolicy extends DocumentedInformation {
    /** The specific topic addressed by the policy. */
    topic_area?: string,
    /** The parent AI policy this topic-specific policy supports. */
    parent_policy?: AIPolicyId,
    /** Reference controls related to this policy or AI system. */
    applicable_controls?: AIReferenceControlId[],
    /** Intended audience for the policy or document. */
    target_audience?: string,
}


/**
 * An AI-related role with defined responsibilities and authorities per Clause 5.3 and Annex A.3.2.
 */
export interface Role extends NamedEntity {
    /** Category of the role. Use a `GovernanceRoleType` value for the normative AIMS governance positions; free-form strings remain accepted for organization-defined roles. */
    role_type?: string,
    /** Responsibilities assigned to the role. */
    responsibilities?: string[],
    /** Authorities granted to the role. */
    authorities?: string[],
    /** What the role is accountable for. */
    accountability?: string,
    /** Person(s) assigned to this role or resource. */
    assigned_to?: string[],
    /** Rules for delegating responsibilities. */
    delegation_rules?: string,
    /** To whom this role reports. */
    reporting_line?: string,
}


/**
 * A measurable AI objective per Clause 6.2, established at relevant functions and levels and aligned with the AI policy.
 */
export interface AIObjective extends NamedEntity {
    /** Clear statement of the objective. */
    objective_statement?: string,
    /** Category of AI objective (e.g., fairness, transparency, robustness). */
    objective_category?: string,
    /** Target value for the objective metric. */
    target_value?: string,
    /** Current measured value. */
    current_value?: string,
    /** Definition of how the objective is measured. */
    metric_definition?: string,
    /** Method used to measure the metric. */
    measurement_method?: string,
    /** How often measurement is performed. */
    measurement_frequency?: string,
    /** Role responsible for the objective or control. */
    responsible_role?: RoleId,
    /** Resources required for implementation. */
    resources_required?: string,
    /** Target date for achieving the objective. */
    target_date?: date,
    /** Current status of objective achievement. */
    achievement_status?: string,
    /** Associated AI risks. */
    related_risks?: AIRiskId[],
    /** Other reference controls related to this one. */
    related_controls?: AIReferenceControlId[],
    /** Plan for achieving the objective. */
    action_plan?: string,
}


/**
 * The documented AI risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analysing, and evaluating AI risks. Aligned with ISO/IEC 23894.
 */
export interface AIRiskAssessmentProcess extends DocumentedInformation {
    /** Criteria for accepting AI risks. */
    risk_acceptance_criteria?: string,
    /** Criteria for performing AI risk or impact assessments. */
    assessment_criteria?: string,
    /** Methodology used for assessment. */
    assessment_methodology?: string,
    /** Scale used for likelihood rating. */
    likelihood_scale?: string,
    /** Scale used for impact rating. */
    impact_scale?: string,
    /** Risk matrix or calculation method. */
    risk_matrix?: string,
    /** Planned frequency of assessments. */
    assessment_frequency?: string,
    /** Events that trigger an assessment outside the planned schedule. */
    trigger_events?: string[],
    /** Statement of how the process aligns with the AI policy. */
    alignment_with_ai_policy?: string,
}


/**
 * An instance of AI risk assessment performed per Clause 8.2, identifying and evaluating AI risks at planned intervals or following significant change.
 */
export interface AIRiskAssessment extends DocumentedInformation {
    /** Scope of the assessment. */
    assessment_scope?: string,
    /** AI systems covered by this assessment. */
    ai_systems_assessed?: AISystemId[],
    /** Date the assessment was conducted. */
    assessment_date?: date,
    /** Person or team who conducted the assessment. */
    assessor?: string,
    /** Specific methodology applied in this assessment. */
    methodology_used?: string,
    /** Risks identified in this assessment. */
    risks_identified?: AIRiskId[],
    /** AI system impact assessment linked to this risk assessment. */
    linked_impact_assessment?: AISystemImpactAssessmentId,
    /** Summary of assessment findings. */
    summary_findings?: string,
    /** Recommendations from the assessment. */
    recommendations?: string[],
    /** Planned date for next assessment. */
    next_assessment_date?: date,
}


/**
 * An identified AI risk that may affect achievement of AI objectives, individuals, groups, or societies within the AIMS scope.
 */
export interface AIRisk extends NamedEntity {
    /** Category of AI risk source per Annex C. */
    risk_source_category?: string,
    /** Description of the specific source of risk. */
    risk_source_description?: string,
    /** AI systems affected by this risk. */
    affected_ai_systems?: AISystemId[],
    /** Dimensions of impact affected by the risk (individual, group, societal, safety, privacy, security, environmental). */
    affected_dimensions?: string,
    /** Person accountable for managing the AI risk. */
    risk_owner?: string,
    /** Assessed likelihood of risk occurrence. */
    likelihood?: string,
    /** Assessed consequence if the risk materializes. */
    impact?: string,
    /** Risk level before controls are applied. */
    inherent_risk_level?: string,
    /** Controls currently in place affecting this risk. */
    existing_controls?: AIReferenceControlId[],
    /** Risk level after controls are applied. */
    residual_risk_level?: string,
    /** Selected treatment option for the AI risk. */
    risk_treatment_option?: string,
    /** Priority for treating this risk. */
    treatment_priority?: string,
    /** Risk treatment plan addressing this risk. */
    related_treatment_plan?: AIRiskTreatmentPlanId,
    /** AI system impact assessment associated with this risk. */
    related_impact_assessment?: AISystemImpactAssessmentId,
}


/**
 * The documented AI risk treatment process per Clause 6.1.3, defining how treatment options are selected, how Annex A controls are considered, and how the Statement of Applicability is produced.
 */
export interface AIRiskTreatmentProcess extends DocumentedInformation {
    /** Guidance on selecting AI risk treatment options. */
    treatment_options_guidance?: string,
    /** Criteria for selecting Annex A controls. */
    control_selection_criteria?: string,
    /** Template used for the Statement of Applicability. */
    soa_template?: string,
    /** Workflow for approving AI risk treatment. */
    approval_workflow?: string,
}


/**
 * A plan documenting planned actions to address identified AI risks through selected controls. Requires approval by designated management per Clause 6.1.3.
 */
export interface AIRiskTreatmentPlan extends DocumentedInformation {
    /** Scope of the treatment plan. */
    plan_scope?: string,
    /** Risks addressed by this plan. */
    risks_addressed?: AIRiskId[],
    /** Actions to be taken for treatment. */
    treatment_actions?: string[],
    /** Controls to be implemented as part of treatment. */
    controls_to_implement?: AIReferenceControlId[],
    /** Resources required for implementation. */
    resources_required?: string,
    /** Parties responsible for implementation. */
    responsible_parties?: string[],
    /** Timeline for implementation. */
    implementation_timeline?: string,
    /** Risk owner who approved the plan. */
    risk_owner_approval?: string,
    /** Date when the document was approved. */
    approved_date?: date,
    /** Documentation of residual AI risk acceptance. */
    residual_risk_acceptance?: string,
    /** Current implementation status. */
    implementation_status?: string,
    /** Date when implementation was completed. */
    completion_date?: date,
}


/**
 * The documented process for assessing the potential consequences for individuals, groups, and societies arising from the development, provision, or use of AI systems per Clause 6.1.4.
 */
export interface AISystemImpactAssessmentProcess extends DocumentedInformation {
    /** Criteria for performing AI risk or impact assessments. */
    assessment_criteria?: string,
    /** Methodology used for assessment. */
    assessment_methodology?: string,
    /** Impact dimensions evaluated by the process. */
    dimensions_in_scope?: string,
    /** Planned frequency of assessments. */
    assessment_frequency?: string,
    /** Events that trigger an assessment outside the planned schedule. */
    trigger_events?: string[],
    /** Description of how impact assessment results feed into AI risk assessment per Clause 6.1.4. */
    linkage_to_risk_assessment?: string,
}


/**
 * An instance of an AI system impact assessment performed per Clause 6.1.4 and Clause 8.4. Documents consequences of deployment, intended use, and foreseeable misuse on individuals, groups, and societies.
 */
export interface AISystemImpactAssessment extends DocumentedInformation {
    /** Scope of the assessment. */
    assessment_scope?: string,
    /** AI systems covered by this assessment. */
    ai_systems_assessed?: AISystemId[],
    /** Date the assessment was conducted. */
    assessment_date?: date,
    /** Person or team who conducted the assessment. */
    assessor?: string,
    /** Specific technical context in which the AI system is deployed. */
    technical_context?: string,
    /** Societal context relevant to the impact assessment. */
    societal_context?: string,
    /** Jurisdictions relevant to the assessment. */
    applicable_jurisdictions?: string[],
    /** Impact dimensions actually assessed in this instance. */
    dimensions_assessed?: string,
    /** Identified positive or negative consequences. */
    identified_consequences?: string[],
    /** Mitigations to address identified consequences. */
    mitigations?: string[],
    /** Interested parties with whom the results have been shared. */
    shared_with_parties?: string[],
    /** Planned date for next assessment. */
    next_assessment_date?: date,
}


/**
 * The Statement of Applicability (SoA) for the AIMS recording which Annex A controls apply, justification for inclusion or exclusion, and current implementation state per Clause 6.1.3 f).
 */
export interface StatementOfApplicability extends DocumentedInformation {
    /** Individual control entries in the SoA. */
    soa_entries?: SoAEntry[],
    /** Total number of controls in scope. */
    total_controls?: number,
    /** Number of implemented controls. */
    implemented_count?: number,
    /** Number of controls planned for implementation. */
    planned_count?: number,
    /** Number of controls marked not applicable. */
    not_applicable_count?: number,
    /** Date of last review. */
    last_review_date?: date,
    /** Person who approved the document. */
    approved_by?: string,
}


/**
 * A single entry in the AIMS Statement of Applicability documenting the applicability and implementation status of one reference control.
 */
export interface SoAEntry {
    /** Reference to an Annex A control (e.g., A.6.2.4). */
    control_reference?: AIReferenceControlId,
    /** Whether the control is applicable. */
    is_applicable?: boolean,
    /** Justification for including the control. */
    inclusion_justification?: string,
    /** Justification for excluding the control. */
    exclusion_justification?: string,
    /** Current implementation status. */
    implementation_status?: string,
    /** Evidence of control implementation. */
    implementation_evidence?: string,
    /** Role responsible for the objective or control. */
    responsible_role?: RoleId,
    /** Target date for implementing the control. */
    target_implementation_date?: date,
}


/**
 * A reference control from Annex A of ISO/IEC 42001:2023. Controls are grouped into nine families (A.2 through A.10) and supported by implementation guidance in Annex B.
 */
export interface AIReferenceControl extends NamedEntity {
    /** Control identifier from Annex A (e.g., A.6.2.4). Accepts either an enumerated normative `AnnexAControlId` value or a free-form string for organization-defined controls beyond Annex A. */
    control_id?: string,
    /** Title of the control. */
    control_title?: string,
    /** Family of the Annex A control. */
    control_family?: string,
    /** Organization-authored control statement or external control summary. Do not include verbatim ISO/IEC standards text. */
    control_text?: string,
    /** Organization-authored implementation notes for the control. */
    implementation_guidance?: string,
    /** Other reference controls related to this one. */
    related_controls?: AIReferenceControlId[],
    /** Categories of AI risk source this control addresses. */
    applicable_risk_sources?: string,
    /** AI objective categories this control supports. */
    applicable_objectives?: string,
    /** Person responsible for the control. */
    control_owner?: string,
    /** Current implementation status. */
    implementation_status?: string,
    /** Date the control was implemented. */
    implementation_date?: date,
    /** Rating of control effectiveness. */
    effectiveness_rating?: string,
    /** Date the control was last tested. */
    last_test_date?: date,
    /** References to evidence of implementation. */
    evidence_references?: string[],
}


/**
 * An AI system within the AIMS scope. Captures life cycle stage, intended use, applicable domains, and references to data and tooling resources, technical documentation, and impact assessments.
 */
export interface AISystem extends NamedEntity {
    /** Purpose of the AI system. */
    ai_system_purpose?: string,
    /** Documented intended uses of the AI system. */
    intended_uses?: string[],
    /** Reasonably foreseeable misuse of the AI system. */
    foreseeable_misuse?: string[],
    /** Domain in which the AI system is applied (e.g., health, finance). */
    application_domain?: string,
    /** Operational context in which the AI system is deployed. */
    deployment_context?: string,
    /** Current life cycle stage of the AI system. */
    lifecycle_stage?: string,
    /** The organization's role with respect to this AI system (provider, producer, customer, partner). */
    organization_role?: string,
    /** Description of the level of autonomy and human oversight required for this AI system. Free-form text complements `human_oversight_required` and `human_oversight_description`. */
    autonomy_level?: string,
    /** Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in Annex B.6.2.3. */
    ml_approach?: string,
    /** Whether human oversight is required for outputs of the AI system (Annex A.9, Annex B.9.3). */
    human_oversight_required?: boolean,
    /** Description of human-oversight arrangements, including review points, escalation paths, and oversight authority (Annex B.9.3). */
    human_oversight_description?: string,
    /** AI system life cycle stages at which human oversight applies (Annex B.9.3). */
    human_oversight_stages?: string,
    /** Learning paradigm of the AI system (informs Clause 6.1 risk and Annex A.6.2.6 monitoring considerations). */
    learning_mode?: string,
    /** Data resources used by the AI system. */
    data_resources?: DataResourceId[],
    /** Tooling resources used by the AI system. */
    tooling_resources?: ToolingResourceId[],
    /** System and computing resources used by the AI system. */
    computing_resources?: ComputingResourceId[],
    /** Human resources involved with the AI system. */
    human_resources?: HumanResourceId[],
    /** Reference to AI system technical documentation. */
    technical_documentation?: string[],
    /** Policy for AI system event log recording across life cycle phases. */
    event_log_policy?: string,
    /** Reference controls related to this policy or AI system. */
    applicable_controls?: AIReferenceControlId[],
    /** Impact assessments related to this AI system. */
    related_impact_assessments?: AISystemImpactAssessmentId[],
    /** Supplier relationships relevant to this AI system. */
    supplier_relationships?: SupplierRelationshipId[],
    /** Customer relationships relevant to this AI system. */
    customer_relationships?: CustomerRelationshipId[],
}


/**
 * A data resource used by an AI system per Annex A.7. Includes data acquisition, quality, provenance, and preparation metadata.
 */
export interface DataResource extends NamedEntity {
    /** Category of data resource (training, validation, test, production). */
    data_resource_category?: string,
    /** Source from which the data was obtained. */
    source?: string,
    /** How the data was acquired (e.g., collected, purchased, synthetic). */
    acquisition_method?: string,
    /** Documented data quality requirements for the AI system. */
    data_quality_requirements?: string[],
    /** Measured data quality metrics. */
    data_quality_metrics?: string[],
    /** Provenance information for the data resource. */
    data_provenance?: string,
    /** Description of the data labelling process. */
    labelling_process?: string,
    /** Data preparation methods used (e.g., scaling, encoding, cleaning) per Annex A.7.6. */
    data_preparation_methods?: string,
    /** Date the data was last updated or modified. */
    last_updated_date?: date,
    /** Known or potential bias issues in the data. */
    known_bias_issues?: string[],
    /** Retention and disposal policy applicable to the data. */
    retention_policy?: string,
    /** Classification of the data resource. */
    data_classification?: string,
}


/**
 * A tooling resource (algorithm, framework, model, library) used in an AI system per A.4.4.
 */
export interface ToolingResource extends NamedEntity {
    /** Category of tooling resource (algorithm, framework, model, library). */
    tool_category?: string,
    /** Version identifier for the tooling resource. */
    tool_version?: string,
    /** Vendor or origin of the tooling resource. */
    vendor?: string,
    /** License terms applicable to the tooling resource. */
    license_terms?: string,
    /** Purpose for which the tooling resource is used. */
    usage_purpose?: string,
}


/**
 * A system or computing resource used in the development or operation of an AI system per A.4.5.
 */
export interface ComputingResource extends NamedEntity {
    /** Class of computing resource (e.g., GPU cluster, edge device). */
    resource_class?: string,
    /** Quantity of the resource. */
    quantity?: string,
    /** Physical or logical location of the resource. */
    location?: string,
    /** Type of environment (development, staging, production). */
    environment_type?: string,
    /** Cost of the resource. */
    cost?: string,
}


/**
 * A human resource (role, expertise area) involved in development, deployment, operation, maintenance, or oversight of an AI system per A.4.6.
 */
export interface HumanResource extends NamedEntity {
    /** Competencies required for the role. */
    required_competencies?: string[],
    /** Person(s) assigned to this role or resource. */
    assigned_to?: string[],
    /** Life cycle responsibilities allocated to this human resource. */
    lifecycle_responsibilities?: string[],
}


/**
 * A resource provided for the AIMS per Clause 7.1.
 */
export interface Resource extends NamedEntity {
    /** Type of resource. */
    resource_type?: string,
    /** Quantity of the resource. */
    quantity?: string,
    /** Date the resource was allocated. */
    allocation_date?: date,
    /** What the resource is allocated to. */
    allocated_to?: string,
    /** Cost of the resource. */
    cost?: string,
    /** Current availability of the resource. */
    availability_status?: string,
}


/**
 * Evidence of competence for personnel affecting AIMS performance per Clause 7.2.
 */
export interface CompetenceRecord extends DocumentedInformation {
    /** Name of the person. */
    person_name?: string,
    /** Role of the person. */
    person_role?: string,
    /** Competencies required for the role. */
    required_competencies?: string[],
    /** Education qualifications. */
    education_records?: string[],
    /** Training completed. */
    training_records?: string[],
    /** Relevant experience. */
    experience_records?: string[],
    /** Date of last competency assessment. */
    competency_assessment_date?: date,
    /** Identified competency gaps. */
    competency_gaps?: string[],
    /** Actions to address competency gaps. */
    development_actions?: string[],
}


/**
 * The awareness program ensuring personnel understand their AI-related responsibilities per Clause 7.3.
 */
export interface AwarenessProgram extends DocumentedInformation {
    /** Topics covered in the awareness program. */
    awareness_topics?: string[],
    /** Methods used to deliver awareness content. */
    delivery_methods?: string[],
    /** Intended audience for the policy or document. */
    target_audience?: string,
    /** Frequency of the activity. */
    frequency?: string,
    /** How completion is tracked. */
    completion_tracking?: string,
    /** How effectiveness is measured. */
    effectiveness_measures?: string,
}


/**
 * Plan for internal and external communications relevant to the AIMS per Clause 7.4.
 */
export interface CommunicationPlan extends DocumentedInformation {
    /** Communication items in the plan. */
    communication_items?: CommunicationItem[],
}


/**
 * A single communication requirement within the AIMS communication plan.
 */
export interface CommunicationItem {
    /** Subject of the communication. */
    subject?: string,
    /** Purpose of the communication. */
    purpose?: string,
    /** Target audience. */
    audience?: string,
    /** Frequency of the activity. */
    frequency?: string,
    /** Method of communication. */
    method?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Records required to evidence the activity. */
    records_required?: string,
}


/**
 * A documented procedure for operational planning and control of AIMS processes per Clause 8.1, including AI system life cycle related controls.
 */
export interface OperationalProcedure extends DocumentedInformation {
    /** Scope of the procedure. */
    procedure_scope?: string,
    /** Criteria for the process. */
    process_criteria?: string,
    /** Control measures applied. */
    control_measures?: string[],
    /** Roles responsible for the process. */
    responsible_roles?: RoleId[],
    /** Other reference controls related to this one. */
    related_controls?: AIReferenceControlId[],
    /** Requirements for controlling changes to the process. */
    change_control_requirements?: string,
}


/**
 * The program for monitoring, measurement, analysis, and evaluation of AIMS performance per Clause 9.1.
 */
export interface MonitoringProgram extends DocumentedInformation {
    /** Items to be monitored. */
    monitoring_items?: MonitoringItem[],
}


/**
 * A single item to be monitored and measured per Clause 9.1.
 */
export interface MonitoringItem {
    /** Name of the metric. */
    metric_name?: string,
    /** Description of the metric. */
    metric_description?: string,
    /** Method used to measure the metric. */
    measurement_method?: string,
    /** How often measurement is performed. */
    measurement_frequency?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Frequency of analysis. */
    analysis_frequency?: string,
    /** Person performing the analysis. */
    analyst?: string,
    /** Target threshold for the metric. */
    target_threshold?: string,
    /** Threshold that triggers an alert. */
    alert_threshold?: string,
    /** Current measured value. */
    current_value?: string,
    /** Observed trend in the metric. */
    trend?: string,
}


/**
 * An internal audit instance per Clause 9.2 assessing AIMS conformance and effectiveness.
 */
export interface InternalAudit extends DocumentedInformation {
    /** Unique reference identifier for the audit. */
    audit_reference?: string,
    /** Type of audit (internal, external second-party, external third-party, surveillance, recertification, combined). */
    audit_type?: string,
    /** Scope of the audit. */
    audit_scope?: string,
    /** Criteria used for the audit. */
    audit_criteria?: string,
    /** Objectives of the audit. */
    audit_objectives?: string,
    /** Start date of the audit period. */
    audit_period_start?: date,
    /** End date of the audit period. */
    audit_period_end?: date,
    /** Lead auditor for the audit. */
    lead_auditor?: string,
    /** Members of the audit team. */
    audit_team?: string[],
    /** Representatives of the auditee. */
    auditee_representatives?: string[],
    /** Reference to the audit plan. */
    audit_plan?: string,
    /** Findings from the audit. */
    findings?: AuditFindingId[],
    /** Positive observations from the audit. */
    positive_observations?: string[],
    /** Overall conclusion of the audit. */
    audit_conclusion?: string,
    /** Date the audit report was issued. */
    report_date?: date,
    /** Distribution list for the audit report. */
    report_distribution?: string[],
}


/**
 * The internal audit programme per Clause 9.2.2, planning AIMS audit activities over a defined period.
 */
export interface AuditProgramme extends DocumentedInformation {
    /** Period covered by the audit programme. */
    programme_period?: string,
    /** Audits planned within the programme. */
    planned_audits?: InternalAuditId[],
    /** Rationale for the audit cadence. */
    audit_frequency_rationale?: string,
    /** Resources required for the activity. */
    resource_requirements?: string,
    /** Required auditor qualifications. */
    auditor_qualifications?: string,
    /** Status of the audit programme. */
    programme_status?: string,
}


/**
 * A finding from an AIMS internal audit, including nonconformities, observations, and positive findings.
 */
export interface AuditFinding extends NamedEntity {
    /** Type of audit finding. */
    finding_type?: string,
    /** ISO/IEC 42001 clause referenced by the finding. */
    clause_reference?: string,
    /** Reference to an Annex A control (e.g., A.6.2.4). */
    control_reference?: AIReferenceControlId,
    /** Description of the finding. */
    finding_description?: string,
    /** Objective evidence supporting the finding. */
    objective_evidence?: string,
    /** Analysis of the root cause. */
    root_cause_analysis?: string,
    /** AI risk implication of the finding. */
    risk_implication?: string,
    /** Recommended action to address the finding. */
    recommended_action?: string,
    /** Auditee's response to the finding. */
    auditee_response?: string,
    /** Linked corrective action addressing the finding. */
    linked_corrective_action?: CorrectiveActionId,
    /** Closure status of the finding. */
    closure_status?: string,
    /** Date when the item was closed. */
    closure_date?: date,
}


/**
 * A management review per Clause 9.3, conducted by top management to evaluate ongoing AIMS suitability, adequacy, and effectiveness.
 */
export interface ManagementReview extends DocumentedInformation {
    /** Date when the document is due for review. */
    review_date?: date,
    /** Attendees of the review. */
    attendees?: string[],
    /** Status of actions from previous reviews. */
    previous_actions_status?: string,
    /** Changes in external or internal context. */
    context_changes?: string[],
    /** Changes in interested party needs and expectations. */
    interested_party_changes?: string[],
    /** Trends in AIMS performance. */
    performance_trends?: string,
    /** Summary of audit results. */
    audit_results_summary?: string,
    /** Summary of AI risk assessment results. */
    risk_assessment_results?: string,
    /** Summary of AI system impact assessment results. */
    impact_assessment_results?: string,
    /** Improvement opportunities identified. */
    improvement_opportunities?: ImprovementOpportunityId[],
    /** Decisions made during the review. */
    decisions?: string[],
    /** Action items resulting from the review. */
    action_items?: string[],
    /** Date of the next review. */
    next_review_date?: date,
}


/**
 * A nonconformity identified per Clause 10.2 representing failure to fulfill an AIMS requirement.
 */
export interface Nonconformity extends NamedEntity {
    /** Source from which the nonconformity was identified. */
    nonconformity_source?: string,
    /** Date the nonconformity was detected. */
    detection_date?: date,
    /** Person or process that detected the nonconformity. */
    detected_by?: string,
    /** Requirement that was violated. */
    requirement_violated?: string,
    /** Description of the nonconformity. */
    nonconformity_description?: string,
    /** Immediate actions taken. */
    immediate_actions?: string[],
    /** How consequences were addressed. */
    consequences_addressed?: string,
    /** Identified root cause. */
    root_cause?: string,
    /** Check for similar nonconformities. */
    similar_nonconformities_check?: string,
    /** Linked corrective actions. */
    linked_corrective_actions?: CorrectiveActionId[],
    /** Current status of the document or entity. */
    status?: string,
    /** Date when the item was closed. */
    closure_date?: date,
    /** Evidence of closure. */
    closure_evidence?: string,
}


/**
 * A corrective action per Clause 10.2 to address the root cause of an AIMS nonconformity and reduce the likelihood of recurrence.
 */
export interface CorrectiveAction extends NamedEntity {
    /** Linked nonconformity. */
    linked_nonconformity?: NonconformityId,
    /** Description of the action. */
    action_description?: string,
    /** Root cause addressed by the action. */
    root_cause_addressed?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Target completion date. */
    target_completion_date?: date,
    /** Actual completion date. */
    actual_completion_date?: date,
    /** Resources required for implementation. */
    resources_required?: string,
    /** Criteria for assessing effectiveness. */
    effectiveness_criteria?: string,
    /** Date when effectiveness was reviewed. */
    effectiveness_review_date?: date,
    /** Whether effectiveness was verified. */
    effectiveness_verified?: boolean,
    /** Whether AIMS changes are required as a result of the action. */
    aims_changes_required?: boolean,
    /** Current status of the document or entity. */
    status?: string,
}


/**
 * An opportunity for continual improvement of the AIMS per Clause 10.1.
 */
export interface ImprovementOpportunity extends NamedEntity {
    /** Source of the improvement opportunity. */
    improvement_source?: string,
    /** Date the improvement opportunity was identified. */
    identification_date?: date,
    /** Person who identified the improvement opportunity. */
    identified_by?: string,
    /** Description of the improvement opportunity. */
    improvement_description?: string,
    /** Expected benefit of the improvement. */
    expected_benefit?: string,
    /** Priority assigned (qualitative level). */
    priority?: string,
    /** Plan for implementing the improvement. */
    implementation_plan?: string,
    /** Party responsible for the activity. */
    responsible_party?: string,
    /** Target date for achieving the objective. */
    target_date?: date,
    /** Actual completion date. */
    actual_completion_date?: date,
    /** Assessment of the outcome. */
    outcome_assessment?: string,
    /** Current status of the document or entity. */
    status?: string,
}


/**
 * A documented relationship with a third party (supplier, partner, or customer) involved in the AI system life cycle per A.10.
 */
export interface ThirdPartyRelationship extends NamedEntity {
    /** Category of party. */
    party_type?: string,
    /** Name of the third party. */
    party_name?: string,
    /** Contractual basis of the relationship. */
    contractual_basis?: string,
    /** Responsibilities allocated to the third party. */
    allocated_responsibilities?: string[],
    /** Role of the third party in data processing (e.g., PII controller, PII processor). */
    data_processing_role?: string,
    /** AI systems involved in the third-party relationship. */
    ai_systems_involved?: AISystemId[],
    /** AI life cycle stages where the third party is involved. */
    lifecycle_stages_involved?: string,
    /** Evidence of assurance over the third party's conformance with the organization's responsible AI approach. */
    assurance_evidence?: string[],
    /** Frequency at which the relationship is reviewed. */
    review_frequency?: string,
}


/**
 * A supplier relationship covering services, products, or materials (e.g., datasets, models, libraries, full AI systems) provided to the organization per A.10.3.
 */
export interface SupplierRelationship extends ThirdPartyRelationship {
    /** Criteria for assessing the supplier. */
    supplier_assessment_criteria?: string[],
    /** How the supplier or customer relationship is monitored. */
    monitoring_method?: string,
    /** Corrective actions required of the supplier. */
    corrective_actions_required?: string[],
}


/**
 * A customer relationship for an AI product or service supplied by the organization per A.10.4.
 */
export interface CustomerRelationship extends ThirdPartyRelationship {
    /** Documented customer expectations and needs. */
    customer_expectations?: string[],
    /** Reference to the usage agreement with the customer. */
    usage_agreement_reference?: string,
    /** Limitations of the AI system that are communicated to the customer. */
    communicated_limitations?: string[],
}


/**
 * An AI system event detected by monitoring, users, or external reporting channels. Events may or may not be subsequently classified as incidents. Supports A.6.2.8 event log capture and A.8.3 external reporting workflows.
 */
export interface AISystemEvent extends NamedEntity {
    /** Date and time the event was observed. */
    event_datetime?: string,
    /** Identifier or description of the person or system that reported the event. */
    reporter?: string,
    /** Type of party that reported the event (internal user, external interested party, monitoring system, etc.). */
    reporter_party_type?: string,
    /** Source channel through which the event was raised (monitoring, user report, external report, audit). */
    event_source?: string,
    /** Free-text description of the event. */
    event_description?: string,
    /** AI systems affected by this risk. */
    affected_ai_systems?: AISystemId[],
    /** Initial triage assessment of the event. */
    initial_assessment?: string,
    /** Whether the event has been categorized as an incident requiring response. */
    categorized_as_incident?: boolean,
    /** AI incident linked to the originating event. */
    linked_incident?: AIIncidentId,
}


/**
 * An AI incident, i.e., an AI system event determined to require response, escalation, or external communication. Captures triage, response lifecycle, and communications to users and other interested parties per A.8.4 and A.8.3.
 */
export interface AIIncident extends NamedEntity {
    /** Date and time the incident was declared or detected. */
    incident_datetime?: string,
    /** AI-specific category of the incident. */
    incident_category?: string,
    /** Severity rating of the incident. */
    severity?: string,
    /** AI systems affected by this risk. */
    affected_ai_systems?: AISystemId[],
    /** Dimensions of impact affected by the risk (individual, group, societal, safety, privacy, security, environmental). */
    affected_dimensions?: string,
    /** Free-text description of the incident. */
    incident_description?: string,
    /** How the incident was detected (monitoring alert, user report, external report). */
    detection_method?: string,
    /** Response actions taken for the incident. */
    response_actions?: string[],
    /** Containment actions taken to limit incident impact. */
    containment_actions?: string[],
    /** Recovery actions taken to restore normal AI system operation. */
    recovery_actions?: string[],
    /** Identified root cause. */
    root_cause?: string,
    /** Lessons learned recorded after incident closure. */
    lessons_learned?: string[],
    /** References to evidence collected during incident response. */
    evidence_collected?: string[],
    /** Whether notification to interested parties or authorities is required. */
    notification_required?: boolean,
    /** Notifications actually made (user communications, regulator filings). */
    notifications_made?: string[],
    /** External reports received or filed regarding the incident. */
    external_reports?: string[],
    /** Reference to the communication plan. */
    communication_plan?: CommunicationPlanId,
    /** Linked corrective actions. */
    linked_corrective_actions?: CorrectiveActionId[],
    /** Date and time the incident was closed. */
    closure_datetime?: string,
    /** Reference to the post-incident review record. */
    post_incident_review?: string,
}


/**
 * A concern raised by employees, contractors, users, or other interested parties about the organization's role with respect to an AI system. Operationalises Annex A.3.3 (Reporting of concerns). Confidentiality, anonymity, anti-reprisal protection, escalation, and timely response are core attributes; informed by ISO 37002.
 */
export interface ConcernReport extends NamedEntity {
    /** Date the concern was reported. */
    reported_date?: date,
    /** Identifier or description of the person or system that reported the event. */
    reporter?: string,
    /** Type of party that reported the event (internal user, external interested party, monitoring system, etc.). */
    reporter_party_type?: string,
    /** Whether the reporter chose to remain anonymous. */
    reporter_anonymous?: boolean,
    /** Confidentiality classification applied to the concern record (e.g., confidential, restricted, internal). */
    confidentiality_level?: string,
    /** Channel through which the concern was reported (e.g., hotline, web form, manager, ombudsperson, external auditor). */
    reporting_channel?: string,
    /** Paraphrased summary of the concern raised. */
    concern_description?: string,
    /** AI systems referenced in the concern report. */
    concern_ai_systems?: AISystemId[],
    /** AI system life cycle stage(s) at which the concern arose. */
    concern_lifecycle_stage?: string,
    /** Severity rating of the incident. */
    severity?: string,
    /** Identifier or description of the investigator assigned to the concern. */
    investigator?: string,
    /** Status of the investigation (e.g., opened, in_progress, closed, escalated, referred_external). */
    investigation_status?: string,
    /** Paraphrased summary of investigation findings. */
    investigation_findings?: string,
    /** Whether and how the concern was escalated (internal management, governing body, external authority). */
    escalation_status?: string,
    /** Target date by which a response is owed to the reporter. */
    response_due_date?: date,
    /** Date a response was provided to the reporter. */
    response_provided_date?: date,
    /** Paraphrased description of the resolution provided. */
    resolution?: string,
    /** Actions taken to protect the reporter from reprisals or detriment (informed by ISO 37002). */
    reprisal_protection_actions?: string[],
    /** AI incidents linked to this concern report. */
    related_incidents?: AIIncidentId[],
    /** Nonconformities linked to this concern report. */
    related_nonconformities?: NonconformityId[],
    /** Date and time the incident was closed. */
    closure_datetime?: string,
}



