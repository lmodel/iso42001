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
  A plan to treat one or more risks: the actions and controls, who carries them out and when, and designated management's approval of the plan and of the risk left over.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRiskTreatmentPlan  {

  private String aimsImplementationState;
  private String aimsPlanScope;
  private List<AimsRisk> aimsPlanRisks;
  private List<String> aimsPlanActions;
  private List<AimsControl> aimsPlanControls;
  private String aimsPlanResources;
  private List<String> aimsPlanResponsibleParties;
  private String aimsPlanTimeline;
  private String aimsPlanApprover;
  private String aimsPlanResidualRiskAcceptance;
  private String aimsPlanEffectiveness;
  private String aimsPlanRevalidation;
  private LocalDate aimsPlanCompletionDate;
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