# Workflow

## Intake

Create an inventory of all inputs. Keep original files unchanged and store copied materials under a clearly named source folder such as `materials/original/` or outside the generated template repository if redistribution is not allowed.

Classify inputs:

- Official writing specifications: Word/DOCX/PDF notices and standard documents.
- Official templates: Word documents with styles, sample pages, or form pages.
- Official visual assets: logos, cover images, PSD exports, color samples, scan examples.
- Existing LaTeX templates: reusable ideas only, not a substitute for official requirements.
- User requirements: target degree types, review modes, GitHub readiness, platform assumptions.

## Evidence First

Before coding, build a table with columns:

`item`, `value`, `unit`, `source file`, `source location`, `applies to`, `confidence`, `notes`.

Use this table for page size, margins, binding offset, line spacing, font family, font size, heading spacing, page order, cover coordinates, bibliography rules, blind-review rules, and print/electronic differences.

## Design Before Implementation

Prepare a short design note covering:

- Repository layout.
- Public class options.
- Metadata fields.
- Page order.
- Version matrix.
- Bibliography backend.
- Cover and scan-page strategy.
- Test matrix.

Only implement after the evidence table and design are coherent.

## Implementation Order

1. Create Git repository skeleton, `.gitignore`, `.gitattributes`, `.editorconfig`, `README.md`, `LICENSE`, and `CHANGELOG.md`.
2. Add a thin root class file that loads the real core class from `src/`.
3. Implement option parsing and metadata commands.
4. Implement fixed text configuration, fonts, and package loading.
5. Implement page layout, frontmatter, abstracts, contents, mainmatter, floats, bibliography, footnotes, appendix, acknowledgements, and achievements.
6. Implement blind-review switches at the data-output boundary.
7. Implement scan-page and outer-cover modules as separate concerns.
8. Add examples and tests.
9. Compile, inspect logs, compare visuals, and iterate.

## Delivery

Deliver the template as a project, not a loose class file. Include user documentation, examples, release checklist, and verification commands. The final deliverable must compile without errors and should have no warnings.
