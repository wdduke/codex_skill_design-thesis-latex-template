#!/usr/bin/env python3
"""Scan LaTeX-related logs for blocking errors and warnings."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = [
    ("error", re.compile(r"LaTeX Error:|Package .* Error:|Class .* Error:")),
    ("error", re.compile(r"Emergency stop|Fatal error occurred|Undefined control sequence")),
    ("error", re.compile(r"Citation .* undefined|Reference .* undefined|There were undefined references")),
    ("error", re.compile(r"Please \(re\)run Biber|Biber error|BibTeX error", re.IGNORECASE)),
    ("warning", re.compile(r"LaTeX Warning:|Package .* Warning:|Class .* Warning:")),
    ("warning", re.compile(r"Overfull \\hbox|Underfull \\hbox|Table width is too small")),
]


def scan_file(path: Path) -> list[tuple[str, int, str]]:
    findings: list[tuple[str, int, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return [("error", 0, f"cannot read {path}: {exc}")]

    for lineno, line in enumerate(text.splitlines(), 1):
        for level, pattern in PATTERNS:
            if pattern.search(line):
                findings.append((level, lineno, line.strip()))
                break
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Log, blg, bcf, or output files to scan")
    parser.add_argument("--allow-warnings", action="store_true", help="Exit 0 when only warnings are found")
    args = parser.parse_args()

    total_errors = 0
    total_warnings = 0
    for path in args.paths:
        findings = scan_file(path)
        if findings:
            print(f"{path}:")
        for level, lineno, message in findings:
            if level == "error":
                total_errors += 1
            else:
                total_warnings += 1
            location = f"{lineno}" if lineno else "-"
            print(f"  {level.upper():7} line {location}: {message}")

    print(f"Summary: errors={total_errors} warnings={total_warnings}")
    if total_errors:
        return 1
    if total_warnings and not args.allow_warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
