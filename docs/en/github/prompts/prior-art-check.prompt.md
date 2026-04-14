---
agent: agent
description: Prior Art & Prior Invention Investigation Prompt — Identify concept names, existing papers, and OSS before starting design
---

# Prior Art & Prior Invention Investigation

> **Purpose**: Before writing requirements, design, or code, verify whether your problem already has a known name, established patterns, or existing implementations.  
> **Standalone Capable**: No Kiro SDD required. Usable in any development workflow.

---

## When to Run

Execute this prompt at the beginning of each phase:

| Phase | Questions to Apply | Depth |
|-------|-------------------|-------|
| Requirements | Q1 (First Principles) + Q6 (Inversion) | Quick — 2 questions only |
| Design | All 7 questions | Phase A + B full investigation |
| Task Design | Q7 (So What) | Quick — Verify tasks reflect investigation |

---

## Step 1: Load Context

Before starting, confirm:
1. Feature or problem description (1-2 sentences)
2. Technology layers involved: ML/AI・Backend・Frontend・Data・Infrastructure・Security etc.
3. Any concept names already mentioned in requirements or design notes (if any)

---

## Step 2: Apply Seven Design Investigation Questions

Ask each question in order, record the answer before moving to the next.

| # | Question | Apply Phase |
|---|----------|-------------|
| **Q1. First Principles** | "Is the problem framework correct? Are you solving the right problem?" | Requirements, Design |
| **Q2. Null Hypothesis** | "Why hasn't this approach already become mainstream? If obvious, it would be mainstream — why isn't it?" | Design |
| **Q3. Start with Failure** | "How many people have failed with this approach? How did they fail?" | Design |
| **Q4. Find the Expert** | "Who thinks deepest about this domain? Where are their words published?" | Design |
| **Q5. Read Primary Sources** | "Have you read primary sources (papers, RFCs, commit logs, Issues) — not just READMEs or blog posts?" | Design |
| **Q6. Inversion** | "If this failed in the worst way possible, what would be the cause? What should you verify?" | Requirements, Design |
| **Q7. So What** | "Now that you've named the concept, how does it change your design?" | Task |

> **Requirements Quick Check**: Apply Q1 + Q6 only.  
> **Task Quick Check**: Apply Q7 only.

---

## Step 3: Phase A — Concept Identification

### A-1: Name the Concept

For the feature or approach:
1. Does a known algorithm name, pattern name, or technology name exist?
2. When was it first published? (indicator of maturity)
3. Which domain does it belong to? (see table below)
4. Are there alternative names for the same problem?

### A-2: Domain-Specific Investigation Focus

| Domain | Concepts to Check | Key Resources |
|--------|------------------|----------------|
| ML / AI | Knowledge Distillation・LoRA・RAG・Active Learning・RLHF | arXiv cs.LG・Papers with Code |
| Web Backend | CQRS・Event Sourcing・Saga・Circuit Breaker・BFF | Martin Fowler's bliki・microservices.io |
| Web Frontend | Island Architecture・Optimistic UI・PRPL Pattern | web.dev・Chrome Developers |
| Mobile | Offline-first・MVVM/MVI・Unidirectional Data Flow | Apple Developer・Android Developers |
| Infrastructure | Blue-Green Deploy・Canary Release・GitOps・Cell-based Architecture | CNCF Landscape・AWS Architecture Blog |
| Data Platform | Medallion Architecture・Data Mesh・Lambda/Kappa・CDC | dbt blog・Databricks Engineering |
| Security | RBAC/ABAC・Zero Trust・PKCE・CSP | OWASP・NIST SP 800 |

### A-3: Research Resources

Choose 2-3 that match your domain. Reading 1-2 deeply is more valuable than skimming 10.

| Category | URL | Use Case |
|----------|-----|----------|
| ML Preprints | https://arxiv.org/list/cs.LG/recent | Latest ML algorithms |
| Papers with Code | https://paperswithcode.com/ | Paper + OSS mapping |
| Paper Search | https://www.semanticscholar.org/ | Citation count・Related work |
| Design Patterns | https://martinfowler.com/ / https://microservices.io/ | Backend・DDD・Microservices |
| Industry Radar | https://www.thoughtworks.com/radar | Adopt/Trial/Assess/Hold classification |
| Cloud Native | https://landscape.cncf.io/ | Infrastructure patterns |
| Frontend | https://web.dev/ | Browser・Performance patterns |
| Security | https://owasp.org/ | Vulnerabilities・Security standards |

---

## Step 4: Phase B — OSS / Implementation Discovery

Only execute Phase B after confirming in Phase A that the concept exists.

### B-1: Investigation Order
1. First check for reusable modules within the project
2. Check ecosystem official packages (npm・PyPI・crates.io・Hex etc.)
3. Check industry-standard OSS
4. Review reference implementations (no adoption yet — review only)

### B-2: License Tier Classification

| Tier | License Examples | Decision |
|------|-----------------|----------|
| **Tier 1** ✅ | MIT・BSD-2/3・Apache-2.0・ISC | Free to adopt |
| **Tier 2** ⚠️ | LGPL-2.1/3.0・MPL-2.0・EPL-2.0 | Usage model must be verified |
| **Tier 3** 🔴 | GPL-2.0/3.0・AGPL-3.0 | Legal review required |
| **Tier 4** ❌ | SSPL・Commons Clause・BSL・CC-BY-NC | Adoption prohibited |

### B-3: Build vs Use Decision

| Decision Criteria | Adopt Existing | Self-Implement |
|------------------|----------------|----------------|
| Feature Fit | Covers 80%+ of requirements | Covers <60% or requires fork |
| License | Tier 1 | Tier 3+ |
| Last Commit | within 12 months | 2+ years old |
| Strategic Differentiation | Non-core (utility/infrastructure) | Product core value |
| Self-Implementation Effort | >200 lines | <50 lines |

---

## Step 5: Record Investigation Results

Record the following in `templates/research.md` (or existing `research.md` in your project):

- Concept name and primary source URL
- Publication year and maturity
- Impact on design (Q7 answer)
- OSS candidates and SPDX license identifiers
- Decision: Adopt / Self-implement / N/A

**If no concept name was found**: Record "No concept name — new combination of X and Y" with reasoning.  
**If concept found but not as OSS**: Explain why self-implementation is a differentiator.

---

## Checklist

**Phase A (Concept-Level)**
- [ ] Applied Q1 + Q6 in requirements phase
- [ ] Applied all 7 questions in design phase
- [ ] Applied Q7 in task phase
- [ ] Searched for concept name (Result: Found / Not Found)
- [ ] If found: Recorded name・URL・publication year・maturity
- [ ] Checked ThoughtWorks Tech Radar classification

**Phase B (OSS-Level)**
- [ ] Checked for reusable modules within project
- [ ] Evaluated 1-3 OSS candidates
- [ ] Classified all candidates by SPDX License Tier
- [ ] Evaluated OSS health (last commit, contributor count)
- [ ] Applied Build vs Use matrix
- [ ] Recorded investigation results including URLs in research.md
