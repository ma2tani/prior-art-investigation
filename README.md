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
/prior-art full I want to use LLM outputs to train a smaller ML model
```

It returns:

- **The name** — "Knowledge Distillation" (a known research area since Hinton et al., 2015)
- **Research lineage** — Model compression → neural distillation → LLM distillation boom (2023+)
- **Existing OSS** — DistilBERT, LLaMA-Factory, Hugging Face transformers, with evaluation matrix
- **Known failure points** — Data quality dependency, teacher bias, training instability

---

## How to Use

| Mode | Use When | Output |
|------|----------|--------|
| `minimal` | Early concept check, before design | Concept name + quick OSS list + risk flags |
| `full` | Architecture decisions, new subsystem design | Research lineage + OSS matrix + tradeoffs + failure modes |
| `selector` | Not sure which to use | Auto-routes to minimal or full |

<details>
<summary><strong>Example: full mode output</strong></summary>

**Input**: `/prior-art full I want to use LLM outputs to train a smaller ML model`

**Concept**: Knowledge Distillation

> This technique has a 10+ year history. It started as a model compression method ([Hinton et al., 2015](https://arxiv.org/abs/1503.02531)), evolved through [DistilBERT](https://arxiv.org/abs/1910.01108) (2019) and [MiniLM](https://arxiv.org/abs/2002.10957) (2021), and exploded with LLM applications starting in 2023. Core insight: a small model can achieve 90% of performance at 10% of compute by learning from a large model's outputs and reasoning.

**Research lineage**:
| Year | Paper | Key Insight |
|------|-------|------------|
| 2015 | Hinton et al. ["Distilling the Knowledge in a Neural Network"](https://arxiv.org/abs/1503.02531) | Temperature-scaled softmax enables knowledge transfer |
| 2019 | Sanh et al. ["DistilBERT"](https://arxiv.org/abs/1910.01108) | BERT-scale distillation is practical |
| 2021 | Wang et al. ["MiniLM"](https://arxiv.org/abs/2002.10957) | Layer-wise matching improves small models |
| 2023 | Li et al. ["Distilling Step-by-Step"](https://arxiv.org/abs/2212.10071) | LLM reasoning can be distilled, not just outputs |
| 2024 | Zheng et al. ["LLaMA-Factory"](https://arxiv.org/abs/2403.13372) | Production-ready distillation pipelines |

**OSS Evaluation Matrix**:
| Tool | License | Maintainer | Updated | Data Prep | Best For | Source |
|------|---------|-----------|---------|-----------|----------|--------|
| Hugging Face transformers | Apache-2.0 | Hugging Face (org) | Active (weekly) | Low | Standard BERT-scale distillation | [GitHub](https://github.com/huggingface/transformers) |
| LLaMA-Factory | Apache-2.0 | HKUST / Tsinghua (academic org) | Active (monthly) | Medium | LLM distillation end-to-end | [GitHub](https://github.com/hiyouga/LLaMA-Factory) |
| Paper training code | Varies | Individual researchers | Stale | High | Research / custom architectures | [arXiv](https://arxiv.org/abs/2212.10071) |

**Key Risks**:
- **Teacher bias**: Small model inherits teacher's errors and biases
- **Data quality**: Without high-quality reasoning labels, distillation fails
- **Instability**: Temperature tuning and loss weighting are sensitive
- **Verify**: Always A/B test against direct training

</details>

---

## Quick Start

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

**One-time install, works across all your projects.** VS Code + Copilot Chat gains `/prior-art`. Add `#web` for live search beyond the training cutoff.

- Full setup (Kiro / Claude Desktop / Custom Agent) → [Setup Guide](docs/en/SETUP.md)
- Usage, reading output, when to skip → [Usage Guide](docs/en/USAGE.md)

---

**Version**: 1.1.0 | **License**: MIT

---

## Documentation

| | English | 日本語 |
|-|---------|--------|
| Overview | [README.md](./README.md) | [docs/ja/README.md](docs/ja/README.md) |
| Usage Guide (SDD workflow) | [docs/en/USAGE.md](docs/en/USAGE.md) | [docs/ja/USAGE.md](docs/ja/USAGE.md) |
| Setup Guide (installation) | [docs/en/SETUP.md](docs/en/SETUP.md) | [docs/ja/SETUP.md](docs/ja/SETUP.md) |
| Q1–Q8 Reference | [docs/en/QUESTIONS.md](docs/en/QUESTIONS.md) | [docs/ja/QUESTIONS.md](docs/ja/QUESTIONS.md) |

---

## License

MIT

- **GitHub**: https://github.com/as-we/prior-art-investigation
- **Release**: https://github.com/as-we/prior-art-investigation/releases/tag/v1.1.0
