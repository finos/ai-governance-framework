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
  One option on an axis of the deployment model taxonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfDeploymentOption  {

  private String name;
  private String description;


}