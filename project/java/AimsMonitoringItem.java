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
  One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AimsMonitoringItem  {

  private AimsRole aimsResponsibleRole;
  private String aimsMonitoringMetric;
  private String aimsMonitoringDescription;
  private String aimsMonitoringMethod;
  private String aimsMonitoringFrequency;
  private String aimsMonitoringAnalysisFrequency;
  private String aimsMonitoringAnalyst;
  private String aimsMonitoringTarget;
  private String aimsMonitoringAlertThreshold;
  private String aimsMonitoringCurrentValue;
  private String aimsMonitoringTrend;


}