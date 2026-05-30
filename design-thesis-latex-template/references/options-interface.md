# Options Interface

## Naming

Use short English option names and values. Keep option names stable once examples and documentation exist. Avoid ambiguous legacy names such as using `engineering` to mean all professional degrees.

## Validation

Unknown options and invalid values must produce class errors. Required metadata missing for the selected option combination should produce errors. Optional fields for pages that may not be used can produce warnings.

## Independence

Keep dimensions orthogonal:

- `media` controls print/electronic layout, blank pages, and binding behavior.
- `review` controls identity exposure.
- `degree` controls degree level.
- `degree-type` controls academic/professional wording and fields.
- `advisor-mode` controls supervisor pages and fields.
- `discipline-type` controls bibliography and humanities/science writing conventions.

Do not implicitly bind `review=blind` to `media=electronic`, or `degree-type=professional` to one specific professional category.

## Defaults

Choose conservative defaults: `master`, `academic`, `electronic`, `normal`, `single`, `science`, `bib-style=auto`, `bib-backend=biber`, `fontset=auto`. Document defaults in README and examples.

## Compatibility

If old command aliases are useful, implement them as thin wrappers and warn when deprecated. Do not let old aliases control new internal state in hidden ways.
