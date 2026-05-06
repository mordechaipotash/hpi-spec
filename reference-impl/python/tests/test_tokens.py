"""Smoke test for the functional path: issue → verify → consume → re-verify-fails."""
from __future__ import annotations

import pytest

from hpi.tokens import (
    TokenConsumed,
    TokenIssuer,
    TokenRevoked,
    TokenVerifier,
    generate_keypair,
)
from hpi.types import ScopeRequest


@pytest.fixture
def keys() -> tuple[bytes, bytes]:
    return generate_keypair()


@pytest.fixture
def issuer(keys: tuple[bytes, bytes]) -> TokenIssuer:
    priv, _ = keys
    return TokenIssuer(issuer_did="did:web:alice.example", private_key=priv)


@pytest.fixture
def verifier(keys: tuple[bytes, bytes], issuer: TokenIssuer) -> TokenVerifier:
    _, pub = keys
    return TokenVerifier(public_keys={issuer.kid: pub})


def test_issue_and_verify(issuer: TokenIssuer, verifier: TokenVerifier) -> None:
    token = issuer.issue(
        agent_did="did:agent:claude-test",
        audience="https://hpi.alice.example/v0",
        scope=ScopeRequest(axiom_families=["OBL"], layers=["L1"], actions=["read"]),
        purpose="test",
        purpose_text="smoke test",
    )
    verified = verifier.verify(token.jwt)
    assert verified.claims.iss == "did:web:alice.example"
    assert verified.claims.sub == "did:agent:claude-test"
    assert "OBL" in verified.claims.scope.axiom_families
    assert verified.claims.purpose == "test"


def test_single_use_enforced(issuer: TokenIssuer, verifier: TokenVerifier) -> None:
    token = issuer.issue(
        agent_did="did:agent:claude-test",
        audience="https://hpi.alice.example/v0",
        scope=ScopeRequest(axiom_families=["OBL"], actions=["read"]),
        purpose="test",
        purpose_text="single-use test",
    )
    verifier.verify(token.jwt)  # first verification ok
    verifier.mark_consumed(token.jti)
    with pytest.raises(TokenConsumed):
        verifier.verify(token.jwt)  # second use refused


def test_revocation(issuer: TokenIssuer, verifier: TokenVerifier) -> None:
    token = issuer.issue(
        agent_did="did:agent:claude-test",
        audience="https://hpi.alice.example/v0",
        scope=ScopeRequest(axiom_families=["OBL"], actions=["read"]),
        purpose="test",
        purpose_text="revocation test",
    )
    verifier.revoke(token.jti)
    with pytest.raises(TokenRevoked):
        verifier.verify(token.jwt)
