# Bibliography Design

## Default Strategy

For Chinese thesis templates, default to GB/T 7714. Prefer `biblatex-gb7714-2015` with `biber` for ordinary users when available. Provide a BibTeX backend option if the school, user, or TeX distribution requires `gbt7714-bibtex-style`.

## Unified User Interface

Expose one set of commands:

```tex
\SchoolAddBibResource{ref/refs.bib}
\printSchoolBibliography
```

The backend module should translate these to `\addbibresource`/`\printbibliography` or `\bibliography` as needed.

## Style Selection

- `bib-style=auto`: choose numeric for science/engineering and author-year for humanities when school rules support this.
- `bib-style=numeric`: sequential numeric citations.
- `bib-style=authoryear`: author-year citations.
- `bib-backend=biber`: use `biblatex`.
- `bib-backend=bibtex`: use `gbt7714`.

Do not load `natbib` or `cite` with the default biblatex backend. Detect conflicts and error.

## Data Guidance

Provide sample entries for journal articles, books, dissertations, conference papers, standards, patents, reports, and online resources. For BibTeX author-year styles with Chinese entries, suggest `key` fields for pinyin sorting when needed.

Do not automatically rewrite titles in ways that damage acronyms, chemical formulas, units, or proper nouns.
