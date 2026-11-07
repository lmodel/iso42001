---
type: AimsPolicy
id: https://w3id.org/lmodel/iso42001/knowledge/datasets/example-policy
genre: reference
title: An AI policy as a concept
description: An example written as a concept of type `AimsPolicy` in the adapt copy's keys. It shows that the domain schema admits a policy as a concept, citing the clause and the Annex A control it answers to by number.
resource: tests/data/valid/AimsPolicy-ai.yaml
references:
  - https://w3id.org/lmodel/iso42001/knowledge/datasets/adapt-copy
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: example
    resource: tests/data/valid/AimsPolicy-ai.yaml
aims_cited_clauses:
  - clause_5_2
aims_cited_annex_a_controls:
  - a_2_2
aims_policy_statement: Acme builds AI to help clinicians, who stay in charge.
aims_policy_commitments:
  - Meet the rules that apply to us
  - Keep making the system better
generated:
  by: process:ktl-librarian
  at: "2026-11-05T11:06:55Z"
status: draft
---

# An AI policy as a concept

This concept carries the statement and commitments of the example in `tests/data/valid/`, written in the keys the adapt copy gives a concept.[^example] The README lists the classes a concept may name as its type.[^readme.md]

[^example]: tests/data/valid/AimsPolicy-ai.yaml
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
