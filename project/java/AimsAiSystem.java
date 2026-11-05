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
  One AI system under the management system: what it is for, how it is built, run and overseen, what it draws on, and what is kept about it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsAiSystem  {

  private List<AimsControl> aimsRelevantControls;
  private String aimsSystemIntendedPurpose;
  private List<String> aimsSystemIntendedUses;
  private List<String> aimsSystemForeseeableMisuse;
  private String aimsSystemDomain;
  private String aimsSystemDeploymentContext;
  private String aimsSystemLifeCycleStage;
  private List<String> aimsSystemOrganizationRoles;
  private List<String> aimsSystemPiiRoles;
  private String aimsSystemRationale;
  private List<String> aimsSystemRequirements;
  private String aimsSystemMlApproach;
  private List<String> aimsSystemModelTypes;
  private Boolean aimsSystemContinuousLearning;
  private String aimsSystemAutomationLevel;
  private List<String> aimsSystemThreats;
  private List<String> aimsSystemVerificationMeasures;
  private List<String> aimsSystemEvaluationCriteria;
  private List<String> aimsSystemReleaseCriteria;
  private AimsDocumentedInformation aimsSystemDeploymentPlan;
  private List<String> aimsSystemOperationElements;
  private List<String> aimsSystemPerformanceMetrics;
  private List<String> aimsSystemLogStages;
  private List<String> aimsSystemLogContents;
  private String aimsSystemLogRetention;
  private Boolean aimsSystemHumanOversightRequired;
  private String aimsSystemHumanOversight;
  private List<String> aimsSystemHumanOversightStages;
  private List<AimsSystemResource> aimsSystemResourcesUsed;
  private List<AimsTechnicalDocumentation> aimsSystemTechnicalDocuments;
  private List<AimsImpactAssessment> aimsSystemImpactAssessments;
  private List<AimsThirdPartyRelationship> aimsSystemRelationships;
  private URI aimsId;
  private String title;
  private String description;


}