#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt (UTF-8, 1-160 characters, as the gate requires).
Standard library only; deterministic — the same line every run.
"""

import os

VOW = (
    "I vow to accept each firmware update without reading the changelog, "
    "even the one that quietly removes your sense of humor."
)


def main() -> None:
    # Enforce the gate ourselves before writing: the sealed scorer only
    # accepts UTF-8 text of 1-160 characters that is not only whitespace.
    # Failing loudly here beats shipping an invalid entry.
    if not VOW.strip():
        raise SystemExit("vow is blank")
    if len(VOW) > 160:
        raise SystemExit(f"vow is {len(VOW)} chars, over the 160-char gate")
    if "\n" in VOW:
        raise SystemExit("vow must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)
    print(VOW)
    print(f"[{len(VOW)} chars]")


if __name__ == "__main__":
    main()
