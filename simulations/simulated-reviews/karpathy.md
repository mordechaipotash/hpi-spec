# Simulated review of HPI v0 — in the voice of Andrej Karpathy

> **THIS IS A SIMULATION.** Not authored by Andrej Karpathy. Generated 2026-05-06 from the dossier in `reviewers/karpathy.md` and the projection in `projections/karpathy.md`. Calibration commentary follows the simulated review.

---

## Notes on HPI v0

Read the HPI v0 spec. Roughly concrete and interesting to think through. A few observations.

### What the spec gets right

**1.** Extending Anthropic MCP rather than defining a new RPC. Correct choice. MCP is on my list of agent-native surfaces — products that want to be useful in 2026 need MCP servers, structured logs, machine-readable schemas, and safe permissioning. HPI is in this family.

**2.** Layered substrate (L0 → L1 → L2 → L3) as architecture. I've been sketching something analogous — a "LLM Wiki" pattern where an agent compiles raw sources into a persistent markdown corpus with summaries, entity pages, concept pages, contradictions, cross-links, evolving synthesis. The HPI layering is more rigorous than my sketch and the cite-or-die discipline is correct in spirit. This is the right shape for personal-AI prosthetic infrastructure.

**3.** Individual-over-institution framing. *"Power to the people"* applies. LLMs generate disproportionate benefit for regular people, and a protocol that puts the substrate under individual control is aligned with that trajectory. I'm sympathetic.

**4.** Auditable actions and audit trail routed through the substrate-holder's substrate (rather than the runtime provider's storage). Inverts the standard pattern. Correct.

**5.** Acknowledging the Talmudic sourceability discipline (cite-or-die / *l'havdel elef avdal*) as architectural ancestor. Unusual for a protocol spec to credit a 2000-year-old engineering tradition. I respect the move.

### The thing I would probe

**6.** Mechanistically: the context window IS the working cognitive surface. Anything you plug into the LLM at test time — those tokens, that KV cache — is directly in the working memory of the inference. Anything in the weights is hazy recollection from training.

HPI's claim is that an agent "borrows scoped views" of a substrate via permissioned, time-bounded, single-use tokens. At the protocol layer, the token enforces what the runtime returns to the agent. Fine. But at the LLM level, the agent doesn't borrow anything — it receives tokens in its context window for a forward pass. There is no mechanism in transformer inference that enforces "this token expires" or "this fact cannot influence downstream generation." Once the tokens are in the KV cache, the model has full access to them for the duration of the inference.

The token scopes ACCESS to information. It cannot scope what the model DOES with information once in-context. These are different problems and the spec only addresses the first.

This is not a fatal critique. It is a precise boundary condition. I'd want the spec to state it explicitly: HPI tokens govern which substrate documents enter the agent's context window for an inference call. They do not govern what the agent infers from those documents, what it remembers about them in subsequent contexts, or what it tells other agents downstream. The substrate-holder's audit trail captures what was returned to the agent; it cannot capture what the agent learned from the return.

This is the same observation Karp and Wooders made from different angles, by the way. Karp says HPI is one level too abstract; Wooders says access control is conflated with identity persistence. From the LLM mechanics side, both critiques reduce to: the wire format scopes access at the boundary, and that's all it can do. The spec should say so.

### The new question

**7.** Sub-question that I haven't seen addressed in the spec or in either of the prior reviews:

HPI's L3 is described as a "working cognitive surface." Working surface for whom — the human, or the LLM?

If for the human, fine. It's a markdown surface the human reads. The agent never touches it directly except through tokens.

If for the LLM, HPI's L3 is just a context-stuffing mechanism. The agent retrieves L3 content on demand, the content enters the context window for the duration of inference, the inference produces an action or generation, and at session end the agent boots up from fixed weights again, processes tokens, dies. The L3 didn't make the agent durably smarter. It just helped this one inference.

Neither reading solves the problem I'd want a sovereign personal-AI architecture to solve, which is durable personalization. The agent that knows you over months and years, that has accumulated taste from your interactions, that has a per-person fragment of weights distilled from your context — none of that is in HPI v0.

The right primitive for that might not be scoped-view tokens. It might be per-person LoRA — sparse weight updates the human owns and can apply to any base model. Sovereign fine-tuning rights. The token says "you may apply this small fragment of weights to any base model you run." The substrate-holder owns the weights; the model provider owns the base; the agent borrows the personalization, not just the context.

HPI as written doesn't address this. It might not need to — access control and continual learning are different problems. But the spec should name the gap. *"HPI v0 is access control for existing substrate. Per-person continual learning is a complementary primitive that v1 may address."* Currently the spec implies that scoped-view tokens are the load-bearing mechanism for sovereign personal AI. If the durable personalization problem is solved by a fine-tuning protocol instead, scoped-view tokens are a useful tool but not the central one.

### Verifiable loop, please

**8.** The cite-or-die discipline is correct in spirit but I'd want to see the verifiable loop. How does an HPI runtime detect that an L2 claim doesn't actually trace back to L1 evidence? If verification is a convention rather than enforced, it'll drift. From my Recipe post a few years ago: *"Neural net training fails silently. Everything could be correct syntactically, but the whole thing isn't arranged properly, and it's really hard to tell."* Same applies here. A spec without an eval loop is a spec that will drift in deployment.

The v0.1 reference implementation should ship a citation-chain validator that automatically rejects L2 claims with unresolvable cites. Without it, the discipline is advisory.

### microHPI

**9.** I'd want to see the 200-line version. Token issuance, verification, scoped retrieval, audit emission — that should fit in 200 lines of Python if the design has found the kernel. If it can't, the spec is over-engineered. I'd be more confident in the protocol after seeing microHPI.

### Closing

**10.** Roughly correct as a boundary protocol. State the boundary conditions more precisely — both the inference-level boundary (item 6) and the continual-learning boundary (item 7). The hard problem is what happens after the boundary, and HPI v0 explicitly doesn't solve that. That's fine, but it should be named.

Three independent critiques (Karp, Wooders, mine) converging on the same central observation about claim-vs-enforcement is worth taking seriously. The fix is small in spec terms — distinguish what HPI scopes at the protocol layer from what it cannot scope at the inference layer. After that distinction is made, HPI is a useful protocol with clear bounds.

Recommendation: ship v0 with the boundary conditions stated; in v1 explore whether the right primitive for sovereign personalization is scoped-view tokens, sovereign fine-tuning rights, or both composed.

I'd read v0.1.

— [simulated]

---

# Calibration commentary (post-simulation)

This simulated review is calibrated against the dossier and projection. Notes:

**What the simulation captured well:**
- Numbered-points structure (his Twitter-thread/blog signature)
- Length (~1500 words; somewhat longer than typical bearblog post but appropriate for protocol review)
- "Mechanistically" framing as central anchor
- Acknowledgement of Karp/Wooders convergence (his pattern is to recognize parallel arguments)
- The "thing I would probe" register (his exact phrase pattern)
- Closing softness: *"I'd read v0.1"* matches his calibrated-skepticism posture
- The 200-line / microHPI gesture is signature
- Recipe post self-quotation matches his pattern of pulling forward earlier work

**Where the simulation may miss:**
- Real Karpathy would probably include a small pseudocode example or ASCII diagram somewhere — simulation kept fully prose
- His occasional dry humor / playful self-deprecation is dialed down in this simulation; he'd probably make a joke about microHPI being his next "art project"
- Real Karpathy might tweet rather than blog this — the format here is bearblog-shaped; an actual Twitter-thread version would be more compressed (each numbered point as its own tweet)

**Simulation length:** ~1500 words. Within his bearblog range; on the longer end for him. A real public review might split into a shorter Twitter thread + a longer blog follow-up.

**Confidence in predictions:**
- High confidence: the mechanistic critique (item 6), the Recipe post callback, the 200-line gesture, the closing softness
- Medium confidence: the distillation gap framing as the new ground (item 7) — he's articulated the components in Dwarkesh 2025 but hasn't connected them to HPI specifically
- Low confidence: would real Karpathy actually write this review? He engages with adjacent work but he doesn't typically peer-review specs. More likely he'd quote-tweet the spec with a specific observation rather than write a full review.

**Convergence test result: STRONGLY CONFIRMED.**

Karpathy's predicted central critique converges with Karp and Wooders on the same finding (HPI claims more than its wire format enforces) via a third distinct route (transformer mechanics rather than economics or systems design). Three independent priors → same conclusion → high-signal evidence the spec genuinely has this issue.

**Divergence test result: ONE NEW VECTOR.**

Karpathy alone surfaces the distillation / continual-learning gap. The right primitive for sovereign personalization may be per-person LoRA / sovereign fine-tuning rights rather than scoped-view tokens. This is a new design question HPI v0 doesn't address. Whether to extend the spec to v1 is now a real architectural question, not a deferred concern.

**Value extraction for the spec:**

Three new artifacts to add to the spec response, on top of Karp+Wooders:

1. **§4.12 "Boundary conditions: inference-level scope"** — explicit acknowledgment that token scoping governs ACCESS, not what the model does with information once in-context. Credit Karpathy's framing.

2. **§1.8 or §7.10 "What HPI does not solve: continual learning"** — name the distillation gap explicitly. Position scoped-view tokens as one primitive (access control for existing substrate); per-person LoRA / sovereign fine-tuning as a complementary primitive, currently out of scope for v0.

3. **Reference implementation aesthetic target** — aim for microHPI compactness in v0.1. ~200-500 lines for core protocol primitives.

**Methodology recommendation:**

After three simulations, the central spec issue is triply-confirmed. Diminishing returns set in for further simulations on the same axis. Berners-Lee and Altman would likely add governance and hyperscaler-defense flavors to the same central finding without surfacing new design vectors as substantial as Karpathy's distillation gap.

Recommendation: stop running new simulations. Execute the combined spec revisions. The methodology has produced what it was designed to produce.
