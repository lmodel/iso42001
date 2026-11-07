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
  One impact assessment carried out under the process: the systems and the setting it looked at, and each impact it found.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsImpactAssessment  {

  private List<AimsAiSystem> aimsAiSystems;
  private String aimsImpactScope;
  private String aimsImpactDiscipline;
  private LocalDate aimsImpactDate;
  private String aimsImpactAssessor;
  private String aimsImpactIntendedUse;
  private String aimsImpactForeseeableMisuse;
  private String aimsImpactTechnicalContext;
  private String aimsImpactSocietalContext;
  private List<String> aimsImpactJurisdictions;
  private List<String> aimsImpactDemographicGroups;
  private String aimsImpactSystemComplexity;
  private String aimsImpactHumanRole;
  private List<String> aimsImpactFailures;
  private String aimsImpactWorkforce;
  private List<AimsIdentifiedImpact> aimsImpactFindings;
  private List<AimsInterestedParty> aimsImpactSharedWith;
  private LocalDate aimsImpactNextDate;
  private URI aimsId;
  private String title;
  private String description;
  private String aimsDocumentReference;
  private String aimsDocumentVersion;
  private String aimsDocumentAuthor;
  private String aimsDocumentOwner;
  private String aimsDocumentFormat;
  private String aimsDocumentMedium;
  private String aimsDocumentApprover;
  private LocalDate aimsDocumentApprovalDate;
  private LocalDate aimsDocumentEffectiveDate;
  private LocalDate aimsDocumentLastReviewDate;
  private LocalDate aimsDocumentNextReviewDate;
  private String aimsDocumentStatus;
  private String aimsDocumentClassification;
  private String aimsDocumentRetention;
  private String aimsDocumentDisposition;
  private List<String> aimsDocumentDistribution;
  private String aimsDocumentStorage;
  private String aimsDocumentChangeControl;
  private Boolean aimsDocumentExternalOrigin;
  private String aimsDocumentExternalSource;


}