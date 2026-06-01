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
  The documented process for assessing the potential consequences for individuals, groups, and societies arising from the development, provision, or use of AI systems per Clause 6.1.4.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AISystemImpactAssessmentProcess extends DocumentedInformation {

  private String assessmentCriteria;
  private String assessmentMethodology;
  private List<String> dimensionsInScope;
  private String assessmentFrequency;
  private List<String> triggerEvents;
  private String linkageToRiskAssessment;


}