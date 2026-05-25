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

### M0 — 设计确认与清理 ✅ (2026-05-25)

**目标**：把 README/SKILL/docs 中残留的旧五件套（task_cards/syntax/diagnostics/provenance.json/module_map.md）清理干净，新方向落地为可执行规划。

**输入**：当前仓库的 `README.md`、`.claude/skills/software-manual-context/SKILL.md`、`docs/add_new_software.md`、`docs/skill_authoring.md`、旧 `CLAUDE.md`、旧 `ROADMAP.md`。

**输出**：
- ✅ `ROADMAP.md`（本文件）重写
- ✅ `AGENT.me` 新建
- ✅ `CLAUDE.md` 替换为薄壳 `@AGENT.me`
- ✅ `README.md` 更新：仓库结构 / 技术栈 / FAQ / 角色 A 示例都换成新产物名；新增"角色 C：在其他项目复用"段
- ✅ `.claude/skills/software-manual-context/SKILL.md` 重写：渐进披露阶梯换成 outline + grep + chapters；R1 字面规则保留
- ✅ `docs/add_new_software.md` 更新：步骤 4/5 输出清单换成 `full.md` / `outline.md` / `chapters/`
- ✅ `docs/skill_authoring.md` 删除（M2 重新引入摘要规范时再写新版）
- ✅ `docs/use_in_other_projects.md` 新建（consumer 端的三种引用模式 + 最小工作示例）

**不做**：写新脚本、生成 `context_layer/` 产物、动 `corpus/`。

**验收标准**：
- ✅ 仓库中（不计 git history）不再有任何文件推荐 task_cards / syntax / diagnostics / provenance.json / module_map.md 作为产物名
- ✅ `CLAUDE.md` ≤ 5 行
- ✅ `AGENT.me` 读完即可独立工作，不需要额外引用 README/ROADMAP

**实际开发成本**：半天。
**使用成本**：0。

---

### M1 — Tier 化 context builder ⏳ (T0/T1 完成；T2/T3 章节切分待做)

**目标**：把 `corpus/markdown/` 已有的全部文档转成 `context_layer/` 下的 T0 / T1 / T2 产物。

**已完成（M1a 半段）**：
- ✅ `lib/token_estimator.py` — tiktoken cl100k_base 估算
- ✅ `lib/page_anchor.py` — 把 `<!-- page:N -->` 注入 markdown（基于 minerU `_content_list.json` 的 `page_idx`）
- ✅ `lib/heading_parser.py` — 解析 markdown 标题树（忽略代码块内的 `#`）
- ✅ `lib/tier_classifier.py` — token → tier（T0/T1/T2/T3）+ 软件级 `needs_router`
- ✅ `lib/outline_builder.py` — 基于标题文本模式（"Chapter N" / "1.2.3" 等）推断逻辑层级；按 tier 应用 max_depth 与 token budget；三级 graceful degradation
- ✅ `lib/manifest.py` — `context_layer/manifest.json` 读写
- ✅ `scripts/02_markdown_to_context.py` — 调用以上模块，T0 写 `full.md`，T1+ 写 `full.md` + `outline.md`
- ✅ 删除旧 stub `lib/heading_tree.py`、`lib/provenance.py`
- ✅ 全量跑通：dakota（1 doc T2）+ sentaurus（30 doc：T0=5、T1=13、T2=9、T3=3，总 4.22M tokens，`needs_router=yes`）
- ✅ 全部 outline 在 token 预算内（T1 ≤ 3K、T2 ≤ 5K、T3 ≤ 8K）

**未做（M1b 半段，待启动）**：
- ⬜ `lib/chapter_splitter.py` — 按章节切 T2/T3 文档到 `chapters/NN_<slug>.md`，每片 8–15K tokens、hard max 25–30K
- ⬜ 02 脚本接入 chapter_splitter，T2/T3 文档产 `chapters/`
- ⬜ 验证所有 T2/T3 文档的 chapter 不超过 hard max
- ⬜ 在 manifest 里登记 `outputs.chapters` 列表，清掉 `chapters_pending` 标记

**输入**：
- `corpus/markdown/<software>/<doc>/<doc>.md`
- `corpus/markdown/<software>/<doc>/<doc>_content_list.json`（含每 block 的 `page_idx`）

**输出**（per doc）：
- `context_layer/<software>/<doc>/full.md`——原 markdown + 内联 `<!-- page:N -->` anchors
- `context_layer/<software>/<doc>/outline.md`（T1+）——章节树 + 简短 blurb；page 范围
- `context_layer/<software>/<doc>/chapters/NN_<slug>.md`（T2+，**尚未生成**）
- `context_layer/manifest.json`（仓库根级）——所有文档的索引

**不做**：
- LLM 章节摘要（M3/backlog；M1 只做规则提取：标题路径 / 首段截断 / 页码范围）
- 软件级 `<software>/index.md` router（M2，T3 才必须）
- SQLite FTS5、RAG、MCP、任务卡
- 多语言手册支持

**分档阈值**（基于 `tiktoken` cl100k_base，近似估算）：

| Tier | token 数 | 产物 |
|---|---|---|
| T0 | < 12K | `full.md` |
| T1 | 12K – 80K | `full.md` + `outline.md` |
| T2 | 80K – 350K | `full.md` + `outline.md` + `chapters/`（待做） |
| T3 | > 350K 单文档（独立维度），或同软件文档总和 > 500K 触发软件级 router | 同 T2，加 `<software>/index.md`（M2） |

**章节切分规则**（M1b 待实现）：

- 按 `#` 标题树切，目标每片 8–15K tokens。
- 若一级章节超过 hard max（30K），按 `##` 递归；仍超则按 `###`。
- 章节命名：`NN_<slug>.md`，`NN` 是两位序号（按阅读顺序），`<slug>` 是 kebab-case 章节标题前 40 字符。
- 每个 `chapters/*.md` 的开头注释 `<!-- page:N -->` 必须与原文档中第一个 page anchor 一致。
- **挑战**：minerU 把所有标题输出为 H1（无嵌套结构）。chapter_splitter 必须复用 outline_builder 中的"按标题文本模式推断层级"逻辑，把推断为 level-1 的"Chapter N"/"Part X" 当切分点。

**模块划分**（在 `scripts/lib/` 下）：

| 模块 | 职责 | 状态 |
|---|---|---|
| `token_estimator.py` | 封装 `tiktoken.get_encoding("cl100k_base")` | ✅ |
| `page_anchor.py` | 读 `_content_list.json`，把 `<!-- page:N -->` 注入 markdown | ✅ |
| `heading_parser.py` | 从 markdown 抽取标题树（忽略 fenced code block） | ✅ |
| `tier_classifier.py` | token → tier；软件级 needs_router | ✅ |
| `outline_builder.py` | 推断逻辑层级 + 规则摘要 → `outline.md` | ✅ |
| `chapter_splitter.py` | 按标题树 + token budget 切 `full.md` → `chapters/*.md` | ⬜ M1b |
| `software_index_builder.py` | M2 才用；M1 阶段未实装 | ⬜ M2 |
| `manifest.py` | `context_layer/manifest.json` 读写 | ✅ |

**验收标准**：
- ✅ `python scripts/02_markdown_to_context.py --software dakota` 与 `--software sentaurus` 都成功跑完
- ✅ `context_layer/manifest.json` 包含全部 31 份文档，每份有 tier / token / outputs
- ✅ 抽样文档的 outline 在 token 预算内
- ⬜ 所有 T2/T3 文档的 `chapters/*.md` 单文件 ≤ 30K tokens（M1b）
- ⬜ 抽样 5 份文档，原 markdown 段落能在对应 chapter / page anchor 之间正确对齐（M1b）
- ✅ 旧产物（`task_cards/` / `syntax/` / `diagnostics/` / `provenance.json` / `module_map.md`）在 `context_layer/` 中不存在

**实际开发成本**：~1 天 M1a；M1b chapter splitter 估约半天。
**使用成本**（每次 query 占用 token，估算）：
- T0 文档：直接读 ~12K tokens
- T1 文档：outline ~1–3K + 一段 grep 命中片段 ~3–5K = ~5–8K
- T2 文档（M1a）：outline ~5K + grep `full.md` 命中片段 ~5–10K = ~10–15K
- T2 文档（M1b 完成后）：outline ~5K + 单章 ~15K = ~20K（更贵但更精准）
- T3 文档（M1b 后）：outline ~8K + 单章 ~15K = ~23K；M2 加软件 index 后 + 5K

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
**M1a 已完成（2026-05-25）；M1b（chapter splitter）暂停，等用户启动**

M0 设计与清理 + M1a 半段（token 估算 / page anchor / outline 生成 / manifest）已落地：
- 31 份文档全部入 `context_layer/`（dakota 1 + sentaurus 30）
- tier 分布：T0=5、T1=13+1、T2=9+1、T3=3；sentaurus `needs_router=yes`
- 所有 outline 在 token 预算内（T1 ≤ 3K、T2 ≤ 5K、T3 ≤ 8K）
- consumer 端使用指南已写：[docs/use_in_other_projects.md](docs/use_in_other_projects.md)

**当前 T2/T3 文档只有 `full.md` + `outline.md`，没有 `chapters/`**——智能体查询时需要在 `outline.md` 定位后 grep `full.md` 命中片段，可能加载较多 token（~10–15K vs 切片后的 ~20K 但更精准）。这是有意的中间状态。

下一步（待用户启动）：
- 实现 `scripts/lib/chapter_splitter.py`
- 02 脚本接入 chapter_splitter，T2/T3 文档产 `chapters/NN_<slug>.md`
- 更新 manifest `outputs.chapters` 字段

或直接跳到 M2（软件级 router）也是可选项——目前 sentaurus 多 doc 路由是 consumer 端最大的不便。
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
