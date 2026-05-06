# Simulated Peer Reviews — HPI v0

Pre-publication review simulation pipeline. Reviewers' real positions are researched, projected onto HPI, and converted to simulated reviews + author responses. Full methodology in [`meta/methodology.md`](meta/methodology.md).

## v1 reviewer cohort (5)

| # | Reviewer | Phase 1 (dossier) | Phase 2 (projection) | Phase 3 (simulated review) | Phase 4 (response) | Phase 5 (real-vs-sim diff) |
|---|---|---|---|---|---|---|
| 1 | [Alex Karp](reviewers/karp.md) | ✅ | [✅](projections/karp.md) | [✅](simulated-reviews/karp.md) | [✅](responses/karp.md) | pending real review |
| 2 | [Sarah Wooders](reviewers/wooders.md) (Letta) | ✅ | [✅](projections/wooders.md) | [✅](simulated-reviews/wooders.md) | [✅](responses/wooders.md) | pending real review |
| 3 | [Andrej Karpathy](reviewers/karpathy.md) | 📝 STUB | — | — | — | — |
| 4 | [Tim Berners-Lee](reviewers/berners-lee.md) | 📝 STUB | — | — | — | — |
| 5 | [Sam Altman](reviewers/altman.md) (OpenAI) | 📝 STUB | — | — | — | — |

## Pipelines complete (2 of 5)

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

### Convergent finding (high-signal):

Karp's "meta vs Ontology" critique and Wooders' "kernel vs process" critique are **structurally the same observation**: the spec tends to claim more than it enforces, and HPI's value is as a boundary protocol that other architectures ride on. Two independent simulations from different angles point at the same fix. The combined revision (clarifying what HPI specifies vs what it recommends; honoring layer-vs-content distinction) addresses both.

**Combined: 15 spec revisions across 2 simulations, ~15-20 hours of revision work.**

## Order of priority for remaining 3

1. **Karpathy** next — high-signal LLM-systems voice; Twitter active so real engagement likely
2. **Berners-Lee** — protocol elder; real engagement low-probability but high-impact
3. **Altman** — least likely real engagement; highest forcing function for response prep

Recommend running Karpathy (3rd simulation) before deciding whether to continue. If Karpathy's simulation surfaces critiques substantially divergent from Karp + Wooders, the methodology has more to offer; if Karpathy converges on the same observations, diminishing returns set in.

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
