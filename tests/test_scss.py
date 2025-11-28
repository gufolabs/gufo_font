# ---------------------------------------------------------------------
# Gufo Font: Test SCSS parser
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
from pathlib import Path

# Third-party modules
import pytest

# Gufo Font modules
from gufo.font.scss import ScssParser


def test_invalid_path() -> None:
    with pytest.raises(FileNotFoundError):
        ScssParser(Path("nonexistent-file"))


def test_dict_not_found() -> None:
    parser = ScssParser(Path("scss", "_colors.scss"))
    with pytest.raises(ValueError):
        parser.extract_dict("colorz")


def test_extract_dict() -> None:
    parser = ScssParser(Path("scss", "_colors.scss"))
    r = parser.extract_dict("colors")
    assert isinstance(r, dict)
    assert "black" in r
    assert r["black"] == "#000000"
    assert "asbestos" in r
    assert r["asbestos"] == "#7f8c8d"
