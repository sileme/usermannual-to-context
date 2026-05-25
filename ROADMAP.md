# Roadmap

给开发者读。最终用户看 [README.md](README.md)。智能体行为规范看 [AGENT.me](AGENT.me)。

---

## Vision

把工程软件的官方手册转成 Claude Code 可按需加载的背景知识层（`context_layer/`），让不熟悉该软件的人也能通过对话查询用法、生成配置脚本。

**设计原则**：

1. **Tier 化、按需加载**：用 `tiktoken` 估算每份文档 token 数，按 T0–T3 分档生成不同细粒度的产物。智能体读最少必要的导航层，再 grep 定位原文。
2. **Grep 而非 RAG**：技术手册术语精确，`rg/grep` 在精确匹配场景胜过 embedding。RAG / vector DB / SQLite FTS5 都推到 backlog，仅在评测证明 grep + 章节切分不够时再引入。
3. **页码内联**：每个文本块的 PDF 页码以 `<!-- page:N -->` HTML 注释直接嵌入 `full.md` / `chapters/*.md`，不维护单独的 `provenance.json`。
4. **轻产物**：每份文档只产 `full.md`（T0+）/ `outline.md`（T1+）/ `chapters/*.md`（T2+）。**不再产** `task_cards/` / `syntax/` / `diagnostics/` / `provenance.json` / `module_map.md`。
5. **导航层短**：软件级 `index.md` ≤ 5K tokens；`outline.md` 目标 1–3K tokens；摘要只用于导航，不作为事实来源。

---

## Milestones

### M0 — 设计确认与清理 ⏳

**目标**：把 README/SKILL/docs 中残留的旧五件套（task_cards/syntax/diagnostics/provenance.json/module_map.md）清理干净，新方向落地为可执行规划。

**输入**：当前仓库的 `README.md`、`.claude/skills/software-manual-context/SKILL.md`、`docs/add_new_software.md`、`docs/skill_authoring.md`、旧 `CLAUDE.md`、旧 `ROADMAP.md`。

**输出**：
- ✅ `ROADMAP.md`（本文件）重写
- ✅ `AGENT.me` 新建
- ✅ `CLAUDE.md` 替换为薄壳 `@AGENT.me`
- ⬜ `README.md` 更新：仓库结构 / 技术栈 / FAQ / 角色 A 示例都换成新产物名；删除 task_cards/syntax/diagnostics 提及
- ⬜ `.claude/skills/software-manual-context/SKILL.md` 更新：渐进披露阶梯改为 outline + grep + chapters；R1 字面规则保留；Registered software 段保留
- ⬜ `docs/add_new_software.md` 更新：步骤 4 输出清单换成 `full.md` / `outline.md` / `chapters/`；步骤 5 抽查指南更新
- ⬜ `docs/skill_authoring.md` 删除（M2 真正引入摘要规范时再写新版）

**不做**：写新脚本、生成 `context_layer/` 产物、动 `corpus/`。

**验收标准**：
- 仓库中（不计 git history）不再有任何文件推荐 task_cards / syntax / diagnostics / provenance.json / module_map.md 作为产物名。
- `CLAUDE.md` ≤ 5 行。
- `AGENT.me` 读完即可独立工作，不需要额外引用 README/ROADMAP。
- `grep -ri "task_cards\|provenance\.json\|module_map" .` 在 `corpus/` 外只剩 ROADMAP backlog 的历史说明。

**开发成本**：半天。
**使用成本**：0（这一档只是文档整理）。

---

### M1 — Tier 化 context builder

**目标**：把 `corpus/markdown/` 已有的全部文档转成 `context_layer/` 下的 T0 / T1 / T2 产物（暂不做 T3 软件级 router）。

**输入**：
- `corpus/markdown/<software>/<doc>/<doc>.md`
- `corpus/markdown/<software>/<doc>/<doc>_content_list.json`（含每 block 的 `page_idx`）

**输出**（per doc）：
- `context_layer/<software>/<doc>/full.md`——原 markdown + 内联 `<!-- page:N -->` anchors
- `context_layer/<software>/<doc>/outline.md`（T1+）——章节树 + 每章规则摘要 + 高频关键词
- `context_layer/<software>/<doc>/chapters/NN_<slug>.md`（T2+）——按章节拆分，每个 8–15K tokens（hard max 30K）
- `context_layer/manifest.json`（仓库根级）——所有文档的 `source_pdf` / `md_path` / `estimated_tokens` / `page_count` / `tier` / `outputs`

**不做**：
- LLM 章节摘要（M2/backlog；M1 只做规则摘要：标题路径 / 章节首段截断 / 子标题列表 / 高频术语 / 页码范围）
- 软件级 `index.md`（M2，T3 才必须）
- SQLite FTS5、RAG、MCP、任务卡
- 多语言手册支持

**分档阈值**（基于 `tiktoken` cl100k_base，近似估算）：

| Tier | token 数 | 产物 |
|---|---|---|
| T0 | < 12K | `full.md` |
| T1 | 12K – 80K | `full.md` + `outline.md` |
| T2 | 80K – 350K | `full.md` + `outline.md` + `chapters/` |
| T3 | 单文档 > 350K，或同软件文档总和 > 500K | 同 T2，且 M2 引入软件级 router |

**章节切分规则**（T2）：

- 按 `#` 标题树切，目标每片 8–15K tokens。
- 若一级章节超过 hard max（30K），按 `##` 递归；仍超则按 `###`。
- 章节命名：`NN_<slug>.md`，`NN` 是两位序号（按阅读顺序），`<slug>` 是 kebab-case 章节标题前 40 字符。
- 每个 `chapters/*.md` 的开头注释 `<!-- page:N -->` 必须与原文档中第一个 page anchor 一致。

**模块划分**（在 `scripts/lib/` 下）：

| 模块 | 职责 |
|---|---|
| `token_estimator.py` | 封装 `tiktoken.get_encoding("cl100k_base")`，给字符串返回估算 token 数 |
| `page_anchor.py` | 读 `_content_list.json`，把 `<!-- page:N -->` 注入 markdown 文本（按 block 顺序 + `page_idx` 边界） |
| `heading_parser.py` | 从 markdown 抽取标题树（`#` / `##` / `###` …），返回带文本范围的节点列表 |
| `tier_classifier.py` | (token_count, doc_count_in_software) → tier |
| `outline_builder.py` | 标题树 + 章节首段截断 + 高频关键词（基于 simple stoplist + 频率） → `outline.md` |
| `chapter_splitter.py` | 按标题树 + token budget 切 `full.md` 成 `chapters/*.md` |
| `software_index_builder.py` | M2 才用；M1 写好接口占位 |
| `manifest.py` | `context_layer/manifest.json` 的读写 |

**可执行改造步骤**（不要一次性大重写）：

1. 新增 `token_estimator.py`，把 02 改成"只跑估算 → 写 manifest"，先验证分档分布合理。
2. 新增 `page_anchor.py`，02 产 `full.md`（仍只 T0 走通完整流程；T1/T2 暂只产 full.md）。
3. 新增 `heading_parser.py` + `outline_builder.py`，T1 路径接通。
4. 新增 `tier_classifier.py`，02 根据 tier 选择产物组合。
5. 新增 `chapter_splitter.py`，T2 路径接通。
6. 删除旧 02 中写 `task_cards/syntax/diagnostics/_TODO.md` 的逻辑；清理 `lib/heading_tree.py`、`lib/provenance.py` 旧 stub。
7. 全量跑：dakota（1 doc，预期 T1）+ sentaurus 抽样（cpps T0、calikit_ug T1、sdevice_ug T2、sprocess_ug T2/T3 边界）。
8. 跑全量 sentaurus 30 doc。

**验收标准**：
- `python scripts/02_markdown_to_context.py --software dakota` 与 `--software sentaurus` 都成功跑完。
- `context_layer/manifest.json` 包含全部 31 份文档，每份有完整 tier / token / outputs。
- 所有 T2 文档的 `chapters/*.md` 单文件 ≤ 30K tokens。
- 抽样 5 份文档，原 markdown 中段落能在对应 chapter / page anchor 之间正确对齐。
- 旧产物（`task_cards/` / `syntax/` / `diagnostics/` / `provenance.json` / `module_map.md`）在 `context_layer/` 中不存在。

**开发成本**：2–3 天（含调试章节切分边界情况）。
**使用成本**（每次 query 占用 token，估算）：
- T0 文档：直接读 ~12K tokens。
- T1 文档：outline ~2K + 一段 grep 命中片段 ~3K = ~5K。
- T2 文档：outline ~3K + 一个章节 ~15K = ~18K。
- T3 文档：软件 index ~5K（M2 才有）+ outline ~3K + 章节 ~15K = ~23K。

---

### M2 — 软件级 router + T3 + 评测集

**目标**：多文档软件（sentaurus 30 doc）可被高效路由；引入小规模 query 评测集，能验证 M1/M2 改动是否回退。

**输入**：
- M1 产出的 `context_layer/manifest.json`
- 每份文档的 `outline.md`

**输出**：
- `context_layer/<software>/index.md`——软件级 router，≤ 5K tokens；内容是"问 X 类问题查 Y doc"的高密度索引，从各 doc 的 outline 第一段 + 章节顶层关键词聚合
- `tests/queries/<software>.jsonl`——每个软件 10–20 条 query，每条带 `expected_doc` / `expected_chapter`（人工标注）
- `scripts/eval.py`——给定 query，跑智能体（或本地 grep + outline 启发式），统计命中率
- T3 文档的额外验证：长文档（如 sdevice_ug ~725K tokens）的章节切分是否仍 ≤ 30K，必要时再细分

**不做**：
- LLM 章节摘要
- SQLite FTS5
- RAG / vector DB

**验收标准**：
- sentaurus 30 doc 的 router 让评测脚本在不读全部 outline 的情况下 ≥ 80% 命中正确 doc。
- sdevice_ug、sprocess_ug 的所有 `chapters/*.md` ≤ 30K tokens。
- `scripts/eval.py` 可重复跑，输出 markdown 报告（每条 query：命中 doc / chapter / 召回片段是否包含期望关键词）。

**开发成本**：1–2 天 + 评测集人工标注时间（每个软件半天）。
**使用成本**：T3 query ~23K tokens，相比 M1 单 doc 加载，多出软件 index 的 5K。

---

### M3 / Backlog

按用户需求 / 评测反馈决定优先级。**仅在 M2 评测显示瓶颈时**才启动对应 backlog。

- **LLM 章节摘要**：M1 规则摘要若导致路由命中率低（< 70%），引入一次性 LLM pass 提升 outline 质量。结果入 git。成本：单次 API 费用 + 重跑流程。
- **SQLite FTS5 / BM25 全文索引**：若 grep 在跨章节 / 跨文档检索慢或召回差，引入 `scripts/build_fts.py` 生成 `.context_index.db`（gitignored，按 manifest 时间戳重建）。**比 RAG 优先**。
- **RAG / vector embedding**：仅在 FTS5 + tier 化仍不够（语义 query 而非关键词 query 大量出现）时考虑。需要前置评测证据。
- **任务卡 / 错误诊断卡复活**：若评测显示某些高频 query pattern 反复命中同一段，把它沉淀成 curated 卡片。**按需而非全量。**
- **MCP server 化**：把 AGENT.me 工作流封装成 MCP server，让 Cursor / Continue / Cline 等非 Claude Code 客户端复用同一份 `context_layer/`。
- **多语言手册支持**：minerU `--lang` 当前写死英文；中日韩手册要看 OCR 表现。
- **`context_layer/` 版本化**：手册升级（dakota 6.16 → 6.17）如何 diff、是否双版本并存。
- **手册更新自动化**：`Makefile` / `justfile`，把 `01 → 02 → manifest` 串成一条命令。
- **API 配额监控**：minerU 云端 API 调用记账到 `corpus/.api_log.jsonl`（gitignored）。
- **页码 anchor 校验脚本**：`scripts/verify_anchors.py`，确保 `full.md` / `chapters/*.md` 中所有 `<!-- page:N -->` 单调递增且与原 `_content_list.json` 对齐。

---

## Currently Working On

<!-- BEGIN: currently-working-on -->
**M0 — 设计确认与清理（进行中）**

已完成：
- `ROADMAP.md` 重写
- `AGENT.me` 新建
- `CLAUDE.md` 替换为薄壳

待完成（M0 后半段）：
- 更新 `README.md` —— 把仓库结构 / 技术栈 / FAQ 中提到的旧产物全部换名
- 更新 `.claude/skills/software-manual-context/SKILL.md` —— 渐进披露阶梯改为 outline + grep + chapters；R1 字面规则不动；Registered software 段保留
- 更新 `docs/add_new_software.md` —— 步骤 4 / 5 输出清单与抽查指南换成新产物
- 删除 `docs/skill_authoring.md`（M2 再写新版）

M0 完成后立刻进入 M1 第 1 步（`token_estimator.py` + 跑估算 + 写 manifest 验证分档分布）。
<!-- END: currently-working-on -->

---

## 工程约定

- **02 脚本与 PDF 引擎解耦**：02 只读 `<doc>.md` + `<doc>_content_list.json`。换 PDF 引擎（docling / marker / 商用 API）只动 01。
- **页码内联，不再单独 provenance.json**：minerU 的 `page_idx` 在 02 阶段以 `<!-- page:N -->` 注释嵌入 markdown。智能体引用时向上回溯最近的 anchor。
- **manifest 单一来源**：`context_layer/manifest.json` 是仓库级唯一的"哪些文档 / tier / outputs"索引。任何脚本 / 智能体决策都从这里读。
- **拒答字符串**：永远用中文「资料中无相关内容」，即使手册是英文。修改前先在 issue 里讨论。
- **不引入新检索机制时不写新依赖**：M1 / M2 阶段除 `tiktoken` 外不加 Python 依赖。SQLite FTS5 / embedding / vector DB 是 M3+ 才考虑的。
- **`.agent/`** 是模型自用工作笔记，gitignored；每个开发周期结束删除。不要把它当 ROADMAP 的草稿——半成品记 `.agent/PLAN.md`，公开规划写这里。

---

## 进度更新流程

完成一个 milestone 时：

1. 在 Milestones 下把 `⏳` 改 `✅` 并加日期。
2. 把 "Currently Working On" 区块**清空内容、保留 BEGIN/END 注释**，等下一个 milestone 接手时重填。
3. 新开 milestone 的工作时把详情写回 "Currently Working On"。

`grep -A30 "BEGIN: currently-working-on" ROADMAP.md` 可以扫到当前活跃工作。
