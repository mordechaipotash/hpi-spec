"""Discovery document builder — .well-known/hpi.json (per SPEC §5.3)."""
from __future__ import annotations

from typing import Any


def build_discovery_document(
    issuer_did: str,
    runtime_url: str,
    supported_axiom_families: list[str],
    transports: list[str] | None = None,
) -> dict[str, Any]:
    """Build the JSON for /.well-known/hpi.json.

    The substrate-holder publishes this at their own domain. Hosted runtimes
    serve it on the holder's behalf — but the issuer DID and key URLs always
    point at infrastructure under the holder's control.
    """
    if transports is None:
        transports = ["mcp", "http+json"]

    issuer_domain = issuer_did.replace("did:web:", "").rstrip("/")

    return {
        "version": "0",
        "issuer": issuer_did,
        "runtime_endpoint": runtime_url,
        "transport": transports,
        "supported_axiom_families": list(supported_axiom_families),
        "key_endpoint": f"https://{issuer_domain}/.well-known/jwks.json",
        "revocation_endpoint": f"{runtime_url}/.well-known/hpi/revocations.json",
    }
