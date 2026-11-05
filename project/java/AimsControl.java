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
  A control the organization has found it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsControl  {

  private List<AimsControl> aimsRelevantControls;
  private String aimsImplementationState;
  private List<String> aimsCitedAnnexAControls;
  private List<AimsAiSystem> aimsAiSystems;
  private List<String> aimsObjectiveCategories;
  private List<String> aimsRiskSourceCategories;
  private String aimsControlArea;
  private String aimsControlText;
  private String aimsControlGuidance;
  private String aimsControlOwner;
  private LocalDate aimsControlImplementationDate;
  private String aimsControlEffectiveness;
  private LocalDate aimsControlLastTested;
  private List<String> aimsControlEvidence;
  private URI aimsId;
  private String title;
  private String description;


}