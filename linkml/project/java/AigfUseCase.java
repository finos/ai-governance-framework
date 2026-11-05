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
  A worked use case with its risks, mitigations and data, from a file under docs/_usecases/.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfUseCase extends AigfItem {

  private String category;
  private String description;
  private String endUser;
  private String businessValue;
  private List<AigfRisk> relatedRisks;
  private List<AigfMitigation> relatedMitigations;
  private List<AigfDataClassificationUse> dataClassifications;
  private List<String> dataHandlingAspects;
  private List<AigfRegulatoryReference> regulatoryConcerns;
  private List<AigfFurtherReading> furtherReading;
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