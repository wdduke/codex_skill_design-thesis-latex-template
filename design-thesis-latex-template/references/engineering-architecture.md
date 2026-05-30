# Engineering Architecture

## Thin Root Class

Keep the root class as a stable user entry point. It should add `src/` to the input path and load `schoolthesis-core.cls`. This keeps `\documentclass{schoolthesis}` simple while allowing maintainers to split implementation files.

## Suggested Module Responsibilities

- `*-core.cls`: option parsing, metadata keys, top-level conditionals, module loading, public core commands.
- `*-packages.sty`: base packages and package-order control.
- `*-fonts.cfg`: platform font detection and named font commands.
- `*.cfg`: fixed school names, labels, declaration text, blind placeholders.
- `*-layout.sty`: geometry, page styles, page lifecycle, front/main/back matter behavior.
- `*-frontmatter.sty`: inner covers, declaration pages, committee pages, abstracts, contents.
- `*-outercover.sty`: standalone outer cover and spine.
- `*-blind.sty`: anonymization helpers.
- `*-bib.sty`: bibliography backend abstraction.
- `*-floats.sty`: figures, tables, equations, captions, long tables, algorithms.
- `*-writing.sty`: footnotes, lists, denotation table, theorem-like environments.
- `*-backmatter.sty`: acknowledgements, achievements, appendix behavior.
- `*-hyperref.sty`: PDF metadata, bookmarks, link colors.
- `*-debug.sty`: optional grids, frames, layout logging.

## Implementation Principles

Use `expl3`/`l3keys2e` or a similarly structured key system for options and metadata. Unknown class options should error. Optional page data may warn, but required metadata should error before producing an invalid thesis.

Do not scatter school fixed text in page implementation files. Centralize it in the config module.

Do not duplicate normal and blind pages. Generate the same page from the same data path, and anonymize at field-output boundaries.

Use local page geometry for fragile cover/frontmatter pages and restore the main layout afterward.
