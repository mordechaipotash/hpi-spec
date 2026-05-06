# HPI Governance Charter — v0 stub

**Status:** v0 stub. Names the governance gap explicitly so the spec is honest about what is not yet decided. v0.1 expands.
**Last updated:** 2026-05-06
**Editor:** Mordechai Potash (sole maintainer at v0 — see §3 transition plan)

---

## Why this exists

This charter exists because the cohort meta-evaluation (Doctorow simulation specifically) named governance-void as the single highest-impact remaining gap in HPI v0. Without a governance model, "anyone can be HPI-compliant" is structurally indistinguishable from "the best-resourced implementor will capture the canonical grammar." Open protocols have learned this lesson repeatedly (SMTP→Gmail, OAuth→Auth0, ActivityPub→Threads risk). HPI v0 takes the lesson seriously by stating its governance position plainly, even when the position is "we have not yet built the governance body, here is the path to one."

---

## 1. The governance objects

These are the artifacts that need explicit canonical ownership:

1. **The SPEC.md document** — the wire format and access control protocol
2. **The THREAT-MODEL.md document** — the binding adversarial threat model (normative per SPEC §5.0)
3. **The typed axiom grammar** — OBL, RCG, TRU, PAT in v0; future families
4. **Reference implementations** — the canonical Python/TypeScript reference shipped per SPEC §6.3
5. **JSON Schema appendices** — when v0.1 ships them
6. **The conformance test suite** — when v0.1 ships it
7. **The revocation list endpoint conventions** — `/.well-known/hpi/revocations.json` format and update cadence
8. **Capture-resistance enforcement** — which implementations are flagged non-conformant per SPEC §7.11

---

## 2. The governance gap as of v0 (honest disclosure)

**Sole maintainer.** As of 2026-05-06, all governance objects above are under the sole authorship and maintenance of Mordechai Potash. There is no committee, no foundation, no consortium. The repository at github.com/mordechaipotash/hpi-spec is privately held; the spec has not yet been publicly released.

**This is a v0 fact, not a v0 plan.** A protocol whose canonical artifacts are maintained by a single individual is by definition a single point of capture. The v0 status is honest about this and is NOT a long-term architecture.

**Risks the current state creates:**
- Single-implementor capture of the typed axiom grammar (an extension or modification adopted by a hyperscaler could fork the canon)
- Single-author bias in threat modeling and conformance criteria
- No appeal process for implementations flagged non-conformant
- No audit accountability for the maintainer's own conformance claims
- No succession plan if the maintainer becomes unavailable

These risks are named so they can be addressed, not denied.

---

## 3. Transition plan to broader governance

Three phases, in increasing rigor:

### Phase 1 — v0 transparency (current)

- All decisions logged publicly in this charter and in commit messages
- All conformance test results published
- All threat-model updates announced publicly with rationale
- Maintainer commits to NOT modifying the typed axiom grammar without public RFC + 30-day comment period

### Phase 2 — v0.1 working group (target: within 6 months of v0 publication)

- Form an HPI working group with at least 5 contributors from at least 3 distinct organizations
- Working-group charter committing to: rotating chair, public minutes, RFC process for changes, dispute resolution
- Conformance test suite + JSON Schemas maintained by working group, not sole maintainer
- Working group has authority to flag implementations non-conformant (with appeal process)

### Phase 3 — v1.0 foundation or standards body (target: within 18 months of v0 publication)

Two paths, decided by the working group based on adoption signals:

**Path A — Independent foundation** (Apache Software Foundation / Linux Foundation / Solid Foundation models)
- HPI assets transferred to a 501(c)(3) or equivalent
- Board with representation from: protocol implementors, civil society, academia, end-user advocates (NOT exclusively industry)
- Funding model: grants + sponsorship; no single industry sponsor exceeds 25% of operating budget
- Governance documents publicly maintained
- Trademark and reference-implementation rights held by foundation, not individual

**Path B — IETF / W3C standards track** (RFC process for HPI core; W3C CG for VC/DID interop)
- Submit core protocol as IETF Internet-Draft
- Submit axiom-grammar interop work as W3C Community Group
- Standards-body process governs changes
- Conformance test suite remains community-maintained

The choice between Path A and Path B is made by the working group when the time comes. Both paths are acceptable; neither is acceptable as v0.

---

## 4. Decision authority during v0

Until Phase 2 launches, the following decision categories and authorities apply:

| Decision category | v0 authority | v0.1 target authority |
|---|---|---|
| SPEC.md changes | Maintainer | Working group consensus |
| THREAT-MODEL.md changes | Maintainer with public review | Working group + security WG sub-committee |
| Axiom family additions | Maintainer with 30-day public RFC | Working group RFC process |
| Conformance flags (non-conformant designation) | Maintainer publishes findings; no appeal yet | Working group with formal appeal process |
| Reference implementation merges | Maintainer | Working group code-owners |
| Trademark + brand decisions | Maintainer | Foundation board (Path A) or none (Path B) |

---

## 5. Capture-resistance enforcement mechanism

Per SPEC §7.11, certain anti-patterns are FORBIDDEN. The mechanism for enforcing these:

**v0:** Public naming. The maintainer publishes a `non-conformance/` directory with documented findings on implementations that violate §7.7–§7.12. Findings include: implementation name, specific violation, evidence, date.

**v0.1:** Working-group review. Findings are reviewed by the WG before publication; implementations have 30-day notice to remedy or contest.

**v1.0:** Foundation enforcement. The foundation may revoke the right to use the "HPI-compliant" trademark for implementations that fail to remedy.

**The legal mechanism for trademark revocation requires v1.0 foundation status.** Until then, "HPI-compliant" is an informal claim with public-naming as the only enforcement.

---

## 6. Multi-stakeholder representation principles

Path A foundation, when established, MUST have board representation including (not exclusively from industry implementors):

- **End-user advocacy** — representatives whose constituency is substrate-holders, not implementors
- **Civil society** — privacy + digital rights organizations (EFF, EDRi, ACLU, equivalent)
- **Academia** — at least one cryptographer, one HCI researcher, one law professor
- **Standards bodies** — W3C and/or IETF liaisons
- **Equity** — at least one representative whose mandate is access for substrate-holders without technical capacity (per the cohort meta-evaluation's identified equity gap)

This composition is NOT decided by industry implementors alone. Industry implementor representatives constitute at most 40% of the board.

---

## 7. Open questions for v0.1

The following questions are NOT decided by this v0 stub. They are listed so the v0.1 working group has explicit scope.

1. **Path A vs Path B** — foundation or standards body? Decision by working group based on 12-month adoption signal.
2. **Funding model for foundation** — grants only, sponsorship-tiered, member dues?
3. **Trademark policy** — strict, permissive, or no trademark?
4. **Conformance suite licensing** — Apache 2.0 or similar; reciprocal vs permissive?
5. **Reference implementation language** — Python primary + TypeScript secondary, or both first-class?
6. **Bilingual / international scope** — English-only v0; multi-language for v0.1?
7. **The equity question** — how does HPI ensure substrate-holders without technical capacity are not excluded by construction? (raised by danah boyd in cohort meta-evaluation, deferred from v0)

---

## 8. Acknowledgements

The structure of this charter borrows from:

- **Solid Project governance** (Inrupt + W3C Solid CG) — multi-stakeholder model
- **Apache Software Foundation** governance — board composition, project lifecycle
- **IETF process** — RFC + comment period + WG model
- **Plurality / OCL** — early thinking on user-owned protocol governance

The decision to ship a v0 charter that names the governance gap rather than pretending it doesn't exist follows Christopher Allen's "Dispatches of a Trust Architect" approach (April 2026): admit what wasn't right in v0 so v1 can address it.

The pressure to ship this charter even at v0-stub quality came from Cory Doctorow's predicted critique (cohort meta-evaluation, May 2026): *"Deferred governance is not governance — it's a promise to be captured later."*

This is v0. It is honestly insufficient. v0.1 starts the working group.
