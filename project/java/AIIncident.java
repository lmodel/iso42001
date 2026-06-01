package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An AI incident, i.e., an AI system event determined to require response, escalation, or external communication. Captures triage, response lifecycle, and communications to users and other interested parties per A.8.4 and A.8.3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIIncident extends NamedEntity {

  private ZonedDateTime incidentDatetime;
  private String incidentCategory;
  private String severity;
  private List<AISystem> affectedAiSystems;
  private List<String> affectedDimensions;
  private String incidentDescription;
  private String detectionMethod;
  private List<String> responseActions;
  private List<String> containmentActions;
  private List<String> recoveryActions;
  private String rootCause;
  private List<String> lessonsLearned;
  private List<String> evidenceCollected;
  private Boolean notificationRequired;
  private List<String> notificationsMade;
  private List<String> externalReports;
  private CommunicationPlan communicationPlan;
  private List<CorrectiveAction> linkedCorrectiveActions;
  private ZonedDateTime closureDatetime;
  private String postIncidentReview;


}