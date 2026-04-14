# OSS Evaluation Rules

> **Scope**: These rules apply throughout the prior art investigation (Phase A/B) for comprehensive OSS evaluation.
> **Standalone Capable**: No Kiro SDD required. Usable in any development workflow.

---

## Phase A: Concept-Level Investigation

### A-0: Seven Questions to Begin

Answer the following questions before starting design. Do not proceed to design without answering all questions.

| # | Question |
|---|----------|
| Q1 | Is this problem framework correct? Are you solving the right problem? |
| Q2 | Why hasn't this approach already become mainstream? |
| Q3 | How many people have failed with this approach? How did they fail? |
| Q4 | Who thinks most deeply about this domain? Where are their words written? |
| Q5 | Have you read primary sources (papers, RFCs, commit logs, Issues)? |
| Q6 | If this failed in the worst possible way, what would be the cause? |
| Q7 | Now that you've named the concept, how does it change your design? |

### A-1: Naming Convention

- **Concept Identification**: Identify known algorithm names, pattern names, or technology names
- **Multiple Reference Names**: The same concept may have multiple names (e.g., "KD" vs "Knowledge Distillation")
- **Publication Year Recording**: Necessary to measure future obsolescence risks
- **Maturity Assessment**: Classify as Production Ready / Experimental / Theoretical / Deprecated

### A-2: Domain-Specific Investigation Scope

| Domain | Concepts to Investigate |
|--------|------------------------|
| ML / AI | Knowledge Distillation・LoRA・RAG・Active Learning・RLHF・Vector Stores |
| Web Backend | CQRS・Event Sourcing・Saga・Circuit Breaker・BFF・Hexagonal Architecture |
| Web Frontend | Island Architecture・Optimistic UI・PRPL Pattern・Micro Frontends |
| Mobile | Offline-first・MVVM/MVI・Unidirectional Data Flow・Composable Navigation |
| Infrastructure | Blue-Green Deploy・Canary Release・GitOps・Cell-based Architecture・eBPF |
| Data Platform | Medallion Architecture・Data Mesh・Lambda/Kappa・CDC・dbt Metrics |
| Security | RBAC/ABAC・Zero Trust・PKCE・CSP・SSRF Protection |

### A-3: Investigation Resources

| Category | URL | Use Case |
|----------|-----|----------|
| ML Preprints | https://arxiv.org/list/cs.LG/recent | Latest ML algorithms |
| Papers with Code | https://paperswithcode.com/ | Papers + OSS mapping |
| Paper Search | https://www.semanticscholar.org/ | Citation count & related work |
| Design Patterns | https://martinfowler.com/ | Backend・DDD・Microservices |
| Microservices | https://microservices.io/ | Pattern library |
| Industry Radar | https://www.thoughtworks.com/radar | Adopt/Trial/Assess/Hold classification |
| Cloud Native | https://landscape.cncf.io/ | Infrastructure patterns |
| Frontend | https://web.dev/ | Browser・Performance patterns |
| Security | https://owasp.org/ | Vulnerabilities・Security standards |

### A-4: Recording Concept Results

Record findings in `templates/research.md` under the "Named Concept / Prior Art" section.

**Required fields**:
- Concept name (if found) or "No concept name — new combination of [X] and [Y]" (if not found)
- Primary source URL
- Publication year and maturity
- Q7 answer: Why this concept name changes your design

---

## Phase B: OSS-Level Evaluation

### B-1: Investigation Order (Mandatory)

1. Check for reusable modules within the project first
2. Check official ecosystem packages (npm・PyPI・crates.io・Hex)
3. Check industry-standard OSS
4. Review reference implementations only (no adoption yet)

### B-2: License Tier Classification

Classify all OSS candidates by SPDX identifier into Tiers.

| Tier | SPDX License Examples | Decision |
|------|----------------------|----------|
| **Tier 1** ✅ Adoptable | MIT・BSD-2-Clause・BSD-3-Clause・Apache-2.0・ISC・0BSD | Can adopt without override |
| **Tier 2** ⚠️ Conditional | LGPL-2.1-only・LGPL-3.0-only・MPL-2.0・EPL-2.0・CDDL-1.0 | Usage model must be verified |
| **Tier 3** 🔴 Legal Review Required | GPL-2.0-only・GPL-3.0-only・AGPL-3.0-only・OSL-3.0 | Adoption prohibited without legal approval |
| **Tier 4** ❌ No Adoption | SSPL-1.0・Commons Clause・BSL-1.1・CC-BY-NC-*・Proprietary | Prohibited from adoption |

**If license is not found**: Do not adopt that OSS.

### B-3: OSS Health Evaluation

Even if license is Tier 1 or 2, evaluate:
- **Last Commit**: Must be within 12 months (flag if 2+ years old)
- **Contributor Count**: Single-person projects are risky (2+ recommended)
- **Open Issues**: Fewer bug issues better than many feature requests
- **Successor Project**: If archived, consider switching to successor

### B-4: Build vs Use Decision Matrix

| Decision Criteria | Score +1 (Adopt Existing) | Score −1 (Self-Implement) |
|------------------|---------------------------|--------------------------|
| Feature Fit | Covers 80%+ of requirements | Covers <60% or requires fork |
| License | Tier 1 | Tier 3+ |
| Last Commit | within 12 months | 2+ years old |
| Strategic Differentiation | Non-core (utility/infrastructure) | Product core value |
| Self-Implementation Effort | >200 lines | <50 lines |

**Total Score ≥ +2 → Recommend adopting existing OSS**  
**Total Score ≤ 0 → Recommend self-implementation (document reasoning)**

---

## Completion Checklist

**Phase A (Concept-Level)**
- [ ] Answered all Q1-Q7 (design phase) or Q1+Q6 only (requirements phase)
- [ ] Searched for concept name (Result: Found / Not Found)
- [ ] If found: Recorded name・URL・publication year・maturity in research.md
- [ ] If not found: Recorded "No concept name — new combination of [X] and [Y]" with reasoning
- [ ] Checked ThoughtWorks Tech Radar classification

**Phase B (OSS-Level)**
- [ ] Checked for reusable modules within project
- [ ] Evaluated 1-3 OSS candidates
- [ ] Classified all candidates by SPDX License Tier
- [ ] Evaluated OSS health (last commit, contributor count)
- [ ] Applied Build vs Use matrix
- [ ] Recorded investigation results including URLs in research.md
- [ ] Reflected adoption decision (adopt/self-implement/N/A) in design document
