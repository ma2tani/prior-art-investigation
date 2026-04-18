# Setup Guide

Choose the integration that fits your toolchain.

---

## Quick Start (Recommended)

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

`make install` sets up both **Layer 1 (Agent Skills) + Layer 2 (auto-detect hook)** in one step. One-time, user-scoped — works across all your projects.

---

## A. VS Code Copilot Chat — Agent Skills

### Install

```bash
make install-skills
```

Or manually:

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md

# Linux
cp .instructions.md \
  ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md

# Windows (PowerShell)
$dir = "$env:APPDATA\Code\User\globalStorage\github.copilot-chat\agent-skills"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
Copy-Item ".instructions.md" "$dir\prior-art.md"
```

Restart VS Code to apply.

### Usage

```
@prior-art minimal  I need to implement an API rate limiter
@prior-art full     I want to design a distributed caching layer
@prior-art selector ← auto-routes to minimal or full
```

> **Why `.instructions.md` (English) is recommended**  
> Agent Skills are sent directly as LLM prompts. English costs 20–30% fewer tokens for the same content, and GPT/Claude both produce more accurate research results from English prompts. If you need responses in Japanese, append `(respond in Japanese)` to your call:  
> ```
> @prior-art full knowledge distillation design (respond in Japanese)
> ```

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| Agent not appearing | Verify the file was copied, then fully restart VS Code |
| Errors in output | Update Copilot Chat to the latest version |

---

## B. Auto-detect Hook (VS Code / UserPromptSubmit)

### Install

```bash
make install-hook
```

Add to VS Code settings:

```json
"chat.hookFilesLocations": { "~/.copilot/hooks": true }
```

### How It Works

When you send a prompt about design or implementation, a one-line reminder is automatically inserted:

> 💡 Prior art check recommended: this looks like a design or implementation decision...

The hook lives at `~/.copilot/hooks/` — it does **not** pollute your project files.

### Uninstall

```bash
make uninstall
# or manually:
rm ~/.copilot/hooks/prior-art-detect.json
rm ~/.copilot/hooks/scripts/prior-art-detect.sh
```

---

## C. Claude Desktop (MCP Server)

### Install

Add to `~/.claude/claude_desktop_config.json` (Windows: `%APPDATA%\Claude\claude_desktop_config.json`):

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

Restart Claude Desktop.

### Available Tools

| Tool | Use |
|------|-----|
| `load_minimal` | Q1 + Q6 only — requirements phase |
| `load_full` | Q1–Q8 — design phase |
| `load_selector` | Auto-routing |

### Troubleshooting

```bash
# Verify Python path
which python3

# Test server starts standalone
python3 /path/to/prior-art-investigation/mcp/server_lite.py

# Check file permissions
chmod +x /path/to/prior-art-investigation/mcp/server_lite.py
```

Check Claude Desktop logs (macOS: Console.app, search "Claude").

---

## D. Kiro IDE — Hooks & Personalities

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

Kiro IDE will automatically run prior art investigation at the requirements (`/kiro-spec-requirements`) and design (`/kiro-spec-design`) phases.

### Personality List

A personality controls **which angle to investigate from**. Different phases use different defaults.

| Personality | Focus | Kiro Default Phase |
|-------------|-------|-------------------|
| `startup-hunter` | Market validation, competitor analysis, startup trends | Requirements (`/kiro-spec-requirements`) |
| `tech-auditor` | Technical depth, architecture, engineering best practices | Design (`/kiro-spec-design`) |
| `researcher` | Academic papers, citations, prior research | — |
| `patent-search` | IP risk, patent landscape, prior art claims | — |
| `team-internal` | Internal knowledge, existing docs, in-house patterns | — |
| `platform-expert` | IDE/runtime native APIs, platform hooks, SDK capabilities — avoids re-inventing what the platform provides | — |

### Changing the Personality

**Edit the hook config** (`.kiro/hooks/*.json`):

```json
// .kiro/hooks/prior-art-requirements.json
{
  "phase": "requirements",
  "personality": "researcher",   // ← change here
  "trigger": "after_kiro_spec_requirements"
}
```

**Override temporarily with an environment variable**:

```bash
PRIOR_ART_PERSONALITY=patent-search kiro spec requirements
```

### Creating a Custom Personality

Add a JSON file to `.kiro/personalities/`:

```json
// .kiro/personalities/security-auditor.json
{
  "name": "security-auditor",
  "label": "Security Auditor",
  "description": "Focus on known vulnerabilities, CVEs, and security patterns",
  "questions": [
    "Are there known CVEs or vulnerabilities in this approach?",
    "What security patterns already exist for this problem?",
    "Are there OWASP guidelines relevant here?"
  ],
  "web_sources": ["GitHub", "NIST NVD", "OWASP", "CVE Database"]
}
```

---

## E. VS Code Custom Agent (per-project)

For teams that want to commit agent config to the repository:

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Select **Prior Art Investigation** from the Copilot Chat agent dropdown.

---

## About the Investigation Questions

For details on Q1–Q8 (intent, sample output, why each matters), see [QUESTIONS.md](./QUESTIONS.md).
