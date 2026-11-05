## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/iso42001.yaml` is the copy `lokf adapt` writes from the schema so that
# it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The
# roots are the classes a knowledge concept may use as its `type`: a policy, a
# role, a control, an AI system with its resources, and the documents and
# processes that describe how the system runs. The recipes run the `lokf` the
# sidecar's floor pins (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root AimsPolicy --root AimsTopicSpecificPolicy --root AimsRole --root AimsControl --root AimsAiSystem --root AimsSystemResource --root AimsDevelopmentProcess --root AimsResponsibleUseProcess --root AimsDocumentedInformation --root AimsOperationalProcedure"

# Rewrite .lokf/iso42001.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/iso42001.yaml

# Fail when .lokf/iso42001.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/iso42001.yaml --check
