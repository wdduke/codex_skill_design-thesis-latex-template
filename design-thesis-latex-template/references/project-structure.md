# Project Structure

Use a GitHub-ready repository layout similar to:

```text
schoolthesis/
  .github/
  .editorconfig
  .gitattributes
  .gitignore
  LICENSE
  README.md
  CHANGELOG.md
  RELEASE_CHECKLIST.md
  schoolthesis.cls
  thesis.tex
  cover.tex
  metadata.tex
  clean-intermediates.bat
  src/
    schoolthesis-core.cls
    schoolthesis-packages.sty
    schoolthesis-fonts.cfg
    schoolthesis.cfg
    schoolthesis-layout.sty
    schoolthesis-frontmatter.sty
    schoolthesis-outercover.sty
    schoolthesis-blind.sty
    schoolthesis-bib.sty
    schoolthesis-floats.sty
    schoolthesis-writing.sty
    schoolthesis-backmatter.sty
    schoolthesis-hyperref.sty
    schoolthesis-debug.sty
  data/
    abstract-cn.tex
    abstract-en.tex
    denotation.tex
    chap01.tex
    chap02.tex
    appendix.tex
    acknowledgements.tex
    achievements.tex
  ref/
    refs.bib
  assets/
    cover/
    fonts/
    scan/
  examples/
    electronic-normal/
    electronic-blind/
    print-normal/
    print-blind/
    humanities-normal/
  tests/
    inner-cover/
    outer-cover/
    visual-baseline/
  scripts/
    check-phase1.ps1
    check-blind-leaks.ps1
    check-frontmatter-visual.ps1
    estimate-outercover-spine.ps1
    prepare-release.ps1
```

Keep ordinary users in root files, `data/`, `ref/`, `assets/scan/`, and `examples/`. Keep maintainers in `src/`, `tests/`, and `scripts/`.

Do not commit build directories, generated `.aux/.log/.xdv/.bbl/.bcf/.run.xml` files, private scans, real signatures, student IDs, or non-redistributable official documents.
