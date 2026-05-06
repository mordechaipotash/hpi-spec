# HPI Spec — Status

**Last updated:** 2026-05-06
**Current version:** v0 (draft — not for public release)

## Visibility status

🔒 **Private repository.** Not yet circulated for public review. Local-only.

Do NOT publish to GitHub / share publicly until:
1. ✅ Naming finalized (HPI brand confirmed 2026-05-06)
2. ✅ All 9 sections drafted (done 2026-05-06 — single sitting)
3. ❌ At least 3 trusted readers have reviewed (candidates: Shaul, Yitzhak, Plurality team contact, Letta researcher contact)
4. ✅ Insperanto-related material in axioms/examples sanitized to placeholders 2026-05-06 (residual `Insperanto` only in this STATUS.md, intentional)
5. ✅ LICENSE present (Apache 2.0); per-impl MIT pending v0.1 reference impl
6. ✅ THREAT-MODEL.md drafted (2026-05-06) — adversarial threat model addressing Karp + Schneier-predicted critiques

Gate that remains: **#3, reader review.** Everything else cleared on 2026-05-06.

## What's drafted (v0)

| Section | Status | Notes |
|---|---|---|
| README.md | ✅ DRAFT | First-pass complete; needs review |
| SPEC.md §1 — Foundations | ✅ DRAFT | Full draft, ~1100 words. 7 subsections including hyperscaler trajectory, alignment claim, open-protocol historical pattern, scope, audience |
| SPEC.md §2 — Substrate Model | ✅ DRAFT | Full draft, ~2000 words. Needs example fleshing in 2.5 |
| SPEC.md §3 — Typed Axiom Grammar | ✅ DRAFT | Full draft, references existing axiom files |
| SPEC.md §4 — Token Handoff Protocol | ✅ DRAFT | Full draft, ~1800 words. JWT format, scope structure, issuance flow, single-use, revocation, audit trail, delegation, worked example |
| SPEC.md §5 — Wire Format & Transport | ✅ DRAFT | Full draft, ~1200 words. MCP method JSON shapes, discovery, storage interface, key management, versioning |
| SPEC.md §6 — Reference Implementation | ✅ DRAFT | ~700 words. Existence proofs (Brain MCP / Viter / Persofi), gap-analysis matrix, v0.1 reference target, conformance criteria |
| SPEC.md §7 — Non-Goals & Anti-Patterns | ✅ DRAFT | ~750 words. 6 non-goals + 3 anti-patterns including hosted-runtime-with-vendor-keys and silent-agent-persistence |
| SPEC.md §8 — Open Questions for the Community | ✅ DRAFT | ~1000 words across 8 RFC-style items including governance/naming/composition with adjacent standards |
| SPEC.md §9 — Acknowledgements & Lineage | ✅ DRAFT | ~600 words. 8 explicit precedents including Torah sourceability discipline credited honestly |
| axioms/OBL-obligations.md | ✅ DRAFT | Imported from viter-workspace/ontology/ |
| axioms/RCG-recharges.md | ✅ DRAFT | Imported |
| axioms/TRU-trust.md | ✅ DRAFT | Imported |
| axioms/PAT-patents.md | ✅ DRAFT | Imported, v0.1 draft |
| axioms/README.md | ✅ DRAFT | The "we ship a worldview" framing |
| examples/01-obligation-end-to-end.md | ✅ DRAFT | Full L0→L1→L2 trace for one obligation |
| schemas/ | ❌ EMPTY | v0.1 scope — JSON Schemas per family |

## What's complete vs what needs work

**Complete and load-bearing (as of 2026-05-06):**
- All 9 SPEC.md sections drafted — ~9700 words, the load-bearing core of v0
- 4 v0 axiom families (OBL/RCG/TRU/PAT) with full structure
- Worked example tracing one obligation L0→L1→L2 with typed projection rule
- Letta comparison document with honest framing of inverted axiom
- Plurality outreach draft ready to send
- Sanitization complete in axiom + example files
- Apache 2.0 LICENSE present
- Repo committed, clean git history (5 commits)

**Needs work before v0 publication:**
- 3+ trusted readers review the document (the SOLE remaining gate)
- Reference implementation v0.1 demonstrating the protocol (recommended for adoption, not strictly required for publication)
- Public-domain version of the worked example with no sanitization residue (current `<client-corp>`-style placeholders are sufficient; alternative is a fully synthetic example)

**Out of scope until v0.1:**
- JSON Schemas per axiom family
- Flow diagrams (Mermaid sequence diagrams)
- Interop notes for OAuth/VC/DID/Solid/OCL composition
- Reference HPI runtime as standalone library

## Production roadmap (revised 2026-05-06)

### ✅ Phase 1: complete v0 draft — DONE 2026-05-06

Original plan: 3 weeks. Actual: 1 day, single sitting. SPEC.md sections 1-9 drafted plus README, STATUS, LICENSE, axiom imports, worked example, Letta comparison, Plurality outreach.

**Rationale for compression:** The substrate-thinking material had been accumulating in viter-workspace and Brain MCP since 2024-04. Drafting was synthesis of existing material, not generation of new claims. The Persofi axiom files were already written; they just needed to be imported and contextualized.

### Phase 2: reader review (target: 2-3 weeks, dependent on others)

The only remaining publication gate. Cannot be compressed unilaterally — requires other humans' time and attention.

- [ ] Week 1: Send Plurality outreach (`outreach/PLURALITY.md`) — gate has lifted
- [ ] Week 1: Brief Shaul on the spec; ask for architectural review (Vita Substrate vs HPI relationship)
- [ ] Week 1: Brief Yitzhak; ask for security review of token mechanism (§4)
- [ ] Week 2: Optional — reach out to Letta team contact (Sarah Wooders or similar) sharing `comparisons/LETTA.md`
- [ ] Week 2-3: Address feedback. Most likely scope of changes: clarifying §3.6 (substrate-vs-ontology), tightening §4 token format details, adjusting §8 open questions

### Phase 3: reference implementation (target: 4-6 weeks, parallelizable with Phase 2)

Not strictly required for v0 publication — the spec stands on its own with the existing implementations cited in §6 as existence proofs. But strongly recommended before public release: a clean v0.1 reference moves the spec from "interesting whitepaper" to "implementable protocol with working code."

- [ ] Week 1-2: Python module: JWT issuer/verifier, signing key management, MCP method surface (4 required + optional discover)
- [ ] Week 3: One axiom family (OBL) end-to-end with synthetic data (replacing sanitized Persofi data)
- [ ] Week 4: Audit log as L0 substrate stream; revocation list endpoint
- [ ] Week 5-6: Documented integration story: HPI runtime + Plurality OCL vault as L0 backing (assumes Phase 2 outreach yielded a working OCL relationship)

**Estimated cost:** ~80-120 hours solo; ~30 hours if reusing Brain MCP MCP server scaffolding.

### Phase 4: public release (target: 1 week)

- [ ] Publish hpi-spec to GitHub under personal namespace `mordechaipotash/hpi-spec` (or org `hpi-protocol/spec` if community signals form)
- [ ] Cross-post: Anthropic MCP discussion forums, Plurality forum (after their alignment), Hacker News, AI-protocols subreddit
- [ ] Companion post: technical blog explaining the substrate conservation law and HPI's position relative to hyperscaler memory features

### Total revised timeline

- Phase 1: ✅ done (2026-05-06)
- Phase 2: ~2-3 weeks (reader-time-dependent)
- Phase 3: ~4-6 weeks (parallelizable with Phase 2)
- Phase 4: ~1 week
- **Net: 7-10 weeks from today to public release, IF Phase 3 is pursued in parallel.** 5-6 weeks if Phase 3 is deferred to post-publication v0.1.

## Decision log

| Date | Decision | Rationale |
|---|---|---|
| 2026-05-06 | Brand name: HPI (Hyperpersonalized API) | Mordechai's existing private term since 2024-04. Memorable. Self-contained. |
| 2026-05-06 | License: Apache 2.0 for spec; MIT for reference impls | Standard for protocol adoption. Apache permits commercial reference impls; MIT minimizes friction for impls. |
| 2026-05-06 | Repo home: ~/Projects/hpi-spec/ initially; future GitHub `hpi-protocol/spec` org | Personal first to ship faster; org-level later for adoption optics |
| 2026-05-06 | v0 axiom families: OBL, RCG, TRU, PAT | Already drafted in viter-workspace/ontology/, in production at Insperanto pilot. Existence proof matters more than completeness. |
| 2026-05-06 | Transport: extend Anthropic MCP | Reuse existing wire format. HPI-native RPC is unnecessary scope expansion in v0. |
| 2026-05-06 | Token format candidate: signed JWT v0; W3C VC v0.1 | JWT is universally implementable; VC adds cryptographic provenance for v0.1. |

## Reader candidates (for pre-publication review)

To be confirmed by Mordechai before outreach. Suggested:

- **Shaul Levine** — architectural review; does HPI compete with or layer under Vita Substrate?
- **Yitzhak (Viter security lead)** — security review of token mechanism
- **Plurality / OCL contact** — fellow-traveler validation; potential alignment
- **Letta team contact** (maybe Sarah Wooders or other) — peer review from agent-context space
- **W3C VC/DID community** member — cryptographic primitives review
- **One CFO or compliance officer** familiar with finance-vertical use (Jeffrey Levine?) — domain validation for axiom families

## Risk flags

- **Hyperscaler walled-garden timeline.** Estimated 18-30 month window before user lock-in solidifies. Spec needs to ship publicly within Phase 4 timeline (12 weeks from now = ~2026-08).
- **Persofi material exposure.** Axiom files reference Insperanto, Jeffrey Levine, specific suppliers. Sanitization required before public release. Decision: replace specific names with `<vendor-A>`, `<client-X>` placeholders, or get explicit Insperanto sign-off.
- **Mordechai bandwidth.** 40-60 hours over 12 weeks must compete with Persofi shipping (revenue) and family obligations. Phase 1 (3 weeks of writing) must happen in early-morning / late-evening blocks.


## Spec revisions executed (2026-05-06 afternoon)

After three simulated peer reviews (Karp / Wooders / Karpathy) produced 20 distinct revisions, executed all 19 remaining (Karp #4 / THREAT-MODEL.md was shipped earlier).

| # | Revision | Status |
|---|---|---|
| Wooders #1 | Split §4.1 into access axiom + persistence position + kernel-as-handle | DONE |
| Wooders #6 | Add §4.11 Learning across boundaries | DONE |
| Wooders #7 | Add §4.10 Failure modes (benign) | DONE |
| Karpathy #1 | Add §4.12 Boundary conditions (access vs inference) | DONE |
| Karpathy #2 | Add §1.8 What HPI does NOT solve | DONE |
| Karp #6 | Substrate-holder primitive in §2.1 | DONE |
| Karp #1 | Add §3.7 HPI as cross-Ontology transport | DONE |
| Karp #2 | Promote PAT to Reference Domain Ontology | DONE |
| Karp #7 | Add §3.8 v0.1 axiom validator commitment | DONE |
| Karpathy #3 | §6.4 conformance gains v0.1 validator requirement | DONE |
| Karpathy #4 | Add §6.5 microHPI compactness aesthetic | DONE |
| Wooders #8 | Reword §7.2 memory-products composable | DONE |
| Wooders #5 | Add §8.10 empirical comparison question | DONE |
| Karp #5 | Add §8.9 value-capture pattern question | DONE |
| Wooders #2 | README access-control as load-bearing claim | DONE |
| Karp #3 | README How HPI relates to domain Ontologies | DONE |
| Wooders #3 | comparisons/LETTA.md compositional framing | DONE |
| Wooders #4 | HPI-as-kernel framing handle | DONE |
| Karpathy #5 | Anthropomorphic-language sweep (no changes needed) | DONE |

The triple-converged central critique (claims more than enforces) is now structurally addressed via the section 4.1 split plus section 3.7 cross-Ontology framing.
