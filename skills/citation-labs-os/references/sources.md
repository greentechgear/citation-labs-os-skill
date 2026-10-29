# Sources

Every reference file in this skill is a copy of material Citation Labs publishes for exactly this use (download the guides and give them to your AI) at https://citationlabs.com/operating-system/. All content is by Garrett French and Citation Labs. Fetched 27 October 2026. The guides are converted from the published Word files to Markdown; images were dropped and text is otherwise unchanged.

| Label | File here | Edition | Published at |
|---|---|---|---|
| G1 | guides/ai-visibility.md | AI Visibility: Diagnose, Intervene, Report. 2026 edition (2 September 2026 working edition) | https://citationlabs.com/wp-content/uploads/2026/09/AI-Visibility.docx |
| G2 | guides/shared-decision.md | Helping People Work Through a Shared Decision, Revision 8, 10 September 2026 | https://citationlabs.com/wp-content/uploads/2026/09/Shared-Decision.docx |
| G3 | guides/information-design.md | Information Design for Humans at Work, September 2026 working edition | https://citationlabs.com/wp-content/uploads/2026/09/Information-Design.docx |
| G4 | guides/business-impact.md | Tracing Business Impact Beyond the Click, September 2026 working edition | https://citationlabs.com/wp-content/uploads/2026/09/Business-Impact.docx |
| Tasks | task-instructions.md | Task Instructions for the Citation Labs Guides v0.1 (10 Sept 2026, published 16 Oct 2026) | https://citationlabs.com/operating-system/assistant/task-instructions/ |
| Intro | using-the-guides-with-an-assistant.md | v0.1, 10 September 2026 | https://citationlabs.com/operating-system/assistant/Using_the_Citation_Labs_Guides_With_an_Assistant_v0_1.md |
| T1 | instruments/ti-mcp-briefing-v0.3.md | TI MCP Briefing for the Assistant, reviewed v0.3 | https://citationlabs.com/operating-system/references/TI_MCP_Briefing_for_Assistant_reviewed_v0_3.md |
| O | instruments/observations.v0.2.yaml | Observation catalog v0.2 | https://citationlabs.com/operating-system/references/observations.v0.2.yaml |
| S | instruments/instrument-card-schema-v0.2.md | Instrument Card Schema v0.2 | https://citationlabs.com/operating-system/references/INSTRUMENT_CARD_SCHEMA_v0_2.md |
| Card | instruments/ti.card.v0.2.yaml | Thinking Inspector capability card v0.2 | https://citationlabs.com/operating-system/references/ti.card.v0.2.yaml |
| | instruments/ai-visibility-instrument-reference.md | AI Visibility Instrument Reference (XOFU, TI, Citation Inspector) | https://citationlabs.com/operating-system/instrument/AI_Visibility_Instrument_Reference.md |
| | instruments/citation-inspector.md | Citation Inspector (planned TI successor) | https://citationlabs.com/operating-system/instrument/Citation_Inspector.md |

## Known gaps in the published set

The task instructions mention files that were not publicly available when this skill was built: the XOFU MCP Briefing [T2], `references/START_HERE.md`, `SOURCE_INDEX.md`, the validator, the interview proposals [P1-P2], and the Operating System Hub Source docx (returned 404). Where the task instructions cite [T2], use the XOFU sections of `instruments/ai-visibility-instrument-reference.md` and the live tool definitions of any connected XOFU server.

## Refreshing

Run `scripts/refresh.sh` from the repository root to re-download everything and regenerate the Markdown. Review the diff before committing; the guides are living editions.
