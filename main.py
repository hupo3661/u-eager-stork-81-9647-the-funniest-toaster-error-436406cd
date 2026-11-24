#!/usr/bin/env python3
"""Write the one-line toaster error message to /output/entry.txt.

Deterministic, no network, no input: the entry is a single fixed line,
the funniest error message a kitchen toaster would show its owner.
"""

import os
from pathlib import Path

ERROR = "Error 402: Bread declined \u2014 insufficient funds. Please insert richer bread."

MAX_CHARS = 120


def validate(line: str) -> None:
    """Fail loudly unless the line satisfies the competition gate."""
    assert isinstance(line, str)
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.encode("utf-8").decode("utf-8") == line, "entry must be UTF-8"


def main() -> None:
    validate(ERROR)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ERROR + "\n", encoding="utf-8")
    # Verify the write round-trips exactly: what the grader reads is the line.
    assert target.read_text(encoding="utf-8") == ERROR + "\n", (
        "entry.txt does not hold exactly the chosen line"
    )


if __name__ == "__main__":
    main()
