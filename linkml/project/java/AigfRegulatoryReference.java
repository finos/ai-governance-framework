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
  A regulation or guideline named by its title and address, with where it applies.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfRegulatoryReference  {

  private String name;
  private String url;
  private String jurisdiction;


}