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
  A part of a system, and how it is joined to the rest.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsComponentResource extends AimsSystemResource {

  private String aimsComponentKind;
  private String aimsComponentIntegration;


}