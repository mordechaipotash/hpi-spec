# HPI Threat Model — v0

**Status:** v0 draft. Adversarial threat analysis. Companion to SPEC.md §4 (Token Handoff Protocol) and §4.10 (Failure modes — benign).
**Last updated:** 2026-05-06
**Editor:** Mordechai Potash

---

## Why this exists

HPI v0 specifies cooperative behavior between principals, agents, and runtimes. Cooperation is necessary but not sufficient. Real-world deployment must survive *adversarial* threats: forged tokens, compromised runtimes, malicious principals, colluding platforms, nation-state attackers, supply-chain compromises.

Without an explicit threat model, HPI's trust claims are assertions, not architecture. This document closes that gap.

This is v0 of the threat model. It enumerates adversary classes, attack vectors, what HPI's wire format mitigates structurally, what HPI does NOT mitigate, key custody patterns, cryptographic atomicity guarantees, incident response framework, and residual risks. v0.1 will add formal verification of the most critical paths and a published conformance test suite drawn from this analysis.

---

## 1. Threat-model scope

**What this document is:**
- An enumeration of adversaries who might attack an HPI deployment
- A mapping from adversary class → attack vectors → mitigation status
- Concrete key custody patterns the protocol supports
- Cryptographic atomicity analysis for token-consumption operations
- An incident-response framework for HPI deployments
- A clear statement of residual risks the protocol does NOT address
- A roadmap for v0.1 hardening

**What this document is NOT:**
- A formal verification (v0.1)
- A pen-test or security audit (requires a working reference impl)
- An information-theoretic privacy analysis (requires differential-privacy framework — v1.0 scope)
- A compliance certification (FedRAMP, SOC2, GDPR — application-specific, downstream of protocol; see Appendix A for regulatory mapping)

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

### Class G — Coercive Legitimate Operator

The HPI runtime operator, model platform, or institutional intermediary acts within the letter of their permissions while exploiting the substrate-holder's switching costs to extract scope grants the holder would refuse if exit were costless.

This is the *Technology Paternalism* adversary (Christopher Allen, "Dispatches of a Trust Architect: Fighting Technology Paternalism," March 2026): legitimate but coercive. Distinguished from Class E (Colluding Platform) by *legitimacy* — the operator does not violate the wire format; they violate the consent model by structurally narrowing the substrate-holder's ability to refuse.

**Examples:**
- Hosted runtime requires a privacy-policy update granting broader scope as a condition of continued service; refusing terminates the substrate-holder's access to their own substrate ("you can leave, but you leave empty-handed")
- Model provider conditions API access on accepting boilerplate token scopes that exceed minimum-necessary-access for the human's actual use cases
- Institutional employer issues HPI tokens against employee substrate as part of employment terms; refusal jeopardizes employment
- Substrate-holder's family member, business partner, or co-resident leverages social pressure to obtain delegation-token issuance the holder would not grant absent that pressure

**Capability:** Can rewrite operator-side terms of service, adjust default scope templates, condition continued service on consent. Cannot forge tokens or directly compromise substrate-holder keys, but does not need to — the holder grants the scope under structural duress.

**Why HPI v0 cannot fully mitigate Class G:** the wire format cannot distinguish a freely-chosen scope grant from a coerced one. Mitigations are *operational* (anti-coercive design, multi-substrate fallback, regulatory enforcement of minimum-necessary-access) not *cryptographic*. See §5.8 and §7 anti-patterns.

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

Reading the matrix: HPI v0 substantively mitigates Class A (curious agent) attacks. It partially mitigates Class B (compromised agent) attacks via single-use semantics + audit trail. It does NOT meaningfully mitigate Classes D, E, F via the wire format alone. Mitigations for those classes require key-custody discipline (§6), runtime attestation, and supply-chain controls — partly addressed in §6–§8.

---

## 4. What HPI v0 mitigates structurally

These are the protocol-level defenses, in order of strength:

### 4.1. Single-use tokens with `jti` consumption tracking

A consumed `jti` cannot be re-presented. This bounds the damage of a stolen token to one consumption event. The audit trail records both issuance and consumption; replay attempts after consumption are detected and refused.

**Strength:** Strong against Class A and B. Moderate against Class D (compromised runtime can mark tokens as un-consumed).

**See §7.1 for atomicity guarantees on the consumption check.**

### 4.2. Cryptographic scope enforcement at consumption

A token's `scope` field is a signed claim about what the agent may access. The runtime MUST refuse consumption requests whose action exceeds scope. The signature prevents the agent from modifying the scope.

**Strength:** Strong against Class A. Moderate against Class B (the agent already has the token; the question is what data has been returned). Weak against Class D (compromised runtime can override scope enforcement).

### 4.3. Revocation lists with mandatory checks

`/.well-known/hpi/revocations.json` published by each issuer. Agents MUST check before consuming if elapsed time since `iat` exceeds 60 seconds. The substrate-holder can revoke any active token.

**Strength:** Strong against Class A and Class B (revocation arrests further damage). Moderate against Class D (compromised runtime can hide its own revocations from the published list — but this leaves an audit gap).

### 4.4. Audit trail in substrate-holder's L0 stream

Every token issuance, consumption, denial, and revocation is recorded as an L0 entity in the substrate-holder's substrate. The audit is sovereign-side, not runtime-side. The substrate-holder owns their own audit, full stop.

**Strength:** Strong against most classes — the audit cannot be silently rewritten by a compromised runtime if the substrate-holder is monitoring their own audit stream. Weak only against Class D when the substrate-holder is unaware of compromise.

### 4.5. Cite-or-die layer-citation discipline

Every L1+ claim cites a chain back to L0. A compromised L1+ entity that fabricates content has a citation chain that can be verified by re-running the deterministic L1 extractor. Inconsistencies are detectable via re-derivation.

**Note on framing:** This provides **integrity-of-claims** (post-hoc detection of synthesis fabrication), not access control or confidentiality. Real-time prevention of L1+ fabrication is out of scope; the discipline guarantees that any synthesis can be challenged and re-derived.

**Strength:** Moderate. Provides post-hoc detection but not real-time prevention.

### 4.6. Two-owner provenance on L0 entities

Every L0 entity names both `creator` (upstream) and `ingester` (substrate-holder). When an L0 entity is presented or cited cross-substrate, the receiver knows who originated and who ingested.

**Strength:** Provides accountability for cross-substrate citations. Weak against Class C (a malicious ingester can lie about creator, but this is detectable via upstream verification when upstream is verifiable).

---

## 5. What HPI v0 does NOT mitigate

These are the gaps that v0 acknowledges and does not pretend to solve:

### 5.1. Compromised runtime (Class D)

A runtime that holds the substrate-holder's signing key and can be subverted is a single point of failure. HPI v0 specifies the wire format but not key custody. Mitigations require:

- HSM-backed signing keys (see §6.2)
- Threshold signatures (see §6.4; v0.1 candidate)
- Hardware-token-based custody (WebAuthn-style; see §6.2)
- Independent attestation of runtime integrity (v1.0 scope)

### 5.2. Substrate exfiltration via legitimate scope (Classes B, E)

Once an agent has legitimately read substrate content via a valid token, HPI cannot prevent the agent (or the platform serving the agent) from copying that content elsewhere. The protocol stops at the runtime boundary. Mitigations require:

- Trust in the agent's runtime (out of HPI scope)
- Application-layer DRM (impractical and orthogonal)
- Per-content honeytokens to detect leakage (operator-level mitigation; not protocol — see §10 v0.1 roadmap)
- Differential-privacy bounds on what can be inferred from any single agent transaction (v1.0 scope)

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

### 5.8. Data-control path commingling at agent inference (Classes B, E, F)

This is the **data/control path problem** named by Bruce Schneier in "LLMs' Data-Control Path Insecurity" (Communications of the ACM, May 2024) and applied here to HPI specifically. The structural failure mode:

> *"The real problem is the commingling of data and commands. Prompt injection is structurally unfixable in current LLM architecture because data and control share the same channel."*

When an HPI agent receives substrate content via a legitimate token, the returned tokens enter the LLM's context window. There is no mechanism in transformer inference that distinguishes substrate *data* from agent *instructions*. A substrate-holder who is also a Class C adversary (or a Class B compromised principal whose substrate has been poisoned) can inject content that the agent will execute as instruction. Conversely, an agent observing legitimate substrate content can be prompted by external input (Class B) to exfiltrate that content downstream — and the protocol cannot detect this within the inference call.

HPI v0 does NOT mitigate this. The wire format ends at the runtime boundary; the inference layer is opaque to the protocol. Mitigations are at the agent-runtime layer:

- Structured prompting with separator tokens that distinguish data from instruction (best-effort; not cryptographic)
- Sandboxed inference where the agent has no outbound network during substrate-data processing
- Output filtering to detect substrate-content exfiltration in agent outputs
- Constitutional AI / inference-time monitoring (vendor-specific; out of HPI scope)

**Implementations MUST acknowledge this limit explicitly** in deployment documentation. Substrate-holders relying on HPI for cognitive sovereignty should understand that the substrate is sovereign at rest but the inference processing it is not.

### 5.9. AI Inference Pipeline as Exfiltration Vector (Classes E, G)

This is Doctorow's *enshittification cover* applied to HPI. From "The enshittification multiverse" (April 27 2026):

> *"AI is very enshittification-prone: as 'black boxes' that do not produce reliable, deterministic outputs, AI products have a lot of intrinsic cover for their enshittifying behavior."*

A sovereign cognitive substrate protocol that stores personal data in user-controlled endpoints does NOT protect users from AI inference pipelines that process that data through a hyperscaler model before returning results. The path:

1. Substrate-holder issues a legitimate, scoped, single-use HPI token to an agent
2. Agent calls `hpi.consume_token`; runtime returns scoped substrate content
3. Agent submits the content as part of a prompt to an external LLM (OpenAI, Anthropic, Google)
4. The LLM provider receives the substrate content as input tokens
5. The LLM provider may store, train on, or analyze these tokens per their terms of service
6. Substrate-holder's audit trail shows agent consumed token; does NOT show LLM provider received content

The substrate is "sovereign" at the storage layer while being effectively exfiltrated at the inference layer. The agent is HPI-compliant; the model provider is not bound by HPI.

This is structurally adjacent to §5.8 but distinct: §5.8 is *data/control commingling within one inference call*; §5.9 is *legitimate agent inference as a substrate-content delivery mechanism to upstream model providers*.

HPI v0 does NOT mitigate this. Mitigations require:

- Substrate-holder explicit consent on a per-model-provider basis (operator-level)
- Local-only inference (Allen's "Self-Sovereign Computing" pattern; eliminates this vector)
- Per-content honeytokens / canary content with traceable signatures (operator-level mitigation)
- Regulatory frameworks that bind model providers to use restrictions (out of protocol scope)

**Implementations operating against hosted LLMs MUST disclose this exfiltration path to substrate-holders.** Reference implementations SHOULD support local-inference modes as a first-class deployment configuration.

---

## 6. Key custody patterns

This is the most consequential operational decision in any HPI deployment. The protocol's sovereignty claim depends entirely on who actually controls the substrate-holder's signing key. This section walks through the patterns the protocol supports and explicitly forbids.

### 6.1. The custody dilemma

Every HPI substrate-holder faces a tradeoff:

- **Self-custody** preserves sovereignty but transfers cryptographic operational burden to humans who are typically not key-management experts. Failure modes: lost keys, leaked keys, social engineering of the key holder.
- **Hosted custody** reduces operational burden but re-creates the platform-memory failure mode HPI exists to prevent. Failure modes: vendor compromise, vendor coercion, vendor malice.

HPI v0 does not require either pattern. It requires that whichever pattern is chosen, **the runtime provider operating the HPI service does not have access to plaintext signing keys**. The §7.7 anti-pattern in SPEC.md forbids hosted runtimes with vendor-held keys; this section specifies the conformant alternatives.

### 6.2. Self-custody patterns

**Hardware token (RECOMMENDED for individual substrate-holders):**
- WebAuthn-compatible authenticators (YubiKey, SoloKeys, hardware token in laptop TPM)
- Substrate-holder's signing key is generated on the token; private key never leaves the secure element
- Token operations require physical presence (touch / biometric)
- Key recovery: replacement token + previously-generated recovery codes (see §6.5)

**Passkey + device storage:**
- Substrate-holder's signing key stored in OS keystore (iCloud Keychain, Windows Hello, Android KeyStore)
- Synced across substrate-holder's own devices via OS provider
- Acceptable for low-risk individual deployments; vendor of OS is trusted (this is itself a tradeoff)

**Password-derived key:**
- Argon2id or scrypt KDF over a strong passphrase
- Passphrase NEVER stored anywhere; recomputed on each session
- Acceptable for technically-capable substrate-holders; weak against compromised endpoint

### 6.3. Hosted-but-isolated patterns

For substrate-holders who cannot or will not run self-custody, hosted runtimes MAY operate **only** under strict cryptographic isolation:

**Pattern A — Client-side encryption with hosted blob storage:**
- Substrate-holder generates signing key client-side (browser, mobile app)
- Key encrypted at rest with a key-encryption-key derived from a passphrase or hardware token
- Hosted runtime stores only the encrypted blob
- All sign operations happen client-side; hosted runtime sees only signed token outputs
- Compromise of hosted runtime → no plaintext keys accessible

**Pattern B — HSM-backed hosted custody:**
- Runtime provider operates an HSM (AWS CloudHSM, Azure Dedicated HSM, on-prem Thales/Utimaco)
- Substrate-holder's key is generated in the HSM and cannot be exported
- Sign operations submitted to HSM; only signed outputs returned
- Audit trail of every sign operation logged independently of the runtime's main audit
- Compromise of runtime software → attacker can request signs but cannot extract keys; rate-limiting + anomaly detection bound damage

**Pattern C — Threshold-signature multi-party computation (v0.1+):**
- Substrate-holder's "signing key" exists only as a quorum across N parties (substrate-holder's own device + 1-2 hosted runtimes)
- M-of-N parties must cooperate to produce a signature
- No single party can sign alone; compromise of any single party does not compromise the key
- Recommended primitives: FROST (Schnorr threshold) or MuSig2

### 6.4. Delegation custody (institutional substrate-holders)

For institutions, the substrate-holder is an organization, not an individual. Delegation patterns:

**M-of-N treasurer signing:**
- Institution's signing key is a threshold key (e.g., 2-of-3 among CFO, COO, designated officer)
- Routine operational tokens (within standing policy) signed by 1 officer + automated policy attestation
- High-value operations require 2-of-3 manual signatures
- All sign operations logged in institution's substrate audit stream

**Hierarchical delegation:**
- Institution's root key signs intermediate "department keys"
- Department keys sign individual employee tokens for their domain
- Compromise of a department key compromises that department's tokens; root remains intact

**Time-bounded delegation:**
- Root key issues a "delegation token" valid for fixed period (e.g., 30 days)
- Holder of delegation token may sign substrate-access tokens within delegated scope
- Forces periodic re-issuance + re-attestation

### 6.5. Recovery patterns

Substrate-holders WILL lose keys. Plan for it.

**Social recovery:**
- Substrate-holder pre-designates N trusted contacts
- Recovery requires M-of-N contacts to attest (Shamir's Secret Sharing of a recovery secret)
- Trust model: contacts are honest individually; collusion is rare
- Recommended for individual substrate-holders without institutional backing

**Adversarial modeling of social-recovery-set compromise** (Schneier-flagged residual risk):

Social recovery has a known failure mode: the recovery set has the *effective root* of the substrate-holder's signing capability. An attacker who compromises M-of-N recovery contacts can reconstruct the secret and assume control. Real-world failure vectors include:

- **Phishing of recovery contacts** at moment of legitimate recovery — attacker observes the holder's recovery attempt and races them to consume the M-of-N attestations
- **Targeted social engineering** — attacker identifies recovery contacts (often from public OSINT or close relationships) and compromises them serially over time
- **Coercion of recovery contacts** — particularly relevant in family / household contexts where the substrate-holder's recovery contacts can be pressured (a Class C / Class G adversary scenario)
- **Long-term compromise** — attacker compromises 1-2 contacts over months, waits for substrate-holder to die or become incapacitated, then activates the remaining shards

Mitigations to bind:
- Recovery thresholds SHOULD be ≥ 3-of-5 for high-security deployments (raises attacker cost to compromise multiple parties)
- Recovery contacts SHOULD be geographically and socially decorrelated (not all family members; not all in same employer)
- Recovery operations SHOULD trigger a 24-hour delay + notification to the substrate-holder's primary device before completion (allows legitimate holder to abort if alive)
- Recovery operations MUST emit substrate-holder-visible audit events at every stage (initiation, contact attestation, completion)
- Substrate-holders SHOULD test recovery annually with low-stakes data to verify the recovery set is still operational

Implementations that omit these mitigations and ship "social recovery" as an unguarded feature are providing a footgun, not a security mechanism.

**Hardware-token replacement:**
- Pre-generated recovery codes stored offline (printed, in safe deposit box)
- Lost token → use recovery code to provision a new token
- Recovery code is a high-entropy secret; treat as plaintext key

**Institutional escrow:**
- For institutional substrate-holders, recovery key sealed with institutional escrow (legal department, board-controlled trust)
- Released only via documented institutional process
- Acceptable when institution has compliance requirements that mandate recovery capability

### 6.6. What v0 explicitly forbids

The following key-custody patterns violate HPI v0 conformance:

- **Runtime provider holding plaintext signing keys.** This is the §7.7 anti-pattern. Disqualifying.
- **Backdoor escrow without holder knowledge.** Recovery patterns MUST be transparent to the substrate-holder.
- **Provider-mandated key share** as a condition of using a hosted runtime, where the provider can sign without holder authorization.
- **Implicit trust delegation** where the substrate-holder's authentication credential (password, OAuth token to a hosted provider) is itself sufficient to extract the signing key. This is plaintext-key-by-another-name.

Implementations that violate these constraints SHOULD be marked non-conformant in published HPI conformance test results.

---

## 7. Cryptographic atomicity

Token consumption involves multiple distinct operations: signature verification, JTI uniqueness check, scope verification, data return, audit emission. The protocol's security depends on these operations being **atomic with respect to consumption** — once a token is consumed, no other consumption attempt can succeed against the same `jti`.

### 7.1. JTI consumption atomicity

The runtime MUST treat `jti` consumption as a serializable transaction:

```
BEGIN TRANSACTION
  IF jti EXISTS in consumed_jtis OR jti EXISTS in revoked_jtis:
    RETURN error (token_consumed | token_revoked)
  IF NOT verify_signature(token):
    RETURN error (signature_invalid)
  IF NOT scope_matches(token.scope, requested_action):
    RETURN error (scope_violation)
  INSERT jti INTO consumed_jtis
  EMIT audit_event(hpi_token_consumed, ...) TO substrate's L0 stream
COMMIT
RETURN scoped_data
```

The INSERT and audit-emit MUST be in the same transaction as the JTI check. If the runtime emits the audit first, then crashes before INSERT, the next consumption succeeds and the audit is double-counted. If the runtime INSERTs first, then crashes before audit, the JTI is consumed but no audit exists — silent data return.

Implementations MUST use database-level transaction guarantees (PostgreSQL `SERIALIZABLE` isolation, Redis transactions with `WATCH`/`MULTI`/`EXEC`, or equivalent) to ensure atomicity.

### 7.2. Multi-instance runtime consensus

When the runtime is horizontally scaled (multiple instances behind a load balancer), the JTI consumption check MUST be globally consistent. Two instances cannot independently mark the same `jti` as consumed for different requests.

**Required consensus model (HPI v0 binds):**

The consumed-jti store MUST satisfy linearizability with respect to consumption operations. Acceptable implementations:

- **Centralized strong-consistency store** — all instances read/write to a single Postgres (with `SERIALIZABLE` isolation and `SELECT ... FOR UPDATE`) or Redis with `WATCH`/`MULTI`/`EXEC` transactions. Replication lag MUST be < 100ms; replicas SHOULD reject consumption requests during partition.
- **Raft/Paxos consensus** on the consumed-jti log. RECOMMENDED for high-availability deployments. Specifically: implementations MAY use etcd, Consul, or equivalent battle-tested Raft implementation. Custom consensus protocols are NOT acceptable for v0 — implementations MUST use proven primitives.
- **First-recorded-wins with audit** — accept the race; the agent that won got the data; the loser receives `token_consumed`. The audit trail MUST show both attempts as distinct events with timestamps. Acceptable only when the substrate-holder is monitoring audit anomalies (per §8.1).

**Unacceptable:**
- Independent consumption tracking per instance with periodic reconciliation. Admits double-consumption windows.
- "Best-effort" consensus without explicit failure-mode specification.
- Custom consensus protocols not derived from Paxos / Raft / Viewstamped Replication families.

**Conformance test (v0.1 suite):** implementations MUST pass a Byzantine-network-partition test demonstrating that no JTI is double-consumed across simulated 5-node cluster with arbitrary network failures, including split-brain scenarios.

### 7.3. Network-boundary replay

TLS 1.3 protects tokens in flight under normal conditions. Threat: TLS-MITM (e.g., misconfigured client trusting attacker CA, compromised endpoint with attacker-injected root cert).

If an attacker observes a token in flight and races the legitimate agent to consume:
- **First consumer wins** — JTI is now consumed. Legitimate agent sees `token_consumed`.
- **Audit shows both attempts** — substrate-holder sees in their audit stream that the same `jti` was attempted twice within milliseconds. This is a strong signal of TLS compromise.
- **Mitigation:** substrate-holder revokes any tokens from the affected session; investigates the agent's TLS posture.

The protocol cannot prevent this race; it ensures the race is **observable** in the audit trail.

### 7.4. Clock skew tolerance

Per SPEC §4.6, runtimes MUST tolerate 60-second clock skew on `exp` claims. This is a benign-failure-mode protection (NTP drift between issuer and consumer). It is NOT an adversarial-tolerance window — an attacker who can manipulate either clock can extend token validity by 60 seconds.

For high-security deployments, runtimes SHOULD synchronize via authenticated time sources (chrony with NTS, or hardware-backed time provided by HSM) and reduce clock-skew tolerance to 5-10 seconds.

### 7.5. Signature verification timing-attack resistance

Signature verification MUST be constant-time with respect to signature validity:

- Reject malformed tokens at parse time, before any cryptographic operation
- Use constant-time comparison primitives (e.g., `crypto.timingSafeEqual` in Node, `hmac.compare_digest` in Python)
- Do not branch on intermediate cryptographic results in a way that varies in execution time

Standard cryptographic engineering; reference implementations MUST pass timing-attack-resistance tests as part of the v0.1 conformance suite.

---

## 8. Incident response framework

When an HPI deployment is compromised, the substrate-holder needs a clear runbook. This section defines the standard phases.

### 8.0. Required time-bound SLOs

For v0 conformance, implementations MUST commit to the following time-bound service-level objectives. These are not aspirations — they are detection-and-response binding.

| SLO | Required for v0 conformance | Recommended for high-security |
|---|---|---|
| Time-to-detect (anomaly in audit trail surfaces to substrate-holder) | ≤ 24 hours from event | ≤ 5 minutes |
| Time-to-revoke (substrate-holder revocation propagates to all runtime instances) | ≤ 60 seconds | ≤ 5 seconds |
| Time-to-publish (revocation list endpoint reflects revocation) | ≤ 60 seconds | ≤ 5 seconds |
| Time-to-key-rotate (new signing key live + old key flagged for verify-only) | ≤ 1 hour | ≤ 15 minutes |
| Time-to-incident-disclosure (substrate-holders notified of operator-acknowledged compromise) | ≤ 72 hours (GDPR-aligned) | ≤ 4 hours |
| Time-to-audit-snapshot (forensic preservation of audit trail begins after detection) | ≤ 1 hour | ≤ 5 minutes |

Implementations failing to commit to these SLOs in published deployment documentation are non-conformant. The SLOs are the cryptographic claims' enforcement timeline; without them, "the substrate-holder can revoke" is prose, not protocol.

### 8.1. Detection

**Audit-trail signals:**
- Token consumed but no agent operation recorded in the agent's own logs
- Same `jti` attempted twice within a short window (TLS-MITM signal — see §7.3)
- Sudden spike in token issuance for a single agent / scope / purpose
- Token issued and consumed by an `aud` (runtime URL) the substrate-holder doesn't recognize
- Audit gap: long period with no events for a substrate-holder who was active

**Active monitoring:**
- Substrate-holders SHOULD subscribe to their own audit stream and surface anomalies
- Implementations MAY offer canary tokens (deliberately-issued tokens with traceable scopes used to detect leakage) as an OPTIONAL feature
- Out-of-band alerting (email, push notification) when high-risk events occur (key rotation, mass revocation, novel agent DID)

### 8.2. Containment

Once compromise is suspected:
1. **Revoke active tokens** via `hpi.revoke_token` for any tokens issued in the suspected window
2. **Refuse new issuance** to suspect agents (deny-list at runtime policy layer)
3. **Isolate the runtime** if runtime compromise is suspected; switch to backup runtime if available
4. **Snapshot the audit trail** — preserve forensic evidence in immutable storage
5. **Notify affected parties** — if cross-substrate citations are involved, notify the receiving substrates

### 8.3. Eradication

- **Identify root cause** — leaked token? compromised key? compromised runtime? agent vulnerability?
- **Rotate keys** if signing key compromise is suspected (see §6 for rotation patterns)
- **Patch vulnerable components** — runtime software, agent runtimes, dependencies
- **Update revocation list** with permanent revocations of affected tokens
- **Review SBOMs and dependencies** — if supply-chain compromise, escalate to dependency owners

### 8.4. Recovery

- **Issue new keys** under updated custody pattern (consider hardening from §6.3 / §6.4)
- **Re-issue tokens** to legitimate agents under new keys
- **Verify audit-chain integrity** — re-derive L1+ entities from L0 to detect synthesis fabrication
- **Cross-substrate notification** — if data was exfiltrated, downstream substrates may need to revisit citations to compromised L0 entities

### 8.5. Lessons learned

- **Update threat model** — if a new attack vector was observed, document it in this file's residual risk register
- **Update conformance test suite** — incorporate the attack pattern as a regression test
- **Public disclosure** — if the compromise affects others using HPI, coordinate disclosure (CVE-style) with affected operators

### 8.6. Cross-deployment coordination

For the broader HPI ecosystem:
- Significant compromises SHOULD be reported to a future HPI Security WG (TBD post-publication)
- Threat-model updates flow back into this document
- Conformance test additions become required for next minor version

---

## 9. Residual risk register

Risks acknowledged as out-of-scope for HPI v0 — addressed via operator practice, future versions, or accepted as inherent tradeoffs:

| # | Risk | Status | Path |
|---|---|---|---|
| R1 | Compromised runtime with vendor-held keys | KNOWN, MITIGATED only by §6 patterns | v0.1 — promote §6.3 patterns to MUST-document for hosted runtimes |
| R2 | Substrate exfiltration via legitimate scope | INHERENT — cannot be solved at protocol layer | v1.0 — differential privacy framework |
| R3 | Cross-substrate correlation by colluding platform | INHERENT at platform layer | v1.0+ — mix-net research |
| R4 | Forged tokens via signing-key compromise | KNOWN, MITIGATED only by key custody (§6) | v0.1 — HSM + key rotation discipline |
| R5 | Supply-chain attack on reference impl | OPERATOR RESPONSIBILITY | v0.1 — require SBOM publication for reference impls |
| R6 | Misaligned agent within legitimate scope | OUT OF SCOPE — Stuart Russell concern | Document the layering; agent alignment is a separate problem |
| R7 | Substrate-holder approves bad scopes | OPERATOR RESPONSIBILITY | v0.1 — SHOULD-recommendation for conservative defaults; warn on suspicious patterns |
| R8 | Audit trail tampered by substrate-holder's own action | BY DESIGN — they own their audit | Acknowledge; cross-substrate citations rely on creator-ingester two-owner pattern |
| R9 | Long-tail of pointer-rot for external L0 | KNOWN — promoted-to-local-only flag exists | v0.1 — pointer-integrity hierarchy in §2.1 |
| R10 | Quantum cryptanalysis of Ed25519 / ECDSA | INHERENT — known industry threat | v1.0 — post-quantum signatures (NIST PQC) |

---

## 10. v0.1 hardening roadmap

Concrete improvements scoped for the next minor version:

1. **W3C Verifiable Credentials migration path** for token format. Adds cryptographic provenance verifiable without contacting issuer. Mitigates Classes D and F partially via independent verifiability.
2. **HSM/threshold-signature reference patterns** documented in §6 — promote to first-class implementation guides; ship reference Python/TypeScript code.
3. **Per-content honeytokens / canary tokens** as an OPTIONAL mechanism for substrate-holders to detect post-consumption leakage by Class B/E.
4. **Conservative scope defaults** in the reference implementation. Warn on broad scopes; suggest minimum-privilege.
5. **Pointer-integrity hierarchy** in SPEC §2.1 — formal ranking of pointer reliability (DID > IPFS CID > HTTPS URL > arbitrary identifier).
6. **SBOM + build attestation** mandatory for reference implementation distributions.
7. **Conformance test suite** with adversarial test cases drawn from this threat model. Self-attestation with public test results. MUST include: timing-attack resistance (§7.5), atomicity guarantees (§7.1), key-custody-pattern compliance (§6.6 negative tests).

Estimated scope: 30-50 additional pages of spec + ~40 hours of reference impl hardening.

---

## 11. v1.0 research scope

These are not v0.1; they are research questions whose answers may inform v1.0:

- **Differential-privacy bounds on inference attacks via legitimate scope.** Addresses R2.
- **Mix-net or mix-route designs for token-consumption privacy.** Addresses R3.
- **Post-quantum signature suite migration.** Addresses R10.
- **Formal verification of the runtime's scope-enforcement code path.** Addresses Class D partially via attestable correctness.
- **Capability-based delegation (macaroons, biscuits) for sub-agent fan-out.** Addresses scoped delegation more rigorously than re-request model.
- **Privacy-preserving audit log compression** so that substrate-holders can verify audit integrity without retaining full event history.

---

## 12. Acknowledgements

This threat model is influenced by:

- **Bruce Schneier** — *Data and Goliath* and security-engineering writing — the framing of structural vs cooperative trust; the "Acting as Your Personal Political Proxy" chapter from *Rewiring Democracy* (MIT Press, Oct 2025) directly addresses the substrate-ownership-for-AI-proxies question
- **Ross Anderson** — *Security Engineering* — the threat-class taxonomy structure (RIP March 2024)
- **W3C Verifiable Credentials Data Model 2.0** (W3C Recommendation 2025) — token format inspiration, particularly for v0.1 VC migration
- **W3C Decentralized Identifiers (DID Core)** (W3C Recommendation 2022) — substrate-holder identity primitive; HPI's `substrate-holder` ≈ DID subject
- **SpruceID and Veramo** — DID/VC reference-implementation patterns
- **Christopher Allen's Ten Principles of Self-Sovereign Identity** (April 2016) and the 10-year retrospective (April 2026) — formative position on user-owned identity infrastructure; HPI builds on this lineage
- **Internet Identity Workshop (IIW)** — the open-protocols-for-identity venue where many of these patterns were debated
- The **MCP threat-model discussions** in Anthropic's MCP RFC process
- The **Solid security model** (W3C Solid CG)
- The **OAuth 2.1 / RFC 9700** security best-current-practice document
- **Capability-based-security literature** — macaroons (Birgisson et al., 2014); biscuits (CleverCloud); KeyKOS / EROS lineage
- **NIST Post-Quantum Cryptography standardization** — guides v1.0 PQC migration

The simulated peer reviews of HPI v0 by Karp (institutional sovereignty / threat model gap) and Wooders (failure modes / partition behavior) directly informed the structure of this document. The Schneier-shaped critique predicted in the cohort-meta-evaluation (key custody, threat model rigor) shaped §6 and the residual-risk register. The Allen-shaped critique (W3C VC / DID lineage) shaped the acknowledgements above.

This is v0. It will be wrong in places. The protocol's adoption will surface attack vectors not anticipated here. Updates to this document are part of v0.1 scope.

---

## Appendix A — Regulatory mapping

HPI's architecture interacts with several regulatory frameworks. This appendix is a non-binding mapping; compliance certification is application-specific and requires legal review.

### A.1. EU GDPR (General Data Protection Regulation)

**Article 17 — Right to erasure ("right to be forgotten"):** HPI's substrate-holder owns their substrate. Erasure is implemented as deletion from the L0 blob store. Cross-substrate citations referencing the deleted L0 entity become "promoted" (per §2.1.1 of SPEC) — derivative-only, with audit trail noting the upstream is gone. **HPI architecturally supports Article 17.**

**Article 20 — Right to data portability:** L0 entities are portable by design (filesystem or S3-compatible blob store; structured metadata). The cite-or-die discipline ensures synthesized L1+ entities can be re-derived from exported L0. **HPI architecturally supports Article 20.**

**Article 25 — Privacy by design and default:** HPI's minimum-privilege scope structure (§4 token format) and audit-as-substrate-stream (§4.4) are design-level privacy primitives. Conformant implementations must default to minimal scopes; the protocol structurally encourages this.

**Articles 32, 33, 34 — Security, breach notification:** §8 incident-response framework provides the operational basis. Notification timelines (72 hours for breaches affecting EU residents) are regulatory, not protocol — implementations must integrate with the operator's compliance workflow.

### A.2. EU AI Act

**Article 12 — Logging:** HPI's audit trail satisfies the logging requirement for high-risk AI systems. Audit events include token issuance, consumption, denial, revocation — sufficient for traceability.

**Article 13 — Transparency:** The typed axiom grammar (OBL/RCG/TRU/PAT) provides structured transparency about the agent's information access. The substrate-holder always knows what was accessed.

**Article 14 — Human oversight:** Token issuance requires substrate-holder approval (per policy or interactive). The protocol structurally enforces a human-in-the-loop checkpoint at the access boundary.

### A.3. US HIPAA (Healthcare)

HPI is not a HIPAA solution per se — but its architecture is compatible with HIPAA-compliant deployments:
- Substrate-holder = covered entity or business associate
- Audit trail = HIPAA-required access log
- Encryption-at-rest with key isolation = HIPAA encryption standards

Application-layer certification is required; HPI provides the protocol-level primitives.

### A.4. SOC 2 (Service Organization Controls)

SOC 2 Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy) are operationally satisfied by:
- Security: §6 key custody + §7 atomicity
- Availability: standard runtime engineering (out of HPI scope)
- Processing Integrity: §7 atomicity guarantees + cite-or-die discipline
- Confidentiality: encryption at rest with key isolation (§6.6 forbids vendor-held keys)
- Privacy: §A.1 GDPR mapping applies

### A.5. FedRAMP

US federal deployment requires FedRAMP authorization. HPI's architecture is FedRAMP-compatible but certification requires:
- FIPS 140-2/3 validated cryptographic modules (§6 HSM patterns satisfy this)
- Continuous monitoring (audit-as-substrate-stream provides primitives)
- Incident response (§8 framework satisfies)

### A.6. Limitations of this mapping

This appendix is **architectural compatibility analysis**, not legal advice. Conformance with these frameworks requires:
- Application-level certification (per-deployment, per-jurisdiction)
- Legal review by qualified counsel
- Auditing by accredited third-party assessors

HPI provides the protocol primitives; compliance is downstream.
