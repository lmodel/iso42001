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
  A relationship with a supplier to the organization's AI work: what it provides, the risk that brings, and how it is held to the organization's approach.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsSupplierRelationship extends AimsThirdPartyRelationship {

  private List<String> aimsSupplierProvides;
  private String aimsSupplierRisk;
  private List<String> aimsSupplierRequirements;
  private String aimsSupplierMonitoring;
  private String aimsSupplierIntegration;
  private List<String> aimsSupplierCorrectiveActions;


}