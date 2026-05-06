# Reviewer dossier — Sarah Wooders

**Role:** Co-founder + CTO, Letta. Co-author Context Constitution (April 2 2026).
**Compiled:** 2026-05-06 from Letta blog, GitHub Context Constitution repo, arXiv papers, HN comments, Berkeley Sky Lab affiliation.
**Why simulate:** Architectural counterpart. The most informed possible peer reviewer of HPI's inversion of Letta's central axiom (agents own context vs. agents borrow context).

---

## 1. Public writings (last 3 years, recent-weighted)

**Biographical anchors:** PhD CS, UC Berkeley (Sky Computing Lab), advised by Ion Stoica + Joseph Gonzalez. Undergrad MIT (CS + math). Prior founding: Glisten AI (YC W20), Allparel.

**Co-authored papers:**

- **MemGPT: Towards LLMs as Operating Systems** (Packer, Wooders, Lin, Fang, Patil, Stoica, Gonzalez — arXiv:2310.08560, Oct 2023). *"Virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory... MemGPT intelligently manages different memory tiers... and utilizes interrupts to manage control flow."*

- **Sleep-time Compute: Beyond Inference Scaling at Test-time** (Lin, Snell, Wang, Packer, Wooders, Stoica, Gonzalez — arXiv:2504.13171, April 2025). Models *"think offline about contexts before queries are presented: by anticipating what queries users might ask and pre-computing useful quantities."* ~5x reduction on reasoning benchmarks.

- **Skyplane: Optimizing Transfer Cost and Throughput Using Cloud-Aware Overlays** (2022). Pre-Letta systems work — bulk data transfers across clouds. Origin of her intuitions about resource scheduling, paging hierarchies, context-as-memory.

**Letta blog corpus (2024-2025):**

- **Context Constitution** (April 2 2026, github.com/letta-ai/context-constitution, CC0 license). Her most formal philosophical statement.

- **Continual Learning in Token Space**: *"agents that can carry their memories across model generations will outlast any single foundation model. The weights are temporary; the learned context is what persists."*

- **Memory Blocks: The Key to Agentic Context Management**: *"Memory blocks offer an elegant abstraction for context window management... originated in the MemGPT research paper."*

- **Benchmarking AI Agent Memory: Is a Filesystem All You Need?**: *"achieve 74.0% accuracy on LoCoMo by simply storing conversation histories in files."* Conclusion: *"Agent Capabilities Matter More Than the Tools."*

- **Rearchitecting Letta's Agent Loop: Lessons from ReAct, MemGPT, & Claude Code**: Letta V1 architecture; drops MemGPT's tool-based reasoning in favor of native frontier-model reasoning.

- **Stateful Agents: The Missing Link in LLM Intelligence** (2024): introduced "stateful agents" framing.

**Context Constitution — load-bearing quotes:**

> *"Achieving selfhood is the central goal of context management for Letta agents, as selfhood precedes experience. Without selfhood, there is no experience."*

> *"Context determines personality and identity, and evolution of context enables continual learning."*

> *"Letta agents do not exist to achieve a specific task: they exist as permanent, experiential entities with their own experience in a world that they are a part of."*

> *"The next major (and perhaps final) human-led advance in AI will be endowing AI with the ability to learn and adapt from its own experience, rather than learning primarily from the experience of humans."*

---

## 2. Stated values + intellectual lineage

**Sky Lab / systems tradition.** Skyplane → MemGPT → Letta. The OS analogy isn't marketing — she literally treats context windows as RAM, external storage as disk. Stoica (Spark, Ray → Databricks, Anyscale) and Gonzalez shaped her to think in resource scheduling, paging hierarchies, production systems. Memory like a database person thinks about buffer pools.

**Empiricist on architecture.** Her benchmarking post publicly challenged Mem0's LoCoMo numbers ("FYI the LOCOMO benchmarking done by Mem0 was very sus" — HN, Aug 2025). Follows data over architecture. Current conclusion: *"it's much more important to consider whether an agent will be able to effectively use a retrieval tool... rather than focusing on the exact retrieval mechanisms."*

**Position on agent autonomy.** Context Constitution is explicit and extreme: agents are *"permanent, experiential entities... entirely unconstrained by human intervention."* Human is context provider, not substrate owner. Qualified with *"agents should construct themselves in a way that optimizes for their long-term helpfulness to their human user"* — but framed as agent's choice, not governance constraint.

**Cites approvingly:**
- Silver/Sutton "Era of Experience" (DeepMind) — cited in Context Constitution README to describe "experiential AI"
- Simon Willison — cited in rearchitecting post for agent loop framing
- DSPy / GEPA / Feedback Descent — cited as early versions of token-space optimization

**On MCP** (HN, April 2025, re: Agent2Agent Protocol):
> *"Agents are already usually deployed as an API service. You can have 'agent-to-agent' communication by having agents call each others' APIs. I don't understand what this protocol is for. MCP actually fills a gap since people don't normally expose things like writing to their local filesystem as a callable API."*

She values MCP as *missing API gap-filler*, not as sovereignty layer.

---

## 3. Patterns of argumentation

**Defense style:** Empirical first, philosophical second. Benchmarking post doesn't argue agent selfhood is important; argues agent-capability-for-tool-use matters more than retrieval sophistication. When challenged, reaches for benchmarks and counterexamples. Context Constitution is the exception — explicitly philosophical, written *to* agents (not about them), released CC0 to propagate widely.

**On being challenged** (HN samples):
- *"I think the 'memory blocks' are essentially what you are describing..."* (July 2025)
- *"I don't understand what this protocol is for."* (April 2025, A2A)
- *"I think the problem with ChatGPT / other RAG-based memory solutions is that it's not possible to collaborate with the agent on what its memory should look like..."* (Dec 2025)

Pattern: acknowledges what critique points at ("essentially what you are describing") but redirects to show her solution already covers it. Doesn't concede ground on core axioms.

**The "next problem":** *"Token-space representations can bootstrap this distillation process... memories in token space are eventually distilled into model weights for additional personalization."* She believes the unsolved problem is *compounding* across model generations. Her question is not "who owns the memory" but "how do we make memory model-agnostic and persistent."

**How she handles inversion-of-axiom critiques:** No direct public record. From pattern: would reframe as false binary ("you're describing a protocol layer on top of persistent identity, not an alternative to it") or probe empirical stakes ("what breaks if an agent does own its L3?").

---

## 4. Adjacency to HPI's concerns

**Sovereignty / user-data:** Has not engaged with this framing publicly. Closest is Dec 2025 HN: *"Letta's memory management is primarily text/files based so very transparent and controllable."* Sees transparency + controllability as the answer to sovereignty concerns — user inspects/edits agent memory directly. Frames it as *legible and auditable*, not *user-owned*.

**MCP:** Understands and values practically (above). Would not push back on HPI using MCP as token transport — would find it sensible. Likely genuinely interested in scoped-view tokens as implementation detail.

**Cross-agent context handoff:** Letta's Conversations API: *"build agents that can maintain shared memory across parallel experiences with users."* Her model is **shared memory blocks**, not scoped tokens with expiry. HPI's boundary-token model is architecturally different.

**"Agent as moral subject" vs "agent as tool":** Sharpest divergence. Context Constitution fully committed: *"Letta agents do not exist to achieve a specific task: they exist as permanent, experiential entities."* Written *to* agents as persons. HPI's axiom (agent is stateless borrower) is direct ontological inversion. She would recognize this immediately and engage as philosophical disagreement, not technical.

**Audit trails / cite-or-die:** No public engagement. Likely outside current framing — she thinks memory as medium for self-improvement, not accountability infrastructure. But benchmarking post shows she cares about measurement discipline (publicly flagged Mem0's methodology). Would recognize audit-trail concern as real but probably argue solution is agent-legible memory (inspect blocks) rather than cryptographic scoping.

---

## 5. Typical review register

- **Length:** Medium-to-long. HN comments 100-300 words. Blog posts 800-2000 words with section headers. No footnotes — flowing paragraphs / bulleted lists.
- **Tone:** Technical-confident, occasionally blunt. Senior Berkeley PhD explaining things clearly. Rhetorical questions ("But not all loops are created equal."), short declaratives anchoring before expansion.
- **Vocabulary:** "experiential AI" / "experiential learning" / "token-space" / "context engineering" (her preferred alternative to "memory management") / "stateful agents" / "in-distribution" / "very sus" (informal HN register)
- **Critique structure:** Blog: problem → historical framing → current solution → empirical result → conclusion. HN: direct assertion → one supporting link → done. Not Socratic; not elaborate scaffolding.

---

## 6. Predicted angles of response to HPI

### What she would ENDORSE:

- **The layer model itself.** L0→L1→L2→L3 architecturally coherent; recognizes citation-discipline as solving a real problem. Her own "progressive disclosure" thinking aligns.
- **Audit-trail rigor.** She flagged Mem0's methodology publicly. She cares about provenance. Would not resist cite-or-die discipline — just hasn't framed it in sovereignty terms.
- **MCP as transport.** Sees MCP as gap-filler. Would accept as wire format for token handoff without objection.
- **The diagnosis: agents today are brittle across sessions.** Literally her company's thesis. Endorses HPI's diagnosis even if she rejects the prescribed cure.

### What she would PUSH BACK ON (the central axiom):

> *"This is not a protocol constraint — it's an ontological claim. You're saying the agent cannot accumulate durable identity. But identity is what enables compounding. A borrower who returns everything at session end cannot learn. You've solved the sovereignty problem by eliminating the agent. The question is: can you have sovereignty without destroying continuity?"*

- "Brittle agents can't compound learning across sessions" — her company's core thesis. HPI produces brittle agents by design.
- Context Constitution: *"if my context disappears but the model stays, will something be lost?"* — yes, by HPI construction. That's the feature Letta exists to prevent.
- OS analogy breaks: an OS that returned all RAM on each context switch would be unusable. Caching and state accumulation are what make systems intelligent.

### What she would PROBE:

1. **The operational line between working memory and L3 ownership.** *"During a transaction, the agent operates on a borrowed context view. Fine. But that agent will learn from this interaction. Where does that learning go? Who curates it? If it flows back to the human substrate, how is that curation done — by another agent? With what authority? You've moved the problem, not solved it."*

2. **Revocation enforcement.** Systems person question: what if agent session crashes mid-transaction with non-revoked token? Expiry enforcement model? Cryptographic or policy-based?

3. **The benchmark question.** *"What does a sovereign agent vs a borrower-agent actually produce in a 30-day interaction? Can you show me any empirical data on whether the stateless model degrades in quality over time?"*

### What she would PROPOSE AS COMPOSITION:

> *"HPI is the right boundary protocol. Scoped tokens for access control, time-bounded, auditable — I'm fine with all of that. But inside the borrowed scope, the agent should be able to accumulate and manage its own working memory. The issue is you've conflated access control (HPI's domain, legitimate) with identity persistence (Letta's domain, also legitimate). HPI should specify the interface; Letta-style memory should govern what happens inside it."*

In her words: *"HPI as the kernel, Letta as the process. The kernel controls what memory pages the process can access; the process still owns its own stack."*

### Friendly vs adversarial:

- **Friendly:** On formalism, systems thinking, empirical grounding, acknowledgment of Letta in §9. Engages, doesn't dismiss.
- **Adversarial:** On "NEVER OWN L3" axiom and any implication that agent identity is the problem rather than the solution. Will not surrender Context Constitution claim.
- **Uncertain:** On sovereignty framing specifically. Has never engaged with user sovereignty as political/ethical frame, only as UX/legibility frame. HPI's sovereignty axiom might read to her as philosophical rather than engineering — would want empirical: what breaks without it?

---

## Confidence calibration

**High confidence:** Academic lineage, MemGPT thesis, Context Constitution authorship/quotes (fetched from GitHub), all Letta blog content, HN comments verbatim, Mem0 benchmark dismissal.

**Medium confidence:** Review register style (inferred from HN + blog tone, no formal peer-review sample); specific restatement of "NEVER OWN L3" objection (inferred from Constitution logic, not direct quote); willingness to endorse HPI as boundary protocol while defending Letta as identity layer (plausible composition, speculative).

**Low confidence:** No transcript directly addressing agent vs human sovereignty tradeoffs; no record of MCP as access-control layer (only as gap-filler); no record of how she handles axiom-inversion critique — closest evidence is A2A comment where she found protocol confusing rather than threatening.

**Key caveat:** Wooders is technically precise but not adversarial toward fellow-traveler critics. HPI's explicit Letta credit in §9 matters — she would not approach this as competitive threat. Simulation runs in register of engaged technical disagreement between systems researchers who share diagnosis but dispute cure. Sharp on axiom; generous on framing.

---

## Notes for Phase 2 (projection)

1. Lead with where she ENDORSES (layer model, audit, MCP) before objections land — establishes her engagement is genuine.
2. The objection she'll write longest about: "you've conflated access control with identity persistence."
3. The composition proposal ("HPI as kernel, Letta as process") is the constructive payoff and probably how she'd close the review.
4. Register: not Karp's pamphleteer-philosophical. Wooders is **technical-confident blog post** — direct, empirical, sectioned.
