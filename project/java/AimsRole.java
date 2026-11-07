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
  A role in the system, with the duties and powers it carries and who holds it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRole  {

  private String aimsRoleCategory;
  private List<String> aimsRoleAreas;
  private List<String> aimsRoleResponsibilities;
  private List<String> aimsRoleAuthorities;
  private Boolean aimsRoleEnsuresConformity;
  private Boolean aimsRoleReportsPerformance;
  private String aimsRoleAccountability;
  private List<String> aimsRoleHolders;
  private String aimsRoleDelegation;
  private AimsRole aimsRoleReportsTo;
  private URI aimsId;
  private String title;
  private String description;


}