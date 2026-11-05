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
  The plan for telling users when a system goes wrong: which incidents, how soon, to which authorities, and with what details.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsIncidentCommunicationPlan  {

  private List<AimsAiSystem> aimsAiSystems;
  private List<String> aimsIncidentPlanCategories;
  private String aimsIncidentPlanTimeline;
  private List<String> aimsIncidentPlanAuthorities;
  private List<String> aimsIncidentPlanDetails;
  private String aimsIncidentPlanIntegration;
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