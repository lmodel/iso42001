-- # Class: AimsRecordMixin Description: What every record of the system has, so that other records can refer to it: an identifier, a title and a description.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsDocumentControlMixin Description: The control that documented information is kept under: who wrote, owns and approved it, its format and medium, when it takes effect and is looked at again, how it is classified, handed out, stored and changed, how long it is kept, and whether it came from outside.
--     * Slot: id
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsManagementSystem Description: One organization's management system for AI: its scope and context, and every record it keeps, each kind in a list of its own.
--     * Slot: aims_top_management Description: The person or group that runs the organization from the very top.
--     * Slot: aims_governing_body Description: The body top management answers to, such as a board, where there is one.
--     * Slot: aims_scope Description: How far the system reaches, in the organization's words.
--     * Slot: aims_processes Description: The processes the system needs and how they work together.
--     * Slot: aims_certification_status Description: Where the system stands with certification, in the organization's own terms.
--     * Slot: aims_certification_body Description: The body that certifies the system.
--     * Slot: aims_certification_date Description: When the system was certified.
--     * Slot: aims_recertification_date Description: When the system is next due for recertification.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_organization_aims_id Description: The organization that runs the system.
--     * Slot: aims_policy_aims_id Description: The AI policy.
--     * Slot: aims_risk_assessment_process_aims_id Description: The process for assessing AI risks.
--     * Slot: aims_risk_treatment_process_aims_id Description: The process for treating AI risks.
--     * Slot: aims_impact_assessment_process_aims_id Description: The process for assessing what AI systems may do to people and society.
--     * Slot: aims_statement_of_applicability_aims_id Description: The Statement of Applicability.
--     * Slot: aims_awareness_programme_aims_id Description: The awareness programme.
--     * Slot: aims_communication_plan_aims_id Description: The plan for communication about the system.
--     * Slot: aims_monitoring_programme_aims_id Description: The programme of monitoring and measurement.
--     * Slot: aims_concern_reporting_process_aims_id Description: The way people raise worries about the organization's part in AI.
-- # Class: AimsOrganization Description: The organization that runs the system, with what it needs to know about itself to understand its context and the parts it plays with AI.
--     * Slot: aims_organization_legal_name Description: The organization's registered legal name.
--     * Slot: aims_organization_kind Description: What kind of organization it is, such as a company, an agency or a charity.
--     * Slot: aims_organization_size Description: How the organization classes its own size.
--     * Slot: aims_organization_employee_count Description: About how many people the organization employs.
--     * Slot: aims_organization_parent Description: The organization's parent, if it has one.
--     * Slot: aims_organization_climate_change_relevant Description: Whether the organization has found climate change to matter for the system.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsInterestedParty Description: A person or organization whose needs and expectations bear on the system, or who may feel its decisions, inside the organization or outside it.
--     * Slot: aims_party_category Description: What kind of interested party it is, in the organization's own terms.
--     * Slot: aims_party_relationship Description: How the party relates to the organization.
--     * Slot: aims_party_communication_needs Description: What the party needs to be told, and how.
--     * Slot: aims_party_contact Description: How to reach the party.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsPolicy Description: The AI policy that top management sets: the organization's commitments and the frame for its AI objectives.
--     * Slot: aims_policy_statement Description: The policy's own statement, in the organization's words.
--     * Slot: aims_policy_objectives_framework Description: How the policy frames the setting of AI objectives.
--     * Slot: aims_policy_exceptions_process Description: How departures from the policy are handled.
--     * Slot: aims_policy_communication_date Description: When the policy was made known inside the organization.
--     * Slot: aims_policy_availability Description: How interested parties can get the policy, where that is fitting.
--     * Slot: aims_policy_review_role Description: The role management approved to develop, review and evaluate the policy.
--     * Slot: aims_policy_review_interval Description: How often the policy is reviewed, as an ISO 8601 duration.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsTopicSpecificPolicy Description: A policy on one topic that gives more guidance under the AI policy, such as assessing impacts or building systems.
--     * Slot: aims_topic_policy_topic Description: The topic the policy covers.
--     * Slot: aims_topic_policy_parent Description: The AI policy this policy supports.
--     * Slot: aims_topic_policy_audience Description: Whom the policy is written for.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsRole Description: A role in the system, with the duties and powers it carries and who holds it.
--     * Slot: aims_role_category Description: What kind of role it is, in the organization's own terms.
--     * Slot: aims_role_ensures_conformity Description: Whether the role sees that the system meets the standard.
--     * Slot: aims_role_reports_performance Description: Whether the role tells top management how the system is doing.
--     * Slot: aims_role_accountability Description: What the role is accountable for.
--     * Slot: aims_role_delegation Description: How the role may delegate its duties.
--     * Slot: aims_role_reports_to Description: The role this role reports to.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsObjective Description: An AI objective: a result the organization aims for, with how it plans to reach it and how it judges progress.
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_objective_purpose Description: What the objective is for.
--     * Slot: aims_objective_statement Description: The objective, as the organization states it.
--     * Slot: aims_objective_target Description: The value the objective aims for, where it can be measured.
--     * Slot: aims_objective_current_value Description: The value last measured.
--     * Slot: aims_objective_metric Description: How the objective's value is defined.
--     * Slot: aims_objective_measurement_method Description: How the value is measured.
--     * Slot: aims_objective_measurement_frequency Description: How often the value is measured.
--     * Slot: aims_objective_target_date Description: When the objective is to be reached.
--     * Slot: aims_objective_achievement Description: How far the objective has been reached, in the organization's own terms.
--     * Slot: aims_objective_action_plan Description: The steps that lead to the objective.
--     * Slot: aims_objective_resources Description: The resources needed to reach the objective.
--     * Slot: aims_objective_evaluation Description: How the outcome will be judged.
--     * Slot: aims_objective_communication Description: How the objective is made known.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsPlannedAction Description: An action planned on a risk or an opportunity the system faces, with how it fits the system's processes and how its effect will be judged.
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_planned_action_integration Description: How the action fits into the system's processes.
--     * Slot: aims_planned_action_effectiveness Description: How the action's effect will be judged.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsRiskAssessmentProcess Description: The organization's process for assessing AI risks: its criteria, scales and method, and when it runs.
--     * Slot: aims_risk_policy_alignment Description: How the process follows the AI policy and the AI objectives.
--     * Slot: aims_risk_comparability Description: How the process keeps repeated assessments consistent and comparable.
--     * Slot: aims_risk_method Description: The method used to identify, analyse and evaluate risks.
--     * Slot: aims_risk_likelihood_scale Description: The scale for rating likelihood.
--     * Slot: aims_risk_consequence_scale Description: The scale for rating consequences.
--     * Slot: aims_risk_matrix Description: How likelihood and consequence combine into a risk level.
--     * Slot: aims_risk_prioritization Description: How the assessed risks are ranked for treatment.
--     * Slot: aims_risk_assessment_interval Description: How often risks are assessed, as an ISO 8601 duration.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsRiskAssessment Description: One risk assessment carried out under the process, and what it found.
--     * Slot: aims_assessment_scope Description: What the assessment covered.
--     * Slot: aims_assessment_date Description: When the assessment was carried out.
--     * Slot: aims_assessment_assessor Description: Who carried out the assessment.
--     * Slot: aims_assessment_method_used Description: The method this assessment applied.
--     * Slot: aims_assessment_summary Description: A summary of what the assessment found.
--     * Slot: aims_assessment_next_date Description: When the next assessment is planned.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsRisk Description: An AI risk in the risk register: where it comes from, which objectives it helps or hinders, who could feel its consequences, how it is rated and how it is treated.
--     * Slot: aims_risk_source Description: Where the risk comes from, in the organization's words.
--     * Slot: aims_risk_consequences_for_organization Description: What the organization could suffer if the risk came about.
--     * Slot: aims_risk_consequences_for_individuals Description: What persons could suffer if the risk came about.
--     * Slot: aims_risk_consequences_for_societies Description: What society could suffer if the risk came about.
--     * Slot: aims_risk_owner Description: The person who is accountable for the risk and has the authority to manage it.
--     * Slot: aims_risk_likelihood Description: How likely the risk is, where that can be judged.
--     * Slot: aims_risk_consequence Description: How severe the consequences would be.
--     * Slot: aims_risk_inherent_level Description: The risk's level before controls.
--     * Slot: aims_risk_residual_level Description: The risk's level after controls.
--     * Slot: aims_risk_acceptable Description: Whether the risk is acceptable under the organization's criteria.
--     * Slot: aims_risk_treatment_option Description: The treatment chosen for the risk.
--     * Slot: aims_risk_treatment_priority Description: How soon the risk is to be treated, in the organization's own terms.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsRiskTreatmentProcess Description: The organization's process for treating AI risks: how it chooses options and controls, checks them against Annex A and produces the Statement of Applicability and the plan.
--     * Slot: aims_treatment_options_guidance Description: How a treatment option is chosen for a risk.
--     * Slot: aims_treatment_control_selection Description: How the controls a treatment needs are chosen.
--     * Slot: aims_treatment_annex_a_comparison Description: How the chosen controls are compared with Annex A, so that none is missed.
--     * Slot: aims_treatment_additional_controls Description: How the organization decides it needs controls beyond Annex A, and where it gets them.
--     * Slot: aims_treatment_annex_b_use Description: How the guidance of Annex B is taken into account.
--     * Slot: aims_treatment_soa_template Description: The template the Statement of Applicability follows.
--     * Slot: aims_treatment_approval_workflow Description: How designated management approves a plan and accepts the risk left over.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsRiskTreatmentPlan Description: A plan to treat one or more risks: the actions and controls, who carries them out and when, and designated management's approval of the plan and of the risk left over.
--     * Slot: aims_implementation_state Description: How far the control or the plan has been put into effect.
--     * Slot: aims_plan_scope Description: What the plan covers.
--     * Slot: aims_plan_resources Description: The resources the plan needs.
--     * Slot: aims_plan_timeline Description: When the plan's actions are to happen.
--     * Slot: aims_plan_approver Description: The designated management that approved the plan.
--     * Slot: aims_plan_residual_risk_acceptance Description: How that management accepted the risk left over.
--     * Slot: aims_plan_effectiveness Description: What the check on whether the plan works found.
--     * Slot: aims_plan_revalidation Description: How options that did not work were reviewed, and what changed.
--     * Slot: aims_plan_completion_date Description: When the plan was completed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsImpactAssessmentProcess Description: The process for working out what AI systems may do to people and society: when it applies, what it takes in, who runs it and how the results are used.
--     * Slot: aims_impact_process_interval Description: How often assessments run, as an ISO 8601 duration.
--     * Slot: aims_impact_process_assessors Description: Who carries out an assessment.
--     * Slot: aims_impact_process_use Description: How results feed risk assessments and a system's design or use.
--     * Slot: aims_impact_process_retention Description: How long results are kept, as an ISO 8601 duration.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsImpactAssessment Description: One impact assessment carried out under the process: the systems and the setting it looked at, and each impact it found.
--     * Slot: aims_impact_scope Description: What the assessment covered.
--     * Slot: aims_impact_discipline Description: The discipline it was carried out for, if it was only one, such as privacy or safety.
--     * Slot: aims_impact_date Description: When the assessment was carried out.
--     * Slot: aims_impact_assessor Description: Who carried out the assessment.
--     * Slot: aims_impact_intended_use Description: What the system is for.
--     * Slot: aims_impact_foreseeable_misuse Description: How the system could predictably be misused.
--     * Slot: aims_impact_technical_context Description: The technical setting the system runs in.
--     * Slot: aims_impact_societal_context Description: The social setting the system runs in.
--     * Slot: aims_impact_system_complexity Description: How complex the system is.
--     * Slot: aims_impact_human_role Description: What part people play beside the system, and their means of oversight.
--     * Slot: aims_impact_workforce Description: What the system means for jobs and the skills of staff.
--     * Slot: aims_impact_next_date Description: When the next assessment is planned.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsIdentifiedImpact Description: One impact an assessment found: on whom it falls, in what area, whether it helps or harms, and what limits the harm.
--     * Slot: id
--     * Slot: aims_identified_impact_subject Description: Who the impact falls on.
--     * Slot: aims_identified_impact_area Description: The area the impact falls in.
--     * Slot: aims_identified_impact_direction Description: Whether the impact helps or harms.
--     * Slot: aims_identified_impact_text Description: What the impact is, in the organization's words.
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
-- # Class: AimsStatementOfApplicability Description: The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each control it leaves out, with why.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Abstract Class: AimsApplicabilityEntry Description: One entry of the Statement of Applicability, which either includes a control or leaves one out, and says why.
--     * Slot: id
--     * Slot: aims_entry_annex_a_control Description: The Annex A control a Statement of Applicability entry concerns.
--     * Slot: aims_entry_type Description: The kind of entry, AimsIncludedControl or AimsExcludedControl.
--     * Slot: aims_entry_justification Description: Why the control is included or left out.
--     * Slot: AimsStatementOfApplicability_aims_id Description: Autocreated FK slot
-- # Class: AimsIncludedControl Description: An entry that includes a control the organization needs, from Annex A or from elsewhere, says which risks call for it and whether it is in place.
--     * Slot: id
--     * Slot: aims_implementation_state Description: How far the control or the plan has been put into effect.
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_included_control Description: The organization's control the entry includes.
--     * Slot: aims_included_evidence Description: What shows that the control is in place.
--     * Slot: aims_included_target_date Description: When the control is to be in place, if it is not yet.
--     * Slot: aims_entry_annex_a_control Description: The Annex A control a Statement of Applicability entry concerns.
--     * Slot: aims_entry_type Description: The kind of entry, AimsIncludedControl or AimsExcludedControl.
--     * Slot: aims_entry_justification Description: Why the control is included or left out.
-- # Class: AimsExcludedControl Description: An entry that leaves out an Annex A control the organization does not need, and says why.
--     * Slot: id
--     * Slot: aims_entry_annex_a_control Description: The Annex A control a Statement of Applicability entry concerns.
--     * Slot: aims_entry_type Description: The kind of entry, AimsIncludedControl or AimsExcludedControl.
--     * Slot: aims_entry_justification Description: Why the control is included or left out.
-- # Class: AimsControl Description: A control the organization has found it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
--     * Slot: aims_implementation_state Description: How far the control or the plan has been put into effect.
--     * Slot: aims_control_area Description: Which of Annex A's nine areas the control belongs to.
--     * Slot: aims_control_text Description: What the control does, in the organization's own words.
--     * Slot: aims_control_guidance Description: The organization's notes on putting the control in place.
--     * Slot: aims_control_owner Description: The person who owns the control.
--     * Slot: aims_control_implementation_date Description: When the control was put in place.
--     * Slot: aims_control_effectiveness Description: How well the control works, in the organization's own terms.
--     * Slot: aims_control_last_tested Description: When the control was last tested.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsAiSystem Description: One AI system under the management system: what it is for, how it is built, run and overseen, what it draws on, and what is kept about it.
--     * Slot: aims_system_intended_purpose Description: What the system is for.
--     * Slot: aims_system_domain Description: The field the system is applied in.
--     * Slot: aims_system_deployment_context Description: The setting the system runs in.
--     * Slot: aims_system_life_cycle_stage Description: The stage of its life the system is in now.
--     * Slot: aims_system_rationale Description: Why the system is being built, such as a business case or a customer's request.
--     * Slot: aims_system_ml_approach Description: The machine learning approach it takes, such as supervised or unsupervised.
--     * Slot: aims_system_continuous_learning Description: Whether what it meets in service goes on changing its behaviour.
--     * Slot: aims_system_automation_level Description: How much the system does without people.
--     * Slot: aims_system_deployment_plan Description: The documented information that holds the plan for putting it into service.
--     * Slot: aims_system_log_retention Description: How long the logs are kept, as an ISO 8601 duration.
--     * Slot: aims_system_human_oversight_required Description: Whether the system may be used only with people watching over it.
--     * Slot: aims_system_human_oversight Description: How people watch over the system, and who may overrule it.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Abstract Class: AimsSystemResource Description: Something an AI system draws on, told apart by its type, with the stages of the system's life that need it and who provides it.
--     * Slot: aims_resource_type Description: The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.
--     * Slot: aims_resource_provider Description: Who provides the resource.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsComponentResource Description: A part of a system, and how it is joined to the rest.
--     * Slot: aims_component_kind Description: What kind of part it is.
--     * Slot: aims_component_integration Description: How the part is joined to the system.
--     * Slot: aims_resource_type Description: The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.
--     * Slot: aims_resource_provider Description: Who provides the resource.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsDataResource Description: Data an AI system draws on: where it came from, what part it plays, how it was obtained, made ready and judged fit, and how long it is kept.
--     * Slot: aims_data_intended_use Description: What the data is for.
--     * Slot: aims_data_quantity Description: How much data is needed.
--     * Slot: aims_data_prior_handling Description: What was done with the data before, such as earlier uses.
--     * Slot: aims_data_provenance Description: The record of where the data came from and what happened to it.
--     * Slot: aims_data_provenance_verification Description: How that record is checked, where it needs to be.
--     * Slot: aims_data_representativeness Description: How well training data stands for what the system will meet in service.
--     * Slot: aims_data_labelling_process Description: How the data is labelled.
--     * Slot: aims_data_preparation_criteria Description: What decides how the data is made ready.
--     * Slot: aims_data_last_updated Description: When the data last changed.
--     * Slot: aims_data_retention Description: How long the data is kept and how it is disposed of.
--     * Slot: aims_data_classification Description: The information classification the data carries.
--     * Slot: aims_resource_type Description: The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.
--     * Slot: aims_resource_provider Description: Who provides the resource.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsToolingResource Description: A tool an AI system draws on, such as an algorithm, a model or a development tool.
--     * Slot: aims_tool_category Description: What kind of tool it is, such as a model or an evaluation method.
--     * Slot: aims_tool_version Description: The version in use.
--     * Slot: aims_tool_vendor Description: Who supplies the tool.
--     * Slot: aims_tool_licence Description: The terms the tool is used under.
--     * Slot: aims_tool_purpose Description: What the tool is used for.
--     * Slot: aims_resource_type Description: The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.
--     * Slot: aims_resource_provider Description: Who provides the resource.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsComputingResource Description: Hardware or computing an AI system draws on: what it needs, where it runs and what the hardware costs.
--     * Slot: aims_computing_requirements Description: What the system needs in order to run, such as on a small device.
--     * Slot: aims_computing_location Description: Where it runs, such as on the premises, in a cloud or at the edge.
--     * Slot: aims_computing_processing Description: The processing it provides, network and storage included.
--     * Slot: aims_computing_hardware_impact Description: What the hardware costs, in money or to the environment.
--     * Slot: aims_resource_type Description: The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.
--     * Slot: aims_resource_provider Description: Who provides the resource.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsHumanResource Description: People an AI system draws on: their skills and the work they do on it.
--     * Slot: aims_human_role Description: The role these people hold.
--     * Slot: aims_human_diversity Description: How the team's range of expertise was considered.
--     * Slot: aims_resource_type Description: The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.
--     * Slot: aims_resource_provider Description: Who provides the resource.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsDevelopmentProcess Description: A process for designing and building an AI system responsibly: the life cycle it follows, and what it asks of testing, oversight, data and approvals.
--     * Slot: aims_development_life_cycle_model Description: The life cycle model followed, which may be the organization's own.
--     * Slot: aims_development_testing Description: What must be tested and how.
--     * Slot: aims_development_human_oversight Description: What oversight by people is asked for, with its tools and processes.
--     * Slot: aims_development_training_data_rules Description: What data may be used, from which suppliers, and how it is labelled.
--     * Slot: aims_development_expertise Description: The expertise or training developers need.
--     * Slot: aims_development_change_control Description: How changes are controlled.
--     * Slot: aims_development_usability Description: What is asked of how easy the system is to use and how far people stay in control.
--     * Slot: aims_development_party_engagement Description: How interested parties are brought in.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsResponsibleUseProcess Description: A process for using AI systems responsibly: what decides if a system may be used, built in-house or brought in.
--     * Slot: aims_use_costs Description: What use costs, ongoing upkeep included.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsTechnicalDocumentation Description: Technical documents about an AI system for one kind of reader: what they hold, and the form they take.
--     * Slot: aims_technical_doc_form Description: The form the documents take for those readers.
--     * Slot: aims_technical_doc_failure_plan Description: How failures are managed, such as rolling back or turning features off.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsUserInformation Description: What those who use a system are told: the contents, how it reaches them, what decided it, and the check that they got it.
--     * Slot: aims_user_information_validated Description: Whether the organization has checked that users can get it and that it is right.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsIncidentCommunicationPlan Description: The plan for telling users when a system goes wrong: which incidents, how soon, to which authorities, and with what details.
--     * Slot: aims_incident_plan_timeline Description: How soon people must be told.
--     * Slot: aims_incident_plan_integration Description: How the plan fits the organization's wider handling of incidents.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsReportingObligation Description: Something the organization must report about a system to an interested party: to whom, under what rule, what and how soon.
--     * Slot: aims_obligation_basis Description: The law or agreement that creates the duty.
--     * Slot: aims_obligation_jurisdiction Description: The jurisdiction the duty arises in.
--     * Slot: aims_obligation_timeframe Description: How soon it must be reported.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsResource Description: A resource provided for the management system itself, such as people, time, tools or budget. What an AI system draws on is an AimsSystemResource.
--     * Slot: aims_support_category Description: What kind of resource it is.
--     * Slot: aims_support_quantity Description: How much of the resource is provided.
--     * Slot: aims_support_allocation_date Description: When the resource was allocated.
--     * Slot: aims_support_allocated_to Description: What the resource is allocated to.
--     * Slot: aims_support_cost Description: What the resource costs.
--     * Slot: aims_support_availability Description: Whether the resource is available now, in the organization's own terms.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsCompetenceRecord Description: The evidence of one person's competence for work that affects AI performance, and what is done to close any gap.
--     * Slot: aims_competence_person Description: The person the record is about.
--     * Slot: aims_competence_role Description: The role the person holds.
--     * Slot: aims_competence_assessment_date Description: When the person's competence was last assessed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsAwarenessProgramme Description: The programme that tells people working for the organization about the AI policy, their part in the system and what failing it would mean.
--     * Slot: aims_awareness_audience Description: Whom the programme is for.
--     * Slot: aims_awareness_frequency Description: How often the programme runs.
--     * Slot: aims_awareness_completion_tracking Description: How completion is tracked.
--     * Slot: aims_awareness_effectiveness Description: How the programme's effect is measured.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsCommunicationPlan Description: The plan for communication about the system, inside the organization and outside it.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsCommunication Description: One communication the plan provides for: what about, to whom, when, how, and who communicates.
--     * Slot: id
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_communication_subject Description: What the communication is about.
--     * Slot: aims_communication_purpose Description: Why it is communicated.
--     * Slot: aims_communication_audience Description: To whom it is communicated.
--     * Slot: aims_communication_external Description: Whether it goes outside the organization.
--     * Slot: aims_communication_timing Description: When it is communicated.
--     * Slot: aims_communication_method Description: How it is communicated.
--     * Slot: aims_communication_records_required Description: Whether a record of the communication is kept.
--     * Slot: AimsCommunicationPlan_aims_id Description: Autocreated FK slot
-- # Class: AimsDocumentedInformation Description: A document or record the system keeps under control that no more specific record describes, such as a procedure, a plan or a report.
--     * Slot: aims_document_kind Description: What kind of documented information it is.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsOperationalProcedure Description: A procedure by which the organization plans and controls the processes that meet its requirements, such as managing data for building or vetting suppliers.
--     * Slot: aims_procedure_scope Description: What the procedure covers.
--     * Slot: aims_procedure_criteria Description: The criteria the processes are run to.
--     * Slot: aims_procedure_change_control Description: How planned changes are controlled, and unplanned ones reviewed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsMonitoringProgramme Description: The programme that watches, measures, analyses and judges how well the system does and how well it works.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsMonitoringItem Description: One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
--     * Slot: id
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_monitoring_metric Description: The name of what is measured.
--     * Slot: aims_monitoring_description Description: What the measurement shows.
--     * Slot: aims_monitoring_method Description: How it is measured.
--     * Slot: aims_monitoring_frequency Description: How often it is measured.
--     * Slot: aims_monitoring_analysis_frequency Description: How often the results are analysed and evaluated.
--     * Slot: aims_monitoring_analyst Description: Who analyses and evaluates the results.
--     * Slot: aims_monitoring_target Description: The value aimed for.
--     * Slot: aims_monitoring_alert_threshold Description: The value that calls for action.
--     * Slot: aims_monitoring_current_value Description: The value last measured.
--     * Slot: aims_monitoring_trend Description: Which way the value is moving.
--     * Slot: AimsMonitoringProgramme_aims_id Description: Autocreated FK slot
-- # Class: AimsAuditProgramme Description: A programme of internal audits: the audits planned over a period, how often and why, and the resources and auditors they need.
--     * Slot: aims_programme_period Description: The period the programme covers.
--     * Slot: aims_programme_frequency_rationale Description: Why the audits happen as often as they do, given what matters most and past results.
--     * Slot: aims_programme_methods Description: How the audits are carried out.
--     * Slot: aims_programme_resources Description: The resources the programme needs.
--     * Slot: aims_programme_auditor_selection Description: How auditors are chosen so that they stay objective and impartial.
--     * Slot: aims_programme_status Description: Where the programme stands, in the organization's own terms.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsAudit Description: An audit of the system: an internal audit, or one by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
--     * Slot: aims_audit_type Description: Who carries out the audit, relative to the organization.
--     * Slot: aims_audit_scope Description: What the audit covers.
--     * Slot: aims_audit_period_start Description: When the audit began.
--     * Slot: aims_audit_period_end Description: When the audit ended.
--     * Slot: aims_audit_lead Description: Who led the audit.
--     * Slot: aims_audit_plan Description: The documented information that holds the audit plan.
--     * Slot: aims_audit_conclusion Description: The audit's overall conclusion.
--     * Slot: aims_audit_report_date Description: When the audit report was issued.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsAuditFinding Description: One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
--     * Slot: aims_finding_type Description: What kind of finding it is.
--     * Slot: aims_finding_control Description: The organization's control the finding concerns.
--     * Slot: aims_finding_evidence Description: The objective evidence for the finding.
--     * Slot: aims_finding_root_cause Description: What the analysis of the finding's cause found.
--     * Slot: aims_finding_risk Description: What the finding means for risk.
--     * Slot: aims_finding_recommendation Description: What the auditor recommends.
--     * Slot: aims_finding_auditee_response Description: How the auditee responded.
--     * Slot: aims_finding_corrective_action Description: The corrective action the finding led to.
--     * Slot: aims_finding_closure_status Description: Whether the finding is closed, in the organization's own terms.
--     * Slot: aims_finding_closure_date Description: When the finding was closed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
-- # Class: AimsManagementReview Description: A review of the system by top management: what it took in, what it decided and what it asked to be done.
--     * Slot: aims_review_held_on Description: When the review was held.
--     * Slot: aims_review_previous_actions Description: Where the actions from earlier reviews stand.
--     * Slot: aims_review_context_changes Description: How the matters that bear on the system have changed.
--     * Slot: aims_review_interested_party_changes Description: How interested parties' needs and expectations have changed.
--     * Slot: aims_review_nonconformity_trends Description: How nonconformities and their corrections have been trending.
--     * Slot: aims_review_monitoring_trends Description: The trends in what was monitored and measured.
--     * Slot: aims_review_audit_trends Description: The trends in audit results.
--     * Slot: aims_review_next_date Description: When the next review is planned.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsNonconformity Description: A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
--     * Slot: aims_nonconformity_source Description: How the nonconformity came to light, such as an audit, a review or an incident.
--     * Slot: aims_nonconformity_detected_on Description: When the nonconformity was found.
--     * Slot: aims_nonconformity_detected_by Description: Who or what found it.
--     * Slot: aims_nonconformity_requirement Description: The requirement not met, of the organization or of an interested party, in words.
--     * Slot: aims_nonconformity_consequences Description: How its consequences were dealt with.
--     * Slot: aims_nonconformity_root_cause Description: What caused it.
--     * Slot: aims_nonconformity_similar_check Description: Whether it could happen, or has happened, elsewhere.
--     * Slot: aims_nonconformity_status Description: Where the nonconformity stands, in the organization's own terms.
--     * Slot: aims_nonconformity_closure_date Description: When it was closed.
--     * Slot: aims_nonconformity_closure_evidence Description: What shows that it is closed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsCorrectiveAction Description: An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_action_root_cause Description: The cause the action removes.
--     * Slot: aims_action_target_date Description: When the action is to be complete.
--     * Slot: aims_action_completion_date Description: When the action was complete.
--     * Slot: aims_action_resources Description: The resources the action needs.
--     * Slot: aims_action_effectiveness_criteria Description: How the action's effect will be judged.
--     * Slot: aims_action_effectiveness_review_date Description: When the action's effect was reviewed.
--     * Slot: aims_action_effective Description: Whether the review found the action effective.
--     * Slot: aims_action_system_changes Description: The changes to the system the action needs.
--     * Slot: aims_action_status Description: Where the action stands, in the organization's own terms.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsImprovementOpportunity Description: An opportunity to make the system more suitable, adequate or effective, and what came of it.
--     * Slot: aims_responsible_role Description: The role that answers for the record's activity or outcome.
--     * Slot: aims_improvement_source Description: Where the opportunity came from, such as a review, an audit or daily work.
--     * Slot: aims_improvement_identified_on Description: When the opportunity was identified.
--     * Slot: aims_improvement_identified_by Description: Who identified it.
--     * Slot: aims_improvement_benefit Description: What the improvement is expected to bring.
--     * Slot: aims_improvement_priority Description: How soon it is to be acted on, in the organization's own terms.
--     * Slot: aims_improvement_plan Description: How the improvement is to be made.
--     * Slot: aims_improvement_target_date Description: When the improvement is to be made.
--     * Slot: aims_improvement_completion_date Description: When it was made.
--     * Slot: aims_improvement_outcome Description: What the improvement brought.
--     * Slot: aims_improvement_status Description: Where it stands, in the organization's own terms.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsThirdPartyRelationship Description: A relationship with another party in an AI system's life, such as a partner: who carries which duty, and what assures the organization of that.
--     * Slot: aims_relationship_type Description: The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship.
--     * Slot: aims_relationship_party Description: The other party.
--     * Slot: aims_relationship_contract Description: The agreement the relationship rests on.
--     * Slot: aims_relationship_pii_role Description: The part the other party plays when personal data is processed.
--     * Slot: aims_relationship_review_frequency Description: How often the relationship is reviewed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsSupplierRelationship Description: A relationship with a supplier to the organization's AI work: what it provides, the risk that brings, and how it is held to the organization's approach.
--     * Slot: aims_supplier_risk Description: How much risk what it provides brings.
--     * Slot: aims_supplier_monitoring Description: How the supplier is watched and judged over time.
--     * Slot: aims_supplier_integration Description: How what it provides is joined to the organization's systems.
--     * Slot: aims_relationship_type Description: The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship.
--     * Slot: aims_relationship_party Description: The other party.
--     * Slot: aims_relationship_contract Description: The agreement the relationship rests on.
--     * Slot: aims_relationship_pii_role Description: The part the other party plays when personal data is processed.
--     * Slot: aims_relationship_review_frequency Description: How often the relationship is reviewed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsCustomerRelationship Description: A relationship with a customer of the organization's AI work: what it expects, who answers for what, and which limits it was told of.
--     * Slot: aims_customer_agreement Description: The contract or terms of use that apply.
--     * Slot: aims_customer_responsibility_split Description: What the provider answers for, and what the customer answers for.
--     * Slot: aims_relationship_type Description: The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship.
--     * Slot: aims_relationship_party Description: The other party.
--     * Slot: aims_relationship_contract Description: The agreement the relationship rests on.
--     * Slot: aims_relationship_pii_role Description: The part the other party plays when personal data is processed.
--     * Slot: aims_relationship_review_frequency Description: How often the relationship is reviewed.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsSystemEvent Description: Something that happened with a system and was reported, by monitoring, by a user or by someone outside, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an AimsIncident.
--     * Slot: aims_event_type Description: The kind of record, AimsSystemEvent or AimsIncident.
--     * Slot: aims_event_occurred_at Description: When the event happened, or when it was first noticed.
--     * Slot: aims_event_reporter Description: Who reported the event.
--     * Slot: aims_event_source Description: How the event came to light, such as a log, monitoring or a report from outside.
--     * Slot: aims_event_adverse_impact Description: The harm that was reported, if any.
--     * Slot: aims_event_assessment Description: What the assessment of the event found.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsIncident Description: An event assessed as an incident: what it concerns, how severe it is, what was done, who was told, and what was learned.
--     * Slot: aims_incident_category Description: What the incident concerns.
--     * Slot: aims_incident_severity Description: How severe the incident is.
--     * Slot: aims_incident_detection_method Description: How the incident was detected.
--     * Slot: aims_incident_root_cause Description: What caused the incident.
--     * Slot: aims_incident_notification_required Description: Whether users, authorities or others had to be told.
--     * Slot: aims_incident_closed_at Description: When the incident was closed.
--     * Slot: aims_event_type Description: The kind of record, AimsSystemEvent or AimsIncident.
--     * Slot: aims_event_occurred_at Description: When the event happened, or when it was first noticed.
--     * Slot: aims_event_reporter Description: Who reported the event.
--     * Slot: aims_event_source Description: How the event came to light, such as a log, monitoring or a report from outside.
--     * Slot: aims_event_adverse_impact Description: The harm that was reported, if any.
--     * Slot: aims_event_assessment Description: What the assessment of the event found.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: AimsConcernReportingProcess Description: The way people raise worries about the organization's part in a system: how it keeps them safe, who looks into a worry, and how fast it answers.
--     * Slot: aims_concern_process_audience Description: How staff and contractors learn of it and reach it.
--     * Slot: aims_concern_process_investigators Description: Who looks into a report, and what powers they hold.
--     * Slot: aims_concern_process_escalation Description: How a report reaches management in good time.
--     * Slot: aims_concern_process_reprisal_protection Description: How those who report or investigate are shielded from reprisal.
--     * Slot: aims_concern_process_response_time Description: How soon a report is answered.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: aims_document_reference Description: The reference the organization's document control gives it.
--     * Slot: aims_document_version Description: The version of the document.
--     * Slot: aims_document_author Description: Who wrote the document.
--     * Slot: aims_document_owner Description: Who answers for the document's content and upkeep.
--     * Slot: aims_document_format Description: The document's format, such as its language or software version.
--     * Slot: aims_document_medium Description: What the document is held on, such as paper or an electronic system.
--     * Slot: aims_document_approver Description: Who approved the document.
--     * Slot: aims_document_approval_date Description: When the document was approved.
--     * Slot: aims_document_effective_date Description: When the document takes effect.
--     * Slot: aims_document_last_review_date Description: When the document was last reviewed.
--     * Slot: aims_document_next_review_date Description: When the document is next due for review.
--     * Slot: aims_document_status Description: Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.
--     * Slot: aims_document_classification Description: The information classification the document carries.
--     * Slot: aims_document_retention Description: How long the document is kept, as an ISO 8601 duration.
--     * Slot: aims_document_disposition Description: What becomes of the document when that time is up.
--     * Slot: aims_document_storage Description: How the document is stored so that it stays legible.
--     * Slot: aims_document_change_control Description: How changes to the document are controlled, such as version control.
--     * Slot: aims_document_external_origin Description: Whether the document comes from outside the organization and is kept because the system needs it.
--     * Slot: aims_document_external_source Description: Who the document came from, when it comes from outside.
-- # Class: AimsConcernReport Description: One worry someone raised about the organization's part in a system, and how it was looked into and settled.
--     * Slot: aims_concern_reported_on Description: When the worry was raised.
--     * Slot: aims_concern_reporter Description: Who raised it, unless they stayed unnamed.
--     * Slot: aims_concern_anonymous Description: Whether the person stayed unnamed.
--     * Slot: aims_concern_channel Description: How it was raised.
--     * Slot: aims_concern_life_cycle_stage Description: The stage of the system's life it concerns.
--     * Slot: aims_concern_severity Description: How serious it is.
--     * Slot: aims_concern_investigator Description: Who looked into it.
--     * Slot: aims_concern_investigation_status Description: Where the inquiry stands, in the organization's own terms.
--     * Slot: aims_concern_findings Description: What the inquiry found.
--     * Slot: aims_concern_escalation Description: Whether and how it went up to management.
--     * Slot: aims_concern_response_due Description: When an answer is due.
--     * Slot: aims_concern_responded_on Description: When it was answered.
--     * Slot: aims_concern_resolution Description: How it was settled.
--     * Slot: aims_concern_reprisal_protection Description: What was done to shield those involved from reprisal.
--     * Slot: aims_id Description: The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
-- # Class: AimsDocumentControlMixin_aims_document_distribution
--     * Slot: AimsDocumentControlMixin_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsManagementSystem_aims_leadership_evidence
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_leadership_evidence Description: What shows that top management leads and commits to the system.
-- # Class: AimsManagementSystem_aims_scope_boundaries
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_scope_boundaries Description: Where the system stops.
-- # Class: AimsManagementSystem_aims_scope_applicability
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_scope_applicability Description: What in the organization's work the system applies to.
-- # Class: AimsManagementSystem_aims_internal_issues
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_internal_issues Description: The matters inside the organization that bear on the system.
-- # Class: AimsManagementSystem_aims_external_issues
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_external_issues Description: The matters outside the organization that bear on the system.
-- # Class: AimsManagementSystem_aims_planned_changes
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_planned_changes Description: The changes to the system that are planned.
-- # Class: AimsManagementSystem_aims_external_services
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_external_services Description: What the system takes from outside the organization and keeps under control.
-- # Class: AimsManagementSystem_aims_integrated_standards
--     * Slot: AimsManagementSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_integrated_standards Description: Other standards for management systems that this one is run beside.
-- # Class: AimsOrganization_aims_organization_trading_names
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_trading_names Description: Other names the organization trades under.
-- # Class: AimsOrganization_aims_organization_sectors
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_sectors Description: The sectors the organization works in, such as health or finance.
-- # Class: AimsOrganization_aims_organization_locations
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_locations Description: The countries or regions the organization works in.
-- # Class: AimsOrganization_aims_organization_jurisdictions
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_jurisdictions Description: The jurisdictions whose laws and regulations apply to the organization.
-- # Class: AimsOrganization_aims_organization_subsidiaries
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_subsidiaries Description: The organization's subsidiaries, if it has any.
-- # Class: AimsOrganization_aims_organization_ai_roles
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_ai_roles Description: The parts the organization plays towards its AI systems.
-- # Class: AimsOrganization_aims_organization_pii_roles
--     * Slot: AimsOrganization_aims_id Description: Autocreated FK slot
--     * Slot: aims_organization_pii_roles Description: The parts the organization plays when its AI systems process personal data.
-- # Class: AimsInterestedParty_aims_party_ai_roles
--     * Slot: AimsInterestedParty_aims_id Description: Autocreated FK slot
--     * Slot: aims_party_ai_roles Description: The parts the party plays towards the organization's AI systems.
-- # Class: AimsInterestedParty_aims_party_requirements
--     * Slot: AimsInterestedParty_aims_id Description: Autocreated FK slot
--     * Slot: aims_party_requirements Description: The party's requirements that bear on the system.
-- # Class: AimsInterestedParty_aims_party_addressed_requirements
--     * Slot: AimsInterestedParty_aims_id Description: Autocreated FK slot
--     * Slot: aims_party_addressed_requirements Description: Which of those requirements the system addresses.
-- # Class: AimsInterestedParty_aims_party_climate_change_requirements
--     * Slot: AimsInterestedParty_aims_id Description: Autocreated FK slot
--     * Slot: aims_party_climate_change_requirements Description: The party's requirements that concern climate change.
-- # Class: AimsPolicy_aims_cited_clauses
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_clauses Description: The clauses of the standard the record answers to or concerns.
-- # Class: AimsPolicy_aims_cited_annex_a_controls
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsPolicy_aims_policy_commitments
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_policy_commitments Description: The commitments the policy makes, at least to meeting requirements and to improving.
-- # Class: AimsPolicy_aims_policy_principles
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_policy_principles Description: The principles that guide what the organization does with AI.
-- # Class: AimsPolicy_aims_policy_influences
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_policy_influences Description: What shaped the policy, such as strategy, values, the law or the risks.
-- # Class: AimsPolicy_aims_policy_related_policies
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_policy_related_policies Description: The organization's other policies this one refers to or touches.
-- # Class: AimsPolicy_aims_document_distribution
--     * Slot: AimsPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsTopicSpecificPolicy_aims_relevant_controls
--     * Slot: AimsTopicSpecificPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_relevant_controls_aims_id Description: The organization's controls that the record concerns.
-- # Class: AimsTopicSpecificPolicy_aims_cited_annex_a_controls
--     * Slot: AimsTopicSpecificPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsTopicSpecificPolicy_aims_document_distribution
--     * Slot: AimsTopicSpecificPolicy_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsRole_aims_role_areas
--     * Slot: AimsRole_aims_id Description: Autocreated FK slot
--     * Slot: aims_role_areas Description: The areas the role covers, such as privacy, safety or human oversight.
-- # Class: AimsRole_aims_role_responsibilities
--     * Slot: AimsRole_aims_id Description: Autocreated FK slot
--     * Slot: aims_role_responsibilities Description: The duties assigned to the role.
-- # Class: AimsRole_aims_role_authorities
--     * Slot: AimsRole_aims_id Description: Autocreated FK slot
--     * Slot: aims_role_authorities Description: The powers the role carries.
-- # Class: AimsRole_aims_role_holders
--     * Slot: AimsRole_aims_id Description: Autocreated FK slot
--     * Slot: aims_role_holders Description: The people who hold the role.
-- # Class: AimsObjective_aims_relevant_controls
--     * Slot: AimsObjective_aims_id Description: Autocreated FK slot
--     * Slot: aims_relevant_controls_aims_id Description: The organization's controls that the record concerns.
-- # Class: AimsObjective_aims_objective_categories
--     * Slot: AimsObjective_aims_id Description: Autocreated FK slot
--     * Slot: aims_objective_categories Description: The kinds of objective the record bears on.
-- # Class: AimsObjective_aims_objective_risks
--     * Slot: AimsObjective_aims_id Description: Autocreated FK slot
--     * Slot: aims_objective_risks_aims_id Description: The risks that help or hinder the objective.
-- # Class: AimsPlannedAction_aims_ai_systems
--     * Slot: AimsPlannedAction_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsPlannedAction_aims_planned_action_risks
--     * Slot: AimsPlannedAction_aims_id Description: Autocreated FK slot
--     * Slot: aims_planned_action_risks_aims_id Description: The risks the action addresses.
-- # Class: AimsPlannedAction_aims_planned_action_opportunities
--     * Slot: AimsPlannedAction_aims_id Description: Autocreated FK slot
--     * Slot: aims_planned_action_opportunities Description: The opportunities the action addresses.
-- # Class: AimsRiskAssessmentProcess_aims_risk_criteria
--     * Slot: AimsRiskAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_criteria Description: The criteria for AI risk, which tell acceptable risk from the rest and steer assessment, treatment and the weighing of impacts.
-- # Class: AimsRiskAssessmentProcess_aims_risk_assessment_triggers
--     * Slot: AimsRiskAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_assessment_triggers Description: The changes that start an assessment outside the schedule.
-- # Class: AimsRiskAssessmentProcess_aims_document_distribution
--     * Slot: AimsRiskAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsRiskAssessment_aims_ai_systems
--     * Slot: AimsRiskAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsRiskAssessment_aims_assessment_risks
--     * Slot: AimsRiskAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_assessment_risks_aims_id Description: The risks the assessment identified.
-- # Class: AimsRiskAssessment_aims_assessment_impact_assessments
--     * Slot: AimsRiskAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_assessment_impact_assessments_aims_id Description: The impact assessments the assessment drew on.
-- # Class: AimsRiskAssessment_aims_assessment_recommendations
--     * Slot: AimsRiskAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_assessment_recommendations Description: What the assessment recommends.
-- # Class: AimsRiskAssessment_aims_document_distribution
--     * Slot: AimsRiskAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsRisk_aims_ai_systems
--     * Slot: AimsRisk_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsRisk_aims_risk_source_categories
--     * Slot: AimsRisk_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_source_categories Description: The kinds of risk source the record bears on.
-- # Class: AimsRisk_aims_risk_objectives
--     * Slot: AimsRisk_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_objectives_aims_id Description: The AI objectives the risk helps or hinders.
-- # Class: AimsRisk_aims_risk_existing_controls
--     * Slot: AimsRisk_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_existing_controls_aims_id Description: The organization's controls already acting on the risk.
-- # Class: AimsRisk_aims_risk_impact_assessments
--     * Slot: AimsRisk_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_impact_assessments_aims_id Description: The impact assessments that inform the risk.
-- # Class: AimsRiskTreatmentProcess_aims_document_distribution
--     * Slot: AimsRiskTreatmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsRiskTreatmentPlan_aims_plan_risks
--     * Slot: AimsRiskTreatmentPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_plan_risks_aims_id Description: The risks the plan treats.
-- # Class: AimsRiskTreatmentPlan_aims_plan_actions
--     * Slot: AimsRiskTreatmentPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_plan_actions Description: The actions the plan takes.
-- # Class: AimsRiskTreatmentPlan_aims_plan_controls
--     * Slot: AimsRiskTreatmentPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_plan_controls_aims_id Description: The controls the plan puts in place.
-- # Class: AimsRiskTreatmentPlan_aims_plan_responsible_parties
--     * Slot: AimsRiskTreatmentPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_plan_responsible_parties Description: Who carries out the plan.
-- # Class: AimsRiskTreatmentPlan_aims_document_distribution
--     * Slot: AimsRiskTreatmentPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsImpactAssessmentProcess_aims_impact_process_triggers
--     * Slot: AimsImpactAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_process_triggers Description: What calls for an assessment, such as how critical the use is or a large change.
-- # Class: AimsImpactAssessmentProcess_aims_impact_process_steps
--     * Slot: AimsImpactAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_process_steps Description: The steps of an assessment, from finding impacts to reporting them.
-- # Class: AimsImpactAssessmentProcess_aims_impact_process_subjects
--     * Slot: AimsImpactAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_process_subjects Description: Who the process looks at.
-- # Class: AimsImpactAssessmentProcess_aims_impact_process_areas
--     * Slot: AimsImpactAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_process_areas Description: The areas of impact the process looks at.
-- # Class: AimsImpactAssessmentProcess_aims_document_distribution
--     * Slot: AimsImpactAssessmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsImpactAssessment_aims_ai_systems
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsImpactAssessment_aims_impact_jurisdictions
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_jurisdictions Description: The jurisdictions that apply to where the system runs.
-- # Class: AimsImpactAssessment_aims_impact_demographic_groups
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_demographic_groups Description: The groups of people the system is meant for or touches.
-- # Class: AimsImpactAssessment_aims_impact_failures
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_failures Description: The failures that can be foreseen, their effects and what limits them.
-- # Class: AimsImpactAssessment_aims_impact_shared_with
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_impact_shared_with_aims_id Description: The interested parties told of the result.
-- # Class: AimsImpactAssessment_aims_document_distribution
--     * Slot: AimsImpactAssessment_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsIdentifiedImpact_aims_identified_impact_mitigation
--     * Slot: AimsIdentifiedImpact_id Description: Autocreated FK slot
--     * Slot: aims_identified_impact_mitigation Description: What is done to limit the harm.
-- # Class: AimsStatementOfApplicability_aims_document_distribution
--     * Slot: AimsStatementOfApplicability_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsApplicabilityEntry_aims_ai_systems
--     * Slot: AimsApplicabilityEntry_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsIncludedControl_aims_included_risks
--     * Slot: AimsIncludedControl_id Description: Autocreated FK slot
--     * Slot: aims_included_risks_aims_id Description: The risks the control answers to.
-- # Class: AimsIncludedControl_aims_ai_systems
--     * Slot: AimsIncludedControl_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsExcludedControl_aims_ai_systems
--     * Slot: AimsExcludedControl_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsControl_aims_relevant_controls
--     * Slot: AimsControl_aims_id Description: Autocreated FK slot
--     * Slot: aims_relevant_controls_aims_id Description: The organization's controls that the record concerns.
-- # Class: AimsControl_aims_cited_annex_a_controls
--     * Slot: AimsControl_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsControl_aims_ai_systems
--     * Slot: AimsControl_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsControl_aims_objective_categories
--     * Slot: AimsControl_aims_id Description: Autocreated FK slot
--     * Slot: aims_objective_categories Description: The kinds of objective the record bears on.
-- # Class: AimsControl_aims_risk_source_categories
--     * Slot: AimsControl_aims_id Description: Autocreated FK slot
--     * Slot: aims_risk_source_categories Description: The kinds of risk source the record bears on.
-- # Class: AimsControl_aims_control_evidence
--     * Slot: AimsControl_aims_id Description: Autocreated FK slot
--     * Slot: aims_control_evidence Description: Where the evidence that the control is in place is kept.
-- # Class: AimsAiSystem_aims_relevant_controls
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_relevant_controls_aims_id Description: The organization's controls that the record concerns.
-- # Class: AimsAiSystem_aims_system_intended_uses
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_intended_uses Description: The uses the system is meant for.
-- # Class: AimsAiSystem_aims_system_foreseeable_misuse
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_foreseeable_misuse Description: The ways people could predictably misuse the system.
-- # Class: AimsAiSystem_aims_system_organization_roles
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_organization_roles Description: The parts the organization plays towards this system.
-- # Class: AimsAiSystem_aims_system_pii_roles
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_pii_roles Description: The parts the organization plays when this system processes personal data.
-- # Class: AimsAiSystem_aims_system_requirements
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_requirements Description: What the system must meet, across its whole life.
-- # Class: AimsAiSystem_aims_system_model_types
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_model_types Description: The learning algorithms and kinds of model it uses.
-- # Class: AimsAiSystem_aims_system_threats
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_threats Description: The threats peculiar to AI that were considered for the system.
-- # Class: AimsAiSystem_aims_system_verification_measures
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_verification_measures Description: The tests, data and methods used to verify and validate the system.
-- # Class: AimsAiSystem_aims_system_evaluation_criteria
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_evaluation_criteria Description: What the system is judged against, such as a limit on its errors.
-- # Class: AimsAiSystem_aims_system_release_criteria
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_release_criteria Description: What must hold before the system is released.
-- # Class: AimsAiSystem_aims_system_operation_elements
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_operation_elements Description: What keeping the system in service takes, such as watching, repairs and updates.
-- # Class: AimsAiSystem_aims_system_performance_metrics
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_performance_metrics Description: The measures of how the system does in service, with acceptable values.
-- # Class: AimsAiSystem_aims_system_log_stages
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_log_stages Description: The stages of its life at which the system keeps event logs.
-- # Class: AimsAiSystem_aims_system_log_contents
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_log_contents Description: What the logs record, such as times of use or out-of-range results.
-- # Class: AimsAiSystem_aims_system_human_oversight_stages
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_human_oversight_stages Description: The stages of its life at which people watch over the system.
-- # Class: AimsAiSystem_aims_system_resources_used
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_resources_used_aims_id Description: The resources the system draws on.
-- # Class: AimsAiSystem_aims_system_technical_documents
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_technical_documents_aims_id Description: The technical documents kept for the system.
-- # Class: AimsAiSystem_aims_system_impact_assessments
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_impact_assessments_aims_id Description: The impact assessments of the system.
-- # Class: AimsAiSystem_aims_system_relationships
--     * Slot: AimsAiSystem_aims_id Description: Autocreated FK slot
--     * Slot: aims_system_relationships_aims_id Description: The partners, suppliers and customers that deal with the system.
-- # Class: AimsSystemResource_aims_life_cycle_stages
--     * Slot: AimsSystemResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsComponentResource_aims_life_cycle_stages
--     * Slot: AimsComponentResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsDataResource_aims_data_categories
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_categories Description: The parts the data plays in machine learning.
-- # Class: AimsDataResource_aims_data_kinds
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_kinds Description: What kind of data it is, in a classification the organization names.
-- # Class: AimsDataResource_aims_data_sources
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_sources Description: Where the data comes from, such as bought, shared, open or synthetic.
-- # Class: AimsDataResource_aims_data_source_characteristics
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_source_characteristics Description: How the source behaves, such as fixed, streamed or made by machine.
-- # Class: AimsDataResource_aims_data_subject_demographics
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_subject_demographics Description: Who the data is about, with any known bias or systematic error.
-- # Class: AimsDataResource_aims_data_rights
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_rights Description: The rights bearing on the data, such as personal data or copyright.
-- # Class: AimsDataResource_aims_data_metadata
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_metadata Description: The metadata that comes with it, such as details of labelling.
-- # Class: AimsDataResource_aims_data_quality_requirements
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_quality_requirements Description: What quality the data must have.
-- # Class: AimsDataResource_aims_data_quality_results
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_quality_results Description: How the data measures up to those requirements.
-- # Class: AimsDataResource_aims_data_bias_issues
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_bias_issues Description: Known or suspected bias in the data.
-- # Class: AimsDataResource_aims_data_preparation_methods
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_data_preparation_methods Description: The methods used to make the data ready.
-- # Class: AimsDataResource_aims_life_cycle_stages
--     * Slot: AimsDataResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsToolingResource_aims_life_cycle_stages
--     * Slot: AimsToolingResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsComputingResource_aims_life_cycle_stages
--     * Slot: AimsComputingResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsHumanResource_aims_human_competences
--     * Slot: AimsHumanResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_human_competences Description: The skills they bring.
-- # Class: AimsHumanResource_aims_human_activities
--     * Slot: AimsHumanResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_human_activities Description: The work they do on the system, from building it to decommissioning it.
-- # Class: AimsHumanResource_aims_life_cycle_stages
--     * Slot: AimsHumanResource_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsDevelopmentProcess_aims_ai_systems
--     * Slot: AimsDevelopmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsDevelopmentProcess_aims_development_impact_assessment_stages
--     * Slot: AimsDevelopmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_development_impact_assessment_stages Description: The stages at which impact assessments run.
-- # Class: AimsDevelopmentProcess_aims_development_release_criteria
--     * Slot: AimsDevelopmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_development_release_criteria Description: What must hold before a release.
-- # Class: AimsDevelopmentProcess_aims_development_approvals
--     * Slot: AimsDevelopmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_development_approvals Description: Who must approve what, at each stage.
-- # Class: AimsDevelopmentProcess_aims_document_distribution
--     * Slot: AimsDevelopmentProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsResponsibleUseProcess_aims_ai_systems
--     * Slot: AimsResponsibleUseProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsResponsibleUseProcess_aims_use_approvals
--     * Slot: AimsResponsibleUseProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_use_approvals Description: The approvals needed before use.
-- # Class: AimsResponsibleUseProcess_aims_use_sourcing_requirements
--     * Slot: AimsResponsibleUseProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_use_sourcing_requirements Description: What a system or its supplier must meet to be taken on.
-- # Class: AimsResponsibleUseProcess_aims_use_legal_requirements
--     * Slot: AimsResponsibleUseProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_use_legal_requirements Description: The laws that bear on use.
-- # Class: AimsResponsibleUseProcess_aims_document_distribution
--     * Slot: AimsResponsibleUseProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsTechnicalDocumentation_aims_ai_systems
--     * Slot: AimsTechnicalDocumentation_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsTechnicalDocumentation_aims_technical_doc_audiences
--     * Slot: AimsTechnicalDocumentation_aims_id Description: Autocreated FK slot
--     * Slot: aims_technical_doc_audiences Description: Who the documents are for, such as users or a supervisory authority.
-- # Class: AimsTechnicalDocumentation_aims_technical_doc_contents
--     * Slot: AimsTechnicalDocumentation_aims_id Description: Autocreated FK slot
--     * Slot: aims_technical_doc_contents Description: What the documents hold, such as limits, design choices or test records.
-- # Class: AimsTechnicalDocumentation_aims_document_distribution
--     * Slot: AimsTechnicalDocumentation_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsUserInformation_aims_ai_systems
--     * Slot: AimsUserInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsUserInformation_aims_user_information_contents
--     * Slot: AimsUserInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_user_information_contents Description: What users are told, such as that AI is behind what they see and how to overrule it.
-- # Class: AimsUserInformation_aims_user_information_channels
--     * Slot: AimsUserInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_user_information_channels Description: How it reaches them, such as instructions, alerts or a web page.
-- # Class: AimsUserInformation_aims_user_information_criteria
--     * Slot: AimsUserInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_user_information_criteria Description: What decided what they are told.
-- # Class: AimsUserInformation_aims_document_distribution
--     * Slot: AimsUserInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsIncidentCommunicationPlan_aims_ai_systems
--     * Slot: AimsIncidentCommunicationPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsIncidentCommunicationPlan_aims_incident_plan_categories
--     * Slot: AimsIncidentCommunicationPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_plan_categories Description: The kinds of incident the plan covers.
-- # Class: AimsIncidentCommunicationPlan_aims_incident_plan_authorities
--     * Slot: AimsIncidentCommunicationPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_plan_authorities Description: The authorities that must be told, if any.
-- # Class: AimsIncidentCommunicationPlan_aims_incident_plan_details
--     * Slot: AimsIncidentCommunicationPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_plan_details Description: What each notice must say.
-- # Class: AimsIncidentCommunicationPlan_aims_document_distribution
--     * Slot: AimsIncidentCommunicationPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsReportingObligation_aims_ai_systems
--     * Slot: AimsReportingObligation_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsReportingObligation_aims_obligation_parties
--     * Slot: AimsReportingObligation_aims_id Description: Autocreated FK slot
--     * Slot: aims_obligation_parties_aims_id Description: Who must be told.
-- # Class: AimsReportingObligation_aims_obligation_contents
--     * Slot: AimsReportingObligation_aims_id Description: Autocreated FK slot
--     * Slot: aims_obligation_contents Description: What must be reported, such as risks, assessments or logs.
-- # Class: AimsCompetenceRecord_aims_competence_required
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_competence_required Description: The competences the role needs.
-- # Class: AimsCompetenceRecord_aims_competence_education
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_competence_education Description: The person's relevant education.
-- # Class: AimsCompetenceRecord_aims_competence_training
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_competence_training Description: The training the person has completed.
-- # Class: AimsCompetenceRecord_aims_competence_experience
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_competence_experience Description: The person's relevant experience.
-- # Class: AimsCompetenceRecord_aims_competence_gaps
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_competence_gaps Description: The gaps the assessment found.
-- # Class: AimsCompetenceRecord_aims_competence_actions
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_competence_actions Description: What is done to close the gaps, and how well it worked.
-- # Class: AimsCompetenceRecord_aims_document_distribution
--     * Slot: AimsCompetenceRecord_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsAwarenessProgramme_aims_awareness_topics
--     * Slot: AimsAwarenessProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_awareness_topics Description: The topics the programme covers.
-- # Class: AimsAwarenessProgramme_aims_awareness_methods
--     * Slot: AimsAwarenessProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_awareness_methods Description: How the programme is delivered.
-- # Class: AimsAwarenessProgramme_aims_document_distribution
--     * Slot: AimsAwarenessProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsCommunicationPlan_aims_document_distribution
--     * Slot: AimsCommunicationPlan_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsDocumentedInformation_aims_cited_clauses
--     * Slot: AimsDocumentedInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_clauses Description: The clauses of the standard the record answers to or concerns.
-- # Class: AimsDocumentedInformation_aims_cited_annex_a_controls
--     * Slot: AimsDocumentedInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsDocumentedInformation_aims_document_distribution
--     * Slot: AimsDocumentedInformation_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsOperationalProcedure_aims_relevant_controls
--     * Slot: AimsOperationalProcedure_aims_id Description: Autocreated FK slot
--     * Slot: aims_relevant_controls_aims_id Description: The organization's controls that the record concerns.
-- # Class: AimsOperationalProcedure_aims_cited_annex_a_controls
--     * Slot: AimsOperationalProcedure_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsOperationalProcedure_aims_procedure_control_measures
--     * Slot: AimsOperationalProcedure_aims_id Description: Autocreated FK slot
--     * Slot: aims_procedure_control_measures Description: The measures that control the processes.
-- # Class: AimsOperationalProcedure_aims_procedure_roles
--     * Slot: AimsOperationalProcedure_aims_id Description: Autocreated FK slot
--     * Slot: aims_procedure_roles_aims_id Description: The roles that carry out the procedure.
-- # Class: AimsOperationalProcedure_aims_document_distribution
--     * Slot: AimsOperationalProcedure_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsMonitoringProgramme_aims_document_distribution
--     * Slot: AimsMonitoringProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsAuditProgramme_aims_programme_audits
--     * Slot: AimsAuditProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_programme_audits_aims_id Description: The audits the programme plans.
-- # Class: AimsAuditProgramme_aims_programme_responsibilities
--     * Slot: AimsAuditProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_programme_responsibilities Description: Who answers for planning, running and reporting them.
-- # Class: AimsAuditProgramme_aims_document_distribution
--     * Slot: AimsAuditProgramme_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsAudit_aims_audit_standards
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_audit_standards Description: Other standards for management systems the audit covers.
-- # Class: AimsAudit_aims_audit_criteria
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_audit_criteria Description: What the audit compares the system against.
-- # Class: AimsAudit_aims_audit_objectives
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_audit_objectives Description: What the audit sets out to establish.
-- # Class: AimsAudit_aims_audit_team
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_audit_team Description: Who else audited.
-- # Class: AimsAudit_aims_audit_auditees
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_audit_auditees Description: Who represented the parts of the organization audited.
-- # Class: AimsAudit_aims_audit_report_distribution
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_audit_report_distribution Description: Who received the audit report.
-- # Class: AimsAudit_aims_document_distribution
--     * Slot: AimsAudit_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsAuditFinding_aims_cited_clauses
--     * Slot: AimsAuditFinding_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_clauses Description: The clauses of the standard the record answers to or concerns.
-- # Class: AimsAuditFinding_aims_cited_annex_a_controls
--     * Slot: AimsAuditFinding_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsManagementReview_aims_review_attendees
--     * Slot: AimsManagementReview_aims_id Description: Autocreated FK slot
--     * Slot: aims_review_attendees Description: Who attended the review.
-- # Class: AimsManagementReview_aims_review_improvement_opportunities
--     * Slot: AimsManagementReview_aims_id Description: Autocreated FK slot
--     * Slot: aims_review_improvement_opportunities Description: The opportunities for improvement raised.
-- # Class: AimsManagementReview_aims_review_decisions
--     * Slot: AimsManagementReview_aims_id Description: Autocreated FK slot
--     * Slot: aims_review_decisions Description: What the review decided about improving.
-- # Class: AimsManagementReview_aims_review_system_changes
--     * Slot: AimsManagementReview_aims_id Description: Autocreated FK slot
--     * Slot: aims_review_system_changes Description: The changes to the system the review found were needed.
-- # Class: AimsManagementReview_aims_review_actions
--     * Slot: AimsManagementReview_aims_id Description: Autocreated FK slot
--     * Slot: aims_review_actions Description: What the review asked to be done.
-- # Class: AimsManagementReview_aims_document_distribution
--     * Slot: AimsManagementReview_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsNonconformity_aims_cited_clauses
--     * Slot: AimsNonconformity_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_clauses Description: The clauses of the standard the record answers to or concerns.
-- # Class: AimsNonconformity_aims_cited_annex_a_controls
--     * Slot: AimsNonconformity_aims_id Description: Autocreated FK slot
--     * Slot: aims_cited_annex_a_controls Description: The controls of Annex A the record answers to or concerns.
-- # Class: AimsNonconformity_aims_nonconformity_immediate_actions
--     * Slot: AimsNonconformity_aims_id Description: Autocreated FK slot
--     * Slot: aims_nonconformity_immediate_actions Description: What was done at once to contain and fix it.
-- # Class: AimsCorrectiveAction_aims_action_nonconformities
--     * Slot: AimsCorrectiveAction_aims_id Description: Autocreated FK slot
--     * Slot: aims_action_nonconformities_aims_id Description: The nonconformities the action addresses.
-- # Class: AimsThirdPartyRelationship_aims_ai_systems
--     * Slot: AimsThirdPartyRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsThirdPartyRelationship_aims_life_cycle_stages
--     * Slot: AimsThirdPartyRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsThirdPartyRelationship_aims_relationship_party_roles
--     * Slot: AimsThirdPartyRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_party_roles Description: The parts the other party plays towards the system.
-- # Class: AimsThirdPartyRelationship_aims_relationship_responsibilities
--     * Slot: AimsThirdPartyRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_responsibilities Description: The duties each side carries.
-- # Class: AimsThirdPartyRelationship_aims_relationship_documentation
--     * Slot: AimsThirdPartyRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_documentation Description: The documents one side owes the other about the system.
-- # Class: AimsThirdPartyRelationship_aims_relationship_assurance_evidence
--     * Slot: AimsThirdPartyRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_assurance_evidence Description: What assures the organization that the party meets its duties.
-- # Class: AimsSupplierRelationship_aims_supplier_provides
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_supplier_provides Description: What it provides, such as data, models, software or a whole system.
-- # Class: AimsSupplierRelationship_aims_supplier_requirements
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_supplier_requirements Description: What the organization asks of the supplier.
-- # Class: AimsSupplierRelationship_aims_supplier_corrective_actions
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_supplier_corrective_actions Description: What the supplier was asked to put right.
-- # Class: AimsSupplierRelationship_aims_ai_systems
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsSupplierRelationship_aims_life_cycle_stages
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsSupplierRelationship_aims_relationship_party_roles
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_party_roles Description: The parts the other party plays towards the system.
-- # Class: AimsSupplierRelationship_aims_relationship_responsibilities
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_responsibilities Description: The duties each side carries.
-- # Class: AimsSupplierRelationship_aims_relationship_documentation
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_documentation Description: The documents one side owes the other about the system.
-- # Class: AimsSupplierRelationship_aims_relationship_assurance_evidence
--     * Slot: AimsSupplierRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_assurance_evidence Description: What assures the organization that the party meets its duties.
-- # Class: AimsCustomerRelationship_aims_customer_expectations
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_customer_expectations Description: What the customer expects and wants.
-- # Class: AimsCustomerRelationship_aims_customer_communicated_limits
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_customer_communicated_limits Description: What the customer was told the system cannot do, or where it stops being valid.
-- # Class: AimsCustomerRelationship_aims_ai_systems
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsCustomerRelationship_aims_life_cycle_stages
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_life_cycle_stages Description: The stages of an AI system's life the record applies to.
-- # Class: AimsCustomerRelationship_aims_relationship_party_roles
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_party_roles Description: The parts the other party plays towards the system.
-- # Class: AimsCustomerRelationship_aims_relationship_responsibilities
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_responsibilities Description: The duties each side carries.
-- # Class: AimsCustomerRelationship_aims_relationship_documentation
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_documentation Description: The documents one side owes the other about the system.
-- # Class: AimsCustomerRelationship_aims_relationship_assurance_evidence
--     * Slot: AimsCustomerRelationship_aims_id Description: Autocreated FK slot
--     * Slot: aims_relationship_assurance_evidence Description: What assures the organization that the party meets its duties.
-- # Class: AimsSystemEvent_aims_ai_systems
--     * Slot: AimsSystemEvent_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsIncident_aims_incident_threats
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_threats Description: The threats peculiar to AI that the incident involved.
-- # Class: AimsIncident_aims_incident_impact_areas
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_impact_areas Description: The areas of impact the incident touched.
-- # Class: AimsIncident_aims_incident_response_actions
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_response_actions Description: What was done in response.
-- # Class: AimsIncident_aims_incident_recovery_actions
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_recovery_actions Description: What was done to restore normal operation.
-- # Class: AimsIncident_aims_incident_lessons_learned
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_lessons_learned Description: What the organization learned from it.
-- # Class: AimsIncident_aims_incident_notifications
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_notifications Description: Whom the organization told, and when.
-- # Class: AimsIncident_aims_incident_corrective_actions
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_incident_corrective_actions_aims_id Description: The corrective actions the incident led to.
-- # Class: AimsIncident_aims_ai_systems
--     * Slot: AimsIncident_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsConcernReportingProcess_aims_concern_process_confidentiality
--     * Slot: AimsConcernReportingProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_concern_process_confidentiality Description: The ways a person can stay unnamed or keep a report private.
-- # Class: AimsConcernReportingProcess_aims_document_distribution
--     * Slot: AimsConcernReportingProcess_aims_id Description: Autocreated FK slot
--     * Slot: aims_document_distribution Description: Who gets the document, how they reach it and what they may do with it.
-- # Class: AimsConcernReport_aims_ai_systems
--     * Slot: AimsConcernReport_aims_id Description: Autocreated FK slot
--     * Slot: aims_ai_systems_aims_id Description: The AI systems the record concerns.
-- # Class: AimsConcernReport_aims_concern_incidents
--     * Slot: AimsConcernReport_aims_id Description: Autocreated FK slot
--     * Slot: aims_concern_incidents_aims_id Description: The incidents it relates to.
-- # Class: AimsConcernReport_aims_concern_nonconformities
--     * Slot: AimsConcernReport_aims_id Description: Autocreated FK slot
--     * Slot: aims_concern_nonconformities_aims_id Description: The nonconformities it relates to.

CREATE TABLE "AimsRecordMixin" (
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsRecordMixin_aims_id" ON "AimsRecordMixin" (aims_id);

CREATE TABLE "AimsDocumentControlMixin" (
	id INTEGER NOT NULL,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AimsDocumentControlMixin_id" ON "AimsDocumentControlMixin" (id);

CREATE TABLE "AimsManagementSystem" (
	aims_top_management TEXT,
	aims_governing_body TEXT,
	aims_scope TEXT,
	aims_processes TEXT,
	aims_certification_status TEXT,
	aims_certification_body TEXT,
	aims_certification_date DATE,
	aims_recertification_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_organization_aims_id TEXT,
	aims_policy_aims_id TEXT,
	aims_risk_assessment_process_aims_id TEXT,
	aims_risk_treatment_process_aims_id TEXT,
	aims_impact_assessment_process_aims_id TEXT,
	aims_statement_of_applicability_aims_id TEXT,
	aims_awareness_programme_aims_id TEXT,
	aims_communication_plan_aims_id TEXT,
	aims_monitoring_programme_aims_id TEXT,
	aims_concern_reporting_process_aims_id TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_organization_aims_id) REFERENCES "AimsOrganization" (aims_id),
	FOREIGN KEY(aims_policy_aims_id) REFERENCES "AimsPolicy" (aims_id),
	FOREIGN KEY(aims_risk_assessment_process_aims_id) REFERENCES "AimsRiskAssessmentProcess" (aims_id),
	FOREIGN KEY(aims_risk_treatment_process_aims_id) REFERENCES "AimsRiskTreatmentProcess" (aims_id),
	FOREIGN KEY(aims_impact_assessment_process_aims_id) REFERENCES "AimsImpactAssessmentProcess" (aims_id),
	FOREIGN KEY(aims_statement_of_applicability_aims_id) REFERENCES "AimsStatementOfApplicability" (aims_id),
	FOREIGN KEY(aims_awareness_programme_aims_id) REFERENCES "AimsAwarenessProgramme" (aims_id),
	FOREIGN KEY(aims_communication_plan_aims_id) REFERENCES "AimsCommunicationPlan" (aims_id),
	FOREIGN KEY(aims_monitoring_programme_aims_id) REFERENCES "AimsMonitoringProgramme" (aims_id),
	FOREIGN KEY(aims_concern_reporting_process_aims_id) REFERENCES "AimsConcernReportingProcess" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_id" ON "AimsManagementSystem" (aims_id);

CREATE TABLE "AimsOrganization" (
	aims_organization_legal_name TEXT,
	aims_organization_kind TEXT,
	aims_organization_size TEXT,
	aims_organization_employee_count INTEGER,
	aims_organization_parent TEXT,
	aims_organization_climate_change_relevant BOOLEAN,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_id" ON "AimsOrganization" (aims_id);

CREATE TABLE "AimsPolicy" (
	aims_policy_statement TEXT,
	aims_policy_objectives_framework TEXT,
	aims_policy_exceptions_process TEXT,
	aims_policy_communication_date DATE,
	aims_policy_availability TEXT,
	aims_policy_review_role TEXT,
	aims_policy_review_interval TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_policy_review_role) REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_id" ON "AimsPolicy" (aims_id);

CREATE TABLE "AimsRole" (
	aims_role_category TEXT,
	aims_role_ensures_conformity BOOLEAN,
	aims_role_reports_performance BOOLEAN,
	aims_role_accountability TEXT,
	aims_role_delegation TEXT,
	aims_role_reports_to TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_role_reports_to) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsRole_aims_id" ON "AimsRole" (aims_id);

CREATE TABLE "AimsRiskAssessmentProcess" (
	aims_risk_policy_alignment TEXT,
	aims_risk_comparability TEXT,
	aims_risk_method TEXT,
	aims_risk_likelihood_scale TEXT,
	aims_risk_consequence_scale TEXT,
	aims_risk_matrix TEXT,
	aims_risk_prioritization TEXT,
	aims_risk_assessment_interval TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_id" ON "AimsRiskAssessmentProcess" (aims_id);

CREATE TABLE "AimsRiskTreatmentProcess" (
	aims_treatment_options_guidance TEXT,
	aims_treatment_control_selection TEXT,
	aims_treatment_annex_a_comparison TEXT,
	aims_treatment_additional_controls TEXT,
	aims_treatment_annex_b_use TEXT,
	aims_treatment_soa_template TEXT,
	aims_treatment_approval_workflow TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentProcess_aims_id" ON "AimsRiskTreatmentProcess" (aims_id);

CREATE TABLE "AimsImpactAssessmentProcess" (
	aims_impact_process_interval TEXT,
	aims_impact_process_assessors TEXT,
	aims_impact_process_use TEXT,
	aims_impact_process_retention TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_id" ON "AimsImpactAssessmentProcess" (aims_id);

CREATE TABLE "AimsStatementOfApplicability" (
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsStatementOfApplicability_aims_id" ON "AimsStatementOfApplicability" (aims_id);

CREATE TABLE "AimsExcludedControl" (
	id INTEGER NOT NULL,
	aims_entry_annex_a_control VARCHAR(7) NOT NULL,
	aims_entry_type TEXT,
	aims_entry_justification TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AimsExcludedControl_id" ON "AimsExcludedControl" (id);

CREATE TABLE "AimsComponentResource" (
	aims_component_kind TEXT,
	aims_component_integration TEXT,
	aims_resource_type TEXT NOT NULL,
	aims_resource_provider VARCHAR(12),
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsComponentResource_aims_id" ON "AimsComponentResource" (aims_id);

CREATE TABLE "AimsDataResource" (
	aims_data_intended_use TEXT,
	aims_data_quantity TEXT,
	aims_data_prior_handling TEXT,
	aims_data_provenance TEXT,
	aims_data_provenance_verification TEXT,
	aims_data_representativeness TEXT,
	aims_data_labelling_process TEXT,
	aims_data_preparation_criteria TEXT,
	aims_data_last_updated DATE,
	aims_data_retention TEXT,
	aims_data_classification TEXT,
	aims_resource_type TEXT NOT NULL,
	aims_resource_provider VARCHAR(12),
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_id" ON "AimsDataResource" (aims_id);

CREATE TABLE "AimsToolingResource" (
	aims_tool_category TEXT,
	aims_tool_version TEXT,
	aims_tool_vendor TEXT,
	aims_tool_licence TEXT,
	aims_tool_purpose TEXT,
	aims_resource_type TEXT NOT NULL,
	aims_resource_provider VARCHAR(12),
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsToolingResource_aims_id" ON "AimsToolingResource" (aims_id);

CREATE TABLE "AimsComputingResource" (
	aims_computing_requirements TEXT,
	aims_computing_location TEXT,
	aims_computing_processing TEXT,
	aims_computing_hardware_impact TEXT,
	aims_resource_type TEXT NOT NULL,
	aims_resource_provider VARCHAR(12),
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsComputingResource_aims_id" ON "AimsComputingResource" (aims_id);

CREATE TABLE "AimsAwarenessProgramme" (
	aims_awareness_audience TEXT,
	aims_awareness_frequency TEXT,
	aims_awareness_completion_tracking TEXT,
	aims_awareness_effectiveness TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsAwarenessProgramme_aims_id" ON "AimsAwarenessProgramme" (aims_id);

CREATE TABLE "AimsCommunicationPlan" (
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsCommunicationPlan_aims_id" ON "AimsCommunicationPlan" (aims_id);

CREATE TABLE "AimsMonitoringProgramme" (
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsMonitoringProgramme_aims_id" ON "AimsMonitoringProgramme" (aims_id);

CREATE TABLE "AimsSupplierRelationship" (
	aims_supplier_risk VARCHAR(8),
	aims_supplier_monitoring TEXT,
	aims_supplier_integration TEXT,
	aims_relationship_type TEXT,
	aims_relationship_party TEXT,
	aims_relationship_contract TEXT,
	aims_relationship_pii_role VARCHAR(20),
	aims_relationship_review_frequency TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship" (aims_id);

CREATE TABLE "AimsCustomerRelationship" (
	aims_customer_agreement TEXT,
	aims_customer_responsibility_split TEXT,
	aims_relationship_type TEXT,
	aims_relationship_party TEXT,
	aims_relationship_contract TEXT,
	aims_relationship_pii_role VARCHAR(20),
	aims_relationship_review_frequency TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship" (aims_id);

CREATE TABLE "AimsIncident" (
	aims_incident_category VARCHAR(20),
	aims_incident_severity VARCHAR(8),
	aims_incident_detection_method TEXT,
	aims_incident_root_cause TEXT,
	aims_incident_notification_required BOOLEAN,
	aims_incident_closed_at DATETIME,
	aims_event_type TEXT,
	aims_event_occurred_at DATETIME,
	aims_event_reporter TEXT,
	aims_event_source TEXT,
	aims_event_adverse_impact TEXT,
	aims_event_assessment TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_id" ON "AimsIncident" (aims_id);

CREATE TABLE "AimsConcernReportingProcess" (
	aims_concern_process_audience TEXT,
	aims_concern_process_investigators TEXT,
	aims_concern_process_escalation TEXT,
	aims_concern_process_reprisal_protection TEXT,
	aims_concern_process_response_time TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	PRIMARY KEY (aims_id)
);
CREATE INDEX "ix_AimsConcernReportingProcess_aims_id" ON "AimsConcernReportingProcess" (aims_id);

CREATE TABLE "AimsInterestedParty" (
	aims_party_category TEXT,
	aims_party_relationship TEXT,
	aims_party_communication_needs TEXT,
	aims_party_contact TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsInterestedParty_aims_id" ON "AimsInterestedParty" (aims_id);

CREATE TABLE "AimsTopicSpecificPolicy" (
	aims_topic_policy_topic TEXT,
	aims_topic_policy_parent TEXT,
	aims_topic_policy_audience TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_topic_policy_parent) REFERENCES "AimsPolicy" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_id" ON "AimsTopicSpecificPolicy" (aims_id);

CREATE TABLE "AimsObjective" (
	aims_responsible_role TEXT,
	aims_objective_purpose VARCHAR(23),
	aims_objective_statement TEXT,
	aims_objective_target TEXT,
	aims_objective_current_value TEXT,
	aims_objective_metric TEXT,
	aims_objective_measurement_method TEXT,
	aims_objective_measurement_frequency TEXT,
	aims_objective_target_date DATE,
	aims_objective_achievement TEXT,
	aims_objective_action_plan TEXT,
	aims_objective_resources TEXT,
	aims_objective_evaluation TEXT,
	aims_objective_communication TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsObjective_aims_id" ON "AimsObjective" (aims_id);

CREATE TABLE "AimsPlannedAction" (
	aims_responsible_role TEXT,
	aims_planned_action_integration TEXT,
	aims_planned_action_effectiveness TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsPlannedAction_aims_id" ON "AimsPlannedAction" (aims_id);

CREATE TABLE "AimsRiskAssessment" (
	aims_assessment_scope TEXT,
	aims_assessment_date DATE,
	aims_assessment_assessor TEXT,
	aims_assessment_method_used TEXT,
	aims_assessment_summary TEXT,
	aims_assessment_next_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessment_aims_id" ON "AimsRiskAssessment" (aims_id);

CREATE TABLE "AimsRisk" (
	aims_risk_source TEXT,
	aims_risk_consequences_for_organization TEXT,
	aims_risk_consequences_for_individuals TEXT,
	aims_risk_consequences_for_societies TEXT,
	aims_risk_owner TEXT,
	aims_risk_likelihood VARCHAR(14),
	aims_risk_consequence VARCHAR(10),
	aims_risk_inherent_level VARCHAR(8),
	aims_risk_residual_level VARCHAR(8),
	aims_risk_acceptable BOOLEAN,
	aims_risk_treatment_option VARCHAR(6),
	aims_risk_treatment_priority TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsRisk_aims_id" ON "AimsRisk" (aims_id);

CREATE TABLE "AimsRiskTreatmentPlan" (
	aims_implementation_state VARCHAR(11),
	aims_plan_scope TEXT,
	aims_plan_resources TEXT,
	aims_plan_timeline TEXT,
	aims_plan_approver TEXT,
	aims_plan_residual_risk_acceptance TEXT,
	aims_plan_effectiveness TEXT,
	aims_plan_revalidation TEXT,
	aims_plan_completion_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_id" ON "AimsRiskTreatmentPlan" (aims_id);

CREATE TABLE "AimsImpactAssessment" (
	aims_impact_scope TEXT,
	aims_impact_discipline TEXT,
	aims_impact_date DATE,
	aims_impact_assessor TEXT,
	aims_impact_intended_use TEXT,
	aims_impact_foreseeable_misuse TEXT,
	aims_impact_technical_context TEXT,
	aims_impact_societal_context TEXT,
	aims_impact_system_complexity TEXT,
	aims_impact_human_role TEXT,
	aims_impact_workforce TEXT,
	aims_impact_next_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment" (aims_id);

CREATE TABLE "AimsApplicabilityEntry" (
	id INTEGER NOT NULL,
	aims_entry_annex_a_control VARCHAR(7),
	aims_entry_type TEXT,
	aims_entry_justification TEXT NOT NULL,
	"AimsStatementOfApplicability_aims_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AimsStatementOfApplicability_aims_id") REFERENCES "AimsStatementOfApplicability" (aims_id)
);
CREATE INDEX "ix_AimsApplicabilityEntry_id" ON "AimsApplicabilityEntry" (id);

CREATE TABLE "AimsControl" (
	aims_implementation_state VARCHAR(11),
	aims_control_area VARCHAR(23),
	aims_control_text TEXT,
	aims_control_guidance TEXT,
	aims_control_owner TEXT,
	aims_control_implementation_date DATE,
	aims_control_effectiveness TEXT,
	aims_control_last_tested DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_id" ON "AimsControl" (aims_id);

CREATE TABLE "AimsSystemResource" (
	aims_resource_type TEXT NOT NULL,
	aims_resource_provider VARCHAR(12),
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsSystemResource_aims_id" ON "AimsSystemResource" (aims_id);

CREATE TABLE "AimsHumanResource" (
	aims_human_role TEXT,
	aims_human_diversity TEXT,
	aims_resource_type TEXT NOT NULL,
	aims_resource_provider VARCHAR(12),
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_human_role) REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsHumanResource_aims_id" ON "AimsHumanResource" (aims_id);

CREATE TABLE "AimsDevelopmentProcess" (
	aims_development_life_cycle_model TEXT,
	aims_development_testing TEXT,
	aims_development_human_oversight TEXT,
	aims_development_training_data_rules TEXT,
	aims_development_expertise TEXT,
	aims_development_change_control TEXT,
	aims_development_usability TEXT,
	aims_development_party_engagement TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_id" ON "AimsDevelopmentProcess" (aims_id);

CREATE TABLE "AimsResponsibleUseProcess" (
	aims_use_costs TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_id" ON "AimsResponsibleUseProcess" (aims_id);

CREATE TABLE "AimsTechnicalDocumentation" (
	aims_technical_doc_form TEXT,
	aims_technical_doc_failure_plan TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_id" ON "AimsTechnicalDocumentation" (aims_id);

CREATE TABLE "AimsUserInformation" (
	aims_user_information_validated BOOLEAN,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsUserInformation_aims_id" ON "AimsUserInformation" (aims_id);

CREATE TABLE "AimsIncidentCommunicationPlan" (
	aims_incident_plan_timeline TEXT,
	aims_incident_plan_integration TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_id" ON "AimsIncidentCommunicationPlan" (aims_id);

CREATE TABLE "AimsReportingObligation" (
	aims_obligation_basis TEXT,
	aims_obligation_jurisdiction TEXT,
	aims_obligation_timeframe TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsReportingObligation_aims_id" ON "AimsReportingObligation" (aims_id);

CREATE TABLE "AimsResource" (
	aims_support_category TEXT,
	aims_support_quantity TEXT,
	aims_support_allocation_date DATE,
	aims_support_allocated_to TEXT,
	aims_support_cost TEXT,
	aims_support_availability TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsResource_aims_id" ON "AimsResource" (aims_id);

CREATE TABLE "AimsCompetenceRecord" (
	aims_competence_person TEXT,
	aims_competence_role TEXT,
	aims_competence_assessment_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_competence_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord" (aims_id);

CREATE TABLE "AimsCommunication" (
	id INTEGER NOT NULL,
	aims_responsible_role TEXT,
	aims_communication_subject TEXT NOT NULL,
	aims_communication_purpose TEXT,
	aims_communication_audience TEXT,
	aims_communication_external BOOLEAN,
	aims_communication_timing TEXT,
	aims_communication_method TEXT,
	aims_communication_records_required BOOLEAN,
	"AimsCommunicationPlan_aims_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsCommunicationPlan_aims_id") REFERENCES "AimsCommunicationPlan" (aims_id)
);
CREATE INDEX "ix_AimsCommunication_id" ON "AimsCommunication" (id);

CREATE TABLE "AimsDocumentedInformation" (
	aims_document_kind VARCHAR(9) NOT NULL,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsDocumentedInformation_aims_id" ON "AimsDocumentedInformation" (aims_id);

CREATE TABLE "AimsOperationalProcedure" (
	aims_procedure_scope TEXT,
	aims_procedure_criteria TEXT,
	aims_procedure_change_control TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsOperationalProcedure_aims_id" ON "AimsOperationalProcedure" (aims_id);

CREATE TABLE "AimsMonitoringItem" (
	id INTEGER NOT NULL,
	aims_responsible_role TEXT,
	aims_monitoring_metric TEXT NOT NULL,
	aims_monitoring_description TEXT,
	aims_monitoring_method TEXT,
	aims_monitoring_frequency TEXT,
	aims_monitoring_analysis_frequency TEXT,
	aims_monitoring_analyst TEXT,
	aims_monitoring_target TEXT,
	aims_monitoring_alert_threshold TEXT,
	aims_monitoring_current_value TEXT,
	aims_monitoring_trend TEXT,
	"AimsMonitoringProgramme_aims_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsMonitoringProgramme_aims_id") REFERENCES "AimsMonitoringProgramme" (aims_id)
);
CREATE INDEX "ix_AimsMonitoringItem_id" ON "AimsMonitoringItem" (id);

CREATE TABLE "AimsAuditProgramme" (
	aims_programme_period TEXT,
	aims_programme_frequency_rationale TEXT,
	aims_programme_methods TEXT,
	aims_programme_resources TEXT,
	aims_programme_auditor_selection TEXT,
	aims_programme_status TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsAuditProgramme_aims_id" ON "AimsAuditProgramme" (aims_id);

CREATE TABLE "AimsManagementReview" (
	aims_review_held_on DATE NOT NULL,
	aims_review_previous_actions TEXT,
	aims_review_context_changes TEXT,
	aims_review_interested_party_changes TEXT,
	aims_review_nonconformity_trends TEXT,
	aims_review_monitoring_trends TEXT,
	aims_review_audit_trends TEXT,
	aims_review_next_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_id" ON "AimsManagementReview" (aims_id);

CREATE TABLE "AimsNonconformity" (
	aims_nonconformity_source TEXT,
	aims_nonconformity_detected_on DATE,
	aims_nonconformity_detected_by TEXT,
	aims_nonconformity_requirement TEXT,
	aims_nonconformity_consequences TEXT,
	aims_nonconformity_root_cause TEXT,
	aims_nonconformity_similar_check TEXT,
	aims_nonconformity_status TEXT,
	aims_nonconformity_closure_date DATE,
	aims_nonconformity_closure_evidence TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsNonconformity_aims_id" ON "AimsNonconformity" (aims_id);

CREATE TABLE "AimsCorrectiveAction" (
	aims_responsible_role TEXT,
	aims_action_root_cause TEXT,
	aims_action_target_date DATE,
	aims_action_completion_date DATE,
	aims_action_resources TEXT,
	aims_action_effectiveness_criteria TEXT,
	aims_action_effectiveness_review_date DATE,
	aims_action_effective BOOLEAN,
	aims_action_system_changes TEXT,
	aims_action_status TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsCorrectiveAction_aims_id" ON "AimsCorrectiveAction" (aims_id);

CREATE TABLE "AimsImprovementOpportunity" (
	aims_responsible_role TEXT,
	aims_improvement_source TEXT,
	aims_improvement_identified_on DATE,
	aims_improvement_identified_by TEXT,
	aims_improvement_benefit TEXT,
	aims_improvement_priority TEXT,
	aims_improvement_plan TEXT,
	aims_improvement_target_date DATE,
	aims_improvement_completion_date DATE,
	aims_improvement_outcome TEXT,
	aims_improvement_status TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsImprovementOpportunity_aims_id" ON "AimsImprovementOpportunity" (aims_id);

CREATE TABLE "AimsThirdPartyRelationship" (
	aims_relationship_type TEXT,
	aims_relationship_party TEXT,
	aims_relationship_contract TEXT,
	aims_relationship_pii_role VARCHAR(20),
	aims_relationship_review_frequency TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship" (aims_id);

CREATE TABLE "AimsSystemEvent" (
	aims_event_type TEXT,
	aims_event_occurred_at DATETIME,
	aims_event_reporter TEXT,
	aims_event_source TEXT,
	aims_event_adverse_impact TEXT,
	aims_event_assessment TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsSystemEvent_aims_id" ON "AimsSystemEvent" (aims_id);

CREATE TABLE "AimsConcernReport" (
	aims_concern_reported_on DATE,
	aims_concern_reporter TEXT,
	aims_concern_anonymous BOOLEAN,
	aims_concern_channel TEXT,
	aims_concern_life_cycle_stage VARCHAR(27),
	aims_concern_severity VARCHAR(8),
	aims_concern_investigator TEXT,
	aims_concern_investigation_status TEXT,
	aims_concern_findings TEXT,
	aims_concern_escalation TEXT,
	aims_concern_response_due DATE,
	aims_concern_responded_on DATE,
	aims_concern_resolution TEXT,
	aims_concern_reprisal_protection TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsConcernReport_aims_id" ON "AimsConcernReport" (aims_id);

CREATE TABLE "AimsDocumentControlMixin_aims_document_distribution" (
	"AimsDocumentControlMixin_id" INTEGER,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsDocumentControlMixin_id", aims_document_distribution),
	FOREIGN KEY("AimsDocumentControlMixin_id") REFERENCES "AimsDocumentControlMixin" (id)
);
CREATE INDEX "ix_AimsDocumentControlMixin_aims_document_distribution_aims_document_distribution" ON "AimsDocumentControlMixin_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsDocumentControlMixin_aims_document_distribution_AimsDocumentControlMixin_id" ON "AimsDocumentControlMixin_aims_document_distribution" ("AimsDocumentControlMixin_id");

CREATE TABLE "AimsManagementSystem_aims_leadership_evidence" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_leadership_evidence TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_leadership_evidence),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_leadership_evidence_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_leadership_evidence" ("AimsManagementSystem_aims_id");
CREATE INDEX "ix_AimsManagementSystem_aims_leadership_evidence_aims_leadership_evidence" ON "AimsManagementSystem_aims_leadership_evidence" (aims_leadership_evidence);

CREATE TABLE "AimsManagementSystem_aims_scope_boundaries" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_scope_boundaries TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_scope_boundaries),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_scope_boundaries_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_scope_boundaries" ("AimsManagementSystem_aims_id");
CREATE INDEX "ix_AimsManagementSystem_aims_scope_boundaries_aims_scope_boundaries" ON "AimsManagementSystem_aims_scope_boundaries" (aims_scope_boundaries);

CREATE TABLE "AimsManagementSystem_aims_scope_applicability" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_scope_applicability TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_scope_applicability),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_scope_applicability_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_scope_applicability" ("AimsManagementSystem_aims_id");
CREATE INDEX "ix_AimsManagementSystem_aims_scope_applicability_aims_scope_applicability" ON "AimsManagementSystem_aims_scope_applicability" (aims_scope_applicability);

CREATE TABLE "AimsManagementSystem_aims_internal_issues" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_internal_issues TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_internal_issues),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_internal_issues_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_internal_issues" ("AimsManagementSystem_aims_id");
CREATE INDEX "ix_AimsManagementSystem_aims_internal_issues_aims_internal_issues" ON "AimsManagementSystem_aims_internal_issues" (aims_internal_issues);

CREATE TABLE "AimsManagementSystem_aims_external_issues" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_external_issues TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_external_issues),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_external_issues_aims_external_issues" ON "AimsManagementSystem_aims_external_issues" (aims_external_issues);
CREATE INDEX "ix_AimsManagementSystem_aims_external_issues_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_external_issues" ("AimsManagementSystem_aims_id");

CREATE TABLE "AimsManagementSystem_aims_planned_changes" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_planned_changes TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_planned_changes),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_planned_changes_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_planned_changes" ("AimsManagementSystem_aims_id");
CREATE INDEX "ix_AimsManagementSystem_aims_planned_changes_aims_planned_changes" ON "AimsManagementSystem_aims_planned_changes" (aims_planned_changes);

CREATE TABLE "AimsManagementSystem_aims_external_services" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_external_services TEXT,
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_external_services),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_external_services_aims_external_services" ON "AimsManagementSystem_aims_external_services" (aims_external_services);
CREATE INDEX "ix_AimsManagementSystem_aims_external_services_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_external_services" ("AimsManagementSystem_aims_id");

CREATE TABLE "AimsManagementSystem_aims_integrated_standards" (
	"AimsManagementSystem_aims_id" TEXT,
	aims_integrated_standards VARCHAR(13),
	PRIMARY KEY ("AimsManagementSystem_aims_id", aims_integrated_standards),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsManagementSystem_aims_integrated_standards_AimsManagementSystem_aims_id" ON "AimsManagementSystem_aims_integrated_standards" ("AimsManagementSystem_aims_id");
CREATE INDEX "ix_AimsManagementSystem_aims_integrated_standards_aims_integrated_standards" ON "AimsManagementSystem_aims_integrated_standards" (aims_integrated_standards);

CREATE TABLE "AimsOrganization_aims_organization_trading_names" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_trading_names TEXT,
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_trading_names),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_trading_names_aims_organization_trading_names" ON "AimsOrganization_aims_organization_trading_names" (aims_organization_trading_names);
CREATE INDEX "ix_AimsOrganization_aims_organization_trading_names_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_trading_names" ("AimsOrganization_aims_id");

CREATE TABLE "AimsOrganization_aims_organization_sectors" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_sectors TEXT,
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_sectors),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_sectors_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_sectors" ("AimsOrganization_aims_id");
CREATE INDEX "ix_AimsOrganization_aims_organization_sectors_aims_organization_sectors" ON "AimsOrganization_aims_organization_sectors" (aims_organization_sectors);

CREATE TABLE "AimsOrganization_aims_organization_locations" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_locations TEXT,
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_locations),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_locations_aims_organization_locations" ON "AimsOrganization_aims_organization_locations" (aims_organization_locations);
CREATE INDEX "ix_AimsOrganization_aims_organization_locations_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_locations" ("AimsOrganization_aims_id");

CREATE TABLE "AimsOrganization_aims_organization_jurisdictions" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_jurisdictions TEXT,
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_jurisdictions),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_jurisdictions_aims_organization_jurisdictions" ON "AimsOrganization_aims_organization_jurisdictions" (aims_organization_jurisdictions);
CREATE INDEX "ix_AimsOrganization_aims_organization_jurisdictions_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_jurisdictions" ("AimsOrganization_aims_id");

CREATE TABLE "AimsOrganization_aims_organization_subsidiaries" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_subsidiaries TEXT,
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_subsidiaries),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_subsidiaries_aims_organization_subsidiaries" ON "AimsOrganization_aims_organization_subsidiaries" (aims_organization_subsidiaries);
CREATE INDEX "ix_AimsOrganization_aims_organization_subsidiaries_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_subsidiaries" ("AimsOrganization_aims_id");

CREATE TABLE "AimsOrganization_aims_organization_ai_roles" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_ai_roles VARCHAR(30),
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_ai_roles),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_ai_roles_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_ai_roles" ("AimsOrganization_aims_id");
CREATE INDEX "ix_AimsOrganization_aims_organization_ai_roles_aims_organization_ai_roles" ON "AimsOrganization_aims_organization_ai_roles" (aims_organization_ai_roles);

CREATE TABLE "AimsOrganization_aims_organization_pii_roles" (
	"AimsOrganization_aims_id" TEXT,
	aims_organization_pii_roles VARCHAR(20),
	PRIMARY KEY ("AimsOrganization_aims_id", aims_organization_pii_roles),
	FOREIGN KEY("AimsOrganization_aims_id") REFERENCES "AimsOrganization" (aims_id)
);
CREATE INDEX "ix_AimsOrganization_aims_organization_pii_roles_aims_organization_pii_roles" ON "AimsOrganization_aims_organization_pii_roles" (aims_organization_pii_roles);
CREATE INDEX "ix_AimsOrganization_aims_organization_pii_roles_AimsOrganization_aims_id" ON "AimsOrganization_aims_organization_pii_roles" ("AimsOrganization_aims_id");

CREATE TABLE "AimsPolicy_aims_cited_clauses" (
	"AimsPolicy_aims_id" TEXT,
	aims_cited_clauses VARCHAR(12),
	PRIMARY KEY ("AimsPolicy_aims_id", aims_cited_clauses),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_cited_clauses_aims_cited_clauses" ON "AimsPolicy_aims_cited_clauses" (aims_cited_clauses);
CREATE INDEX "ix_AimsPolicy_aims_cited_clauses_AimsPolicy_aims_id" ON "AimsPolicy_aims_cited_clauses" ("AimsPolicy_aims_id");

CREATE TABLE "AimsPolicy_aims_cited_annex_a_controls" (
	"AimsPolicy_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsPolicy_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsPolicy_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);
CREATE INDEX "ix_AimsPolicy_aims_cited_annex_a_controls_AimsPolicy_aims_id" ON "AimsPolicy_aims_cited_annex_a_controls" ("AimsPolicy_aims_id");

CREATE TABLE "AimsPolicy_aims_policy_commitments" (
	"AimsPolicy_aims_id" TEXT,
	aims_policy_commitments TEXT,
	PRIMARY KEY ("AimsPolicy_aims_id", aims_policy_commitments),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_policy_commitments_aims_policy_commitments" ON "AimsPolicy_aims_policy_commitments" (aims_policy_commitments);
CREATE INDEX "ix_AimsPolicy_aims_policy_commitments_AimsPolicy_aims_id" ON "AimsPolicy_aims_policy_commitments" ("AimsPolicy_aims_id");

CREATE TABLE "AimsPolicy_aims_policy_principles" (
	"AimsPolicy_aims_id" TEXT,
	aims_policy_principles TEXT,
	PRIMARY KEY ("AimsPolicy_aims_id", aims_policy_principles),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_policy_principles_AimsPolicy_aims_id" ON "AimsPolicy_aims_policy_principles" ("AimsPolicy_aims_id");
CREATE INDEX "ix_AimsPolicy_aims_policy_principles_aims_policy_principles" ON "AimsPolicy_aims_policy_principles" (aims_policy_principles);

CREATE TABLE "AimsPolicy_aims_policy_influences" (
	"AimsPolicy_aims_id" TEXT,
	aims_policy_influences TEXT,
	PRIMARY KEY ("AimsPolicy_aims_id", aims_policy_influences),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_policy_influences_AimsPolicy_aims_id" ON "AimsPolicy_aims_policy_influences" ("AimsPolicy_aims_id");
CREATE INDEX "ix_AimsPolicy_aims_policy_influences_aims_policy_influences" ON "AimsPolicy_aims_policy_influences" (aims_policy_influences);

CREATE TABLE "AimsPolicy_aims_policy_related_policies" (
	"AimsPolicy_aims_id" TEXT,
	aims_policy_related_policies TEXT,
	PRIMARY KEY ("AimsPolicy_aims_id", aims_policy_related_policies),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_policy_related_policies_aims_policy_related_policies" ON "AimsPolicy_aims_policy_related_policies" (aims_policy_related_policies);
CREATE INDEX "ix_AimsPolicy_aims_policy_related_policies_AimsPolicy_aims_id" ON "AimsPolicy_aims_policy_related_policies" ("AimsPolicy_aims_id");

CREATE TABLE "AimsPolicy_aims_document_distribution" (
	"AimsPolicy_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsPolicy_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsPolicy_aims_id") REFERENCES "AimsPolicy" (aims_id)
);
CREATE INDEX "ix_AimsPolicy_aims_document_distribution_AimsPolicy_aims_id" ON "AimsPolicy_aims_document_distribution" ("AimsPolicy_aims_id");
CREATE INDEX "ix_AimsPolicy_aims_document_distribution_aims_document_distribution" ON "AimsPolicy_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsRole_aims_role_areas" (
	"AimsRole_aims_id" TEXT,
	aims_role_areas TEXT,
	PRIMARY KEY ("AimsRole_aims_id", aims_role_areas),
	FOREIGN KEY("AimsRole_aims_id") REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsRole_aims_role_areas_AimsRole_aims_id" ON "AimsRole_aims_role_areas" ("AimsRole_aims_id");
CREATE INDEX "ix_AimsRole_aims_role_areas_aims_role_areas" ON "AimsRole_aims_role_areas" (aims_role_areas);

CREATE TABLE "AimsRole_aims_role_responsibilities" (
	"AimsRole_aims_id" TEXT,
	aims_role_responsibilities TEXT,
	PRIMARY KEY ("AimsRole_aims_id", aims_role_responsibilities),
	FOREIGN KEY("AimsRole_aims_id") REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsRole_aims_role_responsibilities_aims_role_responsibilities" ON "AimsRole_aims_role_responsibilities" (aims_role_responsibilities);
CREATE INDEX "ix_AimsRole_aims_role_responsibilities_AimsRole_aims_id" ON "AimsRole_aims_role_responsibilities" ("AimsRole_aims_id");

CREATE TABLE "AimsRole_aims_role_authorities" (
	"AimsRole_aims_id" TEXT,
	aims_role_authorities TEXT,
	PRIMARY KEY ("AimsRole_aims_id", aims_role_authorities),
	FOREIGN KEY("AimsRole_aims_id") REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsRole_aims_role_authorities_aims_role_authorities" ON "AimsRole_aims_role_authorities" (aims_role_authorities);
CREATE INDEX "ix_AimsRole_aims_role_authorities_AimsRole_aims_id" ON "AimsRole_aims_role_authorities" ("AimsRole_aims_id");

CREATE TABLE "AimsRole_aims_role_holders" (
	"AimsRole_aims_id" TEXT,
	aims_role_holders TEXT,
	PRIMARY KEY ("AimsRole_aims_id", aims_role_holders),
	FOREIGN KEY("AimsRole_aims_id") REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsRole_aims_role_holders_AimsRole_aims_id" ON "AimsRole_aims_role_holders" ("AimsRole_aims_id");
CREATE INDEX "ix_AimsRole_aims_role_holders_aims_role_holders" ON "AimsRole_aims_role_holders" (aims_role_holders);

CREATE TABLE "AimsRiskAssessmentProcess_aims_risk_criteria" (
	"AimsRiskAssessmentProcess_aims_id" TEXT,
	aims_risk_criteria TEXT,
	PRIMARY KEY ("AimsRiskAssessmentProcess_aims_id", aims_risk_criteria),
	FOREIGN KEY("AimsRiskAssessmentProcess_aims_id") REFERENCES "AimsRiskAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_risk_criteria_AimsRiskAssessmentProcess_aims_id" ON "AimsRiskAssessmentProcess_aims_risk_criteria" ("AimsRiskAssessmentProcess_aims_id");
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_risk_criteria_aims_risk_criteria" ON "AimsRiskAssessmentProcess_aims_risk_criteria" (aims_risk_criteria);

CREATE TABLE "AimsRiskAssessmentProcess_aims_risk_assessment_triggers" (
	"AimsRiskAssessmentProcess_aims_id" TEXT,
	aims_risk_assessment_triggers TEXT,
	PRIMARY KEY ("AimsRiskAssessmentProcess_aims_id", aims_risk_assessment_triggers),
	FOREIGN KEY("AimsRiskAssessmentProcess_aims_id") REFERENCES "AimsRiskAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_risk_assessment_triggers_AimsRiskAssessmentProcess_aims_id" ON "AimsRiskAssessmentProcess_aims_risk_assessment_triggers" ("AimsRiskAssessmentProcess_aims_id");
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_risk_assessment_triggers_aims_risk_assessment_triggers" ON "AimsRiskAssessmentProcess_aims_risk_assessment_triggers" (aims_risk_assessment_triggers);

CREATE TABLE "AimsRiskAssessmentProcess_aims_document_distribution" (
	"AimsRiskAssessmentProcess_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsRiskAssessmentProcess_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsRiskAssessmentProcess_aims_id") REFERENCES "AimsRiskAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_document_distribution_aims_document_distribution" ON "AimsRiskAssessmentProcess_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsRiskAssessmentProcess_aims_document_distribution_AimsRiskAssessmentProcess_aims_id" ON "AimsRiskAssessmentProcess_aims_document_distribution" ("AimsRiskAssessmentProcess_aims_id");

CREATE TABLE "AimsRiskTreatmentProcess_aims_document_distribution" (
	"AimsRiskTreatmentProcess_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsRiskTreatmentProcess_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsRiskTreatmentProcess_aims_id") REFERENCES "AimsRiskTreatmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentProcess_aims_document_distribution_AimsRiskTreatmentProcess_aims_id" ON "AimsRiskTreatmentProcess_aims_document_distribution" ("AimsRiskTreatmentProcess_aims_id");
CREATE INDEX "ix_AimsRiskTreatmentProcess_aims_document_distribution_aims_document_distribution" ON "AimsRiskTreatmentProcess_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsImpactAssessmentProcess_aims_impact_process_triggers" (
	"AimsImpactAssessmentProcess_aims_id" TEXT,
	aims_impact_process_triggers TEXT,
	PRIMARY KEY ("AimsImpactAssessmentProcess_aims_id", aims_impact_process_triggers),
	FOREIGN KEY("AimsImpactAssessmentProcess_aims_id") REFERENCES "AimsImpactAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_triggers_AimsImpactAssessmentProcess_aims_id" ON "AimsImpactAssessmentProcess_aims_impact_process_triggers" ("AimsImpactAssessmentProcess_aims_id");
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_triggers_aims_impact_process_triggers" ON "AimsImpactAssessmentProcess_aims_impact_process_triggers" (aims_impact_process_triggers);

CREATE TABLE "AimsImpactAssessmentProcess_aims_impact_process_steps" (
	"AimsImpactAssessmentProcess_aims_id" TEXT,
	aims_impact_process_steps TEXT,
	PRIMARY KEY ("AimsImpactAssessmentProcess_aims_id", aims_impact_process_steps),
	FOREIGN KEY("AimsImpactAssessmentProcess_aims_id") REFERENCES "AimsImpactAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_steps_aims_impact_process_steps" ON "AimsImpactAssessmentProcess_aims_impact_process_steps" (aims_impact_process_steps);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_steps_AimsImpactAssessmentProcess_aims_id" ON "AimsImpactAssessmentProcess_aims_impact_process_steps" ("AimsImpactAssessmentProcess_aims_id");

CREATE TABLE "AimsImpactAssessmentProcess_aims_impact_process_subjects" (
	"AimsImpactAssessmentProcess_aims_id" TEXT,
	aims_impact_process_subjects VARCHAR(21),
	PRIMARY KEY ("AimsImpactAssessmentProcess_aims_id", aims_impact_process_subjects),
	FOREIGN KEY("AimsImpactAssessmentProcess_aims_id") REFERENCES "AimsImpactAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_subjects_AimsImpactAssessmentProcess_aims_id" ON "AimsImpactAssessmentProcess_aims_impact_process_subjects" ("AimsImpactAssessmentProcess_aims_id");
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_subjects_aims_impact_process_subjects" ON "AimsImpactAssessmentProcess_aims_impact_process_subjects" (aims_impact_process_subjects);

CREATE TABLE "AimsImpactAssessmentProcess_aims_impact_process_areas" (
	"AimsImpactAssessmentProcess_aims_id" TEXT,
	aims_impact_process_areas VARCHAR(31),
	PRIMARY KEY ("AimsImpactAssessmentProcess_aims_id", aims_impact_process_areas),
	FOREIGN KEY("AimsImpactAssessmentProcess_aims_id") REFERENCES "AimsImpactAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_areas_aims_impact_process_areas" ON "AimsImpactAssessmentProcess_aims_impact_process_areas" (aims_impact_process_areas);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_impact_process_areas_AimsImpactAssessmentProcess_aims_id" ON "AimsImpactAssessmentProcess_aims_impact_process_areas" ("AimsImpactAssessmentProcess_aims_id");

CREATE TABLE "AimsImpactAssessmentProcess_aims_document_distribution" (
	"AimsImpactAssessmentProcess_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsImpactAssessmentProcess_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsImpactAssessmentProcess_aims_id") REFERENCES "AimsImpactAssessmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_document_distribution_aims_document_distribution" ON "AimsImpactAssessmentProcess_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsImpactAssessmentProcess_aims_document_distribution_AimsImpactAssessmentProcess_aims_id" ON "AimsImpactAssessmentProcess_aims_document_distribution" ("AimsImpactAssessmentProcess_aims_id");

CREATE TABLE "AimsStatementOfApplicability_aims_document_distribution" (
	"AimsStatementOfApplicability_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsStatementOfApplicability_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsStatementOfApplicability_aims_id") REFERENCES "AimsStatementOfApplicability" (aims_id)
);
CREATE INDEX "ix_AimsStatementOfApplicability_aims_document_distribution_aims_document_distribution" ON "AimsStatementOfApplicability_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsStatementOfApplicability_aims_document_distribution_AimsStatementOfApplicability_aims_id" ON "AimsStatementOfApplicability_aims_document_distribution" ("AimsStatementOfApplicability_aims_id");

CREATE TABLE "AimsComponentResource_aims_life_cycle_stages" (
	"AimsComponentResource_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsComponentResource_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsComponentResource_aims_id") REFERENCES "AimsComponentResource" (aims_id)
);
CREATE INDEX "ix_AimsComponentResource_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsComponentResource_aims_life_cycle_stages" (aims_life_cycle_stages);
CREATE INDEX "ix_AimsComponentResource_aims_life_cycle_stages_AimsComponentResource_aims_id" ON "AimsComponentResource_aims_life_cycle_stages" ("AimsComponentResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_categories" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_categories VARCHAR(10),
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_categories),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_categories_aims_data_categories" ON "AimsDataResource_aims_data_categories" (aims_data_categories);
CREATE INDEX "ix_AimsDataResource_aims_data_categories_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_categories" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_kinds" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_kinds TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_kinds),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_kinds_aims_data_kinds" ON "AimsDataResource_aims_data_kinds" (aims_data_kinds);
CREATE INDEX "ix_AimsDataResource_aims_data_kinds_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_kinds" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_sources" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_sources TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_sources),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_sources_aims_data_sources" ON "AimsDataResource_aims_data_sources" (aims_data_sources);
CREATE INDEX "ix_AimsDataResource_aims_data_sources_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_sources" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_source_characteristics" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_source_characteristics TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_source_characteristics),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_source_characteristics_aims_data_source_characteristics" ON "AimsDataResource_aims_data_source_characteristics" (aims_data_source_characteristics);
CREATE INDEX "ix_AimsDataResource_aims_data_source_characteristics_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_source_characteristics" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_subject_demographics" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_subject_demographics TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_subject_demographics),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_subject_demographics_aims_data_subject_demographics" ON "AimsDataResource_aims_data_subject_demographics" (aims_data_subject_demographics);
CREATE INDEX "ix_AimsDataResource_aims_data_subject_demographics_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_subject_demographics" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_rights" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_rights TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_rights),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_rights_aims_data_rights" ON "AimsDataResource_aims_data_rights" (aims_data_rights);
CREATE INDEX "ix_AimsDataResource_aims_data_rights_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_rights" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_metadata" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_metadata TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_metadata),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_metadata_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_metadata" ("AimsDataResource_aims_id");
CREATE INDEX "ix_AimsDataResource_aims_data_metadata_aims_data_metadata" ON "AimsDataResource_aims_data_metadata" (aims_data_metadata);

CREATE TABLE "AimsDataResource_aims_data_quality_requirements" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_quality_requirements TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_quality_requirements),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_quality_requirements_aims_data_quality_requirements" ON "AimsDataResource_aims_data_quality_requirements" (aims_data_quality_requirements);
CREATE INDEX "ix_AimsDataResource_aims_data_quality_requirements_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_quality_requirements" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_quality_results" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_quality_results TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_quality_results),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_quality_results_aims_data_quality_results" ON "AimsDataResource_aims_data_quality_results" (aims_data_quality_results);
CREATE INDEX "ix_AimsDataResource_aims_data_quality_results_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_quality_results" ("AimsDataResource_aims_id");

CREATE TABLE "AimsDataResource_aims_data_bias_issues" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_bias_issues TEXT,
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_bias_issues),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_bias_issues_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_bias_issues" ("AimsDataResource_aims_id");
CREATE INDEX "ix_AimsDataResource_aims_data_bias_issues_aims_data_bias_issues" ON "AimsDataResource_aims_data_bias_issues" (aims_data_bias_issues);

CREATE TABLE "AimsDataResource_aims_data_preparation_methods" (
	"AimsDataResource_aims_id" TEXT,
	aims_data_preparation_methods VARCHAR(23),
	PRIMARY KEY ("AimsDataResource_aims_id", aims_data_preparation_methods),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_data_preparation_methods_AimsDataResource_aims_id" ON "AimsDataResource_aims_data_preparation_methods" ("AimsDataResource_aims_id");
CREATE INDEX "ix_AimsDataResource_aims_data_preparation_methods_aims_data_preparation_methods" ON "AimsDataResource_aims_data_preparation_methods" (aims_data_preparation_methods);

CREATE TABLE "AimsDataResource_aims_life_cycle_stages" (
	"AimsDataResource_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsDataResource_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsDataResource_aims_id") REFERENCES "AimsDataResource" (aims_id)
);
CREATE INDEX "ix_AimsDataResource_aims_life_cycle_stages_AimsDataResource_aims_id" ON "AimsDataResource_aims_life_cycle_stages" ("AimsDataResource_aims_id");
CREATE INDEX "ix_AimsDataResource_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsDataResource_aims_life_cycle_stages" (aims_life_cycle_stages);

CREATE TABLE "AimsToolingResource_aims_life_cycle_stages" (
	"AimsToolingResource_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsToolingResource_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsToolingResource_aims_id") REFERENCES "AimsToolingResource" (aims_id)
);
CREATE INDEX "ix_AimsToolingResource_aims_life_cycle_stages_AimsToolingResource_aims_id" ON "AimsToolingResource_aims_life_cycle_stages" ("AimsToolingResource_aims_id");
CREATE INDEX "ix_AimsToolingResource_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsToolingResource_aims_life_cycle_stages" (aims_life_cycle_stages);

CREATE TABLE "AimsComputingResource_aims_life_cycle_stages" (
	"AimsComputingResource_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsComputingResource_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsComputingResource_aims_id") REFERENCES "AimsComputingResource" (aims_id)
);
CREATE INDEX "ix_AimsComputingResource_aims_life_cycle_stages_AimsComputingResource_aims_id" ON "AimsComputingResource_aims_life_cycle_stages" ("AimsComputingResource_aims_id");
CREATE INDEX "ix_AimsComputingResource_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsComputingResource_aims_life_cycle_stages" (aims_life_cycle_stages);

CREATE TABLE "AimsAwarenessProgramme_aims_awareness_topics" (
	"AimsAwarenessProgramme_aims_id" TEXT,
	aims_awareness_topics TEXT,
	PRIMARY KEY ("AimsAwarenessProgramme_aims_id", aims_awareness_topics),
	FOREIGN KEY("AimsAwarenessProgramme_aims_id") REFERENCES "AimsAwarenessProgramme" (aims_id)
);
CREATE INDEX "ix_AimsAwarenessProgramme_aims_awareness_topics_aims_awareness_topics" ON "AimsAwarenessProgramme_aims_awareness_topics" (aims_awareness_topics);
CREATE INDEX "ix_AimsAwarenessProgramme_aims_awareness_topics_AimsAwarenessProgramme_aims_id" ON "AimsAwarenessProgramme_aims_awareness_topics" ("AimsAwarenessProgramme_aims_id");

CREATE TABLE "AimsAwarenessProgramme_aims_awareness_methods" (
	"AimsAwarenessProgramme_aims_id" TEXT,
	aims_awareness_methods TEXT,
	PRIMARY KEY ("AimsAwarenessProgramme_aims_id", aims_awareness_methods),
	FOREIGN KEY("AimsAwarenessProgramme_aims_id") REFERENCES "AimsAwarenessProgramme" (aims_id)
);
CREATE INDEX "ix_AimsAwarenessProgramme_aims_awareness_methods_AimsAwarenessProgramme_aims_id" ON "AimsAwarenessProgramme_aims_awareness_methods" ("AimsAwarenessProgramme_aims_id");
CREATE INDEX "ix_AimsAwarenessProgramme_aims_awareness_methods_aims_awareness_methods" ON "AimsAwarenessProgramme_aims_awareness_methods" (aims_awareness_methods);

CREATE TABLE "AimsAwarenessProgramme_aims_document_distribution" (
	"AimsAwarenessProgramme_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsAwarenessProgramme_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsAwarenessProgramme_aims_id") REFERENCES "AimsAwarenessProgramme" (aims_id)
);
CREATE INDEX "ix_AimsAwarenessProgramme_aims_document_distribution_AimsAwarenessProgramme_aims_id" ON "AimsAwarenessProgramme_aims_document_distribution" ("AimsAwarenessProgramme_aims_id");
CREATE INDEX "ix_AimsAwarenessProgramme_aims_document_distribution_aims_document_distribution" ON "AimsAwarenessProgramme_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsCommunicationPlan_aims_document_distribution" (
	"AimsCommunicationPlan_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsCommunicationPlan_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsCommunicationPlan_aims_id") REFERENCES "AimsCommunicationPlan" (aims_id)
);
CREATE INDEX "ix_AimsCommunicationPlan_aims_document_distribution_aims_document_distribution" ON "AimsCommunicationPlan_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsCommunicationPlan_aims_document_distribution_AimsCommunicationPlan_aims_id" ON "AimsCommunicationPlan_aims_document_distribution" ("AimsCommunicationPlan_aims_id");

CREATE TABLE "AimsMonitoringProgramme_aims_document_distribution" (
	"AimsMonitoringProgramme_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsMonitoringProgramme_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsMonitoringProgramme_aims_id") REFERENCES "AimsMonitoringProgramme" (aims_id)
);
CREATE INDEX "ix_AimsMonitoringProgramme_aims_document_distribution_aims_document_distribution" ON "AimsMonitoringProgramme_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsMonitoringProgramme_aims_document_distribution_AimsMonitoringProgramme_aims_id" ON "AimsMonitoringProgramme_aims_document_distribution" ("AimsMonitoringProgramme_aims_id");

CREATE TABLE "AimsSupplierRelationship_aims_supplier_provides" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_supplier_provides TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_supplier_provides),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_supplier_provides_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_supplier_provides" ("AimsSupplierRelationship_aims_id");
CREATE INDEX "ix_AimsSupplierRelationship_aims_supplier_provides_aims_supplier_provides" ON "AimsSupplierRelationship_aims_supplier_provides" (aims_supplier_provides);

CREATE TABLE "AimsSupplierRelationship_aims_supplier_requirements" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_supplier_requirements TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_supplier_requirements),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_supplier_requirements_aims_supplier_requirements" ON "AimsSupplierRelationship_aims_supplier_requirements" (aims_supplier_requirements);
CREATE INDEX "ix_AimsSupplierRelationship_aims_supplier_requirements_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_supplier_requirements" ("AimsSupplierRelationship_aims_id");

CREATE TABLE "AimsSupplierRelationship_aims_supplier_corrective_actions" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_supplier_corrective_actions TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_supplier_corrective_actions),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_supplier_corrective_actions_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_supplier_corrective_actions" ("AimsSupplierRelationship_aims_id");
CREATE INDEX "ix_AimsSupplierRelationship_aims_supplier_corrective_actions_aims_supplier_corrective_actions" ON "AimsSupplierRelationship_aims_supplier_corrective_actions" (aims_supplier_corrective_actions);

CREATE TABLE "AimsSupplierRelationship_aims_life_cycle_stages" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsSupplierRelationship_aims_life_cycle_stages" (aims_life_cycle_stages);
CREATE INDEX "ix_AimsSupplierRelationship_aims_life_cycle_stages_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_life_cycle_stages" ("AimsSupplierRelationship_aims_id");

CREATE TABLE "AimsSupplierRelationship_aims_relationship_party_roles" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_relationship_party_roles VARCHAR(30),
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_relationship_party_roles),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_party_roles_aims_relationship_party_roles" ON "AimsSupplierRelationship_aims_relationship_party_roles" (aims_relationship_party_roles);
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_party_roles_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_relationship_party_roles" ("AimsSupplierRelationship_aims_id");

CREATE TABLE "AimsSupplierRelationship_aims_relationship_responsibilities" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_relationship_responsibilities TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_relationship_responsibilities),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_responsibilities_aims_relationship_responsibilities" ON "AimsSupplierRelationship_aims_relationship_responsibilities" (aims_relationship_responsibilities);
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_responsibilities_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_relationship_responsibilities" ("AimsSupplierRelationship_aims_id");

CREATE TABLE "AimsSupplierRelationship_aims_relationship_documentation" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_relationship_documentation TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_relationship_documentation),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_documentation_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_relationship_documentation" ("AimsSupplierRelationship_aims_id");
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_documentation_aims_relationship_documentation" ON "AimsSupplierRelationship_aims_relationship_documentation" (aims_relationship_documentation);

CREATE TABLE "AimsSupplierRelationship_aims_relationship_assurance_evidence" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_relationship_assurance_evidence TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_relationship_assurance_evidence),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_assurance_evidence_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_relationship_assurance_evidence" ("AimsSupplierRelationship_aims_id");
CREATE INDEX "ix_AimsSupplierRelationship_aims_relationship_assurance_evidence_aims_relationship_assurance_evidence" ON "AimsSupplierRelationship_aims_relationship_assurance_evidence" (aims_relationship_assurance_evidence);

CREATE TABLE "AimsCustomerRelationship_aims_customer_expectations" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_customer_expectations TEXT,
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_customer_expectations),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_customer_expectations_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_customer_expectations" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_customer_expectations_aims_customer_expectations" ON "AimsCustomerRelationship_aims_customer_expectations" (aims_customer_expectations);

CREATE TABLE "AimsCustomerRelationship_aims_customer_communicated_limits" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_customer_communicated_limits TEXT,
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_customer_communicated_limits),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_customer_communicated_limits_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_customer_communicated_limits" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_customer_communicated_limits_aims_customer_communicated_limits" ON "AimsCustomerRelationship_aims_customer_communicated_limits" (aims_customer_communicated_limits);

CREATE TABLE "AimsCustomerRelationship_aims_life_cycle_stages" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_life_cycle_stages_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_life_cycle_stages" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsCustomerRelationship_aims_life_cycle_stages" (aims_life_cycle_stages);

CREATE TABLE "AimsCustomerRelationship_aims_relationship_party_roles" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_relationship_party_roles VARCHAR(30),
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_relationship_party_roles),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_party_roles_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_relationship_party_roles" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_party_roles_aims_relationship_party_roles" ON "AimsCustomerRelationship_aims_relationship_party_roles" (aims_relationship_party_roles);

CREATE TABLE "AimsCustomerRelationship_aims_relationship_responsibilities" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_relationship_responsibilities TEXT,
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_relationship_responsibilities),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_responsibilities_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_relationship_responsibilities" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_responsibilities_aims_relationship_responsibilities" ON "AimsCustomerRelationship_aims_relationship_responsibilities" (aims_relationship_responsibilities);

CREATE TABLE "AimsCustomerRelationship_aims_relationship_documentation" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_relationship_documentation TEXT,
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_relationship_documentation),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_documentation_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_relationship_documentation" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_documentation_aims_relationship_documentation" ON "AimsCustomerRelationship_aims_relationship_documentation" (aims_relationship_documentation);

CREATE TABLE "AimsCustomerRelationship_aims_relationship_assurance_evidence" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_relationship_assurance_evidence TEXT,
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_relationship_assurance_evidence),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_assurance_evidence_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_relationship_assurance_evidence" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_relationship_assurance_evidence_aims_relationship_assurance_evidence" ON "AimsCustomerRelationship_aims_relationship_assurance_evidence" (aims_relationship_assurance_evidence);

CREATE TABLE "AimsIncident_aims_incident_threats" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_threats VARCHAR(15),
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_threats),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_threats_AimsIncident_aims_id" ON "AimsIncident_aims_incident_threats" ("AimsIncident_aims_id");
CREATE INDEX "ix_AimsIncident_aims_incident_threats_aims_incident_threats" ON "AimsIncident_aims_incident_threats" (aims_incident_threats);

CREATE TABLE "AimsIncident_aims_incident_impact_areas" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_impact_areas VARCHAR(31),
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_impact_areas),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_impact_areas_AimsIncident_aims_id" ON "AimsIncident_aims_incident_impact_areas" ("AimsIncident_aims_id");
CREATE INDEX "ix_AimsIncident_aims_incident_impact_areas_aims_incident_impact_areas" ON "AimsIncident_aims_incident_impact_areas" (aims_incident_impact_areas);

CREATE TABLE "AimsIncident_aims_incident_response_actions" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_response_actions TEXT,
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_response_actions),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_response_actions_AimsIncident_aims_id" ON "AimsIncident_aims_incident_response_actions" ("AimsIncident_aims_id");
CREATE INDEX "ix_AimsIncident_aims_incident_response_actions_aims_incident_response_actions" ON "AimsIncident_aims_incident_response_actions" (aims_incident_response_actions);

CREATE TABLE "AimsIncident_aims_incident_recovery_actions" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_recovery_actions TEXT,
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_recovery_actions),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_recovery_actions_aims_incident_recovery_actions" ON "AimsIncident_aims_incident_recovery_actions" (aims_incident_recovery_actions);
CREATE INDEX "ix_AimsIncident_aims_incident_recovery_actions_AimsIncident_aims_id" ON "AimsIncident_aims_incident_recovery_actions" ("AimsIncident_aims_id");

CREATE TABLE "AimsIncident_aims_incident_lessons_learned" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_lessons_learned TEXT,
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_lessons_learned),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_lessons_learned_aims_incident_lessons_learned" ON "AimsIncident_aims_incident_lessons_learned" (aims_incident_lessons_learned);
CREATE INDEX "ix_AimsIncident_aims_incident_lessons_learned_AimsIncident_aims_id" ON "AimsIncident_aims_incident_lessons_learned" ("AimsIncident_aims_id");

CREATE TABLE "AimsIncident_aims_incident_notifications" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_notifications TEXT,
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_notifications),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_notifications_AimsIncident_aims_id" ON "AimsIncident_aims_incident_notifications" ("AimsIncident_aims_id");
CREATE INDEX "ix_AimsIncident_aims_incident_notifications_aims_incident_notifications" ON "AimsIncident_aims_incident_notifications" (aims_incident_notifications);

CREATE TABLE "AimsConcernReportingProcess_aims_concern_process_confidentiality" (
	"AimsConcernReportingProcess_aims_id" TEXT,
	aims_concern_process_confidentiality TEXT,
	PRIMARY KEY ("AimsConcernReportingProcess_aims_id", aims_concern_process_confidentiality),
	FOREIGN KEY("AimsConcernReportingProcess_aims_id") REFERENCES "AimsConcernReportingProcess" (aims_id)
);
CREATE INDEX "ix_AimsConcernReportingProcess_aims_concern_process_confidentiality_AimsConcernReportingProcess_aims_id" ON "AimsConcernReportingProcess_aims_concern_process_confidentiality" ("AimsConcernReportingProcess_aims_id");
CREATE INDEX "ix_AimsConcernReportingProcess_aims_concern_process_confidentiality_aims_concern_process_confidentiality" ON "AimsConcernReportingProcess_aims_concern_process_confidentiality" (aims_concern_process_confidentiality);

CREATE TABLE "AimsConcernReportingProcess_aims_document_distribution" (
	"AimsConcernReportingProcess_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsConcernReportingProcess_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsConcernReportingProcess_aims_id") REFERENCES "AimsConcernReportingProcess" (aims_id)
);
CREATE INDEX "ix_AimsConcernReportingProcess_aims_document_distribution_aims_document_distribution" ON "AimsConcernReportingProcess_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsConcernReportingProcess_aims_document_distribution_AimsConcernReportingProcess_aims_id" ON "AimsConcernReportingProcess_aims_document_distribution" ("AimsConcernReportingProcess_aims_id");

CREATE TABLE "AimsIdentifiedImpact" (
	id INTEGER NOT NULL,
	aims_identified_impact_subject VARCHAR(21) NOT NULL,
	aims_identified_impact_area VARCHAR(31),
	aims_identified_impact_direction VARCHAR(8),
	aims_identified_impact_text TEXT NOT NULL,
	"AimsImpactAssessment_aims_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsIdentifiedImpact_id" ON "AimsIdentifiedImpact" (id);

CREATE TABLE "AimsIncludedControl" (
	id INTEGER NOT NULL,
	aims_implementation_state VARCHAR(11) NOT NULL,
	aims_responsible_role TEXT,
	aims_included_control TEXT,
	aims_included_evidence TEXT,
	aims_included_target_date DATE,
	aims_entry_annex_a_control VARCHAR(7),
	aims_entry_type TEXT,
	aims_entry_justification TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(aims_responsible_role) REFERENCES "AimsRole" (aims_id),
	FOREIGN KEY(aims_included_control) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsIncludedControl_id" ON "AimsIncludedControl" (id);

CREATE TABLE "AimsAiSystem" (
	aims_system_intended_purpose TEXT,
	aims_system_domain TEXT,
	aims_system_deployment_context TEXT,
	aims_system_life_cycle_stage VARCHAR(27),
	aims_system_rationale TEXT,
	aims_system_ml_approach TEXT,
	aims_system_continuous_learning BOOLEAN,
	aims_system_automation_level TEXT,
	aims_system_deployment_plan TEXT,
	aims_system_log_retention TEXT,
	aims_system_human_oversight_required BOOLEAN,
	aims_system_human_oversight TEXT,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_system_deployment_plan) REFERENCES "AimsDocumentedInformation" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_id" ON "AimsAiSystem" (aims_id);

CREATE TABLE "AimsAudit" (
	aims_audit_type VARCHAR(12) NOT NULL,
	aims_audit_scope TEXT,
	aims_audit_period_start DATE,
	aims_audit_period_end DATE,
	aims_audit_lead TEXT,
	aims_audit_plan TEXT,
	aims_audit_conclusion TEXT,
	aims_audit_report_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	aims_document_reference TEXT,
	aims_document_version TEXT,
	aims_document_author TEXT,
	aims_document_owner TEXT,
	aims_document_format TEXT,
	aims_document_medium TEXT,
	aims_document_approver TEXT,
	aims_document_approval_date DATE,
	aims_document_effective_date DATE,
	aims_document_last_review_date DATE,
	aims_document_next_review_date DATE,
	aims_document_status TEXT,
	aims_document_classification TEXT,
	aims_document_retention TEXT,
	aims_document_disposition TEXT,
	aims_document_storage TEXT,
	aims_document_change_control TEXT,
	aims_document_external_origin BOOLEAN,
	aims_document_external_source TEXT,
	"AimsManagementSystem_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_audit_plan) REFERENCES "AimsDocumentedInformation" (aims_id),
	FOREIGN KEY("AimsManagementSystem_aims_id") REFERENCES "AimsManagementSystem" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_id" ON "AimsAudit" (aims_id);

CREATE TABLE "AimsInterestedParty_aims_party_ai_roles" (
	"AimsInterestedParty_aims_id" TEXT,
	aims_party_ai_roles VARCHAR(30),
	PRIMARY KEY ("AimsInterestedParty_aims_id", aims_party_ai_roles),
	FOREIGN KEY("AimsInterestedParty_aims_id") REFERENCES "AimsInterestedParty" (aims_id)
);
CREATE INDEX "ix_AimsInterestedParty_aims_party_ai_roles_aims_party_ai_roles" ON "AimsInterestedParty_aims_party_ai_roles" (aims_party_ai_roles);
CREATE INDEX "ix_AimsInterestedParty_aims_party_ai_roles_AimsInterestedParty_aims_id" ON "AimsInterestedParty_aims_party_ai_roles" ("AimsInterestedParty_aims_id");

CREATE TABLE "AimsInterestedParty_aims_party_requirements" (
	"AimsInterestedParty_aims_id" TEXT,
	aims_party_requirements TEXT,
	PRIMARY KEY ("AimsInterestedParty_aims_id", aims_party_requirements),
	FOREIGN KEY("AimsInterestedParty_aims_id") REFERENCES "AimsInterestedParty" (aims_id)
);
CREATE INDEX "ix_AimsInterestedParty_aims_party_requirements_aims_party_requirements" ON "AimsInterestedParty_aims_party_requirements" (aims_party_requirements);
CREATE INDEX "ix_AimsInterestedParty_aims_party_requirements_AimsInterestedParty_aims_id" ON "AimsInterestedParty_aims_party_requirements" ("AimsInterestedParty_aims_id");

CREATE TABLE "AimsInterestedParty_aims_party_addressed_requirements" (
	"AimsInterestedParty_aims_id" TEXT,
	aims_party_addressed_requirements TEXT,
	PRIMARY KEY ("AimsInterestedParty_aims_id", aims_party_addressed_requirements),
	FOREIGN KEY("AimsInterestedParty_aims_id") REFERENCES "AimsInterestedParty" (aims_id)
);
CREATE INDEX "ix_AimsInterestedParty_aims_party_addressed_requirements_aims_party_addressed_requirements" ON "AimsInterestedParty_aims_party_addressed_requirements" (aims_party_addressed_requirements);
CREATE INDEX "ix_AimsInterestedParty_aims_party_addressed_requirements_AimsInterestedParty_aims_id" ON "AimsInterestedParty_aims_party_addressed_requirements" ("AimsInterestedParty_aims_id");

CREATE TABLE "AimsInterestedParty_aims_party_climate_change_requirements" (
	"AimsInterestedParty_aims_id" TEXT,
	aims_party_climate_change_requirements TEXT,
	PRIMARY KEY ("AimsInterestedParty_aims_id", aims_party_climate_change_requirements),
	FOREIGN KEY("AimsInterestedParty_aims_id") REFERENCES "AimsInterestedParty" (aims_id)
);
CREATE INDEX "ix_AimsInterestedParty_aims_party_climate_change_requirements_AimsInterestedParty_aims_id" ON "AimsInterestedParty_aims_party_climate_change_requirements" ("AimsInterestedParty_aims_id");
CREATE INDEX "ix_AimsInterestedParty_aims_party_climate_change_requirements_aims_party_climate_change_requirements" ON "AimsInterestedParty_aims_party_climate_change_requirements" (aims_party_climate_change_requirements);

CREATE TABLE "AimsTopicSpecificPolicy_aims_relevant_controls" (
	"AimsTopicSpecificPolicy_aims_id" TEXT,
	aims_relevant_controls_aims_id TEXT,
	PRIMARY KEY ("AimsTopicSpecificPolicy_aims_id", aims_relevant_controls_aims_id),
	FOREIGN KEY("AimsTopicSpecificPolicy_aims_id") REFERENCES "AimsTopicSpecificPolicy" (aims_id),
	FOREIGN KEY(aims_relevant_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_relevant_controls_AimsTopicSpecificPolicy_aims_id" ON "AimsTopicSpecificPolicy_aims_relevant_controls" ("AimsTopicSpecificPolicy_aims_id");
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_relevant_controls_aims_relevant_controls_aims_id" ON "AimsTopicSpecificPolicy_aims_relevant_controls" (aims_relevant_controls_aims_id);

CREATE TABLE "AimsTopicSpecificPolicy_aims_cited_annex_a_controls" (
	"AimsTopicSpecificPolicy_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsTopicSpecificPolicy_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsTopicSpecificPolicy_aims_id") REFERENCES "AimsTopicSpecificPolicy" (aims_id)
);
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_cited_annex_a_controls_AimsTopicSpecificPolicy_aims_id" ON "AimsTopicSpecificPolicy_aims_cited_annex_a_controls" ("AimsTopicSpecificPolicy_aims_id");
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsTopicSpecificPolicy_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);

CREATE TABLE "AimsTopicSpecificPolicy_aims_document_distribution" (
	"AimsTopicSpecificPolicy_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsTopicSpecificPolicy_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsTopicSpecificPolicy_aims_id") REFERENCES "AimsTopicSpecificPolicy" (aims_id)
);
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_document_distribution_aims_document_distribution" ON "AimsTopicSpecificPolicy_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsTopicSpecificPolicy_aims_document_distribution_AimsTopicSpecificPolicy_aims_id" ON "AimsTopicSpecificPolicy_aims_document_distribution" ("AimsTopicSpecificPolicy_aims_id");

CREATE TABLE "AimsObjective_aims_relevant_controls" (
	"AimsObjective_aims_id" TEXT,
	aims_relevant_controls_aims_id TEXT,
	PRIMARY KEY ("AimsObjective_aims_id", aims_relevant_controls_aims_id),
	FOREIGN KEY("AimsObjective_aims_id") REFERENCES "AimsObjective" (aims_id),
	FOREIGN KEY(aims_relevant_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsObjective_aims_relevant_controls_AimsObjective_aims_id" ON "AimsObjective_aims_relevant_controls" ("AimsObjective_aims_id");
CREATE INDEX "ix_AimsObjective_aims_relevant_controls_aims_relevant_controls_aims_id" ON "AimsObjective_aims_relevant_controls" (aims_relevant_controls_aims_id);

CREATE TABLE "AimsObjective_aims_objective_categories" (
	"AimsObjective_aims_id" TEXT,
	aims_objective_categories VARCHAR(31),
	PRIMARY KEY ("AimsObjective_aims_id", aims_objective_categories),
	FOREIGN KEY("AimsObjective_aims_id") REFERENCES "AimsObjective" (aims_id)
);
CREATE INDEX "ix_AimsObjective_aims_objective_categories_AimsObjective_aims_id" ON "AimsObjective_aims_objective_categories" ("AimsObjective_aims_id");
CREATE INDEX "ix_AimsObjective_aims_objective_categories_aims_objective_categories" ON "AimsObjective_aims_objective_categories" (aims_objective_categories);

CREATE TABLE "AimsObjective_aims_objective_risks" (
	"AimsObjective_aims_id" TEXT,
	aims_objective_risks_aims_id TEXT,
	PRIMARY KEY ("AimsObjective_aims_id", aims_objective_risks_aims_id),
	FOREIGN KEY("AimsObjective_aims_id") REFERENCES "AimsObjective" (aims_id),
	FOREIGN KEY(aims_objective_risks_aims_id) REFERENCES "AimsRisk" (aims_id)
);
CREATE INDEX "ix_AimsObjective_aims_objective_risks_AimsObjective_aims_id" ON "AimsObjective_aims_objective_risks" ("AimsObjective_aims_id");
CREATE INDEX "ix_AimsObjective_aims_objective_risks_aims_objective_risks_aims_id" ON "AimsObjective_aims_objective_risks" (aims_objective_risks_aims_id);

CREATE TABLE "AimsPlannedAction_aims_planned_action_risks" (
	"AimsPlannedAction_aims_id" TEXT,
	aims_planned_action_risks_aims_id TEXT,
	PRIMARY KEY ("AimsPlannedAction_aims_id", aims_planned_action_risks_aims_id),
	FOREIGN KEY("AimsPlannedAction_aims_id") REFERENCES "AimsPlannedAction" (aims_id),
	FOREIGN KEY(aims_planned_action_risks_aims_id) REFERENCES "AimsRisk" (aims_id)
);
CREATE INDEX "ix_AimsPlannedAction_aims_planned_action_risks_aims_planned_action_risks_aims_id" ON "AimsPlannedAction_aims_planned_action_risks" (aims_planned_action_risks_aims_id);
CREATE INDEX "ix_AimsPlannedAction_aims_planned_action_risks_AimsPlannedAction_aims_id" ON "AimsPlannedAction_aims_planned_action_risks" ("AimsPlannedAction_aims_id");

CREATE TABLE "AimsPlannedAction_aims_planned_action_opportunities" (
	"AimsPlannedAction_aims_id" TEXT,
	aims_planned_action_opportunities TEXT,
	PRIMARY KEY ("AimsPlannedAction_aims_id", aims_planned_action_opportunities),
	FOREIGN KEY("AimsPlannedAction_aims_id") REFERENCES "AimsPlannedAction" (aims_id)
);
CREATE INDEX "ix_AimsPlannedAction_aims_planned_action_opportunities_AimsPlannedAction_aims_id" ON "AimsPlannedAction_aims_planned_action_opportunities" ("AimsPlannedAction_aims_id");
CREATE INDEX "ix_AimsPlannedAction_aims_planned_action_opportunities_aims_planned_action_opportunities" ON "AimsPlannedAction_aims_planned_action_opportunities" (aims_planned_action_opportunities);

CREATE TABLE "AimsRiskAssessment_aims_assessment_risks" (
	"AimsRiskAssessment_aims_id" TEXT,
	aims_assessment_risks_aims_id TEXT,
	PRIMARY KEY ("AimsRiskAssessment_aims_id", aims_assessment_risks_aims_id),
	FOREIGN KEY("AimsRiskAssessment_aims_id") REFERENCES "AimsRiskAssessment" (aims_id),
	FOREIGN KEY(aims_assessment_risks_aims_id) REFERENCES "AimsRisk" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessment_aims_assessment_risks_aims_assessment_risks_aims_id" ON "AimsRiskAssessment_aims_assessment_risks" (aims_assessment_risks_aims_id);
CREATE INDEX "ix_AimsRiskAssessment_aims_assessment_risks_AimsRiskAssessment_aims_id" ON "AimsRiskAssessment_aims_assessment_risks" ("AimsRiskAssessment_aims_id");

CREATE TABLE "AimsRiskAssessment_aims_assessment_impact_assessments" (
	"AimsRiskAssessment_aims_id" TEXT,
	aims_assessment_impact_assessments_aims_id TEXT,
	PRIMARY KEY ("AimsRiskAssessment_aims_id", aims_assessment_impact_assessments_aims_id),
	FOREIGN KEY("AimsRiskAssessment_aims_id") REFERENCES "AimsRiskAssessment" (aims_id),
	FOREIGN KEY(aims_assessment_impact_assessments_aims_id) REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessment_aims_assessment_impact_assessments_AimsRiskAssessment_aims_id" ON "AimsRiskAssessment_aims_assessment_impact_assessments" ("AimsRiskAssessment_aims_id");
CREATE INDEX "ix_AimsRiskAssessment_aims_assessment_impact_assessments_aims_assessment_impact_assessments_aims_id" ON "AimsRiskAssessment_aims_assessment_impact_assessments" (aims_assessment_impact_assessments_aims_id);

CREATE TABLE "AimsRiskAssessment_aims_assessment_recommendations" (
	"AimsRiskAssessment_aims_id" TEXT,
	aims_assessment_recommendations TEXT,
	PRIMARY KEY ("AimsRiskAssessment_aims_id", aims_assessment_recommendations),
	FOREIGN KEY("AimsRiskAssessment_aims_id") REFERENCES "AimsRiskAssessment" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessment_aims_assessment_recommendations_AimsRiskAssessment_aims_id" ON "AimsRiskAssessment_aims_assessment_recommendations" ("AimsRiskAssessment_aims_id");
CREATE INDEX "ix_AimsRiskAssessment_aims_assessment_recommendations_aims_assessment_recommendations" ON "AimsRiskAssessment_aims_assessment_recommendations" (aims_assessment_recommendations);

CREATE TABLE "AimsRiskAssessment_aims_document_distribution" (
	"AimsRiskAssessment_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsRiskAssessment_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsRiskAssessment_aims_id") REFERENCES "AimsRiskAssessment" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessment_aims_document_distribution_AimsRiskAssessment_aims_id" ON "AimsRiskAssessment_aims_document_distribution" ("AimsRiskAssessment_aims_id");
CREATE INDEX "ix_AimsRiskAssessment_aims_document_distribution_aims_document_distribution" ON "AimsRiskAssessment_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsRisk_aims_risk_source_categories" (
	"AimsRisk_aims_id" TEXT,
	aims_risk_source_categories VARCHAR(20),
	PRIMARY KEY ("AimsRisk_aims_id", aims_risk_source_categories),
	FOREIGN KEY("AimsRisk_aims_id") REFERENCES "AimsRisk" (aims_id)
);
CREATE INDEX "ix_AimsRisk_aims_risk_source_categories_aims_risk_source_categories" ON "AimsRisk_aims_risk_source_categories" (aims_risk_source_categories);
CREATE INDEX "ix_AimsRisk_aims_risk_source_categories_AimsRisk_aims_id" ON "AimsRisk_aims_risk_source_categories" ("AimsRisk_aims_id");

CREATE TABLE "AimsRisk_aims_risk_objectives" (
	"AimsRisk_aims_id" TEXT,
	aims_risk_objectives_aims_id TEXT,
	PRIMARY KEY ("AimsRisk_aims_id", aims_risk_objectives_aims_id),
	FOREIGN KEY("AimsRisk_aims_id") REFERENCES "AimsRisk" (aims_id),
	FOREIGN KEY(aims_risk_objectives_aims_id) REFERENCES "AimsObjective" (aims_id)
);
CREATE INDEX "ix_AimsRisk_aims_risk_objectives_AimsRisk_aims_id" ON "AimsRisk_aims_risk_objectives" ("AimsRisk_aims_id");
CREATE INDEX "ix_AimsRisk_aims_risk_objectives_aims_risk_objectives_aims_id" ON "AimsRisk_aims_risk_objectives" (aims_risk_objectives_aims_id);

CREATE TABLE "AimsRisk_aims_risk_existing_controls" (
	"AimsRisk_aims_id" TEXT,
	aims_risk_existing_controls_aims_id TEXT,
	PRIMARY KEY ("AimsRisk_aims_id", aims_risk_existing_controls_aims_id),
	FOREIGN KEY("AimsRisk_aims_id") REFERENCES "AimsRisk" (aims_id),
	FOREIGN KEY(aims_risk_existing_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsRisk_aims_risk_existing_controls_AimsRisk_aims_id" ON "AimsRisk_aims_risk_existing_controls" ("AimsRisk_aims_id");
CREATE INDEX "ix_AimsRisk_aims_risk_existing_controls_aims_risk_existing_controls_aims_id" ON "AimsRisk_aims_risk_existing_controls" (aims_risk_existing_controls_aims_id);

CREATE TABLE "AimsRisk_aims_risk_impact_assessments" (
	"AimsRisk_aims_id" TEXT,
	aims_risk_impact_assessments_aims_id TEXT,
	PRIMARY KEY ("AimsRisk_aims_id", aims_risk_impact_assessments_aims_id),
	FOREIGN KEY("AimsRisk_aims_id") REFERENCES "AimsRisk" (aims_id),
	FOREIGN KEY(aims_risk_impact_assessments_aims_id) REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsRisk_aims_risk_impact_assessments_AimsRisk_aims_id" ON "AimsRisk_aims_risk_impact_assessments" ("AimsRisk_aims_id");
CREATE INDEX "ix_AimsRisk_aims_risk_impact_assessments_aims_risk_impact_assessments_aims_id" ON "AimsRisk_aims_risk_impact_assessments" (aims_risk_impact_assessments_aims_id);

CREATE TABLE "AimsRiskTreatmentPlan_aims_plan_risks" (
	"AimsRiskTreatmentPlan_aims_id" TEXT,
	aims_plan_risks_aims_id TEXT,
	PRIMARY KEY ("AimsRiskTreatmentPlan_aims_id", aims_plan_risks_aims_id),
	FOREIGN KEY("AimsRiskTreatmentPlan_aims_id") REFERENCES "AimsRiskTreatmentPlan" (aims_id),
	FOREIGN KEY(aims_plan_risks_aims_id) REFERENCES "AimsRisk" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_risks_AimsRiskTreatmentPlan_aims_id" ON "AimsRiskTreatmentPlan_aims_plan_risks" ("AimsRiskTreatmentPlan_aims_id");
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_risks_aims_plan_risks_aims_id" ON "AimsRiskTreatmentPlan_aims_plan_risks" (aims_plan_risks_aims_id);

CREATE TABLE "AimsRiskTreatmentPlan_aims_plan_actions" (
	"AimsRiskTreatmentPlan_aims_id" TEXT,
	aims_plan_actions TEXT,
	PRIMARY KEY ("AimsRiskTreatmentPlan_aims_id", aims_plan_actions),
	FOREIGN KEY("AimsRiskTreatmentPlan_aims_id") REFERENCES "AimsRiskTreatmentPlan" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_actions_aims_plan_actions" ON "AimsRiskTreatmentPlan_aims_plan_actions" (aims_plan_actions);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_actions_AimsRiskTreatmentPlan_aims_id" ON "AimsRiskTreatmentPlan_aims_plan_actions" ("AimsRiskTreatmentPlan_aims_id");

CREATE TABLE "AimsRiskTreatmentPlan_aims_plan_controls" (
	"AimsRiskTreatmentPlan_aims_id" TEXT,
	aims_plan_controls_aims_id TEXT,
	PRIMARY KEY ("AimsRiskTreatmentPlan_aims_id", aims_plan_controls_aims_id),
	FOREIGN KEY("AimsRiskTreatmentPlan_aims_id") REFERENCES "AimsRiskTreatmentPlan" (aims_id),
	FOREIGN KEY(aims_plan_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_controls_aims_plan_controls_aims_id" ON "AimsRiskTreatmentPlan_aims_plan_controls" (aims_plan_controls_aims_id);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_controls_AimsRiskTreatmentPlan_aims_id" ON "AimsRiskTreatmentPlan_aims_plan_controls" ("AimsRiskTreatmentPlan_aims_id");

CREATE TABLE "AimsRiskTreatmentPlan_aims_plan_responsible_parties" (
	"AimsRiskTreatmentPlan_aims_id" TEXT,
	aims_plan_responsible_parties TEXT,
	PRIMARY KEY ("AimsRiskTreatmentPlan_aims_id", aims_plan_responsible_parties),
	FOREIGN KEY("AimsRiskTreatmentPlan_aims_id") REFERENCES "AimsRiskTreatmentPlan" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_responsible_parties_AimsRiskTreatmentPlan_aims_id" ON "AimsRiskTreatmentPlan_aims_plan_responsible_parties" ("AimsRiskTreatmentPlan_aims_id");
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_plan_responsible_parties_aims_plan_responsible_parties" ON "AimsRiskTreatmentPlan_aims_plan_responsible_parties" (aims_plan_responsible_parties);

CREATE TABLE "AimsRiskTreatmentPlan_aims_document_distribution" (
	"AimsRiskTreatmentPlan_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsRiskTreatmentPlan_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsRiskTreatmentPlan_aims_id") REFERENCES "AimsRiskTreatmentPlan" (aims_id)
);
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_document_distribution_AimsRiskTreatmentPlan_aims_id" ON "AimsRiskTreatmentPlan_aims_document_distribution" ("AimsRiskTreatmentPlan_aims_id");
CREATE INDEX "ix_AimsRiskTreatmentPlan_aims_document_distribution_aims_document_distribution" ON "AimsRiskTreatmentPlan_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsImpactAssessment_aims_impact_jurisdictions" (
	"AimsImpactAssessment_aims_id" TEXT,
	aims_impact_jurisdictions TEXT,
	PRIMARY KEY ("AimsImpactAssessment_aims_id", aims_impact_jurisdictions),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_jurisdictions_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment_aims_impact_jurisdictions" ("AimsImpactAssessment_aims_id");
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_jurisdictions_aims_impact_jurisdictions" ON "AimsImpactAssessment_aims_impact_jurisdictions" (aims_impact_jurisdictions);

CREATE TABLE "AimsImpactAssessment_aims_impact_demographic_groups" (
	"AimsImpactAssessment_aims_id" TEXT,
	aims_impact_demographic_groups TEXT,
	PRIMARY KEY ("AimsImpactAssessment_aims_id", aims_impact_demographic_groups),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_demographic_groups_aims_impact_demographic_groups" ON "AimsImpactAssessment_aims_impact_demographic_groups" (aims_impact_demographic_groups);
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_demographic_groups_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment_aims_impact_demographic_groups" ("AimsImpactAssessment_aims_id");

CREATE TABLE "AimsImpactAssessment_aims_impact_failures" (
	"AimsImpactAssessment_aims_id" TEXT,
	aims_impact_failures TEXT,
	PRIMARY KEY ("AimsImpactAssessment_aims_id", aims_impact_failures),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_failures_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment_aims_impact_failures" ("AimsImpactAssessment_aims_id");
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_failures_aims_impact_failures" ON "AimsImpactAssessment_aims_impact_failures" (aims_impact_failures);

CREATE TABLE "AimsImpactAssessment_aims_impact_shared_with" (
	"AimsImpactAssessment_aims_id" TEXT,
	aims_impact_shared_with_aims_id TEXT,
	PRIMARY KEY ("AimsImpactAssessment_aims_id", aims_impact_shared_with_aims_id),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id),
	FOREIGN KEY(aims_impact_shared_with_aims_id) REFERENCES "AimsInterestedParty" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_shared_with_aims_impact_shared_with_aims_id" ON "AimsImpactAssessment_aims_impact_shared_with" (aims_impact_shared_with_aims_id);
CREATE INDEX "ix_AimsImpactAssessment_aims_impact_shared_with_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment_aims_impact_shared_with" ("AimsImpactAssessment_aims_id");

CREATE TABLE "AimsImpactAssessment_aims_document_distribution" (
	"AimsImpactAssessment_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsImpactAssessment_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_document_distribution_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment_aims_document_distribution" ("AimsImpactAssessment_aims_id");
CREATE INDEX "ix_AimsImpactAssessment_aims_document_distribution_aims_document_distribution" ON "AimsImpactAssessment_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsControl_aims_relevant_controls" (
	"AimsControl_aims_id" TEXT,
	aims_relevant_controls_aims_id TEXT,
	PRIMARY KEY ("AimsControl_aims_id", aims_relevant_controls_aims_id),
	FOREIGN KEY("AimsControl_aims_id") REFERENCES "AimsControl" (aims_id),
	FOREIGN KEY(aims_relevant_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_relevant_controls_aims_relevant_controls_aims_id" ON "AimsControl_aims_relevant_controls" (aims_relevant_controls_aims_id);
CREATE INDEX "ix_AimsControl_aims_relevant_controls_AimsControl_aims_id" ON "AimsControl_aims_relevant_controls" ("AimsControl_aims_id");

CREATE TABLE "AimsControl_aims_cited_annex_a_controls" (
	"AimsControl_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsControl_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsControl_aims_id") REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_cited_annex_a_controls_AimsControl_aims_id" ON "AimsControl_aims_cited_annex_a_controls" ("AimsControl_aims_id");
CREATE INDEX "ix_AimsControl_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsControl_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);

CREATE TABLE "AimsControl_aims_objective_categories" (
	"AimsControl_aims_id" TEXT,
	aims_objective_categories VARCHAR(31),
	PRIMARY KEY ("AimsControl_aims_id", aims_objective_categories),
	FOREIGN KEY("AimsControl_aims_id") REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_objective_categories_AimsControl_aims_id" ON "AimsControl_aims_objective_categories" ("AimsControl_aims_id");
CREATE INDEX "ix_AimsControl_aims_objective_categories_aims_objective_categories" ON "AimsControl_aims_objective_categories" (aims_objective_categories);

CREATE TABLE "AimsControl_aims_risk_source_categories" (
	"AimsControl_aims_id" TEXT,
	aims_risk_source_categories VARCHAR(20),
	PRIMARY KEY ("AimsControl_aims_id", aims_risk_source_categories),
	FOREIGN KEY("AimsControl_aims_id") REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_risk_source_categories_aims_risk_source_categories" ON "AimsControl_aims_risk_source_categories" (aims_risk_source_categories);
CREATE INDEX "ix_AimsControl_aims_risk_source_categories_AimsControl_aims_id" ON "AimsControl_aims_risk_source_categories" ("AimsControl_aims_id");

CREATE TABLE "AimsControl_aims_control_evidence" (
	"AimsControl_aims_id" TEXT,
	aims_control_evidence TEXT,
	PRIMARY KEY ("AimsControl_aims_id", aims_control_evidence),
	FOREIGN KEY("AimsControl_aims_id") REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_control_evidence_aims_control_evidence" ON "AimsControl_aims_control_evidence" (aims_control_evidence);
CREATE INDEX "ix_AimsControl_aims_control_evidence_AimsControl_aims_id" ON "AimsControl_aims_control_evidence" ("AimsControl_aims_id");

CREATE TABLE "AimsSystemResource_aims_life_cycle_stages" (
	"AimsSystemResource_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsSystemResource_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsSystemResource_aims_id") REFERENCES "AimsSystemResource" (aims_id)
);
CREATE INDEX "ix_AimsSystemResource_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsSystemResource_aims_life_cycle_stages" (aims_life_cycle_stages);
CREATE INDEX "ix_AimsSystemResource_aims_life_cycle_stages_AimsSystemResource_aims_id" ON "AimsSystemResource_aims_life_cycle_stages" ("AimsSystemResource_aims_id");

CREATE TABLE "AimsHumanResource_aims_human_competences" (
	"AimsHumanResource_aims_id" TEXT,
	aims_human_competences TEXT,
	PRIMARY KEY ("AimsHumanResource_aims_id", aims_human_competences),
	FOREIGN KEY("AimsHumanResource_aims_id") REFERENCES "AimsHumanResource" (aims_id)
);
CREATE INDEX "ix_AimsHumanResource_aims_human_competences_aims_human_competences" ON "AimsHumanResource_aims_human_competences" (aims_human_competences);
CREATE INDEX "ix_AimsHumanResource_aims_human_competences_AimsHumanResource_aims_id" ON "AimsHumanResource_aims_human_competences" ("AimsHumanResource_aims_id");

CREATE TABLE "AimsHumanResource_aims_human_activities" (
	"AimsHumanResource_aims_id" TEXT,
	aims_human_activities TEXT,
	PRIMARY KEY ("AimsHumanResource_aims_id", aims_human_activities),
	FOREIGN KEY("AimsHumanResource_aims_id") REFERENCES "AimsHumanResource" (aims_id)
);
CREATE INDEX "ix_AimsHumanResource_aims_human_activities_AimsHumanResource_aims_id" ON "AimsHumanResource_aims_human_activities" ("AimsHumanResource_aims_id");
CREATE INDEX "ix_AimsHumanResource_aims_human_activities_aims_human_activities" ON "AimsHumanResource_aims_human_activities" (aims_human_activities);

CREATE TABLE "AimsHumanResource_aims_life_cycle_stages" (
	"AimsHumanResource_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsHumanResource_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsHumanResource_aims_id") REFERENCES "AimsHumanResource" (aims_id)
);
CREATE INDEX "ix_AimsHumanResource_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsHumanResource_aims_life_cycle_stages" (aims_life_cycle_stages);
CREATE INDEX "ix_AimsHumanResource_aims_life_cycle_stages_AimsHumanResource_aims_id" ON "AimsHumanResource_aims_life_cycle_stages" ("AimsHumanResource_aims_id");

CREATE TABLE "AimsDevelopmentProcess_aims_development_impact_assessment_stages" (
	"AimsDevelopmentProcess_aims_id" TEXT,
	aims_development_impact_assessment_stages VARCHAR(27),
	PRIMARY KEY ("AimsDevelopmentProcess_aims_id", aims_development_impact_assessment_stages),
	FOREIGN KEY("AimsDevelopmentProcess_aims_id") REFERENCES "AimsDevelopmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_development_impact_assessment_stages_aims_development_impact_assessment_stages" ON "AimsDevelopmentProcess_aims_development_impact_assessment_stages" (aims_development_impact_assessment_stages);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_development_impact_assessment_stages_AimsDevelopmentProcess_aims_id" ON "AimsDevelopmentProcess_aims_development_impact_assessment_stages" ("AimsDevelopmentProcess_aims_id");

CREATE TABLE "AimsDevelopmentProcess_aims_development_release_criteria" (
	"AimsDevelopmentProcess_aims_id" TEXT,
	aims_development_release_criteria TEXT,
	PRIMARY KEY ("AimsDevelopmentProcess_aims_id", aims_development_release_criteria),
	FOREIGN KEY("AimsDevelopmentProcess_aims_id") REFERENCES "AimsDevelopmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_development_release_criteria_aims_development_release_criteria" ON "AimsDevelopmentProcess_aims_development_release_criteria" (aims_development_release_criteria);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_development_release_criteria_AimsDevelopmentProcess_aims_id" ON "AimsDevelopmentProcess_aims_development_release_criteria" ("AimsDevelopmentProcess_aims_id");

CREATE TABLE "AimsDevelopmentProcess_aims_development_approvals" (
	"AimsDevelopmentProcess_aims_id" TEXT,
	aims_development_approvals TEXT,
	PRIMARY KEY ("AimsDevelopmentProcess_aims_id", aims_development_approvals),
	FOREIGN KEY("AimsDevelopmentProcess_aims_id") REFERENCES "AimsDevelopmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_development_approvals_aims_development_approvals" ON "AimsDevelopmentProcess_aims_development_approvals" (aims_development_approvals);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_development_approvals_AimsDevelopmentProcess_aims_id" ON "AimsDevelopmentProcess_aims_development_approvals" ("AimsDevelopmentProcess_aims_id");

CREATE TABLE "AimsDevelopmentProcess_aims_document_distribution" (
	"AimsDevelopmentProcess_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsDevelopmentProcess_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsDevelopmentProcess_aims_id") REFERENCES "AimsDevelopmentProcess" (aims_id)
);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_document_distribution_AimsDevelopmentProcess_aims_id" ON "AimsDevelopmentProcess_aims_document_distribution" ("AimsDevelopmentProcess_aims_id");
CREATE INDEX "ix_AimsDevelopmentProcess_aims_document_distribution_aims_document_distribution" ON "AimsDevelopmentProcess_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsResponsibleUseProcess_aims_use_approvals" (
	"AimsResponsibleUseProcess_aims_id" TEXT,
	aims_use_approvals TEXT,
	PRIMARY KEY ("AimsResponsibleUseProcess_aims_id", aims_use_approvals),
	FOREIGN KEY("AimsResponsibleUseProcess_aims_id") REFERENCES "AimsResponsibleUseProcess" (aims_id)
);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_use_approvals_aims_use_approvals" ON "AimsResponsibleUseProcess_aims_use_approvals" (aims_use_approvals);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_use_approvals_AimsResponsibleUseProcess_aims_id" ON "AimsResponsibleUseProcess_aims_use_approvals" ("AimsResponsibleUseProcess_aims_id");

CREATE TABLE "AimsResponsibleUseProcess_aims_use_sourcing_requirements" (
	"AimsResponsibleUseProcess_aims_id" TEXT,
	aims_use_sourcing_requirements TEXT,
	PRIMARY KEY ("AimsResponsibleUseProcess_aims_id", aims_use_sourcing_requirements),
	FOREIGN KEY("AimsResponsibleUseProcess_aims_id") REFERENCES "AimsResponsibleUseProcess" (aims_id)
);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_use_sourcing_requirements_aims_use_sourcing_requirements" ON "AimsResponsibleUseProcess_aims_use_sourcing_requirements" (aims_use_sourcing_requirements);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_use_sourcing_requirements_AimsResponsibleUseProcess_aims_id" ON "AimsResponsibleUseProcess_aims_use_sourcing_requirements" ("AimsResponsibleUseProcess_aims_id");

CREATE TABLE "AimsResponsibleUseProcess_aims_use_legal_requirements" (
	"AimsResponsibleUseProcess_aims_id" TEXT,
	aims_use_legal_requirements TEXT,
	PRIMARY KEY ("AimsResponsibleUseProcess_aims_id", aims_use_legal_requirements),
	FOREIGN KEY("AimsResponsibleUseProcess_aims_id") REFERENCES "AimsResponsibleUseProcess" (aims_id)
);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_use_legal_requirements_AimsResponsibleUseProcess_aims_id" ON "AimsResponsibleUseProcess_aims_use_legal_requirements" ("AimsResponsibleUseProcess_aims_id");
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_use_legal_requirements_aims_use_legal_requirements" ON "AimsResponsibleUseProcess_aims_use_legal_requirements" (aims_use_legal_requirements);

CREATE TABLE "AimsResponsibleUseProcess_aims_document_distribution" (
	"AimsResponsibleUseProcess_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsResponsibleUseProcess_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsResponsibleUseProcess_aims_id") REFERENCES "AimsResponsibleUseProcess" (aims_id)
);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_document_distribution_aims_document_distribution" ON "AimsResponsibleUseProcess_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_document_distribution_AimsResponsibleUseProcess_aims_id" ON "AimsResponsibleUseProcess_aims_document_distribution" ("AimsResponsibleUseProcess_aims_id");

CREATE TABLE "AimsTechnicalDocumentation_aims_technical_doc_audiences" (
	"AimsTechnicalDocumentation_aims_id" TEXT,
	aims_technical_doc_audiences TEXT,
	PRIMARY KEY ("AimsTechnicalDocumentation_aims_id", aims_technical_doc_audiences),
	FOREIGN KEY("AimsTechnicalDocumentation_aims_id") REFERENCES "AimsTechnicalDocumentation" (aims_id)
);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_technical_doc_audiences_aims_technical_doc_audiences" ON "AimsTechnicalDocumentation_aims_technical_doc_audiences" (aims_technical_doc_audiences);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_technical_doc_audiences_AimsTechnicalDocumentation_aims_id" ON "AimsTechnicalDocumentation_aims_technical_doc_audiences" ("AimsTechnicalDocumentation_aims_id");

CREATE TABLE "AimsTechnicalDocumentation_aims_technical_doc_contents" (
	"AimsTechnicalDocumentation_aims_id" TEXT,
	aims_technical_doc_contents TEXT,
	PRIMARY KEY ("AimsTechnicalDocumentation_aims_id", aims_technical_doc_contents),
	FOREIGN KEY("AimsTechnicalDocumentation_aims_id") REFERENCES "AimsTechnicalDocumentation" (aims_id)
);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_technical_doc_contents_aims_technical_doc_contents" ON "AimsTechnicalDocumentation_aims_technical_doc_contents" (aims_technical_doc_contents);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_technical_doc_contents_AimsTechnicalDocumentation_aims_id" ON "AimsTechnicalDocumentation_aims_technical_doc_contents" ("AimsTechnicalDocumentation_aims_id");

CREATE TABLE "AimsTechnicalDocumentation_aims_document_distribution" (
	"AimsTechnicalDocumentation_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsTechnicalDocumentation_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsTechnicalDocumentation_aims_id") REFERENCES "AimsTechnicalDocumentation" (aims_id)
);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_document_distribution_AimsTechnicalDocumentation_aims_id" ON "AimsTechnicalDocumentation_aims_document_distribution" ("AimsTechnicalDocumentation_aims_id");
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_document_distribution_aims_document_distribution" ON "AimsTechnicalDocumentation_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsUserInformation_aims_user_information_contents" (
	"AimsUserInformation_aims_id" TEXT,
	aims_user_information_contents TEXT,
	PRIMARY KEY ("AimsUserInformation_aims_id", aims_user_information_contents),
	FOREIGN KEY("AimsUserInformation_aims_id") REFERENCES "AimsUserInformation" (aims_id)
);
CREATE INDEX "ix_AimsUserInformation_aims_user_information_contents_aims_user_information_contents" ON "AimsUserInformation_aims_user_information_contents" (aims_user_information_contents);
CREATE INDEX "ix_AimsUserInformation_aims_user_information_contents_AimsUserInformation_aims_id" ON "AimsUserInformation_aims_user_information_contents" ("AimsUserInformation_aims_id");

CREATE TABLE "AimsUserInformation_aims_user_information_channels" (
	"AimsUserInformation_aims_id" TEXT,
	aims_user_information_channels TEXT,
	PRIMARY KEY ("AimsUserInformation_aims_id", aims_user_information_channels),
	FOREIGN KEY("AimsUserInformation_aims_id") REFERENCES "AimsUserInformation" (aims_id)
);
CREATE INDEX "ix_AimsUserInformation_aims_user_information_channels_AimsUserInformation_aims_id" ON "AimsUserInformation_aims_user_information_channels" ("AimsUserInformation_aims_id");
CREATE INDEX "ix_AimsUserInformation_aims_user_information_channels_aims_user_information_channels" ON "AimsUserInformation_aims_user_information_channels" (aims_user_information_channels);

CREATE TABLE "AimsUserInformation_aims_user_information_criteria" (
	"AimsUserInformation_aims_id" TEXT,
	aims_user_information_criteria TEXT,
	PRIMARY KEY ("AimsUserInformation_aims_id", aims_user_information_criteria),
	FOREIGN KEY("AimsUserInformation_aims_id") REFERENCES "AimsUserInformation" (aims_id)
);
CREATE INDEX "ix_AimsUserInformation_aims_user_information_criteria_AimsUserInformation_aims_id" ON "AimsUserInformation_aims_user_information_criteria" ("AimsUserInformation_aims_id");
CREATE INDEX "ix_AimsUserInformation_aims_user_information_criteria_aims_user_information_criteria" ON "AimsUserInformation_aims_user_information_criteria" (aims_user_information_criteria);

CREATE TABLE "AimsUserInformation_aims_document_distribution" (
	"AimsUserInformation_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsUserInformation_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsUserInformation_aims_id") REFERENCES "AimsUserInformation" (aims_id)
);
CREATE INDEX "ix_AimsUserInformation_aims_document_distribution_AimsUserInformation_aims_id" ON "AimsUserInformation_aims_document_distribution" ("AimsUserInformation_aims_id");
CREATE INDEX "ix_AimsUserInformation_aims_document_distribution_aims_document_distribution" ON "AimsUserInformation_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsIncidentCommunicationPlan_aims_incident_plan_categories" (
	"AimsIncidentCommunicationPlan_aims_id" TEXT,
	aims_incident_plan_categories VARCHAR(20),
	PRIMARY KEY ("AimsIncidentCommunicationPlan_aims_id", aims_incident_plan_categories),
	FOREIGN KEY("AimsIncidentCommunicationPlan_aims_id") REFERENCES "AimsIncidentCommunicationPlan" (aims_id)
);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_incident_plan_categories_aims_incident_plan_categories" ON "AimsIncidentCommunicationPlan_aims_incident_plan_categories" (aims_incident_plan_categories);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_incident_plan_categories_AimsIncidentCommunicationPlan_aims_id" ON "AimsIncidentCommunicationPlan_aims_incident_plan_categories" ("AimsIncidentCommunicationPlan_aims_id");

CREATE TABLE "AimsIncidentCommunicationPlan_aims_incident_plan_authorities" (
	"AimsIncidentCommunicationPlan_aims_id" TEXT,
	aims_incident_plan_authorities TEXT,
	PRIMARY KEY ("AimsIncidentCommunicationPlan_aims_id", aims_incident_plan_authorities),
	FOREIGN KEY("AimsIncidentCommunicationPlan_aims_id") REFERENCES "AimsIncidentCommunicationPlan" (aims_id)
);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_incident_plan_authorities_aims_incident_plan_authorities" ON "AimsIncidentCommunicationPlan_aims_incident_plan_authorities" (aims_incident_plan_authorities);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_incident_plan_authorities_AimsIncidentCommunicationPlan_aims_id" ON "AimsIncidentCommunicationPlan_aims_incident_plan_authorities" ("AimsIncidentCommunicationPlan_aims_id");

CREATE TABLE "AimsIncidentCommunicationPlan_aims_incident_plan_details" (
	"AimsIncidentCommunicationPlan_aims_id" TEXT,
	aims_incident_plan_details TEXT,
	PRIMARY KEY ("AimsIncidentCommunicationPlan_aims_id", aims_incident_plan_details),
	FOREIGN KEY("AimsIncidentCommunicationPlan_aims_id") REFERENCES "AimsIncidentCommunicationPlan" (aims_id)
);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_incident_plan_details_AimsIncidentCommunicationPlan_aims_id" ON "AimsIncidentCommunicationPlan_aims_incident_plan_details" ("AimsIncidentCommunicationPlan_aims_id");
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_incident_plan_details_aims_incident_plan_details" ON "AimsIncidentCommunicationPlan_aims_incident_plan_details" (aims_incident_plan_details);

CREATE TABLE "AimsIncidentCommunicationPlan_aims_document_distribution" (
	"AimsIncidentCommunicationPlan_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsIncidentCommunicationPlan_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsIncidentCommunicationPlan_aims_id") REFERENCES "AimsIncidentCommunicationPlan" (aims_id)
);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_document_distribution_aims_document_distribution" ON "AimsIncidentCommunicationPlan_aims_document_distribution" (aims_document_distribution);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_document_distribution_AimsIncidentCommunicationPlan_aims_id" ON "AimsIncidentCommunicationPlan_aims_document_distribution" ("AimsIncidentCommunicationPlan_aims_id");

CREATE TABLE "AimsReportingObligation_aims_obligation_parties" (
	"AimsReportingObligation_aims_id" TEXT,
	aims_obligation_parties_aims_id TEXT,
	PRIMARY KEY ("AimsReportingObligation_aims_id", aims_obligation_parties_aims_id),
	FOREIGN KEY("AimsReportingObligation_aims_id") REFERENCES "AimsReportingObligation" (aims_id),
	FOREIGN KEY(aims_obligation_parties_aims_id) REFERENCES "AimsInterestedParty" (aims_id)
);
CREATE INDEX "ix_AimsReportingObligation_aims_obligation_parties_AimsReportingObligation_aims_id" ON "AimsReportingObligation_aims_obligation_parties" ("AimsReportingObligation_aims_id");
CREATE INDEX "ix_AimsReportingObligation_aims_obligation_parties_aims_obligation_parties_aims_id" ON "AimsReportingObligation_aims_obligation_parties" (aims_obligation_parties_aims_id);

CREATE TABLE "AimsReportingObligation_aims_obligation_contents" (
	"AimsReportingObligation_aims_id" TEXT,
	aims_obligation_contents TEXT,
	PRIMARY KEY ("AimsReportingObligation_aims_id", aims_obligation_contents),
	FOREIGN KEY("AimsReportingObligation_aims_id") REFERENCES "AimsReportingObligation" (aims_id)
);
CREATE INDEX "ix_AimsReportingObligation_aims_obligation_contents_aims_obligation_contents" ON "AimsReportingObligation_aims_obligation_contents" (aims_obligation_contents);
CREATE INDEX "ix_AimsReportingObligation_aims_obligation_contents_AimsReportingObligation_aims_id" ON "AimsReportingObligation_aims_obligation_contents" ("AimsReportingObligation_aims_id");

CREATE TABLE "AimsCompetenceRecord_aims_competence_required" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_competence_required TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_competence_required),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_required_aims_competence_required" ON "AimsCompetenceRecord_aims_competence_required" (aims_competence_required);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_required_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_competence_required" ("AimsCompetenceRecord_aims_id");

CREATE TABLE "AimsCompetenceRecord_aims_competence_education" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_competence_education TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_competence_education),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_education_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_competence_education" ("AimsCompetenceRecord_aims_id");
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_education_aims_competence_education" ON "AimsCompetenceRecord_aims_competence_education" (aims_competence_education);

CREATE TABLE "AimsCompetenceRecord_aims_competence_training" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_competence_training TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_competence_training),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_training_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_competence_training" ("AimsCompetenceRecord_aims_id");
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_training_aims_competence_training" ON "AimsCompetenceRecord_aims_competence_training" (aims_competence_training);

CREATE TABLE "AimsCompetenceRecord_aims_competence_experience" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_competence_experience TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_competence_experience),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_experience_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_competence_experience" ("AimsCompetenceRecord_aims_id");
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_experience_aims_competence_experience" ON "AimsCompetenceRecord_aims_competence_experience" (aims_competence_experience);

CREATE TABLE "AimsCompetenceRecord_aims_competence_gaps" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_competence_gaps TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_competence_gaps),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_gaps_aims_competence_gaps" ON "AimsCompetenceRecord_aims_competence_gaps" (aims_competence_gaps);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_gaps_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_competence_gaps" ("AimsCompetenceRecord_aims_id");

CREATE TABLE "AimsCompetenceRecord_aims_competence_actions" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_competence_actions TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_competence_actions),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_actions_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_competence_actions" ("AimsCompetenceRecord_aims_id");
CREATE INDEX "ix_AimsCompetenceRecord_aims_competence_actions_aims_competence_actions" ON "AimsCompetenceRecord_aims_competence_actions" (aims_competence_actions);

CREATE TABLE "AimsCompetenceRecord_aims_document_distribution" (
	"AimsCompetenceRecord_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsCompetenceRecord_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsCompetenceRecord_aims_id") REFERENCES "AimsCompetenceRecord" (aims_id)
);
CREATE INDEX "ix_AimsCompetenceRecord_aims_document_distribution_AimsCompetenceRecord_aims_id" ON "AimsCompetenceRecord_aims_document_distribution" ("AimsCompetenceRecord_aims_id");
CREATE INDEX "ix_AimsCompetenceRecord_aims_document_distribution_aims_document_distribution" ON "AimsCompetenceRecord_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsDocumentedInformation_aims_cited_clauses" (
	"AimsDocumentedInformation_aims_id" TEXT,
	aims_cited_clauses VARCHAR(12),
	PRIMARY KEY ("AimsDocumentedInformation_aims_id", aims_cited_clauses),
	FOREIGN KEY("AimsDocumentedInformation_aims_id") REFERENCES "AimsDocumentedInformation" (aims_id)
);
CREATE INDEX "ix_AimsDocumentedInformation_aims_cited_clauses_AimsDocumentedInformation_aims_id" ON "AimsDocumentedInformation_aims_cited_clauses" ("AimsDocumentedInformation_aims_id");
CREATE INDEX "ix_AimsDocumentedInformation_aims_cited_clauses_aims_cited_clauses" ON "AimsDocumentedInformation_aims_cited_clauses" (aims_cited_clauses);

CREATE TABLE "AimsDocumentedInformation_aims_cited_annex_a_controls" (
	"AimsDocumentedInformation_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsDocumentedInformation_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsDocumentedInformation_aims_id") REFERENCES "AimsDocumentedInformation" (aims_id)
);
CREATE INDEX "ix_AimsDocumentedInformation_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsDocumentedInformation_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);
CREATE INDEX "ix_AimsDocumentedInformation_aims_cited_annex_a_controls_AimsDocumentedInformation_aims_id" ON "AimsDocumentedInformation_aims_cited_annex_a_controls" ("AimsDocumentedInformation_aims_id");

CREATE TABLE "AimsDocumentedInformation_aims_document_distribution" (
	"AimsDocumentedInformation_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsDocumentedInformation_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsDocumentedInformation_aims_id") REFERENCES "AimsDocumentedInformation" (aims_id)
);
CREATE INDEX "ix_AimsDocumentedInformation_aims_document_distribution_AimsDocumentedInformation_aims_id" ON "AimsDocumentedInformation_aims_document_distribution" ("AimsDocumentedInformation_aims_id");
CREATE INDEX "ix_AimsDocumentedInformation_aims_document_distribution_aims_document_distribution" ON "AimsDocumentedInformation_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsOperationalProcedure_aims_relevant_controls" (
	"AimsOperationalProcedure_aims_id" TEXT,
	aims_relevant_controls_aims_id TEXT,
	PRIMARY KEY ("AimsOperationalProcedure_aims_id", aims_relevant_controls_aims_id),
	FOREIGN KEY("AimsOperationalProcedure_aims_id") REFERENCES "AimsOperationalProcedure" (aims_id),
	FOREIGN KEY(aims_relevant_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsOperationalProcedure_aims_relevant_controls_aims_relevant_controls_aims_id" ON "AimsOperationalProcedure_aims_relevant_controls" (aims_relevant_controls_aims_id);
CREATE INDEX "ix_AimsOperationalProcedure_aims_relevant_controls_AimsOperationalProcedure_aims_id" ON "AimsOperationalProcedure_aims_relevant_controls" ("AimsOperationalProcedure_aims_id");

CREATE TABLE "AimsOperationalProcedure_aims_cited_annex_a_controls" (
	"AimsOperationalProcedure_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsOperationalProcedure_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsOperationalProcedure_aims_id") REFERENCES "AimsOperationalProcedure" (aims_id)
);
CREATE INDEX "ix_AimsOperationalProcedure_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsOperationalProcedure_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);
CREATE INDEX "ix_AimsOperationalProcedure_aims_cited_annex_a_controls_AimsOperationalProcedure_aims_id" ON "AimsOperationalProcedure_aims_cited_annex_a_controls" ("AimsOperationalProcedure_aims_id");

CREATE TABLE "AimsOperationalProcedure_aims_procedure_control_measures" (
	"AimsOperationalProcedure_aims_id" TEXT,
	aims_procedure_control_measures TEXT,
	PRIMARY KEY ("AimsOperationalProcedure_aims_id", aims_procedure_control_measures),
	FOREIGN KEY("AimsOperationalProcedure_aims_id") REFERENCES "AimsOperationalProcedure" (aims_id)
);
CREATE INDEX "ix_AimsOperationalProcedure_aims_procedure_control_measures_aims_procedure_control_measures" ON "AimsOperationalProcedure_aims_procedure_control_measures" (aims_procedure_control_measures);
CREATE INDEX "ix_AimsOperationalProcedure_aims_procedure_control_measures_AimsOperationalProcedure_aims_id" ON "AimsOperationalProcedure_aims_procedure_control_measures" ("AimsOperationalProcedure_aims_id");

CREATE TABLE "AimsOperationalProcedure_aims_procedure_roles" (
	"AimsOperationalProcedure_aims_id" TEXT,
	aims_procedure_roles_aims_id TEXT,
	PRIMARY KEY ("AimsOperationalProcedure_aims_id", aims_procedure_roles_aims_id),
	FOREIGN KEY("AimsOperationalProcedure_aims_id") REFERENCES "AimsOperationalProcedure" (aims_id),
	FOREIGN KEY(aims_procedure_roles_aims_id) REFERENCES "AimsRole" (aims_id)
);
CREATE INDEX "ix_AimsOperationalProcedure_aims_procedure_roles_AimsOperationalProcedure_aims_id" ON "AimsOperationalProcedure_aims_procedure_roles" ("AimsOperationalProcedure_aims_id");
CREATE INDEX "ix_AimsOperationalProcedure_aims_procedure_roles_aims_procedure_roles_aims_id" ON "AimsOperationalProcedure_aims_procedure_roles" (aims_procedure_roles_aims_id);

CREATE TABLE "AimsOperationalProcedure_aims_document_distribution" (
	"AimsOperationalProcedure_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsOperationalProcedure_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsOperationalProcedure_aims_id") REFERENCES "AimsOperationalProcedure" (aims_id)
);
CREATE INDEX "ix_AimsOperationalProcedure_aims_document_distribution_AimsOperationalProcedure_aims_id" ON "AimsOperationalProcedure_aims_document_distribution" ("AimsOperationalProcedure_aims_id");
CREATE INDEX "ix_AimsOperationalProcedure_aims_document_distribution_aims_document_distribution" ON "AimsOperationalProcedure_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsAuditProgramme_aims_programme_responsibilities" (
	"AimsAuditProgramme_aims_id" TEXT,
	aims_programme_responsibilities TEXT,
	PRIMARY KEY ("AimsAuditProgramme_aims_id", aims_programme_responsibilities),
	FOREIGN KEY("AimsAuditProgramme_aims_id") REFERENCES "AimsAuditProgramme" (aims_id)
);
CREATE INDEX "ix_AimsAuditProgramme_aims_programme_responsibilities_AimsAuditProgramme_aims_id" ON "AimsAuditProgramme_aims_programme_responsibilities" ("AimsAuditProgramme_aims_id");
CREATE INDEX "ix_AimsAuditProgramme_aims_programme_responsibilities_aims_programme_responsibilities" ON "AimsAuditProgramme_aims_programme_responsibilities" (aims_programme_responsibilities);

CREATE TABLE "AimsAuditProgramme_aims_document_distribution" (
	"AimsAuditProgramme_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsAuditProgramme_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsAuditProgramme_aims_id") REFERENCES "AimsAuditProgramme" (aims_id)
);
CREATE INDEX "ix_AimsAuditProgramme_aims_document_distribution_AimsAuditProgramme_aims_id" ON "AimsAuditProgramme_aims_document_distribution" ("AimsAuditProgramme_aims_id");
CREATE INDEX "ix_AimsAuditProgramme_aims_document_distribution_aims_document_distribution" ON "AimsAuditProgramme_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsManagementReview_aims_review_attendees" (
	"AimsManagementReview_aims_id" TEXT,
	aims_review_attendees TEXT,
	PRIMARY KEY ("AimsManagementReview_aims_id", aims_review_attendees),
	FOREIGN KEY("AimsManagementReview_aims_id") REFERENCES "AimsManagementReview" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_review_attendees_aims_review_attendees" ON "AimsManagementReview_aims_review_attendees" (aims_review_attendees);
CREATE INDEX "ix_AimsManagementReview_aims_review_attendees_AimsManagementReview_aims_id" ON "AimsManagementReview_aims_review_attendees" ("AimsManagementReview_aims_id");

CREATE TABLE "AimsManagementReview_aims_review_improvement_opportunities" (
	"AimsManagementReview_aims_id" TEXT,
	aims_review_improvement_opportunities TEXT,
	PRIMARY KEY ("AimsManagementReview_aims_id", aims_review_improvement_opportunities),
	FOREIGN KEY("AimsManagementReview_aims_id") REFERENCES "AimsManagementReview" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_review_improvement_opportunities_AimsManagementReview_aims_id" ON "AimsManagementReview_aims_review_improvement_opportunities" ("AimsManagementReview_aims_id");
CREATE INDEX "ix_AimsManagementReview_aims_review_improvement_opportunities_aims_review_improvement_opportunities" ON "AimsManagementReview_aims_review_improvement_opportunities" (aims_review_improvement_opportunities);

CREATE TABLE "AimsManagementReview_aims_review_decisions" (
	"AimsManagementReview_aims_id" TEXT,
	aims_review_decisions TEXT,
	PRIMARY KEY ("AimsManagementReview_aims_id", aims_review_decisions),
	FOREIGN KEY("AimsManagementReview_aims_id") REFERENCES "AimsManagementReview" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_review_decisions_aims_review_decisions" ON "AimsManagementReview_aims_review_decisions" (aims_review_decisions);
CREATE INDEX "ix_AimsManagementReview_aims_review_decisions_AimsManagementReview_aims_id" ON "AimsManagementReview_aims_review_decisions" ("AimsManagementReview_aims_id");

CREATE TABLE "AimsManagementReview_aims_review_system_changes" (
	"AimsManagementReview_aims_id" TEXT,
	aims_review_system_changes TEXT,
	PRIMARY KEY ("AimsManagementReview_aims_id", aims_review_system_changes),
	FOREIGN KEY("AimsManagementReview_aims_id") REFERENCES "AimsManagementReview" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_review_system_changes_AimsManagementReview_aims_id" ON "AimsManagementReview_aims_review_system_changes" ("AimsManagementReview_aims_id");
CREATE INDEX "ix_AimsManagementReview_aims_review_system_changes_aims_review_system_changes" ON "AimsManagementReview_aims_review_system_changes" (aims_review_system_changes);

CREATE TABLE "AimsManagementReview_aims_review_actions" (
	"AimsManagementReview_aims_id" TEXT,
	aims_review_actions TEXT,
	PRIMARY KEY ("AimsManagementReview_aims_id", aims_review_actions),
	FOREIGN KEY("AimsManagementReview_aims_id") REFERENCES "AimsManagementReview" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_review_actions_AimsManagementReview_aims_id" ON "AimsManagementReview_aims_review_actions" ("AimsManagementReview_aims_id");
CREATE INDEX "ix_AimsManagementReview_aims_review_actions_aims_review_actions" ON "AimsManagementReview_aims_review_actions" (aims_review_actions);

CREATE TABLE "AimsManagementReview_aims_document_distribution" (
	"AimsManagementReview_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsManagementReview_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsManagementReview_aims_id") REFERENCES "AimsManagementReview" (aims_id)
);
CREATE INDEX "ix_AimsManagementReview_aims_document_distribution_AimsManagementReview_aims_id" ON "AimsManagementReview_aims_document_distribution" ("AimsManagementReview_aims_id");
CREATE INDEX "ix_AimsManagementReview_aims_document_distribution_aims_document_distribution" ON "AimsManagementReview_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsNonconformity_aims_cited_clauses" (
	"AimsNonconformity_aims_id" TEXT,
	aims_cited_clauses VARCHAR(12),
	PRIMARY KEY ("AimsNonconformity_aims_id", aims_cited_clauses),
	FOREIGN KEY("AimsNonconformity_aims_id") REFERENCES "AimsNonconformity" (aims_id)
);
CREATE INDEX "ix_AimsNonconformity_aims_cited_clauses_aims_cited_clauses" ON "AimsNonconformity_aims_cited_clauses" (aims_cited_clauses);
CREATE INDEX "ix_AimsNonconformity_aims_cited_clauses_AimsNonconformity_aims_id" ON "AimsNonconformity_aims_cited_clauses" ("AimsNonconformity_aims_id");

CREATE TABLE "AimsNonconformity_aims_cited_annex_a_controls" (
	"AimsNonconformity_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsNonconformity_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsNonconformity_aims_id") REFERENCES "AimsNonconformity" (aims_id)
);
CREATE INDEX "ix_AimsNonconformity_aims_cited_annex_a_controls_AimsNonconformity_aims_id" ON "AimsNonconformity_aims_cited_annex_a_controls" ("AimsNonconformity_aims_id");
CREATE INDEX "ix_AimsNonconformity_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsNonconformity_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);

CREATE TABLE "AimsNonconformity_aims_nonconformity_immediate_actions" (
	"AimsNonconformity_aims_id" TEXT,
	aims_nonconformity_immediate_actions TEXT,
	PRIMARY KEY ("AimsNonconformity_aims_id", aims_nonconformity_immediate_actions),
	FOREIGN KEY("AimsNonconformity_aims_id") REFERENCES "AimsNonconformity" (aims_id)
);
CREATE INDEX "ix_AimsNonconformity_aims_nonconformity_immediate_actions_AimsNonconformity_aims_id" ON "AimsNonconformity_aims_nonconformity_immediate_actions" ("AimsNonconformity_aims_id");
CREATE INDEX "ix_AimsNonconformity_aims_nonconformity_immediate_actions_aims_nonconformity_immediate_actions" ON "AimsNonconformity_aims_nonconformity_immediate_actions" (aims_nonconformity_immediate_actions);

CREATE TABLE "AimsCorrectiveAction_aims_action_nonconformities" (
	"AimsCorrectiveAction_aims_id" TEXT,
	aims_action_nonconformities_aims_id TEXT,
	PRIMARY KEY ("AimsCorrectiveAction_aims_id", aims_action_nonconformities_aims_id),
	FOREIGN KEY("AimsCorrectiveAction_aims_id") REFERENCES "AimsCorrectiveAction" (aims_id),
	FOREIGN KEY(aims_action_nonconformities_aims_id) REFERENCES "AimsNonconformity" (aims_id)
);
CREATE INDEX "ix_AimsCorrectiveAction_aims_action_nonconformities_AimsCorrectiveAction_aims_id" ON "AimsCorrectiveAction_aims_action_nonconformities" ("AimsCorrectiveAction_aims_id");
CREATE INDEX "ix_AimsCorrectiveAction_aims_action_nonconformities_aims_action_nonconformities_aims_id" ON "AimsCorrectiveAction_aims_action_nonconformities" (aims_action_nonconformities_aims_id);

CREATE TABLE "AimsThirdPartyRelationship_aims_life_cycle_stages" (
	"AimsThirdPartyRelationship_aims_id" TEXT,
	aims_life_cycle_stages VARCHAR(27),
	PRIMARY KEY ("AimsThirdPartyRelationship_aims_id", aims_life_cycle_stages),
	FOREIGN KEY("AimsThirdPartyRelationship_aims_id") REFERENCES "AimsThirdPartyRelationship" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_life_cycle_stages_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship_aims_life_cycle_stages" ("AimsThirdPartyRelationship_aims_id");
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_life_cycle_stages_aims_life_cycle_stages" ON "AimsThirdPartyRelationship_aims_life_cycle_stages" (aims_life_cycle_stages);

CREATE TABLE "AimsThirdPartyRelationship_aims_relationship_party_roles" (
	"AimsThirdPartyRelationship_aims_id" TEXT,
	aims_relationship_party_roles VARCHAR(30),
	PRIMARY KEY ("AimsThirdPartyRelationship_aims_id", aims_relationship_party_roles),
	FOREIGN KEY("AimsThirdPartyRelationship_aims_id") REFERENCES "AimsThirdPartyRelationship" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_party_roles_aims_relationship_party_roles" ON "AimsThirdPartyRelationship_aims_relationship_party_roles" (aims_relationship_party_roles);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_party_roles_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship_aims_relationship_party_roles" ("AimsThirdPartyRelationship_aims_id");

CREATE TABLE "AimsThirdPartyRelationship_aims_relationship_responsibilities" (
	"AimsThirdPartyRelationship_aims_id" TEXT,
	aims_relationship_responsibilities TEXT,
	PRIMARY KEY ("AimsThirdPartyRelationship_aims_id", aims_relationship_responsibilities),
	FOREIGN KEY("AimsThirdPartyRelationship_aims_id") REFERENCES "AimsThirdPartyRelationship" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_responsibilities_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship_aims_relationship_responsibilities" ("AimsThirdPartyRelationship_aims_id");
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_responsibilities_aims_relationship_responsibilities" ON "AimsThirdPartyRelationship_aims_relationship_responsibilities" (aims_relationship_responsibilities);

CREATE TABLE "AimsThirdPartyRelationship_aims_relationship_documentation" (
	"AimsThirdPartyRelationship_aims_id" TEXT,
	aims_relationship_documentation TEXT,
	PRIMARY KEY ("AimsThirdPartyRelationship_aims_id", aims_relationship_documentation),
	FOREIGN KEY("AimsThirdPartyRelationship_aims_id") REFERENCES "AimsThirdPartyRelationship" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_documentation_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship_aims_relationship_documentation" ("AimsThirdPartyRelationship_aims_id");
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_documentation_aims_relationship_documentation" ON "AimsThirdPartyRelationship_aims_relationship_documentation" (aims_relationship_documentation);

CREATE TABLE "AimsThirdPartyRelationship_aims_relationship_assurance_evidence" (
	"AimsThirdPartyRelationship_aims_id" TEXT,
	aims_relationship_assurance_evidence TEXT,
	PRIMARY KEY ("AimsThirdPartyRelationship_aims_id", aims_relationship_assurance_evidence),
	FOREIGN KEY("AimsThirdPartyRelationship_aims_id") REFERENCES "AimsThirdPartyRelationship" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_assurance_evidence_aims_relationship_assurance_evidence" ON "AimsThirdPartyRelationship_aims_relationship_assurance_evidence" (aims_relationship_assurance_evidence);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_relationship_assurance_evidence_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship_aims_relationship_assurance_evidence" ("AimsThirdPartyRelationship_aims_id");

CREATE TABLE "AimsIncident_aims_incident_corrective_actions" (
	"AimsIncident_aims_id" TEXT,
	aims_incident_corrective_actions_aims_id TEXT,
	PRIMARY KEY ("AimsIncident_aims_id", aims_incident_corrective_actions_aims_id),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id),
	FOREIGN KEY(aims_incident_corrective_actions_aims_id) REFERENCES "AimsCorrectiveAction" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_incident_corrective_actions_AimsIncident_aims_id" ON "AimsIncident_aims_incident_corrective_actions" ("AimsIncident_aims_id");
CREATE INDEX "ix_AimsIncident_aims_incident_corrective_actions_aims_incident_corrective_actions_aims_id" ON "AimsIncident_aims_incident_corrective_actions" (aims_incident_corrective_actions_aims_id);

CREATE TABLE "AimsConcernReport_aims_concern_incidents" (
	"AimsConcernReport_aims_id" TEXT,
	aims_concern_incidents_aims_id TEXT,
	PRIMARY KEY ("AimsConcernReport_aims_id", aims_concern_incidents_aims_id),
	FOREIGN KEY("AimsConcernReport_aims_id") REFERENCES "AimsConcernReport" (aims_id),
	FOREIGN KEY(aims_concern_incidents_aims_id) REFERENCES "AimsIncident" (aims_id)
);
CREATE INDEX "ix_AimsConcernReport_aims_concern_incidents_aims_concern_incidents_aims_id" ON "AimsConcernReport_aims_concern_incidents" (aims_concern_incidents_aims_id);
CREATE INDEX "ix_AimsConcernReport_aims_concern_incidents_AimsConcernReport_aims_id" ON "AimsConcernReport_aims_concern_incidents" ("AimsConcernReport_aims_id");

CREATE TABLE "AimsConcernReport_aims_concern_nonconformities" (
	"AimsConcernReport_aims_id" TEXT,
	aims_concern_nonconformities_aims_id TEXT,
	PRIMARY KEY ("AimsConcernReport_aims_id", aims_concern_nonconformities_aims_id),
	FOREIGN KEY("AimsConcernReport_aims_id") REFERENCES "AimsConcernReport" (aims_id),
	FOREIGN KEY(aims_concern_nonconformities_aims_id) REFERENCES "AimsNonconformity" (aims_id)
);
CREATE INDEX "ix_AimsConcernReport_aims_concern_nonconformities_AimsConcernReport_aims_id" ON "AimsConcernReport_aims_concern_nonconformities" ("AimsConcernReport_aims_id");
CREATE INDEX "ix_AimsConcernReport_aims_concern_nonconformities_aims_concern_nonconformities_aims_id" ON "AimsConcernReport_aims_concern_nonconformities" (aims_concern_nonconformities_aims_id);

CREATE TABLE "AimsAuditFinding" (
	aims_finding_type VARCHAR(19) NOT NULL,
	aims_finding_control TEXT,
	aims_finding_evidence TEXT,
	aims_finding_root_cause TEXT,
	aims_finding_risk TEXT,
	aims_finding_recommendation TEXT,
	aims_finding_auditee_response TEXT,
	aims_finding_corrective_action TEXT,
	aims_finding_closure_status TEXT,
	aims_finding_closure_date DATE,
	aims_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AimsAudit_aims_id" TEXT,
	PRIMARY KEY (aims_id),
	FOREIGN KEY(aims_finding_control) REFERENCES "AimsControl" (aims_id),
	FOREIGN KEY(aims_finding_corrective_action) REFERENCES "AimsCorrectiveAction" (aims_id),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAuditFinding_aims_id" ON "AimsAuditFinding" (aims_id);

CREATE TABLE "AimsPlannedAction_aims_ai_systems" (
	"AimsPlannedAction_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsPlannedAction_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsPlannedAction_aims_id") REFERENCES "AimsPlannedAction" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsPlannedAction_aims_ai_systems_AimsPlannedAction_aims_id" ON "AimsPlannedAction_aims_ai_systems" ("AimsPlannedAction_aims_id");
CREATE INDEX "ix_AimsPlannedAction_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsPlannedAction_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsRiskAssessment_aims_ai_systems" (
	"AimsRiskAssessment_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsRiskAssessment_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsRiskAssessment_aims_id") REFERENCES "AimsRiskAssessment" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsRiskAssessment_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsRiskAssessment_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsRiskAssessment_aims_ai_systems_AimsRiskAssessment_aims_id" ON "AimsRiskAssessment_aims_ai_systems" ("AimsRiskAssessment_aims_id");

CREATE TABLE "AimsRisk_aims_ai_systems" (
	"AimsRisk_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsRisk_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsRisk_aims_id") REFERENCES "AimsRisk" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsRisk_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsRisk_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsRisk_aims_ai_systems_AimsRisk_aims_id" ON "AimsRisk_aims_ai_systems" ("AimsRisk_aims_id");

CREATE TABLE "AimsImpactAssessment_aims_ai_systems" (
	"AimsImpactAssessment_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsImpactAssessment_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsImpactAssessment_aims_id") REFERENCES "AimsImpactAssessment" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsImpactAssessment_aims_ai_systems_AimsImpactAssessment_aims_id" ON "AimsImpactAssessment_aims_ai_systems" ("AimsImpactAssessment_aims_id");
CREATE INDEX "ix_AimsImpactAssessment_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsImpactAssessment_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsIdentifiedImpact_aims_identified_impact_mitigation" (
	"AimsIdentifiedImpact_id" INTEGER,
	aims_identified_impact_mitigation TEXT,
	PRIMARY KEY ("AimsIdentifiedImpact_id", aims_identified_impact_mitigation),
	FOREIGN KEY("AimsIdentifiedImpact_id") REFERENCES "AimsIdentifiedImpact" (id)
);
CREATE INDEX "ix_AimsIdentifiedImpact_aims_identified_impact_mitigation_aims_identified_impact_mitigation" ON "AimsIdentifiedImpact_aims_identified_impact_mitigation" (aims_identified_impact_mitigation);
CREATE INDEX "ix_AimsIdentifiedImpact_aims_identified_impact_mitigation_AimsIdentifiedImpact_id" ON "AimsIdentifiedImpact_aims_identified_impact_mitigation" ("AimsIdentifiedImpact_id");

CREATE TABLE "AimsApplicabilityEntry_aims_ai_systems" (
	"AimsApplicabilityEntry_id" INTEGER,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsApplicabilityEntry_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsApplicabilityEntry_id") REFERENCES "AimsApplicabilityEntry" (id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsApplicabilityEntry_aims_ai_systems_AimsApplicabilityEntry_id" ON "AimsApplicabilityEntry_aims_ai_systems" ("AimsApplicabilityEntry_id");
CREATE INDEX "ix_AimsApplicabilityEntry_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsApplicabilityEntry_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsIncludedControl_aims_included_risks" (
	"AimsIncludedControl_id" INTEGER,
	aims_included_risks_aims_id TEXT,
	PRIMARY KEY ("AimsIncludedControl_id", aims_included_risks_aims_id),
	FOREIGN KEY("AimsIncludedControl_id") REFERENCES "AimsIncludedControl" (id),
	FOREIGN KEY(aims_included_risks_aims_id) REFERENCES "AimsRisk" (aims_id)
);
CREATE INDEX "ix_AimsIncludedControl_aims_included_risks_aims_included_risks_aims_id" ON "AimsIncludedControl_aims_included_risks" (aims_included_risks_aims_id);
CREATE INDEX "ix_AimsIncludedControl_aims_included_risks_AimsIncludedControl_id" ON "AimsIncludedControl_aims_included_risks" ("AimsIncludedControl_id");

CREATE TABLE "AimsIncludedControl_aims_ai_systems" (
	"AimsIncludedControl_id" INTEGER,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsIncludedControl_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsIncludedControl_id") REFERENCES "AimsIncludedControl" (id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsIncludedControl_aims_ai_systems_AimsIncludedControl_id" ON "AimsIncludedControl_aims_ai_systems" ("AimsIncludedControl_id");
CREATE INDEX "ix_AimsIncludedControl_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsIncludedControl_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsExcludedControl_aims_ai_systems" (
	"AimsExcludedControl_id" INTEGER,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsExcludedControl_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsExcludedControl_id") REFERENCES "AimsExcludedControl" (id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsExcludedControl_aims_ai_systems_AimsExcludedControl_id" ON "AimsExcludedControl_aims_ai_systems" ("AimsExcludedControl_id");
CREATE INDEX "ix_AimsExcludedControl_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsExcludedControl_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsControl_aims_ai_systems" (
	"AimsControl_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsControl_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsControl_aims_id") REFERENCES "AimsControl" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsControl_aims_ai_systems_AimsControl_aims_id" ON "AimsControl_aims_ai_systems" ("AimsControl_aims_id");
CREATE INDEX "ix_AimsControl_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsControl_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsAiSystem_aims_relevant_controls" (
	"AimsAiSystem_aims_id" TEXT,
	aims_relevant_controls_aims_id TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_relevant_controls_aims_id),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id),
	FOREIGN KEY(aims_relevant_controls_aims_id) REFERENCES "AimsControl" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_relevant_controls_aims_relevant_controls_aims_id" ON "AimsAiSystem_aims_relevant_controls" (aims_relevant_controls_aims_id);
CREATE INDEX "ix_AimsAiSystem_aims_relevant_controls_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_relevant_controls" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_intended_uses" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_intended_uses TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_intended_uses),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_intended_uses_aims_system_intended_uses" ON "AimsAiSystem_aims_system_intended_uses" (aims_system_intended_uses);
CREATE INDEX "ix_AimsAiSystem_aims_system_intended_uses_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_intended_uses" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_foreseeable_misuse" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_foreseeable_misuse TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_foreseeable_misuse),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_foreseeable_misuse_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_foreseeable_misuse" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_foreseeable_misuse_aims_system_foreseeable_misuse" ON "AimsAiSystem_aims_system_foreseeable_misuse" (aims_system_foreseeable_misuse);

CREATE TABLE "AimsAiSystem_aims_system_organization_roles" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_organization_roles VARCHAR(30),
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_organization_roles),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_organization_roles_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_organization_roles" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_organization_roles_aims_system_organization_roles" ON "AimsAiSystem_aims_system_organization_roles" (aims_system_organization_roles);

CREATE TABLE "AimsAiSystem_aims_system_pii_roles" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_pii_roles VARCHAR(20),
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_pii_roles),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_pii_roles_aims_system_pii_roles" ON "AimsAiSystem_aims_system_pii_roles" (aims_system_pii_roles);
CREATE INDEX "ix_AimsAiSystem_aims_system_pii_roles_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_pii_roles" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_requirements" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_requirements TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_requirements),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_requirements_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_requirements" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_requirements_aims_system_requirements" ON "AimsAiSystem_aims_system_requirements" (aims_system_requirements);

CREATE TABLE "AimsAiSystem_aims_system_model_types" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_model_types TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_model_types),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_model_types_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_model_types" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_model_types_aims_system_model_types" ON "AimsAiSystem_aims_system_model_types" (aims_system_model_types);

CREATE TABLE "AimsAiSystem_aims_system_threats" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_threats VARCHAR(15),
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_threats),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_threats_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_threats" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_threats_aims_system_threats" ON "AimsAiSystem_aims_system_threats" (aims_system_threats);

CREATE TABLE "AimsAiSystem_aims_system_verification_measures" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_verification_measures TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_verification_measures),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_verification_measures_aims_system_verification_measures" ON "AimsAiSystem_aims_system_verification_measures" (aims_system_verification_measures);
CREATE INDEX "ix_AimsAiSystem_aims_system_verification_measures_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_verification_measures" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_evaluation_criteria" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_evaluation_criteria TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_evaluation_criteria),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_evaluation_criteria_aims_system_evaluation_criteria" ON "AimsAiSystem_aims_system_evaluation_criteria" (aims_system_evaluation_criteria);
CREATE INDEX "ix_AimsAiSystem_aims_system_evaluation_criteria_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_evaluation_criteria" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_release_criteria" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_release_criteria TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_release_criteria),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_release_criteria_aims_system_release_criteria" ON "AimsAiSystem_aims_system_release_criteria" (aims_system_release_criteria);
CREATE INDEX "ix_AimsAiSystem_aims_system_release_criteria_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_release_criteria" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_operation_elements" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_operation_elements TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_operation_elements),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_operation_elements_aims_system_operation_elements" ON "AimsAiSystem_aims_system_operation_elements" (aims_system_operation_elements);
CREATE INDEX "ix_AimsAiSystem_aims_system_operation_elements_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_operation_elements" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_performance_metrics" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_performance_metrics TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_performance_metrics),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_performance_metrics_aims_system_performance_metrics" ON "AimsAiSystem_aims_system_performance_metrics" (aims_system_performance_metrics);
CREATE INDEX "ix_AimsAiSystem_aims_system_performance_metrics_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_performance_metrics" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_log_stages" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_log_stages VARCHAR(27),
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_log_stages),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_log_stages_aims_system_log_stages" ON "AimsAiSystem_aims_system_log_stages" (aims_system_log_stages);
CREATE INDEX "ix_AimsAiSystem_aims_system_log_stages_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_log_stages" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_log_contents" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_log_contents TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_log_contents),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_log_contents_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_log_contents" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_log_contents_aims_system_log_contents" ON "AimsAiSystem_aims_system_log_contents" (aims_system_log_contents);

CREATE TABLE "AimsAiSystem_aims_system_human_oversight_stages" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_human_oversight_stages VARCHAR(27),
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_human_oversight_stages),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_human_oversight_stages_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_human_oversight_stages" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_human_oversight_stages_aims_system_human_oversight_stages" ON "AimsAiSystem_aims_system_human_oversight_stages" (aims_system_human_oversight_stages);

CREATE TABLE "AimsAiSystem_aims_system_resources_used" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_resources_used_aims_id TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_resources_used_aims_id),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id),
	FOREIGN KEY(aims_system_resources_used_aims_id) REFERENCES "AimsSystemResource" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_resources_used_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_resources_used" ("AimsAiSystem_aims_id");
CREATE INDEX "ix_AimsAiSystem_aims_system_resources_used_aims_system_resources_used_aims_id" ON "AimsAiSystem_aims_system_resources_used" (aims_system_resources_used_aims_id);

CREATE TABLE "AimsAiSystem_aims_system_technical_documents" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_technical_documents_aims_id TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_technical_documents_aims_id),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id),
	FOREIGN KEY(aims_system_technical_documents_aims_id) REFERENCES "AimsTechnicalDocumentation" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_technical_documents_aims_system_technical_documents_aims_id" ON "AimsAiSystem_aims_system_technical_documents" (aims_system_technical_documents_aims_id);
CREATE INDEX "ix_AimsAiSystem_aims_system_technical_documents_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_technical_documents" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_impact_assessments" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_impact_assessments_aims_id TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_impact_assessments_aims_id),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id),
	FOREIGN KEY(aims_system_impact_assessments_aims_id) REFERENCES "AimsImpactAssessment" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_impact_assessments_aims_system_impact_assessments_aims_id" ON "AimsAiSystem_aims_system_impact_assessments" (aims_system_impact_assessments_aims_id);
CREATE INDEX "ix_AimsAiSystem_aims_system_impact_assessments_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_impact_assessments" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsAiSystem_aims_system_relationships" (
	"AimsAiSystem_aims_id" TEXT,
	aims_system_relationships_aims_id TEXT,
	PRIMARY KEY ("AimsAiSystem_aims_id", aims_system_relationships_aims_id),
	FOREIGN KEY("AimsAiSystem_aims_id") REFERENCES "AimsAiSystem" (aims_id),
	FOREIGN KEY(aims_system_relationships_aims_id) REFERENCES "AimsThirdPartyRelationship" (aims_id)
);
CREATE INDEX "ix_AimsAiSystem_aims_system_relationships_aims_system_relationships_aims_id" ON "AimsAiSystem_aims_system_relationships" (aims_system_relationships_aims_id);
CREATE INDEX "ix_AimsAiSystem_aims_system_relationships_AimsAiSystem_aims_id" ON "AimsAiSystem_aims_system_relationships" ("AimsAiSystem_aims_id");

CREATE TABLE "AimsDevelopmentProcess_aims_ai_systems" (
	"AimsDevelopmentProcess_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsDevelopmentProcess_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsDevelopmentProcess_aims_id") REFERENCES "AimsDevelopmentProcess" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsDevelopmentProcess_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsDevelopmentProcess_aims_ai_systems_AimsDevelopmentProcess_aims_id" ON "AimsDevelopmentProcess_aims_ai_systems" ("AimsDevelopmentProcess_aims_id");

CREATE TABLE "AimsResponsibleUseProcess_aims_ai_systems" (
	"AimsResponsibleUseProcess_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsResponsibleUseProcess_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsResponsibleUseProcess_aims_id") REFERENCES "AimsResponsibleUseProcess" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_ai_systems_AimsResponsibleUseProcess_aims_id" ON "AimsResponsibleUseProcess_aims_ai_systems" ("AimsResponsibleUseProcess_aims_id");
CREATE INDEX "ix_AimsResponsibleUseProcess_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsResponsibleUseProcess_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsTechnicalDocumentation_aims_ai_systems" (
	"AimsTechnicalDocumentation_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsTechnicalDocumentation_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsTechnicalDocumentation_aims_id") REFERENCES "AimsTechnicalDocumentation" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsTechnicalDocumentation_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsTechnicalDocumentation_aims_ai_systems_AimsTechnicalDocumentation_aims_id" ON "AimsTechnicalDocumentation_aims_ai_systems" ("AimsTechnicalDocumentation_aims_id");

CREATE TABLE "AimsUserInformation_aims_ai_systems" (
	"AimsUserInformation_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsUserInformation_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsUserInformation_aims_id") REFERENCES "AimsUserInformation" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsUserInformation_aims_ai_systems_AimsUserInformation_aims_id" ON "AimsUserInformation_aims_ai_systems" ("AimsUserInformation_aims_id");
CREATE INDEX "ix_AimsUserInformation_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsUserInformation_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsIncidentCommunicationPlan_aims_ai_systems" (
	"AimsIncidentCommunicationPlan_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsIncidentCommunicationPlan_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsIncidentCommunicationPlan_aims_id") REFERENCES "AimsIncidentCommunicationPlan" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsIncidentCommunicationPlan_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsIncidentCommunicationPlan_aims_ai_systems_AimsIncidentCommunicationPlan_aims_id" ON "AimsIncidentCommunicationPlan_aims_ai_systems" ("AimsIncidentCommunicationPlan_aims_id");

CREATE TABLE "AimsReportingObligation_aims_ai_systems" (
	"AimsReportingObligation_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsReportingObligation_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsReportingObligation_aims_id") REFERENCES "AimsReportingObligation" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsReportingObligation_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsReportingObligation_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsReportingObligation_aims_ai_systems_AimsReportingObligation_aims_id" ON "AimsReportingObligation_aims_ai_systems" ("AimsReportingObligation_aims_id");

CREATE TABLE "AimsAuditProgramme_aims_programme_audits" (
	"AimsAuditProgramme_aims_id" TEXT,
	aims_programme_audits_aims_id TEXT,
	PRIMARY KEY ("AimsAuditProgramme_aims_id", aims_programme_audits_aims_id),
	FOREIGN KEY("AimsAuditProgramme_aims_id") REFERENCES "AimsAuditProgramme" (aims_id),
	FOREIGN KEY(aims_programme_audits_aims_id) REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAuditProgramme_aims_programme_audits_AimsAuditProgramme_aims_id" ON "AimsAuditProgramme_aims_programme_audits" ("AimsAuditProgramme_aims_id");
CREATE INDEX "ix_AimsAuditProgramme_aims_programme_audits_aims_programme_audits_aims_id" ON "AimsAuditProgramme_aims_programme_audits" (aims_programme_audits_aims_id);

CREATE TABLE "AimsAudit_aims_audit_standards" (
	"AimsAudit_aims_id" TEXT,
	aims_audit_standards VARCHAR(13),
	PRIMARY KEY ("AimsAudit_aims_id", aims_audit_standards),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_audit_standards_aims_audit_standards" ON "AimsAudit_aims_audit_standards" (aims_audit_standards);
CREATE INDEX "ix_AimsAudit_aims_audit_standards_AimsAudit_aims_id" ON "AimsAudit_aims_audit_standards" ("AimsAudit_aims_id");

CREATE TABLE "AimsAudit_aims_audit_criteria" (
	"AimsAudit_aims_id" TEXT,
	aims_audit_criteria TEXT,
	PRIMARY KEY ("AimsAudit_aims_id", aims_audit_criteria),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_audit_criteria_AimsAudit_aims_id" ON "AimsAudit_aims_audit_criteria" ("AimsAudit_aims_id");
CREATE INDEX "ix_AimsAudit_aims_audit_criteria_aims_audit_criteria" ON "AimsAudit_aims_audit_criteria" (aims_audit_criteria);

CREATE TABLE "AimsAudit_aims_audit_objectives" (
	"AimsAudit_aims_id" TEXT,
	aims_audit_objectives TEXT,
	PRIMARY KEY ("AimsAudit_aims_id", aims_audit_objectives),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_audit_objectives_aims_audit_objectives" ON "AimsAudit_aims_audit_objectives" (aims_audit_objectives);
CREATE INDEX "ix_AimsAudit_aims_audit_objectives_AimsAudit_aims_id" ON "AimsAudit_aims_audit_objectives" ("AimsAudit_aims_id");

CREATE TABLE "AimsAudit_aims_audit_team" (
	"AimsAudit_aims_id" TEXT,
	aims_audit_team TEXT,
	PRIMARY KEY ("AimsAudit_aims_id", aims_audit_team),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_audit_team_aims_audit_team" ON "AimsAudit_aims_audit_team" (aims_audit_team);
CREATE INDEX "ix_AimsAudit_aims_audit_team_AimsAudit_aims_id" ON "AimsAudit_aims_audit_team" ("AimsAudit_aims_id");

CREATE TABLE "AimsAudit_aims_audit_auditees" (
	"AimsAudit_aims_id" TEXT,
	aims_audit_auditees TEXT,
	PRIMARY KEY ("AimsAudit_aims_id", aims_audit_auditees),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_audit_auditees_AimsAudit_aims_id" ON "AimsAudit_aims_audit_auditees" ("AimsAudit_aims_id");
CREATE INDEX "ix_AimsAudit_aims_audit_auditees_aims_audit_auditees" ON "AimsAudit_aims_audit_auditees" (aims_audit_auditees);

CREATE TABLE "AimsAudit_aims_audit_report_distribution" (
	"AimsAudit_aims_id" TEXT,
	aims_audit_report_distribution TEXT,
	PRIMARY KEY ("AimsAudit_aims_id", aims_audit_report_distribution),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_audit_report_distribution_AimsAudit_aims_id" ON "AimsAudit_aims_audit_report_distribution" ("AimsAudit_aims_id");
CREATE INDEX "ix_AimsAudit_aims_audit_report_distribution_aims_audit_report_distribution" ON "AimsAudit_aims_audit_report_distribution" (aims_audit_report_distribution);

CREATE TABLE "AimsAudit_aims_document_distribution" (
	"AimsAudit_aims_id" TEXT,
	aims_document_distribution TEXT,
	PRIMARY KEY ("AimsAudit_aims_id", aims_document_distribution),
	FOREIGN KEY("AimsAudit_aims_id") REFERENCES "AimsAudit" (aims_id)
);
CREATE INDEX "ix_AimsAudit_aims_document_distribution_AimsAudit_aims_id" ON "AimsAudit_aims_document_distribution" ("AimsAudit_aims_id");
CREATE INDEX "ix_AimsAudit_aims_document_distribution_aims_document_distribution" ON "AimsAudit_aims_document_distribution" (aims_document_distribution);

CREATE TABLE "AimsThirdPartyRelationship_aims_ai_systems" (
	"AimsThirdPartyRelationship_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsThirdPartyRelationship_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsThirdPartyRelationship_aims_id") REFERENCES "AimsThirdPartyRelationship" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsThirdPartyRelationship_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsThirdPartyRelationship_aims_ai_systems_AimsThirdPartyRelationship_aims_id" ON "AimsThirdPartyRelationship_aims_ai_systems" ("AimsThirdPartyRelationship_aims_id");

CREATE TABLE "AimsSupplierRelationship_aims_ai_systems" (
	"AimsSupplierRelationship_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsSupplierRelationship_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsSupplierRelationship_aims_id") REFERENCES "AimsSupplierRelationship" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsSupplierRelationship_aims_ai_systems_AimsSupplierRelationship_aims_id" ON "AimsSupplierRelationship_aims_ai_systems" ("AimsSupplierRelationship_aims_id");
CREATE INDEX "ix_AimsSupplierRelationship_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsSupplierRelationship_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsCustomerRelationship_aims_ai_systems" (
	"AimsCustomerRelationship_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsCustomerRelationship_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsCustomerRelationship_aims_id") REFERENCES "AimsCustomerRelationship" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsCustomerRelationship_aims_ai_systems_AimsCustomerRelationship_aims_id" ON "AimsCustomerRelationship_aims_ai_systems" ("AimsCustomerRelationship_aims_id");
CREATE INDEX "ix_AimsCustomerRelationship_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsCustomerRelationship_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsSystemEvent_aims_ai_systems" (
	"AimsSystemEvent_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsSystemEvent_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsSystemEvent_aims_id") REFERENCES "AimsSystemEvent" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsSystemEvent_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsSystemEvent_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsSystemEvent_aims_ai_systems_AimsSystemEvent_aims_id" ON "AimsSystemEvent_aims_ai_systems" ("AimsSystemEvent_aims_id");

CREATE TABLE "AimsIncident_aims_ai_systems" (
	"AimsIncident_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsIncident_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsIncident_aims_id") REFERENCES "AimsIncident" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsIncident_aims_ai_systems_AimsIncident_aims_id" ON "AimsIncident_aims_ai_systems" ("AimsIncident_aims_id");
CREATE INDEX "ix_AimsIncident_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsIncident_aims_ai_systems" (aims_ai_systems_aims_id);

CREATE TABLE "AimsConcernReport_aims_ai_systems" (
	"AimsConcernReport_aims_id" TEXT,
	aims_ai_systems_aims_id TEXT,
	PRIMARY KEY ("AimsConcernReport_aims_id", aims_ai_systems_aims_id),
	FOREIGN KEY("AimsConcernReport_aims_id") REFERENCES "AimsConcernReport" (aims_id),
	FOREIGN KEY(aims_ai_systems_aims_id) REFERENCES "AimsAiSystem" (aims_id)
);
CREATE INDEX "ix_AimsConcernReport_aims_ai_systems_aims_ai_systems_aims_id" ON "AimsConcernReport_aims_ai_systems" (aims_ai_systems_aims_id);
CREATE INDEX "ix_AimsConcernReport_aims_ai_systems_AimsConcernReport_aims_id" ON "AimsConcernReport_aims_ai_systems" ("AimsConcernReport_aims_id");

CREATE TABLE "AimsAuditFinding_aims_cited_clauses" (
	"AimsAuditFinding_aims_id" TEXT,
	aims_cited_clauses VARCHAR(12),
	PRIMARY KEY ("AimsAuditFinding_aims_id", aims_cited_clauses),
	FOREIGN KEY("AimsAuditFinding_aims_id") REFERENCES "AimsAuditFinding" (aims_id)
);
CREATE INDEX "ix_AimsAuditFinding_aims_cited_clauses_aims_cited_clauses" ON "AimsAuditFinding_aims_cited_clauses" (aims_cited_clauses);
CREATE INDEX "ix_AimsAuditFinding_aims_cited_clauses_AimsAuditFinding_aims_id" ON "AimsAuditFinding_aims_cited_clauses" ("AimsAuditFinding_aims_id");

CREATE TABLE "AimsAuditFinding_aims_cited_annex_a_controls" (
	"AimsAuditFinding_aims_id" TEXT,
	aims_cited_annex_a_controls VARCHAR(7),
	PRIMARY KEY ("AimsAuditFinding_aims_id", aims_cited_annex_a_controls),
	FOREIGN KEY("AimsAuditFinding_aims_id") REFERENCES "AimsAuditFinding" (aims_id)
);
CREATE INDEX "ix_AimsAuditFinding_aims_cited_annex_a_controls_aims_cited_annex_a_controls" ON "AimsAuditFinding_aims_cited_annex_a_controls" (aims_cited_annex_a_controls);
CREATE INDEX "ix_AimsAuditFinding_aims_cited_annex_a_controls_AimsAuditFinding_aims_id" ON "AimsAuditFinding_aims_cited_annex_a_controls" ("AimsAuditFinding_aims_id");
