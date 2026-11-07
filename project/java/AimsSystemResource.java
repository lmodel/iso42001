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
  Something an AI system draws on, told apart by its type, with the stages of the system's life that need it and who provides it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AimsSystemResource  {

  private String aimsResourceType;
  private List<String> aimsLifeCycleStages;
  private String aimsResourceProvider;
  private URI aimsId;
  private String title;
  private String description;


}