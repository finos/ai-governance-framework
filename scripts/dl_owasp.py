#!/usr/bin/env python3
"""
Unified OWASP Content Downloader

Downloads content from various OWASP projects and generates structured documentation
in both Markdown and YAML formats.

DESCRIPTION:
    This script downloads markdown files from OWASP GitHub repositories and generates
    YAML data files for Jekyll integration. It supports multiple OWASP projects through
    a configuration-driven approach.

SUPPORTED PROJECTS:
    - LLM: OWASP Top 10 for Large Language Model Applications
    - ML: OWASP Machine Learning Security Top 10

FEATURES:
    - Configuration-driven approach for easy extensibility
    - Downloads and caches markdown content locally
    - Generates YAML data with normalized keys for Jekyll integration
    - Handles different metadata extraction methods (headings vs YAML frontmatter)
    - Supports different file filtering patterns and URL generation

OUTPUT FILES:
    - _refs-markdown/owasp-{project}_{year}/: Downloaded markdown files
    - docs/_data/owasp-{project}.yml: YAML data for Jekyll integration

DEPENDENCIES:
    - requests: HTTP client for downloading content
    - pyyaml: YAML file generation

USAGE:
    python dl_owasp.py [project]
    
    project: llm, ml, or all (default: all)

EXAMPLES:
    # Download all OWASP projects
    python dl_owasp.py
    
    # Download only LLM project
    python dl_owasp.py llm
    
    # Download only ML project
    python dl_owasp.py ml

AUTHOR:
    Generated for FINOS AI Governance Framework
    
LAST UPDATED:
    2025
"""

import os
import sys
import json
import time
import requests
import argparse
from pathlib import Path
import yaml
import re

# Constants
SCRIPT_DIR = Path(__file__).parent

# Project configurations
OWASP_PROJECTS = {
    'llm': {
        'repo': 'www-project-top-10-for-large-language-model-applications',
        'branch': 'main',
        'subdir': '2_0_vulns',
        'year': '2025',
        'filter_pattern': r'.*\.md$',
        'metadata_type': 'heading',
        'url_template': 'https://genai.owasp.org/llmrisk/llm{num_year_format}-{slug}/',
        'key_format': 'llm{num:02d}-{year}',
        'title_prefix': 'LLM'
    },
    'ml': {
        'repo': 'www-project-machine-learning-security-top-10',
        'branch': 'master',
        'subdir': 'docs',
        'year': '2023',
        'filter_pattern': r'^ML\d{2}_\d{4}.*\.md$',
        'metadata_type': 'frontmatter',
        'url_template': 'https://owasp.org/www-project-machine-learning-security-top-10/docs/{filename}.html',
        'key_format': 'ml{num:02d}-{year}',
        'title_prefix': 'ML'
    }
}

def get_paths(project_name, config):
    """Calculate all file and directory paths based on script directory and project config."""
    return {
        'output_dir': SCRIPT_DIR / ".." / f"_refs-markdown/owasp-{project_name}_{config['year']}",
        'data_file': SCRIPT_DIR / ".." / "docs" / "_data" / f"owasp-{project_name}.yml"
    }


def download_project_files(project_name, config):
    """Download OWASP project markdown files and generate data file."""
    
    paths = get_paths(project_name, config)
    output_dir = paths['output_dir']
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get file list from GitHub API
    print(f"Fetching {project_name.upper()} file list from GitHub API for year {config['year']}...")
    api_url = f"https://api.github.com/repos/OWASP/{config['repo']}/contents/{config['subdir']}"
    
    try:
        response = requests.get(api_url, params={"ref": config['branch']})
        response.raise_for_status()
        files = response.json()
    except requests.RequestException as e:
        print(f"Error fetching {project_name.upper()} file list: {e}")
        return []
    
    # Filter for markdown files using project-specific pattern
    pattern = re.compile(config['filter_pattern'])
    md_files = [f for f in files if f["name"].endswith(".md") and pattern.match(f["name"])]
    
    # Download each markdown file
    print(f"Downloading {project_name.upper()} markdown files...")
    downloaded_files = []
    
    for file_info in md_files:
        filename = file_info["name"]
        file_path = file_info["path"]
        output_file = output_dir / filename
        
        # Skip download if file already exists
        if output_file.exists():
            print(f"Skipping {filename} (already exists)...")
            downloaded_files.append(filename)
            continue
        
        raw_url = f"https://raw.githubusercontent.com/OWASP/{config['repo']}/{config['branch']}/{file_path}"
        
        try:
            print(f"Downloading {filename}...")
            response = requests.get(raw_url)
            response.raise_for_status()
            
            output_file.write_text(response.text, encoding='utf-8')
            downloaded_files.append(filename)
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
            
        except requests.RequestException as e:
            print(f"Error downloading {filename}: {e}")
    
    print(f"Done! Downloaded {len(downloaded_files)} .md files for {project_name.upper()} {config['year']} to {output_dir}/")
    
    # Generate data file
    generate_data_file(project_name, config, downloaded_files)
    return downloaded_files


def extract_file_metadata_heading(file_path, config):
    """Extract title and URL from a markdown file using heading parsing."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title from first heading
        lines = content.split('\n')
        title = None
        for line in lines:
            if line.startswith('## '):
                title = line[3:].strip()
                break
        
        # Generate URL based on filename and title for LLM project
        filename = file_path.stem
        if filename.startswith(config['title_prefix']) and title:
            num = filename[3:5]  # Extract number like "01", "02", etc.
            # Create slug from title: remove LLM prefix and year, convert to lowercase, replace spaces/special chars with hyphens
            title_for_slug = title
            if title_for_slug.startswith('LLM'):
                # Remove "LLM01:2025" or "LLM04:" or similar prefix
                title_for_slug = re.sub(r'^LLM\d+:(\d+\s*)?', '', title_for_slug)
            
            # Convert to slug: lowercase, replace spaces and special chars with hyphens
            slug = re.sub(r'[^\w\s-]', '', title_for_slug.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')
            
            # Format URL with number, year, and slug - LLM01 is special case without year
            num_int = int(num)
            if num_int == 1:
                num_year_format = f"{num_int:02d}"  # LLM01 doesn't have year in URL
            else:
                num_year_format = f"{num_int:02d}{config['year']}"  # LLM02+ have year
            
            url = config['url_template'].format(
                num_year_format=num_year_format,
                slug=slug
            )
        else:
            url = config['url_template'].format(num_year_format='', slug='')
        
        return title, url
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None


def extract_file_metadata_frontmatter(file_path, config):
    """Extract title and URL from a markdown file using YAML frontmatter parsing."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        title = None
        if content.startswith('---'):
            yaml_end = content.find('\n---\n', 4)
            if yaml_end != -1:
                yaml_content = content[4:yaml_end]
                try:
                    metadata = yaml.safe_load(yaml_content)
                    title = metadata.get('title', '')
                except yaml.YAMLError:
                    title = None
        
        # Generate URL based on filename
        filename = file_path.stem
        url = config['url_template'].format(filename=filename)
        
        return title, url
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None


def extract_file_metadata(file_path, config):
    """Extract title and URL from a markdown file using project-specific method."""
    if config['metadata_type'] == 'heading':
        return extract_file_metadata_heading(file_path, config)
    elif config['metadata_type'] == 'frontmatter':
        return extract_file_metadata_frontmatter(file_path, config)
    else:
        raise ValueError(f"Unknown metadata type: {config['metadata_type']}")


def generate_data_file(project_name, config, files):
    """Generate OWASP project data file at docs/_data/owasp-{project}.yml"""
    
    paths = get_paths(project_name, config)
    data_file = paths['data_file']
    output_dir = paths['output_dir']
    
    # Ensure data directory exists
    data_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Create data structure
    data = {}
    
    # Process each downloaded file
    for filename in files:
        file_path = output_dir / filename
        title, url = extract_file_metadata(file_path, config)
        
        if title and url:
            # Extract number based on project type
            if project_name == 'llm' and filename.startswith('LLM'):
                num = filename[3:5]  # Extract "01", "02", etc.
                # Skip preface with number "00"
                if num == "00":
                    continue
                key = config['key_format'].format(num=int(num), year=config['year'])
                
            elif project_name == 'ml' and filename.startswith('ML') and '_' in filename:
                # Extract ML number and year (e.g., ML01_2023 -> ml01-2023)
                parts = filename.split('_', 1)
                num = int(parts[0][2:])  # Extract numeric part after "ML"
                year_part = parts[1].split('-')[0] if '-' in parts[1] else parts[1].split('.')[0]
                key = config['key_format'].format(num=num, year=year_part)
                
            else:
                continue  # Skip files that don't match expected pattern
            
            data[key] = {
                'title': title,
                'url': url
            }
            print(f"Added {key}: {title}")
    
    # Write data file
    with open(data_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Created {data_file} with OWASP {project_name.upper()} {config['year']} entries")


def main():
    """Download OWASP project files."""
    parser = argparse.ArgumentParser(description="Download OWASP project content")
    parser.add_argument('project', nargs='?', default='all', 
                        choices=['llm', 'ml', 'all'],
                        help='OWASP project to download (default: all)')
    args = parser.parse_args()
    
    # Determine which projects to process
    if args.project == 'all':
        projects_to_process = list(OWASP_PROJECTS.keys())
    else:
        projects_to_process = [args.project]
    
    # Process each selected project
    total_files = 0
    for project_name in projects_to_process:
        config = OWASP_PROJECTS[project_name]
        print(f"\n=== Processing OWASP {project_name.upper()} ===")
        files = download_project_files(project_name, config)
        total_files += len(files)
    
    print(f"\n=== Summary ===")
    print(f"Total files processed across all projects: {total_files}")


if __name__ == "__main__":
    main()
