# Simulated Peer Reviews — HPI v0

Pre-publication review simulation pipeline. Reviewers' real positions are researched, projected onto HPI, and converted to simulated reviews + author responses. Full methodology in [`meta/methodology.md`](meta/methodology.md).

## v1 reviewer cohort (5)

| # | Reviewer | Phase 1 (dossier) | Phase 2 (projection) | Phase 3 (simulated review) | Phase 4 (response) | Phase 5 (real-vs-sim diff) |
|---|---|---|---|---|---|---|
| 1 | [Alex Karp](reviewers/karp.md) | ✅ | [✅](projections/karp.md) | [✅](simulated-reviews/karp.md) | [✅](responses/karp.md) | pending real review |
| 2 | [Sarah Wooders](reviewers/wooders.md) (Letta) | 📝 STUB | — | — | — | — |
| 3 | [Andrej Karpathy](reviewers/karpathy.md) | 📝 STUB | — | — | — | — |
| 4 | [Tim Berners-Lee](reviewers/berners-lee.md) | 📝 STUB | — | — | — | — |
| 5 | [Sam Altman](reviewers/altman.md) (OpenAI) | 📝 STUB | — | — | — | — |

## Karp pipeline — what it produced

The Karp simulation (one full pipeline cycle) generated:
- **3 spec revisions** committed (cross-Ontology framing in §3.7, PAT promoted to Reference Domain Ontology, substrate-holder primitive in §2.1 + institutional example)
- **1 new file** to draft (`THREAT-MODEL.md`) addressing the sharpest objection
- **1 new framing claim** (HPI as cross-Ontology transport) strengthening positioning
- **1 acknowledged philosophical disagreement** (meta-Ontologies as inherently academic) that survives revision

By methodology success criteria: this simulation is **useful** (≥1 spec revision, ≥1 fortified counter-argument, ≥1 named axiom-level disagreement).

## Order of priority for remaining 4

1. **Wooders** — comparison doc already drafted; lowest-friction simulation
2. **Karpathy** — high-signal LLM-systems voice; Twitter active so real engagement likely
3. **Berners-Lee** — protocol elder; real engagement low-probability but high-impact
4. **Altman** — least likely real engagement; highest forcing function for response prep

Recommend running 2-3 more simulations before publication; full 5 is not strictly required.

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
