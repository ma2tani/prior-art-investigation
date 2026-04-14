# Setting Up the MCP Server with Claude Desktop

Configure the Prior Art Investigation Framework as a Model Context Protocol (MCP) server for Claude Desktop.

---

## Prerequisites

- Claude Desktop installed
- Python 3.6+
- Text editor

---

## Setup Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/as-we/prior-art-investigation.git
cd prior-art-investigation
```

### Step 2: Edit the MCP Config File

Claude Desktop reads MCP server configuration from `claude_desktop_config.json`.

**macOS/Linux**:
```bash
nano ~/.claude/claude_desktop_config.json
```

**Windows**:
```powershell
notepad $env:APPDATA\Claude\claude_desktop_config.json
```

### Step 3: Add the Configuration

Add the following (adjust the path to match your clone location):

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

### Step 4: Restart Claude Desktop

```bash
# macOS
pkill -f "Claude" && open /Applications/Claude.app

# Linux
pkill -f claude-app

# Windows
taskkill /IM claude.exe /F
```

### Step 5: Verify

In Claude chat, confirm the three tools are available:

- `load_minimal` — Requirements phase (~150 tokens, 5-10 min)
- `load_full` — Design phase (~500 tokens, 20-40 min)
- `load_selector` — Auto-routing (~100 tokens, 1-2 min)

---

## Troubleshooting

### MCP server not connecting

1. Verify the JSON config path is correct
2. Confirm Python 3.6+ is installed: `python3 --version`
3. Test the server starts manually:
   ```bash
   python3 /path/to/prior-art-investigation/mcp/server_lite.py
   ```

### Tools not showing up

Check Claude Desktop logs (macOS: search "Claude" in Console.app), then fully restart Claude Desktop.

---

## Related Docs

- [README.md](./README.md) — Overview & full guide
- [AGENT-SKILLS-SETUP.md](./AGENT-SKILLS-SETUP.md) — Setup for VS Code

---

**Version**: 1.0.0 | **Protocol**: JSON-RPC 2.0
