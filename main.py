"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

Writes one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output/entry.txt). The line is the vacuum's own deadpan excuse, in its
own robot voice: a staring contest it could not lose, because blinking
needs eyelids it was never given.
"""

import os

ENTRY = "The sock looked at me. I looked at the sock. One of us had to blink, and I don't have eyelids."

# Gate: one line, 1-200 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert 1 <= len(written) <= 200, "written entry out of range"


if __name__ == "__main__":
    main()
