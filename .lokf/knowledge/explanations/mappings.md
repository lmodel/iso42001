---
type: Explanation
id: https://w3id.org/lmodel/iso42001/knowledge/explanations/mappings
genre: explanation
title: Mappings and the SSSOM sets
description: "Where the schema crosses to other vocabularies: close mappings to lmodel/iso27001's class of the same clause number, to OSCAL's role, SPDX's organization, the AI system and impact of lmodel/nist-ai-100-1 and the controller and processor of lmodel/iso29100, and related mappings to OSCAL's control and the AI RMF's risk, each tested. The seven SSSOM sets are gone."
references:
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/neighbour-copies
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:01:53Z"
status: draft
---

# Mappings and the SSSOM sets

The README lists each mapping, and the schema is their one home. A class maps closely to the class of lmodel/iso27001 that cites the same clause number, since both standards follow the harmonized structure.[^readme.md] `tests/test_schema_rules.py` holds each mapping to a class of a released copy, and each iso27001 mapping to the same clause number.[^test_schema_rules.py]

The seven SSSOM sets are gone: a matching tool wrote their rows, and many named terms or repositories that do not exist.[^readme.md]

[^readme.md]: README.md, Mappings
[^test_schema_rules.py]: tests/test_schema_rules.py
