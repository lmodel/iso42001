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
  A data resource used by an AI system per Annex A.7. Includes data acquisition, quality, provenance, and preparation metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataResource extends NamedEntity {

  private String dataResourceCategory;
  private String source;
  private String acquisitionMethod;
  private List<String> dataQualityRequirements;
  private List<String> dataQualityMetrics;
  private String dataProvenance;
  private String labellingProcess;
  private List<String> dataPreparationMethods;
  private LocalDate lastUpdatedDate;
  private List<String> knownBiasIssues;
  private String retentionPolicy;
  private String dataClassification;


}