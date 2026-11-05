## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The catalogue and the SSSOM sets ============

# Write src/ai_governance_framework/data/aigf-v3.yaml from FINOS's files
[group('model development')]
build-catalogue:
  uv run python scripts/build_catalogue.py

# Fail when the catalogue differs from what FINOS's files give
[group('model development')]
check-catalogue:
  uv run python scripts/build_catalogue.py --check

# Write one SSSOM set for each of FINOS's reference files
[group('model development')]
build-mappings:
  uv run python scripts/build_sssom_mappings.py

# Fail when an SSSOM set differs from what FINOS's files give
[group('model development')]
check-mappings:
  uv run python scripts/build_sssom_mappings.py --check
