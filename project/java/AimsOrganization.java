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
  The organization that runs the system, with what it needs to know about itself to understand its context and the parts it plays with AI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsOrganization  {

  private String aimsOrganizationLegalName;
  private List<String> aimsOrganizationTradingNames;
  private String aimsOrganizationKind;
  private List<String> aimsOrganizationSectors;
  private String aimsOrganizationSize;
  private Integer aimsOrganizationEmployeeCount;
  private List<String> aimsOrganizationLocations;
  private List<String> aimsOrganizationJurisdictions;
  private String aimsOrganizationParent;
  private List<String> aimsOrganizationSubsidiaries;
  private List<String> aimsOrganizationAiRoles;
  private List<String> aimsOrganizationPiiRoles;
  private Boolean aimsOrganizationClimateChangeRelevant;
  private URI aimsId;
  private String title;
  private String description;


}