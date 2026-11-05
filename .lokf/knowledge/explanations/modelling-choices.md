---
type: Explanation
id: https://w3id.org/lmodel/iso42001/knowledge/explanations/modelling-choices
genre: explanation
title: Modelling choices
description: "Why the schema has these shapes: records that refer by identifier, documented information under one document-control mixin, variants told apart by a designator, numbers for citing the standard, and scales offered for an organization that adopts them."
references:
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/iso42001-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
  - id: changelog.md
    resource: CHANGELOG.md
    title: Unreleased
generated:
  by: process:ktl-librarian
  at: "2026-11-05T11:06:55Z"
status: draft
---

# Modelling choices

The schema was rewritten with the `Aims` prefix on classes and enums and the `aims_` prefix on slots. Every record has an `aims_id`, a reference holds one, and a record of a class that comes in kinds states its kind.[^changelog.md]

`AimsClause` and `AimsAnnexAControl` let a record cite the standard by number, with titles and descriptions of this project's own. The risk, likelihood and consequence scales are offered for an organization that adopts them, since the standard leaves them to the organization, and an enum built from an annex that gives examples has the value `other`.[^about.md]

[^about.md]: docs/about.md
[^changelog.md]: CHANGELOG.md, Unreleased
