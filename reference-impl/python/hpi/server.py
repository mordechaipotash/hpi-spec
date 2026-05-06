"""HPI MCP server — exposes the four required methods from SPEC §5.2.

SKETCH ONLY — method signatures + TODO bodies. Real wiring to the `mcp`
Python library is the next sprint. The shape here is meant to make that
wiring a 30-minute mechanical translation.

Each method's docstring captures the spec method semantics; the body is a
stub that wires through to tokens, storage, audit, and discovery.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from hpi.audit import emit_audit_event, query_audit
from hpi.storage import L0BlobStore, L1TypedStore
from hpi.tokens import (
    HpiTokenError,
    ScopeViolation,
    Token,
    TokenIssuer,
    TokenVerifier,
)
from hpi.types import (
    AuditEventType,
    ScopeRequest,
)


class HpiServer:
    """In-process HPI runtime. Wraps issuer + verifier + storage + audit.

    Production implementations expose this over MCP transport. v0 sketch only
    provides direct method calls.
    """

    def __init__(
        self,
        issuer: TokenIssuer,
        verifier: TokenVerifier,
        l0_store: L0BlobStore,
        l1_store: L1TypedStore,
        runtime_url: str,
    ) -> None:
        self.issuer = issuer
        self.verifier = verifier
        self.l0_store = l0_store
        self.l1_store = l1_store
        self.runtime_url = runtime_url

    # ─── §5.2.1 hpi.request_context ─────────────────────────────────────

    def request_context(
        self,
        agent_did: str,
        purpose: str,
        purpose_text: str,
        scope: ScopeRequest,
        expiry_seconds: int = 3600,
        approver_callback: Any = None,
    ) -> dict[str, Any]:
        """Agent requests permission to read scoped substrate context.

        Per SPEC §4.4 step 2-5:
        - Check policy (skipped for v0 — assume manual approve)
        - If no policy match, present to substrate-holder via approver_callback
        - Issue signed token, emit audit event
        """
        # TODO v0.1: policy engine integration
        if approver_callback:
            approved_scope = approver_callback(agent_did, purpose, purpose_text, scope, expiry_seconds)
            if approved_scope is None:
                emit_audit_event(
                    self.l0_store,
                    self.issuer.issuer_did,
                    AuditEventType.TOKEN_DENIED,
                    {
                        "agent_did": agent_did,
                        "requested_scope": scope.__dict__,
                        "denial_reason": "user-denied",
                    },
                )
                return {"error": "denied", "reason": "user-denied"}
            scope = approved_scope

        token = self.issuer.issue(
            agent_did=agent_did,
            audience=self.runtime_url,
            scope=scope,
            purpose=purpose,
            purpose_text=purpose_text,
            expiry_seconds=expiry_seconds,
        )

        emit_audit_event(
            self.l0_store,
            self.issuer.issuer_did,
            AuditEventType.TOKEN_ISSUED,
            {
                "jti": token.jti,
                "agent_did": agent_did,
                "scope": token.claims.scope.__dict__,
                "purpose": purpose,
                "expiry": token.claims.exp,
            },
        )

        return {
            "token": token.jwt,
            "issued_at": datetime.fromtimestamp(token.claims.iat, tz=timezone.utc).isoformat(),
            "expires_at": token.expires_at.isoformat(),
            "approved_scope": token.claims.scope.__dict__,
        }

    # ─── §5.2.2 hpi.consume_token ───────────────────────────────────────

    def consume_token(
        self,
        token_jwt: str,
        action: dict[str, Any],
    ) -> dict[str, Any]:
        """Agent presents token to retrieve scoped data.

        Per SPEC §4.4 step 6-8:
        - Verify signature, expiry, single-use, audience
        - Check action against scope
        - Mark consumed
        - Return data filtered to scope
        - Emit audit event
        """
        try:
            token = self.verifier.verify(token_jwt)
            self.verifier.check_scope(token, action)
        except HpiTokenError as e:
            return {"error": type(e).__name__, "reason_text": str(e)}

        # Execute the action against L1 store, filtered to scope
        data: list = []
        action_type = action.get("type", "")
        if action_type == "query_axioms":
            family_filter = action.get("filters", {}).get("family")
            scope_families = set(token.claims.scope.axiom_families)
            scope_ids = set(token.claims.scope.axiom_ids)
            for axiom in self.l1_store.query_axioms(family=family_filter):
                if scope_families and axiom.family.value not in scope_families:
                    continue
                if scope_ids and axiom.id not in scope_ids:
                    continue
                from dataclasses import asdict
                d = asdict(axiom)
                d["family"] = axiom.family.value
                data.append(d)

        self.verifier.mark_consumed(token.jti)

        audit_id = emit_audit_event(
            self.l0_store,
            self.issuer.issuer_did,
            AuditEventType.TOKEN_CONSUMED,
            {
                "jti": token.jti,
                "agent_did": token.claims.sub,
                "action": action,
                "data_returned_size": len(data),
            },
        )

        return {
            "data": data,
            "consumed_at": datetime.now(timezone.utc).isoformat(),
            "audit_event_id": audit_id,
        }

    # ─── §5.2.3 hpi.revoke_token ────────────────────────────────────────

    def revoke_token(self, jti: str, reason: str) -> dict[str, Any]:
        """Substrate-holder revokes an active token."""
        # TODO v0.1: signature verification on revocation request itself
        self.verifier.revoke(jti)
        audit_id = emit_audit_event(
            self.l0_store,
            self.issuer.issuer_did,
            AuditEventType.TOKEN_REVOKED,
            {"jti": jti, "reason": reason, "revoked_by": self.issuer.issuer_did},
        )
        return {
            "revoked_at": datetime.now(timezone.utc).isoformat(),
            "audit_event_id": audit_id,
        }

    # ─── §5.2.4 hpi.audit_query ─────────────────────────────────────────

    def audit_query(
        self,
        since: str | None = None,
        agent_did: str | None = None,
        purpose: str | None = None,
        event_types: list[str] | None = None,
        limit: int = 100,
        caller_did: str | None = None,
    ) -> dict[str, Any]:
        """Substrate-holder queries their own audit trail.

        AUTHENTICATION REQUIRED — only the substrate-holder may query their own audit.
        v0 reference: in-process check that caller_did matches issuer_did.
        v0.1 production: signed challenge-response per SPEC §5.5.
        """
        # Per SPEC §5.2.4 — restricted to the substrate-holder
        if caller_did is not None and caller_did != self.issuer.issuer_did:
            return {"error": "unauthorized", "reason_text": "audit_query restricted to substrate-holder"}

        since_dt = datetime.fromisoformat(since) if since else None
        type_filter = [AuditEventType(t) for t in event_types] if event_types else None

        events = query_audit(
            self.l0_store,
            since=since_dt,
            event_types=type_filter,
            agent_did=agent_did,
            purpose=purpose,
            limit=limit,
        )
        return {
            "events": [
                {
                    "id": e.id,
                    "type": e.type.value,
                    "timestamp": e.timestamp.isoformat(),
                    "fields": e.fields,
                }
                for e in events
            ],
            "next_cursor": None,
        }

    # ─── §5.2.5 hpi.discover (optional) ─────────────────────────────────

    def discover(self) -> dict[str, Any]:
        """Return runtime capabilities."""
        from hpi.discovery import build_discovery_document

        return build_discovery_document(
            issuer_did=self.issuer.issuer_did,
            runtime_url=self.runtime_url,
            supported_axiom_families=["OBL", "RCG", "TRU", "PAT"],
        )
