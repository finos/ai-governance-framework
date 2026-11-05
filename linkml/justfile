# ============ Shell configuration for Windows ============

# On Windows the "bash" shell from Git for Windows is used.
# If Git is installed in a non-standard location, edit the path below.
set windows-shell := ["C:/Program Files/Git/bin/bash", "-cu"]

# ============ Variables used in recipes ============

# Detect WSL2 variable
_wsl2_check := `[ -n "${WSL_INTEROP:-}" ] && [ -z "${JUST_TEMPDIR:-}" ] && echo "ERROR" || echo "OK"`

# Load environment variables from config.public.mk or specified file
set dotenv-load := true
# set dotenv-filename := env_var_or_default("LINKML_ENVIRONMENT_FILENAME", "config.public.mk")
set dotenv-filename := x'${LINKML_ENVIRONMENT_FILENAME:-config.public.mk}'

# Set shebang line for cross-platform Python recipes (assumes presence of launcher on Windows)
shebang := if os() == 'windows' {
  'py'
} else {
  '/usr/bin/env python3'
}

# Environment variables with defaults
schema_name := env_var_or_default("LINKML_SCHEMA_NAME", "_no_schema_given_")
source_schema_dir := env_var_or_default("LINKML_SCHEMA_SOURCE_DIR", "")
config_yaml := if env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "") != "" {
  "--config-file " + env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "")
} else {
  ""
}
gen_doc_args := env_var_or_default("LINKML_GENERATORS_DOC_ARGS", "")
gen_java_args := env_var_or_default("LINKML_GENERATORS_JAVA_ARGS", "")
gen_owl_args := env_var_or_default("LINKML_GENERATORS_OWL_ARGS", "")
gen_pydantic_args := env_var_or_default("LINKML_GENERATORS_PYDANTIC_ARGS", "")
gen_ts_args := env_var_or_default("LINKML_GENERATORS_TYPESCRIPT_ARGS", "")

# Directory variables
src := "src"
dest := "project"
pymodel := src / schema_name / "datamodel"
source_schema_path := source_schema_dir / schema_name + ".yaml"
docdir := "docs/elements"  # Directory for generated documentation
distrib_schema_path := "docs/schema"  # Directory for publishing schema artifacts

# ============== Project recipes ==============

# List all commands as default command. The prefix "_" hides the command.
_default: _status
    @{{ if _wsl2_check == "ERROR" { "echo 'WSL2 detected: run export JUST_TEMPDIR=/tmp'" } else { "" } }}
    @just --list

# WSL2 status check - warns but does not abort (safe to use in _status/_default)
[private]
_wsl2_status_check:
    @if [ -n "${WSL_INTEROP:-}" ] && [ -z "${JUST_TEMPDIR:-}" ]; then \
      echo "WARNING: WSL2 detected but JUST_TEMPDIR is not set."; \
      echo "Shebang recipes will fail with 'Permission denied' errors."; \
      echo "Fix: run 'export JUST_TEMPDIR=/tmp'"; \
    fi

# WSL2 compatibility check - fails early with helpful message
[private]
_wsl2_compat_check:
    @if [ -n "${WSL_INTEROP:-}" ] && [ -z "${JUST_TEMPDIR:-}" ]; then \
      echo "ERROR: WSL2 detected but JUST_TEMPDIR is not set."; \
      echo "Shebang recipes will fail with 'Permission denied' errors."; \
      echo ""; \
      echo "Fix: run this command:"; \
      echo ""; \
      echo "  export JUST_TEMPDIR=/tmp"; \
      echo ""; \
      echo "Or add it to your ~/.bashrc for persistence."; \
      exit 1; \
    fi

# Initialize a new project (use this for projects not yet under version control)
[group('project management')]
setup: _wsl2_compat_check _check-config _git-init install _git-add && _setup_part2
  git commit -m "Initialise git with minimal project" -a || true

_setup_part2: gen-project gen-doc
  @echo
  @echo '=== Setup completed! ==='
  @echo 'Various model representations have been created under directory "project". By default'
  @echo 'they are ignored by git. You decide whether you want to add them to git tracking or'
  @echo 'continue to git-ignore them as they can be regenerated if needed.'
  @echo 'For tracking specific subfolders, add !project/[foldername]/* line(s) to ".gitignore".'

# Install project dependencies
[group('project management')]
install:
  uv sync --group dev

# Updates project template and LinkML package
[group('project management')]
update: _update-template _update-linkml

# Clean all generated files
[group('project management')]
clean: _wsl2_compat_check _clean_project
  rm -rf tmp
  rm -rf {{docdir}}/*.md

# (Re-)Generate project and documentation locally
[group('model development')]
site: gen-project gen-doc

# Run all tests
[group('model development')]
test: _test-schema _test-python _test-examples

# Run linting
[group('model development')]
lint:
  uv run linkml-lint {{source_schema_dir}}

# Generate md documentation for the schema and add artifacts
[group('model development')]
gen-doc: _gen-yaml && _add-artifacts
  uv run gen-doc {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}

# Build docs and serve the website locally
[group('model development')]
testdoc: gen-doc _serve

# Generate the Python data models (dataclasses & pydantic)
gen-python:
  uv run gen-project -d  {{pymodel}} -I python {{source_schema_path}}
  uv run gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py

# Generate project files including Python data model
[group('model development')]
gen-project:
  uv run gen-project {{config_yaml}} -d {{dest}} {{source_schema_path}}
  mkdir -p {{pymodel}}
  mv {{dest}}/*.py {{pymodel}}/
  uv run gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py

  @# Some generators ignore config_yaml or cannot create directories, so we run them separately.
  uv run gen-java {{gen_java_args}} --output-directory {{dest}}/java/ {{source_schema_path}}

  @if [ ! -d "{{dest}}/typescript" ]; then \
    mkdir -p {{dest}}/typescript ; \
  fi
  uv run gen-typescript {{gen_ts_args}} {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts

  @if [ ! -d "{{dest}}/owl" ]; then \
    mkdir -p {{dest}}/owl ; \
  fi
  uv run gen-owl {{gen_owl_args}} {{source_schema_path}} > "{{dest}}/owl/{{schema_name}}.owl.ttl"

# ============== Migrations recipes for Copier ==============

# Hidden command to adjust the directory layout on upgrading a project
# created with linkml-project-copier v0.1.x to v0.2.0 or newer.
# Use with care! - It may not work for customized projects.
_post_upgrade_v020: _wsl2_compat_check && _post_upgrade_v020py
  mv docs/*.md docs/elements

_post_upgrade_v020py:
    #!{{shebang}}
    import subprocess
    from pathlib import Path
    # Git move files from folder src to folder dest
    tasks = [
        (Path("src/docs/files"), Path("docs")),
        (Path("src/docs/templates"), Path("docs/templates-linkml")),
        (Path("src/data/examples"), Path("tests/data/")),
    ]
    for src, dest in tasks:
        for path_obj in src.rglob("*"):
            if not path_obj.is_file():
                continue
            file_dest = dest / path_obj.relative_to(src)
            if not file_dest.parent.exists():
                file_dest.parent.mkdir(parents=True)
            print(f"Moving {path_obj} --> {file_dest}")
            subprocess.run(["git", "mv", str(path_obj), str(file_dest)])
    print(
        "Migration to v0.2.x completed! Check the changes carefully before committing."
    )

# ============== Hidden internal recipes ==============

# Show current project status
_status: _wsl2_status_check _check-config
  @echo "Project: {{schema_name}}"
  @echo "Source: {{source_schema_path}}"

# Check project configuration
_check-config:
    #!{{shebang}}
    import os
    schema_name = os.getenv('LINKML_SCHEMA_NAME')
    if not schema_name:
        print('**Project not configured**:\n - See \'.env.public\'')
        exit(1)
    print('Project-status: Ok')

# Update project template
_update-template:
  copier update --trust --skip-answered

# Update LinkML runtime and LinkML to latest versions
_update-linkml:
  uv lock --upgrade-package linkml-runtime --upgrade-package linkml

# Test schema generation
_test-schema:
  uv run gen-project {{config_yaml}} -d tmp {{source_schema_path}}

# Run Python unit tests with pytest
_test-python: gen-python
  uv run python -m pytest

# Run example tests
_test-examples: _ensure_examples_output
  uv run linkml-run-examples \
    --input-formats json \
    --input-formats yaml \
    --output-formats json \
    --output-formats yaml \
    --counter-example-input-directory tests/data/invalid \
    --input-directory tests/data/valid \
    --output-directory examples/output \
    --schema {{source_schema_path}} > examples/output/README.md

# Add the merged model to docs/schema.
_gen-yaml:
  -mkdir -p {{distrib_schema_path}}
  uv run gen-yaml {{source_schema_path}} > {{distrib_schema_path}}/{{schema_name}}.yaml

# Overridable recipe to add project-specific artifacts to the distribution schema path
_add-artifacts:

# Run the website's development server
_serve:
  cd website && npm ci --ignore-scripts && npm run dev

# Initialize git repository
_git-init:
  git init

# Add files to git
_git-add:
  git add .

# Commit files to git
_git-commit:
  git commit -m 'chore: just setup was run' -a

# Show git status
_git-status:
  git status

_clean_project:
    #!{{shebang}}
    import shutil, pathlib
    # remove the generated project files
    for d in pathlib.Path("{{dest}}").iterdir():
        if d.is_dir():
            print(f'removing "{d}"')
            shutil.rmtree(d, ignore_errors=True)
    # remove the generated python data model
    for d in pathlib.Path("{{pymodel}}").iterdir():
        if d.name == "__init__.py":
            continue
        print(f'removing "{d}"')
        if d.is_dir():
            shutil.rmtree(d, ignore_errors=True)
        else:
            d.unlink()

_ensure_examples_output:  # Ensure a clean examples/output directory exists
  -mkdir -p examples/output
  -rm -rf examples/output/*.*

# ============== Include project-specific recipes ==============

import "project.justfile"

# ====== Override recipes from above with custom versions =======

# Uncomment the following line to allow duplicate recipe names
#set allow-duplicate-recipes

# Overriding recipes from the root justfile by adding a recipe with the same
# name in an imported file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540 - So we need to override them here.
