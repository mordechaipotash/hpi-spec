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

    v0 reference impl: linear scan over L0 with in-memory filtering.
    v0.1 production: indexed query (e.g., Postgres GIN on event_type + jsonb fields).
    """
    import json as _json

    type_values = {t.value for t in event_types} if event_types else None

    results: list[AuditEvent] = []
    for entity in store.iter_entities():
        if not entity.type.startswith("hpi_token_"):
            continue
        if type_values is not None and entity.type not in type_values:
            continue

        try:
            content = store.get_content(entity.id)
            payload = _json.loads(content.decode("utf-8"))
        except (KeyError, ValueError, UnicodeDecodeError):
            continue

        ts = datetime.fromisoformat(payload["timestamp"])
        if since is not None and ts < since:
            continue

        fields = payload.get("fields", {})
        if agent_did is not None and fields.get("agent_did") != agent_did:
            continue
        if purpose is not None and fields.get("purpose") != purpose:
            continue

        results.append(
            AuditEvent(
                id=payload["id"],
                type=AuditEventType(payload["type"]),
                timestamp=ts,
                fields=fields,
            )
        )
        if len(results) >= limit:
            break

    results.sort(key=lambda e: e.timestamp)
    return results
