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
  The process for working out what AI systems may do to people and society: when it applies, what it takes in, who runs it and how the results are used.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsImpactAssessmentProcess  {

  private List<String> aimsImpactProcessTriggers;
  private String aimsImpactProcessInterval;
  private List<String> aimsImpactProcessSteps;
  private String aimsImpactProcessAssessors;
  private String aimsImpactProcessUse;
  private List<String> aimsImpactProcessSubjects;
  private List<String> aimsImpactProcessAreas;
  private String aimsImpactProcessRetention;
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