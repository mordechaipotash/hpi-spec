# Axiom family 3 — Trust

## The opinion

A counterparty isn't a foreign key — it's a node with a **trust score** that the system reasons about. Two suppliers with identical schemas can be *qualitatively different*, and the worldview must encode that difference. Trust is what allows the system to act with appropriate confidence: high-trust gets auto-actioned, medium-trust gets flagged-for-review, low-trust gets blocked-pending-human. Without typed trust, every action is the same risk and every approval is theatre.

This is the axiom that answers the policy question from yesterday: *"Where does an agent prove it was allowed to do what it did?"* Allowed isn't an RLS rule — it's a worldview claim: *"this counterparty's trust score, multiplied by this action's risk class, is below the auto-action threshold for this user's authority level."*

## Core axiom

> **TRU-1 (draft):** Every counterparty (vendor, customer, intermediary) is a node with a numeric trust score t ∈ [0, 1] computed deterministically from a fixed set of evidence dimensions, with the computation rule cited in every L2 that uses the score. Trust is *not* a vibe.

## Sub-axioms

> **TRU-2 (draft):** Trust is computed from at least these dimensions, weighted per worldview policy: (a) reconciliation match rate over rolling 90 days; (b) variance distribution (mean + stddev) of (claimed − reconciled) amounts; (c) on-time payment / on-time delivery ratio; (d) dispute count and resolution outcomes; (e) tenure (length of relationship, log-scaled); (f) compliance flags (sanctions, KYC). Each dimension is bounded; trust = weighted sum, clipped to [0,1].

> **TRU-3 (draft):** Trust is a *property of the counterparty at a point in time*, not a forever-property. It must be re-computed on every new piece of evidence and *the historical trajectory is preserved*. A counterparty's trust score yesterday is an audit fact, not a stale value. L2 facts that depend on trust must cite the score-as-of-that-evidence-time, not the current score.

> **TRU-4 (draft):** Auto-action thresholds are typed by *(action class, user authority class, counterparty trust score)*. The threshold table is part of the worldview, not a configuration value. Example shape:
>
> | Action class | Min trust for auto | Min trust for flag-and-review | Below this: blocked |
> |---|---|---|---|
> | Match invoice | 0.5 | 0.2 | <0.2 |
> | Auto-pay <$1K | 0.8 | 0.5 | <0.5 |
> | Auto-pay $1K–$10K | 0.9 | 0.7 | <0.7 |
> | Auto-pay >$10K | (none — always human) | 0.8 | <0.8 |
>
> The numbers are placeholders; the *shape* of the table is the axiom.

> **TRU-5 (draft):** Trust degrades on bad outcomes faster than it grows on good ones. A single dispute resolved against the supplier moves the score down by Δ_bad; a clean reconciliation moves it up by Δ_good where Δ_bad > Δ_good (default ratio: 3×). This is opinionated and is the encoding of *"trust takes years to build, seconds to lose."*

> **TRU-6 (draft):** Trust does not transit relationships unmodified. When a recharge chain (RCG-1) involves multiple counterparties, the chain's effective trust is **min** across the chain (per RCG-5), not average. This prevents a trusted endpoint from laundering trust for an untrusted intermediary.

## What this axiom buys you

- **Variance explanation as a typed answer**, not free text. *"Why is supplier-X auto-reconciling at 99% but supplier-Y at 60%?"* — answer: their TRU vectors differ on dimensions (b) and (d), here are the underlying evidence trails, the L2 cites it.
- **Policy-as-data**, not policy-as-prompt. *"Is this agent allowed to auto-pay this invoice?"* is a typed lookup against TRU-4, not an LLM judgment. Answers are reproducible and auditable.
- **Behavioral memory**. The system *learns* whom to trust without ML — the score is a deterministic function of evidence, recomputable, replayable.
- **Compliance-as-product** is a derivative of TRU. Sanctions check failure → dimension (f) drops → trust collapses → action class blocked. No special-case code path; the worldview enforces it through the threshold table.

## L2 projection rule (worked)

```
L2_action_decision(action, agent, counterparty) = lookup(
  TRU-4 table,
  action_class = classify(action),
  agent_authority = lookup(agent.policy),
  trust_score = compute_trust(counterparty, as_of=now())
) ∈ { auto, review, block }
```

The L2 always cites the trust score that was used and the threshold row that decided. If either changes later, the historical decision remains queryable as it was made.

## Anti-pattern this axiom prevents

> *Treating "trusted vendor" as a boolean flag set by an admin in a settings panel.* This is the default for every accounting package and CRM. It fails because:
> - it doesn't decay or grow with evidence;
> - it doesn't surface *why* the system is treating two vendors differently;
> - it can't distinguish risk classes (auto-pay $50 vs $50K);
> - it makes audit answers depend on "who set the flag and when," which is recoverable only if the audit log was built specifically for it.

By making trust a typed score with a cited derivation, all four failures dissolve.

## Open questions

- **Cold-start trust.** What's the trust score of a brand-new counterparty with no history? Lean toward: a *prior* derived from class (industry, jurisdiction, legal form), not zero — but the prior must be cited as an axiom, not a magic number.
- **Manual override.** When <the CFO> says *"I trust this supplier, override the score"* — does that write a manual evidence node into the trust graph (preserving the typed-derivation property) or override the score directly (breaking the typed-derivation property)? Strong opinion: the former. Manual trust is just another evidence dimension with weight = however much <the CFO>'s authority carries in the policy.
- **Cross-customer trust transfer.** If Persofi sees the same supplier across multiple <client-corp> customers, does the trust score generalize across the network or stay per-customer? Strong opinion: stay per-customer by default; aggregate only with explicit consent, because privacy and competitive dynamics in a multi-tenant system require it.
- **Trust on the customer side.** Persofi has a buyer-side view through <client-corp>. The mirror axiom for *customer trust* (does this client pay on time, do they dispute fairly) needs writing, but the shape is the same as TRU-1..6 with the role reversed. v0 punts.
