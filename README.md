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
@prior-art-investigation full I want to use LLM outputs to train a smaller ML model
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

**Input**: `@prior-art-investigation full I want to use LLM outputs to train a smaller ML model`

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

## 3 Ways to Use

### 1. VS Code Copilot — 0 min setup

Copy `.instructions.md` to your Agent Skills folder:

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Linux
cp .instructions.md \
  ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md
```

Then use in Copilot Chat:

```
@prior-art-investigation minimal I need a real-time caching layer for our API
```

→ [Full setup guide](docs/en/AGENT-SKILLS-SETUP.md)

---

### 2. Claude Desktop (MCP) — 5 min setup

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "prior-art-investigation": {
      "command": "python3",
      "args": ["/path/to/prior-art-investigation/mcp/server_lite.py"]
    }
  }
}
```

Restart Claude Desktop → 3 tools available: `load_minimal`, `load_full`, `load_selector`.

→ [Full setup guide](docs/en/MCP-SETUP.md)

---

### 3. Kiro SDD — hooks & personalities

Copy directly into your project:

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

Prior art investigation runs automatically at requirements and design phases.

#### VS Code Copilot Chat: Hook Format & Disabling

The `.kiro/hooks/` directory includes both **Kiro IDE** format (`.json` with `enabled` flag) and **VS Code** format (`.kiro.hook` with `agentStop` trigger).

**VS Code setup** (copy `.kiro.hook` files, not `.json`):
```bash
cp .kiro/hooks/*.kiro.hook /your-project/.kiro/hooks/
```

**To disable in VS Code** (edit `enabled` flag):
```bash
# Disable requirements hook only
# Edit .kiro/hooks/prior-art-requirements.kiro.hook:
# Change "enabled": true to "enabled": false
# 
# The hook name will automatically change to show [DISABLED] status,
# and a lightweight skipping prompt will be used instead

# Disable design hook only  
# Edit .kiro/hooks/prior-art-design.kiro.hook:
# Change "enabled": true to "enabled": false

# Re-enable
# Change "enabled": false back to "enabled": true
```

**Note**: VS Code hooks use `agentStop` trigger + git diff detection (checks if `requirements.md` or `design.md` changed). Kiro IDE hooks use command-specific triggers (`after_kiro_spec_requirements`, `after_kiro_spec_design`).

---

## Optional: Control Hook Execution

Each prior art investigation increases token consumption. You can disable hooks for contexts where investigation is not needed:

### Disable hooks
1. Open `.kiro/hooks/prior-art-requirements.json`
2. Change `"enabled": true` to `"enabled": false`
3. Repeat for `.kiro/hooks/prior-art-design.json`

### When to disable
- **Maintenance / refactoring** — existing codebase, no new paradigms
- **Well-known patterns** — already familiar, investigation not needed
- **Token budget constraint** — running multiple investigations in parallel

### When to keep enabled
- **Greenfield / zero-to-one projects** — unknown territory, high discovery value
- **Major architecture decisions** — new subsystem design, new dependency selection
- **Technology selection** — choosing between OSS options

---

## Personalities (Kiro SDD)

Switch investigation focus by selecting a personality:

| Personality | Focus |
|-------------|-------|
| `researcher` | Academic papers, citations, prior research |
| `startup-hunter` | Market validation, competitor analysis, startup trends |
| `tech-auditor` | Technical depth, architecture, engineering best practices |
| `patent-search` | IP risk, patent landscape, prior art claims |
| `team-internal` | Internal knowledge, existing docs, in-house patterns |

---

## Customization

Extend the framework by adding your own personalities, modes, or integration hooks.

See `.kiro/personalities/` and `.kiro/hooks/` for examples.

---

## Documentation

Language-specific setup guides:

| | English | 日本語 |
|-|---------|--------|
| VS Code setup | [docs/en/AGENT-SKILLS-SETUP.md](docs/en/AGENT-SKILLS-SETUP.md) | [docs/ja/AGENT-SKILLS-SETUP.md](docs/ja/AGENT-SKILLS-SETUP.md) |
| Claude setup | [docs/en/MCP-SETUP.md](docs/en/MCP-SETUP.md) | [docs/ja/MCP-SETUP.md](docs/ja/MCP-SETUP.md) |

---

## License

MIT

- **GitHub**: https://github.com/as-we/prior-art-investigation
- **Release**: https://github.com/as-we/prior-art-investigation/releases/tag/v1.0.0
