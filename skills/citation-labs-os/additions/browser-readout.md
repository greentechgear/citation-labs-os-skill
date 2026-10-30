# Showing the result in the browser

**Addition to the Citation Labs OS, not part of it.** Written by the skill's packager, not by Garrett French or Citation Labs. Where this file and the guides disagree, the guides govern.

The working record is Markdown, and most people will not open a Markdown file to read it. After the result is written, also show it as a page the user can read in their browser. This needs nothing installed: one self-contained HTML file and the browser the user already has.

## When

At the end of any task that returns a working record or readout (Tasks 01 to 06), and whenever the user asks to see a result. Skip it for a short chat answer that has no file behind it.

## How

1. Write the Markdown result first. It stays the record. The page is only a view of it.
2. Copy `readout-template.html` (next to this file). Keep its `<head>` and `<style>` exactly as they are. Replace everything inside `<main>` with the result, using only the components the template shows (masthead with task status, lead, tiles, measured set, zone matrix, findings, coverage and limits, next action, carry forward, footer). Leave out components the result does not need. Remove all of the template's example content.
3. Lay it out the way the Markdown already is, in the same order, with the same labels:
   - lead with what was measured and the most consequential observation;
   - keep observation, interpretation, and proposed action in separate columns of each finding;
   - tag evidence states exactly as the Markdown does, never stronger;
   - show the denominator and counting unit with every count;
   - mark explicit zero, missing, failed, and unknown differently (grey for absent, purple for unknown, missing, or failed).
4. HTML-escape all text that came from AI answers, web pages, interviews, or tools. Do not add scripts, external fonts, stylesheets, or images; the template's Content-Security-Policy blocks them.
5. Save it next to the Markdown with the same name and `.html` (for example `readout.md` and `readout.html`). If the Markdown changes later, regenerate the page from scratch rather than editing it.

## Opening it

- **Claude Code, Claude Desktop with file access, or any agent with a shell:** open the file in the user's default browser.
  - macOS: `open readout.html`
  - Linux: `xdg-open readout.html`
  - Windows: `start "" readout.html` (from WSL: `explorer.exe readout.html`, run in the file's folder)

  Then tell the user the full path, so they can open it again later.
- **Claude.ai and other chat surfaces without a local file system:** show the same HTML as an artifact so it renders in the chat panel, and offer the Markdown as a download if code execution is available.

If opening fails (a headless server, no display), say so and give the path. Do not install anything to get around it.
