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
  A reference control from Annex A of ISO/IEC 42001:2023. Controls are grouped into nine families (A.2 through A.10) and supported by implementation guidance in Annex B.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIReferenceControl extends NamedEntity {

  private String controlId;
  private String controlTitle;
  private String controlFamily;
  private String controlText;
  private String implementationGuidance;
  private List<AIReferenceControl> relatedControls;
  private List<String> applicableRiskSources;
  private List<String> applicableObjectives;
  private String controlOwner;
  private String implementationStatus;
  private LocalDate implementationDate;
  private String effectivenessRating;
  private LocalDate lastTestDate;
  private List<String> evidenceReferences;


}