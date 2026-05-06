# Persofi Ontology — what we ship as a worldview

> *"You shipped a database. We ship a worldview."* — what Karp would say (yesterday, 2026-04-29 14:11, contrarian read on the L0→L3 stack).

This folder is **the first commit before any UI**. Every L1→L2 derivation rule must live inside one of these documents. If a derivation can't be expressed as a projection of L1 evidence into one of these worldview claims, the worldview is incomplete and the L2 is unsafe.

## Why this folder exists, not just a schema

A schema says *what is*. An ontology says *how things relate, what's allowed, what's derived* — and it encodes an **opinion** about how the financial-vertical universe is shaped. Customers conform their business to a worldview. They use a database. The ontology is the moat; the streamer, the L0 substrate, the L2 synthesis pipeline are all plumbing in service of the worldview.

## The load-bearing axiom families

**v0 (2026-04-30) — financial-vertical foundation:**

1. [`01-obligations.md`](01-obligations.md) — what an invoice/bill/receivable actually IS, abstracted from its source representation
2. [`02-recharges.md`](02-recharges.md) — recharge as first-class, with profit-attribution rules. *"If recharge is not accounted for, profit is not real."* — Jeffrey, 2026-04-19
3. [`03-trust.md`](03-trust.md) — supplier trust, variance explanation, auto-action thresholds — encoded so the system reasons about *qualitative difference* between counterparties, not just foreign keys.

**v0.1 (2026-05-01) — patent vertical extension:**

4. [`05-patents.md`](05-patents.md) — patent as first-class node that *generates* obligations rather than being described by them. PAT-* axioms encoding lifecycle, jurisdictional fan-out, ownership-as-typed-relation, and renewal-as-expected-obligation. Drafted in response to Jeffrey's 2026-05-01 strategic update naming patent-lifecycle insights as the path to direct-to-corporate distribution.

## Worked example

[`04-worked-example-obligation.md`](04-worked-example-obligation.md) — a single Persofi obligation traced from L0 evidence (email + PDF + Plunet line + Xero bill) through L1 extraction, into L2 projection under the obligations axiom, with the typed projection rule made explicit.

## Companion notes

[`06-substrate-vs-ontology.md`](06-substrate-vs-ontology.md) — layering note explaining the relationship between this ontology repo and Shaul's `Vita_Substrate_Scope_v0.1.docx` (2026-05-03). Substrate = horizontal plumbing; Ontology = vertical worldview. Open reconciliation questions captured for Shaul.

## Per-entity instantiations

The universal axioms above apply across any financial-vertical deployment. The folders below are **scoped instantiations** — per Shaul's 2026-05-03 00:25 IDT directive that *"every company has to be represented ... Viter has one, Persefy has one."*

- [`viter/`](viter/) — the platform-org
- [`persofi/`](persofi/) — the financial-vertical product pack (Jeffrey distribution; the "patent is a job" instantiation)
- [`clients/insperanto/`](clients/insperanto/) — Persofi's first pilot client (Jeffrey's CFO employer)

## Status

- v0 written 2026-04-30 in response to the Apr 29 Thiel/Palantir critique that the stack lacks an ontology layer (the deepest cut — see [chat-log/by-day/2026-04-29-L1.md:3112](../chat-log/by-day/2026-04-29-L1.md)).
- v0.1 added 2026-05-01 — `05-patents.md` PAT-* family, drafted from Jeffrey's strategic memo same morning. Schema work on patents is forbidden until PAT-* is promoted from draft.
- Numbers, thresholds, and template counts are placeholders — the *shapes* of the axioms are the load-bearing claim, not the constants.
- Yitzhak's "17 axiom templates" framing (Apr 30 IKEA pitch) is the right shape but generic — these axiom families plus their derivations are the financial-vertical-specific instantiation.

## Promotion path

When an axiom in this folder is referenced by ≥2 L2 files and confirmed by Mordechai, it gets a stable ID (`OBL-1`, `RCG-2`, `TRU-1`, etc.) and becomes part of the contract for L2 synthesis. Until then, axioms are draft.

## Anti-rules

- **Do not write a generic ontology** (place / time / person / event). That's a schema dressed up. The financial-vertical-specific opinion is the point.
- **Do not derive an L2 fact that doesn't trace to an axiom in this folder.** If you need to, you've found a missing axiom — add it here first.
- **Do not pre-empt UI here.** UI is downstream. The ontology answers *"what is true,"* not *"what does the user click."*
