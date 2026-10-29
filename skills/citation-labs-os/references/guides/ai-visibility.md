**CITATION LABS FIELD GUIDE**

# AI VISIBILITY: DIAGNOSE, INTERVENE, REPORT

A practical guide to choosing a tracked prompt set, diagnosing how AI answer environments use the information relevant to those prompts, choosing an intervention, and measuring what changed.

**2026 EDITION | Citation Labs**

## THE OPERATING SEQUENCE

| **1 CHOOSE THE TRACKED PROMPT SET** | **2 BASELINE THE ANSWER ENVIRONMENT** | **3 DIAGNOSE THE GAP** | **4 CHOOSE THE INTERVENTION** |
| --- | --- | --- | --- |
| **5 DEFINE THE MEASUREMENT CONTRACT** | **6 RE-TEST AND INTERPRET** | **7 CARRY THE EVIDENCE FORWARD** |  |

### GUIDE MAP

| **If you need to…** | **Go to** |
| --- | --- |
| Decide what to measure and why | Part I - Choose the Tracked Prompt Set |
| Establish the pre-intervention state | Part II - Baseline the Answer Environment |
| Find where the problem occurs | Part III - Diagnose the Gap |
| Decide what information or evidence should change | Part IV - Choose the Intervention |
| Define what should happen if it works | Part V - Define the Measurement Contract |
| Compare the re-test with the baseline | Part VI - Re-test and Interpret |
| Decide whether further work is justified | Part VII - Carry the Evidence Forward |
| Evaluate tools, APIs, agents, or MCPs | Part VIII - Evaluating AI Visibility Measurement Tools, Agents, and MCPs |
| See the method applied end to end | Part IX - Worked Case: Industrial Gateway Security Review |
| Trace methods and practitioner lineage | Part X - Methods, Practitioner Lineage, and Sources |
| Use the working record | Appendix - AI Visibility Plan + Readout |
| Work through the method with an assistant | **Using This Guide With an Assistant** |
| Hand off an unresolved question | **See Family Handoff Protocol** |

## WHAT THIS GUIDE HELPS YOU DO

AI visibility work can begin with keyword research, stakeholder prompts, modeled AI-demand estimates, observed prompts, customer questions, platform scores, citations, source logs, or raw answers.

Each can be useful. None tells you by itself what should change.

This guide helps answer five questions:

**Which prompts are worth measuring?**

**What is the answer environment doing now?**

**Where does the problem occur?**

**What intervention fits that diagnosis?**

**What changed afterward?**

The goal is not one visibility score. It is a diagnosis specific enough to support an intervention and a re-test.

### USE THIS GUIDE WHEN

Use this guide when you have an AI visibility concern and need to move from observation to a defensible next action.

It is especially useful when you need to:

• choose a finite prompt set worth measuring repeatedly;

• establish a baseline before changing content, evidence, or distribution;

• distinguish retrieval, citation, mention, recommendation, and accuracy problems;

• decide whether an intervention is warranted and where it should operate;

• define success before an intervention ships;

• interpret a re-test without turning every movement into a business claim;

• understand what a measurement tool can and cannot establish.

## IMPORTANT EVIDENCE BOUNDARIES

Different evidence supports different claims.

• A stakeholder request establishes a strategic concern, not market demand.

• Historical keyword demand establishes search behavior, not equivalent AI-prompt demand.

• A modeled AI-demand estimate remains an estimate.

• A customer or support question establishes that the question occurred, not how prevalent it is.

• AI query decomposition shows how a system investigated a prompt. It does not establish human information need.

**AI behavior can provide a research lead about human information need. It is not evidence of human information need by itself.**

Likewise:

**Better AI visibility does not by itself establish better human outcomes or business impact.**

Use an evidence state when the strength of a finding, requirement, interpretation, expected effect, or handoff matters to a decision. You do not need to classify every sentence.

• OBSERVED / DOCUMENTED - directly observed, measured, recorded, documented, or established through inspection.

• MODELED / ESTIMATED - produced through modeling, weighting, extrapolation, forecasting, or estimation.

• INFERRED - a reasonable conclusion from evidence that was not directly observed.

• HYPOTHESIS - a proposed explanation, requirement, mechanism, or expected effect that still needs evidence.

• UNKNOWN - the available evidence does not support a stronger classification.

Provenance remains separate. Record where the evidence came from.

## THE WORKING RECORD

Use one **AI Visibility Plan + Readout**.

Before the intervention, record:

• decision this investigation must help make;

• tracked prompt set and provenance;

• baseline and measurement conditions;

• diagnosis;

• intervention;

• measurement contract.

After the re-test, add:

• what changed;

• what did not;

• comparison and relevant concurrent changes;

• interpretation;

• strongest supported statement;

• next decision;

• evidence or hypotheses worth carrying forward.

The complete working version appears in the Appendix.

### THE CITATION LABS FIELD-GUIDE FAMILY

Start anywhere. The next unresolved question determines the guide.

| **AI VISIBILITY** | **INFORMATION DESIGN** | **BUSINESS IMPACT** |
| --- | --- | --- |
| What is the AI answer environment doing? | What must information enable for people? | What happened in the organization? |
| **YOU ARE HERE** | **PEER GUIDE** | **PEER GUIDE** |

### AI VISIBILITY: DIAGNOSE, INTERVENE, RETEST

AI VISIBILITY: DIAGNOSE, INTERVENE, RETEST investigates the AI answer environment: what systems find, retrieve, cite, represent, omit, and recommend, and whether an AI-facing intervention changed those conditions.

### INFORMATION DESIGN FOR HUMANS AT WORK

[<u>INFORMATION DESIGN FOR HUMANS AT WORK</u>](https://citationlabs.com/operating-system/field-guides/information-design/) investigates human work and the information environment: what people are trying to accomplish, what information must enable, where the environment falls short, what should change, and whether the change helped.

### TRACING BUSINESS IMPACT BEYOND THE CLICK

[<u>TRACING BUSINESS IMPACT BEYOND THE CLICK</u>](https://citationlabs.com/operating-system/field-guides/business-impact/) investigates whether a bounded information or human-work result produces a meaningful organizational consequence - or whether an observed business burden or opportunity has an information component worth investigating.

**QUESTIONS, NOT ARTIFACTS** The guides own questions and evidence, not pages, resources, or systems. The same artifact may appear in more than one guide, but each kind of effect must be established separately.

**HANDOFF RULE** When work moves, carry the established result at the strength already earned, together with its evidence state, evidence and provenance, material conditions, important limits, and the next uncertainty or hypothesis. Do not upgrade it on arrival.

**ANOTHER DOMAIN** Product truth, Engineering judgment, Finance definitions, Legal or regulatory interpretation, formal causal estimation, and other specialist questions belong with the person or method closest to them.

### HELPING PEOPLE WORK THROUGH A SHARED DECISION

[<u>Helping People Work Through a Shared Decision</u>](https://citationlabs.com/operating-system/field-guides/shared-decision/) for an applied Information Design exercise that examines one consequential decision through the responsibilities of the people involved, see Helping People Work Through a Shared Decision.

## USING THIS GUIDE WITH AN ASSISTANT

An assistant can help organize evidence, preserve distinctions, identify missing questions, test the logic of a proposed claim, and draft the working record. It cannot establish facts about people, systems, or the organization that its sources do not support.

### START HERE IF YOUR STRATEGY FEELS UNCLEAR OR INDISTINCT

You do not need a fully formed ai visibility direction or strategy to begin.

Give the assistant three things:

* what you are seeing or concerned about;
* what evidence you already have, or “none yet”;
* what decision you need to make, or “I’m not sure yet.”

The assistant should help narrow the concern and return a small candidate prompt set. For each prompt, it should explain why the prompt may be useful and identify what still needs to be established.

For example, if your concern is:

“Our gateway’s security capabilities seem to be missing or misrepresented in AI answers.”

The first candidate set might include:

* “Does Product X support certificate-based authentication?”
  **Why include it:** Tests a specific security capability that may affect product evaluation.
  **Still unknown:** Whether this question reflects an important customer or buyer requirement.
* “What industrial gateways support secure offline operation?”
  **Why include it:** Tests whether the product appears when a relevant operating constraint is introduced.
  **Still unknown:** Whether offline operation materially affects the target decision.
* “What are the security limitations of Product X?”
  **Why include it:** Tests how the system represents conditions, limitations, and risk.
  **Still unknown:** Which limitations are consequential to the intended user.

This is a candidate set, not a baseline. Refine the prompts before measurement begins.

Framing the initial concern and producing a candidate prompt set should be a short first step. Gathering evidence, running the measurement, and completing a later re-test may take longer.

For the full guided interaction, see the [**<u>Assistant Overview</u>**](https://drive.google.com/file/d/1LfexxyBUKh4EtlTZUmNJw1h4k3NX5MR-/view) and [**<u>Task Instructions</u>**](https://drive.google.com/file/d/1fDoXZk19cI7HmIoXrRu-RWOAFUfoqv0T/view).

When using more than one guide, ask the assistant to identify which guide owns the next unresolved question and to carry the established result forward without upgrading it.

**FAMILY ROUTER PROMPT** “Here is what we know and the current Evidence to Carry Forward block. Which guide or specialist domain owns the next unresolved question? Separate the established result from the working hypothesis, preserve the evidence state and provenance, and begin in the receiving method without upgrading the claim.”

## PART I - CHOOSE THE TRACKED PROMPT SET

The first job is not to collect every prompt you can find.

It is to build a finite set of prompts worth measuring repeatedly - and to know why each one is there.

Prompts can come from many places: keyword research, stakeholders, AI-demand tools, customer conversations, support records, communities, domain experts, or your own diagnostic testing.

Those sources are useful for different reasons.

The goal is to preserve those differences rather than flatten them into one list.

### 1. START WITH WHAT IS WORTH MEASURING

Keyword research still matters.

It can tell you how people search, which topics recur, which comparisons have demand, how language varies, and where commercial interest appears.

AI visibility work gives you additional sources of candidate prompts:

• stakeholder priorities;

• Search Console and internal search;

• modeled AI-demand estimates;

• observed prompt datasets;

• sales and support;

• communities and reviews;

• customer research;

• subject-matter experts;

• AI query decomposition;

• deliberate diagnostic probes.

At this stage, these are **candidates**.

A prompt belongs in the tracked prompt set when you can state why measuring it will help answer the current question.

Common reasons include:

• there is evidence people ask it or something close to it;

• it matters to a real task or decision;

• the organization has a strategic reason to monitor it;

• it helps test a suspected AI-search mechanism.

**WHAT TO DO** For every prompt you admit to the tracked prompt set, write one sentence explaining why it is there. If you cannot do that, it is probably still a candidate.

### 2. RECORD WHY EACH PROMPT IS IN THE SET

Different sources support different claims.

| **Source** | **What it can help establish** | **What it does not establish by itself** | **Provenance** |
| --- | --- | --- | --- |
| Stakeholder input | Strategic priority or concern | Market prevalence | stakeholder |
| Keyword research | Search demand and language | Equivalent AI-prompt demand | search-demand |
| Search Console / site search | First-party search behavior | Full information need | first-party-search |
| Modeled AI demand | Directional prioritization | Observed prompt frequency | modeled-ai-demand |
| Observed prompt data | Behavior in the measured sample | Total market prevalence | observed-ai-prompt |
| Sales / support / CRM | Real customer questions | Market-wide frequency | first-party-customer |
| Communities / reviews | Natural language, objections, criteria | Representative prevalence | community |
| Customer research | Work context and information needs | Large-scale frequency | human-research |
| Domain expert | Technical criteria and constraints | Customer demand | domain-expert |
| Decision/work research | Task and information requirements | AI-prompt frequency | decision-research |
| AI query decomposition | Machine investigation behavior | Human need or demand | ai-system-behavior |
| Diagnostic probe | Mechanism testing | External demand | diagnostic-probe |

A prompt can have more than one provenance tag.

For example:

industrial gateway security

might have historical keyword demand.

Does Product X support certificate-based authentication?

might come from sales records and security SMEs.

What are the best gateways for factories with no external connectivity?

might initially exist only because you want to test how an AI system handles that condition.

All three can belong in the same measurement program. They do not support the same conclusions.

#### START WITH THE EVIDENCE YOU ALREADY HAVE

You do not need every source in the table before starting.

Use the evidence your organization can already inspect: keyword data, Search Console, customer and support records, existing research, domain expertise, and current AI measurements.

Add modeled data, observed-prompt datasets, community research, new primary research, or diagnostic probes when they would improve an actual decision.

The job is not to collect every possible source. It is to know what the evidence behind each prompt allows you to say.

### 3. SEPARATE DEMAND FROM DECISION IMPORTANCE

Two questions are easy to collapse:

**Do people ask this?**

and

**Does resolving it matter?**

Keep them separate.

#### DEMAND EVIDENCE

What suggests this question, or something close to it, is actually being expressed?

#### WORK / DECISION EVIDENCE

What suggests the answer matters to a real task, choice, approval, comparison, or decision?

A high-volume query can be commercially unimportant.

A low-volume question can determine whether a product is approved.

And a diagnostic prompt may be worth measuring even when there is no evidence of external demand.

**WHAT TO DO** Record demand evidence and decision/work evidence in separate fields. That prevents a strong number in one from silently standing in for the other.

### 4. SEARCH INTENT DOES NOT FULLY DESCRIBE THE WORK

Search intent remains useful.

It helps practitioners interpret what sits behind literal keywords and organize content around likely goals.

But broad labels such as *informational*, *commercial*, or *transactional* may not describe what a consequential task actually requires.

Consider:

**industrial gateway security**

An OT security reviewer deciding whether a gateway can be approved for regulated manufacturing may need to establish:

• how authentication works;

• whether certificates are supported;

• how firmware is updated;

• how vulnerabilities are handled;

• which standards apply;

• whether external connectivity is required;

• which product/version the evidence applies to;

• which documentation is authoritative.

Those requirements may appear across many different searches and prompts.

A longer prompt does not automatically give you that context.

### 5. WHEN YOU NEED TO UNDERSTAND THE HUMAN WORK

You do not need customer research for every prompt.

You can measure a stakeholder priority or a diagnostic probe without claiming it represents an important human need.

Stronger evidence becomes necessary when you want to say:

• people need this information;

• an omission makes the answer inadequate;

• a question matters to the decision;

• improving the answer would better serve the person using it.

When those claims matter, ask:

1. Who is doing the work?

2. What are they trying to accomplish?

3. What must they decide, compare, verify, execute, communicate, approve, or reject?

4. What information does that require?

5. What would a satisfactory answer contain?

**WHAT TO DO** Record what you know and how you know it. Use INFERRED or HYPOTHESIS when the evidence is indirect. Use UNKNOWN when you do not know.

If answering these questions becomes a substantial research project of its own, move into [**<u>Information Design for Humans at Work</u>**](https://citationlabs.com/operating-system/field-guides/information-design/).

**CALL INFORMATION DESIGN** Call when the unresolved question is what people are trying to accomplish, what information must enable, or whether an information change helped their work. Bring the established AI result, evidence state, evidence and provenance, material conditions, important limits, and the new uncertainty.

#### PIVOT TO INFORMATION DESIGN

If you cannot define required answer elements based on the human task, the AI Visibility guide cannot resolve this. Switch to [<u>'Information Design for Humans at Work</u>](https://citationlabs.com/operating-system/field-guides/information-design/)' to establish the human requirement first. Carry forward the established AI result, evidence state, and provenance.

### 6. BUILD THE TRACKED PROMPT SET

For each tracked prompt, preserve:

• exact wording;

• why it is included;

• provenance;

• demand evidence;

• work/decision evidence;

• required answer elements, if known;

• important context;

• competitors or alternatives, where relevant.

| **Prompt** | **Why included** | **Provenance** | **Demand evidence** | **Work / decision evidence** | **Required answer elements** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

This table belongs inside the **AI Visibility Plan + Readout**. It does not need another artifact name.

#### PILOT THE PROMPT WORDING

Before treating the tracked prompt set as fixed, run each candidate prompt in the answer environment you intend to measure.

Check whether the wording actually evokes the category, task, or decision the prompt is meant to probe. If a prompt produces an unrelated interpretation, revise it or remove it. A result from the wrong category cannot be treated as evidence that the intended category is absent.

Preserve the exact final wording and the reason each prompt remains in the set.

Keep natural buyer questions separate from deliberately instructed research conditions. Do not add instructions such as “cite your sources” to a natural buyer prompt simply to make the answer easier to inspect. If both conditions are useful, label and preserve them separately.

### 7. PRESERVE THE MEASUREMENT SETUP

Once baseline measurement begins, preserve the version of the tracked prompt set you actually measured.

Record:

• exact prompt text;

• prompts added or removed;

• platform/model/surface;

• repeat or sampling approach;

• important competitor or comparison settings;

• material changes and dates.

This does not mean the tracked prompt set can never change.

It means a changed measurement instrument should look changed in the record.

**WHAT TO DO** Version any setup change you would hesitate to compare directly with the old baseline.

## PART II - BASELINE THE ANSWER ENVIRONMENT

A baseline is more than the first number in a before/after chart.

It is the record of what the answer environment was doing **before you changed it**, under conditions specific enough that the later re-test makes sense.

If the baseline says only:

Visibility score: 42

then you may know that the score changed later, but not what actually changed or why.

#### PRESERVE THE TEST CONDITION AND ORIGINAL ANSWER

Before inspecting or following up on an answer, preserve the original test condition and result.

At minimum, record:

* exact prompt and tracked prompt-set version;
* purpose of the test;
* platform and available model identity;
* date;
* relevant account or personalization context;
* whether browsing or search was explicitly invoked;
* full initial answer, including surfaced links or citations;
* any missing, failed, or incomplete result.

Preserve the initial answer before asking follow-up questions or checking sources manually. A follow-up request for sources or a manual source check is a separate observation. Do not treat it as part of the original baseline answer.

A one-platform, low-effort pass can still be useful for exploration. Name that scope clearly in your tracking instrument (spreadsheets are perfect for your first pass through this). Do not assume it represents unfamiliar buyers, other accounts, or other platforms, or that it is automatically suitable as a later comparison baseline.

Where available, use an export or suitable measurement instrument to preserve the condition and result. The requirement is to preserve a re-testable record, not to use a particular tool.

### 8. RECORD ENOUGH TO RE-TEST

In addition to the test condition and original answer above, preserve the observations you expect to compare later:

• repeat or sampling approach;
 • competitors and aliases;
 • citations;
 • mentions;
 • recommendation state;
 • Accuracy / Framing;
 • answer adequacy, where required answer elements are known;
 • retrieval evidence, where observable;
 • known variation.

If the answer environment is variable, a single run may be only a snapshot. Use enough repetition to understand the variation that matters to the decision, and record the sampling approach rather than implying a universal run count.

#### BE CAREFUL WITH RETRIEVAL

Not every tool exposes the retrieval process.

Use:

**OBSERVED** - the instrument exposes evidence that the source was retrieved.

**INFERRED** - other evidence suggests retrieval, but you cannot observe it directly.

**UNKNOWN** - the available instrument cannot support the distinction.

**WHAT TO DO** Save enough information that someone revisiting the project six weeks later could understand what was measured without relying on memory. That is the baseline you want.

## PART III - DIAGNOSE THE GAP

Once you have a baseline, the next question is not:

How visible are we?

It is:

**What, specifically, is going wrong?**

A weak result can have several causes.

Your information may not be available in the source environment. It may be available but not retrieved. It may be retrieved but not cited. Your brand may be mentioned but not recommended. Or the answer may look favorable while getting an important condition wrong.

Those problems call for different interventions.

The purpose of diagnosis is to narrow the problem enough that you know what kind of change is worth testing.

### 9. CHECK THE SIX VISIBILITY ZONES SEPARATELY

These zones are not a funnel.

You will not always be able to observe all six.

| **Zone** | **Practical question** |
| --- | --- |
| Ranked / In-result | Is the relevant evidence available where the system might find it? |
| Retrieved | Do we have evidence that the system selected the source? |
| Cited | Is the source explicitly used or credited? |
| Mentioned | Is the relevant brand/product/entity named? |
| Recommended | When choices are compared, how is the brand treated? |
| Accuracy / Framing | Are important facts, conditions, and limits represented correctly? |

#### RANKED / IN-RESULT

Start upstream.

Here, Ranked / In-result means upstream discoverability - not simply a conventional organic rank position.

Is the needed information actually available and discoverable?

Problems may include:

• the evidence has never been published;

• the useful page is stale;

• the wrong page is canonical;

• technical access is poor;

• stronger competing sources dominate the result environment.

**WHAT TO DO** Establish whether a usable source exists before spending time diagnosing downstream behavior.

#### RETRIEVED

If the information is available, can you tell whether the system selected it?

Some instruments expose retrieval or read behavior. Many do not.

If you cannot see retrieval, keep it **UNKNOWN** or, where justified, **INFERRED**.

Do not turn “not cited” into “not retrieved.”

**Example**

Your technical page ranks for the relevant searches, but a process-level instrument repeatedly shows the system selecting two competitor sources instead.

That supports a retrieval diagnosis.

If you can see only the final answer and citations, it does not.

#### CITED

Now ask which sources are explicitly used.

A common citation gap looks like this:

Your page contains the relevant fact, but another source is repeatedly cited for it.

Inspect:

• clarity;

• proposition fit;

• currentness;

• authority;

• specificity;

• portability;

• whether the useful evidence is buried.

**WHAT TO DO** Compare the cited evidence with the evidence you expected the system to use. Ask what the cited source makes easier to establish. That answer can be more useful than “we need more links.”

#### MENTIONED

Citation and mention are separate.

An answer can cite your documentation without presenting your product as an option.

Or it can mention your brand while relying entirely on outside sources.

Ask:

• Is the brand present?

• Is it associated with the right use case?

• Which competitors appear instead?

• Does the product genuinely fit the situation?

#### RECOMMENDED

Mention does not mean recommendation.

When an answer compares choices, record enough detail to distinguish:

• included;

• qualified;

• “best for X”;

• explicitly preferred;

• explicitly ruled out.

Then inspect the criteria controlling the recommendation.

**WHAT TO DO** Determine whether the product actually meets those criteria and whether credible evidence of that fit exists.

Sometimes the correct finding is that the product should **not** be recommended for that prompt.

That is a useful diagnosis.

#### ACCURACY / FRAMING

Finally, ask whether the important facts and conditions are represented correctly.

Problems can include:

• old capabilities presented as current;

• versions combined incorrectly;

• conditional claims presented as universal;

• missing limitations;

• outdated third-party information;

• correct recommendation for the wrong reason.

**WHAT TO DO** Identify the consequential statement that is wrong or incomplete, then trace its supporting evidence as far as your tools allow.

Accuracy can be the problem even when every visibility metric looks healthy.

#### USE THE ZONES TO CHANGE WHAT YOU DO NEXT

Compare:

Our AI visibility is weak.

with:

Our product is mentioned regularly, but competing sources are cited for the technical criterion that appears to drive recommendation.

The second finding gives the team somewhere to work.

That is what diagnosis is for.

### 10. CHECK ANSWER ADEQUACY SEPARATELY

The six zones tell you what happened to a source, brand, product, or claim.

They do not tell you whether the answer was sufficient for the task.

If you know what the task requires, inspect those requirements directly.

| **Required element** | **Present?** | **Accurate?** | **Supported?** | **Conditions / limits?** | **Current?** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

A security answer may mention the product, cite the manufacturer, and recommend it while omitting a version limitation that determines whether the product can actually be approved.

That is an **answer-adequacy problem**.

**WHAT TO DO** Use this check only when you have a credible basis for defining the required elements. Do not derive the requirements from the AI answer itself.

### 11. FIND THE FIRST USEFUL POINT OF DIAGNOSIS

You do not need to investigate every possible mechanism.

Find the first point where the evidence changes what you would do.

**Not available upstream**
-> investigate availability, currentness, discoverability, source competition.

**Available but not retrieved**
-> where observable, inspect query decomposition and source selection.

**Retrieved but not cited**
-> inspect evidence quality, specificity, source suitability, proposition fit.

**Cited but not represented as expected**
-> inspect what the citation actually supports.

**Mentioned but not recommended**
-> inspect criteria, comparative evidence, and product fit.

**Recommended but wrong**
-> inspect version, conditions, limitations, and answer requirements.

### 12. INSPECT QUERY DECOMPOSITION WHERE AVAILABLE

Some answer systems or research instruments expose additional searches or subqueries.

Look for:

• recurring branches;

• technical terminology;

• standards;

• criteria;

• source types;

• authorities;

• missing evidence.

If a gateway-security prompt repeatedly causes the system to investigate:

certificate authentication
IEC 62443
firmware updates
offline operation

look at each branch separately.

Which sources appear?

Which sources are cited?

Do you have credible evidence for the criterion?

This can also produce useful human-research questions.

But the system’s subqueries are evidence about **machine behavior**, not proof that humans think about the problem in the same way.

### 13. INSPECT THE SOURCE ENVIRONMENT

AI answers are often assembled from an ecosystem of sources rather than one ranking.

Identify recurring:

• domains;

• URLs;

• competitors;

• publishers;

• communities;

• standards bodies;

• regulators;

• product documentation;

• technical references.

Where query decomposition is visible, inspect sources by branch.

**What to look for:**

• evidence that exists but is rarely used;

• evidence that does not exist publicly;

• authoritative sources that dominate particular criteria;

• contradictory versions of the same fact;

• competitors whose information is easier to verify.

This is often where an intervention becomes much more concrete.

### 14. USE ONLY AS MUCH RESOLUTION AS YOU NEED

Start broad.

The useful level is the one that can still change the intervention.

For example:

**Domain level:**

A competing domain is cited more frequently.

**Page level:**

One technical page accounts for most of the difference.

**Proposition level:**

One competing technical page states the exact claim, names the applicable version, and provides current supporting evidence. Your documentation spreads the same information across several pages.

At that point, the finer resolution changes the intervention.

Do not keep decomposing the problem merely because the data permit it. Diagnosis has done its job once the next intervention becomes materially clearer.

### 15. CHECK WHETHER THE MECHANISM CAN OPERATE

Before committing resources, make sure the intervention has a reasonable path to the effect you expect.

Ask:

• Is fresh retrieval relevant here?

• Can retrieval be observed?

• Does the system use the surface we plan to change?

• Is the claim actually true?

• Does the product fit the use case?

• Does credible evidence exist?

• Can it be published and maintained?

• Can you influence the relevant surface?

• Can the re-test detect a useful signal?

Then decide:

**TEST** - enough evidence to try a bounded intervention.

**MONITOR** - important, but no action justified yet.

**RESEARCH FIRST** - a key part of the diagnosis is still uncertain.

**MAINTAIN / DEFEND** - the current result is already strong.

**DO NOT PURSUE YET** - the likely value or mechanism does not justify the work.

A good diagnosis can end in **no AI-visibility intervention**.

For example, if the product lacks the capability that legitimately drives recommendation, the useful next step may belong to Product or Strategy.

## PART IV - CHOOSE THE INTERVENTION

At this point, resist jumping straight to a familiar tactic.

**LANE GUARD** This Part chooses an intervention for a diagnosed AI-answer-environment condition. It does not establish what people need information to enable or whether the change helps their work.

“Write more content.”

“Get links.”

“Do digital PR.”

“Improve GEO.”

Any of those might eventually be useful.

But the diagnosis should tell you **what needs to change and where** before you choose the implementation work.

### 16. DEFINE THE INTERVENTION FROM THE GAP

Record four things:

| **Field** | **Question** |
| --- | --- |
| Diagnosed gap | What is happening now? |
| Target surface | Where must something change? |
| Information / evidence change | What needs to become better? |
| Expected close-in effect | What should change first if it works? |

**EXAMPLE**

Diagnosis:

Product X is mentioned regularly, but competing sources are cited more consistently for version-specific security claims. Product X documentation makes version applicability difficult to verify.

Weak intervention:

Publish more security content.

Better intervention:

Consolidate the version-specific security evidence into a current authoritative resource that states the relevant claims, conditions, and limitations clearly.

Expected close-in effect:

The revised evidence is cited more consistently on the targeted security prompts, and version-specific answer accuracy improves.

Now the team knows both **what to build** and **what to measure afterward**.

### 17. CHOOSE THE SURFACE THAT MATCHES THE GAP

#### OWNED INFORMATION

Use when the problem is in your own evidence or documentation.

Possible work:

• correct stale information;

• consolidate conflicting pages;

• make important claims explicit;

• improve structure;

• clarify versions;

• repair technical access;

• create a reusable evidence resource.

#### THIRD-PARTY / PUBLISHER SOURCES

Use when important answers depend heavily on independent or external sources.

Possible work:

• correct inaccurate existing coverage;

• make verifiable evidence available to relevant publishers;

• earn appropriate comparison/reference inclusion;

• support independent research or documentation.

#### COMMUNITY / OPEN WEB

Use when practitioner discussion or lived experience materially influences the environment.

Possible work:

• credible expert participation;

• transparent correction;

• useful evidence supplied to real discussions.

#### DISTRIBUTED / SUPPORTING INFORMATION

This may include:

• partner resources;

• reseller documentation;

• implementation guides;

• public knowledge bases;

• standards/reference material;

• data feeds;

• maintained supporting resources.

**WHAT TO DO** Choose the surface the diagnosis points to. Do not distribute work everywhere merely because several channels are available.

### 18. INFORMATION ARCHITECTURE MAY BE THE INTERVENTION

Sometimes the information exists but the structure makes it difficult to use.

| **Problem** | **Possible intervention** |
| --- | --- |
| Conflicting product states | Consolidation and governance |
| Fragmented evidence | Governed evidence resource |
| Version ambiguity | Explicit product/version structure |
| Incompatible comparison data | Normalized comparison structure |

In these cases, another article may add to the problem.

If the deeper question becomes what information structure would best support human work, move into [<u>Information Design for Humans at Work</u>](https://citationlabs.com/operating-system/field-guides/information-design/).

#### WHEN AN AI ASSISTANT IS PART OF A PERSON'S INFORMATION PATH

An AI assistant may be an encounter environment inside a person's real task, not only a public visibility surface. When that matters, [<u>Information Design for Humans at Work</u>](https://citationlabs.com/operating-system/field-guides/information-design/) should establish what the person needs information to enable and what source, applicability, conditions, limits, and verification paths must survive AI mediation.

AI Visibility can then test the machine-facing part of that path: whether the relevant AI environment retrieves, cites, distinguishes, and accurately represents the governed evidence under the measured conditions.

Do not infer the human requirement from AI behavior alone.

**CALL INFORMATION DESIGN** AI Visibility can test the machine-facing path. Information Design owns the human requirement, the human-facing information gap, and the human-use test.

## PART V - DEFINE THE MEASUREMENT CONTRACT

This is the point where you decide what success would look like **before seeing the result**.

Without a measurement contract, it is easy to publish an intervention, watch several metrics move, and later choose whichever one looks favorable.

### 19. WRITE THE CONTRACT BEFORE THE INTERVENTION SHIPS

Record:

• baseline;

• intervention date/window;

• primary close-in measure;

• expected direction;

• expected magnitude, if there is a real basis;

• secondary/context measures;

• comparison;

• repeat/sampling approach;

• observation window;

• known lag;

• important concurrent changes.

**WHAT TO DO** Choose the measure closest to the intervention. If you changed citation evidence, citation may be the primary measure. If you corrected a version problem, Accuracy / Framing may matter more than overall visibility. If you targeted recommendation criteria, measure recommendation directly.

### 20. DEFINE THE RESULT PATTERNS BEFOREHAND

#### EXPECTED / SUPPORTIVE

The predicted movement appears under the planned conditions and the guardrail holds.

#### NO MEANINGFUL CHANGE / NULL

The expected movement does not meaningfully appear under the tested conditions.

A null result is not automatically a failure.

It tells you the expected effect was not observed under the conditions you tested.

#### CONTRADICTORY / COMPLICATING

Some observations weaken, redirect, or complicate the diagnosis or expected mechanism.

Examples:

• citation rises while accuracy falls;

• mention rises while recommendation declines;

• the treated prompts move no differently from untreated prompts;

• visibility rises while answer adequacy worsens.

#### ADVERSE / GUARDRAIL FAILURE

Something important becomes worse or the guardrail fails.

#### INCONCLUSIVE / INSUFFICIENT EVIDENCE

The measurement, comparison, or setup cannot answer the question with enough confidence for the decision.

**WHAT TO DO** Write these states before deployment so they can inform the next decision rather than being invented afterward.

### 21. USE A MEANINGFUL COMPARISON WHEN AVAILABLE

Before finalizing the measurement contract, choose the comparison that will make the result easier to interpret.

Start with the specific intervention and expected effect. Then list the comparisons that are feasible.

Possible comparisons include:

* unchanged prompts;
* similar untreated prompts;
* competitor movement;
* untreated assets or categories;
* prior intervention waves;
* historical periods;
* another platform or model.

Choose the comparison that bears most directly on the same question while remaining untreated or otherwise informative.

Record:

* why this comparison was selected;
* what it holds roughly constant;
* material differences between it and the treated condition;
* concurrent changes that could affect interpretation;
* what the comparison can and cannot help establish.

For example, if targeted prompts improve while similar untreated prompts remain stable, the intervention-specific explanation becomes more plausible. If both move together, a broader system change may be contributing.

If no credible comparison is available, record:

**No meaningful comparison available.**

Then limit the strength of the resulting claim accordingly.

Do not manufacture a control merely to complete the measurement contract. A useful comparison can reduce ambiguity, but it does not by itself establish causation.

### 22. KEEP A CHANGE LOG

Record anything during the observation window that could complicate interpretation:

• model updates;

• platform changes;

• prompt edits;

• site releases;

• product changes;

• PR activity;

• third-party updates;

• measurement changes;

• important competitor activity.

You do not need perfect control.

You need enough history to understand the result later.

## PART VI - RE-TEST AND INTERPRET

After the observation window, return to the tracked prompt set and measurement contract.

You are now trying to answer four questions:

**What changed?**

**What did not change?**

**Does the pattern fit the mechanism we expected?**

**What does the evidence justify doing next?**

### 23. RE-RUN THE TRACKED PROMPT SET

Use comparable conditions wherever practical.

Record differences in:

• prompt wording;

• platform/model;

• answer surface;

• sampling;

• instrumentation;

• important external conditions.

Capture the same observations you used at baseline.

If the setup changed materially, keep that visible rather than pretending the comparison is exact.

### 24. START WITH THE MEASURE YOU INTENDED TO CHANGE

This is why you wrote the measurement contract first.

If the intervention targeted citation, begin with citation.

If it targeted inaccurate product/version information, begin with Accuracy / Framing.

If it targeted retrieval and retrieval is observable, begin there.

Only then look outward to secondary measures.

**EXAMPLE**

Diagnosis:

Version-specific security evidence is difficult to use.

Intervention:

Publish clear governed version-specific evidence.

Result:

Citation rises and version accuracy improves. Recommendation remains unchanged.

That is a useful result.

The intervention appears to have affected what it was designed to change.

The unchanged recommendation is another finding, not proof that the intervention failed.

### 25. KEEP AN EXPECTED RESULT WITHIN ITS BOUNDARY

If the expected movement appears, record:

• what moved;

• where;

• how consistently;

• what the comparison did;

• other relevant changes;

• remaining uncertainty.

Then state only what the evidence supports.

For example:

Citation of the revised evidence increased and version representation improved on the targeted prompts.

That does not yet mean:

Buyers now prefer the product.

Those are different questions.

### 26. USE A NULL RESULT TO NARROW THE NEXT QUESTION

If the expected effect does not appear, investigate why before abandoning the work or declaring success elsewhere.

| **Check** | **Ask** |
| --- | --- |
| Exposure | Did the intervention reach the intended surface? |
| Execution | Was it completed as planned? |
| Mechanism | Was the expected mechanism active? |
| Information | Did you actually supply the missing evidence? |
| Structure | Was the information usable? |
| Timing | Was the observation window appropriate? |
| Variation | Is normal variation larger than the expected effect? |
| Measurement | Did you measure the right thing? |
| Diagnosis | Is the original explanation still plausible? |

A null result can be valuable because it narrows what remains plausible and points to the next diagnostic question.

### 27. KEEP CONTRADICTORY RESULTS VISIBLE

Different measures sometimes move in opposite directions.

For example:

Citation increased. Accuracy decreased.

or:

Mention improved. Recommendation worsened.

Do not average these into:

Visibility improved slightly.

The contradiction may reveal:

• an incomplete diagnosis;

• more than one mechanism;

• a tradeoff;

• a wider environmental change;

• weak measurement;

• or simply insufficient evidence.

The uncomfortable result can be the useful result.

### 28. USE THE COMPARISON TO IMPROVE THE READ

#### TREATED IMPROVES; COMPARISON DOES NOT

More consistent with an intervention-specific effect.

#### BOTH MOVE TOGETHER

A broader environmental change may matter.

#### TREATED HOLDS WHILE COMPARISON DECLINES

The intervention may have helped preserve position.

#### PLATFORMS DIFFER

Report the difference.

Do not average materially different behavior merely to make the readout simpler.

### 29. SEPARATE WHAT YOU SAW FROM WHY YOU THINK IT HAPPENED

Consider three statements:

**Observation**

The target source was cited in 11 of 20 re-test runs versus 4 of 20 baseline runs.

**Supported result**

Citation increased under the measured conditions.

**Interpretation**

The new evidence resource may have contributed by making the relevant claim easier to identify and reuse.

Those statements have different evidentiary strength.

Keep them separate.

### 30. REPORT WHAT DID NOT CHANGE

A bounded result is often more useful than a broad one.

For example:

Citation increased.
Version accuracy improved.
Recommendation did not materially change.
Broad category prompts showed little movement.

That tells the next practitioner much more than:

AI visibility improved.

### 31. END WITH THE STRONGEST SUPPORTED STATEMENT

At the end of the re-test, capture:

**Intervention**
What changed?

**Observed result**
What happened?

**Comparison/context**
What helps interpret it?

**Limits**
What remains untested?

**Next decision**
What does this result justify now?

Then update the **AI Visibility Plan + Readout**.

## PART VII - CARRY THE EVIDENCE FORWARD

Not every successful investigation needs another phase.

Continue only when an unresolved question matters to the next decision.

### 32. CARRY FORWARD THE RESULT, NOT A STRONGER CLAIM

Preserve:

• established result;

• evidence/provenance;

• important limitations;

• current hypothesis;

• reason for further work.

Example:

**Established**

Version-specific answer accuracy improved after the evidence intervention.

**Hypothesis**

Clearer evidence may reduce reconstruction work for security reviewers.

The first came from this investigation.

The second still needs evidence.

### 33. WHEN THE NEXT QUESTION IS ABOUT HUMAN WORK

Use [**<u>Information Design for Humans at Work</u>**](https://citationlabs.com/operating-system/field-guides/information-design/) when you need to know:

• what the person actually needs;

• which criteria matter;

• what a satisfactory answer requires;

• how the information is used;

• whether better information improves the task.

Carry forward what AI Visibility already established.

Do not restart the investigation from zero.

### 34. WHEN THE NEXT QUESTION IS DOWNSTREAM

Use [**<u>Tracing Business Impact Beyond the Click</u>**](https://citationlabs.com/operating-system/field-guides/business-impact/) when an established AI result raises a meaningful organizational question.

**CALL BUSINESS IMPACT** Call when a bounded AI result raises a consequential question about organizational work, burden, risk, capacity, customer economics, or another business result. Carry the intervention, baseline, result, comparison, limits, and downstream hypothesis.

Carry forward the intervention, baseline, result, comparison, limits, and downstream hypothesis.

Investigate that hypothesis rather than treating it as already proven.

#### PIVOT TO BUSINESS IMPACT

If your bounded result raises questions about organizational burden, capacity, or customer economics, the AI Visibility guide cannot resolve this. Switch to '[<u>Tracing Business Impact Beyond the Click</u>](https://citationlabs.com/operating-system/field-guides/business-impact/)' to trace that consequence. Carry forward the intervention, baseline, result, comparison, limits, and downstream hypothesis.

### 35. LET NEW EVIDENCE CHANGE THE ORIGINAL WORK

Later evidence may show that:

• a prompt matters less than expected;

• a low-volume criterion is decisive;

• answer requirements were incomplete;

• the original diagnosis was wrong;

• the effect stops before reaching a meaningful outcome.

Use that evidence.

You may change the prompt set, revise the diagnosis, test something else, monitor, or stop.

### 36. KEEP THE HANDOFF IN THE PLAN + READOUT

Record:

Established result

Evidence state

Evidence / provenance

Conditions / scope

Important limits / unknowns

Next uncertainty or working hypothesis

Next guide or specialist domain

Decision the next answer must help make

Why further work is justified

No separate handoff document is required.

## PART VIII - EVALUATING AI VISIBILITY MEASUREMENT TOOLS, AGENTS, AND MCPs

Use this section to judge whether a measurement tool can support the work above.

The central question is:

**What can this tool actually establish?**

### 37. DISTINGUISH OBSERVATION FROM TOOL LABELS

A platform may report:

• visibility;

• share of voice;

• citation share;

• brand presence;

• recommendation;

• sentiment;

• source influence.

Those labels can be useful.

Before relying on them, determine what underlying observation actually produces the metric.

For this guide, distinguish:

**direct observation**
**derived analysis**
**external coding**
**unavailable / unknown**

If a tool measures citations, use it confidently for citations.

Do not assume that automatically tells you retrieval.

### 38. CHECK THE TOOL AGAINST THE WORK YOU NEED TO DO

Ask whether it preserves:

#### TRACKED PROMPTS

• exact wording;

• stable IDs;

• grouping;

• history/versioning;

• provenance, or somewhere to attach it.

#### BASELINE + RE-TEST

• platform/model;

• run history;

• repeats;

• competitors;

• full responses;

• citations;

• mentions;

• source URLs/domains;

• historical comparison.

#### DIAGNOSIS

Which of these can it actually support?

• Ranked / In-result

• Retrieved

• Cited

• Mentioned

• Recommended

• Accuracy / Framing

• answer adequacy

#### INTERVENTION MEASUREMENT

Can you preserve:

• intervention dates;

• events;

• comparison groups;

• model changes;

• consistent historical exports?

**WHAT TO DO** Treat unsupported parts of the method as external work, not as reasons to force the nearest available metric into service.

### 39. PROGRAMMATIC ACCESS SHOULD MAKE THE DATA EASIER TO VERIFY

Useful API or MCP access should ideally provide:

• stable project/prompt IDs;

• exact prompt text;

• prompt history;

• explicit filters;

• raw responses;

• citation records;

• source URLs/domains;

• defined aggregates;

• events;

• pagination;

• record counts;

• consistent schemas.

Prior Citation Labs work comparing programmatic process-level analysis with manual XOFU exports identified these as practical requirements. In that work, machine-readable access reduced manual handling and made extraction completeness easier to verify.

An agent is most useful when it can move from a question to verifiable evidence without hiding how the answer was assembled.

*For current implementation details and verified capabilities, see* [*<u>the maintained technical reference</u>*](https://citationlabs.com/operating-system/field-guides/ai-visibility/)*.*

### 40. XOFU + THINKING INSPECTOR: CURRENT EXAMPLE

For the current XOFU + Thinking Inspector capability map, see the [<u>maintained technical reference</u>](https://citationlabs.com/operating-system/#reference).

Use that reference to determine which observations the current tools support directly, which require export or external analysis, and which remain unavailable or unknown.

Requirements or proposed-capability documents should not be treated as evidence that a function is currently available.

### 41. KEEP THE TOOL COMPARISON LIVING

Use consistent states:

**YES**
**PARTIAL**
**EXPORT / EXTERNAL**
**NO**
**UNKNOWN**
**PLANNED**

UNKNOWN is useful.

It means we have not yet established the capability.

The detailed vendor comparison should live outside this guide so it can be updated without rewriting the method.

### 42. CHOOSE THE TOOL FROM THE MEASUREMENT REQUIREMENT

A team measuring broad brand presence may prioritize scale.

A team diagnosing retrieval may prioritize process-level observability.

A team studying answer accuracy may prioritize raw response access.

A team using agents may prioritize complete programmatic access.

There is no requirement that one tool do everything.

There is a requirement that you know which evidence came from which instrument.

## PART IX - WORKED CASE: INDUSTRIAL GATEWAY SECURITY REVIEW

### FIRST LEG — THE ANSWER ENVIRONMENT

| **FIRST LEG** | **SECOND LEG** | **THIRD LEG** |
| --- | --- | --- |
| AI ANSWER ENVIRONMENT | HUMAN WORK | ORGANIZATIONAL CONSEQUENCE |
| **YOU ARE HERE** | **NOT YET ESTABLISHED** | **NOT YET ESTABLISHED** |

**CASE SPINE** This teaching case follows one possible route through the family. The guides do not require this order and can be used independently.

## INDUSTRIAL GATEWAY SECURITY REVIEW

This case is synthetic. It is not a client case or a description of a real product.

It shows how the decisions in the guide connect.

### 43. THE TEAM STARTS WITH A BROAD VISIBILITY CONCERN

A company selling industrial gateways notices that competitors appear more often in AI-assisted security comparisons.

The first temptation is obvious:

We need more AI visibility.

But that is not yet a diagnosis.

The team builds a tracked prompt set using several kinds of evidence.

| **Prompt** | **Why included** | **Evidence** |
| --- | --- | --- |
| industrial gateway security | Category question with established search demand | Keyword research |
| What are the most secure industrial gateways for regulated manufacturing? | Leadership wants the competitive answer monitored | Stakeholder |
| Does Product X support certificate-based authentication? | Known security-review criterion | Domain expert + customer-facing evidence |
| Can Product X continue operating without external connectivity? | Known deployment concern | Domain expert + customer-facing evidence |
| Product X IEC 62443 | Standards investigation | Search + domain expertise |
| Product X security documentation | Repeated need for authoritative evidence | Sales/support |

The team also knows that security reviewers may need version applicability, conditions, limitations, implementation requirements, and authoritative documentation.

That gives them something more useful than “Does Product X appear?”

They can also ask whether the answer contains what a real review requires.

### 44. THE BASELINE CHANGES THE QUESTION

Repeated measurement produces a more interesting picture.

Before inspecting the results further, the team preserves the exact prompts and prompt-set version, platform/model and date, relevant account and search conditions, and the full initial responses with their surfaced citations or links. Follow-up source checks are recorded separately from those original answers.

Product X is already mentioned fairly often.

So simple brand absence is not the main problem.

On technical prompts, however:

• competing and third-party sources are cited more consistently;

• owned evidence appears inconsistently where retrieval can be observed;

• product/version conditions are represented unevenly;

• important answer elements are sometimes missing;

• recommendation remains mixed.

The question shifts from:

How do we get mentioned more?

To:

Why does the answer environment have better usable evidence for some competitors and technical claims?

That is a much more actionable problem.

### 45. THE TEAM NARROWS THE DIAGNOSIS

They inspect relevant source environments and observable query decomposition.

The system repeatedly investigates questions around:

• certificates;

• IEC 62443;

• firmware updates;

• vulnerability handling;

• offline operation;

• security documentation.

The company does have relevant information.

But some of it is split across several documents, some is difficult to tie to the correct product version, and third-party technical sources state comparable claims more cleanly.

The working diagnosis becomes:

Version-specific security evidence exists, but it is fragmented and inconsistently represented. Competing or independent sources are easier for the answer environment to use for several important technical claims.

Recommendation remains a separate issue.

The team does not assume that fixing the evidence problem will automatically fix recommendation.

### 46. THE INTERVENTION FOLLOWS THE DIAGNOSIS

Instead of publishing another broad security article, the team creates a governed security evidence resource.

It makes explicit:

• product/version;

• authentication and certificates;

• updates;

• vulnerability handling;

• standards applicability;

• external-connectivity requirements;

• limitations;

• authoritative source;

• currentness.

Contradictory or obsolete information is reconciled.

Where independent coverage is appropriate, the same verifiable evidence can support relevant third-party sources.

The expected close-in result is deliberately narrow:

The revised evidence should be used or cited more consistently on the targeted technical prompts, and version-specific accuracy should improve.

### 47. THE TEAM WRITES THE MEASUREMENT CONTRACT

#### PRIMARY MEASURES

• use/citation of the relevant evidence;

• version-specific Accuracy / Framing;

• required answer elements.

#### SECONDARY MEASURES

• source-set changes;

• mention;

• recommendation;

• platform differences.

#### NULL

No meaningful change in evidence use or accuracy.

#### CONTRADICTORY

Citation improves but accuracy or answer adequacy worsens.

#### COMPARISON

The team uses similar untreated technical prompts where the underlying evidence was not changed. These prompts address comparable security questions but do not rely on the revised evidence resource.

If targeted prompts improve while the untreated prompts remain relatively stable, that pattern is more consistent with an intervention-specific effect. If both groups move together, a broader change in the answer environment may be contributing.

The comparison does not establish causation. Differences between prompts, platform behavior, and concurrent changes remain relevant limits.

The team records the publication date and other meaningful changes during the observation window.

Now the re-test has something specific to evaluate.

### 48. THE RE-TEST PRODUCES A BOUNDED RESULT

Assume the re-test finds:

• greater use/citation of the revised evidence;

• better version-specific accuracy;

• more complete answers on the targeted technical prompts;

• little change in recommendation;

• little movement on broad category prompts.

That pattern matters.

The targeted technical evidence measures improved under the re-test conditions.

It did not obviously affect recommendation.

So the result is not:

AI visibility improved.

It is:

Use of the targeted security evidence increased and product/version representation became more accurate under the measured conditions.

That is a useful result precisely because its boundary is clear.

### 49. THE NEXT QUESTION MAY BELONG SOMEWHERE ELSE

The team can now ask a new question:

Does this clearer evidence also help real security reviewers do their work?

That belongs in [**<u>Information Design for Humans at Work</u>**](https://citationlabs.com/operating-system/field-guides/information-design/).

If that human effect is established, a further question might be:

Does better security-review information reduce clarification, rework, delay, or unnecessary escalation?

That belongs in [**<u>Tracing Business Impact Beyond the Click</u>**](https://citationlabs.com/operating-system/field-guides/business-impact/).

Neither conclusion comes automatically from the AI result.

The AI Visibility work has done its job: it established a bounded change in the answer environment and supplied evidence worth carrying forward.

## PART X - METHODS, PRACTITIONER LINEAGE, AND SOURCES

The method in this guide draws from established work in search, information retrieval, information behavior, human-centered design, information quality, and evaluation.

It also reflects current practitioner research into AI search: how prompt sets are constructed, how answer systems find and cite sources, how probabilistic answers can be measured, and where common visibility metrics stop being reliable.

The sources below do not necessarily endorse this guide or use its terminology.

They are included so readers can see the work that informed it and distinguish established concepts from Citation Labs’ own applied instruments and findings. Current platform, vendor, and practitioner sources in this section were checked on 26 August 2026.

### 50. ESTABLISHED METHODOLOGICAL LINEAGES

#### SEARCH AND SEO PRACTICE

SEO contributes demand research, query and intent analysis, technical accessibility, indexing and ranking, competitive analysis, authority analysis, content evaluation, and repeated performance measurement.

AI search adds new observable conditions. It does not make those practices irrelevant.

The important evidence boundary is narrower:

**Search demand is evidence of search demand. It is not automatically evidence of AI-prompt frequency or human information need.**

Google continues to state that foundational SEO practices remain relevant to AI Overviews and AI Mode.

[Google Search Central - AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features)

#### INFORMATION RETRIEVAL AND INFORMATION NEED

Robert S. Taylor’s 1968 work on **question negotiation** distinguishes four levels at which an information need becomes articulated: visceral, conscious, formalized, and compromised.

Nicholas Belkin, Robert Oddy, and Helen Brooks’ **Anomalous State of Knowledge** work starts from the premise that an information need may not be precisely specifiable by the person experiencing it.

These traditions support a central boundary in this guide: a prompt is evidence. It should not automatically be treated as a complete representation of the underlying need.

[<u>Robert S. Taylor - Question-Negotiation and Information Seeking in Libraries</u>](https://crl.acrl.org/index.php/crl/article/view/12027)

[<u>Belkin, Oddy & Brooks - ASK for Information Retrieval, Part I</u>](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/ASK-FOR-INFORMATION-RETRIEVAL-PART-I/991031665289904646)

#### EVOLVING SEARCH AND INFORMATION FORAGING

Marcia Bates’s **berrypicking** model describes search as an evolving process in which the question can change and information is accumulated across several sources rather than retrieved through one perfect query.

Peter Pirolli and Stuart Card’s **information foraging** work examines how people seek, gather, and consume information in relation to the value and cost of finding it.

These models help explain why a real information problem should not automatically be reduced to one keyword, one prompt, or one source.

They do not establish that machine query decomposition is equivalent to human information seeking.

[<u>Marcia J. Bates - The Design of Browsing and Berrypicking Techniques for the Online Search Interface</u>](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html)

[<u>Pirolli & Card - Information Foraging (Psychological Review, 1999)</u>](https://doi.org/10.1037/0033-295X.106.4.643)

#### SENSE-MAKING AND CONTEXT

Brenda Dervin developed Sense-Making Methodology as an approach to studying human communication, information needs, seeking, and use in context. Her work has been influential in communication and information science.

For this guide, the relevant lesson is modest: when the question is what information matters to a person in a particular situation, evidence about that situation is required.

A deeper investigation belongs in [**<u>Information Design for Humans at Work</u>**](https://citationlabs.com/operating-system/field-guides/information-design/).

[<u>Brenda Dervin - What We Know About Information Seeking and Use</u>](https://journals.sagepub.com/doi/10.3233/ISU-230182)

#### HUMAN-CENTERED DESIGN

ISO 9241-210 describes human-centered design as a set of principles and activities applied across the life cycle of interactive systems.

The practical boundary for this guide is:

When you make a claim about whether an answer supports a person’s work, the evidence should come from the work context - not solely from AI-system behavior.

[<u>ISO 9241-210</u>](https://www.iso.org/standard/77520.html)

#### INFORMATION QUALITY

Richard Wang and Diane Strong’s work on data quality argues that quality is broader than accuracy alone and includes contextual, representational, and accessibility dimensions relevant to the person using the information.

That distinction is directly useful for **Accuracy / Framing** and answer adequacy.

An answer can contain individually accurate facts and still be poor for a task because important conditions are missing, the information is stale, distinctions have been collapsed, or the evidence is difficult to use.

[<u>Wang & Strong - Beyond Accuracy: What Data Quality Means to Data Consumers</u>](https://jmis-web.org/articles/1002)

#### PROGRAM EVALUATION AND EXPERIMENTAL DISCIPLINE

The measurement portions of this guide borrow ordinary evaluation practices: establish a baseline, specify the intervention and expected result, use comparisons where feasible, record competing explanations, interpret null results, and keep the claim consistent with the design.

The CDC’s 2024 Program Evaluation Framework is a useful accessible reference and presents evaluation as systematic evidence gathering for learning and decision-making rather than requiring one universal study design.

This guide does not require every intervention to become a formal experiment.

It does require the practitioner to distinguish:

**we observed a change**

from

**we established that our intervention caused it.**

[<u>CDC Program Evaluation Framework, 2024</u>](https://www.cdc.gov/mmwr/volumes/73/rr/rr7306a1.htm)

### 51. CURRENT AI SEARCH PRACTITIONER WORK

This is not an exhaustive history of AI-search practice.

It identifies current work that has materially informed, challenged, or paralleled parts of this guide.

#### MIKE KING / iPULLRANK

iPullRank’s **Relevance Engineering** work frames modern search as a multidisciplinary practice spanning information retrieval, user experience, artificial intelligence, content strategy, and digital PR, positioned as an evolution of SEO.

Recent iPullRank measurement work also argues for AI-specific measures rather than relying only on conventional search clicks, sessions, and rankings.

The overlap with this guide is particularly strong around retrieval mechanics, relevance, measurement, and the need to understand AI search as more than traditional ranking.

The frameworks are not identical.

[<u>iPullRank - Introduction to the Relevance Engineering Framework</u>](https://ipullrank.com/relevance-engineering-introduction)

[<u>iPullRank - From Clicks to Citations: New AI Search Measurement Metrics</u>](https://ipullrank.com/ai-search-measurement)

#### ALEYDA SOLIS

Aleyda Solis’s 2026 work on representative AI-search prompt libraries starts with the business question, emphasizes representative rather than exhaustive prompt sets, uses real audience language and constraints, preserves a stable core set for comparison, and connects measurement to action.

Her prompt-library framework also separates brand appearance, recommendation, citation, source environment, and accurate representation - several of the distinctions this guide treats diagnostically.

[<u>Aleyda Solis - How to Build a Representative AI Search Prompt Library</u>](https://www.aleydasolis.com/en/ai-search/ai-search-prompt-library/)

#### RAND FISHKIN, SPARKTORO, AND GUMSHOE

Rand Fishkin and the Gumshoe team tested the consistency of AI brand recommendations directly.

Their 2026 study used 600 volunteers, 12 prompts, three major AI environments, and 2,961 runs. It found very high variation in ordered recommendation lists but also found that appearance frequency across repeated runs could produce a more stable signal.

Gumshoe subsequently examined sample size and uncertainty more directly, treating brand appearance as a probability estimated across repeated observations.

This work is important because it challenges simplistic single-run rank tracking while still supporting repeated sampling when the measurement design warrants it.

[<u>SparkToro - AI Recommendation Consistency Research</u>](https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/)

[<u>Gumshoe - How Much Data Do You Need to Measure AI Visibility with Confidence?</u>](https://gumshoe.ai/blog/?p=7)

#### LILY RAY

Lily Ray’s 2026 analysis of B2B software queries provides a concrete example of why **citation and recommendation should remain separate measurements**.

The study found instances where Google AI Overviews cited a brand’s own comparison content while recommending competing products instead.

The important methodological point is:

**A citation is evidence of source use. It is not evidence that the cited brand won the recommendation.**

[<u>Search Engine Land - Lily Ray study on citation versus recommendation</u>](https://searchengineland.com/google-ai-overviews-cite-self-serving-listicles-recommend-competitors-480573)

#### KEVIN INDIG

Kevin Indig’s work has been particularly useful for understanding cross-engine variation.

In an Omnia dataset weighted toward European markets, Kevin Indig’s 2026 analysis of 3.7 million URL citations found very low cross-engine overlap across ChatGPT, Perplexity, and Google AI Overviews and argues against treating blended AI visibility as one leaderboard.

His broader work also examines the changing relationship among ranking, traffic, AI answers, trust, and influence rather than assuming that the click captures the complete search journey.

That supports this guide’s insistence on keeping platform and answer surface visible in the measurement record.

[<u>Kevin Indig - The Consensus Gap</u>](https://www.growth-memo.com/p/the-consensus-gap)

[<u>Kevin Indig - Beyond the SERP: Visibility Layer & Trust Stack</u>](https://www.kevin-indig.com/talks/beyond-the-serp-visibility-trust)

#### JAMES WIRTH AND CITATION LABS

James Wirth’s recent Citation Labs work has focused heavily on the measurement problem created when AI answers influence selection before the click.

That work separates mention, citation, recommendation, and downstream behavior and argues for measuring answer environments directly rather than treating traffic as a complete record of search influence.

Citation Labs’ 2026 work tracked 4,579 prompts over 12 weeks for one B2B enterprise client. As an applied precedent, it supports repeated runs and stable prompt sets rather than single screenshots; within that project, presence rates stabilized while ordering and cited URLs rotated.

Citation Labs’ work on third-party influence likewise distinguishes being cited as a source from being included or recommended in an answer.

These are direct applied predecessors of this guide.

The current method tightens several evidence boundaries beyond some earlier Citation Labs practice, particularly around prompt provenance, human information need, retrieval observability, and causal language.

[<u>James Wirth - Measuring AI Visibility When Google Answers Before the Click</u>](https://citationlabs.com/measuring-ai-visibility-when-google-answers-before-the-click/)

[<u>Citation Labs - Results From Tracking 4,579 Buyer Prompts</u>](https://citationlabs.com/measuring-ai-visibility-with-visibility-percent-and-recommendation-rank/)

[<u>Citation Labs - Measuring 3rd Party Influence on AI Answers</u>](https://citationlabs.com/measuring-3rd-party-influence-on-ai-answers/)

### 52. PROMPT-DEMAND METHODOLOGIES ARE NOT EQUIVALENT

There is no universal prompt-demand dataset equivalent to established keyword-volume systems.

Current providers use different evidence and modeling choices.

Ahrefs describes Brand Radar as combining a large search-keyword database, People Also Ask data, semantic fan-out, and repeated execution of questions across supported AI platforms. Its Estimated Impressions metric uses Google search volume as a weighting input, and Ahrefs describes that as a modeled visibility signal rather than measured AI audience reach.

Semrush’s current Prompt Research documentation describes a database of 317M+ AI queries and reports **AI Volume** as an estimated measure of AI search activity at the topic level.

These can both be useful.

They are not the same evidence.

Nor are they equivalent to a stakeholder request, a support ticket, observed first-party search behavior, customer research, or an analyst-created diagnostic prompt.

Record the provenance.

[<u>Ahrefs - Brand Radar Methodology</u>](https://ahrefs.com/blog/brand-radar-methodology/)

[<u>Semrush - Prompt Research Report</u>](https://www.semrush.com/kb/1597-prompt-research-report)

### 53. USE CURRENT PLATFORM DOCUMENTATION FOR PLATFORM-SPECIFIC CLAIMS

AI-search mechanics change quickly.

Where a platform documents its own behavior, check the current documentation before relying on old practitioner shorthand.

Google documents query fan-out as a set of concurrent, related queries generated to fetch additional relevant search results. Google Search Central also states that pages shown as supporting links in AI Overviews or AI Mode must be indexed and eligible to appear in Google Search with a snippet.

OpenAI’s current ChatGPT Search documentation states that web-search responses may include citations and a Sources view, that search may rewrite a request into one or more targeted queries, and that citations or search results can still be incomplete, outdated, or incorrect.

These are dated product descriptions.

Re-check them when the mechanism matters to an intervention.

[<u>Google Search Central - Optimizing for Generative AI Features</u>](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

[<u>Google Search Central - AI Features and Your Website</u>](https://developers.google.com/search/docs/appearance/ai-features)

[<u>OpenAI - Searching the Web with ChatGPT</u>](https://help.openai.com/en/articles/9237897-chatgpt-search)

### 54. CITATION LABS-SPECIFIC INSTRUMENTS

Citation Labs uses several working terms for recurring observations.

The terms do not imply that Citation Labs invented the underlying retrieval or evaluation concepts.

#### QUERY FAN-OUT / QFO ANALYSIS

**Examines:** observable machine-generated searches, subqueries, branches, and associated sources.

**Useful for:** identifying technical terminology, standards, criteria, source classes, and branches worth investigating.

**Boundary:** machine-generated subqueries describe machine behavior. They do not establish human prompt demand or human information need.

Google now publicly uses **query fan-out** for related behavior in AI Mode.

#### RETRIEVAL / READ / CITATION ANALYSIS

**Examines:** where instrumentation permits, whether evidence was available, retrieved or read, and ultimately cited.

**Useful for:** separating upstream availability from evidence-selection or citation problems.

**Boundary:** do not infer an internal state the instrument does not expose.

#### SOURCE-ENVIRONMENT ANALYSIS

**Examines:** recurring domains, URLs, publishers, authorities, competitors, and source types across a tracked prompt set.

**Useful for:** determining where the answer environment repeatedly finds evidence.

**Boundary:** recurrence does not by itself establish why a source was selected.

#### RETRIEVAL-INVOCATION ANALYSIS

**Examines:** whether fresh retrieval appears to be active for the measured prompt and surface.

**Useful for:** determining whether a retrieval-facing intervention has a plausible mechanism.

**Boundary:** use **OBSERVED, INFERRED, NOT OBSERVED, or UNKNOWN** according to the instrument.

#### REPEATED-RUN / CROSS-PLATFORM MEASUREMENT

**Examines:** how answer behavior varies across repeated runs, platforms, models, and time.

**Useful for:** distinguishing persistent patterns from single-output variation.

**Boundary:** keep platform-specific observations separate when the environments behave differently.

### 55. EVIDENCE STATES USED IN THIS GUIDE

The five evidence states are:

**OBSERVED / DOCUMENTED
Directly observed, measured, recorded, documented, or established through inspection.**

**MODELED / ESTIMATED
Produced through modeling, weighting, extrapolation, forecasting, or estimation.**

**INFERRED
A reasonable conclusion from evidence that was not directly observed.**

**HYPOTHESIS
A proposed explanation, requirement, mechanism, or expected effect that still needs evidence.**

**UNKNOWN
The available evidence does not support a stronger classification.**

Provenance remains separate.

For example:

**MODELED / ESTIMATED - Ahrefs Brand Radar**

is different from:

**OBSERVED / DOCUMENTED - support record**

and both differ from:

**INFERRED - analyst interpretation of repeated AI behavior**

The vocabulary matters less than preserving the distinction.

### 56. KEEP CURRENT SOURCES DATED

The foundational sources in this section are comparatively stable.

AI-search platforms, vendor methodologies, measurement products, APIs, MCPs, and practitioner findings are not.

Before relying on a current source operationally:

• check its date;

• check whether the method has changed;

• check whether the current product still exposes the same evidence;

• preserve the source used for the decision.

## APPENDIX - AI VISIBILITY PLAN + READOUT

Use one **AI Visibility Plan + Readout** for each bounded investigation or intervention.

Complete the plan before the intervention. Complete the readout after the observation window and re-test.

The artifact can live in a document, spreadsheet, database, or measurement system. Keep it understandable even when different parts of the evidence live in different tools.

Use **UNKNOWN** where the evidence does not support an answer.

### A. SCOPE + TRACKED PROMPT SET

**Investigation / project:**

**Owner:**

| **DECISION THIS INVESTIGATION MUST HELP MAKE** | What will someone decide differently depending on what we learn? |
| --- | --- |
| **OWNER OF THAT DECISION** |  |
| **WHEN THE ANSWER IS NEEDED, IF RELEVANT** |  |

**Scope:**

#### TRACKED PROMPTS

| **Prompt** | **Why included** | **Provenance** | **Demand evidence** | **Work / decision evidence** | **Required answer elements, if known** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

#### MEASUREMENT SETUP

**Tracked prompt set version:**

**Purpose of test:**

**Platform / model / surface:**

**Date / baseline period:**

**Account / personalization context:**

**Browsing / search explicitly invoked:**

**Repeat / sampling approach:**

**Competitors / aliases / important settings:**

**Original answer / result record location:**

**Missing, failed, or incomplete results:**

### B. BASELINE + DIAGNOSIS

| **Prompt / group** | **Ranked / In-result** | **Retrieved** | **Cited** | **Mentioned** | **Recommended** | **Accuracy / Framing** | **Adequacy** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

For retrieval, use **OBSERVED / INFERRED / UNKNOWN** where needed.

#### SOURCE ENVIRONMENT / IMPORTANT EVIDENCE

#### DIAGNOSIS

**Observed gap:**

**Evidence supporting it:**

**Important uncertainty:**

**Diagnosis statement:**

### C. INTERVENTION + MEASUREMENT CONTRACT

**Target surface:**

**Information / evidence change:**

**Intervention:**

**Owner / dependencies:**

**Primary close-in measure:**

| **EXPECTED / SUPPORTIVE** |  |
| --- | --- |
| **NO MEANINGFUL CHANGE / NULL** |  |
| **CONTRADICTORY / COMPLICATING** |  |
| **ADVERSE / GUARDRAIL FAILURE** |  |
| **INCONCLUSIVE / INSUFFICIENT EVIDENCE** |  |

**Comparison:**

**Why selected:**

**What it holds roughly constant:**

**Material differences from the treated condition:**

**Concurrent changes that may affect interpretation:**

**What this comparison can and cannot help establish:**

**Observation window / known lag:**

#### CHANGE LOG

| **Date** | **Change that could affect interpretation** |
| --- | --- |
|  |  |
|  |  |

### D. RE-TEST + INTERPRETATION

**Re-test period:**

**Material measurement changes from baseline:**

| **Measure** | **Baseline** | **Re-test** | **Change / comparison** |
| --- | --- | --- | --- |
| Primary close-in measure |  |  |  |
| Ranked / In-result |  |  |  |
| Retrieved |  |  |  |
| Cited |  |  |  |
| Mentioned |  |  |  |
| Recommended |  |  |  |
| Accuracy / Framing |  |  |  |
| Answer adequacy |  |  |  |

**What changed?**

**What did not?**

**Contradictory / complicating observations:**

**Adverse / guardrail failure:**

**Inconclusive / insufficient evidence:**

**Strongest supported statement:**

**Important limits:**

### E. NEXT DECISION + EVIDENCE TO CARRY FORWARD

#### NEXT DECISION

| [ ] Scale | [ ] Apply selectively |
| --- | --- |
| [ ] Repair and re-test | [ ] Rebaseline |
| [ ] Diagnose another condition | [ ] Monitor |
| [ ] Research first | [ ] Maintain / defend |
| [ ] Stop for now | [ ] Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

**Reason:**

#### EVIDENCE TO CARRY FORWARD — IF NEEDED

| **Originating guide / investigation:** |  |
| --- | --- |
| **Established result - preserve verbatim:** |  |
| **Evidence state:** |  |
| **Evidence / provenance:** |  |
| **Conditions / scope:** |  |
| **Important limits / unknowns:** |  |
| **Next uncertainty or working hypothesis:** |  |
| **Next guide or specialist domain:** | AI Visibility / Information Design / Business Impact / Product / Research / Operations / Finance / Legal / other |
| **Decision the next answer must help make:** |  |
| **Why further work is justified:** |  |

**HANDOFF RULE** A handoff begins a new question. It does not add another conclusion to the originating investigation. Copy the established result without rewriting it; enter the hypothesis as an uncertainty to investigate.

### F. FAMILY HANDOFF PACKET

Use this packet when moving an unresolved question to a sibling guide.

* **Established Result:** (The outcome you just achieved)
* **Evidence State:** (Observed/Inferred/Hypothesis)
* **Provenance:** (Where the evidence came from)
* **Important Limits:** (What was NOT tested)
* **Next Uncertainty:** (The specific hypothesis for the next guide to solve)

## ONE-PAGE READOUT

| **Decision:** | **Diagnosed gap:** |
| --- | --- |
| **Intervention:** | **Expected close-in effect:** |
| **Observed result:** | |
| **What did not change:** | |
| **Comparison / context:** | **Important limits:** |
| **Strongest supported statement:** | |
| **Next decision:** | |

## CLOSING

Choose prompts for a stated reason. Establish the baseline before changing anything. Diagnose the gap. Change the information or evidence that diagnosis points to. Specify the expected result, re-test, report what changed and what did not, and make the next decision at the level the evidence supports.

Investigate human-work and downstream consequences separately. If the evidence does not support a stronger conclusion, leave it there.
