# Reviewer dossier — Andrej Karpathy

**Role:** Co-founder Eureka Labs. Former Director Tesla AI. OpenAI founding member. Stanford PhD (Fei-Fei Li). Author of "Software 2.0," nanogpt/microgpt, "Intro to LLMs."
**Compiled:** 2026-05-06 from karpathy.bearblog.dev, karpathy.github.io, YouTube transcripts, Sequoia Ascent 2026 talk, Dwarkesh 2025 podcast.
**Why simulate:** LLM-systems researcher with deep mechanistic knowledge. Will scrutinize HPI's claims against transformer mechanics — what does "agent borrows scoped view" mean at the token level, where the context window IS the working memory?

---

## 1. Public writings (last 3 years, recent-weighted)

**karpathy.bearblog.dev** (active venue, Mar 2025–Apr 2026):

- **"Sequoia Ascent 2026"** (Apr 30 2026 — most recent): *"In Software 3.0, the context window becomes the main lever. The LLM is an interpreter over that context."* On agent-native infrastructure: *"Products need agent-native surfaces: Markdown docs, CLIs, APIs, MCP servers, structured logs, machine-readable schemas, copy-pasteable agent instructions, safe permissioning, auditable actions."* Explicitly names MCP. On agentic engineering: *"the agentic engineer designs specs, supervises plans, inspects diffs, writes tests, creates evaluation loops, manages permissions, isolates worktrees."* On what's scarce: *"understanding, taste, eval design, security, system boundaries, agent orchestration, domain-specific feedback loops, and knowing when the model is off the rails."*

- **"2025 LLM Year in Review"** (Dec 19 2025): On Claude Code: *"the first convincing demonstration of what an LLM Agent looks like... CC is notable to me in that it runs on your computer and with your private environment, data and context. I think OpenAI got this wrong because they focused their early codex/agent efforts on cloud deployments... the primary distinction that matters is not about where the 'AI ops' happen to run, but about everything else — the already-existing and booted up computer, its installation, context, data, secrets, configuration."* *"It's a little spirit/ghost that 'lives' on your computer."*

- **"Verifiability"** (Nov 17 2025): *"Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify."* If there's no verifiable loop, the claim is suspicious.

- **"The space of minds"** (Nov 29 2025): *"an LLM with a knowledge cutoff that boots up from fixed weights, processes tokens and then dies."*

- **"Animals vs Ghosts"** (Oct 1 2025): Critique of Sutton's animal-intelligence framing; LLMs are ghosts (token-processors), not animals (continual-learners).

- **"Vibe coding MenuGen"** (Apr 27 2025): Documented agent introduced security bug — matched Stripe purchases to Google accounts via email; Stripe email and Google login email differ. *"A human needs enough product and engineering judgment to insist on persistent user IDs."*

- **"Power to the people: How LLMs flip the script on technology diffusion"** (Apr 7 2025): *"LLMs display a dramatic reversal of [top-down diffusion]... they generate disproportionate benefit for regular people."* Key constraint: *"It's not so easy to put all of it into a context window. You can't just vibe code something."*

**karpathy.github.io:**

- **"microgpt"** (Feb 12 2026): 200-line dependency-free Python file that trains and inferences a GPT. *"This file contains the full algorithmic content of what is needed... I cannot simplify this any further."*

- **"A Recipe for Training Neural Networks"** (Apr 25 2019, still cited): *"Neural net training fails silently. Everything could be correct syntactically, but the whole thing isn't arranged properly, and it's really hard to tell."*

**YouTube:** "Intro to Large Language Models" (Nov 2023) gave LLM-as-OS framing canonical form. "Deep Dive into LLMs like ChatGPT" — full training stack pedagogy. "Zero to Hero" playlist — implementation pedagogy.

**Dwarkesh podcast (2025) — most relevant transcript:**

> *"Anything that happens in the context window of the neural network—you're plugging in all the tokens and building up all those KV cache representations—is very directly accessible to the neural net. So I compare the KV cache and the stuff that happens at test time to more like a working memory... anything that's in the weights, it's a hazy recollection of what you read a year ago. Anything that you give it as a context at test time is directly in the working memory."*

> *"We don't have an equivalent of [sleep-time distillation] in large language models... maybe having a specific neural net per person. Maybe it's a LoRA. It's not a full-weight neural network. It's just some small sparse subset of the weights that are changed. But we do want to create ways of creating these individuals that have very long context."*

> *"These models don't really have a distillation phase of taking what happened, analyzing it obsessively, thinking through it, doing some synthetic data generation process and distilling it back into the weights."*

---

## 2. Stated values + intellectual lineage

**Stanford PhD lineage (Fei-Fei Li, 2011–2015):** CS231n co-designer; if you can't implement it from scratch, you don't understand it. Pedagogy shapes everything.

**OpenAI founding (2015–2017, 2023–2024):** First-principles evaluation. No product stake.

**Tesla Autopilot Director (2017–2022):** Autonomy is a spectrum, not binary. Each increment of trust requires engineering rigor, not capability claims. Has seen what happens when autonomy claims outrun enforcement mechanisms.

**Position on agent autonomy:** Explicit: *"decade of agents, not year of agents."* Iron Man framing (augmentation) over "agents taking over." Skeptical of full-autonomy claims.

**Bare-metal mechanics:** Cares what is actually happening in the model. Context window IS the working memory. Weights ARE the hazy long-term memory. Anything contradicting operating reality is suspect.

**Build-from-scratch pedagogy:** micrograd → nanogpt → microgpt. When evaluating a spec: what is the 200-line version? If you can't state the irreducible core, the spec hasn't found it yet.

**Cites approvingly:** Sutton (selectively — Bitter Lesson yes, animal-intelligence framing no), LeCun, Hinton, DeepSeek (sparse attention), Anthropic (Claude Code architecture).

**No agent-product stake.** Adjacent observer; evaluates as sophisticated user, not vendor.

---

## 3. Patterns of argumentation

**Response to architectural proposals:** Interrogates enforcement mechanism before aspiration. *"The 'possible error surface' is large, logical (as opposed to syntactic), and very tricky to unit test."* Will ask: what fails silently here?

**Operational mechanics vs system design:** Both, but starts with mechanics. Validates system designs against mechanical reality.

**Elegant in spec but messy in practice:** Has a name for it now — the MenuGen payment bug. Plausible code, bad system design.

**Twitter/X critique style:** Numbered lists, short dense observations with specific callouts, occasional longer threads. Occasionally playful (microgpt as "art project"). Not adversarial toward authors — critiques the system, not the person. Sharpest when seeing anthropomorphic confusion (treating LLM memory like human memory).

**Engagement with protocols/standards:** Now explicitly pro-MCP (Sequoia 2026). Doesn't build protocols but evaluates them through: does this match how the underlying system works?

**Provenance/cite-or-die:** Closest analog is verifiability: *"if a task/job is verifiable, then it is optimizable directly or via reinforcement learning."* Hasn't articulated formal attribution discipline; "future LLMs are watching" gestures at provenance.

---

## 4. Adjacency to HPI's concerns

**Sovereignty / personal AI:** Engaged through capability lens (how do we give LLMs per-person memory?), not sovereignty lens (who controls). Per-person LoRA framing in Dwarkesh — concept articulated, protocol not. Sympathetic to individual empowerment via AI ("Power to the people").

**Personal AI predictions:** *"maybe having a specific neural net per person. Maybe it's a LoRA."* — fine-tuning concern, not access-control concern.

**Agent memory architectures:** Mechanistic frame: weights = hazy long-term, context window = working memory, missing = distillation phase (sleep equivalent). Target architecture: *"some very elaborate, sparse attention scheme"* + per-person LoRA. NOT articulated a token/JWT-based access protocol.

**Context window and agent state:** Canonical: context window IS the working cognitive surface. *"the context window becomes the main lever. The LLM is an interpreter over that context."* This is HPI's most contested ground.

**MCP specifically:** Explicitly positive. Lists MCP servers as required agent-native surface. Has not criticized MCP.

**Audit / cite-or-die:** Verifiability is closest analog. Cares about eval loops, test signals. Not formal cite-or-die.

---

## 5. Typical review register

- **Length:** Bearblog 400–1500 words. Twitter 1–3 sentences. Talks 30–40 min. Does NOT write long architectural reviews — sharp dense numbered observations.
- **Tone:** Technical-precise, occasional dry humor, self-deprecating ("art project"). Pedagogically warm, analytically cold. Not sycophantic — will call something "roughly concrete and interesting to think through" then dismantle it.
- **Vocabulary:** "jagged" (capability), "ghosts not animals," "context window as working memory," "hazy recollection," "verifiable/resettable/rewardable," "autonomy slider," "people spirits," "agentic engineering," "Software 1.0/2.0/3.0," "partially autonomous," "sensors and actuators."
- **Code examples:** Heavy. Will sketch pseudocode or 10-line demo to test claim. microgpt is the extreme.
- **Critique structure:** Numbered points, each compressed. Separates "what is claimed" from "what is enforced." Credits before pushing back.
- **Negative findings:** Not attacks. *"This is the part I would probe."* Calibrated skepticism.

---

## 6. Predicted angles of response to HPI

### Endorse:

1. **MCP extension** — explicit Sequoia 2026 endorsement of MCP servers as agent-native surface. HPI builds on right primitive.
2. **Typed axiom grammar.** Verifiability framework maps. Typed claims more verifiable than untyped.
3. **Individual-over-institution framing.** "Power to the people" thesis aligned.
4. **Layered substrate as architecture.** He's building analogous "LLM Wiki" pattern (Sequoia 2026): *"raw sources into a persistent Markdown wiki: summaries, entity pages, concept pages, contradictions, cross-links, logs, and evolving synthesis."*
5. **Auditable actions + safe permissioning.** On his agent-native list.

### Probe (this is the central mechanistic challenge):

**What does "agent borrows scoped view" mean at the token level?**

His Dwarkesh frame: *"anything that's in the weights is hazy recollection. Anything in the context window is directly in the working memory."*

Karpathy's question: When agent gets time-bounded single-use token to borrow scoped view of L3, what actually happens at the LLM level? The agent doesn't "borrow" a view — it receives tokens in its context window. Context window IS the working cognitive surface. **No mechanism in transformer inference enforces "this token expires" or "this fact cannot be retained after the call."**

Token may expire at protocol layer, but model has already ingested those tokens into KV cache for that forward pass. Any downstream action, tool call, or generation is downstream of that inference. **HPI tokens scope ACCESS to information; cannot scope what model DOES with information once in-context.**

Not fatal — boundary condition. But he will state it precisely.

### Probe (new ground — the distillation gap):

**HPI's L3 is described as a "working cognitive surface." For whom — the human, or the LLM?**

Sub-claim: HPI's L3 layer face his sleep/distillation critique. *"We don't have an equivalent of that in LLMs... taking what happened, analyzing it obsessively, doing synthetic data generation, distilling back into weights."*

Question: HPI proposes scoped-view tokens. But the right architecture might be **per-person LoRA / sovereign fine-tuning rights**, not scoped-view access. If the goal is durable personalization, the L3 needs to be distilled into a sovereign model fragment — and HPI doesn't address that.

**This is genuinely new ground vs Karp/Wooders.**

### Push back on:

1. **Anthropomorphic memory framing.** If spec implies agents "maintain state" / "accumulate context" in human-memory sense, he'll rephrase mechanistically: agents have tokens in context window, nothing more.

2. **JWT-scoped-view as complete solution.** *"Token correctly scopes access at protocol layer. Does not scope inference. Different problems; spec addresses only the first."*

3. **L3 persistence as "sovereign surface."** Agent boots, processes tokens, dies. L3 persistence is storage problem, not protocol property. Sovereignty comes from who controls what enters storage, not from inference call.

### Propose:

1. **Verifiable loop spec.** What's the automatic success signal for correct HPI token usage? What does eval loop look like? How test cite-or-die actually happens?

2. **Simpler enforcement.** *"Instead of 4-D scope in JWT, what if scope is enforced at retrieval — only scoped documents enter context window? Then problem reduces to access control over retrieval, which is solved."*

3. **The 200-line version.** Wants to see irreducible minimum. If can't state in 200 lines of Python, over-engineered.

---

## Convergence vs Divergence Verdict

**CONVERGENT with Karp+Wooders on central critique. Arrived via mechanistically distinct route. Adds one genuinely new divergent vector.**

The Karp/Wooders finding: HPI claims more than its wire format enforces; spec's value is as a boundary protocol that other architectures ride on.

Karpathy arrives at same conclusion via different route:
- **Karp:** economic / systems design — what does protocol guarantee at boundary?
- **Wooders:** systems architecture — access control conflated with identity persistence
- **Karpathy:** mechanistic — context window IS working cognitive surface; protocol-layer token scoping cannot constrain what happens inside transformer inference once tokens are in-context

Three independent priors, three different routes, **same finding.** This is high-signal: the spec genuinely has this issue.

**New vector Karpathy adds:** The distillation gap. Per-person LoRA / sovereign fine-tuning rights might be the correct architecture, not scoped-view tokens. This is a *different design question* than HPI proposes — and it opens whether the right solution is the protocol HPI specifies at all.

---

## Confidence calibration

| Claim | Confidence | Source |
|---|---|---|
| Context-window-as-working-memory frame | Very high | Dwarkesh 2025, Intro to LLMs Nov 2023 |
| MCP endorsement | High | Sequoia 2026 (Apr 30 2026) |
| Autonomy-slider partial-autonomy position | Very high | YC 2025, year-in-review 2025 |
| Verifiability framework as primary filter | Very high | Nov 2025, Sequoia 2026 |
| Build-from-scratch critique posture | Very high | microgpt, nanogpt, recipe |
| Personal LoRA / per-person model interest | High | Dwarkesh 2025 |
| Specific response to HPI's claim-enforcement gap | Medium-high | Inferred from verifiability + silent failure doctrine |
| Positive read of individual sovereignty | Medium | "Power to the people" |
| Would propose simpler enforcement | Medium | Pattern inference |
| Has engaged with cite-or-die discipline | Low | No direct evidence; adjacent gestures |

**Overall:** Predicted critique converges with Karp+Wooders on central finding (claim-enforcement gap), arrives via mechanistically distinct route, adds one new vector (distillation gap). Third simulation does not falsify convergence — strengthens it via independent reasoning to same conclusion. Opens new design question: is the right solution scoped-view tokens at all, or sovereign fine-tuning rights?

---

## Notes for Phase 2 (projection)

1. Lead with what he'd endorse (MCP, Power to the people, verifiability framework) — establishes engagement.
2. The mechanistic critique (context-window-as-working-memory) is the central one. State precisely.
3. The distillation gap is the new ground. Make this explicit so the simulation surfaces what Karp+Wooders missed.
4. Register: numbered points, ~600-1000 words, technical precision, occasional dry humor. NOT pamphleteer (Karp) or blog-post (Wooders). Twitter-thread compressed.
5. Closing posture: not rejection, calibrated skepticism. *"This is the part I would probe."*
