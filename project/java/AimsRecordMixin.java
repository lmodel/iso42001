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
  What every record of the system has, so that other records can refer to it: an identifier, a title and a description.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRecordMixin  {

  private URI aimsId;
  private String title;
  private String description;


}