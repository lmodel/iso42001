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
  A relationship with another party in an AI system's life, such as a partner: who carries which duty, and what assures the organization of that.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsThirdPartyRelationship  {

  private List<AimsAiSystem> aimsAiSystems;
  private List<String> aimsLifeCycleStages;
  private String aimsRelationshipType;
  private String aimsRelationshipParty;
  private List<String> aimsRelationshipPartyRoles;
  private String aimsRelationshipContract;
  private List<String> aimsRelationshipResponsibilities;
  private String aimsRelationshipPiiRole;
  private List<String> aimsRelationshipDocumentation;
  private List<String> aimsRelationshipAssuranceEvidence;
  private String aimsRelationshipReviewFrequency;
  private URI aimsId;
  private String title;
  private String description;


}