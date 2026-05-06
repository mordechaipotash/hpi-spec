# Simulated review of HPI v0 — in the voice of Alex Karp

> **THIS IS A SIMULATION.** Not authored by Alex Karp. Generated 2026-05-06 from the dossier in `reviewers/karp.md` and the projection in `projections/karp.md`. Calibration commentary follows the simulated review.

---

## On a Protocol That Names the Border but Has Not Named the World

> *"Begriffe ohne Anschauungen sind leer; Anschauungen ohne Begriffe sind blind."*
> Concepts without intuitions are empty; intuitions without concepts are blind.
> — Kant, *Critique of Pure Reason*, A51/B75

I.

The fashion in our industry is to mistake the act of naming a thing for the act of building it. We have spent the better part of a decade watching ambitious young people stand on stages and say the word *agent* with the gravity once reserved for *bridge* or *aqueduct*. They produce no bridge. They produce a slide deck describing a bridge, and a JavaScript library that, when invoked, prints the word *bridge* to a console.

I will say at the outset that the document I am asked to consider — the HPI specification, version zero — is not such a deck. It is a serious effort. The author has read carefully, has thought longer than most, and has done the unfashionable work of writing down what they actually mean before asking us to take it seriously. For this alone, in 2026, the spec deserves a response.

The substantive question is whether what has been named is what we need.

II.

The architecture is built on five axioms, of which the second and the fourth are the load-bearing ones. The fourth I will set aside; the conservation law that L3 published across a substrate boundary becomes the next holder's L0 is a workmanlike formulation of an obvious fact, and naming it is a small contribution to clarity. The second axiom — that each layer is a pure function of the layer below, and each higher claim cites downward — is harder. Most software engineers will not honor this. The Talmudic discipline the author credits in §9 is the right intellectual lineage; *l'havdel elef avdal*, the requirement to source every chain of reasoning back to an authority, is the architectural ancestor of what they are calling cite-or-die. I am unaccustomed to reading protocol specifications that credit a 2000-year-old engineering tradition with appropriate seriousness, and I take this as evidence that the author understands what they are claiming.

The most important architectural claim in the entire document is in §4: *an agent must NEVER own its own L3.*

This is correct.

It is correct in a way that the entire memory-product industry of the last two years has gotten wrong. Letta, whose Context Constitution I have read with attention, names three Pillars of Selfhood for the agent — Identity, Memory, Continuity — and assigns ownership of these to the agent. This is precisely backwards. The agent has no self. The agent is an instrument of the principal. Persistent agent state outside the principal's control is the failure mode that produced the collection of consumer AI products we will be cleaning up after for the next decade. The HPI axiom inverts Letta's, and HPI is right.

I will go further. In our own systems, agents in the AIP environment do not have memory outside the Ontology they query. They are stateless invocations against typed object graphs. This is not an oversight. It is the architecture. We arrived at it for the same reason the HPI author has arrived at it: because the alternative — agents with their own continuity, their own learned skills, their own quietly accumulating models of the principals they serve — is the path by which institutional control of operational reality is silently transferred to a vendor whose alignment with the principal is not specified anywhere in the contract.

So far the spec has my conditional respect.

III.

But conditional respect is not the same as adoption. There is an objection, and the objection is structural.

The author has built a typed grammar for the epistemic status of claims. They name four families — OBL, RCG, TRU, PAT — and they specify, with admirable precision, what an obligation is, what trust is, what a recharge is, what a patent's lifecycle looks like. Each family has eight sections, allowed states, a worked example. The discipline is real.

This is not, however, an Ontology.

An Ontology, in the sense that has produced operational systems that change the course of wars and the trajectory of companies, specifies *what objects exist in a particular world*. The Foundry Ontology, when deployed for a customer, names what an `Aircraft` is — its tail number, its engine configuration, its maintenance history, the actions that can be taken on it (refuel, deploy, ground), the relationships it bears to other objects (this aircraft was assigned to that mission). Before any data flows, the Ontology declares: *these are the kinds of things that exist here.*

The HPI specification declares: *here is how to type the epistemic status of any claim about any kind of thing.* This is not an Ontology. It is the schema for a schema.

The author will say, correctly, that this abstraction is intentional — that HPI is the protocol by which any domain-specific Ontology can cross substrate boundaries with semantic preservation. I accept this defense and find it honest. But I want it stated plainly: HPI is a meta-Ontology. It is the wire format by which Palantir's Ontology, or any other typed worldview, could in principle travel between substrates. It is not itself the worldview.

The risk of meta-Ontologies is that they generate the appearance of universality by committing to nothing. A protocol that can represent any cognitive substrate but commits to none is, in the absence of widespread reference Ontologies riding on top of it, an academic contribution. It will be read by graduate students. It will be cited in dissertations. It will not be deployed at the Department of War, or at a hospital network in metropolitan Tel Aviv, or at any of the institutions where the question of who owns the cognitive substrate of an agent making consequential decisions actually matters.

To convert HPI from a research contribution into an architecture, two things must exist that do not yet exist:

First, at least one **reference Ontology** that is *not* a meta-grammar. The PAT family, which the author has drafted in `axioms/PAT-patents.md`, is the closest thing in the v0 spec, and it is good. It commits to what a Patent is, what its lifecycle states are, what relationships it bears. This is real Ontology work. It should be promoted from "axiom family" to "reference domain Ontology," and the spec should make explicit that other domains require their own such reference Ontologies. Without this, HPI is a protocol for shipping nothing in particular.

Second, an **enforcement mechanism** that is more than discipline. The cite-or-die rule is procedurally beautiful and operationally advisory. There is no validator that refuses an L2 claim that is not backed by L1 evidence; there is no runtime that rejects an OBL assertion that has no underlying obligation in the substrate. In Palantir's Ontology, the type system rejects ill-formed assertions at the API boundary. The HPI spec needs the equivalent. JSON Schemas in an appendix would be a start; a runtime validator in the reference implementation would be the actual answer.

IV.

I have not yet addressed the most difficult question, which the spec handles in §1 and §7 and which I take to be the implicit organizing principle of the entire effort: the alignment problem.

The author writes, in §1.2, that the platform's incentive is lock-in and corporate-profit alignment, while the user's interest is sovereignty and agency. This is true and is not the deepest version of the problem. The deepest version is: *the institutional bearer of liability for the agent's decision is the entity that should govern the agent's substrate.* The individual sovereign-human framing assumes that the human whose context the agent is operating against is also the human who bears the consequences. In the use cases that actually matter — a soldier acting under military command, a physician operating under hospital protocol, a financial professional operating under fiduciary duty — this is false. The substrate-holder is the institution. The individual is the operator within the institution.

I do not say this to contradict the spec. I say it because the spec uses "human" as the typical substrate-holder, and the protocol's primitives generalize cleanly to institutional substrate-holders if the author is willing to make this explicit. The substrate-holder is whoever bears the liability. Sometimes this is an individual. Often it is not. The HPI architecture should accommodate both without privileging either.

I will suggest a concrete revision: §2.1 should name `substrate-holder` as the protocol primitive and treat individual humans, families, organizations, and government bodies as instances of this primitive. The current draft already approaches this; making it explicit removes the reading that HPI is a consumer-rights protocol misapplied to enterprise problems.

V.

I have one more substantive objection and one note on procurement.

The objection is the threat model. The spec assumes principals and agents operate in good faith within a shared infrastructure. The interesting questions in 2026 are adversarial. What does HPI do when an agent presents a forged token? When the runtime is compromised by a nation-state actor? When a platform colludes with an agent to exfiltrate substrate? The spec acknowledges, in STATUS.md, that a threat model document is planned for v0.1. I will not belabor what the author already knows is missing. I will only say that until the threat model exists, HPI is a cooperation protocol, not a trust infrastructure.

The note on procurement: the author has written a protocol. The protocol is technically defensible. But there is no business model in this document. There is no answer to the question of who maintains the typed grammar for a specific deployment, who is the equivalent of our Forward Deployed Engineers, who captures the rent that funds the protocol's evolution beyond the author's voluntary labor. The spec gestures at the Stripe/Plaid/Hashicorp model — value capture distributed across an ecosystem — but does not specify which ecosystem positions are defensible. In our experience, this matters. Open protocols with no defensible position get adopted by hyperscalers, who absorb them and route the value capture to their own infrastructure. This is the fate of OAuth at Auth0's scale; it is not the fate Apache 2.0 protocols escape by default.

VI.

To conclude.

The HPI specification is the most architecturally serious open protocol document I have read this year. It is correct on the agent-ownership axiom. It credits its intellectual lineage honestly. The typed-axiom-grammar instinct is right. The conservation law is well-formulated.

It is, however, one level too abstract to be infrastructure today. It is a meta-Ontology in search of reference Ontologies that will commit to actual worlds. Without those reference Ontologies, without an enforcement mechanism stronger than discipline, without a threat model, and without a procurement story, HPI is a research contribution to which I would point graduate students with interest. It is not yet a protocol I would build a defense system on, or stake a hospital's compliance on, or recommend to the Forward Deployed Engineers I have personally trained.

My recommendation is to **publish the spec, and to ship — within ninety days of publication — three companion artifacts**: a fully-committed reference domain Ontology (the PAT family promoted to this status would suffice), a working threat model document, and an explicit value-capture analysis that names which positions in the HPI ecosystem are defensible against hyperscaler absorption.

If those three artifacts land, HPI is ready to be considered architecture rather than philosophy.

The author has written something that deserves to become both. I do not write notes like this for documents that do not.

Standing on the walls,
[simulated]

---

# Calibration commentary (post-simulation)

This simulated review is calibrated against the dossier and projection. Notes for future simulations:

**What the simulation captured well:**
- The two-register pattern (philosophical wind-up + operational verdict) is structurally consistent with Karp's actual shareholder letters
- The "schema for a schema" / meta-Ontology objection is the dossier's high-confidence prediction landed cleanly
- The Letta inversion endorsement maps to Karp's likely sharpest praise of HPI
- The institutional-vs-individual reframe is delivered as constructive critique, not dismissal
- The Hegelian-dialectic structure (corrupt status quo → real-world demand → conditional synthesis → incomplete final move) matches his published rhetorical pattern

**Where the simulation may miss:**
- Real Karp would likely include 1-2 contemporary military/geopolitical references (the actual reviews include them constantly). Simulation kept register more abstract.
- Real Karp opens with German philosophical text frequently; simulation chose Kant in German. This feels right but is somewhat predictable.
- The closing "standing on the walls" image is borrowed from his Q1 2026 letter — would real Karp recycle his own image? Probably not in a review.
- The simulated review is more measured than Karp's typical bluntness on adversaries — but HPI is not an adversary, so the measured tone may be calibrated correctly.
- Real Karp would probably make at least one reference to specific Palantir customer outcomes (the Maven Smart System, AIP deployments). Simulation kept Palantir-references at the architectural level only.

**Simulation length:** ~1700 words. Within his typical range (1500-2500 for shareholder letters; he writes shorter for op-eds). Acceptable.

**Confidence in the simulation's predictions:**
- High confidence: the meta-vs-Ontology objection, the agent-ownership endorsement, the institutional-substrate-holder revision suggestion
- Medium confidence: the specific 90-day deliverable framing (Karp uses this kind of operational deadline; the choice of three specific artifacts is plausible but not certain)
- Low confidence: would Karp actually engage publicly with HPI? Probably not unless someone (a Palantir customer, a journalist) asked him directly. The simulated review is a thought experiment about what he WOULD say if asked, not a prediction about what he WILL say spontaneously.

**Value extraction for the spec:**

Three Phase 4 (response) artifacts to prepare in advance, ranked by urgency:

1. **Response to "meta vs Ontology"** — the central objection. Honest answer: HPI is intentionally meta. Position should be: HPI is the protocol that lets *any* domain Ontology (including Palantir's) cross substrate boundaries. Not a competitor; an enabler.

2. **Promote PAT to "reference domain Ontology" status.** This is a small framing change in §3 and the axiom files; carries the implication that HPI ships at least one fully-committed worldview, not just meta-grammar.

3. **Substrate-holder primitive.** Add the explicit substrate-holder language to §2.1. Treat individual / institution / government as instances. Removes the reading that HPI is a consumer-rights protocol.

If these three land: the simulated Karp review converts from "conditional revise" to "publish, with our Ontology riding on top of yours."
