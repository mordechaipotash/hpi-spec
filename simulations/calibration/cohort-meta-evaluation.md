# Cohort meta-evaluation — calibration of v1 reviewer cohort

**Generated:** 2026-05-06
**Source:** Parallel session 20c9aa02 dispatched a researcher subagent (a7b135a5) to vet the v1 cohort against the Karp+Wooders convergence finding. That research output is integrated here.
**Purpose:** Document where the v1 cohort selection got it right, where it got it wrong, and what the v2 cohort should be.

---

## The TL;DR

**The v1 cohort selection (Karp/Karpathy/Wooders/Berners-Lee/Altman) was 2-of-5 right, 1-of-5 lucky, 2-of-5 wrong.** Replacing the wrong picks with the cohort-vetter's top recommendations produces a substantially better v2 cohort.

**Specifically:**
- Karp ✅ right (the catalyst critic; produced 7 spec revisions)
- Wooders ✅ right (architectural counterpart; produced 8 spec revisions including the load-bearing §4.1 split)
- Karpathy 🟡 lucky (the cohort-vetter judged him low-signal for HPI specifically — same reasoning as LeCun exclusion; in practice he produced the genuinely-new distillation gap design vector)
- Berners-Lee ❌ wrong (cohort-vetter excludes from top 10; too generic / unlikely real engagement)
- Altman ❌ wrong (cohort-vetter excludes from top 10; least likely to engage)

**The v2 cohort should drop Berners-Lee + Altman and add: Allen + Stenberg + Schneier (the top three "high engagement likelihood" candidates the vetter identified).**

---

## What the cohort-vetter produced

The parallel-session researcher dispatched against this question:

> *"Find reviewers whose priors will surface NEW critiques beyond the Karp/Wooders convergence — not more reviewers who'll repeat it."*

Researched against six axes likely uncovered:
1. Cryptography / formal threat model / key custody / partition behavior
2. Privacy law / GDPR / AI Act / regulatory leverage
3. Internet governance / standards bodies / W3C/IETF process
4. Web3 / decentralized identity (DID) / verifiable credentials
5. AI safety from non-product angle (controllability / honesty)
6. Information philosophy / what "cognitive substrate" means ontologically
7. Open-source protocol economics / capture dynamics

Then ranked the top 10 candidates by `(novelty of critique axis) × (real engagement likelihood)`.

---

## v2 cohort — top 10 ranked

| # | Reviewer | Critique axis | Engagement likelihood |
|---|---|---|---|
| 1 | **Christopher Allen** | Self-Sovereign Identity / W3C DID + VC ecosystem | **HIGH** — runs Agentic Internet Workshop (just launched 2026); just published 10-year SSI retrospective (Apr 26 2026) admitting the original 2016 principles were exploitable |
| 2 | **Bruce Schneier** | Formal cryptographic threat model / "Acting as Your Personal Political Proxy" | Medium-high — co-authored *Rewiring Democracy* (MIT Press, Oct 2025) with chapter on this exact problem |
| 3 | **Kaliya Young** | IIW operations / VC issuance + presentation / "No Phone Home" alignment | **HIGH** — running Agentic Internet Workshop at IIW 40 (Apr 28-30 2026) |
| 4 | **Cynthia Dwork** | Differential privacy / composability theory / formal privacy bounds | Medium — engages with formal protocol claims |
| 5 | **Moxie Marlinspike** | Key custody reality / decentralization-trends-toward-centralization | Low-medium — but his "first impressions of web3" essay directly contradicts HPI's sovereignty thesis |
| 6 | **Daniel Stenberg** (curl) | Wire-format completeness / IETF protocol pragmatics | **HIGH** — actively reviews protocol specs publicly |
| 7 | **Adam Langley** | Cryptographic audit log architecture / Certificate Transparency pattern | Medium |
| 8 | **Yoshua Bengio** | Agent honesty / oversight / LawZero | Low-medium — runs international AI safety report |
| 9 | **Stuart Russell** | Decision-theoretic agent control / objective alignment | Medium |
| 10 | **Cory Doctorow** | Protocol economics / enshittification / capture dynamics | **HIGH** — daily Pluralistic posts |

### Runners-up (5)
Luciano Floridi (info ontology), Max Schrems (GDPR enforcement), danah boyd (equity/access), Ben Laurie (HACL formal verification), Whitfield Diffie (foundational PK crypto).

### Honest exclusions
- **Ross Anderson** died March 2024 ❌
- **Patrick Collison** — last protocol writing 2019; covered by Doctorow
- **Phil Zimmermann** — homepage static, last activity ~2015-2016
- **Vint Cerf** — 82, no agent-substrate work
- **Holden Karnofsky** — Cold Takes stopped Jan 2024
- **Yann LeCun** — would debate context-window vs persistent-memory unit (signal-to-noise low for HPI specifically)
- **Maciej Ceglowski** — pivoted to NASA heat shields
- **Sherry Turkle** — psychological/sociological level, not architectural

### Two axes still uncovered after this top 10
1. **Equity/access** — who counts as a sovereign substrate-holder? Excludes people without technical capacity, stable internet, secure personal computing. boyd (#11) would force this.
2. **Cognitive science / human-prosthetic-interaction** — what does "cognitive substrate" mean phenomenologically? Closest proxy is Bengio.

---

## Where my v1 cohort selection went wrong

**Karp ✅ right.** The catalyst critic. The May 5 ontology gap finding was triggered by Karp/Thiel-style critique. Selecting him was correct. He produced 7 spec revisions including the load-bearing "cross-Ontology transport" framing.

**Wooders ✅ right.** Architectural counterpart with public Context Constitution. Produced 8 spec revisions including the central §4.1 split (access-control vs identity-persistence). The most operationally productive simulation.

**Karpathy 🟡 lucky.** I included him for "LLM-systems researcher with deep mechanistic knowledge." The cohort-vetter excluded him implicitly via the same reasoning as LeCun: *"would devolve into a debate about whether context-window attention vs. persistent memory is the right unit, not about the protocol boundary HPI specifies. Signal-to-noise ratio for HPI specifically: low."*

In practice, Karpathy produced the genuinely-new distillation gap (per-person LoRA / sovereign fine-tuning rights). This was the single new design vector across all three simulations. **The cohort-vetter was wrong in this specific case** — but the methodological point stands: Karpathy was a higher-variance pick than the top-ranked candidates. Lucky outcome on a marginal selection.

**Berners-Lee ❌ wrong.** I selected him as the protocol-elder + Solid creator. The cohort-vetter doesn't include him in top 10 (or even runners-up). Implicit reasoning: too generic, unlikely to engage with a v0 spec from an unknown author, and Christopher Allen + Daniel Stenberg better represent the "protocol elder" axis with HIGHER engagement likelihood. Allen specifically has been running working groups on exactly HPI's problem space for 10 years.

**Altman ❌ wrong.** I selected him as the "hyperscaler-default opposition" forcing function. The cohort-vetter excludes him implicitly. He won't engage substantively — and Cory Doctorow covers the political-economic critique against hyperscaler capture better and with HIGH engagement likelihood. Altman is a forcing-function-only pick; if no real engagement is plausible, the simulation produces less honest critique than if a representative who'd actually read the spec is chosen.

---

## v2 cohort recommendation

**Replace Berners-Lee + Altman with Allen + Stenberg.** Optionally add Schneier as #3 (the threat model angle is now partially covered by the just-shipped THREAT-MODEL.md, but Schneier's specific cryptographic-engineering critique would deepen it).

**Final v2 cohort:**

| # | Reviewer | Status |
|---|---|---|
| 1 | Karp | ✅ pipeline complete |
| 2 | Wooders | ✅ pipeline complete |
| 3 | Karpathy | ✅ pipeline complete |
| 4 | **Christopher Allen** (replacing Berners-Lee) | 📝 STUB |
| 5 | **Daniel Stenberg** (replacing Altman) | 📝 STUB |
| 6 | **Bruce Schneier** (added) | 📝 STUB |
| 7 | **Cory Doctorow** (added) | 📝 STUB |

Plus running-the-numbers candidates if the convergence is questioned:
- Kaliya Young — operational SSI / IIW alignment with Allen
- Cynthia Dwork — formal privacy bounds (Dwork would be highest-rigor reviewer if she engages)

---

## Why this calibration matters

The v1 cohort produced 22 spec revisions and triple-confirmed the central claim-vs-enforcement finding. This is real value. But the cohort-vetter's analysis suggests the v1 cohort was structurally suboptimal:

- **Two of five picks were unlikely to engage substantively** (Berners-Lee, Altman)
- **One was high-variance** (Karpathy — got lucky)
- **The vetter identified seven entirely-new critique axes** my v1 cohort missed (cryptography / privacy / DID / capture / formal verification / SSI ecosystem / IETF process)

The methodological lesson: **dispatch a cohort-vetter BEFORE picking the v1 cohort**, not after. Future protocol-spec authors using this simulation methodology should run the cohort-vetting research as a Phase 0 step.

---

## What's been executed since this calibration ran

While the cohort-vetter was running in parallel, the main session (and a follow-up) shipped:

- **THREAT-MODEL.md** (Schneier-predicted critique pre-empted)
- **19 of 22 simulation-identified spec revisions** committed in `1a358a1`
- **Chidush 019 ratified** to HELD-BELIEFS
- **GitHub Actions** for link-check + spec-stats + schema-validate
- **Repo pushed to private GitHub** (mordechaipotash/hpi-spec)

The v1 cohort's value is locked in. The v2 cohort decision is whether to run additional simulations (Allen + Stenberg + Schneier + Doctorow) before reader review, or whether the central finding is sufficiently confirmed and we pivot to real-reviewer outreach.

---

## Recommendation: Phase 0 ("dispatch cohort-vetter before picking") AND Allen-as-next

For this spec specifically: **run Allen as the v2 #4 simulation**. The W3C DID / VC ecosystem axis is genuinely orthogonal to all three v1 critiques. If Allen converges on the same claim-vs-enforcement finding, the central spec issue is now FIVE-confirmed across maximum-distance priors. If Allen surfaces SSI-lineage-specific revisions (citing W3C VC Data Model, DID Core, etc. in §9 lineage section), that's net-new spec value.

Stenberg and Schneier remain on deck. Doctorow could be the one who actually gets approached for a real review (highest engagement likelihood + critique axis perfectly orthogonal to the v1 cohort).

---

## Reading order rationale (per cohort-vetter)

> *"Run Allen (SSI/DID axis) and Stenberg (wire-format completeness) next. These are the two axes most likely to produce revisions orthogonal to Karp/Wooders. If they converge on the same meta-claim-vs-enforcement critique, that's strong evidence the spec's core gap has been fully identified. If Allen's W3C VC critique produces new citations/revisions and Stenberg's wire-format critique produces schema appendices, both are spec improvements that don't overlap."*
>
> *"Schneier is third — his threat model / key custody critique is the most likely to produce a new standalone document (THREAT-MODEL.md already stubbed in STATUS.md)."*

Note: THREAT-MODEL.md has now been DRAFTED. Schneier's simulation would calibrate against it — does the existing v0 threat model survive a Schneier read? That's a different test from "would Schneier identify the gap."
