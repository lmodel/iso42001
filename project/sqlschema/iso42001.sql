-- # Abstract Class: NamedEntity Description: Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Abstract Class: DocumentedInformation Description: Abstract class for documented information per Clause 7.5. Captures metadata required for document control under the AIMS.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIManagementSystem Description: Top-level container representing an organization's complete AI Management System (AIMS) per ISO/IEC 42001:2023. Aggregates all components required to support the AIMS lifecycle.
--     * Slot: organization Description: Reference to the organization operating the AIMS.
--     * Slot: scope_statement Description: Documented statement of AIMS scope per Clause 4.3.
--     * Slot: top_management Description: Reference to the person or group exercising top management direction and control over the AIMS (Clause 3.3, 5.1).
--     * Slot: governing_body Description: Reference to the governing body to which top management is accountable (Clause 3.22).
--     * Slot: ai_policy Description: Reference to the AI policy.
--     * Slot: ai_risk_assessment_process Description: Reference to the AI risk assessment process.
--     * Slot: ai_risk_treatment_process Description: Reference to the AI risk treatment process.
--     * Slot: ai_system_impact_assessment_process Description: Reference to the AI system impact assessment process.
--     * Slot: statement_of_applicability Description: Reference to the AIMS Statement of Applicability.
--     * Slot: awareness_program Description: Reference to the awareness program.
--     * Slot: communication_plan Description: Reference to the communication plan.
--     * Slot: monitoring_program Description: Reference to the monitoring program.
--     * Slot: certification_status Description: Current certification status of the AIMS.
--     * Slot: certification_body Description: Body that issued the certification.
--     * Slot: certification_date Description: Date the AIMS was certified.
--     * Slot: recertification_date Description: Date when recertification is due.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Organization Description: The organization establishing and operating the AIMS. Captures the context required by Clause 4.1, including the organization's role(s) with respect to AI systems.
--     * Slot: legal_name Description: Legal registered name of the organization.
--     * Slot: organization_type Description: Type of organization (e.g., corporation, government, nonprofit).
--     * Slot: industry_sector Description: Primary industry sector of the organization (free-form label).
--     * Slot: size_category Description: Organization size classification.
--     * Slot: employee_count Description: Approximate number of employees.
--     * Slot: parent_organization Description: Parent organization if applicable.
--     * Slot: climate_change_relevant Description: Whether climate change has been determined to be a relevant issue for the organization's context per Clause 4.1.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: InterestedParty Description: A stakeholder whose needs and expectations are relevant to the AIMS per Clause 4.2. Includes internal and external parties such as users, regulators, partners, suppliers, customers, AI subjects, and relevant authorities.
--     * Slot: party_type Description: Category of party.
--     * Slot: relationship Description: Nature of the relationship with the organization.
--     * Slot: communication_needs Description: Communication requirements for this party.
--     * Slot: contact_information Description: Contact details for the party.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIPolicy Description: The AI policy established by top management per Clause 5.2. Provides a framework for setting AI objectives and demonstrates commitment to responsible AI.
--     * Slot: policy_statement Description: The core policy statement text.
--     * Slot: policy_objectives_framework Description: Framework for setting AI objectives.
--     * Slot: applicability_statement Description: Statement of policy applicability.
--     * Slot: communication_date Description: Date when the policy was communicated.
--     * Slot: acknowledgment_required Description: Whether acknowledgment is required from personnel.
--     * Slot: last_policy_review_date Description: Date of the most recent AI policy review.
--     * Slot: next_policy_review_date Description: Planned date of the next AI policy review.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: TopicSpecificPolicy Description: A topic-specific policy supporting the overarching AI policy, for example covering data governance, fairness, transparency, supplier use, or human oversight of AI systems.
--     * Slot: topic_area Description: The specific topic addressed by the policy.
--     * Slot: parent_policy Description: The parent AI policy this topic-specific policy supports.
--     * Slot: target_audience Description: Intended audience for the policy or document.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Role Description: An AI-related role with defined responsibilities and authorities per Clause 5.3 and Annex A.3.2.
--     * Slot: role_type Description: Category of the role. Use a `GovernanceRoleType` value for the normative AIMS governance positions; free-form strings remain accepted for organization-defined roles.
--     * Slot: accountability Description: What the role is accountable for.
--     * Slot: delegation_rules Description: Rules for delegating responsibilities.
--     * Slot: reporting_line Description: To whom this role reports.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIObjective Description: A measurable AI objective per Clause 6.2, established at relevant functions and levels and aligned with the AI policy.
--     * Slot: objective_statement Description: Clear statement of the objective.
--     * Slot: objective_category Description: Category of AI objective (e.g., fairness, transparency, robustness).
--     * Slot: target_value Description: Target value for the objective metric.
--     * Slot: current_value Description: Current measured value.
--     * Slot: metric_definition Description: Definition of how the objective is measured.
--     * Slot: measurement_method Description: Method used to measure the metric.
--     * Slot: measurement_frequency Description: How often measurement is performed.
--     * Slot: responsible_role Description: Role responsible for the objective or control.
--     * Slot: resources_required Description: Resources required for implementation.
--     * Slot: target_date Description: Target date for achieving the objective.
--     * Slot: achievement_status Description: Current status of objective achievement.
--     * Slot: action_plan Description: Plan for achieving the objective.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIRiskAssessmentProcess Description: The documented AI risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analysing, and evaluating AI risks. Aligned with ISO/IEC 23894.
--     * Slot: risk_acceptance_criteria Description: Criteria for accepting AI risks.
--     * Slot: assessment_criteria Description: Criteria for performing AI risk or impact assessments.
--     * Slot: assessment_methodology Description: Methodology used for assessment.
--     * Slot: likelihood_scale Description: Scale used for likelihood rating.
--     * Slot: impact_scale Description: Scale used for impact rating.
--     * Slot: risk_matrix Description: Risk matrix or calculation method.
--     * Slot: assessment_frequency Description: Planned frequency of assessments.
--     * Slot: alignment_with_ai_policy Description: Statement of how the process aligns with the AI policy.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIRiskAssessment Description: An instance of AI risk assessment performed per Clause 8.2, identifying and evaluating AI risks at planned intervals or following significant change.
--     * Slot: assessment_scope Description: Scope of the assessment.
--     * Slot: assessment_date Description: Date the assessment was conducted.
--     * Slot: assessor Description: Person or team who conducted the assessment.
--     * Slot: methodology_used Description: Specific methodology applied in this assessment.
--     * Slot: linked_impact_assessment Description: AI system impact assessment linked to this risk assessment.
--     * Slot: summary_findings Description: Summary of assessment findings.
--     * Slot: next_assessment_date Description: Planned date for next assessment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIRisk Description: An identified AI risk that may affect achievement of AI objectives, individuals, groups, or societies within the AIMS scope.
--     * Slot: risk_source_category Description: Category of AI risk source per Annex C.
--     * Slot: risk_source_description Description: Description of the specific source of risk.
--     * Slot: risk_owner Description: Person accountable for managing the AI risk.
--     * Slot: likelihood Description: Assessed likelihood of risk occurrence.
--     * Slot: impact Description: Assessed consequence if the risk materializes.
--     * Slot: inherent_risk_level Description: Risk level before controls are applied.
--     * Slot: residual_risk_level Description: Risk level after controls are applied.
--     * Slot: risk_treatment_option Description: Selected treatment option for the AI risk.
--     * Slot: treatment_priority Description: Priority for treating this risk.
--     * Slot: related_treatment_plan Description: Risk treatment plan addressing this risk.
--     * Slot: related_impact_assessment Description: AI system impact assessment associated with this risk.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIRiskTreatmentProcess Description: The documented AI risk treatment process per Clause 6.1.3, defining how treatment options are selected, how Annex A controls are considered, and how the Statement of Applicability is produced.
--     * Slot: treatment_options_guidance Description: Guidance on selecting AI risk treatment options.
--     * Slot: control_selection_criteria Description: Criteria for selecting Annex A controls.
--     * Slot: soa_template Description: Template used for the Statement of Applicability.
--     * Slot: approval_workflow Description: Workflow for approving AI risk treatment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIRiskTreatmentPlan Description: A plan documenting planned actions to address identified AI risks through selected controls. Requires approval by designated management per Clause 6.1.3.
--     * Slot: plan_scope Description: Scope of the treatment plan.
--     * Slot: resources_required Description: Resources required for implementation.
--     * Slot: implementation_timeline Description: Timeline for implementation.
--     * Slot: risk_owner_approval Description: Risk owner who approved the plan.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: residual_risk_acceptance Description: Documentation of residual AI risk acceptance.
--     * Slot: implementation_status Description: Current implementation status.
--     * Slot: completion_date Description: Date when implementation was completed.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AISystemImpactAssessmentProcess Description: The documented process for assessing the potential consequences for individuals, groups, and societies arising from the development, provision, or use of AI systems per Clause 6.1.4.
--     * Slot: assessment_criteria Description: Criteria for performing AI risk or impact assessments.
--     * Slot: assessment_methodology Description: Methodology used for assessment.
--     * Slot: assessment_frequency Description: Planned frequency of assessments.
--     * Slot: linkage_to_risk_assessment Description: Description of how impact assessment results feed into AI risk assessment per Clause 6.1.4.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AISystemImpactAssessment Description: An instance of an AI system impact assessment performed per Clause 6.1.4 and Clause 8.4. Documents consequences of deployment, intended use, and foreseeable misuse on individuals, groups, and societies.
--     * Slot: assessment_scope Description: Scope of the assessment.
--     * Slot: assessment_date Description: Date the assessment was conducted.
--     * Slot: assessor Description: Person or team who conducted the assessment.
--     * Slot: technical_context Description: Specific technical context in which the AI system is deployed.
--     * Slot: societal_context Description: Societal context relevant to the impact assessment.
--     * Slot: next_assessment_date Description: Planned date for next assessment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: StatementOfApplicability Description: The Statement of Applicability (SoA) for the AIMS recording which Annex A controls apply, justification for inclusion or exclusion, and current implementation state per Clause 6.1.3 f).
--     * Slot: total_controls Description: Total number of controls in scope.
--     * Slot: implemented_count Description: Number of implemented controls.
--     * Slot: planned_count Description: Number of controls planned for implementation.
--     * Slot: not_applicable_count Description: Number of controls marked not applicable.
--     * Slot: last_review_date Description: Date of last review.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: SoAEntry Description: A single entry in the AIMS Statement of Applicability documenting the applicability and implementation status of one reference control.
--     * Slot: id
--     * Slot: control_reference Description: Reference to an Annex A control (e.g., A.6.2.4).
--     * Slot: is_applicable Description: Whether the control is applicable.
--     * Slot: inclusion_justification Description: Justification for including the control.
--     * Slot: exclusion_justification Description: Justification for excluding the control.
--     * Slot: implementation_status Description: Current implementation status.
--     * Slot: implementation_evidence Description: Evidence of control implementation.
--     * Slot: responsible_role Description: Role responsible for the objective or control.
--     * Slot: target_implementation_date Description: Target date for implementing the control.
-- # Class: AIReferenceControl Description: A reference control from Annex A of ISO/IEC 42001:2023. Controls are grouped into nine families (A.2 through A.10) and supported by implementation guidance in Annex B.
--     * Slot: control_id Description: Control identifier from Annex A (e.g., A.6.2.4). Accepts either an enumerated normative `AnnexAControlId` value or a free-form string for organization-defined controls beyond Annex A.
--     * Slot: control_title Description: Title of the control.
--     * Slot: control_family Description: Family of the Annex A control.
--     * Slot: control_text Description: Organization-authored control statement or external control summary. Do not include verbatim ISO/IEC standards text.
--     * Slot: implementation_guidance Description: Organization-authored implementation notes for the control.
--     * Slot: control_owner Description: Person responsible for the control.
--     * Slot: implementation_status Description: Current implementation status.
--     * Slot: implementation_date Description: Date the control was implemented.
--     * Slot: effectiveness_rating Description: Rating of control effectiveness.
--     * Slot: last_test_date Description: Date the control was last tested.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AISystem Description: An AI system within the AIMS scope. Captures life cycle stage, intended use, applicable domains, and references to data and tooling resources, technical documentation, and impact assessments.
--     * Slot: ai_system_purpose Description: Purpose of the AI system.
--     * Slot: application_domain Description: Domain in which the AI system is applied (e.g., health, finance).
--     * Slot: deployment_context Description: Operational context in which the AI system is deployed.
--     * Slot: lifecycle_stage Description: Current life cycle stage of the AI system.
--     * Slot: organization_role Description: The organization's role with respect to this AI system (provider, producer, customer, partner).
--     * Slot: autonomy_level Description: Description of the level of autonomy and human oversight required for this AI system. Free-form text complements `human_oversight_required` and `human_oversight_description`.
--     * Slot: ml_approach Description: Machine-learning approach used by the AI system, capturing the design-choice dimension referenced in Annex B.6.2.3.
--     * Slot: human_oversight_required Description: Whether human oversight is required for outputs of the AI system (Annex A.9, Annex B.9.3).
--     * Slot: human_oversight_description Description: Description of human-oversight arrangements, including review points, escalation paths, and oversight authority (Annex B.9.3).
--     * Slot: learning_mode Description: Learning paradigm of the AI system (informs Clause 6.1 risk and Annex A.6.2.6 monitoring considerations).
--     * Slot: event_log_policy Description: Policy for AI system event log recording across life cycle phases.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: DataResource Description: A data resource used by an AI system per Annex A.7. Includes data acquisition, quality, provenance, and preparation metadata.
--     * Slot: data_resource_category Description: Category of data resource (training, validation, test, production).
--     * Slot: source Description: Source from which the data was obtained.
--     * Slot: acquisition_method Description: How the data was acquired (e.g., collected, purchased, synthetic).
--     * Slot: data_provenance Description: Provenance information for the data resource.
--     * Slot: labelling_process Description: Description of the data labelling process.
--     * Slot: last_updated_date Description: Date the data was last updated or modified.
--     * Slot: retention_policy Description: Retention and disposal policy applicable to the data.
--     * Slot: data_classification Description: Classification of the data resource.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ToolingResource Description: A tooling resource (algorithm, framework, model, library) used in an AI system per A.4.4.
--     * Slot: tool_category Description: Category of tooling resource (algorithm, framework, model, library).
--     * Slot: tool_version Description: Version identifier for the tooling resource.
--     * Slot: vendor Description: Vendor or origin of the tooling resource.
--     * Slot: license_terms Description: License terms applicable to the tooling resource.
--     * Slot: usage_purpose Description: Purpose for which the tooling resource is used.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ComputingResource Description: A system or computing resource used in the development or operation of an AI system per A.4.5.
--     * Slot: resource_class Description: Class of computing resource (e.g., GPU cluster, edge device).
--     * Slot: quantity Description: Quantity of the resource.
--     * Slot: location Description: Physical or logical location of the resource.
--     * Slot: environment_type Description: Type of environment (development, staging, production).
--     * Slot: cost Description: Cost of the resource.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: HumanResource Description: A human resource (role, expertise area) involved in development, deployment, operation, maintenance, or oversight of an AI system per A.4.6.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Resource Description: A resource provided for the AIMS per Clause 7.1.
--     * Slot: resource_type Description: Type of resource.
--     * Slot: quantity Description: Quantity of the resource.
--     * Slot: allocation_date Description: Date the resource was allocated.
--     * Slot: allocated_to Description: What the resource is allocated to.
--     * Slot: cost Description: Cost of the resource.
--     * Slot: availability_status Description: Current availability of the resource.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CompetenceRecord Description: Evidence of competence for personnel affecting AIMS performance per Clause 7.2.
--     * Slot: person_name Description: Name of the person.
--     * Slot: person_role Description: Role of the person.
--     * Slot: competency_assessment_date Description: Date of last competency assessment.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AwarenessProgram Description: The awareness program ensuring personnel understand their AI-related responsibilities per Clause 7.3.
--     * Slot: target_audience Description: Intended audience for the policy or document.
--     * Slot: frequency Description: Frequency of the activity.
--     * Slot: completion_tracking Description: How completion is tracked.
--     * Slot: effectiveness_measures Description: How effectiveness is measured.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CommunicationPlan Description: Plan for internal and external communications relevant to the AIMS per Clause 7.4.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CommunicationItem Description: A single communication requirement within the AIMS communication plan.
--     * Slot: id
--     * Slot: subject Description: Subject of the communication.
--     * Slot: purpose Description: Purpose of the communication.
--     * Slot: audience Description: Target audience.
--     * Slot: frequency Description: Frequency of the activity.
--     * Slot: method Description: Method of communication.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: records_required Description: Records required to evidence the activity.
-- # Class: OperationalProcedure Description: A documented procedure for operational planning and control of AIMS processes per Clause 8.1, including AI system life cycle related controls.
--     * Slot: procedure_scope Description: Scope of the procedure.
--     * Slot: process_criteria Description: Criteria for the process.
--     * Slot: change_control_requirements Description: Requirements for controlling changes to the process.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: MonitoringProgram Description: The program for monitoring, measurement, analysis, and evaluation of AIMS performance per Clause 9.1.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: MonitoringItem Description: A single item to be monitored and measured per Clause 9.1.
--     * Slot: id
--     * Slot: metric_name Description: Name of the metric.
--     * Slot: metric_description Description: Description of the metric.
--     * Slot: measurement_method Description: Method used to measure the metric.
--     * Slot: measurement_frequency Description: How often measurement is performed.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: analysis_frequency Description: Frequency of analysis.
--     * Slot: analyst Description: Person performing the analysis.
--     * Slot: target_threshold Description: Target threshold for the metric.
--     * Slot: alert_threshold Description: Threshold that triggers an alert.
--     * Slot: current_value Description: Current measured value.
--     * Slot: trend Description: Observed trend in the metric.
-- # Class: InternalAudit Description: An internal audit instance per Clause 9.2 assessing AIMS conformance and effectiveness.
--     * Slot: audit_reference Description: Unique reference identifier for the audit.
--     * Slot: audit_type Description: Type of audit (internal, external second-party, external third-party, surveillance, recertification, combined).
--     * Slot: audit_scope Description: Scope of the audit.
--     * Slot: audit_criteria Description: Criteria used for the audit.
--     * Slot: audit_objectives Description: Objectives of the audit.
--     * Slot: audit_period_start Description: Start date of the audit period.
--     * Slot: audit_period_end Description: End date of the audit period.
--     * Slot: lead_auditor Description: Lead auditor for the audit.
--     * Slot: audit_plan Description: Reference to the audit plan.
--     * Slot: audit_conclusion Description: Overall conclusion of the audit.
--     * Slot: report_date Description: Date the audit report was issued.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AuditProgramme Description: The internal audit programme per Clause 9.2.2, planning AIMS audit activities over a defined period.
--     * Slot: programme_period Description: Period covered by the audit programme.
--     * Slot: audit_frequency_rationale Description: Rationale for the audit cadence.
--     * Slot: resource_requirements Description: Resources required for the activity.
--     * Slot: auditor_qualifications Description: Required auditor qualifications.
--     * Slot: programme_status Description: Status of the audit programme.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AuditFinding Description: A finding from an AIMS internal audit, including nonconformities, observations, and positive findings.
--     * Slot: finding_type Description: Type of audit finding.
--     * Slot: clause_reference Description: ISO/IEC 42001 clause referenced by the finding.
--     * Slot: control_reference Description: Reference to an Annex A control (e.g., A.6.2.4).
--     * Slot: finding_description Description: Description of the finding.
--     * Slot: objective_evidence Description: Objective evidence supporting the finding.
--     * Slot: root_cause_analysis Description: Analysis of the root cause.
--     * Slot: risk_implication Description: AI risk implication of the finding.
--     * Slot: recommended_action Description: Recommended action to address the finding.
--     * Slot: auditee_response Description: Auditee's response to the finding.
--     * Slot: linked_corrective_action Description: Linked corrective action addressing the finding.
--     * Slot: closure_status Description: Closure status of the finding.
--     * Slot: closure_date Description: Date when the item was closed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ManagementReview Description: A management review per Clause 9.3, conducted by top management to evaluate ongoing AIMS suitability, adequacy, and effectiveness.
--     * Slot: review_date Description: Date when the document is due for review.
--     * Slot: previous_actions_status Description: Status of actions from previous reviews.
--     * Slot: performance_trends Description: Trends in AIMS performance.
--     * Slot: audit_results_summary Description: Summary of audit results.
--     * Slot: risk_assessment_results Description: Summary of AI risk assessment results.
--     * Slot: impact_assessment_results Description: Summary of AI system impact assessment results.
--     * Slot: next_review_date Description: Date of the next review.
--     * Slot: document_type Description: Classification of the documented information.
--     * Slot: document_reference Description: Unique reference number for document control.
--     * Slot: author Description: Person who created the document.
--     * Slot: owner Description: Person accountable for the document content and maintenance.
--     * Slot: approved_by Description: Person who approved the document.
--     * Slot: approved_date Description: Date when the document was approved.
--     * Slot: effective_date Description: Date when the document becomes effective.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: classification Description: Information classification level.
--     * Slot: retention_period Description: Duration for which the document is retained.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: Nonconformity Description: A nonconformity identified per Clause 10.2 representing failure to fulfill an AIMS requirement.
--     * Slot: nonconformity_source Description: Source from which the nonconformity was identified.
--     * Slot: detection_date Description: Date the nonconformity was detected.
--     * Slot: detected_by Description: Person or process that detected the nonconformity.
--     * Slot: requirement_violated Description: Requirement that was violated.
--     * Slot: nonconformity_description Description: Description of the nonconformity.
--     * Slot: consequences_addressed Description: How consequences were addressed.
--     * Slot: root_cause Description: Identified root cause.
--     * Slot: similar_nonconformities_check Description: Check for similar nonconformities.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: closure_date Description: Date when the item was closed.
--     * Slot: closure_evidence Description: Evidence of closure.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CorrectiveAction Description: A corrective action per Clause 10.2 to address the root cause of an AIMS nonconformity and reduce the likelihood of recurrence.
--     * Slot: linked_nonconformity Description: Linked nonconformity.
--     * Slot: action_description Description: Description of the action.
--     * Slot: root_cause_addressed Description: Root cause addressed by the action.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: target_completion_date Description: Target completion date.
--     * Slot: actual_completion_date Description: Actual completion date.
--     * Slot: resources_required Description: Resources required for implementation.
--     * Slot: effectiveness_criteria Description: Criteria for assessing effectiveness.
--     * Slot: effectiveness_review_date Description: Date when effectiveness was reviewed.
--     * Slot: effectiveness_verified Description: Whether effectiveness was verified.
--     * Slot: aims_changes_required Description: Whether AIMS changes are required as a result of the action.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ImprovementOpportunity Description: An opportunity for continual improvement of the AIMS per Clause 10.1.
--     * Slot: improvement_source Description: Source of the improvement opportunity.
--     * Slot: identification_date Description: Date the improvement opportunity was identified.
--     * Slot: identified_by Description: Person who identified the improvement opportunity.
--     * Slot: improvement_description Description: Description of the improvement opportunity.
--     * Slot: expected_benefit Description: Expected benefit of the improvement.
--     * Slot: priority Description: Priority assigned (qualitative level).
--     * Slot: implementation_plan Description: Plan for implementing the improvement.
--     * Slot: responsible_party Description: Party responsible for the activity.
--     * Slot: target_date Description: Target date for achieving the objective.
--     * Slot: actual_completion_date Description: Actual completion date.
--     * Slot: outcome_assessment Description: Assessment of the outcome.
--     * Slot: status Description: Current status of the document or entity.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ThirdPartyRelationship Description: A documented relationship with a third party (supplier, partner, or customer) involved in the AI system life cycle per A.10.
--     * Slot: party_type Description: Category of party.
--     * Slot: party_name Description: Name of the third party.
--     * Slot: contractual_basis Description: Contractual basis of the relationship.
--     * Slot: data_processing_role Description: Role of the third party in data processing (e.g., PII controller, PII processor).
--     * Slot: review_frequency Description: Frequency at which the relationship is reviewed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: SupplierRelationship Description: A supplier relationship covering services, products, or materials (e.g., datasets, models, libraries, full AI systems) provided to the organization per A.10.3.
--     * Slot: monitoring_method Description: How the supplier or customer relationship is monitored.
--     * Slot: party_type Description: Category of party.
--     * Slot: party_name Description: Name of the third party.
--     * Slot: contractual_basis Description: Contractual basis of the relationship.
--     * Slot: data_processing_role Description: Role of the third party in data processing (e.g., PII controller, PII processor).
--     * Slot: review_frequency Description: Frequency at which the relationship is reviewed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: CustomerRelationship Description: A customer relationship for an AI product or service supplied by the organization per A.10.4.
--     * Slot: usage_agreement_reference Description: Reference to the usage agreement with the customer.
--     * Slot: party_type Description: Category of party.
--     * Slot: party_name Description: Name of the third party.
--     * Slot: contractual_basis Description: Contractual basis of the relationship.
--     * Slot: data_processing_role Description: Role of the third party in data processing (e.g., PII controller, PII processor).
--     * Slot: review_frequency Description: Frequency at which the relationship is reviewed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AISystemEvent Description: An AI system event detected by monitoring, users, or external reporting channels. Events may or may not be subsequently classified as incidents. Supports A.6.2.8 event log capture and A.8.3 external reporting workflows.
--     * Slot: event_datetime Description: Date and time the event was observed.
--     * Slot: reporter Description: Identifier or description of the person or system that reported the event.
--     * Slot: reporter_party_type Description: Type of party that reported the event (internal user, external interested party, monitoring system, etc.).
--     * Slot: event_source Description: Source channel through which the event was raised (monitoring, user report, external report, audit).
--     * Slot: event_description Description: Free-text description of the event.
--     * Slot: initial_assessment Description: Initial triage assessment of the event.
--     * Slot: categorized_as_incident Description: Whether the event has been categorized as an incident requiring response.
--     * Slot: linked_incident Description: AI incident linked to the originating event.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIIncident Description: An AI incident, i.e., an AI system event determined to require response, escalation, or external communication. Captures triage, response lifecycle, and communications to users and other interested parties per A.8.4 and A.8.3.
--     * Slot: incident_datetime Description: Date and time the incident was declared or detected.
--     * Slot: incident_category Description: AI-specific category of the incident.
--     * Slot: severity Description: Severity rating of the incident.
--     * Slot: incident_description Description: Free-text description of the incident.
--     * Slot: detection_method Description: How the incident was detected (monitoring alert, user report, external report).
--     * Slot: root_cause Description: Identified root cause.
--     * Slot: notification_required Description: Whether notification to interested parties or authorities is required.
--     * Slot: communication_plan Description: Reference to the communication plan.
--     * Slot: closure_datetime Description: Date and time the incident was closed.
--     * Slot: post_incident_review Description: Reference to the post-incident review record.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: ConcernReport Description: A concern raised by employees, contractors, users, or other interested parties about the organization's role with respect to an AI system. Operationalises Annex A.3.3 (Reporting of concerns). Confidentiality, anonymity, anti-reprisal protection, escalation, and timely response are core attributes; informed by ISO 37002.
--     * Slot: reported_date Description: Date the concern was reported.
--     * Slot: reporter Description: Identifier or description of the person or system that reported the event.
--     * Slot: reporter_party_type Description: Type of party that reported the event (internal user, external interested party, monitoring system, etc.).
--     * Slot: reporter_anonymous Description: Whether the reporter chose to remain anonymous.
--     * Slot: confidentiality_level Description: Confidentiality classification applied to the concern record (e.g., confidential, restricted, internal).
--     * Slot: reporting_channel Description: Channel through which the concern was reported (e.g., hotline, web form, manager, ombudsperson, external auditor).
--     * Slot: concern_description Description: Paraphrased summary of the concern raised.
--     * Slot: severity Description: Severity rating of the incident.
--     * Slot: investigator Description: Identifier or description of the investigator assigned to the concern.
--     * Slot: investigation_status Description: Status of the investigation (e.g., opened, in_progress, closed, escalated, referred_external).
--     * Slot: investigation_findings Description: Paraphrased summary of investigation findings.
--     * Slot: escalation_status Description: Whether and how the concern was escalated (internal management, governing body, external authority).
--     * Slot: response_due_date Description: Target date by which a response is owed to the reporter.
--     * Slot: response_provided_date Description: Date a response was provided to the reporter.
--     * Slot: resolution Description: Paraphrased description of the resolution provided.
--     * Slot: closure_datetime Description: Date and time the incident was closed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity was created.
--     * Slot: modified_date Description: Date when the entity was last modified.
--     * Slot: version Description: Version identifier for the entity.
-- # Class: AIManagementSystem_scope_boundaries
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: scope_boundaries Description: Defined boundaries of the AIMS scope.
-- # Class: AIManagementSystem_scope_exclusions
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: scope_exclusions Description: Any exclusions from scope with justification.
-- # Class: AIManagementSystem_context_internal_issues
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: context_internal_issues Description: Internal issues relevant to the AIMS per Clause 4.1.
-- # Class: AIManagementSystem_context_external_issues
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: context_external_issues Description: External issues relevant to the AIMS per Clause 4.1.
-- # Class: AIManagementSystem_organizational_roles_with_ai
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: organizational_roles_with_ai Description: Documented set of roles the organization plays in the AI ecosystem within the AIMS scope.
-- # Class: AIManagementSystem_integrated_management_systems
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: integrated_management_systems Description: Related management-system standards with which the AIMS is jointly implemented or aligned (Introduction - Compatibility with other management system standards, Annex D).
-- # Class: AIManagementSystem_leadership_commitment_evidence
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: leadership_commitment_evidence Description: Records or references demonstrating top-management leadership and commitment to the AIMS per Clause 5.1.
-- # Class: AIManagementSystem_planned_changes
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: planned_changes Description: Records of planned changes to the AIMS, including purpose, consequences, resource implications, and responsibilities per Clause 6.3.
-- # Class: AIManagementSystem_interested_parties
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: interested_parties_id Description: Stakeholders relevant to the AIMS.
-- # Class: AIManagementSystem_ai_objectives
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_objectives_id Description: AI objectives established by the organization.
-- # Class: AIManagementSystem_reference_controls
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: reference_controls_id Description: AI reference controls applied within the AIMS.
-- # Class: AIManagementSystem_ai_systems
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_systems_id Description: AI systems within the AIMS scope.
-- # Class: AIManagementSystem_roles
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: roles_id Description: AI-related roles defined in the AIMS.
-- # Class: AIManagementSystem_resources
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: resources_id Description: Resources provided for the AIMS.
-- # Class: AIManagementSystem_competence_records
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: competence_records_id Description: Competence records for personnel.
-- # Class: AIManagementSystem_documented_information_register
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: documented_information_register_id Description: Register of all documented information.
-- # Class: AIManagementSystem_operational_procedures
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: operational_procedures_id Description: Operational procedures of the AIMS.
-- # Class: AIManagementSystem_ai_risk_assessments
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_risk_assessments_id Description: AI risk assessment instances.
-- # Class: AIManagementSystem_ai_risk_treatment_plans
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_risk_treatment_plans_id Description: AI risk treatment plans.
-- # Class: AIManagementSystem_ai_system_impact_assessments
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_system_impact_assessments_id Description: AI system impact assessment instances.
-- # Class: AIManagementSystem_internal_audits
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: internal_audits_id Description: Internal audits conducted.
-- # Class: AIManagementSystem_management_reviews
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: management_reviews_id Description: Management reviews of the AIMS.
-- # Class: AIManagementSystem_nonconformities
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: nonconformities_id Description: Nonconformities identified.
-- # Class: AIManagementSystem_corrective_actions
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: corrective_actions_id Description: Corrective actions taken.
-- # Class: AIManagementSystem_improvements
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: improvements_id Description: Improvement opportunities being tracked.
-- # Class: AIManagementSystem_third_party_relationships
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: third_party_relationships_id Description: Third-party relationships within the AIMS scope.
-- # Class: AIManagementSystem_ai_system_events
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_system_events_id Description: AI system events recorded under the AIMS.
-- # Class: AIManagementSystem_ai_incidents
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: ai_incidents_id Description: AI incidents managed under the AIMS.
-- # Class: AIManagementSystem_concern_reports
--     * Slot: AIManagementSystem_id Description: Autocreated FK slot
--     * Slot: concern_reports_id Description: Concern reports raised and managed under the AIMS per A.3.3.
-- # Class: Organization_trading_names
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: trading_names Description: Names under which the organization conducts business.
-- # Class: Organization_sector_domains
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: sector_domains Description: Application sectors in which the organization deploys AI systems, drawn from the Annex D examples; supports identification of sector- specific management system standards that integrate with the AIMS.
-- # Class: Organization_geographic_locations
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: geographic_locations Description: Countries or regions where the organization operates.
-- # Class: Organization_regulatory_jurisdictions
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: regulatory_jurisdictions Description: Jurisdictions whose regulations apply to the organization.
-- # Class: Organization_subsidiaries
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: subsidiaries Description: Subsidiary organizations if applicable.
-- # Class: Organization_ai_roles
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: ai_roles Description: Roles the organization takes with respect to AI systems (provider, producer, customer, partner, subject, authority).
-- # Class: InterestedParty_requirements
--     * Slot: InterestedParty_id Description: Autocreated FK slot
--     * Slot: requirements Description: Requirements of the interested party.
-- # Class: AIPolicy_commitment_statements
--     * Slot: AIPolicy_id Description: Autocreated FK slot
--     * Slot: commitment_statements Description: Statements of commitment included in the policy.
-- # Class: AIPolicy_related_topic_policies
--     * Slot: AIPolicy_id Description: Autocreated FK slot
--     * Slot: related_topic_policies_id Description: Topic-specific policies supporting this policy.
-- # Class: TopicSpecificPolicy_applicable_controls
--     * Slot: TopicSpecificPolicy_id Description: Autocreated FK slot
--     * Slot: applicable_controls_id Description: Reference controls related to this policy or AI system.
-- # Class: Role_responsibilities
--     * Slot: Role_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Responsibilities assigned to the role.
-- # Class: Role_authorities
--     * Slot: Role_id Description: Autocreated FK slot
--     * Slot: authorities Description: Authorities granted to the role.
-- # Class: Role_assigned_to
--     * Slot: Role_id Description: Autocreated FK slot
--     * Slot: assigned_to Description: Person(s) assigned to this role or resource.
-- # Class: AIObjective_related_risks
--     * Slot: AIObjective_id Description: Autocreated FK slot
--     * Slot: related_risks_id Description: Associated AI risks.
-- # Class: AIObjective_related_controls
--     * Slot: AIObjective_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Other reference controls related to this one.
-- # Class: AIRiskAssessmentProcess_trigger_events
--     * Slot: AIRiskAssessmentProcess_id Description: Autocreated FK slot
--     * Slot: trigger_events Description: Events that trigger an assessment outside the planned schedule.
-- # Class: AIRiskAssessment_ai_systems_assessed
--     * Slot: AIRiskAssessment_id Description: Autocreated FK slot
--     * Slot: ai_systems_assessed_id Description: AI systems covered by this assessment.
-- # Class: AIRiskAssessment_risks_identified
--     * Slot: AIRiskAssessment_id Description: Autocreated FK slot
--     * Slot: risks_identified_id Description: Risks identified in this assessment.
-- # Class: AIRiskAssessment_recommendations
--     * Slot: AIRiskAssessment_id Description: Autocreated FK slot
--     * Slot: recommendations Description: Recommendations from the assessment.
-- # Class: AIRisk_affected_ai_systems
--     * Slot: AIRisk_id Description: Autocreated FK slot
--     * Slot: affected_ai_systems_id Description: AI systems affected by this risk.
-- # Class: AIRisk_affected_dimensions
--     * Slot: AIRisk_id Description: Autocreated FK slot
--     * Slot: affected_dimensions Description: Dimensions of impact affected by the risk (individual, group, societal, safety, privacy, security, environmental).
-- # Class: AIRisk_existing_controls
--     * Slot: AIRisk_id Description: Autocreated FK slot
--     * Slot: existing_controls_id Description: Controls currently in place affecting this risk.
-- # Class: AIRiskTreatmentPlan_risks_addressed
--     * Slot: AIRiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: risks_addressed_id Description: Risks addressed by this plan.
-- # Class: AIRiskTreatmentPlan_treatment_actions
--     * Slot: AIRiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: treatment_actions Description: Actions to be taken for treatment.
-- # Class: AIRiskTreatmentPlan_controls_to_implement
--     * Slot: AIRiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: controls_to_implement_id Description: Controls to be implemented as part of treatment.
-- # Class: AIRiskTreatmentPlan_responsible_parties
--     * Slot: AIRiskTreatmentPlan_id Description: Autocreated FK slot
--     * Slot: responsible_parties Description: Parties responsible for implementation.
-- # Class: AISystemImpactAssessmentProcess_dimensions_in_scope
--     * Slot: AISystemImpactAssessmentProcess_id Description: Autocreated FK slot
--     * Slot: dimensions_in_scope Description: Impact dimensions evaluated by the process.
-- # Class: AISystemImpactAssessmentProcess_trigger_events
--     * Slot: AISystemImpactAssessmentProcess_id Description: Autocreated FK slot
--     * Slot: trigger_events Description: Events that trigger an assessment outside the planned schedule.
-- # Class: AISystemImpactAssessment_ai_systems_assessed
--     * Slot: AISystemImpactAssessment_id Description: Autocreated FK slot
--     * Slot: ai_systems_assessed_id Description: AI systems covered by this assessment.
-- # Class: AISystemImpactAssessment_applicable_jurisdictions
--     * Slot: AISystemImpactAssessment_id Description: Autocreated FK slot
--     * Slot: applicable_jurisdictions Description: Jurisdictions relevant to the assessment.
-- # Class: AISystemImpactAssessment_dimensions_assessed
--     * Slot: AISystemImpactAssessment_id Description: Autocreated FK slot
--     * Slot: dimensions_assessed Description: Impact dimensions actually assessed in this instance.
-- # Class: AISystemImpactAssessment_identified_consequences
--     * Slot: AISystemImpactAssessment_id Description: Autocreated FK slot
--     * Slot: identified_consequences Description: Identified positive or negative consequences.
-- # Class: AISystemImpactAssessment_mitigations
--     * Slot: AISystemImpactAssessment_id Description: Autocreated FK slot
--     * Slot: mitigations Description: Mitigations to address identified consequences.
-- # Class: AISystemImpactAssessment_shared_with_parties
--     * Slot: AISystemImpactAssessment_id Description: Autocreated FK slot
--     * Slot: shared_with_parties Description: Interested parties with whom the results have been shared.
-- # Class: StatementOfApplicability_soa_entries
--     * Slot: StatementOfApplicability_id Description: Autocreated FK slot
--     * Slot: soa_entries_id Description: Individual control entries in the SoA.
-- # Class: AIReferenceControl_related_controls
--     * Slot: AIReferenceControl_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Other reference controls related to this one.
-- # Class: AIReferenceControl_applicable_risk_sources
--     * Slot: AIReferenceControl_id Description: Autocreated FK slot
--     * Slot: applicable_risk_sources Description: Categories of AI risk source this control addresses.
-- # Class: AIReferenceControl_applicable_objectives
--     * Slot: AIReferenceControl_id Description: Autocreated FK slot
--     * Slot: applicable_objectives Description: AI objective categories this control supports.
-- # Class: AIReferenceControl_evidence_references
--     * Slot: AIReferenceControl_id Description: Autocreated FK slot
--     * Slot: evidence_references Description: References to evidence of implementation.
-- # Class: AISystem_intended_uses
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: intended_uses Description: Documented intended uses of the AI system.
-- # Class: AISystem_foreseeable_misuse
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: foreseeable_misuse Description: Reasonably foreseeable misuse of the AI system.
-- # Class: AISystem_human_oversight_stages
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: human_oversight_stages Description: AI system life cycle stages at which human oversight applies (Annex B.9.3).
-- # Class: AISystem_data_resources
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: data_resources_id Description: Data resources used by the AI system.
-- # Class: AISystem_tooling_resources
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: tooling_resources_id Description: Tooling resources used by the AI system.
-- # Class: AISystem_computing_resources
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: computing_resources_id Description: System and computing resources used by the AI system.
-- # Class: AISystem_human_resources
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: human_resources_id Description: Human resources involved with the AI system.
-- # Class: AISystem_technical_documentation
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: technical_documentation Description: Reference to AI system technical documentation.
-- # Class: AISystem_applicable_controls
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: applicable_controls_id Description: Reference controls related to this policy or AI system.
-- # Class: AISystem_related_impact_assessments
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: related_impact_assessments_id Description: Impact assessments related to this AI system.
-- # Class: AISystem_supplier_relationships
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: supplier_relationships_id Description: Supplier relationships relevant to this AI system.
-- # Class: AISystem_customer_relationships
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: customer_relationships_id Description: Customer relationships relevant to this AI system.
-- # Class: DataResource_data_quality_requirements
--     * Slot: DataResource_id Description: Autocreated FK slot
--     * Slot: data_quality_requirements Description: Documented data quality requirements for the AI system.
-- # Class: DataResource_data_quality_metrics
--     * Slot: DataResource_id Description: Autocreated FK slot
--     * Slot: data_quality_metrics Description: Measured data quality metrics.
-- # Class: DataResource_data_preparation_methods
--     * Slot: DataResource_id Description: Autocreated FK slot
--     * Slot: data_preparation_methods Description: Data preparation methods used (e.g., scaling, encoding, cleaning) per Annex A.7.6.
-- # Class: DataResource_known_bias_issues
--     * Slot: DataResource_id Description: Autocreated FK slot
--     * Slot: known_bias_issues Description: Known or potential bias issues in the data.
-- # Class: HumanResource_required_competencies
--     * Slot: HumanResource_id Description: Autocreated FK slot
--     * Slot: required_competencies Description: Competencies required for the role.
-- # Class: HumanResource_assigned_to
--     * Slot: HumanResource_id Description: Autocreated FK slot
--     * Slot: assigned_to Description: Person(s) assigned to this role or resource.
-- # Class: HumanResource_lifecycle_responsibilities
--     * Slot: HumanResource_id Description: Autocreated FK slot
--     * Slot: lifecycle_responsibilities Description: Life cycle responsibilities allocated to this human resource.
-- # Class: CompetenceRecord_required_competencies
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: required_competencies Description: Competencies required for the role.
-- # Class: CompetenceRecord_education_records
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: education_records Description: Education qualifications.
-- # Class: CompetenceRecord_training_records
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: training_records Description: Training completed.
-- # Class: CompetenceRecord_experience_records
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: experience_records Description: Relevant experience.
-- # Class: CompetenceRecord_competency_gaps
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: competency_gaps Description: Identified competency gaps.
-- # Class: CompetenceRecord_development_actions
--     * Slot: CompetenceRecord_id Description: Autocreated FK slot
--     * Slot: development_actions Description: Actions to address competency gaps.
-- # Class: AwarenessProgram_awareness_topics
--     * Slot: AwarenessProgram_id Description: Autocreated FK slot
--     * Slot: awareness_topics Description: Topics covered in the awareness program.
-- # Class: AwarenessProgram_delivery_methods
--     * Slot: AwarenessProgram_id Description: Autocreated FK slot
--     * Slot: delivery_methods Description: Methods used to deliver awareness content.
-- # Class: CommunicationPlan_communication_items
--     * Slot: CommunicationPlan_id Description: Autocreated FK slot
--     * Slot: communication_items_id Description: Communication items in the plan.
-- # Class: OperationalProcedure_control_measures
--     * Slot: OperationalProcedure_id Description: Autocreated FK slot
--     * Slot: control_measures Description: Control measures applied.
-- # Class: OperationalProcedure_responsible_roles
--     * Slot: OperationalProcedure_id Description: Autocreated FK slot
--     * Slot: responsible_roles_id Description: Roles responsible for the process.
-- # Class: OperationalProcedure_related_controls
--     * Slot: OperationalProcedure_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Other reference controls related to this one.
-- # Class: MonitoringProgram_monitoring_items
--     * Slot: MonitoringProgram_id Description: Autocreated FK slot
--     * Slot: monitoring_items_id Description: Items to be monitored.
-- # Class: InternalAudit_audit_team
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: audit_team Description: Members of the audit team.
-- # Class: InternalAudit_auditee_representatives
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: auditee_representatives Description: Representatives of the auditee.
-- # Class: InternalAudit_findings
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: findings_id Description: Findings from the audit.
-- # Class: InternalAudit_positive_observations
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: positive_observations Description: Positive observations from the audit.
-- # Class: InternalAudit_report_distribution
--     * Slot: InternalAudit_id Description: Autocreated FK slot
--     * Slot: report_distribution Description: Distribution list for the audit report.
-- # Class: AuditProgramme_planned_audits
--     * Slot: AuditProgramme_id Description: Autocreated FK slot
--     * Slot: planned_audits_id Description: Audits planned within the programme.
-- # Class: ManagementReview_attendees
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: attendees Description: Attendees of the review.
-- # Class: ManagementReview_context_changes
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: context_changes Description: Changes in external or internal context.
-- # Class: ManagementReview_interested_party_changes
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: interested_party_changes Description: Changes in interested party needs and expectations.
-- # Class: ManagementReview_improvement_opportunities
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: improvement_opportunities_id Description: Improvement opportunities identified.
-- # Class: ManagementReview_decisions
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: decisions Description: Decisions made during the review.
-- # Class: ManagementReview_action_items
--     * Slot: ManagementReview_id Description: Autocreated FK slot
--     * Slot: action_items Description: Action items resulting from the review.
-- # Class: Nonconformity_immediate_actions
--     * Slot: Nonconformity_id Description: Autocreated FK slot
--     * Slot: immediate_actions Description: Immediate actions taken.
-- # Class: Nonconformity_linked_corrective_actions
--     * Slot: Nonconformity_id Description: Autocreated FK slot
--     * Slot: linked_corrective_actions_id Description: Linked corrective actions.
-- # Class: ThirdPartyRelationship_allocated_responsibilities
--     * Slot: ThirdPartyRelationship_id Description: Autocreated FK slot
--     * Slot: allocated_responsibilities Description: Responsibilities allocated to the third party.
-- # Class: ThirdPartyRelationship_ai_systems_involved
--     * Slot: ThirdPartyRelationship_id Description: Autocreated FK slot
--     * Slot: ai_systems_involved_id Description: AI systems involved in the third-party relationship.
-- # Class: ThirdPartyRelationship_lifecycle_stages_involved
--     * Slot: ThirdPartyRelationship_id Description: Autocreated FK slot
--     * Slot: lifecycle_stages_involved Description: AI life cycle stages where the third party is involved.
-- # Class: ThirdPartyRelationship_assurance_evidence
--     * Slot: ThirdPartyRelationship_id Description: Autocreated FK slot
--     * Slot: assurance_evidence Description: Evidence of assurance over the third party's conformance with the organization's responsible AI approach.
-- # Class: SupplierRelationship_supplier_assessment_criteria
--     * Slot: SupplierRelationship_id Description: Autocreated FK slot
--     * Slot: supplier_assessment_criteria Description: Criteria for assessing the supplier.
-- # Class: SupplierRelationship_corrective_actions_required
--     * Slot: SupplierRelationship_id Description: Autocreated FK slot
--     * Slot: corrective_actions_required Description: Corrective actions required of the supplier.
-- # Class: SupplierRelationship_allocated_responsibilities
--     * Slot: SupplierRelationship_id Description: Autocreated FK slot
--     * Slot: allocated_responsibilities Description: Responsibilities allocated to the third party.
-- # Class: SupplierRelationship_ai_systems_involved
--     * Slot: SupplierRelationship_id Description: Autocreated FK slot
--     * Slot: ai_systems_involved_id Description: AI systems involved in the third-party relationship.
-- # Class: SupplierRelationship_lifecycle_stages_involved
--     * Slot: SupplierRelationship_id Description: Autocreated FK slot
--     * Slot: lifecycle_stages_involved Description: AI life cycle stages where the third party is involved.
-- # Class: SupplierRelationship_assurance_evidence
--     * Slot: SupplierRelationship_id Description: Autocreated FK slot
--     * Slot: assurance_evidence Description: Evidence of assurance over the third party's conformance with the organization's responsible AI approach.
-- # Class: CustomerRelationship_customer_expectations
--     * Slot: CustomerRelationship_id Description: Autocreated FK slot
--     * Slot: customer_expectations Description: Documented customer expectations and needs.
-- # Class: CustomerRelationship_communicated_limitations
--     * Slot: CustomerRelationship_id Description: Autocreated FK slot
--     * Slot: communicated_limitations Description: Limitations of the AI system that are communicated to the customer.
-- # Class: CustomerRelationship_allocated_responsibilities
--     * Slot: CustomerRelationship_id Description: Autocreated FK slot
--     * Slot: allocated_responsibilities Description: Responsibilities allocated to the third party.
-- # Class: CustomerRelationship_ai_systems_involved
--     * Slot: CustomerRelationship_id Description: Autocreated FK slot
--     * Slot: ai_systems_involved_id Description: AI systems involved in the third-party relationship.
-- # Class: CustomerRelationship_lifecycle_stages_involved
--     * Slot: CustomerRelationship_id Description: Autocreated FK slot
--     * Slot: lifecycle_stages_involved Description: AI life cycle stages where the third party is involved.
-- # Class: CustomerRelationship_assurance_evidence
--     * Slot: CustomerRelationship_id Description: Autocreated FK slot
--     * Slot: assurance_evidence Description: Evidence of assurance over the third party's conformance with the organization's responsible AI approach.
-- # Class: AISystemEvent_affected_ai_systems
--     * Slot: AISystemEvent_id Description: Autocreated FK slot
--     * Slot: affected_ai_systems_id Description: AI systems affected by this risk.
-- # Class: AIIncident_affected_ai_systems
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: affected_ai_systems_id Description: AI systems affected by this risk.
-- # Class: AIIncident_affected_dimensions
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: affected_dimensions Description: Dimensions of impact affected by the risk (individual, group, societal, safety, privacy, security, environmental).
-- # Class: AIIncident_response_actions
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: response_actions Description: Response actions taken for the incident.
-- # Class: AIIncident_containment_actions
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: containment_actions Description: Containment actions taken to limit incident impact.
-- # Class: AIIncident_recovery_actions
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: recovery_actions Description: Recovery actions taken to restore normal AI system operation.
-- # Class: AIIncident_lessons_learned
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: lessons_learned Description: Lessons learned recorded after incident closure.
-- # Class: AIIncident_evidence_collected
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: evidence_collected Description: References to evidence collected during incident response.
-- # Class: AIIncident_notifications_made
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: notifications_made Description: Notifications actually made (user communications, regulator filings).
-- # Class: AIIncident_external_reports
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: external_reports Description: External reports received or filed regarding the incident.
-- # Class: AIIncident_linked_corrective_actions
--     * Slot: AIIncident_id Description: Autocreated FK slot
--     * Slot: linked_corrective_actions_id Description: Linked corrective actions.
-- # Class: ConcernReport_concern_ai_systems
--     * Slot: ConcernReport_id Description: Autocreated FK slot
--     * Slot: concern_ai_systems_id Description: AI systems referenced in the concern report.
-- # Class: ConcernReport_concern_lifecycle_stage
--     * Slot: ConcernReport_id Description: Autocreated FK slot
--     * Slot: concern_lifecycle_stage Description: AI system life cycle stage(s) at which the concern arose.
-- # Class: ConcernReport_reprisal_protection_actions
--     * Slot: ConcernReport_id Description: Autocreated FK slot
--     * Slot: reprisal_protection_actions Description: Actions taken to protect the reporter from reprisals or detriment (informed by ISO 37002).
-- # Class: ConcernReport_related_incidents
--     * Slot: ConcernReport_id Description: Autocreated FK slot
--     * Slot: related_incidents_id Description: AI incidents linked to this concern report.
-- # Class: ConcernReport_related_nonconformities
--     * Slot: ConcernReport_id Description: Autocreated FK slot
--     * Slot: related_nonconformities_id Description: Nonconformities linked to this concern report.

CREATE TABLE "NamedEntity" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedEntity_id" ON "NamedEntity" (id);

CREATE TABLE "DocumentedInformation" (
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DocumentedInformation_id" ON "DocumentedInformation" (id);

CREATE TABLE "Organization" (
	legal_name TEXT,
	organization_type TEXT,
	industry_sector TEXT,
	size_category TEXT,
	employee_count INTEGER,
	parent_organization TEXT,
	climate_change_relevant BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Organization_id" ON "Organization" (id);

CREATE TABLE "InterestedParty" (
	party_type TEXT,
	relationship TEXT,
	communication_needs TEXT,
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InterestedParty_id" ON "InterestedParty" (id);

CREATE TABLE "AIPolicy" (
	policy_statement TEXT,
	policy_objectives_framework TEXT,
	applicability_statement TEXT,
	communication_date DATE,
	acknowledgment_required BOOLEAN,
	last_policy_review_date DATE,
	next_policy_review_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIPolicy_id" ON "AIPolicy" (id);

CREATE TABLE "Role" (
	role_type TEXT,
	accountability TEXT,
	delegation_rules TEXT,
	reporting_line TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Role_id" ON "Role" (id);

CREATE TABLE "AIRiskAssessmentProcess" (
	risk_acceptance_criteria TEXT,
	assessment_criteria TEXT,
	assessment_methodology TEXT,
	likelihood_scale TEXT,
	impact_scale TEXT,
	risk_matrix TEXT,
	assessment_frequency TEXT,
	alignment_with_ai_policy TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIRiskAssessmentProcess_id" ON "AIRiskAssessmentProcess" (id);

CREATE TABLE "AIRiskTreatmentProcess" (
	treatment_options_guidance TEXT,
	control_selection_criteria TEXT,
	soa_template TEXT,
	approval_workflow TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIRiskTreatmentProcess_id" ON "AIRiskTreatmentProcess" (id);

CREATE TABLE "AIRiskTreatmentPlan" (
	plan_scope TEXT,
	resources_required TEXT,
	implementation_timeline TEXT,
	risk_owner_approval TEXT,
	approved_date DATE,
	residual_risk_acceptance TEXT,
	implementation_status VARCHAR(14),
	completion_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIRiskTreatmentPlan_id" ON "AIRiskTreatmentPlan" (id);

CREATE TABLE "AISystemImpactAssessmentProcess" (
	assessment_criteria TEXT,
	assessment_methodology TEXT,
	assessment_frequency TEXT,
	linkage_to_risk_assessment TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AISystemImpactAssessmentProcess_id" ON "AISystemImpactAssessmentProcess" (id);

CREATE TABLE "AISystemImpactAssessment" (
	assessment_scope TEXT,
	assessment_date DATE,
	assessor TEXT,
	technical_context TEXT,
	societal_context TEXT,
	next_assessment_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_id" ON "AISystemImpactAssessment" (id);

CREATE TABLE "StatementOfApplicability" (
	total_controls INTEGER,
	implemented_count INTEGER,
	planned_count INTEGER,
	not_applicable_count INTEGER,
	last_review_date DATE,
	approved_by TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StatementOfApplicability_id" ON "StatementOfApplicability" (id);

CREATE TABLE "AIReferenceControl" (
	control_id TEXT,
	control_title TEXT,
	control_family VARCHAR(25),
	control_text TEXT,
	implementation_guidance TEXT,
	control_owner TEXT,
	implementation_status VARCHAR(14),
	implementation_date DATE,
	effectiveness_rating TEXT,
	last_test_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIReferenceControl_id" ON "AIReferenceControl" (id);

CREATE TABLE "AISystem" (
	ai_system_purpose TEXT,
	application_domain TEXT,
	deployment_context TEXT,
	lifecycle_stage VARCHAR(31),
	organization_role VARCHAR(18),
	autonomy_level TEXT,
	ml_approach VARCHAR(15),
	human_oversight_required BOOLEAN,
	human_oversight_description TEXT,
	learning_mode VARCHAR(22),
	event_log_policy TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AISystem_id" ON "AISystem" (id);

CREATE TABLE "DataResource" (
	data_resource_category VARCHAR(10),
	source TEXT,
	acquisition_method TEXT,
	data_provenance TEXT,
	labelling_process TEXT,
	last_updated_date DATE,
	retention_policy TEXT,
	data_classification TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DataResource_id" ON "DataResource" (id);

CREATE TABLE "ToolingResource" (
	tool_category TEXT,
	tool_version TEXT,
	vendor TEXT,
	license_terms TEXT,
	usage_purpose TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ToolingResource_id" ON "ToolingResource" (id);

CREATE TABLE "ComputingResource" (
	resource_class TEXT,
	quantity TEXT,
	location TEXT,
	environment_type TEXT,
	cost TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComputingResource_id" ON "ComputingResource" (id);

CREATE TABLE "HumanResource" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HumanResource_id" ON "HumanResource" (id);

CREATE TABLE "Resource" (
	resource_type TEXT,
	quantity TEXT,
	allocation_date DATE,
	allocated_to TEXT,
	cost TEXT,
	availability_status TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "CompetenceRecord" (
	person_name TEXT,
	person_role TEXT,
	competency_assessment_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CompetenceRecord_id" ON "CompetenceRecord" (id);

CREATE TABLE "AwarenessProgram" (
	target_audience TEXT,
	frequency TEXT,
	completion_tracking TEXT,
	effectiveness_measures TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AwarenessProgram_id" ON "AwarenessProgram" (id);

CREATE TABLE "CommunicationPlan" (
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CommunicationPlan_id" ON "CommunicationPlan" (id);

CREATE TABLE "CommunicationItem" (
	id INTEGER NOT NULL,
	subject TEXT,
	purpose TEXT,
	audience TEXT,
	frequency TEXT,
	method TEXT,
	responsible_party TEXT,
	records_required TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CommunicationItem_id" ON "CommunicationItem" (id);

CREATE TABLE "OperationalProcedure" (
	procedure_scope TEXT,
	process_criteria TEXT,
	change_control_requirements TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OperationalProcedure_id" ON "OperationalProcedure" (id);

CREATE TABLE "MonitoringProgram" (
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MonitoringProgram_id" ON "MonitoringProgram" (id);

CREATE TABLE "MonitoringItem" (
	id INTEGER NOT NULL,
	metric_name TEXT,
	metric_description TEXT,
	measurement_method TEXT,
	measurement_frequency TEXT,
	responsible_party TEXT,
	analysis_frequency TEXT,
	analyst TEXT,
	target_threshold TEXT,
	alert_threshold TEXT,
	current_value TEXT,
	trend TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MonitoringItem_id" ON "MonitoringItem" (id);

CREATE TABLE "InternalAudit" (
	audit_reference TEXT,
	audit_type VARCHAR(21),
	audit_scope TEXT,
	audit_criteria TEXT,
	audit_objectives TEXT,
	audit_period_start DATE,
	audit_period_end DATE,
	lead_auditor TEXT,
	audit_plan TEXT,
	audit_conclusion TEXT,
	report_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InternalAudit_id" ON "InternalAudit" (id);

CREATE TABLE "AuditProgramme" (
	programme_period TEXT,
	audit_frequency_rationale TEXT,
	resource_requirements TEXT,
	auditor_qualifications TEXT,
	programme_status TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AuditProgramme_id" ON "AuditProgramme" (id);

CREATE TABLE "ManagementReview" (
	review_date DATE,
	previous_actions_status TEXT,
	performance_trends TEXT,
	audit_results_summary TEXT,
	risk_assessment_results TEXT,
	impact_assessment_results TEXT,
	next_review_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ManagementReview_id" ON "ManagementReview" (id);

CREATE TABLE "Nonconformity" (
	nonconformity_source TEXT,
	detection_date DATE,
	detected_by TEXT,
	requirement_violated TEXT,
	nonconformity_description TEXT,
	consequences_addressed TEXT,
	root_cause TEXT,
	similar_nonconformities_check TEXT,
	status TEXT,
	closure_date DATE,
	closure_evidence TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Nonconformity_id" ON "Nonconformity" (id);

CREATE TABLE "ImprovementOpportunity" (
	improvement_source TEXT,
	identification_date DATE,
	identified_by TEXT,
	improvement_description TEXT,
	expected_benefit TEXT,
	priority VARCHAR(8),
	implementation_plan TEXT,
	responsible_party TEXT,
	target_date DATE,
	actual_completion_date DATE,
	outcome_assessment TEXT,
	status TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ImprovementOpportunity_id" ON "ImprovementOpportunity" (id);

CREATE TABLE "ThirdPartyRelationship" (
	party_type TEXT,
	party_name TEXT,
	contractual_basis TEXT,
	data_processing_role TEXT,
	review_frequency TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ThirdPartyRelationship_id" ON "ThirdPartyRelationship" (id);

CREATE TABLE "SupplierRelationship" (
	monitoring_method TEXT,
	party_type TEXT,
	party_name TEXT,
	contractual_basis TEXT,
	data_processing_role TEXT,
	review_frequency TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SupplierRelationship_id" ON "SupplierRelationship" (id);

CREATE TABLE "CustomerRelationship" (
	usage_agreement_reference TEXT,
	party_type TEXT,
	party_name TEXT,
	contractual_basis TEXT,
	data_processing_role TEXT,
	review_frequency TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CustomerRelationship_id" ON "CustomerRelationship" (id);

CREATE TABLE "ConcernReport" (
	reported_date DATE,
	reporter TEXT,
	reporter_party_type TEXT,
	reporter_anonymous BOOLEAN,
	confidentiality_level TEXT,
	reporting_channel TEXT,
	concern_description TEXT,
	severity VARCHAR(8),
	investigator TEXT,
	investigation_status TEXT,
	investigation_findings TEXT,
	escalation_status TEXT,
	response_due_date DATE,
	response_provided_date DATE,
	resolution TEXT,
	closure_datetime DATETIME,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ConcernReport_id" ON "ConcernReport" (id);

CREATE TABLE "AIManagementSystem" (
	organization TEXT,
	scope_statement TEXT,
	top_management TEXT,
	governing_body TEXT,
	ai_policy TEXT,
	ai_risk_assessment_process TEXT,
	ai_risk_treatment_process TEXT,
	ai_system_impact_assessment_process TEXT,
	statement_of_applicability TEXT,
	awareness_program TEXT,
	communication_plan TEXT,
	monitoring_program TEXT,
	certification_status TEXT,
	certification_body TEXT,
	certification_date DATE,
	recertification_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(organization) REFERENCES "Organization" (id),
	FOREIGN KEY(ai_policy) REFERENCES "AIPolicy" (id),
	FOREIGN KEY(ai_risk_assessment_process) REFERENCES "AIRiskAssessmentProcess" (id),
	FOREIGN KEY(ai_risk_treatment_process) REFERENCES "AIRiskTreatmentProcess" (id),
	FOREIGN KEY(ai_system_impact_assessment_process) REFERENCES "AISystemImpactAssessmentProcess" (id),
	FOREIGN KEY(statement_of_applicability) REFERENCES "StatementOfApplicability" (id),
	FOREIGN KEY(awareness_program) REFERENCES "AwarenessProgram" (id),
	FOREIGN KEY(communication_plan) REFERENCES "CommunicationPlan" (id),
	FOREIGN KEY(monitoring_program) REFERENCES "MonitoringProgram" (id)
);
CREATE INDEX "ix_AIManagementSystem_id" ON "AIManagementSystem" (id);

CREATE TABLE "TopicSpecificPolicy" (
	topic_area TEXT,
	parent_policy TEXT,
	target_audience TEXT,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(parent_policy) REFERENCES "AIPolicy" (id)
);
CREATE INDEX "ix_TopicSpecificPolicy_id" ON "TopicSpecificPolicy" (id);

CREATE TABLE "AIObjective" (
	objective_statement TEXT,
	objective_category VARCHAR(29),
	target_value TEXT,
	current_value TEXT,
	metric_definition TEXT,
	measurement_method TEXT,
	measurement_frequency TEXT,
	responsible_role TEXT,
	resources_required TEXT,
	target_date DATE,
	achievement_status TEXT,
	action_plan TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(responsible_role) REFERENCES "Role" (id)
);
CREATE INDEX "ix_AIObjective_id" ON "AIObjective" (id);

CREATE TABLE "AIRiskAssessment" (
	assessment_scope TEXT,
	assessment_date DATE,
	assessor TEXT,
	methodology_used TEXT,
	linked_impact_assessment TEXT,
	summary_findings TEXT,
	next_assessment_date DATE,
	document_type VARCHAR(23),
	document_reference TEXT,
	author TEXT,
	owner TEXT,
	approved_by TEXT,
	approved_date DATE,
	effective_date DATE,
	review_date DATE,
	status TEXT,
	classification TEXT,
	retention_period TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(linked_impact_assessment) REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AIRiskAssessment_id" ON "AIRiskAssessment" (id);

CREATE TABLE "AIRisk" (
	risk_source_category VARCHAR(38),
	risk_source_description TEXT,
	risk_owner TEXT,
	likelihood VARCHAR(14),
	impact VARCHAR(10),
	inherent_risk_level VARCHAR(8),
	residual_risk_level VARCHAR(8),
	risk_treatment_option VARCHAR(6),
	treatment_priority TEXT,
	related_treatment_plan TEXT,
	related_impact_assessment TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(related_treatment_plan) REFERENCES "AIRiskTreatmentPlan" (id),
	FOREIGN KEY(related_impact_assessment) REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AIRisk_id" ON "AIRisk" (id);

CREATE TABLE "SoAEntry" (
	id INTEGER NOT NULL,
	control_reference TEXT,
	is_applicable BOOLEAN,
	inclusion_justification TEXT,
	exclusion_justification TEXT,
	implementation_status VARCHAR(14),
	implementation_evidence TEXT,
	responsible_role TEXT,
	target_implementation_date DATE,
	PRIMARY KEY (id),
	FOREIGN KEY(control_reference) REFERENCES "AIReferenceControl" (id),
	FOREIGN KEY(responsible_role) REFERENCES "Role" (id)
);
CREATE INDEX "ix_SoAEntry_id" ON "SoAEntry" (id);

CREATE TABLE "CorrectiveAction" (
	linked_nonconformity TEXT,
	action_description TEXT,
	root_cause_addressed TEXT,
	responsible_party TEXT,
	target_completion_date DATE,
	actual_completion_date DATE,
	resources_required TEXT,
	effectiveness_criteria TEXT,
	effectiveness_review_date DATE,
	effectiveness_verified BOOLEAN,
	aims_changes_required BOOLEAN,
	status TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(linked_nonconformity) REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_CorrectiveAction_id" ON "CorrectiveAction" (id);

CREATE TABLE "AIIncident" (
	incident_datetime DATETIME,
	incident_category VARCHAR(23),
	severity VARCHAR(8),
	incident_description TEXT,
	detection_method TEXT,
	root_cause TEXT,
	notification_required BOOLEAN,
	communication_plan TEXT,
	closure_datetime DATETIME,
	post_incident_review TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(communication_plan) REFERENCES "CommunicationPlan" (id)
);
CREATE INDEX "ix_AIIncident_id" ON "AIIncident" (id);

CREATE TABLE "Organization_trading_names" (
	"Organization_id" TEXT,
	trading_names TEXT,
	PRIMARY KEY ("Organization_id", trading_names),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_trading_names_trading_names" ON "Organization_trading_names" (trading_names);
CREATE INDEX "ix_Organization_trading_names_Organization_id" ON "Organization_trading_names" ("Organization_id");

CREATE TABLE "Organization_sector_domains" (
	"Organization_id" TEXT,
	sector_domains VARCHAR(18),
	PRIMARY KEY ("Organization_id", sector_domains),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_sector_domains_sector_domains" ON "Organization_sector_domains" (sector_domains);
CREATE INDEX "ix_Organization_sector_domains_Organization_id" ON "Organization_sector_domains" ("Organization_id");

CREATE TABLE "Organization_geographic_locations" (
	"Organization_id" TEXT,
	geographic_locations TEXT,
	PRIMARY KEY ("Organization_id", geographic_locations),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_geographic_locations_Organization_id" ON "Organization_geographic_locations" ("Organization_id");
CREATE INDEX "ix_Organization_geographic_locations_geographic_locations" ON "Organization_geographic_locations" (geographic_locations);

CREATE TABLE "Organization_regulatory_jurisdictions" (
	"Organization_id" TEXT,
	regulatory_jurisdictions TEXT,
	PRIMARY KEY ("Organization_id", regulatory_jurisdictions),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_regulatory_jurisdictions_regulatory_jurisdictions" ON "Organization_regulatory_jurisdictions" (regulatory_jurisdictions);
CREATE INDEX "ix_Organization_regulatory_jurisdictions_Organization_id" ON "Organization_regulatory_jurisdictions" ("Organization_id");

CREATE TABLE "Organization_subsidiaries" (
	"Organization_id" TEXT,
	subsidiaries TEXT,
	PRIMARY KEY ("Organization_id", subsidiaries),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_subsidiaries_Organization_id" ON "Organization_subsidiaries" ("Organization_id");
CREATE INDEX "ix_Organization_subsidiaries_subsidiaries" ON "Organization_subsidiaries" (subsidiaries);

CREATE TABLE "Organization_ai_roles" (
	"Organization_id" TEXT,
	ai_roles VARCHAR(18),
	PRIMARY KEY ("Organization_id", ai_roles),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_ai_roles_Organization_id" ON "Organization_ai_roles" ("Organization_id");
CREATE INDEX "ix_Organization_ai_roles_ai_roles" ON "Organization_ai_roles" (ai_roles);

CREATE TABLE "InterestedParty_requirements" (
	"InterestedParty_id" TEXT,
	requirements TEXT,
	PRIMARY KEY ("InterestedParty_id", requirements),
	FOREIGN KEY("InterestedParty_id") REFERENCES "InterestedParty" (id)
);
CREATE INDEX "ix_InterestedParty_requirements_InterestedParty_id" ON "InterestedParty_requirements" ("InterestedParty_id");
CREATE INDEX "ix_InterestedParty_requirements_requirements" ON "InterestedParty_requirements" (requirements);

CREATE TABLE "AIPolicy_commitment_statements" (
	"AIPolicy_id" TEXT,
	commitment_statements TEXT,
	PRIMARY KEY ("AIPolicy_id", commitment_statements),
	FOREIGN KEY("AIPolicy_id") REFERENCES "AIPolicy" (id)
);
CREATE INDEX "ix_AIPolicy_commitment_statements_commitment_statements" ON "AIPolicy_commitment_statements" (commitment_statements);
CREATE INDEX "ix_AIPolicy_commitment_statements_AIPolicy_id" ON "AIPolicy_commitment_statements" ("AIPolicy_id");

CREATE TABLE "Role_responsibilities" (
	"Role_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("Role_id", responsibilities),
	FOREIGN KEY("Role_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Role_responsibilities_Role_id" ON "Role_responsibilities" ("Role_id");
CREATE INDEX "ix_Role_responsibilities_responsibilities" ON "Role_responsibilities" (responsibilities);

CREATE TABLE "Role_authorities" (
	"Role_id" TEXT,
	authorities TEXT,
	PRIMARY KEY ("Role_id", authorities),
	FOREIGN KEY("Role_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Role_authorities_Role_id" ON "Role_authorities" ("Role_id");
CREATE INDEX "ix_Role_authorities_authorities" ON "Role_authorities" (authorities);

CREATE TABLE "Role_assigned_to" (
	"Role_id" TEXT,
	assigned_to TEXT,
	PRIMARY KEY ("Role_id", assigned_to),
	FOREIGN KEY("Role_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Role_assigned_to_Role_id" ON "Role_assigned_to" ("Role_id");
CREATE INDEX "ix_Role_assigned_to_assigned_to" ON "Role_assigned_to" (assigned_to);

CREATE TABLE "AIRiskAssessmentProcess_trigger_events" (
	"AIRiskAssessmentProcess_id" TEXT,
	trigger_events TEXT,
	PRIMARY KEY ("AIRiskAssessmentProcess_id", trigger_events),
	FOREIGN KEY("AIRiskAssessmentProcess_id") REFERENCES "AIRiskAssessmentProcess" (id)
);
CREATE INDEX "ix_AIRiskAssessmentProcess_trigger_events_AIRiskAssessmentProcess_id" ON "AIRiskAssessmentProcess_trigger_events" ("AIRiskAssessmentProcess_id");
CREATE INDEX "ix_AIRiskAssessmentProcess_trigger_events_trigger_events" ON "AIRiskAssessmentProcess_trigger_events" (trigger_events);

CREATE TABLE "AIRiskTreatmentPlan_treatment_actions" (
	"AIRiskTreatmentPlan_id" TEXT,
	treatment_actions TEXT,
	PRIMARY KEY ("AIRiskTreatmentPlan_id", treatment_actions),
	FOREIGN KEY("AIRiskTreatmentPlan_id") REFERENCES "AIRiskTreatmentPlan" (id)
);
CREATE INDEX "ix_AIRiskTreatmentPlan_treatment_actions_treatment_actions" ON "AIRiskTreatmentPlan_treatment_actions" (treatment_actions);
CREATE INDEX "ix_AIRiskTreatmentPlan_treatment_actions_AIRiskTreatmentPlan_id" ON "AIRiskTreatmentPlan_treatment_actions" ("AIRiskTreatmentPlan_id");

CREATE TABLE "AIRiskTreatmentPlan_controls_to_implement" (
	"AIRiskTreatmentPlan_id" TEXT,
	controls_to_implement_id TEXT,
	PRIMARY KEY ("AIRiskTreatmentPlan_id", controls_to_implement_id),
	FOREIGN KEY("AIRiskTreatmentPlan_id") REFERENCES "AIRiskTreatmentPlan" (id),
	FOREIGN KEY(controls_to_implement_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIRiskTreatmentPlan_controls_to_implement_controls_to_implement_id" ON "AIRiskTreatmentPlan_controls_to_implement" (controls_to_implement_id);
CREATE INDEX "ix_AIRiskTreatmentPlan_controls_to_implement_AIRiskTreatmentPlan_id" ON "AIRiskTreatmentPlan_controls_to_implement" ("AIRiskTreatmentPlan_id");

CREATE TABLE "AIRiskTreatmentPlan_responsible_parties" (
	"AIRiskTreatmentPlan_id" TEXT,
	responsible_parties TEXT,
	PRIMARY KEY ("AIRiskTreatmentPlan_id", responsible_parties),
	FOREIGN KEY("AIRiskTreatmentPlan_id") REFERENCES "AIRiskTreatmentPlan" (id)
);
CREATE INDEX "ix_AIRiskTreatmentPlan_responsible_parties_AIRiskTreatmentPlan_id" ON "AIRiskTreatmentPlan_responsible_parties" ("AIRiskTreatmentPlan_id");
CREATE INDEX "ix_AIRiskTreatmentPlan_responsible_parties_responsible_parties" ON "AIRiskTreatmentPlan_responsible_parties" (responsible_parties);

CREATE TABLE "AISystemImpactAssessmentProcess_dimensions_in_scope" (
	"AISystemImpactAssessmentProcess_id" TEXT,
	dimensions_in_scope VARCHAR(14),
	PRIMARY KEY ("AISystemImpactAssessmentProcess_id", dimensions_in_scope),
	FOREIGN KEY("AISystemImpactAssessmentProcess_id") REFERENCES "AISystemImpactAssessmentProcess" (id)
);
CREATE INDEX "ix_AISystemImpactAssessmentProcess_dimensions_in_scope_AISystemImpactAssessmentProcess_id" ON "AISystemImpactAssessmentProcess_dimensions_in_scope" ("AISystemImpactAssessmentProcess_id");
CREATE INDEX "ix_AISystemImpactAssessmentProcess_dimensions_in_scope_dimensions_in_scope" ON "AISystemImpactAssessmentProcess_dimensions_in_scope" (dimensions_in_scope);

CREATE TABLE "AISystemImpactAssessmentProcess_trigger_events" (
	"AISystemImpactAssessmentProcess_id" TEXT,
	trigger_events TEXT,
	PRIMARY KEY ("AISystemImpactAssessmentProcess_id", trigger_events),
	FOREIGN KEY("AISystemImpactAssessmentProcess_id") REFERENCES "AISystemImpactAssessmentProcess" (id)
);
CREATE INDEX "ix_AISystemImpactAssessmentProcess_trigger_events_AISystemImpactAssessmentProcess_id" ON "AISystemImpactAssessmentProcess_trigger_events" ("AISystemImpactAssessmentProcess_id");
CREATE INDEX "ix_AISystemImpactAssessmentProcess_trigger_events_trigger_events" ON "AISystemImpactAssessmentProcess_trigger_events" (trigger_events);

CREATE TABLE "AISystemImpactAssessment_ai_systems_assessed" (
	"AISystemImpactAssessment_id" TEXT,
	ai_systems_assessed_id TEXT,
	PRIMARY KEY ("AISystemImpactAssessment_id", ai_systems_assessed_id),
	FOREIGN KEY("AISystemImpactAssessment_id") REFERENCES "AISystemImpactAssessment" (id),
	FOREIGN KEY(ai_systems_assessed_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_ai_systems_assessed_AISystemImpactAssessment_id" ON "AISystemImpactAssessment_ai_systems_assessed" ("AISystemImpactAssessment_id");
CREATE INDEX "ix_AISystemImpactAssessment_ai_systems_assessed_ai_systems_assessed_id" ON "AISystemImpactAssessment_ai_systems_assessed" (ai_systems_assessed_id);

CREATE TABLE "AISystemImpactAssessment_applicable_jurisdictions" (
	"AISystemImpactAssessment_id" TEXT,
	applicable_jurisdictions TEXT,
	PRIMARY KEY ("AISystemImpactAssessment_id", applicable_jurisdictions),
	FOREIGN KEY("AISystemImpactAssessment_id") REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_applicable_jurisdictions_applicable_jurisdictions" ON "AISystemImpactAssessment_applicable_jurisdictions" (applicable_jurisdictions);
CREATE INDEX "ix_AISystemImpactAssessment_applicable_jurisdictions_AISystemImpactAssessment_id" ON "AISystemImpactAssessment_applicable_jurisdictions" ("AISystemImpactAssessment_id");

CREATE TABLE "AISystemImpactAssessment_dimensions_assessed" (
	"AISystemImpactAssessment_id" TEXT,
	dimensions_assessed VARCHAR(14),
	PRIMARY KEY ("AISystemImpactAssessment_id", dimensions_assessed),
	FOREIGN KEY("AISystemImpactAssessment_id") REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_dimensions_assessed_AISystemImpactAssessment_id" ON "AISystemImpactAssessment_dimensions_assessed" ("AISystemImpactAssessment_id");
CREATE INDEX "ix_AISystemImpactAssessment_dimensions_assessed_dimensions_assessed" ON "AISystemImpactAssessment_dimensions_assessed" (dimensions_assessed);

CREATE TABLE "AISystemImpactAssessment_identified_consequences" (
	"AISystemImpactAssessment_id" TEXT,
	identified_consequences TEXT,
	PRIMARY KEY ("AISystemImpactAssessment_id", identified_consequences),
	FOREIGN KEY("AISystemImpactAssessment_id") REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_identified_consequences_AISystemImpactAssessment_id" ON "AISystemImpactAssessment_identified_consequences" ("AISystemImpactAssessment_id");
CREATE INDEX "ix_AISystemImpactAssessment_identified_consequences_identified_consequences" ON "AISystemImpactAssessment_identified_consequences" (identified_consequences);

CREATE TABLE "AISystemImpactAssessment_mitigations" (
	"AISystemImpactAssessment_id" TEXT,
	mitigations TEXT,
	PRIMARY KEY ("AISystemImpactAssessment_id", mitigations),
	FOREIGN KEY("AISystemImpactAssessment_id") REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_mitigations_mitigations" ON "AISystemImpactAssessment_mitigations" (mitigations);
CREATE INDEX "ix_AISystemImpactAssessment_mitigations_AISystemImpactAssessment_id" ON "AISystemImpactAssessment_mitigations" ("AISystemImpactAssessment_id");

CREATE TABLE "AISystemImpactAssessment_shared_with_parties" (
	"AISystemImpactAssessment_id" TEXT,
	shared_with_parties TEXT,
	PRIMARY KEY ("AISystemImpactAssessment_id", shared_with_parties),
	FOREIGN KEY("AISystemImpactAssessment_id") REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AISystemImpactAssessment_shared_with_parties_AISystemImpactAssessment_id" ON "AISystemImpactAssessment_shared_with_parties" ("AISystemImpactAssessment_id");
CREATE INDEX "ix_AISystemImpactAssessment_shared_with_parties_shared_with_parties" ON "AISystemImpactAssessment_shared_with_parties" (shared_with_parties);

CREATE TABLE "AIReferenceControl_related_controls" (
	"AIReferenceControl_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("AIReferenceControl_id", related_controls_id),
	FOREIGN KEY("AIReferenceControl_id") REFERENCES "AIReferenceControl" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIReferenceControl_related_controls_AIReferenceControl_id" ON "AIReferenceControl_related_controls" ("AIReferenceControl_id");
CREATE INDEX "ix_AIReferenceControl_related_controls_related_controls_id" ON "AIReferenceControl_related_controls" (related_controls_id);

CREATE TABLE "AIReferenceControl_applicable_risk_sources" (
	"AIReferenceControl_id" TEXT,
	applicable_risk_sources VARCHAR(38),
	PRIMARY KEY ("AIReferenceControl_id", applicable_risk_sources),
	FOREIGN KEY("AIReferenceControl_id") REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIReferenceControl_applicable_risk_sources_applicable_risk_sources" ON "AIReferenceControl_applicable_risk_sources" (applicable_risk_sources);
CREATE INDEX "ix_AIReferenceControl_applicable_risk_sources_AIReferenceControl_id" ON "AIReferenceControl_applicable_risk_sources" ("AIReferenceControl_id");

CREATE TABLE "AIReferenceControl_applicable_objectives" (
	"AIReferenceControl_id" TEXT,
	applicable_objectives VARCHAR(29),
	PRIMARY KEY ("AIReferenceControl_id", applicable_objectives),
	FOREIGN KEY("AIReferenceControl_id") REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIReferenceControl_applicable_objectives_applicable_objectives" ON "AIReferenceControl_applicable_objectives" (applicable_objectives);
CREATE INDEX "ix_AIReferenceControl_applicable_objectives_AIReferenceControl_id" ON "AIReferenceControl_applicable_objectives" ("AIReferenceControl_id");

CREATE TABLE "AIReferenceControl_evidence_references" (
	"AIReferenceControl_id" TEXT,
	evidence_references TEXT,
	PRIMARY KEY ("AIReferenceControl_id", evidence_references),
	FOREIGN KEY("AIReferenceControl_id") REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIReferenceControl_evidence_references_AIReferenceControl_id" ON "AIReferenceControl_evidence_references" ("AIReferenceControl_id");
CREATE INDEX "ix_AIReferenceControl_evidence_references_evidence_references" ON "AIReferenceControl_evidence_references" (evidence_references);

CREATE TABLE "AISystem_intended_uses" (
	"AISystem_id" TEXT,
	intended_uses TEXT,
	PRIMARY KEY ("AISystem_id", intended_uses),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_intended_uses_AISystem_id" ON "AISystem_intended_uses" ("AISystem_id");
CREATE INDEX "ix_AISystem_intended_uses_intended_uses" ON "AISystem_intended_uses" (intended_uses);

CREATE TABLE "AISystem_foreseeable_misuse" (
	"AISystem_id" TEXT,
	foreseeable_misuse TEXT,
	PRIMARY KEY ("AISystem_id", foreseeable_misuse),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_foreseeable_misuse_AISystem_id" ON "AISystem_foreseeable_misuse" ("AISystem_id");
CREATE INDEX "ix_AISystem_foreseeable_misuse_foreseeable_misuse" ON "AISystem_foreseeable_misuse" (foreseeable_misuse);

CREATE TABLE "AISystem_human_oversight_stages" (
	"AISystem_id" TEXT,
	human_oversight_stages VARCHAR(31),
	PRIMARY KEY ("AISystem_id", human_oversight_stages),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_human_oversight_stages_AISystem_id" ON "AISystem_human_oversight_stages" ("AISystem_id");
CREATE INDEX "ix_AISystem_human_oversight_stages_human_oversight_stages" ON "AISystem_human_oversight_stages" (human_oversight_stages);

CREATE TABLE "AISystem_data_resources" (
	"AISystem_id" TEXT,
	data_resources_id TEXT,
	PRIMARY KEY ("AISystem_id", data_resources_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(data_resources_id) REFERENCES "DataResource" (id)
);
CREATE INDEX "ix_AISystem_data_resources_AISystem_id" ON "AISystem_data_resources" ("AISystem_id");
CREATE INDEX "ix_AISystem_data_resources_data_resources_id" ON "AISystem_data_resources" (data_resources_id);

CREATE TABLE "AISystem_tooling_resources" (
	"AISystem_id" TEXT,
	tooling_resources_id TEXT,
	PRIMARY KEY ("AISystem_id", tooling_resources_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(tooling_resources_id) REFERENCES "ToolingResource" (id)
);
CREATE INDEX "ix_AISystem_tooling_resources_tooling_resources_id" ON "AISystem_tooling_resources" (tooling_resources_id);
CREATE INDEX "ix_AISystem_tooling_resources_AISystem_id" ON "AISystem_tooling_resources" ("AISystem_id");

CREATE TABLE "AISystem_computing_resources" (
	"AISystem_id" TEXT,
	computing_resources_id TEXT,
	PRIMARY KEY ("AISystem_id", computing_resources_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(computing_resources_id) REFERENCES "ComputingResource" (id)
);
CREATE INDEX "ix_AISystem_computing_resources_computing_resources_id" ON "AISystem_computing_resources" (computing_resources_id);
CREATE INDEX "ix_AISystem_computing_resources_AISystem_id" ON "AISystem_computing_resources" ("AISystem_id");

CREATE TABLE "AISystem_human_resources" (
	"AISystem_id" TEXT,
	human_resources_id TEXT,
	PRIMARY KEY ("AISystem_id", human_resources_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(human_resources_id) REFERENCES "HumanResource" (id)
);
CREATE INDEX "ix_AISystem_human_resources_AISystem_id" ON "AISystem_human_resources" ("AISystem_id");
CREATE INDEX "ix_AISystem_human_resources_human_resources_id" ON "AISystem_human_resources" (human_resources_id);

CREATE TABLE "AISystem_technical_documentation" (
	"AISystem_id" TEXT,
	technical_documentation TEXT,
	PRIMARY KEY ("AISystem_id", technical_documentation),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_technical_documentation_AISystem_id" ON "AISystem_technical_documentation" ("AISystem_id");
CREATE INDEX "ix_AISystem_technical_documentation_technical_documentation" ON "AISystem_technical_documentation" (technical_documentation);

CREATE TABLE "AISystem_applicable_controls" (
	"AISystem_id" TEXT,
	applicable_controls_id TEXT,
	PRIMARY KEY ("AISystem_id", applicable_controls_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(applicable_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AISystem_applicable_controls_applicable_controls_id" ON "AISystem_applicable_controls" (applicable_controls_id);
CREATE INDEX "ix_AISystem_applicable_controls_AISystem_id" ON "AISystem_applicable_controls" ("AISystem_id");

CREATE TABLE "AISystem_related_impact_assessments" (
	"AISystem_id" TEXT,
	related_impact_assessments_id TEXT,
	PRIMARY KEY ("AISystem_id", related_impact_assessments_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(related_impact_assessments_id) REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AISystem_related_impact_assessments_AISystem_id" ON "AISystem_related_impact_assessments" ("AISystem_id");
CREATE INDEX "ix_AISystem_related_impact_assessments_related_impact_assessments_id" ON "AISystem_related_impact_assessments" (related_impact_assessments_id);

CREATE TABLE "AISystem_supplier_relationships" (
	"AISystem_id" TEXT,
	supplier_relationships_id TEXT,
	PRIMARY KEY ("AISystem_id", supplier_relationships_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(supplier_relationships_id) REFERENCES "SupplierRelationship" (id)
);
CREATE INDEX "ix_AISystem_supplier_relationships_AISystem_id" ON "AISystem_supplier_relationships" ("AISystem_id");
CREATE INDEX "ix_AISystem_supplier_relationships_supplier_relationships_id" ON "AISystem_supplier_relationships" (supplier_relationships_id);

CREATE TABLE "AISystem_customer_relationships" (
	"AISystem_id" TEXT,
	customer_relationships_id TEXT,
	PRIMARY KEY ("AISystem_id", customer_relationships_id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY(customer_relationships_id) REFERENCES "CustomerRelationship" (id)
);
CREATE INDEX "ix_AISystem_customer_relationships_AISystem_id" ON "AISystem_customer_relationships" ("AISystem_id");
CREATE INDEX "ix_AISystem_customer_relationships_customer_relationships_id" ON "AISystem_customer_relationships" (customer_relationships_id);

CREATE TABLE "DataResource_data_quality_requirements" (
	"DataResource_id" TEXT,
	data_quality_requirements TEXT,
	PRIMARY KEY ("DataResource_id", data_quality_requirements),
	FOREIGN KEY("DataResource_id") REFERENCES "DataResource" (id)
);
CREATE INDEX "ix_DataResource_data_quality_requirements_DataResource_id" ON "DataResource_data_quality_requirements" ("DataResource_id");
CREATE INDEX "ix_DataResource_data_quality_requirements_data_quality_requirements" ON "DataResource_data_quality_requirements" (data_quality_requirements);

CREATE TABLE "DataResource_data_quality_metrics" (
	"DataResource_id" TEXT,
	data_quality_metrics TEXT,
	PRIMARY KEY ("DataResource_id", data_quality_metrics),
	FOREIGN KEY("DataResource_id") REFERENCES "DataResource" (id)
);
CREATE INDEX "ix_DataResource_data_quality_metrics_DataResource_id" ON "DataResource_data_quality_metrics" ("DataResource_id");
CREATE INDEX "ix_DataResource_data_quality_metrics_data_quality_metrics" ON "DataResource_data_quality_metrics" (data_quality_metrics);

CREATE TABLE "DataResource_data_preparation_methods" (
	"DataResource_id" TEXT,
	data_preparation_methods VARCHAR(23),
	PRIMARY KEY ("DataResource_id", data_preparation_methods),
	FOREIGN KEY("DataResource_id") REFERENCES "DataResource" (id)
);
CREATE INDEX "ix_DataResource_data_preparation_methods_DataResource_id" ON "DataResource_data_preparation_methods" ("DataResource_id");
CREATE INDEX "ix_DataResource_data_preparation_methods_data_preparation_methods" ON "DataResource_data_preparation_methods" (data_preparation_methods);

CREATE TABLE "DataResource_known_bias_issues" (
	"DataResource_id" TEXT,
	known_bias_issues TEXT,
	PRIMARY KEY ("DataResource_id", known_bias_issues),
	FOREIGN KEY("DataResource_id") REFERENCES "DataResource" (id)
);
CREATE INDEX "ix_DataResource_known_bias_issues_known_bias_issues" ON "DataResource_known_bias_issues" (known_bias_issues);
CREATE INDEX "ix_DataResource_known_bias_issues_DataResource_id" ON "DataResource_known_bias_issues" ("DataResource_id");

CREATE TABLE "HumanResource_required_competencies" (
	"HumanResource_id" TEXT,
	required_competencies TEXT,
	PRIMARY KEY ("HumanResource_id", required_competencies),
	FOREIGN KEY("HumanResource_id") REFERENCES "HumanResource" (id)
);
CREATE INDEX "ix_HumanResource_required_competencies_HumanResource_id" ON "HumanResource_required_competencies" ("HumanResource_id");
CREATE INDEX "ix_HumanResource_required_competencies_required_competencies" ON "HumanResource_required_competencies" (required_competencies);

CREATE TABLE "HumanResource_assigned_to" (
	"HumanResource_id" TEXT,
	assigned_to TEXT,
	PRIMARY KEY ("HumanResource_id", assigned_to),
	FOREIGN KEY("HumanResource_id") REFERENCES "HumanResource" (id)
);
CREATE INDEX "ix_HumanResource_assigned_to_assigned_to" ON "HumanResource_assigned_to" (assigned_to);
CREATE INDEX "ix_HumanResource_assigned_to_HumanResource_id" ON "HumanResource_assigned_to" ("HumanResource_id");

CREATE TABLE "HumanResource_lifecycle_responsibilities" (
	"HumanResource_id" TEXT,
	lifecycle_responsibilities TEXT,
	PRIMARY KEY ("HumanResource_id", lifecycle_responsibilities),
	FOREIGN KEY("HumanResource_id") REFERENCES "HumanResource" (id)
);
CREATE INDEX "ix_HumanResource_lifecycle_responsibilities_HumanResource_id" ON "HumanResource_lifecycle_responsibilities" ("HumanResource_id");
CREATE INDEX "ix_HumanResource_lifecycle_responsibilities_lifecycle_responsibilities" ON "HumanResource_lifecycle_responsibilities" (lifecycle_responsibilities);

CREATE TABLE "CompetenceRecord_required_competencies" (
	"CompetenceRecord_id" TEXT,
	required_competencies TEXT,
	PRIMARY KEY ("CompetenceRecord_id", required_competencies),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_required_competencies_required_competencies" ON "CompetenceRecord_required_competencies" (required_competencies);
CREATE INDEX "ix_CompetenceRecord_required_competencies_CompetenceRecord_id" ON "CompetenceRecord_required_competencies" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_education_records" (
	"CompetenceRecord_id" TEXT,
	education_records TEXT,
	PRIMARY KEY ("CompetenceRecord_id", education_records),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_education_records_CompetenceRecord_id" ON "CompetenceRecord_education_records" ("CompetenceRecord_id");
CREATE INDEX "ix_CompetenceRecord_education_records_education_records" ON "CompetenceRecord_education_records" (education_records);

CREATE TABLE "CompetenceRecord_training_records" (
	"CompetenceRecord_id" TEXT,
	training_records TEXT,
	PRIMARY KEY ("CompetenceRecord_id", training_records),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_training_records_training_records" ON "CompetenceRecord_training_records" (training_records);
CREATE INDEX "ix_CompetenceRecord_training_records_CompetenceRecord_id" ON "CompetenceRecord_training_records" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_experience_records" (
	"CompetenceRecord_id" TEXT,
	experience_records TEXT,
	PRIMARY KEY ("CompetenceRecord_id", experience_records),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_experience_records_experience_records" ON "CompetenceRecord_experience_records" (experience_records);
CREATE INDEX "ix_CompetenceRecord_experience_records_CompetenceRecord_id" ON "CompetenceRecord_experience_records" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_competency_gaps" (
	"CompetenceRecord_id" TEXT,
	competency_gaps TEXT,
	PRIMARY KEY ("CompetenceRecord_id", competency_gaps),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_competency_gaps_competency_gaps" ON "CompetenceRecord_competency_gaps" (competency_gaps);
CREATE INDEX "ix_CompetenceRecord_competency_gaps_CompetenceRecord_id" ON "CompetenceRecord_competency_gaps" ("CompetenceRecord_id");

CREATE TABLE "CompetenceRecord_development_actions" (
	"CompetenceRecord_id" TEXT,
	development_actions TEXT,
	PRIMARY KEY ("CompetenceRecord_id", development_actions),
	FOREIGN KEY("CompetenceRecord_id") REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_CompetenceRecord_development_actions_CompetenceRecord_id" ON "CompetenceRecord_development_actions" ("CompetenceRecord_id");
CREATE INDEX "ix_CompetenceRecord_development_actions_development_actions" ON "CompetenceRecord_development_actions" (development_actions);

CREATE TABLE "AwarenessProgram_awareness_topics" (
	"AwarenessProgram_id" TEXT,
	awareness_topics TEXT,
	PRIMARY KEY ("AwarenessProgram_id", awareness_topics),
	FOREIGN KEY("AwarenessProgram_id") REFERENCES "AwarenessProgram" (id)
);
CREATE INDEX "ix_AwarenessProgram_awareness_topics_awareness_topics" ON "AwarenessProgram_awareness_topics" (awareness_topics);
CREATE INDEX "ix_AwarenessProgram_awareness_topics_AwarenessProgram_id" ON "AwarenessProgram_awareness_topics" ("AwarenessProgram_id");

CREATE TABLE "AwarenessProgram_delivery_methods" (
	"AwarenessProgram_id" TEXT,
	delivery_methods TEXT,
	PRIMARY KEY ("AwarenessProgram_id", delivery_methods),
	FOREIGN KEY("AwarenessProgram_id") REFERENCES "AwarenessProgram" (id)
);
CREATE INDEX "ix_AwarenessProgram_delivery_methods_delivery_methods" ON "AwarenessProgram_delivery_methods" (delivery_methods);
CREATE INDEX "ix_AwarenessProgram_delivery_methods_AwarenessProgram_id" ON "AwarenessProgram_delivery_methods" ("AwarenessProgram_id");

CREATE TABLE "CommunicationPlan_communication_items" (
	"CommunicationPlan_id" TEXT,
	communication_items_id INTEGER,
	PRIMARY KEY ("CommunicationPlan_id", communication_items_id),
	FOREIGN KEY("CommunicationPlan_id") REFERENCES "CommunicationPlan" (id),
	FOREIGN KEY(communication_items_id) REFERENCES "CommunicationItem" (id)
);
CREATE INDEX "ix_CommunicationPlan_communication_items_CommunicationPlan_id" ON "CommunicationPlan_communication_items" ("CommunicationPlan_id");
CREATE INDEX "ix_CommunicationPlan_communication_items_communication_items_id" ON "CommunicationPlan_communication_items" (communication_items_id);

CREATE TABLE "OperationalProcedure_control_measures" (
	"OperationalProcedure_id" TEXT,
	control_measures TEXT,
	PRIMARY KEY ("OperationalProcedure_id", control_measures),
	FOREIGN KEY("OperationalProcedure_id") REFERENCES "OperationalProcedure" (id)
);
CREATE INDEX "ix_OperationalProcedure_control_measures_control_measures" ON "OperationalProcedure_control_measures" (control_measures);
CREATE INDEX "ix_OperationalProcedure_control_measures_OperationalProcedure_id" ON "OperationalProcedure_control_measures" ("OperationalProcedure_id");

CREATE TABLE "OperationalProcedure_responsible_roles" (
	"OperationalProcedure_id" TEXT,
	responsible_roles_id TEXT,
	PRIMARY KEY ("OperationalProcedure_id", responsible_roles_id),
	FOREIGN KEY("OperationalProcedure_id") REFERENCES "OperationalProcedure" (id),
	FOREIGN KEY(responsible_roles_id) REFERENCES "Role" (id)
);
CREATE INDEX "ix_OperationalProcedure_responsible_roles_responsible_roles_id" ON "OperationalProcedure_responsible_roles" (responsible_roles_id);
CREATE INDEX "ix_OperationalProcedure_responsible_roles_OperationalProcedure_id" ON "OperationalProcedure_responsible_roles" ("OperationalProcedure_id");

CREATE TABLE "OperationalProcedure_related_controls" (
	"OperationalProcedure_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("OperationalProcedure_id", related_controls_id),
	FOREIGN KEY("OperationalProcedure_id") REFERENCES "OperationalProcedure" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_OperationalProcedure_related_controls_OperationalProcedure_id" ON "OperationalProcedure_related_controls" ("OperationalProcedure_id");
CREATE INDEX "ix_OperationalProcedure_related_controls_related_controls_id" ON "OperationalProcedure_related_controls" (related_controls_id);

CREATE TABLE "MonitoringProgram_monitoring_items" (
	"MonitoringProgram_id" TEXT,
	monitoring_items_id INTEGER,
	PRIMARY KEY ("MonitoringProgram_id", monitoring_items_id),
	FOREIGN KEY("MonitoringProgram_id") REFERENCES "MonitoringProgram" (id),
	FOREIGN KEY(monitoring_items_id) REFERENCES "MonitoringItem" (id)
);
CREATE INDEX "ix_MonitoringProgram_monitoring_items_MonitoringProgram_id" ON "MonitoringProgram_monitoring_items" ("MonitoringProgram_id");
CREATE INDEX "ix_MonitoringProgram_monitoring_items_monitoring_items_id" ON "MonitoringProgram_monitoring_items" (monitoring_items_id);

CREATE TABLE "InternalAudit_audit_team" (
	"InternalAudit_id" TEXT,
	audit_team TEXT,
	PRIMARY KEY ("InternalAudit_id", audit_team),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_audit_team_InternalAudit_id" ON "InternalAudit_audit_team" ("InternalAudit_id");
CREATE INDEX "ix_InternalAudit_audit_team_audit_team" ON "InternalAudit_audit_team" (audit_team);

CREATE TABLE "InternalAudit_auditee_representatives" (
	"InternalAudit_id" TEXT,
	auditee_representatives TEXT,
	PRIMARY KEY ("InternalAudit_id", auditee_representatives),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_auditee_representatives_auditee_representatives" ON "InternalAudit_auditee_representatives" (auditee_representatives);
CREATE INDEX "ix_InternalAudit_auditee_representatives_InternalAudit_id" ON "InternalAudit_auditee_representatives" ("InternalAudit_id");

CREATE TABLE "InternalAudit_positive_observations" (
	"InternalAudit_id" TEXT,
	positive_observations TEXT,
	PRIMARY KEY ("InternalAudit_id", positive_observations),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_positive_observations_positive_observations" ON "InternalAudit_positive_observations" (positive_observations);
CREATE INDEX "ix_InternalAudit_positive_observations_InternalAudit_id" ON "InternalAudit_positive_observations" ("InternalAudit_id");

CREATE TABLE "InternalAudit_report_distribution" (
	"InternalAudit_id" TEXT,
	report_distribution TEXT,
	PRIMARY KEY ("InternalAudit_id", report_distribution),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_InternalAudit_report_distribution_InternalAudit_id" ON "InternalAudit_report_distribution" ("InternalAudit_id");
CREATE INDEX "ix_InternalAudit_report_distribution_report_distribution" ON "InternalAudit_report_distribution" (report_distribution);

CREATE TABLE "AuditProgramme_planned_audits" (
	"AuditProgramme_id" TEXT,
	planned_audits_id TEXT,
	PRIMARY KEY ("AuditProgramme_id", planned_audits_id),
	FOREIGN KEY("AuditProgramme_id") REFERENCES "AuditProgramme" (id),
	FOREIGN KEY(planned_audits_id) REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_AuditProgramme_planned_audits_planned_audits_id" ON "AuditProgramme_planned_audits" (planned_audits_id);
CREATE INDEX "ix_AuditProgramme_planned_audits_AuditProgramme_id" ON "AuditProgramme_planned_audits" ("AuditProgramme_id");

CREATE TABLE "ManagementReview_attendees" (
	"ManagementReview_id" TEXT,
	attendees TEXT,
	PRIMARY KEY ("ManagementReview_id", attendees),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_attendees_attendees" ON "ManagementReview_attendees" (attendees);
CREATE INDEX "ix_ManagementReview_attendees_ManagementReview_id" ON "ManagementReview_attendees" ("ManagementReview_id");

CREATE TABLE "ManagementReview_context_changes" (
	"ManagementReview_id" TEXT,
	context_changes TEXT,
	PRIMARY KEY ("ManagementReview_id", context_changes),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_context_changes_ManagementReview_id" ON "ManagementReview_context_changes" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_context_changes_context_changes" ON "ManagementReview_context_changes" (context_changes);

CREATE TABLE "ManagementReview_interested_party_changes" (
	"ManagementReview_id" TEXT,
	interested_party_changes TEXT,
	PRIMARY KEY ("ManagementReview_id", interested_party_changes),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_interested_party_changes_ManagementReview_id" ON "ManagementReview_interested_party_changes" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_interested_party_changes_interested_party_changes" ON "ManagementReview_interested_party_changes" (interested_party_changes);

CREATE TABLE "ManagementReview_improvement_opportunities" (
	"ManagementReview_id" TEXT,
	improvement_opportunities_id TEXT,
	PRIMARY KEY ("ManagementReview_id", improvement_opportunities_id),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id),
	FOREIGN KEY(improvement_opportunities_id) REFERENCES "ImprovementOpportunity" (id)
);
CREATE INDEX "ix_ManagementReview_improvement_opportunities_ManagementReview_id" ON "ManagementReview_improvement_opportunities" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_improvement_opportunities_improvement_opportunities_id" ON "ManagementReview_improvement_opportunities" (improvement_opportunities_id);

CREATE TABLE "ManagementReview_decisions" (
	"ManagementReview_id" TEXT,
	decisions TEXT,
	PRIMARY KEY ("ManagementReview_id", decisions),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_decisions_decisions" ON "ManagementReview_decisions" (decisions);
CREATE INDEX "ix_ManagementReview_decisions_ManagementReview_id" ON "ManagementReview_decisions" ("ManagementReview_id");

CREATE TABLE "ManagementReview_action_items" (
	"ManagementReview_id" TEXT,
	action_items TEXT,
	PRIMARY KEY ("ManagementReview_id", action_items),
	FOREIGN KEY("ManagementReview_id") REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_ManagementReview_action_items_ManagementReview_id" ON "ManagementReview_action_items" ("ManagementReview_id");
CREATE INDEX "ix_ManagementReview_action_items_action_items" ON "ManagementReview_action_items" (action_items);

CREATE TABLE "Nonconformity_immediate_actions" (
	"Nonconformity_id" TEXT,
	immediate_actions TEXT,
	PRIMARY KEY ("Nonconformity_id", immediate_actions),
	FOREIGN KEY("Nonconformity_id") REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_Nonconformity_immediate_actions_Nonconformity_id" ON "Nonconformity_immediate_actions" ("Nonconformity_id");
CREATE INDEX "ix_Nonconformity_immediate_actions_immediate_actions" ON "Nonconformity_immediate_actions" (immediate_actions);

CREATE TABLE "ThirdPartyRelationship_allocated_responsibilities" (
	"ThirdPartyRelationship_id" TEXT,
	allocated_responsibilities TEXT,
	PRIMARY KEY ("ThirdPartyRelationship_id", allocated_responsibilities),
	FOREIGN KEY("ThirdPartyRelationship_id") REFERENCES "ThirdPartyRelationship" (id)
);
CREATE INDEX "ix_ThirdPartyRelationship_allocated_responsibilities_allocated_responsibilities" ON "ThirdPartyRelationship_allocated_responsibilities" (allocated_responsibilities);
CREATE INDEX "ix_ThirdPartyRelationship_allocated_responsibilities_ThirdPartyRelationship_id" ON "ThirdPartyRelationship_allocated_responsibilities" ("ThirdPartyRelationship_id");

CREATE TABLE "ThirdPartyRelationship_ai_systems_involved" (
	"ThirdPartyRelationship_id" TEXT,
	ai_systems_involved_id TEXT,
	PRIMARY KEY ("ThirdPartyRelationship_id", ai_systems_involved_id),
	FOREIGN KEY("ThirdPartyRelationship_id") REFERENCES "ThirdPartyRelationship" (id),
	FOREIGN KEY(ai_systems_involved_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_ThirdPartyRelationship_ai_systems_involved_ThirdPartyRelationship_id" ON "ThirdPartyRelationship_ai_systems_involved" ("ThirdPartyRelationship_id");
CREATE INDEX "ix_ThirdPartyRelationship_ai_systems_involved_ai_systems_involved_id" ON "ThirdPartyRelationship_ai_systems_involved" (ai_systems_involved_id);

CREATE TABLE "ThirdPartyRelationship_lifecycle_stages_involved" (
	"ThirdPartyRelationship_id" TEXT,
	lifecycle_stages_involved VARCHAR(31),
	PRIMARY KEY ("ThirdPartyRelationship_id", lifecycle_stages_involved),
	FOREIGN KEY("ThirdPartyRelationship_id") REFERENCES "ThirdPartyRelationship" (id)
);
CREATE INDEX "ix_ThirdPartyRelationship_lifecycle_stages_involved_ThirdPartyRelationship_id" ON "ThirdPartyRelationship_lifecycle_stages_involved" ("ThirdPartyRelationship_id");
CREATE INDEX "ix_ThirdPartyRelationship_lifecycle_stages_involved_lifecycle_stages_involved" ON "ThirdPartyRelationship_lifecycle_stages_involved" (lifecycle_stages_involved);

CREATE TABLE "ThirdPartyRelationship_assurance_evidence" (
	"ThirdPartyRelationship_id" TEXT,
	assurance_evidence TEXT,
	PRIMARY KEY ("ThirdPartyRelationship_id", assurance_evidence),
	FOREIGN KEY("ThirdPartyRelationship_id") REFERENCES "ThirdPartyRelationship" (id)
);
CREATE INDEX "ix_ThirdPartyRelationship_assurance_evidence_assurance_evidence" ON "ThirdPartyRelationship_assurance_evidence" (assurance_evidence);
CREATE INDEX "ix_ThirdPartyRelationship_assurance_evidence_ThirdPartyRelationship_id" ON "ThirdPartyRelationship_assurance_evidence" ("ThirdPartyRelationship_id");

CREATE TABLE "SupplierRelationship_supplier_assessment_criteria" (
	"SupplierRelationship_id" TEXT,
	supplier_assessment_criteria TEXT,
	PRIMARY KEY ("SupplierRelationship_id", supplier_assessment_criteria),
	FOREIGN KEY("SupplierRelationship_id") REFERENCES "SupplierRelationship" (id)
);
CREATE INDEX "ix_SupplierRelationship_supplier_assessment_criteria_SupplierRelationship_id" ON "SupplierRelationship_supplier_assessment_criteria" ("SupplierRelationship_id");
CREATE INDEX "ix_SupplierRelationship_supplier_assessment_criteria_supplier_assessment_criteria" ON "SupplierRelationship_supplier_assessment_criteria" (supplier_assessment_criteria);

CREATE TABLE "SupplierRelationship_corrective_actions_required" (
	"SupplierRelationship_id" TEXT,
	corrective_actions_required TEXT,
	PRIMARY KEY ("SupplierRelationship_id", corrective_actions_required),
	FOREIGN KEY("SupplierRelationship_id") REFERENCES "SupplierRelationship" (id)
);
CREATE INDEX "ix_SupplierRelationship_corrective_actions_required_SupplierRelationship_id" ON "SupplierRelationship_corrective_actions_required" ("SupplierRelationship_id");
CREATE INDEX "ix_SupplierRelationship_corrective_actions_required_corrective_actions_required" ON "SupplierRelationship_corrective_actions_required" (corrective_actions_required);

CREATE TABLE "SupplierRelationship_allocated_responsibilities" (
	"SupplierRelationship_id" TEXT,
	allocated_responsibilities TEXT,
	PRIMARY KEY ("SupplierRelationship_id", allocated_responsibilities),
	FOREIGN KEY("SupplierRelationship_id") REFERENCES "SupplierRelationship" (id)
);
CREATE INDEX "ix_SupplierRelationship_allocated_responsibilities_SupplierRelationship_id" ON "SupplierRelationship_allocated_responsibilities" ("SupplierRelationship_id");
CREATE INDEX "ix_SupplierRelationship_allocated_responsibilities_allocated_responsibilities" ON "SupplierRelationship_allocated_responsibilities" (allocated_responsibilities);

CREATE TABLE "SupplierRelationship_ai_systems_involved" (
	"SupplierRelationship_id" TEXT,
	ai_systems_involved_id TEXT,
	PRIMARY KEY ("SupplierRelationship_id", ai_systems_involved_id),
	FOREIGN KEY("SupplierRelationship_id") REFERENCES "SupplierRelationship" (id),
	FOREIGN KEY(ai_systems_involved_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_SupplierRelationship_ai_systems_involved_SupplierRelationship_id" ON "SupplierRelationship_ai_systems_involved" ("SupplierRelationship_id");
CREATE INDEX "ix_SupplierRelationship_ai_systems_involved_ai_systems_involved_id" ON "SupplierRelationship_ai_systems_involved" (ai_systems_involved_id);

CREATE TABLE "SupplierRelationship_lifecycle_stages_involved" (
	"SupplierRelationship_id" TEXT,
	lifecycle_stages_involved VARCHAR(31),
	PRIMARY KEY ("SupplierRelationship_id", lifecycle_stages_involved),
	FOREIGN KEY("SupplierRelationship_id") REFERENCES "SupplierRelationship" (id)
);
CREATE INDEX "ix_SupplierRelationship_lifecycle_stages_involved_SupplierRelationship_id" ON "SupplierRelationship_lifecycle_stages_involved" ("SupplierRelationship_id");
CREATE INDEX "ix_SupplierRelationship_lifecycle_stages_involved_lifecycle_stages_involved" ON "SupplierRelationship_lifecycle_stages_involved" (lifecycle_stages_involved);

CREATE TABLE "SupplierRelationship_assurance_evidence" (
	"SupplierRelationship_id" TEXT,
	assurance_evidence TEXT,
	PRIMARY KEY ("SupplierRelationship_id", assurance_evidence),
	FOREIGN KEY("SupplierRelationship_id") REFERENCES "SupplierRelationship" (id)
);
CREATE INDEX "ix_SupplierRelationship_assurance_evidence_assurance_evidence" ON "SupplierRelationship_assurance_evidence" (assurance_evidence);
CREATE INDEX "ix_SupplierRelationship_assurance_evidence_SupplierRelationship_id" ON "SupplierRelationship_assurance_evidence" ("SupplierRelationship_id");

CREATE TABLE "CustomerRelationship_customer_expectations" (
	"CustomerRelationship_id" TEXT,
	customer_expectations TEXT,
	PRIMARY KEY ("CustomerRelationship_id", customer_expectations),
	FOREIGN KEY("CustomerRelationship_id") REFERENCES "CustomerRelationship" (id)
);
CREATE INDEX "ix_CustomerRelationship_customer_expectations_CustomerRelationship_id" ON "CustomerRelationship_customer_expectations" ("CustomerRelationship_id");
CREATE INDEX "ix_CustomerRelationship_customer_expectations_customer_expectations" ON "CustomerRelationship_customer_expectations" (customer_expectations);

CREATE TABLE "CustomerRelationship_communicated_limitations" (
	"CustomerRelationship_id" TEXT,
	communicated_limitations TEXT,
	PRIMARY KEY ("CustomerRelationship_id", communicated_limitations),
	FOREIGN KEY("CustomerRelationship_id") REFERENCES "CustomerRelationship" (id)
);
CREATE INDEX "ix_CustomerRelationship_communicated_limitations_communicated_limitations" ON "CustomerRelationship_communicated_limitations" (communicated_limitations);
CREATE INDEX "ix_CustomerRelationship_communicated_limitations_CustomerRelationship_id" ON "CustomerRelationship_communicated_limitations" ("CustomerRelationship_id");

CREATE TABLE "CustomerRelationship_allocated_responsibilities" (
	"CustomerRelationship_id" TEXT,
	allocated_responsibilities TEXT,
	PRIMARY KEY ("CustomerRelationship_id", allocated_responsibilities),
	FOREIGN KEY("CustomerRelationship_id") REFERENCES "CustomerRelationship" (id)
);
CREATE INDEX "ix_CustomerRelationship_allocated_responsibilities_allocated_responsibilities" ON "CustomerRelationship_allocated_responsibilities" (allocated_responsibilities);
CREATE INDEX "ix_CustomerRelationship_allocated_responsibilities_CustomerRelationship_id" ON "CustomerRelationship_allocated_responsibilities" ("CustomerRelationship_id");

CREATE TABLE "CustomerRelationship_ai_systems_involved" (
	"CustomerRelationship_id" TEXT,
	ai_systems_involved_id TEXT,
	PRIMARY KEY ("CustomerRelationship_id", ai_systems_involved_id),
	FOREIGN KEY("CustomerRelationship_id") REFERENCES "CustomerRelationship" (id),
	FOREIGN KEY(ai_systems_involved_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_CustomerRelationship_ai_systems_involved_CustomerRelationship_id" ON "CustomerRelationship_ai_systems_involved" ("CustomerRelationship_id");
CREATE INDEX "ix_CustomerRelationship_ai_systems_involved_ai_systems_involved_id" ON "CustomerRelationship_ai_systems_involved" (ai_systems_involved_id);

CREATE TABLE "CustomerRelationship_lifecycle_stages_involved" (
	"CustomerRelationship_id" TEXT,
	lifecycle_stages_involved VARCHAR(31),
	PRIMARY KEY ("CustomerRelationship_id", lifecycle_stages_involved),
	FOREIGN KEY("CustomerRelationship_id") REFERENCES "CustomerRelationship" (id)
);
CREATE INDEX "ix_CustomerRelationship_lifecycle_stages_involved_CustomerRelationship_id" ON "CustomerRelationship_lifecycle_stages_involved" ("CustomerRelationship_id");
CREATE INDEX "ix_CustomerRelationship_lifecycle_stages_involved_lifecycle_stages_involved" ON "CustomerRelationship_lifecycle_stages_involved" (lifecycle_stages_involved);

CREATE TABLE "CustomerRelationship_assurance_evidence" (
	"CustomerRelationship_id" TEXT,
	assurance_evidence TEXT,
	PRIMARY KEY ("CustomerRelationship_id", assurance_evidence),
	FOREIGN KEY("CustomerRelationship_id") REFERENCES "CustomerRelationship" (id)
);
CREATE INDEX "ix_CustomerRelationship_assurance_evidence_assurance_evidence" ON "CustomerRelationship_assurance_evidence" (assurance_evidence);
CREATE INDEX "ix_CustomerRelationship_assurance_evidence_CustomerRelationship_id" ON "CustomerRelationship_assurance_evidence" ("CustomerRelationship_id");

CREATE TABLE "ConcernReport_concern_ai_systems" (
	"ConcernReport_id" TEXT,
	concern_ai_systems_id TEXT,
	PRIMARY KEY ("ConcernReport_id", concern_ai_systems_id),
	FOREIGN KEY("ConcernReport_id") REFERENCES "ConcernReport" (id),
	FOREIGN KEY(concern_ai_systems_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_ConcernReport_concern_ai_systems_ConcernReport_id" ON "ConcernReport_concern_ai_systems" ("ConcernReport_id");
CREATE INDEX "ix_ConcernReport_concern_ai_systems_concern_ai_systems_id" ON "ConcernReport_concern_ai_systems" (concern_ai_systems_id);

CREATE TABLE "ConcernReport_concern_lifecycle_stage" (
	"ConcernReport_id" TEXT,
	concern_lifecycle_stage VARCHAR(31),
	PRIMARY KEY ("ConcernReport_id", concern_lifecycle_stage),
	FOREIGN KEY("ConcernReport_id") REFERENCES "ConcernReport" (id)
);
CREATE INDEX "ix_ConcernReport_concern_lifecycle_stage_ConcernReport_id" ON "ConcernReport_concern_lifecycle_stage" ("ConcernReport_id");
CREATE INDEX "ix_ConcernReport_concern_lifecycle_stage_concern_lifecycle_stage" ON "ConcernReport_concern_lifecycle_stage" (concern_lifecycle_stage);

CREATE TABLE "ConcernReport_reprisal_protection_actions" (
	"ConcernReport_id" TEXT,
	reprisal_protection_actions TEXT,
	PRIMARY KEY ("ConcernReport_id", reprisal_protection_actions),
	FOREIGN KEY("ConcernReport_id") REFERENCES "ConcernReport" (id)
);
CREATE INDEX "ix_ConcernReport_reprisal_protection_actions_reprisal_protection_actions" ON "ConcernReport_reprisal_protection_actions" (reprisal_protection_actions);
CREATE INDEX "ix_ConcernReport_reprisal_protection_actions_ConcernReport_id" ON "ConcernReport_reprisal_protection_actions" ("ConcernReport_id");

CREATE TABLE "ConcernReport_related_nonconformities" (
	"ConcernReport_id" TEXT,
	related_nonconformities_id TEXT,
	PRIMARY KEY ("ConcernReport_id", related_nonconformities_id),
	FOREIGN KEY("ConcernReport_id") REFERENCES "ConcernReport" (id),
	FOREIGN KEY(related_nonconformities_id) REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_ConcernReport_related_nonconformities_ConcernReport_id" ON "ConcernReport_related_nonconformities" ("ConcernReport_id");
CREATE INDEX "ix_ConcernReport_related_nonconformities_related_nonconformities_id" ON "ConcernReport_related_nonconformities" (related_nonconformities_id);

CREATE TABLE "AuditFinding" (
	finding_type VARCHAR(19),
	clause_reference TEXT,
	control_reference TEXT,
	finding_description TEXT,
	objective_evidence TEXT,
	root_cause_analysis TEXT,
	risk_implication TEXT,
	recommended_action TEXT,
	auditee_response TEXT,
	linked_corrective_action TEXT,
	closure_status TEXT,
	closure_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(control_reference) REFERENCES "AIReferenceControl" (id),
	FOREIGN KEY(linked_corrective_action) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_AuditFinding_id" ON "AuditFinding" (id);

CREATE TABLE "AISystemEvent" (
	event_datetime DATETIME,
	reporter TEXT,
	reporter_party_type TEXT,
	event_source TEXT,
	event_description TEXT,
	initial_assessment TEXT,
	categorized_as_incident BOOLEAN,
	linked_incident TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	version TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(linked_incident) REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AISystemEvent_id" ON "AISystemEvent" (id);

CREATE TABLE "AIManagementSystem_scope_boundaries" (
	"AIManagementSystem_id" TEXT,
	scope_boundaries TEXT,
	PRIMARY KEY ("AIManagementSystem_id", scope_boundaries),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_scope_boundaries_AIManagementSystem_id" ON "AIManagementSystem_scope_boundaries" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_scope_boundaries_scope_boundaries" ON "AIManagementSystem_scope_boundaries" (scope_boundaries);

CREATE TABLE "AIManagementSystem_scope_exclusions" (
	"AIManagementSystem_id" TEXT,
	scope_exclusions TEXT,
	PRIMARY KEY ("AIManagementSystem_id", scope_exclusions),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_scope_exclusions_scope_exclusions" ON "AIManagementSystem_scope_exclusions" (scope_exclusions);
CREATE INDEX "ix_AIManagementSystem_scope_exclusions_AIManagementSystem_id" ON "AIManagementSystem_scope_exclusions" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_context_internal_issues" (
	"AIManagementSystem_id" TEXT,
	context_internal_issues TEXT,
	PRIMARY KEY ("AIManagementSystem_id", context_internal_issues),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_context_internal_issues_AIManagementSystem_id" ON "AIManagementSystem_context_internal_issues" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_context_internal_issues_context_internal_issues" ON "AIManagementSystem_context_internal_issues" (context_internal_issues);

CREATE TABLE "AIManagementSystem_context_external_issues" (
	"AIManagementSystem_id" TEXT,
	context_external_issues TEXT,
	PRIMARY KEY ("AIManagementSystem_id", context_external_issues),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_context_external_issues_context_external_issues" ON "AIManagementSystem_context_external_issues" (context_external_issues);
CREATE INDEX "ix_AIManagementSystem_context_external_issues_AIManagementSystem_id" ON "AIManagementSystem_context_external_issues" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_organizational_roles_with_ai" (
	"AIManagementSystem_id" TEXT,
	organizational_roles_with_ai VARCHAR(18),
	PRIMARY KEY ("AIManagementSystem_id", organizational_roles_with_ai),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_organizational_roles_with_ai_organizational_roles_with_ai" ON "AIManagementSystem_organizational_roles_with_ai" (organizational_roles_with_ai);
CREATE INDEX "ix_AIManagementSystem_organizational_roles_with_ai_AIManagementSystem_id" ON "AIManagementSystem_organizational_roles_with_ai" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_integrated_management_systems" (
	"AIManagementSystem_id" TEXT,
	integrated_management_systems VARCHAR(13),
	PRIMARY KEY ("AIManagementSystem_id", integrated_management_systems),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_integrated_management_systems_AIManagementSystem_id" ON "AIManagementSystem_integrated_management_systems" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_integrated_management_systems_integrated_management_systems" ON "AIManagementSystem_integrated_management_systems" (integrated_management_systems);

CREATE TABLE "AIManagementSystem_leadership_commitment_evidence" (
	"AIManagementSystem_id" TEXT,
	leadership_commitment_evidence TEXT,
	PRIMARY KEY ("AIManagementSystem_id", leadership_commitment_evidence),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_leadership_commitment_evidence_leadership_commitment_evidence" ON "AIManagementSystem_leadership_commitment_evidence" (leadership_commitment_evidence);
CREATE INDEX "ix_AIManagementSystem_leadership_commitment_evidence_AIManagementSystem_id" ON "AIManagementSystem_leadership_commitment_evidence" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_planned_changes" (
	"AIManagementSystem_id" TEXT,
	planned_changes TEXT,
	PRIMARY KEY ("AIManagementSystem_id", planned_changes),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_planned_changes_AIManagementSystem_id" ON "AIManagementSystem_planned_changes" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_planned_changes_planned_changes" ON "AIManagementSystem_planned_changes" (planned_changes);

CREATE TABLE "AIManagementSystem_interested_parties" (
	"AIManagementSystem_id" TEXT,
	interested_parties_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", interested_parties_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(interested_parties_id) REFERENCES "InterestedParty" (id)
);
CREATE INDEX "ix_AIManagementSystem_interested_parties_interested_parties_id" ON "AIManagementSystem_interested_parties" (interested_parties_id);
CREATE INDEX "ix_AIManagementSystem_interested_parties_AIManagementSystem_id" ON "AIManagementSystem_interested_parties" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_ai_objectives" (
	"AIManagementSystem_id" TEXT,
	ai_objectives_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_objectives_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_objectives_id) REFERENCES "AIObjective" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_objectives_AIManagementSystem_id" ON "AIManagementSystem_ai_objectives" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_ai_objectives_ai_objectives_id" ON "AIManagementSystem_ai_objectives" (ai_objectives_id);

CREATE TABLE "AIManagementSystem_reference_controls" (
	"AIManagementSystem_id" TEXT,
	reference_controls_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", reference_controls_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(reference_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIManagementSystem_reference_controls_reference_controls_id" ON "AIManagementSystem_reference_controls" (reference_controls_id);
CREATE INDEX "ix_AIManagementSystem_reference_controls_AIManagementSystem_id" ON "AIManagementSystem_reference_controls" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_ai_systems" (
	"AIManagementSystem_id" TEXT,
	ai_systems_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_systems_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_systems_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_systems_ai_systems_id" ON "AIManagementSystem_ai_systems" (ai_systems_id);
CREATE INDEX "ix_AIManagementSystem_ai_systems_AIManagementSystem_id" ON "AIManagementSystem_ai_systems" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_roles" (
	"AIManagementSystem_id" TEXT,
	roles_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", roles_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(roles_id) REFERENCES "Role" (id)
);
CREATE INDEX "ix_AIManagementSystem_roles_AIManagementSystem_id" ON "AIManagementSystem_roles" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_roles_roles_id" ON "AIManagementSystem_roles" (roles_id);

CREATE TABLE "AIManagementSystem_resources" (
	"AIManagementSystem_id" TEXT,
	resources_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", resources_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(resources_id) REFERENCES "Resource" (id)
);
CREATE INDEX "ix_AIManagementSystem_resources_resources_id" ON "AIManagementSystem_resources" (resources_id);
CREATE INDEX "ix_AIManagementSystem_resources_AIManagementSystem_id" ON "AIManagementSystem_resources" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_competence_records" (
	"AIManagementSystem_id" TEXT,
	competence_records_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", competence_records_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(competence_records_id) REFERENCES "CompetenceRecord" (id)
);
CREATE INDEX "ix_AIManagementSystem_competence_records_AIManagementSystem_id" ON "AIManagementSystem_competence_records" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_competence_records_competence_records_id" ON "AIManagementSystem_competence_records" (competence_records_id);

CREATE TABLE "AIManagementSystem_documented_information_register" (
	"AIManagementSystem_id" TEXT,
	documented_information_register_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", documented_information_register_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(documented_information_register_id) REFERENCES "DocumentedInformation" (id)
);
CREATE INDEX "ix_AIManagementSystem_documented_information_register_documented_information_register_id" ON "AIManagementSystem_documented_information_register" (documented_information_register_id);
CREATE INDEX "ix_AIManagementSystem_documented_information_register_AIManagementSystem_id" ON "AIManagementSystem_documented_information_register" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_operational_procedures" (
	"AIManagementSystem_id" TEXT,
	operational_procedures_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", operational_procedures_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(operational_procedures_id) REFERENCES "OperationalProcedure" (id)
);
CREATE INDEX "ix_AIManagementSystem_operational_procedures_AIManagementSystem_id" ON "AIManagementSystem_operational_procedures" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_operational_procedures_operational_procedures_id" ON "AIManagementSystem_operational_procedures" (operational_procedures_id);

CREATE TABLE "AIManagementSystem_ai_risk_assessments" (
	"AIManagementSystem_id" TEXT,
	ai_risk_assessments_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_risk_assessments_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_risk_assessments_id) REFERENCES "AIRiskAssessment" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_risk_assessments_AIManagementSystem_id" ON "AIManagementSystem_ai_risk_assessments" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_ai_risk_assessments_ai_risk_assessments_id" ON "AIManagementSystem_ai_risk_assessments" (ai_risk_assessments_id);

CREATE TABLE "AIManagementSystem_ai_risk_treatment_plans" (
	"AIManagementSystem_id" TEXT,
	ai_risk_treatment_plans_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_risk_treatment_plans_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_risk_treatment_plans_id) REFERENCES "AIRiskTreatmentPlan" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_risk_treatment_plans_ai_risk_treatment_plans_id" ON "AIManagementSystem_ai_risk_treatment_plans" (ai_risk_treatment_plans_id);
CREATE INDEX "ix_AIManagementSystem_ai_risk_treatment_plans_AIManagementSystem_id" ON "AIManagementSystem_ai_risk_treatment_plans" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_ai_system_impact_assessments" (
	"AIManagementSystem_id" TEXT,
	ai_system_impact_assessments_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_system_impact_assessments_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_system_impact_assessments_id) REFERENCES "AISystemImpactAssessment" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_system_impact_assessments_ai_system_impact_assessments_id" ON "AIManagementSystem_ai_system_impact_assessments" (ai_system_impact_assessments_id);
CREATE INDEX "ix_AIManagementSystem_ai_system_impact_assessments_AIManagementSystem_id" ON "AIManagementSystem_ai_system_impact_assessments" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_internal_audits" (
	"AIManagementSystem_id" TEXT,
	internal_audits_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", internal_audits_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(internal_audits_id) REFERENCES "InternalAudit" (id)
);
CREATE INDEX "ix_AIManagementSystem_internal_audits_AIManagementSystem_id" ON "AIManagementSystem_internal_audits" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_internal_audits_internal_audits_id" ON "AIManagementSystem_internal_audits" (internal_audits_id);

CREATE TABLE "AIManagementSystem_management_reviews" (
	"AIManagementSystem_id" TEXT,
	management_reviews_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", management_reviews_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(management_reviews_id) REFERENCES "ManagementReview" (id)
);
CREATE INDEX "ix_AIManagementSystem_management_reviews_AIManagementSystem_id" ON "AIManagementSystem_management_reviews" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_management_reviews_management_reviews_id" ON "AIManagementSystem_management_reviews" (management_reviews_id);

CREATE TABLE "AIManagementSystem_nonconformities" (
	"AIManagementSystem_id" TEXT,
	nonconformities_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", nonconformities_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(nonconformities_id) REFERENCES "Nonconformity" (id)
);
CREATE INDEX "ix_AIManagementSystem_nonconformities_nonconformities_id" ON "AIManagementSystem_nonconformities" (nonconformities_id);
CREATE INDEX "ix_AIManagementSystem_nonconformities_AIManagementSystem_id" ON "AIManagementSystem_nonconformities" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_corrective_actions" (
	"AIManagementSystem_id" TEXT,
	corrective_actions_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", corrective_actions_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(corrective_actions_id) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_AIManagementSystem_corrective_actions_corrective_actions_id" ON "AIManagementSystem_corrective_actions" (corrective_actions_id);
CREATE INDEX "ix_AIManagementSystem_corrective_actions_AIManagementSystem_id" ON "AIManagementSystem_corrective_actions" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_improvements" (
	"AIManagementSystem_id" TEXT,
	improvements_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", improvements_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(improvements_id) REFERENCES "ImprovementOpportunity" (id)
);
CREATE INDEX "ix_AIManagementSystem_improvements_AIManagementSystem_id" ON "AIManagementSystem_improvements" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_improvements_improvements_id" ON "AIManagementSystem_improvements" (improvements_id);

CREATE TABLE "AIManagementSystem_third_party_relationships" (
	"AIManagementSystem_id" TEXT,
	third_party_relationships_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", third_party_relationships_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(third_party_relationships_id) REFERENCES "ThirdPartyRelationship" (id)
);
CREATE INDEX "ix_AIManagementSystem_third_party_relationships_AIManagementSystem_id" ON "AIManagementSystem_third_party_relationships" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_third_party_relationships_third_party_relationships_id" ON "AIManagementSystem_third_party_relationships" (third_party_relationships_id);

CREATE TABLE "AIManagementSystem_ai_incidents" (
	"AIManagementSystem_id" TEXT,
	ai_incidents_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_incidents_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_incidents_id) REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_incidents_ai_incidents_id" ON "AIManagementSystem_ai_incidents" (ai_incidents_id);
CREATE INDEX "ix_AIManagementSystem_ai_incidents_AIManagementSystem_id" ON "AIManagementSystem_ai_incidents" ("AIManagementSystem_id");

CREATE TABLE "AIManagementSystem_concern_reports" (
	"AIManagementSystem_id" TEXT,
	concern_reports_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", concern_reports_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(concern_reports_id) REFERENCES "ConcernReport" (id)
);
CREATE INDEX "ix_AIManagementSystem_concern_reports_AIManagementSystem_id" ON "AIManagementSystem_concern_reports" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_concern_reports_concern_reports_id" ON "AIManagementSystem_concern_reports" (concern_reports_id);

CREATE TABLE "AIPolicy_related_topic_policies" (
	"AIPolicy_id" TEXT,
	related_topic_policies_id TEXT,
	PRIMARY KEY ("AIPolicy_id", related_topic_policies_id),
	FOREIGN KEY("AIPolicy_id") REFERENCES "AIPolicy" (id),
	FOREIGN KEY(related_topic_policies_id) REFERENCES "TopicSpecificPolicy" (id)
);
CREATE INDEX "ix_AIPolicy_related_topic_policies_AIPolicy_id" ON "AIPolicy_related_topic_policies" ("AIPolicy_id");
CREATE INDEX "ix_AIPolicy_related_topic_policies_related_topic_policies_id" ON "AIPolicy_related_topic_policies" (related_topic_policies_id);

CREATE TABLE "TopicSpecificPolicy_applicable_controls" (
	"TopicSpecificPolicy_id" TEXT,
	applicable_controls_id TEXT,
	PRIMARY KEY ("TopicSpecificPolicy_id", applicable_controls_id),
	FOREIGN KEY("TopicSpecificPolicy_id") REFERENCES "TopicSpecificPolicy" (id),
	FOREIGN KEY(applicable_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_TopicSpecificPolicy_applicable_controls_TopicSpecificPolicy_id" ON "TopicSpecificPolicy_applicable_controls" ("TopicSpecificPolicy_id");
CREATE INDEX "ix_TopicSpecificPolicy_applicable_controls_applicable_controls_id" ON "TopicSpecificPolicy_applicable_controls" (applicable_controls_id);

CREATE TABLE "AIObjective_related_risks" (
	"AIObjective_id" TEXT,
	related_risks_id TEXT,
	PRIMARY KEY ("AIObjective_id", related_risks_id),
	FOREIGN KEY("AIObjective_id") REFERENCES "AIObjective" (id),
	FOREIGN KEY(related_risks_id) REFERENCES "AIRisk" (id)
);
CREATE INDEX "ix_AIObjective_related_risks_related_risks_id" ON "AIObjective_related_risks" (related_risks_id);
CREATE INDEX "ix_AIObjective_related_risks_AIObjective_id" ON "AIObjective_related_risks" ("AIObjective_id");

CREATE TABLE "AIObjective_related_controls" (
	"AIObjective_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("AIObjective_id", related_controls_id),
	FOREIGN KEY("AIObjective_id") REFERENCES "AIObjective" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIObjective_related_controls_related_controls_id" ON "AIObjective_related_controls" (related_controls_id);
CREATE INDEX "ix_AIObjective_related_controls_AIObjective_id" ON "AIObjective_related_controls" ("AIObjective_id");

CREATE TABLE "AIRiskAssessment_ai_systems_assessed" (
	"AIRiskAssessment_id" TEXT,
	ai_systems_assessed_id TEXT,
	PRIMARY KEY ("AIRiskAssessment_id", ai_systems_assessed_id),
	FOREIGN KEY("AIRiskAssessment_id") REFERENCES "AIRiskAssessment" (id),
	FOREIGN KEY(ai_systems_assessed_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AIRiskAssessment_ai_systems_assessed_ai_systems_assessed_id" ON "AIRiskAssessment_ai_systems_assessed" (ai_systems_assessed_id);
CREATE INDEX "ix_AIRiskAssessment_ai_systems_assessed_AIRiskAssessment_id" ON "AIRiskAssessment_ai_systems_assessed" ("AIRiskAssessment_id");

CREATE TABLE "AIRiskAssessment_risks_identified" (
	"AIRiskAssessment_id" TEXT,
	risks_identified_id TEXT,
	PRIMARY KEY ("AIRiskAssessment_id", risks_identified_id),
	FOREIGN KEY("AIRiskAssessment_id") REFERENCES "AIRiskAssessment" (id),
	FOREIGN KEY(risks_identified_id) REFERENCES "AIRisk" (id)
);
CREATE INDEX "ix_AIRiskAssessment_risks_identified_AIRiskAssessment_id" ON "AIRiskAssessment_risks_identified" ("AIRiskAssessment_id");
CREATE INDEX "ix_AIRiskAssessment_risks_identified_risks_identified_id" ON "AIRiskAssessment_risks_identified" (risks_identified_id);

CREATE TABLE "AIRiskAssessment_recommendations" (
	"AIRiskAssessment_id" TEXT,
	recommendations TEXT,
	PRIMARY KEY ("AIRiskAssessment_id", recommendations),
	FOREIGN KEY("AIRiskAssessment_id") REFERENCES "AIRiskAssessment" (id)
);
CREATE INDEX "ix_AIRiskAssessment_recommendations_AIRiskAssessment_id" ON "AIRiskAssessment_recommendations" ("AIRiskAssessment_id");
CREATE INDEX "ix_AIRiskAssessment_recommendations_recommendations" ON "AIRiskAssessment_recommendations" (recommendations);

CREATE TABLE "AIRisk_affected_ai_systems" (
	"AIRisk_id" TEXT,
	affected_ai_systems_id TEXT,
	PRIMARY KEY ("AIRisk_id", affected_ai_systems_id),
	FOREIGN KEY("AIRisk_id") REFERENCES "AIRisk" (id),
	FOREIGN KEY(affected_ai_systems_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AIRisk_affected_ai_systems_AIRisk_id" ON "AIRisk_affected_ai_systems" ("AIRisk_id");
CREATE INDEX "ix_AIRisk_affected_ai_systems_affected_ai_systems_id" ON "AIRisk_affected_ai_systems" (affected_ai_systems_id);

CREATE TABLE "AIRisk_affected_dimensions" (
	"AIRisk_id" TEXT,
	affected_dimensions VARCHAR(14),
	PRIMARY KEY ("AIRisk_id", affected_dimensions),
	FOREIGN KEY("AIRisk_id") REFERENCES "AIRisk" (id)
);
CREATE INDEX "ix_AIRisk_affected_dimensions_affected_dimensions" ON "AIRisk_affected_dimensions" (affected_dimensions);
CREATE INDEX "ix_AIRisk_affected_dimensions_AIRisk_id" ON "AIRisk_affected_dimensions" ("AIRisk_id");

CREATE TABLE "AIRisk_existing_controls" (
	"AIRisk_id" TEXT,
	existing_controls_id TEXT,
	PRIMARY KEY ("AIRisk_id", existing_controls_id),
	FOREIGN KEY("AIRisk_id") REFERENCES "AIRisk" (id),
	FOREIGN KEY(existing_controls_id) REFERENCES "AIReferenceControl" (id)
);
CREATE INDEX "ix_AIRisk_existing_controls_AIRisk_id" ON "AIRisk_existing_controls" ("AIRisk_id");
CREATE INDEX "ix_AIRisk_existing_controls_existing_controls_id" ON "AIRisk_existing_controls" (existing_controls_id);

CREATE TABLE "AIRiskTreatmentPlan_risks_addressed" (
	"AIRiskTreatmentPlan_id" TEXT,
	risks_addressed_id TEXT,
	PRIMARY KEY ("AIRiskTreatmentPlan_id", risks_addressed_id),
	FOREIGN KEY("AIRiskTreatmentPlan_id") REFERENCES "AIRiskTreatmentPlan" (id),
	FOREIGN KEY(risks_addressed_id) REFERENCES "AIRisk" (id)
);
CREATE INDEX "ix_AIRiskTreatmentPlan_risks_addressed_risks_addressed_id" ON "AIRiskTreatmentPlan_risks_addressed" (risks_addressed_id);
CREATE INDEX "ix_AIRiskTreatmentPlan_risks_addressed_AIRiskTreatmentPlan_id" ON "AIRiskTreatmentPlan_risks_addressed" ("AIRiskTreatmentPlan_id");

CREATE TABLE "StatementOfApplicability_soa_entries" (
	"StatementOfApplicability_id" TEXT,
	soa_entries_id INTEGER,
	PRIMARY KEY ("StatementOfApplicability_id", soa_entries_id),
	FOREIGN KEY("StatementOfApplicability_id") REFERENCES "StatementOfApplicability" (id),
	FOREIGN KEY(soa_entries_id) REFERENCES "SoAEntry" (id)
);
CREATE INDEX "ix_StatementOfApplicability_soa_entries_StatementOfApplicability_id" ON "StatementOfApplicability_soa_entries" ("StatementOfApplicability_id");
CREATE INDEX "ix_StatementOfApplicability_soa_entries_soa_entries_id" ON "StatementOfApplicability_soa_entries" (soa_entries_id);

CREATE TABLE "Nonconformity_linked_corrective_actions" (
	"Nonconformity_id" TEXT,
	linked_corrective_actions_id TEXT,
	PRIMARY KEY ("Nonconformity_id", linked_corrective_actions_id),
	FOREIGN KEY("Nonconformity_id") REFERENCES "Nonconformity" (id),
	FOREIGN KEY(linked_corrective_actions_id) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_Nonconformity_linked_corrective_actions_Nonconformity_id" ON "Nonconformity_linked_corrective_actions" ("Nonconformity_id");
CREATE INDEX "ix_Nonconformity_linked_corrective_actions_linked_corrective_actions_id" ON "Nonconformity_linked_corrective_actions" (linked_corrective_actions_id);

CREATE TABLE "AIIncident_affected_ai_systems" (
	"AIIncident_id" TEXT,
	affected_ai_systems_id TEXT,
	PRIMARY KEY ("AIIncident_id", affected_ai_systems_id),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id),
	FOREIGN KEY(affected_ai_systems_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AIIncident_affected_ai_systems_affected_ai_systems_id" ON "AIIncident_affected_ai_systems" (affected_ai_systems_id);
CREATE INDEX "ix_AIIncident_affected_ai_systems_AIIncident_id" ON "AIIncident_affected_ai_systems" ("AIIncident_id");

CREATE TABLE "AIIncident_affected_dimensions" (
	"AIIncident_id" TEXT,
	affected_dimensions VARCHAR(14),
	PRIMARY KEY ("AIIncident_id", affected_dimensions),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_affected_dimensions_AIIncident_id" ON "AIIncident_affected_dimensions" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_affected_dimensions_affected_dimensions" ON "AIIncident_affected_dimensions" (affected_dimensions);

CREATE TABLE "AIIncident_response_actions" (
	"AIIncident_id" TEXT,
	response_actions TEXT,
	PRIMARY KEY ("AIIncident_id", response_actions),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_response_actions_response_actions" ON "AIIncident_response_actions" (response_actions);
CREATE INDEX "ix_AIIncident_response_actions_AIIncident_id" ON "AIIncident_response_actions" ("AIIncident_id");

CREATE TABLE "AIIncident_containment_actions" (
	"AIIncident_id" TEXT,
	containment_actions TEXT,
	PRIMARY KEY ("AIIncident_id", containment_actions),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_containment_actions_AIIncident_id" ON "AIIncident_containment_actions" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_containment_actions_containment_actions" ON "AIIncident_containment_actions" (containment_actions);

CREATE TABLE "AIIncident_recovery_actions" (
	"AIIncident_id" TEXT,
	recovery_actions TEXT,
	PRIMARY KEY ("AIIncident_id", recovery_actions),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_recovery_actions_AIIncident_id" ON "AIIncident_recovery_actions" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_recovery_actions_recovery_actions" ON "AIIncident_recovery_actions" (recovery_actions);

CREATE TABLE "AIIncident_lessons_learned" (
	"AIIncident_id" TEXT,
	lessons_learned TEXT,
	PRIMARY KEY ("AIIncident_id", lessons_learned),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_lessons_learned_AIIncident_id" ON "AIIncident_lessons_learned" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_lessons_learned_lessons_learned" ON "AIIncident_lessons_learned" (lessons_learned);

CREATE TABLE "AIIncident_evidence_collected" (
	"AIIncident_id" TEXT,
	evidence_collected TEXT,
	PRIMARY KEY ("AIIncident_id", evidence_collected),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_evidence_collected_evidence_collected" ON "AIIncident_evidence_collected" (evidence_collected);
CREATE INDEX "ix_AIIncident_evidence_collected_AIIncident_id" ON "AIIncident_evidence_collected" ("AIIncident_id");

CREATE TABLE "AIIncident_notifications_made" (
	"AIIncident_id" TEXT,
	notifications_made TEXT,
	PRIMARY KEY ("AIIncident_id", notifications_made),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_notifications_made_AIIncident_id" ON "AIIncident_notifications_made" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_notifications_made_notifications_made" ON "AIIncident_notifications_made" (notifications_made);

CREATE TABLE "AIIncident_external_reports" (
	"AIIncident_id" TEXT,
	external_reports TEXT,
	PRIMARY KEY ("AIIncident_id", external_reports),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_AIIncident_external_reports_AIIncident_id" ON "AIIncident_external_reports" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_external_reports_external_reports" ON "AIIncident_external_reports" (external_reports);

CREATE TABLE "AIIncident_linked_corrective_actions" (
	"AIIncident_id" TEXT,
	linked_corrective_actions_id TEXT,
	PRIMARY KEY ("AIIncident_id", linked_corrective_actions_id),
	FOREIGN KEY("AIIncident_id") REFERENCES "AIIncident" (id),
	FOREIGN KEY(linked_corrective_actions_id) REFERENCES "CorrectiveAction" (id)
);
CREATE INDEX "ix_AIIncident_linked_corrective_actions_AIIncident_id" ON "AIIncident_linked_corrective_actions" ("AIIncident_id");
CREATE INDEX "ix_AIIncident_linked_corrective_actions_linked_corrective_actions_id" ON "AIIncident_linked_corrective_actions" (linked_corrective_actions_id);

CREATE TABLE "ConcernReport_related_incidents" (
	"ConcernReport_id" TEXT,
	related_incidents_id TEXT,
	PRIMARY KEY ("ConcernReport_id", related_incidents_id),
	FOREIGN KEY("ConcernReport_id") REFERENCES "ConcernReport" (id),
	FOREIGN KEY(related_incidents_id) REFERENCES "AIIncident" (id)
);
CREATE INDEX "ix_ConcernReport_related_incidents_ConcernReport_id" ON "ConcernReport_related_incidents" ("ConcernReport_id");
CREATE INDEX "ix_ConcernReport_related_incidents_related_incidents_id" ON "ConcernReport_related_incidents" (related_incidents_id);

CREATE TABLE "AIManagementSystem_ai_system_events" (
	"AIManagementSystem_id" TEXT,
	ai_system_events_id TEXT,
	PRIMARY KEY ("AIManagementSystem_id", ai_system_events_id),
	FOREIGN KEY("AIManagementSystem_id") REFERENCES "AIManagementSystem" (id),
	FOREIGN KEY(ai_system_events_id) REFERENCES "AISystemEvent" (id)
);
CREATE INDEX "ix_AIManagementSystem_ai_system_events_AIManagementSystem_id" ON "AIManagementSystem_ai_system_events" ("AIManagementSystem_id");
CREATE INDEX "ix_AIManagementSystem_ai_system_events_ai_system_events_id" ON "AIManagementSystem_ai_system_events" (ai_system_events_id);

CREATE TABLE "InternalAudit_findings" (
	"InternalAudit_id" TEXT,
	findings_id TEXT,
	PRIMARY KEY ("InternalAudit_id", findings_id),
	FOREIGN KEY("InternalAudit_id") REFERENCES "InternalAudit" (id),
	FOREIGN KEY(findings_id) REFERENCES "AuditFinding" (id)
);
CREATE INDEX "ix_InternalAudit_findings_InternalAudit_id" ON "InternalAudit_findings" ("InternalAudit_id");
CREATE INDEX "ix_InternalAudit_findings_findings_id" ON "InternalAudit_findings" (findings_id);

CREATE TABLE "AISystemEvent_affected_ai_systems" (
	"AISystemEvent_id" TEXT,
	affected_ai_systems_id TEXT,
	PRIMARY KEY ("AISystemEvent_id", affected_ai_systems_id),
	FOREIGN KEY("AISystemEvent_id") REFERENCES "AISystemEvent" (id),
	FOREIGN KEY(affected_ai_systems_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystemEvent_affected_ai_systems_AISystemEvent_id" ON "AISystemEvent_affected_ai_systems" ("AISystemEvent_id");
CREATE INDEX "ix_AISystemEvent_affected_ai_systems_affected_ai_systems_id" ON "AISystemEvent_affected_ai_systems" (affected_ai_systems_id);
