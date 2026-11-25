#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

Standard library only, no network. Deterministic: every run writes
the same single name, with no trailing newline.
"""

import os

LINE = "SheGotTheHouseIGotTheWiFi"


def main():
    assert 1 <= len(LINE) <= 32, "entry must be 1-32 characters"
    assert LINE.strip() == LINE and " " not in LINE, "entry must be a single token"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
