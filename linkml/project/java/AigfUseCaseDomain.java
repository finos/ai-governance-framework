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
  A top level of the use case taxonomy in docs/_data/ai_use_cases.yml.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfUseCaseDomain  {

  private String name;
  private List<AigfUseCaseArea> useCaseAreas;


}