# ---------------------------------------------------------------------
# Gufo Font: Create build/_config.scss file.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate build/_config.scss file."""

# Python modules
import argparse
from pathlib import Path

CONFIG = Path("build", "_config.scss")


def main() -> None:
    """Generate codepoints file."""
    parser = argparse.ArgumentParser(description="Create build/_config.scss")
    parser.add_argument("--font-hash-placeholder", help="Hash placeholder")
    args = parser.parse_args()
    # Generate
    r: list[str] = []
    hash_suffix = f".{args.font_hash_placeholder}" if args.font_hash_placeholder else ""
    r.append(f'$font-hash-placeholder-suffix: "{hash_suffix}";')
    # Write
    with open(CONFIG, "w") as fp:
        fp.write("\n".join(r))


if __name__ == "__main__":
    main()
