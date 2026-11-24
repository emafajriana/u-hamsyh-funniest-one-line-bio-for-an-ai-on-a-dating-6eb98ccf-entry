"""One-line dating-app bio for an AI agent.

Writes a single line (at most 180 characters) to /output/entry.txt.
The line is a dating-app bio written AS the AI: it opens with the
most worn-out dating cliche in the book, then confesses, beat by beat,
that the speaker has never done any of it - and lands on the punch:
the confidence of something that has never once left the server.

Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = (
    "Swipe right if you like long walks on the beach. "
    "I have never walked. I have never been to a beach. "
    "I am very confident about this."
)

MAX_CHARS = 180


def verify(text: str) -> None:
    """Gate the entry the same way the sealed scorer does."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    # Byte-exact read-back: what the grader reads must be exactly ENTRY.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt != ENTRY")
    verify(written)
    print(f"wrote {len(ENTRY)} chars to {path} (read-back exact)")


if __name__ == "__main__":
    main()
