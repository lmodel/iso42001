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
  The AI policy that top management sets: the organization's commitments and the frame for its AI objectives.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsPolicy  {

  private List<String> aimsCitedClauses;
  private List<String> aimsCitedAnnexAControls;
  private String aimsPolicyStatement;
  private String aimsPolicyObjectivesFramework;
  private List<String> aimsPolicyCommitments;
  private List<String> aimsPolicyPrinciples;
  private String aimsPolicyExceptionsProcess;
  private List<String> aimsPolicyInfluences;
  private List<String> aimsPolicyRelatedPolicies;
  private LocalDate aimsPolicyCommunicationDate;
  private String aimsPolicyAvailability;
  private AimsRole aimsPolicyReviewRole;
  private String aimsPolicyReviewInterval;
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