# 在其他项目中使用 `context_layer/`

本仓库的核心产物是 `context_layer/`——已 tier 化、内联了 PDF 页码锚点的工程软件手册知识层。其他项目（例如某个 Sentaurus TCAD 仿真工程）可以**直接复用**这份产物，让 Claude Code 在那个项目里也具备"手册查询助理"能力。

本文给消费方读：你想在自己的项目里查 dakota/sentaurus 用法，但不想关心 PDF→markdown 入库流程。

---

## 三种消费模式

### 模式 A：git submodule（推荐）

适合：希望随上游同步更新、不想手动维护副本。

```bash
# 在你的项目根目录
git submodule add https://<host>/software_usermanual_context.git vendor/usermanual_context
git submodule update --init
```

然后让 Claude Code 知道这层手册存在。在你项目的 `CLAUDE.md` 里加入：

```markdown
# 你项目的 CLAUDE.md（追加这一段）

## 工程软件手册
本项目使用的 dakota / sentaurus 等工程软件，手册查询通过子模块 `vendor/usermanual_context/` 提供：

- 阅读其 [vendor/usermanual_context/AGENT.me](vendor/usermanual_context/AGENT.me) 获取查询协议。
- 手册产物在 `vendor/usermanual_context/context_layer/`。
- manifest 在 `vendor/usermanual_context/context_layer/manifest.json`。
- 路径全部相对你项目的根目录。
```

> **路径注意**：当前的 `AGENT.me` 用的是仓库根相对路径（`context_layer/...`）。consumer 在引用前缀 `vendor/usermanual_context/` 时，需要在自己的 CLAUDE.md 里**明示完整路径前缀**，否则 Claude Code 会在你项目根找不到 `context_layer/`。

升级上游：

```bash
cd vendor/usermanual_context
git pull
cd ../..
git add vendor/usermanual_context
git commit -m "bump usermanual_context"
```

### 模式 B：直接复制 context_layer 子集

适合：消费方只用某个软件（比如只用 sentaurus），不想引入整个仓库；或网络受限无法 submodule。

```bash
# 在你的项目根目录
mkdir -p vendor/usermanual_context/context_layer
cp -r /path/to/software_usermanual_context/context_layer/sentaurus \
      vendor/usermanual_context/context_layer/
cp /path/to/software_usermanual_context/context_layer/manifest.json \
      vendor/usermanual_context/context_layer/
cp /path/to/software_usermanual_context/AGENT.me vendor/usermanual_context/
```

`manifest.json` 里其它软件的条目可选择性删除。

CLAUDE.md 的引用方式同模式 A。

### 模式 C：MCP server（M3 backlog，尚未实现）

未来计划把 SKILL 工作流封装为 MCP server，consumer 只需在自己的 MCP 配置里指向本仓库，无需复制文件。进度看 [ROADMAP.md](../ROADMAP.md) Backlog 段「MCP server 化」。

---

## 消费方必读：硬规则

无论用哪种模式，消费 `context_layer/` 时**必须**遵守：

1. **R1 拒答规则**：手册未覆盖的内容，Claude Code 的回答必须以「资料中无相关内容」开头。这条字面措辞不要本地化。详见 [AGENT.me](../AGENT.me)。
2. **页码锚点引用**：所有事实陈述附 `[<doc> p.<n>]`，页码取自 `<!-- page:N -->` HTML 注释。
3. **不要修改 `context_layer/` 内容**：如果你发现手册有缺失或错误，请回到上游仓库提 issue 或 PR，不要在你的项目里 local patch——consumer 端的修改不会被上游感知，也不会经过质量审核。
4. **manifest 单一来源**：`context_layer/manifest.json` 是判断"某文档存在 / tier / outputs 是什么"的唯一权威。consumer 不要自己维护一份。

---

## 最小工作示例

假设你在做 sentaurus sdevice 仿真，项目结构如下：

```
my_tcad_project/
  CLAUDE.md                              ← 你项目的 Claude Code 入口
  inputs/
    nmos.cmd                             ← 你写的 sdevice 命令文件
  vendor/
    usermanual_context/                  ← git submodule
      AGENT.me
      context_layer/
        sentaurus/sdevice_ug/
          full.md
          outline.md
        manifest.json
```

你项目的 `CLAUDE.md`：

```markdown
# my_tcad_project

## 工程软件手册
手册查询见 [vendor/usermanual_context/AGENT.me](vendor/usermanual_context/AGENT.me)。
所有 `context_layer/<software>/...` 路径请前缀 `vendor/usermanual_context/`。
```

提问示例：

```
你> 我 nmos.cmd 里 Physics{} 段加 Recombination(SRH) 报 token mismatch，怎么排查？

Claude>
  1. 读 vendor/usermanual_context/context_layer/manifest.json
     → sdevice_ug 是 T3
  2. 读 vendor/usermanual_context/context_layer/sentaurus/sdevice_ug/outline.md
     → 定位 "Physics" / "Recombination" 章节
  3. grep "Recombination(SRH)" vendor/usermanual_context/context_layer/sentaurus/sdevice_ug/full.md
     → 读命中片段附近 ±50 行
  4. 回答 + 引用 [sdevice_ug p.143]
```

---

## 当前限制（与上游 ROADMAP 同步）

- T2/T3 文档目前**只产** `full.md` + `outline.md`，没有 `chapters/`。consumer 在 grep T2/T3 的 `full.md` 时可能加载较多 token。M1 后续会补 `chapters/*.md`。
- T3 软件（如 sentaurus）**尚无** `<software>/index.md` 路由器。consumer 多文档软件查询时需要自己根据 `manifest.json` 选择 doc。M2 会补上。
- 检索仅靠 `rg/grep`，不提供 RAG / vector / embedding。

---

## 反馈

- bug / 手册缺漏 / 新软件入库请求：回上游仓库提 issue。
- consumer 端常见使用问题：先看 [README.md](../README.md) FAQ，再提 issue。
