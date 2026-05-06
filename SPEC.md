# HPI Specification — v0 draft

> **Hyperpersonalized API. A protocol for sovereign cognitive substrate.**

**Status:** v0 draft. Sections 2 and 3 are full draft; Sections 1, 4–9 are outlines awaiting expansion.
**Last updated:** 2026-05-06
**Editor:** Mordechai Potash

---

## 1. Foundations & Problem Statement

### 1.1. The 2026 trajectory

By May 2026, every major model provider has shipped or is shipping a "memory" feature for their primary chat product. OpenAI's ChatGPT Memory has been live since 2024, with deep cross-conversation personalization and a developing "Chronicle" feature for long-running session state. Google's Gemini personalization layer reads across the user's entire Google account — Gmail, Drive, Calendar, YouTube, Search history — as a single accumulated context surface. Anthropic's Projects feature persists per-project context with a memory layer in beta. All three trajectories converge on the same architecture: **the user's accumulated cognitive context lives on the platform's servers**, owned by the platform under the platform's terms of service, accessible to the user only through the platform's product surfaces.

This is not an accident or a temporary state. Cross-conversation context is the moat. Switching costs are exactly the value of the user's accumulated history, and the platforms that own that history capture the rent. The competitive logic is sound and unlikely to reverse without protocol-level intervention.

### 1.2. The alignment problem

The platform's incentive is lock-in, monetization, and corporate-profit alignment. The user's interest is sovereignty, portability, and agency. These are not the same thing — and at platform scale, the divergence compounds.

Mordechai Potash, articulating this position publicly in February 2026:

> *"The elephant in the room is that obviously big tech are all trying to get to be this layer of transformation. It is incredibly dangerous that the layer should lie with the alignment of corporate profit. It is the complete incorrect alignment by definition. This is pashut [obvious]."*

The claim is structural, not adversarial. It is not that any specific platform is acting in bad faith. It is that an architecture in which the cognitive substrate of an individual human is owned by an entity whose primary obligation is to its shareholders cannot, by construction, optimize for the human's agency over the long term. The economics will route around any temporary alignment.

### 1.3. Why open protocols beat walled gardens at scale

History suggests the eventual answer at scale is a protocol, not a product:

- **SMTP** (1982) won email against AOL/CompuServe walled gardens. Nobody owns "your email." Hosting providers (Gmail, Microsoft, Proton) capture rent on infrastructure; the protocol itself is uncapturable.
- **TCP/IP** (1981) won networking against telco walled gardens. Nobody owns "your packets." ISPs and CDNs capture rent; the protocol is open.
- **HTTP** (1991) won information access against AOL Channels and CompuServe forums. Nobody owns "your browsing." Cloudflare, browsers, and edge providers capture rent; the protocol is open.
- **OAuth 2.0** (2012) won delegated authentication against custom-API-key sprawl. Nobody owns "your authentication." Auth0, Okta, and SaaS-side identity layers capture rent; the protocol is open.

The pattern is consistent: when value passes through a layer that's owned by a single entity, that entity captures the value AND constrains the system's evolution to its commercial interests. When the layer is an open protocol, value distributes across an ecosystem of infrastructure providers, and the system's evolution tracks user needs more honestly.

The cognitive-substrate layer of 2026 is exactly the next instance of this pattern. **HPI exists because that protocol does not exist yet.**

### 1.4. What HPI is

HPI is a typed protocol for substrate-boundary context handoff. Specifically:

- A **substrate model** (§2) — L0 through L3 — that names what cognitive context IS, where it lives, and how it transforms across layers within a substrate.
- A **typed axiom grammar** (§3) — families of typed assertions (OBL, RCG, TRU, PAT in v0) that preserve semantic meaning across substrate boundaries. Without typed grammar, bytes crossing a boundary lose meaning and require re-derivation.
- An **access control protocol** (§4) — agents request scoped, time-bounded, single-use, revocable tokens to read a human's context, with full audit trail emitted to the human's own substrate.
- A **wire format** (§5) — extends Anthropic's MCP (Model Context Protocol) with HPI-specific methods. Discovery via well-known URLs. Storage interface implementation-agnostic.

The v0 protocol is the minimum that lets a human own their substrate, agents borrow scoped views, and audit trails accrue under the human's control. It is implementable in a weekend by a single engineer; it is sufficient to demonstrate the architecture; it is positioned to be extended in v0.1 toward W3C Verifiable Credentials, capability-based delegation (macaroons), and ecosystem interop with adjacent open standards.

### 1.5. What HPI is not

HPI is not a model, not a memory product, not a wallet, not a blockchain, not anti-LLM, and not anti-platform. It is a **protocol** that defines a constraint at the substrate boundary. Anyone — including hyperscalers — can be HPI-compliant if their architecture respects the constraint. The constraint forbids a specific failure mode (the platform owning the user's accumulated cognitive substrate); it does not prescribe what the platform's commercial offering must be.

Specifically, HPI is NOT:

- **A model.** LLMs remain LLMs. HPI does not constrain model architecture or training. It governs what data the model has access to during a transaction and what records of that access accrue afterwards.
- **A memory product.** Mem0, Letta, Khoj, and Pieces solve a related but distinct problem (intra-session and cross-session memory management for agents). HPI's concern is one layer above: who owns the substrate the memory is stored against.
- **A wallet.** No native token, no cryptocurrency, no token economics. The "tokens" in HPI are JWT-style access credentials, not financial instruments.
- **Blockchain-required.** Implementations may use Web3 primitives (Ceramic, IPFS, ENS) or pure HTTP+JWT+filesystem. The protocol is silent on storage backing.
- **Anti-LLM.** LLMs are extraordinarily useful and HPI's whole point is to enable agents acting on the user's behalf. The constraint is on substrate ownership, not on AI utility.
- **Anti-platform.** Platforms can be HPI-compliant by routing their memory features through user-issued tokens, emitting audit events to the user's substrate, and accepting that the substrate cannot accumulate as the platform's asset. This is a real engineering constraint but not a business-model-killer.

### 1.6. Scope of v0

The v0 spec covers:
- The substrate model (§2) — load-bearing
- The typed axiom grammar framework (§3) — load-bearing; v0 ships four reference axiom families
- The access control protocol (§4) — load-bearing
- The wire format (§5) — implementable
- Reference implementation pointers (§6) — pointing at existing working code, not a new clean-room implementation
- Non-goals (§7) — to manage the discourse around what HPI is being asked to solve
- Open questions (§8) — RFC-style discussion items
- Acknowledgements & lineage (§9) — explicit credits for the precedents this builds on

**Out of scope for v0:**
- W3C Verifiable Credentials integration (target v0.1)
- Macaroons-style delegation attenuation (target v0.1)
- JSON Schema appendices for axiom families (target v0.1)
- Reference implementation as a separate library (target v0.1)
- Migration tooling from hyperscaler-stored memory to HPI substrate (target v1.0)

### 1.7. Audience

This spec is written for two audiences in roughly equal weight:

1. **Protocol implementers** — engineers building HPI runtimes, axiom-family extensions, or HPI-compliant agents. They need enough specificity to build interoperably.
2. **Architects and decision-makers** — at organizations choosing between sovereign-substrate and platform-memory architectures. They need the Foundation/Substrate Model/Non-Goals sections to evaluate the constraint.

A third audience — researchers and future protocol authors — is not the primary target but will likely read this document. The Acknowledgements section (§9) is for them: an honest map of what HPI builds on and where the genuinely novel claims are.

### 1.8. What HPI does NOT solve: continual learning and sovereign personalization

A category of problem HPI explicitly does not address: **per-person fine-tuned model weights**.

HPI specifies who can READ the substrate. It says nothing about who owns the model WEIGHTS that get distilled FROM the substrate. A per-person LoRA adapter, a personalized RLHF trace, or a distilled small model trained on the human's substrate — these are valuable and arguably essential primitives for sovereign personalization, but they are NOT what HPI v0 specifies.

The asymmetry: a user might own their L0–L3 substrate (HPI's claim) while the model that learned from it is owned by whoever ran the training. A complete sovereign-personalization stack would treat fine-tuned weights as another L-layer artifact subject to the same conservation law. HPI v0 doesn't.

This is named in `comparisons/LETTA.md` as one of the genuinely new architectural questions HPI v0 hasn't taken a position on. Per Karpathy's Dwarkesh-podcast framing (2025): *"maybe having a specific neural net per person... it's not a full-weight neural network. It's just some small sparse subset of the weights that are changed."* That direction may be where v1.0 needs to go.

For v0: this is acknowledged as a real gap, scoped out, and named as the most likely v1.0 architectural extension.

(Gap surfaced by Andrej Karpathy, simulated review of HPI v0, 2026-05-06.)

---

## 2. The Substrate Model (L0–L3)

### 2.1. Axiom 1 — L0 is the substrate boundary

**L0 is the most-raw digital copy held at the substrate's boundary.**

A *substrate* is the cognitive surface of a **substrate-holder** — the protocol's primitive party. A substrate-holder MAY be:
- An individual human (the typical case, e.g., Mordechai, Alice)
- An organization or institution (a hospital, a law firm, a government body)
- A government department, agency, or military unit
- A family unit or other small-group entity that bears collective responsibility
- A specific persona or role within a larger entity (e.g., "Alice-as-CFO" distinct from "Alice-as-private-individual")

The substrate-holder is whoever **bears the consequences** of decisions made by agents operating against their substrate. In the high-stakes use cases HPI is designed for — defense agents on classified context, hospital agents on PHI, financial agents on fiduciary data — the substrate-holder is typically an institution; the individual operator within the institution is an agent of the institution. For consumer-grade use cases, the substrate-holder is often the individual.

The protocol does not privilege individual humans over institutional substrate-holders. The mechanics of token issuance, scope, audit, and revocation work identically across these cases. What differs is who holds the signing keys and who reviews the audit trail.

The substrate has a boundary: everything inside the boundary is the substrate's information. L0 is whatever sits at that boundary — the most-raw digital artifact the holder has, however backed.

#### 2.1.1. L0 is a logical entity, not necessarily a file

An L0 entity has three possible backings:

- **Local L0** — bytes the holder possesses (a stored file). Example: a Claude Code session JSONL on the holder's filesystem.
- **External L0 by pointer** — bytes the holder does not store, addressed by a stable identifier. Examples: YouTube video ID, DOI, gmail message-id, git commit SHA, IPFS CID, Drive file-id. The pointer IS L0-grade as long as the upstream honors it.
- **Promoted L0** — bytes the holder no longer has upstream access to. A derivative the holder retained becomes the only available copy of the substrate at that point. Example: a YouTube video the holder consumed and transcribed; the video is later deleted from YouTube; the transcript is now the only L0 backing for that entity.

#### 2.1.2. Provenance metadata (REQUIRED)

Every L0 entity MUST carry the following provenance fields:

```yaml
l0_entity:
  id: <opaque unique identifier within the substrate>
  type: <typed enum — youtube_video | local_file | http_url | git_sha | gmail_message | ...>
  backing:
    - {kind: local, path: <path>}
    - {kind: external, url: <url>, identifier: <stable-id>}
  creator: <upstream — substrate-id or party that produced the bytes>
  ingester: <substrate-holder — who pulled it across THEIR boundary>
  fetched_at: <RFC3339 timestamp>
  upstream_status: live | drifted | lost
  promoted: <boolean — true iff backing is local-only and upstream is no longer available>
  derivatives: [<list of pointers to L1+ entities derived from this L0>]
```

**The creator is distinct from the ingester.** The creator MAY equal the ingester (a meeting recording: holder both creates and ingests). They MAY differ (a YouTube video the holder consumed — Nate B Jones is the creator; the holder is the ingester).

The protocol does not require these to be the same entity. Implementations MUST surface both fields.

#### 2.1.3. L0 is immutable from the moment of ingestion

Once an L0 entity is recorded, its `bytes` (if local-backed) and its `pointer` (if external-backed) MUST NOT be modified. Re-fetches that produce different bytes from the same pointer create a new L0 entity with `upstream_status: drifted` on the prior entity. Mutability is handled by versioning, not in-place edits.

Rationale: L0 is the bedrock for the citation chain. If L0 mutates, all higher-layer claims become unverifiable retrospectively.

### 2.2. Axiom 2 — Layers are pure functions of the layer below

The cognitive pyramid above L0, for v0, has three layers:

#### 2.2.1. L1 — deterministic extraction

L1 is a deterministic, judgment-free transformation of L0. Per-day normalization, per-channel chronological extraction, per-thread bundling. Examples (drawn from existing implementations):

- **chat-log L1**: Per-day markdown digest of all Claude Code session JSONLs. Format: chronological by session, prompts and responses verbatim.
- **whatsapp L1**: Per-day chronological extraction from canonical-chat.jsonl with inline attachment references and voice-note transcriptions.
- **transcripts L1**: Per-day digest from screenpipe + per-meeting m4a/.tsv extraction.

Implementations MUST emit L1 such that re-running the extractor over the same L0 produces byte-identical output (modulo timestamps in metadata). L1 is mechanical, not interpretive.

#### 2.2.2. L2 — synthesis with judgment

L2 is interpretive synthesis. Decisions, themes, tagged quotes, state shifts. L2 carries the synthesizer's identity — *Mordechai's L2 of meeting M* and *Shaul's L2 of meeting M* are sibling L2 artifacts citing the same L1, not conflicting versions.

L2 MUST cite L1 by reference. Citation is structural (machine-resolvable pointer) and procedural (the L2 author affirms the citation).

#### 2.2.3. L3 — working surface (the prosthetic)

L3 is the holder's current cognitive surface. State, open questions, recent decisions. It is the prosthetic — *what I need in front of me to think with*.

L3 is regenerated from L2 on a cadence the holder defines (typically daily, often per-session).

#### 2.2.4. The governing rule

> **L0 is immutable. Each layer is a pure function of the layer below. Every higher-layer claim cites a citation chain back to L0.**

This rule has procedural form (cite-or-die discipline; *l'havdel elef avdal*) and structural form (every L1+ entity carries an explicit `cites: [<l0_or_lower_layer_id>...]` field; citations MUST be machine-resolvable).

#### 2.2.5. Layer count is conventional, not load-bearing

The protocol does NOT hard-code "exactly 4 layers." Implementations MAY introduce intermediate layers (L1.5 for cross-day bundling; L2.5 for narrated artifacts) AS LONG AS the layer-citation rule holds. The conventional 4-layer model is the v0 reference; the rules are normative.

### 2.3. Axiom 3 — The subjectivity gradient

| Layer | Approximate objectivity | Sharing economics |
|---|---|---|
| L0 | ~99% objective (the bytes are the bytes) | shareable (storage cost only) |
| L1 | ~90% objective (extraction is mostly mechanical) | shareable (verifiable by re-running extractor) |
| L2 | ~50% subjective | shareable as **attributed perspective** |
| L3 | ~95% subjective | mostly private; shared as windows into the holder |

This gradient is asymptotic, not absolute. The point is the **monotonic relationship**: subjectivity rises from L0 to L3; sharing economics fall in lockstep.

**Operational implications:**

- L0/L1 stores MAY be shared infrastructure (multi-tenant blob store, RLS-gated rows) without violating sovereignty
- L2 stores MUST attribute synthesis to the synthesizer (`author: <substrate-id>`) and MAY be shared with attribution
- L3 stores SHOULD default to single-substrate-only access; shared windows MUST be issued via §4 token mechanics

### 2.4. Axiom 4 — The Substrate Conservation Law

When an L3 artifact is published, sent, or persisted across a substrate boundary, it becomes the receiving substrate's L0.

This applies in two cases:

#### 2.4.1. Interpersonal collapse

Holder A publishes an L3 artifact (memo, article, video, code commit, social post). Holder B receives the artifact. **In B's substrate, the artifact is L0** — the most-raw digital copy B has of A's published synthesis.

B never had access to A's L0/L1/L2 chain; B's L1+ chain on top is built atop A's L3 *as B's L0*.

Worked example: Mordechai publishes a Persofi-flow memo as L3. <the CFO> receives the PDF. In <the CFO>'s substrate, the PDF is an L0 entity with:
- `creator: did:web:mordechai.id`
- `ingester: did:web:jeffrey.id`
- `backing: {kind: local, path: ".../persofi-flow-v3.pdf"}` + `{kind: external, url: "<gmail-message-id>"}`
- `fetched_at: 2026-04-19T07:30Z`

<the CFO>'s L1 extracts the memo's section structure deterministically; <the CFO>'s L2 decides what to do about it. Citations in <the CFO>'s L2 point at his L0 entity for the memo. They do NOT transit through to Mordechai's interior pyramid — <the CFO> doesn't have access.

#### 2.4.2. Intertemporal collapse

Holder A's L3 written at time *t* (e.g., today's `_now.md`). At time *t + δ*, today-A has structurally the same epistemic position as receiver-B in §2.4.1. Today-A does not have access to yesterday-A's L1/L2 thinking process; today-A only has the published L3 artifact.

The L3 has collapsed to L0 across the time boundary within the same human substrate.

This is why prosthetics like `_now.md` work. Without intertemporal collapse, every session would re-derive from raw L0; with it, today-A stands on yesterday-A's compressed work. The substrate accumulates value geometrically across time precisely because of this mechanism.

#### 2.4.3. The conservation law (formal)

> **Information at rest in a substrate is L0 to its holder. Information in motion across substrate boundaries collapses from L3 (sender) to L0 (receiver).**

#### 2.4.4. Citations stop at substrate boundaries

A claim in B's L2 may cite an L0 entity in B's substrate that points at A's published L3. **The chain does not transit through to A's interior pyramid.** B's L0 entity is the terminal of B's citation chain.

This is honest epistemology: B never had A's interior process. B has only A's published artifact. B's claims rest on what B holds.

### 2.5. Axiom 5 — Two owners per L0

Every L0 entity has **two owners**, distinct and both REQUIRED:

- **Creator** — the upstream substrate or party that produced the bytes.
- **Ingester** — the substrate-holder who pulled the artifact across THEIR boundary, into their substrate.

The creator MAY equal the ingester. They MAY differ. The protocol does not collapse them.

This matters because:
- Citations across substrate boundaries name the creator (for attribution) AND the ingester's L0 entity (for re-fetch resolution)
- Deletion semantics differ: creator can break the upstream pointer (causing `upstream_status: lost`); ingester can delete the local backing
- Trust assertions can be made independently about each (TRU-* axiom per §3)

---

## 3. Typed Axiom Grammar

### 3.1. Why typed axioms

Plain L0 bytes have no semantics across substrate boundaries. When my L3 synthesis (an obligation ruling, say) lands in <the CFO>'s substrate as L0, its bytes alone are just text or JSON. For the meaning to survive the boundary, the L0 entity needs to be **typed** — identified as instance-of an axiom family with known semantics.

Axiom families are the typed grammar for substrate-boundary preservation. They are not database tables; they are not schemas. They are **opinions about how the world is shaped**, expressed strictly enough that L0 entities can be tagged with them and downstream claims can be machine-validated against them.

### 3.2. Axiom families (v0)

Each axiom family is a *worldview claim* about a domain, expressed as a small set of typed sub-axioms. v0 covers four families, drawn from financial-vertical operations (the Persofi pilot at <client-corp>):

| Family | Domain | Type | File |
|---|---|---|---|
| **OBL** | Obligations: contracts, evidence, identity | axiom family | [`axioms/OBL-obligations.md`](axioms/OBL-obligations.md) |
| **RCG** | Recharges: trust-based renewal, margin attribution | axiom family | [`axioms/RCG-recharges.md`](axioms/RCG-recharges.md) |
| **TRU** | Trust: counterparty ratings, thresholds, scopes | axiom family | [`axioms/TRU-trust.md`](axioms/TRU-trust.md) |
| **PAT** | Patents: long-lived legal entity lifecycle | **Reference Domain Ontology** | [`axioms/PAT-patents.md`](axioms/PAT-patents.md) |

The four families are **not exhaustive of the protocol's reach.** They are v0 — drawn from one vertical (financial operations with patent-prosecution focus) because that vertical has working production code and traceable derivations. Other verticals (healthcare records, legal discovery, software engineering, scientific publication) will require their own axiom families. The framework in §3.3 is the universal part; the families are vertical instantiations.

**PAT is promoted from "axiom family" to "Reference Domain Ontology."** The PAT family commits to what objects exist in the patent-prosecution domain — `Patent`, `PatentApplication`, `Jurisdiction`, `Family`, `Renewal`, lifecycle states with forbidden transitions — at a level of specificity that constitutes a worldview claim, not just typed claim grammar. Implementers building HPI for new verticals should look at PAT as the model for how to commit to a domain Ontology that rides on the HPI substrate-boundary protocol.

### 3.3. Anatomy of a v0 axiom family

A conformant axiom family file MUST contain:

1. **The opinion** — a 1–3 paragraph statement of the worldview claim. Why this domain has a non-obvious shape. What this opinion buys downstream.
2. **The core axiom** — the load-bearing typed assertion. Numbered (e.g., `OBL-1`).
3. **Sub-axioms** — typed extensions of the core. Numbered sequentially within the family.
4. **Allowed states** (for axioms with state machines) — explicit transition diagram, with forbidden transitions named.
5. **What this axiom buys you** — concrete downstream affordances enabled by the opinion.
6. **L2 projection rule** — how L1 evidence projects into L2 facts under this family. Worked example required.
7. **What's NOT in this axiom (intentionally)** — scope discipline. Lists adjacent concerns that belong in sibling families or out-of-scope.
8. **Open questions** — unresolved tensions in the v0 draft.

Each sub-axiom MUST be expressible as a typed assertion machines can verify. JSON Schema 2020-12 is the v0 reference; alternative encodings (Protobuf, Avro, OpenAPI) are conformant if they preserve the typed structure.

### 3.4. Axiom file conformance status (v0)

| File | Sections present | Schema drafted? | In production? |
|---|---|---|---|
| `OBL-obligations.md` | All 8 sections | ⚠️ inline only, no JSON Schema yet | ✅ <client-corp> pilot, since 2026-04 |
| `RCG-recharges.md` | All 8 sections | ⚠️ inline only | ✅ <client-corp> pilot |
| `TRU-trust.md` | All 8 sections | ⚠️ inline only | ⚠️ partial — supplier trust scores live |
| `PAT-patents.md` | All 8 sections | ⚠️ inline only | ❌ v0.1 draft — not yet wired in production |

JSON Schema appendices for each family are scope for v0.1.

### 3.5. Worked example

A single Persofi obligation traced from L0 evidence (5 sources) through L1 extraction and L2 projection under the OBL family axioms is given in [`examples/01-obligation-end-to-end.md`](examples/01-obligation-end-to-end.md). This is the canonical reference for "how does an axiom family actually fire on real data." Implementers should read it before writing new axiom families.

### 3.6. The substrate-vs-ontology distinction

Axiom families (this section) are the **vertical worldview** — what a domain MEANS. They are distinct from the **horizontal substrate** — how data physically traverses the L0–L3 stack.

A discussion of this distinction, including the relationship to Anthropic MCP and to Plurality/OCL, is captured in [`axioms/06-substrate-vs-ontology.md`](axioms/06-substrate-vs-ontology.md).

For the protocol: **HPI's transport (§5) is substrate-level. HPI's typed grammar (this section) is ontology-level. Both are required, both are separable.** An HPI implementation could swap axiom families without changing transport; or swap transport (e.g., from MCP to a future RPC) without changing axiom families.

### 3.7. HPI as cross-Ontology transport (not Ontology replacement)

The framework in §3.1–§3.3 is deliberately **meta-ontological**: it specifies how typed claims are structured (epistemic status, provenance, scope), not what objects exist in any specific world. This is intentional and has a name.

**HPI is the cross-Ontology transport layer.** Domain Ontologies — Palantir's Foundry Ontology, healthcare's HL7 FHIR, legal's Akoma Ntoso, IP's WIPO ST.96, scientific publication's CrossRef metadata — ride on top of HPI as the wire format that lets typed claims from any of them cross substrate boundaries with semantic preservation.

HPI does NOT compete with these Ontologies. HPI does NOT replace them. HPI is the protocol layer that lets a Foundry-typed `Aircraft` claim emitted by Substrate A land in Substrate B with its typing intact. Without HPI, the receiving substrate would have to re-derive the typing from raw bytes.

To say it sharply: **per-domain Ontologies specify what objects exist in a domain. HPI specifies how typed objects from any domain travel across substrate boundaries.** Both are required for a complete agent infrastructure. Neither is the other. The two compose.

This positioning was sharpened by simulated peer review of HPI v0 (Alex Karp, 2026-05-06): *"You shipped a meta-language. We ship a worldview."* The disambiguation in this section is the response. HPI is meta by design, not by oversight; the typed-grammar move is the cross-domain transport contribution, not an attempt to specify any single domain. PAT (§3.4) demonstrates how a domain-specific Ontology can be expressed as an axiom family riding on the HPI framework.

### 3.8. v0.1 axiom validator commitment

The v0 spec defines axiom families at the prose level. **v0.1 will provide JSON Schemas (Draft 2020-12) for each family AND a runtime validator that rejects axiom assertions whose `cites` field does not resolve to existing L0 entities.** This converts the cite-or-die discipline from advisory (procedural) to enforceable (structural). The reference implementation (§6) will include this validator.

---

## 4. The Token Handoff Protocol

The HPI access-control primitive. Defines how an agent obtains scoped, time-bounded, revocable, audited permission to read a human's L1+ context for a single transaction.

### 4.1. The access axiom

The HPI access-control primitive separates two claims that prior drafts conflated. The wire format enforces only the first; the second is an architectural recommendation HPI does not technically prevent agent runtimes from violating.

#### 4.1.1. What HPI ENFORCES (the access axiom)

> **An agent MAY only access a substrate's L1+ content via permissioned, time-bounded, single-use tokens issued by the substrate-holder.**

This is a wire-format claim. It is enforceable: the runtime refuses requests without valid tokens; tokens are signed; scopes are signed; revocation is published; consumption is logged. Any agent that consumes substrate context outside this mechanism is non-compliant by detectable construction.

#### 4.1.2. What HPI RECOMMENDS (the persistence position)

> **An agent SHOULD NOT accumulate persistent identity, memory, or continuity across substrate-boundary transactions in a way that routes around the substrate-holder's audit and control.**

This is a normative position, not a wire-format guarantee. HPI cannot directly prevent an agent from caching returned scope content within the agent's own runtime. The wire format ends at the runtime boundary. Agent-internal state — whether the agent develops a persistent persona, learned skills, durable identity — is invisible to HPI.

Stateful agent architectures (Letta-style memory blocks, Mem0-style memory layers, Pieces-style local-first persistence) MAY be HPI-compliant by:
- requesting scoped tokens like any other agent,
- emitting audit events for every consumption,
- respecting single-use semantics,
- writing durable substrate updates back as new L0 entities (§4.11).

What such agents do *inside* the borrowed scope — accumulate working memory, distill skills, evolve persona — is architecturally legitimate even though HPI's normative position discourages it. The constraint that bites is the boundary, not the interior.

#### 4.1.3. The framing handle

Conceptually: **HPI is the kernel. Stateful agent architectures are processes.** The kernel controls what memory pages a process can access; the process owns its own stack. (Framing credited to Sarah Wooders, simulated review of HPI v0, 2026-05-06.)

#### 4.1.4. Inverse of agent-centric architectures

HPI's normative position (§4.1.2) is the inverse of agent-centric architectures (e.g., Letta's Context Constitution, which holds that *"agents own their context"* and assigns agents "Three Pillars of Selfhood: Identity, Memory, Continuity"). HPI is human-centric by axiom; agent-centric architectures are coherent but build a different future. The two compose at the boundary: see `comparisons/LETTA.md` for the architectural diff and the proposed integration story.

### 4.2. Token format

#### v0 (this draft): signed JWT

A v0 HPI token is a JSON Web Token (RFC 7519) signed with the issuer's key (Ed25519 RECOMMENDED; ECDSA P-256 permitted). Required claims:

```json
{
  "iss": "did:web:alice.example",
  "sub": "did:agent:claude-instance-7afe",
  "aud": "https://hpi.alice.example/v0",
  "iat": 1746518400,
  "exp": 1746522000,
  "jti": "01J5K9R7Q8XQVN3KT9V0V0F0V8",
  "hpi": {
    "version": "0",
    "scope": {
      "axiom_families": ["OBL", "RCG"],
      "axiom_ids": ["OBL:o-2026-04-18-DE-87332"],
      "layers": ["L1", "L2"],
      "actions": ["read"]
    },
    "purpose": "reconcile-supplier-statement",
    "purpose_text": "User asked agent to reconcile <de-vendor-corp> April statement",
    "single_use": true,
    "delegation": "forbid"
  }
}
```

Field semantics:

- `iss` (REQUIRED) — DID of the substrate-holder issuing the token. Identifies the human (or human-controlled organization).
- `sub` (REQUIRED) — DID of the agent the token is issued to. Tokens are non-transferable; the agent's DID MUST match the bearer.
- `aud` (REQUIRED) — URL of the HPI runtime that will consume the token.
- `iat` / `exp` (REQUIRED) — issued-at and expiry. RECOMMENDED max validity: 1 hour for read-only scopes; 15 minutes for action-emitting scopes.
- `jti` (REQUIRED) — unique token identifier. Used for single-use enforcement and revocation.
- `hpi.scope.axiom_families` — array of family codes (e.g., `OBL`, `RCG`, `TRU`, `PAT`) the agent may read.
- `hpi.scope.axiom_ids` — array of specific axiom IDs (overrides families if both specified). Empty = all in family.
- `hpi.scope.layers` — array of permitted layers. Tokens MAY grant L1, L2, or both. **Tokens SHOULD NOT grant L3** unless the holder explicitly opts in (it's the prosthetic; sharing it is sharing the working mind).
- `hpi.scope.actions` — array of action verbs. v0: `read`, `write` (with sub-scopes). v0.1 will add `propose`, `commit-on-confirm`, etc.
- `hpi.purpose` — machine-tag describing why this token was issued. Used for audit aggregation.
- `hpi.purpose_text` — human-readable purpose description, surfaced in audit UI.
- `hpi.single_use` — boolean. Default `true`. If `true`, the token is consumed on first use and the HPI runtime refuses further consumption attempts with the same `jti`.
- `hpi.delegation` — `forbid` (default) | `attenuate` | `re-request`. Controls sub-agent handoff (see §4.8).

#### v0.1 (planned): W3C Verifiable Credential format

Migration path: tokens become VCs with cryptographic proof chains, allowing third-party audit without contacting the issuer. v0 JWT format is a strict subset of the v0.1 VC envelope — implementations that emit v0 JWTs can be upgraded by re-wrapping in VC structure without changing the issuance or consumption semantics.

### 4.3. Scope structure

Scopes are **typed, additive, and minimum-privilege by default.**

The scope structure has four orthogonal dimensions:

1. **Axiom dimension** — which typed semantic content (families, specific IDs)
2. **Layer dimension** — which substrate layers (L1, L2, L3)
3. **Action dimension** — what the agent may do (`read`, `write`, `propose`)
4. **Time dimension** — `exp` claim sets the upper bound

A token's effective capability is the **intersection** of its scope dimensions. Granting `axiom_families: [OBL]` + `layers: [L1]` + `actions: [read]` permits read-only access to L1 entities tagged as instances of OBL — nothing else.

Implementations MUST refuse expansion of scope (no "promote" semantics inside the agent). Scope expansion requires a new token issuance.

### 4.4. Issuance flow

```
┌──────────────┐         ┌──────────────┐        ┌─────────────┐
│  AGENT       │         │  HPI RUNTIME │        │  HUMAN      │
│ (acting on   │         │  (issuer)    │        │ (substrate- │
│  behalf of)  │         │              │        │  holder)    │
└──────┬───────┘         └──────┬───────┘        └──────┬──────┘
       │                        │                       │
       │  1. request_context    │                       │
       │  (purpose, scope)      │                       │
       │ ────────────────────►  │                       │
       │                        │                       │
       │                        │  2. policy check      │
       │                        │  (pre-approved? ask?) │
       │                        │                       │
       │                        │  3. (if asks)         │
       │                        │   present to human    │
       │                        │ ─────────────────────►│
       │                        │                       │
       │                        │   4. approve/deny     │
       │                        │ ◄─────────────────────│
       │                        │   (with scope edits)  │
       │                        │                       │
       │  5. token (signed)     │                       │
       │ ◄────────────────────  │                       │
       │                        │                       │
       │  6. consume_token      │                       │
       │  (jti, action)         │                       │
       │ ────────────────────►  │                       │
       │                        │  7. verify, mark      │
       │                        │  used, return data    │
       │  8. data (scoped)      │                       │
       │ ◄────────────────────  │                       │
       │                        │                       │
       │                        │  9. emit audit event  │
       │                        │  to human's L0        │
       │                        │ ─────────────────────►│
```

Steps:

1. **Agent calls `hpi.request_context`** with a structured request: purpose, requested scope, requested expiry.
2. **HPI runtime checks policy.** Policies are pre-defined rules ("auto-approve OBL+RCG read for purpose=reconcile up to 1h"). If the request matches a policy, skip to step 5.
3. **If no matching policy**, runtime presents the request to the human via the human's chosen interface (CLI prompt, mobile push, IDE hover).
4. **Human approves, denies, or modifies scope.** Approval is signed by the human's key. Modifications: human MAY narrow the scope (drop an axiom family, shorten expiry); human MAY NOT broaden it.
5. **Runtime issues signed token** to the agent.
6. **Agent calls `hpi.consume_token`** with the token + a specific action.
7. **Runtime verifies** signature, expiry, single-use, scope match. On success, marks `jti` consumed and returns the requested data filtered to scope.
8. **Agent receives data**, performs its task, returns result.
9. **Runtime emits an audit event** to the human's substrate as a new L0 entity (typed `hpi_token_consumed`). The audit trail is itself substrate; the human owns their own audit.

### 4.5. Single-use semantics

The default `single_use: true` means a token's `jti` is consumed on first call to `hpi.consume_token`. Re-presenting the same `jti` MUST fail with error `token_consumed`.

Multi-use tokens (`single_use: false`) are permitted but DISCOURAGED. They exist for narrow operational scenarios (e.g., a long-running agent that needs continuous read access for a single user-initiated reconciliation run). Multi-use tokens MUST have stricter expiry (RECOMMENDED 5 minutes) and MUST log every consumption event individually.

### 4.6. Revocation

The substrate-holder MAY revoke any active token at any time.

#### 4.6.1. Revocation list

Each HPI runtime publishes a revocation list at a well-known endpoint:

```
GET /.well-known/hpi/revocations.json
{
  "version": "0",
  "issuer": "did:web:alice.example",
  "updated_at": "2026-05-06T12:00:00Z",
  "revoked": [
    {"jti": "01J5K9R7Q8XQVN3KT9V0V0F0V8", "revoked_at": "2026-05-06T11:55:00Z", "reason": "user-initiated"}
  ]
}
```

Agents MUST check this list before consuming a token if the time elapsed since `iat` exceeds 60 seconds. Implementations MAY cache the list with HTTP caching semantics; agents MUST honor `Cache-Control` from the issuer.

#### 4.6.2. Reasons

Standard revocation reasons:
- `user-initiated` — substrate-holder explicitly revoked
- `policy-changed` — automated policy rotation
- `compromise-suspected` — agent or runtime credential compromise
- `expired-superseded` — token replaced by a newer issuance covering the same scope

### 4.7. Audit trail

Every token issuance, consumption, denial, and revocation MUST be recorded as an L0 entity in the substrate-holder's substrate.

Standard audit-event types:
- `hpi_token_issued` — fields: `jti`, `agent_did`, `scope`, `purpose`, `expiry`
- `hpi_token_consumed` — fields: `jti`, `agent_did`, `action`, `data_returned_size`
- `hpi_token_denied` — fields: `request_id`, `agent_did`, `requested_scope`, `denial_reason`
- `hpi_token_revoked` — fields: `jti`, `revoked_by`, `reason`

The audit trail is itself a substrate stream (parallel to chat-log, whatsapp, transcripts). It is L0; deterministic L1 extracts roll up by day / by agent / by purpose; L2 syntheses surface anomalies. Because the audit trail is in the substrate, the substrate-holder owns their own audit, full stop.

This is the structural inversion of platform-mediated auditing — when OpenAI logs your prompts on their servers, the audit lives in OpenAI's substrate. When HPI logs your tokens, the audit lives in YOURS.

### 4.8. Delegation

When an agent holding a token wants to invoke a sub-agent (a different DID) on the substrate-holder's behalf, the protocol provides three modes:

#### 4.8.1. `forbid` (default, RECOMMENDED for v0)

The token MUST NOT be passed to a sub-agent. The sub-agent MUST request its own token directly from the runtime, with its own DID as `sub`. This preserves auditability — the substrate-holder sees both agent invocations distinctly.

#### 4.8.2. `attenuate` (macaroon-style, v0.1)

The agent MAY derive a sub-token by attenuating its own scope. The sub-token's scope MUST be a strict subset of the parent token's scope. The agent signs the attenuation; the runtime verifies the chain on consumption. This pattern is borrowed from macaroons (Birgisson et al., 2014) and biscuits (CleverCloud).

Attenuation is a v0.1 feature — it requires careful audit-trail extension and is omitted from v0 to keep the threat model simple.

#### 4.8.3. `re-request` (v0.1)

The agent MAY request a fresh token on the sub-agent's behalf. The runtime treats this as a new issuance request, with the parent agent named as the requester and the sub-agent named as `sub`. Human approval is re-asked unless a policy auto-approves the chain.

### 4.9. Worked example (one transaction)

Alice (substrate-holder) asks her agent to "reconcile <de-vendor-corp>'s April invoice against the <client-corp> books."

1. **Agent constructs request:**
   ```json
   {
     "method": "hpi.request_context",
     "purpose": "reconcile-supplier-statement",
     "purpose_text": "Alice asked agent to reconcile <de-vendor-corp> April statement against book records",
     "scope": {
       "axiom_families": ["OBL", "RCG"],
       "layers": ["L1", "L2"],
       "actions": ["read"]
     },
     "expiry_seconds": 3600
   }
   ```
2. **Runtime checks Alice's policy.** Policy: "auto-approve OBL+RCG read up to 1h, max 50 axiom IDs returned." Match. Skip human prompt.
3. **Runtime issues token** with `single_use: true`, scope as requested, exp=now+3600s.
4. **Agent calls `hpi.consume_token`** with the token and a specific action: `query_obligations(supplier="<de-vendor-corp>", period="2026-04")`.
5. **Runtime verifies, returns** the relevant L1 evidence + L2 obligation/recharge syntheses, filtered to scope. 23 OBL entities, 7 RCG entities returned.
6. **Agent runs reconciliation logic** in its own working memory. Produces a result. Returns to Alice.
7. **Runtime emits audit events:**
   - `hpi_token_issued` (jti=..., scope=..., purpose=reconcile-supplier-statement)
   - `hpi_token_consumed` (jti=..., action=query_obligations, data_returned_size=30 entities)
8. **Alice's L1 audit extract** rolls up: "1 reconciliation transaction today, 1 agent (Claude-7afe), 30 entities accessed, 0 anomalies."

The agent never persisted any of Alice's data outside the transaction. The agent never asserted ownership of Alice's L3. Alice's substrate accumulates the audit trail. The reconciliation result is returned to Alice; if Alice approves, she emits the action herself (or grants the agent a separate write-scoped token to act on her behalf).

This is the full HPI pattern.

### 4.10. Failure modes (benign)

The §4 issuance/consumption flow specifies happy-path behavior. Real deployments encounter failures that aren't adversarial but still need defined semantics. This section addresses **benign** failures; adversarial ones are in `THREAT-MODEL.md`.

**Agent crash mid-transaction with non-revoked token.** Token is treated as consumed by the runtime as a defensive default (the conservative choice — assume the agent saw the data even if it didn't process it). Retry requires a fresh token issuance. Audit event `hpi_token_consumed` is emitted at runtime with a synthetic note that no consumption confirmation was received.

**Runtime crash before consumption.** Token may be re-presented after runtime recovery; runtime MUST be idempotent at the consumption layer (consuming the same `jti` twice MUST return the same data response, not error). The `jti` log is the authoritative consumption record.

**Network partition between agent and runtime.** Agent re-presents token on reconnect. Runtime detects double-consumption attempts via `jti` log and refuses with `error: token_consumed`. If the agent has not yet received the data response, it requests a fresh token.

**Clock skew on `exp` claim.** Implementations MUST tolerate up to 60 seconds of clock skew on `exp` validation. Agents and runtimes SHOULD use NTP-synchronized clocks. The revocation list is the authoritative override for ambiguity.

**Discovery document unavailable.** When `/.well-known/hpi.json` returns 5xx or times out, agents MUST fail closed (refuse to construct a request rather than fall back to insecure defaults). Implementations SHOULD cache the discovery document with HTTP cache-control semantics.

**Revocation list unavailable.** When the revocation endpoint is unreachable, agents MUST fail closed for tokens whose elapsed time since `iat` exceeds 60 seconds (cannot verify revocation status). For fresh tokens (<60s since issuance), agents MAY proceed under the assumption that revocation could not have propagated yet.

### 4.11. Learning across boundaries

Learning that occurs during a transaction is the agent's working state. By default, this state is discarded at session end — the borrowed scope expires, the agent's working memory has no durable backing in the substrate.

**For learning to persist across substrate boundaries**, it MUST be written back to the substrate-holder's substrate as a new L0 entity, with provenance fields naming the agent as `creator` and the substrate-holder as `ingester`. The substrate-holder MAY then choose to incorporate the new L0 entity into their L1+ chain, or MAY discard it.

**Stateful agent architectures (Letta-style memory blocks, Mem0-style memory layers) MAY persist learned content within the agent's own runtime**, separate from the substrate. Such persistence is invisible to HPI — the substrate-holder cannot directly inspect the agent's working memory or learned skills. The HPI-enforced constraint is that durable presence in the substrate-holder's substrate requires the explicit write-back mechanism above.

This separates two concerns:
- **The agent's accumulating capability** lives in the agent's runtime, not the substrate.
- **The substrate's accumulating record** lives in the substrate, written explicitly via the boundary protocol.

The substrate-holder governs what enters their substrate. The agent's runtime governs what the agent retains across sessions. Neither has authority over the other; the boundary is sacred.

### 4.12. Boundary conditions: inference-level scope

A subtle but load-bearing distinction. HPI's tokens scope DATA ACCESS — what content the agent may read from the substrate. They do NOT scope INFERENCE — what conclusions the agent may draw from accessed content, or what derivative information the agent may generate by combining accessed content with model parameters.

This distinction matters because:
- An agent with `OBL` scope can read obligation entities. Once read, the agent can infer trends, summaries, predictions, behavioral patterns of the substrate-holder. None of these inferences are token-mediated; they happen inside the agent's working memory using the model's parameters.
- The model's training data already contains generic priors that, combined with the agent's scoped read, may produce outputs the substrate-holder didn't intend to authorize.
- HPI cannot prevent this. The protocol stops at the runtime boundary; what the model does with returned data is governed by model architecture and the agent's prompting, not by HPI.

**The HPI position:** access control is necessary but not sufficient for full information sovereignty. Inference-level governance requires either (a) trust in the agent's runtime to honor purpose constraints, (b) differential-privacy bounds on what can be inferred from any single transaction (v1.0 research scope), or (c) post-hoc review of agent outputs by the substrate-holder before acting on them.

HPI v0 does the first thing well, gestures at the third (audit trail), and defers the second to research. v1.0 may close this gap; v0 acknowledges it explicitly.

(Distinction credited to Andrej Karpathy, simulated review of HPI v0, 2026-05-06: *"Once tokens are in the context window, they ARE the working memory; protocol-layer scoping cannot constrain inference."*)

---

## 5. Wire Format & Transport

### 5.1. Transport: extending Anthropic MCP

HPI extends the Anthropic Model Context Protocol (MCP), Apache 2.0, first published November 2024. The choice is deliberate:

- MCP has substantial 2026 adoption (3,000+ community servers, multi-vendor client support)
- MCP defines the JSON-RPC envelope HPI needs without HPI having to define its own RPC
- HPI methods become discoverable as MCP tools, naturally interoperating with MCP-aware agents

HPI does NOT replace MCP. An HPI runtime is a specialized MCP server that exposes the methods defined in §5.2 in addition to whatever other tools it offers. An MCP client (e.g., Claude Code, Cursor, or any MCP-compatible agent) interacts with HPI via standard MCP semantics — there is no separate transport layer to implement.

For implementations where MCP is unavailable (offline agents, embedded systems), HPI methods MAY be exposed via plain HTTP+JSON. The method semantics and JSON shapes defined in this section are normative; the choice of transport (MCP vs HTTP) is non-normative.

### 5.2. HPI methods (MCP tool surface)

An HPI runtime MUST expose the following methods. All methods take JSON arguments and return JSON results.

#### 5.2.1. `hpi.request_context`

Agent requests permission to read scoped substrate context.

**Arguments:**
```json
{
  "purpose": "<machine-tag>",
  "purpose_text": "<human-readable description>",
  "scope": {
    "axiom_families": ["OBL", "RCG"],
    "axiom_ids": [],
    "layers": ["L1", "L2"],
    "actions": ["read"]
  },
  "expiry_seconds": 3600,
  "agent_did": "did:agent:<id>"
}
```

**Returns (success):**
```json
{
  "token": "<signed-jwt>",
  "issued_at": "2026-05-06T10:43:00Z",
  "expires_at": "2026-05-06T11:43:00Z",
  "approved_scope": { /* may be narrower than requested */ }
}
```

**Returns (denial):**
```json
{
  "error": "denied",
  "reason": "<machine-code>",
  "reason_text": "<human-readable explanation>",
  "request_id": "<for-audit-correlation>"
}
```

#### 5.2.2. `hpi.consume_token`

Agent presents a token to retrieve scoped data.

**Arguments:**
```json
{
  "token": "<signed-jwt>",
  "action": {
    "type": "query_obligations",
    "filters": {"supplier": "<de-vendor-corp>", "period": "2026-04"}
  }
}
```

**Returns (success):**
```json
{
  "data": [ /* array of typed entities filtered to scope */ ],
  "consumed_at": "2026-05-06T10:43:15Z",
  "audit_event_id": "<l0-entity-id>"
}
```

**Returns (failure):**
```json
{
  "error": "<error-code>",
  "reason_text": "<explanation>"
}
```

Standard error codes: `token_expired`, `token_consumed`, `token_revoked`, `signature_invalid`, `scope_violation`, `audience_mismatch`.

#### 5.2.3. `hpi.revoke_token`

Substrate-holder revokes an active token.

**Arguments:**
```json
{
  "jti": "<token-id>",
  "reason": "user-initiated",
  "issuer_signature": "<signed-revocation-attestation>"
}
```

**Returns:**
```json
{
  "revoked_at": "2026-05-06T11:55:00Z",
  "audit_event_id": "<l0-entity-id>"
}
```

The revocation MUST be propagated to the runtime's revocation list (§4.6.1) within 5 seconds (RECOMMENDED) or 60 seconds (REQUIRED).

#### 5.2.4. `hpi.audit_query`

Substrate-holder queries their own audit trail. This method is restricted to the substrate-holder's authenticated session — agents cannot call it.

**Arguments:**
```json
{
  "filters": {
    "since": "2026-05-01T00:00:00Z",
    "agent_did": "did:agent:<id>",
    "purpose": "reconcile-supplier-statement",
    "event_types": ["hpi_token_consumed"]
  },
  "limit": 100
}
```

**Returns:**
```json
{
  "events": [
    {
      "id": "<l0-entity-id>",
      "type": "hpi_token_consumed",
      "timestamp": "2026-05-06T10:43:15Z",
      "fields": { /* event-type-specific */ }
    }
  ],
  "next_cursor": "<opaque>"
}
```

#### 5.2.5. Optional: `hpi.discover`

Returns runtime capabilities, supported axiom families, supported v-spec versions. Useful for agents adapting to runtime variants.

### 5.3. Discovery

A substrate-holder publishes a discovery document at a well-known URL:

```
GET https://<holder-domain>/.well-known/hpi.json
{
  "version": "0",
  "issuer": "did:web:<holder-domain>",
  "runtime_endpoint": "https://hpi.<holder-domain>/v0",
  "transport": ["mcp", "http+json"],
  "supported_axiom_families": ["OBL", "RCG", "TRU", "PAT"],
  "key_endpoint": "https://<holder-domain>/.well-known/jwks.json",
  "revocation_endpoint": "https://hpi.<holder-domain>/.well-known/hpi/revocations.json"
}
```

This pattern is borrowed from OAuth 2.0 well-known endpoints (RFC 8414) and OpenID Connect Discovery. It allows agents to bootstrap with a single domain name and discover everything else.

**Self-hosted holders** publish their own well-known URL on a domain they control.

**Hosted holders** (using a managed HPI runtime provider, e.g., a future Stripe-of-substrate company) point their well-known URL at the provider's runtime, but the issuer DID and signing keys remain under the holder's control. This is the structural analog of self-custody crypto wallets running on hosted infrastructure — the keys never leave the holder.

### 5.4. Storage interface (non-normative)

The protocol does NOT prescribe a storage backing. Implementations choose. For interop, implementations SHOULD document the storage interface they expose so adjacent implementations can swap.

**Recommended storage shapes:**

- **L0 blob store** — content-addressed, append-only, immutable. Reference implementations: filesystem with content-hash naming, S3-compatible object storage, IPFS, Plurality OCL vault, Solid pod, Supabase Storage.
- **L1+ typed store** — structured, queryable, RLS-gated. Reference implementations: Postgres+JSONB, sqlite, MotherDuck, IPLD.
- **Audit log** — append-only L0 stream specific to HPI events. SHOULD use the same L0 blob store as the rest of the substrate, tagged with a stable type (`hpi_audit_event`) for downstream extraction.

**Storage MUST be at-rest-encrypted with keys controlled by the substrate-holder.** Implementations MAY support hosted offerings where the runtime provider operates the storage, but the encryption keys MUST NOT be accessible to the runtime provider. This is the structural constraint that distinguishes HPI from platform-memory: a hosted HPI runtime has zero ability to read the substrate it stores. Without this constraint, the architecture collapses back into a platform-memory pattern.

### 5.5. Token signing keys

Tokens are signed by the substrate-holder's signing key. Standard key management:

- **Active key** — current signing key, published in the holder's JWKS endpoint
- **Rotation policy** — recommended 90-day rotation; old keys remain in JWKS for verification of in-flight tokens but are not used for new signing
- **Compromise recovery** — if a key is compromised, the holder publishes a revocation of all tokens issued by that key, then rotates. Tokens already consumed are not affected (the audit trail records what happened); tokens not yet consumed become invalid.

**Key custody in v0:** the substrate-holder's runtime holds the key. v0.1 will introduce options for split-key custody (HSM, threshold signatures, hardware tokens via WebAuthn).

### 5.6. Versioning

The wire format is versioned via the `version` field in tokens and discovery documents. This document specifies version `"0"`. Backwards-incompatible changes increment the version. Forward-compatible additions (new axiom families, new method options) are non-breaking and do not increment.

Implementations SHOULD support multiple versions side-by-side during transitions; agents and runtimes negotiate the highest mutually-supported version per session.

---

## 6. Reference Implementation Pointers

A specification without working code is theology. This section names the closest existing implementations of HPI's components as of 2026-05-06, identifies the gaps between them and a complete HPI runtime, and specifies the minimum target for a v0.1 reference implementation.

### 6.1. Existing implementations that satisfy parts of HPI

**Brain MCP** (Mordechai Potash, 2024–present)
- ~400K-message indexed personal corpus, semantically searchable via 82K embeddings
- MCP server exposing the corpus to Claude Code and other MCP-compatible agents
- Implements: L0 blob storage (filesystem-backed), L1 extraction (per-conversation summaries), L2 semantic search, audit logging
- Does NOT yet implement: HPI token issuance/consumption, scoped agent borrowing, cite-or-die enforcement at the API surface

**Viter L0→L3 pipeline** (Mordechai Potash + Shaul Levine, 2026-04–present)
- Three substrate streams (chat-log, whatsapp, transcripts) each with deterministic L1 extraction (Python scripts) and LLM-driven L2 synthesis
- L3 cross-stream fusion via daily-rebuild hook (`SessionEnd → rebuild-pipeline.sh`)
- Implements: full L0–L3 layering with cite-or-die discipline, intertemporal collapse mechanism via `_now.md` regeneration
- Does NOT yet implement: token-mediated agent access, multi-substrate boundary handoff

**Persofi reconciliation** (financial-vertical product on Viter platform, 2026-04–present)
- Working axiom-typed OBL/RCG/TRU/PAT data on one pilot client's books
- Implements: typed L1 evidence extraction, L2 obligation projection per the OBL family, partial RCG margin attribution
- Does NOT yet implement: PAT lifecycle, full TRU scoring, HPI token surface

### 6.2. Gap analysis: what these implementations don't yet do

| HPI requirement | Brain MCP | Viter L0–L3 | Persofi |
|---|---|---|---|
| L0 immutable storage | ✅ | ✅ | ✅ |
| L1 deterministic extraction | ✅ | ✅ | ✅ |
| L2 attributed synthesis | ⚠️ partial | ✅ | ✅ |
| L3 personal surface | ⚠️ via search | ✅ | ❌ |
| Typed axiom grammar | ❌ | ❌ | ✅ |
| HPI token issuance | ❌ | ❌ | ❌ |
| HPI token consumption | ❌ | ❌ | ❌ |
| Audit trail as L0 stream | ⚠️ partial | ⚠️ partial | ❌ |
| Cross-substrate boundary collapse | ❌ | ❌ | ❌ |
| Agent never owns L3 | ✅ enforced by architecture | ✅ enforced by architecture | N/A |

The existence proof: every individual HPI requirement has been met by some part of one of these implementations. No single implementation meets all requirements simultaneously. **The gap is integration, not invention.**

### 6.3. Minimum v0.1 reference implementation target

A v0.1 reference HPI runtime SHOULD provide:

1. **Token issuance + verification** — JWT issue/verify with the v0 claim shape from §4.2; signing key management; `jti` consumption tracking; revocation list publication.
2. **MCP method surface** — the four required methods from §5.2 exposed as MCP tools.
3. **One axiom family end-to-end** — OBL is the recommended starting family because it has full v0 documentation, a worked example, and existing Persofi production data. Any third-party reference can use synthetic obligations.
4. **L0 blob store backing** — filesystem reference; documented interface so alternative backings (S3, OCL, IPFS, Solid) drop in.
5. **Audit log as L0 stream** — emit `hpi_*` events back into the substrate's L0 store.
6. **Discovery document** — `.well-known/hpi.json` served from a configurable domain.

**Estimated build cost:** ~80–120 hours for a single experienced engineer to ship a functional v0.1 reference covering all six requirements. ~30 hours if reusing Brain MCP's MCP server scaffolding.

**Languages:** Python or TypeScript recommended. Both have mature MCP server libraries, JOSE/JWT libraries, and JSON Schema validators.

### 6.4. Conformance criteria

An implementation is **HPI v0-conformant** if it:
- Exposes the four required methods from §5.2 with matching JSON shapes
- Issues tokens matching the v0 claim shape from §4.2
- Honors single-use semantics for tokens with `single_use: true`
- Publishes a revocation list at the `/.well-known/hpi/revocations.json` endpoint
- Emits audit events to the substrate-holder's L0 store on every token lifecycle event
- Refuses scope-violating consumption requests
- Does NOT retain plaintext L1+ content outside the substrate-holder's encrypted store
- **v0.1: Validates axiom assertions** by resolving every `cites` field against the substrate's L0 store before accepting an L1+ entity. Assertions whose citation chain does not resolve MUST be rejected. (Converts cite-or-die from procedural to structural.)

A conformance test suite is scope for v0.1. Self-attestation is acceptable for v0.

### 6.5. The microHPI compactness target

**Aspirational constraint for the v0.1 reference implementation:** the smallest possible HPI runtime that demonstrates the protocol end-to-end SHOULD fit in a single readable file (Python or TypeScript, ≤500 lines, dependency-light).

This is borrowed from Karpathy's `microgpt` aesthetic — *"This file contains the full algorithmic content of what is needed... I cannot simplify this any further."* — and applied to protocol implementations. The microHPI reference is a teaching artifact and a complexity floor: if the protocol cannot be implemented in 500 readable lines, the spec has scope creep.

The microHPI reference is NOT the production reference (full v0.1 will likely be 2000-5000 lines with proper error handling, logging, observability). But the existence of a 500-line readable implementation is a forcing function on spec parsimony.

(Aesthetic credited to Andrej Karpathy via simulated review of HPI v0, 2026-05-06.)

---

## 7. Non-Goals & Anti-Patterns

HPI is constrained by what it deliberately refuses to be. This section names the constraints; agents reading this spec should infer that adjacent problems are out of scope and adjacent solutions are not endorsed.

### 7.1. HPI is NOT a model

LLMs remain LLMs. HPI does not constrain model architecture, training data, fine-tuning practices, or inference behavior. It constrains what data the model has access to during a transaction and what records of that access accrue afterwards. Any model — open-weights or hosted — can operate under HPI as long as the implementation surrounding the model honors the token semantics and audit requirements.

### 7.2. HPI is NOT a memory product

Letta, Mem0, Khoj, Pieces, and Rewind solve agent memory architecture. HPI specifies the access-control protocol governing what context an agent may read from a substrate-holder's substrate, with what scope and audit. **These layers compose**: an HPI-compliant agent may use any memory architecture inside its borrowed scope, including stateful-agent architectures with cross-session persistence in the agent's own runtime (subject to the access constraints when re-crossing substrate boundaries — see §4.11).

Letta and HPI are not subordinate to each other. They are complementary architectures operating at different layers — HPI as the kernel that mediates substrate access, stateful-agent architectures as the processes that operate within the borrowed scope (see §4.1.3 and `comparisons/LETTA.md`).

### 7.3. HPI is NOT a wallet

No native token. No cryptocurrency. No token economics. The "tokens" in HPI are JWT-style or VC-style access credentials — short-lived, single-use, revocable. They have no on-chain representation, no transferability, no market value. Implementations using blockchain primitives (DIDs anchored to chains, content-addressed storage on IPFS) are permitted but not required.

### 7.4. HPI is NOT blockchain-required

Implementations may use Web3 primitives (Ceramic, IPFS, ENS, Solid) or pure HTTP+JWT+filesystem. The protocol is silent on storage backing. Implementations choosing Web3 backings inherit Web3's tradeoffs (latency, finality, key management); implementations choosing centralized HTTP backings inherit those tradeoffs (host availability, key custody). HPI's conformance requirements are agnostic to either choice.

### 7.5. HPI is NOT anti-LLM

LLMs are extraordinarily useful. HPI's whole point is to enable agents (LLM-powered or otherwise) acting on the user's behalf with appropriate access controls. The constraint is on substrate ownership, not on AI utility. An HPI-compliant LLM-based agent has full access to the human's substrate via tokens; the human retains the ability to revoke that access at any time and audit what the agent did with it.

### 7.6. HPI is NOT anti-platform

A platform CAN be HPI-compliant. Doing so requires:
- The platform issues tokens against the user's substrate, not the platform's own user-context store
- The platform emits audit events to the user's substrate, not the platform's logs
- The platform's encryption keys for storing user data are user-controlled, not platform-controlled
- The platform's terms of service do NOT claim ownership of accumulated user context

A platform that meets these constraints can offer HPI-compliant memory, personalization, and agentic features. The constraint kills certain monetization patterns (selling aggregated user data, training on accumulated context without consent) but doesn't kill the product.

### 7.7. Anti-pattern: hosted runtime with vendor-held keys

The most subtle failure mode is a hosted HPI runtime where the runtime provider holds the encryption keys to the substrate. This re-creates platform-memory under the cosmetic appearance of sovereignty: the user appears to own their substrate, but the runtime provider can read it.

HPI v0 forbids this pattern. Hosted runtimes MUST be technically equivalent to self-hosting from a sovereignty standpoint — encryption keys held by the user (HSM, hardware token, password-derived key, key-shard recovery), runtime operating only on encrypted blobs and short-lived in-memory plaintext.

### 7.8. Anti-pattern: mixing axioms across substrate boundaries without re-validation

When axiom-typed L0 entities cross substrate boundaries, the receiving substrate MUST treat them as new L0 entities subject to the receiver's own validation rules. Inheriting trust ("this OBL was validated in Mordechai's substrate, so I'll trust it") is not permitted by default. The receiving substrate's TRU axiom assigns trust to the sender; high-trust senders can have their axioms accepted with lighter validation, but the validation step is not skippable.

### 7.9. Anti-pattern: silent agent persistence

An agent that retains user-derived state across transactions WITHOUT writing audit events to the substrate violates the spec, even if the retention is "innocent" (e.g., conversational context for a follow-up turn). All cross-transaction state MUST be either: (a) explicitly scoped via a long-lived token, with corresponding audit events, or (b) discarded between transactions. There is no third option.

---

## 8. Open Questions for the Community

This section enumerates issues that v0 leaves intentionally open, in RFC-style format. Implementers and reviewers are invited to engage with these questions; positions taken here will inform v0.1.

### 8.1. Axiom family naming and count

The v0 axiom families (OBL, RCG, TRU, PAT) are drawn from one vertical (financial operations with patent-prosecution focus) because that's where existing production code lives. Are these names broadly applicable to other domains, or vertical-specific?

- **OBL** generalizes well — obligations exist in healthcare (treatment plans), legal (contracts), software (commitments in code reviews), academic (paper-citation obligations).
- **RCG** as "recharges" is finance-specific; as "recognitions / renewals" it generalizes to attestations, periodic review.
- **TRU** generalizes — trust is universal.
- **PAT** as "patents" is IP-specific; as "patterns" it might generalize to recurring artifacts in any domain.

**Question for community:** rename PAT and possibly RCG for cross-vertical legibility, or keep finance-specific names with a clear convention that other verticals add their own families (e.g., MED-* for medical, LEG-* for legal)?

### 8.2. Token format: JWT vs W3C Verifiable Credentials

v0 specifies signed JWT. v0.1 path to W3C VC is sketched but not committed. JWT is universally implementable today; VC adds cryptographic provenance for third-party audit without contacting issuer.

**Question for community:** is JWT sufficient long-term, or should v1.0 mandate VC? Tradeoff: VC tooling is less mature in 2026 but better-aligned with the substrate-conservation thesis (third-party-auditable provenance maps cleanly onto cross-substrate citation chains).

### 8.3. Transport: MCP-only vs HPI-native RPC

v0 extends Anthropic MCP. Pros: existing tool ecosystem, no new RPC to specify. Cons: MCP is Anthropic-controlled (though Apache 2.0); evolution of MCP is not under HPI control; an HPI-native RPC could optimize for HPI-specific patterns.

**Question for community:** in v1.0, should HPI define its own RPC layer, or remain an MCP extension? The protocol-vs-platform tradeoff matters: an MCP-extension HPI inherits MCP's adoption but also its constraints; an HPI-native RPC owns its evolution but loses interop with the broader MCP tool ecosystem.

### 8.4. Composition with existing open standards

HPI builds on multiple precedents but doesn't yet specify integration patterns:

- **OAuth 2.1 / OIDC** — how does an OAuth-authenticated session originate an HPI token? The natural composition is OAuth authenticates the substrate-holder; HPI tokens are then issued under their authority.
- **AT Protocol** (Bluesky's social-graph protocol) — both protocols treat the user's data as user-owned. AT Protocol is social-graph-shaped; HPI is cognitive-substrate-shaped. Composition: AT Protocol's `did:plc` identifiers as HPI substrate-holder DIDs.
- **Solid** — Solid pods are L0 blob stores. An HPI implementation backed by Solid is a clean composition.
- **Plurality OCL** — context vaults as L0 backing. Most active integration target. See `outreach/PLURALITY.md`.
- **W3C VC/DID** — for v0.1 token format upgrade.

**Question for community:** which of these compositions is highest-priority for v0.1? The answer probably depends on which adjacent ecosystem ships interesting HPI use cases first.

### 8.5. Agent-to-agent delegation semantics

§4.8 specifies three modes (forbid / attenuate / re-request). v0 only requires `forbid`. v0.1 adds attenuation (macaroon-style) and re-request flows. The unresolved question: when delegation chains span multiple substrate-holders (Alice's agent invokes Bob's agent), how does the audit trail compose? Each holder needs to see their own slice; cross-substrate correlation requires a shared identifier scheme.

**Question for community:** is there prior art (capability-based security literature, distributed-systems audit research) that solves cross-substrate audit composition cleanly?

### 8.6. Migration from hyperscaler-stored memory

Users with accumulated context in OpenAI Memory, Google Gemini personalization, or Anthropic Projects need a migration path to HPI substrate. The platforms are unlikely to provide structured exports; the migration is closer to "ingestion of unstructured memory dumps" than "schema migration."

**Question for community:** what does an "HPI ingestion bridge" look like for hyperscaler-stored memory? Is there a use case where HPI-storage + hyperscaler-memory coexist (the user's substrate has L0 entities representing the hyperscaler memory, with `creator: did:web:openai.com` provenance), or does the architecture require a clean break?

### 8.7. The hard naming question

"HPI" is the working brand. Subtitle is currently "Hyperpersonalized API." Alternative subtitle considered: "Sovereign Cognitive Substrate Protocol."

**Question for community:** does HPI as an acronym still resonate when the protocol matures? Or should the brand evolve toward a more self-explanatory name? Past protocol naming examples: SMTP (Simple Mail Transfer Protocol — operationally descriptive), OAuth (Open Authorization — clear), MCP (Model Context Protocol — recent and clear). HPI as "Hyperpersonalized API" is suggestive but less self-explanatory.

### 8.8. The trillion-dollar question

If HPI succeeds as a category, the value distributes across an ecosystem (hosted runtime providers, axiom-family libraries, agent platforms). No single entity captures $1T from this protocol — the same pattern as SMTP or HTTP. But the category at scale is plausibly $1T+ in transaction value passing through HPI-typed boundaries.

**Question for community:** what governance model best preserves protocol neutrality at scale? A foundation (Mozilla, Linux Foundation, Apache Software Foundation precedents)? A consortium (W3C model)? A pure RFC process? The decision affects long-term incentive alignment of HPI-compliant infrastructure providers.

### 8.9. Value-capture pattern: which positions are defensible?

Karp's predicted critique (simulated review, 2026-05-06): *"You've built the infrastructure of a great open-source project. There is no enterprise procurement story. Without it, HPI is a research contribution."* The critique applies to most successful open protocols at v0; SMTP/HTTP/OAuth all faced the same gap and survived because rent was captured around the protocol, not on it.

**Question for community:** which positions in the HPI ecosystem are defensible against hyperscaler absorption?

Candidate positions to evaluate:
- **Hosted runtime provider** (Stripe-of-substrate model) — captures per-transaction or subscription rent on token issuance + storage. Vulnerable to hyperscaler in-house equivalents.
- **Axiom-family library curator** (Linux-distro model) — captures consulting + support on domain-specific Ontologies. Niche but defensible if domain expertise is real.
- **HPI-compliant agent marketplace** (App Store model) — captures intermediation fees. Tends toward winner-take-most.
- **Enterprise gateway product** (Okta-of-substrate model) — captures licensing for institutional substrate-holder deployments. Defensible if compliance/audit features mature.
- **Standards body / foundation** (Linux Foundation model) — captures membership dues, no per-transaction rent. Sustains the protocol but doesn't make anyone rich.

The author's working assumption: the right position from his own seat is to be the **protocol designer + first reference implementor + axiom-family curator for one vertical** (Persofi as the demonstration), with subsequent revenue from consulting/expansion. Other positions emerge as the ecosystem develops. Open for discussion.

### 8.10. Empirical comparison: agent capability under sovereign vs platform-memory architectures

Wooders' predicted critique (simulated review, 2026-05-06): *"What does the data say about agent quality over a 30-day interaction under HPI's stateless borrowing model versus a stateful model? You're making an architectural claim about substrate ownership; if the architectural claim has cost in agent capability, that cost needs to be measured."*

**Question for community:** does HPI-mediated agent access produce measurably worse agent outcomes than unmediated platform memory? If so, by how much, on which task classes, and is the cost justified by the sovereignty gain?

v0 makes architectural claims without empirical comparison. Letta has LoCoMo + LongMemEval results; HPI has none. The empirical study is research scope, possibly v1.0 or post-v1.0. Acknowledged as a gap worth addressing.

---

## 9. Acknowledgements & Lineage

HPI is not a clean-room invention. It synthesizes precedents from multiple traditions; honest acknowledgement of those precedents is itself a substrate-conservation discipline (cite-or-die at the meta-level).

**Solid (Tim Berners-Lee, W3C, 2015–present)** — the personal-data-pod precedent. Solid established the position that user data should be user-owned and accessed via user-issued permissions. HPI adopts this stance and extends it from data to cognitive substrate, adding the layer model and typed axiom grammar that Solid omits.

**Anthropic Model Context Protocol (Anthropic, 2024–present)** — the transport HPI extends. MCP is the JSON-RPC envelope that lets HPI methods be discovered as tools by any MCP-compatible agent. Anthropic published MCP as Apache 2.0 in November 2024; without that openness, HPI would have to define its own transport.

**Plurality / Open Context Layer (2025–present)** — fellow-traveler at the storage substrate layer. OCL provides user-owned encrypted vaults with MCP-native access; HPI specifies the typed grammar and access protocol that runs on top of such vaults. Identified as ally not competitor in early 2026; outreach in `outreach/PLURALITY.md`.

**Letta / MemGPT (UC Berkeley Sky Computing Lab, 2023–present)** — directionally aligned on principled agent-context management. Letta's Context Constitution (April 2 2026) is the most architecturally serious document in agent-context space. HPI inverts Letta's axiom (agents own context → agents borrow context) but adopts Letta's seriousness about typed context management. Comparison in `comparisons/LETTA.md`.

**W3C Verifiable Credentials and Decentralized Identifiers (W3C, 2017–present)** — cryptographic primitives for v0.1 token issuance. SpruceID, Veramo, and the broader VC/DID community provide the toolchain HPI will adopt for cryptographically-provable provenance.

**OAuth 2.1 / capability-based security (IETF, 2012–present; Birgisson et al. macaroons, 2014; Biscuits at CleverCloud, 2019)** — scoped access patterns. HPI's token model is a cousin of OAuth 2.1's scope mechanism, with single-use semantics borrowed from short-lived access-token patterns and delegation semantics borrowed from macaroons.

**Torah sourceability discipline (*l'havdel elef avdal*)** — the cite-or-die rule's intellectual lineage. The Talmudic discipline that every claim must be sourced to its origin (passuk → Mishnah → Gemara → Rishonim → Achronim) is the structural ancestor of HPI's layer-citation rule. Crediting this lineage honestly is unusual for a protocol document and is intentional. The architectural discipline of strict sourceability is not invented by Western computer science; it has a 2000-year-old engineering tradition that HPI consciously inherits.

**Brain MCP and Viter L0→L3 pipeline (Mordechai Potash + Shaul Levine, 2024–present)** — the working implementations from which HPI's specification is extracted. Without Brain MCP's existence as a personal cognitive prosthetic, HPI's claims about substrate-as-prosthetic would be theoretical. Without Viter's L0→L3 pipeline running in production, HPI's layering rules would be untested.

**The substrate conservation insight (Mordechai Potash, 2026-05-06)** — the specific articulation that "L3 published across a substrate boundary becomes the next holder's L0" is the load-bearing novel claim of this spec. Prior precedents articulate user-data ownership and citation chains separately; the conservation law that unifies them across both interpersonal and intertemporal substrate boundaries is, to the editor's knowledge, unique to this document.

This document stands on the shoulders of all of the above. Where it adds something new, it is the unification — not the components.

---

## Appendix A — JSON Schemas (v0.1 scope)

Per-family JSON Schema 2020-12 documents. Not in v0.

## Appendix B — Reference flow diagrams (v0.1 scope)

Mermaid sequence diagrams for token issuance, consumption, revocation. Not in v0.

## Appendix C — Interop Notes (v0.1 scope)

Concrete how-to for layering HPI over MCP, OAuth, Plurality OCL, Solid pods. Not in v0.
