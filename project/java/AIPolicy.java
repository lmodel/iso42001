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
  The AI policy established by top management per Clause 5.2. Provides a framework for setting AI objectives and demonstrates commitment to responsible AI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIPolicy extends DocumentedInformation {

  private String policyStatement;
  private String policyObjectivesFramework;
  private List<String> commitmentStatements;
  private String applicabilityStatement;
  private LocalDate communicationDate;
  private Boolean acknowledgmentRequired;
  private List<TopicSpecificPolicy> relatedTopicPolicies;
  private LocalDate lastPolicyReviewDate;
  private LocalDate nextPolicyReviewDate;


}