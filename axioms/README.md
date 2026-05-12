# Axioms — what HPI ships as a worldview

> *"You shipped a database. We ship a worldview."*

This folder contains the **v0 axiom families** — typed worldview claims about specific domains, against which any L2 synthesis is judged. Each family is a small set of typed sub-axioms with explicit derivation rules.

## Why this folder exists, not just a schema

A schema says *what is*. An axiom family says *how things relate, what's allowed, what's derived* — and it encodes an **opinion** about how the domain is shaped. Schemas can be auto-generated from a database; axiom families must be authored. **The axiom family is the load-bearing artifact; the schema is plumbing.**

## v0 axiom families

| File | Family | Status |
|---|---|---|
| [`OBL-obligations.md`](OBL-obligations.md) | **OBL** — Obligations | drafted |
| [`RCG-recharges.md`](RCG-recharges.md) | **RCG** — Recharges | drafted |
| [`TRU-trust.md`](TRU-trust.md) | **TRU** — Trust / counterparty ratings | drafted |
| [`PAT-patents.md`](PAT-patents.md) | **PAT** — Patents (Reference Domain Ontology) | drafted |

The OBL/RCG/TRU families are drawn from finance-vertical operations (production deployment at one pilot). PAT is the v0.1 Reference Domain Ontology that demonstrates how a domain-specific Ontology rides on HPI's protocol layer.

See [`../examples/01-obligation-end-to-end.md`](../examples/01-obligation-end-to-end.md) for a single obligation traced L0 → L1 → L2 with the typed projection rule made explicit.

## Anti-rules

- **Do not write a generic ontology** (place / time / person / event). That's a schema dressed up. The domain-specific opinion is the point.
- **Do not derive an L2 fact that doesn't trace to an axiom in this folder.** If you need to, you've found a missing axiom — add it here first.
- **Do not pre-empt UI here.** UI is downstream. The axiom family answers *"what is true,"* not *"what does the user click."*

## Promotion path

When an axiom is referenced by ≥2 L2 files in a working implementation, it gets a stable ID (`OBL-1`, `RCG-2`, `TRU-1`, etc.) and becomes part of the contract for L2 synthesis. Until then, axioms are draft.

## Adding new axiom families

A new family follows the same structure as OBL/RCG/TRU/PAT:

1. Name (3-letter prefix, e.g., `TAX`, `BAN`, `IPP`)
2. Core axiom (the worldview claim in one sentence)
3. Sub-axioms (typed rules)
4. Allowed state transitions
5. L2 projection rule (worked)
6. What's NOT in this family (boundaries)
7. Open questions

Submit by PR to `hpi-protocol/spec` (org pending — currently `mordechaipotash/hpi-spec`).
