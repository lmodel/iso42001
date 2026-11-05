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
  An event assessed as an incident: what it concerns, how severe it is, what was done, who was told, and what was learned.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsIncident extends AimsSystemEvent {

  private String aimsIncidentCategory;
  private List<String> aimsIncidentThreats;
  private String aimsIncidentSeverity;
  private List<String> aimsIncidentImpactAreas;
  private String aimsIncidentDetectionMethod;
  private List<String> aimsIncidentResponseActions;
  private List<String> aimsIncidentRecoveryActions;
  private String aimsIncidentRootCause;
  private List<String> aimsIncidentLessonsLearned;
  private Boolean aimsIncidentNotificationRequired;
  private List<String> aimsIncidentNotifications;
  private List<AimsCorrectiveAction> aimsIncidentCorrectiveActions;
  private ZonedDateTime aimsIncidentClosedAt;


}