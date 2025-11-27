# ---------------------------------------------------------------------
# Gufo Font: Manifest class
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Third-party modules
import pytest

# Gufo Font modules
from gufo.font.manifest import Manifest


@pytest.fixture(scope="session")
def manifest() -> Manifest:
    return Manifest.read()


def test_version(manifest: Manifest) -> None:
    assert manifest.version


def test_not_empty(manifest: Manifest) -> None:
    assert manifest.icons


def test_icons_order(manifest: Manifest) -> None:
    for section in manifest.icons:
        prev_codepoint: int | None = None
        for icon in manifest.icons[section]:
            if prev_codepoint is not None:
                assert icon.code > prev_codepoint, f"icon {icon.name} is out-of-order"
            prev_codepoint = icon.code
