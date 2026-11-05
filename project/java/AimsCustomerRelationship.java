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
  A relationship with a customer of the organization's AI work: what it expects, who answers for what, and which limits it was told of.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsCustomerRelationship extends AimsThirdPartyRelationship {

  private List<String> aimsCustomerExpectations;
  private String aimsCustomerAgreement;
  private String aimsCustomerResponsibilitySplit;
  private List<String> aimsCustomerCommunicatedLimits;


}