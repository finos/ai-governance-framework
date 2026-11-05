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
  One edition of the framework, as the facts FINOS's front matter and data files state.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AigfCatalogue  {

  private String title;
  private String version;
  private LocalDate releaseDate;
  private String sourceCommit;
  private List<AigfReferenceLens> referenceLenses;
  private List<AigfReferenceIndex> referenceIndexes;
  private List<AigfRisk> risks;
  private List<AigfMitigation> mitigations;
  private List<AigfUseCase> useCases;
  private List<AigfDataClassification> financialDataClassification;
  private List<AigfUseCaseDomain> aiUseCases;
  private List<String> crossCuttingCapabilities;
  private List<AigfDeploymentAxis> aiDeploymentModelTaxonomy;


}