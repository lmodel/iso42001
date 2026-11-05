# About iso42001

This page says how the [LinkML](https://linkml.io) schema's classes fit together and what the model leaves out. [NOTICE](https://github.com/lmodel/iso42001/blob/main/NOTICE) says what rights it rests on.

## How the classes fit together

`AimsManagementSystem` is the tree root and holds each kind of record in a list of its own. Every record mixes in `AimsRecordMixin`, which gives it an `aims_id`, a title and a description, and a reference holds the `aims_id` of the record it names. A record that is documented information also mixes in `AimsDocumentControlMixin`.

Three families of variants are told apart by a designator: the entries of the Statement of Applicability, the resources of an AI system, and events with the incidents among them. `AimsThirdPartyRelationship` and its supplier and customer classes work the same way.

## Lists and scales

`AimsClause` and `AimsAnnexAControl` let a record cite the standard by number. Their titles and descriptions are this project's. The risk, likelihood and consequence scales are offered for an organization that adopts them, since the standard leaves them to the organization. An enum built from an annex that gives examples has the value `other`.

## What the model leaves out

- The text of the standard.
- Certification itself, beyond the system's own record of an audit and its status.
- A fixed method of risk assessment.
- The rules no validator checks, which the [overview](index.md) lists.
