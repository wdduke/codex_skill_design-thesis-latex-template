# design-thesis-latex-template Codex Skill

This repository contains a Codex Skill named `design-thesis-latex-template`.

The skill helps Codex design and implement maintainable LaTeX thesis template projects for Chinese universities from official Word/DOCX writing specifications, Word templates, PDF/image samples, and provided assets. It focuses on evidence-based specification extraction, clean LaTeX class architecture, class option design, metadata interfaces, bibliography support, print/electronic and blind-review variants, independent cover handling, scan-page workflows, tests, and warning-free compilation.

## Repository Layout

```text
.
├─ README.md
└─ design-thesis-latex-template/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
   ├─ references/
   │  ├─ contents-and-order.md
   │  ├─ workflow.md
   │  ├─ evidence-and-spec-extraction.md
   │  ├─ project-structure.md
   │  ├─ engineering-architecture.md
   │  ├─ class-interface.md
   │  ├─ options-interface.md
   │  ├─ bibliography.md
   │  ├─ variants.md
   │  ├─ cover-pages.md
   │  ├─ scan-pages.md
   │  ├─ blind-review-safety.md
   │  ├─ visual-regression.md
   │  ├─ validation.md
   │  └─ release-and-packaging.md
   └─ scripts/
      └─ check_latex_log.py
```

## Who Should Use This Skill

Use this skill if you want Codex to repeatedly perform this kind of task:

1. You provide a Chinese university's official thesis writing specification, usually in Word/DOCX format.
2. You provide supporting files such as official Word templates, cover images, PDF notices, logos, fonts, PSD exports, old LaTeX templates, or scan-page examples.
3. You want Codex to produce a full LaTeX thesis template project rather than a single `.cls` file.
4. You want the result to be maintainable, GitHub-ready, documented, tested, and compiled without warnings or errors.

## Installation

Codex discovers personal skills from your local Codex skills directory.

On Windows, the usual directory is:

```powershell
C:\Users\<YourUserName>\.codex\skills
```

For the current Windows user, you can open it with:

```powershell
explorer "$env:USERPROFILE\.codex\skills"
```

On macOS or Linux, the usual directory is:

```bash
~/.codex/skills
```

If you use a custom `CODEX_HOME`, install the skill under:

```text
$CODEX_HOME/skills
```

## Install From GitHub On Windows

Open PowerShell and choose a temporary download location:

```powershell
cd "$env:USERPROFILE\Downloads"
git clone https://github.com/wdduke/codex_skill_design-thesis-latex-template.git
```

Create the Codex skills directory if it does not already exist:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
```

Copy the skill folder into the Codex skills directory:

```powershell
Copy-Item -Recurse -Force `
  "$env:USERPROFILE\Downloads\codex_skill_design-thesis-latex-template\design-thesis-latex-template" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

The final installed folder should be:

```text
C:\Users\<YourUserName>\.codex\skills\design-thesis-latex-template
```

Do not copy only `SKILL.md`; copy the whole `design-thesis-latex-template` folder so that `references/`, `scripts/`, and `agents/` are installed too.

## Install From GitHub On macOS Or Linux

Open a terminal:

```bash
cd ~/Downloads
git clone https://github.com/wdduke/codex_skill_design-thesis-latex-template.git
mkdir -p ~/.codex/skills
cp -R ~/Downloads/codex_skill_design-thesis-latex-template/design-thesis-latex-template ~/.codex/skills/
```

The final installed folder should be:

```text
~/.codex/skills/design-thesis-latex-template
```

## Updating An Existing Installation

If the skill is already installed, remove or replace only this skill folder:

Windows:

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
Copy-Item -Recurse -Force `
  "$env:USERPROFILE\Downloads\codex_skill_design-thesis-latex-template\design-thesis-latex-template" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

macOS/Linux:

```bash
rm -rf ~/.codex/skills/design-thesis-latex-template
cp -R ~/Downloads/codex_skill_design-thesis-latex-template/design-thesis-latex-template ~/.codex/skills/
```

Do not delete your entire `~/.codex/skills` folder. It may contain other skills.

## Verify The Skill Was Installed

Check that the required files exist.

Windows:

```powershell
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\SKILL.md"
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\references\contents-and-order.md"
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\scripts\check_latex_log.py"
```

Each command should print:

```text
True
```

macOS/Linux:

```bash
test -f ~/.codex/skills/design-thesis-latex-template/SKILL.md && echo OK
test -f ~/.codex/skills/design-thesis-latex-template/references/contents-and-order.md && echo OK
test -f ~/.codex/skills/design-thesis-latex-template/scripts/check_latex_log.py && echo OK
```

Each command should print `OK`.

You can also count files. The current skill contains 18 files:

Windows:

```powershell
(Get-ChildItem -Recurse -File "$env:USERPROFILE\.codex\skills\design-thesis-latex-template").Count
```

macOS/Linux:

```bash
find ~/.codex/skills/design-thesis-latex-template -type f | wc -l
```

## Validate The Skill Metadata

If you have Codex's built-in `skill-creator` system skill available locally, you can run its validator.

Windows example:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

Expected output:

```text
Skill is valid!
```

If you do not have that validator, the file-existence checks above are enough to confirm that the skill files were copied into the right place.

## How To Invoke The Skill

After installation, restart Codex or start a new Codex thread so the skill list is refreshed.

You can invoke it explicitly:

```text
Use $design-thesis-latex-template. I will provide a Chinese university thesis Word specification, official Word template files, cover images, and old LaTeX template references. Please design the full LaTeX template project structure, class interfaces, variants, bibliography system, cover/scanned-page strategy, validation plan, and then implement the project.
```

You can also invoke it naturally:

```text
请根据这所学校的学位论文撰写规范 Word 文件和官方模板素材，设计并实现一个完整的 LaTeX 学位论文模板项目。
```

For best results, provide:

- Official Word/DOCX writing specification.
- Official Word thesis template.
- Official PDF notices or interpretation documents.
- Cover samples, logos, PSD exports, or images.
- Any existing LaTeX template that should be used only as an engineering reference.
- Required output variants, such as electronic/print and normal/blind.
- Whether the result should be a public GitHub repository or only a private local template.

## Recommended Workflow When Using The Skill

The skill itself tells Codex to begin with:

```text
references/contents-and-order.md
```

The intended order is:

1. Read the skill map and production order.
2. Inventory all source files.
3. Extract school requirements into an evidence table.
4. Ask about missing or conflicting parameters.
5. Design the project structure.
6. Design the class options and metadata interface.
7. Design bibliography, variants, cover pages, scan pages, and blind-review rules.
8. Implement the LaTeX template project.
9. Compile all examples.
10. Eliminate warnings and errors.
11. Package or publish only when explicitly asked.

## Important Guardrails

This skill tells Codex not to:

- Overwrite existing skills unless the user explicitly agrees.
- Delete original materials.
- Automatically publish, tag, release, or push without explicit permission.
- Invent school-specific design parameters.
- Put all implementation logic into one huge `.cls` file.
- Treat a single successful compile as final success.

## Log Checking Utility

The skill includes:

```text
design-thesis-latex-template/scripts/check_latex_log.py
```

You can use it in a generated thesis template project to scan logs:

```powershell
python path\to\check_latex_log.py build\thesis.log build\thesis.blg
```

It reports LaTeX errors, package/class errors, warnings, overfull/underfull boxes, undefined references, undefined citations, and bibliography backend problems.

By default, warnings make the script exit non-zero because this skill's target standard is warning-free compilation.
