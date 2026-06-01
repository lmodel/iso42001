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
  A tooling resource (algorithm, framework, model, library) used in an AI system per A.4.4.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ToolingResource extends NamedEntity {

  private String toolCategory;
  private String toolVersion;
  private String vendor;
  private String licenseTerms;
  private String usagePurpose;


}