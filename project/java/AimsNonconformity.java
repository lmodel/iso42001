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
  A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsNonconformity  {

  private List<String> aimsCitedClauses;
  private List<String> aimsCitedAnnexAControls;
  private String aimsNonconformitySource;
  private LocalDate aimsNonconformityDetectedOn;
  private String aimsNonconformityDetectedBy;
  private String aimsNonconformityRequirement;
  private List<String> aimsNonconformityImmediateActions;
  private String aimsNonconformityConsequences;
  private String aimsNonconformityRootCause;
  private String aimsNonconformitySimilarCheck;
  private String aimsNonconformityStatus;
  private LocalDate aimsNonconformityClosureDate;
  private String aimsNonconformityClosureEvidence;
  private URI aimsId;
  private String title;
  private String description;


}