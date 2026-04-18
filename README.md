# Prior Art Investigation Framework

**[日本語](docs/ja/README.md)**

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
|------|----------|---------|
| **minimal** | Early concept check, before design | Concept name + quick OSS list + risk flags |
| **full** | Architecture decisions, new subsystem design | Research lineage + OSS matrix + tradeoffs + failure modes |
| **selector** | Not sure which to use | Auto-routes to minimal or full |

<details>
<summary><strong>Example: Full investigation output</strong></summary>

**Input**: `@prior-art full I want to use LLM outputs to train a smaller ML model`

**Output**:

**Concept**: Knowledge Distillation

> This technique has a 10+ year history. It started as a model compression method ([Hinton et al., 2015](https://arxiv.org/abs/1503.02531): "Distilling the Knowledge in a Neural Network"), evolved through [DistilBERT](https://arxiv.org/abs/1910.01108) (2019), [MiniLM](https://arxiv.org/abs/2002.10957) (2021), and exploded with LLM applications starting in 2023. The core insight: a small model can learn from a large model's outputs + reasoning, achieving 90% of performance at 10% of compute.

**Research lineage**:
| Year | Paper | Key Insight |
|------|-------|------------|
| 2015 | Hinton et al. ["Distilling the Knowledge in a Neural Network"](https://arxiv.org/abs/1503.02531) | Temperature-scaled softmax enables knowledge transfer |
| 2019 | Sanh et al. ["DistilBERT"](https://arxiv.org/abs/1910.01108) | BERT-scale distillation is practical |
| 2021 | Wang et al. ["MiniLM"](https://arxiv.org/abs/2002.10957) | Layer-wise intermediate matching improves small models |
| 2023 | Li et al. ["Distilling Step-by-Step"](https://arxiv.org/abs/2212.10071) | LLM reasoning can be distilled, not just outputs |
| 2024 | Zheng et al. ["LLaMA-Factory"](https://arxiv.org/abs/2403.13372) | Production-ready distillation pipelines |

**OSS Evaluation Matrix**:
| Tool | License | Maintainer | Updated | Data Prep | Best For | Source |
|------|---------|-----------|---------|-----------|----------|--------|
| Hugging Face transformers | Apache-2.0 | Hugging Face (org) | Active (weekly) | Low | Standard BERT-scale distillation | [GitHub](https://github.com/huggingface/transformers) |
| LLaMA-Factory | Apache-2.0 | HKUST / Tsinghua (academic org) | Active (monthly) | Medium | LLM distillation end-to-end | [GitHub](https://github.com/hiyouga/LLaMA-Factory) |
| Paper training code | Varies | Individual researchers | Stale | High | Research / custom architectures | [arXiv](https://arxiv.org/abs/2212.10071) |

**Key Risks**:
- **Teacher bias**: Small model inherits teacher's errors + biases
- **Data quality**: Without high-quality reasoning labels, distillation fails
- **Instability**: Temperature tuning and loss weighting are sensitive
- **Verify**: Always A/B test against direct training on data

</details>

---

## Quick Install

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

`make install` sets up both layers below. One-time, user-scoped — works across all your projects.

---

## How to Use

### Layer 1 — Agent Skills: explicit invocation

Install once → available in every project:

```bash
make install-skills
# or manually:
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md
```

Then call on demand in Copilot Chat:

```
@prior-art full I want to use LLM outputs to train a smaller ML model
@prior-art minimal I need a real-time caching layer
@prior-art selector  ← auto-routes to minimal or full
```

**Works across**: VS Code Copilot Chat, Kiro IDE, Cursor, Windsurf.
**Token cost**: only when you explicitly call it.

→ [Full VS Code setup](docs/en/SETUP.md)

---

### Layer 2 — Auto-detect hook: zero-effort reminders

A `UserPromptSubmit` hook watches your prompts and injects a one-line reminder when the message looks like a design or architecture decision — **no LLM involved, deterministic shell match**.

Install once → active in every session:

```bash
make install-hook
```

Then in VS Code settings, enable user-scoped hooks:
```json
"chat.hookFilesLocations": { "~/.copilot/hooks": true }
```

**What it does**: when your prompt contains words like `design`, `architecture`, `requirements.md`, `/kiro-spec-design`, `設計`, `実装`, etc. — you see:

> 💡 Prior art check recommended: this looks like a design or implementation decision. Before building, consider running: `@prior-art full <topic>`

**Token cost**: near-zero (the hook itself runs a shell script, not an LLM).

The hook lives at `~/.copilot/hooks/` — it does **not** pollute your project files.

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

→ [Full Claude setup](docs/en/SETUP.md#c-mcp-server-claude-desktop--other-clients)

---

### Layer 4 — VS Code Custom Agent (per-project)

The `.github/agents/prior-art.agent.md` file in this repo works as a workspace-scoped agent for VS Code Copilot Chat.

**In your project** — copy the agent file:

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Select **Prior Art Investigation** from the Copilot Chat dropdown when needed.

> Use this layer when you want per-project control over when investigation runs, or want to share the agent config with your team via the repository.

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

Layer 2 fires only when keywords match — no full investigation, just a reminder. Only use `make uninstall-hook` if you find it distracting:

```bash
# Remove user-scope auto-detect hook
rm ~/.copilot/hooks/prior-art-detect.json
rm ~/.copilot/hooks/scripts/prior-art-detect.sh
```

**When the full investigation adds value:**
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
| `platform-expert` | IDE/runtime native APIs, platform hooks, SDK capabilities — avoids re-inventing what the platform already provides | — |

Configured via the `personality` field in `.kiro/hooks/*.json`. See [docs/en/SETUP.md § Personalities](docs/en/SETUP.md#d-kiro-ide--hooks--personalities) for details.

---

## Documentation

| | English | 日本語 |
|-|---------|--------|
| Overview | [docs/en/README.md](docs/en/README.md) | [docs/ja/README.md](docs/ja/README.md) |
| Setup guide | [docs/en/SETUP.md](docs/en/SETUP.md) | [docs/ja/SETUP.md](docs/ja/SETUP.md) |
| Q1–8 reference | [docs/en/QUESTIONS.md](docs/en/QUESTIONS.md) | [docs/ja/QUESTIONS.md](docs/ja/QUESTIONS.md) |

---


## License

MIT

- **GitHub**: https://github.com/as-we/prior-art-investigation
- **Release**: https://github.com/as-we/prior-art-investigation/releases/tag/v1.1.0
