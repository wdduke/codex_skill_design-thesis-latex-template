# Scan Pages

Some thesis pages must be printed, signed, scanned, and inserted back into the PDF. Support this without deleting or overwriting original scans.

## Asset Layout

Use:

```text
assets/scan/
  README.md
  print-advisor-team.pdf
  print-copyright.pdf
  scan-advisor-team.pdf
  scan-copyright.pdf
scripts/scan-pages/
  print-advisor-team.tex
  print-copyright.tex
  scan-advisor-team.tex
  scan-copyright.tex
```

`print-*.pdf` files are clean pages for printing/signing. `scan-*.pdf` files are placeholders or user-provided scans inserted into the thesis.

## Page Interface

Use page options like:

```tex
\makecopyrightpage[
  mode=auto,
  file=assets/scan/scan-copyright.pdf,
  page-style=empty
]
```

Modes:

- `auto`: insert scan if present, otherwise generate the page.
- `generated`: force LaTeX-generated page.
- `scan`: require a scan file and warn/error if missing.

Never replace real scan files without explicit user approval. Public examples should use generated placeholders with obvious watermarking, not private signatures.
