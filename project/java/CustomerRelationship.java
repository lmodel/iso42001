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
  A customer relationship for an AI product or service supplied by the organization per A.10.4.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CustomerRelationship extends ThirdPartyRelationship {

  private List<String> customerExpectations;
  private String usageAgreementReference;
  private List<String> communicatedLimitations;


}