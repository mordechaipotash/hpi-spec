"""End-to-end smoke test of the HPI v0.1 reference implementation.

Exercises the full happy path:
  1. Substrate-holder issues a token to an agent for OBL+RCG read scope
  2. Agent consumes the token to query axioms; data is filtered to scope
  3. Audit events accrue in the substrate-holder's L0 store
  4. Substrate-holder queries their own audit trail
  5. Substrate-holder revokes a token; subsequent consumption fails
  6. Citation-chain validator rejects an axiom with unresolvable cites

Plus a few negative tests:
  - scope violation refused
  - replay of consumed token refused
  - revoked token refused
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from hpi.citations import validate_axiom_or_raise
from hpi.server import HpiServer
from hpi.storage import FilesystemL0BlobStore, InMemoryL1TypedStore
from hpi.tokens import TokenIssuer, TokenVerifier
from hpi.types import (
    AuditEventType,
    AxiomEntity,
    AxiomFamily,
    L0Entity,
    LocalBacking,
    ScopeRequest,
    UpstreamStatus,
)


@pytest.fixture
def server(tmp_path: Path) -> HpiServer:
    """Build a fresh HpiServer with all in-memory/temp-filesystem stores."""
    from hpi.tokens import generate_keypair
    private_key, public_key = generate_keypair()
    issuer = TokenIssuer(issuer_did="did:web:alice.example", private_key=private_key)
    verifier = TokenVerifier(
        public_keys={issuer.kid: public_key},
        expected_audience="https://hpi.alice.example/v0",
    )
    l0 = FilesystemL0BlobStore(tmp_path / "l0")
    l1 = InMemoryL1TypedStore()
    return HpiServer(
        issuer=issuer,
        verifier=verifier,
        l0_store=l0,
        l1_store=l1,
        runtime_url="https://hpi.alice.example/v0",
    )


def _seed_axioms(server: HpiServer) -> None:
    """Seed L0 and L1 with one obligation traced to source evidence."""
    # L0 — primary evidence (a fictitious supplier invoice)
    evidence = L0Entity(
        id="evidence-DE-INV-87332",
        type="invoice_pdf",
        backing=(LocalBacking(path="evidence-DE-INV-87332.pdf"),),
        creator="did:web:de-vendor.example",
        ingester="did:web:alice.example",
        fetched_at=datetime(2026, 4, 18, 9, 14, tzinfo=timezone.utc),
        upstream_status=UpstreamStatus.LIVE,
    )
    server.l0_store.put(evidence, content=b"%PDF-1.4 stub")

    # L1+/L2 — typed obligation citing the L0 evidence
    obligation = AxiomEntity(
        family=AxiomFamily.OBL,
        axiom_id="OBL:o-2026-04-18-DE-87332",
        predicate={"amount": "4800.00", "currency": "EUR", "state": "matched"},
        provenance=("evidence-DE-INV-87332",),
        issuer="did:web:alice.example",
    )
    server.l1_store.put_axiom(obligation)


def test_full_happy_path(server: HpiServer) -> None:
    """Issue → consume → verify scoped data returned → audit accrues."""
    _seed_axioms(server)

    # 1. Agent requests context — auto-approved (no callback)
    issued = server.request_context(
        agent_did="did:agent:claude-instance-7afe",
        purpose="reconcile-supplier-statement",
        purpose_text="Alice asked agent to reconcile DE vendor April statement",
        scope=ScopeRequest(
            axiom_families=("OBL",),
            layers=("L1", "L2"),
            actions=("read",),
        ),
        expiry_seconds=3600,
    )
    assert "token" in issued
    assert issued["approved_scope"]["axiom_families"] == ("OBL",) or \
           list(issued["approved_scope"]["axiom_families"]) == ["OBL"]

    # 2. Agent consumes the token to query OBL axioms
    result = server.consume_token(
        token_jwt=issued["token"],
        action={"type": "query_axioms", "filters": {"family": "OBL"}},
    )
    assert "data" in result
    assert len(result["data"]) == 1
    assert result["data"][0]["axiom_id"] == "OBL:o-2026-04-18-DE-87332"

    # 3. Audit events for both issuance and consumption
    audit = server.audit_query(caller_did="did:web:alice.example")
    audit_types = {e["type"] for e in audit["events"]}
    assert AuditEventType.TOKEN_ISSUED.value in audit_types
    assert AuditEventType.TOKEN_CONSUMED.value in audit_types


def test_replay_of_consumed_token_refused(server: HpiServer) -> None:
    """Single-use semantics — re-presenting a consumed jti must fail."""
    _seed_axioms(server)
    issued = server.request_context(
        agent_did="did:agent:test",
        purpose="test",
        purpose_text="test",
        scope=ScopeRequest(axiom_families=("OBL",), layers=("L1",), actions=("read",)),
    )
    server.consume_token(
        token_jwt=issued["token"],
        action={"type": "query_axioms"},
    )
    # Replay
    replay = server.consume_token(
        token_jwt=issued["token"],
        action={"type": "query_axioms"},
    )
    assert "error" in replay


def test_scope_violation_refused(server: HpiServer) -> None:
    """Action outside scope must fail."""
    _seed_axioms(server)
    issued = server.request_context(
        agent_did="did:agent:test",
        purpose="test",
        purpose_text="test",
        scope=ScopeRequest(axiom_families=("OBL",), layers=("L1",), actions=("read",)),
    )
    # Attempt write — out of scope
    result = server.consume_token(
        token_jwt=issued["token"],
        action={"type": "write_axiom", "payload": {}},
    )
    assert "error" in result


def test_revocation_refuses_consumption(server: HpiServer) -> None:
    """Revoked token must be refused."""
    _seed_axioms(server)
    issued = server.request_context(
        agent_did="did:agent:test",
        purpose="test",
        purpose_text="test",
        scope=ScopeRequest(axiom_families=("OBL",), layers=("L1",), actions=("read",)),
    )
    # Extract jti so we can revoke
    import jwt as _jwt
    decoded = _jwt.decode(issued["token"], options={"verify_signature": False})
    jti = decoded["jti"]

    server.revoke_token(jti=jti, reason="user-initiated")
    result = server.consume_token(
        token_jwt=issued["token"],
        action={"type": "query_axioms"},
    )
    assert "error" in result


def test_audit_query_unauthorized_caller_refused(server: HpiServer) -> None:
    """audit_query restricted to substrate-holder per SPEC §5.2.4."""
    result = server.audit_query(caller_did="did:agent:not-the-holder")
    assert "error" in result
    assert result["error"] == "unauthorized"


def test_citation_validator_accepts_valid_chain(server: HpiServer) -> None:
    """Axiom whose provenance resolves to L0 evidence passes validation."""
    _seed_axioms(server)
    obligation = server.l1_store.get_axiom("OBL:o-2026-04-18-DE-87332")
    root_l0 = validate_axiom_or_raise(obligation, server.l0_store, server.l1_store)
    assert root_l0 == {"evidence-DE-INV-87332"}


def test_citation_validator_rejects_unresolvable_cites(server: HpiServer) -> None:
    """Axiom whose provenance points at non-existent id must be rejected."""
    fabricated = AxiomEntity(
        family=AxiomFamily.OBL,
        axiom_id="OBL:fabricated",
        predicate={"amount": "999"},
        provenance=("nonexistent-evidence-id",),
        issuer="did:web:alice.example",
    )
    server.l1_store.put_axiom(fabricated)

    with pytest.raises(ValueError, match="citation validation failed"):
        validate_axiom_or_raise(fabricated, server.l0_store, server.l1_store)


def test_citation_validator_rejects_empty_provenance(server: HpiServer) -> None:
    """Axiom with no provenance violates cite-or-die."""
    bare = AxiomEntity(
        family=AxiomFamily.OBL,
        axiom_id="OBL:bare",
        predicate={},
        provenance=(),
        issuer="did:web:alice.example",
    )
    server.l1_store.put_axiom(bare)

    with pytest.raises(ValueError, match="cite-or-die"):
        validate_axiom_or_raise(bare, server.l0_store, server.l1_store)
