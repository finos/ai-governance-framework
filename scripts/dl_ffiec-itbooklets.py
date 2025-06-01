#!/usr/bin/env python3
"""
FFIEC IT Booklets Manager

This script manages FFIEC IT Handbook booklets by generating YAML mappings,
downloading HTML files with navigation filtering, and converting them to Markdown using pandoc.

The script can perform three main operations:
1. Generate YAML file with booklet structure and URLs
2. Download all booklet URLs as HTML files (filtering out navigation elements)
3. Convert HTML files to Markdown using pandoc

Operations can be run individually or in combination using command line flags.

Input: https://ithandbook.ffiec.gov/it-booklets
Output: 
    - _data/ffiec-itbooklets.yml (YAML mappings)
    - _refs-markdown/ffiec-itbooklets/html/*.html (HTML files with navigation removed)
    - _refs-markdown/ffiec-itbooklets/markdown/*.md (Markdown files)

Usage:
    python scripts/dl_ffiec-booklets.py --yml          # Generate YAML only
    python scripts/dl_ffiec-booklets.py --html         # Download HTML only
    python scripts/dl_ffiec-booklets.py --md           # Convert to Markdown only
    python scripts/dl_ffiec-booklets.py --all          # Do all steps
    python scripts/dl_ffiec-booklets.py                # Do all steps (default)

Dependencies: 
    - pip install requests beautifulsoup4 pyyaml
    - conda install -c conda-forge pandoc (for Markdown conversion)
"""

import requests
from bs4 import BeautifulSoup
import yaml
import sys
import os
import time
import subprocess
import argparse
import roman
import re
from pathlib import Path
from urllib.parse import urljoin

# Constants
SCRIPT_DIR = Path(__file__).parent

BASE_URL = "https://ithandbook.ffiec.gov"
BOOKLETS_URL = f"{BASE_URL}/it-booklets"
YAML_FILENAME = "ffiec-itbooklets_v2.yml"
REQUEST_TIMEOUT = 30
DOWNLOAD_DELAY = 0.5
URL_COMPONENTS_MAIN_BOOKLET = 5
URL_COMPONENTS_SECTION = 6

# Path constants
DATA_DIR = SCRIPT_DIR / ".." / "docs" / "_data"
CONFIG_DIR = SCRIPT_DIR / ".." / "docs"
FFIEC_ITBOOKLETS_DIR = SCRIPT_DIR / ".." / "_refs-markdown" / "ffiec-itbooklets"
YAML_FILE = DATA_DIR / YAML_FILENAME
CONFIG_FILE = CONFIG_DIR / "_config.yml"
HTML_OUTPUT_DIR = FFIEC_ITBOOKLETS_DIR / "html"
MD_OUTPUT_DIR = FFIEC_ITBOOKLETS_DIR / "markdown"



def read_config_file(config_file):
    """Read and parse Jekyll config file to get abbreviations mapping."""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
            return config_data.get('ffiec_itbooklet_abbreviations', {})
    except FileNotFoundError:
        print(f"Error: Config file not found: {config_file}", file=sys.stderr)
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}", file=sys.stderr)
        return {}

def write_yaml_file(yaml_file, booklets):
    """Write booklets data to YAML file."""
    try:
        with open(yaml_file, 'w', encoding='utf-8') as f:
            f.write("# FFIEC IT Booklets\n")
            f.write(f"# Generated from {BOOKLETS_URL}\n\n")
            yaml.dump(booklets, f, 
                     default_flow_style=False, sort_keys=False)
        return True
    except (OSError, yaml.YAMLError) as e:
        print(f"Error writing YAML file: {e}", file=sys.stderr)
        return False

def read_yaml_file(yaml_file):
    """Read and parse YAML file, returning the data or None on error."""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: YAML file not found: {yaml_file}", file=sys.stderr)
        print("Run with --yml flag first to generate the YAML file.", file=sys.stderr)
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}", file=sys.stderr)
        return None

def parse_booklet_url(full_url, abbreviations):
    """Parse booklet URL to extract key and abbreviation.
    
    Args:
        full_url: Full URL to parse
        abbreviations: Dictionary mapping full booklet names to abbreviations
    
    Returns:
        tuple: (key, booklet_abbrev) or (None, None) if parsing fails
    """
    components = full_url.rstrip('/').split('/')
    component_count = len(components)
    
    if component_count < URL_COMPONENTS_MAIN_BOOKLET:
        return None, None
        
    booklet = components[4]
    booklet_abbrev = abbreviations.get(booklet)
    
    if not booklet_abbrev:
        return None, None
    
    if component_count == URL_COMPONENTS_MAIN_BOOKLET:
        # Main booklet page
        key = f"ffiec_{booklet_abbrev}"
    elif component_count == URL_COMPONENTS_SECTION:
        # Section page
        section = components[5]
        key = f"ffiec_{booklet_abbrev}_{section}"
    else:
        # Unexpected URL structure
        return None, None
        
    return key, booklet_abbrev

def parse_title_for_short_key(title, booklet_abbrev):
    """
    Parse a title to extract section identifier for short key generation.
    
    Args:
        title: Full title like "AUD: IT Audit Roles and Responsibilities"
        booklet_abbrev: Booklet abbreviation like "aud"
        
    Returns:
        tuple: (section_type, identifier) where:
            - section_type: 'main', 'intro', 'numbered', 'appendix'
            - identifier: extracted number/letter or None for sequential assignment
    """
    # Remove booklet prefix (e.g., "AUD: " or "DAM: ")
    clean_title = re.sub(rf'^{booklet_abbrev.upper()}:\s*', '', title, flags=re.IGNORECASE)
    
    # Check for introduction
    if 'introduction' in clean_title.lower():
        return 'intro', None
        
    # Check for appendix (e.g., "Appendix A: Something")
    appendix_match = re.match(r'^appendix\s+([a-z])\s*:', clean_title, flags=re.IGNORECASE)
    if appendix_match:
        return 'appendix', appendix_match.group(1).lower()
    
    # Check for roman numerals at start (e.g., "I Overview", "II Governance")
    roman_match = re.match(r'^([ivx]+)\s+', clean_title, flags=re.IGNORECASE)
    if roman_match:
        try:
            roman_num = roman_match.group(1).upper()
            section_num = roman.fromRoman(roman_num)
            return 'numbered', section_num
        except roman.InvalidRomanNumeralError:
            pass
    
    # No explicit numbering found - needs sequential assignment
    return 'numbered', None

def generate_short_key(booklet_abbrev, section_type, identifier, sequential_num=None):
    """
    Generate short key based on parsing results.
    
    Args:
        booklet_abbrev: 3-letter code like "aud"
        section_type: 'main', 'intro', 'numbered', 'appendix'
        identifier: extracted identifier or None
        sequential_num: assigned sequential number if identifier is None
        
    Returns:
        str: Short key like "aud-1", "dam-i", "aud-a"
    """
    if section_type == 'main':
        return booklet_abbrev
    elif section_type == 'intro':
        return f"{booklet_abbrev}-0"
    elif section_type == 'appendix':
        return f"{booklet_abbrev}-{identifier}"
    elif section_type == 'numbered':
        if identifier is not None:
            return f"{booklet_abbrev}-{identifier}"
        elif sequential_num is not None:
            return f"{booklet_abbrev}-{sequential_num}"
        else:
            raise ValueError("Need either identifier or sequential_num for numbered section")
    else:
        raise ValueError(f"Unknown section_type: {section_type}")

def create_booklet_entry(key, booklet_abbrev, title, url):
    """Create a booklet dictionary entry."""
    return {
        'booklet_abbrev': booklet_abbrev,
        'title': f"{booklet_abbrev.upper()}: {title}",
        'url': url
    }

def check_pandoc():
    """Check if pandoc is available on the system."""
    try:
        subprocess.run(['pandoc', '--version'], 
                      capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_html_to_markdown(html_path, md_path):
    """Convert HTML file to Markdown using pandoc."""
    try:
        # Use cleaner pandoc options for better markdown output
        pandoc_args = [
            'pandoc', str(html_path), '-o', str(md_path),
            '--from=html',
            '--to=gfm-raw_html',     # GitHub markdown without raw HTML passthrough
            '--wrap=auto',           # Auto-wrap long lines
            '--strip-comments',      # Remove HTML comments
        ]
        subprocess.run(pandoc_args, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Pandoc conversion error: {e}")
        return False

def generate_yaml_file(yaml_file):
    """Generate the YAML file with FFIEC booklet structure and URLs."""
    
    print("=== Generating YAML file ===")
    
    # Read abbreviations from config file
    print(f"Reading abbreviations from config file: {CONFIG_FILE}")
    abbreviations = read_config_file(CONFIG_FILE)
    if not abbreviations:
        print("Error: No abbreviations found in config file", file=sys.stderr)
        return False
    
    print("Downloading FFIEC IT booklets page...")
    try:
        response = requests.get(BOOKLETS_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error downloading page: {e}", file=sys.stderr)
        return False
    
    print("Parsing booklet information...")
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Look for links in the menu-container class
    menu_container = soup.find(class_="menu-container")
    if not menu_container:
        print("Warning: menu-container not found, searching entire page")
        menu_container = soup
    
    booklets = {}
    booklet_sections = {}  # Track sections by booklet for sequential numbering
    
    # First pass: collect all sections by booklet
    for link in menu_container.find_all('a', href=True):
        href = link['href']
        
        # Skip if not a booklet link
        if '/it-booklets/' not in href:
            continue
            
        # Skip the main booklets page
        if href.endswith('/it-booklets') or href.endswith('/it-booklets/'):
            continue
            
        title = link.get_text(strip=True)
        
        # Skip empty titles or common navigation
        if not title or title in ['IT Booklets', 'Home']:
            continue
            
        # Convert to absolute URL if needed
        full_url = urljoin(BASE_URL, href)
        
        # Parse the URL to extract original key and abbreviation
        old_key, booklet_abbrev = parse_booklet_url(full_url, abbreviations)
        
        if old_key is None:
            print(f"Warning: Could not parse URL {full_url}, skipping", file=sys.stderr)
            continue
        
        # Store for processing
        if booklet_abbrev not in booklet_sections:
            booklet_sections[booklet_abbrev] = []
        
        booklet_sections[booklet_abbrev].append((title, full_url, old_key))
    
    # Second pass: generate short keys with sequential numbering
    for booklet_abbrev in sorted(booklet_sections.keys()):
        sections = booklet_sections[booklet_abbrev]
        sequential_counter = 1
        
        for title, full_url, old_key in sections:
            # Determine if this is a main booklet page (no section suffix)
            is_main_booklet = old_key == f"ffiec_{booklet_abbrev}"
            
            if is_main_booklet:
                # Main booklet page
                short_key = booklet_abbrev
            else:
                # Parse title to determine section type
                section_type, identifier = parse_title_for_short_key(title, booklet_abbrev)
                
                if section_type == 'numbered' and identifier is None:
                    # Assign sequential number
                    short_key = generate_short_key(booklet_abbrev, section_type, identifier, sequential_counter)
                    sequential_counter += 1
                else:
                    # Use extracted identifier
                    short_key = generate_short_key(booklet_abbrev, section_type, identifier)
            
            # Check for duplicate keys
            if short_key in booklets:
                print(f"ERROR: Duplicate key '{short_key}' found for '{title}'", file=sys.stderr)
                print(f"       Existing: {booklets[short_key]['title']}", file=sys.stderr)
                print(f"       New: {title}", file=sys.stderr)
                return False
            
            # Create booklet entry
            booklets[short_key] = create_booklet_entry(short_key, booklet_abbrev, title, full_url)
            print(f"  {old_key} -> {short_key}: {title}")
    
    # Write YAML file
    if not write_yaml_file(yaml_file, booklets):
        return False
    
    print(f"[OK] YAML file created: {yaml_file}")
    print(f"[OK] Found {len(booklets)} booklets/sections")
    return True

def download_html_files(yaml_file, html_output_dir):
    """Download HTML files for all booklets listed in the YAML file."""
    # Create output directory
    html_output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=== Downloading HTML files ===")
    print(f"Reading YAML file: {yaml_file}")
    data = read_yaml_file(yaml_file)
    if data is None:
        return False
    
    # Extract booklets data
    if not data:
        print("No booklet data found in YAML file", file=sys.stderr)
        return False
    
    print(f"Found {len(data)} booklets/sections to download")
    print(f"HTML output directory: {html_output_dir}")
    
    success_count = 0
    error_count = 0
    
    for key, booklet_info in data.items():
        url = booklet_info.get('url')
        title = booklet_info.get('title', 'Unknown Title')
        
        if not url:
            print(f"Warning: No URL found for {key}")
            continue
            
        # Create filename from key
        html_filename = f"{key}.html"
        html_path = html_output_dir / html_filename
        
        # Skip if file already exists
        if html_path.exists():
            print(f"Skipping: {title}")
            print(f"  HTML: {html_filename} (already exists)")
            success_count += 1
            continue
        
        print(f"Downloading: {title}")
        print(f"  URL: {url}")
        print(f"  HTML: {html_filename}")
        
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            
            # Parse HTML and filter out navigation elements
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove navigation elements that interfere with content
            for nav_element in soup.find_all('ul', class_='menu-container'):
                nav_element.decompose()
            
            for nav_element in soup.find_all('ul', class_='nav-booklet-toc nav-pills text-smaller nobottommargin'):
                nav_element.decompose()
            
            # Write filtered HTML content to file
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            print(f"  [OK] HTML downloaded ({len(response.text)} characters)")
            success_count += 1
            
        except requests.RequestException as e:
            print(f"  ✗ Error downloading {url}: {e}")
            error_count += 1
            continue
        
        # Small delay to be respectful to the server
        time.sleep(DOWNLOAD_DELAY)
    
    print(f"[OK] HTML download complete: {success_count} success, {error_count} errors")
    return error_count == 0

def convert_to_markdown(html_output_dir, md_output_dir):
    """Convert HTML files to Markdown using pandoc."""
    # Create output directory
    md_output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=== Converting to Markdown ===")
    
    # Check for pandoc
    has_pandoc = check_pandoc()
    if not has_pandoc:
        print("✗ Pandoc not found - cannot convert to Markdown")
        print("  Install with: conda install -c conda-forge pandoc")
        return False
    
    print("[OK] Pandoc found")
    print(f"HTML input directory: {html_output_dir}")
    print(f"Markdown output directory: {md_output_dir}")
    
    # Find all HTML files
    html_files = list(html_output_dir.glob("*.html"))
    if not html_files:
        print("No HTML files found to convert")
        print("Run with --html flag first to download HTML files.")
        return False
    
    print(f"Found {len(html_files)} HTML files to convert")
    
    success_count = 0
    error_count = 0
    
    for html_path in html_files:
        md_filename = f"{html_path.stem}.md"
        md_path = md_output_dir / md_filename
        
        # Skip if markdown file already exists
        if md_path.exists():
            print(f"Skipping: {html_path.name} -> {md_filename} (already exists)")
            success_count += 1
            continue
        
        print(f"Converting: {html_path.name} -> {md_filename}")
        
        if convert_html_to_markdown(html_path, md_path):
            print("  [OK] Converted successfully")
            success_count += 1
        else:
            error_count += 1
    
    print(f"[OK] Markdown conversion complete: {success_count} success, {error_count} errors")
    return error_count == 0

def main():
    parser = argparse.ArgumentParser(
        description="FFIEC IT Booklets Manager - Generate YAML, download HTML, and convert to Markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --yml           Generate YAML file only
  %(prog)s --html          Download HTML files only  
  %(prog)s --md            Convert HTML to Markdown only
  %(prog)s --all           Perform all operations
  %(prog)s                 Perform all operations (default)
        """)
    
    parser.add_argument('--yml', action='store_true',
                       help='Generate YAML file with booklet structure')
    parser.add_argument('--html', action='store_true',
                       help='Download HTML files')
    parser.add_argument('--md', action='store_true',
                       help='Convert HTML files to Markdown')
    parser.add_argument('--all', action='store_true',
                       help='Perform all operations (yml + html + md)')
    
    args = parser.parse_args()
    
    # Default to --all if no specific flags are provided
    if not any([args.yml, args.html, args.md, args.all]):
        args.all = True
    
    # Set individual flags if --all is specified
    if args.all:
        args.yml = args.html = args.md = True
    
    success = True
    
    print("FFIEC IT Booklets Manager")
    print("=" * 50)
    
    if args.yml:
        success &= generate_yaml_file(YAML_FILE)
        print()
    
    if args.html and success:
        success &= download_html_files(YAML_FILE, HTML_OUTPUT_DIR)
        print()
    
    if args.md and success:
        success &= convert_to_markdown(HTML_OUTPUT_DIR, MD_OUTPUT_DIR)
        print()
    
    if success:
        print("[OK] All operations completed successfully!")
    else:
        print("✗ Some operations failed. Check the output above for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()