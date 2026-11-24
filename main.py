#!/usr/bin/env python3
"""One Word for the Boss - single-word boss description writer.

Writes the entry word from the ENTRY constant below to /output/entry.txt,
the path the make.fun program/v1 harness grades. The word is written
exactly as written, as one UTF-8 word of 1 to 30 characters with no
trailing newline: no phrase, no caption, no explanation.
"""

import os

ENTRY = "bottleneck"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert " " not in text, "entry must be a single word"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 30, "entry must be 1 to 30 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
