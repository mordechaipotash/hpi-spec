# HPI v0.1 Reference Implementation — Python

**Status:** v0.1 working reference. **11 tests passing**. Functional for end-to-end testing; not production-hardened.
**Conformance:** v0 of [HPI spec](../../SPEC.md). Implements §4 token handoff + §5 wire format + §6 reference targets.

## What's working

- ✅ Token issue / verify / consume / revoke (Ed25519 / EdDSA JWT)
- ✅ Single-use semantics with `jti` consumption tracking
- ✅ Scope enforcement at consumption (axiom families, layers, actions)
- ✅ Audit trail emitted to substrate-holder's L0 store (audit-as-substrate-stream)
- ✅ Audit query with substrate-holder authorization check (per SPEC §5.2.4)
- ✅ Filesystem L0 blob store (content-addressed; entity-id + content-hash dual indexing)
- ✅ In-memory L1 typed store with family + valid-at filtering
- ✅ HpiServer with all 4 required methods (`request_context`, `consume_token`, `revoke_token`, `audit_query`) + optional `discover`
- ✅ **Citation-chain validator** (Karpathy-flagged enforcement of cite-or-die discipline)
- ✅ End-to-end smoke test: issue → consume → query → revoke → re-consume fails
- ✅ Negative tests: scope violation, replay refusal, unauthorized audit query, citation-chain rejection

## What's stubbed (v0.2+ hardening)

- Multi-instance JTI consensus (currently single-process; production needs Raft/Paxos per THREAT-MODEL §7.2)
- Encryption at rest (filesystem store is plaintext for testing; production must encrypt with substrate-holder-controlled keys per THREAT-MODEL §6.3)
- HTTP transport + actual MCP wire (currently in-process method calls; trivial to wrap)
- Discovery endpoint serving (function exists; HTTP scaffolding TBD)
- Revocation list endpoint serving (`.well-known/hpi/revocations.json`)
- W3C VC token format (v0.1 migration path per SPEC §4.2)
- SD-JWT / BBS+ for selective disclosure (Allen-flagged for v0.1)
- Threshold signatures + HSM integration (THREAT-MODEL §6.3 Pattern C)
- JSON Schema validation at API surface (Stenberg-flagged for v0.1)
- Conformance test suite covering §7 anti-patterns as negative tests

## Quick start

```bash
cd reference-impl/python
python3.14 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest

# Run all tests
python -m pytest tests/

# Or run individual tests with verbose output
python -m pytest tests/test_e2e.py::test_full_happy_path -v
python -m pytest tests/test_e2e.py::test_citation_validator_rejects_unresolvable_cites -v
```

## Test inventory

`tests/test_tokens.py` (3 tests): low-level token primitives
- `test_issue_then_verify_round_trip`
- `test_consumed_jti_is_refused`
- `test_revoked_jti_is_refused`

`tests/test_e2e.py` (8 tests): full pipeline
- `test_full_happy_path` — issue → consume → query → audit accrues
- `test_replay_of_consumed_token_refused` — single-use semantics
- `test_scope_violation_refused` — write attempt on read-only token
- `test_revocation_refuses_consumption` — revoke + re-consume = error
- `test_audit_query_unauthorized_caller_refused` — auth check works
- `test_citation_validator_accepts_valid_chain` — cite-or-die when valid
- `test_citation_validator_rejects_unresolvable_cites` — cite-or-die enforcement
- `test_citation_validator_rejects_empty_provenance` — bare claim rejected

## Architecture (microHPI compactness — Karpathy's request)

Core protocol primitives in ~1100 lines of Python:

```
hpi/
├── __init__.py       (31 lines)  exports
├── types.py         (189 lines)  L0Entity, Scope, Token, AxiomEntity, AuditEvent
├── tokens.py        (335 lines)  TokenIssuer, TokenVerifier, single-use + revocation
├── storage.py       (~190 lines) L0BlobStore + L1TypedStore (FilesystemL0 + InMemoryL1)
├── audit.py         (~145 lines) emit_audit_event, query_audit
├── server.py        (~225 lines) HpiServer with §5.2 method surface
├── citations.py     (109 lines)  cite-or-die discipline enforcement
├── discovery.py      (32 lines)  .well-known/hpi.json builder
└── axioms/
    ├── __init__.py
    └── obl.py                    OBL family schema + validators
```

**The microHPI design aesthetic:** every primitive should fit in a head. If a function is hard to understand, decompose it. Per Karpathy's "Recipe for Training Neural Networks": *"neural net training fails silently."* Same applies to protocol implementations — opaque code fails in opaque ways.

The **irreducible token + storage + audit core** is closer to ~300 lines of substantive logic (the rest is type definitions, error classes, and serialization). Anyone wanting to understand HPI mechanically can read tokens.py + storage.py + audit.py + server.py in 30 minutes.

## How to extend

To add a new axiom family (e.g., `MED` for medical-vertical):

1. Document the family per the 8-section conformance contract in SPEC §3.3
2. Add `axioms/med.py` with state machine + validators
3. Add `MED` to `AxiomFamily` enum in `types.py`
4. Add tests demonstrating: family-scoped token returns MED axioms, cross-family scope violations refused, citation chains valid

To add a new storage backing (e.g., S3-compatible):

1. Subclass `L0BlobStore` (interface in `storage.py`)
2. Implement `put`, `get`, `get_content`, `iter_entities` (4 methods, ~100 lines)
3. Wire encryption at rest using substrate-holder's key derivation (THREAT-MODEL §6.3 Pattern A)

To run a real network deployment:

1. Wrap `HpiServer` methods in an MCP server (use `mcp` Python package)
2. Or expose via plain HTTP+JSON — each method is a POST to `/v0/<method-name>`
3. Serve `.well-known/hpi.json` via existing web server (output of `HpiServer.discover()`)
4. Serve `.well-known/hpi/revocations.json` via the same (TODO: scaffold a flask app for this)

## What this proves

The HPI protocol primitives are **implementable**. The §4 token handoff + §5 wire format + cite-or-die enforcement + audit-as-substrate-stream compose into a working runtime in ~1100 lines. **The next sprint is hardening (encryption, multi-instance, MCP wire) — not invention.**

This addresses:

- **Karpathy's "200-line version" challenge:** Close to 1100 for the full surface; ~300 lines for the irreducible token + storage + audit core. Compactness aesthetic preserved.
- **Karpathy's verifiability framework:** Citation-chain validator runs at API surface, rejecting axioms whose `provenance` does not resolve. Cite-or-die is no longer advisory.
- **Stenberg's implementability challenge:** *"I can't implement this from prose alone."* Now you can. Method names, parameter shapes, error codes are concrete. JSON Schemas remain v0.1 scope.
- **Schneier's audit-as-substrate-stream design:** *"the substrate-holder owns their own audit, full stop."* Verified by `test_full_happy_path`'s assertion that audit events accrue in the substrate-holder's L0 store, not in any runtime-side log.
- **Doctorow's enshittification critique (partial):** Anti-capture clauses from SPEC §7.10–§7.12 are not yet enforced by this implementation; conformance test suite for them is v0.2 scope. The wire-format primitives are correct; enforcement-at-implementation is the next layer.

## Compatibility note

This Python reference is **indicative**, not normative. The normative spec is `SPEC.md`. If this implementation diverges from `SPEC.md`, the spec is correct and this code is wrong. Pull requests welcome on either side.

## License

Apache 2.0 (planned for spec); MIT (planned for this implementation). License files pending v0 publication gate.
