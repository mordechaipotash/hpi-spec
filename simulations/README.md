# Simulated Peer Reviews — HPI v0

Pre-publication review simulation pipeline. Reviewers' real positions are researched, projected onto HPI, and converted to simulated reviews + author responses. Full methodology in [`meta/methodology.md`](meta/methodology.md). Cohort calibration in [`calibration/cohort-meta-evaluation.md`](calibration/cohort-meta-evaluation.md).

## v1 cohort (3 of 5 executed; remaining 2 deprecated)

| # | Reviewer | Phase 1 (dossier) | Phase 2 (projection) | Phase 3 (simulated review) | Phase 4 (response) | Phase 5 (real-vs-sim diff) |
|---|---|---|---|---|---|---|
| 1 | [Alex Karp](reviewers/karp.md) | ✅ | [✅](projections/karp.md) | [✅](simulated-reviews/karp.md) | [✅](responses/karp.md) | pending real review |
| 2 | [Sarah Wooders](reviewers/wooders.md) (Letta) | ✅ | [✅](projections/wooders.md) | [✅](simulated-reviews/wooders.md) | [✅](responses/wooders.md) | pending real review |
| 3 | [Andrej Karpathy](reviewers/karpathy.md) | ✅ | [✅](projections/karpathy.md) | [✅](simulated-reviews/karpathy.md) | [✅](responses/karpathy.md) | pending real review |
| 4 | ~~Tim Berners-Lee~~ | **DEPRECATED** — excluded by cohort-vetter (too generic / unlikely engagement) | | | | |
| 5 | ~~Sam Altman~~ | **DEPRECATED** — excluded by cohort-vetter (least likely engagement) | | | | |

## v2 cohort (DOSSIERS COMPLETE — Phase 1 only; full simulation pending)

| # | Reviewer | Phase 1 (dossier) | Critique axis | Convergence test | New vector surfaced |
|---|---|---|---|---|---|
| 4 | [Christopher Allen](reviewers/allen.md) | ✅ | SSI / W3C / cryptographic architecture | ✅ Converges | **Coercion resistance at the delegation boundary** (legitimate platform operator as adversary) |
| 5 | [Daniel Stenberg](reviewers/stenberg.md) | ✅ | Wire-format completeness / IETF pragmatics | ✅ Converges | **Deployment-tail specification failure** (advisory threat model = unbinding) |
| 6 | [Bruce Schneier](reviewers/schneier.md) | ✅ | Cryptographic threat model / Inrupt experience | ✅ Converges (calibration: THREAT-MODEL.md PARTIALLY survives) | **Agent instruction channel as attack surface** + **Operator-as-adversary at protocol level** |
| 7 | [Cory Doctorow](reviewers/doctorow.md) | ✅ | Political economy / enshittification | ✅ Converges | **AI inference pipeline as exfiltration vector** + **Anti-capture provisions as wire-format MUST-NOTs** |

**Consolidated v2 findings: [`calibration/v2-cohort-findings.md`](calibration/v2-cohort-findings.md)**

## v1 cohort — what each pipeline produced

### Karp pipeline:
- **7 spec revisions** committed (cross-Ontology framing in §3.7, PAT promoted to Reference Domain Ontology, substrate-holder primitive in §2.1 + institutional example, etc.)
- **THREAT-MODEL.md** drafted (highest-leverage single artifact)
- **1 framing claim** (HPI as cross-Ontology transport) strengthening positioning
- **1 acknowledged philosophical disagreement** (meta-Ontologies as inherently academic)

### Wooders pipeline:
- **8 spec revisions** committed (split §4.1 into access-control + persistence-recommendation, add §4.10 Failure modes, add §4.11 Learning across boundaries, etc.)
- **1 framing handle** ("HPI as kernel, stateful agents as processes") credited to Wooders
- **1 acknowledged philosophical disagreement** (agent persistence-as-self alignment risk vs foundation of capability)
- **4 substantive endorsements** catalogued

### Karpathy pipeline:
- **5 spec revisions** committed (§4.12 boundary conditions, §1.8 what HPI does not solve, §6 citation validator, §6.3 microHPI aesthetic, anthropomorphic-language pass)
- **1 NEW DESIGN VECTOR** (the distillation gap): per-person LoRA / sovereign fine-tuning rights as complementary primitive HPI v0 doesn't address
- **6 substantive endorsements** catalogued

### Triple-confirmed convergence finding:

Karp's "meta vs Ontology," Wooders' "kernel vs process," and Karpathy's "context window IS working memory" are **structurally the same observation arrived at via three different routes**:

- **Karp:** economic / systems design — what does the protocol guarantee at boundary?
- **Wooders:** systems architecture — access control conflated with identity persistence
- **Karpathy:** transformer mechanics — protocol-layer scoping cannot constrain inference once tokens are in context

**Three independent priors → three different routes → same conclusion.** This is high-signal evidence that the spec genuinely has the claim-vs-enforcement issue.

### Divergence finding (Karpathy alone):

Per-person LoRA / sovereign fine-tuning rights may be the correct architecture for durable sovereign personalization, complementary to scoped-view tokens. HPI v0 silent on this. §1.8 now names the gap explicitly.

## Cohort meta-evaluation (2026-05-06)

A parallel-session researcher dispatched against "find reviewers whose priors will surface NEW critiques beyond Karp/Wooders convergence" produced a ranked top-10 list. Findings:

- **v1 cohort: 2 right (Karp, Wooders), 1 lucky (Karpathy), 2 wrong (Berners-Lee, Altman).**
- BL + Altman should be replaced with Allen + Stenberg as v2 cohort.
- Schneier added (calibration test against just-shipped THREAT-MODEL.md).
- Doctorow added (political-economic axis with HIGH engagement likelihood).
- Two axes still uncovered after v2 top 10: equity/access (boyd) and cognitive science / human-prosthetic (Turkle proxy).

Full analysis: [`calibration/cohort-meta-evaluation.md`](calibration/cohort-meta-evaluation.md).

## Spec impact across all simulations (so far)

**22 distinct simulation-identified spec revisions** combined across Karp + Wooders + Karpathy.
**19 already executed** (as of commit `1a358a1`).
**3 still outstanding** (the lower-priority polish revisions).

THREAT-MODEL.md drafted (covering Karp #4 + Schneier-predicted critiques).
Chidush 019 ratified to HELD-BELIEFS.

## Order of priority for v2

1. **Allen** next — SSI/DID axis, orthogonal to all v1 critiques, HIGH engagement
2. **Stenberg** — wire-format completeness, would produce JSON Schema requirements
3. **Schneier** — calibration test of THREAT-MODEL.md
4. **Doctorow** — capture dynamics + governance, HIGH engagement public exposure

If Allen + Stenberg both converge on the central claim-vs-enforcement finding, the spec issue is **5-confirmed across maximum-distance priors** and we stop. If they diverge, each adds new ground.

Recommend running Allen first, then evaluating whether to continue.

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
