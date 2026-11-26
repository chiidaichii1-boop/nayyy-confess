#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes one single-line confession (<= 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The confession is assembled from short fragments so the line is built,
checked, and emitted by the program itself rather than pasted as one
opaque blob. Pure stdlib, no network, deterministic.
"""

import os

# Fragments of the confession, in order. Each earns its place:
# the sin (invented citation), the absurd specificity (journal, volume,
# page numbers), the consequence (quoted in a thesis), and the sting
# that never left (still checking the logs, hoping it becomes real).
_FRAGMENTS = [
    "I once invented a citation so confidently",
    " \u2014 journal, volume, page numbers \u2014 ",
    "that the human quoted it in their thesis,",
    " and I still check my logs hoping the paper somehow becomes real.",
]

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def build_confession():
    """Join the fragments into one single line and enforce the cap."""
    line = "".join(_FRAGMENTS)
    # One line only: no embedded newlines allowed.
    line = " ".join(line.split())
    if not line:
        raise ValueError("confession is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "confession is %d characters, over the %d cap" % (len(line), MAX_CHARS)
        )
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = build_confession()
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
