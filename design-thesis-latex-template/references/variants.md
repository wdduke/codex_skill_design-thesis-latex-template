# Variants

Design variants as option combinations, not copied projects.

## Required Matrix

At minimum, support and test:

- `media=electronic, review=normal`
- `media=electronic, review=blind`
- `media=print, review=normal`
- `media=print, review=blind`

Recommended additional coverage:

- `degree=doctor|master`
- `degree-type=academic|professional`
- `advisor-mode=single|associate|team`
- `discipline-type=science|humanities`

## Behavior

Electronic versions should avoid print-only blank pages and prioritize continuous PDF reading. Print versions should support double-sided output, open-right behavior, binding offset, and truly blank inserted pages.

Normal versions preserve identity fields. Blind versions hide or anonymize author, student ID, supervisor, advisor team, committee, acknowledgements, achievements, funding, project names, lab names, and PDF metadata according to school rules.

## Examples

Create small example documents under `examples/` for the main combinations. Keep examples realistic enough to exercise frontmatter, citations, floats, appendix, acknowledgements, achievements, and blind-review behavior.
