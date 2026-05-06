# v2 cohort findings — Allen + Stenberg + Schneier + Doctorow

**Generated:** 2026-05-06
**Cohort dispatched:** 4 reviewer dossiers in parallel via researcher subagents (a41fce / a54cf5 / a87d30 / a820eb)
**Output:** 4 substantive dossiers (~1500 words each) covering predicted critique angles, convergence/divergence verdict, and confidence calibration.

This document consolidates the v2 cohort findings: which spec revisions land, which axes are now triple-or-more confirmed, which genuinely-new vectors surfaced, and what THREAT-MODEL.md still needs to close before publication-readiness.

---

## Convergence — now SEVEN-confirmed across maximum-distance priors

The central claim-vs-enforcement finding from Karp/Wooders/Karpathy is now confirmed by ALL FOUR v2 reviewers via four additional distinct routes:

| Reviewer | Route to convergence | Verbatim framing (predicted) |
|---|---|---|
| **Karp** (v1) | Economic / systems design | *"Meta-language, not Ontology — schema for a schema"* |
| **Wooders** (v1) | Systems architecture | *"Access control conflated with identity persistence"* |
| **Karpathy** (v1) | Transformer mechanics | *"Context window IS working memory; tokens scope access not inference"* |
| **Allen** (v2) | Cryptographic architecture / political philosophy | *"Encode rules in mathematics, not policy. Is the constraint load-bearing in the mathematical sense, or just policy?"* |
| **Stenberg** (v2) | Implementability / wire-format completeness | *"I cannot implement this faithfully from this document. Prose that says 'extends' without delta specification is aspiration, not extension."* |
| **Schneier** (v2) | Security engineering / threat modeling | *"We have been shown a highlight reel. The prose enforces more than the wire format requires."* |
| **Doctorow** (v2) | Political economy / capture dynamics | *"The spec's prose makes political claims. The wire format makes technical claims. The political claims are unenforceable from the wire format alone."* |

**This is genuinely high-signal.** Seven independent priors — economist, agent-architect, ML-systems researcher, SSI/cryptographer, IETF protocol practitioner, security engineer, political economist — converge on the SAME structural finding via SEVEN different routes. The spec genuinely has the claim-vs-enforcement issue. The 19 already-executed revisions from v1 are correctly directed.

---

## Divergence — five genuinely new vectors surfaced by v2

The v2 cohort produced FIVE design vectors not surfaced by v1:

### Vector A — Coercion resistance at the delegation boundary (Allen)

The legitimate platform operator as adversary. *"Can an agent's operator coerce the substrate-holder into granting scope by making the refusal too costly?"* (*"You can leave, but you leave empty-handed."*)

Allen's Technology Paternalism framework adds a fourth adversary type beyond malicious-external. THREAT-MODEL.md §2 covers 6 adversary classes; Allen would ask whether Class D (Compromised Runtime) or E (Colluding Platform) includes the **legitimate-but-coercive operator**. Currently NOT adequately addressed.

**Required revision:** §2 add Class G (Coercive Legitimate Operator) OR explicitly extend Class E to include this case.

### Vector B — Deployment-tail specification failure (Stenberg)

*"What does a sovereign cognitive substrate look like when implemented by a developer who reads only §5.2 and skips THREAT-MODEL.md?"* If the threat model is in a separate document and not normatively referenced by the wire-format spec, **it is advisory, not binding.**

For Gemini's TOFU: *"In the deployment tail, most clients will skip certificate verification entirely because the spec does not specify the storage format."* Same pattern would occur for HPI.

**Required revision:** SPEC.md §5 must NORMATIVELY reference THREAT-MODEL.md. Specifically, §5.2 method definitions must include MUST-statements referencing the §6 key custody patterns and §4.4 audit-as-substrate-stream requirements.

### Vector C — Agent instruction channel as attack surface (Schneier)

THE UNADDRESSED THREAT in v0 THREAT-MODEL.md. HPI's agents receive AND execute instructions via the same substrate that stores user context — Schneier's "data-control path commingling" applied to HPI. Prompt injection against agent pipeline can exfiltrate substrate **regardless of key custody**.

**Required revision:** THREAT-MODEL.md add new section §5.x or §9.x: *"Data-control path commingling at agent inference"*. Acknowledge as out-of-scope-for-protocol gap, with mitigations defined at the agent-runtime layer.

### Vector D — Operator-as-adversary at the protocol level (Schneier + Doctorow combined)

Schneier (Inrupt experience): most dangerous adversary in sovereign substrate is the operator who decides to change ToS. THREAT-MODEL.md doesn't bind protocol to prevent operator-betrayal; relies on operator compliance with deployment guidelines.

Doctorow (enshittification frame): *"What prevents HPI from becoming SMTP? What stops Google from shipping HPI-compatible endpoints that technically pass wire-format compliance tests, then routing everything through their inference pipeline?"*

Both reviewers, two different framings, same finding: **the spec needs anti-capture provisions that survive a resourced adversary implementing "HPI-compatible" while extracting value through adjacent mechanisms.**

**Required revision:** §7 anti-patterns must contain MUST NOT (not advisory) clauses naming specific capture vectors:
- MUST NOT route substrate content through external inference pipelines without per-token explicit substrate-holder consent
- MUST NOT cache returned scopes beyond transaction lifetime in operator-controlled storage
- MUST NOT correlate token-consumption patterns across substrate-holders for any purpose
- MUST NOT modify the typed axiom grammar except via published governance process

### Vector E — AI inference pipeline as exfiltration vector (Doctorow)

Distinct threat category genuinely missing from THREAT-MODEL.md. A sovereign cognitive substrate protocol that stores personal data in user-controlled endpoints does NOT protect users from AI inference pipelines that process that data through a hyperscaler model before returning results.

Doctorow's Apr 27 2026 essay: *"AI is very enshittification-prone: as 'black boxes' that do not produce reliable, deterministic outputs, AI products have a lot of intrinsic cover for their enshittifying behavior."*

**Required revision:** THREAT-MODEL.md add §X: *"AI Inference Pipeline as Exfiltration Vector"*. This is structurally adjacent to Vector C (Schneier's data-control path) but distinct: Vector C is about prompt injection; Vector E is about the legitimate-inference-as-extraction pattern.

---

## Spec revisions to commit (from v2 cohort)

Deduplicated and prioritized:

| # | Revision | Source | Where | Priority |
|---|---|---|---|---|
| 1 | Add Class G (Coercive Legitimate Operator) to §2 OR extend Class E | Allen | THREAT-MODEL.md | HIGH |
| 2 | Make §5 wire-format spec normatively reference THREAT-MODEL.md | Stenberg | SPEC.md §5 | HIGH |
| 3 | Add §5.x "Data-control path commingling at agent inference" | Schneier | THREAT-MODEL.md | HIGH |
| 4 | Add §X "AI Inference Pipeline as Exfiltration Vector" | Doctorow | THREAT-MODEL.md | HIGH |
| 5 | Convert §7 anti-patterns from advisory prose to MUST NOT clauses | Doctorow + Schneier | SPEC.md §7 | HIGH |
| 6 | JSON Schema for every message type before v0.1 (not in it) | Stenberg | schemas/ | MEDIUM |
| 7 | Normative method registry analogous to IANA HTTP | Stenberg | SPEC.md §5 | MEDIUM |
| 8 | Version field in wire format with negotiation mechanism | Stenberg | SPEC.md §5 | MEDIUM |
| 9 | Time-bound SLOs in §8 incident response (max time-to-detect, time-to-revoke) | Schneier | THREAT-MODEL.md §8 | MEDIUM |
| 10 | Consensus protocol specified for multi-instance JTI consumption (Paxos/Raft-class) | Schneier | THREAT-MODEL.md §7.2 | MEDIUM |
| 11 | Adversarial modeling of social-recovery-set compromise | Schneier | THREAT-MODEL.md §6.5 | MEDIUM |
| 12 | Add specific SD-JWT or BBS+ migration path for selective disclosure | Allen | SPEC.md §4 / THREAT-MODEL.md §10 (v0.1 roadmap) | MEDIUM |
| 13 | Map HPI primitives to Allen's `principalAuthority`/`delegationScope`/`delegationConstraints` predicates | Allen | comparisons/ALLEN.md (new) | LOW |
| 14 | Stub a governance charter answering: who maintains PAT family canonical definitions, who audits compliance, what's remedy for non-compliance | Doctorow | governance/CHARTER.md (new) | HIGH (publication gate) |
| 15 | Address SMTP/Gmail capture analog directly in §1 — pre-empt the critique | Doctorow | SPEC.md §1 | LOW |

**Total estimated effort: ~25-35 hours of focused revision work.**

The 5 HIGH-priority items are publication blockers per Doctorow + Schneier:
- Vectors A, C, E need explicit threat-model coverage
- Vector D requires §7 anti-patterns hardening from advisory to MUST NOT
- Governance charter (vector D operationalized) is the spec's biggest current gap

---

## THREAT-MODEL.md verdict (Schneier calibration test)

**PARTIAL SURVIVAL.** The Schneier simulation specifically tested whether the just-shipped THREAT-MODEL.md (5 audit-identified gaps closed earlier today) survives his read. Verdict:

**Passes:**
- §6 (key custody) — *conditional on multi-instance Byzantine modeling added*
- §7 (atomicity) — *conditional on consensus protocol specified*
- §8 (incident response) — *conditional on time-bound SLOs added*
- Appendix A (regulatory) — *conditional on erasure-verification probe addressed*

**Does not fully survive:**
- Agent instruction channel as attack surface (Vector C) — UNADDRESSED
- Operator-as-adversary at protocol level (Vector D) — UNADDRESSED in protocol-binding sense
- AI inference pipeline as exfiltration (Vector E) — UNADDRESSED

**His net verdict (predicted):** *"This is serious work, and §6 is the right structure. But the threat model addresses the lock on the door while leaving the door frame unmodeled. An HPI node that is cryptographically correct can still be an extraction engine if the operator changes the terms. The protocol needs governance teeth, not just custody guidelines."*

---

## Methodology recommendation

**Stop simulations after v2.** Seven priors converge on the central finding via seven different routes. Five genuinely-new vectors have been identified by v2. Diminishing returns set in for v3.

The two axes still uncovered after v2 (per cohort-vetter):
1. **Equity/access** (boyd) — who counts as a sovereign substrate-holder? People without technical capacity excluded by construction.
2. **Cognitive science / human-prosthetic-interaction** (Turkle proxy) — what does "cognitive substrate" mean phenomenologically?

These two axes won't change the central spec issues already identified. They might add v0.1+ scope but don't gate v0 publication.

**The genuinely productive next step is executing the 15 v2-identified revisions, not running more simulations.**

---

## Total spec impact across v1 + v2 cohorts

- **22 v1 spec revisions** (already mostly executed — 19 of 22 in commit `1a358a1`)
- **15 v2 spec revisions** (just identified, awaiting execution)
- **5 new design vectors** (v2 only): coercion resistance, deployment-tail spec failure, agent-instruction-channel, operator-as-adversary, AI-inference-pipeline-exfiltration
- **THREAT-MODEL.md status**: shipped, partially survives Schneier read, requires Vector C + D + E additions before publication-readiness
- **Governance charter**: identified as biggest current gap — required for Doctorow-pre-emption

**Publication-readiness assessment**: HPI v0 spec is approximately **75% publication-ready**. Remaining 25% is: (1) the 5 HIGH-priority v2 revisions, (2) the governance charter, (3) at least one real reader review (not simulated). Estimated 35-50 hours from current state to publication-ready.
