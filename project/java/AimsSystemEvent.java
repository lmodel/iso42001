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
  Something that happened with a system and was reported, by monitoring, by a user or by someone outside, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an AimsIncident.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsSystemEvent  {

  private List<AimsAiSystem> aimsAiSystems;
  private String aimsEventType;
  private ZonedDateTime aimsEventOccurredAt;
  private String aimsEventReporter;
  private String aimsEventSource;
  private String aimsEventAdverseImpact;
  private String aimsEventAssessment;
  private URI aimsId;
  private String title;
  private String description;


}