#!/usr/bin/env bash
# Re-download the Citation Labs Operating System materials and regenerate the
# skill's reference files. Requires curl, python3, and uv (for markitdown).
# Run from the repository root, then review `git diff` before committing.
set -euo pipefail

BASE=https://citationlabs.com
REF=skills/citation-labs-os/references
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

fetch() { curl -fsSL "$BASE/$1" -o "$2"; }

mkdir -p "$REF/guides" "$REF/instruments"

for pair in AI-Visibility:ai-visibility Information-Design:information-design \
            Business-Impact:business-impact Shared-Decision:shared-decision; do
  src=${pair%%:*}; dst=${pair##*:}
  fetch "wp-content/uploads/2026/09/$src.docx" "$WORK/$src.docx"
  uvx --quiet --from 'markitdown[docx]' markitdown "$WORK/$src.docx" > "$REF/guides/$dst.md"
done

fetch operating-system/assistant/task-instructions/ "$WORK/task-instructions.html"
python3 -I scripts/task_instructions_to_md.py "$WORK/task-instructions.html" "$REF/task-instructions.md"

fetch operating-system/assistant/Using_the_Citation_Labs_Guides_With_an_Assistant_v0_1.md "$REF/using-the-guides-with-an-assistant.md"
fetch operating-system/instrument/AI_Visibility_Instrument_Reference.md "$REF/instruments/ai-visibility-instrument-reference.md"
fetch operating-system/instrument/Citation_Inspector.md "$REF/instruments/citation-inspector.md"
fetch operating-system/references/INSTRUMENT_CARD_SCHEMA_v0_2.md "$REF/instruments/instrument-card-schema-v0.2.md"
fetch operating-system/references/observations.v0.2.yaml "$REF/instruments/observations.v0.2.yaml"
fetch operating-system/references/ti.card.v0.2.yaml "$REF/instruments/ti.card.v0.2.yaml"
fetch operating-system/references/TI_MCP_Briefing_for_Assistant_reviewed_v0_3.md "$REF/instruments/ti-mcp-briefing-v0.3.md"

echo "Refreshed. If Citation Labs published new versions or file names, update references/sources.md and SKILL.md."
