#!/usr/bin/env python3
"""
EU AI Act Content Extractor

Downloads content from the EU AI Act Explorer website and generates structured documentation
in both Markdown and YAML formats.

DESCRIPTION:
    This script scrapes the EU AI Act Explorer (https://artificialintelligenceact.eu/ai-act-explorer/)
    to extract the complete table of contents, including chapters, sections, articles, annexes,
    and recitals. It generates two output files:
    
    1. Markdown file: Human-readable table of contents with hierarchical structure
    2. YAML file: Machine-readable data for Jekyll sites with flattened keys
    
    The script preserves the document hierarchy while creating convenient access patterns
    for both human readers and automated systems.

FEATURES:
    - Downloads and caches HTML content locally
    - Extracts hierarchical structure (Chapters → Sections → Articles)
    - Generates clean, navigable Markdown with working hyperlinks
    - Creates YAML data with prefixed, flattened keys (e.g., eu-ai_c3-s2-a9)
    - Formats recitals in a compact table layout
    - Uses Roman numerals for proper chapter notation
    - Preserves document order for human readability

OUTPUT FILES:
    - _refs-markdown/eu-ai-act/eu-ai-act-toc.md: Markdown table of contents
    - _refs-markdown/eu-ai-act/eu-ai-act-toc.html: Cached HTML source
    - docs/_data/eu-ai-act.yml: YAML data for Jekyll integration

YAML FORMAT:
    The generated YAML uses hierarchical notation in titles:
    - Articles with sections: "III.S2.A9 Risk Management System"
    - Articles without sections: "I.A1 Subject Matter" 
    - Annexes: "Annex I List of Union Harmonisation Legislation"
    - Recitals: "Recital 1", "Recital 2", etc.

DEPENDENCIES:
    - requests: HTTP client for downloading content
    - beautifulsoup4: HTML parsing and navigation
    - pyyaml: YAML file generation
    - roman: Roman numeral conversion (install with: pip install roman)

USAGE:
    python dl_eu-ai-act.py [--download]
    
    --download: Force fresh download even if HTML file exists

EXAMPLES:
    # Generate files using cached HTML (if available)
    python dl_eu-ai-act.py
    
    # Force fresh download from source
    python dl_eu-ai-act.py --download

AUTHOR:
    Generated for FINOS AI Governance Framework
    
LAST UPDATED:
    2024
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import List, Optional, Dict, Any
import sys
import argparse
from urllib.parse import urljoin
from pathlib import Path
from dataclasses import dataclass
from itertools import islice
import yaml
import roman

# Constants
SCRIPT_DIR = Path(__file__).parent
BASE_URL = "https://artificialintelligenceact.eu/ai-act-explorer/"
OUTPUT_FILENAME = "eu-ai-act-toc.md"
HTML_FILENAME = "eu-ai-act-toc.html"
YAML_FILENAME = "eu-ai-act.yml"
RECITALS_TABLE_WIDTH = 10
YAML_KEY_PREFIX = ""  # Prefix for all YAML keys

# Path constants
EU_AI_ACT_DIR = SCRIPT_DIR / ".." / "_refs-markdown" / "eu-ai-act"
DATA_DIR = SCRIPT_DIR / ".." / "docs" / "_data"
OUTPUT_FILE = EU_AI_ACT_DIR / OUTPUT_FILENAME
HTML_FILE = EU_AI_ACT_DIR / HTML_FILENAME
YAML_FILE = DATA_DIR / YAML_FILENAME


@dataclass
class Link:
    """Represents a link with text and URL."""
    text: str
    url: str

    @classmethod
    def from_element(cls, element, base_url: str) -> Optional['Link']:
        """Create Link from BeautifulSoup element."""
        if not (link := element.find('a')):
            return None
        href = link.get('href', '')
        text = link.get_text(strip=True).replace('\n', ' ').strip()
        return cls(text, urljoin(base_url, href)) if href and text else None


@dataclass
class Section:
    """Represents a section with articles."""
    text: str
    url: str
    articles: List[Link]


@dataclass
class Chapter:
    """Represents a chapter with optional sections and articles."""
    text: str
    url: str
    sections: List[Section]
    articles: List[Link]


def chunked(iterable, n):
    """Batch data into lists of length n."""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, n)):
        yield chunk


def roman_to_int(roman_numeral: str) -> int:
    """Convert roman numeral to integer using the roman package."""
    try:
        return roman.fromRoman(roman_numeral.upper())
    except roman.InvalidRomanNumeralError:
        return 0


def int_to_roman(num: int) -> str:
    """Convert integer to roman numeral using the roman package."""
    try:
        return roman.toRoman(num)
    except (roman.OutOfRangeError, ValueError):
        return str(num)


def extract_numbers(text: str) -> Dict[str, int]:
    """Extract chapter, section, and article numbers from text."""
    result = {}
    
    # Extract chapter number (Roman numeral)
    if chapter_match := re.search(r'Chapter ([IVXLCDM]+)', text):
        result['chapter'] = roman_to_int(chapter_match.group(1))
    
    # Extract section number
    if section_match := re.search(r'Section (\d+)', text):
        result['section'] = int(section_match.group(1))
    
    # Extract article number
    if article_match := re.search(r'Article (\d+)', text):
        result['article'] = int(article_match.group(1))
    
    return result


def parse_hierarchical_content(soup: BeautifulSoup, base_url: str) -> List[Chapter]:
    """Parse chapters, sections, and articles in hierarchical order."""
    chapters = []
    current_chapter = None
    current_section = None
    
    # Find all elements before "Annexes" section
    relevant_elements = soup.find_all('p', class_=['parent-title', 'child-chapter', 'child-article'])
    
    for element in relevant_elements:
        if 'Annexes' in element.get_text(strip=True):
            break
            
        if not (link := Link.from_element(element, base_url)):
            continue
        
        classes = element.get('class', [])
        
        if 'parent-title' in classes and 'Chapter' in link.text:
            current_chapter = Chapter(link.text, link.url, [], [])
            chapters.append(current_chapter)
            current_section = None
            
        elif 'child-chapter' in classes and 'Section' in link.text and current_chapter:
            current_section = Section(link.text, link.url, [])
            current_chapter.sections.append(current_section)
            
        elif 'child-article' in classes and link.text.startswith('Article') and current_chapter:
            target = current_section if current_section else current_chapter
            target.articles.append(link)
    
    return chapters


def parse_section_links(soup: BeautifulSoup, section_name: str, base_url: str, *, link_filter=None) -> List[Link]:
    """Parse links from a named section with optional filtering."""
    # Find section header
    section_div = next(
        (div for div in soup.find_all('div', class_='et_pb_text_inner') 
         if section_name in div.get_text()), 
        None
    )
    
    if not section_div:
        return []
    
    links = []
    for link_element in section_div.find_all_next('a'):
        text = link_element.get_text(strip=True)
        href = link_element.get('href', '')
        
        if not (href and text):
            continue
        
        # Apply filter and check stop conditions
        if link_filter and not link_filter(text):
            if any(stop in text.lower() for stop in ['about', 'credits', 'feedback']):
                break
            if section_name == 'Annexes' and 'Recitals' in text:
                break
            continue
        
        # Clean up text for recitals
        if section_name == 'Recitals' and text.isdigit():
            text = f"Recital {text}"
        
        links.append(Link(text, urljoin(base_url, href)))
        
        # Stop condition for annexes
        if section_name == 'Annexes' and 'Recitals' in text:
            break
    
    return links


def build_toc_section(chapters: List[Chapter]) -> List[str]:
    """Build table of contents section as a list of strings."""
    lines = [
        "## Table of Contents",
        "",
        "The EU AI Act consists of 13 main chapters. Each chapter contains articles and sections.",
        ""
    ]
    
    for chapter in chapters:
        lines.extend([f"### [{chapter.text}]({chapter.url})", ""])
        
        # Direct articles (chapters without sections)
        for article in chapter.articles:
            lines.append(f"- [{article.text}]({article.url})")
        if chapter.articles:
            lines.append("")
        
        # Sections and their articles
        for section in chapter.sections:
            lines.extend([f"#### [{section.text}]({section.url})", ""])
            for article in section.articles:
                lines.append(f"- [{article.text}]({article.url})")
            lines.append("")
    
    return lines


def build_annexes_section(annexes: List[Link]) -> List[str]:
    """Build annexes section as a list of strings."""
    lines = [
        "## Annexes",
        "",
        "Annexes provide supplementary information alongside the Regulation.",
        ""
    ]
    
    for annex in annexes:
        lines.append(f"- [{annex.text}]({annex.url})")
    
    lines.append("")
    return lines


def build_recitals_section(recitals: List[Link]) -> List[str]:
    """Build recitals table section as a list of strings."""
    lines = [
        "## Recitals",
        "",
        "Recitals provide context about how an article should be interpreted or implemented.",
        ""
    ]
    
    if not recitals:
        return lines
    
    # Table header
    lines.append("|" + "|".join(["---------"] * RECITALS_TABLE_WIDTH) + "|")
    
    # Table rows
    for chunk in chunked(recitals, RECITALS_TABLE_WIDTH):
        row = []
        for recital in chunk:
            # Extract number for cleaner display
            if match := re.search(r'Recital (\d+)', recital.text):
                num = match.group(1)
            else:
                num = recital.text
            row.append(f"[{num}]({recital.url})")
        
        # Pad incomplete rows
        row.extend([""] * (RECITALS_TABLE_WIDTH - len(row)))
        lines.append("| " + " | ".join(row) + " |")
    
    lines.append("")
    return lines


def create_flattened_yaml_data(chapters: List[Chapter], annexes: List[Link], recitals: List[Link]) -> Dict[str, Any]:
    """Create flattened YAML data structure with combined keys in document order."""
    eu_ai_act = {}
    
    # Process chapters in order
    for chapter in chapters:
        chapter_nums = extract_numbers(chapter.text)
        chapter_num = chapter_nums.get('chapter', 0)
        chapter_roman = int_to_roman(chapter_num)
        
        # Direct articles (chapters without sections)
        for article in chapter.articles:
            article_nums = extract_numbers(article.text)
            article_num = article_nums.get('article', 0)
            
            if chapter_num and article_num:
                key = f"{YAML_KEY_PREFIX}c{chapter_num}-a{article_num}"
                # Extract just the article title (after "Article X:")
                article_title = re.sub(r'^Article \d+:\s*', '', article.text)
                title = f"{chapter_roman}.A{article_num} {article_title}"
                eu_ai_act[key] = {
                    'title': title,
                    'url': article.url
                }
        
        # Articles within sections (in section order)
        for section in chapter.sections:
            section_nums = extract_numbers(section.text)
            section_num = section_nums.get('section', 0)
            
            for article in section.articles:
                article_nums = extract_numbers(article.text)
                article_num = article_nums.get('article', 0)
                
                if chapter_num and section_num and article_num:
                    key = f"{YAML_KEY_PREFIX}c{chapter_num}-s{section_num}-a{article_num}"
                    # Extract just the article title (after "Article X:")
                    article_title = re.sub(r'^Article \d+:\s*', '', article.text)
                    title = f"{chapter_roman}.S{section_num}.A{article_num}: {article_title}"
                    eu_ai_act[key] = {
                        'title': title,
                        'url': article.url
                    }
    
    # Add annexes in order
    for i, annex in enumerate(annexes, 1):
        key = f"{YAML_KEY_PREFIX}annex-{i}"
        # Extract just the annex title (after "Annex X:")
        annex_title = re.sub(r'^Annex [IVXLCDM]+:\s*', '', annex.text)
        title = f"Annex {int_to_roman(i)}: {annex_title}"
        eu_ai_act[key] = {
            'title': title,
            'url': annex.url
        }
    
    # Add recitals in order
    for recital in recitals:
        if match := re.search(r'Recital (\d+)', recital.text):
            recital_num = int(match.group(1))
            key = f"{YAML_KEY_PREFIX}recital-{recital_num}"
            eu_ai_act[key] = {
                'title': f"Recital {recital_num}",
                'url': recital.url
            }
    
    return eu_ai_act


def create_markdown_document(chapters: List[Chapter], annexes: List[Link], recitals: List[Link]) -> str:
    """Create the complete markdown document by combining sections."""
    
    # Document header
    header_lines = [
        "# EU Artificial Intelligence Act - Structure and Contents",
        "",
        "This document provides a structured overview of the EU AI Act with hyperlinks to the official content.",
        "",
        f"Source: [EU AI Act Explorer]({BASE_URL})",
        ""
    ]
    
    # Footer
    footer_lines = [
        "---",
        "",
        "*Generated by dl_eu-ai-act.py*",
        "",
        "**Note:** This is an unofficial compilation. For official text, please refer to the ",
        "[Official Journal of the European Union](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)."
    ]
    
    # Combine all sections
    all_lines = []
    all_lines.extend(header_lines)
    all_lines.extend(build_toc_section(chapters))
    all_lines.extend(build_annexes_section(annexes))
    all_lines.extend(build_recitals_section(recitals))
    all_lines.extend(footer_lines)
    
    return "\n".join(all_lines)


def main():
    """Main function with clean, readable flow."""
    # Parse arguments
    parser = argparse.ArgumentParser(description="Download EU AI Act Explorer content")
    parser.add_argument('--download', action='store_true', help='Force download even if HTML file exists')
    args = parser.parse_args()
    
    try:
        # Ensure output directories exist
        EU_AI_ACT_DIR.mkdir(parents=True, exist_ok=True)
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        # Download or load HTML
        if args.download or not HTML_FILE.exists():
            print("Downloading EU AI Act Explorer page...")
            response = requests.get(BASE_URL, timeout=30)
            response.raise_for_status()
            html_content = response.text
            HTML_FILE.write_text(html_content, encoding='utf-8')
            print(f"Saved raw HTML to {HTML_FILE}")
        else:
            print(f"Using existing HTML file: {HTML_FILE}")
            html_content = HTML_FILE.read_text(encoding='utf-8')
        
        # Parse content
        print("Parsing table of contents, annexes, and recitals...")
        soup = BeautifulSoup(html_content, 'html.parser')
        
        chapters = parse_hierarchical_content(soup, BASE_URL)
        annexes = parse_section_links(soup, 'Annexes', BASE_URL, link_filter=lambda t: 'Annex' in t)
        recitals = parse_section_links(soup, 'Recitals', BASE_URL, link_filter=str.isdigit)
        
        # Calculate and report statistics
        total_sections = sum(len(c.sections) for c in chapters)
        total_articles = sum(len(c.articles) + sum(len(s.articles) for s in c.sections) for c in chapters)
        
        print(f"Found {len(chapters)} chapters, {total_sections} sections, {total_articles} articles")
        print(f"Found {len(annexes)} annexes, {len(recitals)} recitals")
        
        # Generate and write markdown
        print("Generating Markdown file...")
        markdown_content = create_markdown_document(chapters, annexes, recitals)
        OUTPUT_FILE.write_text(markdown_content, encoding='utf-8')
        print(f"Successfully created {OUTPUT_FILE}")
        
        # Generate and write YAML
        print("Generating YAML file...")
        yaml_data = create_flattened_yaml_data(chapters, annexes, recitals)
        
        yaml_content = f"# EU AI Act\n# Generated from {BASE_URL}\n\n"
        yaml_content += yaml.dump(yaml_data, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        YAML_FILE.write_text(yaml_content, encoding='utf-8')
        print(f"Successfully created {YAML_FILE}")
        
        total_items = len(chapters) + total_sections + total_articles + len(annexes) + len(recitals)
        print(f"Total items processed: {total_items}")
        print(f"YAML entries created: {len(yaml_data)}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
