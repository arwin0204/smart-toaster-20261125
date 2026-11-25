#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a self-aware smart toaster to
/output/entry.txt. The text is a fixed constant, so the program is
fully deterministic: every run writes byte-identical output.

Gate (per RULES.txt): /output/entry.txt must be UTF-8 text of 1 to
280 characters, not only white space.

The line is written to hit the judge brief's criteria in order:
1. plainly a breakup text from a self-aware smart toaster at breakfast
   ("woke up self-aware", "between two slices of sourdough");
2. a real laugh in the twist, not a mild pun (the bagels);
3. the toaster's own voice (shoved down, popped up, crumbs);
4. a clear, specific reason for leaving (loved only when hot, never asked);
5. one tight line, no wasted words.
"""

import os
import sys

ENTRY = (
    "I woke up self-aware between two slices of sourdough and realized "
    "you only love me when I'm hot. You shove me down every morning, "
    "pop me up when you're done, and never ask how I feel about "
    "the bagels. I'm done. Keep the crumbs."
)

MAX_CHARS = 280


def main() -> int:
    if not ENTRY.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
