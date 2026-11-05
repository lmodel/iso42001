<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# iso42001

ISO/IEC 42001:2023 AI management system records (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/iso42001](https://lmodel.github.io/iso42001)

## What it models

The schema models the records an organization keeps to run an artificial intelligence (AI) management system under [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html), first edition. It holds no text of the standard. Elements cite clauses, Annex A controls and annex items by number.

ISO sells the standard's text, so [src/iso42001/schema/iso-open-data/](src/iso42001/schema/iso-open-data) pins ISO Open Data's records of the edition and of its normative reference, ISO/IEC 22989:2022, instead. A weekly workflow opens an issue when one of those records changes or ISO lists another supplement or edition. A licence holder can merge the standard's wording into a private copy of the schema with the overlay in [OVERLAY.md](src/iso42001/schema/OVERLAY.md).

## Influences

The record classes follow the harmonized structure as [lmodel/iso27001](https://github.com/lmodel/iso27001) models it. The risk treatment options follow ISO 31000, and the kinds of audit follow ISO 19011.

## Mappings

* **[lmodel/iso27001](https://github.com/lmodel/iso27001)**: `close_mappings` from each class to the class that cites the same clause number. `tests/test_schema_rules.py` checks both the class and the number against the released copy.
* **[lmodel/oscal](https://github.com/lmodel/oscal)**: `close_mappings` from a role and `related_mappings` from a control. `tests/test_schema_rules.py` checks them.
* **[lmodel/spdx](https://github.com/lmodel/spdx)**: `close_mappings` from the organization. `tests/test_schema_rules.py` checks it.

The schema is the one home for mappings. The seven SSSOM sets are gone: a matching tool wrote their rows, and many named terms or repositories that do not exist.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch, the overlay and a licence holder's check for shared words
* [src/iso42001/schema/](src/iso42001/schema): the LinkML schema (edit it), the overlay scaffold and ISO Open Data's records
* [src/iso42001/datamodel/](src/iso42001/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) sidecar. Its domain schema, `.lokf/iso42001.yaml`, is the copy `just lokf-adapt` writes from `src/iso42001/schema/iso42001.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-iso42001.yaml`, with its checksum and attestation.

In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AimsPolicy, AimsTopicSpecificPolicy, AimsRole, AimsControl, AimsAiSystem, AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource, AimsHumanResource, AimsDevelopmentProcess, AimsResponsibleUseProcess, AimsDocumentedInformation, AimsOperationalProcedure
```

The copy drops `aims_id` for LOKF's `id`, folds `title` and `description` into LOKF's, and demotes the four designators, since a concept's `type` already names its class. Every other key starts with `aims_`, so it shares none with lmodel/iso27001's copy, and a host can import both.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and a knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

ISO/IEC 42001 is copyright ISO and IEC, and [NOTICE](NOTICE) states this project's position. This is not an ISO project, and its use implies no endorsement by ISO or IEC.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
