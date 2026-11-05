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
  A tool an AI system draws on, such as an algorithm, a model or a development tool.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsToolingResource extends AimsSystemResource {

  private String aimsToolCategory;
  private String aimsToolVersion;
  private String aimsToolVendor;
  private String aimsToolLicence;
  private String aimsToolPurpose;


}