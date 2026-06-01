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
  The documented AI risk treatment process per Clause 6.1.3, defining how treatment options are selected, how Annex A controls are considered, and how the Statement of Applicability is produced.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIRiskTreatmentProcess extends DocumentedInformation {

  private String treatmentOptionsGuidance;
  private String controlSelectionCriteria;
  private String soaTemplate;
  private String approvalWorkflow;


}