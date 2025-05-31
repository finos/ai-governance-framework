#!/usr/bin/env python3
"""
NIST Document PDF Deep Link Extractor

A utility tool for extracting precise deep-linkable bookmarks from NIST documents.

Supported Documents:
- NIST SP 800-53r5 (Security and Privacy Controls)
- NIST AI 600-1 (Artificial Intelligence Risk Management Framework)

Features:
- Object-based deep links using PDF internal references
- Section filtering with hierarchical navigation
- Coordinate-based positioning for pixel-perfect navigation
- Robust error handling and logging

Dependencies:
    pip install requests pypdf
"""

import argparse
import json
import logging
import re
import urllib.parse
import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import requests
from pypdf import PdfReader

# Constants
SCRIPT_DIR = Path(__file__).parent


@dataclass
class BookmarkInfo:
    """Represents a PDF bookmark with navigation metadata."""
    title: str
    page: Optional[int] = None
    level: int = 0
    x_coord: Optional[float] = None
    y_coord: Optional[float] = None
    zoom: Optional[float] = None
    obj_num: Optional[int] = None
    obj_gen: Optional[int] = None

    @property
    def has_coordinates(self) -> bool:
        """Check if bookmark has positioning coordinates."""
        return self.x_coord is not None and self.y_coord is not None

    @property
    def has_object_reference(self) -> bool:
        """Check if bookmark has PDF object reference."""
        return self.obj_num is not None


@dataclass
class Config:
    """Configuration for the PDF processor."""
    filename_prefix: str
    section_filter: str = "ALL"
    force_download: bool = False
    debug: bool = False
    title_case: bool = False
    ignore_anonymous_sections: bool = False
    leafs: bool = False
    leafs_section: str = ""

    @property
    def document_type(self) -> str:
        """Derive document type from filename prefix."""
        # Convert "NIST.SP.800-53r5" -> "nist-sp-800-53r5"
        # Convert "NIST.AI.600-1" -> "nist-ai-600-1"
        return self.filename_prefix.lower().replace('.', '-')

    @property
    def pdf_url(self) -> str:
        """Construct PDF URL from filename prefix."""
        base_url = "https://nvlpubs.nist.gov/nistpubs"
        
        if '.SP.' in self.filename_prefix:
            return f"{base_url}/SpecialPublications/{self.filename_prefix}.pdf"
        elif '.AI.' in self.filename_prefix:
            return f"{base_url}/ai/{self.filename_prefix}.pdf"
        else:
            # Fallback for other document types
            return f"{base_url}/{self.filename_prefix}.pdf"

    @property
    def output_dir(self) -> Path:
        """Derive output directory from document type."""
        return (SCRIPT_DIR / ".." / "_refs-markdown" / self.document_type).resolve()

    @property
    def pdf_filename(self) -> str:
        """Generate PDF filename from prefix."""
        return f"{self.filename_prefix}.pdf"
    

    
    def yaml_filename(self) -> str:
        """Generate YAML filename from document type."""
        return f"{self.document_type}.yml"
    
    @property
    def yaml_output_dir(self) -> Path:
        """Get YAML output directory (docs/_data)."""
        return SCRIPT_DIR / ".." / "docs" / "_data"
    
    def format_title(self, title: str) -> str:
        """Apply title case formatting to bookmark titles if enabled."""
        if not self.title_case:
            return title
            
        # Security control acronyms that should remain uppercase
        acronyms = {
            'AC', 'AT', 'AU', 'CA', 'CM', 'CP', 'IA', 'IR', 'MA', 'MP', 
            'PE', 'PL', 'PM', 'PS', 'PT', 'RA', 'SA', 'SC', 'SI', 'SR',
            'API', 'DNS', 'HTTP', 'HTTPS', 'IP', 'IT', 'OS', 'PKI', 'SQL',
            'TCP', 'TLS', 'SSL', 'VPN', 'GAI', 'AI', 'ML', 'PII', 'POA&M'
        }
        
        words = title.split()
        result = []
        
        for word in words:
            # Remove punctuation for acronym checking but preserve it
            clean_word = ''.join(c for c in word if c.isalnum())
            
            if clean_word.upper() in acronyms:
                # Keep acronyms uppercase but preserve original punctuation
                result.append(word.upper())
            elif clean_word.isalpha() and len(clean_word) > 1:
                # Apply title case to regular words
                result.append(word.capitalize())
            else:
                # Keep short words, numbers, punctuation as-is
                result.append(word)
        
        return ' '.join(result)

    @classmethod
    def for_sp_800_53r5(cls) -> 'Config':
        """Create configuration for NIST SP 800-53r5 document."""
        return cls(
            filename_prefix="NIST.SP.800-53r5",
            title_case=True,
            ignore_anonymous_sections=False,
            leafs_section="THE CONTROLS"
        )

    @classmethod  
    def for_ai_600_1(cls) -> 'Config':
        """Create configuration for NIST AI 600-1 document."""
        return cls(
            filename_prefix="NIST.AI.600-1",
            title_case=False,
            ignore_anonymous_sections=True,
            leafs_section="2. Overview of Risks Unique to or Exacerbated by GAI"
        )


class PDFProcessor:
    """Handles PDF downloading and parsing operations."""

    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def download_pdf(self) -> Path:
        """Download PDF if not cached locally."""
        pdf_path = self.config.output_dir / self.config.pdf_filename
        self.config.output_dir.mkdir(parents=True, exist_ok=True)

        if pdf_path.exists() and not self.config.force_download:
            self.logger.info(f"Using cached PDF: {pdf_path}")
            return pdf_path

        self.logger.info(f"Downloading PDF from {self.config.pdf_url}")
        try:
            response = requests.get(self.config.pdf_url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(pdf_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            self.logger.info(f"PDF saved to {pdf_path}")
            return pdf_path
            
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to download PDF: {e}")

    def load_pdf(self, pdf_path: Path) -> PdfReader:
        """Load PDF and return reader object."""
        try:
            reader = PdfReader(str(pdf_path))
            self.logger.info(f"Loaded PDF with {len(reader.pages)} pages")
            return reader
        except Exception as e:
            raise RuntimeError(f"Failed to load PDF: {e}")


class BookmarkExtractor:
    """Extracts and processes PDF bookmarks with coordinates."""

    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def extract_bookmarks(self, reader: PdfReader) -> List[BookmarkInfo]:
        """Extract all bookmarks from PDF with full navigation hierarchy."""
        if not reader.outline:
            self.logger.warning("No outline found in PDF")
            return []

        # Use the simpler approach from V2 that works better with pypdf
        bookmarks = self._extract_v2_recursive(reader.outline, reader)
        
        self.logger.info(f"Extracted {len(bookmarks)} bookmarks")
        
        coord_count = sum(1 for bm in bookmarks if bm.has_coordinates)
        obj_count = sum(1 for bm in bookmarks if bm.has_object_reference)
        self.logger.info(f"Found {coord_count} bookmarks with coordinates, {obj_count} with object references")
        
        return bookmarks

    def _extract_v2_recursive(self, outline_items: Union[List, object], reader: PdfReader, level: int = 0) -> List[BookmarkInfo]:
        """V2-style recursive extraction that handles pypdf children properly."""
        bookmarks = []
        
        # Handle both single items and lists
        if not isinstance(outline_items, list):
            outline_items = [outline_items]
        
        for outline_item in outline_items:
            # Extract current item
            bookmark = self._extract_bookmark_info(outline_item, reader, level)
            if bookmark:
                bookmarks.append(bookmark)
                
                if self.config.debug:
                    coords = f"@({bookmark.x_coord:.1f},{bookmark.y_coord:.1f})" if bookmark.has_coordinates else ""
                    obj_ref = f"obj({bookmark.obj_num},{bookmark.obj_gen})" if bookmark.has_object_reference else ""
                    self.logger.debug(f"{'  ' * level}{bookmark.title} -> Page {bookmark.page} {coords} {obj_ref}")
            
            # Process children - handle different child container types
            children = None
            if hasattr(outline_item, 'children') and outline_item.children:
                children = outline_item.children
            elif isinstance(outline_item, list):
                children = outline_item
            
            if children:
                try:
                    # Convert children to list if it's an iterator or other type
                    if hasattr(children, '__iter__') and not isinstance(children, (str, bytes)):
                        children_list = list(children)
                        if children_list:
                            bookmarks.extend(self._extract_v2_recursive(children_list, reader, level + 1))
                    else:
                        bookmarks.extend(self._extract_v2_recursive([children], reader, level + 1))
                except Exception as e:
                    if self.config.debug:
                        self.logger.warning(f"Error processing children at level {level}: {e}")
        
        return bookmarks



    def _extract_bookmark_info(self, outline_item: object, reader: PdfReader, level: int) -> Optional[BookmarkInfo]:
        """Extract detailed information from a single bookmark."""
        if not hasattr(outline_item, 'title'):
            return None

        title = str(outline_item.title).strip()
        bookmark = BookmarkInfo(title=title, level=level)

        try:
            # Extract page information and object reference
            if '/Page' in outline_item:
                page_ref = outline_item['/Page']
                
                # Get object reference - try multiple approaches like V2
                if hasattr(page_ref, 'idnum') and hasattr(page_ref, 'generation'):
                    bookmark.obj_num = page_ref.idnum
                    bookmark.obj_gen = page_ref.generation
                elif hasattr(page_ref, 'indirect_reference'):
                    ref = page_ref.indirect_reference
                    if hasattr(ref, 'idnum') and hasattr(ref, 'generation'):
                        bookmark.obj_num = ref.idnum
                        bookmark.obj_gen = ref.generation

                # Find page number
                for page_idx, page in enumerate(reader.pages):
                    if page == page_ref:
                        bookmark.page = page_idx + 1
                        break

            # Extract coordinates from destination
            self._extract_coordinates(outline_item, bookmark)

        except Exception as e:
            self.logger.warning(f"Error extracting bookmark info for '{title}': {e}")

        return bookmark

    def _extract_coordinates(self, outline_item: object, bookmark: BookmarkInfo) -> None:
        """Extract coordinate information from outline item."""
        try:
            # Try to get coordinates from destination array
            if hasattr(outline_item, 'node') and outline_item.node and '/D' in outline_item.node:
                dest_array = outline_item.node['/D']
                if isinstance(dest_array, list) and len(dest_array) >= 4:
                    if dest_array[1] == '/XYZ':
                        bookmark.x_coord = float(dest_array[2]) if dest_array[2] is not None else None
                        bookmark.y_coord = float(dest_array[3]) if dest_array[3] is not None else None
                        if len(dest_array) >= 5 and dest_array[4] is not None:
                            bookmark.zoom = float(dest_array[4])
                    elif dest_array[1] == '/FitH' and len(dest_array) >= 3:
                        bookmark.y_coord = float(dest_array[2]) if dest_array[2] is not None else None

            # Fallback coordinate extraction
            if bookmark.x_coord is None and '/Left' in outline_item:
                bookmark.x_coord = float(outline_item['/Left'])
            if bookmark.y_coord is None and '/Top' in outline_item:
                bookmark.y_coord = float(outline_item['/Top'])

        except (ValueError, TypeError, KeyError) as e:
            self.logger.debug(f"Could not extract coordinates for '{bookmark.title}': {e}")


class BookmarkFilter:
    """Filters bookmarks by section and other criteria."""

    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def filter_by_section(self, bookmarks: List[BookmarkInfo]) -> List[BookmarkInfo]:
        """Filter bookmarks by section name."""
        filtered = []
        in_target_section = self.config.section_filter.upper() == "ALL"
        target_level = None

        for bookmark in bookmarks:
            # Skip anonymous sections if configured
            if self.config.ignore_anonymous_sections and self._is_anonymous_section(bookmark.title):
                continue

            if in_target_section:
                # For specific section: include children until we hit another section at same/higher level
                if self.config.section_filter.upper() == "ALL" or bookmark.level > target_level:
                    filtered.append(bookmark)
                else:
                    # Hit another section at same/higher level, stop
                    break
            else:
                # For specific section: check if this is our target section
                if self.config.section_filter.upper() in bookmark.title.upper():
                    in_target_section = True
                    target_level = bookmark.level
                    filtered.append(bookmark)

        # Apply leafs filtering if enabled
        if self.config.leafs:
            filtered = self._filter_to_leaf_nodes(filtered)

        self.logger.info(f"Filtered to {len(filtered)} bookmarks for section '{self.config.section_filter}'")
        if self.config.leafs:
            self.logger.info("Applied leaf node filtering")
        return filtered

    def _filter_to_leaf_nodes(self, bookmarks: List[BookmarkInfo]) -> List[BookmarkInfo]:
        """Filter bookmarks to only include leaf nodes (nodes with no children)."""
        leaf_bookmarks = []
        
        for i, bookmark in enumerate(bookmarks):
            # Check if this bookmark has any children (next bookmark at deeper level)
            is_leaf = True
            for j in range(i + 1, len(bookmarks)):
                next_bookmark = bookmarks[j]
                if next_bookmark.level > bookmark.level:
                    # Found a child, this is not a leaf
                    is_leaf = False
                    break
                elif next_bookmark.level <= bookmark.level:
                    # Found a sibling or parent, stop checking
                    break
            
            if is_leaf:
                leaf_bookmarks.append(bookmark)
        
        return leaf_bookmarks



    def _is_anonymous_section(self, title: str) -> bool:
        """Check if a section title is anonymous (just numbers/punctuation)."""
        import re
        # Match titles that are just numbers, dots, and whitespace (like "1.", "2.", etc.)
        return bool(re.match(r'^\s*\d+\.?\s*$', title.strip()))


class DeepLinkGenerator:
    """Generates enhanced deep links with object references and coordinates."""

    def __init__(self, config: Config):
        self.config = config
        self.base_url = self.config.pdf_url

    def create_link(self, bookmark: BookmarkInfo) -> str:
        """Create the most precise deep link possible for a bookmark."""
        if not bookmark.page:
            return self.base_url

        # Prefer object-based links for maximum precision
        if bookmark.has_object_reference and bookmark.has_coordinates:
            return self._create_object_link(bookmark)

        # Fallback to page+coordinate links
        if bookmark.has_coordinates:
            return self._create_coordinate_link(bookmark)

        # Final fallback to page-only link
        return f"{self.base_url}#page={bookmark.page}"

    def _create_object_link(self, bookmark: BookmarkInfo) -> str:
        """Create object-based deep link with coordinates."""
        dest_array = [
            {"num": bookmark.obj_num, "gen": bookmark.obj_gen or 0},
            {"name": "XYZ"},
            bookmark.x_coord,
            bookmark.y_coord,
            bookmark.zoom or 0
        ]
        dest_json = json.dumps(dest_array, separators=(',', ':'))
        dest_encoded = urllib.parse.quote(dest_json)
        return f"{self.base_url}#{dest_encoded}"

    def _create_coordinate_link(self, bookmark: BookmarkInfo) -> str:
        """Create page+coordinate deep link."""
        page_url = f"{self.base_url}#page={bookmark.page}"
        
        if bookmark.x_coord is not None and bookmark.y_coord is not None:
            zoom_param = f",{bookmark.zoom:.2f}" if bookmark.zoom else ",null"
            return f"{page_url}&view=XYZ,{bookmark.x_coord:.1f},{bookmark.y_coord:.1f}{zoom_param}"
        elif bookmark.y_coord is not None:
            return f"{page_url}&view=FitH,{bookmark.y_coord:.1f}"
        
        return page_url




class YamlGenerator:
    """Generates YAML output for Jekyll integration."""

    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def generate_yaml(self, bookmarks: List[BookmarkInfo], link_generator: DeepLinkGenerator) -> str:
        """Generate YAML document with flattened keys."""
        # Remove the extra level and output bookmark dict directly
        yaml_data = self._create_bookmark_dict(bookmarks, link_generator)
        
        # Generate YAML content with header
        yaml_content = f"# NIST {self.config.document_type.upper()}\n"
        yaml_content += f"# Generated from {self.config.pdf_url}\n\n"
        yaml_content += yaml.dump(yaml_data, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        return yaml_content

    def _create_bookmark_dict(self, bookmarks: List[BookmarkInfo], link_generator: DeepLinkGenerator) -> Dict[str, Dict[str, str]]:
        """Create dictionary of bookmarks with normalized keys."""
        result = {}
        
        for bookmark in bookmarks:
            # Generate normalized key from title
            key = self._normalize_key(bookmark.title)
            if key:
                result[key] = {
                    'title': self.config.format_title(bookmark.title),
                    'url': link_generator.create_link(bookmark)
                }
        
        return result

    def _normalize_key(self, title: str) -> str:
        """Normalize bookmark title to create YAML key."""
        # Extract section number if present (e.g., "2.1.", "AC-1", etc.)
        # Handle different patterns: "2.1. Title", "AC-1 Title", "2.10. Title"
        
        # Pattern for numbered sections like "2.1. Title" or "2.10. Title"
        if match := re.match(r'^(\d+(?:\.\d+)*)\.\s*(.+)', title):
            section_num = match.group(1).replace('.', '-')
            return section_num
        
        # Pattern for control codes like "AC-1 Title"
        if match := re.match(r'^([A-Z]{2,3}-\d+(?:\(\d+\))?)\s+(.+)', title):
            control_code = match.group(1).lower()
            return control_code
        
        # Pattern for simple numbers like "1.", "2."
        if match := re.match(r'^(\d+)\.\s*(.+)', title):
            return match.group(1)
        
        # Fallback: create key from first meaningful part
        # Remove special characters and use first few words
        cleaned = re.sub(r'[^\w\s-]', '', title.lower())
        words = cleaned.split()[:3]  # Take first 3 words
        return '-'.join(words) if words else 'item'

    def write_to_file(self, content: str) -> Path:
        """Write YAML content to file in docs/_data directory."""
        output_dir = self.config.yaml_output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = self.config.yaml_filename()
        output_path = output_dir / filename
        
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.logger.info(f"YAML written to {output_path}")
            return output_path
        except IOError as e:
            raise RuntimeError(f"Failed to write YAML file: {e}")



class NISTProcessor:
    """Main orchestrator for NIST document processing workflow."""

    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.pdf_processor = PDFProcessor(config)
        self.bookmark_extractor = BookmarkExtractor(config)
        self.bookmark_filter = BookmarkFilter(config)
        self.link_generator = DeepLinkGenerator(config)

        self.yaml_generator = YamlGenerator(config)

    def process(self) -> Path:
        """Execute the complete processing workflow."""
        doc_name = "NIST AI 600-1" if self.config.document_type == "ai-600-1" else "NIST SP 800-53r5"
        self.logger.info(f"Starting {doc_name} processing for section: {self.config.section_filter}")
        
        # Download and load PDF
        pdf_path = self.pdf_processor.download_pdf()
        reader = self.pdf_processor.load_pdf(pdf_path)
        
        # Extract and filter bookmarks
        all_bookmarks = self.bookmark_extractor.extract_bookmarks(reader)
        filtered_bookmarks = self.bookmark_filter.filter_by_section(all_bookmarks)
        
        # Generate YAML output
        yaml_content = self.yaml_generator.generate_yaml(filtered_bookmarks, self.link_generator)
        output_path = self.yaml_generator.write_to_file(yaml_content)
        
        self.logger.info("Processing completed successfully")
        return output_path


def setup_logging(debug: bool = False) -> None:
    """Configure logging with appropriate level and format."""
    level = logging.DEBUG if debug else logging.INFO
    format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" if debug else "%(levelname)s: %(message)s"
    
    logging.basicConfig(
        level=level,
        format=format_str,
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def parse_arguments() -> Config:
    """Parse command line arguments and return configuration."""
    parser = argparse.ArgumentParser(
        description="Extract NIST document bookmarks as YAML data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""
Examples:
  %(prog)s --document sp-800-53r5                          # Extract all sections from SP 800-53r5
  %(prog)s --document ai-600-1                             # Extract all sections from AI 600-1
  %(prog)s --document sp-800-53r5 --section "THE CONTROLS" # Extract THE CONTROLS section  
  %(prog)s --document sp-800-53r5 --leafs                  # Extract only leaf nodes from THE CONTROLS
  %(prog)s --document ai-600-1 --leafs                     # Extract leaf nodes from AI document
  %(prog)s --document sp-800-53r5 --force-download --debug # Force re-download with debug
        """
    )
    
    parser.add_argument(
        '--document',
        choices=['sp-800-53r5', 'ai-600-1'],
        required=True,
        help='NIST document to process'
    )
    parser.add_argument(
        '--section', 
        default='ALL',
        help='Section to extract. Use "ALL" for all sections'
    )
    parser.add_argument(
        '--force-download',
        action='store_true',
        help='Force re-download of PDF even if cached locally'
    )
    parser.add_argument(
        '--debug',
        action='store_true', 
        help='Enable debug logging'
    )


    parser.add_argument(
        '--leafs',
        action='store_true',
        help='Extract only leaf nodes from the document-specific leafs section'
    )

    
    args = parser.parse_args()
    
    # Create appropriate config based on document type
    if args.document == 'ai-600-1':
        config = Config.for_ai_600_1()
    else:
        config = Config.for_sp_800_53r5()
    
    # Override with command line arguments
    config.section_filter = args.section
    config.force_download = args.force_download
    config.debug = args.debug

    config.leafs = args.leafs
    
    # When leafs mode is enabled, override section filter to use leafs_section
    if config.leafs:
        config.section_filter = config.leafs_section
    

    
    return config


def main() -> None:
    """Main entry point."""
    config = None
    try:
        config = parse_arguments()
        setup_logging(config.debug)
        
        processor = NISTProcessor(config)
        output_path = processor.process()
        
        print(f"Successfully generated: {output_path}")
        
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        if config and config.debug:
            raise


if __name__ == "__main__":
    main()
