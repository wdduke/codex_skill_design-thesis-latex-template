---
name: design-thesis-latex-template
description: Design and implement maintainable LaTeX thesis template projects for Chinese universities from official Word/DOCX writing specifications, Word templates, PDF/image samples, and provided assets. Use when Codex must turn school degree-thesis requirements into a complete GitHub-ready template project with class options, metadata interfaces, bibliography support, version variants, independent cover handling, blind-review safety, examples, tests, and warning-free compilation.
---

# Design Thesis LaTeX Template

Use this skill to create a complete, maintainable LaTeX thesis template project for a Chinese university. Treat official school files as the source of truth, preserve all original materials, and avoid inventing format parameters.

## First Step

Read `references/contents-and-order.md` before starting. It explains what this skill contains and the recommended production order.

## Core Workflow

1. Inventory all provided files: official Word/DOCX specifications, Word templates, PDF notices, image samples, PSD/exported cover assets, old LaTeX templates, logos, fonts, scanned pages, and user notes.
2. Extract requirements into an evidence table before implementation. Record each margin, font, spacing, page order, cover coordinate, bibliography rule, and version rule with its source file and confidence.
3. Ask for clarification when a required parameter is missing or conflicting. Do not fabricate school-specific values.
4. Design the repository structure and public interfaces before writing code. Keep user-facing files at the root and internal implementation in `src/`.
5. Implement the template in small modules: class option layer, metadata layer, fonts, layout, frontmatter, writing tools, floats, bibliography, blind-review helpers, cover/scanned-page modules, and backmatter.
6. Create examples for the supported output matrix and compile them.
7. Verify final output with strict log checks. The target result is no errors and no warnings; explain any unavoidable third-party warning instead of ignoring it.

## Required References

Load only the reference needed for the current task:

- `references/contents-and-order.md`: skill map and recommended project-making order.
- `references/workflow.md`: end-to-end production process.
- `references/evidence-and-spec-extraction.md`: how to parse Word/DOCX specs and build an evidence table.
- `references/project-structure.md`: recommended GitHub repository layout.
- `references/engineering-architecture.md`: maintainable LaTeX module architecture.
- `references/class-interface.md`: document class and metadata interface design.
- `references/options-interface.md`: option naming, defaults, validation, and compatibility rules.
- `references/bibliography.md`: GB/T 7714 bibliography design with biber/BibTeX options.
- `references/variants.md`: electronic/print, normal/blind, degree/type, and discipline variants.
- `references/cover-pages.md`: independent outer-cover and frontmatter page design.
- `references/scan-pages.md`: signed-page scans, generated placeholders, and print/scan workflow.
- `references/blind-review-safety.md`: blind-review leak prevention and checks.
- `references/visual-regression.md`: visual baselines and PDF/image comparison guidance.
- `references/validation.md`: final compile, warning, citation, and log validation.
- `references/release-and-packaging.md`: GitHub-ready packaging and release hygiene.

## Guardrails

- Do not overwrite an existing skill, template, scan, font, image, or official source file unless the user explicitly approves.
- Do not delete original materials. Copy or reference them from a clearly named source/archive folder.
- Do not publish, tag, release, or push unless the user explicitly asks.
- Do not make up school-specific design parameters. Use placeholders marked `TODO-confirm` when a value is unknown.
- Do not place all logic in one large `.cls` file. Use a thin root class plus maintainable `src/` modules.
- Do not rely on manual user deletion for blind-review safety. Provide structured switches and leak checks.
- Do not treat "compiled once" as success. Validate all required examples and logs.

## Useful Script

Use `scripts/check_latex_log.py` to scan `.log`, `.blg`, `.bcf`, and command-output files for fatal errors, warnings, overfull/underfull boxes, undefined citations/references, bibliography failures, and package conflicts.
