# CHANGELOG

All notable changes to the Prior Art Investigation Framework are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [1.0.0] — 2026-04-14

### Initial Release 🎉

**Overview**: Phase-split Prior Art Investigation framework with three distribution channels (npm, Agent Skills, MCP).

### Added

#### Core Framework
- **MINIMAL Prompt** (Q1+Q6) — Requirements phase, ~150 tokens
  - First Principles validation
  - Risk inversion analysis
  - Quick 5-10 minute workflow
  
- **FULL Prompt** (Q1-Q7) — Design phase, ~500 tokens
  - Complete 7-question investigation
  - OSS options evaluation
  - Architecture decision mapping
  - 20-40 minute workflow

- **SELECTOR Prompt** — Automatic phase detection, ~100 tokens
  - Routes to MINIMAL or FULL based on context
  - User-friendly phase identification
  - 1-2 minute workflow

#### Distribution Channels

**Tier 1: VS Code Copilot Agent Skills** ✅ Ready
- `.instructions.md` (EN) — Agent Skills definition
- `.instructions.ja.md` (JA) — Bilingual support
- `copilot-instructions.md` — Alternative format
- Zero-config: `@prior-art-investigation [minimal|full|selector]`

**Tier 2: MCP Server** ✅ Ready
- `mcp/server_lite.py` — JSON-RPC implementation (no dependencies)
- `mcp/server.py` — FastMCP version (optional)
- `docs/en/CLAUDE-DESKTOP-SETUP.md` — Local setup guide
- 3 tools: load_minimal, load_full, load_selector
- Tested & verified with local MCP client

**Tier 3: npm Package** ✅ Ready
- `@ma2tani/prior-art-investigation` on npm
- Tree-shake enabled (`sideEffects: false`)
- Granular exports: `./prompts/minimal`, `./prompts/full`, `./prompts/selector`
- MCP metadata for future wrapper registration

#### Documentation

- **[NAVIGATION.md](docs/en/NAVIGATION.md)** — Discovery hub for all user types
- **[AGENT-SKILLS-SETUP.md](docs/en/AGENT-SKILLS-SETUP.md)** — VS Code integration guide
- **[AGENT-SKILLS-USAGE.md](docs/en/AGENT-SKILLS-USAGE.md)** — Complete command reference
- **[CLAUDE-DESKTOP-SETUP.md](docs/en/CLAUDE-DESKTOP-SETUP.md)** — MCP local testing guide
- **[MCP-SETUP.md](docs/en/MCP-SETUP.md)** — MCP server documentation
- **[INSTALL.md](docs/en/INSTALL.md)** — Installation instructions
- **[README.md](README.md)** — Project overview
- Bilingual support: All EN docs have JA equivalents

#### Templates & Resources
- `docs/templates/research.md` — Structured research output template
- `docs/kiro/settings/rules/oss-evaluation.md` — OSS evaluation framework
- Repository memory for future reference

### Technical Achievements

- **70% Token Reduction** — MINIMAL achieves 150 tokens vs 500 for FULL (70% reduction on Requirements phase)
- **Zero Dependencies** — MCP server uses only Python standard library
- **Bilingual Framework** — English + Japanese support throughout
- **Kiro SDD Compatible** — Integrates with spec-driven development workflows
- **Production Ready** — Tested locally, ready for immediate deployment

### Supported Platforms

- ✅ **VS Code Copilot** — Agent Skills (zero-config)
- ✅ **Claude Desktop** — MCP Server (local)
- ✅ **npm Packages** — Programmatic access
- ✅ **GitHub Raw URLs** — Manual copy/paste
- ✅ **Kiro SDD** — Workflow integration
- ✅ **ChatGPT / Claude.ai** — Browser clients

### Commits This Release

- `3f5cedd` — feat: phase-split prompts (minimal/full/selector)
- `5816eba` — fix: optimize npm package (tree-shake, exports, mcp config)
- `145e726` — feat: implement MCP server wrapper (FastMCP)
- `15c7e8c` — test: verify MCP server works locally
- `ea08fce` — feat: implement Agent Skills template (VS Code Copilot)

### Known Limitations

- MCP server Smithery registration: Coming in v1.1
- Docker container: Coming in v1.1
- GitHub Actions token CI: Planned for future release
- Advanced Agent Skills features: Planned for v1.2

### Next Steps (Roadmap)

**v1.1.0** (Q2 2026)
- [ ] Smithery MCP registry submission
- [ ] Docker container for hosted option
- [ ] Token measurement GitHub Actions
- [ ] Enhanced error handling

**v1.2.0** (Q3 2026)
- [ ] Native Agent Skills personality
- [ ] Kiro SDD deep integration
- [ ] Workspace auto-save features
- [ ] Community feedback implementation

### Contributors

- Initial framework & implementation: ma2tani

### Links

- **Repository**: https://github.com/ma2tani/prior-art-investigation
- **npm Package**: https://www.npmjs.com/package/@ma2tani/prior-art-investigation
- **MCP Servers**: https://registry.modelcontextprotocol.io/
- **GitHub Copilot**: https://code.visualstudio.com/docs/copilot/agents/overview

### License

MIT

---

## Release Notes

### How to Get Started

1. **VS Code Copilot** → Just type `@prior-art-investigation`
2. **Claude Desktop** → Add MCP config (2 minutes)
3. **npm** → `npm install @ma2tani/prior-art-investigation`

See [NAVIGATION.md](docs/en/NAVIGATION.md) for platform-specific guides.

### Support

- 📖 Documentation: [docs/en/README.md](docs/en/README.md)
- 💬 Discussions: [GitHub Discussions](https://github.com/ma2tani/prior-art-investigation/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/ma2tani/prior-art-investigation/issues)

---

**Version**: 1.0.0  
**Release Date**: 2026-04-14  
**Status**: ✅ Production Ready
