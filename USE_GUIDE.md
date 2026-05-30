# design-thesis-latex-template 使用指南

本文档说明如何一步一步安装、验证和使用 `design-thesis-latex-template` 这个 Codex Skill。

## 1. 准备环境

你需要：

- 已安装 Codex。
- 能访问本机文件系统。
- 如果从 GitHub 下载，需要本机安装 Git。
- 如果后续要让 Codex 编译 LaTeX 模板，需要安装 TeX Live、MiKTeX 或其他可用的 LaTeX 发行版。

这个 Skill 本身不包含 LaTeX 发行版，也不会自动安装 TeX Live。

## 2. 下载 Skill 仓库

Windows PowerShell：

```powershell
cd "$env:USERPROFILE\Downloads"
git clone https://github.com/wdduke/codex_skill_design-thesis-latex-template.git
```

macOS/Linux：

```bash
cd ~/Downloads
git clone https://github.com/wdduke/codex_skill_design-thesis-latex-template.git
```

下载后应看到这样的目录：

```text
codex_skill_design-thesis-latex-template/
  README.md
  USE_GUIDE.md
  design-thesis-latex-template/
    SKILL.md
    agents/
    references/
    scripts/
```

## 3. 安装到 Codex Skills 目录

### Windows

创建 Skills 目录：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
```

复制 Skill：

```powershell
Copy-Item -Recurse -Force `
  "$env:USERPROFILE\Downloads\codex_skill_design-thesis-latex-template\design-thesis-latex-template" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

### macOS/Linux

```bash
mkdir -p ~/.codex/skills
cp -R ~/Downloads/codex_skill_design-thesis-latex-template/design-thesis-latex-template ~/.codex/skills/
```

## 4. 验证文件是否复制成功

### Windows

```powershell
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\SKILL.md"
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\references\contents-and-order.md"
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\scripts\check_latex_log.py"
```

三条命令都应输出 `True`。

也可以查看文件数量：

```powershell
(Get-ChildItem -Recurse -File "$env:USERPROFILE\.codex\skills\design-thesis-latex-template").Count
```

当前版本应为 18 个文件。

### macOS/Linux

```bash
test -f ~/.codex/skills/design-thesis-latex-template/SKILL.md && echo OK
test -f ~/.codex/skills/design-thesis-latex-template/references/contents-and-order.md && echo OK
test -f ~/.codex/skills/design-thesis-latex-template/scripts/check_latex_log.py && echo OK
find ~/.codex/skills/design-thesis-latex-template -type f | wc -l
```

前三条应输出 `OK`，最后一条应显示文件数量。

## 5. 验证 Skill 元数据

如果你的 Codex 安装中有系统 Skill `skill-creator`，可以运行：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

期望输出：

```text
Skill is valid!
```

如果没有这个脚本，可以跳过本步。只要第 4 步中的文件存在，通常就说明安装位置正确。

## 6. 重启 Codex 或开启新线程

安装新 Skill 后，建议：

1. 重启 Codex；或
2. 至少开启一个新的 Codex 对话线程。

这样 Codex 才能重新扫描本地 Skill 列表。

## 7. 第一次调用 Skill

可以直接写：

```text
Use $design-thesis-latex-template. 请根据我提供的学校学位论文撰写规范 Word 文件、官方模板和素材，设计并实现完整的 LaTeX 学位论文模板项目。
```

也可以写：

```text
请使用 design-thesis-latex-template 这个 Skill，帮我设计某某大学的学位论文 LaTeX 模板。
```

为了让 Codex 明确使用这个 Skill，推荐第一次使用时写出：

```text
Use $design-thesis-latex-template
```

## 8. 提供项目材料

建议把材料放在一个项目文件夹中，例如：

```text
my-university-thesis-template/
  materials/
    official-spec.docx
    official-template.docx
    cover-sample.jpg
    notice.pdf
    old-latex-template/
```

然后告诉 Codex：

```text
材料都在 my-university-thesis-template/materials 下面。请先盘点文件，不要删除或覆盖原始素材。
```

推荐提供：

- 官方撰写规范 Word/DOCX。
- 官方论文 Word 模板。
- 官方 PDF 通知或文件解读。
- 外封、内封、声明页、签字页等样张。
- 校徽、校名、封面背景、字体等素材。
- 旧版 LaTeX 模板。
- 你希望支持的版本，例如电子版、打印版、盲审版。

## 9. 让 Codex 先做规范证据表

第一次正式制作模板时，建议先要求：

```text
请先使用这个 Skill 的流程，读取 references/contents-and-order.md，然后盘点材料，建立规范证据表。暂时不要写代码。
```

证据表通常应包含：

- 项目名称
- 参数值
- 单位
- 来源文件
- 来源位置
- 适用页面或版本
- 可信度
- 备注

例如：

```text
正文字号 | 小四 | 号 | official-spec.docx | 第 3.2 节 | 正文 | 高 | 与 Word 模板一致
```

如果某个参数缺失，Codex 应标记为 `TODO-confirm`，而不是自行编造。

## 10. 确认设计方案

在写代码前，建议让 Codex 输出设计方案：

```text
请基于证据表给出模板项目设计方案，包括目录结构、类文件接口、元数据接口、参考文献方案、版本矩阵、外封方案、扫描页方案、盲审安全方案和验证方案。先不要创建文件。
```

你确认后，再让 Codex 创建项目文件。

## 11. 开始创建 LaTeX 模板项目

确认方案后可以说：

```text
我确认这个设计方案。请按方案创建 LaTeX 模板项目文件。不要删除 materials 下的原始素材，不要自动发布。
```

Skill 会引导 Codex 优先创建类似结构：

```text
schoolthesis/
  schoolthesis.cls
  thesis.tex
  metadata.tex
  README.md
  CHANGELOG.md
  src/
  data/
  ref/
  assets/
  examples/
  tests/
  scripts/
```

## 12. 编译和调试

模板项目创建后，应要求 Codex 编译：

```text
请编译根目录 thesis.tex 和 examples 下的电子版、打印版、盲审版示例，并检查日志。最终目标是没有 warning 和 error。
```

这个 Skill 的验证标准不是“能生成 PDF 就行”，而是：

- 无 LaTeX error。
- 无 package/class error。
- 无 undefined reference。
- 无 undefined citation。
- 无 biber/BibTeX 错误。
- 尽量无 LaTeX/package/class warning。
- 尽量无 overfull/underfull box。
- 盲审版无身份泄露。

## 13. 使用日志检查脚本

Skill 自带：

```text
scripts/check_latex_log.py
```

可以让 Codex 在生成的模板项目中复制或调用它：

```powershell
python path\to\check_latex_log.py build\thesis.log build\thesis.blg
```

如果只想临时允许警告，可以加：

```powershell
python path\to\check_latex_log.py build\thesis.log --allow-warnings
```

但正式交付前仍建议消除警告。

## 14. 发布前检查

如果你希望把生成的论文模板发布到 GitHub，请明确告诉 Codex：

```text
请准备发布到 GitHub。先给出发布前检查清单，不要直接 push。
```

发布前应检查：

- README 是否准确。
- LICENSE 是否合适。
- CHANGELOG 是否更新。
- 是否误提交了真实签名、学号、私人论文内容。
- 是否误提交了不可再分发的官方 Word/PDF/PSD 文件。
- 示例是否可编译。
- 日志是否无警告和报错。

## 15. 常见问题

### Codex 没有自动使用这个 Skill

请显式写：

```text
Use $design-thesis-latex-template
```

并确认 Skill 已安装到正确目录。

### 文件复制到了错误位置

正确结构应是：

```text
~/.codex/skills/design-thesis-latex-template/SKILL.md
```

而不是：

```text
~/.codex/skills/codex_skill_design-thesis-latex-template/design-thesis-latex-template/SKILL.md
```

也不是：

```text
~/.codex/skills/SKILL.md
```

### Codex 编造了参数

提醒 Codex：

```text
请遵守 Skill 的边界条件：不要编造设计参数。缺失值请标记为 TODO-confirm，并问我确认。
```

### 只生成了一个 cls 文件

提醒 Codex：

```text
请按 Skill 的 project-structure 和 engineering-architecture 设计完整模板项目，不要把所有逻辑放进一个巨大的 .cls 文件。
```

## 16. 推荐的完整首条提示词

可以直接复制下面这段作为新项目的第一条消息：

```text
Use $design-thesis-latex-template.

我想为一所中国高校制作完整的学位论文 LaTeX 模板。材料在当前工作区的 materials 文件夹中，包括官方 Word 撰写规范、官方 Word 模板、PDF 通知、封面图片和旧版 LaTeX 模板。

请先读取 Skill 的 references/contents-and-order.md，然后按 Skill 流程执行：
1. 盘点材料；
2. 建立规范证据表；
3. 标出缺失或冲突参数；
4. 给出项目结构、类文件接口、元数据接口、参考文献、版本矩阵、外封、扫描页、盲审安全和验证方案；
5. 在我确认前不要创建项目文件；
6. 不要删除原始素材；
7. 不要编造设计参数；
8. 不要自动发布。
```
