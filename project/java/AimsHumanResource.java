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
  People an AI system draws on: their skills and the work they do on it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsHumanResource extends AimsSystemResource {

  private AimsRole aimsHumanRole;
  private List<String> aimsHumanCompetences;
  private List<String> aimsHumanActivities;
  private String aimsHumanDiversity;


}