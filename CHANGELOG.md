# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `iso42001.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-07

### Added

- **ISO Open Data's records** of the edition and its normative reference, with a weekly watch. It reads only https addresses on a list of hosts and caps what it reads.
- **Enums for citing the standard by number**, `AimsClause` and `AimsAnnexAControl`, and slots that use them.
- **Classes for processes and information the old schema lacked**, such as planned actions, identified impacts, development and use processes, and what users and others are told.
- **Mappings to lmodel/nist-ai-100-1 and lmodel/iso29100**, for an AI system, an impact and a risk, and for the parts a party plays with personal data.
- **A link from an audit finding to the nonconformity it records**, `aims_finding_nonconformity`, which only a finding of a nonconformity may carry.
- **`.lokf/iso42001.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-iso42001.yaml`.
- **The Knowledge Trust Ladder (KTL) sidecar**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md and the CONTRIBUTING checklist.
- **`scripts/check_overlap.py`**, for a licence holder to test this repository's words against their own copy.

### Changed

- **The schema is rewritten.** Classes and enums take the `Aims` prefix and slots the `aims_` prefix, every record has an `aims_id`, a reference holds one, and a record of a class that comes in kinds states its kind.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, the Python project is named `iso42001-linkml`, and the generators' settings move to `.linkml/generators.yaml`.

### Removed

- **The private text overlay**: its scaffold, scripts and page. An element cites the standard by number, and a reader with a licensed copy looks the text up there.
- **The seven SSSOM sets**, whose rows a matching tool wrote and many of whose targets do not exist.
- **The mkdocs site**, with redirects from its addresses to the new site.
