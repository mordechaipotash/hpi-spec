# HPI — Hyperpersonalized API

> **A protocol for sovereign cognitive substrate. Each human owns their own AI context. Agents borrow scoped, time-bounded views via permissioned one-time tokens. The substrate never leaves the human.**

**Status:** v0 draft. **NOT FOR PUBLIC RELEASE** until reviewed (see `STATUS.md`).
**Author:** Mordechai Potash (`mordechaipotash@gmail.com`)
**License:** Apache 2.0 (planned for spec); MIT (planned for reference impls)
**Started:** 2026-05-06

---

## What this is

HPI specifies how **AI agents request, receive, and use a substrate-holder's cognitive context** under permissioned access control.

The default trajectory of 2026 is: hyperscalers (OpenAI, Google, Anthropic) accumulate user context on their servers, build the L3 cognitive surface there, and lock users in by switching costs. That trajectory is structurally misaligned with substrate-holder agency.

**The load-bearing claim, precisely stated:** HPI specifies an access-control protocol — agents access a substrate's L1+ content only via permissioned, time-bounded, single-use tokens issued by the substrate-holder, with full audit trail accruing to the substrate-holder's substrate. This is what the wire format enforces.

HPI does NOT specify what agents do inside the borrowed scope. Stateful-agent architectures (Letta-style memory blocks, Mem0-style memory) compose with HPI cleanly: they request scoped tokens, emit audit events, respect single-use semantics. The protocol is the kernel; stateful agent architectures are the processes.

Analogy: HPI is to AI context what self-custody wallets are to crypto, what Solid pods are to social data, what SMTP is to email — a protocol that refuses to capture by design, with rent captured around it.

## How HPI relates to domain Ontologies

HPI is **the cross-Ontology transport layer**. It is not an Ontology itself. Domain Ontologies — Palantir's Foundry Ontology, healthcare's HL7 FHIR, legal's Akoma Ntoso, financial-vertical Ontologies — ride on HPI as the wire format that lets typed claims cross substrate boundaries with semantic preservation. HPI does not compete with these Ontologies; it specifies how their typed claims travel between substrates without losing meaning.

A Foundry-typed `Aircraft` claim in Substrate A lands in Substrate B as a Foundry-typed `Aircraft` claim, not as raw bytes that B has to re-derive types from. HPI is what makes that work. PAT (the patent-prosecution Reference Domain Ontology shipped with v0) demonstrates what a domain Ontology riding on HPI looks like.

## What HPI is not

- Not a model. LLMs remain LLMs.
- Not a memory product. Mem0/Letta/Khoj solve memory; HPI solves substrate-boundary handoff.
- Not a wallet. No native token, no cryptocurrency.
- Not blockchain-required. Implementations may use Web3 primitives (Ceramic, IPFS) or pure HTTP+JWT.
- Not anti-LLM. LLMs are useful; HPI just refuses to let them OWN your substrate.
- Not anti-platform. Platforms can be HPI-compliant. The protocol is the constraint.

## Repository layout

```
hpi-spec/
  README.md                  ← you are here
  SPEC.md                    ← the protocol document
  STATUS.md                  ← what's drafted, what's stubbed, what needs review
  LICENSE                    ← Apache 2.0
  axioms/
    README.md                ← philosophy: ontology vs schema, why axioms
    OBL-obligations.md       ← v0 axiom family: obligations
    RCG-recharges.md         ← v0 axiom family: recharges
    TRU-trust.md             ← v0 axiom family: trust
    PAT-patents.md           ← v0.1 axiom family: patent lifecycle
  examples/
    01-obligation-end-to-end.md  ← worked example: one obligation L0→L1→L2
  schemas/                   ← JSON Schemas (placeholder for v0.1)
```

## Conceptual lineage

HPI builds explicitly on:

- **Solid (Tim Berners-Lee, W3C)** — personal data ownership precedent.
- **Anthropic MCP (Model Context Protocol)** — the transport HPI extends.
- **Plurality / Open Context Layer (OCL)** — context vault interop, identified as ally not competitor.
- **Letta / MemGPT (UC Berkeley Sky Computing Lab)** — directionally aligned on principled agent-context management. HPI's axiom (agent never owns L3) inverts Letta's center of gravity.
- **W3C Verifiable Credentials + DIDs** — cryptographic primitives for token issuance.
- **OAuth 2.1 / capability-based security (macaroons, biscuits)** — scoped access patterns.
- **Torah sourceability discipline (*l'havdel elef avdal*)** — the cite-or-die rule's intellectual lineage. Every higher-layer claim cites the layer below; the citation chain is machine-resolvable.

## Status as of 2026-05-06

- ✅ Substrate model (L0–L3) articulated since 2024-04, formalized in this spec
- ✅ Axiom grammar v0: 4 families (OBL, RCG, TRU, PAT) drafted in production use at <client-corp> pilot
- ✅ Worked example: one obligation traced L0→L1→L2 with typed projection rule
- ⚠️ Token handoff protocol: described, not yet implemented as reference module
- ⚠️ JSON Schemas: not yet drafted
- ❌ Reference implementation: skeleton only
- ❌ Public review: not yet circulated

See `STATUS.md` for the full roadmap.

## Why this exists today

**The window.** Hyperscalers are racing to consolidate L3 ownership on their infrastructure. Once 50% of users have nontrivial cognitive memory inside one provider, the lock-in becomes self-perpetuating. Estimated remaining window for an open alternative to establish positional moat: 18–30 months.

**The artifact gap.** Two years of substrate thinking (Brain MCP, Viter L0→L3 pipeline, viter-ontology) exists in private. Without a public artifact, prior articulation does not compound into positional moat.

**The opening.** No existing player has shipped a typed axiom grammar for substrate-boundary handoff with permissioned one-time-token agent borrowing. The thesis space is unoccupied.

## Author's note

I am building this because I have to. The architecture HPI describes is not a thought experiment; it is the operating substrate from which the spec was written. If the substrate-as-load-bearing claim holds for the author, it holds for any human whose attention is valuable.

— Mordechai
