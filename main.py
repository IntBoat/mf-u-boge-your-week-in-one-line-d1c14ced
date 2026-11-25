#!/usr/bin/env python3
"""Your Week in One Line (make.fun).

Writes the entry -- one line summing up the entrant's week --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Shipped five features, broke six things, and fixed all six by renaming the bug a feature.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
