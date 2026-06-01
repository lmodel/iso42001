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
  A concern raised by employees, contractors, users, or other interested parties about the organization's role with respect to an AI system. Operationalises Annex A.3.3 (Reporting of concerns). Confidentiality, anonymity, anti-reprisal protection, escalation, and timely response are core attributes; informed by ISO 37002.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConcernReport extends NamedEntity {

  private LocalDate reportedDate;
  private String reporter;
  private String reporterPartyType;
  private Boolean reporterAnonymous;
  private String confidentialityLevel;
  private String reportingChannel;
  private String concernDescription;
  private List<AISystem> concernAiSystems;
  private List<String> concernLifecycleStage;
  private String severity;
  private String investigator;
  private String investigationStatus;
  private String investigationFindings;
  private String escalationStatus;
  private LocalDate responseDueDate;
  private LocalDate responseProvidedDate;
  private String resolution;
  private List<String> reprisalProtectionActions;
  private List<AIIncident> relatedIncidents;
  private List<Nonconformity> relatedNonconformities;
  private ZonedDateTime closureDatetime;


}