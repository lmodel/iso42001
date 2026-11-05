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
  A person or organization whose needs and expectations bear on the system, or who may feel its decisions, inside the organization or outside it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsInterestedParty  {

  private String aimsPartyCategory;
  private List<String> aimsPartyAiRoles;
  private String aimsPartyRelationship;
  private List<String> aimsPartyRequirements;
  private List<String> aimsPartyAddressedRequirements;
  private List<String> aimsPartyClimateChangeRequirements;
  private String aimsPartyCommunicationNeeds;
  private String aimsPartyContact;
  private URI aimsId;
  private String title;
  private String description;


}