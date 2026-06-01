"""Data test."""

import os
import glob
import yaml
import pytest
from pathlib import Path

import iso42001.datamodel.iso42001
from linkml_runtime.loaders import yaml_loader
from linkml.validator import validate

SCHEMA = Path(__file__).parents[1] / "src" / "iso42001" / "schema" / "iso42001.yaml"

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))


def _target_class(filepath):
    """Infer the target class name from the file stem (text before the first '-')."""
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Valid data files load and validate cleanly against the schema."""
    target_class_name = _target_class(filepath)
    tgt_class = getattr(iso42001.datamodel.iso42001, target_class_name)
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj

    report = validate(yaml.safe_load(Path(filepath).read_text()), str(SCHEMA), target_class_name)
    assert not report.results, f"{filepath} unexpectedly failed validation: {report.results}"


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Invalid (counter-example) data files are rejected by schema validation."""
    target_class_name = _target_class(filepath)
    report = validate(yaml.safe_load(Path(filepath).read_text()), str(SCHEMA), target_class_name)
    assert report.results, f"{filepath} unexpectedly passed validation"
