"""Core types for HPI runtime.

All dataclasses are immutable (`frozen=True`) where the underlying spec calls for
immutability — particularly L0Entity (per SPEC §2.1.3 "L0 is immutable").

These types are the wire format. Any implementation that emits or consumes HPI
data must produce shapes that round-trip through these dataclasses.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Literal


# ─── L0 substrate types ──────────────────────────────────────────────────────


class UpstreamStatus(str, Enum):
    """Status of an L0 entity's upstream backing."""

    LIVE = "live"
    DRIFTED = "drifted"
    LOST = "lost"


@dataclass(frozen=True)
class LocalBacking:
    """L0 entity backed by local bytes (a file)."""

    kind: Literal["local"] = "local"
    path: str = ""


@dataclass(frozen=True)
class ExternalBacking:
    """L0 entity backed by stable upstream pointer (URL, DOI, message-id, ...)."""

    kind: Literal["external"] = "external"
    url: str = ""
    identifier: str = ""  # stable id — youtube_id, gmail_message_id, etc.


L0Backing = LocalBacking | ExternalBacking


@dataclass(frozen=True)
class L0Entity:
    """An L0 entity — the most-raw digital copy at MY substrate boundary.

    Per SPEC §2.1: L0 is immutable, has two owners (creator + ingester), and is
    backed by some combination of local bytes and external pointers.
    """

    id: str  # opaque unique id within the substrate
    type: str  # typed enum: youtube_video | local_file | http_url | git_sha | ...
    backing: tuple[L0Backing, ...]  # one or more backings
    creator: str  # upstream — substrate-id or party that produced the bytes
    ingester: str  # substrate-holder — who pulled it across THEIR boundary
    fetched_at: datetime
    upstream_status: UpstreamStatus = UpstreamStatus.LIVE
    promoted: bool = False  # true iff backing is local-only and upstream is lost
    derivatives: tuple[str, ...] = ()  # pointers to L1+ entities derived from this L0


# ─── Token types ─────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Scope:
    """Permission scope a token grants (per SPEC §4.3).

    A token's effective capability is the INTERSECTION of all four dimensions.
    """

    axiom_families: tuple[str, ...] = ()  # OBL, RCG, TRU, PAT, ...
    axiom_ids: tuple[str, ...] = ()  # specific entity IDs (overrides families if set)
    layers: tuple[str, ...] = ()  # L1, L2, L3 — L3 SHOULD NOT be granted by default
    actions: tuple[str, ...] = ()  # read, write, propose, ...


@dataclass(frozen=True)
class ScopeRequest:
    """Agent's request for permission. Runtime may narrow (never broaden) before approving."""

    axiom_families: list[str] = field(default_factory=list)
    axiom_ids: list[str] = field(default_factory=list)
    layers: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)

    def to_scope(self) -> Scope:
        return Scope(
            axiom_families=tuple(self.axiom_families),
            axiom_ids=tuple(self.axiom_ids),
            layers=tuple(self.layers),
            actions=tuple(self.actions),
        )


@dataclass(frozen=True)
class TokenClaims:
    """The claims set inside an HPI JWT (per SPEC §4.2 v0)."""

    iss: str  # substrate-holder DID
    sub: str  # agent DID
    aud: str  # runtime URL
    iat: int  # unix timestamp
    exp: int  # unix timestamp
    jti: str  # unique token id
    scope: Scope
    purpose: str  # machine-tag
    purpose_text: str  # human-readable
    single_use: bool = True
    delegation: Literal["forbid", "attenuate", "re-request"] = "forbid"
    version: str = "0"


@dataclass
class Token:
    """A wrapped, signed token with metadata. The `jwt` field is the over-the-wire form."""

    claims: TokenClaims
    jwt: str  # signed JWT string

    @property
    def jti(self) -> str:
        return self.claims.jti

    @property
    def expires_at(self) -> datetime:
        return datetime.fromtimestamp(self.claims.exp)


# ─── Audit types ─────────────────────────────────────────────────────────────


class AuditEventType(str, Enum):
    """Standard audit event types per SPEC §4.7."""

    TOKEN_ISSUED = "hpi_token_issued"
    TOKEN_CONSUMED = "hpi_token_consumed"
    TOKEN_DENIED = "hpi_token_denied"
    TOKEN_REVOKED = "hpi_token_revoked"


@dataclass(frozen=True)
class AuditEvent:
    """An audit event — itself an L0 entity in the substrate-holder's substrate.

    Persisted as a typed L0 entry; rolls up via L1 extractor.
    """

    id: str  # unique event id (also acts as L0 entity id)
    type: AuditEventType
    timestamp: datetime
    fields: dict[str, Any]  # event-type-specific


# ─── Axiom types ─────────────────────────────────────────────────────────────


class AxiomFamily(str, Enum):
    """v0 axiom families. Implementations MAY add more."""

    OBL = "OBL"
    RCG = "RCG"
    TRU = "TRU"
    PAT = "PAT"


@dataclass(frozen=True)
class AxiomEntity:
    """An entity tagged as instance-of an axiom family.

    This is the typed grammar for substrate-boundary preservation. When an
    AxiomEntity crosses from holder A's L3 to holder B's L0, B's L1 extractor
    can recognize the type and extract semantic fields without re-derivation.
    """

    family: AxiomFamily
    axiom_id: str  # e.g., "OBL:o-2026-04-18-DE-87332"
    predicate: dict[str, Any]  # the family-specific assertion content
    provenance: tuple[str, ...]  # citation chain back to L0 entity ids
    issuer: str  # substrate-holder who emitted this axiom
    subject: str | None = None  # substrate-holder this axiom is about, if applicable
    valid_from: datetime | None = None
    valid_until: datetime | None = None
    signature: str | None = None  # cryptographic signature, optional in v0
