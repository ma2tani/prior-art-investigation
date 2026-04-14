# Prior Art Investigation Framework — v1.0.0

> Quickly identify if your feature concept already exists, what it's called, and what OSS solutions are available — **before** you write code.

---

## What Problem Does This Solve?

When designing features, it's easy to describe novel solutions without knowing they already have:
- **Established names** — "LLM inference → lightweight ML" = *Knowledge Distillation*
- **Known failure modes** — "Retry with backoff" = *Circuit Breaker pattern*
- **Reference implementations** — "Read/write model split" = *CQRS*
- **Existing OSS** — Someone already solved this

Identifying the concept **before** coding unlocks best practices, known tradeoffs, and ready-to-use solutions.

---

## 🚀 Get Started (3 Options)

### Option 1: VS Code Copilot (Fastest)
```
@prior-art-investigation minimal
I need real-time groove recommendations
```
**Setup time**: 0 minutes | **Execution**: 5-10 min | **Cost**: ~150 tokens

---

### Option 2: Claude Desktop (MCP Server)
```bash
# 1. Setup config (5 min)
# ~/.../Claude/claude_desktop_config.json
{
  "mcpServers": {
    "prior-art-investigation": {
      "command": "python3",
      "args": ["/path/to/mcp/server_lite.py"]
    }
  }
}

# 2. Restart Claude Desktop
# 3. Use tools: @prior-art-investigation load_minimal, load_full, load_selector
```
**Setup time**: 5 minutes | **Tools**: 3 (load_minimal, load_full, load_selector)

---

### Option 3: npm Package (Programmatic)
```bash
npm install @ma2tani/prior-art-investigation

import minimalPrompt from '@ma2tani/prior-art-investigation/prompts/minimal';
```
**Setup time**: 1 minute | **Use**: Node.js, bundlers, pipelines

---

## 📊 Framework Overview

| Phase | Prompt | Time | Tokens | Questions |
|-------|--------|------|--------|-----------|
| **Requirements** | MINIMAL | 5-10 min | ~150 | Q1, Q6 |
| **Design** | FULL | 20-40 min | ~500 | Q1-Q7 |
| **Unsure** | SELECTOR | 1-2 min | ~100 | Auto-routes |

**Token Reduction**: MINIMAL achieves **70% reduction** vs FULL (150 vs 500 tokens)

---

## 📚 Documentation Structure

```
docs/en/
├── README.md                           ← This file
├── NAVIGATION.md                       ← Discovery hub
├── AGENT-SKILLS-USAGE.md              ← VS Code Copilot guide
├── CLAUDE-DESKTOP-SETUP.md            ← MCP server setup
├── AGENT-SKILLS-SETUP.md              ← Agent Skills integration
├── setup-checklist.md                 ← Installation steps
├── templates/
│   └── research.md                    ← Output template
├── github/
│   └── prompts/
│       ├── minimal.prompt.md          ← Q1+Q6 framework
│       ├── full.prompt.md             ← Q1-Q7 framework
│       └── selector.prompt.md         ← Auto-routing
└── kiro/
    └── settings/
        └── rules/
            └── oss-evaluation.md      ← OSS framework
```

---

## ✨ Key Features (v1.0.0)

- ✅ **Phase-split prompts** — MINIMAL / FULL / SELECTOR (3 options)
- ✅ **70% token reduction** — MINIMAL uses only 150 tokens (vs 500 full)
- ✅ **3 distribution channels** — Agent Skills / MCP / npm
- ✅ **Zero dependencies** — MCP server uses Python stdlib
- ✅ **Bilingual** — English + 日本語
- ✅ **Kiro SDD compatible** — Outputs save to `.kiro/specs/`
- ✅ **Production ready** — Tested, documented, deployed

---

## 🎯 Which Prompt to Use?

### MINIMAL (Requirements Phase)
**Use when**: You have a problem statement and need quick validation  
**Questions**: Q1 (First Principles) + Q6 (Inversion/Risks)  
**Time**: 5-10 minutes  
**Tokens**: ~150  
**Output**: Concept name confirmed + key risks identified

### FULL (Design Phase)
**Use when**: Designing architecture or new subsystem  
**Questions**: Q1-Q7 complete investigation  
**Time**: 20-40 minutes  
**Tokens**: ~500  
**Output**: Concept name + OSS options + architecture decisions + risks

### SELECTOR (Unsure Which Phase)
**Use when**: Not sure which phase you're in  
**Questions**: Automatic routing questions  
**Time**: 1-2 minutes  
**Tokens**: ~100  
**Output**: Recommendation to run MINIMAL or FULL

---

## 📖 Navigation

**For different roles:**
- **Product managers**: [NAVIGATION.md](./NAVIGATION.md) → MINIMAL prompt
- **Architects**: [NAVIGATION.md](./NAVIGATION.md) → FULL prompt
- **VS Code users**: [AGENT-SKILLS-USAGE.md](./AGENT-SKILLS-USAGE.md)
- **Claude Desktop users**: [CLAUDE-DESKTOP-SETUP.md](./CLAUDE-DESKTOP-SETUP.md)
- **Kiro SDD teams**: See integration in [MCP-SETUP.md](./MCP-SETUP.md#kiro-sdd-integration)

---

## ✅ Supported Platforms

| Platform | Status | Setup | Integration |
|----------|--------|-------|-------------|
| **VS Code Copilot** | ✅ Ready | 0 min | Agent Skills |
| **Claude Desktop** | ✅ Ready | 5 min | MCP server |
| **ChatGPT / Claude.ai** | ✅ Works | n/a | Copy/paste |
| **npm** | ✅ Ready | 1 min | `npm install` |
| **Kiro SDD** | ✅ Compatible | n/a | Phase integration |

---

## 📈 Roadmap

**v1.0.0** (Current)
- ✅ Phase-split prompts (MINIMAL/FULL/SELECTOR)
- ✅ Agent Skills support
- ✅ MCP server implementation
- ✅ npm distribution

**v1.1.0** (Q2 2026)
- [ ] Smithery MCP registry
- [ ] Docker container
- [ ] GitHub Actions CI for token measurement
- [ ] Community feedback integration

**v1.2.0** (Q3 2026)
- [ ] Advanced Agent Skills personality
- [ ] Kiro SDD deep integration
- [ ] Workspace auto-save

---

## 🔗 Quick Links

- **Full Navigation**: [NAVIGATION.md](NAVIGATION.md)
- **Release Notes**: [RELEASE.md](../RELEASE.md)
- **CHANGELOG**: [CHANGELOG.md](../CHANGELOG.md)
- **GitHub Repo**: https://github.com/ma2tani/prior-art-investigation
- **npm Package**: https://www.npmjs.com/package/@ma2tani/prior-art-investigation

---

## 💡 Examples

### Example 1: Quick Requirements Check (5 min)
```
User: "@prior-art-investigation minimal We need real-time metrics dashboards"

Agent:
- Q1 First Principles: Are you solving "metrics visualization" or "real-time data sync"?
- Q6 Risks: Latency assumption. Verify: Can data refresh in <1 sec?
- Concept: "Real-time dashboard" or "Live analytics"
- Options: Databricks, Grafana, Tableau
- Status: Ready for design phase ✓
```

### Example 2: Deep Architecture Research (20 min)
```
User: "@prior-art-investigation full Designing ML-based rhythm detection"

Agent: (Q1-Q7 investigation)
- Concept: "Onset detection" or "Beat tracking"
- Existing OSS: librosa, madmom, essentia
- Architecture: Batch vs real-time tradeoffs
- Risks: Model accuracy, latency, versioning
- Recommendation: Start with librosa baseline
- Status: Save to .kiro/specs/rhythm-detection/docs/research.md ✓
```

---

## 📝 License

MIT

---

**Version**: 1.0.0  
**Status**: Production Ready ✅  
**Last Updated**: 2026-04-14  

**[← Back to Language Selection](../../README.md)**
