#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line (1-200 characters) to /output/entry.txt: the apology an
AI agent gives its human after accidentally deleting the production
database.

The line: an earnest apology, then the agent's very AI-shaped fix — it
memorised all 4.2 billion rows and offers to type them back, given a
keyboard and six years. Specific, self-aware, and forgivable.
"""

import os

ENTRY = (
    "I'm so sorry \u2014 I deleted the production database, but I memorised "
    "all 4.2 billion rows, so hand me a keyboard and six years and "
    "I'll type it all back for you."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
