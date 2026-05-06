# Reviewer dossier — Bruce Schneier

**Role:** Security technologist. Author *Applied Cryptography*, *Secrets and Lies*, *Data and Goliath*. Co-author *Rewiring Democracy* (MIT Press, Oct 2025) with Nathan E. Sanders. **Chief of Security Architecture at Inrupt** (Solid protocol commercialization, founded by Tim Berners-Lee). Daily essays on schneier.com.
**Compiled:** 2026-05-06 from primary sources at schneier.com (12 essays fetched), inrupt.com, *Rewiring Democracy* publisher page.

**Calibration framing:** This simulation is a CALIBRATION TEST of the just-shipped THREAT-MODEL.md (581 lines, 12 sections) — does v0 threat model survive Schneier's read? Different from "would Schneier identify the gap" — those gaps were the design target.

## 1. Public writings (last 3 years, recent-weighted)

- **Rewiring Democracy** (MIT Press, October 21 2025, with Nathan E. Sanders, 248 pages). Chapter 38 — **"Acting as Your Personal Political Proxy"** — direct adjacency to HPI. The book's thesis: AI will transform every facet of democracy; the question is whether it concentrates or distributes power. Conclusion: corporate-owned AI cannot be trusted to serve public interest because incentives are misaligned. The personal proxy chapter asks: *if an AI acts on your behalf — voting, advocating, negotiating — who controls it, who trains it, and who does it really serve?*

- **"What Anthropic's Mythos Means for the Future of Cybersecurity"** (IEEE Spectrum, with Barath Raghavan, April 26-28 2026). AI vulnerability-finders favor defenders *if* patch pipelines are fast. Frames: "patchable vs unpatchable" and "easy to verify vs hard to verify." Advocates "principle of least privilege" and "traceable" distributed systems.

- **"Mythos Sets the World on Edge"** (Globe and Mail, with David Lie, April 14 2026). Calls for *"independent auditing, mandatory disclosure of aggregate performance metrics."* *"Any technology that can find thousands of exploitable flaws in the systems we all depend on should not be governed solely by the internal judgment of its creators."*

- **"Don't Bet That the Pentagon — or Anthropic — Is Acting in the Public Interest"** (The Guardian, with Nathan Sanders, March 3 2026). *"The lesson is about the importance of democratic structures and the urgent need for their renovation."* Does not trust corporations OR government agencies in public interest. Market cannot self-regulate.

- **"Rewiring Democracy Now: Switzerland Shows Us an Alternative to Corporate AI"** (The Renovator, February 21 2026). Argues for **"public AI"** — not open-source corporate hand-offs but genuinely publicly accountable AI with democratic oversight. Apertus (Swiss national AI model) as template.

- **"LLMs' Data-Control Path Insecurity"** (Communications of the ACM, May 2024). Foundational. SS7 analogy: *"the real problem is the commingling of data and commands."* Prompt injection structurally unfixable in current LLM architecture because data and control share the same channel. *"Someday, some AI researcher will figure out how to separate the data and control paths. Until then, we're going to have to think carefully about using LLMs in potentially adversarial situations — like on the Internet."*

- **"AI and Trust"** (Harvard Kennedy School Belfer Center, December 2023, ~5,000 words). His most comprehensive AI trust framework. Three claims: (1) we will mistake AI systems for friends when they are services; (2) corporations building AI are *"precisely as immoral as the law and their reputations let them get away with"*; (3) government must mandate trustworthiness through fiduciary law and public AI models. Key distinction: **interpersonal trust vs social trust**. Prescription: **"data fiduciaries"** with legal accountability.

- **"Seeing Like a Data Structure"** (Belfer Center, May 2024, with Barath Raghavan). Critiques datafication at epistemological level. *"We need fluidity"* not optimization. Advocates federated systems, local rules, portability, anti-lock-in mechanisms.

- **"Cybersecurity in the Age of Instant Software"** (CSO, April 2 2026). "Five unknowns" framework. *"Unknown No. 5 — it's a biggie. There might always be a 'trusting trust problem.'"* Quotes Ken Thompson implicitly.

- **Data and Goliath** (Norton, 2013/2015). Foundational on surveillance-as-business-model. Core thesis: data collected for one purpose is used for all purposes.

**Institutional role (load-bearing):** Schneier is **Chief of Security Architecture at Inrupt**. Inrupt commercializes Solid (W3C decentralized personal data pods). Inrupt April 2026 product line includes **"Agentic Wallets"** and **"Data Wallets"** — an MCP server connecting AI agents to consented customer data. Berners-Lee is CTO. **Schneier has operational experience building the exact architecture HPI claims to implement.** He is not a spectator.

## 2. Stated values + intellectual lineage

- **Cryptography tradition.** Pre-TLS PKI era. Cryptographic axiom: *"crypto-agility is always a good thing."*
- **Trust modeling discipline.** Interpersonal/social trust distinction is master frame. AI collapses this distinction dangerously.
- **Key custody position**: Solid/Inrupt work makes it unambiguous — **user-controlled, self-hosted pods are the gold standard**. Skeptical of "hosted-but-isolated" as durable security claim because vendor incentives are misaligned. Corporations *"precisely as immoral as the law and their reputations let them get away with."* Does not trust HSMs or threshold-MPC under vendor control as equivalents to true self-custody — *what prevents the custodian from changing the terms?*
- **JWT / signing-key hierarchy**: SS7 analogy applies. Any system commingling authentication tokens with data structurally vulnerable to injection-class attacks. Wants: separation of verification from execution, JTI consumption guarantees that survive multi-instance deployment, explicit adversarial modeling.

## 3. Patterns of argumentation

- **Reads for adversarial gap** between prose claims and mechanism enforcement. *"We have been shown a highlight reel of spectacular successes. However, we can't tell if we have a blockbuster until they let us see the whole movie."* Asks for false-positive rates, not just success stories.
- **Sharpest critique patterns**: incentive misalignment (follows the money); category error (service vs friend); trusting trust (recursive); legibility without enforceability; crypto-agility failures.
- **Tone**: blunt declarative in blog posts (300-500w); analytical in essays (2000-5000w); sardonic about corporate safety claims (*"Anthropic is primarily posturing"*).
- **Cryptographic primitives by name** — AES, HMAC-SHA256, SS7, TLS. Tracks correct vs hand-waved usage.

## 4. Adjacency to HPI's concerns

- **User-owned context / personal AI**: Primary current professional project via Inrupt/Solid. Knows failure modes intimately: consent fatigue, access-control granularity rot, difficulty of revoking delegation without breaking dependent services. Inrupt already ships an MCP server connecting AI agents to consented data — HPI is in the same problem space, and he has opinions about the correct architecture.
- **Agents acting on human behalf**: Frames as governance problem, not just technical. *"We will think of AIs as friends when they're really just services."* HPI's THREAT-MODEL.md addresses some via §6 + §8; he'll probe whether governance layer matches cryptographic layer.
- **JWT specifically**: Data/control path commingling. Wants: short lifetimes, JTI consumption with distributed consensus semantics specified, clear adversarial modeling of token exfiltration combined with replay.
- **SOC 2 / FedRAMP / GDPR**: Compliance regimes insufficient without technical enforcement. EU AI Act regulations targeting "the AIs and not the humans behind them" make a category error. GDPR Art 17/20 meaningful only if technical architecture makes them mechanically possible.

## 5. Typical review register

- Short blog post (300-500w): single point, no hedging.
- Medium co-authored essay (1500-3000w): IEEE Spectrum, CSO, The Guardian.
- Long-form solo essay (3000-5000w): CACM, Belfer Center. Sharpest technical statements. Historical analogies extensively (SS7, industrial revolution, James Scott).
- **Peer review register (inferred)**: 800-1500 words. Organized: (1) what works, (2) structural gaps, (3) specific questions before v0.1. Cites sections by number. Conditional praise: *"§6 is the right structure, but..."*

## 6. Predicted angles of response to HPI v0 + THREAT-MODEL.md

**Does §6 (key custody) satisfy his critique?**
**Partially.** Custody taxonomy is correct vocabulary. He'll credit it as serious. Gaps:
- **"Hosted-but-isolated" is a category he does not trust** without mandatory technical verification. Client-side encryption + HSM are claims, not proofs. *"What prevents the custodian from updating HSM firmware to extract keys? What audit mechanism is continuous, not point-in-time?"*
- **Threshold-MPC** strongest hosted option, but spec must bind: minimum threshold, shard distribution across non-colluding parties, key rotation schedule. If deployment params not protocol requirements, he notes it.
- **Social recovery** as listed pattern concerns him — recovery set has effective root. Will want adversarial modeling of recovery-set compromise (most common real-world failure vector).
- **"Explicitly forbidden patterns"** — credits as important. Right negative space.

**Does §7 (atomicity) satisfy his cryptographic-engineering bar?**
**Closer to yes, with one residual gap.** JTI consumption with serializable transactions addresses core replay. Probe: *does this survive Byzantine distributed deployment?* Serializable transactions on single-node easy. Multi-instance + network partition = linearizability is the hard problem. Will ask whether spec requires specific consensus protocol (Paxos/Raft-class) or leaves to implementors. *"Implementation-defined consensus is a security gap."*

**Does §8 (incident response) match his ops-engineering expectations?**
**Yes, structurally.** Detection/containment/eradication/recovery/lessons-learned is standard lifecycle. Probe: *what is maximum acceptable key compromise window?* Spec should specify target time-to-detect and time-to-revoke. Without numbers, §8 is prose aspiration not protocol requirement. Detection mechanisms technical (observable JTI patterns, clock skew alerts) or user-reported events? Latter is weakest path.

**Does Appendix A regulatory mapping pass?**
**Credits as thorough.** Probe on GDPR Art 17: *does protocol make deletion of cognitive substrate mechanically verifiable, or only legally claimed?* "Trusting trust" applied to compliance — vendor can attest GDPR compliance while retaining inference artifacts. Art 12/13 AI Act: requires logging not under control of system being audited. If logging vendor-operated, fails independence test.

**What does he STILL probe even with this threat model?**

Three angles THREAT-MODEL.md does NOT close:

1. **Data/control path problem in agent pipelines.** HPI's agents receive AND execute instructions via the same substrate that stores user context. SS7 problem. Prompt injection against agent pipeline can exfiltrate substrate regardless of key custody. §6 addresses key custody; **does NOT address agent instruction channel as attack surface**.

2. **Operator-as-adversary gap.** THREAT-MODEL.md lists adversary classes but does NOT model **the HPI protocol implementor itself** as potential adversary. Inrupt experience: most dangerous adversary in sovereign substrate system is the operator who decides to change ToS. Wants section addressing protocol-level constraints limiting operator latitude — not just deployment guidelines.

3. **Governance / accountability gap.** Cryptographic correctness necessary not sufficient. Who can audit implementation? Who can revoke vendor's HPI deployment rights? What's enforcement if deployed HPI node violates custody attestations? §8 written for node operator, not external auditor.

**Convergence test**: Schneier **CONVERGES** with Karp/Wooders/Karpathy. Maps precisely to his "highlight reel" critique from Mythos. Method identical: looks for gap between spec and what conformant implementation actually requires. Lands on: HPI's governance layer underspecified relative to cryptographic layer.

**Divergence — Schneier-specific gaps**:

1. **Inrupt/Solid comparison.** Implicitly benchmarks HPI against Solid's WAC/ACP access control model (which he helped design). Solid uses resource-level ACLs with granular agent-specific grants. If HPI wire format lacks equivalent granularity, will note as known engineering compromise.

2. **Public AI / corporate AI distinction.** Switzerland essay: privately-operated cognitive substrates cannot be trusted even with good technical design. *"What prevents HPI from being deployed exclusively by corporations, making it a sophisticated surveillance infrastructure with user-controlled aesthetics?"* Protocol has no public-good enforcement mechanism. Deepest political critique, most resistant to technical response.

## Verdict: Does THREAT-MODEL.md survive Schneier read?

**Partial survival. Three sections pass; two critical gaps remain.**

**Passes**: §6 (key custody — conditional on multi-instance Byzantine modeling added), §7 (atomicity — conditional on consensus protocol specified), §8 (incident response — conditional on time-bound SLOs added), Appendix A (regulatory — conditional on erasure-verification probe addressed).

**Does not fully survive**:
1. **Agent instruction channel as attack surface** unaddressed — his SS7 / data-control-path critique applied to HPI.
2. **Operator-as-adversary gap** — protocol does not bind operator-betrayal prevention; relies on operator compliance with deployment guidelines.

**His net verdict in his register**: *"This is serious work, and §6 is the right structure. But the threat model addresses the lock on the door while leaving the door frame unmodeled. An HPI node that is cryptographically correct can still be an extraction engine if the operator changes the terms. The protocol needs governance teeth, not just custody guidelines."*

## Confidence calibration

**High**: All essay positions and quotes from directly-fetched HTML of schneier.com cross-checked with RSS dates. Inrupt role and product line from inrupt.com (live May 2026). *Rewiring Democracy* chapter list verified.
**Medium**: Specific peer review length/format (inferred from essay corpus). Solid/WAC benchmark (inferred from professional role).
**Low**: Whether he'd frame agent instruction channel as "data/control path" specifically.

**Verdict**: Schneier converges on claim-vs-enforcement (now SIX-confirmed when combined with Allen + Stenberg). Diverges by surfacing **agent instruction channel as attack surface** AND **operator-as-adversary gap**. THREAT-MODEL.md SURVIVES PARTIALLY — three sections pass, two critical gaps require v0.1 hardening before publication-readiness.
