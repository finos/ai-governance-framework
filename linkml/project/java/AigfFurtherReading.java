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
  A paper or article a use case points to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfFurtherReading  {

  private String name;
  private String url;
  private String source;


}