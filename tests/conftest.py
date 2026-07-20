from pathlib import Path

import pytest

from auditor import load_package


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def package():
    return load_package((ROOT / "demo_data" / "continuity-package.json").read_text(encoding="utf-8"))


@pytest.fixture
def problematic_scene():
    return (ROOT / "demo_data" / "new-scene.md").read_text(encoding="utf-8")


@pytest.fixture
def clean_scene():
    return (ROOT / "demo_data" / "clean-scene.md").read_text(encoding="utf-8")
