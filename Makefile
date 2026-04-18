.PHONY: install install-skills install-hook uninstall validate help

UNAME := $(shell uname)
ifeq ($(UNAME), Darwin)
  SKILLS_DIR := $(HOME)/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills
else
  SKILLS_DIR := $(HOME)/.config/Code/User/globalStorage/github.copilot-chat/agent-skills
endif
HOOKS_DIR := $(HOME)/.copilot/hooks

# ─── Layer 1: Agent Skills (cross-workspace, explicit invocation) ───────────

install-skills:
	@echo "Installing Agent Skills..."
	@mkdir -p "$(SKILLS_DIR)"
	@cp .instructions.md "$(SKILLS_DIR)/prior-art.md"
	@echo "✓ Agent Skills installed → @prior-art minimal/full/selector"

# ─── Layer 2: UserPromptSubmit hook (user-scope, deterministic) ─────────────

install-hook:
	@echo "Installing UserPromptSubmit hook..."
	@mkdir -p "$(HOOKS_DIR)/scripts"
	@cp .github/hooks/prior-art-detect.json "$(HOOKS_DIR)/prior-art-detect.json"
	@cp .github/hooks/scripts/prior-art-detect.sh "$(HOOKS_DIR)/scripts/prior-art-detect.sh"
	@chmod +x "$(HOOKS_DIR)/scripts/prior-art-detect.sh"
	@echo "✓ Hook installed → auto-reminder on design/architecture prompts"
	@echo ""
	@echo "  Enable in VS Code settings:"
	@echo "    chat.hookFilesLocations: { \"~/.copilot/hooks\": true }"

# ─── Combined install ────────────────────────────────────────────────────────

install: install-skills install-hook
	@echo ""
	@echo "✅ Prior Art Investigation installed (2-layer setup)"
	@echo ""
	@echo "  Layer 1 — Agent Skills: @prior-art full <topic>"
	@echo "  Layer 2 — Auto hook:    fires on design/spec prompts"

# ─── Uninstall ───────────────────────────────────────────────────────────────

uninstall:
	@rm -f "$(SKILLS_DIR)/prior-art.md"
	@rm -f "$(HOOKS_DIR)/prior-art-detect.json"
	@rm -f "$(HOOKS_DIR)/scripts/prior-art-detect.sh"
	@rm -f "$(HOOKS_DIR)/scripts/prior-art-detect.ps1"
	@echo "✓ Uninstalled"

# ─── Validation ──────────────────────────────────────────────────────────────

validate:
	@echo "Validating directory structure..."
	@test -f README.md && echo "✓ README" || (echo "✗ README.md missing"; exit 1)
	@test -f docs/ja/README.md && echo "✓ Japanese docs" || (echo "✗ Japanese docs missing"; exit 1)
	@test -f docs/en/AGENT-SKILLS-SETUP.md && echo "✓ Agent Skills setup" || (echo "✗ AGENT-SKILLS-SETUP.md missing"; exit 1)
	@test -f docs/en/MCP-SETUP.md && echo "✓ MCP setup" || (echo "✗ MCP-SETUP.md missing"; exit 1)
	@test -f .instructions.md && echo "✓ Agent Skills template" || (echo "✗ .instructions.md missing"; exit 1)
	@test -f mcp/server_lite.py && echo "✓ MCP server" || (echo "✗ MCP server missing"; exit 1)
	@test -f LICENSE && echo "✓ LICENSE" || (echo "✗ LICENSE missing"; exit 1)
	@test -f .github/hooks/prior-art-detect.json && echo "✓ Hook JSON" || (echo "✗ Hook JSON missing"; exit 1)
	@test -f .github/hooks/scripts/prior-art-detect.sh && echo "✓ Hook script" || (echo "✗ Hook script missing"; exit 1)
	@echo "✅ All validations passed"

help:
	@echo "Prior Art Investigation Framework"
	@echo ""
	@echo "Install (recommended — both layers):"
	@echo "  make install          - Install Agent Skills + UserPromptSubmit hook"
	@echo ""
	@echo "Install individually:"
	@echo "  make install-skills   - Layer 1: Agent Skills (@prior-art)"
	@echo "  make install-hook     - Layer 2: Auto-detect hook (user-scope)"
	@echo ""
	@echo "Other:"
	@echo "  make uninstall        - Remove all installed files"
	@echo "  make validate         - Validate repository structure"
