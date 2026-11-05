# ISO/IEC 42001:2023 private overlay

This page is for a licence holder who wants the standard's own wording in a private copy of the schema. The public schema, [iso42001.yaml](iso42001.yaml), holds only this project's words. The standard's text is © ISO/IEC and appears nowhere in this repository.

## The files

| File | In the repository? | What it holds |
| --- | --- | --- |
| [`iso42001.yaml`](iso42001.yaml) | yes | The public schema, complete without the overlay. |
| [`iso42001-overlay.template.yaml`](iso42001-overlay.template.yaml) | yes | An empty scaffold of every element, which `just create-empty-overlay` writes. It holds no text of the standard. |
| `iso42001-overlay.yaml` | no, git ignores it | Your copy of the scaffold, filled from your licensed copy. Never commit or publish it. |
| `tmp/iso42001-merged.yaml` | no, git ignores it | The merge of the public schema and your copy. Do not distribute it. |

## Steps

```bash
just create-empty-overlay
cp src/iso42001/schema/iso42001-overlay.template.yaml \
   src/iso42001/schema/iso42001-overlay.yaml
# Fill in iso42001-overlay.yaml from your licensed copy.
just overlay-licensed-text
```

An element's annotations in [iso42001.yaml](iso42001.yaml) name the clause, control or annex item to copy from: `iso42001_clause`, `annex_a_control`, `annex_b_item`, `annex_c_item` or `annex_d_item`. Fill only the entries you want, as a block scalar (`|`) so that lettered lists survive:

```yaml
classes:
  AimsPolicy:
    description: |
      <The text of clause 5.2 from your licensed copy.>
    comments:
      - "source: ISO/IEC 42001:2023 clause 5.2"
```

When the public schema changes, run `just create-empty-overlay` again and compare the scaffold with your copy to find new entries.

## What the merge takes

`scripts/overlay_populated_text.py` writes only under `tmp/` and refuses any other path. It reads `description`, `comments`, `title`, `aliases`, `see_also` and `notes`. A value in your copy replaces the public one, and an empty value is ignored. Everything else comes from the public schema, so the overlay changes only the text a person reads.

`tests/test_overlay.py` checks that git ignores both private files, that the scaffold holds no text, and that it matches the schema. If you fork this repository, keep those `.gitignore` lines.
