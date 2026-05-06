# Worked example — one obligation, end-to-end

A single Persofi obligation traced from L0 evidence through L1 extraction into L2 projection, with the typed projection rule made explicit at every step.

> **Why this exists:** Yesterday Shaul asked at IKEA `24:37` *"how does it derive the L2 from L1?"* and we couldn't answer concretely. This is the answer.

## The scenario

Insperanto coordinates a patent prosecution job in Germany. The Insperanto client (final buyer) is *Acme Pharma*. Insperanto engages a German agent (vendor) to file the patent locally. The German agent invoices Insperanto €4,800; Insperanto invoices Acme Pharma €5,400. Net margin €600.

This is a textbook 2-leg recharge under [`02-recharges.md`](02-recharges.md) RCG-1.

## L0 — the evidence (immutable)

Five evidence sources land in the system over 9 days:

| Source | Timestamp | Content | Substrate |
|---|---|---|---|
| `E1` Email from German agent | Apr 18 09:14 CET | "Please find attached our invoice for the German filing of Acme matter, ref AC-2026-DE-0042" | inbox/L0 |
| `E2` PDF attached to E1 | (same) | German agent invoice; supplier-invoice-number `DE-INV-87332`, amount €4,800.00, VAT 0% (cross-border B2B), due 30 days | files/L0 |
| `E3` Plunet job-cost line | Apr 18 11:22 IDT | Job 4172, supplier-cost line €4,810.00, ref `DE-INV-87332` | plunet/L0 |
| `E4` Insperanto's outgoing invoice to Acme Pharma | Apr 22 16:08 IDT | Customer invoice `INSP-2026-04-1099`, amount €5,400, ref `Job 4172`, due 45 days | xero/L0 |
| `E5` Acme Pharma payment confirmation in Xero | Apr 27 09:01 IDT | Bank receipt €5,400 against `INSP-2026-04-1099` | xero/L0 |

Note `E2` says €4,800; `E3` says €4,810. Off by €10 — a Plunet rounding error that Jeffrey has flagged in the past.

## L1 — deterministic extraction

Each L0 source is extracted by a typed extractor producing a typed evidence node. No LLM judgment at L1.

```
N1 = extract(E1) → EmailEvidence{ from: "billing@de-agent.de", references: ["AC-2026-DE-0042"], attachments: [N2] }
N2 = extract(E2) → InvoiceEvidence{
        supplier: "DE-AGENT-GMBH",
        supplier_invoice_no: "DE-INV-87332",
        amount: 4800.00, currency: "EUR",
        issue_date: 2026-04-18, due_date: 2026-05-18,
        client_ref: "AC-2026-DE-0042"
     }
N3 = extract(E3) → PlunetJobLine{
        job_id: 4172,
        supplier: "DE-AGENT-GMBH",
        supplier_ref: "DE-INV-87332",
        cost_amount: 4810.00, currency: "EUR",
        booked_at: 2026-04-18T11:22+03:00
     }
N4 = extract(E4) → XeroInvoice{
        customer: "ACME-PHARMA",
        invoice_no: "INSP-2026-04-1099",
        amount: 5400.00, currency: "EUR",
        issue_date: 2026-04-22, due_date: 2026-06-06,
        memo_ref: "Job 4172"
     }
N5 = extract(E5) → XeroPayment{
        invoice_ref: "INSP-2026-04-1099",
        amount: 5400.00, currency: "EUR",
        booked_at: 2026-04-27T09:01+03:00
     }
```

Five typed evidence nodes. No claims yet about *what they mean together*.

## L2 — projection into the worldview

This is where the ontology earns its keep. **L2 is the typed projection of L1 evidence into the obligation/recharge worldview.** Not a prompt. Not a heuristic. A rule.

### Step 1 — apply OBL-3 (evidence merge)

Find evidence nodes that point at the same obligation. The merge predicate is:

```
same_obligation(a, b) ⟺ (
  counterparty(a) == counterparty(b)
  AND reference(a) == reference(b)
  AND |amount(a) - amount(b)| ≤ T_amount(currency=a.currency)
)
```

Result:

- **Obligation O₁** (German agent → Insperanto): merges {N1, N2, N3} via shared counterparty `DE-AGENT-GMBH` + ref `DE-INV-87332` + amounts within T_amount = max(1%, €5) ≈ €48 → €10 mismatch is within tolerance.
- **Obligation O₂** (Insperanto → Acme Pharma): {N4, N5} via shared customer + invoice number.

### Step 2 — apply OBL-4 (canonical value, source priority)

For O₁, priority order is `Xero > Plunet > supplier-PDF > email`. Xero has nothing for this obligation (it's an upstream supplier bill, not yet booked into Xero). Plunet says €4,810; supplier PDF says €4,800. Per OBL-4, the supplier's own invoice **wins** when Xero is silent (because the supplier knows what they billed; Plunet's number is internally generated).

→ **canonical_amount(O₁) = €4,800.00**, derivation cited: `OBL-4, supplier-PDF over Plunet, Xero unbooked`.

The €10 discrepancy between Plunet and PDF is **preserved as an audit-trail node** on O₁: `discrepancy{ source_a: PlunetJobLine N3 €4,810, source_b: InvoiceEvidence N2 €4,800, axiom: OBL-4, resolution: prefer N2, magnitude: €10 }`. It's not gone; it's typed.

For O₂ there's no conflict: canonical_amount(O₂) = €5,400.

### Step 3 — apply OBL-5 (FX freeze)

Both obligations are in EUR. Insperanto's book currency is EUR. No FX conversion needed at the obligation level. (If the book were ILS, each obligation would freeze the EUR→ILS rate at its respective creation moment.)

### Step 4 — apply OBL-2 (state)

- O₁ state: `recognized` (April 18) → no payment evidence yet → still `recognized` as of April 27.
- O₂ state: `recognized` (April 22) → `settled` (April 27, on N5) → terminal.

### Step 5 — apply RCG-1 (recharge link)

The recharge predicate: do O₁ and O₂ form a recharge?

```
recharge_candidate(upstream, downstream) ⟺ (
  is_intermediary_role(upstream.buyer, downstream.seller)
  AND shared_underlying_job(upstream, downstream)
)
```

Both conditions hold: Insperanto is buyer of O₁ and seller of O₂; both reference Job 4172 (Plunet `job_id` 4172, Xero `memo_ref` "Job 4172"). → **Recharge R₁ = (upstream: O₁, downstream: O₂)**.

### Step 6 — apply RCG-2 (margin)

```
margin(R₁) = canonical_amount(O₂) − canonical_amount(O₁) = €5,400 − €4,800 = €600
```

### Step 7 — apply RCG-3 (completeness)

R₁ is *incomplete* because O₁ is `recognized`, not `settled`. → margin is **provisional** until O₁ settles.

### Step 8 — apply RCG-4 (profit recognition)

Profit on R₁ contributes to the period of the *second leg's settlement*. O₂ settled in April. **But O₁ is unsettled** → R₁ is incomplete → profit-on-R₁ for April is **provisional €600** with the unresolved leg cited.

### Step 9 — apply TRU-1..3 (trust at decision time)

Trust score for `DE-AGENT-GMBH` as of April 27 = `compute_trust(...)`. Suppose it returns 0.82 (long-standing relationship, clean reconciliation history). For Acme Pharma, suppose 0.91. Per RCG-5, recharge-chain trust = min(0.82, 0.91) = **0.82**.

This score doesn't decide anything by itself yet — it's an input for any *action* the system might take next (e.g., auto-pay O₁ when it falls due). Per TRU-4 the auto-pay class for €4,800 (between $1K–$10K equivalent) requires trust ≥ 0.9 → action = `flag-and-review`, not `auto`.

## The L2 file's output

What lands in `chat-log/by-day/2026-04-27-L2.md` (or wherever this gets synthesized) is:

```markdown
## Obligation O₁ · DE-AGENT-GMBH → Insperanto · €4,800

**State:** recognized (since 2026-04-18)
**Canonical amount:** €4,800.00 [OBL-4: supplier-PDF over Plunet, Xero unbooked]
**Discrepancy preserved:** Plunet says €4,810 (audit-trail node attached) — €10 rounding, within tolerance, supplier-PDF authoritative
**Evidence:** N1 (email Apr 18), N2 (PDF DE-INV-87332), N3 (Plunet line job 4172)
**FX:** none (book = native = EUR)

## Obligation O₂ · Insperanto → ACME-PHARMA · €5,400

**State:** settled (2026-04-27)
**Canonical amount:** €5,400.00 [OBL-4: Xero authoritative, no conflict]
**Evidence:** N4 (Xero invoice INSP-2026-04-1099), N5 (Xero payment Apr 27)

## Recharge R₁ · O₁ → O₂ via Job 4172

**Margin (provisional):** €600 [RCG-2]
**Status:** incomplete [RCG-3] — upstream leg O₁ still recognized, not settled
**Profit attribution:** April 2026 *provisional*, will become canonical when O₁ settles [RCG-4]
**Chain trust:** 0.82 [RCG-5, min(DE-AGENT 0.82, ACME 0.91)]

## Action recommendation

When O₁ falls due 2026-05-18: TRU-4 says action_class=auto-pay-$1K-$10K requires trust ≥ 0.9; chain trust 0.82 < 0.9 → **flag-and-review**, not auto-pay.
```

## What this proves

- **L2 isn't free text trusting an LLM.** Every claim cites an axiom; the axioms are typed; the derivation is reproducible.
- **Profit isn't a number, it's a derived fact with provenance.** The €600 margin can't masquerade as confirmed profit because RCG-3 won't let it.
- **Discrepancies don't disappear.** The €10 Plunet/PDF mismatch lives on the obligation as an audit-trail node, surfaceable in any view.
- **Action policy is a typed lookup, not a vibe.** When the agent considers auto-paying O₁, the answer is determined, not generated.

## What L1 still has to do well

- **Extractors must be correct** — if N3 has wrong `supplier_ref` because Plunet has bad data, the merge in step 1 fails and we get two phantom obligations. This is the L1's job: extract typed evidence faithfully, *don't* try to interpret meaning. Interpretation is L2's job, governed by axioms.
- **Identity resolution on counterparties** is part of L1, not L2. *"DE-AGENT-GMBH"* in the email and *"DE Agent GmbH"* in Plunet have to resolve to the same node before they reach L2. This is a typed normalization step, not an LLM judgment — though LLMs may *propose* matches that the typed step then accepts/rejects against rules.

## What this changes about the streamer

Today's pitch: *"I made a streamer that could be multi-tenant, goes into Supabase Viter, lands L0s."* That's correct, but the streamer's job is **only L0**. Don't let it accidentally do L1 extraction or L2 projection on the way in. Those are typed downstream stages with their own correctness contracts. Conflating them is how you end up with the "free text trusting an LLM" problem yesterday's contrarian read warned about.
