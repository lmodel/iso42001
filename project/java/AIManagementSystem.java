package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Top-level container representing an organization's complete AI Management System (AIMS) per ISO/IEC 42001:2023. Aggregates all components required to support the AIMS lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIManagementSystem extends NamedEntity {

  private Organization organization;
  private String scopeStatement;
  private List<String> scopeBoundaries;
  private List<String> scopeExclusions;
  private List<String> contextInternalIssues;
  private List<String> contextExternalIssues;
  private List<String> organizationalRolesWithAi;
  private List<String> integratedManagementSystems;
  private String topManagement;
  private String governingBody;
  private List<String> leadershipCommitmentEvidence;
  private List<String> plannedChanges;
  private List<InterestedParty> interestedParties;
  private AIPolicy aiPolicy;
  private List<AIObjective> aiObjectives;
  private AIRiskAssessmentProcess aiRiskAssessmentProcess;
  private AIRiskTreatmentProcess aiRiskTreatmentProcess;
  private AISystemImpactAssessmentProcess aiSystemImpactAssessmentProcess;
  private StatementOfApplicability statementOfApplicability;
  private List<AIReferenceControl> referenceControls;
  private List<AISystem> aiSystems;
  private List<Role> roles;
  private List<Resource> resources;
  private List<CompetenceRecord> competenceRecords;
  private AwarenessProgram awarenessProgram;
  private CommunicationPlan communicationPlan;
  private List<DocumentedInformation> documentedInformationRegister;
  private List<OperationalProcedure> operationalProcedures;
  private List<AIRiskAssessment> aiRiskAssessments;
  private List<AIRiskTreatmentPlan> aiRiskTreatmentPlans;
  private List<AISystemImpactAssessment> aiSystemImpactAssessments;
  private MonitoringProgram monitoringProgram;
  private List<InternalAudit> internalAudits;
  private List<ManagementReview> managementReviews;
  private List<Nonconformity> nonconformities;
  private List<CorrectiveAction> correctiveActions;
  private List<ImprovementOpportunity> improvements;
  private List<ThirdPartyRelationship> thirdPartyRelationships;
  private String certificationStatus;
  private String certificationBody;
  private LocalDate certificationDate;
  private LocalDate recertificationDate;
  private List<AISystemEvent> aiSystemEvents;
  private List<AIIncident> aiIncidents;
  private List<ConcernReport> concernReports;


}