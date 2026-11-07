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
  Data an AI system draws on: where it came from, what part it plays, how it was obtained, made ready and judged fit, and how long it is kept.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsDataResource extends AimsSystemResource {

  private List<String> aimsDataCategories;
  private List<String> aimsDataKinds;
  private String aimsDataIntendedUse;
  private String aimsDataQuantity;
  private List<String> aimsDataSources;
  private List<String> aimsDataSourceCharacteristics;
  private List<String> aimsDataSubjectDemographics;
  private String aimsDataPriorHandling;
  private List<String> aimsDataRights;
  private List<String> aimsDataMetadata;
  private String aimsDataProvenance;
  private String aimsDataProvenanceVerification;
  private List<String> aimsDataQualityRequirements;
  private List<String> aimsDataQualityResults;
  private List<String> aimsDataBiasIssues;
  private String aimsDataRepresentativeness;
  private String aimsDataLabellingProcess;
  private String aimsDataPreparationCriteria;
  private List<String> aimsDataPreparationMethods;
  private LocalDate aimsDataLastUpdated;
  private String aimsDataRetention;
  private String aimsDataClassification;


}