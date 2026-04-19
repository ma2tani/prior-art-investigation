---
name: prior-art
description: Prior Art Investigation — Identify concept names, existing OSS, and failure risks before building. Use when designing new features, selecting technologies, or evaluating architecture patterns. Invoke with /prior-art minimal (quick check) or /prior-art full (deep investigation). Add #web for real-time OSS data beyond training cutoff.
argument-hint: "[minimal | full | selector] <topic> [#web]"
---

# Prior Art Investigation

Quickly identify if your feature concept already exists, what it's called, and what OSS solutions are available — **before** you code.

> 💡 **Recommended**: Add `#web` to your prompt so this agent can search the live web for current OSS releases, recent GitHub activity, and platform changelog entries — bypassing LLM training cutoff entirely.

## What This Agent Does

1. **Names Your Concept** — Discovers the real technical term (e.g., "auto-refresh cache" → "Cache-Aside pattern")
2. **Maps Risk** — Identifies what could go wrong (architectural, performance, adoption)
3. **Lists OSS Options** — Shows existing solutions you could adapt or build on

## When to Use

### Requirements phase (quick check)
- Use `/prior-art minimal` — concept name + OSS list + risk flags (~150 tokens, 5–10 min)

### Design phase (deep investigation)
- Use `/prior-art full` — research lineage + OSS matrix + failure modes (~500 tokens, 20–40 min)

### Not sure which?
- Use `/prior-art selector` — auto-routes to minimal or full

## Commands

| Command | Effect |
|---------|--------|
| `/prior-art selector` | Auto-detect phase, run appropriate investigation |
| `/prior-art minimal` | Q1 + Q6 only — concept name, OSS list, risk flags |
| `/prior-art full` | Q1–Q8 complete — research lineage, OSS matrix, tradeoffs, failure modes |

**Add `#web` for live results** (VS Code Copilot Chat):
```
/prior-art full #web LLM knowledge distillation
```

## Web Search

This agent is designed to be used **with web search enabled**. Prior art investigation is about "what exists right now" — LLM training data alone is insufficient.

| Tool | How to enable web search |
|------|--------------------------|
| VS Code Copilot Chat | Add `#web` to your prompt |
| VS Code agent mode | Agent calls web search automatically when instructed |
| Kiro IDE | Web search tool available if granted in agent permissions |
| Claude Desktop | Add a search MCP server (Brave Search, Tavily, or Exa) — see USAGE.md |

## MINIMAL Investigation (Q1 + Q6)

### Q1: First Principles
- Is this problem correctly defined?
- Are we solving root causes, not symptoms?
- What is the simplest restatement without jargon?

### Q6: Inversion
- If this fails spectacularly in 6 months, what caused it?
- Which assumptions might be wrong?
- What must be verified **before** proceeding?

## FULL Investigation (Q1–Q8)

Run all questions in sequence:

**Q1** First Principles — Is the problem correctly defined?
**Q2** Concept Name — What is this called in existing research? What is the research lineage?
**Q3** Technical Options — What algorithms/architecture patterns exist? What are the tradeoffs?
**Q4** OSS Ecosystem — **Use web search here.** What existing OSS already solves this? Check GitHub for latest release dates and activity. Evaluate: license, maintainer, update frequency, best-fit use cases. Include source links.
**Q5** Architecture Choice — Build vs. Adopt recommendation and rationale.
**Q6** Inversion — Failure scenarios and assumptions to validate.
**Q7** Next Steps — Prioritized concrete actions.
**Q8** Platform Native — **Use web search here.** Does the target platform (VS Code, GitHub, Azure, AWS, etc.) already provide this natively? Search the official Changelog and recent release notes for the latest status.

## Output Rules

Every output must include:
- ✅ Concept name confirmed + alternative names
- ✅ OSS evaluation matrix with columns: Tool | License | Maintainer | Updated | Best For | Source
- ✅ Source links (arXiv / GitHub / official docs) for every claim — facts without sources are not accepted
- ✅ Risk map (assumptions → potential failures)
- ✅ If web search was NOT used: flag any OSS/platform items that may have changed in the past 12 months and recommend the user verify with `#web`

## Integration with SDD Workflows

### GitHub SpecKit (VS Code Copilot)

Run manually before each SpecKit phase — no automatic hooks:

```
# Before speckit.specify (requirements phase)
/prior-art minimal #web <feature topic>

# Before speckit.plan (design phase)
/prior-art full #web <feature topic>
```

### Kiro SDD

```bash
# Phase 1 (Requirements)
/kiro-spec-requirements FEATURE-NAME
# → auto-runs minimal investigation via .kiro/hooks/prior-art-requirements.kiro.hook

# Phase 2 (Design)
/kiro-spec-design FEATURE-NAME
# → auto-runs full investigation via .kiro/hooks/prior-art-design.kiro.hook
```

Results are saved to `.tmp/[TICKET-XXX]/prior-art-requirements.md` / `prior-art-design.md`.
