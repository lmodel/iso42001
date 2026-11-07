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
  An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsCorrectiveAction  {

  private AimsRole aimsResponsibleRole;
  private List<AimsNonconformity> aimsActionNonconformities;
  private String aimsActionRootCause;
  private LocalDate aimsActionTargetDate;
  private LocalDate aimsActionCompletionDate;
  private String aimsActionResources;
  private String aimsActionEffectivenessCriteria;
  private LocalDate aimsActionEffectivenessReviewDate;
  private Boolean aimsActionEffective;
  private String aimsActionSystemChanges;
  private String aimsActionStatus;
  private URI aimsId;
  private String title;
  private String description;


}