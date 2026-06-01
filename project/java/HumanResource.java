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
  A human resource (role, expertise area) involved in development, deployment, operation, maintenance, or oversight of an AI system per A.4.6.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HumanResource extends NamedEntity {

  private List<String> requiredCompetencies;
  private List<String> assignedTo;
  private List<String> lifecycleResponsibilities;


}