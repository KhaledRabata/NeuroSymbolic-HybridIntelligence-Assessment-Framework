# Hybrid Intelligence Scenarios — LeapSpace by Elsevier

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **LeapSpace (Elsevier)**
Eight standardised Hybrid Intelligence (HI) scenarios, each evidence-backed per RAS Section 15/16 (File 4). Every scenario is either explicitly documented or strongly supported by ≥2 independent sources; where a detail is Inferred rather than Observed, it is explicitly labelled with reasoning, supporting evidence, and confidence.

Evidence IDs (E-0xx) correspond to `sources.md`. Ontology class references correspond to `hiontology.ttl` and are elaborated in `ontology_mapping.md`.

---

## Scenario 1 — Literature Review & Staying Current

**Scenario Name:** Departmental Literature Review Synthesis

**Description:** A researcher uses LeapSpace to update a departmental or personal literature review by processing large volumes of recent scholarly output, generating summarized responses or full Deep Research reports, and visualizing findings as tables or flowcharts, addressing the challenge that "more than 5.14 million academic articles [were] published in 2024" alone. [Observed — E-010]

**Goal:** Keep a literature review current and comprehensive despite rapidly growing publication volume. [Observed — E-010]

**Human Actors:**
- Academic researcher / faculty member conducting the review [Observed — E-010]
- Course instructor designing course materials from the review output [Observed — E-010]

**Artificial Agents:**
- LeapSpace conversational summarization engine (Standard mode) [Observed — E-001, E-013]
- Deep Research report generator [Observed — E-001, E-010]

**Context:** Academic setting with a rapidly growing, high-volume scholarly literature base (7,000+ publishers indexed). [Observed — E-010]

**Input Data:** Natural-language research query; optionally uploaded prior review drafts (PDF/DOCX/TXT/CSV). [Observed — E-013, E-010]

**Knowledge Sources:** Abstracts and full text from 7,000+ publishers via Scopus and Elsevier full-text corpus (18–20+ million articles/books). [Observed — E-003, E-010]

**Processing Method:** Retrieval over the indexed corpus followed by LLM-based summarization or agentic Deep Research synthesis. [Observed — E-005, E-010]

**Processing Tasks:**
1. Formulate natural-language literature-review query [Observed — E-010]
2. Process abstracts across publishers [Observed — E-010]
3. Generate summary response or full Deep Research report [Observed — E-010]
4. Visualize findings as tables or flowcharts [Observed — E-010]
5. Compare results to previous/prior work [Observed — E-010]

**Interaction Points:** Researcher ↔ LeapSpace multi-turn conversation (system retains ~5 prior exchanges of context). [Observed — E-013]

**Outputs:** Identification of latest research; comparison to previous work; course-material design input; methodology evaluation. [Observed — E-010]

**Evaluation Metrics:** Not separately named for this specific workflow beyond the general Trust Card/citation mechanism (see Scenario 4); output quality is implicitly judged by the researcher via cited-source review. [Observed — E-001; cross-reference E-007]

**Required Capabilities:** Large-scale literature retrieval, summarization, tabular/flowchart visualization. [Observed — E-010]

**Decision Points:** Whether the synthesized review is comprehensive enough to finalize; which sources to foreground in the written review. [Inferred — Medium confidence; reasoning: the source states the review-writing outcome but does not describe an explicit accept/reject decision step, though one is implied by any literature-review-writing process]

**Feedback Mechanisms:** Iterative follow-up questioning within the same conversation to refine or expand the review. [Observed — E-013]

**Expected HI Characteristics (CARE):** Collaborative (researcher steers scope, AI processes volume); Responsible (citation-grounded, per Responsible AI Principle 3, Transparency — E-014); Adaptive (iterative refinement via follow-up questions). [Observed — E-010, E-013, E-014]

**Evidence IDs:** E-001, E-003, E-005, E-007, E-010, E-013, E-014

---

## Scenario 2 — Exploring a New Research Topic or Field

**Scenario Name:** Cross-Domain Onboarding for Unfamiliar Research Areas

**Description:** A researcher transitioning into an unfamiliar field (e.g., a PhD student pivoting topics, or a domain expert entering an adjacent discipline) uses LeapSpace's natural-language search — requiring no Boolean query syntax — to receive responses tailored to their stated experience level, leveraging the observation that "more than 60% of searches on Scopus alone are linked to learning about new topics." [Observed — E-010]

**Goal:** Rapidly build foundational understanding of a new research area without prior domain expertise. [Observed — E-010]

**Human Actors:**
- Researcher/PhD student entering a new field [Observed — E-010]

**Artificial Agents:**
- LeapSpace natural-language query interpreter and response engine [Observed — E-010, E-013]

**Context:** Cross-disciplinary or early-career research setting where domain vocabulary is not yet fluent. [Observed — E-010]

**Input Data:** Natural-language question, phrased "in whatever wording and language feels natural" to the user. [Observed — E-013]

**Knowledge Sources:** Full corpus (Scopus abstracts + full text). [Observed — E-001]

**Processing Method:** Natural-language understanding with automatic query refinement/translation/error-correction; response calibrated to stated or inferred experience level. [Observed — E-010, E-013]

**Processing Tasks:**
1. Submit natural-language question about the new field [Observed — E-013]
2. System interprets intent and formulates search strategy automatically [Observed — E-013]
3. Response tailored to experience level via contextual prompts [Observed — E-010]
4. Researcher asks follow-up questions to deepen understanding [Observed — E-013]

**Interaction Points:** Multi-turn natural-language dialogue; refinement of an initial broad question (e.g., "How does brain activity differ in ADHD vs autism?") into a more targeted one (e.g., "How can we use brain activity to improve diagnostic accuracy?"). [Observed — E-013]

**Outputs:** Sparked research ideas; identified topic synergies; alignment for funding applications; new collaboration leads. [Observed — E-010]

**Evaluation Metrics:** Not explicitly named beyond general citation/trust grounding. [Observed — E-001]

**Required Capabilities:** Natural-language query interpretation, experience-level-adaptive response generation. [Observed — E-010, E-013]

**Decision Points:** Whether to pursue the newly discovered topic synergy or collaboration lead. [Inferred — Medium confidence; reasoning: the source lists these as outputs/outcomes but does not describe the decision process explicitly]

**Feedback Mechanisms:** Follow-up-question loop within the same conversational context. [Observed — E-013]

**Expected HI Characteristics (CARE):** Collaborative (human states level of unfamiliarity, AI adapts response depth); Adaptive (experience-level tailoring). [Observed — E-010]

**Evidence IDs:** E-001, E-010, E-013

---

## Scenario 3 — Evidence Synthesis and Gap Identification via Deep Research

**Scenario Name:** Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature

**Description:** A researcher examining a complex, multidisciplinary question — including in evidence-sparse domains such as rare-disease research — uses Deep Research (considering up to 300 sources) combined with Claim Radar to identify supporting and contradicting evidence, and can upload their own PDFs, DOCX, TXT, or CSV files for blended analysis alongside the published literature, in order to expose "the negative space — where fields overlap but understanding has yet to catch up." [Observed — E-010]

**Goal:** Synthesize scattered, multidisciplinary evidence and surface previously unrecognized research gaps. [Observed — E-010]

**Human Actors:**
- Researcher examining a complex/multidisciplinary question [Observed — E-010]
- Nonprofit/foundation Chief Science Officer conducting rare-disease evidence review (named example) [Observed — E-006]

**Artificial Agents:**
- Deep Research agentic synthesis engine (up to 300 sources) [Observed — E-010]
- Claim Radar evaluation engine [Observed — E-007, E-010]

**Context:** Multidisciplinary or evidence-sparse research domains (e.g., rare disease, where published evidence volume is inherently limited). [Observed — E-006, E-010]

**Input Data:** Research question; optionally uploaded personal documents (PDF/DOCX/TXT/CSV). [Observed — E-010]

**Knowledge Sources:** Full Scopus/Elsevier corpus plus user-uploaded documents, blended in a single analysis. [Observed — E-010]

**Processing Method:** Agentic multi-source retrieval and synthesis (up to 300 sources) combined with claim-level support/contradict/mixed classification. [Observed — E-007, E-010]

**Processing Tasks:**
1. Pose complex/multidisciplinary research question [Observed — E-010]
2. Run Deep Research across up to 300 sources [Observed — E-010]
3. Upload and blend personal documents into the analysis [Observed — E-010]
4. Run Claim Radar on key claims to identify support/contradiction [Observed — E-007]
5. Review synthesized report for patterns, contradictions, and evidence gaps [Observed — E-001]

**Interaction Points:** Researcher ↔ Deep Research report (reading/reviewing); researcher ↔ Claim Radar panel (clicking the shield icon next to a claim, reviewing category tabs). [Observed — E-007]

**Outputs:** Confirmed key articles; identified supporting/contradicting evidence; located "growth areas" (gaps); refined research questions; for the rare-disease example, stated "confidence in the accuracy and rigor of its outputs." [Observed — E-006, E-010]

**Evaluation Metrics:** Support/Contradict/Mixed source-classification counts (Claim Radar); source count considered (up to 40 for Claim Radar, up to 300 for Deep Research). [Observed — E-007, E-010]

**Required Capabilities:** Multi-source agentic synthesis, claim-level evidence classification, blended internal/external document analysis. [Observed — E-007, E-010]

**Decision Points:** Whether an apparent "evidence gap" represents a genuine research opportunity or an artifact of incomplete indexing; how to weight contradicting sources. [Inferred — Medium confidence; reasoning: Claim Radar surfaces the contradiction data (Observed) but the interpretive decision is necessarily left to the human researcher, consistent with Responsible AI Principle 4's "human accountability" (E-014), though this specific decision point is not spelled out verbatim in any source]

**Feedback Mechanisms:** Claim Radar explicitly signals when "insufficient data exists," prompting the researcher to broaden or adjust the question. [Observed — E-007]

**Expected HI Characteristics (CARE):** Collaborative (AI surfaces the evidence landscape, human interprets significance); Explainable (category tabs, key insights); Responsible (explicit low-data warning rather than false confidence). [Observed — E-007, E-010]

**Evidence IDs:** E-001, E-006, E-007, E-010, E-014

---

## Scenario 4 — Claim Validation via Trust Cards and Claim Radar

**Scenario Name:** Evidence-Strength Calibration and Hallucination Mitigation

**Description:** A researcher evaluating research integrity or calibrating the strength of a specific claim uses Trust Cards to see claim-to-source alignment (including, per later product updates, "the exact passage used to support a claim") and reviews confidence-level paragraphs and the system's reasoning steps, with the explicit design guarantee that "when LeapSpace does make a claim or assertion, at least one reference is always required." [Observed — E-009, E-010]

**Goal:** Reduce the risk of relying on an unsupported or hallucinated AI claim, and build calibrated confidence in cited evidence. [Observed — E-010]

**Human Actors:**
- Researcher validating a specific claim or assertion [Observed — E-010]

**Artificial Agents:**
- Trust Card generator (claim-to-source alignment engine) [Observed — E-001, E-007, E-009]
- Claim Radar (research-level context engine) [Observed — E-007]

**Context:** Any research task where AI-generated content must be checked against primary literature before being relied upon (general AI-trust concern named explicitly by Elsevier as a design driver). [Observed — E-001]

**Input Data:** A specific AI-generated claim/assertion produced during any other LeapSpace task. [Observed — E-010]

**Knowledge Sources:** The specific cited source(s) underlying the claim; the broader Scopus-indexed literature for Claim Radar's contextualization. [Observed — E-007, E-009]

**Processing Method:** Passage-level source attribution (Trust Cards) plus multi-source support/contradict/mixed aggregation (Claim Radar). [Observed — E-007, E-009]

**Processing Tasks:**
1. Review a generated claim's Trust Card [Observed — E-001, E-009]
2. Inspect the exact cited passage supporting the claim [Observed — E-009]
3. Review the confidence-level paragraph [Observed — E-010]
4. Trace the system's reasoning steps ("real-time visibility into the steps used to generate an answer") [Observed — E-001]
5. Optionally escalate to Claim Radar for broader literature context [Observed — E-007]

**Interaction Points:** Researcher ↔ Trust Card UI element (per-claim); researcher ↔ Claim Radar panel. [Observed — E-007, E-009]

**Outputs:** Reduced source-evaluation time; increased citation confidence; identified potential hallucinations. [Observed — E-010]

**Evaluation Metrics:** Mandatory-citation guarantee (≥1 reference per claim); claim-to-passage alignment; support/contradict/mixed classification. [Observed — E-009, E-010]

**Required Capabilities:** Passage-level source attribution, reasoning-step transparency, mandatory citation enforcement. [Observed — E-001, E-009, E-010]

**Decision Points:** Whether to accept, qualify, or discard a specific AI-generated claim before using it in the researcher's own work. [Observed — implied directly by the stated outcome "identified potential hallucinations" — E-010]

**Feedback Mechanisms:** None described as automatic; the loop is closed entirely by human judgment reviewing the Trust Card/Claim Radar evidence — this is the scenario where the platform's stated design philosophy ("reinforce — not replace — human research judgment," E-008) is most directly instantiated. [Observed — E-008]

**Expected HI Characteristics (CARE):** Explainable (this is the platform's flagship explainability mechanism); Responsible (mandatory citation, hallucination mitigation); Collaborative (AI proposes, human verifies and decides). [Observed — E-001, E-008, E-009, E-010, E-014]

**Evidence IDs:** E-001, E-007, E-008, E-009, E-010, E-014

---

## Scenario 5 — Cross-Disciplinary Discovery and Collaborator Identification

**Scenario Name:** Cross-Disciplinary Connection-Finding and Author/Collaborator Search

**Description:** A researcher seeking to bridge research fields or find cross-disciplinary connections uses LeapSpace's blended keyword-and-semantic (vector) search — which spans 330+ disciplines via Scopus — including to identify relevant collaborators, mentors, and topic contributors through the Author Search feature. [Observed — E-001, E-010]

**Goal:** Discover non-obvious cross-disciplinary connections and identify potential collaborators aligned with a research direction. [Observed — E-001, E-010]

**Human Actors:**
- Researcher seeking cross-disciplinary connections or collaborators [Observed — E-010]

**Artificial Agents:**
- Hybrid keyword + semantic (vector) search engine [Observed — E-010]
- Author Search / collaborator-identification engine [Observed — E-001]

**Context:** Multidisciplinary research spanning 330+ disciplines and 7,000+ publishers. [Observed — E-010]

**Input Data:** Research topic/question; author or field-of-interest query. [Observed — E-010]

**Knowledge Sources:** Scopus author/publication index (330+ disciplines). [Observed — E-010]

**Processing Method:** Blended keyword and semantic (vector) search, ranked by relevance with a small recency boost, applied both to publications and to author identification. [Observed — E-008, E-010]

**Processing Tasks:**
1. Query for cross-disciplinary literature connections [Observed — E-010]
2. Blend keyword and vector search to surface non-obvious matches [Observed — E-010]
3. Run Author Search to identify relevant collaborators, mentors, and topic contributors [Observed — E-001]
4. Rank/filter results by relevance and recency [Observed — E-008]

**Interaction Points:** Researcher ↔ ranked results list; researcher ↔ author profile results. [Observed — E-010]

**Outputs:** Tackled complex/interdisciplinary problems; strengthened funding applications; new collaborations; amplified research impact. [Observed — E-010]

**Evaluation Metrics:** Relevance ranking with recency boost (publisher/discipline-neutral, per E-008). [Observed — E-008]

**Required Capabilities:** Hybrid keyword/semantic search, cross-disciplinary indexing, author/collaborator identification. [Observed — E-001, E-008, E-010]

**Decision Points:** Whether to reach out to an identified potential collaborator; which cross-disciplinary connection is worth pursuing. [Inferred — Low-Medium confidence; reasoning: not explicitly described as a decision step in any source, but is the necessary human action following the stated output "built collaborations"]

**Feedback Mechanisms:** Not explicitly described for this specific scenario beyond the general iterative-query pattern common to all LeapSpace interactions (E-013). [Partially Inferred — E-013]

**Expected HI Characteristics (CARE):** Collaborative (directly enables human-to-human collaboration formation, a second-order HI effect); Responsible (publisher-neutral ranking prevents commercial bias in who gets surfaced as a collaborator). [Observed — E-008, E-010]

**Evidence IDs:** E-001, E-008, E-010, E-013

---

## Scenario 6 — Funding Discovery and Grant Matching

**Scenario Name:** Research-to-Funding Opportunity Matching

**Description:** A researcher connects their research discoveries or planned direction to relevant grant programs using the Find Funding tool, which searches a large, curated database of active grants (reported variously as 36,000+ and 45,000+ across different official sources — see note below) and allows filtering by country and research topic, addressing the documented pain point that "identifying relevant funders or grants is the most challenging task in the grant application process." [Observed — E-005, E-010]

**Goal:** Match research direction to appropriate, currently active funding opportunities, including lesser-known grants. [Observed — E-010]

**Human Actors:**
- Researcher or research-office staff searching for funding [Observed — E-010]

**Artificial Agents:**
- Find Funding / Funding Discovery engine, drawing on Elsevier's Funding Institutional database [Observed — E-005]

**Context:** Grant-application preparation, spanning both academic and institutional funding-office contexts. [Observed — E-010]

**Input Data:** Research topic; country/geography filter. [Observed — E-010]

**Knowledge Sources:** Elsevier's Funding Institutional database (curated institutional funding data). [Observed — E-002, E-005]

**Processing Method:** Filtered search/matching against a curated grants database. [Observed — E-010]

**Processing Tasks:**
1. Search Find Funding tool by topic and country [Observed — E-010]
2. Filter by research topic [Observed — E-010]
3. Review eligibility criteria and funder pages [Observed — E-010]

**Interaction Points:** Researcher ↔ Find Funding filtered results list; researcher ↔ funder eligibility pages. [Observed — E-010]

**Outputs:** Matched funding opportunities; surfaced lesser-known grants; access to award/eligibility information. [Observed — E-010]

**Evaluation Metrics:** Not explicitly named (a matching/filtering task rather than a claim-evaluation task). [Observed — E-010]

**Required Capabilities:** Curated funding-database search and filtering, international/local funding coverage. [Observed — E-010]

**Decision Points:** Which of the matched funding opportunities to pursue and apply for. [Inferred — Low confidence; standard implication of a matching tool's use, not explicitly described]

**Feedback Mechanisms:** Not explicitly described. [Not established — see `knowledge_gaps.md`]

**Expected HI Characteristics (CARE):** Collaborative (AI narrows a very large search space, human makes the funding-strategy decision); Adaptive (filterable by evolving research topic). [Observed — E-010]

**Evidence note:** Two official sources give different total grant counts (E-010: "36,000+ active grants"; E-005: "45,000 active and recurring grants worth over $100 billion") — this discrepancy is likely a timing difference between publication dates (the database grows over time) rather than a true contradiction, but is flagged here per RAS Section 8's "remove contradictions" step, and both figures are reported rather than silently reconciled.

**Evidence IDs:** E-002, E-005, E-010

---

## Scenario 7 — Writing Coach: Argument Strengthening and Draft Review

**Scenario Name:** AI-Assisted Argument Testing and Draft Strengthening

**Description:** A researcher drafting a paper, grant proposal, or thesis chapter uses the Writing Coach — a secure, private workspace "grounded entirely in publisher-neutral, Scopus-indexed literature" — to test their reasoning, shore up weak arguments, and surface missing evidence, through iterative back-and-forth dialogue, with claims checked "against current, relevant research." [Observed — E-001, E-002, E-004]

**Goal:** Strengthen the evidentiary and logical rigor of a research draft before submission. [Observed — E-001]

**Human Actors:**
- Researcher/author drafting a paper, proposal, or thesis [Observed — E-004]

**Artificial Agents:**
- Writing Coach dialogue engine [Observed — E-001, E-008]

**Context:** Private, secure drafting environment, content-grounded exclusively in peer-reviewed/Scopus-indexed literature (not general internet text). [Observed — E-001, E-009]

**Input Data:** Draft text or argument statement, submitted conversationally. [Observed — E-004]

**Knowledge Sources:** Publisher-neutral, Scopus-indexed literature. [Observed — E-001]

**Processing Method:** Conversational, dialogue-based argument interrogation checked against current literature. [Observed — E-001, E-004]

**Processing Tasks:**
1. Submit a draft argument or reasoning chain [Observed — E-004]
2. System tests the reasoning against current, relevant research [Observed — E-001]
3. System surfaces what evidence is missing [Observed — E-001]
4. Researcher engages in "back-and-forth dialogue" to refine the argument [Observed — E-004]

**Interaction Points:** Multi-turn dialogue between researcher and Writing Coach, explicitly framed as a "challenge" dynamic ("Challenge your draft through back-and-forth dialogue," E-004). [Observed — E-004]

**Outputs:** Strengthened arguments; surfaced evidence gaps; writing recommendations grounded in evidence. [Observed — E-001, E-011]

**Evaluation Metrics:** Not separately named; relies on the same underlying citation-grounding mechanism as Trust Cards (Scenario 4). [Observed — E-001]

**Required Capabilities:** Dialogue-based reasoning interrogation, literature-grounded fact-checking, private/secure session handling. [Observed — E-001, E-015]

**Decision Points:** Which surfaced gaps or counter-evidence to incorporate into the revised draft. [Inferred — Medium confidence; the "challenge" framing implies an accept/revise decision by the human author, not explicitly detailed]

**Feedback Mechanisms:** Iterative dialogue loop is itself the feedback mechanism — each round of challenge-and-response directly refines the draft. [Observed — E-004]

**Expected HI Characteristics (CARE):** Collaborative (explicitly dialogic, adversarial-but-constructive human-AI exchange); Explainable (claims checked against literature); Responsible (private/secure, not used for model training — E-001, E-015). [Observed — E-001, E-004, E-015]

**Evidence IDs:** E-001, E-002, E-004, E-008, E-009, E-011, E-015

---

## Scenario 8 — Corporate/Regulated R&D Evidence Verification (Reading Assistant & Compare Experiments)

**Scenario Name:** Governed Evidence Verification for Corporate and Regulated R&D

**Description:** Corporate R&D scientists (e.g., in pharmaceutical, biotech, or engineering firms) and the library/information-services managers who support them use Reading Assistant to analyze and summarize individual full-text articles or book chapters, and Compare Experiments to instantly generate structured tables comparing multiple studies' goals, materials, methods, results, and conclusions — within a security and IP framework designed for confidential corporate use ("Everything you do in LeapSpace is private, secure and encrypted... we never use your data to train any large language models"). [Observed — E-011, E-016]

**Goal:** Accelerate evidence-based R&D decision-making in a corporate/regulated setting while protecting intellectual property and maintaining an auditable evidence trail. [Observed — E-011]

**Human Actors:**
- Corporate R&D scientist/researcher [Observed — E-011]
- Library / information-services manager supporting the R&D function (named example: Samantha Intriligator, Manager, Regeneron Pharmaceuticals) [Observed — E-011]
- (Regulatory affairs / compliance function, implied by "regulatory compliance" framing for biopharmaceutical teams) [Observed — E-003; role title Inferred, Medium confidence — see reasoning below]

**Artificial Agents:**
- Reading Assistant (single-article/chapter analysis and summarization) [Observed — E-016]
- Compare Experiments (multi-study structured comparison table generator) [Observed — E-016]
- Trust Card / citation-traceability engine, providing the audit trail [Observed — E-011]

**Context:** Confidential corporate R&D environment (engineering, energy, pharma, biotech, MedTech per E-017) requiring IP protection and, for biopharmaceutical teams specifically, regulatory-compliance-grade evidence handling. [Observed — E-003, E-011, E-017]

**Input Data:** Individual articles/chapters for Reading Assistant; a research question or topic yielding multiple related studies for Compare Experiments; optionally, proprietary internal documents. [Observed — E-011, E-016]

**Knowledge Sources:** Elsevier full-text corpus plus vetted Open Access materials validated through Scopus. [Observed — E-016]

**Processing Method:** Single-document conversational analysis (Reading Assistant); structured multi-document tabular comparison across five fixed dimensions — goals, materials, methods, results, conclusions (Compare Experiments). [Observed — E-016]

**Processing Tasks:**
1. Upload or query for a specific article/chapter for Reading Assistant analysis [Observed — E-016]
2. Query for a topic to generate a Compare Experiments table across multiple studies [Observed — E-016]
3. Review Trust Card citations for audit-trail purposes [Observed — E-011]
4. Consolidate abstracts and full text in one workspace to free time for "hands-on discovery" [Observed — E-011]

**Interaction Points:** R&D scientist ↔ Reading Assistant (conversational article interrogation); R&D scientist ↔ Compare Experiments table; library manager ↔ platform administration/support role (implied by the named persona's job function). [Observed — E-011, E-016]

**Outputs:** Article/chapter summaries; structured comparison tables; cited, traceable research summaries suitable for internal audit; time freed for hands-on experimental discovery. [Observed — E-011, E-016]

**Evaluation Metrics:** Traceable-citation audit trail (qualitative); implicit time-savings (qualitative, "streamline... research, which frees up more time for hands-on discovery"). [Observed — E-011]

**Required Capabilities:** Single-document deep analysis, structured multi-study comparison, enterprise-grade encryption and data non-retention. [Observed — E-011, E-015, E-016]

**Decision Points:** Whether a compared set of studies provides sufficient/consistent evidence to proceed with a corporate R&D direction; what proprietary content is safe to upload given IP-protection requirements. [Inferred — Medium confidence; the sources establish the tools and the security guarantees but do not narrate a specific decision-making moment]

**Feedback Mechanisms:** Not explicitly described beyond the general privacy/non-training guarantee, which functions as a standing organizational-trust mechanism rather than a task-level feedback loop. [Observed — E-011, E-015]

**Expected HI Characteristics (CARE):** Responsible (IP protection, zero-retention data policy, ISO 27001-aligned security); Explainable (traceable citations for audit); Collaborative (scientist + library/information-services manager + AI tool, a three-way HI team spanning research and information-management roles). [Observed — E-008, E-011, E-015, E-016]

**Note on gap:** The specific role title and formal responsibilities of a "regulatory affairs/compliance" function for biopharmaceutical use of LeapSpace are implied by E-003's framing ("biopharmaceutical teams requiring regulatory compliance") but never named or detailed in any source — flagged as Inferred and logged in `knowledge_gaps.md`.

**Evidence IDs:** E-003, E-008, E-011, E-015, E-016, E-017

---

## Cross-Scenario Saturation Note

Together, these eight scenarios exercise every HI Ontology class (`hi:UseCase`, `hi:HITeam`, `hi:HumanAgent`, `hi:ArtificialAgent`, `hi:Goal`, `hi:Task`, `hi:Capability`, `hi:TaskExecution`, `hi:Interaction`, `hi:Context`, `hi:Evaluation`) at least twice, span both individual-academic and institutional/corporate contexts, and cover the full named feature set of LeapSpace (Writing Coach, Trust Cards, Claim Radar, Deep Research, Reading Assistant, Compare Experiments, Funding Discovery, Author Search) — satisfying the RAS saturation criterion (Section 8) for this knowledge-acquisition phase, within the bounds of what a newly launched (January 2026) product has yet made publicly documentable.
