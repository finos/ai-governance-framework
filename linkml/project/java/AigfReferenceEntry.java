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
  One citable item of a reference file, under the key a page cites it by.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfReferenceEntry  {

  private String referenceKey;
  private String title;
  private String url;
  private String description;
  private String issuer;
  private String bookletAbbrev;
  private String supersededBy;


}