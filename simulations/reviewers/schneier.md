# Reviewer dossier — Bruce Schneier

**Status:** STUB. Promoted to v2 cohort #6 by cohort-meta-evaluation 2026-05-06.
**Estimated effort:** 2-3 hours of focused research.
**Why simulate:** Co-authored *Rewiring Democracy: How AI Will Transform Our Politics, Government, and Citizenship* (MIT Press, October 2025) — chapter "Acting as Your Personal Political Proxy" is the substrate-ownership question HPI addresses. Daily essays on schneier.com. *Data and Goliath* (2013) is the foundational text on surveillance-as-business-model. Engagement likelihood: medium-high.

**Calibration note:** THREAT-MODEL.md was drafted (2026-05-06) explicitly addressing Schneier-predicted critiques. His simulation is now a calibration test: does the v0 threat model survive a Schneier reading? Different from "would Schneier identify the gap" — that gap has been filled.

## Research targets

- *Rewiring Democracy* (MIT Press, Oct 2025) — chapter on AI proxies
- schneier.com daily blog (verify recent posts)
- IEEE Spectrum AI security columns (April 26 2026 with Barath Raghavan)
- Co-authored work with Nathan E. Sanders (2026)
- *Data and Goliath* (2013) — foundational position on surveillance
- His position on JWT vs other token formats
- His position on key custody / trust hierarchy

## Predicted critique angle (from cohort-vetter)

> *"The token issuance section describes a JWT-shaped object but never specifies the signing key hierarchy. Who holds the root? If the substrate owner generates their own root key, you have a key management problem that makes PGP's web of trust look simple. If a third party holds it, you've re-created the platform custody problem you're trying to eliminate. The spec needs a §4.x on key custody before it can claim to be a trust protocol."*

## Convergence test (with calibration twist)

Because THREAT-MODEL.md now exists, Schneier's simulation has a SECOND test:
1. Does Schneier converge on the central claim-vs-enforcement finding? (FIVE-confirmation if yes)
2. Does v0 THREAT-MODEL.md survive a Schneier read?

If THREAT-MODEL.md survives Schneier, the document is robust. If it doesn't, the gaps Schneier identifies become v0.1 hardening priorities.

## Why third of v2 cohort

The simulation is now a stress-test of THREAT-MODEL.md, not just a gap-finder. This is a more demanding test of the spec — but if it passes, it's stronger evidence the spec is ready for reader review.

## Order of priority

Run third of v2 cohort, after Allen + Stenberg. By that point we'll have FIVE simulated reviews; the convergence (or divergence) signal will be definitive.
