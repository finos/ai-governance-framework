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
  The keys one reference file holds, so that a catalogue's citations resolve within it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfReferenceIndex  {

  private String referenceFile;
  private String lens;
  private List<String> entryKeys;


}