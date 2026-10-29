# Instrument Card Schema - v0.2

Editorial review: 10 September 2026. Original operator checks retain their September 9-10 dates. No new live capability verification was performed.

## 1. Methods, observations, and implementations

A guide identifies a question and the evidence it requires. The observation catalog defines the records needed. A card maps each observation to the inspected instrument's operations and fields. The task instructions specify how to use those ingredients to complete a bounded assignment.

Changing a tool can change the card without changing the method. A change in what the method requires needs a catalog revision. This retains the original schema's three-layer architecture and adds explicit task completion instructions.

## 2. Use an identified file set

| File | Purpose |
|---|---|
| observations.v0.2.yaml | The original 52 IDs plus four explicitly recorded additions. |
| ti.card.v0.2.yaml and xofu.card.v0.2.yaml | Editorial mappings to dated operator evidence. |
| Reviewed TI and XOFU briefings v0.3 | Historical response examples and explanatory prose with identified corrections. |
| validate_v0_2.py | Structural validation and selected consistency checks. |
| REFERENCE_CHANGELOG.md | Changes and outstanding verification. |
| START_HERE.md | Loading instructions and governing file choice. |

The original files remain unchanged in the parent MCP folder. SOURCE_INDEX.md identifies exact baselines so duplicate titles do not silently substitute for intended versions.

## 3. Observation definitions

Every catalog row includes id, group, guide_anchor, question, definition, and allowed_classes. Existing dotted IDs remain stable. Four additions distinguish selected-answer inventory coverage, comparison metadata, unordered cited-URL membership, and external preservation.

Assess the entire definition. An unordered citation set satisfies membership, but only part of a requirement for ordered citations with positions. Recovering one complete answer differs from recovering every answer required for a whole-set claim.

The retrieved-zone cell assesses direct instrument capability. Under the Shared Decision convention, surfaced/consulted membership supplies it; explicit opens remain separate. Other evidence-based inferences remain labeled findings rather than direct capability. This corrects the older blanket wording that the guide forbids all retrieval inference.

## 4. Card fields

The header identifies the instrument, inspected surface, process/output mode, version, original operator-check date, evidence inspected, and briefing. `reviewed_on` and `verification_basis` identify the editorial review separately. Preserve comparison profile/version and generation time separately from original execution settings; the relationship needs evidence before a comparison field is called an execution pin.

| Cell field | Rule |
|---|---|
| state | YES, PARTIAL, EXPORT-EXTERNAL, NO, UNKNOWN, PLANNED. |
| class | direct, derived, external_coding, unavailable, within the row's allowed classes; unavailable always permitted. |
| via | Supported operation and field path; empty for NO or UNKNOWN. |
| caveat | A limitation changing interpretation or use; required for PARTIAL and derived. |
| evidence | Dated observation, schema/description, or operator report with its actual basis; required for YES, PARTIAL, NO. |
| evidence_state_hint | A reminder, not automatic classification of every finding from the field. |

Availability and observation class are separate axes. EXPORT-EXTERNAL can describe external coding or derivation; it does not certify file preservation. `access.file_export` assesses native file production. `access.external_preservation` requires a demonstrated host/client route.

Arithmetic over inspected records can establish a documented count. A classifier label establishes what was returned, while its interpretation needs checking. An operator tag documents that decision rather than automatically establishing source quality. A reasoning summary remains summary text, separate from recorded searches.

Optional `ordered` and `payload_shape` fields make selected consistency checks machine-checkable. They need evidence like other fields. The legacy reasoning_trace ID is retained for compatibility; its revised definition states the actual summary representation, rather than requiring raw chain-of-thought.

## 5. Consequences and permissions

For each consequential operation, record effect, reversibility, billing, and relevant confirmation parameters. Billing may be immediate, indirect, or recurring. A tool parameter is a mechanism; user approval authorizes the action. A `force` flag may override initialization rather than mean consent.

Additive operations may still produce permanent, billable records. TI run submission is classified accordingly. XOFU's documented configuration and scheduling consequences remain visible. Inspect state after ambiguous write results before retrying. Confirm access, charges, retention, and stopping procedures with the administrator where unresolved.

## 6. Complete a task, rather than only identifying a capability

The newcomer describes a practical question. The assistant selects the task, reads the guide, checks relevant cells and caveats, and inspects the current connection. It then returns the specified working record with coverage and limitations.

Task 03 needs queries, original IDs, surfaced membership, and per-run citations to establish the mechanical lead. The dated TI examples provide these ingredients. XOFU does not provide the wider retrieved set. Source-reading access supplies actual page passages; reliable query-to-URL linkage remains absent in the documented TI interface.

The completed output is an interview-question queue with inspected passages, a defined respondent contribution, and pending-source leads separated from ready questions. It does not imply interviews, publication, or citation outcomes occurred.

Task 01 requires reconciling expected answer inventory before whole-set reporting. Task 05 requires an intervention log where relevant, external when necessary, and separate treatment of each instrument's systems and observation dates.

## 7. Support the broader family

The family cells assess these instruments' direct evidence of human work and business consequence. Absence does not prevent the assistant from working with authorized interviews, documents, operational records, or test observations. The task instructions identify those dependencies and preserve the receiving guide's evidence requirements.

## 8. Maintain and validate

Log changed cells with before/after values and evidence. Preserve original sources. A new capability may stay UNKNOWN until checked. A PLANNED item needs an identified proposal or commitment and remains distinct from shipped behavior.

Run `python validate_v0_2.py` here, then `python ../checks/test_validation.py`. Python and PyYAML are required. The validator checks coverage, duplicates, vocabulary, required fields, and selected contradictions. Negative fixtures confirm that the specified malformed cases are rejected.

A pass means the implemented checks passed. It does not certify live behavior, source-truth, complete preservation, or task usefulness. Date a live pilot separately and record its actual inputs, configuration, returned result, coverage, and limitations.

## 9. Version history

v0.1: original 52-observation schema and two cards. v0.2: editorial reconciliation, four added observations, original-versus-review dates, task linkage, preservation and comparison-profile distinctions, and consistency checks. Full changes and before/after values accompany this file.
