---
type: Dataset
id: https://w3id.org/lmodel/iso42001/knowledge/datasets/iso42001-linkml-schema
genre: reference
title: The iso42001 LinkML schema
description: "`src/iso42001/schema/iso42001.yaml`: the records an organization keeps to run an AI management system under ISO/IEC 42001:2023, with the `Aims` class prefix, the `aims_` slot prefix and `AimsManagementSystem` as its root."
resource: src/iso42001/schema/iso42001.yaml
about:
  - https://w3id.org/lmodel/iso42001/knowledge/references/iso-iec-42001
sources:
  - id: schema
    resource: src/iso42001/schema/iso42001.yaml
  - id: about.md
    resource: docs/about.md
    title: How the classes fit together
generated:
  by: process:ktl-librarian
  at: "2026-11-05T11:06:55Z"
status: draft
---

# The iso42001 LinkML schema

`AimsManagementSystem` is the tree root and holds each kind of record in a list of its own. Every record mixes in `AimsRecordMixin`, which gives it an `aims_id`, a title and a description, and a reference holds the `aims_id` of the record it names. A record that is documented information also mixes in `AimsDocumentControlMixin`.[^about.md]

Four families of variants are told apart by a designator: the entries of the Statement of Applicability, the resources of an AI system, events with the incidents among them, and third-party relationships with suppliers and customers among them.[^about.md]

An element cites what it models by number, in the `iso42001_clause`, `annex_a_control`, `annex_b_item`, `annex_c_item` or `annex_d_item` annotation, and its title and description are this project's own words. `AimsClause` and `AimsAnnexAControl` let a record cite the standard by number.[^schema]

[^schema]: src/iso42001/schema/iso42001.yaml
[^about.md]: docs/about.md, How the classes fit together
