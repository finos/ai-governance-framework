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
  One axis of the deployment model taxonomy in docs/_data/ai_deployment_model.yml.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfDeploymentAxis  {

  private String name;
  private List<AigfDeploymentOption> options;


}