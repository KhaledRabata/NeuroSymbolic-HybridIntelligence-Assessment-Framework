# Hybrid Intelligence Scenarios — Elsevier LeapSpace
RAS v1.0 | 5 evidence-backed scenarios | Namespaces: `hi:`, `hint:` per supplied `hiontology.ttl`

Each scenario below is either (a) explicitly documented by Elsevier in the accepted evidence, or (b) strongly supported by convergence across ≥2 independent accepted sources, per protocol §15. Modelling assumptions, where unavoidable to complete a scenario's field, are labelled inline as **[Assumption]**. No scenario asserts a fact without a cited Evidence ID.

---

## Scenario 1: Academic Literature Exploration and Deep Research Report Generation

**Scenario Name:** University Researcher Literature Exploration and Deep Research Reporting

**Description:** A university researcher or PhD student uses LeapSpace to explore a complex research question against the scholarly literature, generating a structured Deep Research report that surfaces patterns, assumptions, and evidence gaps, with every claim traceable to a source via a Trust Card.

**Goal:** Help the researcher move "from curiosity to discovery, faster," reaching insights they "wouldn't reach otherwise," while retaining full responsibility for interpretation. (hi:Goal)

**Human Actors:**
- University researcher / PhD student (e.g., an HCI researcher exploring topics outside their home discipline) (E-001, E-003)
- Journal peer reviewers and Advisory Board members, as upstream content-governance actors whose curation decisions shape what the researcher sees (E-011, E-017)

**Artificial Agents:**
- LeapSpace's multi-model AI system, selecting models per task (E-001, E-011)
- The Deep Research reasoning/RAG engine that produces structured reports (E-002, E-006)
- The Trust Card mechanism that attaches source provenance to each generated insight (E-001, E-003, E-011)

**Context:** Higher-education academic research environment; publisher-neutral literature spanning 100+ million Scopus abstracts from 7,000+ publishers and 15–20+ million peer-reviewed full-text articles/books (figures vary slightly by announcement date) (E-001, E-002, E-011). (hi:Context)

**Input Data:** The researcher's natural-language research question; optionally, the researcher's own uploaded documents (E-001, E-003).

**Knowledge Sources:** Scopus-indexed abstracts and records; peer-reviewed full-text articles and books from Elsevier and partner publishers (Emerald, IOP, NEJM Group, Sage, and others) (E-002, E-003, E-012).

**Processing Method:** Multi-model AI selection per task; agentic AI, generative AI, reasoning engines, and retrieval-augmented generation (E-002, E-011). (hi:Method)

**Processing Tasks:**
1. Submit a complex research question to LeapSpace (E-001)
2. LeapSpace analyzes abstracts and full text to produce structured, referenced answers (E-006)
3. Generate a Deep Research report with outlined scope, assumptions, and evidence (E-001)
4. Attach a Trust Card to each generated insight, showing the exact supporting passage (E-001, E-011)
5. Researcher reviews sources, contradictions, and evidence strength before accepting a claim (E-001, E-011)

**Interaction Points:** Researcher's natural-language query and follow-up exploration; real-time visibility into "the steps used to generate an answer" (E-011); researcher's independent judgment applied to Trust Card evidence before incorporating a claim into their own work (E-001). (hi:Interaction)

**Outputs:** A Deep Research report highlighting patterns, assumptions, and evidence gaps; individual referenced answers with Trust Cards (E-001, E-002, E-006).

**Evaluation Metrics:** Vendor-reported "less than 1%" serious-hallucination risk (E-005); claim-to-source traceability as a qualitative trust marker (E-001, E-011); independently reported researcher-trust baseline of "only 22% currently trust existing AI tools" that the product is designed to improve upon (E-010).

**Required Capabilities:** Multi-model task-appropriate AI selection; real-time reasoning-step visibility; claim-to-source traceability; hallucination minimization via curated source grounding (E-001, E-005, E-011, E-018).

**Decision Points:** Whether to trust and incorporate a given AI-surfaced claim into the researcher's own work, informed by the Trust Card's source and contradiction information (E-001, E-011).

**Feedback Mechanisms:** [Assumption — Inferred] The sources describe an ongoing "quality framework" evaluation process for the underlying Scopus AI engine (E-008) and "ongoing validation and governance" for LeapSpace generally (E-017), which plausibly incorporates researcher usage/feedback signals, but no source explicitly describes a documented mechanism by which an individual researcher's acceptance/rejection of a claim feeds back into model improvement. **Confidence: Low-Medium.**

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* The researcher directs inquiry and interprets AI-surfaced evidence; the AI does the large-scale literature synthesis the human could not do alone (E-001, E-006) — **Observed**.
- *Adaptive:* Multi-model selection adapts the underlying AI method to the task at hand (E-001, E-011) — **Observed**, though "adaptive" in the CARE sense of learning/personalizing over time specifically to an individual researcher is not explicitly documented — **Confidence: Medium**.
- *Responsible:* Grounded exclusively in curated, peer-reviewed content; publisher-neutral ranking; explicit hallucination-minimization design (E-001, E-005, E-017, E-018) — **Observed**.
- *Explainable:* Trust Cards and real-time reasoning-step visibility directly support interpretability of *why* a given answer was produced (E-001, E-011) — **Observed**.

**Evidence IDs:** E-001, E-002, E-003, E-005, E-006, E-011, E-012, E-018

---

## Scenario 2: Evidence-Grounded Scientific Writing with Writing Coach and Claim Radar

**Scenario Name:** Dialogue-Based Manuscript Drafting and Evidence Verification

**Description:** A researcher drafts a manuscript section using LeapSpace's Writing Coach, engaging in a back-and-forth dialogue with an AI assistant that checks claims against the published literature (via Claim Radar) and surfaces missing evidence or unanswered questions, with every recommended change requiring the researcher's explicit approval.

**Goal:** Strengthen the evidential grounding, clarity, and logic of a research argument — "the drafting tool that challenges you to improve your evidence, not just your eloquence" — without ceding authorial control. (hi:Goal)

**Human Actors:**
- The researcher/author drafting the manuscript (E-014, E-015)

**Artificial Agents:**
- Writing Coach (dialogue-based drafting assistant) (E-014, E-015)
- Claim Radar (claim-level evidence-verification agent, checking against 107M+ peer-reviewed papers) (E-004, E-014, E-015)

**Context:** Private, encrypted individual or corporate research-writing environment; content never used to train third-party or public AI models (E-003, E-014, E-015). (hi:Context)

**Input Data:** The researcher's in-progress draft text; specific claims or arguments the researcher wants checked (E-015).

**Knowledge Sources:** The same Scopus-indexed, 107M+-paper peer-reviewed literature base used elsewhere in LeapSpace (E-015).

**Processing Method:** Two-panel dialogue interface (document editor + chat assistant); claim-level evidence checking returning support/contradict/mixed labels (E-015). (hi:Method)

**Processing Tasks:**
1. Researcher drafts or pastes text into the document editor panel (E-015)
2. Researcher asks the Assistant (chat panel) to test reasoning or check a specific claim (E-015)
3. Claim Radar checks the claim against the literature, returning labeled supporting/contradicting/mixed evidence (E-014, E-015)
4. Writing Coach surfaces missing evidence, unanswered questions, or new opportunities (E-014)
5. Writing Coach recommends specific changes; researcher reviews and approves or rejects each one (E-014)

**Interaction Points:** Continuous chat-based dialogue between researcher and Writing Coach (E-015); explicit approval gate before any recommended change is applied (E-014). (hi:Interaction)

**Outputs:** A strengthened draft with evidence-checked claims; a labeled evidence map (support/contradict/mixed) for checked claims (E-015).

**Evaluation Metrics:** [Assumption — Inferred] No explicit quantitative metric (e.g., "% of claims strengthened" or "average evidence-support score") is documented for Writing Coach specifically; the qualitative support/contradict/mixed labeling scheme (E-015) is the closest documented evaluative output. **Confidence: Medium** that this labeling scheme functions as the tool's de facto evaluation metric.

**Required Capabilities:** Dialogue-based reasoning support; claim-level evidence verification against a large peer-reviewed corpus; gap/missing-evidence surfacing; user-approval-gated edit application (E-014, E-015).

**Decision Points:** Whether to accept, modify, or reject each individual Writing-Coach-recommended change (E-014) — the single most explicitly documented human-in-the-loop decision point in the entire evidence base.

**Feedback Mechanisms:** [Assumption — Inferred] Researcher approval/rejection choices plausibly refine subsequent recommendations within the same session (consistent with "dialogue" framing), though no source explicitly documents session-level or cross-session learning from these approval decisions. **Confidence: Low.**

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Genuinely dialogic — the human and AI iterate together on argument construction (E-014, E-015) — **Observed**.
- *Adaptive:* [Assumption] Plausible within-session responsiveness to researcher direction, but no explicit cross-session personalization documented — **Confidence: Low-Medium**.
- *Responsible:* Explicit "no automatic edits — all changes are user-approved" policy directly operationalizes accountability (E-015) — **Observed**.
- *Explainable:* Claims are labeled as supporting, contradicting, or mixed rather than given an opaque single score, and gaps are explicitly surfaced (E-014, E-015) — **Observed**.

**Evidence IDs:** E-003, E-004, E-014, E-015

---

## Scenario 3: Pharmaceutical/Biotechnology R&D Evidence Synthesis

**Scenario Name:** Cross-Functional Pharma R&D Evidence Synthesis (Discovery Through Pharmacovigilance)

**Description:** Multiple specialized roles within a pharmaceutical or biotechnology R&D organization — discovery scientists, medicinal chemists, preclinical teams, clinical development teams, pharmacovigilance/regulatory professionals, and medical affairs specialists — each use LeapSpace, integrated with Elsevier's specialized databases (Reaxys, PharmaPendium, Embase, ScienceDirect), to synthesize evidence relevant to their stage of the drug-development lifecycle.

**Goal:** Make "confident, evidence-based decisions to optimize R&D" — including evaluating target-disease relevance, de-risking compounds before committing to series development, designing stronger clinical trials, and detecting safety signals earlier with regulator-ready documentation. (hi:Goal)

**Human Actors:**
- Discovery scientists (target identification and validation) (E-013)
- Medicinal chemists (hit identification to lead optimization) (E-013)
- Preclinical teams (safety and translational research) (E-013)
- Clinical development teams (trial design and safety monitoring) (E-013)
- Pharmacovigilance and regulatory professionals (safety signal detection) (E-013)
- Medical affairs specialists (evidence synthesis) (E-013)
- Global Library Services staff supporting evidence retrieval across these functions (E-004, E-010)

**Artificial Agents:**
- LeapSpace's core AI workspace (literature exploration, Deep Research, Compare) (E-004, E-013)
- Integration layer connecting LeapSpace to Reaxys (chemistry data), PharmaPendium (regulatory/safety data), and Embase (biomedical literature) (E-013)

**Context:** Regulated pharmaceutical/biotechnology R&D environment characterized by "intense time pressures, information overload and regulatory hurdles" (E-004); spans the full drug-development lifecycle from discovery to post-market pharmacovigilance (E-013). (hi:Context)

**Input Data:** Research questions specific to each function (e.g., target validation evidence, compound safety data, trial-design precedent, adverse-event literature) (E-013).

**Knowledge Sources:** Reaxys, PharmaPendium, Embase, ScienceDirect, plus LeapSpace's general Scopus-indexed and peer-reviewed literature base (E-013).

**Processing Method:** Multi-model AI evidence synthesis across specialized proprietary databases and general scholarly literature (E-013). (hi:Method)

**Processing Tasks:**
1. Discovery scientists evaluate target-disease relevance early in discovery (E-013)
2. Medicinal chemists synthesize evidence to de-risk compounds before committing to series development (E-013)
3. Clinical development teams design trials and gather safety evidence (E-013)
4. Pharmacovigilance/regulatory professionals detect safety signals and prepare regulator-ready documentation (E-013)
5. Medical affairs specialists synthesize evidence for external communication (E-013)
6. Library Services staff verify references and structure evidence tables to support all of the above (E-010)

**Interaction Points:** Each functional role's natural-language querying of LeapSpace and its integrated databases; Library Services staff acting as an intermediary/support role between raw literature and R&D scientists (E-010). (hi:Interaction)

**Outputs:** Target-validation assessments; compound de-risking evidence; clinical trial design evidence; regulator-ready safety-signal documentation; synthesized medical-affairs evidence summaries (E-013).

**Evaluation Metrics:** [Assumption — Inferred] No pharma-specific quantitative evaluation metric is documented beyond the general platform-level hallucination-rate figure (E-005) and reference-verification time savings mentioned qualitatively by a library-services testimonial (E-010: "shortens reference verification time"). **Confidence: Low** that this generalizes quantitatively to pharma-specific workflows, since no numeric time-savings figure was disclosed.

**Required Capabilities:** Multi-database evidence synthesis (chemistry, regulatory/safety, biomedical literature); regulatory-context-aware evidence gathering; structured table extraction for evidence comparison (E-013, E-014).

**Decision Points:** Whether a compound's evidence profile justifies committing to further series development (E-013); whether detected safety-signal evidence is sufficient to trigger regulatory action (E-013).

**Feedback Mechanisms:** [Assumption — Inferred] No explicit source documents a feedback loop from pharma R&D outcomes (e.g., a compound's eventual clinical success/failure) back into LeapSpace's models. **Confidence: Low** — flagged as a genuine gap, not filled.

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Six distinct human role-types each bring domain judgment to AI-synthesized evidence at their specific lifecycle stage (E-013) — **Observed**.
- *Adaptive:* [Assumption] Not explicitly documented for this scenario beyond the platform-general multi-model selection — **Confidence: Low**.
- *Responsible:* Explicit orientation toward "regulator-ready documentation" implies an accountability/compliance design intent (E-013) — **Observed** (design intent); **Inferred** (regulatory-acceptance outcome, not independently verified).
- *Explainable:* Inherits the platform-general Trust Card / evidence-traceability mechanism (E-001, E-011), not separately re-documented for pharma specifically — **Observed** (by inheritance), **Confidence: Medium**.

**Evidence IDs:** E-004, E-010, E-013, E-014

---

## Scenario 4: Funding and Collaborator Discovery for Research Planning

**Scenario Name:** Research Project Planning via Funding and Collaborator Discovery

**Description:** A researcher planning a new project uses LeapSpace to identify potential collaborators/topic experts through natural-language author search and to discover relevant funding opportunities from a curated database of active grants.

**Goal:** Accelerate the earliest, highest-uncertainty phase of the research lifecycle — project planning and hypothesis generation — by reducing the manual effort of literature-based expert-finding and funding-landscape scanning. (hi:Goal)

**Human Actors:**
- The planning researcher (academic or corporate) (E-002, E-003)

**Artificial Agents:**
- Author Search (natural-language collaborator/expert-identification agent) (E-001, E-006)
- Funding Discovery engine, drawing on curated institutional grant data (E-001, E-002)

**Context:** Early-stage research planning, applicable in both academic and corporate R&D settings; funding landscape of "45,000+ active and recurring grants worth over $100 billion" (E-002, E-006). (hi:Context)

**Input Data:** A natural-language description of the researcher's planned topic or question (E-006).

**Knowledge Sources:** Indexed publication records (for author/expert identification) (E-001); curated institutional funding-agency data (E-001, E-002).

**Processing Method:** Natural-language semantic search over publication records, contrasted explicitly with traditional keyword search (E-006). (hi:Method)

**Processing Tasks:**
1. Researcher describes their planned topic in natural language (E-006)
2. Author Search identifies possible collaborators/topic experts based on indexed publication records (E-001, E-006)
3. Funding Discovery surfaces relevant active/recurring grants matching the topic (E-001, E-002)
4. Researcher reviews and selects candidate collaborators and funding opportunities (E-001)

**Interaction Points:** Natural-language topic description as the primary interaction input; researcher's downstream selection/outreach decisions occur outside LeapSpace itself (E-001, E-006). (hi:Interaction)

**Outputs:** A ranked or curated list of potential collaborators/topic experts; a list of matching funding opportunities (E-001, E-002, E-006).

**Evaluation Metrics:** [Assumption — Inferred] No explicit precision/recall or match-quality metric is documented for either Author Search or Funding Discovery. **Confidence: Low** for any specific numeric evaluation claim; the only adjacent, platform-general metric available is the overall hallucination-rate figure (E-005), which is not specific to search/matching tasks.

**Required Capabilities:** Natural-language semantic author/expert search; curated funding-data aggregation and matching (E-001, E-002, E-006).

**Decision Points:** Which surfaced collaborators to actually approach; which funding opportunities are worth pursuing given eligibility and fit (implicit — outside LeapSpace's documented scope) (E-001).

**Feedback Mechanisms:** [Assumption — Inferred] Not documented. **Confidence: Low** — no source describes how outcomes of collaborator outreach or grant applications feed back into the platform.

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* AI surfaces candidates; human makes the relational/strategic decision of whom to contact and which funding to pursue (E-001) — **Observed**.
- *Adaptive:* [Assumption] Not documented — **Confidence: Low**.
- *Responsible:* Funding data is explicitly described as "curated" from "recognized institutional sources" (E-017), implying a data-quality control step — **Observed**.
- *Explainable:* Natural-language search is explicitly contrasted with opaque keyword matching (E-006), implying some interpretability advantage, but no dedicated "why was this collaborator suggested" explanation mechanism is documented for Author Search specifically (unlike Trust Cards for literature claims) — **Confidence: Low-Medium**.

**Evidence IDs:** E-001, E-002, E-006, E-017

---

## Scenario 5: Responsible AI Governance and Trust Validation of LeapSpace Outputs

**Scenario Name:** Multi-Layer Human Governance of AI-Generated Research Insights

**Description:** Before and after any AI-generated insight reaches a researcher, a multi-layer human governance structure — journal peer reviewers, the independent Scopus Content Selection and Advisory Board, the new independent LeapSpace Advisory Board, and Elsevier's enterprise-wide Responsible AI policy process — curates source content, evaluates model quality, and monitors for bias and unfair outcomes, operationalizing Elsevier's five Responsible AI Principles.

**Goal:** Ensure that AI-assisted research insights remain trustworthy, unbiased, explainable, and subject to meaningful human accountability, addressing a documented researcher-trust deficit (only 22% currently trust existing AI tools). (hi:Goal)

**Human Actors:**
- Journal peer reviewers (content-level curation) (E-011)
- Scopus Content Selection and Advisory Board members (E-011, E-017)
- LeapSpace Advisory Board members, chaired by a named professor (E-011, E-017)
- Elsevier Responsible AI policy owners within "individual business areas" (E-007)

**Artificial Agents:**
- The models underlying LeapSpace, ScienceDirect AI, and Scopus AI, which are the subject of evaluation (E-007, E-008)
- Automated bias-detection tooling used as part of the governance process (E-007)

**Context:** Enterprise-wide AI governance context spanning all Elsevier AI-enabled products, of which LeapSpace is one instance; independent (non-Elsevier-employee) oversight bodies exist specifically to check for undue publisher bias (E-011, E-017). (hi:Context)

**Input Data:** Candidate content sources (journal articles, books, abstracts) for curation; deployed model outputs for quality/bias evaluation (E-007, E-011).

**Knowledge Sources:** Elsevier's Responsible AI Principles document; Scopus AI's periodic quality-framework evaluation results (E-007, E-008).

**Processing Method:** Human expert review (peer review, advisory-board deliberation) combined with automated bias-detection tooling and ongoing post-deployment monitoring (E-007). (hi:Method)

**Processing Tasks:**
1. Peer reviewers vet individual articles before they enter the corpus (E-011)
2. The Scopus Content Selection and Advisory Board governs which publishers/content sources are indexed (E-011)
3. The LeapSpace Advisory Board oversees platform-level transparency and neutrality (E-005, E-011, E-017)
4. Automated bias-detection tools are run against deployed models (E-007)
5. Ongoing monitoring and response occurs after deployment (E-007)
6. Retracted articles are actively excluded via ongoing governance processes (E-017)

**Interaction Points:** Advisory-board deliberation and decision-making (implicitly human-only, upstream of any researcher-facing interaction) (E-011, E-017); the assignment of "clear... oversight responsibilities" with "capacity to intervene" (E-007). (hi:Interaction)

**Outputs:** A curated, retraction-filtered content corpus; a governed, publisher-neutral ranking algorithm; documented bias-detection and monitoring results (not publicly disclosed in detail within the accessible sources) (E-007, E-017).

**Evaluation Metrics:** Scopus AI's "quality framework" evaluation (methodology not disclosed in the accessible support documentation) (E-008); implicit bias-detection tooling output (E-007); [Assumption — Inferred] no publicly disclosed quantitative bias or fairness metric (e.g., a specific disparate-impact-style statistic) was found for LeapSpace or its underlying engines. **Confidence: Low** for any specific fairness metric value; **High confidence** that a qualitative governance *process* exists.

**Required Capabilities:** Multi-layer content curation; independent advisory oversight; automated bias detection; publisher-neutral ranking; retraction monitoring (E-007, E-011, E-017).

**Decision Points:** Whether a given source/publisher is included in the indexed corpus; whether a deployed model passes quality/bias review; whether/when to intervene on a flagged issue (E-007, E-011, E-017).

**Feedback Mechanisms:** "Ongoing monitoring and response after deployment" is explicitly documented as a continuous post-deployment feedback loop, and the Responsible AI Principles themselves are stated to "iterate over time, based on colleague and customer feedback, as well as industry and legislative trends" (E-007) — the most explicitly documented feedback mechanism in the entire evidence base.

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Multiple independent human bodies (internal Elsevier, external advisory boards) jointly govern AI behavior rather than any single actor unilaterally controlling it (E-011, E-017) — **Observed**.
- *Adaptive:* Explicit statement that principles "iterate over time" based on feedback and legislative trends (E-007) — **Observed**.
- *Responsible:* This entire scenario *is* the Responsible-AI operationalization — bias prevention, accountability, data governance are all named principles with process detail (E-007) — **Observed**.
- *Explainable:* "We support transparency and can explain how our solutions work" is a named, explicit principle (E-007) — **Observed**. However, an independent critic's observation that "no standardized evaluation method exists for assessing AI-generated summary accuracy" generally (E-016) tempers confidence that this explainability commitment is independently verified rather than self-assessed — **Confidence: Medium** on independent verification specifically.

**Evidence IDs:** E-005, E-007, E-008, E-011, E-016, E-017

---

## Cross-Scenario Summary Table

| Scenario | Primary HI Ontology Classes Instantiated | Evidence Breadth |
|---|---|---|
| 1. Academic Literature Exploration & Deep Research | HITeam, HumanAgent, ArtificialAgent, Task, TaskExecution, Interaction, Context | 8 sources |
| 2. Writing Coach / Claim Radar Drafting | HumanAgent, ArtificialAgent, Task, TaskExecution, Interaction | 4 sources |
| 3. Pharma/Biotech R&D Evidence Synthesis | HumanAgent (6 role types), ArtificialAgent, Task, Goal, Context | 4 sources |
| 4. Funding & Collaborator Discovery | HumanAgent, ArtificialAgent, Task, Context | 4 sources |
| 5. Responsible AI Governance & Trust Validation | HumanAgent, ArtificialAgent, Context, Evaluation, Interaction | 6 sources |
