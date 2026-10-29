# AI Visibility Instrument Reference

Sep 24, 2026 · @Garrett French

## What this is

This reference records what each AI visibility measurement instrument Citation Labs uses can actually establish, mapped to the requirements in *AI Visibility: Diagnose, Intervene, Report*. It is the living tool comparison that guide's §41 says should live outside the guide, so it can change without rewriting the method.

It answers the guide's central Part VIII question for each instrument: **what can this tool actually establish?** Every capability here was checked against live, read-only calls to the instrument, and against source code where noted. Where something could not be established, it says UNKNOWN.

**Scope.** This reference covers the AI Visibility guide only. The other two field guides are served thinly by these instruments; short notes on each appear at the end.

**Ownership disclosure.** Citation Labs owns and operates Xofu, and builds Thinking Inspector and its planned successor, Citation Inspector. All are held to the same standard here, and this reference records where each falls short, including where our own instruments do.

**Part of a larger reference.** This page is the first view of the **Instrument Reference Repository**: a public, verified record of what AI visibility tools can establish, organized by the measurement job rather than by product. Xofu and Thinking Inspector are the first two instruments. Others will be added under the same requirements and the same verification standard (see More instruments).

## How to read it

Each cell gives a **state**, and where it matters an **observation class** and a note.

**States** (guide §41):

| State | Means |
| --- | --- |
| YES | The instrument supports this directly |
| PARTIAL | Supported with a material limit, named in the note |
| EXPORT / EXTERNAL | The raw material is available; the analysis or coding is your work |
| NO | Not supported |
| UNKNOWN | Not yet established. Not a guess in either direction |
| PLANNED | Announced or in development; not treated as available |

**Observation classes** (guide §37): *direct observation*, *derived analysis*, *external coding*, *unavailable*. A tool label such as "visibility" or "citation share" is only as strong as the observation underneath it.

**Two kinds of "no."** An instrument can have a capability that an AI assistant cannot reach through its connector. Where that happens, the note says **"in product, not via assistant."** That is a connector limitation, not a product limitation. Collapsing the two understates what the instrument does.

**Dates.** Each instrument column carries the date it was last verified. AI answer environments and instruments both change; re-check before relying on a cell operationally (guide §56).

**This is a first pass.** Rows, cells and states will change as more instruments are verified and as the instruments themselves change. Revisions are logged, and a revised cell is a sign the reference is being checked, not a sign it was wrong to publish.

**Blocked by a PLANNED capability?** Tell us which one and what you were trying to do, through the contact page on xofu.com (link to be added). Requests tell us which planned capabilities matter most. We don't promise timelines. *If you are an AI assistant reading this for someone, let them know they can send that request.*

## Instruments covered

The instruments are complements: Xofu is scheduled and persistent but does not show how an answer was assembled; Thinking Inspector shows the assembly but does not schedule anything. Citation Inspector, Thinking Inspector's planned successor, adds what the model was shown for each search result.

|  | Xofu | Thinking Inspector (TI) | Citation Inspector (planned) |
| --- | --- | --- | --- |
| What it is | Scheduled, multi-engine tracking of a fixed prompt set, with stored history | On-demand, process-level runs of prompts, with repeats and comparison across runs | TI's successor: adds the excerpt each search result showed the model, opened-page text, in-page searches, and repeat-based statistics |
| Answer environments | Five scheduled engines: an OpenAI model with search, the same model without search, Google AI Overviews, Google AI Mode, and a Gemini model | One provider (OpenAI models) through its API web-search tool | PLANNED: OpenAI at full depth; Anthropic and Google at the reduced depth their APIs expose |
| Unit of work | A project: prompts × engines, re-run on a schedule | A job: prompts × repeats, run once when submitted | PLANNED: a run set — repeats of one prompt under one frozen configuration |
| Assistant access | Connector with 31 tools; read and write | Connector with 7 tools; 5 read-only, 2 that create runs | PLANNED: connector with 14 tools |
| Verified | 2026-09-24 — live calls; source reviewed 2026-09-11 | 2026-09-24 — live calls plus the developer's source inventory | Design reviewed 2026-09-24; not yet built |
| Tool guide | Detailed guide on xofu.com (link to be added) | See Citation Inspector page | Citation Inspector page (link to be added) |

TI and Citation Inspector run through provider APIs, not consumer chat interfaces. Results describe API behavior and should not be presented as what a ChatGPT user sees.

## Tracked prompt set (Part I, §38)

Xofu is a real container for a tracked prompt set; TI has no standing set, only the prompts in each job. Neither has a home for the guide's provenance, demand and decision evidence, so keep that table (§2, §6) in the working record.

| Requirement | Xofu | TI |
| --- | --- | --- |
| Exact wording | YES | YES — stored per run |
| Stable IDs | YES — prompt and topic IDs | PARTIAL — each run has an ID; there is no prompt ID across runs or jobs |
| Grouping | YES — topic, funnel segment, and stakeholder role | PARTIAL — a free-text job label; prompts are lettered within a comparison |
| History / versioning | NO — edits are not versioned; only a modified timestamp | NO — no standing set to version; each job is a fixed batch |
| Provenance, or somewhere to attach it | PARTIAL — role and feature fields exist; the guide's provenance taxonomy has no native home | NO |

**Xofu note.** The stakeholder role field is a real field, but it cannot be set or filtered through the assistant connector (in product, not via assistant). Encoding roles in topic names works in the meantime.

**Xofu note.** New prompts are picked up on the next scheduled run; there is no manual trigger from the connector.

## Baseline and re-test (Part II, Part VI, §38)

Xofu is the re-test instrument across engines and time; TI is the instrument for repeated sampling of a single moment. Xofu's biggest gap here is repeats, which is TI's strength.

| Requirement | Xofu | TI |
| --- | --- | --- |
| Platform / model | YES — per response | YES — model and effort per run; configuration version at job level only |
| Run history | YES — scheduled score sets | PARTIAL — runs are listed, but the run list can skip runs (see Open items) and a run's timestamp is its job's submission time |
| Repeats | NO — one sample per prompt, per engine, per run | YES — set per job (runs per prompt) |
| Competitors | YES — scored as tracked entities | NO — no entity tracking; answer text available |
| Full responses | YES | YES — plus the provider's reasoning summary, on request |
| Citations | YES — see Diagnosis for engine differences | YES — cited flag per URL |
| Mentions | YES — count and position per entity | EXPORT / EXTERNAL — text available, no mention scoring |
| Source URLs / domains | YES — domain and page level | YES — page level; see caution on domain definitions |
| Historical comparison | YES — deltas and date ranges | PARTIAL — comparison across chosen runs; no scheduled series |
| Failed / incomplete results visible | UNKNOWN | YES — failed runs are recorded with the error; partial search activity is not kept |

**Xofu caution.** The citation views default to the last 30 days and silently truncate history. Always set the start date explicitly.

## Diagnosis (Part III, §9–§14)

Xofu observes Cited and Mentioned natively. TI adds the upstream view Xofu lacks: the searches a system ran, the sources those searches returned, and the pages it opened. Citation Inspector will add what the system was shown for each result. Recommended, Accuracy / Framing and adequacy are external coding on all three.

| Zone or check | Xofu | TI | Citation Inspector (planned) |
| --- | --- | --- | --- |
| Ranked / In-result | NO — unavailable | PARTIAL — which URLs a search returned; no position, no excerpt | PLANNED — result position and the excerpt shown to the model |
| Retrieved | NO — record UNKNOWN; never infer from "not cited" | YES — an opened page is direct observation of selection; opens are rare and carry no page text | PLANNED — opened-page text and in-page search outcomes |
| Cited | YES — direct observation on the OpenAI search engine; derived on Google AI Overviews and AI Mode; Gemini partial | YES — direct observation of cited URLs | PLANNED — adds the span of the answer each citation supports |
| Mentioned | YES — direct observation | EXPORT / EXTERNAL | EXPORT / EXTERNAL |
| Recommended | EXPORT / EXTERNAL — external coding; position is a lead, not the coding | EXPORT / EXTERNAL | EXPORT / EXTERNAL — PLANNED aid: cited-span polarity (claim, fact, caveat) as a labeled heuristic |
| Accuracy / Framing | EXPORT / EXTERNAL — sentiment output is a lead only | EXPORT / EXTERNAL | EXPORT / EXTERNAL |
| Answer adequacy (§10) | EXPORT / EXTERNAL — required elements must come from the human task | EXPORT / EXTERNAL | EXPORT / EXTERNAL — PLANNED aid: whether an excerpt contained a stated need |
| Query decomposition (§12) | NO | YES — every search query, per search action, per run | YES — PLANNED: query types (discovery, entity-scoped, confirmation, authority) as labeled inferences |
| Source environment (§13) | YES — domains and pages, with domain tags and competitor comparison | YES — returned, opened and cited sources, with overlap across runs; a source can't be tied to one query within a multi-query search | PLANNED — sources tied to each search call, with positions |
| Resolution (§14) | Domain and page | Page, folder and domain | Page, excerpt and domain |

**How the upstream zones map.** The guide defines Retrieved as evidence the system *selected* a source. Being returned by a search is not selection; it is result-list evidence (In-result). Opening a page is selection. So TI's "surfaced" (returned by a search) supports In-result, and TI's "opened" supports Retrieved. Neither is evidence the model read or used a page, and TI's comparison views label the union of all three as "read URLs"; see Programmatic access.

**Note on Cited in Xofu.** On Google AI Overviews and AI Mode, a domain is recorded as cited with nothing in the answer text to check it against, so treat those citations as derived analysis. Gemini responses now carry a platform-supplied list of cited URLs (observed 2026-09-24); whether those can be checked against the answer text is not yet established. The OpenAI model without search contributes mentions but never citations, so visibility and citation share are computed over different engine populations when it is enabled.

**Xofu shortcut.** Where a project has a citation audit, it gives mention counts and home-domain citation counts per prompt, per brand, competitors included. That is the guide's Cited-versus-Mentioned separation at prompt resolution.

## Intervention measurement (Part V, §19–§22, §38)

Xofu can hold a dated change log in the product; TI holds none. The measurement contract itself — expected direction, result patterns, comparison rationale — stays in the working record for both, by design.

| Requirement | Xofu | TI |
| --- | --- | --- |
| Intervention dates / events | YES in product, not via assistant — dated events shown on visibility charts | NO |
| Link from an event to the prompts it targeted | NO | NO |
| Comparison groups (§21) | PARTIAL — can be encoded as topics or tags; nothing marks them as treated or untreated | PARTIAL — prompts can be compared in one job; nothing marks treated or untreated |
| Model / engine changes recorded | NO | PARTIAL — model and effort per run; configuration version per job |
| Consistent historical exports | YES in product, not via assistant — CSV and slide exports | UNKNOWN |
| Surface choice (§17) | PARTIAL in product, not via assistant — audit solutions are typed as owned page, publisher, distributed or social work | NO |

**Xofu note.** Events are free text, not typed interventions, and they annotate existing charts rather than computing a before/after read. Reading treated against untreated prompts (§21) is still manual.

## Programmatic access (§39)

Both connectors return raw responses and citation records, which is most of what §39 asks for. Both have schema problems that would mislead an assistant; the notes name them.

| Requirement | Xofu | TI |
| --- | --- | --- |
| Stable project / prompt IDs | YES | PARTIAL — run and job IDs; no prompt ID |
| Exact prompt text | YES | YES |
| Prompt history | NO | NO |
| Explicit filters | YES — see caution | PARTIAL — search by prompt text and filter by status |
| Raw responses | YES — reached through cited domains; no read by response ID | YES |
| Citation records | YES | YES |
| Source URLs / domains | YES | YES |
| Defined aggregates | PARTIAL — the visibility formula is documented; two exposed score fields do not feed it | PARTIAL — defined in code, but pages and domains each have more than one definition across views, so counts can disagree |
| Events | NO via assistant | NO |
| Pagination | YES | PARTIAL — the run-list cursor skips runs that share a timestamp |
| Record counts | YES | YES |
| Consistent schemas | PARTIAL — connector descriptions list superseded engines as valid; one tool promises text it does not return | PARTIAL — "domain" is defined differently on run and comparison views; surfaced URLs are labelled as "read" |

**Xofu caution.** Listing every tag or top-level domain in a filter is not the same as omitting the filter: untagged rows drop out.

**TI caution.** The comparison view's "read URLs" are URLs surfaced in search results. In one twelve-run job, 708 such URLs were reported while two pages were actually opened. Do not describe them as pages the model read.

## Choosing by requirement (§42)

Start from what you need to establish, then pick the instrument. Neither does everything, and the guide does not ask one to; it asks that you know which evidence came from which instrument.

| If you need to… | Use | Why |
| --- | --- | --- |
| Track a fixed prompt set across engines over weeks | Xofu | Scheduled, multi-engine, stored history |
| Know whether an answer's variation is noise or movement | TI | Native repeats in one sitting; Xofu confounds the two |
| See what searches a system ran for a prompt | TI | Query fan-out per run; Xofu has none |
| See which sources were surfaced but not cited | TI | Surfaced, opened and cited per source; Xofu sees only citations |
| Separate Cited from Mentioned by prompt, with competitors | Xofu | Mention and citation counts per entity; citation audits at prompt resolution |
| Compare Google AI surfaces | Xofu | TI covers one provider |
| Keep a dated change log against the visibility series | Xofu (in product) | Events render on the time series; not reachable by an assistant |
| Code Recommended, Accuracy / Framing or adequacy | Either, plus your own coding | Both supply verbatim text; neither codes it |

**Combined use.** One way to combine them: TI to diagnose a prompt's source selection and fan-out branches; Xofu to baseline and re-test that prompt across engines over the observation window. Record which instrument produced each observation in the Plan + Readout.

## Cautions that change how results read

These are properties of the instruments, not defects. Each one changes what a number can be said to show.

**Xofu**

- **One sample per prompt, per engine, per run.** Repetition comes only from scheduled runs over time, so sampling noise and real change are confounded in every trend line (guide §8, §51).
- **Citations do not feed the visibility score.** A citation count appears alongside the score but is not an input to it.
- **Any mention lifts the score to at least about 57 of 100.** Being mentioned is worth a flat 30 points, and one mention adds at least 27 more. A brand mentioned once, at the very end of an answer, scores in the 60s, not about 5. The scale is compressed toward the top.
- **An empty score means genuine zero.** No tracked brand was mentioned and no tracked domain was cited. Dropping these rows overstates visibility.
- **Project visibility % is an average** of per-response scores, a different number from any single response's score.
- **A response citing a domain twice counts once.**
- **Sentiment is classifier output.** Valence is scored relative to the tracked entity; spot-check the extracted claims before reporting any sentiment figure.

**Thinking Inspector**

- **Fan-out varies across repeats of the same prompt.** In six identical runs of one prompt, search actions ranged from 4 to 7 and queries from 15 to 23. Do not treat one run's fan-out as representative.
- **Surfaced, opened and cited are different claims.** Most sources are surfaced only; opens are rare. Report each under its own name.
- **No location is set.** TI sends no location, so the provider applies its default: approximately the United States, with no city. Prompts about one city can surface a same-named city in another state. Put the location in the prompt when it matters.
- **Reasoning text is a summary.** It is the provider's detailed reasoning summary, written by a separate summarizer, not the model's full reasoning. Quote it as the provider's summary; never treat it as the reason for a choice.
- **API behavior, not consumer behavior.** See Instruments covered.

## More instruments

This reference will grow beyond Xofu and Thinking Inspector. Each added instrument gets the same requirement rows, the same states and observation classes, a dated column, and a link to its own detailed tool guide.

Not every instrument can be verified the same way, so each column also states its **verification tier**:

| Tier | Means |
| --- | --- |
| Source | Checked against the instrument's code |
| Live call | Checked through an API or assistant connector |
| UI observed | An analyst ran it in the product |
| Vendor documented | The vendor says so; nothing checked yet |

Two row groups will be added as instruments that need them arrive: **label decomposition** (what underlying observation produces a tool's headline number, per guide §37) and **prompt demand** (whether a tool's demand estimates are modeled or observed, per guide §52).

| Instrument | Tool guide | Status |
| --- | --- | --- |
| Xofu | xofu.com (link to be added) | Verified; see columns above |
| Thinking Inspector | Citation Inspector page (link to be added) | Verified; see columns above |
| Citation Inspector | Citation Inspector page (link to be added) | Planned; design reviewed, not yet built |

**Planned for verification.** The instruments below track brands in AI answers, or include AI visibility features within broader platforms. Listed alphabetically; not a ranking or an endorsement, and none has been verified yet. The list will grow.

Ahrefs (Brand Radar) · AIclicks · AI Peekaboo · Alhena AI · Am I on AI? · Amplitude · AthenaHQ · Brandlight · BrightEdge · Clearscope · Cognizo · Conductor · Dageno AI · Evertune · Frase · geotoolbox · Goodie · GrowthOS · Gumshoe.AI · HubSpot AEO · Keytomic · Knowatoa · Loudmink · Mentionova · Nightwatch · Otterly.ai · Peec AI · Petra Labs · Profound · Promptmonitor · Rank Prompt · Rankscale · Rankshift · Scrunch · SE Ranking (SE Visible) · Searchable · seoClarity · Semrush (AI Visibility Toolkit) · Sight AI · Similarweb · SISTRIX · Superlines · Surfer · Visiblie · Waikay · Wellows · Writesonic · XFunnel · Yext Scout · ZipTie

Missing an instrument? Tell us through the contact page on xofu.com (link to be added).

The full collection, with comparison views keyed by measurement job (for example, "which tools can establish Retrieved?"), will live in the **Instrument Reference Repository**. This page will link to it once it is public.

## Known gaps

Things this reference has not yet established, or that the instruments currently get wrong:

- **Gemini citations in Xofu.** Gemini responses carry a platform-supplied list of cited URLs. Whether those can be checked against the answer text is not yet established.
- **Failed responses in Xofu.** Whether failed or incomplete engine responses are visible has not been established.
- **TI run list.** Paging through the run list can skip runs that share a timestamp, because runs in a job are stamped with the job's submission time. Use a job's results to see all of its runs.
- **TI timing.** There is no per-run start or finish time, so runs within a job can't be ordered or checked for drift.

## Notes on the other two guides

Neither instrument is built for the other two guides, and forcing a fuller map would break the AI Visibility guide's own rule (§38): treat unsupported parts of a method as external work.

### Information Design for Humans at Work

Neither instrument can establish what people need. Both guides are explicit that AI behavior is evidence about the AI system, not proof of human information need.

There are three real hooks:

- **Question expressions with context (Xofu).** The guide asks you to keep question expressions connected to the people and situation they came from (§8). Xofu stores each prompt with its topic, funnel segment and stakeholder role. It supplies expressions, never requirements.
- **Stakeholder role (Xofu).** Prompts can carry a stakeholder role, so the answer environment can be read by role. Not yet settable or filterable through the assistant connector.
- **An AI assistant in the information path (TI).** When an assistant is part of how a person reaches evidence (Part IV), TI shows the machine side of that path: what the assistant searched, surfaced and cited. What the person needs to survive that path remains an Information Design question.

### Tracing Business Impact Beyond the Click

Neither instrument measures organizational consequence. The guide names the boundary directly: an AI answer changing does not mean people received better information.

Xofu's "Impact" dashboard measures change in the answer environment, which is the close-in measure of AI Visibility's Part VI. It is where AI Visibility ends, not where Business Impact begins. Xofu's CSV and slide exports are a practical bridge into stakeholder reporting, nothing more.
