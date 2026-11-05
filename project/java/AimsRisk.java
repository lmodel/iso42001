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
  An AI risk in the risk register: where it comes from, which objectives it helps or hinders, who could feel its consequences, how it is rated and how it is treated.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsRisk  {

  private List<AimsAiSystem> aimsAiSystems;
  private List<String> aimsRiskSourceCategories;
  private String aimsRiskSource;
  private List<AimsObjective> aimsRiskObjectives;
  private String aimsRiskConsequencesForOrganization;
  private String aimsRiskConsequencesForIndividuals;
  private String aimsRiskConsequencesForSocieties;
  private String aimsRiskOwner;
  private String aimsRiskLikelihood;
  private String aimsRiskConsequence;
  private String aimsRiskInherentLevel;
  private List<AimsControl> aimsRiskExistingControls;
  private String aimsRiskResidualLevel;
  private Boolean aimsRiskAcceptable;
  private String aimsRiskTreatmentOption;
  private String aimsRiskTreatmentPriority;
  private List<AimsImpactAssessment> aimsRiskImpactAssessments;
  private URI aimsId;
  private String title;
  private String description;


}