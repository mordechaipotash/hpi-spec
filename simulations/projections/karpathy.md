# Projection — Andrej Karpathy on HPI

**Compiled:** 2026-05-06 from `reviewers/karpathy.md` + SPEC.md v0.
**Method:** Project Karpathy's most likely reactions, focused on the convergence test (does he validate Karp+Wooders central finding?) and the divergence test (does he surface new ground?).

---

## Overall stance: ENGAGED, MECHANISTICALLY-CORRECTIVE, OPENS NEW DESIGN QUESTION

Confidence: high.

Karpathy will engage HPI as serious work. He will not dismiss it. He will mostly endorse the architectural choices (MCP extension, layered substrate, individual-sovereignty framing) — these align with positions he's published. He's already explicitly endorsed MCP as a required agent-native surface (Sequoia 2026).

He will state the central critique mechanistically: **the context window IS the working cognitive surface; protocol-layer token scoping cannot constrain what happens inside transformer inference once tokens are in-context.** Same finding as Karp/Wooders, different route.

He will then open a question they didn't: **is the right architecture scoped-view tokens at all, or sovereign fine-tuning rights / per-person LoRA?** This is genuinely new ground.

His review register is the most distinctive: ~700-1000 words, numbered points, mechanistic precision, occasional dry humor. Not pamphleteer (Karp), not blog-post (Wooders). Closer to a Twitter thread compressed into a numbered structure.

---

## Sections he'll engage with most

Ranked by predicted depth:

1. **§4 Token Handoff Protocol** — most engagement. The central mechanistic question lives here. He'll scrutinize whether the JWT scope mechanism survives contact with transformer inference.
2. **§2 Substrate Model** — second-most. The L0–L3 layering will draw his attention because he's building something analogous (the "LLM Wiki" pattern in Sequoia 2026). Will probe whether L3 is for the human or the LLM.
3. **§3 Typed Axiom Grammar** — moderate engagement. Verifiability framework will check whether typed claims are actually enforced.
4. **§5 Wire Format** — moderate. MCP extension is on his agent-native list; he'll endorse but probably probe specific failure modes.
5. **§7 Non-Goals** — moderate. The "not anti-LLM" subsection he'll appreciate. The "not a memory product" subsection might draw a comment about whether HPI inadvertently treats memory anthropomorphically.
6. **§1, §6, §8, §9** — light engagement. He may quote-tweet §9's Torah lineage credit favorably (he respects unusual intellectual lineages).

---

## Specific objections, ranked by predicted probability + sharpness

### Objection 1 — "The context window IS the working cognitive surface" (P=0.95, sharpness=high, MECHANISTIC route to convergent finding)

**The line:** *"HPI's central claim is that agents borrow scoped views via tokens. The protocol layer enforces what tokens permit. But at the LLM level, the agent doesn't 'borrow' a view — it receives tokens in its context window. The KV cache is the working memory of the inference. There is no mechanism in transformer inference that enforces 'this token expires' or 'this fact cannot influence downstream generation.' Token scoping happens AT the protocol boundary; nothing constrains what the model does with information once in-context. This is not a fatal critique — it's a precise boundary condition the spec should state explicitly."*

**Why this is sharp:** Mechanistically correct, and his Dwarkesh 2025 framing makes it inescapable. *"Anything in the context window is directly in the working memory."*

**Where it lands:** Lands cleanly. The spec should acknowledge this boundary condition explicitly. HPI's tokens scope ACCESS to information (which documents enter the context window for an inference call); they cannot scope what the model DOES with the information. These are different problems and only the first is in HPI's domain.

**Convergence note:** Same finding as Karp's "meta vs Ontology" and Wooders' "access control conflated with identity persistence." All three reviewers, three different routes, same conclusion: the spec claims more than its wire format enforces. **The convergence is now triply-confirmed.**

### Objection 2 — "The distillation gap" (P=0.85, sharpness=medium-high, NEW GROUND)

**The line:** *"HPI's L3 is described as a 'working cognitive surface.' For whom is it working — the human, or the LLM? If for the human, fine — it's a markdown surface the human reads. If for the LLM, it's just a context-stuffing mechanism that dies at session end. Either way, this doesn't solve the problem I'd want a personal-AI architecture to solve, which is durable personalization. The right architecture might be per-person LoRA / sovereign fine-tuning rights — small sparse weight updates the human owns and can apply to any base model. HPI's scoped tokens are useful for access control on existing material; they don't address how learned content distills back into a sovereign model fragment. The spec might be solving the wrong problem."*

**Why this is sharp:** This is genuinely new ground vs Karp/Wooders. They critiqued the spec's enforcement claims; Karpathy critiques the spec's design choice. He's saying: even if the conflation is fixed, scoped-view tokens may be the wrong primitive for sovereign personalization.

**Where it lands:** Partially. HPI v0 explicitly does NOT specify continual learning or model personalization — those are out of scope. But the spec also doesn't acknowledge that this is a different problem from the one HPI solves. Honest revision: §1 or §7 should name this distinction explicitly. HPI is access control for existing substrate; per-person LoRA / continual learning is a complementary problem requiring different primitives.

**Possible composition:** HPI's tokens govern access to substrate; the agent's per-person LoRA is updated only with human-issued write tokens that authorize substrate modification AND model-fragment update. Two-layer authorization. This is genuinely interesting and would be the spec's response to Karpathy's new vector.

### Objection 3 — "Verifiable loop, please" (P=0.75, sharpness=medium)

**The line:** *"The cite-or-die discipline is correct in spirit. But what's the verifiable loop? How does an HPI runtime detect that an L2 claim doesn't actually trace back to L1 evidence? If verification is a convention rather than enforced, it'll drift. From my Recipe post: things fail silently when the error surface is logical rather than syntactic. A spec without an eval loop is a spec that will drift."*

**Where it lands:** Real gap. The spec mentions JSON Schema for v0.1 but doesn't specify a runtime validator. Karpathy's verifiability frame is correct: an enforced cite-or-die requires automatic verification; advisory cite-or-die will degrade.

**Revision:** v0.1 reference implementation should include a citation-chain validator. Add to §6 explicit conformance-test mechanism for cite-or-die.

### Objection 4 — "What's the 200-line version?" (P=0.65, sharpness=low-medium)

**The line:** *"I'd want to see microHPI — the 200 lines of Python that implement the irreducible core of the protocol. If you can't state it that compactly, the spec hasn't found the kernel. Token issuance + verification + scoped retrieval + audit emission. That should fit in 200 lines if the design is right."*

**Where it lands:** Partial. The full spec is necessarily larger than 200 lines (it's a protocol document, not a reference impl). But the *reference implementation* should aim for that compactness. Karpathy's challenge maps onto the v0.1 reference impl target — that should be a microHPI in his style.

**Action:** Reference implementation v0.1 (already on roadmap) should be designed with Karpathy's compactness aesthetic. Aim for ~200-500 lines for the core protocol primitives.

### Objection 5 — "Don't anthropomorphize agent memory" (P=0.55, sharpness=low)

**The line:** *"The spec is mostly clean on this, but watch the language. Agents don't 'maintain state' or 'accumulate context' in the human sense. They have tokens in their context window. The spec sometimes drifts toward agent-as-person framing. The Letta comparison doc walks this line carefully — but the SPEC.md prose occasionally implies agents have continuity that they don't have, mechanistically."*

**Where it lands:** Soft critique. Worth a prose-level pass for anthropomorphic phrasing.

---

## Specific endorsements, ranked by predicted probability

### Endorsement 1 — "MCP extension is correct" (P=0.95)

He explicitly endorsed MCP servers as required agent-native surface (Sequoia 2026). HPI extending MCP rather than defining new RPC is on his approved list.

### Endorsement 2 — "Individual-over-institution framing" (P=0.85)

His "Power to the people" thesis is directly aligned. *"LLMs generate disproportionate benefit for regular people."* HPI's individual-sovereignty axiom matches this trajectory.

### Endorsement 3 — "Layered substrate" (P=0.80)

He's building analogous "LLM Wiki" pattern. Will recognize L0→L3 as the correct architecture for personal-AI prosthetic. *"raw sources into a persistent Markdown wiki: summaries, entity pages, concept pages, contradictions, cross-links, logs, and evolving synthesis."*

### Endorsement 4 — "Audit trail as substrate stream" (P=0.75)

Auditable actions are on his agent-native list. The decision to route audit through the substrate-holder's substrate (not the runtime's storage) he'll find correct.

### Endorsement 5 — "Cite-or-die instinct" (P=0.65)

Verifiability framework adjacent. He'll endorse the *direction* even if he probes the enforcement.

### Endorsement 6 — "Torah sourceability lineage" (P=0.55)

Surprise endorsement. He respects unusual intellectual lineages (cites Sutton's Bitter Lesson, Lasch, Houellebecq in his own work). The §9 Torah credit is the kind of move he'd quote-tweet favorably.

---

## What he'll PROPOSE (the constructive payoff)

Two-layer authorization framing for the distillation gap:

> *"HPI's tokens govern access to substrate (L0–L2). For per-person model personalization, you need a complementary primitive: a write-token that authorizes substrate modification AND model-fragment (LoRA) update. This is two-layer authorization, with HPI as the outer layer and a continual-learning protocol as the inner. The spec should name this explicitly — HPI v0 is access control; personalization-and-continual-learning is v1 territory."*

This is the constructive close that would convert his review from "interesting limits" to "interesting boundary, here's what's beyond it."

---

## Predicted register and structure of his actual review

If Karpathy reviewed HPI publicly (he might — he engages with adjacent work, especially on Twitter/X):

**Format:** Numbered list of compressed observations. Could be a Twitter thread or a short bearblog post.
**Length:** 700-1000 words. Not pamphleteer (Karp 1700w), not blog-post (Wooders 1700w). Tighter.
**Structure:**
1. Brief endorsement of what's right (MCP, layer model, individual framing)
2-3. Mechanistic critique (context window IS working memory; tokens scope access not inference)
4. New ground: distillation gap / per-person LoRA
5. Verifiable loop request
6. The 200-line version aspiration
7. Closing posture: calibrated skepticism, not rejection

**Voice patterns:**
- "The thing I would probe..."
- "Mechanistically..."
- "Anything in the context window IS the working memory"
- "Roughly concrete and interesting to think through"
- "I still feel there's so much work to be done"
- Occasional dry humor / playful self-deprecation

---

## Predicted closing recommendation

**Engaged calibrated skepticism with new vector identified.** Not "publish unchanged" — wants the boundary conditions stated precisely. Not "reject" — the architecture is too aligned with positions he's already published. Most likely: *"Roughly correct as a boundary protocol. State the boundary conditions more precisely. The harder problem is what happens after the boundary — continual learning, sovereign fine-tuning rights — and that's not what this spec solves. Maybe v1 should."*

If real Karpathy engaged: HPI would likely benefit from a Twitter-thread acknowledgment that's substantially more impactful than any Letta blog post would be — Karpathy's public engagement reshapes adoption trajectories at scale.

---

## What this projection produces for Phase 4 (response)

Three new artifacts to add to the spec response, on top of Karp+Wooders:

1. **§4.12 "Boundary conditions: what HPI does and does not scope at the inference level"** — explicit acknowledgment that token scoping governs ACCESS, not what the model does with information once in-context. Cites Karpathy's framing.

2. **§1.8 or §7.10 "What HPI does not solve: continual learning and personalization"** — explicit statement that per-person LoRA / sovereign fine-tuning is a complementary problem. HPI v0 is access control for existing substrate; v1 may extend.

3. **§6 update** — reference implementation target should aim for "microHPI" compactness aesthetic. ~200-500 lines for core protocol primitives.

**Cross-reference with Karp+Wooders:**

- All three reviewers identify the SAME spec issue (claims more than enforced) via DIFFERENT routes. Convergence triply-confirmed.
- Karpathy ALONE surfaces the distillation/continual-learning gap. This is genuinely new.
- The combined revisions from all three simulations: ~20-25 spec improvements, ~25-30 hours of focused revision work.

The methodology has now produced:
- **Strong evidence the central spec issue is real** (three priors converge)
- **One new design question** that HPI v0 hadn't acknowledged (distillation gap)
- **A clear path to v0.1** with substantive revisions

After Karpathy: diminishing returns are real. Berners-Lee and Altman would likely converge on the same central critique with new flavor (governance for BL, hyperscaler-defense for Altman) but unlikely to surface another design vector as substantial as the distillation gap.

Recommendation: stop simulations after Karpathy unless a fresh divergence is needed. Move to spec revisions + reference impl.
