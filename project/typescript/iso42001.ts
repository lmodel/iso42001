export type AimsRecordMixinAimsId = string;
export type AimsManagementSystemAimsId = string;
export type AimsOrganizationAimsId = string;
export type AimsInterestedPartyAimsId = string;
export type AimsPolicyAimsId = string;
export type AimsTopicSpecificPolicyAimsId = string;
export type AimsRoleAimsId = string;
export type AimsObjectiveAimsId = string;
export type AimsPlannedActionAimsId = string;
export type AimsRiskAssessmentProcessAimsId = string;
export type AimsRiskAssessmentAimsId = string;
export type AimsRiskAimsId = string;
export type AimsRiskTreatmentProcessAimsId = string;
export type AimsRiskTreatmentPlanAimsId = string;
export type AimsImpactAssessmentProcessAimsId = string;
export type AimsImpactAssessmentAimsId = string;
export type AimsStatementOfApplicabilityAimsId = string;
export type AimsControlAimsId = string;
export type AimsAiSystemAimsId = string;
export type AimsSystemResourceAimsId = string;
export type AimsComponentResourceAimsId = string;
export type AimsDataResourceAimsId = string;
export type AimsToolingResourceAimsId = string;
export type AimsComputingResourceAimsId = string;
export type AimsHumanResourceAimsId = string;
export type AimsDevelopmentProcessAimsId = string;
export type AimsResponsibleUseProcessAimsId = string;
export type AimsTechnicalDocumentationAimsId = string;
export type AimsUserInformationAimsId = string;
export type AimsIncidentCommunicationPlanAimsId = string;
export type AimsReportingObligationAimsId = string;
export type AimsResourceAimsId = string;
export type AimsCompetenceRecordAimsId = string;
export type AimsAwarenessProgrammeAimsId = string;
export type AimsCommunicationPlanAimsId = string;
export type AimsDocumentedInformationAimsId = string;
export type AimsOperationalProcedureAimsId = string;
export type AimsMonitoringProgrammeAimsId = string;
export type AimsAuditProgrammeAimsId = string;
export type AimsAuditAimsId = string;
export type AimsAuditFindingAimsId = string;
export type AimsManagementReviewAimsId = string;
export type AimsNonconformityAimsId = string;
export type AimsCorrectiveActionAimsId = string;
export type AimsImprovementOpportunityAimsId = string;
export type AimsThirdPartyRelationshipAimsId = string;
export type AimsSupplierRelationshipAimsId = string;
export type AimsCustomerRelationshipAimsId = string;
export type AimsSystemEventAimsId = string;
export type AimsIncidentAimsId = string;
export type AimsConcernReportingProcessAimsId = string;
export type AimsConcernReportAimsId = string;
/**
* The numbered clauses and subclauses of the standard from 4 to 10, by their numbers. A value's description is this project's own summary, and the clause headings and the requirements are ISO's.
*/
export enum AimsClause {
    
    /** Why the system exists and what it reaches. */
    number_4 = "clause_4",
    /** Matters inside and outside that bear on the system, climate among them, and the part the organization plays with AI. */
    number_4FULL_STOP1 = "clause_4_1",
    /** Who has a stake in the system, and what they want from it. */
    number_4FULL_STOP2 = "clause_4_2",
    /** Where the system stops, stated in writing. */
    number_4FULL_STOP3 = "clause_4_3",
    /** Having the system and its processes in place, and keeping them up. */
    number_4FULL_STOP4 = "clause_4_4",
    /** What top management must do. */
    number_5 = "clause_5",
    /** How top management shows it leads and backs the system. */
    number_5FULL_STOP1 = "clause_5_1",
    /** Management's written direction on AI. */
    number_5FULL_STOP2 = "clause_5_2",
    /** Who holds which duty and power, including who checks conformity and who reports on performance. */
    number_5FULL_STOP3 = "clause_5_3",
    /** Deciding what to do before doing it. */
    number_6 = "clause_6",
    /** Dealing with what could go well or badly. */
    number_6FULL_STOP1 = "clause_6_1",
    /** Criteria for risk, and the actions planned on risks and opportunities. */
    number_6FULL_STOP1FULL_STOP1 = "clause_6_1_1",
    /** A repeatable way to find, analyse and rank AI risks. */
    number_6FULL_STOP1FULL_STOP2 = "clause_6_1_2",
    /** Choosing treatments and controls, with the Statement of Applicability and the plan. */
    number_6FULL_STOP1FULL_STOP3 = "clause_6_1_3",
    /** A way to work out what AI systems may do to people and society. */
    number_6FULL_STOP1FULL_STOP4 = "clause_6_1_4",
    /** Measurable aims for AI, and how each will be reached. */
    number_6FULL_STOP2 = "clause_6_2",
    /** Changing the system in an orderly way. */
    number_6FULL_STOP3 = "clause_6_3",
    /** What the system needs in order to run. */
    number_7 = "clause_7",
    /** Providing what the system needs. */
    number_7FULL_STOP1 = "clause_7_1",
    /** People's ability to do the work, and the evidence of it. */
    number_7FULL_STOP2 = "clause_7_2",
    /** What those who work for the organization must know. */
    number_7FULL_STOP3 = "clause_7_3",
    /** Who is told what, when and how. */
    number_7FULL_STOP4 = "clause_7_4",
    /** Keeping information under control. */
    number_7FULL_STOP5 = "clause_7_5",
    /** Which information the system holds. */
    number_7FULL_STOP5FULL_STOP1 = "clause_7_5_1",
    /** Naming, formatting, reviewing and approving it. */
    number_7FULL_STOP5FULL_STOP2 = "clause_7_5_2",
    /** Keeping it to hand and protected. */
    number_7FULL_STOP5FULL_STOP3 = "clause_7_5_3",
    /** Carrying out what was planned. */
    number_8 = "clause_8",
    /** Running and controlling the processes, including those from outside. */
    number_8FULL_STOP1 = "clause_8_1",
    /** Carrying out risk assessments, on schedule and when things change. */
    number_8FULL_STOP2 = "clause_8_2",
    /** Carrying out the treatment plan and checking that it works. */
    number_8FULL_STOP3 = "clause_8_3",
    /** Carrying out impact assessments, on schedule and when things change. */
    number_8FULL_STOP4 = "clause_8_4",
    /** Checking how the system is doing. */
    number_9 = "clause_9",
    /** What is measured, how and when, and what the results mean. */
    number_9FULL_STOP1 = "clause_9_1",
    /** Audits the organization runs on itself. */
    number_9FULL_STOP2 = "clause_9_2",
    /** What such an audit must establish, and how often. */
    number_9FULL_STOP2FULL_STOP1 = "clause_9_2_1",
    /** The plan for those audits, and how impartial they are. */
    number_9FULL_STOP2FULL_STOP2 = "clause_9_2_2",
    /** Top management's own look at the system. */
    number_9FULL_STOP3 = "clause_9_3",
    /** How often it looks, and to what end. */
    number_9FULL_STOP3FULL_STOP1 = "clause_9_3_1",
    /** What it must take in. */
    number_9FULL_STOP3FULL_STOP2 = "clause_9_3_2",
    /** What it must produce. */
    number_9FULL_STOP3FULL_STOP3 = "clause_9_3_3",
    /** Getting better and putting things right. */
    number_10 = "clause_10",
    /** Making the system better over time. */
    number_10FULL_STOP1 = "clause_10_1",
    /** Dealing with an unmet requirement and removing its cause. */
    number_10FULL_STOP2 = "clause_10_2",
};
/**
* The nine areas Annex A sorts its controls into, under names of this project's own. An area's number is its annotation.
*/
export enum AimsControlArea {
    
    /** Written direction from management on AI, and how it fits with other policies. */
    AFULL_STOP2 = "policy_direction",
    /** Who answers for AI within the organization's walls, and the way worries are raised. */
    AFULL_STOP3 = "accountability",
    /** What each AI system draws on: components, data, tools, computing and people. */
    AFULL_STOP4 = "system_resources",
    /** Working out what AI systems may do to people and society. */
    AFULL_STOP5 = "impact_assessment",
    /** Building and running AI systems, from the goals set for them to their logs. */
    AFULL_STOP6 = "system_life_cycle",
    /** The data AI systems use: how it is managed, obtained, kept fit, traced and readied. */
    AFULL_STOP7 = "data_management",
    /** What users and others are told about a system, and their way to report harm. */
    AFULL_STOP8 = "stakeholder_information",
    /** How AI systems are put to use, against the organization's goals and the systems' documents. */
    AFULL_STOP9 = "responsible_use",
    /** Duties shared with partners, suppliers and customers. */
    AFULL_STOP10 = "external_relationships",
};
/**
* The 38 reference controls of Annex A. A value's title holds the control's number and a name of this project's own, and its description says in this project's words what the control asks for. The headings and the control text are ISO's.
*/
export enum AimsAnnexAControl {
    
    /** Set down in writing how the organization means to treat AI systems. */
    AFULL_STOP2FULL_STOP2_Written_direction_on_AI = "a_2_2",
    /** Find where the organization's other policies touch its aims for AI, in either direction. */
    AFULL_STOP2FULL_STOP3_Fit_with_other_policies = "a_2_3",
    /** Look at the AI policy again on a schedule and whenever the need arises, to see that it still serves. */
    AFULL_STOP2FULL_STOP4_Regular_policy_check = "a_2_4",
    /** Decide who carries which duty for AI, as the organization's needs dictate. */
    AFULL_STOP3FULL_STOP2_Who_answers_for_what = "a_3_2",
    /** Give people a way to raise worries about the organization's part in a system, at any point in that system's life. */
    AFULL_STOP3FULL_STOP3_A_way_to_raise_worries = "a_3_3",
    /** List what each stage of a system's life, and other AI work, draws on. */
    AFULL_STOP4FULL_STOP2_Inventory_of_what_is_needed = "a_4_2",
    /** Record facts about the data a system draws on. */
    AFULL_STOP4FULL_STOP3_Record_of_data_used = "a_4_3",
    /** Record facts about the tools a system draws on. */
    AFULL_STOP4FULL_STOP4_Record_of_tools_used = "a_4_4",
    /** Record facts about the hardware and computing a system draws on. */
    AFULL_STOP4FULL_STOP5_Record_of_infrastructure_used = "a_4_5",
    /** Record who works on a system across its whole life, and what skills they bring. */
    AFULL_STOP4FULL_STOP6_Record_of_people_used = "a_4_6",
    /** Set up a way to work out what a system could do to people and society over its life. */
    AFULL_STOP5FULL_STOP2_Method_for_weighing_consequences = "a_5_2",
    /** Write down what each impact assessment found, and hold on to it for a set time. */
    AFULL_STOP5FULL_STOP3_Keeping_assessment_results = "a_5_3",
    /** Work out and record how a system could affect single persons or particular groups over its life. */
    AFULL_STOP5FULL_STOP4_Effects_on_people = "a_5_4",
    /** Work out and record how a system could affect society over its life. */
    AFULL_STOP5FULL_STOP5_Effects_on_society = "a_5_5",
    /** Set goals that steer responsible building, and work measures for them into the development cycle. */
    AFULL_STOP6FULL_STOP1FULL_STOP2_Goals_for_building = "a_6_1_2",
    /** Set down the particular processes for designing and building a system responsibly. */
    AFULL_STOP6FULL_STOP1FULL_STOP3_Defined_ways_of_building = "a_6_1_3",
    /** Write down what a new system, or a large upgrade to one, must meet. */
    AFULL_STOP6FULL_STOP2FULL_STOP2_What_a_system_must_do = "a_6_2_2",
    /** Write down how a system was designed and built, against the goals and the requirements. */
    AFULL_STOP6FULL_STOP2FULL_STOP3_Build_records = "a_6_2_3",
    /** Set the checks that verify and validate a system, and say when each applies. */
    AFULL_STOP6FULL_STOP2FULL_STOP4_Checks_and_their_criteria = "a_6_2_4",
    /** Keep a plan for putting a system into service, and meet its conditions first. */
    AFULL_STOP6FULL_STOP2FULL_STOP5_Going_live = "a_6_2_5",
    /** Set down what keeping a system in service takes: at least watching it, fixing it, updating it and supporting it. */
    AFULL_STOP6FULL_STOP2FULL_STOP6_Running_and_watching = "a_6_2_6",
    /** Decide what technical documents each kind of reader needs, and give them those documents in a suitable form. */
    AFULL_STOP6FULL_STOP2FULL_STOP7_Documents_per_audience = "a_6_2_7",
    /** Decide at which points in a system's life it keeps event logs, and keep them at least while it is in service. */
    AFULL_STOP6FULL_STOP2FULL_STOP8_Keeping_logs = "a_6_2_8",
    /** Set down and follow processes that manage the data used to build systems. */
    AFULL_STOP7FULL_STOP2_Managing_data_for_building = "a_7_2",
    /** Record how the data a system uses was obtained and picked. */
    AFULL_STOP7FULL_STOP3_Obtaining_and_choosing_data = "a_7_3",
    /** State what quality data must have, and see that the data used to build and run a system has it. */
    AFULL_STOP7FULL_STOP4_Data_fit_for_purpose = "a_7_4",
    /** Keep a process that records where data came from and what happened to it, while it and the system last. */
    AFULL_STOP7FULL_STOP5_Tracing_where_data_came_from = "a_7_5",
    /** Set criteria for choosing how data is made ready, and name the methods to use. */
    AFULL_STOP7FULL_STOP6_Readying_data = "a_7_6",
    /** Work out what those who use a system need to know, and tell them. */
    AFULL_STOP8FULL_STOP2_What_users_are_told = "a_8_2",
    /** Give people outside the organization a way to report harm a system has done. */
    AFULL_STOP8FULL_STOP3_Letting_outsiders_report_harm = "a_8_3",
    /** Keep a plan for telling those who use a system when something goes wrong. */
    AFULL_STOP8FULL_STOP4_Telling_users_about_incidents = "a_8_4",
    /** Work out what the organization owes others by way of reports about a system. */
    AFULL_STOP8FULL_STOP5_Duties_to_inform_others = "a_8_5",
    /** Set down the processes for using AI systems responsibly. */
    AFULL_STOP9FULL_STOP2_Defined_ways_of_using = "a_9_2",
    /** Set goals that steer how AI systems are used responsibly. */
    AFULL_STOP9FULL_STOP3_Goals_for_use = "a_9_3",
    /** See that a system is used only as intended and as its documents say. */
    AFULL_STOP9FULL_STOP4_Staying_within_documented_use = "a_9_4",
    /** Settle who carries which duty across a system's life, among the organization and those it deals with. */
    AFULL_STOP10FULL_STOP2_Sharing_out_duties = "a_10_2",
    /** Keep a process that holds what suppliers provide to how the organization means to treat AI. */
    AFULL_STOP10FULL_STOP3_What_is_bought_in = "a_10_3",
    /** See that how the organization treats AI takes account of what its customers expect and want. */
    AFULL_STOP10FULL_STOP4_BuyersAPOSTROPHE_needs = "a_10_4",
};
/**
* The eight stages of the generic life cycle model that ISO/IEC 22989:2022 gives, which ISO/IEC 42001 points to.
*/
export enum AimsLifecycleStage {
    
    /** Someone sees a need, weighs whether to meet it, and sets goals. */
    inception = "inception",
    /** The system is designed and built. */
    design_and_development = "design_and_development",
    /** The system is checked against what was asked of it. */
    verification_and_validation = "verification_and_validation",
    /** The system is put into service. */
    deployment = "deployment",
    /** The system runs and is watched. */
    operation_and_monitoring = "operation_and_monitoring",
    /** A system that goes on learning is checked again as it changes. */
    continuous_validation = "continuous_validation",
    /** The system's results are weighed against its goals afresh. */
    re_evaluation = "re_evaluation",
    /** The system is taken out of service. */
    retirement = "retirement",
};
/**
* The parts an organization or a person can play towards AI systems. The six families are those of ISO/IEC 22989:2022, and each more specific role names its family in an annotation.
*/
export enum AimsAiRole {
    
    /** Offers AI systems or platforms to others. */
    ai_provider = "ai_provider",
    /** Offers a platform that others build AI services on. */
    ai_platform_provider = "ai_platform_provider",
    /** Offers goods or services that hold an AI system. */
    ai_product_or_service_provider = "ai_product_or_service_provider",
    /** Makes AI systems. */
    ai_producer = "ai_producer",
    /** Writes and trains what goes into a system. */
    ai_developer = "ai_developer",
    /** Decides how a system should work. */
    ai_designer = "ai_designer",
    /** Keeps a system running. */
    ai_operator = "ai_operator",
    /** Checks how well a system does. */
    ai_tester_or_evaluator = "ai_tester_or_evaluator",
    /** Puts a system into service. */
    ai_deployer = "ai_deployer",
    /** Looks after how people and a system work together. */
    ai_human_factor_professional = "ai_human_factor_professional",
    /** Knows the field a system is used in. */
    domain_expert = "domain_expert",
    /** Weighs what a system may do to people and society. */
    ai_impact_assessor = "ai_impact_assessor",
    /** Buys systems or their parts. */
    procurer = "procurer",
    /** Oversees how AI is run and held to account. */
    ai_governance_professional = "ai_governance_professional",
    /** Takes AI systems from a provider. */
    ai_customer = "ai_customer",
    /** Works with a system directly. */
    ai_user = "ai_user",
    /** Helps others make or run AI systems. */
    ai_partner = "ai_partner",
    /** Joins a system to others. */
    ai_system_integrator = "ai_system_integrator",
    /** Supplies data for a system. */
    data_provider = "data_provider",
    /** Is affected by what a system decides or does. */
    ai_subject = "ai_subject",
    /** Is someone a system's data is about. */
    data_subject = "data_subject",
    /** Is affected in some other way. */
    other_subject = "other_subject",
    /** Sets or enforces rules for AI. */
    relevant_authority = "relevant_authority",
    /** Sets the rules. */
    policymaker = "policymaker",
    /** Enforces the rules. */
    regulator = "regulator",
};
/**
* The parts a party can play when personal data passes through AI, which ISO/IEC 29100 describes.
*/
export enum AimsPiiRole {
    
    /** Decides why and how personal data is processed. */
    pii_controller = "pii_controller",
    /** Makes those decisions together with another party. */
    joint_pii_controller = "joint_pii_controller",
    /** Processes personal data on a controller's behalf. */
    pii_processor = "pii_processor",
};
/**
* What an AI objective is for. Clause 6.2 asks for objectives in general, and two Annex A controls ask for objectives of a narrower kind.
*/
export enum AimsObjectivePurpose {
    
    /** An objective for the whole system. */
    organizational = "organizational",
    /** A goal that steers how systems are built. */
    responsible_development = "responsible_development",
    /** A goal that steers how systems are used. */
    responsible_use = "responsible_use",
};
/**
* Kinds of objective an organization may set for AI: those Annex C lists, two more from the guidance on responsible use, and other.
*/
export enum AimsObjectiveCategory {
    
    /** Someone stays answerable for what a system helps to do. */
    accountability = "accountability",
    /** The organization has people with the skills AI calls for. */
    ai_expertise = "ai_expertise",
    /** Good data to train and check a system is to hand. */
    training_and_test_data = "training_and_test_data",
    /** A system's effect on the environment is kept in view. */
    environmental_impact = "environmental_impact",
    /** Automated decisions do not wrong particular persons or groups. */
    fairness = "fairness",
    /** Defects can be mended and new needs met. */
    maintainability = "maintainability",
    /** Data about people, sensitive data above all, is neither misused nor exposed. */
    privacy = "privacy",
    /** A system does as well on unseen data as on what it was trained on. */
    robustness = "robustness",
    /** Nobody's life or health, and no property or part of nature, comes to harm. */
    safety = "safety",
    /** Threats peculiar to AI are met, beyond the usual ones. */
    security = "security",
    /** Those concerned can see how a system works and why it gave a result. */
    transparency_and_explainability = "transparency_and_explainability",
    /** A system keeps doing what it is meant to. */
    reliability = "reliability",
    /** A system can be used by people with differing abilities. */
    accessibility = "accessibility",
    /** A kind of objective the organization sets for itself. */
    other = "other",
};
/**
* Kinds of source a risk from AI can come from: those Annex C lists, and other.
*/
export enum AimsRiskSourceCategory {
    
    /** A system works where situations vary widely, so its results are less sure. */
    complex_environment = "complex_environment",
    /** The organization cannot tell people enough about a system. */
    opaque_system = "opaque_system",
    /** How much a system does alone, which bears on safety or fairness among others. */
    level_of_automation = "level_of_automation",
    /** The data a model learns from, or how it was gathered, is flawed. */
    machine_learning = "machine_learning",
    /** Faulty parts, or moving a trained model to other equipment. */
    hardware = "hardware",
    /** Flaws anywhere in a system's life, from design to retirement. */
    life_cycle = "life_cycle",
    /** A technology is too new to know well, or so old it breeds complacency. */
    technology_readiness = "technology_readiness",
    /** A source the organization names for itself. */
    other = "other",
};
/**
* Who an AI system's impact falls on.
*/
export enum AimsImpactSubject {
    
    /** Particular persons. */
    individuals = "individuals",
    /** Groups of persons, such as children or workers. */
    groups_of_individuals = "groups_of_individuals",
    /** Society at large. */
    societies = "societies",
};
/**
* Areas where AI systems can touch people or society: those the guidance on impact assessment names as examples, and other.
*/
export enum AimsImpactArea {
    
    /** Treating persons and groups even-handedly. */
    fairness = "fairness",
    /** Someone staying answerable for the outcome. */
    accountability = "accountability",
    /** Being able to see how a system works and why it gave a result. */
    transparency_and_explainability = "transparency_and_explainability",
    /** Keeping people's information safe and private. */
    security_and_privacy = "security_and_privacy",
    /** Physical and mental harm and wellbeing. */
    safety_and_health = "safety_and_health",
    /** What people stand to gain or lose in money. */
    financial = "financial",
    /** Whether people with differing abilities can use a system. */
    accessibility = "accessibility",
    /** Rights everyone holds. */
    human_rights = "human_rights",
    /** Natural resources and emissions. */
    environmental_sustainability = "environmental_sustainability",
    /** Jobs, access to finance, taxes and trade. */
    economic = "economic",
    /** Lawmaking, political falsehoods, defence of the state and the courts. */
    government = "government",
    /** What a society holds to, and the biases a system can feed. */
    culture_and_values = "culture_and_values",
    /** An area the organization names for itself. */
    other = "other",
};
/**
* Whether an impact helps or harms.
*/
export enum AimsImpactDirection {
    
    /** It helps. */
    positive = "positive",
    /** It harms. */
    negative = "negative",
};
/**
* Who provides a resource an AI system draws on.
*/
export enum AimsResourceProvider {
    
    /** The organization itself. */
    organization = "organization",
    /** One of its customers. */
    customer = "customer",
    /** Someone else. */
    third_party = "third_party",
};
/**
* The parts data can play in machine learning.
*/
export enum AimsDataCategory {
    
    /** Data a model learns from. */
    training = "training",
    /** Data used to tune a model and compare versions of it. */
    validation = "validation",
    /** Data held back to see how a finished model does. */
    test = "test",
    /** Data a system meets in service. */
    production = "production",
};
/**
* Common ways of making data ready for AI: those the guidance names, and other.
*/
export enum AimsDataPreparationMethod {
    
    /** Looking at how the values are spread, and describing them. */
    statistical_exploration = "statistical_exploration",
    /** Mending wrong values and dealing with gaps. */
    cleaning = "cleaning",
    /** Filling gaps by a method. */
    imputation = "imputation",
    /** Reshaping values to a common distribution or range. */
    normalization = "normalization",
    /** Bringing values to comparable sizes. */
    scaling = "scaling",
    /** Marking the values a model is to predict. */
    labelling = "labelling",
    /** Turning categories into numbers. */
    encoding = "encoding",
    /** A method the organization names for itself. */
    other = "other",
};
/**
* Threats to information security peculiar to AI: those the guidance names, and other.
*/
export enum AimsAiThreat {
    
    /** Slipping bad data in to spoil what a model learns. */
    data_poisoning = "data_poisoning",
    /** Copying a model by querying it or by taking it. */
    model_stealing = "model_stealing",
    /** Working back from a model to the data it learned from. */
    model_inversion = "model_inversion",
    /** A threat the organization names for itself. */
    other = "other",
};
/**
* How far a control or a plan has been put into effect.
*/
export enum AimsImplementationStatus {
    
    /** Nothing has been done yet. */
    not_started = "not_started",
    /** The work is planned, with a timeline. */
    planned = "planned",
    /** The work is under way. */
    in_progress = "in_progress",
    /** The work is done and in operation. */
    implemented = "implemented",
};
/**
* The ways of treating a risk, by the names ISO 31000 gives them.
*/
export enum AimsRiskTreatmentOption {
    
    /** Change the risk with controls that lower its likelihood or its consequences. */
    modify = "modify",
    /** Keep the risk as it is, with management's approval. */
    retain = "retain",
    /** Remove the risk by stopping or changing what gives rise to it. */
    avoid = "avoid",
    /** Share the risk with another party, such as an insurer or a supplier. */
    share = "share",
};
/**
* A five-point scale of risk level, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.
*/
export enum AimsRiskLevel {
    
    /** Small enough to need no action. */
    very_low = "very_low",
    /** Managed by routine procedures. */
    low = "low",
    /** Needs management's attention and planned controls. */
    medium = "medium",
    /** Needs treatment first and escalation. */
    high = "high",
    /** Threatens the organization's objectives and needs action at once. */
    critical = "critical",
};
/**
* A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.
*/
export enum AimsLikelihood {
    
    /** Not expected to happen. */
    rare = "rare",
    /** Could happen, but is not expected to. */
    unlikely = "unlikely",
    /** Might happen at some point. */
    possible = "possible",
    /** Will probably happen. */
    likely = "likely",
    /** Expected to happen. */
    almost_certain = "almost_certain",
};
/**
* A five-point scale of consequence, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.
*/
export enum AimsConsequence {
    
    /** No noticeable effect. */
    negligible = "negligible",
    /** An effect normal operations absorb. */
    minor = "minor",
    /** An effect that needs management to step in. */
    moderate = "moderate",
    /** A serious effect on people, objectives or reputation. */
    major = "major",
    /** An effect that threatens lives or the organization's survival. */
    severe = "severe",
};
/**
* The kinds of documented information an AimsDocumentedInformation record holds. Policies have records of their own.
*/
export enum AimsDocumentKind {
    
    /** The steps for carrying out an activity the same way each time. */
    procedure = "procedure",
    /** Mandatory requirements for a technology or a process. */
    standard = "standard",
    /** Recommended practice that supports a policy or a procedure. */
    guideline = "guideline",
    /** Evidence of what was done or achieved. */
    record = "record",
    /** How the organization means to reach an objective. */
    plan = "plan",
    /** The formal output of an assessment, audit or review. */
    report = "report",
};
/**
* Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.
*/
export enum AimsAuditType {
    
    /** The organization audits itself, or someone audits it on its behalf. */
    first_party = "first_party",
    /** A party with an interest in the organization audits it, such as a customer. */
    second_party = "second_party",
    /** An independent body audits it, such as a certification body or a regulator. */
    third_party = "third_party",
};
/**
* The kinds of audit finding.
*/
export enum AimsAuditFindingType {
    
    /** A requirement not met in a way that puts the system's results in doubt. */
    major_nonconformity = "major_nonconformity",
    /** A requirement not met in an isolated way that leaves its results in reach. */
    minor_nonconformity = "minor_nonconformity",
    /** A condition that could lead to a nonconformity if left alone. */
    observation = "observation",
    /** Evidence of practice that works well. */
    positive_finding = "positive_finding",
};
/**
* What an incident involving an AI system concerns. ISO/IEC 42001 tells apart an incident of the system itself from one about security of information or about privacy.
*/
export enum AimsIncidentCategory {
    
    /** The system itself misbehaved or failed. */
    ai_system = "ai_system",
    /** Information was exposed, altered or made unavailable. */
    information_security = "information_security",
    /** Personal data was exposed or misused. */
    privacy = "privacy",
    /** Someone or something was put in danger. */
    safety = "safety",
    /** Something the organization names for itself. */
    other = "other",
};
/**
* Management system standards Annex D names as ones to run this system beside, and other.
*/
export enum AimsManagementSystemStandard {
    
    /** Managing information security. */
    iso_iec_27001 = "iso_iec_27001",
    /** Managing privacy of information. */
    iso_iec_27701 = "iso_iec_27701",
    /** Managing quality. */
    iso_9001 = "iso_9001",
    /** Managing food safety. */
    iso_22000 = "iso_22000",
    /** Managing quality of medical devices. */
    iso_13485 = "iso_13485",
    /** Another management system standard, generic or for one sector. */
    other = "other",
};


/**
 * What every record of the system has, so that other records can refer to it: an identifier, a title and a description.
 */
export interface AimsRecordMixin {
    /** The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it. */
    aims_id: string,
    /** The name the organization gives the record. */
    title: string,
    /** What the record says or describes, in the organization's own words. */
    description?: string,
}


/**
 * The control that documented information is kept under: who wrote, owns and approved it, its format and medium, when it takes effect and is looked at again, how it is classified, handed out, stored and changed, how long it is kept, and whether it came from outside.
 */
export interface AimsDocumentControlMixin {
    /** The reference the organization's document control gives it. */
    aims_document_reference?: string,
    /** The version of the document. */
    aims_document_version?: string,
    /** Who wrote the document. */
    aims_document_author?: string,
    /** Who answers for the document's content and upkeep. */
    aims_document_owner?: string,
    /** The document's format, such as its language or software version. */
    aims_document_format?: string,
    /** What the document is held on, such as paper or an electronic system. */
    aims_document_medium?: string,
    /** Who approved the document. */
    aims_document_approver?: string,
    /** When the document was approved. */
    aims_document_approval_date?: date,
    /** When the document takes effect. */
    aims_document_effective_date?: date,
    /** When the document was last reviewed. */
    aims_document_last_review_date?: date,
    /** When the document is next due for review. */
    aims_document_next_review_date?: date,
    /** Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn. */
    aims_document_status?: string,
    /** The information classification the document carries. */
    aims_document_classification?: string,
    /** How long the document is kept, as an ISO 8601 duration. */
    aims_document_retention?: string,
    /** What becomes of the document when that time is up. */
    aims_document_disposition?: string,
    /** Who gets the document, how they reach it and what they may do with it. */
    aims_document_distribution?: string[],
    /** How the document is stored so that it stays legible. */
    aims_document_storage?: string,
    /** How changes to the document are controlled, such as version control. */
    aims_document_change_control?: string,
    /** Whether the document comes from outside the organization and is kept because the system needs it. */
    aims_document_external_origin?: boolean,
    /** Who the document came from, when it comes from outside. */
    aims_document_external_source?: string,
}


/**
 * One organization's management system for AI: its scope and context, and every record it keeps, each kind in a list of its own.
 */
export interface AimsManagementSystem extends AimsRecordMixin {
    /** The organization that runs the system. */
    aims_organization?: AimsOrganization,
    /** The person or group that runs the organization from the very top. */
    aims_top_management?: string,
    /** The body top management answers to, such as a board, where there is one. */
    aims_governing_body?: string,
    /** What shows that top management leads and commits to the system. */
    aims_leadership_evidence?: string[],
    /** How far the system reaches, in the organization's words. */
    aims_scope?: string,
    /** Where the system stops. */
    aims_scope_boundaries?: string[],
    /** What in the organization's work the system applies to. */
    aims_scope_applicability?: string[],
    /** The processes the system needs and how they work together. */
    aims_processes?: string,
    /** The matters inside the organization that bear on the system. */
    aims_internal_issues?: string[],
    /** The matters outside the organization that bear on the system. */
    aims_external_issues?: string[],
    /** The changes to the system that are planned. */
    aims_planned_changes?: string[],
    /** What the system takes from outside the organization and keeps under control. */
    aims_external_services?: string[],
    /** Other standards for management systems that this one is run beside. */
    aims_integrated_standards?: string,
    /** Where the system stands with certification, in the organization's own terms. */
    aims_certification_status?: string,
    /** The body that certifies the system. */
    aims_certification_body?: string,
    /** When the system was certified. */
    aims_certification_date?: date,
    /** When the system is next due for recertification. */
    aims_recertification_date?: date,
    /** The interested parties the system takes into account. */
    aims_interested_parties?: AimsInterestedParty[],
    /** The AI policy. */
    aims_policy?: AimsPolicy,
    /** The policies on single topics under the AI policy. */
    aims_topic_specific_policies?: AimsTopicSpecificPolicy[],
    /** The roles that carry the system's duties and powers. */
    aims_roles?: AimsRole[],
    /** The AI objectives. */
    aims_objectives?: AimsObjective[],
    /** The actions planned on risks and opportunities. */
    aims_planned_actions?: AimsPlannedAction[],
    /** The process for assessing AI risks. */
    aims_risk_assessment_process?: AimsRiskAssessmentProcess,
    /** The process for treating AI risks. */
    aims_risk_treatment_process?: AimsRiskTreatmentProcess,
    /** The process for assessing what AI systems may do to people and society. */
    aims_impact_assessment_process?: AimsImpactAssessmentProcess,
    /** The risk assessments carried out. */
    aims_risk_assessments?: AimsRiskAssessment[],
    /** The risks identified, the risk register. */
    aims_risks?: AimsRisk[],
    /** The risk treatment plans. */
    aims_risk_treatment_plans?: AimsRiskTreatmentPlan[],
    /** The impact assessments carried out. */
    aims_impact_assessments?: AimsImpactAssessment[],
    /** The Statement of Applicability. */
    aims_statement_of_applicability?: AimsStatementOfApplicability,
    /** The controls the organization has determined it needs. */
    aims_controls?: AimsControl[],
    /** The AI systems the management system covers. */
    aims_systems?: AimsAiSystem[],
    /** The resources those AI systems draw on, each told apart by its type. */
    aims_system_resources?: AimsSystemResource[],
    /** The processes for designing and building AI systems responsibly. */
    aims_development_processes?: AimsDevelopmentProcess[],
    /** The processes for using AI systems responsibly. */
    aims_use_processes?: AimsResponsibleUseProcess[],
    /** The technical documents kept for AI systems. */
    aims_technical_documentation?: AimsTechnicalDocumentation[],
    /** What users of AI systems are told. */
    aims_user_information?: AimsUserInformation[],
    /** The plans for telling users about incidents. */
    aims_incident_communication_plans?: AimsIncidentCommunicationPlan[],
    /** What the organization must report to others about AI systems. */
    aims_reporting_obligations?: AimsReportingObligation[],
    /** The relationships with partners, suppliers, buyers and others. */
    aims_third_party_relationships?: AimsThirdPartyRelationship[],
    /** The resources provided for the management system itself. */
    aims_resources?: AimsResource[],
    /** The records of competence. */
    aims_competence_records?: AimsCompetenceRecord[],
    /** The awareness programme. */
    aims_awareness_programme?: AimsAwarenessProgramme,
    /** The plan for communication about the system. */
    aims_communication_plan?: AimsCommunicationPlan,
    /** The documented information the system keeps that no more specific list holds, such as procedures, plans and reports. */
    aims_documented_information?: AimsDocumentedInformation[],
    /** The procedures for planning and running operations. */
    aims_operational_procedures?: AimsOperationalProcedure[],
    /** The programme of monitoring and measurement. */
    aims_monitoring_programme?: AimsMonitoringProgramme,
    /** The audit programmes. */
    aims_audit_programmes?: AimsAuditProgramme[],
    /** The audits of the system, internal and external. */
    aims_audits?: AimsAudit[],
    /** The management reviews. */
    aims_management_reviews?: AimsManagementReview[],
    /** The nonconformities found. */
    aims_nonconformities?: AimsNonconformity[],
    /** The corrective actions taken. */
    aims_corrective_actions?: AimsCorrectiveAction[],
    /** The opportunities for improvement identified. */
    aims_improvements?: AimsImprovementOpportunity[],
    /** The events reported about AI systems, the incidents among them. */
    aims_system_events?: AimsSystemEvent[],
    /** The way people raise worries about the organization's part in AI. */
    aims_concern_reporting_process?: AimsConcernReportingProcess,
    /** The worries people have raised. */
    aims_concern_reports?: AimsConcernReport[],
}


/**
 * The organization that runs the system, with what it needs to know about itself to understand its context and the parts it plays with AI.
 */
export interface AimsOrganization extends AimsRecordMixin {
    /** The organization's registered legal name. */
    aims_organization_legal_name?: string,
    /** Other names the organization trades under. */
    aims_organization_trading_names?: string[],
    /** What kind of organization it is, such as a company, an agency or a charity. */
    aims_organization_kind?: string,
    /** The sectors the organization works in, such as health or finance. */
    aims_organization_sectors?: string[],
    /** How the organization classes its own size. */
    aims_organization_size?: string,
    /** About how many people the organization employs. */
    aims_organization_employee_count?: number,
    /** The countries or regions the organization works in. */
    aims_organization_locations?: string[],
    /** The jurisdictions whose laws and regulations apply to the organization. */
    aims_organization_jurisdictions?: string[],
    /** The organization's parent, if it has one. */
    aims_organization_parent?: string,
    /** The organization's subsidiaries, if it has any. */
    aims_organization_subsidiaries?: string[],
    /** The parts the organization plays towards its AI systems. */
    aims_organization_ai_roles?: string,
    /** The parts the organization plays when its AI systems process personal data. */
    aims_organization_pii_roles?: string,
    /** Whether the organization has found climate change to matter for the system. */
    aims_organization_climate_change_relevant?: boolean,
}


/**
 * A person or organization whose needs and expectations bear on the system, or who may feel its decisions, inside the organization or outside it.
 */
export interface AimsInterestedParty extends AimsRecordMixin {
    /** What kind of interested party it is, in the organization's own terms. */
    aims_party_category?: string,
    /** The parts the party plays towards the organization's AI systems. */
    aims_party_ai_roles?: string,
    /** How the party relates to the organization. */
    aims_party_relationship?: string,
    /** The party's requirements that bear on the system. */
    aims_party_requirements?: string[],
    /** Which of those requirements the system addresses. */
    aims_party_addressed_requirements?: string[],
    /** The party's requirements that concern climate change. */
    aims_party_climate_change_requirements?: string[],
    /** What the party needs to be told, and how. */
    aims_party_communication_needs?: string,
    /** How to reach the party. */
    aims_party_contact?: string,
}


/**
 * The AI policy that top management sets: the organization's commitments and the frame for its AI objectives.
 */
export interface AimsPolicy extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The clauses of the standard the record answers to or concerns. */
    aims_cited_clauses?: string,
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** The policy's own statement, in the organization's words. */
    aims_policy_statement?: string,
    /** How the policy frames the setting of AI objectives. */
    aims_policy_objectives_framework?: string,
    /** The commitments the policy makes, at least to meeting requirements and to improving. */
    aims_policy_commitments?: string[],
    /** The principles that guide what the organization does with AI. */
    aims_policy_principles?: string[],
    /** How departures from the policy are handled. */
    aims_policy_exceptions_process?: string,
    /** What shaped the policy, such as strategy, values, the law or the risks. */
    aims_policy_influences?: string[],
    /** The organization's other policies this one refers to or touches. */
    aims_policy_related_policies?: string[],
    /** When the policy was made known inside the organization. */
    aims_policy_communication_date?: date,
    /** How interested parties can get the policy, where that is fitting. */
    aims_policy_availability?: string,
    /** The role management approved to develop, review and evaluate the policy. */
    aims_policy_review_role?: AimsRoleAimsId,
    /** How often the policy is reviewed, as an ISO 8601 duration. */
    aims_policy_review_interval?: string,
}


/**
 * A policy on one topic that gives more guidance under the AI policy, such as assessing impacts or building systems.
 */
export interface AimsTopicSpecificPolicy extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The organization's controls that the record concerns. */
    aims_relevant_controls?: AimsControlAimsId[],
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** The topic the policy covers. */
    aims_topic_policy_topic?: string,
    /** The AI policy this policy supports. */
    aims_topic_policy_parent?: AimsPolicyAimsId,
    /** Whom the policy is written for. */
    aims_topic_policy_audience?: string,
}


/**
 * A role in the system, with the duties and powers it carries and who holds it.
 */
export interface AimsRole extends AimsRecordMixin {
    /** What kind of role it is, in the organization's own terms. */
    aims_role_category?: string,
    /** The areas the role covers, such as privacy, safety or human oversight. */
    aims_role_areas?: string[],
    /** The duties assigned to the role. */
    aims_role_responsibilities?: string[],
    /** The powers the role carries. */
    aims_role_authorities?: string[],
    /** Whether the role sees that the system meets the standard. */
    aims_role_ensures_conformity?: boolean,
    /** Whether the role tells top management how the system is doing. */
    aims_role_reports_performance?: boolean,
    /** What the role is accountable for. */
    aims_role_accountability?: string,
    /** The people who hold the role. */
    aims_role_holders?: string[],
    /** How the role may delegate its duties. */
    aims_role_delegation?: string,
    /** The role this role reports to. */
    aims_role_reports_to?: AimsRoleAimsId,
}


/**
 * An AI objective: a result the organization aims for, with how it plans to reach it and how it judges progress.
 */
export interface AimsObjective extends AimsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** The organization's controls that the record concerns. */
    aims_relevant_controls?: AimsControlAimsId[],
    /** The kinds of objective the record bears on. */
    aims_objective_categories?: string,
    /** What the objective is for. */
    aims_objective_purpose?: string,
    /** The objective, as the organization states it. */
    aims_objective_statement?: string,
    /** The value the objective aims for, where it can be measured. */
    aims_objective_target?: string,
    /** The value last measured. */
    aims_objective_current_value?: string,
    /** How the objective's value is defined. */
    aims_objective_metric?: string,
    /** How the value is measured. */
    aims_objective_measurement_method?: string,
    /** How often the value is measured. */
    aims_objective_measurement_frequency?: string,
    /** When the objective is to be reached. */
    aims_objective_target_date?: date,
    /** How far the objective has been reached, in the organization's own terms. */
    aims_objective_achievement?: string,
    /** The risks that help or hinder the objective. */
    aims_objective_risks?: AimsRiskAimsId[],
    /** The steps that lead to the objective. */
    aims_objective_action_plan?: string,
    /** The resources needed to reach the objective. */
    aims_objective_resources?: string,
    /** How the outcome will be judged. */
    aims_objective_evaluation?: string,
    /** How the objective is made known. */
    aims_objective_communication?: string,
}


/**
 * An action planned on a risk or an opportunity the system faces, with how it fits the system's processes and how its effect will be judged.
 */
export interface AimsPlannedAction extends AimsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The risks the action addresses. */
    aims_planned_action_risks?: AimsRiskAimsId[],
    /** The opportunities the action addresses. */
    aims_planned_action_opportunities?: string[],
    /** How the action fits into the system's processes. */
    aims_planned_action_integration?: string,
    /** How the action's effect will be judged. */
    aims_planned_action_effectiveness?: string,
}


/**
 * The organization's process for assessing AI risks: its criteria, scales and method, and when it runs.
 */
export interface AimsRiskAssessmentProcess extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The criteria for AI risk, which tell acceptable risk from the rest and steer assessment, treatment and the weighing of impacts. */
    aims_risk_criteria?: string[],
    /** How the process follows the AI policy and the AI objectives. */
    aims_risk_policy_alignment?: string,
    /** How the process keeps repeated assessments consistent and comparable. */
    aims_risk_comparability?: string,
    /** The method used to identify, analyse and evaluate risks. */
    aims_risk_method?: string,
    /** The scale for rating likelihood. */
    aims_risk_likelihood_scale?: string,
    /** The scale for rating consequences. */
    aims_risk_consequence_scale?: string,
    /** How likelihood and consequence combine into a risk level. */
    aims_risk_matrix?: string,
    /** How the assessed risks are ranked for treatment. */
    aims_risk_prioritization?: string,
    /** How often risks are assessed, as an ISO 8601 duration. */
    aims_risk_assessment_interval?: string,
    /** The changes that start an assessment outside the schedule. */
    aims_risk_assessment_triggers?: string[],
}


/**
 * One risk assessment carried out under the process, and what it found.
 */
export interface AimsRiskAssessment extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** What the assessment covered. */
    aims_assessment_scope?: string,
    /** When the assessment was carried out. */
    aims_assessment_date?: date,
    /** Who carried out the assessment. */
    aims_assessment_assessor?: string,
    /** The method this assessment applied. */
    aims_assessment_method_used?: string,
    /** The risks the assessment identified. */
    aims_assessment_risks?: AimsRiskAimsId[],
    /** The impact assessments the assessment drew on. */
    aims_assessment_impact_assessments?: AimsImpactAssessmentAimsId[],
    /** A summary of what the assessment found. */
    aims_assessment_summary?: string,
    /** What the assessment recommends. */
    aims_assessment_recommendations?: string[],
    /** When the next assessment is planned. */
    aims_assessment_next_date?: date,
}


/**
 * An AI risk in the risk register: where it comes from, which objectives it helps or hinders, who could feel its consequences, how it is rated and how it is treated.
 */
export interface AimsRisk extends AimsRecordMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The kinds of risk source the record bears on. */
    aims_risk_source_categories?: string,
    /** Where the risk comes from, in the organization's words. */
    aims_risk_source?: string,
    /** The AI objectives the risk helps or hinders. */
    aims_risk_objectives?: AimsObjectiveAimsId[],
    /** What the organization could suffer if the risk came about. */
    aims_risk_consequences_for_organization?: string,
    /** What persons could suffer if the risk came about. */
    aims_risk_consequences_for_individuals?: string,
    /** What society could suffer if the risk came about. */
    aims_risk_consequences_for_societies?: string,
    /** The person who is accountable for the risk and has the authority to manage it. */
    aims_risk_owner?: string,
    /** How likely the risk is, where that can be judged. */
    aims_risk_likelihood?: string,
    /** How severe the consequences would be. */
    aims_risk_consequence?: string,
    /** The risk's level before controls. */
    aims_risk_inherent_level?: string,
    /** The organization's controls already acting on the risk. */
    aims_risk_existing_controls?: AimsControlAimsId[],
    /** The risk's level after controls. */
    aims_risk_residual_level?: string,
    /** Whether the risk is acceptable under the organization's criteria. */
    aims_risk_acceptable?: boolean,
    /** The treatment chosen for the risk. */
    aims_risk_treatment_option?: string,
    /** How soon the risk is to be treated, in the organization's own terms. */
    aims_risk_treatment_priority?: string,
    /** The impact assessments that inform the risk. */
    aims_risk_impact_assessments?: AimsImpactAssessmentAimsId[],
}


/**
 * The organization's process for treating AI risks: how it chooses options and controls, checks them against Annex A and produces the Statement of Applicability and the plan.
 */
export interface AimsRiskTreatmentProcess extends AimsRecordMixin, AimsDocumentControlMixin {
    /** How a treatment option is chosen for a risk. */
    aims_treatment_options_guidance?: string,
    /** How the controls a treatment needs are chosen. */
    aims_treatment_control_selection?: string,
    /** How the chosen controls are compared with Annex A, so that none is missed. */
    aims_treatment_annex_a_comparison?: string,
    /** How the organization decides it needs controls beyond Annex A, and where it gets them. */
    aims_treatment_additional_controls?: string,
    /** How the guidance of Annex B is taken into account. */
    aims_treatment_annex_b_use?: string,
    /** The template the Statement of Applicability follows. */
    aims_treatment_soa_template?: string,
    /** How designated management approves a plan and accepts the risk left over. */
    aims_treatment_approval_workflow?: string,
}


/**
 * A plan to treat one or more risks: the actions and controls, who carries them out and when, and designated management's approval of the plan and of the risk left over.
 */
export interface AimsRiskTreatmentPlan extends AimsRecordMixin, AimsDocumentControlMixin {
    /** How far the control or the plan has been put into effect. */
    aims_implementation_state?: string,
    /** What the plan covers. */
    aims_plan_scope?: string,
    /** The risks the plan treats. */
    aims_plan_risks?: AimsRiskAimsId[],
    /** The actions the plan takes. */
    aims_plan_actions?: string[],
    /** The controls the plan puts in place. */
    aims_plan_controls?: AimsControlAimsId[],
    /** The resources the plan needs. */
    aims_plan_resources?: string,
    /** Who carries out the plan. */
    aims_plan_responsible_parties?: string[],
    /** When the plan's actions are to happen. */
    aims_plan_timeline?: string,
    /** The designated management that approved the plan. */
    aims_plan_approver?: string,
    /** How that management accepted the risk left over. */
    aims_plan_residual_risk_acceptance?: string,
    /** What the check on whether the plan works found. */
    aims_plan_effectiveness?: string,
    /** How options that did not work were reviewed, and what changed. */
    aims_plan_revalidation?: string,
    /** When the plan was completed. */
    aims_plan_completion_date?: date,
}


/**
 * The process for working out what AI systems may do to people and society: when it applies, what it takes in, who runs it and how the results are used.
 */
export interface AimsImpactAssessmentProcess extends AimsRecordMixin, AimsDocumentControlMixin {
    /** What calls for an assessment, such as how critical the use is or a large change. */
    aims_impact_process_triggers?: string[],
    /** How often assessments run, as an ISO 8601 duration. */
    aims_impact_process_interval?: string,
    /** The steps of an assessment, from finding impacts to reporting them. */
    aims_impact_process_steps?: string[],
    /** Who carries out an assessment. */
    aims_impact_process_assessors?: string,
    /** How results feed risk assessments and a system's design or use. */
    aims_impact_process_use?: string,
    /** Who the process looks at. */
    aims_impact_process_subjects?: string,
    /** The areas of impact the process looks at. */
    aims_impact_process_areas?: string,
    /** How long results are kept, as an ISO 8601 duration. */
    aims_impact_process_retention?: string,
}


/**
 * One impact assessment carried out under the process: the systems and the setting it looked at, and each impact it found.
 */
export interface AimsImpactAssessment extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** What the assessment covered. */
    aims_impact_scope?: string,
    /** The discipline it was carried out for, if it was only one, such as privacy or safety. */
    aims_impact_discipline?: string,
    /** When the assessment was carried out. */
    aims_impact_date?: date,
    /** Who carried out the assessment. */
    aims_impact_assessor?: string,
    /** What the system is for. */
    aims_impact_intended_use?: string,
    /** How the system could predictably be misused. */
    aims_impact_foreseeable_misuse?: string,
    /** The technical setting the system runs in. */
    aims_impact_technical_context?: string,
    /** The social setting the system runs in. */
    aims_impact_societal_context?: string,
    /** The jurisdictions that apply to where the system runs. */
    aims_impact_jurisdictions?: string[],
    /** The groups of people the system is meant for or touches. */
    aims_impact_demographic_groups?: string[],
    /** How complex the system is. */
    aims_impact_system_complexity?: string,
    /** What part people play beside the system, and their means of oversight. */
    aims_impact_human_role?: string,
    /** The failures that can be foreseen, their effects and what limits them. */
    aims_impact_failures?: string[],
    /** What the system means for jobs and the skills of staff. */
    aims_impact_workforce?: string,
    /** The impacts the assessment found. */
    aims_impact_findings?: AimsIdentifiedImpact[],
    /** The interested parties told of the result. */
    aims_impact_shared_with?: AimsInterestedPartyAimsId[],
    /** When the next assessment is planned. */
    aims_impact_next_date?: date,
}


/**
 * One impact an assessment found: on whom it falls, in what area, whether it helps or harms, and what limits the harm.
 */
export interface AimsIdentifiedImpact {
    /** Who the impact falls on. */
    aims_identified_impact_subject: string,
    /** The area the impact falls in. */
    aims_identified_impact_area?: string,
    /** Whether the impact helps or harms. */
    aims_identified_impact_direction?: string,
    /** What the impact is, in the organization's words. */
    aims_identified_impact_text: string,
    /** What is done to limit the harm. */
    aims_identified_impact_mitigation?: string[],
}


/**
 * The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each control it leaves out, with why.
 */
export interface AimsStatementOfApplicability extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The statement's entries, one for each control included or left out. */
    aims_soa_entries?: AimsApplicabilityEntry[],
}


/**
 * One entry of the Statement of Applicability, which either includes a control or leaves one out, and says why.
 */
export interface AimsApplicabilityEntry {
    /** The Annex A control a Statement of Applicability entry concerns. */
    aims_entry_annex_a_control?: string,
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The kind of entry, AimsIncludedControl or AimsExcludedControl. */
    aims_entry_type?: string,
    /** Why the control is included or left out. */
    aims_entry_justification: string,
}


/**
 * An entry that includes a control the organization needs, from Annex A or from elsewhere, says which risks call for it and whether it is in place.
 */
export interface AimsIncludedControl extends AimsApplicabilityEntry {
    /** How far the control or the plan has been put into effect. */
    aims_implementation_state: string,
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** The organization's control the entry includes. */
    aims_included_control?: AimsControlAimsId,
    /** The risks the control answers to. */
    aims_included_risks?: AimsRiskAimsId[],
    /** What shows that the control is in place. */
    aims_included_evidence?: string,
    /** When the control is to be in place, if it is not yet. */
    aims_included_target_date?: date,
}


/**
 * An entry that leaves out an Annex A control the organization does not need, and says why.
 */
export interface AimsExcludedControl extends AimsApplicabilityEntry {
}


/**
 * A control the organization has found it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
 */
export interface AimsControl extends AimsRecordMixin {
    /** The organization's controls that the record concerns. */
    aims_relevant_controls?: AimsControlAimsId[],
    /** How far the control or the plan has been put into effect. */
    aims_implementation_state?: string,
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The kinds of objective the record bears on. */
    aims_objective_categories?: string,
    /** The kinds of risk source the record bears on. */
    aims_risk_source_categories?: string,
    /** Which of Annex A's nine areas the control belongs to. */
    aims_control_area?: string,
    /** What the control does, in the organization's own words. */
    aims_control_text?: string,
    /** The organization's notes on putting the control in place. */
    aims_control_guidance?: string,
    /** The person who owns the control. */
    aims_control_owner?: string,
    /** When the control was put in place. */
    aims_control_implementation_date?: date,
    /** How well the control works, in the organization's own terms. */
    aims_control_effectiveness?: string,
    /** When the control was last tested. */
    aims_control_last_tested?: date,
    /** Where the evidence that the control is in place is kept. */
    aims_control_evidence?: string[],
}


/**
 * One AI system under the management system: what it is for, how it is built, run and overseen, what it draws on, and what is kept about it.
 */
export interface AimsAiSystem extends AimsRecordMixin {
    /** The organization's controls that the record concerns. */
    aims_relevant_controls?: AimsControlAimsId[],
    /** What the system is for. */
    aims_system_intended_purpose?: string,
    /** The uses the system is meant for. */
    aims_system_intended_uses?: string[],
    /** The ways people could predictably misuse the system. */
    aims_system_foreseeable_misuse?: string[],
    /** The field the system is applied in. */
    aims_system_domain?: string,
    /** The setting the system runs in. */
    aims_system_deployment_context?: string,
    /** The stage of its life the system is in now. */
    aims_system_life_cycle_stage?: string,
    /** The parts the organization plays towards this system. */
    aims_system_organization_roles?: string,
    /** The parts the organization plays when this system processes personal data. */
    aims_system_pii_roles?: string,
    /** Why the system is being built, such as a business case or a customer's request. */
    aims_system_rationale?: string,
    /** What the system must meet, across its whole life. */
    aims_system_requirements?: string[],
    /** The machine learning approach it takes, such as supervised or unsupervised. */
    aims_system_ml_approach?: string,
    /** The learning algorithms and kinds of model it uses. */
    aims_system_model_types?: string[],
    /** Whether what it meets in service goes on changing its behaviour. */
    aims_system_continuous_learning?: boolean,
    /** How much the system does without people. */
    aims_system_automation_level?: string,
    /** The threats peculiar to AI that were considered for the system. */
    aims_system_threats?: string,
    /** The tests, data and methods used to verify and validate the system. */
    aims_system_verification_measures?: string[],
    /** What the system is judged against, such as a limit on its errors. */
    aims_system_evaluation_criteria?: string[],
    /** What must hold before the system is released. */
    aims_system_release_criteria?: string[],
    /** The documented information that holds the plan for putting it into service. */
    aims_system_deployment_plan?: AimsDocumentedInformationAimsId,
    /** What keeping the system in service takes, such as watching, repairs and updates. */
    aims_system_operation_elements?: string[],
    /** The measures of how the system does in service, with acceptable values. */
    aims_system_performance_metrics?: string[],
    /** The stages of its life at which the system keeps event logs. */
    aims_system_log_stages?: string,
    /** What the logs record, such as times of use or out-of-range results. */
    aims_system_log_contents?: string[],
    /** How long the logs are kept, as an ISO 8601 duration. */
    aims_system_log_retention?: string,
    /** Whether the system may be used only with people watching over it. */
    aims_system_human_oversight_required?: boolean,
    /** How people watch over the system, and who may overrule it. */
    aims_system_human_oversight?: string,
    /** The stages of its life at which people watch over the system. */
    aims_system_human_oversight_stages?: string,
    /** The resources the system draws on. */
    aims_system_resources_used?: AimsSystemResourceAimsId[],
    /** The technical documents kept for the system. */
    aims_system_technical_documents?: AimsTechnicalDocumentationAimsId[],
    /** The impact assessments of the system. */
    aims_system_impact_assessments?: AimsImpactAssessmentAimsId[],
    /** The partners, suppliers and customers that deal with the system. */
    aims_system_relationships?: AimsThirdPartyRelationshipAimsId[],
}


/**
 * Something an AI system draws on, told apart by its type, with the stages of the system's life that need it and who provides it.
 */
export interface AimsSystemResource extends AimsRecordMixin {
    /** The stages of an AI system's life the record applies to. */
    aims_life_cycle_stages?: string,
    /** The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource. */
    aims_resource_type: string,
    /** Who provides the resource. */
    aims_resource_provider?: string,
}


/**
 * A part of a system, and how it is joined to the rest.
 */
export interface AimsComponentResource extends AimsSystemResource {
    /** What kind of part it is. */
    aims_component_kind?: string,
    /** How the part is joined to the system. */
    aims_component_integration?: string,
}


/**
 * Data an AI system draws on: where it came from, what part it plays, how it was obtained, made ready and judged fit, and how long it is kept.
 */
export interface AimsDataResource extends AimsSystemResource {
    /** The parts the data plays in machine learning. */
    aims_data_categories?: string,
    /** What kind of data it is, in a classification the organization names. */
    aims_data_kinds?: string[],
    /** What the data is for. */
    aims_data_intended_use?: string,
    /** How much data is needed. */
    aims_data_quantity?: string,
    /** Where the data comes from, such as bought, shared, open or synthetic. */
    aims_data_sources?: string[],
    /** How the source behaves, such as fixed, streamed or made by machine. */
    aims_data_source_characteristics?: string[],
    /** Who the data is about, with any known bias or systematic error. */
    aims_data_subject_demographics?: string[],
    /** What was done with the data before, such as earlier uses. */
    aims_data_prior_handling?: string,
    /** The rights bearing on the data, such as personal data or copyright. */
    aims_data_rights?: string[],
    /** The metadata that comes with it, such as details of labelling. */
    aims_data_metadata?: string[],
    /** The record of where the data came from and what happened to it. */
    aims_data_provenance?: string,
    /** How that record is checked, where it needs to be. */
    aims_data_provenance_verification?: string,
    /** What quality the data must have. */
    aims_data_quality_requirements?: string[],
    /** How the data measures up to those requirements. */
    aims_data_quality_results?: string[],
    /** Known or suspected bias in the data. */
    aims_data_bias_issues?: string[],
    /** How well training data stands for what the system will meet in service. */
    aims_data_representativeness?: string,
    /** How the data is labelled. */
    aims_data_labelling_process?: string,
    /** What decides how the data is made ready. */
    aims_data_preparation_criteria?: string,
    /** The methods used to make the data ready. */
    aims_data_preparation_methods?: string,
    /** When the data last changed. */
    aims_data_last_updated?: date,
    /** How long the data is kept and how it is disposed of. */
    aims_data_retention?: string,
    /** The information classification the data carries. */
    aims_data_classification?: string,
}


/**
 * A tool an AI system draws on, such as an algorithm, a model or a development tool.
 */
export interface AimsToolingResource extends AimsSystemResource {
    /** What kind of tool it is, such as a model or an evaluation method. */
    aims_tool_category?: string,
    /** The version in use. */
    aims_tool_version?: string,
    /** Who supplies the tool. */
    aims_tool_vendor?: string,
    /** The terms the tool is used under. */
    aims_tool_licence?: string,
    /** What the tool is used for. */
    aims_tool_purpose?: string,
}


/**
 * Hardware or computing an AI system draws on: what it needs, where it runs and what the hardware costs.
 */
export interface AimsComputingResource extends AimsSystemResource {
    /** What the system needs in order to run, such as on a small device. */
    aims_computing_requirements?: string,
    /** Where it runs, such as on the premises, in a cloud or at the edge. */
    aims_computing_location?: string,
    /** The processing it provides, network and storage included. */
    aims_computing_processing?: string,
    /** What the hardware costs, in money or to the environment. */
    aims_computing_hardware_impact?: string,
}


/**
 * People an AI system draws on: their skills and the work they do on it.
 */
export interface AimsHumanResource extends AimsSystemResource {
    /** The role these people hold. */
    aims_human_role?: AimsRoleAimsId,
    /** The skills they bring. */
    aims_human_competences?: string[],
    /** The work they do on the system, from building it to decommissioning it. */
    aims_human_activities?: string[],
    /** How the team's range of expertise was considered. */
    aims_human_diversity?: string,
}


/**
 * A process for designing and building an AI system responsibly: the life cycle it follows, and what it asks of testing, oversight, data and approvals.
 */
export interface AimsDevelopmentProcess extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The life cycle model followed, which may be the organization's own. */
    aims_development_life_cycle_model?: string,
    /** What must be tested and how. */
    aims_development_testing?: string,
    /** What oversight by people is asked for, with its tools and processes. */
    aims_development_human_oversight?: string,
    /** The stages at which impact assessments run. */
    aims_development_impact_assessment_stages?: string,
    /** What data may be used, from which suppliers, and how it is labelled. */
    aims_development_training_data_rules?: string,
    /** The expertise or training developers need. */
    aims_development_expertise?: string,
    /** What must hold before a release. */
    aims_development_release_criteria?: string[],
    /** Who must approve what, at each stage. */
    aims_development_approvals?: string[],
    /** How changes are controlled. */
    aims_development_change_control?: string,
    /** What is asked of how easy the system is to use and how far people stay in control. */
    aims_development_usability?: string,
    /** How interested parties are brought in. */
    aims_development_party_engagement?: string,
}


/**
 * A process for using AI systems responsibly: what decides if a system may be used, built in-house or brought in.
 */
export interface AimsResponsibleUseProcess extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The approvals needed before use. */
    aims_use_approvals?: string[],
    /** What use costs, ongoing upkeep included. */
    aims_use_costs?: string,
    /** What a system or its supplier must meet to be taken on. */
    aims_use_sourcing_requirements?: string[],
    /** The laws that bear on use. */
    aims_use_legal_requirements?: string[],
}


/**
 * Technical documents about an AI system for one kind of reader: what they hold, and the form they take.
 */
export interface AimsTechnicalDocumentation extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** Who the documents are for, such as users or a supervisory authority. */
    aims_technical_doc_audiences?: string[],
    /** The form the documents take for those readers. */
    aims_technical_doc_form?: string,
    /** What the documents hold, such as limits, design choices or test records. */
    aims_technical_doc_contents?: string[],
    /** How failures are managed, such as rolling back or turning features off. */
    aims_technical_doc_failure_plan?: string,
}


/**
 * What those who use a system are told: the contents, how it reaches them, what decided it, and the check that they got it.
 */
export interface AimsUserInformation extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** What users are told, such as that AI is behind what they see and how to overrule it. */
    aims_user_information_contents?: string[],
    /** How it reaches them, such as instructions, alerts or a web page. */
    aims_user_information_channels?: string[],
    /** What decided what they are told. */
    aims_user_information_criteria?: string[],
    /** Whether the organization has checked that users can get it and that it is right. */
    aims_user_information_validated?: boolean,
}


/**
 * The plan for telling users when a system goes wrong: which incidents, how soon, to which authorities, and with what details.
 */
export interface AimsIncidentCommunicationPlan extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The kinds of incident the plan covers. */
    aims_incident_plan_categories?: string,
    /** How soon people must be told. */
    aims_incident_plan_timeline?: string,
    /** The authorities that must be told, if any. */
    aims_incident_plan_authorities?: string[],
    /** What each notice must say. */
    aims_incident_plan_details?: string[],
    /** How the plan fits the organization's wider handling of incidents. */
    aims_incident_plan_integration?: string,
}


/**
 * Something the organization must report about a system to an interested party: to whom, under what rule, what and how soon.
 */
export interface AimsReportingObligation extends AimsRecordMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** Who must be told. */
    aims_obligation_parties?: AimsInterestedPartyAimsId[],
    /** The law or agreement that creates the duty. */
    aims_obligation_basis?: string,
    /** The jurisdiction the duty arises in. */
    aims_obligation_jurisdiction?: string,
    /** What must be reported, such as risks, assessments or logs. */
    aims_obligation_contents?: string[],
    /** How soon it must be reported. */
    aims_obligation_timeframe?: string,
}


/**
 * A resource provided for the management system itself, such as people, time, tools or budget. What an AI system draws on is an AimsSystemResource.
 */
export interface AimsResource extends AimsRecordMixin {
    /** What kind of resource it is. */
    aims_support_category?: string,
    /** How much of the resource is provided. */
    aims_support_quantity?: string,
    /** When the resource was allocated. */
    aims_support_allocation_date?: date,
    /** What the resource is allocated to. */
    aims_support_allocated_to?: string,
    /** What the resource costs. */
    aims_support_cost?: string,
    /** Whether the resource is available now, in the organization's own terms. */
    aims_support_availability?: string,
}


/**
 * The evidence of one person's competence for work that affects AI performance, and what is done to close any gap.
 */
export interface AimsCompetenceRecord extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The person the record is about. */
    aims_competence_person?: string,
    /** The role the person holds. */
    aims_competence_role?: AimsRoleAimsId,
    /** The competences the role needs. */
    aims_competence_required?: string[],
    /** The person's relevant education. */
    aims_competence_education?: string[],
    /** The training the person has completed. */
    aims_competence_training?: string[],
    /** The person's relevant experience. */
    aims_competence_experience?: string[],
    /** When the person's competence was last assessed. */
    aims_competence_assessment_date?: date,
    /** The gaps the assessment found. */
    aims_competence_gaps?: string[],
    /** What is done to close the gaps, and how well it worked. */
    aims_competence_actions?: string[],
}


/**
 * The programme that tells people working for the organization about the AI policy, their part in the system and what failing it would mean.
 */
export interface AimsAwarenessProgramme extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The topics the programme covers. */
    aims_awareness_topics?: string[],
    /** How the programme is delivered. */
    aims_awareness_methods?: string[],
    /** Whom the programme is for. */
    aims_awareness_audience?: string,
    /** How often the programme runs. */
    aims_awareness_frequency?: string,
    /** How completion is tracked. */
    aims_awareness_completion_tracking?: string,
    /** How the programme's effect is measured. */
    aims_awareness_effectiveness?: string,
}


/**
 * The plan for communication about the system, inside the organization and outside it.
 */
export interface AimsCommunicationPlan extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The communications the plan provides for. */
    aims_communication_items?: AimsCommunication[],
}


/**
 * One communication the plan provides for: what about, to whom, when, how, and who communicates.
 */
export interface AimsCommunication {
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** What the communication is about. */
    aims_communication_subject: string,
    /** Why it is communicated. */
    aims_communication_purpose?: string,
    /** To whom it is communicated. */
    aims_communication_audience?: string,
    /** Whether it goes outside the organization. */
    aims_communication_external?: boolean,
    /** When it is communicated. */
    aims_communication_timing?: string,
    /** How it is communicated. */
    aims_communication_method?: string,
    /** Whether a record of the communication is kept. */
    aims_communication_records_required?: boolean,
}


/**
 * A document or record the system keeps under control that no more specific record describes, such as a procedure, a plan or a report.
 */
export interface AimsDocumentedInformation extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The clauses of the standard the record answers to or concerns. */
    aims_cited_clauses?: string,
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** What kind of documented information it is. */
    aims_document_kind: string,
}


/**
 * A procedure by which the organization plans and controls the processes that meet its requirements, such as managing data for building or vetting suppliers.
 */
export interface AimsOperationalProcedure extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The organization's controls that the record concerns. */
    aims_relevant_controls?: AimsControlAimsId[],
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** What the procedure covers. */
    aims_procedure_scope?: string,
    /** The criteria the processes are run to. */
    aims_procedure_criteria?: string,
    /** The measures that control the processes. */
    aims_procedure_control_measures?: string[],
    /** The roles that carry out the procedure. */
    aims_procedure_roles?: AimsRoleAimsId[],
    /** How planned changes are controlled, and unplanned ones reviewed. */
    aims_procedure_change_control?: string,
}


/**
 * The programme that watches, measures, analyses and judges how well the system does and how well it works.
 */
export interface AimsMonitoringProgramme extends AimsRecordMixin, AimsDocumentControlMixin {
    /** What the programme monitors and measures. */
    aims_monitoring_items?: AimsMonitoringItem[],
}


/**
 * One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
 */
export interface AimsMonitoringItem {
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** The name of what is measured. */
    aims_monitoring_metric: string,
    /** What the measurement shows. */
    aims_monitoring_description?: string,
    /** How it is measured. */
    aims_monitoring_method?: string,
    /** How often it is measured. */
    aims_monitoring_frequency?: string,
    /** How often the results are analysed and evaluated. */
    aims_monitoring_analysis_frequency?: string,
    /** Who analyses and evaluates the results. */
    aims_monitoring_analyst?: string,
    /** The value aimed for. */
    aims_monitoring_target?: string,
    /** The value that calls for action. */
    aims_monitoring_alert_threshold?: string,
    /** The value last measured. */
    aims_monitoring_current_value?: string,
    /** Which way the value is moving. */
    aims_monitoring_trend?: string,
}


/**
 * A programme of internal audits: the audits planned over a period, how often and why, and the resources and auditors they need.
 */
export interface AimsAuditProgramme extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The period the programme covers. */
    aims_programme_period?: string,
    /** The audits the programme plans. */
    aims_programme_audits?: AimsAuditAimsId[],
    /** Why the audits happen as often as they do, given what matters most and past results. */
    aims_programme_frequency_rationale?: string,
    /** How the audits are carried out. */
    aims_programme_methods?: string,
    /** Who answers for planning, running and reporting them. */
    aims_programme_responsibilities?: string[],
    /** The resources the programme needs. */
    aims_programme_resources?: string,
    /** How auditors are chosen so that they stay objective and impartial. */
    aims_programme_auditor_selection?: string,
    /** Where the programme stands, in the organization's own terms. */
    aims_programme_status?: string,
}


/**
 * An audit of the system: an internal audit, or one by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
 */
export interface AimsAudit extends AimsRecordMixin, AimsDocumentControlMixin {
    /** Who carries out the audit, relative to the organization. */
    aims_audit_type: string,
    /** Other standards for management systems the audit covers. */
    aims_audit_standards?: string,
    /** What the audit covers. */
    aims_audit_scope?: string,
    /** What the audit compares the system against. */
    aims_audit_criteria?: string[],
    /** What the audit sets out to establish. */
    aims_audit_objectives?: string[],
    /** When the audit began. */
    aims_audit_period_start?: date,
    /** When the audit ended. */
    aims_audit_period_end?: date,
    /** Who led the audit. */
    aims_audit_lead?: string,
    /** Who else audited. */
    aims_audit_team?: string[],
    /** Who represented the parts of the organization audited. */
    aims_audit_auditees?: string[],
    /** The documented information that holds the audit plan. */
    aims_audit_plan?: AimsDocumentedInformationAimsId,
    /** What the audit found, good and bad. */
    aims_audit_findings?: AimsAuditFindingAimsId[],
    /** The audit's overall conclusion. */
    aims_audit_conclusion?: string,
    /** When the audit report was issued. */
    aims_audit_report_date?: date,
    /** Who received the audit report. */
    aims_audit_report_distribution?: string[],
}


/**
 * One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
 */
export interface AimsAuditFinding extends AimsRecordMixin {
    /** The clauses of the standard the record answers to or concerns. */
    aims_cited_clauses?: string,
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** What kind of finding it is. */
    aims_finding_type: string,
    /** The organization's control the finding concerns. */
    aims_finding_control?: AimsControlAimsId,
    /** The objective evidence for the finding. */
    aims_finding_evidence?: string,
    /** What the analysis of the finding's cause found. */
    aims_finding_root_cause?: string,
    /** What the finding means for risk. */
    aims_finding_risk?: string,
    /** What the auditor recommends. */
    aims_finding_recommendation?: string,
    /** How the auditee responded. */
    aims_finding_auditee_response?: string,
    /** The corrective action the finding led to. */
    aims_finding_corrective_action?: AimsCorrectiveActionAimsId,
    /** Whether the finding is closed, in the organization's own terms. */
    aims_finding_closure_status?: string,
    /** When the finding was closed. */
    aims_finding_closure_date?: date,
}


/**
 * A review of the system by top management: what it took in, what it decided and what it asked to be done.
 */
export interface AimsManagementReview extends AimsRecordMixin, AimsDocumentControlMixin {
    /** When the review was held. */
    aims_review_held_on: date,
    /** Who attended the review. */
    aims_review_attendees?: string[],
    /** Where the actions from earlier reviews stand. */
    aims_review_previous_actions?: string,
    /** How the matters that bear on the system have changed. */
    aims_review_context_changes?: string,
    /** How interested parties' needs and expectations have changed. */
    aims_review_interested_party_changes?: string,
    /** How nonconformities and their corrections have been trending. */
    aims_review_nonconformity_trends?: string,
    /** The trends in what was monitored and measured. */
    aims_review_monitoring_trends?: string,
    /** The trends in audit results. */
    aims_review_audit_trends?: string,
    /** The opportunities for improvement raised. */
    aims_review_improvement_opportunities?: string[],
    /** What the review decided about improving. */
    aims_review_decisions?: string[],
    /** The changes to the system the review found were needed. */
    aims_review_system_changes?: string[],
    /** What the review asked to be done. */
    aims_review_actions?: string[],
    /** When the next review is planned. */
    aims_review_next_date?: date,
}


/**
 * A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
 */
export interface AimsNonconformity extends AimsRecordMixin {
    /** The clauses of the standard the record answers to or concerns. */
    aims_cited_clauses?: string,
    /** The controls of Annex A the record answers to or concerns. */
    aims_cited_annex_a_controls?: string,
    /** How the nonconformity came to light, such as an audit, a review or an incident. */
    aims_nonconformity_source?: string,
    /** When the nonconformity was found. */
    aims_nonconformity_detected_on?: date,
    /** Who or what found it. */
    aims_nonconformity_detected_by?: string,
    /** The requirement not met, of the organization or of an interested party, in words. */
    aims_nonconformity_requirement?: string,
    /** What was done at once to contain and fix it. */
    aims_nonconformity_immediate_actions?: string[],
    /** How its consequences were dealt with. */
    aims_nonconformity_consequences?: string,
    /** What caused it. */
    aims_nonconformity_root_cause?: string,
    /** Whether it could happen, or has happened, elsewhere. */
    aims_nonconformity_similar_check?: string,
    /** Where the nonconformity stands, in the organization's own terms. */
    aims_nonconformity_status?: string,
    /** When it was closed. */
    aims_nonconformity_closure_date?: date,
    /** What shows that it is closed. */
    aims_nonconformity_closure_evidence?: string,
}


/**
 * An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
 */
export interface AimsCorrectiveAction extends AimsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** The nonconformities the action addresses. */
    aims_action_nonconformities?: AimsNonconformityAimsId[],
    /** The cause the action removes. */
    aims_action_root_cause?: string,
    /** When the action is to be complete. */
    aims_action_target_date?: date,
    /** When the action was complete. */
    aims_action_completion_date?: date,
    /** The resources the action needs. */
    aims_action_resources?: string,
    /** How the action's effect will be judged. */
    aims_action_effectiveness_criteria?: string,
    /** When the action's effect was reviewed. */
    aims_action_effectiveness_review_date?: date,
    /** Whether the review found the action effective. */
    aims_action_effective?: boolean,
    /** The changes to the system the action needs. */
    aims_action_system_changes?: string,
    /** Where the action stands, in the organization's own terms. */
    aims_action_status?: string,
}


/**
 * An opportunity to make the system more suitable, adequate or effective, and what came of it.
 */
export interface AimsImprovementOpportunity extends AimsRecordMixin {
    /** The role that answers for the record's activity or outcome. */
    aims_responsible_role?: AimsRoleAimsId,
    /** Where the opportunity came from, such as a review, an audit or daily work. */
    aims_improvement_source?: string,
    /** When the opportunity was identified. */
    aims_improvement_identified_on?: date,
    /** Who identified it. */
    aims_improvement_identified_by?: string,
    /** What the improvement is expected to bring. */
    aims_improvement_benefit?: string,
    /** How soon it is to be acted on, in the organization's own terms. */
    aims_improvement_priority?: string,
    /** How the improvement is to be made. */
    aims_improvement_plan?: string,
    /** When the improvement is to be made. */
    aims_improvement_target_date?: date,
    /** When it was made. */
    aims_improvement_completion_date?: date,
    /** What the improvement brought. */
    aims_improvement_outcome?: string,
    /** Where it stands, in the organization's own terms. */
    aims_improvement_status?: string,
}


/**
 * A relationship with another party in an AI system's life, such as a partner: who carries which duty, and what assures the organization of that.
 */
export interface AimsThirdPartyRelationship extends AimsRecordMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The stages of an AI system's life the record applies to. */
    aims_life_cycle_stages?: string,
    /** The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship. */
    aims_relationship_type?: string,
    /** The other party. */
    aims_relationship_party?: string,
    /** The parts the other party plays towards the system. */
    aims_relationship_party_roles?: string,
    /** The agreement the relationship rests on. */
    aims_relationship_contract?: string,
    /** The duties each side carries. */
    aims_relationship_responsibilities?: string[],
    /** The part the other party plays when personal data is processed. */
    aims_relationship_pii_role?: string,
    /** The documents one side owes the other about the system. */
    aims_relationship_documentation?: string[],
    /** What assures the organization that the party meets its duties. */
    aims_relationship_assurance_evidence?: string[],
    /** How often the relationship is reviewed. */
    aims_relationship_review_frequency?: string,
}


/**
 * A relationship with a supplier to the organization's AI work: what it provides, the risk that brings, and how it is held to the organization's approach.
 */
export interface AimsSupplierRelationship extends AimsThirdPartyRelationship {
    /** What it provides, such as data, models, software or a whole system. */
    aims_supplier_provides?: string[],
    /** How much risk what it provides brings. */
    aims_supplier_risk?: string,
    /** What the organization asks of the supplier. */
    aims_supplier_requirements?: string[],
    /** How the supplier is watched and judged over time. */
    aims_supplier_monitoring?: string,
    /** How what it provides is joined to the organization's systems. */
    aims_supplier_integration?: string,
    /** What the supplier was asked to put right. */
    aims_supplier_corrective_actions?: string[],
}


/**
 * A relationship with a customer of the organization's AI work: what it expects, who answers for what, and which limits it was told of.
 */
export interface AimsCustomerRelationship extends AimsThirdPartyRelationship {
    /** What the customer expects and wants. */
    aims_customer_expectations?: string[],
    /** The contract or terms of use that apply. */
    aims_customer_agreement?: string,
    /** What the provider answers for, and what the customer answers for. */
    aims_customer_responsibility_split?: string,
    /** What the customer was told the system cannot do, or where it stops being valid. */
    aims_customer_communicated_limits?: string[],
}


/**
 * Something that happened with a system and was reported, by monitoring, by a user or by someone outside, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an AimsIncident.
 */
export interface AimsSystemEvent extends AimsRecordMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** The kind of record, AimsSystemEvent or AimsIncident. */
    aims_event_type?: string,
    /** When the event happened, or when it was first noticed. */
    aims_event_occurred_at?: string,
    /** Who reported the event. */
    aims_event_reporter?: string,
    /** How the event came to light, such as a log, monitoring or a report from outside. */
    aims_event_source?: string,
    /** The harm that was reported, if any. */
    aims_event_adverse_impact?: string,
    /** What the assessment of the event found. */
    aims_event_assessment?: string,
}


/**
 * An event assessed as an incident: what it concerns, how severe it is, what was done, who was told, and what was learned.
 */
export interface AimsIncident extends AimsSystemEvent {
    /** What the incident concerns. */
    aims_incident_category?: string,
    /** The threats peculiar to AI that the incident involved. */
    aims_incident_threats?: string,
    /** How severe the incident is. */
    aims_incident_severity?: string,
    /** The areas of impact the incident touched. */
    aims_incident_impact_areas?: string,
    /** How the incident was detected. */
    aims_incident_detection_method?: string,
    /** What was done in response. */
    aims_incident_response_actions?: string[],
    /** What was done to restore normal operation. */
    aims_incident_recovery_actions?: string[],
    /** What caused the incident. */
    aims_incident_root_cause?: string,
    /** What the organization learned from it. */
    aims_incident_lessons_learned?: string[],
    /** Whether users, authorities or others had to be told. */
    aims_incident_notification_required?: boolean,
    /** Whom the organization told, and when. */
    aims_incident_notifications?: string[],
    /** The corrective actions the incident led to. */
    aims_incident_corrective_actions?: AimsCorrectiveActionAimsId[],
    /** When the incident was closed. */
    aims_incident_closed_at?: string,
}


/**
 * The way people raise worries about the organization's part in a system: how it keeps them safe, who looks into a worry, and how fast it answers.
 */
export interface AimsConcernReportingProcess extends AimsRecordMixin, AimsDocumentControlMixin {
    /** The ways a person can stay unnamed or keep a report private. */
    aims_concern_process_confidentiality?: string[],
    /** How staff and contractors learn of it and reach it. */
    aims_concern_process_audience?: string,
    /** Who looks into a report, and what powers they hold. */
    aims_concern_process_investigators?: string,
    /** How a report reaches management in good time. */
    aims_concern_process_escalation?: string,
    /** How those who report or investigate are shielded from reprisal. */
    aims_concern_process_reprisal_protection?: string,
    /** How soon a report is answered. */
    aims_concern_process_response_time?: string,
}


/**
 * One worry someone raised about the organization's part in a system, and how it was looked into and settled.
 */
export interface AimsConcernReport extends AimsRecordMixin {
    /** The AI systems the record concerns. */
    aims_ai_systems?: AimsAiSystemAimsId[],
    /** When the worry was raised. */
    aims_concern_reported_on?: date,
    /** Who raised it, unless they stayed unnamed. */
    aims_concern_reporter?: string,
    /** Whether the person stayed unnamed. */
    aims_concern_anonymous?: boolean,
    /** How it was raised. */
    aims_concern_channel?: string,
    /** The stage of the system's life it concerns. */
    aims_concern_life_cycle_stage?: string,
    /** How serious it is. */
    aims_concern_severity?: string,
    /** Who looked into it. */
    aims_concern_investigator?: string,
    /** Where the inquiry stands, in the organization's own terms. */
    aims_concern_investigation_status?: string,
    /** What the inquiry found. */
    aims_concern_findings?: string,
    /** Whether and how it went up to management. */
    aims_concern_escalation?: string,
    /** When an answer is due. */
    aims_concern_response_due?: date,
    /** When it was answered. */
    aims_concern_responded_on?: date,
    /** How it was settled. */
    aims_concern_resolution?: string,
    /** What was done to shield those involved from reprisal. */
    aims_concern_reprisal_protection?: string,
    /** The incidents it relates to. */
    aims_concern_incidents?: AimsIncidentAimsId[],
    /** The nonconformities it relates to. */
    aims_concern_nonconformities?: AimsNonconformityAimsId[],
}



