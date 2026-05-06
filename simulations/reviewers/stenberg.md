# Reviewer dossier — Daniel Stenberg

**Status:** STUB. Promoted to v2 cohort #5 by cohort-meta-evaluation 2026-05-06.
**Estimated effort:** 2 hours of focused research.
**Why simulate:** Author and primary maintainer of curl (runs in tens of billions of devices). IETF contributor. Practitioner's view on what protocol design choices survive deployment. His "Don't trust, verify" post (March 26 2026) directly relevant to HPI's cite-or-die discipline. curl 8.20.0 release April 29 2026 confirms active engagement. Engagement likelihood: HIGH.

## Research targets

- daniel.haxx.se (daily blog — active)
- "Don't trust, verify" (March 26 2026)
- curl 8.20.0 release notes (April 29 2026)
- IETF mailing list contributions
- GitHub: bagder
- Mastodon activity
- Past protocol-spec reviews he has written publicly

## Predicted critique angle (from cohort-vetter)

> *"The wire format section (§5) says HPI 'extends MCP with HPI-specific methods.' I can't implement this. Where are the method names? The parameter schemas? The error codes? The interop test vectors? MCP itself doesn't have a stable versioning story. If HPI rides MCP, it inherits MCP's versioning ambiguity. Give me the ABNF or the JSON Schema or the OpenAPI spec. Prose is not a protocol."*

## Convergence test

Stenberg's critique axis (wire-format completeness, IETF pragmatics) is genuinely orthogonal to Karp/Wooders/Karpathy. Convergence on the central claim-vs-enforcement finding would be FOUR-confirmed.

If Stenberg DIVERGES, his most likely net-new contributions:
- Demand for ABNF / JSON Schema / OpenAPI per method (already partially planned for v0.1)
- Interop test vectors as conformance requirement (currently absent from §6.4)
- MCP versioning analysis — does HPI inherit MCP's version-management ambiguity?
- Edge-case enumeration the spec hasn't yet addressed

## Why second of v2 cohort

Practitioner reviewer with HIGH engagement likelihood. Wire-format completeness is the operational complement to the architectural critiques the v1 cohort produced. If Stenberg's review is favorable, it's a strong adoption signal — protocols that pass his "I can implement this" bar tend to get deployed.

## Order of priority

Run as v2 #5 simulation, after Allen. The two paired (Allen on standards lineage + Stenberg on implementation reality) cover the protocol-engineering side of the review surface comprehensively.
