# Simulated Peer Review — Methodology

**Last updated:** 2026-05-06
**Author:** Mordechai Potash

## Why simulate

Real peer review is slow (2-4 weeks per reviewer), bandwidth-limited (5-8 candidates max), and asymmetric (politeness suppresses criticism). Simulated review is fast, infinite, and brutally honest by construction.

Critically: simulated review is NOT a replacement for real review. It cannot catch genuine bugs (which depend on careful reading). It DOES predict structural objections and validate whether the spec survives a skeptical reading from named priors. The two complement each other.

A second purpose: this pipeline is itself an HPI use case. Agents borrow scoped views of public reviewer content to simulate critique, with provenance back to source material. Building it tests whether HPI's primitives are practical or theoretical.

## The 5 reviewers (v1 cohort)

Selected to span the critique surface. Each reviewer covers a distinct axis where HPI's position has the most pressure:

| # | Reviewer | Axis | Why this person |
|---|---|---|---|
| 1 | **Alex Karp** (Palantir CEO) | Ontology / sovereignty skeptic | The May 5 brainstorm was triggered by a Karp/Thiel-style "the stack lacks an ontology layer" critique. He's the actual originator of the axis HPI now formalizes. Harshest believable critic. |
| 2 | **Andrej Karpathy** | LLM-systems researcher | Prolific, public, technically deep. Will scrutinize agent-as-borrower claims at the operational level — does the model's working memory de facto own context during a transaction? |
| 3 | **Sarah Wooders** (Letta) | Architectural counterpart | Co-author of Letta's Context Constitution. HPI inverts Letta's axiom; she's the most informed possible peer reviewer of that inversion. |
| 4 | **Tim Berners-Lee** | Protocol veteran | Shipped Solid (closest existing precedent). Will scrutinize naming, semantics, failure modes, governance with two decades of protocol-design experience. |
| 5 | **Sam Altman** (OpenAI) | Hyperscaler default | Represents the architecture HPI explicitly opposes. Simulation forces the spec to survive its strongest opposition. |

Future cohorts (not v1):
- Bruce Schneier — privacy / security third-party
- Patrick Collison — Stripe-as-protocol-with-rent precedent
- Vint Cerf — protocol elder, internet-architecture lens
- Real reviewers from your immediate orbit (Shaul, Yitzhak, Plurality founder) — these get separate dossiers when scheduled

## The pipeline (5 phases)

### Phase 1: Research dossier (`reviewers/<name>.md`)

For each reviewer, assemble:
- **Public writings** (last 3 years, weighted toward recent). Books, blog posts, interviews, talks, tweets.
- **Working code** patterns (GitHub, talks about codebases they've shipped).
- **Stated values + intellectual lineage.** Who do they cite approvingly? Who do they oppose?
- **Patterns of critique.** What do they typically attack? What do they typically endorse?
- **Adjacency to HPI.** Have they engaged with related problems? At what depth?
- **Typical review register.** Length, sharpness, formality, vocabulary.

Tools: WebSearch + WebFetch + Brain MCP semantic search + GitHub. Time: ~2-4 hours per public reviewer; ~30 min for ones with small public surface.

Dossier output: 800-1500 words covering the above. Quoted source material is preferred; paraphrase only when source is unavailable.

### Phase 2: Position projection (`projections/<name>.md`)

Given the dossier + the HPI SPEC, project:
- **Overall stance** prediction (warm / cold / mixed) with confidence
- **Sections they'll engage with most** (which of §1-§9 attracts their attention)
- **Specific objections likely to surface**, ranked by probability
- **Specific praise likely** (predict where they AGREE, not just where they critique)
- **Areas they'll be agnostic on**

This is a calibrated-prediction exercise. Should be done with both the dossier AND the spec in context. Output: 600-1000 words.

### Phase 3: Simulated review (`simulated-reviews/<name>.md`)

Generate a full review in their voice:
- Inline section-by-section comments
- Top-level summary critique
- Suggestions for revision
- Outright rejections of specific claims if applicable
- Closing recommendation (publish / revise / reject)

Calibrated to:
- Their typical review length
- Their typical register (formal vs informal, professorial vs blunt)
- Their typical structure (numbered objections, narrative essay, Twitter-thread fragments)
- Their vocabulary patterns (what they call things; their preferred metaphors)

Output: variable length, matching their typical output. Some reviewers (Karpathy) write 800-word focused critiques; some (Berners-Lee) write 3000-word essays.

### Phase 4: Author response (`responses/<name>.md`)

For each simulated review, Mordechai writes:
- **Steelman.** The strongest version of their critique you can construct.
- **Where it lands.** Spec changes you commit to.
- **Where it doesn't land.** Defended position with reasoning.
- **Where the disagreement is at axiom level.** Acknowledged but not moved.

This is the value-extraction phase. The simulation only matters if it produces revisions or fortified arguments. If a simulation generates zero of either, the reviewer's dossier is probably underdeveloped.

### Phase 5: Calibration (post-hoc)

When the corresponding real reviewer responds, diff their review against the simulated one. Track:
- **Predicted hits** (simulated objection → real objection within tolerance)
- **Misses** (simulated objection that didn't surface)
- **Surprises** (real objections you didn't predict)
- **Methodology updates** for the next cohort

Calibration data accrues in `calibration/<name>.md` with date-stamped diffs.

## What this is NOT

- Not a replacement for real review (the simulation cannot catch genuine bugs)
- Not a way to gaslight readers (publishing simulated reviews labeled as such is fine; passing as real is fraudulent)
- Not infinitely scalable (~3-5 hours per simulation; 5 reviewers ≈ 25 hours of focused work)
- Not deterministic (different LLM sessions produce different simulated reviews; this is a feature for surfacing different objections, not a bug)

## Validation criteria

A simulation is **useful** if it produces at least ONE of:
- A specific spec revision Mordechai commits to
- A counter-argument Mordechai didn't have before
- A clarification of an axiom-level disagreement that needs explicit acknowledgement

A simulation is **failed** if it produces zero of these. Failure usually means the dossier was too thin or the projection over-fit to easy critiques.

## Time + cost estimate

- **Per simulation:** 3-5 hours (1-2 hr dossier, 30 min projection, 1-2 hr review, 30 min response)
- **5-reviewer cohort:** 15-25 hours of focused work
- **LLM cost:** ~$5-10 per reviewer in tokens (Claude or comparable)
- **Total wall-clock:** ~1 week of part-time work to produce all 5

## Order of operations

Do reviewers in this order, picking up where signal is highest:

1. **Karp first** (highest-leverage, hardest critique, sets the bar)
2. **Wooders second** (architectural counterpart; comparison doc already exists, easy template)
3. **Karpathy third** (technical depth; Twitter writing is easy to dossier)
4. **Berners-Lee fourth** (protocol elder; Solid material is canonical)
5. **Altman last** (hyperscaler perspective; least new — you've been steelmanning his position implicitly throughout)

If any of the first 3 produces a fundamental issue with the methodology, regroup before the last 2.
