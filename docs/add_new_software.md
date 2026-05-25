# 添加新软件

把一个新软件的 user manual 接入 `software_usermanual_context`，从 PDF 走到可被 Claude Code 查询的 `context_layer/<software>/`。

## 前置

- 装好 minerU：见 [install_mineru.md](install_mineru.md)
- 有该软件的官方 user manual PDF（一个或多个）

## 步骤

### 1. 命名

为软件取一个**短、全小写、无空格**的名字。这个名字会成为目录名、SKILL 引用的 key，改起来麻烦，一开始就定好。

例：
- `dakota` ✅
- `sentaurus` ✅
- `comsol_multiphysics` ❌（有下划线 OK 但太长）→ 用 `comsol`
- `Sentaurus TCAD` ❌（有空格、大写）

### 2. 放 PDF

```bash
mkdir -p corpus/raw/<software>/
cp /path/to/manual.pdf corpus/raw/<software>/
```

PDF 文件名也建议**短、可读、无空格**——它会成为 `context_layer/<software>/<doc>/` 的 `<doc>` 部分。比如 `dakota_Users-6.16.0.pdf` → `<doc> = dakota_Users-6.16.0`。

> `corpus/` 整体在 `.gitignore` 里。这是有意的：手册可能受版权限制，且生成的 markdown 太大不适合入库。

### 3. PDF → Markdown

```bash
python scripts/01_pdf_to_markdown.py --software <software>
```

加 `--dry-run` 可以先看会处理哪些文件。加 `--doc <name>` 可以只跑一份。

输出在 `corpus/markdown/<software>/<doc>/`，含：
- `<doc>.md` ——人类可读的连续 markdown，适合抽查章节和表格是否完整
- `<doc>_content_list.json` ——AI 阅读的结构化 block 列表（按阅读顺序），每个 block 含 `type`、`text`、`page_idx`（页码）、`bbox`（坐标）等元数据。02 脚本以此文件为主把 `<!-- page:N -->` 锚点注入 `full.md`
- `images/` ——抽出的图

> `.md` 和 `_content_list.json` 包含相同的文本内容，但 JSON 是 MD 的超集——多了页码、坐标、元素类型等结构化元数据。人类抽查读 `.md`，AI / 下游脚本读 `.json`。

### 4. Markdown → context_layer

```bash
python scripts/02_markdown_to_context.py --software <software>
```

输出在 `context_layer/`，按文档 tier（基于 `tiktoken` 估算 token 数）决定产物组合：

| Tier | token 数 | 产物 |
|---|---|---|
| T0 | < 12K | `<doc>/full.md` |
| T1 | 12K – 80K | `<doc>/full.md` + `<doc>/outline.md` |
| T2 | 80K – 350K | `<doc>/full.md` + `<doc>/outline.md` + `<doc>/chapters/NN_*.md` |
| T3 | > 350K 单文档，或同软件总和 > 500K | 同 T2 + `<software>/index.md`（软件级 router） |

共通产出：
- `context_layer/manifest.json` ——所有文档的 `source_pdf` / `md_path` / `estimated_tokens` / `page_count` / `tier` / `outputs` 索引
- 每个 `full.md` 和 `chapters/*.md` 都内联 `<!-- page:N -->` HTML 注释作为页码锚点，无单独 provenance.json

### 5. 抽查

打开 `context_layer/manifest.json`，对照预期文档列表，确认 tier 分布合理（小手册落 T0/T1，长手册落 T2/T3）。

对每份 T1+ 文档，打开 `outline.md`，对照 PDF 目录，确认章节没漏。

对每份 T2+ 文档，抽样 1–2 个 `chapters/NN_*.md`，确认章节切分边界合理，每片不超过 30K tokens。

### 6. 提交

```bash
git add context_layer/<software>/
git commit -m "context_layer: add <software>"
```

`corpus/` 因为 gitignore 不会被加入，正常。

### 7. 让 Claude Code 知道

更新两处提及"已注册软件"的列表：
- `.claude/skills/software-manual-context/SKILL.md` 的 "Registered software" 小节
- `README.md` 的 "支持的软件" 小节

如果不更新，Skill 仍然能用（它会读 `context_layer/*/index.md`），但用户和 Claude Code 看不到一目了然的清单。

## 如何换 PDF 引擎

`scripts/02_markdown_to_context.py` 与 minerU **解耦**——它只读两个文件：

```
corpus/markdown/<software>/<doc>/<anything>/<doc>.md
corpus/markdown/<software>/<doc>/<anything>/<doc>_content_list.json
```

后者是一个 JSON 数组，每条 block 至少含：

```json
{"type": "text|table|image|equation", "page_idx": 0, "text": "..."}
```

按阅读顺序排列。其它字段（`bbox`、`level`、`img_path` 等）允许存在，02 会忽略未知字段。

如果你换了别的工具（docling、marker、商用 API、自家脚本），让它把上面两个文件按相同路径吐出，01 直接换掉就行，02 不用动。

写一个新的 `01_<engine>_to_markdown.py` 与现有的 `01_pdf_to_markdown.py` 并列，用 `--engine` 参数挑也是一种思路；目前没做，因为只有 minerU。
