# Prior Art Investigation Framework

A lightweight checklist and prompt set for AI coding agents and development teams to identify named concepts, established patterns, and existing OSS implementations **before** writing requirements, design, or code.

**Language / 言語:**
- **[English](docs/en/README.md)** — Investigation framework for global dev teams
- **[日本語](docs/ja/README.md)** — 日本人向けテンプレートとガイド

---

## What This Is

> *Avoid reinventing the wheel.*

When designing a feature, it's easy to describe novel solutions without knowing they already have established names, known failure modes, and existing implementations:

- "LLM inference → lightweight ML training" = **Knowledge Distillation**
- "Retry with backoff" = **Circuit Breaker pattern**
- "Read/write model split" = **CQRS**

Naming the concept unlocks best practices, reference implementations, and OSS options — *before* a single line of code is written.

## Quick Start

1. Choose your language above:
   - **[English version](docs/en/README.md)** for international teams
   - **[日本語版](docs/ja/README.md)** for Japanese-speaking teams

2. Follow the **setup checklist** for your workflow (Kiro SDD, standalone, etc)

3. Use the **investigation prompts** in your design phase

## Features

- ✅ 7-question design inquiry framework
- ✅ OSS license tier classification
- ✅ Build vs Use decision matrix
- ✅ Kiro SDD integration (with `.kiro/settings/` templates)
- ✅ Standalone GitHub Actions prompt
- ✅ Domain-specific research resources

## License

MIT

---

**Looking for more info?** → [English docs](docs/en/) | [日本語ドキュメント](docs/ja/)
