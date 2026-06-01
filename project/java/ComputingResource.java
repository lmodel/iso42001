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
  A system or computing resource used in the development or operation of an AI system per A.4.5.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComputingResource extends NamedEntity {

  private String resourceClass;
  private String quantity;
  private String location;
  private String environmentType;
  private String cost;


}