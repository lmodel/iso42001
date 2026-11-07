"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

import iso42001.datamodel.iso42001

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR_VALID = DATA_DIR / "valid"
DATA_DIR_INVALID = DATA_DIR / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))

SCHEMA = Path(__file__).parent.parent / "src" / "iso42001" / "schema" / "iso42001.yaml"


def _class_of(filepath):
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Each valid example loads into the generated dataclass of its class."""
    tgt_class = getattr(iso42001.datamodel.iso42001, _class_of(filepath))
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint (docs/index.md says what the generated models leave out), so each
# example is held to it: a valid one must pass, and a counter-example must fail.
# The examples quote their dates, as JSON carries them, because the validator
# reads a date as text.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        str(SCHEMA),
        _class_of(filepath),
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, so a file that starts failing for
    another reason fails this test."""
    text = Path(filepath).read_text(encoding="utf-8")
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    report = validate(yaml.safe_load(text), str(SCHEMA), _class_of(filepath))
    messages = [r.message for r in report.results]
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


def test_every_class_has_an_example():
    """Each class that data can be written in has a valid example: every class
    but the mixins and the abstract ones."""
    classes = {
        name
        for name, cls in yaml.safe_load(SCHEMA.read_text())["classes"].items()
        if not cls.get("abstract") and not cls.get("mixin")
    }
    examples = {_class_of(f) for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)


# The rules the validator cannot check, held over the examples. docs/index.md
# lists them.
VIEW = SchemaView(str(SCHEMA))
CLASSES = set(VIEW.all_classes())
DESIGNATORS = {
    name: slot.name
    for name in CLASSES
    for slot in VIEW.class_induced_slots(name)
    if slot.designates_type
}
AREAS = {
    name: value.annotations["area"].value
    for name, value in VIEW.get_enum("AimsAnnexAControl").permissible_values.items()
}


def _records(node, cls, found):
    """Collect every record a document holds, as (class, data), with each inlined
    record under the class its slot ranges over, or the class its designator
    names."""
    if isinstance(node, list):
        for item in node:
            _records(item, cls, found)
        return
    if not isinstance(node, dict):
        return
    cls = node.get(DESIGNATORS.get(cls, ""), cls)
    found.append((cls, node))
    slots = {s.name: s for s in VIEW.class_induced_slots(cls)}
    for key, value in node.items():
        slot = slots.get(key)
        if slot and slot.range in CLASSES and (slot.inlined or slot.inlined_as_list):
            _records(value, slot.range, found)


def _all_records(filepath):
    found = []
    _records(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        _class_of(filepath),
        found,
    )
    return found


@pytest.mark.parametrize(
    "filepath",
    [f for f in VALID_EXAMPLE_FILES if _class_of(f) == "AimsManagementSystem"],
)
def test_a_system_names_each_record_once_and_resolves_its_references(filepath):
    """Within a whole system, no two records share an aims_id, and each reference
    names a record the system holds, of the class it ranges over."""
    records = _all_records(filepath)
    ids = [data["aims_id"] for _, data in records if "aims_id" in data]
    repeated = sorted({i for i in ids if ids.count(i) > 1})
    assert not repeated, repeated
    classes = {data["aims_id"]: cls for cls, data in records if "aims_id" in data}
    for cls, data in records:
        for slot in VIEW.class_induced_slots(cls):
            if slot.range not in CLASSES or slot.inlined or slot.inlined_as_list:
                continue
            value = data.get(slot.name)
            targets = value if isinstance(value, list) else [value]
            for target in (t for t in targets if t is not None):
                assert target in classes, (slot.name, target)
                assert slot.range in VIEW.class_ancestors(classes[target]), (
                    slot.name,
                    target,
                    classes[target],
                )


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_examples_keep_the_rules_no_validator_checks(filepath):
    """A control's area is the area of one of the Annex A controls it answers to,
    an audit ends on or after the day it begins, and a Statement of Applicability
    lists no Annex A control twice."""
    for _, data in _all_records(filepath):
        area = data.get("aims_control_area")
        annex_a = data.get("aims_cited_annex_a_controls") or []
        if area and annex_a:
            assert area in {AREAS[c] for c in annex_a}, data.get("aims_id")
        start, end = (
            data.get("aims_audit_period_start"),
            data.get("aims_audit_period_end"),
        )
        if start and end:
            assert str(start) <= str(end), data.get("aims_id")
        controls = [
            e["aims_entry_annex_a_control"]
            for e in data.get("aims_soa_entries") or []
            if e.get("aims_entry_annex_a_control")
        ]
        repeated = sorted({c for c in controls if controls.count(c) > 1})
        assert not repeated, (data.get("aims_id"), repeated)
