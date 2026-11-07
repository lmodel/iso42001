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
  A process for designing and building an AI system responsibly: the life cycle it follows, and what it asks of testing, oversight, data and approvals.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsDevelopmentProcess  {

  private List<AimsAiSystem> aimsAiSystems;
  private String aimsDevelopmentLifeCycleModel;
  private String aimsDevelopmentTesting;
  private String aimsDevelopmentHumanOversight;
  private List<String> aimsDevelopmentImpactAssessmentStages;
  private String aimsDevelopmentTrainingDataRules;
  private String aimsDevelopmentExpertise;
  private List<String> aimsDevelopmentReleaseCriteria;
  private List<String> aimsDevelopmentApprovals;
  private String aimsDevelopmentChangeControl;
  private String aimsDevelopmentUsability;
  private String aimsDevelopmentPartyEngagement;
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