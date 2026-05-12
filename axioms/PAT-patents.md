# Axiom family 4 — Patent lifecycle (PAT)

> **Status:** v0 draft, written 2026-05-01 in response to <the CFO>'s strategic update — *"the bigger strategic piece is building proper patent insights ... a full patent lifecycle view ... allows us to move beyond law firms and start appealing directly to corporates."*

## The opinion

A patent is not a row, a job, an invoice, or a folder of documents. It is **a long-lived legal entity** with its own state machine, jurisdictional fan-out, and obligation-generation schedule that runs for up to 20 years independently of any single transaction. Most accounting and IP-management software treats a patent as a denormalized attribute — a memo field on an invoice, a tag on a `<workflow-system>` job, a column in a CSV. **`<vertical-product>` treats the patent as a first-class node** that *generates* obligations rather than being described by them.

This inversion is the unlock that makes the patent-lifecycle view a *worldview claim*, not a dashboard. **Corporates buy access to the patent graph** — invoices and jobs are the financial tail of the dog. Law firms buy the inverse view (jobs and invoices, with patents as memo) because their billing model is transactional. `<vertical-product>`'s moat is being the only system that holds *both* views in the same ontology and projects the right one for the audience.

## Core axiom

> **PAT-1 (draft):** Every patent is a node in the graph, identified by a typed `patent_identity` triple (jurisdiction, application_number, kind) with stable identity across renewals, transfers, oppositions, and re-examinations. The patent's identity *survives* every event in its lifecycle; events are typed transitions on the same node, never new nodes.

A US patent application 18/123,456 is the same node before and after grant; the same node before and after a maintenance-fee event; the same node before and after assignment to a new owner. **What changes is the patent's state vector, not its identity.**

## Sub-axioms

> **PAT-2 (draft):** A patent's *jurisdictional presence* is a typed set, not a column. A single underlying invention is represented by **a family of patent nodes**, one per jurisdiction, linked by a typed `family` relation (priority claim, PCT national-phase entry, divisional, continuation). The family relation is explicit and enumerable; it is not derivable from text matching on titles or applicant names.

> **PAT-3 (draft):** Patent state evolves through a typed lifecycle:
>
> ```
> drafted → filed → published → examined → granted → maintained → expired
>                       ↓             ↓          ↓          ↓
>                   abandoned    rejected   opposed    lapsed (non-payment)
> ```
>
> Transitions between non-adjacent states are forbidden and require a compensating event (e.g. `revived` from `lapsed`). Each transition is a typed event with required evidence (a filing receipt, an examination report, a maintenance-fee receipt).

> **PAT-4 (draft):** Patent ownership is a typed temporal relation, not a string field. At any instant, a patent has *exactly one* canonical owner (the assignee), but the *historical chain of owners* is preserved as a sequence of typed `assignment` events. Co-ownership is represented as a multi-party assignment with proportions; it is not a comma-separated string.

> **PAT-5 (draft):** **A patent is an obligation generator.** Granted and pending patents emit *expected future obligations* on a schedule determined by jurisdiction-specific lifecycle rules — annuities, maintenance fees, working-statement filings, divisional deadlines. These expected obligations are typed nodes in the graph *before* their corresponding evidence arrives:
>
> ```
> expected_obligation = (
>   patent_id,
>   event_type ∈ {annuity, maintenance, declaration, ...},
>   due_date,
>   estimated_amount (jurisdiction-specific schedule),
>   confidence ∈ [0, 1],
>   resolved_to_obligation_id (null until the upstream evidence lands)
> )
> ```
>
> When real evidence arrives (an agent's invoice, a fee-receipt PDF), it merges into the expected node via the same OBL-3 predicate; the expected node `resolved_to_obligation_id` populates and the expected/actual delta becomes a typed audit fact.
>
> **This is the axiom that powers renewal forecasting.** It also encodes <the CFO>'s *"future renewal forecasting"* ask as an ontology claim, not a feature. Forecasts are derived facts with provenance, not predictions.

> **PAT-6 (draft):** Each prosecution event on a patent is a **recharge candidate** under RCG-1. The vendor (foreign agent) → intermediary (<client-corp>) → final buyer (corporate or law-firm-acting-for-corporate) chain is the canonical patent-prosecution recharge. A patent therefore generates a *sequence of recharges* over its life, each tied to the patent node via a typed `prosecution_recharge` link. **Profit on a patent over its lifetime** is `Σ(margin)` over its prosecution-recharge sequence (RCG-2 + RCG-4 applied chain-by-chain).

> **PAT-7 (draft):** A patent's *strategic value indicators* are derived facts, not opinions. They include: (a) family breadth — count of jurisdictions in the typed family set; (b) prosecution trajectory — count of office actions, citations, examiner art; (c) maintenance commitment — fraction of due maintenance fees paid on time over rolling N years; (d) ownership stability — count of assignments in N years (low = stable, high = traded). Each indicator has a cited derivation rule. Strategic value is not a single number; it's a typed vector. *"Important patent"* is not in the worldview; *"high family-breadth, stable ownership, examined-and-granted in core jurisdictions"* is.

## Allowed states (recap)

```
drafted → filed → published → examined → granted → maintained → expired
                      ↓             ↓          ↓          ↓
                  abandoned    rejected   opposed    lapsed
                                                        ↓
                                                     revived
```

`expired` and `abandoned` are terminal states; `granted`, `maintained`, `lapsed`, `opposed` are non-terminal but the lifecycle ends within ~20 years from priority date regardless.

## What this axiom buys you

- **The full patent lifecycle view, as a worldview claim.** <the CFO>'s *"ownership, countries, filings, prosecution, renewal forecasting"* is not a feature list — it's PAT-1 (identity) + PAT-2 (jurisdictional fan-out) + PAT-3 (state) + PAT-4 (ownership) + PAT-5 (renewal-as-expected-obligation) + PAT-7 (strategic indicators). Each is a typed projection over the patent graph.

- **Direct-to-corporate is suddenly legible.** Corporates ask: *"what's our portfolio's renewal exposure in EP+JP+CN over the next 18 months at current FX?"* The answer is `sum(expected_obligation.estimated_amount where patent.owner=corporate AND patent.jurisdiction ∈ {EP, JP, CN} AND expected_obligation.due_date ∈ next_18_months)` — a typed query against PAT-2 + PAT-5. **Law firms cannot answer this from their billing system.** `<vertical-product>` can answer it from the worldview directly.

- **Renewal forecasting is not ML.** It's a deterministic projection of PAT-5 expected obligations against the jurisdiction-specific fee schedule. Confidence values are typed; surprises are typed (an actual fee differs from expected → audit-trail node, like the €10 `<workflow-system>`/PDF mismatch in OBL-4).

- **Cross-firm portfolio aggregation falls out.** A corporate that uses three different law firms for prosecution sees one view in `<vertical-product>` because the patent identity (PAT-1) survives the firm boundary. Each firm contributes *evidence* about prosecution events; PAT-1 holds the identity; OBL-3 merges across firms by jurisdiction + application_number.

- **Patent-as-collateral.** When PAT-7 strategic indicators are typed and queryable, the patent becomes a financial asset whose *valuation provenance* is auditable. This is what separates `<vertical-product>` from a DOKKA + `<workflow-system>` integration: **DOKKA sees the bills; `<vertical-product>` sees the asset that generated them.**

## L2 projection rule (worked, sketch)

```
L2_patent_view(patent_id) = project(
  patent_node,
  axioms = [PAT-1..7, OBL-3..5, RCG-1..6, TRU-1..6],
  projections = {
    identity:        PAT-1 → (jurisdiction, application_number, kind),
    family:          PAT-2 → set of related patent_ids with typed relations,
    state:           PAT-3 → current state + transition history,
    ownership:       PAT-4 → current owner + assignment chain,
    expected_costs:  PAT-5 → expected_obligations between now and horizon,
    actual_costs:    PAT-6 → resolved prosecution_recharges with margins,
    strategic:       PAT-7 → typed value vector with cited derivations,
    trust_chain:     TRU-6 → min trust across all counterparties seen on this patent
  }
)
```

A `/patents/<id>` route on the Viter app, or a `get_patent(id)` MCP tool, would *be* this projection. The app and the MCP tool render the same projection in different modalities — UI for human eyes, structured response for machine eyes. Both cite the axiom under each fact.

## Anti-pattern this axiom prevents

> *Treating a patent as a memo field on an invoice or a tag on a job.* Every IP-management package does this. It fails because:
> - the patent identity is recoverable only by string-matching across years of invoices;
> - jurisdictional family relations are not derivable;
> - renewal forecasting requires running a separate model with no provenance;
> - ownership chains are lost when assignments aren't formal events;
> - corporates can't answer portfolio questions without exporting to Excel and reconstructing the graph by hand.

By making the patent a first-class node with PAT-1..7, all five failures dissolve.

## What's NOT in this axiom (intentionally)

- **Patent valuation / price estimation.** Out of scope v0. PAT-7 produces typed indicators; pricing is a separate axiom family if it ever matters (PRX-* — pricing — distinct from PAT-*).
- **Patent search / prior-art retrieval.** Different worldview entirely. `<vertical-product>` doesn't do prior-art search.
- **Litigation / opposition strategy.** PAT-3 captures the `opposed` state as a transition; the strategic *response* to opposition is out of scope.
- **Specific examiner-data ingestion.** USPTO PAIR / EPO Register / etc. are L0 evidence sources for PAT-3 transitions; the integration spec is downstream.
- **Trademark, design, copyright.** Different ontologies. Don't conflate.

## Open questions

- **Identity for unpublished applications.** Until publication, jurisdiction issues an application number that may not be public. Internal `<vertical-product>` identity must use a typed surrogate keyed on (filing_date, applicant, our_internal_ref) until the public number lands and merges in. Spec the merge rule.
- **PCT national-phase entry.** A PCT application is a single node until national-phase entry creates jurisdiction-specific children. Are the children new nodes (PAT-1 says no — same identity) or jurisdiction-properties of one node (then PAT-2 typed family is null because the family is one node)? Strong opinion: each national-phase entry creates a sibling node linked by `family.priority_claim`, because the lifecycle (PAT-3) of the EP and US national-phase entries diverges and must be tracked independently. The PCT itself is a separate node with `expired` terminal state at national-phase entry.
- **Cost allocation for shared-family events.** A single inventor-correction filing can apply to a whole family. Does the cost obligation attach to one node, all nodes, or a family-level node? Lean toward: family-level *event*, attached to a typed `family_event` sibling node, with cost-allocation per jurisdiction by typed rule (per-capita, by-importance, by-fee-schedule). v0 punts; needs a real example from <client-corp>'s data.
- **Continuation / divisional cost attribution.** A continuation filing in the US shares costs with its parent. Should the continuation's prosecution_recharge include a fraction attributable to the parent, or are they wholly independent? Strong opinion: independent at the recharge level, but the family relation surfaces both when `get_patent` is asked about either.
- **Lapsed-then-revived state restoration.** PAT-3 allows `revived` from `lapsed`. Does the patent's TRU-3 trajectory restart, or carry forward the pre-lapse trust? Carry forward, with the lapse event itself as a TRU-2 dimension (a) signal (negative).
- **Confidence on PAT-5 expected obligations.** When fee schedules change mid-life, what's the right way to encode the change? Lean toward: the expected obligation has an `as_of` date and a `schedule_version` reference; re-projection at a later date uses the then-current schedule. Audit trail preserves both.

## Promotion path

PAT-* is **draft** until referenced by ≥2 L2 files and confirmed by Mordechai. The first two L2 references should be:

1. The first patent-lifecycle synthesis L2 in `chat-log/by-day/` once a real patent is traced through the worldview (analogous to `04-worked-example-obligation.md` for OBL/RCG).
2. The L2 that documents the first `/patents/<id>` route or `get_patent` MCP tool implementation in `code/`.

Until then, the axioms are draft and the schema must not lock them in concrete (no production migrations until promotion).

## Connection back to the existing families

- **OBL-3** evidence-merge predicate extends naturally: a patent-event evidence node merges into a patent identity by `(jurisdiction, application_number, event_type, event_date)` rather than `(counterparty, reference, amount)`. The shape is the same; the predicate is event-typed.
- **OBL-5** FX freeze applies per-event on a patent. Annuity fees in EP, USD, JPY are each frozen at the date of expected-obligation creation; PAT-5 inherits this.
- **RCG-1..6** is unchanged. PAT-6 reuses RCG without extending it.
- **TRU-1..6** is unchanged. Patents themselves don't have trust scores; the *counterparties seen on the patent* (foreign agents, examiners-as-rejection-rate-signal, opposers) carry trust under TRU.
- **TRU-6** chain-trust applies to PAT-6 prosecution-recharge chains directly.

## What this changes about the to-do list

Section F of the `<client-corp>` CFO's strategic to-do list is reframed:

- **F0 (NEW, prerequisite):** this file lands first.
- **F1** schema migration (`add_patent_lifecycle.sql`) implements PAT-1..4 in storage; expected-obligations table implements PAT-5; prosecution_recharge_links implements PAT-6.
- **F2** `<workflow-system>` ↔ patents join is the OBL-3 evidence-merge for patent-event evidence sources.
- **F3** renewal forecast is a typed query against PAT-5 expected obligations; not ML.
- **F4** direct-to-corporate is the `viter_mcp/` typed projections of PAT-1..7; not a sales doc.

The schema work is real but secondary; the axioms are the contract. **If we ship F1 without F0, the schema is a guess and the L2 will trust an LLM. That's the failure mode this whole repo exists to prevent.**
