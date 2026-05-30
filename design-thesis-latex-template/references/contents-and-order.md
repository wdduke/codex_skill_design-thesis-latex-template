# Contents And Recommended Order

This skill contains a reusable production method for building Chinese university degree-thesis LaTeX templates from official Word/DOCX requirements and assets.

## What Is Included

- `SKILL.md`: trigger rules, core workflow, guardrails, and reference map.
- `references/workflow.md`: full project workflow from intake to delivery.
- `references/evidence-and-spec-extraction.md`: requirement extraction from Word, DOCX, PDF, image, and old templates.
- `references/project-structure.md`: recommended GitHub repository structure.
- `references/engineering-architecture.md`: LaTeX module boundaries and implementation strategy.
- `references/class-interface.md`: public document class and metadata commands.
- `references/options-interface.md`: class option design and validation rules.
- `references/bibliography.md`: reference/citation system.
- `references/variants.md`: output matrix and version strategy.
- `references/cover-pages.md`: inner cover, outer cover, spine, and special page design.
- `references/scan-pages.md`: signed pages and scan placeholders.
- `references/blind-review-safety.md`: anonymous-review safety checks.
- `references/visual-regression.md`: screenshot/PDF visual regression workflow.
- `references/validation.md`: final zero-warning compile standard.
- `references/release-and-packaging.md`: repository hygiene and packaging.
- `scripts/check_latex_log.py`: reusable log scanner.

## Recommended Production Order

1. Read `workflow.md` for the whole lifecycle.
2. Read `evidence-and-spec-extraction.md` and build the evidence table before coding.
3. Read `project-structure.md` and create the repository skeleton.
4. Read `engineering-architecture.md`, `class-interface.md`, and `options-interface.md` before implementing the class.
5. Implement the core class, metadata layer, fixed names, font system, and layout system.
6. Implement frontmatter, writing tools, floats, bibliography, and backmatter.
7. Read `variants.md`, then create the example matrix.
8. Read `cover-pages.md` and `scan-pages.md`, then implement independent outer cover and signed-page handling.
9. Read `blind-review-safety.md` and implement structured anonymization plus leak checks.
10. Read `visual-regression.md` and create visual baselines for fragile pages.
11. Read `validation.md`, run strict builds, and eliminate errors and warnings.
12. Read `release-and-packaging.md` before any user-approved publication or packaging.

## Stop Points

Stop and ask the user when a required school parameter is missing, when official files conflict, when an asset may be copyrighted or private, or when pushing/publishing would affect a remote repository.
