# usermannual-to-context

> 把工程软件的官方 user manual 转成 **Claude Code 可按需加载的背景知识层**。不熟悉该软件的人也能通过对话查用法、理解参数、生成脚本，而不用从头读几百页 PDF；并且每条回答都附 PDF 页码出处，避免 LLM 编造。

把它当成"会翻手册的工程助理"——你提问，它去 `context_layer/` 里精准定位章节，引用回答；找不到就老实说「资料中无相关内容」。

---

## 目录

- [它解决什么问题](#它解决什么问题)
- [已入库的软件](#已入库的软件)
- [快速上手](#快速上手)
  - [角色 A：查询软件用法](#角色-a查询软件用法)
  - [角色 B：把新软件接入仓库](#角色-b把新软件接入仓库)
  - [角色 C：在你自己的项目里复用 `context_layer/`](#角色-c在你自己的项目里复用-context_layer)
- [仓库结构](#仓库结构)
- [技术栈](#技术栈)
- [核心硬规则](#核心硬规则)
- [当前限制 & FAQ](#当前限制--faq)
- [贡献 / 提问](#贡献--提问)

---

## 它解决什么问题

工程软件手册通常很厚（Dakota 单本 4 MB / 347 页，Sentaurus TCAD 全套 77 MB / 30 份共上万页）。一次性塞给 LLM 既贵又会触发 hallucination。本项目按 **Manual-to-Skill Context Engineering** 思路，用 `tiktoken` 对每份文档估算 token，按四档（T0/T1/T2/T3）生成不同细粒度的产物：

| 产物 | 哪档有 | 角色 | 加载时机 |
|---|---|---|---|
| `context_layer/manifest.json` | 仓库根，单一来源 | 全部文档的 tier / token / outputs 索引 | 智能体定位时读 |
| `<sw>/index.md` | T3 软件 / 多文档软件 | 软件级 router："问 X 类问题查 Y doc" | 多文档软件提问先读 |
| `<sw>/<doc>/full.md` | T0+ | 原文 + 内联 `<!-- page:N -->` 页码锚点 | T0 直接整读；T1+ 仅作 grep 兜底 |
| `<sw>/<doc>/outline.md` | T1+ | 章节树 + 规则摘要 + 高频关键词，导航用 | T1+ 必读 |
| `<sw>/<doc>/chapters/NN_<slug>.md` | T2+ | 按章节切分，每片 8–15K tokens | T2/T3 命中后只读相关章节 |

分档阈值（基于 `tiktoken` cl100k_base 估算，近似）：

| Tier | token 数 | 产物组合 |
|---|---|---|
| T0 | < 12K | `full.md` |
| T1 | 12K – 80K | `full.md` + `outline.md` |
| T2 | 80K – 350K | `full.md` + `outline.md` + `chapters/` |
| T3 | 单文档 > 350K 或同软件文档总和 > 500K | 同 T2 + 软件级 `index.md` |

加上一条硬规则：**手册没说的，回答以「资料中无相关内容」开头，再可选附通用建议**——不允许 paraphrase 没读过的内容。详见 [核心硬规则](#核心硬规则)。

> **检索机制**：当前仅依赖 `rg/grep` + tier 化导航层，**不引入** RAG / vector DB / embedding。若评测证明 grep + 章节切分不够，后续优先考虑 SQLite FTS5，再考虑 vector store。详见 [ROADMAP.md](ROADMAP.md) Backlog。

---

## 已入库的软件

| 软件 | 文档 | 状态 |
|---|---|---|
| **dakota** | `dakota_Users-6.16.0.pdf`（347 页；优化、UQ、灵敏度分析） | PDF→markdown 完成；context_layer 待生成 |
| **sentaurus** | 30 份 TCAD user guide（`sdevice_ug` 1530 页、`sprocess_ug` 1320 页、`svisual_ug` 548 页 等） | PDF→markdown 完成；context_layer 待生成 |

> 状态术语：完整里程碑（M0 设计 / M1 T0–T2 builder / M2 软件 router + 评测 / M3 backlog）见 [ROADMAP.md](ROADMAP.md)。

---

## 快速上手

### 角色 A：查询软件用法

**前提**：有人已经把你想问的软件入库（即 `context_layer/<software>/` 已存在并随仓库提交）。你不需要装任何东西——不需要 minerU、不需要 Python 环境。

**步骤**：

1. 用 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 打开本仓库目录。
2. 直接提问。Claude Code 会自动按渐进式披露读 `context_layer/<software>/`。

**示例提问**：

```
你> Sentaurus sdevice 里 Physics{} 段怎么开 SRH recombination？

Claude> 在 Physics{} 段里加 Recombination(SRH)，可附 (DopingDep) 等修饰符
        开启浓度依赖 [sdevice_ug p.143]。

        （智能体路径：读 outline.md 定位到 Physics 章节 → 读 chapters/
        NN_physics.md → 引用最近的 <!-- page:143 --> anchor）
```

```
你> Dakota 跑参数扫描需要哪些 input 段？

Claude> Dakota 输入文件按 method / variables / interface / responses 四段
        组织 [dakota_Users-6.16.0 p.32]。其中扫描的核心是 method 段的
        multidim_parameter_study 等关键字 [p.215]……
```

**找不到时的回答样式**（不是 bug，是设计）：

```
你> Dakota 怎么对接 ANSYS Fluent？

Claude> 资料中无相关内容

        非手册内容：Dakota 通过通用 black-box 接口（analysis_driver）与外部
        CAE 工具耦合，理论上可调任何能命令行驱动的求解器；具体到 Fluent
        通常需要写 journal 脚本。建议查 dakota_Users-6.16.0.pdf 的
        "Interfaces" 章节。
```

设计意图：让你**一眼看出哪些信息是手册说的、哪些是常识猜测**，不会被混淆的"看起来权威"答复误导。

---

### 角色 B：把新软件接入仓库

让角色 A 能查它。

**前提**：

- 装好 minerU——见 [docs/install_mineru.md](docs/install_mineru.md)（两种方式：本地装 / 云端 API）
- 有官方 user manual PDF（一份或多份）

**步骤**（详细版见 [docs/add_new_software.md](docs/add_new_software.md)）：

```bash
# 1. 放 PDF（命名建议短、全小写）
mkdir -p corpus/raw/<software>/
cp /your/path/manual.pdf corpus/raw/<software>/

# 2. PDF → Markdown
#    本地装 minerU：
python scripts/01_pdf_to_markdown.py --software <software>
#    或用 minerU 云端 API（小批量更快、本机无 GPU 也行）：
export MINERU_API_TOKEN='你的token'   # PowerShell: $env:MINERU_API_TOKEN='...'
python scripts/01_pdf_to_markdown.py --software <software> --engine api

# 3. Markdown → context_layer
python scripts/02_markdown_to_context.py --software <software>

# 4. 抽查 + 提交
git add context_layer/<software>/
git commit -m "context_layer: add <software>"
```

> **大文件自动拆分**：minerU 云端 API 单文件 ≤ 200 页。本仓库的 01 脚本会自动把超长 PDF（如 Sentaurus sdevice_ug 的 1530 页）拆成 ≤ 200 页一片上传，再把多份 markdown 合并回单个文件，`page_idx` 重新校准到原 PDF 页码。下游 02 脚本完全感知不到拆分发生过。可用 `--max-pages-per-file 0` 关闭拆分。

> **`corpus/` 不入 git**：手册可能受版权限制，且生成的 markdown 体积大且可重生成；仓库只追踪 `context_layer/` 这一层 curated 产物。

---

### 角色 C：在你自己的项目里复用 `context_layer/`

你在做一个工程项目（比如 Sentaurus TCAD 仿真），希望 Claude Code 在那个项目里也能查手册——而不想把入库流程或 minerU 装到那个项目里。

最常见的两种模式：

1. **git submodule** 把本仓库挂到你项目的 `vendor/usermanual_context/`，随上游同步更新。
2. **直接复制** `context_layer/<software>/` 子集进你项目（适合网络受限或只用某一个软件）。

完整说明、CLAUDE.md 配置示例、最小工作示例见 [docs/use_in_other_projects.md](docs/use_in_other_projects.md)。

---

## 仓库结构

```text
software_usermanual_context/
  README.md                              你正在读
  ROADMAP.md                             开发者路线图（含当前活跃工作）
  AGENT.me                               智能体工作手册（硬规则、tier-based 加载顺序）
  CLAUDE.md                              薄壳，仅 `@AGENT.me`（Claude Code 自动加载入口）
  .claude/skills/software-manual-context/
    SKILL.md                             Skill 定义：渐进式披露 + 拒答规则
  context_layer/                         ★ 唯一入 git 的产物层 ★
    manifest.json                        所有文档的 tier / token / outputs 索引
    <software>/index.md                  软件级 router（多文档 / T3 软件才有）
    <software>/<doc>/full.md             原 markdown + 内联 <!-- page:N --> 锚点（T0+）
    <software>/<doc>/outline.md          章节树 + 规则摘要 + 关键词（T1+）
    <software>/<doc>/chapters/NN_*.md    按章节切分（T2+，每片 8–15K tokens）
  corpus/                                gitignored（PDF + 中间产物）
    raw/<software>/*.pdf                 原始 PDF（只读）
    markdown/<software>/<doc>/<doc>.md   人类可读的 markdown（抽查用）
    markdown/<software>/<doc>/<doc>_content_list.json  AI 阅读的结构化块列表（含 page_idx、bbox、type）
    markdown/<software>/.parts/...       超 200 页 PDF 的拆分中间产物（API 模式自动）
  scripts/
    01_pdf_to_markdown.py                PDF → Markdown 包装（local CLI / cloud API 两套）
    02_markdown_to_context.py            Markdown → context_layer（tier 化）
    lib/
      backend_detect.py                  GPU/CPU 自动判别
      mineru_runner.py                   本地 minerU CLI 包装
      mineru_api.py                      minerU 云端 API 客户端（含拆分+合并）
      pdf_split.py                       超长 PDF 拆分
      markdown_merge.py                  拆分后 markdown 合并、page_idx 重映射
      token_estimator.py                 tiktoken 估算
      page_anchor.py                     <!-- page:N --> 注入
      heading_parser.py                  标题树解析
      tier_classifier.py                 token → tier
      outline_builder.py                 规则摘要 + outline.md 生成
      chapter_splitter.py                T2/T3 章节切分
      manifest.py                        manifest.json 读写
  docs/
    install_mineru.md                    minerU 安装（Windows GPU/CPU + API token）
    add_new_software.md                  入库完整流程
```

---

## 技术栈

- **PDF → Markdown**：[minerU](https://github.com/opendatalab/MinerU)（local CLI / 云端 API 双引擎，可替换；02 脚本与 PDF 引擎解耦，见 [docs/add_new_software.md](docs/add_new_software.md) 末尾"如何换 PDF 引擎"）
- **拆分 / 合并**：纯 Python + `pypdf`（minerU 自带依赖）
- **Markdown → context_layer**：Python + `tiktoken`（估算 token 数）；无其它第三方依赖。**不引入** RAG / vector DB / embedding。
- **检索**：智能体用 Claude Code 内置 `rg/grep`。
- **运行时知识层**：Claude Code 通过项目级 Skill 加载

---

## 核心硬规则

完整规则在 [AGENT.me](AGENT.me) 和 [.claude/skills/software-manual-context/SKILL.md](.claude/skills/software-manual-context/SKILL.md)。摘要：

1. **R1 拒答规则**：用户问题在 `context_layer/` 找不到时，回答 **必须以「资料中无相关内容」开头**。可选附「**非手册内容**：」一段通用建议，明确标注是手册外推断。这条字面措辞不要随意改。
2. **R2**：`corpus/raw/` 是源 PDF，永远只读。
3. **R3**：`context_layer/` 里每个事实陈述都必须可回溯到 `full.md` / `chapters/*.md` 的原文片段 + page anchor，不允许猜测内容。
4. **R4**：新增软件必须走 `docs/add_new_software.md` 流程，不要让 LLM 凭空编造一个软件的 context_layer。

---

## 当前限制 & FAQ

**当前状态（参见 [ROADMAP.md](ROADMAP.md)）**：

- M0 设计确认进行中；M1 tier 化 context builder 待启动；M2 软件 router + 评测集；M3+ 探索 SQLite FTS5 / LLM 摘要 / RAG。
- 当前阶段不支持 RAG / vector DB / embedding 检索——智能体一律走 grep + outline。
- 仅支持英文手册（minerU `--lang en`）；中日韩手册需调 `--lang` 参数并验证 OCR 表现。

**FAQ**：

- *Q: 手册更新了（dakota 6.16 → 6.17）怎么办？* — 重跑 `01_pdf_to_markdown.py` + `02_markdown_to_context.py`。版本并存策略在 [ROADMAP.md](ROADMAP.md) Backlog。
- *Q: 我没装 minerU 也能用吗？* — 角色 A（查询）不需要装；角色 B（入库）需要。可选 minerU 云端 API 避开本地装模型，见 [docs/install_mineru.md](docs/install_mineru.md)。
- *Q: 可以替换 minerU 吗？* — 可以，[docs/add_new_software.md](docs/add_new_software.md) 末尾"如何换 PDF 引擎"详述了 02 与 minerU 解耦的契约。
- *Q: 为什么不上 RAG？* — 工程手册术语精确，`rg/grep` 在精确匹配场景胜过 embedding，且零依赖、零维护成本。RAG 推到 M3+，且仅在 grep + 章节切分被评测证明不够时引入。
- *Q: Cursor / Continue / 其他 IDE 能用吗？* — 暂时只支持 Claude Code。MCP server 化在 [ROADMAP.md](ROADMAP.md) backlog 中。

---

## 贡献 / 提问

- **想加新软件**：照 [docs/add_new_software.md](docs/add_new_software.md) 做。命名约定、抽查清单都在里面。
- **想改 SKILL/AGENT 规则**：先在 issue 里讨论；特别是「资料中无相关内容」拒答字符串不要随意改。
- **开发进度**：[ROADMAP.md](ROADMAP.md) 的 "Currently Working On" 区块。
- **未来方向**：MCP server 化、SQLite FTS5、LLM 章节摘要、RAG——都在 ROADMAP backlog。
