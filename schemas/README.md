# HPI v0 JSON Schemas — placeholder for v0.1

**Status:** v0.1 scope. This directory is intentionally minimal at v0.

## Why these are not in v0

The Stenberg-predicted critique is sharp: *"The wire format section says HPI 'extends MCP with HPI-specific methods.' I can't implement this. Where are the method names? The parameter schemas? The error codes? Prose is not a protocol."*

This critique lands. HPI v0 specifies the wire format primarily in prose with structured JSON examples. Machine-readable JSON Schema documents are scope for v0.1.

## What v0.1 will ship in this directory

For each of the following, a JSON Schema 2020-12 document with normative `$id`, `$schema`, `title`, `description`, and a complete property+required specification:

- `token.schema.json` — the HPI token envelope (extending JWT structure with `hpi` claim shape from SPEC §4.2)
- `request_context.schema.json` — `hpi.request_context` method arguments + return shapes
- `consume_token.schema.json` — `hpi.consume_token` method arguments + return shapes (success + each error case)
- `revoke_token.schema.json` — `hpi.revoke_token` method
- `audit_query.schema.json` — `hpi.audit_query` method
- `discovery.schema.json` — `/.well-known/hpi.json` document shape
- `revocation_list.schema.json` — `/.well-known/hpi/revocations.json` document shape
- `audit_event.schema.json` — the L0 audit-event types: `hpi_token_issued`, `hpi_token_consumed`, `hpi_token_denied`, `hpi_token_revoked`
- `axiom_OBL.schema.json` — OBL axiom family entity shape (per `axioms/OBL-obligations.md`)
- `axiom_RCG.schema.json` — RCG family
- `axiom_TRU.schema.json` — TRU family
- `axiom_PAT.schema.json` — PAT family

Each schema MUST be:
- Valid JSON Schema 2020-12 (verified by the schema-validate.yml GitHub Actions workflow)
- Cross-referenced from the corresponding SPEC.md or axioms/ document
- Accompanied by at least one positive and one negative example in `schemas/examples/`

## Method registry (per Stenberg)

A normative method registry analogous to IANA's HTTP method registry will live at `schemas/method-registry.json`. v0 has 5 methods: `hpi.request_context`, `hpi.consume_token`, `hpi.revoke_token`, `hpi.audit_query`, `hpi.discover`. Future method additions go through the governance process per `governance/CHARTER.md`.

## v0.1 timeline

- Week 1-2 of Phase 3 (post-publication): full schema set drafted
- Week 3 of Phase 3: schema-validate GitHub Action transitions from no-op stub to enforcing
- Week 4 of Phase 3: positive + negative example test suite
- v0.1 ships with `schemas/` + `governance/CHARTER.md` Phase 2 working-group launched

This file documents the gap honestly to address the Stenberg-predicted "deployment-tail specification failure" — implementations cannot claim HPI v0 conformance based on prose alone. A v0 implementor who wants conformance NOW must:

1. Ship against the prose spec
2. Publish their implementation's interpretation of every prose-defined surface
3. Submit interpretations for review when the v0.1 schemas land
4. Adjust to match canonical schemas when published

This is not ideal. The honest alternative is to acknowledge that v0 is a spec without machine-readable schemas, which limits the strength of "HPI v0-conformant" claims to "implements the prose as I read it."
