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
  A measurable AI objective per Clause 6.2, established at relevant functions and levels and aligned with the AI policy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIObjective extends NamedEntity {

  private String objectiveStatement;
  private String objectiveCategory;
  private String targetValue;
  private String currentValue;
  private String metricDefinition;
  private String measurementMethod;
  private String measurementFrequency;
  private Role responsibleRole;
  private String resourcesRequired;
  private LocalDate targetDate;
  private String achievementStatus;
  private List<AIRisk> relatedRisks;
  private List<AIReferenceControl> relatedControls;
  private String actionPlan;


}