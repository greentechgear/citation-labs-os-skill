> Reviewed working copy v0.3, 10 September 2026. Original operator evidence retains its date. Editorial clarifications are recorded in REFERENCE_CHANGELOG.md; no new live verification. Client names use sector descriptions. The card v0.2 resolves the capability-state qualifications where earlier tables remain historical.

# Thinking Inspector (TI) MCP — Briefing for the Assistant

Purpose of this doc: give a working, accurate mental model of what the TI MCP is, what it can and can't expose, how Garrett/Claude have been using it, and what labels and topographical inputs are worth supplying. Written so it stays valid for whatever TI's next version turns out to be (see the last section).

---

## 1\. What TI actually is

TI is a thin orchestration layer in front of one specific capability: **running a prompt against an OpenAI model with the model's built-in web search tool turned on, and exposing the resulting trace as structured data** rather than just a chat reply.

It is not a search engine, not a citation index, and not a general research agent. It is an instrumented pass-through: you give it prompts and a model; it runs them; it hands back everything the model's tool-use loop did along the way, in a form you can query and diff.

Two execution modes:

- **Submit and run** (`run_compare`) — you give it a batch of prompts, a model, and settings; it runs them all (optionally with repeats) and returns a job you poll.  
- **Re-inspect stored runs** (`compare_runs`, `get_run_result`) — once runs exist (from this session or a past one), you can pull them back and analyze them again without re-running anything.

## 2\. The seven tools, plainly

| Tool | What it does | When to reach for it |
| :---- | :---- | :---- |
| `run_compare` | Submits a batch of prompts \+ model \+ settings as one async job. Each prompt gets `runs` repetitions (default 6; we've used 1 for exploratory work). Returns a `job_id` immediately. | Starting a new comparison — e.g., a fresh role×prompt matrix. |
| `get_compare_status` | Polls a `job_id`: how many of the total runs are done, how many failed. | While waiting for a submitted job. |
| `list_compare_jobs` | Lists recent jobs (their IDs, presumably status/labels). | Finding a job you didn't note the ID for. |
| `get_compare_results` | Pulls the full structured comparison for a completed `job_id` — same `include` options as below. | Once a job status shows completed. |
| `list_runs` | Searches/lists individual stored runs by prompt text or status, independent of any job. | Finding an old run when you only remember roughly what it asked. |
| `get_run_result` | Pulls ONE run: its prompt, full output text, counts, and sources. Can include an optional prose reasoning summary (`include_reasoning`), separate from search events. | Reading a single answer in full, or fetching the verbatim text you couldn't get any other way. |
| `compare_runs` | Deep-compares a list of specific `run_ids` you name yourself, in whatever order you want (this is how role order gets fixed for a table). Same `include` menu as `get_compare_results`. | Comparing runs from different jobs, or a hand-picked subset. |

The `include` menu on `compare_runs` / `get_compare_results` is the important lever:

- `summary` — condensed comparison overview.  
- `outputs` — the actual final-answer texts.  
- `query_fanout` — the search queries issued, broken out per run.  
- `compact` — a context-cheap version for large matrices: top shared pages/folders/domains rather than every row. **Use this by default for anything bigger than a handful of runs** — it's what keeps an 81-condition matrix from blowing the context window.  
- `overlap` — precomputed overlap/similarity between run sets.  
- `read_urls` — the raw row-level data: rows grouped by URL with `cited_any`, `opened_any`, and per-role flags. Resolve labels to original runs before deriving run-by-URL rows. This is what we exported as the source-event CSV. Has `read_urls_limit` / `read_urls_offset` for paging (max 1000 rows per call).

## 3\. What TI actually exposes (the "topography")

This is the trace layer, and it's worth being precise about what's real versus what's an interpretation we impose on top.

**Directly exposed by TI:**

- The exact prompt text and run settings (model, effort, date/time).  
- The search queries the model issued, as an ordered list per run (`query_fanout`).  
- The **surfaced URL set** per run — every URL the model's search tool returned to it, as original strings.  
- **Explicit open / find-in-page actions** — a separate flag per URL indicating whether the model took an additional action (not just saw it in search results, but opened it or searched within it).  
- **Cited URLs** — the subset of the surfaced set that the model actually referenced in its final answer.  
- The **final answer text** itself (via `outputs` or `get_run_result`).  
- A stable **run\_id** tying all of the above together.  
- Token usage.  
- A **reasoning summary**, optionally (`include_reasoning` on `get_run_result`) — a short prose narrative of the model's search/reasoning steps (a few paragraphs, written like "Considering cybersecurity frameworks... I'm looking into NIST SP 800-161 Rev 1..."). This is NOT raw chain-of-thought or a token-level trace — it's a summary, and should be called that. Not pulled by default.

**Not exposed, or only exposed at coarser grain:**

- **Row-level query-to-URL linkage.** You get "these were the queries" and "these were the surfaced URLs" as two lists per run, but not a reliable join saying which query produced which URL. Treat any query→URL causal claim as unsupported.  
- **Retrieval rank** (position in search results).  
- **Snippet text** the model actually saw before deciding to open or cite something.  
- Whether "surfaced" means "fetched" or merely "listed in a search result." We've been treating TI's surfaced set as the working definition of "retrieved," but that's a declared convention on our side, not a TI guarantee.  
- **Verbatim answer export as a downloadable file.** The text lives in TI under the run\_id; there's no confirmed tool-side export to a file, which is why the four Product X answers are still sitting in TI rather than in the Drive folder.

**A heuristic layer that rides along:** TI attaches a `site_type` label to surfaced URLs (e.g., "regulator") in the `read_urls` output. This is TI's own classification heuristic, not a coding of what the source actually is or does — we've been careful to say "TI's site\_type heuristic" rather than treating it as ground truth.

## 4\. Labels, names, and inputs worth supplying

This is the part that matters for your topography question — what vocabulary to hand TI (via the prompt) versus what vocabulary we impose afterward (via our own analysis).

**Things that go INTO the prompt (TI has no separate field for these — they're just text you write into the prompt string):**

- The **common situation record** — the frozen facts everyone sees. Needs a version label (we've been using things like `SYNTHETIC_PRODUCTX_v1.0`) so it's citable later.  
- The **role / responsibility clause** — who the model is asked to be and what they're deciding. This is the manipulated variable across a comparison.  
- The **evidence request** — the constant closing instruction (cite sources, distinguish supplied vs. found vs. inferred). Keep this identical across a role comparison or you've confounded two things at once.  
- A **governing regime**, if relevant — we learned the hard way that leaving "regulated manufacturer" unnamed lets the model pick one for you, and the Product X stress test adopted a common context across its conditions. Record that observation without treating it as a rule for every future run.

**Things that go INTO the tool call itself, not the prompt text:**

- `model` — the OpenAI model ID (we've used `gpt-5.6`).  
- `effort` — none/low/medium/high/xhigh.  
- `profile` — TI's own execution profile (we used the default `latest`; a comparison response can report profileVersion 2026-06-03; preserve requested and returned settings separately and verify their original-execution meaning).  
- `runs` — repetitions per prompt. Default is 6; we've deliberately used 1 for exploratory passes and should say so explicitly whenever we do, since 1 run makes any observed difference provisional.  
- `label` — a free-text job label. This is the one place TI lets you attach a human-readable name to a whole batch (we've used things like `ProductX_4cond_R3_worked_example_2026-09-09`). Worth using every time — it's what makes `list_compare_jobs` useful later.

**Things WE invent afterward, that TI has no concept of:**

- **Role names** (OT\_SEC, IMPL\_ENG, PROCUREMENT, BASELINE) — these are our labels for runs, used purely to keep track of which run\_id is which condition. TI just sees run\_ids.  
- **Record IDs** for the whole investigation (e.g., `PRODX_R3_4C_B1`) — ours, not TI's.  
- **The counting unit and normalization rule** for comparing cited/surfaced sets (exact URL vs. normalized URL vs. domain vs. publisher family) — entirely our analytical choice, applied after pulling `read_urls`.  
- **Evidence states** (OBSERVED/DOCUMENTED, HYPOTHESIS, etc.) — our framework, applied to what TI returns.

## 5\. The pattern we actually use, end to end

1. Freeze a common situation record and give it a version string.  
2. Write N prompts that share that record and evidence request, varying only the role clause (plus a role-agnostic baseline).  
3. `run_compare(model, prompts=[...], effort="medium", runs=1, label="descriptive_label")` → get `job_id`.  
4. Poll `get_compare_status(job_id)` until the job reaches a terminal status. Reconcile completed and failed runs against the expected total; preserve failures and seek approval for another attempt.  
5. `list_runs` or the job's own return value to get the individual `run_id`s, and assign our own role labels to them.  
6. `compare_runs(run_ids=[...], include=["summary","query_fanout","overlap","compact"])` for the topline comparison.  
7. `compare_runs(run_ids=[...], include=["read_urls"], read_urls_limit=...)` separately for the row-level export — this can be large. Use a demonstrated direct capture route where available and record completeness; keep external preservation status unresolved where no such route has been demonstrated.  
8. Compute our own Jaccard/overlap-coefficient tables from the `read_urls` rows, at a declared unit and normalization.  
9. `get_run_result(run_id)` or `outputs` include, if we need the actual answer text.

## 5a. Confirmed schema — dated, sanitized examples (pulled 2026-09-09)

**`get_run_result(run_id, include_reasoning=true)` — single-run pull:**

```
{
  "role": "A",
  "run_id": "<uuid>",
  "query": "<full prompt text>",
  "model": "gpt-5.6",
  "effort": "medium",
  "status": "completed",
  "created_at": "2026-09-09T12:20:29.040Z",
  "usage": {
    "input_tokens": 81524,
    "total_tokens": 88964,
    "output_tokens": 7440,
    "input_tokens_details": { "cached_tokens": 4370, "cache_write_tokens": 341 },
    "output_tokens_details": { "reasoning_tokens": 3339 }
  },
  "error": null,
  "counts": {
    "pages": 78, "domains": 9, "cited": 8, "opened": 3,
    "consulted": 78, "actions": 10, "citations": 24
  },
  "output": "<full markdown answer text>",
  "reasoning": "<short prose summary of the model's search/reasoning steps -- NOT full chain-of-thought>",
  "sources": [
    { "url": "https://...", "title": "...", "domain": "fda.gov", "cited": true, "opened": false },
    { "url": "https://...", "title": "...", "domain": "nist.gov", "cited": false, "opened": false }
  ]
}
```

Note: a single-run pull already returns cited/opened flags per source in `sources` — you don't need `compare_runs` just to see one run's own source list.

**`compare_runs(run_ids=[...], include=["read_urls"])` — cross-run aggregate:**

```
{
  "meta": {
    "run_ids": ["<uuid>", "<uuid>"],
    "runCount": 2,
    "profileVersion": "2026-06-03",
    "generatedAt": "2026-09-09T15:15:49.431Z"
  },
  "read_urls": [
    {
      "url": "https://csrc.nist.gov/pubs/sp/1800/45/final",
      "runs_read": 1,
      "total_reads": 1,
      "subdomain": "csrc.nist.gov",
      "subdomain_freq": 18,
      "folder": "csrc.nist.gov/pubs/sp",
      "folder_freq": 6,
      "registrable_domain": "nist.gov",
      "domain_freq": 51,
      "site_type": "regulator",
      "weight": 1,
      "high_volume_flag": false,
      "flag_source": null,
      "cited_any": true,
      "opened_any": false,
      "per_role": [ { "role": "A", "cited": true, "opened": false } ]
    }
  ],
  "read_urls_page": { "offset": 0, "limit": 3, "returned": 3, "total": 132 }
}
```

`meta.profileVersion` describes the returned comparison. Preserve it and generatedAt separately from original execution settings; their relationship remains unverified.

## 5b. What remains genuinely unconfirmed, and why

**Complete preservation / export.** This is narrower than it first looked. The full TI tool surface is exactly the seven tools in section 2 above \-- confirmed by listing them directly. None writes a file; every one returns data into the calling context. So "no export tool exists on this MCP surface" is a confirmed negative, not a gap. What's still open is whether TI's operators have an out-of-band export (a dashboard, a direct API, a database they can query) outside this MCP surface \-- that can't be settled by calling tools from here. It needs someone with TI account/admin access to confirm or deny.

**Access and connection.** Genuinely out of scope for a tool-schema investigation. Who provisions a new user, which assistant environments TI is wired into, authentication method, cost, and data-handling terms are account and product facts, not things any tool call here can answer. This needs the person who administers the TI connector.

## 6\. Why this needs to stay tool-agnostic

Garrett's standing instruction: don't write guidance so tied to TI's exact tool names that it breaks the moment a successor tool (one that can run multiple models, not just OpenAI) shows up. The R4 method document handles this by defining "the instrument" as a capability checklist — prompt, queries, surfaced set, explicit opens, cited set, exportable verbatim answer, run ID, and whether query→URL linkage exists — rather than by name. The dated record supplies prompt, query, source, citation, answer and run-ID observations. Reliable query-to-URL linkage is absent and external preservation needs a demonstrated route. Any new tool gets checked against that same list before we trust it the same way.  
