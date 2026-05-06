## Latest WhatsApp with Yitzchak (vita `l1_events`, channel `wa-972552631180`)

**Today (May 6) — the active thread:**

- 05:29 Yitzchak: _"if I want to access all the L3 data — final processed output grouped by source (WhatsApp, email, Xero, etc.) — where would I find it in Supabase?"_
- 08:01 Yitzchak: _"do you have a plan for the L3 structure? I'm trying to make the GENUI… I need date sources ie whatsapp, zero etc and then the content itself"_
- 08:48 Yitzchak: _"could we meet for a few minutes?"_
- 08:55 Mordechai: _"cant meet now rather send msg"_
- 08:57 Yitzchak: **"I'm building the dashboard UI… should I focus only on UI and come back to you to connect the data (like calling your MCP), or is there a better approach?"**

May 3 thread was the Zoom + wireframe handoff (`claude.ai/design/p/019dea9b…`). Before that, the chat is Xero OAuth coordination from late March / mid-April.

---

## How you can technically branch Supabase

The vita project (`dkccadwohifcqcdzhhnu`) currently has one branch: `main`, status **`MIGRATIONS_FAILED`** — flag this before doing anything else.

Four real options, ranked by isolation:

||What it is|Cost|Data carried?|Good for|
|---|---|---|---|---|
|**1. Supabase Preview Branch**|`mcp__supabase__create_branch` or push a git branch with `supabase/config.toml` wired to GitHub. Spins up a fresh project_ref, runs all migrations from `supabase/migrations/`, gives Yitzchak his own URL + keys.|~$0.32/day per branch (Pro plan req'd)|❌ schema only — empty tables (`with_data: true` is beta)|Schema experiments, PR previews|
|**2. Separate Supabase project**|New free-tier project, run the same migrations, seed manually|Free|❌|Yitzchak full sandbox, fully isolated|
|**3. Local Supabase**|`supabase start` (Docker: Postgres + GoTrue + Storage + Studio) in vita repo|Free|seed via `supabase/seed.sql`|UI dev with hot reload, offline|
|**4. Shared project + RLS / role**|Give him a read-only PostgREST role + limited anon key on prod|Free|✅ live data|Dashboard reading real L1/L2/L3|

Mechanically for **(1)**:

```bash
# either via MCP
mcp__supabase__create_branch(project_id="dkccadwohifcqcdzhhnu", name="yitzchak-ui")
# or via GitHub integration: enable Branching in Supabase dashboard → push branch
```

Branch inherits migrations from `infra/supabase/migrations/` (you have a `.draft/` dir uncommitted — those won't ship until promoted). Production data does _not_ copy.

---

## Is branching the right approach here?

**Probably not for what Yitzchak is actually asking.** His question is _"where's the data and what's the contract"_, not _"give me a sandbox to mutate"_. Branching would hand him an empty DB and a $10/mo bill without answering either question.

What he actually needs, in order:

1. **A stable read contract** — the `l1_events` schema you already have is the contract. L2/L3 are empty (`l2_syntheses=0`, `l3_surfaces=0`), so there's no "L3 grouped by source" to point him at _yet_. Tell him that honestly: L3 doesn't exist as a table; it's a planned synthesis layer. For now `l1_events.channel_id → channels.kind` _is_ the "grouped by source" cut.
2. **A read-only key + a 5-line query example** — anon key + an RLS policy that gates by his tenant, so his UI calls supabase-js directly. No MCP needed for read. He's already on `gowa_device_id 972524814613` so he has device context.
3. **A local supabase for his UI loop** — `supabase start` + a `seed.sql` snapshot of ~100 l1_events rows. That gives him dev velocity without burning a branch.
4. **Branch only when he writes migrations** — i.e. when he needs to add `l3_surfaces` columns or RPC functions for the dashboard. Then a preview branch is the right tool.

**Suggested reply to him:** "L3 doesn't exist as a table yet — `l1_events` grouped by `channel_id` (joined to `channels.kind`) is the source-of-truth cut today. I'll send you a read-only anon key + a `supabase start` seed so you can build the UI offline. We'll spin a preview branch only when you need schema changes."

Also: fix `MIGRATIONS_FAILED` on main first — Yitzchak forking off a broken branch will compound the problem.