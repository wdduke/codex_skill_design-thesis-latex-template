# Validation

The final goal is not merely "a PDF exists." The target is a maintainable template whose required examples compile without errors or warnings.

## Required Builds

Compile:

- Root `thesis.tex`.
- `examples/electronic-normal/thesis.tex`.
- `examples/electronic-blind/thesis.tex`.
- `examples/print-normal/thesis.tex`.
- `examples/print-blind/thesis.tex`.
- `examples/humanities-normal/thesis.tex` when humanities support exists.
- `cover.tex` when an outer cover is included.

Use the correct backend sequence:

```text
xelatex -> biber -> xelatex -> xelatex
```

or for BibTeX:

```text
xelatex -> bibtex -> xelatex -> xelatex
```

## Blocking Log Patterns

Treat these as failures unless explicitly documented and accepted:

- `LaTeX Error:`
- `Package .* Error:`
- `Class .* Error:`
- `Emergency stop`
- `Fatal error occurred`
- `Undefined control sequence`
- `Citation ... undefined`
- `Reference ... undefined`
- `There were undefined references`
- `Please (re)run Biber`
- `Biber error`
- `BibTeX error`
- `LaTeX Warning:`
- `Package .* Warning:`
- `Class .* Warning:`
- `Overfull \hbox`
- `Underfull \hbox`

Use `scripts/check_latex_log.py` for a reusable check.

## Acceptance

Report commands run, examples checked, warning count, failures, and any residual risks. Do not claim final success when warnings remain without explanation.
