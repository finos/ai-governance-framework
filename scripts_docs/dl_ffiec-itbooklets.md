# FFIEC IT Handbook Info

## Revisions

Be sure you're referring to the latest edition of any given booklet.

Random copies from web searches may go back to 2004.  Check the Archived Booklets page to see if the booklet of interest has received an update:
- https://ithandbook.ffiec.gov/it-booklets/archived-booklets/

Using the "Multiple" download option for PDFs will retrieve the latest:
- https://ithandbook.ffiec.gov/it-booklets

However, that page also links to "Online" HTML versions which are more convenient for deep linking.

## FFIEC IT Booklets Manager

This project includes a comprehensive script to manage FFIEC IT Handbook booklets by generating YAML mappings, downloading HTML files, and converting them to Markdown.

### Script: `scripts/dl_ffiec-itbooklets.py`

This Python script can perform three main operations:

1. **Generate YAML file** with booklet structure and URLs
2. **Download HTML files** with navigation filtering for cleaner content  
3. **Convert HTML files to Markdown** using pandoc

#### Key Features
- **Configuration-driven**: Reads booklet abbreviations from `docs/_config.yml`
- **Automatic key generation**: Creates unique keys for all booklets and sections
- **Navigation filtering**: Removes navigation elements from downloaded HTML for cleaner content
- **Markdown conversion**: Uses pandoc to convert HTML to GitHub-flavored Markdown
- **Flexible operation**: Can run individual steps or all steps together
- **Rate limiting**: Built-in delays to be respectful to the FFIEC server

#### Booklet Abbreviations
The script uses 3-letter abbreviations defined in `docs/_config.yml`:
- **aio** - Architecture, Infrastructure, and Operations
- **arc** - Archived Booklets  
- **aud** - Audit
- **bcm** - Business Continuity Management
- **dam** - Development, Acquisition, and Maintenance
- **mgt** - Management
- **ots** - Outsourcing Technology Services
- **rps** - Retail Payment Systems
- **sec** - Information Security
- **tsp** - Supervision of Technology Service Providers
- **wps** - Wholesale Payment Systems

#### Output Files
- `docs/_data/ffiec-itbooklets.yml` (YAML mappings)
- `_refs-markdown/ffiec-itbooklets/html/*.html` (HTML files with navigation removed)
- `_refs-markdown/ffiec-itbooklets/markdown/*.md` (Markdown files)

#### Dependencies
```bash
# Python dependencies
pip install requests beautifulsoup4 pyyaml

# For Markdown conversion (optional)
conda install -c conda-forge pandoc
```

#### Usage
```bash
# Generate YAML only
python scripts/dl_ffiec-itbooklets.py --yml

# Download HTML only  
python scripts/dl_ffiec-itbooklets.py --html

# Convert to Markdown only (requires pandoc)
python scripts/dl_ffiec-itbooklets.py --md

# Do all steps
python scripts/dl_ffiec-itbooklets.py --all
python scripts/dl_ffiec-itbooklets.py  # default behavior
```

#### Generated YAML Structure
The current script generates a flat YAML structure with booklet entries:

```yaml
# FFIEC IT Booklets
# Generated from https://ithandbook.ffiec.gov/it-booklets

ffiec_aud:
  booklet_abbrev: aud
  title: 'AUD: Audit'
  url: https://ithandbook.ffiec.gov/it-booklets/audit/
ffiec_aud_introduction:
  booklet_abbrev: aud
  title: 'AUD: Introduction'
  url: https://ithandbook.ffiec.gov/it-booklets/audit/introduction/
ffiec_aud_it-audit-roles-and-responsibilities:
  booklet_abbrev: aud
  title: 'AUD: IT Audit Roles and Responsibilities'
  url: https://ithandbook.ffiec.gov/it-booklets/audit/it-audit-roles-and-responsibilities/
# ... more sections
```

**Note**: The booklet abbreviations are stored in `docs/_config.yml`, not in the generated YAML file.

#### Key Generation Logic
The script automatically generates keys for:
- **Main booklets**: `ffiec_{abbrev}` (e.g., `ffiec_aud`)
- **Introduction sections**: `ffiec_{abbrev}_introduction`
- **Named sections**: `ffiec_{abbrev}_{section-slug}` (derived from URL)
- **Appendices**: `ffiec_{abbrev}_appendix-{letter}-{title-slug}`

#### Integration with Risk Files
The generated keys are used in the `ffiec-itbooklets_references:` section of risk files (`docs/_risks/ri-*.md`) to map AI governance risks to specific FFIEC requirements.

