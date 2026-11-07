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
  The evidence of one person's competence for work that affects AI performance, and what is done to close any gap.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsCompetenceRecord  {

  private String aimsCompetencePerson;
  private AimsRole aimsCompetenceRole;
  private List<String> aimsCompetenceRequired;
  private List<String> aimsCompetenceEducation;
  private List<String> aimsCompetenceTraining;
  private List<String> aimsCompetenceExperience;
  private LocalDate aimsCompetenceAssessmentDate;
  private List<String> aimsCompetenceGaps;
  private List<String> aimsCompetenceActions;
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