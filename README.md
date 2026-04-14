# Prior Art Investigation Framework

> Before writing code, identify what your concept is called, what patterns exist, and which OSS already solves it.

**[English](docs/en/README.md)** | **[日本語](docs/ja/README.md)**

---

## What It Does

Prompts an AI agent to investigate your feature concept through structured questions:

| Mode | Use When | Time | Tokens |
|------|----------|------|--------|
| **minimal** | Requirements phase — quick concept check | 5-10 min | ~150 |
| **full** | Design phase — deep architecture research | 20-40 min | ~500 |
| **selector** | Not sure which phase | 1-2 min | auto-routes |

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

---

## Documentation

| | English | 日本語 |
|-|---------|--------|
| Overview | [docs/en/README.md](docs/en/README.md) | [docs/ja/README.md](docs/ja/README.md) |
| VS Code setup | [AGENT-SKILLS-SETUP.md](docs/en/AGENT-SKILLS-SETUP.md) | [AGENT-SKILLS-SETUP.md](docs/ja/AGENT-SKILLS-SETUP.md) |
| Claude setup | [MCP-SETUP.md](docs/en/MCP-SETUP.md) | [MCP-SETUP.md](docs/ja/MCP-SETUP.md) |

---

## License

MIT


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
