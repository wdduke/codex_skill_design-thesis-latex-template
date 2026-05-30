# Class Interface

## Document Class

Use stable, explicit class options:

```tex
\documentclass[
  degree=master,
  degree-type=academic,
  media=electronic,
  review=normal,
  advisor-mode=single,
  discipline-type=science,
  bib-style=auto,
  bib-backend=biber,
  fontset=auto
]{schoolthesis}
```

Recommended dimensions:

- `degree=doctor|master|bachelor` only when official requirements exist.
- `degree-type=academic|professional`.
- `media=electronic|print`.
- `review=normal|blind`.
- `advisor-mode=single|associate|team`.
- `discipline-type=science|humanities`.
- `bib-style=auto|numeric|authoryear`.
- `bib-backend=biber|bibtex`.

## Metadata

Use a single setup command:

```tex
\SchoolThesisSetup{
  title-cn = {...},
  title-en = {...},
  author-cn = {...},
  author-en = {...},
  student-id = {...},
  school-cn = {...},
  school-en = {...},
  supervisor-cn = {...},
  supervisor-title-cn = {...},
  supervisor-en = {...},
  discipline-cn = {...},
  discipline-en = {...},
  professional-category-cn = {...},
  professional-category-en = {...},
  professional-field-cn = {...},
  professional-field-en = {...},
  defense-date-cn = {...},
  defense-date-en = {...},
  thesis-type-cn = {...},
  thesis-type-en = {...},
  keywords-cn = {...},
  keywords-en = {...}
}
```

Use separate commands for list-like data:

```tex
\SchoolCommitteeChair{name}{title}{affiliation}
\SchoolCommitteeMember{name}{title}{affiliation}
\SchoolAdvisorTeamLeader{name}{discipline}{title}
\SchoolAdvisorTeamMember{name}{discipline}{title}
```

## Page Commands

Prefer explicit page commands in the main document:

```tex
\makecover
\makeadvisorteampage
\makecommitteepage
\makecopyrightpage
\frontmatter
\mainmatter
\printSchoolBibliography
\appendix
\backmatter
```

The template, not the user, should decide whether a command outputs, skips, scans, or anonymizes the page under the selected options.
