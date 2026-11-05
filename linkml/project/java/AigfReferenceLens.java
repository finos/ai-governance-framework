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
  How the site presents the reference files of one lens, from reference_lenses in docs/_config.yml.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfReferenceLens  {

  private String lens;
  private String label;
  private String question;
  private String icon;
  private String color;


}