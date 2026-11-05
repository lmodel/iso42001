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
  Hardware or computing an AI system draws on: what it needs, where it runs and what the hardware costs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsComputingResource extends AimsSystemResource {

  private String aimsComputingRequirements;
  private String aimsComputingLocation;
  private String aimsComputingProcessing;
  private String aimsComputingHardwareImpact;


}