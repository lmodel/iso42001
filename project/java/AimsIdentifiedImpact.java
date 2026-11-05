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
  One impact an assessment found: on whom it falls, in what area, whether it helps or harms, and what limits the harm.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsIdentifiedImpact  {

  private String aimsIdentifiedImpactSubject;
  private String aimsIdentifiedImpactArea;
  private String aimsIdentifiedImpactDirection;
  private String aimsIdentifiedImpactText;
  private List<String> aimsIdentifiedImpactMitigation;


}