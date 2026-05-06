"""Token issuance, verification, and revocation.

Functional subset of the HPI runtime — this module is meant to actually run
end-to-end with no MCP / no storage / no audit dependencies. The TokenIssuer
and TokenVerifier are the load-bearing primitives; everything else in the
runtime is wiring around these two.
"""
from __future__ import annotations

import time
import uuid
from dataclasses import asdict, replace
from datetime import datetime
from typing import Any

import jwt as pyjwt
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    PublicFormat,
)

from hpi.types import (
    Scope,
    ScopeRequest,
    Token,
    TokenClaims,
)


# ─── Errors ──────────────────────────────────────────────────────────────────


class HpiTokenError(Exception):
    """Base for token errors."""


class TokenExpired(HpiTokenError):
    pass


class TokenConsumed(HpiTokenError):
    pass


class TokenRevoked(HpiTokenError):
    pass


class SignatureInvalid(HpiTokenError):
    pass


class ScopeViolation(HpiTokenError):
    pass


class AudienceMismatch(HpiTokenError):
    pass


# ─── Key generation ──────────────────────────────────────────────────────────


def generate_keypair() -> tuple[bytes, bytes]:
    """Generate a fresh Ed25519 keypair. Returns (private_pem, public_pem) bytes.

    For testing only. Production runtimes should use a HSM, hardware token,
    or threshold signature scheme. The key custody axiom (SPEC §7.7) forbids
    runtime providers from holding user keys in plaintext.
    """
    priv = Ed25519PrivateKey.generate()
    priv_pem = priv.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.PKCS8,
        encryption_algorithm=NoEncryption(),
    )
    pub_pem = priv.public_key().public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo,
    )
    return priv_pem, pub_pem


# ─── Issuer ──────────────────────────────────────────────────────────────────


class TokenIssuer:
    """Issues HPI tokens. Holds the substrate-holder's private signing key.

    In production, the private key MUST be held by the substrate-holder, not
    the runtime provider (per SPEC §7.7 anti-pattern). This in-memory class is
    for testing and self-hosted runtimes.
    """

    def __init__(
        self,
        issuer_did: str,
        private_key: bytes,
        kid: str = "hpi-v0-key-1",
    ) -> None:
        self.issuer_did = issuer_did
        self.kid = kid
        self._private_key_pem = private_key

    def issue(
        self,
        agent_did: str,
        audience: str,
        scope: ScopeRequest,
        purpose: str,
        purpose_text: str,
        expiry_seconds: int = 3600,
        single_use: bool = True,
        delegation: str = "forbid",
    ) -> Token:
        """Issue a signed token. Caller is responsible for policy enforcement
        (humans approving, scope narrowing, etc.) BEFORE calling this method.
        This method just signs whatever it's given.
        """
        now = int(time.time())
        jti = str(uuid.uuid4())
        claims = TokenClaims(
            iss=self.issuer_did,
            sub=agent_did,
            aud=audience,
            iat=now,
            exp=now + expiry_seconds,
            jti=jti,
            scope=scope.to_scope(),
            purpose=purpose,
            purpose_text=purpose_text,
            single_use=single_use,
            delegation=delegation,  # type: ignore[arg-type]
            version="0",
        )
        payload: dict[str, Any] = {
            "iss": claims.iss,
            "sub": claims.sub,
            "aud": claims.aud,
            "iat": claims.iat,
            "exp": claims.exp,
            "jti": claims.jti,
            "hpi": {
                "version": claims.version,
                "scope": _scope_to_dict(claims.scope),
                "purpose": claims.purpose,
                "purpose_text": claims.purpose_text,
                "single_use": claims.single_use,
                "delegation": claims.delegation,
            },
        }
        signed = pyjwt.encode(
            payload,
            self._private_key_pem,
            algorithm="EdDSA",
            headers={"kid": self.kid},
        )
        return Token(claims=claims, jwt=signed)


# ─── Verifier ────────────────────────────────────────────────────────────────


class TokenVerifier:
    """Verifies HPI tokens, enforces single-use, checks revocation list.

    Runtime-side state:
      - public_keys: kid -> public key PEM (multiple supported for rotation)
      - consumed_jti: set of jti values that have been consumed
      - revoked_jti: set of jti values that have been revoked

    In production, consumed_jti and revoked_jti should be persisted (sqlite,
    redis, sqlite WAL) — in-memory sets here are for testing only.
    """

    def __init__(
        self,
        public_keys: dict[str, bytes],
        expected_audience: str | None = None,
    ) -> None:
        self.public_keys = public_keys
        self.expected_audience = expected_audience
        self.consumed_jti: set[str] = set()
        self.revoked_jti: set[str] = set()

    def verify(self, jwt_str: str) -> Token:
        """Verify signature, expiry, single-use, revocation, audience.

        Raises HpiTokenError subclass on failure.
        """
        # Header inspection — what kid signed this?
        try:
            unverified_header = pyjwt.get_unverified_header(jwt_str)
        except pyjwt.DecodeError as e:
            raise SignatureInvalid(f"malformed JWT header: {e}") from e

        kid = unverified_header.get("kid")
        if kid is None or kid not in self.public_keys:
            raise SignatureInvalid(f"unknown kid: {kid!r}")

        public_key = self.public_keys[kid]

        # Verify signature + standard claims
        try:
            payload = pyjwt.decode(
                jwt_str,
                public_key,
                algorithms=["EdDSA"],
                audience=self.expected_audience if self.expected_audience else None,
                options={
                    "require": ["iss", "sub", "aud", "iat", "exp", "jti"],
                    "verify_aud": self.expected_audience is not None,
                },
            )
        except pyjwt.ExpiredSignatureError as e:
            raise TokenExpired(str(e)) from e
        except pyjwt.InvalidAudienceError as e:
            raise AudienceMismatch(str(e)) from e
        except pyjwt.InvalidSignatureError as e:
            raise SignatureInvalid(str(e)) from e
        except pyjwt.PyJWTError as e:
            raise SignatureInvalid(str(e)) from e

        jti = payload["jti"]

        # Single-use enforcement
        if jti in self.consumed_jti:
            raise TokenConsumed(f"jti {jti} already consumed")

        # Revocation check
        if jti in self.revoked_jti:
            raise TokenRevoked(f"jti {jti} revoked")

        # Reconstruct typed claims
        hpi = payload.get("hpi", {})
        scope = _scope_from_dict(hpi.get("scope", {}))
        claims = TokenClaims(
            iss=payload["iss"],
            sub=payload["sub"],
            aud=payload["aud"],
            iat=payload["iat"],
            exp=payload["exp"],
            jti=jti,
            scope=scope,
            purpose=hpi.get("purpose", ""),
            purpose_text=hpi.get("purpose_text", ""),
            single_use=hpi.get("single_use", True),
            delegation=hpi.get("delegation", "forbid"),
            version=hpi.get("version", "0"),
        )
        return Token(claims=claims, jwt=jwt_str)

    def mark_consumed(self, jti: str) -> None:
        """Mark a token as consumed. Called after successful action by the runtime."""
        self.consumed_jti.add(jti)

    def revoke(self, jti: str) -> None:
        """Revoke a token. Called by substrate-holder via hpi.revoke_token."""
        self.revoked_jti.add(jti)

    def check_scope(self, token: Token, requested_action: dict[str, Any]) -> None:
        """Verify the requested action is within the token's scope.

        v0 only checks `axiom_families` and `actions`. v0.1 will check
        axiom_ids and layers more rigorously.
        """
        action_type: str = requested_action.get("type", "")
        # Heuristic mapping: action type "query_obligations" implies family "OBL"
        # and action verb "read". Production runtimes need a registry.
        family_hint = _action_to_family(action_type)
        action_verb = _action_to_verb(action_type)

        if family_hint and family_hint not in token.claims.scope.axiom_families:
            raise ScopeViolation(
                f"action {action_type!r} requires family {family_hint!r}, "
                f"not in scope {token.claims.scope.axiom_families}"
            )
        if action_verb and action_verb not in token.claims.scope.actions:
            raise ScopeViolation(
                f"action {action_type!r} requires verb {action_verb!r}, "
                f"not in scope {token.claims.scope.actions}"
            )


# ─── Helpers ────────────────────────────────────────────────────────────────


def _scope_to_dict(scope: Scope) -> dict[str, list[str]]:
    return {
        "axiom_families": list(scope.axiom_families),
        "axiom_ids": list(scope.axiom_ids),
        "layers": list(scope.layers),
        "actions": list(scope.actions),
    }


def _scope_from_dict(d: dict[str, Any]) -> Scope:
    return Scope(
        axiom_families=tuple(d.get("axiom_families", [])),
        axiom_ids=tuple(d.get("axiom_ids", [])),
        layers=tuple(d.get("layers", [])),
        actions=tuple(d.get("actions", [])),
    )


def _action_to_family(action_type: str) -> str | None:
    """Map an action verb to its axiom family. v0 heuristic only.

    Production runtimes should use an action registry where each registered
    action declares its family + verb explicitly.
    """
    prefix_map = {
        "query_obligations": "OBL",
        "list_obligations": "OBL",
        "query_recharges": "RCG",
        "query_trust": "TRU",
        "query_patents": "PAT",
    }
    return prefix_map.get(action_type)


def _action_to_verb(action_type: str) -> str | None:
    if action_type.startswith(("query_", "list_", "get_", "read_")):
        return "read"
    if action_type.startswith(("write_", "create_", "update_", "delete_")):
        return "write"
    if action_type.startswith("propose_"):
        return "propose"
    return None
