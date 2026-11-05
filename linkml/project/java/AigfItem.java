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
  A page of the framework that its front matter describes and that others cite by identifier.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AigfItem  {

  private String itemId;
  private int sequence;
  private String title;
  private String layout;
  private String docStatus;
  private String sourceFile;


}