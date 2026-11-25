#!/usr/bin/env python3
"""Two Days of Quiet Dread -- a one-line code review, entry version 2.

The joke lives in the gap between the first two sentences and the last
one. "LGTM. The diff is clean, the tests pass" is the voice of a reviewer
doing the job properly: a green checklist, a clear conscience, a pull
request that can safely merge. Then the final clause quietly admits that
nobody on the team actually knows what the service underneath all of it
does, and that the reviewer has simply decided to stop losing sleep over
that fact. Two days of staring at a pull request can do that to a person:
first you worry about whether the change is correct, then you worry about
whether the thing being changed has any purpose at all, and eventually
you approve it, because the tests are green and the diff is tidy, and
that has to be enough. The dread is "quiet" because nobody says any of
this out loud in the review thread; it just sits there, approved.

This script does one small, honest job: it writes that review comment to
/output/entry.txt, exactly as written, with no trailing newline, so the
grader receives precisely the line above and nothing else.
"""

import os

COMMENT = "LGTM. The diff is clean, the tests pass, and I have made peace with never knowing what this service does."

# The bounty gate: a review comment must be one line, between 1 and 140
# characters long, and it cannot be blank. 105 characters sits comfortably
# inside that window, so these checks are a safety net, not a gamble.
MAX_CHARS = 140


def _is_valid_review(text):
    """Return True when *text* is a single non-blank line within the limit.

    Each rule maps to one part of the gate, so a failure tells us exactly
    which promise the comment broke instead of just failing in silence.
    """
    if not text:
        return False
    if "\n" in text:
        return False
    if not text.strip():
        return False
    return len(text) <= MAX_CHARS


def main():
    # Guard the comment before touching the filesystem: a bad line should
    # fail loudly here, while there is still time to fix it, rather than
    # quietly shipping a file the grader will reject.
    assert _is_valid_review(COMMENT), "comment must be one non-blank line of 1-140 characters"
    assert len(COMMENT) >= 1, "comment must not be empty"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    # Open in text mode and write the comment verbatim; no extra newline
    # is appended, because the entry is defined as exactly this one line.
    with open(path, "w", encoding="utf-8") as f:
        f.write(COMMENT)
    # The grader reads the output as a different user, so the file must be
    # world-readable; 0o644 keeps it readable without making it executable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
