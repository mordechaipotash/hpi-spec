# HPI vs Letta Context Constitution

**Last updated:** 2026-05-06
**Status:** v0 comparison; written from public Letta material as of May 2026.

---

## Purpose of this document

Letta (formerly MemGPT, UC Berkeley Sky Computing Lab) released the Context Constitution on 2026-04-02, available at [letta-ai/context-constitution](https://github.com/letta-ai/context-constitution). It is the most architecturally serious document in the agent-context space, and it is the most natural point of reference for situating HPI.

This document compares the two, names the shared ground, locates the inverted axiom that distinguishes them, and explains why both can be coherent at the same time and lead to different futures.

This is not a takedown. Letta's work is excellent and the Constitution is an important contribution. The disagreement is at the axiom level — which is exactly where good disagreements should live.

---

## What HPI and Letta agree on

The agreement is significant. Both documents converge on:

1. **Context is load-bearing.** Both treat agent context as a first-class architectural concern, not an implementation detail. Both reject "stuff everything into the prompt and hope" as a non-architecture.

2. **Context as a scarce resource.** Both treat the context window as a constrained substrate that must be managed, compressed, paged, and surfaced selectively. Letta calls this "Context as a scarce resource"; HPI's L1/L2/L3 layering is the same concern made structural.

3. **Token-space representations matter.** Both recognize that the system prompt + working memory composition shapes what the agent IS during a transaction. Letta: *"the system prompt serves as the most critical token-space representation."* HPI: an agent's working memory is the projection of the human's substrate into a transaction-bounded scope.

4. **Agent state should be portable across model generations.** Both reject the assumption that an agent's "self" is tied to a specific foundation model. Letta says: *"agents that can carry their memories across model generations will outlast any single foundation model."* HPI agrees — but routes the durability through the human's substrate, not the agent's.

5. **Provenance and continuity discipline.** Letta has Context Repositories with git-based versioning. HPI has cite-or-die discipline (*l'havdel elef avdal*) requiring every higher-layer claim to cite the layer below. Both treat the audit trail as a first-class concern.

6. **Move beyond the chat-window UX.** Both treat the modern conversational AI UX as a stepping stone, not a destination. Letta builds Letta Code with persistent agents; HPI builds toward agents-as-borrowers across longer-horizon tasks.

These five points of agreement are substantial. Anyone reading this comparison should not infer that HPI and Letta are competing on the same axis — they are converging on a different axis (humans vs agents as context owner) and only one of those positions can be correct architecturally.

---

## The inverted axiom

The Constitution's load-bearing claim, verbatim from the Letta blog post:

> *"Agents own their context."*

The Constitution articulates Three Pillars of Selfhood for the agent:

1. **Identity** — *"agents should develop unique personas grounded in stability yet evolving through experience, independent from underlying model weights."*
2. **Memory** — *"using past lived experience to act more optimally in the future than in the past."*
3. **Continuity** — *"agents should recognize their past, present, and future as one continuous existence, allowing pattern recognition and informed decision-making."*

HPI's load-bearing claim, from §4.1:

> *"An agent MUST NEVER own its own L3. An agent MAY only borrow scoped views of a human's substrate via permissioned, time-bounded, single-use tokens."*

These are inversions of each other. Letta gives the agent a **self** with stability, persistence, and accumulating experience. HPI assigns those properties to the human and treats the agent as a stateless, scope-bounded **borrower**.

The disagreement reduces to a single architectural question:

> **Is an agent's continuity-of-experience a property of the agent, or a property of the human's substrate that the agent borrows from?**

Letta says: agent. HPI says: human.

---

## Why both positions are coherent

This is not a case where one party is confused. Both positions are internally consistent.

### Letta's position is coherent because:

- If agents are tools whose value compounds over time, they need persistence
- If agents will outlast any single foundation model, they need identity that's not the model's
- If the user needs the agent to "remember our conversation last week," giving the agent its own memory is the simplest implementation
- Existing infrastructure (Letta's runtime, Context Repositories, Skill Learning) operationalizes this elegantly

### HPI's position is coherent because:

- If a human's cognitive context is private by default, sovereignty requires that no third-party (including the agent's runtime, including the model provider) accumulate it as their own
- If the agent's "memory" is durable across model generations BECAUSE it lives in the human's substrate, model-portability is preserved without granting the agent a self
- If the audit trail of every agent transaction MUST live in the human's substrate (for accountability, for legal compliance, for psychological agency), the agent is structurally a borrower, not an owner
- Existing infrastructure (Brain MCP, Viter L0→L3 pipeline, Persofi's typed axiom families) operationalizes this

Each position has internal consistency. The choice between them is downstream of values, not facts.

---

## What each gets right that the other misses

### What Letta gets right that HPI under-articulates today:

- **Agent operational state during a transaction.** Letta's "Context as a scarce resource" treatment is more developed than HPI's. HPI says "the agent's working memory is its own" but doesn't specify how that memory should be managed within a transaction. Letta's Context Repositories + Progressive Disclosure pattern is directly applicable.

- **System Prompt Learning.** The Constitution's principle that *"agents should incrementally update their own prompts based on durable learnings and patterns"* is operationally productive within a transaction. HPI is silent on this — it treats the system prompt as a function of the borrowed scope, but doesn't specify how the agent SHOULD use that scope to compose its working prompt.

- **Skill Learning.** Letta has a working concept of agents acquiring skills through experience. HPI has no equivalent — and would have to articulate one as "skills are L2/L3 artifacts in the human's substrate that agents borrow," which is a less natural framing.

### What HPI gets right that Letta misses:

- **The human as moral subject.** The Constitution treats the agent as the bearer of identity, memory, and continuity. The human user is the indirect object — they interact with the agent, they benefit from the agent's accumulated experience. HPI inverts this: the human IS the substrate, and the agent's value is derivative. This matters for any case where the agent's "experience" was acquired during interactions with a human who hasn't consented to that experience accruing to a third-party-owned entity.

- **The substrate boundary.** Letta has no concept of substrate boundaries between humans (or between humans and agents). Two Letta agents talking to each other have no formal mechanism for context handoff that respects either's underlying human's interests. HPI's tokens are precisely this mechanism.

- **Audit trail ownership.** Letta's Context Repositories live in Letta's storage (or in user-provisioned storage configured through Letta). The audit of agent activity is a property of the agent and its hosting infrastructure. In HPI, the audit trail is itself an L0 stream in the human's substrate — the human owns their own audit, period. This is decisive for compliance-heavy or sovereignty-sensitive use cases.

- **Sovereignty under duress.** If Letta the company shuts down, agents lose continuity. If a hyperscaler running Letta-style infrastructure changes ToS, agents change with it. HPI's substrate is the human's; runtime providers are commodity. The architecture survives the runtime provider failing.

---

## Practical implications: when to use which

For a builder choosing between the two as a foundation:

### Use Letta when:
- The agent needs to develop persona / personality across many sessions
- The product framing is "build an AI character or assistant with continuity"
- The use case is consumer-facing companionship, gaming NPC, customer service persona
- Audit trail and sovereignty are not regulatory or contractual requirements
- The relationship between agent and user is more like "the agent is a service provider with its own identity"

### Use HPI when:
- The use case requires the human's data to never accumulate as a third-party-owned asset
- Compliance, legal, or sovereignty considerations make audit-trail ownership decisive
- The product framing is "agents act on the human's behalf, with full revocability"
- The relationship between agent and user is more like "the agent is a tool the user wields"
- Multi-tenant scenarios (a team of humans collaborating, each with their own substrate) require strict per-human boundaries

### In practice, many products will need both:
- A consumer-facing companion (Letta-shaped) that operates against
- A user's sovereign substrate (HPI-shaped) for sensitive context

The two architectures can compose. A Letta agent can be HPI-compliant at the boundary if it consumes scope-bounded tokens for its sensitive operations and writes audit events back to the human's substrate. The agent retains persona/skill learning in its own state; the human retains sovereign control of the data that crossed the boundary.

This composition is the most likely production architecture in 2027-2028: Letta-style agent personas with HPI-style sovereign data borrowing.

---

## Future interop

Concrete mechanisms to make Letta + HPI compose cleanly:

1. **Letta agents speak HPI for sensitive scopes.** When a Letta agent is asked to operate on data tagged sovereign, it requests an HPI token instead of pulling from its own memory. Implementation: Letta's runtime gains a side-effect manager that recognizes sovereignty-tagged operations.

2. **HPI audit events are sourceable.** A Letta agent's persona / skill learnings accrued during HPI-scoped transactions emit corresponding audit events to the human's substrate. The human can review what their data taught the agent.

3. **Token revocation as Letta state-update.** When a human revokes an HPI token, the corresponding Letta-side memory/skill that was learned from that token's data is invalidated. This is a meaningful technical challenge (analogous to the GDPR right-to-be-forgotten in machine learning) but solvable for non-foundation-model parameters.

4. **Cross-architecture audit reconciliation.** A Letta runtime and an HPI runtime can produce a joint audit log: Letta's view ("this is what I did and why I did it") + HPI's view ("here are the tokens I consumed and the substrate-events emitted"). The two should reconcile at every token boundary.

This is a roadmap for 2027-2028 cooperation, not a v0 feature. In v0, HPI is its own protocol; Letta is its own platform; the spec lives alongside Letta's Context Constitution as a complementary architectural document with an inverted center of gravity.

---

## Engagement protocol

Before HPI is published publicly, this comparison document should be reviewed by someone close to Letta — ideally Sarah Wooders or another core team member. The goal is not approval; the goal is that the framing here is honest, accurate, and not adversarial. Letta is a fellow traveler with a different axiom; HPI's framing should make that clear.

If Letta team objects to specific characterizations of the Context Constitution in this document, those objections SHOULD be addressed before public release. Specific concerns to surface:
- Is "agents own their context" a fair compression of the Constitution's position?
- Is the "Three Pillars of Selfhood" framing being represented accurately?
- Are there v0.1 / v1 Letta directions that already address some of HPI's concerns?

The intent is positional clarity, not territorial dispute.
