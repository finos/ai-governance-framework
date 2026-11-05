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
  A second level of the use case taxonomy, with the use cases under it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfUseCaseArea  {

  private String name;
  private List<String> useCaseNames;


}