---
type: Reference
id: https://w3id.org/lmodel/iso42001/knowledge/references/iso-iec-42001
genre: reference
title: ISO/IEC 42001:2023
description: "The edition the schema models: ISO's record 81230, first edition, published 2023-12-18, with ISO/IEC 22989:2022 as its one normative reference. This bundle holds none of the standard's text."
resource: src/iso42001/schema/iso-open-data/iso_deliverables_metadata.jsonl
sources:
  - id: extract
    resource: src/iso42001/schema/iso-open-data/iso_deliverables_metadata.jsonl
  - id: notice
    resource: NOTICE
  - id: schema
    resource: src/iso42001/schema/iso42001.yaml
    title: the header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T11:06:55Z"
status: draft
---

# ISO/IEC 42001:2023

ISO's record 81230 gives the first edition, published on 2023-12-18. Record 74296 is ISO/IEC 22989:2022, the one normative reference, and records 88145 and 93144 are two amendments of that reference in progress, with no publication date.[^extract]

The schema header carries `version: "2023"` and ISO's page for the edition as `source`.[^schema] The standard is copyright ISO and IEC, and this repository and bundle hold none of its text. NOTICE gives the position.[^notice]

[^extract]: src/iso42001/schema/iso-open-data/iso_deliverables_metadata.jsonl
[^notice]: NOTICE
[^schema]: src/iso42001/schema/iso42001.yaml, the header
