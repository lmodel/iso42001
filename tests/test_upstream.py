"""Checks that the schema models the edition ISO's records name.

ISO sells the text of ISO/IEC 42001, so src/iso42001/schema/iso-open-data/ holds
ISO Open Data's records of the edition and its normative reference instead, which
scripts/check_upstream_release.py pins and watches. These tests read that extract
with the standard library, hold the schema header to it and to the watch's pins,
and hold the clause and Annex A enums to their numbering.
"""

import importlib.util
import json
import re
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "iso42001" / "schema" / "iso42001.yaml"
EXTRACT = (
    ROOT
    / "src"
    / "iso42001"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)

# Annex A's nine areas, and the last number of each control under them. A.6 has
# two control objectives, so its controls take one more level of number.
CONTROLS = {
    "A.2": (2, 3, 4),
    "A.3": (2, 3),
    "A.4": (2, 3, 4, 5, 6),
    "A.5": (2, 3, 4, 5),
    "A.6.1": (2, 3),
    "A.6.2": (2, 3, 4, 5, 6, 7, 8),
    "A.7": (2, 3, 4, 5, 6),
    "A.8": (2, 3, 4, 5),
    "A.9": (2, 3, 4),
    "A.10": (2, 3, 4),
}
CLAUSES = """
    4 4.1 4.2 4.3 4.4
    5 5.1 5.2 5.3
    6 6.1 6.1.1 6.1.2 6.1.3 6.1.4 6.2 6.3
    7 7.1 7.2 7.3 7.4 7.5 7.5.1 7.5.2 7.5.3
    8 8.1 8.2 8.3 8.4
    9 9.1 9.2 9.2.1 9.2.2 9.3 9.3.1 9.3.2 9.3.3
    10 10.1 10.2
""".split()
LIFE_CYCLE_STAGES = [
    "inception",
    "design_and_development",
    "verification_and_validation",
    "deployment",
    "operation_and_monitoring",
    "continuous_validation",
    "re_evaluation",
    "retirement",
]


@cache
def _watch():
    """The upstream watch script, loaded once as a module."""
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@cache
def _schema():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def _records():
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    return {r["id"]: r for r in map(json.loads, lines)}


def _values(enum):
    return _schema()["enums"][enum]["permissible_values"]


def _annotated(node, key):
    """Every value of an annotation anywhere in the schema."""
    if isinstance(node, dict):
        for name, value in node.items():
            if name == "annotations" and isinstance(value, dict) and key in value:
                yield from str(value[key]).split(", ")
            yield from _annotated(value, key)
    elif isinstance(node, list):
        for item in node:
            yield from _annotated(item, key)


def test_extract_matches_the_pinned_lines():
    """Each line of the extract hashes to the watch's pin, and the extract holds
    no scope, the field that summarizes the standard in ISO's words."""
    watch = _watch()
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    hashes = {json.loads(line)["id"]: watch.digest(line) for line in lines}
    assert hashes == watch.PINNED_RECORDS
    for record in _records().values():
        assert not set(watch.LEFT_OUT) & record.keys(), record["id"]
        assert watch.line_of(record) in lines


def test_header_pins_match_the_watch():
    """The header's version, source and dates are the ones the watch pins and the
    extract records."""
    watch = _watch()
    header = _schema()
    notes = header["annotations"]
    edition = _records()[watch.EDITION_ID]
    assert header["version"] == watch.PINNED_VERSION
    assert header["source"] == watch.PINNED_SOURCE
    assert header["source"].endswith(f"/{watch.EDITION_ID}.html")
    assert notes["standard"] == edition["reference"] == watch.PINNED_EDITION
    assert notes["edition"] == str(edition["edition"])
    assert notes["publication_date"] == edition["publicationDate"]
    assert notes["iso_open_data_date"] == watch.PINNED_DATE
    assert notes["normative_reference"] in {
        r["reference"] for r in _records().values()
    }


def test_published_records_and_supplements_in_development():
    """The two standards are published, and only the amendments of the normative
    reference are in development, so none of them is yet in force."""
    watch = _watch()
    for record in _records().values():
        if record["supplementType"]:
            assert record["currentStage"] != watch.PUBLISHED, record["reference"]
            assert record["reference"].startswith(watch.SUPPLEMENT_PREFIXES)
        else:
            assert record["currentStage"] == watch.PUBLISHED, record["reference"]
            assert not record["replacedBy"], record["reference"]


def test_annex_a_has_38_controls_in_nine_areas():
    """The Annex A enum holds each control once, and its title starts with its
    number and goes on to a name of this project's own."""
    enum = _values("AimsAnnexAControl")
    numbers = [
        f"{parent}.{last}" for parent, lasts in CONTROLS.items() for last in lasts
    ]
    assert len(numbers) == 38
    assert list(enum) == [n.lower().replace(".", "_") for n in numbers]
    for number, value in zip(numbers, enum.values()):
        assert re.fullmatch(rf"{re.escape(number)} \S.*", value["title"]), number
        assert value["description"].strip(), number


def test_areas_count_their_controls():
    """Each area names its number and how many controls it holds, and each control
    names an area whose number starts its own."""
    areas = _values("AimsControlArea")
    assert len(areas) == 9
    numbers = {
        name: pv["annotations"]["annex_a_clause"] for name, pv in areas.items()
    }
    counts = dict.fromkeys(areas, 0)
    for name, control in _values("AimsAnnexAControl").items():
        area = control["annotations"]["area"]
        counts[area] += 1
        assert control["title"].startswith(numbers[area] + "."), name
    assert counts == {
        name: int(pv["annotations"]["control_count"]) for name, pv in areas.items()
    }


def test_clauses_are_those_from_4_to_10():
    """The clause enum holds each numbered clause and subclause from 4 to 10, once,
    with its number as its title."""
    enum = _values("AimsClause")
    assert list(enum) == ["clause_" + n.replace(".", "_") for n in CLAUSES]
    for number, value in zip(CLAUSES, enum.values()):
        assert value["title"] == number


def test_life_cycle_stages_are_the_eight_of_the_normative_reference():
    """The enum holds the stages of ISO/IEC 22989:2022, in their order, and not the
    ten the schema used to carry."""
    assert list(_values("AimsLifecycleStage")) == LIFE_CYCLE_STAGES


def test_roles_name_a_family_of_the_enum():
    """Each more specific AI role names one of the six families."""
    enum = _values("AimsAiRole")
    families = {n for n, v in enum.items() if "annotations" not in v}
    assert len(families) == 6
    for name, value in enum.items():
        if "annotations" in value:
            assert value["annotations"]["role_family"] in families, name


def test_annex_c_values_are_numbered_without_gaps():
    """The objectives and risk sources of Annex C appear once each, and the other
    values are the ones the schema says come from elsewhere."""
    objectives = [
        v["annotations"]["annex_c_item"]
        for v in _values("AimsObjectiveCategory").values()
        if "annex_c_item" in v.get("annotations", {})
    ]
    assert objectives == [f"C.2.{n}" for n in range(1, 12)]
    sources = [
        v["annotations"]["annex_c_item"]
        for v in _values("AimsRiskSourceCategory").values()
        if "annex_c_item" in v.get("annotations", {})
    ]
    assert sources == [f"C.3.{n}" for n in range(1, 8)]
    for enum in ("AimsObjectiveCategory", "AimsRiskSourceCategory"):
        assert "other" in _values(enum)


def test_each_citation_names_something_the_schema_lists():
    """A clause annotation names a clause of the enum, a control annotation a
    control of the enum, and an Annex B item one that answers to a control or
    area, since Annex B numbers its guidance as Annex A numbers its controls."""
    schema = _schema()
    clauses = {v["title"] for v in _values("AimsClause").values()}
    controls = {
        v["title"].split()[0] for v in _values("AimsAnnexAControl").values()
    }
    for number in _annotated(schema, "iso42001_clause"):
        assert number in clauses | {"Annex A"}, number
    for number in _annotated(schema, "annex_a_control"):
        assert number in controls, number
    for number in _annotated(schema, "annex_b_item"):
        assert "A" + number[1:] in controls, number


def test_header_does_not_describe_a_supplement():
    """The standard has no supplement yet, so the version is the year alone. A
    supplement would change the header, as it does in lmodel/iso27001."""
    watch = _watch()
    assert not [
        r
        for r in _records().values()
        if r["reference"].startswith(f"{watch.PINNED_EDITION}/")
    ]
