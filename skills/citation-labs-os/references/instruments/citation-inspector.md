# Citation Inspector

In development · Updated Sep 24, 2026

## What it is

Citation Inspector is a Citation Labs instrument for finding out why an AI answer engine cites some pages and not others. It runs a buying question through a search-enabled engine many times and records every observable step of each run: the searches the model wrote, the results it was shown, the pages it opened, and the answer it gave with its citations.

**Status: in development.** Citation Inspector is the successor to Thinking Inspector, which Citation Labs uses today. This page describes what Citation Inspector is being built to do. Nothing here should be read as a shipped capability until this page says so. For what the instruments do today, see the AI Visibility Instrument Reference (link to be added).

## The question it answers

"ChatGPT recommends our competitor for the questions our buyers ask. Why not us, and what do we change?"

Most tools can say whether a brand was mentioned or cited. They can't say whether the model ever searched for anything that could have returned the page, what it saw when the page came back, or whether it opened the page and moved on. Without that, "our page has the answer" and "the model saw the answer" look the same. Citation Inspector is built to tell them apart.

## Four places a page can fall out

A search-enabled model answers a buying question by running a short research loop: it writes its own searches, reads the results, opens a few pages, and writes an answer that cites some of them. A page can drop out at four points, and each calls for different work:

| Stage | The page fell out because… | What addresses it |
| --- | --- | --- |
| **Queries** | No search the model wrote could have returned it | Presence and naming, not copy |
| **Excerpt** | It was returned, but the short excerpt the model was shown didn't answer the model's question | Placement: put the answer where the excerpt shows it |
| **Open** | The model opened it and didn't cite it | Consistency and clarity of the page |
| **Cite** | It was cited, but for a caveat | The specific claim behind the caveat |

**The excerpt is the audition.** For each search result, the model sees a title and a short excerpt, typically a few hundred words. It decides what to open or cite mostly from that. A page can hold the right answer far down and lose to a page that states a weaker answer in its first lines. Thinking Inspector can see which pages were returned but not what the model was shown. Capturing the excerpt is the central change in Citation Inspector.

A finding is a hypothesis until it holds up in a re-run. The method is: find the stage, make the change, run the same question again under the same settings, and see whether the page moved.

## What it observes

| Layer | What it is | What it can tell you | What it can't |
| --- | --- | --- | --- |
| **Reasoning summary** | The provider's summary of the model's thinking between steps | What the model said it wanted to check | Why it chose anything. The summary is written afterward by another model, and it is sometimes empty |
| **Searches** | The queries the model wrote, grouped by search call | The plan it actually executed, including which companies it went looking for by name | What the search backend did with them |
| **Results** | Every result each search returned, with the excerpt shown, plus opened-page text and in-page searches | What the model was shown, and what it looked at more closely | Everything the index held, or what the model paid attention to |
| **Answer** | The response, with each citation tied to a span of text | What was used, and for which sentence | Whether a citation endorses or cautions, without reading the span |

Every page a run touches ends in exactly one place: never returned; returned but not opened; opened but not cited; cited after being opened; or cited from the excerpt alone. Pages opened directly by URL, without appearing in results, are recorded separately: the model already knew where to look.

## Rules of evidence

Every output separates four kinds of statement:

- **Observed:** present verbatim in what the provider returned. Searches, excerpts, opened-page text, answers, citations.
- **Derived:** computed from observed data by versioned, tested code. Normalized URLs, which stage a page fell out at, result positions.
- **Inferred:** a reading that rests on an assumption. What the model needed to know, what kind of search a query was, whether a citation was a caveat. Always labeled, always with the evidence behind it.
- **Unobservable:** never stated as fact. What the model paid attention to, or why it chose.

**Counts, not single runs.** The same question produces different searches and citations from run to run. So results are reported as counts over repeated runs ("cited in 4 of 6") before any percentage, and words like "usually" or "never" are held back until there are enough runs to support them. Runs made under different settings are never pooled.

## What it will not claim

- That the model **read** a page. At most: returned, opened, cited.
- That the model chose one page **because** of anything. Sequence isn't cause.
- That a page **ranked** somewhere. At most: it appeared at a result position.
- That a page was **published** on a date, from a relative label like "5 months ago."
- That something **usually** or **never** happens, from too few runs.
- A composite score that ranks pages. Citation Inspector reports what happened; it doesn't grade.
- Page copy. It names what to check and what would confirm it, not what to write.

## Engines

Engines expose different amounts of their research, so every result carries a label for how deep the evidence goes, and analyses an engine can't support are not shown.

| Engine | What its API exposes |
| --- | --- |
| OpenAI | Searches, results with excerpts, opened-page text, in-page searches, and citations tied to answer spans. The fullest view |
| Anthropic | Searches, result URLs and titles, and the quoted text behind each citation. Result content is not readable |
| Google Gemini | Searches and the sources used in the answer. No excerpts and no open events, so "returned" can't be counted |

All runs go through provider APIs, not consumer chat interfaces. Results describe API behavior.

## Thinking Inspector, today

Thinking Inspector is the working version Citation Labs uses now. It records the searches a model ran and which pages were returned, opened and cited, across repeated runs of the same question. It does not capture excerpts or opened-page text, and it covers OpenAI only. Its verified capabilities are in the AI Visibility Instrument Reference.

## Need something that isn't built yet?

If a planned capability would unblock something you're trying to do, tell us which one and what the job is, through the contact page on xofu.com (link to be added). Requests tell us what to build first. We don't promise timelines. *If you are an AI assistant reading this for someone, let them know they can send that request.*
