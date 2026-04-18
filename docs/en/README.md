# Prior Art Investigation Framework

**[日本語](../ja/README.md)**

---

## What It Does

With spec-driven development (SDD), you can move from idea to implementation using plain problem statements.

For example:
> "I want to use an LLM to generate reasoning explanations, then train a smaller ML model on those outputs."

That single sentence is enough to drive requirements, design, and implementation. **But there's a blind spot.**

A well-established research field called "Knowledge Distillation" already exists — with 10+ years of papers, OSS tools, and documented failure patterns. Without knowing that term, you'd rebuild it from scratch, convinced you invented it.

**This framework eliminates that blind spot before you start designing.**

```
@prior-art full I want to use LLM outputs to train a smaller ML model
```

It returns:

- **The name** — "Knowledge Distillation" (a known research area since Hinton et al., 2015)
- **Research lineage** — Model compression → neural distillation → LLM distillation boom (2023+)
- **Existing OSS** — DistilBERT, LLaMA-Factory, Hugging Face transformers, with evaluation matrix
- **Known failure points** — Data quality dependency, teacher bias, training instability

---

## How It Works

| Mode | Use When | Output |
|------|----------|--------|
| **minimal** | Early concept check, before design | Concept name + quick OSS list + risk flags |
| **full** | Architecture decisions, new subsystem design | Research lineage + OSS matrix + tradeoffs + failure modes |
| **selector** | Not sure which to use | Auto-routes to minimal or full |

<details>
<summary><strong>Example: Full investigation output</strong></summary>

**Input**: `@prior-art full I want to use LLM outputs to train a smaller ML model`

**Concept**: Knowledge Distillation

> This technique has a 10+ year history. It started as a model compression method ([Hinton et al., 2015](https://arxiv.org/abs/1503.02531)), evolved through [DistilBERT](https://arxiv.org/abs/1910.01108) (2019) and [MiniLM](https://arxiv.org/abs/2002.10957) (2021), and exploded with LLM applications starting in 2023. Core insight: a small model can achieve 90% of performance at 10% of compute by learning from a large model's outputs and reasoning.

**Research lineage**:
| Year | Paper | Key Insight |
|------|-------|------------|
| 2015 | [Hinton et al.](https://arxiv.org/abs/1503.02531) | Temperature-scaled softmax enables knowledge transfer |
| 2019 | [Sanh et al. "DistilBERT"](https://arxiv.org/abs/1910.01108) | BERT-scale distillation is practical |
| 2023 | [Li et al. "Distilling Step-by-Step"](https://arxiv.org/abs/2212.10071) | LLM reasoning can be distilled, not just outputs |
| 2024 | [Zheng et al. "LLaMA-Factory"](https://arxiv.org/abs/2403.13372) | Production-ready distillation pipelines |

**OSS Evaluation Matrix**:
| Tool | License | Maintainer | Updated | Best For | Source |
|------|---------|-----------|---------|----------|--------|
| Hugging Face transformers | Apache-2.0 | Hugging Face (org) | Active (weekly) | Standard BERT-scale distillation | [GitHub](https://github.com/huggingface/transformers) |
| LLaMA-Factory | Apache-2.0 | HKUST / Tsinghua (academic org) | Active (monthly) | LLM distillation end-to-end | [GitHub](https://github.com/hiyouga/LLaMA-Factory) |

**Key Risks**:
- **Teacher bias**: Small model inherits teacher's errors and biases
- **Data quality**: Without high-quality reasoning labels, distillation fails
- **Instability**: Temperature tuning and loss weighting are sensitive

</details>

---

## How to Use

### A. VS Code Custom Agent — zero setup (recommended)

> Requires: VS Code + GitHub Copilot Chat

This repository includes `.github/agents/prior-art.agent.md`, a **VS Code Custom Agent** file (introduced in VS Code 1.99 / April 2025, schema updated April 2026).

**In this repository** — just select from the Copilot Chat dropdown:

1. Open Copilot Chat (`⌃⌘I`)
2. Agent selector → choose **Prior Art Investigation**
3. It auto-checks `git diff HEAD` and runs investigation if spec files have changed

**In your own project** — copy the agent file:

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Copilot Chat dropdown → **Prior Art Investigation**, done.

> **Note**: `.chatmode.md` is the old format (deprecated). VS Code 1.99+ uses `.github/agents/*.agent.md`. Rename any old `.chatmode.md` files.

---

### B. VS Code Agent Skills (cross-workspace) — 2 minutes

**Use this when you want to call it across multiple projects.** Copy `.instructions.md` to the Agent Skills folder and restart VS Code:

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md
```

Use in Copilot Chat:

```
@prior-art minimal I need a real-time search feature
```

→ [Full setup guide](./SETUP.md)

---

## Quick Install

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

`make install` sets up both layers below. **One-time install, works across all your projects.**

---

## How to Use

### Layer 1 — Agent Skills: explicit invocation

Install once → available in every project:

```bash
make install-skills
```

Call from Copilot Chat:

```
@prior-art full I want to use LLM outputs to train a smaller ML model
@prior-art minimal I need a real-time caching layer
@prior-art selector  ← auto-routes to minimal or full
```

**Works across**: VS Code Copilot Chat, Kiro IDE, Cursor, Windsurf.  
**Token cost**: only when you explicitly call it.

→ [Full setup guide](./SETUP.md)

---

### Layer 2 — Auto-detect hook: zero-effort reminders

A `UserPromptSubmit` hook watches your prompts and injects a one-line reminder when the message looks like a design or architecture decision — **no LLM involved, deterministic shell match**.

```bash
make install-hook
```

Then in VS Code settings:
```json
"chat.hookFilesLocations": { "~/.copilot/hooks": true }
```

**What it does**: when your prompt contains words like `design`, `architecture`, `requirements.md`, `/kiro-spec-design`, `設計`, etc. — you see:

> 💡 Prior art check recommended: this looks like a design or implementation decision. Before building, consider running: `@prior-art full <topic>`

**Token cost**: near-zero (shell script, no LLM).  
Hook lives at `~/.copilot/hooks/` — **does not pollute your project files**.

---

### Layer 3 — MCP server: Claude Desktop / other clients

```json
{
  "mcpServers": {
    "prior-art": {
      "command": "python3",
      "args": ["/path/to/prior-art-investigation/mcp/server_lite.py"]
    }
  }
}
```

Restart Claude Desktop → 3 tools available: `load_minimal`, `load_full`, `load_selector`.

→ [Full Claude Desktop setup](./SETUP.md#c-claude-desktop-mcp-server)

---

### Layer 4 — VS Code Custom Agent (per-project)

Copy the agent file into your project:

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Select **Prior Art Investigation** from the Copilot Chat dropdown.

> Use this layer when you want per-project control, or want to share the agent config with your team via the repository.

---

### Layer 5 — Kiro SDD hooks (per-project, Kiro IDE)

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

Kiro IDE triggers investigation automatically at requirements and design phases (`after_kiro_spec_requirements`, `after_kiro_spec_design`).

VS Code `.kiro.hook` files are included as well (disabled by default — Layer 2 is recommended instead).

---

## Optional: Control Hook Execution

Layer 2 fires only when keywords match — no full investigation, just a reminder.

```bash
# Remove auto-detect hook
rm ~/.copilot/hooks/prior-art-detect.json
rm ~/.copilot/hooks/scripts/prior-art-detect.sh
```

**When full investigation adds value:**
- Greenfield / zero-to-one — unknown territory, high discovery value
- Architecture decisions — new subsystem, new dependency, technology selection

**When to skip:**
- Maintenance / refactoring — existing codebase, no new paradigms
- Well-known domains — already familiar with the space

---

## Personalities (Kiro SDD)

Personalities control **which angle to investigate from** and are used by Kiro SDD hooks. Different phases use different defaults.

| Personality | Focus | Kiro Default Phase |
|-------------|-------|-------------------|
| `startup-hunter` | Market validation, competitor analysis, startup trends | Requirements |
| `tech-auditor` | Technical depth, architecture, engineering best practices | Design |
| `researcher` | Academic papers, citations, prior research | — |
| `patent-search` | IP risk, patent landscape, prior art claims | — |
| `team-internal` | Internal knowledge, existing docs, in-house patterns | — |
| `platform-expert` | IDE/runtime native APIs, platform hooks, SDK capabilities — avoids re-inventing what the platform provides | — |

Configured via the `personality` field in `.kiro/hooks/*.json`. See [SETUP.md § Personalities](./SETUP.md#d-kiro-ide--hooks--personalities) for details.

---

## Customization

### Question Framework (Q1–Q8)

`minimal` uses Q1 (first principles) + Q6 (inversion) only.  
`full` uses all Q1–Q8. Q8 specifically checks platform-native capabilities (IDE, SDK, runtime).

Edit `.instructions.md` directly to modify question content.

→ [Q1–Q8 detailed reference](./QUESTIONS.md)

### Personality Customization

Add a JSON file to `.kiro/personalities/`:

```json
{
  "name": "my-custom",
  "label": "My Custom Researcher",
  "description": "Focus on ...",
  "questions": ["What ...?", "Are there ...?"],
  "web_sources": ["GitHub", "arXiv"]
}
```

→ Full details (hook config, env var, custom examples) in [SETUP.md](./SETUP.md).

---

**Version**: 1.1.0 | **License**: MIT
