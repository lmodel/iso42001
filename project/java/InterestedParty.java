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
  A stakeholder whose needs and expectations are relevant to the AIMS per Clause 4.2. Includes internal and external parties such as users, regulators, partners, suppliers, customers, AI subjects, and relevant authorities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InterestedParty extends NamedEntity {

  private String partyType;
  private String relationship;
  private List<String> requirements;
  private String communicationNeeds;
  private String contactInformation;


}