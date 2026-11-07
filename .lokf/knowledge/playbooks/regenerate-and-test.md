---
type: Playbook
id: https://w3id.org/lmodel/iso42001/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the schema: edit `src/iso42001/schema/iso42001.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write."
references:
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/iso42001-linkml-schema
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/generated-artefacts
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the lint step
  - id: justfile
    resource: justfile
    title: the test recipe
  - resource: project.justfile
generated:
  by: process:ktl-librarian
  at: "2026-11-05T11:06:55Z"
status: draft
---

# Regenerate and test

1. Edit `src/iso42001/schema/iso42001.yaml`.[^contributing.md]
2. Run `just lint`. A warning fails it.[^main.yaml]
3. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`.[^contributing.md]
4. Run `just test`.[^justfile]
5. Commit what they wrote, with an example per new class and a counter-example per constraint.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^main.yaml]: .github/workflows/main.yaml, the lint step
[^justfile]: justfile, the test recipe
