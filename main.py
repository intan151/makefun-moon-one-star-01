#!/usr/bin/env python3
"""The Moon Gets One Star - one-star review of the Moon.

Writes the entry deterministically to /output/entry.txt.

The joke: the Moon follows you everywhere (parallax) - a specific,
surprising grievance, not the obvious craters/cheese/brightness jokes.
It reads like a real one-star review: a rating, a complaint, an
escalating punchline.
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 Follows me everywhere. "
    "I moved twice. Still there. "
    "No refund, no restraining order, no stars."
)


def main():
    # Self-check gate: the written entry must be byte-identical to ENTRY
    # and pass the competition gate (UTF-8, 1-120 chars, not only whitespace).
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
