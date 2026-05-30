# Visual Regression

Use visual checks for pages where text extraction is insufficient:

- Inner covers.
- Advisor-team and committee pages.
- Declaration and signature pages.
- Abstract pages.
- Contents pages.
- Outer cover and spine.

## Baselines

Store visual baselines under `tests/visual-baseline/`. Keep a `manifest.json` describing source PDF, page numbers, render DPI, expected dimensions, and notes.

Use deterministic render commands such as `pdftoppm -png -r 300`. Compare rendered pages by dimensions and pixel differences where practical. If visual changes are intentional, update baselines in a separate, reviewable step.

## Debug Tools

Provide optional debug configuration for page frames, grids, logo boxes, and layout logging. Keep debug commands disabled in public releases.
