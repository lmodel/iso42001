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
  A programme of internal audits: the audits planned over a period, how often and why, and the resources and auditors they need.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsAuditProgramme  {

  private String aimsProgrammePeriod;
  private List<AimsAudit> aimsProgrammeAudits;
  private String aimsProgrammeFrequencyRationale;
  private String aimsProgrammeMethods;
  private List<String> aimsProgrammeResponsibilities;
  private String aimsProgrammeResources;
  private String aimsProgrammeAuditorSelection;
  private String aimsProgrammeStatus;
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