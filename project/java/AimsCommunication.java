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
  One communication the plan provides for: what about, to whom, when, how, and who communicates.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsCommunication  {

  private AimsRole aimsResponsibleRole;
  private String aimsCommunicationSubject;
  private String aimsCommunicationPurpose;
  private String aimsCommunicationAudience;
  private Boolean aimsCommunicationExternal;
  private String aimsCommunicationTiming;
  private String aimsCommunicationMethod;
  private Boolean aimsCommunicationRecordsRequired;


}