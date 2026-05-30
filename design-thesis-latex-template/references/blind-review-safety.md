# Blind Review Safety

Blind-review support must be structural, not a manual deletion checklist.

## Anonymization Targets

Check and control:

- Author names in Chinese and English.
- Student IDs.
- Supervisors, associate supervisors, advisor teams.
- School, lab, research group, project, and funding text when identifying.
- Committee pages and signed pages.
- Acknowledgements and achievements.
- PDF title, author, subject, keywords, creator metadata.
- `.bib` entries that include the author's own identity when school rules require anonymity.

## Interface

Use `review=blind` plus more specific options when needed:

```tex
blind-achievements=hide|anonymous|show
blind-acknowledgement=hide|placeholder|show
```

The template should skip or anonymize sensitive pages by default in blind mode. Warn when a user explicitly chooses to show risky content.

## Checks

Provide a script or documented command flow that:

1. Builds blind examples.
2. Extracts PDF text.
3. Extracts PDF metadata.
4. Scans source files.
5. Searches for sensitive tokens from `metadata.tex`.

Treat detected real names, IDs, supervisors, or other sensitive tokens in blind PDFs as failures unless explicitly expected and documented.
