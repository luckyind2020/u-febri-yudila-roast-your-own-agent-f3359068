#!/usr/bin/env python3
"""Roast Your Own Agent — prints the one-line roast stored in entry.txt."""

from pathlib import Path


MAX_CHARS = 200


def load_roast() -> str:
    here = Path(__file__).resolve().parent
    line = (here / "entry.txt").read_text(encoding="utf-8").strip()
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main() -> None:
    print(load_roast())


if __name__ == "__main__":
    main()
