# Author response — Mordechai to simulated Karp review

**Generated:** 2026-05-06
**Reading the simulated review:** [`../simulated-reviews/karp.md`](../simulated-reviews/karp.md)

This is the value-extraction phase. For each substantive critique in the simulated review, I steelman it, decide whether it lands, and either commit to a revision or fortify the current position.

---

## Critique 1: "Meta-language, not Ontology" (the central objection)

**Steelman:** The HPI spec specifies how to type the *epistemic status* of claims (this thing is an obligation, this is a recognition, this is a trust assertion, this is a pattern). It does not specify what *kinds of objects* exist in any specific world. By Karp's standard — Ontology = "what exists in this domain, with typed properties and actions" — HPI is one level too abstract. The PAT family commits closer to a real Ontology (Patent has a typed identity, jurisdictional fan-out, lifecycle states), but even PAT is more "axioms about patents" than "Patent as typed object graph."

**Where it lands:** The objection is structurally correct. HPI v0 IS deliberately meta. This is not a bug; it's the architectural choice. **But the spec does not make this distinction clear enough**, and a serious reader will reach the same conclusion as the simulated Karp.

**Revision committed:**

1. **Add §3.7 "What HPI is and is not at the Ontology level"** to SPEC.md. Explicit framing: HPI is the protocol layer at which *typed substrate-boundary handoff* occurs. Domain Ontologies (Palantir's Foundry, healthcare's HL7 FHIR, legal's Akoma Ntoso) ride on top of HPI as concrete worlds. HPI does NOT replace these; HPI is the cross-domain transport that lets typed claims from any of them cross substrate boundaries with semantic preservation.

2. **Promote PAT to "Reference Domain Ontology"** status. Small framing change in §3.4 conformance-status table and in the `axioms/PAT-patents.md` file header. Carries the implication that HPI ships at least one fully-committed worldview, not just meta-grammar. This addresses the simulated review's specific 90-day deliverable.

3. **Add a new section to README.md "How HPI relates to domain Ontologies"** with one-paragraph explanation positioning HPI as the protocol Palantir's Foundry Ontology (or any equivalent) could ride on, not as a competitor to such Ontologies.

**Where it doesn't land:**

If Karp's deeper objection is that meta-Ontologies are inherently academic ("AI slop with better grammar"), this is an axiom-level disagreement that revisions cannot resolve. HPI's bet is that the cross-domain transport layer is itself valuable — that Palantir's Ontology and a hospital's Ontology and a law firm's Ontology benefit from a shared substrate-boundary protocol even though they don't share content. If Karp denies this premise, the disagreement is foundational and the response is to acknowledge and move on, not to revise.

---

## Critique 2: "No threat model"

**Steelman:** The spec specifies cooperative behavior between principals, agents, and runtimes. It does not formally analyze adversarial threats: forged tokens, compromised runtimes, colluding platforms, nation-state attacks on token infrastructure. Until this analysis exists, HPI is a cooperation protocol, not a trust infrastructure.

**Where it lands:** Completely. STATUS.md acknowledges this as planned for v0.1. The simulated Karp's note that this is acknowledged-but-not-yet-shipped is fair.

**Revision committed:**

Ship `THREAT-MODEL.md` as part of the pre-publication review work (~6-10 hours per the earlier menu). Should cover:

- **Adversary classes:** rogue agent, compromised runtime, malicious principal, colluding platform, nation-state, supply-chain attack on signing keys, side-channel observation.
- **Attack vectors per class.**
- **What HPI v0 mitigates** structurally (single-use tokens, revocation lists, audit trail, key custody requirements).
- **What HPI v0 does NOT yet mitigate** and what would be required (formal verification of axiom claims, cryptographic provenance via VC, hardware-backed key custody, multi-party computation for split-trust).
- **Residual risks** that are acknowledged as out-of-scope for the protocol layer (the agent's foundation model can still hallucinate; HPI cannot prevent the principal from approving harmful scopes).

This converts Karp's objection from "missing" to "addressed at known boundary."

---

## Critique 3: "No procurement story / no moat"

**Steelman:** The spec is a protocol; anyone can implement it. There is no entity that captures rent on its evolution. Without a defensible commercial position, HPI gets adopted by hyperscalers, who absorb the protocol and route value capture to their own infrastructure. This is OAuth's fate at Auth0 scale, not OAuth's fate as Apache 2.0.

**Where it lands:** The critique is structurally correct but applies to almost every successful open protocol. SMTP didn't have a procurement story; the value capture happened at Gmail/Microsoft/Proton. TCP/IP didn't have a procurement story; Cloudflare and the CDN industry captured. Karp is correct that *someone* captures the rent. He's wrong that the absence of a single protocol-author rent-capture mechanism is fatal.

**Where it doesn't land:**

Disagreement at the level of strategy. HPI's deliberate position is to be the protocol designer + first reference implementor + ecosystem cultivator, NOT the captures-all-value company. This is the Stripe-of-payments-protocol pattern, not the OpenAI-of-AI-models pattern. The two are different bets with different risk profiles. Karp's instinct is correct that the latter pattern produces more concentrated value; the former pattern produces more durable infrastructure.

**Partial revision committed:**

Add a section to the §8 open questions specifically naming the value-capture pattern question — should HPI's reference implementor commercialize as hosted runtime, or remain pure-protocol with implementor-neutral position? This converts the absence into an explicit RFC-style discussion item, which is structurally honest.

---

## Critique 4: "Consumer framing applied to enterprise problem"

**Steelman:** The spec uses "human" as the typical substrate-holder. The actual high-stakes use cases — defense agents on classified context, hospital agents on PHI, legal agents on privileged context — require institutional sovereignty. The institution bears liability. The institution must own the L3, not the individual operator within the institution.

**Where it lands:** Real architectural observation. The spec's primitive should be `substrate-holder`, not `human`, with humans and institutions as instances. HPI's mechanics generalize cleanly to institutional substrate-holders.

**Revision committed:**

1. Update §2.1 to define `substrate-holder` as the primitive, with the introductory sentence: "*A substrate is the cognitive surface of a holder — a human, an organization, a government body, or any entity that bears the consequences of decisions made by agents operating against its substrate.*" This was already partially in the spec; making it explicit removes the consumer-framing reading.

2. Add an institutional worked example to `examples/`. Candidate: a hospital's HPI substrate where the institution is the substrate-holder, individual physicians are operators with delegated tokens, and the audit trail accrues to the institution for compliance purposes.

3. Update README and §1 to lead with the institutional framing alongside the individual one.

This converts the simulated Karp's objection from "consumer-rights protocol misapplied to enterprise" to "general-purpose protocol with both individual and institutional substrate-holders as first-class instances."

---

## Critique 5: "No formal verification of axiom claims"

**Steelman:** Cite-or-die is procedural discipline. There is no runtime mechanism that rejects an OBL claim not grounded in L0 evidence. The grammar is advisory. In Palantir's Ontology, the type system rejects ill-formed assertions at the API boundary. HPI needs the equivalent.

**Where it lands:** Mostly. STATUS.md flags JSON Schema appendices as v0.1 scope. The simulated Karp suggests the validator should ship in the reference implementation. This is correct.

**Revision committed:**

1. JSON Schema appendices for OBL/RCG/TRU/PAT in v0.1 (already planned).

2. Reference implementation v0.1 includes a validator that rejects axiom assertions whose `cites` field does not resolve to existing L0 entities.

3. Add a single sentence to §3 noting that v0 specifies the grammar at the prose level; v0.1 will provide the JSON Schemas + runtime validator that make the grammar enforceable rather than advisory.

---

## Endorsement: "Agents must NEVER own their L3" (highest predicted endorsement)

**No response required** — this is the spec's central axiom and the simulated review affirms it. Note for future positioning: when speaking publicly about HPI, lead with this axiom + the Letta inversion, since this is the framing that earns conditional respect from even hostile reviewers like the simulated Karp before structural objections land.

---

## Summary of revisions committed (after this simulated review)

If all three of the highest-priority critiques are addressed, the simulated Karp review converts from "conditional revise" to "publish — with our Ontology riding on top." Specific commits:

| # | Revision | Where | Effort | Resolves |
|---|---|---|---|---|
| 1 | Add §3.7 framing HPI as cross-Ontology transport, not Ontology replacement | SPEC.md | 30 min | Critique 1 |
| 2 | Promote PAT to "Reference Domain Ontology" | §3.4 + axioms/PAT header | 15 min | Critique 1 |
| 3 | README.md "How HPI relates to domain Ontologies" paragraph | README.md | 15 min | Critique 1 |
| 4 | Ship THREAT-MODEL.md | new file | 6-10 hrs | Critique 2 |
| 5 | Add value-capture pattern question to §8 | SPEC.md | 20 min | Critique 3 (partial) |
| 6 | Substrate-holder primitive in §2.1 + institutional example | SPEC.md + examples/ | 2-3 hrs | Critique 4 |
| 7 | Note v0.1 validator commitment in §3 | SPEC.md | 10 min | Critique 5 (deferred to v0.1) |

**Total effort: ~10-15 hours** of focused revision work. About one weekend.

The single highest-leverage revision is #4 (THREAT-MODEL.md). It is the largest, addresses the sharpest objection, and was already on the pre-publication checklist.

The framing revisions (#1-3, #6) collectively reframe HPI as institutional-and-individual + meta-Ontology-by-design, removing two distinct misreadings before they happen.

After these revisions, when (if) Karp actually engages with the spec, the simulated review's predicted critiques are pre-empted. The remaining axiom-level disagreement (whether meta-Ontologies are inherently academic) is a real philosophical disagreement that revisions cannot bridge, and HPI's response is to name it openly and stand on the architectural bet.

---

## Calibration: what this simulation produced

- **3 spec revisions** I will commit to before publication
- **1 new file** to draft (`THREAT-MODEL.md`)
- **1 new framing claim** (HPI as cross-Ontology transport) that strengthens the spec's positioning
- **0 axiom-level changes** required
- **1 acknowledged disagreement** that survives at the philosophical level

By the methodology's success criteria, this simulation is **useful**: produces ≥1 spec revision (it produces 7) and ≥1 fortified counter-argument (the cross-Ontology transport positioning) and ≥1 named axiom-level disagreement.

This is what the simulation pipeline is for.
