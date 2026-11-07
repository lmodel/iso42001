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
  One risk assessment carried out under the process, and what it found.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRiskAssessment  {

  private List<AimsAiSystem> aimsAiSystems;
  private String aimsAssessmentScope;
  private LocalDate aimsAssessmentDate;
  private String aimsAssessmentAssessor;
  private String aimsAssessmentMethodUsed;
  private List<AimsRisk> aimsAssessmentRisks;
  private List<AimsImpactAssessment> aimsAssessmentImpactAssessments;
  private String aimsAssessmentSummary;
  private List<String> aimsAssessmentRecommendations;
  private LocalDate aimsAssessmentNextDate;
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