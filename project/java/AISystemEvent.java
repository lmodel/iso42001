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
  An AI system event detected by monitoring, users, or external reporting channels. Events may or may not be subsequently classified as incidents. Supports A.6.2.8 event log capture and A.8.3 external reporting workflows.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AISystemEvent extends NamedEntity {

  private ZonedDateTime eventDatetime;
  private String reporter;
  private String reporterPartyType;
  private String eventSource;
  private String eventDescription;
  private List<AISystem> affectedAiSystems;
  private String initialAssessment;
  private Boolean categorizedAsIncident;
  private AIIncident linkedIncident;


}