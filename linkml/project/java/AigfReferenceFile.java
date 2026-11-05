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
  One file under docs/_data/references/, which lists the citable entries of one regulation, framework or standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfReferenceFile  {

  private String title;
  private String description;
  private String sourceUrl;
  private String lens;
  private List<AigfReferenceEntry> entries;


}