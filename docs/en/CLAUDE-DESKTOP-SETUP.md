# Claude Desktop MCP Configuration Template

## SETUP (macOS / Linux)

### Step 1: Create MCP server environment
```bash
cd /path/to/prior-art-investigation
python3 -m venv mcp-env
source mcp-env/bin/activate
# No pip install needed - server_lite.py uses standard library only!
```

### Step 2: Add to Claude Desktop config

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Linux**: `~/.config/Claude/claude_desktop_config.json`

**Example config** (use `server_lite.py` — no FastMCP required):

```json
{
  "mcpServers": {
    "prior-art-investigation": {
      "command": "python3",
      "args": [
        "/absolute/path/to/prior-art-investigation/mcp/server_lite.py"
      ]
    }
  }
}
```

### Step 3: Restart Claude Desktop

### Step 4: Verify in Claude

In Claude, you should now see:
- 🔧 prior-art-investigation (3 tools available)

---

## TOOLS AVAILABLE

### 1. `load_minimal`
- **Phase**: Requirements (5-10 min, ~150 tokens)
- **Framework**: Q1 + Q6 only
- **Use when**: Quick feature validation

### 2. `load_full`
- **Phase**: Design (20-40 min, ~500 tokens)
- **Framework**: Q1-Q7 complete
- **Use when**: Architecture decisions

### 3. `load_selector`
- **Phase**: Automatic routing (1-2 min, ~100 tokens)
- **Use when**: Unsure which prompt to start with

---

## USAGE IN CLAUDE

### Quick Example

```
User: "I need to figure out a new feature"
Claude: [calls load_selector tool]
Claude: "Are you in Requirements or Design phase?"
User: "Requirements"
Claude: [auto-routes to load_minimal]
Claude: "Here's the minimal framework - let's answer Q1 and Q6..."
```

---

## TROUBLESHOOTING

### ❌ Tools don't appear in Claude
- [ ] Restart Claude Desktop (`Cmd+Q` then reopen)
- [ ] Check config file syntax (use JSON validator)
- [ ] Verify Python path is absolute (not relative)
- [ ] Check MCP server logs: `~/Library/Logs/Claude/`

### ❌ "Server connection failed"
- [ ] Verify venv activated: `which python3` should show venv path
- [ ] Verify `mcp/requirements.txt` installed: `pip list | grep mcp`
- [ ] Try running server standalone: `python3 mcp/server.py`

### ❌ "Prompt file not found"
- [ ] Verify file exists: `ls docs/en/github/prompts/`
- [ ] Check path is relative to repo root
- [ ] Try absolute path first

---

## NEXT STEPS

1. **Local Testing** (this doc)
   - [ ] Config set up ✅
   - [ ] Claude Desktop restarted
   - [ ] Tool appears in Claude

2. **Kiro SDD Integration** (v1.1, optional)
   - [ ] Create `kiro-spec-loader` workflow
   - [ ] Auto-load prompts by phase
   - [ ] Integrate with kiro commands

3. **Deployment** (v1.1+)
   - [ ] Docker container (optional)
   - [ ] Smithery registry submission
   - [ ] PulseMCP community feature

---

**Version**: 1.0.0  
**Status**: ✅ Ready for local testing  
**Last Updated**: 2026-04-14
