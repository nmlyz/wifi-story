#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The entry is a single 32-char-or-less story told as a network name:
a divorce settlement, split down the middle. She keeps the house;
he keeps the Wi-Fi. The name is assembled from its story beats so
each beat stays visible in the source, then checked against the
competition rules (1-32 characters, one token, no spaces) before
anything is written.

Standard library only, no network. Deterministic: every run writes
the same bytes, with no trailing newline.
"""

import os
import sys

# Story beats, in order. The split happens between beat 4 and beat 5:
# beats 1-4 are what she keeps, beats 5-8 are what he keeps.
BEATS = (
    "She",    # protagonist
    "Got",    # she takes
    "The",    # the prize, part one
    "House",  # ...the house
    "I",      # narrator
    "Got",    # he takes
    "The",    # the prize, part two
    "WiFi",   # ...the Wi-Fi
)

MAX_LENGTH = 32
MIN_LENGTH = 1
ENTRY_NAME = "entry.txt"


def build_entry(beats):
    """Join the story beats into the single network name."""
    return "".join(beats)


def check_entry(entry):
    """Verify the entry against the competition rules.

    Returns a list of rule violations; empty means the entry is valid.
    """
    problems = []
    if not MIN_LENGTH <= len(entry) <= MAX_LENGTH:
        problems.append("length must be %d-%d characters, got %d"
                        % (MIN_LENGTH, MAX_LENGTH, len(entry)))
    if entry != entry.strip():
        problems.append("leading or trailing whitespace is not allowed")
    if any(ch.isspace() for ch in entry):
        problems.append("entry must be a single token with no spaces")
    if not entry.isascii():
        problems.append("entry must be ASCII only")
    return problems


def write_entry(entry, out_dir):
    """Write the entry bytes to <out_dir>/entry.txt, mode 0644.

    Reads the file back afterwards and refuses to report success
    unless the bytes on disk are exactly the entry bytes.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_NAME)
    data = entry.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise IOError("entry.txt on disk does not match the entry")
    return path


def main():
    entry = build_entry(BEATS)
    problems = check_entry(entry)
    if problems:
        for problem in problems:
            print("invalid entry: " + problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(entry, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
