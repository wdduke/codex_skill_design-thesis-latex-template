# Evidence And Specification Extraction

## DOCX/Word Analysis

Prefer structured extraction when possible. Inspect:

- Page setup: paper size, margins, gutter/binding offset, header/footer distance.
- Styles: Normal, title styles, heading levels, caption styles, footnotes, bibliography, table styles.
- Paragraph properties: font, size, line spacing, before/after spacing, indentation, alignment.
- Section breaks: different headers/footers, page numbering, odd/even pages.
- Tables and forms: fixed rows, merged cells, border widths, signature regions.
- Embedded images: logos, cover backgrounds, seals, example scans.

When Word style definitions and actual sample page appearance differ, record both and ask the user which is authoritative unless the official specification clearly resolves it.

## PDF/Image Samples

Use PDF text extraction, screenshots, and pixel measurements for fragile pages such as covers, declaration pages, committee pages, and title pages. Record DPI, measurement method, and uncertainty.

Do not infer exact values from a low-resolution screenshot when the official Word/PDF source can provide the value.

## Existing LaTeX Templates

Use old templates as engineering references only:

- Reusable package choices.
- User-facing command names.
- Known school-specific page order.
- Compatibility ideas.

Do not copy stale fixed text or old dimensions without checking current official files.

## Evidence Table Rules

Every school-specific decision should be traceable. If unknown, mark the value as `TODO-confirm` and make the template fail loudly or document the placeholder clearly. Never silently invent margins, colors, fonts, line spacing, cover coordinates, bibliography variants, or blind-review requirements.
