"""Two Days of Quiet Dread - make.fun entry.

Writes one single-line code review comment to /output/entry.txt:
it approves a pull request while carrying quiet existential dread.

Pure stdlib, no network, fully deterministic: the output is always
the same single line.
"""

import os

# One line, approves the PR, quiet dread by understatement.
# Flat tone, reads like a tired engineer pasting it before approve.
# Revised: the two-day stare is now in the line itself, and the will
# metaphor keeps the fresh turn — the laugh comes from the dread
# itself, not from a joke bolted on.
COMMENT = (
    "LGTM. I stared at this for two days, understood none of it, "
    "and now I approve it the way one approves a will: quietly, "
    "and far too late."
)

DST = "/output/entry.txt"


def main():
    text = COMMENT.strip()
    if not text:
        raise ValueError("comment is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("comment must be a single line")
    if len(text) > 140:
        raise ValueError("comment exceeds 140 characters: %d" % len(text))
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
