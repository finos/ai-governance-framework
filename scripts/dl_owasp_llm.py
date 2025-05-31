#!/usr/bin/env python3

import os
import sys
import json
import time
import requests
from pathlib import Path
import yaml

# Constants
SCRIPT_DIR = Path(__file__).parent
REPO_OWNER = "OWASP"
REPO_NAME = "www-project-top-10-for-large-language-model-applications"
BRANCH = "main"
YEAR = "2025"
YEAR_SUBDIR = "2_0_vulns"

def get_paths():
    """Calculate all file and directory paths based on script directory."""
    return {
        'output_dir': SCRIPT_DIR / ".." / f"_refs-markdown/owasp-llm_{YEAR}",
        'data_file': SCRIPT_DIR / ".." / "docs" / "_data" / "owasp-llm.yml"
    }


def download_owasp_files():
    """Download OWASP LLM markdown files and generate data file."""
    
    paths = get_paths()
    
    output_dir = paths['output_dir']
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get file list from GitHub API
    print(f"Fetching file list from GitHub API for year {YEAR}...")
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YEAR_SUBDIR}"
    
    try:
        response = requests.get(api_url, params={"ref": BRANCH})
        response.raise_for_status()
        files = response.json()
    except requests.RequestException as e:
        print(f"Error fetching file list: {e}")
        sys.exit(1)
    
    # Filter for markdown files
    md_files = [f for f in files if f["name"].endswith(".md")]
    
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
    """Extract title and URL from a markdown file."""
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
        
        # Generate URL based on filename
        filename = file_path.stem
        if filename.startswith('LLM'):
            llm_num = filename[3:5]  # Extract number like "01", "02", etc.
            url = f"https://genai.owasp.org/llmrisk/llm{llm_num}/"
        else:
            url = "https://genai.owasp.org/"
        
        return title, url
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None


def generate_data_file(files):
    """Generate OWASP LLM data file at docs/_data/owasp-llm.yml"""
    
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
            if filename.startswith('LLM'):
                llm_num = filename[3:5]  # Extract "01", "02", etc.
                # Skip preface with number "00".
                if llm_num == "00":
                    continue
                # Sadly, title doesn't always have the year!
                # e.g. "## LLM04: Data and Model Poisoning"
                # So we use the filename to construct the key.
                key = f"llm{llm_num}-{YEAR}"
                
                data[key] = {
                    'title': title,
                    'url': url
                }
                print(f"Added {key}: {title}")
    
    # Write data file
    with open(data_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Created {data_file} with OWASP LLM {YEAR} entries")


def main():
    """Download OWASP LLM files for {YEAR}."""
    download_owasp_files()


if __name__ == "__main__":
    main()