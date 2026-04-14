# Prior Art Investigation Framework

**[日本語](docs/ja/README.md)**

---

## What It Does

When starting from scratch — no reference code, no prior art — it's easy to reinvent what already exists or pick the wrong foundation.

This framework prompts an AI agent to investigate your concept **before you build**, and returns:

- **The right name** — the industry-standard term for your concept (e.g., "auto-refresh cache" → "Cache-Aside Pattern")
- **Existing OSS** — ranked options with tradeoff evaluation, not just a list
- **Research lineage** — where the idea came from, which papers or systems validated it, how it evolved
- **Known failure points** — what tends to break before you're committed to an architecture

| Mode | Use When | Time | Tokens |
|------|----------|------|--------|
| **minimal** | Requirements phase — concept naming + quick OSS scan | 5-10 min | ~150 |
| **full** | Design phase — deep research, evaluation matrix, tradeoffs | 20-40 min | ~500 |
| **selector** | Not sure which phase | 1-2 min | auto-routes |

<details>
<summary><strong>Example output (full mode)</strong></summary>

**Input**: `@prior-art-investigation full We need consistent distributed locking across microservices`

**Output**:

**Concept identified**: Distributed Mutex / Distributed Lock

> This is a well-scoped problem. The term "distributed locking" maps to a body of research starting with Lamport's 1978 paper on logical clocks, expanded through the Chubby lock service (Google, 2006), and popularized for application developers via Redis-based implementations.

**Research lineage**:
| Year | Milestone |
|------|-----------|
| 1978 | Lamport — Logical Clocks, foundational ordering theory |
| 2006 | Google Chubby — first production distributed lock service |
| 2016 | Redlock algorithm (Antirez) — Redis-based distributed lock |
| 2016 | Martin Kleppmann critique — safety concerns with Redlock under clock skew |
| 2023 | etcd RAFT-based leases now standard for k8s-adjacent systems |

**OSS evaluation matrix**:
| Tool | Consistency | Ops Complexity | Best For |
|------|-------------|----------------|----------|
| Redis + Redlock | ⚠️ Not strictly safe | Low | Latency-sensitive, tolerate rare failures |
| etcd leases | ✅ Strong (RAFT) | Medium | Kubernetes-adjacent, infra-level |
| ZooKeeper | ✅ Strong | High | JVM ecosystem, existing ZK usage |
| PostgreSQL advisory locks | ✅ Strong | Low | Already on Postgres, simple case |

**Recommendation**: PostgreSQL advisory locks if you're already on Postgres. etcd if you need true distributed consensus. Avoid Redlock unless failure tolerance is explicitly acceptable.

**Known failure points**:
- Clock skew invalidates TTL assumptions in Redlock
- Lock holder crashes before releasing → need heartbeat / fencing token
- Re-entrant lock requirements add complexity most implementations skip

</details>

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

Extend the framework by adding your own personalities, modes, or integration hooks.

See `.kiro/personalities/` and `.kiro/hooks/` for examples.

---

## Documentation

Language-specific setup guides:

| | English | 日本語 |
|-|---------|--------|
| VS Code setup | [docs/en/AGENT-SKILLS-SETUP.md](docs/en/AGENT-SKILLS-SETUP.md) | [docs/ja/AGENT-SKILLS-SETUP.md](docs/ja/AGENT-SKILLS-SETUP.md) |
| Claude setup | [docs/en/MCP-SETUP.md](docs/en/MCP-SETUP.md) | [docs/ja/MCP-SETUP.md](docs/ja/MCP-SETUP.md) |

---

## License

MIT

- **GitHub**: https://github.com/as-we/prior-art-investigation
- **Release**: https://github.com/as-we/prior-art-investigation/releases/tag/v1.0.0
