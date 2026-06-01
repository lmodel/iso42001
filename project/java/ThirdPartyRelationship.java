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
  A documented relationship with a third party (supplier, partner, or customer) involved in the AI system life cycle per A.10.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThirdPartyRelationship extends NamedEntity {

  private String partyType;
  private String partyName;
  private String contractualBasis;
  private List<String> allocatedResponsibilities;
  private String dataProcessingRole;
  private List<AISystem> aiSystemsInvolved;
  private List<String> lifecycleStagesInvolved;
  private List<String> assuranceEvidence;
  private String reviewFrequency;


}