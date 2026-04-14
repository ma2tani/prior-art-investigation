# Prior Art Investigation Framework

> A lightweight checklist and prompt set that helps AI coding agents identify named concepts, established patterns, and existing implementations **before** writing requirements, design, or code.

## What problem does this solve?

AI agents (and humans) often reinvent the wheel:
- Describing "LLM inference → lightweight ML training" without knowing it's called **Knowledge Distillation**
- Designing a retry-with-backoff mechanism without knowing it's **Circuit Breaker** pattern
- Building a read/write model split without knowing it's **CQRS**

Naming the concept unlocks existing best practices, known failure modes, and reference implementations — before a single line of code is written.

## Contents

```
docs/en/
├── README.md                                     ← This file
├── setup-checklist.md                            ← Step-by-step integration guide
├── templates/
│   └── research.md                               ← research.md with Named Concept section
├── github/
│   └── prompts/
│       └── prior-art-check.prompt.md             ← AI agent prompt
└── kiro/
    └── settings/
        └── rules/
            └── oss-evaluation.md                 ← Main rule file
```

## Quick Start

See [setup-checklist.md](setup-checklist.md) for step-by-step instructions.

### Option A: With Kiro / cc-sdd (recommended)

```bash
cp docs/en/kiro/settings/rules/oss-evaluation.md     .kiro/settings/rules/
cp docs/en/templates/research.md                     .kiro/settings/templates/specs/
cp docs/en/github/prompts/prior-art-check.prompt.md  .github/prompts/
```

### Option B: Standalone

Use `docs/en/github/prompts/prior-art-check.prompt.md` directly as an AI agent prompt in any IDE.

## Investigation Structure

**Phase A — Concept Identification**
- A-0: 7 design inquiry questions
- A-1: Named concept search
- A-2: Domain-specific investigation angles
- A-3: Research resources by domain
- A-4: Record findings in research log

**Phase B — OSS / Implementation Search**
- B-1: Search order (project-internal → ecosystem → industry OSS)
- B-2: License tier classification (Tier 1–4)
- B-3: OSS health assessment
- B-4: Build vs Use decision matrix

## References

- [7 Design Inquiry Questions](github/prompts/prior-art-check.prompt.md)
- [OSS Evaluation Rules](kiro/settings/rules/oss-evaluation.md)
- [Research Template](templates/research.md)

---

**Back to:** [Language Selection](../../README.md)

## License

MIT
