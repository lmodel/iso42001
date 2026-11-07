---
type: Dataset
id: https://w3id.org/lmodel/iso42001/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/schema/iso42001.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: ten classes rooted on `Concept`, `aims_id` dropped for LOKF's `id`, `title` and `description` folded into LOKF's, and the four designators demoted."
resource: .lokf/schema/iso42001.yaml
derivedFrom:
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/iso42001-linkml-schema
about:
  - https://w3id.org/lmodel/iso42001/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - resource: .lokf/schema/iso42001.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:27:09Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/schema/iso42001.yaml` from the schema, and `just lokf-adapt-check` fails when it is stale. The roots are the classes a knowledge concept may use as its `type`: a policy, a role, a control, an AI system with its resources, and the documents and processes that describe how the system runs.[^project.justfile]

The README lists the concept types for the *Known LOKF types* setting. Every other key starts with `aims_`, so the copy shares none with lmodel/iso27001's, and a host can import both. A release attaches the copy as `schema-<tag>-iso42001.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
