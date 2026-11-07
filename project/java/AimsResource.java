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
  A resource provided for the management system itself, such as people, time, tools or budget. What an AI system draws on is an AimsSystemResource.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsResource  {

  private String aimsSupportCategory;
  private String aimsSupportQuantity;
  private LocalDate aimsSupportAllocationDate;
  private String aimsSupportAllocatedTo;
  private String aimsSupportCost;
  private String aimsSupportAvailability;
  private URI aimsId;
  private String title;
  private String description;


}