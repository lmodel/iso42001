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
  An AI objective: a result the organization aims for, with how it plans to reach it and how it judges progress.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsObjective  {

  private AimsRole aimsResponsibleRole;
  private List<AimsControl> aimsRelevantControls;
  private List<String> aimsObjectiveCategories;
  private String aimsObjectivePurpose;
  private String aimsObjectiveStatement;
  private String aimsObjectiveTarget;
  private String aimsObjectiveCurrentValue;
  private String aimsObjectiveMetric;
  private String aimsObjectiveMeasurementMethod;
  private String aimsObjectiveMeasurementFrequency;
  private LocalDate aimsObjectiveTargetDate;
  private String aimsObjectiveAchievement;
  private List<AimsRisk> aimsObjectiveRisks;
  private String aimsObjectiveActionPlan;
  private String aimsObjectiveResources;
  private String aimsObjectiveEvaluation;
  private String aimsObjectiveCommunication;
  private URI aimsId;
  private String title;
  private String description;


}