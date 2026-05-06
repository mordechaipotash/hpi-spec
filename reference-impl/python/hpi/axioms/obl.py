"""OBL — Obligations axiom family.

SKETCH — schema + entry-point validators only. The full axiom set (OBL-1 through
OBL-5) is documented in `axioms/OBL-obligations.md` of the spec; this module is
the executable companion.

Key spec mapping:
  - OBL-1: every obligation is a node with exactly one canonical state
  - OBL-2: obligation born from any evidence source, lives until settlement
  - OBL-3: dedup by (counterparty, reference, amount±tolerance)
  - OBL-4: source priority for canonical-state derivation
  - OBL-5: FX frozen at obligation-creation time
"""
from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Any

from hpi.types import AxiomEntity, AxiomFamily


# ─── OBL state machine (per OBL-1 + OBL-2) ─────────────────────────────────

OBL_STATES = {
    "draft",
    "recognized",
    "matched",
    "reconciled",
    "settled",
    "archived",
    "disputed",
    "partially-paid",
    "cancelled",
}

OBL_TRANSITIONS: dict[str, set[str]] = {
    "draft": {"recognized", "cancelled"},
    "recognized": {"matched", "disputed", "cancelled"},
    "matched": {"reconciled", "disputed"},
    "reconciled": {"settled", "partially-paid", "disputed"},
    "partially-paid": {"settled", "disputed"},
    "settled": {"archived"},
    "disputed": {"recognized", "matched", "reconciled", "cancelled"},
    "archived": set(),
    "cancelled": {"archived"},
}


# ─── Source priority (per OBL-4) ───────────────────────────────────────────

SOURCE_PRIORITY = [
    "xero_reconciled",
    "plunet_job_line",
    "supplier_invoice_pdf",
    "email_body",
    "inferred_by_llm",
]


# ─── JSON Schema (v0.1 will move this to schemas/OBL.json) ─────────────────

OBL_PREDICATE_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["counterparty_pair", "reference", "amount", "currency", "state"],
    "properties": {
        "counterparty_pair": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 2,
            "maxItems": 2,
        },
        "reference": {"type": "string"},
        "amount": {"type": "string"},  # Decimal as string for cross-language safety
        "currency": {"type": "string", "minLength": 3, "maxLength": 3},
        "book_currency": {"type": "string", "minLength": 3, "maxLength": 3},
        "fx_rate_at_creation": {"type": "string"},
        "state": {"enum": list(OBL_STATES)},
        "evidence_source_priority": {"type": "string", "enum": SOURCE_PRIORITY},
        "evidence_ids": {"type": "array", "items": {"type": "string"}},
    },
}


# ─── Validators ────────────────────────────────────────────────────────────


def validate_obl_predicate(predicate: dict[str, Any]) -> None:
    """Validate an OBL predicate against the v0 schema.

    Raises jsonschema.ValidationError on failure.
    """
    import jsonschema

    jsonschema.validate(predicate, OBL_PREDICATE_SCHEMA)


def validate_state_transition(from_state: str, to_state: str) -> None:
    """Per OBL-1 + OBL-2: state transitions are explicit; non-adjacent transitions forbidden."""
    if from_state not in OBL_STATES:
        raise ValueError(f"unknown from_state: {from_state}")
    if to_state not in OBL_STATES:
        raise ValueError(f"unknown to_state: {to_state}")
    if to_state not in OBL_TRANSITIONS.get(from_state, set()):
        raise ValueError(
            f"forbidden transition {from_state} → {to_state}; "
            f"requires compensating event"
        )


def is_same_obligation(
    a_predicate: dict[str, Any],
    b_predicate: dict[str, Any],
    amount_tolerance: Decimal = Decimal("0.01"),
) -> bool:
    """Per OBL-3: two predicates point at the same obligation iff they share
    counterparty pair, reference, and amount within tolerance.
    """
    if set(a_predicate["counterparty_pair"]) != set(b_predicate["counterparty_pair"]):
        return False
    if a_predicate["reference"] != b_predicate["reference"]:
        return False
    a_amount = Decimal(a_predicate["amount"])
    b_amount = Decimal(b_predicate["amount"])
    return abs(a_amount - b_amount) <= amount_tolerance


def derive_canonical_state(evidence_predicates: list[dict[str, Any]]) -> dict[str, Any]:
    """Per OBL-4: derive canonical state by source priority, not recency.

    Returns the highest-priority evidence's predicate. Disagreements with
    lower-priority sources should be preserved as audit trail by the caller.
    """
    if not evidence_predicates:
        raise ValueError("no evidence to derive from")

    def priority_index(p: dict[str, Any]) -> int:
        src = p.get("evidence_source_priority", "inferred_by_llm")
        return SOURCE_PRIORITY.index(src) if src in SOURCE_PRIORITY else len(SOURCE_PRIORITY)

    return min(evidence_predicates, key=priority_index)


# ─── Construction helper ──────────────────────────────────────────────────


def make_obl_axiom(
    axiom_id: str,
    counterparty_pair: tuple[str, str],
    reference: str,
    amount: Decimal,
    currency: str,
    state: str,
    evidence_ids: list[str],
    evidence_source_priority: str,
    issuer: str,
    valid_from: datetime,
    book_currency: str | None = None,
    fx_rate_at_creation: Decimal | None = None,
) -> AxiomEntity:
    """Construct a v0-conformant OBL axiom entity."""
    predicate: dict[str, Any] = {
        "counterparty_pair": list(counterparty_pair),
        "reference": reference,
        "amount": str(amount),
        "currency": currency,
        "state": state,
        "evidence_source_priority": evidence_source_priority,
        "evidence_ids": list(evidence_ids),
    }
    if book_currency:
        predicate["book_currency"] = book_currency
    if fx_rate_at_creation is not None:
        predicate["fx_rate_at_creation"] = str(fx_rate_at_creation)

    validate_obl_predicate(predicate)

    return AxiomEntity(
        family=AxiomFamily.OBL,
        axiom_id=axiom_id,
        predicate=predicate,
        provenance=tuple(evidence_ids),
        issuer=issuer,
        valid_from=valid_from,
    )
