# Simulated Peer Reviews — HPI v0

Pre-publication review simulation pipeline. Reviewers' real positions are researched, projected onto HPI, and converted to simulated reviews + author responses. Full methodology in [`meta/methodology.md`](meta/methodology.md).

## v1 reviewer cohort (5)

| # | Reviewer | Phase 1 (dossier) | Phase 2 (projection) | Phase 3 (simulated review) | Phase 4 (response) | Phase 5 (real-vs-sim diff) |
|---|---|---|---|---|---|---|
| 1 | [Alex Karp](reviewers/karp.md) | ✅ | [✅](projections/karp.md) | [✅](simulated-reviews/karp.md) | [✅](responses/karp.md) | pending real review |
| 2 | [Sarah Wooders](reviewers/wooders.md) (Letta) | ✅ | [✅](projections/wooders.md) | [✅](simulated-reviews/wooders.md) | [✅](responses/wooders.md) | pending real review |
| 3 | [Andrej Karpathy](reviewers/karpathy.md) | ✅ | [✅](projections/karpathy.md) | [✅](simulated-reviews/karpathy.md) | [✅](responses/karpathy.md) | pending real review |
| 4 | [Tim Berners-Lee](reviewers/berners-lee.md) | 📝 STUB | — | — | — | — |
| 5 | [Sam Altman](reviewers/altman.md) (OpenAI) | 📝 STUB | — | — | — | — |

## Pipelines complete (3 of 5)

### Karp pipeline produced:
- **7 spec revisions** committed (cross-Ontology framing in §3.7, PAT promoted to Reference Domain Ontology, substrate-holder primitive in §2.1 + institutional example, etc.)
- **1 new file** to draft (`THREAT-MODEL.md`) addressing the sharpest objection
- **1 new framing claim** (HPI as cross-Ontology transport) strengthening positioning
- **1 acknowledged philosophical disagreement** (meta-Ontologies as inherently academic) that survives revision

### Wooders pipeline produced:
- **8 spec revisions** committed (split §4.1 into access-control + persistence-recommendation, add §4.10 Failure modes, add §4.11 Learning across boundaries, etc.)
- **1 new framing handle** ("HPI as kernel, stateful agents as processes") credited to Wooders
- **1 acknowledged philosophical disagreement** (agent persistence-as-self alignment risk vs foundation of capability) at axiom level
- **4 substantive endorsements** catalogued for positioning

### Karpathy pipeline produced:
- **5 spec revisions** committed (§4.12 boundary conditions, §1.8 what HPI does not solve, §6 citation validator, §6.3 microHPI aesthetic, anthropomorphic-language pass)
- **1 NEW DESIGN VECTOR** (the distillation gap): per-person LoRA / sovereign fine-tuning rights as complementary primitive HPI v0 doesn't address. **This is genuinely new ground vs Karp+Wooders.**
- **6 substantive endorsements** catalogued (highest of the three reviewers — most aligned with HPI's positions)

### Convergence finding (TRIPLY CONFIRMED):

Karp's "meta vs Ontology," Wooders' "kernel vs process," and Karpathy's "context window IS working memory" are **structurally the same observation arrived at via three different routes**:

- **Karp:** economic / systems design — what does the protocol guarantee at boundary?
- **Wooders:** systems architecture — access control conflated with identity persistence
- **Karpathy:** transformer mechanics — protocol-layer scoping cannot constrain inference once tokens are in context

**Three independent priors → three different routes → same conclusion.** This is high-signal evidence that the spec genuinely has the claim-vs-enforcement issue and the planned revisions address something real, not artifact-of-simulation.

### Divergence finding (Karpathy alone):

Karpathy adds the distillation/continual-learning gap. The right primitive for sovereign personalization may be per-person LoRA / sovereign fine-tuning rights, not scoped-view tokens. HPI v0 doesn't address this. Whether to extend to v1 is now a real architectural question, named in §1.8.

**Combined: 22 distinct spec revisions across 3 simulations, ~25-30 hours of revision work.**

## Order of priority for remaining 2

The methodology recommends STOPPING here. Three simulations have triply-confirmed the central spec issue and surfaced one genuinely new design vector. Berners-Lee and Altman would likely converge on the same central finding with new flavor (governance and hyperscaler-defense respectively) but unlikely to surface another design vector as substantial as Karpathy's distillation gap.

If continuing:
1. **Berners-Lee** — protocol elder; real engagement low-probability but high-impact for credibility if it happens
2. **Altman** — least likely real engagement; highest forcing function for response prep

Recommend executing the 22 spec revisions before further simulations. The methodology has produced what it was designed to produce.

## What this is NOT

- Not a replacement for real review (cannot catch genuine bugs)
- Not gaslighting (simulated reviews are clearly labeled as such)
- Not infinitely scalable (~3-5 hours per simulation)
- Not deterministic (different simulation sessions surface different objections; this is feature not bug)

## What this IS

- Pre-publication stress test of the spec against named priors
- Author preparation for likely real-reviewer objections
- A meta-use-case for HPI itself (agents borrow scoped reviewer-public-content to simulate review)
- Publishable artifact alongside the spec — "here's what I expected smart critics to say; here's why the spec survives"

See [`meta/methodology.md`](meta/methodology.md) for the full pipeline specification.
