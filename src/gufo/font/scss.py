# ---------------------------------------------------------------------
# Gufo Font: SCSS Parser
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
import re
from pathlib import Path


class ScssParser(object):
    """Scss file parsing."""

    def __init__(self, path: Path) -> None:
        if not path.exists():
            msg = f"File {path} is not exists"
            raise FileNotFoundError(msg)
        self._path = path
        self._data: str | None = None

    def _read(self) -> None:
        """Read file, when necessary."""
        if not self._data:
            self._data = self._path.read_text()

    def extract_dict(self, name: str) -> dict[str, str]:
        """
        Extract named dict.

        Args:
            name: Dict name, without `$` prefix.
        """
        self._read()
        r = {}
        match = re.search(
            rf"^\${name}\s*:\s*\((.+?)\);", self._data, re.MULTILINE | re.DOTALL
        )
        if not match:
            msg = f"Variable ${name} is not found"
            raise ValueError(msg)
        for line in match.group(1).splitlines():
            line = line.strip().rstrip(",")
            parts = line.split(":", 1)
            if len(parts) == 2:
                r[parts[0].strip()] = parts[1].strip()
        return r
