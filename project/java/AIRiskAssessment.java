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
  An instance of AI risk assessment performed per Clause 8.2, identifying and evaluating AI risks at planned intervals or following significant change.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIRiskAssessment extends DocumentedInformation {

  private String assessmentScope;
  private List<AISystem> aiSystemsAssessed;
  private LocalDate assessmentDate;
  private String assessor;
  private String methodologyUsed;
  private List<AIRisk> risksIdentified;
  private AISystemImpactAssessment linkedImpactAssessment;
  private String summaryFindings;
  private List<String> recommendations;
  private LocalDate nextAssessmentDate;


}