"""Audit event emission.

Per SPEC §4.7: every token issuance, consumption, denial, and revocation MUST
be recorded as an L0 entity in the substrate-holder's substrate.

The audit trail is itself a substrate stream. Because it lives in L0, the
substrate-holder owns their own audit. This is the structural inversion of
platform-mediated audit (where the platform owns the log).
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any

from hpi.storage import L0BlobStore
from hpi.types import (
    AuditEvent,
    AuditEventType,
    L0Entity,
    LocalBacking,
    UpstreamStatus,
)


def emit_audit_event(
    store: L0BlobStore,
    issuer_did: str,
    event_type: AuditEventType,
    fields: dict[str, Any],
) -> str:
    """Persist an audit event as an L0 entity in the substrate-holder's substrate.

    Returns the new L0 entity id.
    """
    event_id = f"audit-{uuid.uuid4()}"
    timestamp = datetime.now(timezone.utc)

    event = AuditEvent(
        id=event_id,
        type=event_type,
        timestamp=timestamp,
        fields=fields,
    )

    # Audit events ARE L0 entities in the substrate
    entity = L0Entity(
        id=event_id,
        type=event_type.value,
        backing=(LocalBacking(path=f"audit/{event_id}.json"),),
        creator=issuer_did,
        ingester=issuer_did,  # creator == ingester for self-emitted audit
        fetched_at=timestamp,
        upstream_status=UpstreamStatus.LIVE,
    )

    # Serialize the event payload as L0 content
    import json
    from dataclasses import asdict

    content = json.dumps(
        {
            "id": event.id,
            "type": event.type.value,
            "timestamp": event.timestamp.isoformat(),
            "fields": event.fields,
        },
        indent=2,
        default=str,
    ).encode("utf-8")

    store.put(entity, content=content)
    return event_id


def query_audit(
    store: L0BlobStore,
    since: datetime | None = None,
    event_types: list[AuditEventType] | None = None,
    agent_did: str | None = None,
    purpose: str | None = None,
    limit: int = 100,
) -> list[AuditEvent]:
    """Query the substrate-holder's own audit log.

    Stub — v0.1 should support efficient indexed queries. v0 just iterates L0.
    """
    # TODO: implement filter logic over store.iter_entities(type_filter=...)
    raise NotImplementedError("query_audit is sketched; v0.1 implementation needed")
