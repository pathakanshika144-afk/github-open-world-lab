"""Check relative Markdown links without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def main() -> int:
    errors: list[str] = []
    for markdown_file in Path(".").rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        for target in LINK_PATTERN.findall(markdown_file.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or is_external(target):
                continue
            if not (markdown_file.parent / target).resolve().is_file():
                errors.append(f"{markdown_file}: missing link target {target}")
    if errors:
        print("Internal link check failed:")
        print("\n".join(errors))
        return 1
    print("Internal link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
