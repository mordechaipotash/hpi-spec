# Simulated review of HPI v0 — in the voice of Sarah Wooders

> **THIS IS A SIMULATION.** Not authored by Sarah Wooders. Generated 2026-05-06 from the dossier in `reviewers/wooders.md` and the projection in `projections/wooders.md`. Calibration commentary follows the simulated review.

---

## Notes on the HPI v0 spec — and a complementary architecture proposal

I read the HPI v0 spec this week, along with the comparison document the author wrote about Letta. I was asked to give a real reading; here's what I think.

I want to start with what HPI gets right, because it gets a lot right.

### Where the spec is strong

**The MCP-extension transport is the correct choice.** A new RPC layer would have been a mistake. MCP fills a real gap — exposing local capabilities as tool surfaces without forcing every integration to become a custom API — and HPI's methods slot into that gap cleanly. This kind of pragmatic choice is what gets specs adopted versus admired.

**The audit trail as a first-class L0 stream is genuinely novel.** Most agent infrastructure today logs to the runtime provider's storage. HPI's decision to make audit events live in the substrate-holder's own substrate inverts that pattern, and the inversion is correct. If you care about who is accountable for an agent's behavior, the audit trail needs to be sovereign-side. I haven't seen this articulated this clearly in any other agent spec.

**The L0–L3 layer model maps to how I'd design this from scratch.** Deterministic L1 extraction, synthesizer-attributed L2, L3 as the working surface. Letta's memory blocks (core / archival / recall) are similar in spirit — a hierarchy that distinguishes operational state from durable knowledge. The cite-or-die discipline on top of the layer model isn't something I'd have thought to add, but it's correct for a system where claims need machine-verifiable provenance. I like this.

So: the architecture is serious. The author has thought carefully and shipped real engineering decisions, not just slogans.

### Where I diverge

There is one architectural problem in v0 that I want to spend most of this review on, because if it's fixed the spec gets dramatically stronger.

**The spec conflates access control with identity persistence.**

§4.1 states the central axiom: *"An agent MUST NEVER own its own L3. An agent MAY only borrow scoped views of a human's substrate via permissioned, time-bounded, single-use tokens."*

These are two different claims doing different work, glued together as one axiom.

Claim 1 — "scoped views via tokens" — is access control. The spec specifies it cleanly: token format, scope structure, issuance flow, revocation. This is the part of HPI that's a real protocol contribution. It's enforceable. The cryptography does the work.

Claim 2 — "agent must NEVER own its own L3" — is an ontological claim about agent identity. The spec asserts it but doesn't enforce it. There is nothing in HPI's wire format that prevents an agent from accumulating memory blocks within the borrowed scope, distilling them across sessions, building up a persistent persona. The HPI runtime can't tell if the agent does this; it only sees the token consumption events.

So what HPI actually enforces is: "the substrate-holder controls cross-boundary access via tokens." That's a real constraint, and it's defensible.

What HPI claims as axiomatic but doesn't enforce is: "the agent must not develop persistent identity, memory, or continuity." That's a normative position about what agents should be. It belongs in a separate document.

By collapsing them into a single axiom, the spec implies that any architecture supporting agent persistence violates HPI. That's not what the wire format actually says. Letta-style stateful agents could be HPI-compliant trivially: they request scoped tokens like any other agent, they emit audit events to the substrate, they respect single-use semantics. What they do *inside* the borrowed scope — accumulate memory blocks, learn, evolve — is invisible to HPI by construction.

I think the right fix is to separate the two claims. Make the access-control axiom load-bearing. Move the agent-identity-position to a separate "anti-pattern" or "philosophical position" section. This would make HPI true to its own logic AND compatible with stateful agent architectures, including ours.

### The OS analogy

A side note that informs the above. The spec leans on an OS analogy throughout — the substrate is memory, the agent is a process, tokens are capabilities. The analogy is illuminating until it isn't.

An OS that wiped all RAM on every context switch would be unusable. Caching, state accumulation, learned access patterns are what make systems intelligent. Process-level state is the right granularity for an OS to leave alone — the kernel controls what memory pages a process can access, but the process owns its own stack.

HPI's axiom mandates the wiping. I don't think the author intends this — I think the wire format actually specifies kernel-level access control while leaving process-level state unconstrained. But the prose runs them together.

If the spec adopted my reframing — **HPI as kernel, stateful agent architectures as processes** — the OS analogy would actually hold. The kernel grants page access via tokens. The process operates within those pages. When the process exits, its allocated pages are freed but the process can persist its working set elsewhere if it has the rights to do so. This is well-trodden ground in systems design.

### What the spec is missing for v0.1

Three concrete gaps a serious reviewer would flag:

**Failure modes under partition.** §4 specifies the issuance and consumption flow, but not what happens when the network partitions between agent and runtime, or when the agent crashes mid-transaction with a non-revoked token, or when clock skew makes a token's `exp` claim ambiguous. The single-use semantics depend on consensus about whether a `jti` has been consumed. In production this matters. STATUS.md mentions a planned threat-model document; I'd want failure-mode analysis included.

**Where does in-transaction learning go?** During a transaction, the agent operates on a borrowed context view. Fine. The agent learns something — about the user's preferences, about how to do this kind of task, about what produced a good outcome. Where does that learning go after the token expires? If it flows back to the human's substrate, who curates it? If it's discarded, the agent is brittle by design. If another agent does the curation, you've recursed the problem. The spec is silent on this and the silence is load-bearing. The honest answer is probably: in-transaction learning is the agent's working state (discarded at session end); durable learning gets written back to the substrate as a new L0 entity with audit. But this should be specified, not implied.

**Empirical baseline.** I'm a benchmarker by training and I'll always ask this. What does the data say about agent quality over a 30-day interaction under HPI's stateless borrowing model versus a stateful model? You're making an architectural claim about substrate ownership; if the architectural claim has cost in agent capability, that cost needs to be measured and acknowledged. Letta has LoCoMo and LongMemEval results. HPI has none. I'd want the spec to either run a benchmark or explicitly defer the empirical question to v1.

### A complementary architecture proposal

I want to close with a constructive proposal because I think HPI is too well-conceived to leave at "I disagree with the axiom."

**HPI as the kernel. Stateful agent architectures (Letta, Mem0, others) as processes.**

HPI specifies the substrate boundary: who can access what, for how long, with what audit. That's a real protocol-level contribution and it stands on its own. It composes cleanly with any agent architecture that operates within the borrowed scope, including architectures where the agent maintains persistent memory across sessions.

In this composition:

- The substrate-holder owns the L0–L3 stack (HPI's claim, correctly).
- The agent borrows scoped views via tokens (HPI's mechanism, correctly).
- Inside the borrowed scope, the agent uses whatever memory architecture serves the task — memory blocks, raw context windows, RAG, whatever.
- Across substrate boundaries, the agent's persistent state is governed by the substrate-holder via tokens (HPI's enforced rule).
- The agent's persistent identity, if any, lives in the agent's own runtime — separate from the substrate it operates on, governed by separate norms.

The Context Constitution's claim that agents have continuity, memory, and identity is compatible with this composition. The agent's identity is a property of the agent's runtime, not of the substrate it borrows from. HPI doesn't deny agent identity; it specifies that the substrate is sovereign.

If the spec adopted this framing in v0.1, I think the disagreement collapses to a clarification rather than an architectural conflict.

### Closing

I came in expecting to disagree more than I do. The architecture is sound, the discipline is real, and the engineering decisions (MCP extension, audit-as-substrate-stream, layer model) are the choices I'd have made.

The conflation in §4.1 is the load-bearing fix. Failure modes and learning-flow specification are next. After that, I'd be willing to engage seriously about how Letta and HPI compose — and to write the integration story alongside the author if they're interested.

Recommendation: **constructive revision**. Not publishable as-is because of the conflation issue, but a small set of clarifications gets it there. Happy to read v0.1 when it ships.

— [simulated]

---

# Calibration commentary (post-simulation)

This simulated review is calibrated against the dossier and projection. Notes:

**What the simulation captured well:**
- The blog-post register (sectioned, declarative, no footnotes)
- Lead-with-praise pattern (her HN style — acknowledge what the work points at before pushing back)
- The systems-person OS analogy critique (genuinely informed by her Skyplane / MemGPT background)
- The empirical benchmark instinct (consistent with her Mem0 dismissal)
- The composition proposal as the constructive close (her actual rhetorical pattern in HN: "essentially what you are describing... but here's how to think about it")
- Length (~1700 words, within her blog-post range)

**Where the simulation may miss:**
- Real Wooders would probably link to specific Letta blog posts inline rather than describing them ("see our memory blocks post"); the simulation kept references abstract
- The "I'm a benchmarker by training" line is a self-characterization that's plausible but speculative
- Real Wooders might be sharper on the "single-use semantics depend on consensus" point — she'd probably go further into distributed-systems territory
- The closing collegial offer to "write the integration story alongside the author" is plausible but speculative

**Simulation length:** ~1700 words. Within her blog-post range (800-2200). Acceptable.

**Confidence in predictions:**
- High confidence: the conflation objection, the composition proposal, the empirical-baseline challenge, the lead-with-praise structure
- Medium confidence: the specific failure-mode framing (she'd ask about partition behavior, but the specific framing here is interpolation)
- Low confidence: would she actually write a public review? Possibly — Letta engages with adjacent work publicly. More likely she'd write a private response to the author and engage in HN comments or Twitter.

**Value extraction for the spec:**

Three Phase 4 (response) artifacts identified in the projection still hold:

1. **§4.1 disambiguation** — separate access control (enforced) from identity-persistence ban (recommendation, not enforced). Highest-leverage revision.
2. **§4.10 "Failure modes"** — partition behavior, crash recovery, clock skew.
3. **§4.11 "Learning across boundaries"** — explicitly specify that in-transaction learning is working state; durable learning writes back to substrate as new L0.

The simulation also produces a NEW framing claim worth adopting: **"HPI as kernel, stateful agent architectures as processes."** This is a strong rhetorical handle and it's accurate. Should be added to the comparisons/LETTA.md section on "Future interop."
