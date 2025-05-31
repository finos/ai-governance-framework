#!/usr/bin/env python3

import os
import sys
import json
import time
import requests
from pathlib import Path
import yaml
import re

# Constants
SCRIPT_DIR = Path(__file__).parent
REPO_OWNER = "OWASP"
REPO_NAME = "www-project-machine-learning-security-top-10"
BRANCH = "master"
YEAR = "2023"
DOCS_SUBDIR = "docs"

def get_paths():
    """Calculate all file and directory paths based on script directory."""
    return {
        'output_dir': SCRIPT_DIR / ".." / f"_refs-markdown/owasp-ml_{YEAR}",
        'data_file': SCRIPT_DIR / ".." / "docs" / "_data" / "owasp-ml.yml"
    }


def download_owasp_ml_files():
    """Download OWASP ML markdown files and generate data file."""
    
    paths = get_paths()
    
    output_dir = paths['output_dir']
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get file list from GitHub API
    print(f"Fetching file list from GitHub API for year {YEAR}...")
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{DOCS_SUBDIR}"
    
    try:
        response = requests.get(api_url, params={"ref": BRANCH})
        response.raise_for_status()
        files = response.json()
    except requests.RequestException as e:
        print(f"Error fetching file list: {e}")
        sys.exit(1)
    
    # Filter for ML markdown files (ML01_2023, ML02_2023, etc.)
    ml_pattern = re.compile(r'^ML\d{2}_\d{4}.*\.md$')
    md_files = [f for f in files if f["name"].endswith(".md") and ml_pattern.match(f["name"])]
    
    # Download each markdown file
    print("Downloading markdown files...")
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
        
        raw_url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/{file_path}"
        
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
    
    print(f"Done! Downloaded {len(downloaded_files)} .md files for year {YEAR} to {output_dir}/")
    
    # Generate data file
    generate_data_file(downloaded_files)


def extract_file_metadata(file_path):
    """Extract title and URL from a markdown file with YAML frontmatter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        if content.startswith('---'):
            yaml_end = content.find('\n---\n', 4)
            if yaml_end != -1:
                yaml_content = content[4:yaml_end]
                try:
                    metadata = yaml.safe_load(yaml_content)
                    title = metadata.get('title', '')
                except yaml.YAMLError:
                    title = None
            else:
                title = None
        else:
            title = None
        
        # Generate URL based on filename and OWASP ML site structure
        filename = file_path.stem
        if filename.startswith('ML') and '_' in filename:
            # Extract ML number and year (e.g., ML01_2023 -> ml01, 2023)
            parts = filename.split('_', 1)
            ml_id = parts[0].lower()  # ml01, ml02, etc.
            url = f"https://owasp.org/www-project-machine-learning-security-top-10/docs/{filename}.html"
        else:
            url = "https://owasp.org/www-project-machine-learning-security-top-10/"
        
        return title, url
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None


def generate_data_file(files):
    """Generate OWASP ML data file at docs/_data/owasp-ml.yml"""
    
    paths = get_paths()
    data_file = paths['data_file']
    output_dir = paths['output_dir']
    
    # Ensure data directory exists
    data_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Create data structure
    data = {}
    
    # Process each downloaded file
    for filename in files:
        file_path = output_dir / filename
        title, url = extract_file_metadata(file_path)
        
        if title and url:
            if filename.startswith('ML') and '_' in filename:
                # Extract ML number and year (e.g., ML01_2023 -> ml01-2023)
                parts = filename.split('_', 1)
                ml_num = parts[0][2:].zfill(2)  # Extract "01", "02", etc.
                year_part = parts[1].split('-')[0] if '-' in parts[1] else parts[1].split('.')[0]
                
                key = f"ml{ml_num}-{year_part}"
                
                data[key] = {
                    'title': title,
                    'url': url
                }
                print(f"Added {key}: {title}")
    
    # Write data file
    with open(data_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Created {data_file} with OWASP ML {YEAR} entries")


def main():
    """Download OWASP ML files for {YEAR}."""
    download_owasp_ml_files()


if __name__ == "__main__":
    main()
