# Release v1.0.0 — Prior Art Investigation Framework

**Date**: April 14, 2026  
**Status**: ✅ Production Ready

---

## 🎉 What's New

Prior Art Investigation is now publicly available across **3 distribution channels**:

### 1. VS Code Copilot Agent Skills (Tier 1)
- **Command**: `@prior-art-investigation [minimal|full|selector]`
- **Setup**: 0 minutes (zero-config)
- **Time**: 5-40 minutes depending on phase
- **Cost**: ~150-500 tokens

### 2. Claude Desktop MCP Server (Tier 2)
- **Setup**: 5 minutes (config file)
- **Tools**: load_minimal, load_full, load_selector
- **Implementation**: server_lite.py (standard library only)
- **Testing**: Verified locally ✅

### 3. npm Package (Tier 3)
- **Package**: `@ma2tani/prior-art-investigation`
- **Import**: Granular prompt access via exports
- **Tree-shake**: Enabled for bundle optimization

---

## 📊 Key Achievements

| Metric | Value |
|--------|-------|
| **Token Reduction** | 70% (150 vs 500 tokens) |
| **Prompts** | 3 phase-specific (minimal/full/selector) |
| **Languages** | English + Japanese |
| **Dependencies** | Zero (MCP server) |
| **Setup Time** | 0-5 minutes |
| **Commissions** | 5 focused commits |

---

## 🚀 Quick Start

### For VS Code Users (Fastest)
```
@prior-art-investigation minimal I need a real-time search feature
```

### For Claude Desktop Users
```bash
# 1. Clone repo
git clone https://github.com/ma2tani/prior-art-investigation.git
cd prior-art-investigation

# 2. Add to Claude config
# macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "prior-art-investigation": {
      "command": "python3",
      "args": ["/path/to/mcp/server_lite.py"]
    }
  }
}

# 3. Restart Claude Desktop ✅
```

### For npm Users
```bash
npm install @ma2tani/prior-art-investigation

# Import in your project
import minimalPrompt from '@ma2tani/prior-art-investigation/prompts/minimal';
```

---

## 📚 Documentation

### User Guides
- [NAVIGATION.md](docs/en/NAVIGATION.md) — Discovery hub (start here!)
- [AGENT-SKILLS-USAGE.md](docs/en/AGENT-SKILLS-USAGE.md) — VS Code guide
- [CLAUDE-DESKTOP-SETUP.md](docs/en/CLAUDE-DESKTOP-SETUP.md) — MCP setup
- [INSTALL.md](docs/en/INSTALL.md) — Installation instructions
- [README.md](README.md) — Project overview

### Technical Docs
- [MCP-SETUP.md](docs/en/MCP-SETUP.md) — MCP server architecture
- [AGENT-SKILLS-SETUP.md](docs/en/AGENT-SKILLS-SETUP.md) — Agent implementation

### Framework
- [Prompts](docs/en/github/prompts/) — MINIMAL, FULL, SELECTOR
- [OSS Evaluation](docs/kiro/settings/rules/oss-evaluation.md) — Framework & rules
- [Research Template](docs/templates/research.md) — Output format

---

## 🔧 Technical Details

### Phase-Split Prompts

| Prompt | Phase | Time | Tokens | Questions |
|--------|-------|------|--------|-----------|
| **MINIMAL** | Requirements | 5-10 min | ~150 | Q1, Q6 |
| **FULL** | Design | 20-40 min | ~500 | Q1-Q7 |
| **SELECTOR** | Auto-detect | 1-2 min | ~100 | Routing |

### MCP Server
- **Implementation**: `mcp/server_lite.py` (JSON-RPC protocol)
- **Dependencies**: Python 3.6+, standard library only
- **Tools**: 3 (load_minimal, load_full, load_selector)
- **Status**: Tested, ready for Claude Desktop

### npm Package
- **Name**: `@ma2tani/prior-art-investigation`
- **Tree-shake**: ✅ Enabled
- **Exports**: Granular (`./prompts/minimal`, etc.)
- **MCP metadata**: Pre-configured for v1.1

---

## 🌐 Platform Support

| Platform | Status | Setup | Command |
|----------|--------|-------|---------|
| **VS Code Copilot** | ✅ Ready | 0 min | `@prior-art-investigation` |
| **Claude Desktop** | ✅ Ready | 5 min | MCP server |
| **ChatGPT / Claude.ai** | ✅ Works | n/a | Copy/paste prompts |
| **npm** | ✅ Ready | 1 min | `npm install` |
| **Kiro SDD** | ✅ Compatible | n/a | Phase integration |

---

## 📈 Roadmap

### v1.0.0 (TODAY)
- ✅ Phase-split prompts (minimal/full/selector)
- ✅ Agent Skills template (VS Code)
- ✅ MCP server implementation (Claude Desktop)
- ✅ npm package ready
- ✅ Complete documentation

### v1.1.0 (Q2 2026)
- [ ] Smithery MCP registry submission
- [ ] Docker container
- [ ] Token measurement GitHub Actions
- [ ] Enhanced error handling
- [ ] Community feedback integration

### v1.2.0 (Q3 2026)
- [ ] Native Agent Skills personality
- [ ] Kiro SDD deep integration
- [ ] Workspace auto-save
- [ ] Multi-language support expansion

---

## 💡 Usage Examples

### Example 1: Quick Requirements Check
```
User: "@prior-art-investigation minimal We need real-time groove recommendations"

Agent:
Q1: Are we solving "recommendations" or "real-time rendering speed"?
Q6: Risks: Latency assumption. Verify: Can we compute in <500ms?

Concept: "Real-time recommendation system"
OSS options: Redis (caching), Milvus (vector DB)
Status: Ready for Design phase ✓
```

### Example 2: Deep Design Investigation
```
User: "@prior-art-investigation full Designing ML-based boundary detection"

Agent: (Full Q1-Q7 investigation)
Concept: "Onset detection" or "Beat tracking"
Existing OSS: librosa, madmom, essentia
Architecture: Batch vs real-time tradeoffs
Risks: Model accuracy, latency, versioning
Recommendation: Start with librosa baseline

→ Save to .kiro/specs/boundary-detection/docs/research.md ✓
```

### Example 3: Unsure Phase
```
User: "@prior-art-investigation selector I don't know what I need yet"

Agent:
→ Asks 3 clarifying questions
→ Detects Requirements phase
→ Loads MINIMAL automatically ✓
```

---

## 🔗 Links

- **GitHub**: https://github.com/ma2tani/prior-art-investigation
- **npm**: https://www.npmjs.com/package/@ma2tani/prior-art-investigation
- **Issues**: https://github.com/ma2tani/prior-art-investigation/issues
- **Discussions**: https://github.com/ma2tani/prior-art-investigation/discussions

---

## 📝 License

MIT — Free for commercial and personal use

---

## 🙏 Thanks

Special thanks to:
- Copilot team (Agent Skills framework)
- Anthropic (Claude + MCP)
- VS Code team
- Open source community

---

**Questions?** See [NAVIGATION.md](docs/en/NAVIGATION.md) or start with `@prior-art-investigation`

**Version**: 1.0.0  
**Release Date**: April 14, 2026  
**Status**: Production Ready ✅
