#!/usr/bin/env python3
"""Everyday Wonder entry: one sentence about a small moment of wonder."""

import os

ENTRY = "The staircase creaked under my step in exactly the spot it always does, and for a second I felt expected."

MAX_CHARS = 200


def validate_entry(text):
    """Gate: UTF-8 text of 1 to 200 characters, a single sentence, no trailing newline."""
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    return text


def main():
    text = validate_entry(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"


if __name__ == "__main__":
    main()
