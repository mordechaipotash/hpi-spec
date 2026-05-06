# Axiom family 2 — Recharges

## The opinion

A recharge is **a first-class entity**, not a flag on an invoice. It's a derivative obligation that re-routes economic substance through an intermediary — and *the profit calculation derives from it*. Treating recharge as a flag means profit numbers will silently drift from reality every time recharge logic changes. Treating it as an entity means profit is a typed derivation that can be audited, replayed, and disagreed with explicitly.

This is the axiom Jeffrey was naming on 2026-04-19 morning when he wrote the 14-section Persofi Flow memo: *"If recharge is not accounted for, profit is not real."* That sentence is ontological, not procedural. It means: in your worldview, profit *cannot exist* unless the recharge graph has been resolved.

## Core axiom

> **RCG-1 (draft):** A recharge is a typed link between two obligations: an *upstream* obligation (vendor → intermediary) and a *downstream* obligation (intermediary → final buyer), where the intermediary's economic role is to pass through the underlying service while extracting a margin. Both obligations exist independently; the recharge link makes their economic relationship explicit.

## Sub-axioms

> **RCG-2 (draft):** Margin = downstream.amount − upstream.amount, in the *book* currency (Insperanto's), computed at FX rates frozen per OBL-5 on each leg independently. Margin can be negative (loss), zero (pass-through at cost), or positive (markup). Sign and magnitude are *typed properties* of the recharge, not derived after the fact.

> **RCG-3 (draft):** A recharge is *complete* iff both legs are in `settled` or `cancelled` (in matching terminal states). An incomplete recharge has *indeterminate margin*; profit calculations that include it must carry an explicit `provisional` tag in the L2 with the unresolved leg cited.

> **RCG-4 (draft):** Profit-for-period = Σ(margin) over recharges where *both legs* settled within the period, plus Σ(other-revenue) − Σ(other-cost). A recharge that crosses a period boundary contributes to profit *in the period of the second leg's settlement*, not the first. This is a strong claim — it means you cannot recognize recharge profit until it's been booked on both sides.

> **RCG-5 (draft):** Trust in a recharge chain is the **minimum** trust score across all counterparties in the chain (per axiom family TRU). A recharge through a low-trust intermediary inherits the low-trust property regardless of how trusted the endpoints are.

> **RCG-6 (draft):** A recharge can have *more than two* legs (vendor → intermediary-A → intermediary-B → final buyer). The margin axiom (RCG-2) generalizes: margin per intermediary is the difference between its outgoing and incoming legs. Total chain margin is the sum.

## What this axiom buys you

- **Profit honesty.** Recharge-aware profit numbers cannot drift silently because every recharge is a node and every margin is a typed property; recompute is deterministic.
- **Provisional flagging.** When Jeffrey asks *"what's profit on Job 4172?"* and one leg of a 2-leg recharge is unsettled, the answer comes back *with* the `provisional` tag and a pointer to the unsettled obligation. No false confidence.
- **Insperanto-specific patent prosecution recharge pattern is encodable** — the firm bills the client, the firm pays the agent in the foreign jurisdiction, the firm extracts a margin that's the value of the prosecution coordination. RCG-2 captures it natively.
- **Audit chain.** Every profit number in an L2 cites the recharge nodes that derived it; an auditor can re-walk the graph and arrive at the same number or find the discrepancy.

## L2 projection rule (worked)

```
L2_profit_for_period = sum(
  recharge.margin
  for recharge in recharges
  if both_legs_settled_within_period(recharge)
) + other_revenue - other_cost,
provisional_flags = [
  recharge.id for recharge in recharges
  if any_leg_settled_within_period(recharge)
  and not both_legs_settled(recharge)
]
```

If the L2 reports a profit number without `provisional_flags` accounted for, the L2 is incorrect.

## Anti-pattern this axiom prevents

> *Treating recharge as an invoice flag* — the upstream and downstream invoices each get a `is_recharge=true` boolean, and profit is computed as Σ(downstream) − Σ(upstream) over the period. This is what every accounting package does. It silently loses correctness when:
> - one leg crosses a period boundary;
> - one leg is in dispute;
> - the chain has more than two legs;
> - currency conversion happens at different times on each leg.

By making the recharge a *typed entity* with both legs as references, all four failure modes become *visible* in the L2 rather than silent.

## Open questions

- **What counts as an "intermediary's service"?** When does pass-through coordination *with no economic value-add* still create a recharge node, vs. just being two unrelated obligations? Lean toward: any intentional pass-through is a recharge, even at cost — because the coordination *is* the value-add and should be visible.
- **Refund/clawback flow.** When a downstream payment is reversed after the upstream was settled, does the recharge revert to `provisional` or transition to `disputed`? Probably `disputed`, but the transition rule needs writing.
- **Multi-currency recharge chains.** When upstream and downstream are in different currencies and intermediary's book is in a third, the FX-freeze rule (OBL-5) per leg is sound but the *margin* number depends on which currency you're computing margin in. Margin should be stated in book currency by default, with native-currency margin available as a derived alternative — but spec'd, not implicit.
- **Recharge expectations / pre-commitments.** When a client pre-commits to a job, an *expected* recharge exists before either leg is created. Out of scope v0; sibling axiom RCG-7 if needed.
