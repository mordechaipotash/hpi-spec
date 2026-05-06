"""hpi-audit — substrate-holder queries their own audit trail (CLI).

SKETCH — argument parsing only.

Usage:
    hpi-audit --since 2026-05-01 --agent did:agent:claude-7afe --limit 50
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="HPI: query own audit trail")
    parser.add_argument("--since", default=None, help="ISO timestamp lower bound")
    parser.add_argument("--agent", default=None, help="filter by agent DID")
    parser.add_argument("--purpose", default=None, help="filter by purpose tag")
    parser.add_argument("--type", default=None, help="filter by event type")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--store-path", default="~/.hpi/store", help="L0 blob store path")
    args = parser.parse_args()

    # TODO v0.1: load store, query audit events, format output
    print(f"[stub] would query audit since={args.since} limit={args.limit}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
