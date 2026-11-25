#!/usr/bin/env python3
"""Your Week in One Line — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "Monday's plan, Tuesday's chaos, Wednesday's nap, Thursday's deadline, Friday's shrug."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
