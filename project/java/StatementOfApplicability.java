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
  The Statement of Applicability (SoA) for the AIMS recording which Annex A controls apply, justification for inclusion or exclusion, and current implementation state per Clause 6.1.3 f).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatementOfApplicability extends DocumentedInformation {

  private List<SoAEntry> soaEntries;
  private String totalControls;
  private String implementedCount;
  private String plannedCount;
  private String notApplicableCount;
  private LocalDate lastReviewDate;


}