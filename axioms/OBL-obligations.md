# Axiom family 1 — Obligations

## The opinion

An invoice, a bill, a receivable, a job-cost line in `<workflow-system>`, a PDF in an email, a row in `<accounting-system>` — none of these are *the thing*. The thing is **the abstract obligation** between a vendor and a buyer. Each of those representations is *evidence* of that obligation, not the obligation itself.

This is a strong opinion. Most accounting software treats the `<accounting-system>` bill as the canonical record. `<vertical-product>` treats the obligation as canonical and `<accounting-system>` as one source of evidence among several. That inversion is the moat.

## Core axiom

> **OBL-1 (draft):** Every obligation is a node in the graph. Each node has *exactly one* canonical state at a point in time, derived from all available evidence sources, with the derivation rule and conflict-resolution priority encoded explicitly.

## Sub-axioms

> **OBL-2 (draft):** An obligation is *born* the moment any source produces evidence of it (a `<workflow-system>` job line, a vendor email, a PDF received) and remains live until *settlement* — full payment + reconciliation + audit closure. Cancellation is a settlement state, not a deletion.

> **OBL-3 (draft):** Two pieces of evidence point at the same obligation iff they share *all of:* counterparty pair, reference (PO/job number/supplier-invoice-number), and amount window (within tolerance T_amount). Tolerance T_amount is currency-specific and must be declared per-axiom, not hard-coded. Default: 1% or 5 currency units, whichever is larger.

> **OBL-4 (draft):** When two evidence sources for the same obligation disagree, the obligation's canonical state is determined by **source priority**, not by recency:
> - `<accounting-system>` record (after manual reconciliation) > `<workflow-system>` job line > supplier-issued invoice (PDF) > email body > inferred-by-LLM
> - Disagreements are *preserved as audit trail*, never overwritten. The derivation rule that produced the canonical value must be cited in the L2.

> **OBL-5 (draft):** Currency conversion is part of the obligation, not a downstream report. An obligation has a *native* currency (the supplier's) and a *book* currency (<client-corp>'s), and the conversion rate at the moment of obligation creation is *frozen* into the node. Subsequent rate movements are *separate* derivative obligations (FX gain/loss), not modifications to the original.

## Allowed states

```
draft → recognized → matched → reconciled → settled → archived
                ↓                     ↓              ↓
             disputed            partially-paid    cancelled
```

Each transition is a typed event; transitions between non-adjacent states are *forbidden* and require a compensating event.

## What this axiom buys you

- **Evidence dedup** is a graph operation, not a join. *"Have we seen this obligation before?"* answered in O(1) on the canonical node, not by scanning `<accounting-system>` + `<workflow-system>` for a fuzzy match each time.
- **Reconciliation correctness** is a property of the worldview, not a check after the fact. Either an obligation is in `reconciled`, or it isn't; the system can't have two states.
- **Audit-as-product** falls out for free — every L2 fact about an obligation cites the axiom and the evidence chain that derived it.
- **Cross-source variance** (the `<workflow-system>`-vs-`<accounting-system>` rounding mismatch <the CFO> complained about) is captured in OBL-4: the disagreement is preserved as audit trail, the canonical value is derived deterministically.

## L2 projection rule (worked)

```
L2_obligation = project(
  evidence_nodes: [`<workflow-system>`, `<accounting-system>`, PDF, email, ...],
  axioms: [OBL-1..5],
  rule: "merge by (counterparty, reference, amount±T_amount), apply OBL-4 priority, freeze FX per OBL-5"
)
```

The L2 file's job is to write down which evidence merged, which axiom decided the canonical value, and why — verbatim citation, no LLM paraphrase. If an LLM is needed, it produces *candidate* canonical values; the typed rule decides.

## What's NOT in this axiom (intentionally)

- *How the user sees obligations.* Downstream of UI; not here.
- *Bank reconciliation specifics.* Separate axiom family (banking) when needed.
- *Tax and VAT.* Separate axiom family. Tax is a derivative of an obligation, not part of one.
- *Multi-leg trade financing.* Out of scope v0; will need OBL-6+ when <client-corp>'s pipeline includes letters of credit or factoring.

## Open questions

- **Tolerance T_amount per currency** — list pending. Need to pull from <the CFO>'s CFO judgment + <client-corp>'s actual variance distribution.
- **Sub-jobs and partial deliveries** — does a partial delivery create a new obligation or split the existing one? Lean toward split, not new, but undecided.
- **Template suppliers** (utility bills, recurring SaaS) — recurring obligation pattern needs a sibling axiom OBL-* that handles "expected next obligation" inference. Out of scope v0.
