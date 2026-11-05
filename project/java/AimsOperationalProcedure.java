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
  A procedure by which the organization plans and controls the processes that meet its requirements, such as managing data for building or vetting suppliers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsOperationalProcedure  {

  private List<AimsControl> aimsRelevantControls;
  private List<String> aimsCitedAnnexAControls;
  private String aimsProcedureScope;
  private String aimsProcedureCriteria;
  private List<String> aimsProcedureControlMeasures;
  private List<AimsRole> aimsProcedureRoles;
  private String aimsProcedureChangeControl;
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