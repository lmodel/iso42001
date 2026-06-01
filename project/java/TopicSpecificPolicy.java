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
  A topic-specific policy supporting the overarching AI policy, for example covering data governance, fairness, transparency, supplier use, or human oversight of AI systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TopicSpecificPolicy extends DocumentedInformation {

  private String topicArea;
  private AIPolicy parentPolicy;
  private List<AIReferenceControl> applicableControls;
  private String targetAudience;


}