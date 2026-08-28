# HI Assessment Report: LeapSpace

**Assessment Date:** 2026-08-28
**Method:** LLM-Only Baseline Assessment (single-LLM analysis of the Phase 1 knowledge-acquisition extraction sheet, evaluated against the CARE framework — Akata et al., 2020)

---

## 1. Executive Summary

LeapSpace achieves an overall HI Conformance score of **37.5%**, placing it at **HI Maturity Level 1 — Partial HI**. Across the eight assessed usage scenarios (S1–S8), none reach a full PASS: four scenarios (S1, S2, S3, S7) are rated WARNING and four (S4, S5, S6, S8) are rated FAIL due to at least one Critical gap each. Twenty-one discrete HI gaps were identified across the four CARE dimensions, with Adaptive gaps present in every single scenario — the system's most consistent and severe weakness.

Examined dimension by dimension, LeapSpace's strongest and weakest properties diverge sharply. Collaborative co-participation is genuinely strong wherever the extraction sheet describes multi-turn dialogue (departmental literature review, cross-domain onboarding, argument-testing, and corporate evidence verification), but drops to a shallower, one-directional "AI generates, human reviews" pattern in four scenarios (multidisciplinary synthesis, evidence-strength calibration, cross-disciplinary search, and funding matching), each scoring 50% conformance across the two respective dimensions. Responsible oversight is similarly bifurcated: where Claim Radar's support/contradict/mixed classification, mandatory citation enforcement, or a named human oversight role (the library/information-services manager in S8) is engaged, fairness and accountability are well evidenced; where the sheet offers only a generic reference to "citation/trust grounding," no scenario-specific fairness mechanism is described at all. Explainable capability follows the same pattern, scoring 37.5%: it is strongest exactly where Trust Card and Claim Radar are actively used within the scenario's own described interactions (S4, S7, S8), and essentially absent where those tools are only referenced in passing or not at all (S1, S2, S5, and most severely S6, where no explanation mechanism for funding matches is named anywhere in the sheet).

Adaptive is the system's defining weakness and the reason the overall score sits at Partial HI rather than Established HI. No scenario in the extraction sheet describes a mechanism by which LeapSpace learns or improves from accumulated human feedback over time, as CARE's Adaptive property requires. The feedback mechanisms documented are, at best, within-conversation follow-up loops that reset at the end of a session (S1, S2, S3, S7); at worst, they are explicitly denied ("None automatic; loop closed entirely by human judgment" in S4) or structurally precluded by design ("standing privacy/non-training guarantee" in S8). This is not necessarily a design flaw — for confidential corporate R&D data, refusing to train on user content is arguably the responsible choice — but it does mean that, as extracted, LeapSpace exhibits essentially no CARE-compliant Adaptive behavior anywhere in its documented usage.

Taken together, LeapSpace should be judged a system with strong, well-engineered point solutions for explainability and oversight (Trust Card, Claim Radar) that are inconsistently deployed across use cases, embedded in genuinely collaborative dialogue in roughly half of its scenarios, and built on essentially no system-level learning loop. The improvement potential is significant and concentrated: closing the Adaptive gap (even a privacy-preserving, non-content-based feedback channel) and extending the existing Trust Card/Claim Radar infrastructure uniformly to the four dimensionally weaker scenarios (S1, S2, S5, S6) would move LeapSpace from Partial HI toward Established HI without requiring fundamentally new capabilities — largely a matter of applying what the platform already does well in S3/S4/S7/S8 to the scenarios where it currently does not.

---

## 2. HI Conformance Overview

### 2.1 Overall Score

| Metric | Value |
|---|---|
| Overall HI Conformance | 37.5% |
| HI Maturity Level | Level 1 — Partial HI |
| Scenarios Assessed | 8 |
| Scenarios PASS | 0 (0%) |
| Scenarios WARNING | 4 (50%) |
| Scenarios FAIL | 4 (50%) |
| Total HI Gaps | 21 |

At Level 1 (Partial HI), LeapSpace demonstrates isolated, well-built CARE-aligned mechanisms (Trust Card, Claim Radar, neutral ranking, dialogic interaction) in specific scenarios, but lacks the consistent, system-wide adaptive-learning and fairness/explanation infrastructure needed for reliable, mature hybrid-intelligence operation across its full range of documented use cases.

### 2.2 CARE Dimension Analysis

| Dimension | Score | Interpretation |
|---|---|---|
| Collaborative | 50% | Half of scenarios (S1, S2, S7, S8) show genuine dialogic co-participation with multi-turn exchange; the remainder (S3, S4, S5, S6) are described only as the AI producing an artifact that the human reviews, a shallower form of joint execution. |
| Adaptive | 0% | No scenario in the extraction sheet provides evidence of the system learning or improving from human feedback over time. All documented feedback loops are session-bound, explicitly denied, or left undocumented. |
| Responsible | 50% | Where present (S3, S4, S5, S7), oversight and fairness mechanisms are concrete and well evidenced — contradiction classification, mandatory citation, publisher/discipline-neutral ranking. Where absent (S1, S2, S6, S8), only a generic trust reference or privacy/security control substitutes for a scenario-specific accountability or fairness mechanism. |
| Explainable | 37.5% | Passage-level attribution and claim classification are strongly evidenced in claim-verification-centric scenarios (S4, S7, S8) but are largely unevidenced in synthesis, onboarding, search, and funding-matching scenarios (S1, S2, S5, S6). |

### 2.3 Scenario Overview

| Scenario | Label | Status | Gaps |
|---|---|---|---|
| S1 | Departmental Literature Review Synthesis | WARNING | 3 |
| S2 | Cross-Domain Onboarding for Unfamiliar Research Areas | WARNING | 3 |
| S3 | Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature | WARNING | 3 |
| S4 | Evidence-Strength Calibration and Hallucination Mitigation | FAIL | 2 |
| S5 | Cross-Disciplinary Connection-Finding and Author/Collaborator Search | FAIL | 3 |
| S6 | Research-to-Funding Opportunity Matching | FAIL | 4 |
| S7 | AI-Assisted Argument Testing and Draft Strengthening | WARNING | 1 |
| S8 | Governed Evidence Verification for Corporate and Regulated R&D | FAIL | 2 |

---

## 3. Detailed Scenario Analysis

### S1 — Departmental Literature Review Synthesis

**Status:** WARNING · **HI Gaps:** 3

The scenario is genuinely collaborative — the sheet describes a multi-turn, iterative conversation between researcher and system — but the extraction sheet provides no scenario-specific evidence of persistent learning, named fairness oversight, or actively engaged explanation, leaving Adaptive, Responsible, and Explainable each substantially deficient.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 1 — Reactive | Interactions are described as a multi-turn conversation, but every AI action (summarizing, visualizing) is triggered by an explicit researcher query or follow-up; no AI-initiated contribution is described. |
| Adaptive | 1 — Reactive | "Iterative follow-up questioning within same conversation" is entirely human-initiated and does not persist past the ~5-exchange memory window. |
| Responsible | 1 — Reactive | No scenario-specific oversight mechanism is named beyond a generic Trust Card reference; the "which sources to foreground" decision carries no described bias check. |
| Explainable | 1 — Reactive | Trust Card is referenced only generically in Evaluation Metrics, not as an interaction actually used within this scenario's workflow. |

**G-S1-01 — No Persistent Learning Beyond Single Conversation**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Major | Learning/improvement through feedback loops over time |

*Gap Description:* The only documented feedback mechanism is "iterative follow-up questioning within same conversation," bounded by a ~5-exchange memory. There is no evidence the system retains or applies what it learns from one literature-review session to the next.

*Practical Impact:* A researcher who returns to update a literature review must re-establish context and preferences from scratch each session, reducing the efficiency gain the tool is meant to provide for an ongoing, recurring task.

*Recommendation: Persist Conversational Learning Across Sessions* — Add a cross-session memory/profile layer that retains researcher preferences, prior foregrounded sources, and follow-up patterns beyond the ~5-exchange window, feeding them back into future query interpretation. *Implementation:* Extend session memory into a persistent, per-user, human-reviewable research profile that biases future retrieval/ranking. *Priority:* Medium. *Expected HI Impact:* Literature reviews become progressively better tailored to the researcher's standing interests without repeated re-briefing.

**G-S1-02 — No Scenario-Specific Fairness/Oversight Mechanism for Source Foregrounding**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Major | Oversight, accountability, and fairness/bias-mitigation |

*Gap Description:* "Which sources to foreground" is an explicit decision point, but no bias-mitigation or coverage-check mechanism is described for it — Evaluation Metrics offer nothing beyond a generic citation reference.

*Practical Impact:* Course materials and comparisons to prior work risk being built on a narrow or skewed slice of the literature without any disclosed safeguard.

*Recommendation: Add Source-Foregrounding Fairness Check* — Introduce an explicit mechanism that flags concentration risk (over-reliance on a small set of publishers/authors) when the system recommends which sources to foreground. *Implementation:* Apply the "publisher/discipline-neutral" ranking logic already used in S5 to literature-review synthesis, surfaced to the user alongside the summary. *Priority:* Medium. *Expected HI Impact:* Reduces risk of biased or narrow literature reviews reaching course materials.

**G-S1-03 — Explainability Mechanism Not Actively Engaged in Literature Synthesis Workflow**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Major | AI clarifies and justifies decisions/recommendations to human partners |

*Gap Description:* Trust Card is mentioned only as a generic platform-wide reference in Evaluation Metrics; the scenario's own Interactions and Decision Points columns contain no description of the researcher actually consulting passage-level attribution during synthesis.

*Practical Impact:* Researchers evaluating methodology or comparing to prior work lack an in-workflow way to verify individual claims in the synthesized summary or report.

*Recommendation: Surface Trust Card Inline During Synthesis* — Actively present passage-level citation/confidence information within the literature-review conversation itself, not only as a background, generic reference. *Implementation:* Auto-attach Trust Card summaries to each claim in the generated summary/Deep Research report by default. *Priority:* Medium. *Expected HI Impact:* Researcher can verify synthesis claims without a separate escalation step.

---

### S2 — Cross-Domain Onboarding for Unfamiliar Research Areas

**Status:** WARNING · **HI Gaps:** 3

Multi-turn dialogue with explicit query refinement makes this a solidly collaborative scenario, and the AI's unprompted tailoring to experience level shows a degree of proactive adaptation within the session — but, as in S1, no cross-session learning, named oversight, or scenario-specific explanation is evidenced.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 2 — Proactive | The AI "tailor[s] response to experience level via contextual prompts" — an unprompted adaptation of behavior, on top of the described multi-turn dialogue and query refinement. |
| Adaptive | 2 — Proactive | The same experience-level tailoring is a proactive, unprompted adaptive behavior, even though it does not persist beyond the session. |
| Responsible | 1 — Reactive | No scenario-specific oversight or fairness mechanism is named for topic-synergy or collaboration-lead suggestions. |
| Explainable | 1 — Reactive | No Trust Card or reasoning-transparency element is described in this scenario's Interactions or Decision Points. |

**G-S2-01 — Follow-Up Loop Confined to Single Conversational Context**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Major | Learning/improvement through feedback loops over time |

*Gap Description:* Feedback Mechanisms is described only as a "follow-up-question loop within same conversational context." No evidence indicates that what a newcomer learns or asks in one onboarding session carries forward to later sessions.

*Practical Impact:* A researcher entering a new field repeatedly re-establishes their foundational understanding rather than building cumulatively across sessions.

*Recommendation: Extend Onboarding Follow-Up Loop Beyond the Session* — Retain a record of the topics/questions a newcomer explored so subsequent sessions build on established foundational understanding rather than restarting. *Implementation:* Persistent topic-progress tracker tied to the researcher's profile. *Priority:* Medium. *Expected HI Impact:* Faster re-onboarding and cumulative domain-building across sessions.

**G-S2-02 — No Named Oversight or Fairness Mechanism for Onboarding Queries**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Major | Oversight, accountability, and fairness/bias-mitigation |

*Gap Description:* Evaluation Metrics state only "general citation/trust grounding," with no scenario-specific fairness mechanism for the topic synergies, funding-alignment cues, or collaboration leads the system surfaces.

*Practical Impact:* Early-career decisions (which topic synergy to pursue, which collaboration lead to follow) may be shaped by unbalanced or undisclosed sourcing.

*Recommendation: Name an Oversight Mechanism for Onboarding Recommendations* — Define and expose a specific accountability/fairness mechanism for the topic synergies and collaboration leads surfaced to newcomers. *Implementation:* Reuse S5's neutral-ranking approach for onboarding topic/collaborator suggestions. *Priority:* Medium. *Expected HI Impact:* Newcomers receive balanced, disclosed sourcing when their career-shaping choices are informed by AI-surfaced leads.

**G-S2-03 — No Scenario-Specific Justification for Tailored/Adaptive Responses**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Major | AI clarifies and justifies decisions/recommendations to human partners |

*Gap Description:* The system tailors responses to an inferred experience level, but nothing in the sheet indicates this inference is disclosed or explained to the user, nor is any Trust Card-style justification described for the onboarding content itself.

*Practical Impact:* A newcomer cannot tell whether a simplified or advanced response reflects their actual level correctly, or verify the underlying claims used to onboard them.

*Recommendation: Justify Tailoring Decisions to the User* — When the system tailors its response to an inferred experience level, disclose that inference and let the user correct it. *Implementation:* Add an explicit "responding at [level] — adjust?" affordance tied to the contextual-prompt logic. *Priority:* Medium. *Expected HI Impact:* Builds calibrated trust in adaptive explanations rather than silent tailoring.

---

### S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature

**Status:** WARNING · **HI Gaps:** 3

This scenario has the strongest Responsible evidence in the entire sheet (Claim Radar's support/contradict/mixed classification), but its interaction pattern is closer to report review than dialogue, its feedback signal does not close a learning loop, and genuine-gap-versus-indexing-artifact disambiguation is left entirely to the human.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 1 — Reactive | Interactions are "researcher reviewing Deep Research report" and "clicking Claim Radar shield icon" — a query-then-review pattern, not a sustained dialogue. |
| Adaptive | 2 — Proactive | "Claim Radar signals when insufficient data exists, prompting question adjustment" is an unprompted, AI-initiated signal, even though it does not feed back into system improvement. |
| Responsible | 2 — Proactive | Support/contradict/mixed classification and gap surfacing are applied automatically to every query without being specifically requested. |
| Explainable | 2 — Proactive | Claim Radar's insufficient-data signal proactively clarifies why confidence should be limited, without waiting for the researcher to ask. |

**G-S3-01 — Interaction Pattern Limited to Report/Panel Review Rather Than Dialogue**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Collaborative | Minor | Joint co-participation of human and AI in interactions |

*Gap Description:* Interactions are described as the researcher reviewing a Deep Research report and clicking through Claim Radar tabs — a single-shot generate-then-review pattern rather than a back-and-forth exchange in which the AI and researcher jointly work the evidence.

*Practical Impact:* Researchers cannot easily interrogate a specific finding or ask the system to dig deeper on a flagged gap without leaving the review flow.

*Recommendation: Enable Dialogue Around Deep Research Reports* — Allow the researcher to question or contest specific findings in the report/Claim Radar tabs conversationally. *Implementation:* Attach a chat affordance to each report section/category tab. *Priority:* Low. *Expected HI Impact:* Turns passive report review into a joint exploration of gaps.

**G-S3-02 — Claim Radar Signal Does Not Close the Learning Loop**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Major | Learning/improvement through feedback loops over time |

*Gap Description:* Claim Radar signals insufficient data and the researcher adjusts the question, but nothing in the sheet indicates this adjustment pattern is captured or used to improve future insufficient-data detection.

*Practical Impact:* The system may repeatedly under- or over-flag insufficient evidence in the same subfield without ever calibrating against how researchers actually respond.

*Recommendation: Close the Claim Radar Feedback Loop* — Record question-adjustment sequences following insufficient-data signals and use them to refine Claim Radar's sufficiency thresholds over time. *Implementation:* Log adjustment sequences and route them into periodic threshold recalibration. *Priority:* Medium. *Expected HI Impact:* Fewer false insufficient-data signals over time, better-calibrated gap detection.

**G-S3-03 — No Explicit Disambiguation Between Genuine Gap and Indexing Artifact**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Minor | AI clarifies and justifies decisions/recommendations to human partners |

*Gap Description:* The decision point "whether an evidence gap is a genuine opportunity or an indexing artifact" is left entirely to human judgment; Claim Radar signals insufficiency but does not explain which of the two explanations is more likely.

*Practical Impact:* A nonprofit science officer or researcher may mistake a database-coverage limitation for a genuine, fundable research gap, or vice versa.

*Recommendation: Distinguish Genuine Gaps from Indexing Artifacts* — Have Claim Radar/Deep Research explicitly flag whether a low-evidence result is more likely a true research gap or a coverage limitation. *Implementation:* Add a coverage-confidence indicator alongside the support/contradict/mixed classification. *Priority:* Low. *Expected HI Impact:* Reduces researcher misinterpretation of indexing limitations as scientific gaps.

---

### S4 — Evidence-Strength Calibration and Hallucination Mitigation

**Status:** FAIL · **HI Gaps:** 2

Explainability and Responsible oversight are the best-evidenced properties in the entire sheet for this scenario — passage-level attribution, reasoning-step transparency, mandatory citation, and an explicit Trust Card→Claim Radar escalation path — but the interaction is fundamentally review-based, and the Feedback Mechanisms field explicitly states there is no automatic loop at all.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 1 — Reactive | "Researcher-Trust Card UI review; researcher-Claim Radar panel review" describes the human consuming a static AI-generated artifact, not a negotiated exchange. |
| Adaptive | 1 — Reactive | Capped by the Critical gap below; the sheet states explicitly there is no automatic feedback loop. |
| Responsible | 3 — Social | Mandatory citation is automatic for every claim, and the design provides an escalation/repair path (Trust Card insufficient → escalate to Claim Radar) that is sustained across the verification process. |
| Explainable | 3 — Social | Passage-level attribution and reasoning-step tracing are automatic per claim, with the same escalation path providing a repair mechanism when initial explanation is insufficient. |

**G-S4-01 — One-Directional Review Pattern; No Described Dialogue Around Claim**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Collaborative | Minor | Joint co-participation of human and AI in interactions |

*Gap Description:* Human Tasks are entirely review/inspection verbs ("review," "inspect," "trace," "escalate"); the AI generates the Trust Card/Claim Radar content once and the researcher consumes it, with no described conversational exchange about the specific claim.

*Practical Impact:* A researcher who disagrees with or wants to probe a confidence rating has no described way to interrogate the system about that specific claim.

*Recommendation: Add Conversational Follow-Up to Trust Card/Claim Radar Review* — Let the researcher ask the system direct questions about a specific citation or confidence rating instead of only reading the static panel. *Implementation:* Embed a claim-specific chat entry point in the Trust Card/Claim Radar UI. *Priority:* Low. *Expected HI Impact:* Converts one-directional verification into a joint claim-checking dialogue.

**G-S4-02 — Explicitly No Automatic Feedback Loop**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Critical | Learning/improvement through feedback loops over time |

*Gap Description:* Feedback Mechanisms states plainly: "None automatic; loop closed entirely by human judgment reviewing Trust Card/Claim Radar evidence." This is the most explicit statement in the entire sheet that no learning mechanism exists for a given scenario.

*Practical Impact:* The researcher's accept/qualify/discard judgment — arguably the single most valuable hallucination-detection signal in the platform — is discarded rather than used to improve future claim-confidence calibration.

*Recommendation: Introduce an Opt-In Feedback Signal on Claim Judgments* — Capture the researcher's accept/qualify/discard decision as a structured signal that can improve future Trust Card confidence calibration, while preserving the human-in-the-loop guarantee. *Implementation:* Add a lightweight accept/qualify/discard control whose aggregate, anonymized outcomes feed a periodic calibration review, without altering the "human closes the loop" guarantee. *Priority:* High. *Expected HI Impact:* Transforms an entirely open-loop verification process into one that improves hallucination detection over time.

---

### S5 — Cross-Disciplinary Connection-Finding and Author/Collaborator Search

**Status:** FAIL · **HI Gaps:** 3

The "publisher/discipline-neutral" ranking is a genuine, well-evidenced fairness mechanism, but the interaction is review-only, no rationale is given for why a specific connection or author was surfaced, and no feedback mechanism is documented beyond a vague reference to "iterative querying."

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 1 — Reactive | "Researcher reviewing ranked results list; researcher reviewing author profile results" — a query-then-browse pattern with no described refinement dialogue. |
| Adaptive | 1 — Reactive | Capped by the Critical gap below; Feedback Mechanisms is undocumented beyond a vague reference. |
| Responsible | 2 — Proactive | "Publisher/discipline-neutral" ranking is applied automatically to every search, without the user needing to request fairness. |
| Explainable | 1 — Reactive | No Trust Card, rationale, or match-explanation mechanism is described anywhere in the scenario. |

**G-S5-01 — Review-Only Interaction with Ranked/Author Results**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Collaborative | Minor | Joint co-participation of human and AI in interactions |

*Gap Description:* The researcher queries once and then reviews a ranked list or author profiles; no iterative negotiation of the search itself is described.

*Practical Impact:* Refining toward a genuinely useful "non-obvious" connection or the right collaborator likely requires several separate, disconnected queries rather than a guided exchange.

*Recommendation: Add Refinement Dialogue to Search Results* — Let researchers refine ranked/author results conversationally ("show more like this," "why is this ranked here"). *Implementation:* Attach a query-refinement chat layer to the results view. *Priority:* Low. *Expected HI Impact:* More targeted collaborator/connection discovery.

**G-S5-02 — No Named Explanation Mechanism for Ranking or Match Rationale**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Major | AI clarifies and justifies decisions/recommendations to human partners |

*Gap Description:* Evaluation Metrics describe ranking criteria ("relevance ranking with small recency boost") but nothing in the sheet indicates this rationale is actually communicated to the researcher for a given result — no Trust Card or per-result justification is mentioned anywhere in the scenario.

*Practical Impact:* Since the goal is surfacing "non-obvious" cross-disciplinary connections, researchers have no way to judge whether a surfaced match is credible before investing time in outreach.

*Recommendation: Explain Why a Result Was Matched* — Provide a per-result rationale (which keyword/semantic signals or which discipline-bridging path produced the match) rather than only a ranking score. *Implementation:* Surface the hybrid keyword+vector match factors as a short explanation attached to each result. *Priority:* Medium. *Expected HI Impact:* Researchers can judge whether a non-obvious connection is credible before pursuing outreach.

**G-S5-03 — Feedback Mechanism Undocumented Beyond Vague Iterative-Query Pattern**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Critical | Learning/improvement through feedback loops over time |

*Gap Description:* Feedback Mechanisms is recorded as "not explicitly described beyond general iterative-query pattern" — the weakest, vaguest evidence of any feedback mechanism in the sheet, with no indication that outreach outcomes or relevance judgments ever reach the ranking system.

*Practical Impact:* The search does not improve at surfacing genuinely useful collaborators or connections as it is used, no matter how many researchers act (or don't act) on its suggestions.

*Recommendation: Document and Implement a Search Feedback Loop* — Define an explicit mechanism that feeds outreach/click signals back into relevance ranking over time. *Implementation:* Track which surfaced collaborators/connections researchers act on and use this to adjust the relevance-ranking model periodically. *Priority:* High. *Expected HI Impact:* Cross-disciplinary matching improves in precision as usage accumulates.

---

### S6 — Research-to-Funding Opportunity Matching

**Status:** FAIL · **HI Gaps:** 4

This is the weakest scenario in the sheet — it carries the lowest confidence rating (Medium) and has no named mechanism at all for three of the four CARE dimensions. Only Collaborative-adjacent search-and-review structure and the general goal of surfacing "lesser-known grants" provide any grounding.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 1 — Reactive | "Researcher reviewing Find Funding filtered results list; researcher reviewing funder eligibility pages" — search-then-browse, no dialogue described. |
| Adaptive | 1 — Reactive | Capped by the Critical gap below; Feedback Mechanisms is recorded as "not explicitly described." |
| Responsible | 1 — Reactive | Capped by the Major gap below; the only equity-adjacent signal is the goal statement "including lesser-known grants," with no disclosed mechanism. |
| Explainable | 1 — Reactive | Capped by the Critical gap below; no explanation mechanism is named anywhere in the row. |

**G-S6-01 — Review-Only Interaction with Funding Results and Eligibility Pages**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Collaborative | Minor | Joint co-participation of human and AI in interactions |

*Gap Description:* Interactions are limited to the researcher reviewing a filtered results list and funder eligibility pages; no conversational refinement of the funding search is described.

*Practical Impact:* Research-office staff preparing grant applications must manually re-filter rather than iteratively narrow the search with the system.

*Recommendation: Add Interactive Filtering Dialogue to Find Funding* — Let users refine funding searches conversationally ("only grants with early-career eligibility," "exclude X funder") instead of only reviewing a filtered list. *Implementation:* Add conversational filter refinement to the Find Funding interface. *Priority:* Low. *Expected HI Impact:* More precisely targeted funding shortlists.

**G-S6-02 — No Fairness/Accountability Mechanism for Funding Matching**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Major | Oversight, accountability, and fairness/bias-mitigation |

*Gap Description:* Beyond the goal of matching "including lesser-known grants," no disclosed or auditable mechanism ensures the database search/filter doesn't systematically favor prominent funders; unlike S5's explicit "publisher/discipline-neutral" ranking statement, S6 has no equivalent disclosed control.

*Practical Impact:* Researchers at less-resourced institutions may be systematically underserved if lesser-known-grant coverage is only an aspiration rather than a verified, measured property of the matching algorithm.

*Recommendation: Add an Accountability/Coverage Mechanism to Funding Matching* — Make the "lesser-known grants" coverage goal an auditable, disclosed mechanism (e.g., show what share of results are lesser-known vs. major funders). *Implementation:* Add a coverage/diversity indicator to Find Funding results, mirroring S5's neutral-ranking disclosure. *Priority:* Medium. *Expected HI Impact:* Research offices can verify the tool isn't systematically favoring well-resourced funders.

**G-S6-03 — No Explanation Mechanism Named at All for Funding Matches**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Critical | AI clarifies and justifies decisions/recommendations to human partners |

*Gap Description:* Evaluation Metrics for this scenario reads simply "not explicitly named (matching/filtering task)" — the only scenario in the sheet with zero explainability evidence of any kind, not even a generic citation/trust reference.

*Practical Impact:* Researchers and grant-office staff cannot tell why a particular grant was matched to their research direction, undermining confidence in pursuing lesser-known or unfamiliar funders specifically.

*Recommendation: Introduce a Funding-Match Rationale* — Provide an explicit reason for each funding match (topic overlap, eligibility fit, geography). *Implementation:* Extend the Trust Card/citation-style rationale pattern used elsewhere in LeapSpace to Find Funding matches. *Priority:* High. *Expected HI Impact:* Researchers and funding-office staff can justify match selections to grant committees and avoid pursuing poorly-fitting opportunities.

**G-S6-04 — No Feedback Mechanism Described**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Critical | Learning/improvement through feedback loops over time |

*Gap Description:* Feedback Mechanisms is recorded flatly as "not explicitly described" — no within-session loop, no cross-session mechanism, nothing.

*Practical Impact:* The matching quality (including the stated goal of surfacing lesser-known grants) cannot improve based on which matches researchers actually pursue or find eligible.

*Recommendation: Define a Funding-Matching Feedback Mechanism* — Establish and document a feedback loop since none currently exists. *Implementation:* Let users mark matched opportunities as pursued/irrelevant and use this to refine future ranking. *Priority:* High. *Expected HI Impact:* Matching precision and lesser-known-grant surfacing improve as the tool is used.

---

### S7 — AI-Assisted Argument Testing and Draft Strengthening

**Status:** WARNING · **HI Gaps:** 1

This is the most CARE-consistent scenario in the sheet: a sustained "challenge" dialogue, literature-grounded fact-checking reusing the Trust Card mechanism, and a clearly retained human decision point. Only Adaptive is deficient, and it is deficient in the same pattern as S1/S2/S3 — a within-session loop that does not persist.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | "Multi-turn 'challenge' dialogue" in which the AI actively tests and surfaces missing evidence is sustained, iterative co-construction of a stronger draft, not a single query-response exchange. |
| Adaptive | 1 — Reactive | Capped by the Major gap below; "iterative dialogue loop itself is the feedback mechanism," entirely human-initiated per turn. |
| Responsible | 1 — Reactive | "Private, secure drafting environment grounded exclusively in peer-reviewed/Scopus-indexed literature" is a static, always-on constraint rather than a demonstrated proactive or sustained oversight behavior. |
| Explainable | 3 — Social | Reasoning is tested and missing evidence surfaced repeatedly across the challenge dialogue, reusing the Trust Card mechanism — a sustained, repaired justification process across multiple turns. |

**G-S7-01 — Feedback Loop Limited to Within-Dialogue Iteration**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Major | Learning/improvement through feedback loops over time |

*Gap Description:* Feedback Mechanisms states "iterative dialogue loop itself is the feedback mechanism" — real and functioning within a single drafting session, but with no evidence it carries over to a researcher's next paper, proposal, or thesis chapter.

*Practical Impact:* A researcher who repeatedly makes the same class of argumentative or evidentiary error across multiple drafts gets no benefit from the Writing Coach having seen this pattern before.

*Recommendation: Persist Draft-Strengthening Patterns Across Sessions* — Retain recurring argument weaknesses or evidence gaps identified across a researcher's drafting sessions so the Writing Coach anticipates similar issues in future drafts. *Implementation:* Maintain a per-user pattern log of previously surfaced gap types, referenced in later challenge dialogues. *Priority:* Medium. *Expected HI Impact:* The Writing Coach becomes progressively more attuned to an individual researcher's argumentative blind spots.

---

### S8 — Governed Evidence Verification for Corporate and Regulated R&D

**Status:** FAIL · **HI Gaps:** 2

Explainability (Trust Card/citation-traceability) and most of Responsible (encryption, non-retention, a dedicated library-manager oversight role) are well evidenced. The scenario fails solely because its privacy-protective, non-training design — appropriate for IP protection — leaves Adaptive completely unaddressed, and fairness/bias-mitigation specifically is not named alongside the strong privacy/accountability controls.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 1 — Reactive | "Conversational interrogation" and a named "platform support role" indicate real engagement, but every described action is triggered by an explicit scientist query or upload. |
| Adaptive | 1 — Reactive | Capped by the Critical gap below; the standing non-training guarantee explicitly precludes learning from this data. |
| Responsible | 3 — Social | The library/information-services manager provides a sustained, institutional human oversight role, combined with an always-on audit trail (Trust Card) and enterprise-grade non-retention — a co-constructed, ongoing governance relationship rather than a one-off check. |
| Explainable | 2 — Proactive | Traceable-citation audit trail is generated automatically for every summary/comparison, without being specifically requested. |

**G-S8-01 — Fairness/Bias-Mitigation Not Named Alongside Privacy/Accountability Controls**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Minor | Oversight, accountability, and fairness/bias-mitigation |

*Gap Description:* Capabilities and Context describe enterprise-grade encryption, data non-retention, and IP protection in detail, and accountability is covered by the audit trail and library-manager role — but no mechanism specifically addresses fairness or one-sided evidence presentation in Compare Experiments tables or Reading Assistant summaries.

*Practical Impact:* A regulated R&D decision could rely on a comparison table or summary that is technically well-governed for privacy but not explicitly checked for balanced, non-cherry-picked evidence presentation.

*Recommendation: Name a Fairness/Bias-Mitigation Mechanism for Regulated R&D Use* — Alongside encryption, non-retention, and audit-trail controls, specify how comparison tables and article summaries are checked for one-sided or biased evidence presentation. *Implementation:* Apply the Claim Radar support/contradict/mixed classification (already used in S3/S4) to Compare Experiments outputs. *Priority:* Low. *Expected HI Impact:* Strengthens regulatory defensibility of AI-assisted R&D evidence summaries.

**G-S8-02 — Non-Training/Non-Retention Guarantee Precludes System Learning**

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Critical | Learning/improvement through feedback loops over time |

*Gap Description:* Feedback Mechanisms states "not explicitly described beyond standing privacy/non-training guarantee." The non-training guarantee, while a defensible and likely necessary IP-protection measure, means the system is explicitly designed not to learn from this scenario's interactions at all.

*Practical Impact:* Regulated R&D users get none of the compounding benefit of a system that improves with use, and this is the only scenario where the Adaptive gap stems from a deliberate design constraint rather than an unaddressed one — meaning it requires a fundamentally different kind of fix.

*Recommendation: Offer an Opt-In, IP-Safe Improvement Channel* — Since the non-training guarantee (rightly, for IP protection) prevents the system from learning from proprietary content, provide an alternative, non-proprietary feedback channel so the platform can still improve without compromising confidentiality. *Implementation:* Aggregate de-identified interaction-quality signals (not document content) across enterprise tenants for platform-level model improvement. *Priority:* High. *Expected HI Impact:* Preserves IP protection while closing the current total absence of adaptive learning in regulated environments.

---

## 4. Consolidated Recommendations

### Collaborative

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Enable Dialogue Around Deep Research Reports | Low | S3 | Allow the researcher to question or contest specific findings conversationally rather than only reviewing them. | Attach a chat affordance to each report section/category tab. |
| Add Conversational Follow-Up to Trust Card/Claim Radar Review | Low | S4 | Let the researcher ask the system direct questions about a specific citation or confidence rating. | Embed a claim-specific chat entry point in the Trust Card/Claim Radar UI. |
| Add Refinement Dialogue to Search Results | Low | S5 | Let researchers refine ranked/author results conversationally. | Attach a query-refinement chat layer to the results view. |
| Add Interactive Filtering Dialogue to Find Funding | Low | S6 | Let users refine funding searches conversationally instead of only reviewing a filtered list. | Add conversational filter refinement to the Find Funding interface. |

### Adaptive

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Persist Conversational Learning Across Sessions | Medium | S1 | Retain researcher preferences and follow-up patterns beyond the ~5-exchange window. | Extend session memory into a persistent, per-user, human-reviewable research profile. |
| Extend Onboarding Follow-Up Loop Beyond the Session | Medium | S2 | Retain a record of topics/questions explored so future sessions build cumulatively. | Persistent topic-progress tracker tied to the researcher's profile. |
| Close the Claim Radar Feedback Loop | Medium | S3 | Use question-adjustment patterns following insufficient-data signals to improve future flagging. | Log adjustment sequences and route into periodic threshold recalibration. |
| Introduce an Opt-In Feedback Signal on Claim Judgments | High | S4 | Capture accept/qualify/discard decisions as a structured signal for Trust Card calibration while preserving human-in-the-loop control. | Add an accept/qualify/discard control feeding an aggregate, anonymized calibration review. |
| Document and Implement a Search Feedback Loop | High | S5 | Feed outreach/click signals back into relevance ranking over time. | Track acted-upon results and use them to periodically adjust the ranking model. |
| Define a Funding-Matching Feedback Mechanism | High | S6 | Establish a feedback loop since none currently exists. | Let users mark matched opportunities as pursued/irrelevant to refine future ranking. |
| Persist Draft-Strengthening Patterns Across Sessions | Medium | S7 | Retain recurring argument weaknesses across a researcher's drafting sessions. | Maintain a per-user pattern log referenced in later challenge dialogues. |
| Offer an Opt-In, IP-Safe Improvement Channel | High | S8 | Provide a non-proprietary feedback channel that preserves the non-training/IP guarantee. | Aggregate de-identified interaction-quality signals across tenants for platform-level improvement. |

### Responsible

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Add Source-Foregrounding Fairness Check | Medium | S1 | Flag concentration risk when recommending which sources to foreground. | Apply S5's publisher/discipline-neutral ranking logic to literature-review synthesis. |
| Name an Oversight Mechanism for Onboarding Recommendations | Medium | S2 | Define an accountability/fairness mechanism for topic-synergy and collaboration-lead suggestions. | Reuse S5's neutral-ranking approach for onboarding suggestions. |
| Add an Accountability/Coverage Mechanism to Funding Matching | Medium | S6 | Make the "lesser-known grants" goal an auditable, disclosed mechanism. | Add a coverage/diversity indicator to Find Funding results. |
| Name a Fairness/Bias-Mitigation Mechanism for Regulated R&D Use | Low | S8 | Specify how comparison tables/summaries are checked for one-sided evidence presentation. | Apply Claim Radar's support/contradict/mixed classification to Compare Experiments outputs. |

### Explainable

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Surface Trust Card Inline During Synthesis | Medium | S1 | Actively present passage-level citation/confidence information within the review conversation. | Auto-attach Trust Card summaries to each claim in the generated summary/report. |
| Justify Tailoring Decisions to the User | Medium | S2 | Disclose the inferred experience level driving response tailoring. | Add a "responding at [level] — adjust?" affordance. |
| Distinguish Genuine Gaps from Indexing Artifacts | Low | S3 | Flag whether low-evidence results reflect a true gap or a coverage limitation. | Add a coverage-confidence indicator alongside support/contradict/mixed classification. |
| Explain Why a Result Was Matched | Medium | S5 | Provide a per-result rationale rather than only a ranking score. | Surface hybrid keyword+vector match factors as a short per-result explanation. |
| Introduce a Funding-Match Rationale | High | S6 | Provide an explicit reason for each funding match. | Extend the Trust Card/citation-style rationale pattern to Find Funding matches. |

---

## 5. HI Maturity Assessment

**Maturity Level: Level 1 — Partial HI.** LeapSpace exhibits fragments of CARE-conformant behavior — most notably concentrated in its Trust Card and Claim Radar infrastructure — but these are not applied consistently across its documented usage scenarios, and no scenario provides evidence of the system-level learning that Adaptive requires. This places LeapSpace above a purely automated Pre-HI tool, but well short of an Established HI system in which all four CARE properties are reliably present across use cases.

| Dimension | Score | Status |
|---|---|---|
| Collaborative | 50% | Needs Work |
| Adaptive | 0% | Needs Work |
| Responsible | 50% | Needs Work |
| Explainable | 37.5% | Needs Work |

**Strengths**
- Genuine multi-turn, dialogic collaboration in scenarios centered on conversation (S1, S2, S7, S8), including AI-initiated challenge and unprompted tailoring behavior.
- A well-evidenced, reusable explainability core (Trust Card passage-level attribution, mandatory citation, Claim Radar support/contradict/mixed classification) that performs strongly wherever it is actively engaged (S3, S4, S7, S8).
- Concrete, disclosed fairness design in at least one scenario — S5's "publisher/discipline-neutral" ranking is the clearest bias-mitigation statement in the sheet.
- A named, sustained human-oversight role (library/information-services manager) embedded directly into the regulated R&D workflow (S8), alongside enterprise-grade privacy and non-retention controls.
- An explicit escalation/repair pathway from Trust Card to Claim Radar (S4) when a first level of explanation or confidence is insufficient.

**Areas for Improvement**
- No scenario documents a mechanism by which LeapSpace learns from accumulated human feedback over time; this is the single largest and most consistent gap in the assessment (0% Adaptive conformance, gaps present in all eight scenarios).
- Fairness/oversight mechanisms are not consistently named across scenarios that involve comparable decision points (S1, S2, S6, S8 lack what S3, S4, S5 have).
- Explainability infrastructure that clearly exists on the platform (Trust Card, citation grounding) is not consistently surfaced within the interactions described for search, onboarding, synthesis, and funding-matching scenarios.
- Four scenarios (S3–S6) describe interaction only as generate-then-review rather than sustained dialogue, limiting collaborative depth even where no critical gap exists.
- The one scenario where Adaptive is absent by deliberate design (S8, for IP protection) needs a fundamentally different remedy — a privacy-preserving feedback channel — rather than simply "add more feedback."

---

## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)

### 6.1 Per-Scenario CARE Levels

| Scenario | Collaborative | Adaptive | Responsible | Explainable |
|---|---|---|---|---|
| S1 | 1 — Reactive | 1 — Reactive | 1 — Reactive | 1 — Reactive |
| S2 | 2 — Proactive | 2 — Proactive | 1 — Reactive | 1 — Reactive |
| S3 | 1 — Reactive | 2 — Proactive | 2 — Proactive | 2 — Proactive |
| S4 | 1 — Reactive | 1 — Reactive | 3 — Social | 3 — Social |
| S5 | 1 — Reactive | 1 — Reactive | 2 — Proactive | 1 — Reactive |
| S6 | 1 — Reactive | 1 — Reactive | 1 — Reactive | 1 — Reactive |
| S7 | 3 — Social | 1 — Reactive | 1 — Reactive | 3 — Social |
| S8 | 1 — Reactive | 1 — Reactive | 3 — Social | 2 — Proactive |

### 6.2 Use-Case CARE Maturity Summary

**Collaborative**

| Level | Scenarios at this level | Count |
|---|---|---|
| 1 — Reactive | S1, S3, S4, S5, S6, S8 | 6 |
| 2 — Proactive | S2 | 1 |
| 3 — Social | S7 | 1 |

Modal level: **1 — Reactive**

**Adaptive**

| Level | Scenarios at this level | Count |
|---|---|---|
| 1 — Reactive | S1, S4, S5, S6, S7, S8 | 6 |
| 2 — Proactive | S2, S3 | 2 |
| 3 — Social | — | 0 |

Modal level: **1 — Reactive**

**Responsible**

| Level | Scenarios at this level | Count |
|---|---|---|
| 1 — Reactive | S1, S2, S6, S7 | 4 |
| 2 — Proactive | S3, S5 | 2 |
| 3 — Social | S4, S8 | 2 |

Modal level: **1 — Reactive**

**Explainable**

| Level | Scenarios at this level | Count |
|---|---|---|
| 1 — Reactive | S1, S2, S5, S6 | 4 |
| 2 — Proactive | S3, S8 | 2 |
| 3 — Social | S4, S7 | 2 |

Modal level: **1 — Reactive**

Across all four CARE dimensions, Reactive is the modal capability level, indicating that even where a CARE property is not formally "gapped," the underlying capability is most often exercised only upon explicit human instruction rather than proactively initiated or socially sustained by the AI.

---

## 7. Methodology

This report was produced by a single large language model, working directly and exclusively from the Phase 1 knowledge-acquisition extraction sheet for LeapSpace (S1–S8, 18 columns per row). No knowledge graph was constructed, no ontology alignment was performed, and no formal constraint validation (e.g., SHACL shape checking) was applied; this is accordingly labeled an LLM-Only Baseline Assessment, intended as a first-pass reference point against which more rigorous, tool-assisted or multi-rater assessments can later be compared. All findings, gaps, and recommendations are grounded strictly in the sheet's own column content (Human/AI Agents, Tasks, Interactions, Decision Points, Feedback Mechanisms, Evaluation Metrics, and the sheet's own HI Characteristics tags); no outside knowledge of LeapSpace as a product was introduced, and no capability, agent, or mechanism not stated in the sheet was assumed to exist.

**Scoring conventions applied:**
- Per-scenario score: PASS = 1.0, WARNING = 0.75, FAIL = 0.0.
- Overall HI Conformance = mean of the eight per-scenario scores, expressed as a percentage (3.0 / 8 = 37.5%).
- CARE dimension score = proportion of scenarios with no gap in that dimension, expressed as a percentage.
- HI Maturity Level: ≥90% Level 4 (Exemplary HI); ≥70% Level 3 (Established HI); ≥50% Level 2 (Emerging HI); ≥25% Level 1 (Partial HI); otherwise Level 0 (Pre-HI). LeapSpace's 37.5% overall score places it at Level 1.
- Scenario status: a scenario with at least one Critical gap is FAIL; a scenario with only Minor/Major concerns and no Critical gap is WARNING; a scenario with no gaps is PASS.
- Gap severity: Critical = a core CARE requirement is absent (e.g., no feedback mechanism at all, no fairness mechanism at all); Major = a requirement is present but substantially deficient (e.g., a feedback loop that does not persist beyond a single session); Minor = a small deficiency (e.g., a review-only interaction pattern where dialogue is otherwise the platform norm).
- CARE capability level per scenario per dimension: 1 (Reactive) = capability exercised only upon explicit instruction; 2 (Proactive) = AI initiates or anticipates without explicit prompting; 3 (Social) = capability sustained, repaired, or co-constructed over time with the human partner. The maximum admissible level per dimension per scenario is capped by that dimension's most severe identified gap in that scenario (Critical → cap 1; Major → cap 2; Minor/none → uncapped at 3); within the cap, the level was chosen conservatively (lower) wherever the sheet's evidence was silent on AI-initiated or sustained behavior.
- Aggregation across scenarios used counts and modal (most frequent) level per dimension, not averaging, since the capability scale is ordinal.
