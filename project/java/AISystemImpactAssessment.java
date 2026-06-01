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
  An instance of an AI system impact assessment performed per Clause 6.1.4 and Clause 8.4. Documents consequences of deployment, intended use, and foreseeable misuse on individuals, groups, and societies.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AISystemImpactAssessment extends DocumentedInformation {

  private String assessmentScope;
  private List<AISystem> aiSystemsAssessed;
  private LocalDate assessmentDate;
  private String assessor;
  private String technicalContext;
  private String societalContext;
  private List<String> applicableJurisdictions;
  private List<String> dimensionsAssessed;
  private List<String> identifiedConsequences;
  private List<String> mitigations;
  private List<String> sharedWithParties;
  private LocalDate nextAssessmentDate;


}