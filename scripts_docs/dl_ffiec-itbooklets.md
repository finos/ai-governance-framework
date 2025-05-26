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

#### Features
- **Booklet abbreviations**: 3-letter codes for each booklet (aio, arc, aud, bcm, dam, mgt, ots, rps, sec, tsp, wps)
- **Hierarchical structure**: All booklets and their individual sections with generated keys
- **Navigation filtering**: Removes navigation elements from downloaded HTML for cleaner content
- **Markdown conversion**: Uses pandoc to convert HTML to GitHub-flavored Markdown
- **Flexible operation**: Can run individual steps or all steps together

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
```yaml
ffiec_itbooklet_abbreviations:
  architecture-infrastructure-and-operations: aio
  archived-booklets: arc
  audit: aud
  business-continuity-management: bcm
  development-acquisition-and-maintenance: dam
  information-security: sec
  management: mgt
  outsourcing-technology-services: ots
  retail-payment-systems: rps
  supervision-of-technology-service-providers: tsp
  wholesale-payment-systems: wps

ffiec_itbooklets:
  ffiec_sec:
    booklet_abbrev: sec
    title: "FFIEC SEC - Information Security"
    url: "https://ithandbook.ffiec.gov/it-booklets/information-security/"
  ffiec_sec_iii-security-operations:
    booklet_abbrev: sec
    title: "FFIEC SEC - III Security Operations"
    url: "https://ithandbook.ffiec.gov/it-booklets/information-security/iii-security-operations/"
  # ... other sections
```

#### Integration with Risk Files
The generated keys (e.g., `ffiec_sec_iii-security-operations`) are used in the `ffiec_references:` section of risk files (`docs/_risks/ri-*.md`) to map AI governance risks to specific FFIEC requirements.

