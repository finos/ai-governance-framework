#!/usr/bin/env python3
"""
This script updates the YAML front matter in risk and mitigation markdown files by adding titles
as comments next to their corresponding IDs in relevant sections.

Dependencies:
    pip install PyYAML

For each file in the '_mitigations' and '_risks' directories, the script:
1. Reads the external risk titles from YAML files in docs/_data/
2. Reads the risk titles from files in the '_risks' directory
3. Reads the mitigation titles from files in the '_mitigations' directory
4. Creates mappings of IDs to their titles
5. Updates the YAML front matter by adding the corresponding titles as comments
6. Preserves the rest of the file content and structure

Mitigation files (mi-*.md):
- Updates 'mitigates' section with risk titles
- Updates 'related_mitigations' section with mitigation titles

Risk files (ri-*.md):
- Updates 'related_risks' section with risk titles
- Updates reference sections (eu-ai-act_references, ffiec-itbooklets_references, ffiec-itbooklets_v2_references, iso-42001_references, nist-ai-600-1_references, nist-sp-800-53r5_references, owasp-llm_references, owasp-ml_references) with reference titles from docs/_data/*.yml

Example:
    Original YAML:
        mitigates:
          - ri-1
          - ri-2
        related_mitigations:
          - mi-8
          - mi-9
    
    Updated YAML:
        mitigates:
          - ri-1  # Information Leaked To Hosted Model
          - ri-2  # Unauthorized Access Data Leaks
        related_mitigations:
          - mi-8  # QoS/DDoS Prevention
          - mi-9  # Alerting DoW Spend Alert
"""

import os
import re
from pathlib import Path
import yaml

# Base directory for all relative paths
SCRIPT_DIR = Path(__file__).parent

# Reference types that correspond to YAML files in docs/_data/
REFERENCE_TYPES = [
    'eu-ai-act',
    'ffiec-itbooklets',
    'ffiec-itbooklets_v2',
    'iso-42001',
    'nist-ai-600-1',
    'nist-sp-800-53r5',
    'owasp-llm',
    'owasp-ml'
]

def read_yaml_header(file_path):
    """Read YAML front matter from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file starts with YAML front matter
    if content.startswith('---'):
        # Find the second '---' that closes the YAML block
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1])
            except Exception as e:
                print(f"Error parsing YAML in {file_path}: {e}")
                return None
    return None

def get_reference_titles():
    """Create mappings of reference IDs to their titles from YAML files in docs/_data."""
    reference_mappings = {}
    data_dir = SCRIPT_DIR / '..' / 'docs' / '_data'
    
    for reference_type in REFERENCE_TYPES:
        yaml_file = data_dir / f'{reference_type}.yml'
        ref_type = f'{reference_type}_references'
        
        if yaml_file.exists():
            reference_mappings[ref_type] = {}
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    
                if data:
                    for ref_id, ref_info in data.items():
                        if isinstance(ref_info, dict) and 'title' in ref_info:
                            reference_mappings[ref_type][ref_id] = ref_info['title']
            except Exception as e:
                print(f"Error reading from {yaml_file.name}: {e}")
    
    return reference_mappings

def get_titles_from_directory(directory_name, file_prefix, id_prefix):
    """Create a mapping of IDs to their titles from markdown files in a directory."""
    titles = {}
    directory = SCRIPT_DIR / '..' / 'docs' / directory_name
    
    for file_path in directory.glob(f'{file_prefix}-*.md'):
        yaml_data = read_yaml_header(file_path)
        if yaml_data and 'title' in yaml_data and 'sequence' in yaml_data:
            item_id = f"{id_prefix}-{yaml_data['sequence']}"
            titles[item_id] = yaml_data['title']
    
    return titles

def process_annotated_section(section_key, items, title_mapping):
    """Process a YAML section by adding title comments to items."""
    if not items:
        return []
    
    # Calculate max width for alignment
    max_width = max(len(str(item).strip()) for item in items)
    
    lines = [f'{section_key}:']
    for item in items:
        item_id = str(item).strip()
        title = title_mapping.get(item_id, '')
        if title:
            padded_id = item_id.ljust(max_width)
            lines.append(f'  - {padded_id}  # {title}')
        else:
            lines.append(f'  - {item_id}')
    
    return lines

def format_regular_section(key, value):
    """Format a regular YAML section (non-annotated)."""
    if isinstance(value, list):
        lines = [f'{key}:']
        lines.extend(f'  - {item}' for item in value)
        return lines
    else:
        return [f'{key}: {value}']

def update_file_yaml(file_path, title_mappings):
    """Update relevant sections of a risk or mitigation file with titles as comments."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has YAML front matter
    if not content.startswith('---'):
        return False
        
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    try:
        yaml_data = yaml.safe_load(parts[1])
        if not yaml_data:
            return False
        
        # Define which sections to annotate and their corresponding title mappings
        annotated_sections = {
            'mitigates': title_mappings['risks'],
            'related_mitigations': title_mappings['mitigations'],
            'related_risks': title_mappings['risks']
        }
        
        # Add all reference sections dynamically
        for key in title_mappings:
            if key.endswith('_references'):
                annotated_sections[key] = title_mappings[key]
        
        # Check if file has any sections we need to update
        sections_to_update = [key for key in annotated_sections if key in yaml_data]
        if not sections_to_update:
            return False
        
        # Build new YAML content
        yaml_lines = []
        for key, value in yaml_data.items():
            if key in annotated_sections:
                yaml_lines.extend(process_annotated_section(key, value, annotated_sections[key]))
            else:
                yaml_lines.extend(format_regular_section(key, value))
        
        # Reconstruct the file content
        updated_yaml = '\n'.join(yaml_lines)
        updated_content = f"---\n{updated_yaml}\n---{parts[2]}"
        
        # Write back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        return True
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def process_files_in_directory(directory_name, file_prefix, title_mappings):
    """Process all files in a directory that match the given prefix."""
    directory = SCRIPT_DIR / '..' / 'docs' / directory_name
    updated_count = 0
    
    for file_path in directory.glob(f'{file_prefix}-*.md'):
        if update_file_yaml(file_path, title_mappings):
            updated_count += 1
            print(f"Updated {file_path.name}")
    
    return updated_count

def main():
    # Get mappings of IDs to titles (references → risks → mitigations)
    reference_mappings = get_reference_titles()
    risk_titles = get_titles_from_directory('_risks', 'ri', 'ri')
    mitigation_titles = get_titles_from_directory('_mitigations', 'mi', 'mi')
    
    # Print counts for each reference type
    total_references = 0
    for ref_type, mapping in reference_mappings.items():
        count = len(mapping)
        total_references += count
        print(f"Found {count} {ref_type.replace('_', ' ')}")
    
    print(f"Found {len(risk_titles)} risk titles")
    print(f"Found {len(mitigation_titles)} mitigation titles")
    
    # Create consolidated title mappings
    title_mappings = {
        'risks': risk_titles,
        'mitigations': mitigation_titles
    }
    
    # Add reference mappings
    title_mappings.update(reference_mappings)
    
    # Process all files (risks → mitigations)
    risk_updated_count = process_files_in_directory('_risks', 'ri', title_mappings)
    mitigation_updated_count = process_files_in_directory('_mitigations', 'mi', title_mappings)
    
    print(f"\nUpdated {risk_updated_count} risk files")
    print(f"Updated {mitigation_updated_count} mitigation files")

if __name__ == '__main__':
    main()