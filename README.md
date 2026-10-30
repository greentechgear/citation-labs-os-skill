# Citation Labs Operating System, as a Claude skill

This repository packages the [Citation Labs Operating System](https://citationlabs.com/operating-system/) by **Garrett French** and [Citation Labs](https://citationlabs.com/) as an [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for Claude Code, Claude.ai, and any other agent that reads `SKILL.md`.

The OS is Citation Labs' methodology for finding where a brand is not showing up in AI answers, what information is missing, what needs to change, and whether the change worked. It is built from four field guides and six assistant task modules, held together by a strict discipline about evidence: every finding keeps the strength it actually earned, and nothing gets upgraded on its way to the next step.

The official way to use it is to download the four guides, upload them to a chat, and paste a starter prompt. This skill does that setup once, permanently. Claude loads the router and rules when the topic comes up, and pulls in only the guide sections and task instructions the current question needs.

## What it does

Ask in plain language. The skill routes the request to one of the OS's six independent tasks and follows the governing guide.

| You ask | Task | You get back |
|---|---|---|
| "What do ChatGPT and Perplexity say and cite about us for these prompts?" | 01 Establish a baseline | AI Visibility Plan + Readout with coverage, the six visibility zones checked separately, and a diagnosis |
| "Our CMO, CFO, and content lead all weigh in on this. What does each need?" | 02 Shared decision | Decision Evidence Record with per-responsibility findings |
| "Turn these query fan-outs and uncited Reddit threads into interview questions" | 03 Interview questions | Passage-grounded question queue with respondent criteria |
| "Make something useful out of these interview transcripts" | 04 Prepare information | Production brief or supported draft with a claim-support table and review list |
| "We published a security evidence page. Did it work?" | 05 Plan or evaluate a test | Measurement contract or readout separating AI effects from human usefulness |
| "Did this visibility win actually matter to the business?" | 06 Business consequence | Business Impact Readout at the supported evidence strength, or a precise inquiry plan |

Say "walk me through the Citation Labs OS" with no specific problem and it runs Citation Labs' own starter flow: a short welcome, an ASCII map of the guides, and four tailored paths (Executive Tour, Diagnose a Problem, Test a Customer Scenario, Stress-Test the Framework).

It works without any paid tools. If you have the Citation Labs instruments (Thinking Inspector or XOFU) connected as MCP servers, the skill knows what each can and cannot establish and asks before anything that costs money.

## Additions to Garrett's OS

Everything above is Citation Labs' method, unchanged. This repo adds two things on top, kept in `skills/citation-labs-os/additions/` and clearly labeled as not part of the OS. Both came out of running Task 01 on a real site.

**Let Claude collect the answers itself.** Task 01 needs the live ChatGPT and Perplexity answers. Without help, that means running every prompt by hand and pasting the results in. If you install the [Claude in Chrome](https://claude.com/claude-in-chrome) extension first, Claude can run the prompts in your own signed-in browser, capture the full answer and every cited link, and code the zones from what it saw. Headless browser tools tend to get blocked by bot checks on these sites. Your real browser does not.

**Measure signed out, or with memory off.** Where a system allows it (Gemini, Google Search), run it signed out from a separate Chrome profile with no Google account. Where it needs an account (ChatGPT), turn memory off first. ChatGPT's Temporary chat still uses your saved memory. In the test run, a "clean" temporary chat answered with a reference to the user's own company, which made the run useless as a baseline. Before collecting answers, turn off memory and chat-history reference, clear custom instructions, and use an account that is not tied to the brand you are measuring. Then check every answer for anything that knows who you are, and rerun any answer that does. The addition walks Claude through this and has it ask you to change the settings yourself.

**See the result in your browser.** The OS's working records are Markdown, which most people will not open. When a task finishes, Claude also writes the readout as a single self-contained HTML page next to the Markdown file and opens it in your default browser. It shows the headline finding first, a grid of the six visibility zones per prompt and system, and each finding with its observation, interpretation, and proposed action side by side. Nothing to install: the page has no scripts, fonts, or outside links to load, and works offline. In Claude.ai the same page appears as an artifact in the chat. The Markdown stays the record.

## Install

Optional but recommended for Task 01: install [Claude in Chrome](https://claude.com/claude-in-chrome) so Claude can observe AI answers directly (see above).


### Claude Code (recommended)

```
/plugin marketplace add greentechgear/citation-labs-os-skill
/plugin install citation-labs-os@citation-labs-os
```

Or copy the skill folder in by hand:

```bash
git clone https://github.com/greentechgear/citation-labs-os-skill
cp -r citation-labs-os-skill/skills/citation-labs-os ~/.claude/skills/
```

### Claude.ai and Claude Desktop

Download `citation-labs-os.zip` from the [latest release](https://github.com/greentechgear/citation-labs-os-skill/releases/latest), then go to **Settings → Capabilities → Skills → Upload skill** and choose the zip. (Code execution must be enabled for skills.)

### Other agents

The `skills/citation-labs-os/` folder is a standard skill. Point any agent that supports `SKILL.md` at it, or copy it into that agent's skills directory.

## What's inside

```
skills/citation-labs-os/
├── SKILL.md                         router, evidence rules, task quick cards, starter flow
├── references/
│   ├── task-instructions.md         the six task modules + common instructions
│   ├── using-the-guides-with-an-assistant.md
│   ├── guides/                      the four field guides, as Markdown
│   │   ├── ai-visibility.md
│   │   ├── information-design.md
│   │   ├── business-impact.md
│   │   └── shared-decision.md
│   ├── instruments/                 Thinking Inspector, XOFU, Citation Inspector, observation catalog, card schema
│   └── sources.md                   provenance, versions, known gaps
└── additions/                       not Citation Labs content (see "Additions" above)
    ├── collecting-live-answers.md   browser collection of live answers, memory off first
    ├── browser-readout.md           show the finished result as a page in the browser
    └── readout-template.html        the self-contained page template
scripts/refresh.sh                   re-download everything from citationlabs.com
```

## Keeping it current

The guides are living editions. `scripts/refresh.sh` re-downloads every file from citationlabs.com and regenerates the Markdown (needs `curl`, `python3`, and [`uv`](https://docs.astral.sh/uv/)). Review the diff, then bump the version in `.claude-plugin/`.

## Credit and rights

The methodology, the four field guides, the task instructions, and the instrument references are the work of Garrett French and Citation Labs, © Citation Labs. Citation Labs publishes them for people to give to their AI assistants; this repository bundles them, unchanged apart from conversion to Markdown, so that a skill can do the same. The `additions/` folder and the parts of `SKILL.md` marked as additions are the packager's, not Citation Labs'. See [NOTICE](NOTICE).

For help applying the field guides to a real problem, [contact Citation Labs](https://citationlabs.com/contact/).

Garrett: if you would rather host this under the Citation Labs GitHub, or want anything changed or removed, open an issue or just say the word and it's yours.
