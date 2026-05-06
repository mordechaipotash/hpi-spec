# Reviewer dossier — Christopher Allen

**Role:** SSI / W3C / TLS 1.0 co-author. Founder of Rebooting the Web of Trust (RWOT) and IIW. Co-founded Agentic Internet Workshop (2026). Currently at Blockchain Commons (Gordian Envelope, XID).
**Compiled:** 2026-05-06 from primary sources via lifewithalacrity.com (5 articles fetched in full), W3C DID Core, IIW 40 announcements.

## 1. Public writings (last 3 years, recent-weighted)

- **"Dispatches of a Trust Architect: Ten Years of Self-Sovereign Identity"** (April 26 2026, lifewithalacrity.com/article/dispatches-ssi-2026-revision/). The 10-year retrospective. The 2026 community draft retains 2016 language verbatim where it survives, revises all ten original principles, adds six new ones: **Inalienability, Cognitive Liberty, Relational Autonomy, Stewardship, Equity, Anti-Coercive Design**. Allen openly admits: *"Capital flows to centrality. We wrote the principles loosely enough that the loopholes were exploitable. And they have been exploited."*

- **"Agency in AI"** (April 22 2026, lifewithalacrity.com/article/Musings-ai-agency/). His most direct engagement with agentic systems. Three frames: (1) The Authority Problem — proposes "Principal Authority" from agency law as the model for delegated AI agents, with predicates: `principalAuthority`, `assertsDelegationFrom`, `delegationScope`, `delegationConstraints`; (2) The Credit Issue — authorship transparency; (3) **Self-Sovereign Computing** as solution: *"We built Self-Sovereign Identity so that your keys and credentials could stay under your control rather than being held by a platform that could revoke them. Local inference is the same principle applied to AI."*

- **"Dispatches of a Trust Architect: Fighting Technology Paternalism"** (March 18 2026). Coins **"Technology Paternalism"**: design / algorithmic / infrastructural / protective paternalism. Countermeasures: *"can you override the system's decision? Contest it? Inspect the reasoning? Leave without losing everything?"* Calls out EUDI wallet ecosystem as exhibiting Infrastructural Paternalism despite claiming interoperability.

- **"Musings of a Trust Architect: The Exodus Protocol"** (October 2025). Five architectural patterns for autonomous infrastructure: operate without external dependencies; **encode rules in mathematics not policy**; make constraints load-bearing; preserve exit through portability. Bitcoin as prime Exodus Protocol.

- **"Musings of a Trust Architect: Least & Necessary Design Patterns"** (September 2023). Foundational. Least Privilege → Least Authority → Least Access (and necessary inverses). Minimization is the primary axis.

- **"Musings of a Trust Architect: Building Trust in Gradients"** (November 2024). Progressive Trust 10-phase model. *"What you reveal is initially minimized."* Maps directly to HPI's scoped, time-bounded token model.

- **W3C DID Core** co-author. **IIW** co-founded 2005. **TLS 1.0** co-author (RFC 2246, January 1999).

## 2. Stated values + intellectual lineage

- **Cypherpunk / Blockstream lineage.** Bitcoin governance, mathematical-rights-not-platform-privileges framing.
- **Self-sovereignty as moral position.** 2016 principles: *"Any self-sovereign identity is ultimately based on the ineffable 'I' that's at the heart of identity."* 2026 expansion includes Cognitive Liberty + Inalienability — moral floor has risen.
- **"Trust Architect" framing.** Architectural, design-pattern level, not protocol-by-protocol.
- **Tension with W3C process.** Calls out EUDI wallets as captured Infrastructural Paternalism. Gordian XID is his answer to DID fragmentation: build cryptographic independence rather than betting on standards committees.
- **Agency law as primary frame.** 2026 work grounds everything in *Laws of Agency* and *Principal Authority* — fiduciary duty / duty of loyalty before ZK proofs.

## 3. Patterns of argumentation

- **Leads with ecosystem fragmentation, not defensively.** Owns SSI's failures publicly. The 2026 retrospective is the canonical example.
- **Selective disclosure as recurring concern** — appears in 2016 principles, 2023 Least/Necessary, 2026 retrospective. Wants cryptographically enforced minimum disclosure.
- **Composable pattern language** — names patterns (Progressive Trust, Least Access, Principal Authority, Technology Paternalism), then analyzes how a system either instantiates or violates them.
- **"What we've learned in 10 years"** rhetorical pattern — leads with failure mode, then describes revision.
- **Direct ownership of past error** — rare in standards community.

## 4. Adjacency to HPI's concerns

- **MCP**: Not directly engaged. His Principal Authority framework in "Agency in AI" addresses the agentic problem at the pattern level; MCP would be viewed as incumbent transport needing sovereignty-preserving extension.
- **JWT vs W3C VC**: Gordian Envelope is his preferred primitive — neither JWT nor W3C VC. CBOR-based with built-in elision (selective disclosure). He'll note JWT lacks cryptographic selective disclosure; will ask whether SD-JWT or BBS+ were considered.
- **Agent-as-principal vs agent-as-instrument**: Accepts agent-as-instrument but insists on **principal accountability** via `delegationScope` and `delegationConstraints` predicates.
- **`substrate-holder` ≈ DID subject**: Yes, with conditions. Does the holder control a private key? Can delegation be revoked without agent cooperation?
- **Selective disclosure / mDL pattern**: Strongly supports the principle. His concern with ISO 18013-5 mDL is Infrastructural Paternalism (Apple/Google attestation reintroduces gatekeepers). Will apply same critique to HPI implementations requiring trusted third-party validation.
- **NoPhoneHome alignment**: Has independently articulated the same principle in Self-Sovereign Computing (2023): *"Your data stays on your device. Your inference runs on your hardware. No API key is required."*

## 5. Typical review register

- **Length**: 600-900 words for peer review, 2000-3000 for essays. Long-form architectural with abstract sections, specific terminology, footnotes.
- **Structure**: numbered taxonomies, historical lineage citations (PGP 1991, Saltzer-Schroeder 1975, Carl Ellison 1996), explicit moral positioning before technical claims.
- **Voice patterns**: "trust architect", "coercion resistance", "principal authority", "minimum disclosure", "infrastructural paternalism", "exodus protocol", "mathematical rights".

## 6. Predicted angles of response to HPI

**ENDORSE:**
- `substrate-holder` as Principal Authority — his framework applied precisely
- Scoped, time-bounded token model — matches Progressive Trust
- THREAT-MODEL.md §6 key custody patterns (HSM / threshold / hosted-but-isolated) — Allen's SmartCustody/Gordian ground
- 6 adversary classes — matches his analytical method
- NoPhoneHome alignment as Exodus Protocol pattern
- GDPR/AI Act regulatory mapping (Appendix A)

**PROBE:**
- Does HPI cite Ten Principles + 2026 retrospective explicitly? §9 acks updated but not yet mapped at sub-axiom level
- Axiom grammar (OBL/RCG/TRU/PAT) — formally express delegation scope cryptographically? Or prose labels on JWT claims?
- Selective disclosure mechanism — can scope be verified without revealing rest of substrate?

**PUSH BACK:**
- **JWT as token primitive.** Bearer JWT is capability token, not verifiable credential. Holder cannot present subset of context claims without re-issuing token. Ask: SD-JWT or BBS+ considered?
- Any dependence on external validation infrastructure (Exodus Protocol pattern violation)
- **MCP as substrate.** Building sovereignty on Anthropic-controlled protocol = architectural risk (same concern as EUDI wallets depending on Apple/Google)

**PROPOSE:**
- `substrate-holder` expressible as DID subject (DID:web for pragmatism, XID for sovereignty)
- **Gordian Envelope** as axiom-grammar container (built-in elision, non-correlation, threshold-sig support)
- His "Agency in AI" predicates (`delegationScope`, `delegationConstraints`) as semantic basis for axiom grammar

**CONVERGENCE TEST:** Allen **CONVERGES** on Karp/Wooders/Karpathy claim-vs-enforcement, BUT arrives via different vocabulary: *"is the constraint load-bearing in the mathematical sense, or is it just policy?"* Exodus Protocol pattern 2 (encode rules in mathematics not policy) = his version of the convergent finding.

**DIVERGENCE — new vector Allen surfaces:**

**Coercion resistance at the delegation boundary.** The prior three reviewers implicitly assume cooperative adversary. Allen's Technology Paternalism framework adds the **coercive legitimate actor** — platform, state, employer — as fourth adversary type. His specific question Karp/Wooders/Karpathy missed: *can an agent's operator coerce the substrate-holder into granting scope by making the refusal too costly?* (*"you can leave, but you leave empty-handed"*). Structural critique of HPI's consent model, not its cryptography.

THREAT-MODEL.md §2 covers 6 adversary classes — Allen would ask whether class 4 (Compromised Runtime) or 5 (Colluding Platform) includes the **legitimate platform operator as coercive actor**. Likely answer: not adequately.

## Confidence calibration

**High:** All public writings 2023-2026 read in full. Pattern of argumentation, rhetorical style, IIW 40 + W3C CG May 5 2026 attendance verified.
**Medium:** JWT vs SD-JWT vs Gordian Envelope hierarchy (his preferred primitive is clear; direct comparative statement on JWT-for-agent absent).
**Low:** Whether he has privately engaged with HPI-adjacent specs (IIW 40 session notes not yet public).

**Verdict:** Allen converges on claim-vs-enforcement (FOUR-confirmed). Diverges by surfacing **coercion resistance at the delegation boundary** — the legitimate platform operator as adversary. This is the genuinely new ground the v2 cohort produced.
