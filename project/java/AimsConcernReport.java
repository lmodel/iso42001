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
  One worry someone raised about the organization's part in a system, and how it was looked into and settled.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsConcernReport  {

  private List<AimsAiSystem> aimsAiSystems;
  private LocalDate aimsConcernReportedOn;
  private String aimsConcernReporter;
  private Boolean aimsConcernAnonymous;
  private String aimsConcernChannel;
  private String aimsConcernLifeCycleStage;
  private String aimsConcernSeverity;
  private String aimsConcernInvestigator;
  private String aimsConcernInvestigationStatus;
  private String aimsConcernFindings;
  private String aimsConcernEscalation;
  private LocalDate aimsConcernResponseDue;
  private LocalDate aimsConcernRespondedOn;
  private String aimsConcernResolution;
  private String aimsConcernReprisalProtection;
  private List<AimsIncident> aimsConcernIncidents;
  private List<AimsNonconformity> aimsConcernNonconformities;
  private URI aimsId;
  private String title;
  private String description;


}