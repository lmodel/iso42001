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
  Something the organization must report about a system to an interested party: to whom, under what rule, what and how soon.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsReportingObligation  {

  private List<AimsAiSystem> aimsAiSystems;
  private List<AimsInterestedParty> aimsObligationParties;
  private String aimsObligationBasis;
  private String aimsObligationJurisdiction;
  private List<String> aimsObligationContents;
  private String aimsObligationTimeframe;
  private URI aimsId;
  private String title;
  private String description;


}