"""Data model package for iso42001."""

from pathlib import Path
from .iso42001 import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "iso42001.yaml"
