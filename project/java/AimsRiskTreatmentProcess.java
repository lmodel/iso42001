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
  The organization's process for treating AI risks: how it chooses options and controls, checks them against Annex A and produces the Statement of Applicability and the plan.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRiskTreatmentProcess  {

  private String aimsTreatmentOptionsGuidance;
  private String aimsTreatmentControlSelection;
  private String aimsTreatmentAnnexAComparison;
  private String aimsTreatmentAdditionalControls;
  private String aimsTreatmentAnnexBUse;
  private String aimsTreatmentSoaTemplate;
  private String aimsTreatmentApprovalWorkflow;
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