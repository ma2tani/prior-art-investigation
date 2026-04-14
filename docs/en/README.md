# Prior Art Investigation Framework

Identify named concepts, existing patterns, and OSS options **before** you write code.

**[日本語](../ja/README.md)**

---

## What It Does

When designing a feature, it answers:

- "Does this concept already have an established name?" → Pinpoints the technical term
- "What OSS already solves this?" → Lists ready-to-use options
- "What tends to fail?" → Surfaces common pitfalls and risky assumptions

Use it at the **start of requirements or design phases**.

| Mode | Use When | Time | Tokens |
|------|----------|------|--------|
| `minimal` | Requirements phase — quick concept check | 5-10 min | ~150 |
| `full` | Design phase — OSS comparison, architecture research | 20-40 min | ~500 |
| `selector` | Not sure which phase | 1-2 min | ~100 |

---

## How to Use

### A. VS Code Copilot — zero setup

Copy `.instructions.md` to the Agent Skills folder and restart VS Code:

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Linux
cp .instructions.md \
  ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md
```

Use in Copilot Chat:

```
@prior-art-investigation minimal I need to design a real-time search feature
```

→ [Full setup guide](./AGENT-SKILLS-SETUP.md)

---

### B. Claude Desktop (MCP) — 5 min

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

Restart Claude Desktop → tools `load_minimal` / `load_full` / `load_selector` are available.

→ [Full setup guide](./MCP-SETUP.md)

---

### C. Kiro SDD — copy hooks & personalities

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

Prior art investigation runs automatically at requirements and design phases.

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

### Question framework (Q1–Q7)

`minimal` uses Q1 (first principles) + Q6 (inversion/risk) only.  
`full` uses Q1–Q7 complete investigation.

Edit `.instructions.md` directly to change the question content.

### Custom personalities

Edit JSON files in `.kiro/personalities/`:

```json
{
  "name": "my-custom",
  "label": "My Custom Researcher",
  "description": "Focus on ...",
  "questions": ["What ...?", "Are there ...?"]
}
```

---

**Version**: 1.0.0 | **License**: MIT
