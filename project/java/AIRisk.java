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
  An identified AI risk that may affect achievement of AI objectives, individuals, groups, or societies within the AIMS scope.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIRisk extends NamedEntity {

  private String riskSourceCategory;
  private String riskSourceDescription;
  private List<AISystem> affectedAiSystems;
  private List<String> affectedDimensions;
  private String riskOwner;
  private String likelihood;
  private String impact;
  private String inherentRiskLevel;
  private List<AIReferenceControl> existingControls;
  private String residualRiskLevel;
  private String riskTreatmentOption;
  private String treatmentPriority;
  private AIRiskTreatmentPlan relatedTreatmentPlan;
  private AISystemImpactAssessment relatedImpactAssessment;


}