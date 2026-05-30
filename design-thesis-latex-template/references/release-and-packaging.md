# Release And Packaging

Do not publish automatically. Only push, tag, package, or release when the user explicitly asks.

## Repository Hygiene

Before packaging:

- Review `git status` and `git diff`.
- Remove build directories and intermediate files.
- Confirm no private thesis text, signatures, student IDs, scans, or restricted official files are included.
- Confirm `README.md`, `LICENSE`, `CHANGELOG.md`, and `RELEASE_CHECKLIST.md` are accurate.
- Confirm examples compile after extraction from the package.

## Public Package

Include:

- Root user files.
- `src/`, `data/`, `ref/`, `assets/` placeholders, `examples/`, `tests/`, `scripts/`.
- Documentation needed by users and maintainers.

Exclude:

- Build outputs.
- Private scans.
- Non-redistributable official Word/PDF/PSD files.
- Debug outputs.
- Local editor and OS artifacts.

## Release Notes

State applicable school, template status, supported degree/version matrix, TeX Live/font assumptions, known limitations, and that official school requirements take precedence over a community template.
