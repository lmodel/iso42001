#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Check this repository's words against a licence holder's copy of the standard.

The schema, the docs and the knowledge bundle are this project's own words, and
NOTICE says so. This script tests that: it fails on any run of four or more
consecutive words shared with the standard. It also fails when the schema cites
a clause, control or annex item whose number starts no line of the standard.

Give it the standard as plain text, for example from ``pdftotext`` run on your
own licensed copy. Keep that file outside the repository: it must never be
committed or published. The script is not part of CI, since CI has no copy.

Usage::

    python scripts/check_overlap.py --source /path/outside/the/repository/iso42001.txt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "iso42001" / "schema" / "iso42001.yaml"
RUN = 4
WORD = re.compile(r"[a-z0-9]+")

# Word runs allowed to match, each with its reason.
ALLOWED = {
    "iso iec 42001 2023": "the standard's own reference",
    "iso iec 22989 2022": "the reference the standard itself cites by this name",
    "information technology artificial intelligence management system": (
        "the standard's own title, which NOTICE cites"
    ),
    "statement of applicability": "a term the standard defines, used as its name",
}

# What holds text a person reads, and what the schema's cross-references cite.
TEXT_KEYS = {"description", "title", "comments", "notes"}
NUMBER_KEYS = {
    "iso42001_clause": "",
    "annex_a_control": "",
    "annex_b_item": "",
    "annex_c_item": "",
    "annex_d_item": "",
}


def words(text: str) -> list[str]:
    """The text's words in lower case, with a dotted number such as A.6.1.2 as one."""
    text = re.sub(r"(?<=\w)\.(?=\d)", "", text.lower())
    return WORD.findall(text.replace("\u2019", "").replace("'", ""))


def source_words(text: str) -> list[str]:
    """The source's words, with a word that a line break split put back together."""
    return words(re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text))


def schema_texts(node, path=""):
    """Each string a person reads in the schema, with where it sits."""
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{path}/{key}"
            if key in TEXT_KEYS and isinstance(value, str):
                yield here, value
            elif key in TEXT_KEYS and isinstance(value, list):
                for item in value:
                    yield here, str(item)
            else:
                yield from schema_texts(value, here)
    elif isinstance(node, list):
        for item in node:
            yield from schema_texts(item, path)


def schema_numbers(node):
    """Each clause, control or annex item number the schema cites."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in NUMBER_KEYS and isinstance(value, str):
                yield from value.split(", ")
            else:
                yield from schema_numbers(value)
    elif isinstance(node, list):
        for item in node:
            yield from schema_numbers(item)


def other_files() -> list[Path]:
    """The Markdown this project writes, and its NOTICE."""
    patterns = (
        "README.md",
        "NOTICE",
        "docs/*.md",
        "src/iso42001/schema/*.md",
        ".lokf/knowledge/**/*.md",
    )
    return sorted(p for pattern in patterns for p in ROOT.glob(pattern))


def overlaps(text: str, shingles: set[tuple[str, ...]]) -> list[str]:
    """Each maximal run of the text's words that the source also holds, with the
    allowed runs taken out first."""
    tokens = words(text)
    for phrase in ALLOWED:
        allowed = phrase.split()
        for start in range(len(tokens) - len(allowed) + 1):
            if tokens[start : start + len(allowed)] == allowed:
                tokens[start : start + len(allowed)] = [""] * len(allowed)
    found, start = [], None
    for i in range(len(tokens) - RUN + 2):
        hit = tuple(tokens[i : i + RUN]) in shingles
        if hit and start is None:
            start = i
        elif not hit and start is not None:
            found.append(" ".join(tokens[start : i + RUN - 1]))
            start = None
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--source", type=Path, required=True, help="The standard as plain text"
    )
    args = parser.parse_args(argv)
    if ROOT in args.source.resolve().parents:
        print(f"{args.source} sits inside the repository. Move it out.")
        return 2
    raw = args.source.read_text(encoding="utf-8", errors="replace")
    tokens = source_words(raw)
    shingles = {tuple(tokens[i : i + RUN]) for i in range(len(tokens) - RUN + 1)}

    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    problems = []
    for where, text in schema_texts(schema):
        problems += [f"schema {where}: {run}" for run in overlaps(text, shingles)]
    for path in other_files():
        text = path.read_text(encoding="utf-8")
        name = path.relative_to(ROOT)
        problems += [f"{name}: {run}" for run in overlaps(text, shingles)]
    for number in sorted(set(schema_numbers(schema))):
        if number == "Annex A":
            continue
        if not re.search(rf"^\s*{re.escape(number)}\s", raw, flags=re.M):
            problems.append(f"schema cites {number}, which starts no line of the source")

    print("\n".join(problems) if problems else "OK: nothing shared, every number found")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
