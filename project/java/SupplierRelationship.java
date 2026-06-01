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
  A supplier relationship covering services, products, or materials (e.g., datasets, models, libraries, full AI systems) provided to the organization per A.10.3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SupplierRelationship extends ThirdPartyRelationship {

  private List<String> supplierAssessmentCriteria;
  private String monitoringMethod;
  private List<String> correctiveActionsRequired;


}