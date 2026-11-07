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
  The organization's process for assessing AI risks: its criteria, scales and method, and when it runs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRiskAssessmentProcess  {

  private List<String> aimsRiskCriteria;
  private String aimsRiskPolicyAlignment;
  private String aimsRiskComparability;
  private String aimsRiskMethod;
  private String aimsRiskLikelihoodScale;
  private String aimsRiskConsequenceScale;
  private String aimsRiskMatrix;
  private String aimsRiskPrioritization;
  private String aimsRiskAssessmentInterval;
  private List<String> aimsRiskAssessmentTriggers;
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