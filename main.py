#!/usr/bin/env python3
"""Crypto Trading Joke — a one-line entry for the make.fun bounty.

The program writes a single joke about crypto and trading life to
/output/entry.txt. The gate: UTF-8 text, 1 to 200 characters, not only
whitespace, one line. The judge reads entries two at a time and picks
the funniest, weighing a clear setup and turn, a real laugh, and a
detail that feels true to trading life.

The joke: buy the coin the group chat will not stop hyping, then watch
that same group chat go quiet. The hype-to-silence arc is the exact
shape of a bad trade, told in one breath.
"""

import sys
from pathlib import Path

# The entry, written fresh for this bounty: setup, then the turn.
ENTRY = (
    "I buy the coin my group chat won't stop hyping, "
    "then I watch the group chat go quiet."
)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def normalize(line: str) -> str:
    """Collapse stray whitespace and strip the line, keeping one line."""
    return " ".join(line.split())


def validate(line: str) -> list[str]:
    """Return a list of gate violations; empty means the line is valid."""
    problems: list[str] = []
    if not line.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in line.strip():
        problems.append("entry must be a single line")
    if len(line) > MAX_CHARS:
        problems.append(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - defensive
        problems.append(f"entry is not valid UTF-8 text: {exc}")
    return problems


def render_entry() -> str:
    """Return the final entry text, normalized and validated."""
    line = normalize(ENTRY)
    problems = validate(line)
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))
    return line


def describe() -> str:
    """One line on why the joke lands: setup, turn, and true detail."""
    return (
        "Setup: buying the coin the group chat hypes. "
        "Turn: that same group chat goes quiet. "
        "True detail: the group chat, where every bad trade begins."
    )


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the entry to path and return the path written."""
    line = render_entry()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> int:
    """Write the entry and print it, so the run is visible."""
    args = argv if argv is not None else sys.argv[1:]
    out = Path(args[0]) if args else OUTPUT_PATH
    path = write_entry(out)
    print(render_entry())
    print(describe())
    print(f"wrote {len(render_entry())} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
