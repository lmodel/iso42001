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
  One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsAuditFinding  {

  private List<String> aimsCitedClauses;
  private List<String> aimsCitedAnnexAControls;
  private String aimsFindingType;
  private AimsControl aimsFindingControl;
  private String aimsFindingEvidence;
  private String aimsFindingRootCause;
  private String aimsFindingRisk;
  private String aimsFindingRecommendation;
  private String aimsFindingAuditeeResponse;
  private AimsCorrectiveAction aimsFindingCorrectiveAction;
  private AimsNonconformity aimsFindingNonconformity;
  private String aimsFindingClosureStatus;
  private LocalDate aimsFindingClosureDate;
  private URI aimsId;
  private String title;
  private String description;


}