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
  A resource provided for the AIMS per Clause 7.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Resource extends NamedEntity {

  private String resourceType;
  private String quantity;
  private LocalDate allocationDate;
  private String allocatedTo;
  private String cost;
  private String availabilityStatus;


}