# HPI Spec — Status

**Last updated:** 2026-05-06
**Current version:** v0 (draft — not for public release)

## Visibility status

🔒 **Private repository.** Not yet circulated for public review. Local-only.

Do NOT publish to GitHub / share publicly until:
1. Naming finalized (HPI brand confirmed; subtitle TBD)
2. Sections 4, 5, 7 drafted (token protocol, transport, non-goals)
3. At least 3 trusted readers have reviewed (candidates: Shaul, Yitzhak, Plurality team contact, Letta researcher contact)
4. Insperanto-related material in axioms/examples reviewed for what's safe to publish vs needs sanitization
5. License files added (Apache 2.0 spec, MIT reference impls)

## What's drafted (v0)

| Section | Status | Notes |
|---|---|---|
| README.md | ✅ DRAFT | First-pass complete; needs review |
| SPEC.md §1 — Foundations | 📝 OUTLINE | ~800 words to expand |
| SPEC.md §2 — Substrate Model | ✅ DRAFT | Full draft, ~2000 words. Needs example fleshing in 2.5 |
| SPEC.md §3 — Typed Axiom Grammar | ✅ DRAFT | Full draft, references existing axiom files |
| SPEC.md §4 — Token Handoff Protocol | 📝 OUTLINE | The hardest technical section. ~1500 words to expand |
| SPEC.md §5 — Wire Format & Transport | 📝 OUTLINE | ~700 words. MCP-extension approach decided |
| SPEC.md §6 — Reference Implementation | 📝 OUTLINE | Brain MCP + Viter L0-L3 are existence proofs |
| SPEC.md §7 — Non-Goals | 📝 OUTLINE | List in README; expand to ~400 words |
| SPEC.md §8 — Open Questions | 📝 OUTLINE | RFC-style items, ~500 words |
| SPEC.md §9 — Acknowledgements | 📝 OUTLINE | Lineage in README; expand to ~200 words |
| axioms/OBL-obligations.md | ✅ DRAFT | Imported from viter-workspace/ontology/ |
| axioms/RCG-recharges.md | ✅ DRAFT | Imported |
| axioms/TRU-trust.md | ✅ DRAFT | Imported |
| axioms/PAT-patents.md | ✅ DRAFT | Imported, v0.1 draft |
| axioms/README.md | ✅ DRAFT | The "we ship a worldview" framing |
| examples/01-obligation-end-to-end.md | ✅ DRAFT | Full L0→L1→L2 trace for one obligation |
| schemas/ | ❌ EMPTY | v0.1 scope — JSON Schemas per family |

## What's complete vs what needs work

**Complete and load-bearing:**
- The substrate model (§2) — formal articulation of L0-L3, conservation law, two-owner schema, subjectivity gradient
- The typed axiom framework (§3.1-§3.3) — what axioms are, conformance requirements
- v0 axiom families (4) drafted with full structure
- Worked example showing real data traversing the stack

**Needs work before v0 publication:**
- Token protocol (§4) — the access-control primitive. Without this section, the "agents borrow via permissioned tokens" claim is asserted but not specified.
- Wire format (§5) — naming the MCP method extensions concretely
- JSON Schema appendix — converting the prose axioms to machine-readable schemas

**Out of scope until v0.1:**
- Full reference implementation
- JSON Schemas
- Flow diagrams
- Interop notes for OAuth/VC/DID/Solid/OCL

## Production roadmap

### Phase 1: complete v0 draft (target: 3 weeks)

- [ ] Week 1: Sections 1, 7, 9 expanded from outline to full prose
- [ ] Week 2: Section 4 (token protocol) drafted — the hardest technical section
- [ ] Week 3: Section 5 (transport) drafted; Section 8 (open questions) finalized

### Phase 2: reference implementation v0.1 (target: 5 weeks)

- [ ] Week 4-5: Python module: token issuer/verifier, MCP API, audit log
- [ ] Week 6: One axiom family (OBL) implemented end-to-end with Persofi data
- [ ] Week 7-8: Documented integration: HPI runtime + Plurality OCL vault as L0 store

### Phase 3: pre-publication review (target: 2 weeks)

- [ ] Week 9: Pre-publication review by 3-5 trusted readers
- [ ] Week 10: Address feedback, finalize naming, sanitize Insperanto material

### Phase 4: public release (target: 1 week)

- [ ] Week 11: Publish to GitHub. Cross-post to: Anthropic MCP discussion, Plurality forum, Letta community, Hacker News (timing TBD)
- [ ] Week 12: Engage with feedback, ship v0.1 patch with first community contributions

**Total: 12 weeks, ~40-60 focused hours, ~$0 direct cost.**

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
