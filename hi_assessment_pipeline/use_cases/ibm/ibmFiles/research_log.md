# Research Log — IBM watsonx.governance

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **IBM watsonx.governance**
Chronological log of every research step performed during the Domain Knowledge Acquisition phase, per RAS Section 14. Each entry follows the Research Protocol (RAS Section 8): identify missing knowledge → search official sources → search engineering docs → search whitepapers → search research papers → search conference/demo material → compare findings → normalise terminology → map to ontology → repeat until saturation.

Search engine used throughout: web search tool (Google-backed), supplemented by direct URL fetches of pages surfaced in results.

---

## Round 1 — Product Scope & Official Overview

**Objective:** Establish what IBM watsonx.governance is, its core pillars, and top-level personas/components before drilling into specific workflows.

**Search terms:**
- "IBM watsonx.governance official documentation overview features"
- "IBM watsonx.governance AI model risk governance lifecycle"

**Sources visited:** IBM product page (ibm.com/products/watsonx-governance), IBM Docs overview, Governance console docs (w-and-w/2.4.x), Medium (Shuvanker Ghosh), G2 reviews, DeepInspect blog, Nexright blog, IBM OpenPages Model Risk Governance docs.

**Sources accepted:** E-001 (product page), E-002 (Governance console docs, partial).
**Sources rejected:** G2 (crowd review, not primary), DeepInspect (competitor blog), Nexright (marketing).

**Information extracted:** Three pillars (Visibility, Control, Accountability); shadow AI detection; governance graph; AI-native embedded assistants; regulatory alignment (EU AI Act, NIST AI RMF, ISO 42001); customer outcome case studies (Infosys, Careerforce Pro, US Open, internal IBM data-clearance use); human roles referenced (risk officers, compliance teams, data scientists, model validators, audit).

**Ontology concepts discovered:** `hi:UseCase`, `hi:HITeam`, `hi:Goal`, `hi:Task`, `hi:ArtificialAgent` (AI assistants), `hi:Context` (regulatory frameworks).

**Scenarios supported:** Seeds for all eight scenarios (general scope); direct seed for Scenario 3 (risk/compliance) and Scenario 8 (model risk governance).

**Remaining unknowns after this round:** Exact workflow steps for MRG; specific persona titles beyond generic "risk officer"; concrete metrics list.

---

## Round 2 — Architecture: OpenPages, OpenScale, AI FactSheets

**Objective:** Understand the three underlying technical components and how governance approval workflows operate.

**Search terms:** (direct fetch, no new search) — followed up on E-001/E-002 findings.

**Sources visited:** heidloff.net (Niklas Heidloff), dataplatform.cloud.ibm.com MRG description page, dataplatform.cloud.ibm.com MRG example workflow page.

**Sources accepted:** E-003 (Heidloff article — high quality, IBM-affiliated author).
**Sources rejected:** MRG description page and MRG example workflow page — both returned only navigation-chrome content (JavaScript-rendered single-page application not retrievable via automated fetch); logged as partial/inaccessible (E-004) and in `knowledge_gaps.md`.

**Information extracted:** Three components confirmed — OpenPages (GRC), OpenScale (monitoring), AI FactSheets (model tracking from request to production); evaluation dimensions (model health, accuracy, drift, bias, gen AI quality); requester → reviewer (questionnaire) → approver workflow pattern; no-code workflow/questionnaire editor for customization.

**Ontology concepts discovered:** `hi:HumanAgent` (requester, reviewer, approver), `hi:ArtificialAgent` (OpenScale monitors), `hi:Task` (questionnaire-based review), `hi:Capability` (workflow customization).

**Scenarios supported:** Scenario 1 (predictive model governance), Scenario 3 (use case approval), Scenario 8 (model risk governance).

**Remaining unknowns:** Full MRG stage-by-stage detail (blocked); specific metric names for GenAI quality.

---

## Round 3 — Metrics, Fairness, Explainability, FactSheets Research Paper

**Objective:** Identify the concrete evaluation metrics (fairness, drift, explainability, GenAI quality) and the academic/research foundation for AI FactSheets.

**Search terms:**
- "watsonx.governance evaluate metrics quality fairness drift explainability documentation"
- ""AI FactSheets" IBM Research paper "increasing trust" model transparency"
- "watsonx.governance generative AI quality metrics hallucination faithfulness prompt evaluation"
- "IBM watsonx.governance model validator risk officer workflow approve model use case"

**Sources visited:** IBM Docs use-case page (2.3.x), Medium (Gautam Chutani), Model Governance product sub-page, researcher.ibm.com/blog/aifactsheets, arxiv.org/pdf/2006.13796v1, research.ibm.com/publications (human-centered FactSheets methodology), IBM announcement on agentic AI governance, Heidloff gen-AI-quality-metrics article, dataplatform MRG desc/workflow pages (retry, still blocked), community.ibm.com use-case-approval blog.

**Sources accepted:** E-005 (agentic AI governance announcement), E-006 (Gautam Chutani predictive monitoring), E-007 (community.ibm.com use case approval blog), E-009 (FactSheets research blog), E-009b (arXiv FactSheets/SDoC paper), E-009c (human-centered FactSheets methodology paper), E-014 (Model Governance product sub-page).
**Sources rejected:** Heidloff's gen-AI-quality-metrics article — page content did not surface the actual metric list (only a pointer to IBM docs that themselves returned HTTP 500); the underlying metric names were instead confirmed via E-008 and E-013 in Round 4.

**Information extracted:** Watson OpenScale metrics: accuracy, precision, recall, fairness (disparate impact, statistical parity difference), drift, explainability (SHAP/LIME, local & global); AI FactSheets as "nutrition labels for models"; Model Governance's three capabilities (tracking/transparency, evaluation/documentation, monitoring); agent lifecycle stages (use-case creation → development → production) with named metrics (HAP, PII, prompt injection, context relevance, faithfulness, answer similarity, answer relevance, hit rate, average precision, reciprocal rank, unsuccessful requests) and explicit human-in-the-loop text: "Human feedback or red teaming: Allows SMEs to observe and verify the agent's actions... and test agents for susceptibilities."; five-step GenAI use-case approval methodology (Use Case Creation → Custom Field Configuration → Initial Approval Workflow Design → Risk Assessment → Development Authorization & Monitoring) with named reviewer roles (Stakeholder, Legal, Data Protection, Brand).

**Ontology concepts discovered:** `hi:Capability` (fairness/drift/explainability/quality evaluation), `hi:Evaluation`, `hi:Interaction` (human feedback/red-teaming episode), `hi:HumanAgent` (SMEs, Legal/Data Protection/Brand reviewers), `hint:Metric` concepts (disparate impact, statistical parity, HAP, PII, faithfulness, etc.).

**Scenarios supported:** Scenario 1, Scenario 3, Scenario 5.

**Remaining unknowns:** Exact GenAI quality metric definitions with numeric ranges; RAG-specific metrics; adversarial/red-teaming metric definitions.

---

## Round 4 — RAG Metrics, EU AI Act Assessment, Third-Party Governance, Prompt Security

**Objective:** Fill in RAG-specific evaluation metrics, EU AI Act risk classification mechanics, multi-cloud/third-party model governance, and adversarial prompt security.

**Search terms:**
- "IBM watsonx.governance Risk Atlas AI regulations mapping"
- "IBM watsonx.governance EU AI Act applicability assessment risk category questionnaire"
- ""watsonx.governance" prompt injection HAP PII detection metric definition"
- "IBM watsonx governance SDK open source metrics evaluator github"

**Sources visited:** IBM Compliance obligations-to-controls mapping blog, dataplatform AI risk atlas page, dataplatform EU AI Act applicability assessment page, ibm.com/think/insights/eu-ai-act, Medium (Doug Stauber — governance 2.0), Medium (Sam Kwan — 3rd-party governance), Medium (Manish Bhide — adversarial attacks), GitHub IBM/ibm-watsonx-gov, GitHub IBM/watson-openscale-samples.

**Sources accepted:** E-008 (watsonx.governance 2.0 announcement), E-010 (AI risk atlas, partial), E-011 (GitHub SDK repo, partial), E-012 (adversarial attacks article), E-019 (third-party governance article).
**Sources rejected:** dataplatform EU AI Act applicability-assessment page — not fetched in full after repeated JS-rendering failures on the same domain in prior rounds; EU AI Act mechanics instead sourced from E-008, which independently confirmed the same feature (AI Model Risk Assessments + EU AI Act Applicability Assessment determining Prohibited/High/Limited/Minimal risk category).

**Information extracted:** RAG metrics with definitions (Faithfulness, Answer Relevance, Unsuccessful Requests, all scored 0–1); AI Model Risk Assessment questionnaire tool; EU AI Act Applicability Assessment (risk category determination); prompt injection taxonomy (basic/intermediate/advanced) and prompt leakage; Adversarial Robustness Score and Prompt Leakage Risk Score (0–1 scale); red-teaming → hardening → recompute remediation loop; multi-cloud third-party governance via Custom ML Provider proxy endpoints and Detached Prompt Templates; full GenAI metric list (ROUGE, SARI, METEOR, Text quality, BLEU, Sentence similarity, PII, HAP, Readability, Exact match, F1/precision/recall); "Human Rating/Voting score" as a custom metric.

**Ontology concepts discovered:** `hi:Evaluation`/`hi:Experiment` (Adversarial Robustness Score, Prompt Leakage Risk Score, RAG metrics), `hi:Context` (EU AI Act risk categories), `hi:ArtificialAgent` (custom ML provider proxy, detached prompt templates as agent representations of third-party models), `hi:Interaction` (human rating/voting as a metric derived from human-agent interaction).

**Scenarios supported:** Scenario 2, Scenario 3, Scenario 4, Scenario 8.

**Remaining unknowns:** Detailed RAG evaluation UI workflow; virtual assistant monitoring; explainability workflow detail; recruitment use case; agent observability platform detail; financial services MRM detail.

---

## Round 5 — RAG Evaluation Workflow, Virtual Assistant Monitoring, Recruitment Case Study

**Objective:** Close remaining gaps on RAG evaluation workflow mechanics, conversational AI production monitoring, and a concrete business-facing case study to ground a human-centric HI scenario.

**Search terms:**
- "IBM Careerforce Pro watsonx.governance case study hiring bias reduction"
- "IBM watsonx.governance US Open case study fairness court"

**Sources visited:** Medium (Gautam Chutani — revisited for corroboration), community.ibm.com blog, Medium (Doug Stauber — revisited), research.ibm.com/blog/factsheets-ai (revisited), ibm.com/case-studies/careerforce-pro, ibm.com/docs/en/watsonx/saas use-case page, Medium (Pratap V — RAG evaluation), TechRepublic article on Watson hiring bias (background only), IBM case study on US Open fan engagement (found to be about generative-AI fan engagement, not fairness scoring — not directly relevant to watsonx.governance; rejected for scenario use).

**Sources accepted:** E-015 (RAG evaluation, Pratap V), E-016 (Careerforce Pro case study), E-017 (IBM Docs use-case personas).
**Sources rejected:** US Open case study — on inspection, the "court fairness" figure cited on the product page (E-001) refers to a different IBM AI system (electronic line-calling / fan engagement), not a documented watsonx.governance workflow; excluded from scenario construction to avoid fabricating an HI scenario not evidenced for this specific product. Logged as a noted ambiguity in `knowledge_gaps.md`.

**Information extracted:** RAG evaluation retrieval metrics (Context Relevance, Retrieval Precision, Average Precision, Hit Rate, NDCG) and answer metrics (Faithfulness, Answer Relevance, Answer Similarity, Unsuccessful Requests); LLM-as-judge vs. fine-tuned slate-model judge; RAG circles UI and root-cause analysis; source attribution for explainability; Careerforce Pro's IRIS voice AI screening agent and its full hiring workflow with quantified outcomes; six named personas from official IBM Docs (Business Analyst, Data Scientist, Prompt Engineering Team, ML Engineer, ModelOps Engineer, Data Analyst) mapped to Projects/Spaces/Factsheets/OpenScale tools.

**Ontology concepts discovered:** `hi:TaskExecution` (development-phase vs. production-phase evaluation), `hi:ArtificialAgent` (IRIS voice agent), `hi:HumanAgent` (hiring manager, recruiter, HR leader; six IBM Docs personas), `hi:Interaction` (root-cause drill-down, source-attribution review).

**Scenarios supported:** Scenario 2, Scenario 7, and persona grounding for Scenario 1/8.

**Remaining unknowns:** Agentic AI runtime observability role detail; explainability (SHAP) workflow; financial-services MRM regulatory detail; academic/conference corroboration.

---

## Round 6 — Agent Observability, Third-Party Governance Mechanics, Neuro-Symbolic Literature Check

**Objective:** Close out agent-runtime observability detail and perform the mandated literature check for adjacent neuro-symbolic/knowledge-graph research (background context for the thesis, not for scenario content).

**Search terms:**
- "IBM watsonx Orchestrate agent governance human in the loop approval"
- "neuro-symbolic AI governance knowledge graph SHACL LLM extraction research paper 2025"

**Sources visited:** ibm.com/products/watsonx-orchestrate/governance-and-observability, HyperFRAME Research blog (background only, not cited), IBM Mediacenter agent-observability video (blocked), ACM/SAGE/arXiv neuro-symbolic papers (background scan — general neuro-symbolic/KG-LLM literature, not watsonx-specific; used only to confirm the thesis's neuro-symbolic framing has active research precedent, no scenario content extracted from these).

**Sources accepted:** E-018 (watsonx Orchestrate governance/observability page).
**Sources rejected:** HyperFRAME Research blog (independent analyst commentary, opinion-oriented, not primary evidence); IBM Mediacenter demo video (blocked by robots.txt).

**Information extracted:** Centralized observability layer for agents; full audit logs and traceability; policy/guardrail enforcement; agent metrics (accuracy, tool-call reliability, completion rate, quality, cost, safety); explicit statement that the page does not detail specific human role titles or approval steps.

**Ontology concepts discovered:** `hi:Context` (centralized operational/observability layer), `hi:Evaluation` (agent runtime metrics).

**Scenarios supported:** Scenario 5 (supplementary).

**Remaining unknowns:** Specific human role titles for agent runtime approval (logged as a gap).

---

## Round 7 — Explainability Workflow, Financial Services MRM, Demo/Conference Material

**Objective:** Close out SHAP explainability workflow detail and financial-services model risk management (MRM) regulatory grounding for Scenario 8; attempt to locate conference/demo material per source-priority tier 5.

**Search terms:**
- "IBM watsonx.governance explainability SHAP LIME local explanation Watson OpenScale documentation"
- ""watsonx.governance" OR "Watson OpenScale" conference presentation demo IBM Think 2025"
- ""watsonx.governance" academic paper case study evaluation research"

**Sources visited:** Medium (Pratap V — SHAP explainability), BizTech Magazine (financial institutions article), IBM Mediacenter (Governed Agentic Catalog demo — blocked by robots.txt), IBM Mediacenter (model monitoring video — not fetched, redundant with E-006), IBM Docs Watson OpenScale overview (software-hub, not fetched — redundant with E-006/E-021), CliffsNotes study notes (rejected — student-generated secondary summary, unreliable provenance).

**Sources accepted:** E-021 (SHAP explainability), E-022 (BizTech financial institutions).
**Sources rejected:** IBM Mediacenter Governed Agentic Catalog demo (robots.txt block — a genuine gap, since RAS Source Priority tier 5 calls for official demos); CliffsNotes study notes (unreliable secondary/student source, explicitly excluded per RAS source-quality standards).

**Information extracted:** SHAP mechanism (Shapley values, marginal contribution); local explanations (transaction-level) vs. global explanations (model-level); stability metric (NDCG-based) tracking explanation consistency over time; financial-services MRM context (data residency, auditability, explainability, consumer protection, third-party risk across jurisdictions); explicit "keeping human risk oversight in the loop" statement without named role titles.

**Ontology concepts discovered:** `hi:Capability` (explainability), `hi:Evaluation` (stability metric), `hi:Context` (banking/insurance MRM standards, multi-jurisdiction).

**Scenarios supported:** Scenario 1 (explainability enrichment), Scenario 8 (regulatory context).

**Remaining unknowns after this round:** Official conference/demo transcript access (blocked by platform robots.txt — logged as a systematic gap, not a content gap); named human role titles for financial-services model validation sign-off (industry-standard titles such as "Model Validator" and "Chief Risk Officer" are common knowledge in MRM practice but not explicitly named in the retrieved watsonx.governance-specific sources — flagged as Inferred, not Observed, wherever used).

---

## SATURATION ASSESSMENT

After 7 rounds covering 25+ distinct searches/fetches across official documentation, IBM engineering blogs, IBM Research publications, community blogs, and trade press, the following saturation criteria (RAS Section 8) are judged met:

- **No new artificial-agent types** emerged after Round 6 (OpenScale, OpenPages, AI FactSheets, Governed Agentic Catalog, Experimentation Studio, detached prompt templates/custom ML provider proxies, IRIS voice agent, and the underlying foundation/ML models themselves cover the full observed range).
- **No new human-role archetypes** emerged after Round 5 (all subsequent searches surfaced the same or overlapping role set: requester/owner, developer/prompt engineer, validator/reviewer, ModelOps engineer, risk officer/approver, SME/red-teamer, business analyst, data analyst, and domain-specific roles for HR/legal/brand/data-protection review).
- **No new evaluation-metric families** emerged after Round 4 (predictive-model metrics, GenAI text-quality metrics, RAG metrics, safety/security metrics, and agent metrics were each independently confirmed by at least two sources).
- Two specific gaps remain **genuinely unresolved** rather than simply unsearched: (1) full text of the official Model Risk Governance (MRG) workflow documentation (blocked by JS-rendering/robots.txt across three separate domains and access attempts), and (2) named human role titles for two runtime-approval contexts (watsonx Orchestrate agent governance; financial-services MRM sign-off). Both are documented in `knowledge_gaps.md` rather than filled by invention, per RAS Section 15.

Research is judged to have reached practical saturation for the purpose of constructing eight evidence-backed, non-overlapping Hybrid Intelligence scenarios sufficient for the next pipeline phase (Knowledge Graph construction).
