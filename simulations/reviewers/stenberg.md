# Reviewer dossier — Daniel Stenberg

**Role:** Author and primary maintainer of curl (since 1998, runs in tens of billions of devices). IETF contributor. 30+ years implementing HTTP/TLS/network protocols.
**Compiled:** 2026-05-06 from daniel.haxx.se primary sources (8 articles fetched), IETF Datatracker, GitHub.

## 1. Public writings (last 3 years, recent-weighted)

- **"Don't trust, verify"** (March 26 2026, daniel.haxx.se/blog/2026/03/26/dont-trust-verify/). *"Software and digital security should rely on verification, rather than trust."* Threat model: malicious committer impersonation (Jia Tan/XZ), compromised release infrastructure, credential theft, deepfake social engineering. Response: cryptographic signing every layer, automated CI verification (200+ CI jobs), code review tied to commits, no binary blobs, test coverage as verification surface.

- **"High-Quality Chaos"** (April 22 2026). curl bug-bounty filtering AI slop. Quality filter: precision. *"You can tell by the way they are worded."* Vague claims classified as slop regardless of source.

- **"curl 8.20.0"** (April 29 2026). 274th release. 8 security fixes. NTLM disabled by default (24-year legacy, 7 CVEs), SMB disabled, RTMP dropped, OpenSSL-QUIC backend dropped (*"the API is lacking. We have communicated with the OpenSSL-QUIC team since even before the API first shipped and it still does not offer the knobs and controls we would like"*). Pattern: when extension cannot give implementers control, it does not graduate.

- **"Deviating from Specs"** (October 2022). His canonical position. Four priority rules: *"Follow established standard protocol specifications / Security is a first-tier property / Interop widely / Maintain behavior for existing features."* Rules conflict; his resolution: *"Users want reliable Internet transfers that are secure and interoperate correctly."* Spec is instrumental, not the end.

- **"The Gemini Protocol Seen by This HTTP Client Person"** (May 2023). His most complete published protocol review — **the template for his HPI review**. Structure: credentials → design motivation (fair reading) → systematic enumeration of specific flaws → quoted spec text → implementability verdict → proposal to fix without abandoning goals. His critique: missing version negotiation, spec defined twice with inconsistent syntax, no explicit connection reuse semantics, TOFU certificate approach that cannot scale, URL spec underspecified (*"138 words for a URL scheme"* — quantified the vagueness). Comment thread response: *"the current design of the protocol makes it worse than it has to be."*

- **"My Cookie Spec Problem"** (March 1 2025). RFC 6265 Set-Cookie syntax defined twice with different grammars in §4.1 vs §5.2. Lost IETF consensus vote twice to fix it. Documents without bitterness; principle clear: **internal inconsistency in a spec is a defect, not a feature.**

- **"Death by a Thousand Slops"** (July 2025). Quality filter for AI-generated security reports: specificity, reproducibility, cited-location of claimed bug. Reports that claim vulnerability in prose without test case or exact code location are dismissed.

- **"Decomplexification Continued"** (February 2026). Average cyclomatic complexity in curl source dropped 20.8 → 15.9 over 10 months. Method: *"split functions into smaller pieces with smaller and more specific scopes."* Lesson: complexity that cannot be decomposed into testable units cannot be maintained.

**IETF**: `draft-stenberg-httpbis-tcp-03` (TCP Tuning for HTTP, 2016, expired). Contributed to RFC 6265 (cookies) as non-browser implementer.

## 2. Stated values + intellectual lineage

- **30 years of transport-layer implementation.** Not theorist. Evaluates every spec against what implementation requires. curl runs in tens of billions of devices = his operating constraint.
- **The practitioner's parsimony.** Drops legacy when sustained security debt accumulates (NTLM after 7 CVEs, SMB, RTMP, OpenSSL-QUIC). If extension cannot give implementers controls they need, doesn't graduate.
- **The interoperability absolute.** *"At times, it is hard to increase security levels by default because it would hamper interop with others."* Interop is the surface on which correctness is measured. Spec that cannot be interop-tested is not yet a spec.
- **Verification over trust as design principle.** Applies to protocol design, not just supply chain. Every behavior verifiable IS verified.
- **Wire format as ground truth.** Critique of Gemini: spec in plain English with interpretation conflicts. Spec being short is not virtue if shortness introduces ambiguity.

## 3. Patterns of argumentation

- **The Gemini review is the template.** Credentials → design motivation → enumerated flaws → quoted spec text → implementability verdict → proposal.
- **The word-count tell.** *"138 words"* for the Gemini URL spec. Doesn't say "vague" — quantifies vagueness.
- **The missing-mechanism probe.** Models likely worst-case deployed implementation, not best-case. *"What's the file format? A common db somehow?... I strongly suspect that many existing Gemini clients avoid this huge mess by simply not verifying the server certificates at all."*
- **"This does not rhyme with reduced complexity"** — exact phrase when spec claims simplicity but introduces hidden implementation complexity.
- **Concurrent-failure model.** *"These could also happen in combinations and in a rapid sequence."* Stress-tests against adversary combinations.
- **Public proposal, not just critique.** Does not exit a review having only criticized. Proposes specific fixes.
- **Implementation experience as primary evidence.** *"In implementing X for 30 years..."* is his sourcing convention.

## 4. Adjacency to HPI's concerns

- **JWT**: No dedicated post but JWT is signed tokens over HTTP — within his domain. curl supports Bearer auth. *"Don't trust, verify"* directly about token/signature verification chains. Will treat unspecified JWT details (mandatory claims, signing algorithms, key custody for verification) as spec gaps.
- **MCP**: No public posts found commenting on MCP. Response to "extends MCP" will be: *what does "extends" mean, mechanically?* Same critique as Gemini's implicit-GET.
- **"Extends MCP" without specifying methods**: Direct parallel to Gemini's "no method at all but it is implied to be GET." Will surface as blocking defect. Ask: ABNF or JSON Schema. **Prose that says "extends" without delta specification is not extension — it is aspiration.**
- **Versioning ambiguity**: *"There is no version number or anything and there is no room for doing a Gemini v2 in a forward-compatible way. This way of a 'living document' seems to be popular these days, even if rather problematic for implementers."* "v0" is not a version scheme.
- **JSON Schemas absent (HPI v0.1 planned)**: Wire format without machine-readable schema cannot be automatically validated. *"How does a conforming implementation know it conforms?"*

## 5. Typical review register

- **Format**: Blog post (1500-4000 words) with H2 headers per critique, inline spec quotations, numbered/bulleted defects.
- **Tone**: Direct, precise, non-adversarial toward author but adversarial toward weakness. Distinguishes spec from designer.
- **Citation pattern**: Quotes exact spec text, includes version number (cited "0.16.1" for Gemini). If HPI has no version number, will note.
- **Length**: Gemini review ~4000 words = his benchmark for serious protocol review.

## 6. Predicted angles of response to HPI

**ENDORSE:**
- Cite-or-die discipline (matches "don't trust, verify")
- THREAT-MODEL.md's 12-section structure with explicit adversaries / mitigations / regulatory mapping (correct hygiene)
- MCP as transport substrate (pragmatic reuse over novel invention)
- JWT as token format (RFC 7519 well-specified) — accept in principle, probe specifics

**PROBE:**
- *"Where are the JSON Schemas?"* First probe. Treats absent schemas like absent test cases — unverifiable claim.
- *"What are the method names?"* If §5.2 enumerates HPI methods in prose without normative list.
- *"What is the version negotiation mechanism?"* If v0 has no forward-compatibility path.
- *"What are the mandatory JWT claims?"* If "signed JWT" without specifying signing algorithm, mandatory claims, key distribution → three separate defects.
- *"What does the deployment tail look like?"* What happens when non-expert developer implements HPI without reading full spec?

**PUSH BACK:**
- **Prose-as-protocol.** Direct objection: *"The only protocol specification is a single fairly short page that documents the over-the-wire format mostly in plain English (undoubtedly featuring interpretation conflicts)."* If HPI's wire format specified primarily in prose, will call out by name.
- Convergence point — claim-vs-enforcement — but framed differently: not *"the prose overclaims"* but *"the spec cannot be implemented faithfully from this document."*

**PROPOSE:**
- A JSON Schema for every message type, **before v0.1 ships, not in it**.
- Conformance test suite with curl-style torture tests: run every fallible operation to failure, verify no resource leak.
- A normative method registry (analogous to IANA's HTTP method registry).
- A version field in wire format with negotiation mechanism.
- Explicit list of mandatory vs. optional JWT claims with algorithm identifiers.

**CONVERGENCE TEST:** Stenberg **CONVERGES** with Karp/Wooders/Karpathy on claim-vs-enforcement. Same gap, framed as **implementability** rather than ambition: *"I cannot implement this faithfully from this document."*

**DIVERGENCE — new vector Stenberg surfaces:**

**Deployment-tail specification failure.** Where prior reviewers ask "does the spec enforce its claims?", Stenberg asks *"what does a bad-faith or incompetent implementation look like, and does the spec close those failure modes?"* For Gemini: TOFU was conceptually fine, but *"in the deployment tail, most clients will skip certificate verification entirely because the spec does not specify the storage format."* For HPI: what does a sovereign cognitive substrate look like when implemented by a developer who reads only §5.2 and skips THREAT-MODEL.md? **If the threat model is in a separate document and not normatively referenced by the wire-format spec, it is advisory, not binding.** That is a new attack vector none of the prior simulations raised.

## Confidence calibration

**High**: Direct primary sources for all blog posts cited. IETF draft authorship confirmed. Argumentation patterns/tone/structure grounded in primary text.
**Medium**: JWT position inferred from general stance. MCP position no direct post — inferred from how he handles "extends" claims generically.
**Low**: Whether he'll blog about HPI vs comment on GitHub depends on engagement level. THREAT-MODEL.md shipping increases probability.

**Verdict**: Stenberg converges on claim-vs-enforcement (FIVE-confirmed when combined with Allen). Diverges by surfacing **deployment-tail specification failure** — the spec creates a conformance vacuum that adversaries can exploit by deploying technically-compliant-but-behaviorally-divergent implementations. For sovereign cognitive substrate, this is sovereignty failure, not just documentation gap.
