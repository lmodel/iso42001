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
  The programme that tells people working for the organization about the AI policy, their part in the system and what failing it would mean.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsAwarenessProgramme  {

  private List<String> aimsAwarenessTopics;
  private List<String> aimsAwarenessMethods;
  private String aimsAwarenessAudience;
  private String aimsAwarenessFrequency;
  private String aimsAwarenessCompletionTracking;
  private String aimsAwarenessEffectiveness;
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