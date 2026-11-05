package example;

/* metamodel_version: 1.12.0 */
/* version: v3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A mitigation the framework names, from a file under docs/_mitigations/.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfMitigation extends AigfItem {

  private String mitigationType;
  private String mitigationDomain;
  private List<AigfRisk> mitigates;
  private List<AigfMitigation> relatedMitigations;
  private List<String> atrReferences;
  private List<String> canadaRegulationsReferences;
  private List<String> euAiActReferences;
  private List<String> ffiecItbookletsReferences;
  private List<String> ioscoSupervisoryToolkitReferences;
  private List<String> iso42001References;
  private List<String> nistAi6001References;
  private List<String> nistSp80053r5References;
  private List<String> owaspAsiReferences;
  private List<String> owaspLlmReferences;
  private List<String> owaspMlReferences;
  private List<String> sr117References;
  private List<String> ukRegulationsReferences;


}