"""L0 blob store + L1+ typed store interfaces.

SKETCH ONLY — interfaces defined, filesystem reference partially implemented.

The L0BlobStore is the load-bearing primitive: substrate-holders persist their
raw substrate here, encrypted with keys they control. Per SPEC §5.4:
  - Storage MUST be at-rest-encrypted with keys controlled by the substrate-holder
  - Hosted runtimes MUST NOT have access to plaintext encryption keys
"""
from __future__ import annotations

import hashlib
import json
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Iterator

from hpi.types import L0Entity, AxiomEntity


# ─── L0 blob store ──────────────────────────────────────────────────────────


class L0BlobStore(ABC):
    """Append-only, content-addressed store for L0 entities + their backing bytes.

    Implementations: filesystem (this file), S3-compatible, IPFS, Plurality OCL,
    Solid pod. The interface is small so adapters are <100 lines each.
    """

    @abstractmethod
    def put(self, entity: L0Entity, content: bytes | None = None) -> str:
        """Store an L0 entity (and optionally its content bytes). Returns the entity's id.

        If content is provided, it is content-addressed and the entity's
        backing[*].path or identifier is updated to the content hash.
        """
        ...

    @abstractmethod
    def get(self, entity_id: str) -> L0Entity:
        """Retrieve an L0 entity by id. Raises KeyError if not found."""
        ...

    @abstractmethod
    def get_content(self, entity_id: str) -> bytes:
        """Retrieve the L0 entity's local content bytes. Raises if external-only."""
        ...

    @abstractmethod
    def iter_entities(self, type_filter: str | None = None) -> Iterator[L0Entity]:
        """Iterate stored entities, optionally filtered by type."""
        ...


class FilesystemL0BlobStore(L0BlobStore):
    """Reference filesystem implementation. NOT encrypted — for testing only.

    Production implementations MUST encrypt at rest. This implementation is
    plaintext deliberately — adding encryption is the next sprint, not this
    sketch.
    """

    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        (self.root / "entities").mkdir(parents=True, exist_ok=True)
        (self.root / "content").mkdir(parents=True, exist_ok=True)

    def put(self, entity: L0Entity, content: bytes | None = None) -> str:
        if content is not None:
            content_hash = hashlib.sha256(content).hexdigest()
            content_path = self.root / "content" / content_hash
            content_path.write_bytes(content)
            # Note: we don't mutate the entity here — caller should set backing
            # to point at content_hash. v0.1 will introduce an explicit helper.

        entity_path = self.root / "entities" / f"{entity.id}.json"
        entity_path.write_text(_serialize_entity(entity))
        return entity.id

    def get(self, entity_id: str) -> L0Entity:
        entity_path = self.root / "entities" / f"{entity_id}.json"
        if not entity_path.exists():
            raise KeyError(entity_id)
        return _deserialize_entity(entity_path.read_text())

    def get_content(self, entity_id: str) -> bytes:
        entity = self.get(entity_id)
        for backing in entity.backing:
            if backing.kind == "local":
                # If path is content-hash style, read from content/
                content_path = self.root / "content" / backing.path  # type: ignore[union-attr]
                if content_path.exists():
                    return content_path.read_bytes()
                # Otherwise treat as direct path
                return Path(backing.path).read_bytes()  # type: ignore[union-attr]
        raise ValueError(f"entity {entity_id} has no local backing")

    def iter_entities(self, type_filter: str | None = None) -> Iterator[L0Entity]:
        for entity_path in (self.root / "entities").glob("*.json"):
            entity = _deserialize_entity(entity_path.read_text())
            if type_filter is None or entity.type == type_filter:
                yield entity


# ─── L1+ typed store ────────────────────────────────────────────────────────


class L1TypedStore(ABC):
    """Storage for typed entities at L1 and above.

    Sketched only — production should use Postgres+JSONB with RLS, sqlite,
    MotherDuck, or IPLD. This stub just shows the interface.
    """

    @abstractmethod
    def put_axiom(self, axiom: AxiomEntity) -> str:
        ...

    @abstractmethod
    def get_axiom(self, axiom_id: str) -> AxiomEntity:
        ...

    @abstractmethod
    def query_axioms(
        self,
        family: str | None = None,
        valid_at: datetime | None = None,
    ) -> Iterator[AxiomEntity]:
        ...


# ─── Serialization helpers (v0 — JSON; v0.1 should use msgpack or canonical JSON) ───


def _serialize_entity(entity: L0Entity) -> str:
    """JSON-serialize an L0 entity. v0 only; v0.1 should canonicalize."""
    from dataclasses import asdict

    d = asdict(entity)
    d["fetched_at"] = entity.fetched_at.isoformat()
    d["upstream_status"] = entity.upstream_status.value
    return json.dumps(d, indent=2, default=str)


def _deserialize_entity(text: str) -> L0Entity:
    """Round-trip an L0Entity from JSON. Stub — v0.1 should validate vs schema."""
    from hpi.types import (
        ExternalBacking,
        L0Entity,
        LocalBacking,
        UpstreamStatus,
    )

    d = json.loads(text)
    backings: list = []
    for b in d.get("backing", []):
        if b["kind"] == "local":
            backings.append(LocalBacking(path=b["path"]))
        else:
            backings.append(ExternalBacking(url=b["url"], identifier=b["identifier"]))
    return L0Entity(
        id=d["id"],
        type=d["type"],
        backing=tuple(backings),
        creator=d["creator"],
        ingester=d["ingester"],
        fetched_at=datetime.fromisoformat(d["fetched_at"]),
        upstream_status=UpstreamStatus(d["upstream_status"]),
        promoted=d.get("promoted", False),
        derivatives=tuple(d.get("derivatives", ())),
    )
