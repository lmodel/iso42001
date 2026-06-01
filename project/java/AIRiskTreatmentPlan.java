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
  A plan documenting planned actions to address identified AI risks through selected controls. Requires approval by designated management per Clause 6.1.3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIRiskTreatmentPlan extends DocumentedInformation {

  private String planScope;
  private List<AIRisk> risksAddressed;
  private List<String> treatmentActions;
  private List<AIReferenceControl> controlsToImplement;
  private String resourcesRequired;
  private List<String> responsibleParties;
  private String implementationTimeline;
  private String riskOwnerApproval;
  private String residualRiskAcceptance;
  private String implementationStatus;
  private LocalDate completionDate;


}