#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun bounty entry (v2).

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread.
"""

import os

COMMENT = "LGTM. The diff is clean, the tests pass, and I have made peace with never knowing what this service does."

def main():
    # Mirror the gate: one line, 1-140 chars, not only whitespace.
    assert 1 <= len(COMMENT) <= 140, "comment must be 1-140 characters"
    assert "\n" not in COMMENT, "comment must be a single line"
    assert COMMENT.strip(), "comment must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(COMMENT)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
