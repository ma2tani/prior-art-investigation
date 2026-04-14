# Setup Checklist — Prior Art Investigation Framework

Use this when integrating prior-art-investigation into a new project.

---

## Prerequisites

- [ ] GitHub Copilot (agent mode) or equivalent AI IDE is available
- [ ] Confirm `.kiro/` directory exists (or will be created)
- [ ] Confirm `.github/prompts/` directory exists (or will be created)

---

## Option A: Integrate with Kiro / cc-sdd (Recommended)

### Step 1: Copy the Kiro rule file

- [ ] Copy `kiro/settings/rules/oss-evaluation.md` to `.kiro/settings/rules/`

```bash
cp kiro/settings/rules/oss-evaluation.md .kiro/settings/rules/
```

### Step 2: Add the Named Concept section to research.md template

- [ ] Merge `templates/research.md` into your project's existing `research.md` template

```bash
# If no template exists yet
cp templates/research.md .kiro/settings/templates/specs/
```

### Step 3: Wire into your design-discovery process

Add a "Prior Art Investigation" step in your design phase:

```markdown
### Prior Art Investigation (Phase A → B)

Before finalizing design decisions, run:
- **Phase A**: Name the concept (is there a known algorithm/pattern?)
- **Phase B**: Search for OSS implementations (only after naming)

Resources: `.kiro/settings/rules/oss-evaluation.md`
```

### Step 4: Add Q1+Q6 to requirements phase (optional)

Quick check before finalizing requirements:

```markdown
## Quick Prior Art Check
- **Q1 (First Principles)**: Is the problem framing correct?
- **Q6 (Inversion)**: What would cause this feature to fail?
```

### Step 5: Add Q7 to tasks phase (optional)

Before finalizing tasks:

```markdown
## "So What" Check (Q7)
For each task: "Does this reflect the prior art findings in research.md?"
```

---

## Option B: Standalone (No Kiro)

- [ ] Copy `github/prompts/prior-art-check.prompt.md` to your project's `.github/prompts/`
- [ ] Copy `templates/research.md` to `docs/` or your design notes folder
- [ ] Use the prompt independently when starting any design work

---

## Next Steps

1. **Read** the [7 Design Inquiry Questions](github/prompts/prior-art-check.prompt.md)
2. **Review** the [OSS Evaluation Rules](kiro/settings/rules/oss-evaluation.md)
3. **Test** with one feature using the [research.md template](templates/research.md)

---

**Questions?** Check the main [README](README.md) or the parent [language selection page](../../README.md).
