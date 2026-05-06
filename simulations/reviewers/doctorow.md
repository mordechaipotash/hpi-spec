# Reviewer dossier — Cory Doctorow

**Role:** Daily Pluralistic.net (verified May 6 2026). EFF Fellow (25+ years). Author *The Internet Con* (Verso, 2023), *Enshittification* (FSG, Oct 2025), *Picks and Shovels* (Tor, Feb 2025). Coined "enshittification" framework. *The Reverse Centaur's Guide to AI* (FSG, June 2026, in production).
**Compiled:** 2026-05-06 from pluralistic.net (verified May 5 + May 6 posts), EFF essays, book corpus.

## 1. Public writings (last 3 years, recent-weighted)

- **"How not to ban surveillance pricing"** (April 30 2026, pluralistic.net/2026/04/30/something-must-be-done/). Maryland Protection Against Predatory Pricing Act is *"a terribly drafted piece of shit"* full of loopholes. Regulators warned, did nothing, produced legislation that is all carve-out. Direct relevance to HPI's regulatory mapping (Appendix A — GDPR 17/20/25): is HPI any more enforceable than Maryland's Act?

- **"The enshittification multiverse"** (April 27 2026, pluralistic.net/2026/04/27/analogs-and-analogies/). Extends enshittification to AI explicitly: *"AI is very enshittification-prone: as 'black boxes' that do not produce reliable, deterministic outputs, AI products have a lot of intrinsic cover for their enshittifying behavior. If you ask a chatbot to recommend a product and it steers you toward an inferior option that generates a higher commission for the company, who can say whether that was the chatbot cheating, or if it was a 'hallucination?'"* **Definition update:** *"Enshittification happens when someone sets out to reduce your choices, and then uses that lock-in to make things worse for you in order to make things better for themself. Note that this definition requires a degree of intent."*

- **"The (other) problem with automatic conversion of free software to proprietary software"** (April 23 2026). Discusses Malus.sh, an LLM tool that strips copyleft via clean-room reimplementation. Current concern: open standards / open source can be structurally laundered by sufficiently motivated actors. **Highly relevant to HPI**: same attack surface for any "open protocol" without governance.

- **"In praise of vultures"** (May 6 2026, pluralistic.net/2026/05/06/champerty-loves-company/). Antitrust / junk fees. Uses "enshittification" as descriptor.

- **Canonical enshittification essay** (Jan 21 2023, pluralistic.net/2023/01/21/potemkin-ai/). *"Here is how platforms die: first, they are good to their users; then they abuse their users to make things better for their business customers; finally, they abuse those business customers to claw back all the value for themselves. Then, they die."* Structural logic: *"surpluses are first directed to users; then, once they're locked in, surpluses go to suppliers; then once they're locked in, the surplus is handed to shareholders."*

**Books (2022-2025):**
- ***The Internet Con: How to Seize the Means of Computation*** (Verso 2023). Interoperability mandates as **the only structural solution to platform lock-in**.
- ***Enshittification: Why Everything Suddenly Got Worse and What to Do About It*** (FSG, Oct 2025). 33-city book tour.
- ***Chokepoint Capitalism*** (Beacon, 2022, w/ Rebecca Giblin). Market power analysis of creative labor.
- ***The Reverse Centaur's Guide to AI*** (FSG, June 2026, in production). *"A short book for being an effective AI critic."* The lens through which he would currently read HPI.

**Talks (verified)**: Re:publica Berlin May 18-20, EFF "How to Disenshittify the Internet" May 14, SXSW London June 2, Guelph May 8, Barcelona Digital Rights Forum May 13.

## 2. Stated values + intellectual lineage

- **FSF / EFF lineage** (25+ years). Right of users to control their own software/data flows is structural precondition for competitive markets — argued in market-theoretic terms, not ideology.
- **Adversarial interoperability ("comcom")**: *"creating a new product or service that plugs into the existing ones without the permission of the companies that make them."* Cooperative interop is not sufficient.
- **Standards capture (SMTP/Gmail pattern)**: email "open" via SMTP, but Gmail's dominance creates de facto lock-in within an "open" protocol. Open standards without governance enforcement become captured.
- **Protocols vs products**: *"an Internet dominated by protocols, not products, ensured that users could shape their online experiences."* But products capture protocols (OAuth/Auth0 example).
- **Consent theater**: privacy regimes that generate consent without choice. Most consent frameworks are theater when there's nowhere to go if you refuse. Will apply to HPI's PAT family + opt-in grammar.

## 3. Patterns of argumentation

- **Post format**: title + section slug + one-sentence teaser + link to prior writing + developed argument (1500-3000w) + "Hey look at this" link dump + "Object permanence" historical archive + upcoming + book plugs + colophon. Dense hyperlinks to prior Pluralistic posts — self-referential argument graph.
- **Historical analogy as primary tool**: typewriter manufacturers (IBM v. Columbia Data Products 1982); radio/TV spectrum capture; cable must-carry rules; AT&T breakup; SMTP/email; Prodigy. **Will reach for SMTP/Gmail analog when reading HPI.**
- **Embrace-Extend-Extinguish framing**: generalized capture pattern. Any spec allowing major players to implement "their version" is at risk. Malus essay shows current anxiety: open source copyleft can be neutralized by LLM-assisted clean-room reimplementation.
- **Sharpest critique trigger: governance void.** *"High 'switching costs' are always a precondition for enshittification — otherwise the people you're trying to enshittify will simply take their business elsewhere."* Any protocol or law: what structural mechanism prevents switching costs from accumulating?
- **Tone**: acerbic + pedagogical. Quotes own prior work. Uses worked examples. Calls governance gap by its worst name.

## 4. Adjacency to HPI's concerns

- **Personal AI / agent ownership**: Apr 27 2026 essay: AI tools steer users toward inferior options through opaque recommendations, with no audit. *Reverse Centaur's Guide* is direct response. Will bring frame to HPI §1.2.
- **JWT-based access control vs interop mandates**: No specific JWT post but OAuth/Auth0 critique applies — cryptographic access control gets captured when canonical implementation controlled by commercial entity. Will ask: who can revoke HPI tokens? Who can update axiom family schema?
- **AT Protocol / ActivityPub / Mastodon governance**: Approves Fediverse as structural alternative, critical of governance gaps. Concern: decentralized protocols shipping without governance get taken over by best-resourced implementor.
- **"Open protocol" claims without governance**: *"Big Tech climbed the adversarial ladder and then pulled it up behind them."* Frame for any open standard lacking anti-capture provisions.
- **DMA / EU Digital Fairness Act**: EFF on DMA: *"digital fairness means addressing the root causes of harm, not requiring platforms to exert more control over their users."* Regulatory mapping (HPI Appendix A) necessary but insufficient without enforcement mechanisms. GDPR Article 20 (data portability) largely unimplemented by hyperscalers because no structural interoperability mandate.
- **DID/VC ecosystem**: No direct engagement found. Adversarial interop framework applies — DIDs are W3C standard; control of canonical resolver infrastructure is capture surface.

## 5. Typical review register

- **Length**: Essays 1500-3000 words. Would write full essay-length review.
- **Structure**: (1) state HPI's claim + endorse the goal; (2) apply enshittification framework to claim-vs-enforcement gap; (3) historical analog (almost certainly SMTP/Gmail); (4) propose structural fix (governance clause / anti-capture provision / interoperability mandate with teeth); (5) evaluate THREAT-MODEL.md as separate doc — likely praise existence + probe binding.
- **Tone register**: Will call governance void by its name. Won't be gentle about "anyone can claim HPI compliance" if spec ships without governance. Uses phrases like *"terribly drafted piece of shit"* for well-intentioned legislation that fails structurally.
- **Self-citation**: Will link to *The Internet Con*, adversarial interop essay, enshittification multiverse essay.

## 6. Predicted angles of response to HPI

**ENDORSE:**
- HPI §1.2 (*"the platform's incentive is lock-in and corporate-profit alignment"*) is his thesis statement for the last decade. Endorses diagnosis without reservation.
- Open-protocol thesis aligns directly with *Internet Con*. *"The right frame."*
- THREAT-MODEL.md as document that names structural threats. He frequently criticizes regulators / spec authors for refusing to name threats. §8 incident response + Appendix A regulatory mapping = HPI taking its own threat model seriously, which he finds unusual and worth noting.

**PROBE (rhetorical first question):**
*"What prevents HPI from becoming SMTP? What stops Google from shipping HPI-compatible endpoints that technically pass wire-format compliance tests, then routing everything through their inference pipeline, then charging for premium PAT resolution speeds, then making non-Google HPI endpoints slow enough that no one uses them?"*

- Who maintains the typed grammar (PAT family canonical definitions)? If GitHub repo controlled by one person/small team with no governance charter → single point of capture.
- Does spec actually prohibit §7 anti-pattern behaviors, or merely describe them? **If prohibition is advisory, it is consent theater.**

**PUSH BACK:**
- Any "anyone can be HPI-compliant" framing without specifying what compliant means structurally, who audits, what's the remedy. Direct: *"'Anyone can implement this' is how SMTP works. How did that go?"*
- "We'll figure out governance post-publication" deferrals. From surveillance pricing essay: lawmakers warned, did nothing, produced loophole-ridden legislation. **Deferred governance is not governance — it's a promise to be captured later.**

**PROPOSE:**
- Specific governance model: consortium (W3C-style), foundation (Apache/Linux Foundation-style), or RFC process (IETF-style). Will note IETF model has known failure modes (SMTP again). Independent foundation with charter preferable.
- **Explicit anti-capture clauses in §7 anti-patterns** — not as advice but as wire-format-level enforcement: HPI-compliant implementations MUST NOT implement behaviors X, Y, Z, where X, Y, Z are named capture vectors.
- PAT family canonical definition under governance body with civil society representation, not just implementors.

**CONVERGENCE TEST**: Doctorow **CONVERGES** on claim-vs-enforcement gap. His version: *"The spec's prose makes political claims. The wire format makes technical claims. The political claims are unenforceable from the wire format alone."*

**DIVERGENCE — TWO new vectors Doctorow surfaces:**

1. **Political economy of protocol capture.** Distinct from technical claim-enforcement. Even perfectly enforced spec becomes worthless if implementation ecosystem captured by hyperscalers. **Spec needs anti-capture provisions structurally independent of technical compliance.**

2. **AI-specific enshittification as distinct threat.** Apr 27 essay: AI systems have intrinsic cover for enshittifying behavior — *"who can say whether that was the chatbot cheating, or if it was a hallucination?"* A sovereign cognitive substrate protocol that stores personal data in user-controlled endpoints does NOT protect users from AI inference pipelines that process that data through hyperscaler model before returning results. **THREAT-MODEL.md needs a §N: "AI Inference Pipeline as Exfiltration Vector."**

His proposed intervention is structural, not syntactic: governance body with anti-capture charter, not cleaner prose. This is the HPI-specific implication of *The Internet Con*'s central argument.

## Confidence calibration

**High**: Enshittification framework + structure verified directly. AI-specific enshittification (April 27 2026 primary source). Governance-void as sharpest critique trigger. Active publication through May 6 2026 confirmed via RSS.
**Medium**: JWT/PAT critique extrapolated from OAuth/Auth0 pattern. DID/VC position inferred from adversarial interop framework.
**Low**: Whether he'd write full review-length response vs brief Pluralistic mention. View on HPI's specific Appendix A regulatory mapping.

**Verdict**: Doctorow converges on claim-vs-enforcement (now SEVEN-confirmed when combined with Allen + Stenberg + Schneier). Diverges by surfacing **two new vectors**: (1) political economy of protocol capture (governance, not just enforcement); (2) AI inference pipeline as exfiltration vector (a category genuinely missing from THREAT-MODEL.md).
