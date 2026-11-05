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
  A review of the system by top management: what it took in, what it decided and what it asked to be done.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsManagementReview  {

  private LocalDate aimsReviewHeldOn;
  private List<String> aimsReviewAttendees;
  private String aimsReviewPreviousActions;
  private String aimsReviewContextChanges;
  private String aimsReviewInterestedPartyChanges;
  private String aimsReviewNonconformityTrends;
  private String aimsReviewMonitoringTrends;
  private String aimsReviewAuditTrends;
  private List<String> aimsReviewImprovementOpportunities;
  private List<String> aimsReviewDecisions;
  private List<String> aimsReviewSystemChanges;
  private List<String> aimsReviewActions;
  private LocalDate aimsReviewNextDate;
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