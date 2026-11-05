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
  An entry that includes a control the organization needs, from Annex A or from elsewhere, says which risks call for it and whether it is in place.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsIncludedControl extends AimsApplicabilityEntry {

  private String aimsImplementationState;
  private AimsRole aimsResponsibleRole;
  private AimsControl aimsIncludedControl;
  private List<AimsRisk> aimsIncludedRisks;
  private String aimsIncludedEvidence;
  private LocalDate aimsIncludedTargetDate;


}