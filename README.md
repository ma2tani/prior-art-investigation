# Prior Art Investigation Framework

Quickly identify named concepts, established patterns, and OSS options **before** building.

**Language / 言語:**
- **[English](docs/en/README.md)** — Quick start for global dev teams
- **[日本語](docs/ja/README.md)** — 日本人向けガイド

---

## 🎯 What This Does

| Scenario | Time | Tokens | Output |
|----------|------|--------|--------|
| **Requirements phase**: Quick concept check | 5-10 min | ~150 | Confirmed concept name + risks |
| **Design phase**: Deep architecture research | 20-40 min | ~500 | OSS options + architecture tradeoffs |
| **Unsure**: Auto-detect phase | 1-2 min | ~100 | Routes to MINIMAL or FULL |

> *Avoid reinventing the wheel. Before coding, identify what it's called and who already built it.*

---

## 🚀 Get Started (Choose Your Path)

### Path 1: VS Code Copilot (Fastest — 0 minutes)
```
@prior-art-investigation minimal
I need real-time search for music grooves
```

### Path 2: Claude Desktop (5 minutes)
```bash
# Add to ~/.../Claude/claude_desktop_config.json
"mcpServers": {
  "prior-art-investigation": {
    "command": "python3",
    "args": ["/path/to/mcp/server_lite.py"]
  }
}

# Restart Claude → 3 tools available
@prior-art-investigation [minimal|full|selector]
```

### Path 3: npm Package (Programmatic)
```bash
npm install @ma2tani/prior-art-investigation

import minimalPrompt from '@ma2tani/prior-art-investigation/prompts/minimal';
```

---

## ✨ Key Features (v1.0.0)

- ✅ **Phase-split prompts** — MINIMAL (Q1+Q6) / FULL (Q1-Q7) / SELECTOR
- ✅ **70% token reduction** — MINIMAL: 150 tokens vs FULL: 500 tokens
- ✅ **3 distribution channels** — Agent Skills / MCP Server / npm
- ✅ **Bilingual** — English + 日本語
- ✅ **Kiro SDD compatible** — Saves to `.kiro/specs/`
- ✅ **Zero dependencies** — MCP server uses stdlib only

---

## 📚 Documentation

**Quick Links:**
- [NAVIGATION.md](docs/en/NAVIGATION.md) — Discovery hub (start here!)
- [AGENT-SKILLS-USAGE.md](docs/en/AGENT-SKILLS-USAGE.md) — VS Code guide
- [CLAUDE-DESKTOP-SETUP.md](docs/en/CLAUDE-DESKTOP-SETUP.md) — MCP setup
- [CHANGELOG.md](CHANGELOG.md) — What's new in v1.0.0
- [RELEASE.md](RELEASE.md) — Release notes

**By Language:**
- [English docs](docs/en/README.md)
- [日本語ドキュメント](docs/ja/README.md)

---

## 🔗 Links

- **GitHub**: https://github.com/ma2tani/prior-art-investigation
- **npm**: https://www.npmjs.com/package/@ma2tani/prior-art-investigation
- **Release**: https://github.com/ma2tani/prior-art-investigation/releases/tag/v1.0.0

---

## 📝 License

MIT

---

**Version**: 1.0.0  
**Status**: Production Ready ✅  
**Last Updated**: 2026-04-14
