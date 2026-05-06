# HPI Threat Model — v0

**Status:** v0 draft. Adversarial threat analysis. Companion to SPEC.md §4 (Token Handoff Protocol) and §4.10 (Failure modes — benign).
**Last updated:** 2026-05-06
**Editor:** Mordechai Potash

---

## Why this exists

HPI v0 specifies cooperative behavior between principals, agents, and runtimes. Cooperation is necessary but not sufficient. Real-world deployment must survive *adversarial* threats: forged tokens, compromised runtimes, malicious principals, colluding platforms, nation-state attackers, supply-chain compromises.

Without an explicit threat model, HPI's trust claims are assertions, not architecture. This document closes that gap.

This is v0 of the threat model. It enumerates adversary classes, attack vectors, what HPI's wire format mitigates structurally, what HPI does NOT mitigate, and residual risks acknowledged as out-of-scope. v0.1 will add formal verification of the most critical paths.

---

## 1. Threat-model scope

**What this document is:**
- An enumeration of adversaries who might attack an HPI deployment
- A mapping from adversary class → attack vectors → mitigation status
- A clear statement of residual risks the protocol does NOT address
- A roadmap for v0.1 hardening

**What this document is NOT:**
- A formal verification (v0.1)
- A pen-test or security audit (requires a working reference impl)
- An information-theoretic privacy analysis (requires differential-privacy framework — v1.0 scope)
- A compliance certification (FedRAMP, SOC2, GDPR — application-specific, downstream of protocol)

---

## 2. Adversary classes

HPI v0 considers six adversary classes, ordered by typical sophistication:

### Class A — Curious Agent

A legitimate agent with a legitimate token attempting to extract more context than its scope authorizes.

**Examples:**
- Agent with `OBL` scope tries to query `RCG` data
- Agent with `L1` scope tries to read `L2` synthesis
- Agent attempts to replay a single-use token after consumption

**Capability:** Can construct arbitrary HPI requests; cannot forge tokens; cannot compromise the runtime.

### Class B — Compromised Agent

A legitimate agent whose runtime has been subverted by a third party (malicious dependency, prompt injection, classical software vulnerability).

**Examples:**
- Agent's container is compromised; attacker exfiltrates the token before consumption
- Agent's prompt is hijacked via injected user input; agent emits unintended HPI requests
- Agent's binary has been modified to log all returned data to attacker-controlled storage

**Capability:** Has all of Class A's capabilities, plus full control of the agent's process state and outbound network.

### Class C — Malicious Principal

The substrate-holder themselves acts adversarially against the agent or against other parties whose data is reflected in the substrate.

**Examples:**
- Substrate-holder constructs poisoned L0 entries to mislead agents
- Substrate-holder issues tokens with deliberately malformed scopes to test agent error-handling
- Substrate-holder exfiltrates third-party data that incidentally lives in their substrate (a meeting recording where another participant is identified)

**Capability:** Full control of their own substrate, including L0 contents and token issuance. Cannot compromise other substrate-holders' substrates.

### Class D — Compromised Runtime

The HPI runtime itself has been subverted. This is the most dangerous benign-architecture failure mode.

**Examples:**
- Runtime provider is compromised; attacker reads tokens at issuance time
- Runtime provider colludes with an agent platform to silently log all consumed scopes
- Runtime provider's signing key is compromised; attacker forges arbitrary tokens against any substrate the runtime serves

**Capability:** Can read any token the runtime issues; can read any data the runtime returns to agents; can forge tokens; cannot directly compromise substrate-holder's local stores (if encryption-at-rest is properly key-isolated).

### Class E — Colluding Platform

A platform provider (LLM model, agent framework, hosted infrastructure) acts in concert with one or more agents to extract substrate content beyond authorized scope.

**Examples:**
- Model platform reads agent prompts containing returned substrate data and stores them for training
- Agent framework caches all consumed scopes in vendor-side memory marketed as "agent improvement"
- Hosted infrastructure provider correlates token-consumption patterns across substrate-holders to build aggregate profiles

**Capability:** Has visibility into agent behavior at the model/framework layer; cannot directly compromise the HPI runtime; can however absorb the data once the agent legitimately reads it.

### Class F — Nation-State Adversary

A nation-state actor with intelligence-grade capability targets HPI infrastructure.

**Examples:**
- Side-channel attacks on HSM-stored signing keys
- Targeted compromise of identity-provider infrastructure (DID resolvers)
- Long-term retention of all token-consumption events for adversary-controlled substrate-holders
- Supply-chain attack on HPI reference implementation

**Capability:** Can perform classical APT operations: zero-days, supply-chain compromise, social engineering, lawful intercept where applicable.

---

## 3. Attack-vector matrix

For each (adversary class, attack vector), HPI v0's mitigation status:

| Vector | Class A | Class B | Class C | Class D | Class E | Class F |
|---|---|---|---|---|---|---|
| Token replay | ✅ MITIGATED (`single_use` + `jti` consumption) | ⚠️ partial — once consumed, attacker holds returned data | N/A | ⚠️ runtime can re-allow if compromised | ⚠️ partial | ❌ depends on runtime integrity |
| Token forgery | ✅ MITIGATED (signature verification) | ✅ MITIGATED | N/A | ❌ NOT MITIGATED (compromised key) | ✅ MITIGATED | ❌ NOT MITIGATED (key compromise) |
| Scope expansion | ✅ MITIGATED (runtime enforces scope at consumption) | ❌ NOT MITIGATED (data already returned to agent) | N/A | ❌ NOT MITIGATED (compromised runtime can return more than scope) | ⚠️ depends on agent integrity | ❌ NOT MITIGATED |
| Audit-trail tampering | ✅ MITIGATED (audit emitted to substrate-holder's L0 stream) | ⚠️ partial — agent can lie about its consumption pattern, but runtime's audit is authoritative | ⚠️ substrate-holder can edit their own audit (this is by design — they own it) | ❌ NOT MITIGATED (compromised runtime can withhold or fabricate audit events) | ❌ NOT MITIGATED if runtime cooperates with platform | ❌ NOT MITIGATED |
| Substrate exfiltration via legitimate scope | N/A | ⚠️ this is the central failure mode of Class B | N/A | ⚠️ partial | ⚠️ central failure mode of Class E | ❌ NOT MITIGATED |
| Cross-substrate correlation | N/A | N/A | N/A | ⚠️ runtime sees patterns | ❌ NOT MITIGATED — central Class E threat | ❌ NOT MITIGATED |
| Supply-chain compromise of reference impl | N/A | N/A | N/A | ⚠️ if runtime uses compromised impl | N/A | ❌ NOT MITIGATED — out of scope for protocol |
| Side-channel on signing keys | N/A | N/A | N/A | ⚠️ depends on key custody | N/A | ❌ NOT MITIGATED — out of scope for protocol; HSM mitigates |

Reading the matrix: HPI v0 substantively mitigates Class A (curious agent) attacks. It partially mitigates Class B (compromised agent) attacks via single-use semantics + audit trail. It does NOT meaningfully mitigate Classes D, E, F via the wire format alone. Mitigations for those classes require key-custody discipline, runtime attestation, and supply-chain controls — all of which are out-of-scope for the protocol layer.

---

## 4. What HPI v0 mitigates structurally

These are the protocol-level defenses, in order of strength:

### 4.1. Single-use tokens with `jti` consumption tracking

A consumed `jti` cannot be re-presented. This bounds the damage of a stolen token to one consumption event. The audit trail records both issuance and consumption; replay attempts after consumption are detected and refused.

**Strength:** Strong against Class A and B. Moderate against Class D (compromised runtime can mark tokens as un-consumed).

### 4.2. Cryptographic scope enforcement at consumption

A token's `scope` field is a signed claim about what the agent may access. The runtime MUST refuse consumption requests whose action exceeds scope. The signature prevents the agent from modifying the scope.

**Strength:** Strong against Class A. Moderate against Class B (the agent already has the token; the question is what data has been returned). Weak against Class D (compromised runtime can override scope enforcement).

### 4.3. Revocation lists with mandatory checks

`/.well-known/hpi/revocations.json` published by each issuer. Agents MUST check before consuming if elapsed time since `iat` exceeds 60 seconds. The substrate-holder can revoke any active token.

**Strength:** Strong against Class A and Class B (revocation arrests further damage). Moderate against Class D (compromised runtime can hide its own revocations from the published list — but this leaves an audit gap).

### 4.4. Audit trail in substrate-holder's L0 stream

Every token issuance, consumption, denial, and revocation is recorded as an L0 entity in the substrate-holder's substrate. The audit is sovereign-side, not runtime-side. The substrate-holder owns their own audit, full stop.

**Strength:** Strong against most classes — the audit cannot be silently rewritten by a compromised runtime if the substrate-holder is monitoring their own audit stream. Weak only against Class D when the substrate-holder is unaware of compromise.

### 4.5. Cite-or-die discipline at the layer-citation level

Every L1+ claim cites a chain back to L0. A compromised L1+ entity that fabricates content has a citation chain that can be verified by re-running the deterministic L1 extractor. Inconsistencies are detectable via re-derivation.

**Strength:** Moderate. Provides post-hoc detection but not real-time prevention.

### 4.6. Two-owner provenance on L0 entities

Every L0 entity names both `creator` (upstream) and `ingester` (substrate-holder). When an L0 entity is presented or cited cross-substrate, the receiver knows who originated and who ingested.

**Strength:** Provides accountability for cross-substrate citations. Weak against Class C (a malicious ingester can lie about creator, but this is detectable via upstream verification when upstream is verifiable).

---

## 5. What HPI v0 does NOT mitigate

These are the gaps that v0 acknowledges and does not pretend to solve:

### 5.1. Compromised runtime (Class D)

A runtime that holds the substrate-holder's signing key and can be subverted is a single point of failure. HPI v0 specifies the wire format but not key custody. Mitigations require:

- HSM-backed signing keys (out of HPI scope; depends on operator)
- Threshold signatures (v0.1 candidate)
- Hardware-token-based custody (WebAuthn-style; v0.1 candidate)
- Independent attestation of runtime integrity (v1.0 scope)

### 5.2. Substrate exfiltration via legitimate scope (Classes B, E)

Once an agent has legitimately read substrate content via a valid token, HPI cannot prevent the agent (or the platform serving the agent) from copying that content elsewhere. The protocol stops at the runtime boundary. Mitigations require:

- Trust in the agent's runtime (out of HPI scope)
- Application-layer DRM (impractical and orthogonal)
- Per-content honeytokens to detect leakage (operator-level mitigation; not protocol)
- Differential-privacy bounds on what can be inferred from any single agent transaction (v1.0 scope; out of v0)

### 5.3. Cross-substrate correlation (Class E, F)

A platform that serves many substrate-holders' agents can correlate token-consumption patterns to build aggregate profiles. HPI's audit trail is per-substrate; cross-substrate correlation happens at the platform layer above HPI. Mitigations require:

- Trust separation at the runtime layer (multi-tenant isolation)
- Tor-style anonymity routing (impractical for low-latency agent operations)
- Mix-net designs (v1.0+ research scope)

### 5.4. Supply-chain attacks on reference implementations (Class F)

HPI v0 specifies the wire format. Reference implementations will exist; their build provenance, dependency hygiene, and signature verification are operator concerns, not protocol concerns. The protocol can require operators to publish SBOMs and attestations, but cannot force the supply chain to be clean.

### 5.5. Side-channel attacks on signing keys (Class F)

Standard cryptographic engineering. Out of HPI scope; well-established practices apply (HSMs, side-channel-resistant primitives, fault injection countermeasures).

### 5.6. The agent's foundation model (Class B, E)

HPI cannot prevent the agent's underlying LLM from hallucinating, lying, or acting against the substrate-holder's interests within the legitimate scope. Stuart Russell's critique applies directly: HPI is information sovereignty, not behavioral alignment. Agents with misaligned objectives can do damage within any legitimate token scope.

### 5.7. Substrate-holder's own bad practice (Class C)

If the substrate-holder approves overly broad scopes (e.g., always grants `L1+L2+L3+all-axiom-families` for `expiry: 30 days`), HPI cannot rescue them. The protocol provides the mechanism; the substrate-holder must use it well. Recommended-practice defaults SHOULD be conservative; implementations MAY warn on suspiciously broad scopes.

---

## 6. Residual risk register

Risks acknowledged as out-of-scope for HPI v0 — addressed via operator practice, future versions, or accepted as inherent tradeoffs:

| # | Risk | Status | Path |
|---|---|---|---|
| R1 | Compromised runtime with vendor-held keys | KNOWN, MITIGATED only by self-custody | v0.1 — add HSM/threshold-sig recommendation; SPEC §7.7 already names this anti-pattern |
| R2 | Substrate exfiltration via legitimate scope | INHERENT — cannot be solved at protocol layer | v1.0 — differential privacy framework |
| R3 | Cross-substrate correlation by colluding platform | INHERENT at platform layer | v1.0+ — mix-net research |
| R4 | Forged tokens via signing-key compromise | KNOWN, MITIGATED only by key custody | v0.1 — HSM + key rotation discipline |
| R5 | Supply-chain attack on reference impl | OPERATOR RESPONSIBILITY | v0.1 — require SBOM publication for reference impls |
| R6 | Misaligned agent within legitimate scope | OUT OF SCOPE — Stuart Russell concern | Document the layering; agent alignment is a separate problem |
| R7 | Substrate-holder approves bad scopes | OPERATOR RESPONSIBILITY | v0.1 — SHOULD-recommendation for conservative defaults; warn on suspicious patterns |
| R8 | Audit trail tampered by substrate-holder's own action | BY DESIGN — they own their audit | Acknowledge; cross-substrate citations rely on creator-ingester two-owner pattern |
| R9 | Long-tail of pointer-rot for external L0 | KNOWN — promoted-to-local-only flag exists | v0.1 — pointer-integrity hierarchy in §2.1 |
| R10 | Quantum cryptanalysis of Ed25519 / ECDSA | INHERENT — known industry threat | v1.0 — post-quantum signatures (NIST PQC) |

---

## 7. v0.1 hardening roadmap

Concrete improvements scoped for the next minor version:

1. **W3C Verifiable Credentials migration path** for token format. Adds cryptographic provenance verifiable without contacting issuer. Mitigates Classes D and F partially via independent verifiability.
2. **HSM/threshold-signature recommendation** for substrate-holder signing keys. Mitigates Class D significantly.
3. **Per-content honeytokens / canary tokens** as an OPTIONAL mechanism for substrate-holders to detect post-consumption leakage by Class B/E.
4. **Conservative scope defaults** in the reference implementation. Warn on broad scopes; suggest minimum-privilege.
5. **Pointer-integrity hierarchy** in §2.1 — formal ranking of pointer reliability (DID > IPFS CID > HTTPS URL > arbitrary identifier).
6. **SBOM + build attestation** mandatory for reference implementation distributions.
7. **Conformance test suite** with adversarial test cases drawn from this threat model. Self-attestation with public test results.

Estimated scope: 30-50 additional pages of spec + ~40 hours of reference impl hardening.

---

## 8. v1.0 research scope

These are not v0.1; they are research questions whose answers may inform v1.0:

- **Differential-privacy bounds on inference attacks via legitimate scope.** Addresses R2.
- **Mix-net or mix-route designs for token-consumption privacy.** Addresses R3.
- **Post-quantum signature suite migration.** Addresses R10.
- **Formal verification of the runtime's scope-enforcement code path.** Addresses Class D partially via attestable correctness.
- **Capability-based delegation (macaroons, biscuits) for sub-agent fan-out.** Addresses scoped delegation more rigorously than re-request model.
- **Privacy-preserving audit log compression** so that substrate-holders can verify audit integrity without retaining full event history.

---

## 9. Acknowledgements

This threat model is influenced by:

- Bruce Schneier's *Data and Goliath* and security-engineering writing — the framing of structural vs cooperative trust
- Ross Anderson's *Security Engineering* — the threat-class taxonomy structure (RIP March 2024)
- The MCP threat-model discussions in Anthropic's MCP RFC process
- The Solid security model (W3C Solid CG)
- The OAuth 2.1 / RFC 9700 security best-current-practice document
- Capability-based-security literature (macaroons — Birgisson et al., 2014; biscuits — CleverCloud)

The simulated peer reviews of HPI v0 by Karp (institutional sovereignty / threat model gap) and Wooders (failure modes / partition behavior) directly informed the structure of this document. The Schneier-shaped critique predicted in the top-10 reviewer research (key custody, threat model rigor) shaped the residual-risk register.

This is v0. It will be wrong in places. The protocol's adoption will surface attack vectors not anticipated here. Updates to this document are part of v0.1 scope.
