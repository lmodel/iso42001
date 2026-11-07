---
type: Dataset
id: https://w3id.org/lmodel/iso42001/knowledge/datasets/example-data
genre: reference
title: The example data
description: "`tests/data/`: a valid example per class and a counter-example per constraint, each counter-example naming on its first line where it must fail. `AimsManagementSystem-acme` is one whole management system."
resource: tests/data
references:
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/iso42001-linkml-schema
sources:
  - id: test_data.py
    resource: tests/test_data.py
  - id: readme
    resource: tests/data/README.md
  - id: index.md
    resource: docs/index.md
    title: Validating data
  - resource: examples/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:13:10Z"
status: draft
---

# The example data

File names follow `ClassName-suffix.yaml`.[^readme] A counter-example's first line, `# Fails at: <pointer>`, names where it must fail, so a file that starts failing for another reason fails the test. Every class that is neither abstract nor a mixin has a valid example.[^test_data.py]

The same test file checks the rules no validator checks: within a whole system no two records share an `aims_id` and each reference names a record the system holds, of the class it ranges over; a control's area is the area of one of the Annex A controls it answers to; an audit ends on or after the day it begins; and a Statement of Applicability lists no Annex A control twice.[^test_data.py] The overview lists those rules for a reader.[^index.md]

[^readme]: tests/data/README.md
[^test_data.py]: tests/test_data.py
[^index.md]: docs/index.md, Validating data
