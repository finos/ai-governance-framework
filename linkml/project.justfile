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

# ============ Knowledge bundle: the adapted domain schema ============

# `../.lokf/ai-governance-framework.yaml` is the copy `lokf adapt` writes from the
# schema so that it can sit beside `../.lokf/lokf.yaml` (`lokf adapt --help` lists
# the moves). The roots are the classes a knowledge concept may use as its `type`.
# The recipes run the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs
# another, such as a checkout:
# LOKF_CMD="uv run --project ../../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project ../.lokf lokf")
lokf_adapt_roots := "--root AigfItem --root AigfDataClassification --prefix aigf"

# Rewrite ../.lokf/ai-governance-framework.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf ../.lokf/lokf.yaml -o ../.lokf/ai-governance-framework.yaml

# Fail when ../.lokf/ai-governance-framework.yaml is stale against the schema or lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf ../.lokf/lokf.yaml -o ../.lokf/ai-governance-framework.yaml --check
