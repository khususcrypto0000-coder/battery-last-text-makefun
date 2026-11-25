"""battery-last-text-makefun: write the battery's last text to /output/entry.txt.

Stdlib only. Run: python3 main.py
"""

import os
import sys

ENTRY = (
    "hey charger, before i die at 1%: i'm not your battery. "
    "yours died at lunch. i've been the earbuds' battery all day, "
    "living in a case that actually closes. "
    "you two were never even plugged in. bye."
)


def main():
    # Gate: 1-200 chars, single line, not whitespace-only.
    assert 1 <= len(ENTRY) <= 200, f"ENTRY is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "ENTRY must be a single line"
    assert ENTRY.strip(), "ENTRY must not be whitespace-only"
    out_dir = "/output"
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out_path, "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "read-back bytes differ from ENTRY"
    print(f"Wrote {out_path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
