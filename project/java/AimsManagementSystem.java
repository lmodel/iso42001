package example;

/* metamodel_version: 1.12.0 */
/* version: 2023 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One organization's management system for AI: its scope and context, and every record it keeps, each kind in a list of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsManagementSystem  {

  private AimsOrganization aimsOrganization;
  private String aimsTopManagement;
  private String aimsGoverningBody;
  private List<String> aimsLeadershipEvidence;
  private String aimsScope;
  private List<String> aimsScopeBoundaries;
  private List<String> aimsScopeApplicability;
  private String aimsProcesses;
  private List<String> aimsInternalIssues;
  private List<String> aimsExternalIssues;
  private List<String> aimsPlannedChanges;
  private List<String> aimsExternalServices;
  private List<String> aimsIntegratedStandards;
  private String aimsCertificationStatus;
  private String aimsCertificationBody;
  private LocalDate aimsCertificationDate;
  private LocalDate aimsRecertificationDate;
  private List<AimsInterestedParty> aimsInterestedParties;
  private AimsPolicy aimsPolicy;
  private List<AimsTopicSpecificPolicy> aimsTopicSpecificPolicies;
  private List<AimsRole> aimsRoles;
  private List<AimsObjective> aimsObjectives;
  private List<AimsPlannedAction> aimsPlannedActions;
  private AimsRiskAssessmentProcess aimsRiskAssessmentProcess;
  private AimsRiskTreatmentProcess aimsRiskTreatmentProcess;
  private AimsImpactAssessmentProcess aimsImpactAssessmentProcess;
  private List<AimsRiskAssessment> aimsRiskAssessments;
  private List<AimsRisk> aimsRisks;
  private List<AimsRiskTreatmentPlan> aimsRiskTreatmentPlans;
  private List<AimsImpactAssessment> aimsImpactAssessments;
  private AimsStatementOfApplicability aimsStatementOfApplicability;
  private List<AimsControl> aimsControls;
  private List<AimsAiSystem> aimsSystems;
  private List<AimsSystemResource> aimsSystemResources;
  private List<AimsDevelopmentProcess> aimsDevelopmentProcesses;
  private List<AimsResponsibleUseProcess> aimsUseProcesses;
  private List<AimsTechnicalDocumentation> aimsTechnicalDocumentation;
  private List<AimsUserInformation> aimsUserInformation;
  private List<AimsIncidentCommunicationPlan> aimsIncidentCommunicationPlans;
  private List<AimsReportingObligation> aimsReportingObligations;
  private List<AimsThirdPartyRelationship> aimsThirdPartyRelationships;
  private List<AimsResource> aimsResources;
  private List<AimsCompetenceRecord> aimsCompetenceRecords;
  private AimsAwarenessProgramme aimsAwarenessProgramme;
  private AimsCommunicationPlan aimsCommunicationPlan;
  private List<AimsDocumentedInformation> aimsDocumentedInformation;
  private List<AimsOperationalProcedure> aimsOperationalProcedures;
  private AimsMonitoringProgramme aimsMonitoringProgramme;
  private List<AimsAuditProgramme> aimsAuditProgrammes;
  private List<AimsAudit> aimsAudits;
  private List<AimsManagementReview> aimsManagementReviews;
  private List<AimsNonconformity> aimsNonconformities;
  private List<AimsCorrectiveAction> aimsCorrectiveActions;
  private List<AimsImprovementOpportunity> aimsImprovements;
  private List<AimsSystemEvent> aimsSystemEvents;
  private AimsConcernReportingProcess aimsConcernReportingProcess;
  private List<AimsConcernReport> aimsConcernReports;
  private URI aimsId;
  private String title;
  private String description;


}