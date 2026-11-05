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
  One entry of the Statement of Applicability, which either includes a control or leaves one out, and says why.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AimsApplicabilityEntry  {

  private String aimsEntryType;
  private String aimsEntryAnnexAControl;
  private List<AimsAiSystem> aimsAiSystems;
  private String aimsEntryJustification;


}