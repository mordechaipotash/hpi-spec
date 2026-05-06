# HPI Specification — v0 draft

> **Hyperpersonalized API. A protocol for sovereign cognitive substrate.**

**Status:** v0 draft. Sections 2 and 3 are full draft; Sections 1, 4–9 are outlines awaiting expansion.
**Last updated:** 2026-05-06
**Editor:** Mordechai Potash

---

## 1. Foundations & Problem Statement

*[OUTLINE — to be expanded. ~800 words target.]*

The default trajectory of 2026 places user cognitive context inside hyperscaler infrastructure. The platform's incentive (lock-in, monetization) is opposed to the user's interest (sovereignty, portability, agency). HPI is the protocol-level alternative.

Must cover:
- The hyperscaler-context-capture trajectory (OpenAI Memory, Google Gemini personalization, Anthropic memory beta)
- The alignment claim: the layer should not lie with the alignment of corporate profit
- Why open protocols beat walled gardens at scale (SMTP, HTTP, OAuth, TCP/IP precedents)
- What HPI is NOT (model, memory product, wallet, crypto-required, anti-LLM)
- What HPI IS

---

## 2. The Substrate Model (L0–L3)

### 2.1. Axiom 1 — L0 is the substrate boundary

**L0 is the most-raw digital copy held at the substrate's boundary.**

A *substrate* is the cognitive surface of a holder — a human, an organization, or (with the constraints of §4) an agent acting on behalf of one. The substrate has a boundary: everything inside the boundary is the substrate's information.

L0 is whatever sits at that boundary — the most-raw digital artifact the holder has, however backed.

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

| Family | Domain | File |
|---|---|---|
| **OBL** | Obligations: contracts, evidence, identity | [`axioms/OBL-obligations.md`](axioms/OBL-obligations.md) |
| **RCG** | Recharges: trust-based renewal, margin attribution | [`axioms/RCG-recharges.md`](axioms/RCG-recharges.md) |
| **TRU** | Trust: counterparty ratings, thresholds, scopes | [`axioms/TRU-trust.md`](axioms/TRU-trust.md) |
| **PAT** | Patents: long-lived legal entity lifecycle | [`axioms/PAT-patents.md`](axioms/PAT-patents.md) |

The four families are **not exhaustive of the protocol's reach.** They are v0 — drawn from one vertical (financial operations with patent-prosecution focus) because that vertical has working production code and traceable derivations. Other verticals (healthcare records, legal discovery, software engineering, scientific publication) will require their own axiom families. The framework in §3.3 is the universal part; the families are vertical instantiations.

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

---

## 4. The Token Handoff Protocol

The HPI access-control primitive. Defines how an agent obtains scoped, time-bounded, revocable, audited permission to read a human's L1+ context for a single transaction.

### 4.1. The access axiom

> **An agent MUST NEVER own its own L3. An agent MAY only borrow scoped views of a human's substrate via permissioned, time-bounded, single-use tokens.**

Stated as a structural constraint:

- An agent's working memory across one transaction is its own (operational state, intermediate computation).
- An agent's persistent state across transactions is **not its own**. Any persistence is achieved by writing back to the human's substrate (with explicit permission) or by re-borrowing on the next transaction.
- "Identity," "personality," or "experience" of an agent are projections of the human's substrate, durable only as long as the human renews the projection. They are not properties of the agent.

This is the inverse of agent-centric architectures (e.g., Letta's Context Constitution, which holds that *"agents own their context"* and assigns agents "Three Pillars of Selfhood: Identity, Memory, Continuity"). HPI is human-centric by axiom; agent-centric architectures are coherent but build a different future. See `comparisons/LETTA.md` for the architectural diff.

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

---

## 5. Wire Format & Transport

*[OUTLINE — to be expanded. ~700 words target.]*

HPI extends Anthropic MCP. Methods: `hpi.request_context`, `hpi.consume_token`, `hpi.revoke_token`, `hpi.audit_query`. Discovery via `/.well-known/hpi.json`. Storage interface: implementation-agnostic L0 blob store + L1+ typed store.

---

## 6. Reference Implementation Pointers

*[OUTLINE — to be expanded. ~400 words target.]*

Closest existing working implementation as of 2026-05-06: Mordechai's Brain MCP (377K-message corpus) + Viter L0–L3 pipeline (chat-log + WhatsApp + transcripts → daily L1/L2/L3 with cite-or-die discipline) + Persofi reconciliation (working axiom-typed OBL/RCG/TRU/PAT data on <client-corp>'s books). These are the existence proofs.

Minimum reference implementation v0.1 target: Python or TypeScript module that issues + verifies tokens, exposes MCP-compatible API, demonstrates one full axiom family (OBL).

---

## 7. Non-Goals & Anti-Patterns

*[OUTLINE — to be expanded. ~400 words target. See `README.md` "What HPI is not" for v0 list.]*

---

## 8. Open Questions for the Community

*[OUTLINE — to be expanded. ~500 words target.]*

RFC-style discussion items: protocol naming (HPI confirmed as brand), axiom family naming + count, token format (JWT vs W3C VC), transport (MCP-only vs HPI-native), composition with existing protocols (OAuth, AT Protocol, Solid, OCL), agent-to-agent delegation, hyperscaler-memory migration path.

---

## 9. Acknowledgements & Lineage

*[OUTLINE — to be expanded. ~200 words target. See `README.md` "Conceptual lineage".]*

---

## Appendix A — JSON Schemas (v0.1 scope)

Per-family JSON Schema 2020-12 documents. Not in v0.

## Appendix B — Reference flow diagrams (v0.1 scope)

Mermaid sequence diagrams for token issuance, consumption, revocation. Not in v0.

## Appendix C — Interop Notes (v0.1 scope)

Concrete how-to for layering HPI over MCP, OAuth, Plurality OCL, Solid pods. Not in v0.
