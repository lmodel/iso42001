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
  An audit of the system: an internal audit, or one by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsAudit  {

  private String aimsAuditType;
  private List<String> aimsAuditStandards;
  private String aimsAuditScope;
  private List<String> aimsAuditCriteria;
  private List<String> aimsAuditObjectives;
  private LocalDate aimsAuditPeriodStart;
  private LocalDate aimsAuditPeriodEnd;
  private String aimsAuditLead;
  private List<String> aimsAuditTeam;
  private List<String> aimsAuditAuditees;
  private AimsDocumentedInformation aimsAuditPlan;
  private List<AimsAuditFinding> aimsAuditFindings;
  private String aimsAuditConclusion;
  private LocalDate aimsAuditReportDate;
  private List<String> aimsAuditReportDistribution;
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