# Projection — Sarah Wooders on HPI

**Compiled:** 2026-05-06 from `reviewers/wooders.md` + SPEC.md v0 + comparisons/LETTA.md.
**Method:** Project Wooders' most likely reactions section-by-section, then synthesize stance + ranked objections + ranked endorsements + composition proposal.

---

## Overall stance: GENUINELY ENGAGED, AXIOM-LEVEL DISAGREEMENT, CONSTRUCTIVE COMPOSITION PROPOSAL

Confidence: high.

Wooders will engage HPI as a fellow systems-researcher's serious work. She will not dismiss it as "yet another sovereignty pitch." She will recognize the layered model, the citation discipline, and the MCP-extension transport as architecturally sound choices a Berkeley Sky Lab person would make.

She will not surrender Letta's central axiom. The Context Constitution is too load-bearing for her company's positioning to concede that "agents must NEVER own their L3." She will reframe rather than concede.

But the closing move will likely be **constructive, not adversarial.** She is wired to see system composition: HPI as the kernel-level access control protocol, Letta-style stateful agents as the processes that operate within the borrowed scope. She will offer this composition as the synthesis. HPI's response should accept the composition (it's actually consistent with the spec) — the architecturally honest position is that HPI doesn't constrain what an agent does WITHIN a transaction, only what it can carry across boundaries.

Her review would be ~1500-2200 words. Blog-post register, not academic-formal. Sectioned. Empirically grounded. Technically confident.

---

## Sections she'll engage with most

Ranked by predicted depth:

1. **§4 Token Handoff Protocol** — most engagement. Systems-person's home territory. She'll scrutinize the issuance flow, single-use semantics, revocation enforcement. The token mechanics are her field of natural attention.
2. **§2 Substrate Model** — second-most. The L0–L3 layering will catch her interest. She'll compare to Letta's memory-block hierarchy (core / archival / recall) and probably observe the structural similarity.
3. **§7 Non-Goals & Anti-Patterns** — third-most. She'll engage with §7.2 ("Not a memory product") because it directly names Letta. The hosted-runtime-with-vendor-keys anti-pattern she'll respect.
4. **comparisons/LETTA.md** — equal engagement. This document was written about her work; she will read it carefully and respond to its specific characterizations.
5. **§3 Typed Axiom Grammar** — moderate engagement. She doesn't have a strong position on typed grammar (Letta uses memory-block formats, not typed claim languages). Probably finds it interesting but not center-of-gravity.
6. **§1 Foundations** — moderate. She has not engaged publicly with hyperscaler-trajectory framing; will read for context but not push back hard.
7. **§5, §6, §8, §9** — light engagement. §9 acknowledgement of Letta she'll appreciate.

---

## Specific objections, ranked by predicted probability + sharpness

### Objection 1 — "You've conflated access control with identity persistence" (P=0.95, sharpness=high)

**The line:** *"HPI specifies a perfectly reasonable boundary protocol — scoped tokens for substrate access. That's access control, and access control is genuinely useful. But you've then jumped from 'the agent must request scoped access' to 'the agent must never own its own L3.' Those are different claims. The first is about the substrate boundary; the second is about agent identity persistence within the borrowed scope. By collapsing them, you've made a token-handoff protocol into an ontological denial of agent identity. The spec would be stronger — and more adoptable — if you separated the two."*

**Why this is sharp:** She's right that the spec runs the two together. §4.1 starts with "agent must NEVER own its own L3" as a single axiom, but operationally the spec only enforces the access-control half (scoped tokens, single-use, revocation). The identity-persistence half is asserted but not enforced — there's nothing in HPI's wire format that prevents a Letta agent from accumulating memory blocks within the borrowed scope.

**Where it lands:** Lands HARD. This is genuinely a conflation in v0. The right fix: §4.1 should distinguish between (a) access control (HPI enforces this), (b) identity-persistence ban (HPI's *recommendation*, not enforced — and the recommendation is conditional on the use case).

### Objection 2 — "Stateless borrowers can't compound" (P=0.90, sharpness=high)

**The line:** *"The OS analogy that runs through HPI's framing is illuminating until it isn't. An OS that wiped all RAM on every context switch would be unusable. Caching, state accumulation, learned access patterns — these are what make systems intelligent. Letta's whole thesis is that compounding agent capability requires persistent state across sessions. HPI's axiom mandates the wiping. What does the empirical data say about agent quality over 30 days under HPI's stateless model vs Letta's stateful model? You can't make this architectural claim without the comparison."*

**Why this is sharp:** This is the empirical challenge from a benchmarker. She publicly flagged Mem0 for unrigorous benchmarking; she'll apply the same standard to HPI. The spec's claims about the agent-borrowing model are architectural, not empirical. HPI has no LoCoMo equivalent.

**Where it lands:** Mostly. The spec doesn't claim the borrowing model produces better agent outputs — it claims the borrowing model preserves human sovereignty over the cognitive substrate. These are different optimization targets. But Wooders' implicit point lands: HPI's axiom is asserted on philosophical grounds without empirical support that the architecture produces good agent behavior.

### Objection 3 — "Where does learning go?" (P=0.85, sharpness=medium-high)

**The line:** *"During a transaction, the agent operates on a borrowed context view. Fine. The agent learns something during that transaction — about the user's preferences, about how to do this kind of task, about what produced a good outcome. Where does that learning go after the token expires? If it flows back to the human's substrate, who curates it? If it's discarded, the agent is brittle. If another agent does the curation on the human's behalf, you've recursed the problem. The spec is silent on this and the silence is load-bearing."*

**Why this is sharp:** Real architectural gap. HPI specifies what happens AT the boundary (tokens, audit) but doesn't specify what happens to learned content INSIDE a transaction after the boundary is recrossed.

**Where it lands:** Lands. The honest answer: HPI v0 specifies the boundary; what the agent learns within the borrowed scope is the agent's working state, discarded at session end. If durable learning is needed, it must be written back to the human's substrate as a new L0 entity (with explicit audit). This pattern needs to be in the spec, probably in §4.

### Objection 4 — "Revocation enforcement under failure modes" (P=0.75, sharpness=medium)

**The line:** *"Systems person question. What happens if the agent's session crashes mid-transaction with a non-revoked token? What happens if the runtime that issued the token goes down before the agent consumes it? What happens under network partition between issuer and consumer? The single-use semantics depend on consensus about whether a jti has been consumed. The spec specifies the cryptography but not the failure-mode behavior. In production this matters enormously."*

**Why this is sharp:** Real gap. v0 spec has issuance + consumption flow but no failure-mode analysis. THREAT-MODEL.md (planned) should cover this.

**Where it lands:** Yes. Add to THREAT-MODEL.md scope. Maybe also add a §4.10 "Failure modes" subsection.

### Objection 5 — "The 'memory product' anti-positioning is too strong" (P=0.55, sharpness=low-medium)

**The line:** *"§7.2 says HPI is 'not a memory product' and names Letta. I appreciate the disambiguation, but the framing slightly misses. Letta is also not 'just a memory product' — Letta is an architecture for stateful agents that happens to use memory blocks as the implementation. HPI and Letta operate at different layers, but neither is the wrong layer. Consider rewording to indicate Letta and HPI are complementary architectures rather than positioning Letta as the layer below HPI."*

**Where it lands:** Soft objection but a fair clarification. Easy revision in §7.2.

---

## Specific endorsements, ranked by predicted probability

### Endorsement 1 — "MCP as transport is the right choice" (P=0.90)

**The line:** *"Extending MCP rather than defining a new RPC layer is correct. MCP fills a real gap (exposing local capabilities as tool surfaces) and HPI's methods slot into it cleanly. This is the kind of choice that gets the spec adopted faster."*

### Endorsement 2 — "The audit trail as L0 stream is novel and right" (P=0.85)

**The line:** *"The decision to make audit events first-class L0 entities in the substrate-holder's substrate is genuinely interesting. It inverts the standard pattern (audit logs live in the runtime provider's storage). Forces auditability to be sovereign-side. I like this."*

### Endorsement 3 — "Layer model is architecturally sound" (P=0.80)

**The line:** *"L0-L3 with deterministic L1 extraction and synthesizer-attributed L2 maps to how I'd design this from scratch. Memory blocks in Letta are similar in spirit (core/archival/recall as a hierarchy). The cite-or-die discipline I'd not have thought to add — but it's correct for systems where claims need provenance."*

### Endorsement 4 — "Acknowledgment of Letta in §9 is appreciated" (P=0.95)

Mostly social — she'll note the credit and reciprocate by engaging substantively rather than dismissively.

---

## What she'll PROPOSE (the constructive payoff)

**The composition proposal:**

> *"HPI as the kernel, Letta as the process.*
>
> *HPI specifies the access control surface — what context an agent can see, for how long, with what audit. That's a real protocol-level contribution. Inside the borrowed scope, the agent should be free to use whatever memory architecture serves the task — Letta's memory blocks, raw context windows, RAG systems, anything. HPI doesn't need to take a position on the agent's working memory architecture; it only needs to specify the boundary.*
>
> *If the spec adopted this framing, it would be true to its own logic AND compatible with stateful agent architectures. The 'agent never owns L3' axiom should be restated as 'the agent's persistent state across substrate boundaries is governed by the human, via tokens.' Within a transaction, the agent owns its working memory. Across transactions, the human owns the substrate. These are different scopes."*

This is the move that converts the simulated review from "interesting disagreement" to "actionable composition." HPI's response should accept this framing because the spec actually doesn't enforce identity persistence — it enforces access control.

---

## Predicted register and structure of her actual review

If Wooders wrote this review (she might — Letta engages publicly with adjacent work):

**Title-style:** Direct. "Notes on the HPI v0 spec" or "HPI and Letta: a complementary architecture proposal" or "Reviewing the agent-borrows-context proposal."

**Length:** 1500-2200 words. Blog post, not academic paper.

**Structure:**
1. Brief praise of what HPI gets right (architecturally sound, MCP transport, audit innovation)
2. Where she diverges (the conflation; the OS analogy breaking; the empirical question)
3. The compositional alternative (HPI as kernel, Letta as process)
4. What she'd want to see in v0.1 (failure modes, learning-flow specification, empirical comparison)
5. Closing: collegial engagement, next steps

**Voice patterns:** "I think...", "But not all loops are created equal." (her actual phrase), short declaratives, technical precision, occasional sharp question ("What does the data say?"). No theological epigraphs. No Hegelian dialectic. No 90-day deliverable framing — that's Karp.

**Triggers:** Architectural sloppiness; unsupported architectural claims; conflation of distinct concerns. NOT triggered by sovereignty framing per se; she's neutral on the political dimension.

---

## Predicted closing recommendation

**Constructive engagement with proposed composition.** Not "publish unchanged" — she'd want the conflation fixed. Not "reject" — the spec is too aligned with Letta's diagnosis. Most likely close: *"This is a serious contribution to the agent-substrate question. I disagree with the central axiom as stated but I think there's a clean composition where HPI specifies the boundary and stateful-agent architectures (including Letta) operate within. I'd encourage the author to make this composition explicit in v0.1. Happy to work on the integration story together."*

If that landing happens: HPI gains a credible peer endorsement from the most informed possible reviewer. The cost of getting there is one architectural clarification (the conflation) and acknowledgment that HPI doesn't enforce the agent-identity-persistence ban inside transactions — only outside them.

---

## What this projection produces for Phase 4 (response)

Three response artifacts to prepare in advance:

1. **Disambiguation of access control vs identity persistence** — the central revision, addressing Objection 1. Make §4.1 distinguish "what HPI enforces (access control via tokens)" from "what HPI recommends (no agent state across boundaries)" from "what the agent does inside a transaction (out of scope for the protocol)." This is honest and accepts Wooders' composition framing.

2. **Add §4.10 "Failure modes"** — addressing Objection 4. Specify behavior under: agent crash mid-transaction, runtime crash before consumption, network partition, clock skew. Cross-reference THREAT-MODEL.md.

3. **Add §4.11 "Learning across boundaries"** — addressing Objection 3. Specify that learning during a transaction is the agent's working state (discarded at session end); durable learning must be written to the human's substrate as a new L0 entity with audit; this is the only path for cross-boundary persistence.

If those three land, the simulated Wooders review converts from "constructive disagreement" to "compositional endorsement." HPI gains the architecturally serious peer voice from the agent-context-product space.
