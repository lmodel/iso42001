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
  An AI system within the AIMS scope. Captures life cycle stage, intended use, applicable domains, and references to data and tooling resources, technical documentation, and impact assessments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AISystem extends NamedEntity {

  private String aiSystemPurpose;
  private List<String> intendedUses;
  private List<String> foreseeableMisuse;
  private String applicationDomain;
  private String deploymentContext;
  private String lifecycleStage;
  private String organizationRole;
  private String autonomyLevel;
  private String mlApproach;
  private Boolean humanOversightRequired;
  private String humanOversightDescription;
  private List<String> humanOversightStages;
  private String learningMode;
  private List<DataResource> dataResources;
  private List<ToolingResource> toolingResources;
  private List<ComputingResource> computingResources;
  private List<HumanResource> humanResources;
  private List<String> technicalDocumentation;
  private String eventLogPolicy;
  private List<AIReferenceControl> applicableControls;
  private List<AISystemImpactAssessment> relatedImpactAssessments;
  private List<SupplierRelationship> supplierRelationships;
  private List<CustomerRelationship> customerRelationships;


}