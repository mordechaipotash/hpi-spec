"""hpi-issue — substrate-holder issues a token (CLI).

SKETCH — argument parsing only. Real implementation needs key loading,
runtime configuration loading, and audit-event persistence.

Usage:
    hpi-issue --agent did:agent:claude-7afe \\
              --purpose reconcile \\
              --scope OBL,RCG \\
              --layers L1,L2 \\
              --actions read \\
              --expiry 3600
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="HPI: issue a token")
    parser.add_argument("--agent", required=True, help="agent DID")
    parser.add_argument("--purpose", required=True, help="machine-tag purpose")
    parser.add_argument("--purpose-text", default="", help="human-readable purpose")
    parser.add_argument("--scope", default="OBL", help="comma-separated axiom families")
    parser.add_argument("--layers", default="L1,L2", help="comma-separated layers")
    parser.add_argument("--actions", default="read", help="comma-separated actions")
    parser.add_argument("--expiry", type=int, default=3600, help="expiry in seconds")
    parser.add_argument("--key-path", default="~/.hpi/private.pem", help="signing key path")
    parser.add_argument("--issuer-did", required=True, help="substrate-holder DID")
    parser.add_argument("--audience", required=True, help="runtime URL")
    args = parser.parse_args()

    # TODO v0.1: load key, instantiate TokenIssuer, issue token, write audit event
    print(f"[stub] would issue token for {args.agent} with scope {args.scope}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
