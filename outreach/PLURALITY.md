# Outreach draft — Plurality / OCL

**Status:** Draft. Do NOT send until reviewed by Mordechai + (optional) Shaul.
**Last updated:** 2026-05-06
**Target:** Plurality Network / Open Context Layer team
**Channel:** TBD — Twitter/X DM, founder email, Telegram, or warm intro

---

## Why I'm contacting you

You're building OCL — user-owned encrypted context vaults with MCP integration and scoped sharing. I have been working alongside this problem from a different angle for the past two years and have just shipped a v0 spec for what I'm calling HPI (Hyperpersonalized API): a typed protocol for substrate-boundary context handoff between humans and agents.

Your work and mine sit at adjacent layers of the same stack. From my reading of OCL's positioning, you've solved the **storage substrate** for sovereign user context. HPI specifies the **typed grammar and access protocol** that runs on top of that substrate — typed axiom families (OBL/RCG/TRU/PAT in v0), one-time-token agent borrowing, full audit trail emitted to the user's own substrate.

I want to figure out whether HPI can ride on OCL's vault primitive cleanly, and whether there's a productive collaboration here.

## What I've already worked through

- **Identified OCL as ally not competitor** in my Feb 2026 sovereignty-stack research. Storage primitive (yours) + typed-protocol (mine) compose. We're not chasing the same surface.
- **HPI v0 draft is private** at the moment. I'd be glad to share it under whatever review constraint feels right (under NDA if you prefer; or open if you'd just like to read).
- **Working implementations exist already**: my Brain MCP (~400K-message indexed personal corpus, queryable), Viter L0→L3 pipeline (chat-log + WhatsApp + transcripts → daily L1/L2/L3 with cite-or-die discipline), and a Persofi reconciliation deployment using OBL/RCG/TRU/PAT axioms in production at one pilot client. All this currently uses filesystem + Supabase as the storage substrate. OCL is the natural upgrade path.

## What I'm proposing for a first conversation

Three concrete points where I think we'd benefit from comparing notes:

1. **Vault primitive ↔ typed entities.** Does OCL's vault model accommodate per-entity typed axioms (the cargo HPI ships through your container)? If yes, what does an OCL-stored OBL look like? If no, what's the gap?

2. **Token issuance ↔ scoped sharing.** Your scoped-sharing model and HPI's token issuance flow seem like cousins. Are they the same mechanism with different framing, or are there genuine differences worth surfacing?

3. **Audit trail ownership.** HPI's load-bearing claim is that the user owns their own audit trail (every token issued and consumed becomes an L0 entity in the user's substrate). Is OCL aligned with this, or is the audit log separate?

I'm not pitching anything. I'm genuinely trying to understand whether the architectures cohere or whether there's a real disagreement we'd both benefit from naming.

## What I'd ideally like to know about OCL

- Where you're at in v0 / production trajectory
- Whether you have a stable spec doc I can reference (or whether it's still in flux)
- Whether you'd be open to HPI spec citing OCL as a recommended L0 backing
- Whether there are open questions in OCL's design where my Persofi-pilot data (a real production use case for typed sovereign context) would be useful input

## About me

I'm Mordechai Potash, an AI-native engineer working from Beit Shemesh, Israel. Background: 2+ years building Brain MCP (personal cognitive corpus + MCP server) and Viter (vertical-SaaS infrastructure for finance ops). I came to this problem from the cognitive-prosthetic angle — I'm monotropic, ADHD + Asperger's, and my substrate IS my prosthetic. The architecture I'm specifying isn't theoretical; it's what lets me work.

Public: github.com/mordechaipotash, brainmcp.dev (work in progress).

## Suggested next step

A 30-minute call (Google Meet / Telegram / your choice) within the next 2 weeks if there's interest. I'd send the HPI v0 spec ahead of the call so the conversation can start from a shared base.

If a call doesn't fit your schedule but you're open to a written exchange, I'll share the spec doc + specific questions and we can iterate via DM.

If neither fits — no worries, I'll continue building and ship the public spec when ready, with OCL named in the lineage section regardless.

Best,
Mordechai

---

## Notes for Mordechai before sending

**What this message accomplishes:**
- Signals genuine engagement (you've named OCL as ally; you reference your own deployed work)
- Asks for conversation, not commitment
- Establishes that you ship public regardless — pre-empts "is this a soft acquisition pitch"
- Names three concrete intersection points (vault, sharing, audit) — keeps the conversation focused
- Closes with a clean fallback (no harm, you'll publish anyway)

**What this message does NOT do:**
- No code commitments
- No funding or partnership ask
- No deadlines that pressure them
- Does not over-position HPI as competing-with-anything

**Tone calibration:**
- Confident but not territorial
- Specific (named axiom families, named existing implementations) — proves you've done the work
- Honest about your background (autistic builder from Beit Shemesh, not a Stanford team) — distinguishes you from the typical pitch

**Before sending, decide:**
1. Channel: warm intro through someone who knows them? Cold founder email? Twitter DM?
2. Spec attachment: send v0 even though it's incomplete (§1, §5–9 still outline)? Or wait until v0 is fully drafted and just describe verbally for now?
3. Is the Persofi pilot mention safe? (It is currently sanitized; client name is `<client-corp>` in axiom files. The mention here uses "one pilot client" which preserves anonymity.)
4. Are you comfortable with the personal disclosure (monotropic / ADHD / Asperger's)? It works rhetorically — but only if you mean it. If it feels performative, cut.

**Response trigger words to watch for:**
- "Tell me more about..." → engaged, schedule call
- "Have you looked at [other player]?" → they're benchmarking; offer your landscape research
- "We're not really focused on this" → polite decline; thank them and move on
- No response in 14 days → send one short follow-up; if no response, leave it alone

**Recommended send-after gate:** Wait until §1 of SPEC is drafted to full prose. Sending with §1 still labeled OUTLINE feels rougher than necessary. Should be done within a week.
