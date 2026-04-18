# Usage Guide — AI Prior Art Investigation

Before designing, confirm: "This concept already has a name", "There's existing OSS for this", "The failure patterns are documented."

---

## Which tool are you using?

| Tool | Automatic | Manual | Section |
|------|-----------|--------|---------|
| **VS Code + GitHub Copilot** | Reminder notification (opt-in for actual investigation) | `/prior-art` slash command | [→ A](#a-vs-code--github-copilot) |
| **Kiro IDE** | Auto-fires at SDD phases | Agent dropdown selection | [→ B](#b-kiro-ide) |
| **Claude Desktop** | None | MCP tool calls | [→ C](#c-claude-desktop) |

> **About investigation modes**  
> `MINIMAL` (Q1+Q6): Requirements phase. "Are we solving the right problem?" and "What could fail?" — 5–10 min.  
> `FULL` (Q1–Q8): Design phase. Concept name, OSS comparison matrix, architecture recommendation, platform-native capabilities — 20–40 min.

---

## A. VS Code + GitHub Copilot

### Install (once)

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

This sets up two things:
- **Agent Skills** — use `/prior-art` slash command from any project in Copilot Chat
- **UserPromptSubmit hook** — auto-insert a one-line reminder for design-related prompts

Enable hooks in VS Code settings:
```json
"chat.hookFilesLocations": { "~/.copilot/hooks": true }
```

---

### Auto 1 — Prompt monitoring reminder (always on after install)

When your prompt contains keywords like "design", "architecture", "implement", etc., a reminder is automatically inserted:

> 💡 Prior art check recommended: this looks like a design or implementation decision. Before building, consider running: `/prior-art full <topic>`

**How it works**: whether to insert the reminder is decided by a deterministic shell script, not an LLM — so the hook itself never generates a premium request.

---

### Auto 2 — SDD phase integration (opt-in)

To trigger **actual investigation** at the end of cc-sdd sessions (`/kiro-spec-requirements`, `/kiro-spec-design`), enable the hooks in your project:

```bash
# Copy hooks to your project (first time only)
cp -r path/to/prior-art-investigation/.kiro/hooks /your-project/.kiro/

# Enable
jq '.enabled = true' .kiro/hooks/prior-art-requirements.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-requirements.kiro.hook
jq '.enabled = true' .kiro/hooks/prior-art-design.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-design.kiro.hook
```

- `/kiro-spec-requirements` ends → detects `requirements.md` change → **MINIMAL investigation (Q1+Q6)**
- `/kiro-spec-design` ends → detects `design.md` change → **FULL investigation (Q1–Q8)**

Output: `.tmp/[TICKET-XXX]/prior-art-requirements.md` / `prior-art-design.md`

---

### Auto on/off control

**Disable** (refactoring, maintenance, already-known patterns):
```bash
jq '.enabled = false' .kiro/hooks/prior-art-requirements.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-requirements.kiro.hook
jq '.enabled = false' .kiro/hooks/prior-art-design.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-design.kiro.hook
```

**Disable only the reminder hook**:
```bash
make uninstall
# or manually:
rm ~/.copilot/hooks/prior-art-detect.json ~/.copilot/hooks/scripts/prior-art-detect.sh
```

> Install `jq` if needed: `brew install jq`

---

### Manual

Type in Copilot Chat as a slash command. **Add `#web` to fetch live OSS data beyond training cutoff:**

```
/prior-art full #web I need to design API rate limiting
/prior-art minimal #web I'm evaluating caching strategies
/prior-art selector #web ← auto-routes to MINIMAL or FULL
```

`#web` activates web search — Copilot fetches GitHub Releases, official changelogs, and recent activity in real time. Works even when no spec files have changed — just describe the topic.

**When to use manually**:
- Investigation independent of SDD phase timing
- Evaluating a new OSS library mid-implementation
- Spot-checking a specific technology

---

## B. Kiro IDE

### Install (once per project)

```bash
# Copy hooks and personalities
cp -r path/to/prior-art-investigation/.kiro/hooks /your-project/.kiro/
cp -r path/to/prior-art-investigation/.kiro/personalities /your-project/.kiro/

# Copy agent (for manual use)
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

---

### Auto — SDD phase integration

Kiro IDE fires investigation **automatically** at SDD phase boundaries. No extra configuration needed.

| Kiro command | Fires when | Mode | Default personality |
|-------------|-----------|------|-------------------|
| `/kiro-spec-requirements` | Session ends + `requirements.md` changed | MINIMAL (Q1+Q6) | `startup-hunter` |
| `/kiro-spec-design` | Session ends + `design.md` changed | FULL (Q1–Q8) | `tech-auditor` |

Output: `.tmp/[TICKET-XXX]/prior-art-requirements.md` / `prior-art-design.md`

---

### Auto on/off control

Control via the `enabled` flag in `.kiro/hooks/*.kiro.hook`:

**Disable** (refactoring, maintenance):
```bash
jq '.enabled = false' .kiro/hooks/prior-art-requirements.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-requirements.kiro.hook
jq '.enabled = false' .kiro/hooks/prior-art-design.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-design.kiro.hook
```

**Enable**:
```bash
jq '.enabled = true' .kiro/hooks/prior-art-requirements.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-requirements.kiro.hook
jq '.enabled = true' .kiro/hooks/prior-art-design.kiro.hook > /tmp/h.tmp \
  && mv /tmp/h.tmp .kiro/hooks/prior-art-design.kiro.hook
```

**Change personality** (which investigation angle to use):
```json
// .kiro/hooks/prior-art-requirements.kiro.hook
{
  "personality": "researcher"   // startup-hunter / tech-auditor / researcher / patent-search / team-internal / platform-expert
}
```

→ Personality details: [SETUP.md § Personalities](./SETUP.md#d-kiro-ide--hooks--personalities)

---

### Manual

Select **Prior Art Investigation** from the Kiro agent dropdown (top of chat), then type the topic:

```
minimal  evaluating a new caching strategy
full     designing a distributed tracing architecture
selector ← auto-routes to MINIMAL or FULL
```

If Kiro supports Agent Skills, you can also use `/prior-art` as a slash command.

---

## C. Claude Desktop

### Install (once)

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

---

### Enable web search (recommended)

Prior art investigation requires current data. Add a search MCP server alongside `prior-art`:

**Option A — Brave Search** (free tier available):
```json
{
  "mcpServers": {
    "prior-art": { "command": "python3", "args": ["/path/to/prior-art-investigation/mcp/server_lite.py"] },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "<your-key>" }
    }
  }
}
```
Get a free API key at [brave.com/search/api](https://brave.com/search/api/).

**Option B — Tavily** (AI-optimized search):
```json
"tavily-search": {
  "command": "npx",
  "args": ["-y", "tavily-mcp"],
  "env": { "TAVILY_API_KEY": "<your-key>" }
}
```
Get a key at [app.tavily.com](https://app.tavily.com/).

Once a search server is active, Claude will automatically call it when `load_full` or `load_minimal` runs Q4 (OSS Ecosystem) and Q8 (Platform Native).

---

### Automatic execution

Claude Desktop has no SDD phase integration — no automatic triggers. Use manual calls below.

---

### Manual

Call MCP tools directly in Claude chat:

| Tool | Use |
|------|-----|
| `load_minimal` | MINIMAL investigation (Q1+Q6) — quick check, requirements phase |
| `load_full` | FULL investigation (Q1–Q8) — deep dive, design phase |
| `load_selector` | Auto-routes to MINIMAL or FULL |

**Example**:
```
Use load_full to investigate "knowledge distillation architecture with LLMs"
```

---

## Reading the output

### MINIMAL output (Q1+Q6)

- **Q1 First Principles**: Is the problem correctly defined? Are we solving the root cause?
- **Q6 Inversion**: If this fails spectacularly in 6 months, what caused it? What must be verified before proceeding?

### FULL output (Q1–Q8)

In addition to Q1 and Q6:
- **Q2**: Concept name, architecture pattern, research lineage
- **Q3**: List of solution approaches and tradeoffs
- **Q4**: OSS evaluation matrix (license, maintainer, update frequency, best-fit use cases)
- **Q5**: Build vs. Adopt recommendation and rationale
- **Q7**: Prioritized next actions
- **Q8**: Platform-native capabilities check (VS Code, GitHub, Azure, AWS, etc.) — prevents re-inventing what the platform already provides

> 💡 **For the most accurate results**, always run with web search enabled (`#web` in VS Code, search MCP in Claude Desktop). OSS release status and platform-native features change frequently.

→ [Q1–Q8 detailed reference](./QUESTIONS.md)

---

## When to skip

| Situation | Decision |
|-----------|----------|
| Maintenance / refactoring | Skip — no new concepts introduced |
| Well-known domain | Skip — already familiar with the space |
| Adopting a new external service or OSS | Recommended (Q4 + Q8) |
| Adopting a new architecture pattern | Recommended (FULL) |
| Greenfield / new subsystem | Recommended (FULL) |
