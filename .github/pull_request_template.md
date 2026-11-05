## Summary

Closes #

## What changed?

- [ ] The schema (`src/iso42001/schema/`), and the regenerated artefacts
- [ ] Tests or example data (`tests/`)
- [ ] This repo's own `.lokf/knowledge/` bundle (documentation *about this repo*)
- [ ] Repository packaging only (CI, templates, docs unrelated to the schema)

## Checklist

- [ ] `just test` passes locally
- [ ] Generated files were regenerated with `just gen-project`, `just gen-doc` and `just lokf-adapt`, not edited by hand
- [ ] Each new or changed element names the clause or Annex A control of ISO/IEC 42001:2023 it models, in this project's own words, with no text copied from the standard
- [ ] `src/iso42001/schema/iso-open-data/` is unchanged, or replaced whole from one day's ISO Open Data with the pins in `scripts/check_upstream_release.py` updated
- [ ] If `.lokf/` changed, `cd .lokf && just lokf-validate` passes
- [ ] A behaviour change has an entry under `## [Unreleased]` in `CHANGELOG.md`

## AI Assistance

If you used AI tools while preparing this PR, you are still the author and responsible for understanding, verifying, and defending your submission. Please engage with reviewers personally rather than through your agent during feedback and revisions. Don't dump LLM output into this PR without curation. See the [AI Covenant](../AI_COVENANT.md) for details.
