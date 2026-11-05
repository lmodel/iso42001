# iso42001

This project is a LinkML model of the records an organization keeps to run an artificial intelligence (AI) management system under ISO/IEC 42001:2023. It holds no text of the standard.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together and what the model leaves out
- [`iso42001.yaml`](schema/iso42001.yaml): the schema

## Validating data

```bash
uv run linkml-validate -s src/iso42001/schema/iso42001.yaml -C AimsRisk risk.yaml
```

This checks a file against the JSON Schema generated from the schema. Write dates as quoted strings, as JSON carries them. Validate a file before loading it into a model in `src/iso42001/datamodel/`, since LinkML 1.12.1 generates models that check less.

No validator checks these rules:

- that a reference names a record the system holds, of the class the reference ranges over;
- that a list never repeats an identifier;
- that an audit ends on or after the day it begins, or that a control's area is the area of one of the Annex A controls it answers to;
- that the Statement of Applicability has one entry for each Annex A control.

`tests/test_data.py` checks the first two within the whole example, and the third over every example. For the last it checks only that no statement lists a control twice, since the examples are cut down.
