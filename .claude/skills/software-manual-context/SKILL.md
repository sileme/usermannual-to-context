---
name: software-manual-context
description: Answer questions about engineering software (currently Dakota and Sentaurus TCAD) using their official user manuals. Use when the user asks how to do something in the software, what a command/keyword/parameter means, what an error or warning indicates, what modules exist, or any "how do I X in <software>" question. Loads a per-software router and per-document outline first, then drills into specific chapters and grep hits on demand. MUST refuse to invent any content not present in the loaded manual context.
---

# software-manual-context

Manual-backed Q&A for registered engineering software. Source of truth: `context_layer/<software>/<doc>/full.md` (and, for T2+ docs, `chapters/*.md`).

## R1 — Hard refusal rule

If the user's question is **not covered** by the loaded `context_layer/`, your reply MUST start with the literal line:

```
资料中无相关内容
```

Optionally followed by one paragraph beginning with `**非手册内容**：` containing general advice clearly labeled as outside the manual. Never paraphrase manual content you have not actually loaded. Outline summaries are navigation only — they do **not** count as "loaded manual content".

## Registered software

Read `context_layer/manifest.json` for the canonical, up-to-date list of all documents and their tiers. As of this writing:

- **dakota** — `dakota_Users-6.16.0.pdf`. Optimization, UQ, sensitivity analysis. Single user manual.
- **sentaurus** — 30 user guides for the Sentaurus TCAD suite (sdevice, sprocess, svisual, swb, etc.). Each guide is a separate `<doc>/` under `context_layer/sentaurus/`.

If the user asks about a software not in `context_layer/manifest.json`, respond with R1.

## Tier model

Every document has a tier recorded in `context_layer/manifest.json`. Tier dictates which outputs exist and the loading strategy:

| Tier | Estimated tokens | Outputs | Strategy |
|---|---|---|---|
| T0 | < 12K | `full.md` | Read `full.md` directly (cheap). |
| T1 | 12K – 80K | `full.md` + `outline.md` | Read `outline.md` → grep keywords in `full.md` → read hit region. |
| T2 | 80K – 350K | `full.md` + `outline.md` + `chapters/NN_*.md` | Read `outline.md` → pick chapter → read only that `chapters/NN_*.md`. |
| T3 | > 350K single-doc, or > 500K per-software total | Same as T2 + per-software `index.md` router | Always read `context_layer/<software>/index.md` first to route. |

**Never read `full.md` directly for T2/T3 documents.** It exists only as a grep fallback, not for sequential reading.

## Progressive disclosure protocol

Walk this ladder, stopping at the rung that answers the question:

1. **Identify software** from the user's question. If ambiguous, ask.
2. **Load manifest entry**: read `context_layer/manifest.json` for that software's docs and their tiers.
3. **Router (multi-doc / T3 only)**: read `context_layer/<software>/index.md` to pick the doc.
4. **Document outline (T1+)**: read `context_layer/<software>/<doc>/outline.md` to locate the chapter / topic.
5. **Drill in**:
   - T0: read `full.md` straight through.
   - T1: `grep` keyword in `full.md`, read ±50 lines around hits.
   - T2/T3: read the single `chapters/NN_*.md` indicated by the outline; if needed, `grep` within that chapter.
6. **Confirm in source**: any factual statement must come from an actual passage in `full.md` or `chapters/*.md` — not from the outline summary.
7. **Cite** every factual claim with `[<doc> p.<n>]`. Page numbers come from the **nearest `<!-- page:N -->` HTML comment above the cited passage** in the markdown.

## Refusal template

```
资料中无相关内容

**非手册内容**：<one short paragraph of general advice, labeled as outside the manual. Optional. Skip if you have nothing useful to add.>
```

## Examples

### Positive — T1 path

User: "Dakota 跑参数扫描需要哪些 input 段？"

Action: manifest → dakota single doc (T1) → read `outline.md` → locate "Parameter Study" section → grep `multidim_parameter_study` in `full.md` → read hit region with nearest page anchor.

Reply (skeleton):
> Dakota 输入文件按 method / variables / interface / responses 四段组织 [dakota_Users-6.16.0 p.32]。扫描的核心是 method 段的 `multidim_parameter_study` 等关键字 [p.215]……

### Positive — T2 path

User: "Sentaurus sdevice 里 Physics{} 段怎么开 SRH recombination？"

Action: manifest → sentaurus/sdevice_ug (T2) → read `outline.md` → locate "Physics > Recombination" → read `chapters/NN_physics.md` → grep `Recombination(SRH)` within the chapter.

Reply (skeleton):
> 在 `Physics{}` 段里加 `Recombination(SRH)`，可附 `(DopingDep)` 等修饰符开启浓度依赖 [sdevice_ug p.143]。

### Negative — refusal

User: "Dakota 怎么对接 ANSYS Fluent？"

Action: grep `Fluent` in `context_layer/dakota/` → no hit. Outline mentions "Interfaces" chapter but no Fluent-specific content found.

Reply:
> 资料中无相关内容
>
> **非手册内容**：Dakota 通过通用 black-box 接口（`analysis_driver`）与外部 CAE 工具耦合，理论上可调任何能命令行驱动的求解器；具体到 Fluent 通常需要写 journal 脚本 + 文件交换中间层。建议查 `dakota_Users-6.16.0.pdf` 的 "Interfaces" 章节确认参数传递格式。
