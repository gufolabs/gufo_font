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
    if args.font_hash_placeholder:
        r.append(f'$font-hash-placeholder: "{args.font_hash_placeholder}";')
    # Write
    with open(CONFIG, "w") as fp:
        fp.write("\n".join(r))


if __name__ == "__main__":
    main()
