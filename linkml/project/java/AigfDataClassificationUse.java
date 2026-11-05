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
  A data classification a use case handles, with the kinds of data it holds under it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfDataClassificationUse  {

  private String name;
  private List<String> dataTypes;


}