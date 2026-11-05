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
  A class of financial data with its sensitivity and its handling, from docs/_data/data_classification.yml.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfDataClassification  {

  private String name;
  private String sensitivity;
  private String description;
  private List<String> examples;
  private String storageLocation;
  private String regulations;
  private List<AigfRegulatoryReference> references;


}