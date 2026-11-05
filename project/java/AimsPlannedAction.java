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
  An action planned on a risk or an opportunity the system faces, with how it fits the system's processes and how its effect will be judged.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsPlannedAction  {

  private AimsRole aimsResponsibleRole;
  private List<AimsAiSystem> aimsAiSystems;
  private List<AimsRisk> aimsPlannedActionRisks;
  private List<String> aimsPlannedActionOpportunities;
  private String aimsPlannedActionIntegration;
  private String aimsPlannedActionEffectiveness;
  private URI aimsId;
  private String title;
  private String description;


}