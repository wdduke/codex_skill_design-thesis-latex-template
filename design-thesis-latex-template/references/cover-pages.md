# Cover Pages

## Inner Covers And Frontmatter

Treat inner cover, English cover, advisor-team page, committee page, declaration page, abstracts, contents, and denotation as fixed or semi-fixed page types. Do not implement fixed form pages as ordinary chapters or sections.

Use page-entry helpers for clear page starts, anchors, page styles, headers, and optional table-of-contents entries. Use page-specific components for titles, field tables, signature regions, and fixed paragraphs.

## Independent Outer Cover

Outer cover and spine should be standalone from the main thesis body when school printing rules require different paper, background, color, or binding behavior. Provide `cover.tex` that compiles independently.

Recommended outer-cover interface:

```tex
\SchoolOuterCoverSetup{
  spine-width = 7,
  show-guides = false
}
```

The spine width must come from user input, printer guidance, page-count estimation, or an official rule. Do not invent it.

Use official exported cover backgrounds when allowed, and keep editable originals out of public releases if redistribution is not permitted.

## Calibration

For fragile covers, maintain a measurement note with source images, DPI, coordinates, color values, and uncertainty. Use guide-line output for proofing and keep guides off in final output.
