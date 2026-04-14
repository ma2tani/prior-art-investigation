# Prior Art & Concept Investigation Template

> **How to use**: Copy this file as a research log (`research.md`) or into your project's documentation directory.  
> Replace bracketed `[…]` sections with actual investigation results. Mark items not found in investigation as "N/A".

---

## Named Concept / Prior Art

### Concept Table

| Field | Content |
|-------|---------|
| **Concept Name** | `[Concept Name]` OR "No concept name — new combination of `[X]` and `[Y]`" |
| **Publication Year / Source** | `[YYYY year]` / `[Author name, publication venue]` |
| **Maturity** | `[ ]` Production Ready `[ ]` Experimental `[ ]` Theoretical `[ ]` Deprecated |
| **Paper / Specification URL** | `[https://...]` |
| **Reference Implementation URL** | `[https://...]` or "N/A" |
| **Impact on Design** | `[Q7 answer: How does this concept name change your design?]` |
| **Differentiating Self-Implementation** | `[Explanation of where existing concept is not adopted or modified]` OR "N/A — direct application" |

---

## OSS Candidates Table

| Candidate | License (SPDX) | Last Commit | Stars / Downloads | Adoption Decision | Reference URL |
|-----------|----------------|-------------|-------------------|-------------------|----------------|
| `[Package Name A]` | `[MIT]` | `[YYYY-MM]` | `[XXk]` | ✅ Adopt / ⚠️ Review / ❌ Reject | `[https://...]` |
| `[Package Name B]` | `[Apache-2.0]` | `[YYYY-MM]` | `[XXk]` | ✅ Adopt / ⚠️ Review / ❌ Reject | `[https://...]` |
| `[Package Name C]` | `[GPL-3.0-only]` | `[YYYY-MM]` | `[XXk]` | ❌ Tier 3 — Adoption Prohibited | `[https://...]` |

---

## Investigation Steps

### Step 1: Concept Naming (Phase A)

Questions and answers from investigation:

**Q1 (First Principles)**: `[Is the problem framework correct?]`

> `[Answer]`

**Q2 (Null Hypothesis)**: `[Why hasn't this approach already become mainstream?]`

> `[Answer]`

**Q3 (Start with Failure)**: `[How many people have failed with this approach?]`

> `[Answer]`

**Q4 (Find the Expert)**: `[Who is the expert thinking deepest about this domain?]`

> `[Answer]`

**Q5 (Read Primary Sources)**: `[Have you read papers, RFCs, commit logs, Issues?]`

> `[Answer]`

**Q6 (Inversion)**: `[If this failed in the worst way, what would be the cause?]`

> `[Answer]`

**Q7 (So What)**: `[Now that you've named the concept, how does it change your design?]`

> `[Answer]`

---

### Step 2: OSS Discovery (Phase B)

**Candidates Investigated**:

1. `[Candidate Name A]`
   - License: `[SPDX identifier]` → Tier `[1/2/3/4]`
   - Last Commit: `[YYYY-MM-DD]`
   - Feature Fit: `[XX]`%
   - Decision: `[Adoption reason / Rejection reason]`

2. `[Candidate Name B]`
   - License: `[SPDX identifier]` → Tier `[1/2/3/4]`
   - Last Commit: `[YYYY-MM-DD]`
   - Feature Fit: `[XX]`%
   - Decision: `[Adoption reason / Rejection reason]`

---

### Step 3: Final Decision

| Decision | Content |
|----------|---------|
| **Adoption Decision** | `[ ]` Adopt existing OSS  `[ ]` Self-implement  `[ ]` Hybrid (OSS + self-implementation) |
| **OSS to Adopt** | `[Package Name]` version `[x.y.z]` or "None" |
| **Self-Implementation Rationale** | `[Reason]` or "Existing OSS covers all requirements" |
| **Remaining Risks** | `[Potential issues]` or "None" |
