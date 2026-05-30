# design-thesis-latex-template Codex Skill

这是一个用于 Codex 的 Skill，名称为 `design-thesis-latex-template`。

它的目标是帮助 Codex 把中国高校的学位论文撰写规范、官方 Word 模板、PDF/图片样张和素材文件，沉淀成一个完整、可维护、可测试、适合 GitHub 管理的 LaTeX 学位论文模板项目。

更具体地说，这个 Skill 会引导 Codex：

- 先从官方 Word/DOCX、PDF、图片、旧模板和素材中提取规范证据。
- 不编造学校特定的字号、行距、页边距、封面坐标、颜色、书脊宽度等参数。
- 设计清晰的 LaTeX 项目结构，而不是只写一个巨大的 `.cls` 文件。
- 设计文档类选项、元数据接口、参考文献接口、版本矩阵、盲审安全策略、外封和扫描页方案。
- 生成示例、测试脚本和最终编译验证流程。
- 以“编译后无报错、无警告”为最终调试目标。

详细的逐步使用方法见：

[USE_GUIDE.md](USE_GUIDE.md)

## 仓库结构

```text
.
├─ README.md
├─ USE_GUIDE.md
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

其中：

- `SKILL.md` 是 Skill 的入口说明，Codex 触发 Skill 后会先读取它。
- `references/contents-and-order.md` 是内容导航和项目制作顺序说明。
- `references/` 中其他文件分别沉淀规范解析、工程结构、接口设计、参考文献、版本、外封、扫描页、盲审、视觉回归、验证和发布流程。
- `scripts/check_latex_log.py` 是日志检查脚本，用于扫描 LaTeX 编译日志中的错误和警告。

## 适用场景

当你希望 Codex 完成下面这类任务时，可以使用本 Skill：

1. 你提供某所中国高校的学位论文撰写规范，一般是 Word/DOCX 文件。
2. 你提供官方 Word 模板、PDF 通知、封面图片、Logo、字体、PSD 导出图、扫描页样例、旧 LaTeX 模板等素材。
3. 你希望 Codex 生成完整 LaTeX 模板项目，而不仅是一个类文件。
4. 你希望模板具有清晰目录结构、README、示例、测试、Git 版本控制和发布前检查。
5. 你希望模板支持电子版/打印版、普通版/盲审版、本科/硕士/博士、学术型/专业型等不同版本。

## 安装位置

Codex 会从本地 Skills 目录发现个人 Skill。

Windows 常见位置是：

```powershell
C:\Users\<你的用户名>\.codex\skills
```

可以用下面命令打开：

```powershell
explorer "$env:USERPROFILE\.codex\skills"
```

macOS/Linux 常见位置是：

```bash
~/.codex/skills
```

如果你配置了自定义 `CODEX_HOME`，则应安装到：

```text
$CODEX_HOME/skills
```

## Windows 安装方法

打开 PowerShell，先下载仓库：

```powershell
cd "$env:USERPROFILE\Downloads"
git clone https://github.com/wdduke/codex_skill_design-thesis-latex-template.git
```

确保 Codex Skills 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
```

复制整个 Skill 文件夹：

```powershell
Copy-Item -Recurse -Force `
  "$env:USERPROFILE\Downloads\codex_skill_design-thesis-latex-template\design-thesis-latex-template" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

最终目录应为：

```text
C:\Users\<你的用户名>\.codex\skills\design-thesis-latex-template
```

注意：不要只复制 `SKILL.md`，必须复制整个 `design-thesis-latex-template` 文件夹，否则 `references/` 和 `scripts/` 不会被安装。

## macOS/Linux 安装方法

打开终端：

```bash
cd ~/Downloads
git clone https://github.com/wdduke/codex_skill_design-thesis-latex-template.git
mkdir -p ~/.codex/skills
cp -R ~/Downloads/codex_skill_design-thesis-latex-template/design-thesis-latex-template ~/.codex/skills/
```

最终目录应为：

```text
~/.codex/skills/design-thesis-latex-template
```

## 验证安装是否成功

Windows：

```powershell
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\SKILL.md"
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\references\contents-and-order.md"
Test-Path "$env:USERPROFILE\.codex\skills\design-thesis-latex-template\scripts\check_latex_log.py"
```

每条命令都应输出：

```text
True
```

macOS/Linux：

```bash
test -f ~/.codex/skills/design-thesis-latex-template/SKILL.md && echo OK
test -f ~/.codex/skills/design-thesis-latex-template/references/contents-and-order.md && echo OK
test -f ~/.codex/skills/design-thesis-latex-template/scripts/check_latex_log.py && echo OK
```

每条命令都应输出：

```text
OK
```

如果本地有 Codex 自带的 `skill-creator` 系统 Skill，还可以运行：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "$env:USERPROFILE\.codex\skills\design-thesis-latex-template"
```

期望输出：

```text
Skill is valid!
```

## 调用方式

安装后，建议重启 Codex 或开启一个新线程，使 Skill 列表刷新。

显式调用：

```text
Use $design-thesis-latex-template. 请根据我提供的学校学位论文撰写规范 Word 文件、官方模板和素材，设计并实现完整的 LaTeX 学位论文模板项目。
```

自然语言调用也可以：

```text
请用 design-thesis-latex-template 这个 Skill，帮我把这所学校的学位论文规范沉淀成完整 LaTeX 模板项目。
```

## 推荐提供的材料

使用时建议一次性提供或说明这些材料：

- 学校官方学位论文撰写规范 Word/DOCX 文件。
- 学校官方论文 Word 模板。
- 学校发布的 PDF 通知、文件解读或格式说明。
- 外封、内封、声明页、签字页、扫描页等图片或 PDF 样张。
- 校徽、校名、封面背景、字体等素材。
- 旧版 LaTeX 模板或其他学校模板，仅作为工程参考。
- 需要支持的版本，例如电子版、打印版、盲审版、普通版。
- 是否需要最终上传 GitHub，还是只在本地使用。

## 使用过程中的关键原则

本 Skill 会要求 Codex 遵守：

- 不覆盖已有 Skill，除非用户明确同意。
- 不删除任何原始素材。
- 不自动发布、打 tag 或 push，除非用户明确要求。
- 不编造学校规范参数。
- 先建立规范证据表，再进行模板设计。
- 外封、扫描页、盲审安全、参考文献、版本矩阵都要独立设计。
- 最终调试目标是编译后没有警告和报错。

## 日志检查脚本

Skill 内置脚本：

```text
design-thesis-latex-template/scripts/check_latex_log.py
```

可用于扫描 LaTeX 编译日志：

```powershell
python path\to\check_latex_log.py build\thesis.log build\thesis.blg
```

它会检查：

- LaTeX 错误
- Package/Class 错误
- LaTeX/Package/Class 警告
- overfull/underfull box
- 未定义引用
- 未定义参考文献
- biber/BibTeX 问题

默认情况下，发现警告也会返回非零状态，因为这个 Skill 的目标是“无警告编译”。
