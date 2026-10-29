"""Convert the published Task Instructions HTML page into clean Markdown.

Usage: python3 scripts/task_instructions_to_md.py page.html out.md
"""
import html
import re
import sys

TOP_LEVEL = {
    "Choose a task",
    "How the instructions connect to the references",
    "Common instructions for every task",
    "Sources and use of examples",
}


def html_to_text(raw):
    body = (re.search(r"(?s)<main.*?</main>", raw) or re.search(r"(?s)<body.*</body>", raw)).group(0)
    body = re.sub(r"(?s)<(script|style|svg|noscript|header|footer|nav)[^>]*>.*?</\1>", "", body)
    body = re.sub(r"(?i)<h[1-6][^>]*>", "\n\n# ", body)
    body = re.sub(r"(?i)<li[^>]*>", "\n- ", body)
    body = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li|tr|section|table)>", "\n", body)
    body = re.sub(r"(?i)</t[dh]>", " | ", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)
    body = re.sub(r"[ \t]+", " ", body)
    return re.sub(r"\n\s*\n+", "\n\n", body)


def text_to_markdown(text):
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("# Task Instructions for the Citation Labs Guides"))
    end = next(i for i, l in enumerate(lines) if l.strip() == "# Garrett French")
    out = []
    for line in lines[start:end]:
        s = line.strip()
        if s.startswith("Summarize with") or s in ("ChatGPT AI", "Perplexity AI"):
            continue
        if s.startswith("# "):
            h = s[2:]
            if h.startswith("Task Instructions for"):
                out.append("# " + h)
            elif h in TOP_LEVEL or re.match(r"Task 0\d\.", h):
                out.append("## " + h)
            else:
                out.append("### " + h)
        elif "|" in s and s.endswith("|"):
            cells = [c.strip() for c in s.strip("| ").split("|")]
            out.append("| " + " | ".join(cells) + " |")
            if cells[0] == "Task":
                out.append("|" + "---|" * len(cells))
        else:
            out.append(s)
    md = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    md = re.sub(
        r"By Garrett French - ([A-Za-z]+ \d+, \d{4})",
        r"*By Garrett French, Citation Labs. Published \1. Source: https://citationlabs.com/operating-system/assistant/task-instructions/*",
        md,
    )
    return md.strip() + "\n"


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        md = text_to_markdown(html_to_text(f.read()))
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(md)
