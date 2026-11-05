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
  An opportunity to make the system more suitable, adequate or effective, and what came of it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsImprovementOpportunity  {

  private AimsRole aimsResponsibleRole;
  private String aimsImprovementSource;
  private LocalDate aimsImprovementIdentifiedOn;
  private String aimsImprovementIdentifiedBy;
  private String aimsImprovementBenefit;
  private String aimsImprovementPriority;
  private String aimsImprovementPlan;
  private LocalDate aimsImprovementTargetDate;
  private LocalDate aimsImprovementCompletionDate;
  private String aimsImprovementOutcome;
  private String aimsImprovementStatus;
  private URI aimsId;
  private String title;
  private String description;


}