# Sources — IBM watsonx.governance

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **IBM watsonx.governance**
Complete source inventory for the Domain Knowledge Acquisition phase. Sources are listed in the order they were consulted. Each entry states Title, URL, Type, Quality Assessment, Relevance, and the Hybrid Intelligence (HI) ontology concepts it supports. Evidence IDs (E-0xx) assigned here are referenced throughout `scenarios.md`, `extractionsheet.csv`, `ontology_mapping.md`, and `knowledge_gaps.md`.

---

## A. ACCEPTED SOURCES

### E-001 — IBM watsonx.governance product page
- **Title:** IBM watsonx.governance
- **URL:** https://www.ibm.com/products/watsonx-governance
- **Type:** Official vendor documentation (product marketing/overview page)
- **Quality Assessment:** High. Primary vendor source; states the platform's three pillars, capabilities, and links to independently reported customer outcomes (Infosys, Careerforce Pro, US Open, internal IBM data-clearance use). Some figures (e.g., "150% increase in operational efficiency") are vendor-reported and unaudited.
- **Relevance:** Core scope definition for the whole use case.
- **Ontology concepts supported:** `hi:UseCase`, `hi:HITeam`, `hi:Goal`, `hi:Task` (shadow AI detection, policy enforcement, risk assessment), `hi:ArtificialAgent` (embedded AI assistants), `hi:Context` (regulatory: EU AI Act, NIST AI RMF, ISO 42001).

### E-002 — Managing risk and compliance with Governance console in IBM watsonx
- **URL:** https://www.ibm.com/docs/en/watsonx/w-and-w/2.4.x?topic=ai-managing-risk-compliance-governance-console
- **Type:** Official vendor documentation (IBM Docs)
- **Quality Assessment:** Medium. Page returned a server error (HTTP 500) on retrieval attempts within this research window; only the search-result meta-description could be captured ("You can use watsonx.governance Model Risk Governance (MRG) workflows as delivered or modify them to meet your requirements"). Recorded as accepted-but-partially-inaccessible; logged again in `knowledge_gaps.md`.
- **Relevance:** Governance console / MRG workflow customization.
- **Ontology concepts supported:** `hi:Task`, `hi:TaskExecution` (workflow customization).

### E-003 — Introduction to watsonx.governance (Niklas Heidloff)
- **URL:** https://heidloff.net/article/watsonx-governance/
- **Type:** Independent technical article by an IBM Distinguished Engineer (IBM-affiliated technologist, personal engineering blog)
- **Quality Assessment:** High. Precise, technically detailed, consistent with official IBM materials; describes the three underlying components (OpenPages, OpenScale, AI FactSheets) and the requester/reviewer/approver workflow pattern.
- **Relevance:** Architecture and governance-approval workflow foundations.
- **Ontology concepts supported:** `hi:HumanAgent` (requester, reviewer, approver), `hi:Task` (use-case approval), `hi:ArtificialAgent` (OpenScale monitoring engine), `hi:Capability` (no-code workflow/questionnaire editor).

### E-004 — Model Risk Governance solution in Governance console (MRG description)
- **URL:** https://dataplatform.cloud.ibm.com/docs/content/svc-watsonxgov/wxgov_mrg_desc.html?context=wx
- **Type:** Official vendor documentation (IBM Docs, Cloud Pak for Data / watsonx platform docs)
- **Quality Assessment:** Low-Medium (access-limited). Page returned only navigation chrome on fetch (dynamic/JS-rendered SPA content not retrievable via automated fetch); substantive MRG description could not be extracted. Accepted as a confirmed-to-exist official source (title/URL verified via search) but content is a documented gap.
- **Relevance:** Model Risk Governance solution structure.
- **Ontology concepts supported:** none extractable beyond existence of `hi:Task` "Model Risk Governance."

### E-005 — Agentic AI governance, evaluation and lifecycle (IBM announcement)
- **URL:** https://www.ibm.com/new/announcements/agentic-ai-governance-evaluation-and-lifecycle
- **Type:** Official vendor documentation (IBM product announcement)
- **Quality Assessment:** High. Direct vendor statement of agent-lifecycle governance stages, named evaluation metrics, and explicit human-in-the-loop mechanism ("Human feedback or red teaming").
- **Relevance:** Core evidence for the Agentic AI Governance scenario (Scenario 5).
- **Ontology concepts supported:** `hi:Task` (risk assessment, tool performance measurement, production monitoring), `hi:Capability` (evaluation metrics with benchmarks), `hi:HumanAgent` (SMEs / red teamers), `hi:ArtificialAgent` (agents, tools, Governed Agentic Catalog), `hi:Interaction` (human feedback/red-teaming episodes), `hi:Evaluation`/`hi:Experiment` (Experimentation Studio).

### E-006 — Predictive Model Monitoring with IBM watsonx.governance (Gautam Chutani)
- **URL:** https://gautam75.medium.com/predictive-model-monitoring-with-ibm-watsonx-governance-c182b0c6095f
- **Type:** Engineering blog (Medium, technical walkthrough, non-IBM-employee community author)
- **Quality Assessment:** High. Detailed, step-by-step, technically consistent with official terminology (OpenScale, AI FactSheets, OpenPages); walks through a full end-to-end predictive-model workflow.
- **Relevance:** Core evidence for Scenario 1 (predictive ML model lifecycle governance).
- **Ontology concepts supported:** `hi:Task` (model inventory creation, training, deployment, monitoring configuration), `hi:ArtificialAgent` (AutoAI, OpenScale monitors, SHAP/LIME explainer), `hi:Capability` (fairness/drift/quality/explainability evaluation), `hi:HumanAgent` (stakeholders resolving issues), `hi:Evaluation` (thresholds, alerts).

### E-007 — Use case approval workflows for generative AI (Prasath K, IBM Community blog)
- **URL:** https://community.ibm.com/community/user/blogs/prasath-k/2025/07/29/use-case-approval-workflows-for-generative-ai
- **Type:** IBM engineering/community blog (hosted on official community.ibm.com domain)
- **Quality Assessment:** High. Hosted on IBM's own community platform; details a concrete five-step methodology with named reviewer roles (Legal, Data Protection, Brand) for a generative-AI (email generation) use case.
- **Relevance:** Core evidence for Scenario 3 (GenAI use-case onboarding & risk classification).
- **Ontology concepts supported:** `hi:Task` (use case creation, custom field configuration, risk assessment via questionnaire), `hi:HumanAgent` (Legal, Data Protection, Brand, Stakeholder reviewers), `hi:Context` (GDPR, brand risk, regulatory exposure), `hi:Interaction` (multi-stage stakeholder review).

### E-008 — watsonx.governance 2.0 — here's what's new (Doug Stauber)
- **URL:** https://medium.com/ibm-data-ai/watsonx-governance-2-0-heres-what-s-new-8cf0889109e2
- **Type:** IBM engineering blog ("IBM Data Science in Practice" — official IBM Medium publication; author is an IBM offering manager)
- **Quality Assessment:** High. Vendor-authored release-notes-style article; names exact RAG metrics with formulas/ranges and describes the AI Model Risk Assessment and EU AI Act Applicability Assessment features precisely.
- **Relevance:** Core evidence for RAG metrics (Scenario 2) and EU AI Act risk classification (Scenario 3).
- **Ontology concepts supported:** `hi:Capability`/metric concepts (Faithfulness, Answer Relevance, Unsuccessful Requests), `hi:Task` (EU AI Act applicability assessment, AI model risk assessment), `hi:Context` (EU AI Act risk categories: Prohibited/High/Limited/Minimal).

### E-009 — Factsheets for AI Services (IBM Research blog)
- **URL:** https://www.research.ibm.com/blog/factsheets-ai
- **Type:** Official AI transparency documentation (IBM Research blog, foundational research announcement)
- **Quality Assessment:** High. Primary origin source for the AI FactSheets concept that underlies watsonx.governance's model-documentation capability; explicitly frames the trust/transparency rationale.
- **Relevance:** Establishes the conceptual and evidentiary basis for the FactSheets artifact used across nearly every scenario.
- **Ontology concepts supported:** `hi:Task` (documentation authoring), `hi:HumanAgent` (AI service developers/providers), `hi:Context` (trust, fairness, robustness, explainability, lineage — CARE-relevant).

### E-009b — Factsheets: Increasing Trust in AI Services through Supplier's Declarations of Conformity (IBM Research publication / arXiv)
- **URL:** https://arxiv.org/pdf/2006.13796v1
- **Type:** Peer-reviewed / preprint research paper (Arnold, Bellamy, Hind, et al., IBM Research, 2019)
- **Quality Assessment:** High. Peer-reviewed-adjacent (widely cited AI-governance paper) formal academic source underpinning the FactSheets/SDoC concept implemented in watsonx.governance.
- **Relevance:** Academic grounding for the FactSheets artifact and its evaluation dimensions (fairness, explainability, robustness, lineage).
- **Ontology concepts supported:** `hi:Goal` (trust), `hi:Task` (declaration/documentation), `hi:Context` (AI supply-chain accountability).

### E-009c — A Human-Centered Methodology for Creating AI FactSheets (IBM Research publication)
- **URL:** https://research.ibm.com/publications/a-human-centered-methodology-for-creating-ai-factsheets
- **Type:** Peer-reviewed research paper (IBM Research)
- **Quality Assessment:** High. Confirms FactSheet creation as a human-centered task with defined authoring/review process — directly supports modelling `hi:Task` "Author FactSheet" as a human task supported by AI tooling.
- **Relevance:** Human-task grounding for FactSheets authoring across scenarios.
- **Ontology concepts supported:** `hi:HumanAgent`, `hi:Task`, `hi:Capability` (documentation).

### E-010 — AI risk atlas (IBM watsonx Docs)
- **URL:** https://dataplatform.cloud.ibm.com/docs/content/wsj/ai-risk-atlas/ai-risk-atlas.html?context=wx
- **Type:** Official vendor documentation
- **Quality Assessment:** Medium (access-limited). Full body content not retrievable (JS-rendered SPA); only the meta-description was captured: "Explore this atlas to understand some of the risks of working with agentic AI, generative AI, and machine learning models."
- **Relevance:** Supports the existence of a structured risk taxonomy (`hint:Constraint`/`hint:Phenomenon` concepts) used during risk assessment tasks.
- **Ontology concepts supported:** `hi:Context` (risk taxonomy reference), `hint:Constraint`, `hint:Phenomenon`.

### E-011 — GitHub: IBM/ibm-watsonx-gov
- **URL:** https://github.com/IBM/ibm-watsonx-gov
- **Type:** Official vendor documentation (open-source SDK repository, IBM organization on GitHub)
- **Quality Assessment:** Medium (access-limited). Repository confirmed to exist and belongs to the official IBM GitHub organization; only the one-line description ("capabilities to evaluate AI applications and generate insights") was retrievable, plus confirmation of a `/samples/notebooks` directory. Full README not captured — logged as a gap.
- **Relevance:** Confirms a programmatic/SDK artificial-agent capability (metrics evaluator) usable at development time, independent of the SaaS UI.
- **Ontology concepts supported:** `hi:ArtificialAgent` (evaluator SDK), `hi:Capability` (evaluation).

### E-012 — Securing your prompts from Adversarial Attacks using IBM watsonx.governance (Manish Bhide)
- **URL:** https://medium.com/trusted-ai/securing-your-prompts-from-adversarial-attacks-using-ibm-watsonx-governance-df00d6b225c7
- **Type:** IBM engineering blog ("Trusted AI" — IBM-affiliated Medium publication; author is an IBM Distinguished Engineer / IBM Research)
- **Quality Assessment:** High. Precise technical description of prompt-injection/leakage detection, scoring, and the red-teaming-to-hardening remediation loop.
- **Relevance:** Core evidence for Scenario 4 (adversarial robustness red-teaming).
- **Ontology concepts supported:** `hi:Task` (red teaming, prompt hardening), `hi:ArtificialAgent` (red-teaming evaluator), `hi:Evaluation` (Adversarial Robustness Score, Prompt Leakage Risk Score), `hi:HumanAgent` (application engineer/prompt engineer).

### E-013 — Monitoring Virtual Assistants with IBM watsonx.governance (Aakanksha Joshi)
- **URL:** https://medium.com/ibm-data-ai/monitoring-virtual-assistants-with-ibm-watsonx-governance-b6865b23db42
- **Type:** IBM engineering blog ("IBM Data Science in Practice")
- **Quality Assessment:** High. Names exact metrics (PII, HAP, ROUGE, METEOR, Readability) with definitions and describes the automatic payload-logging and alerting mechanism.
- **Relevance:** Core evidence for Scenario 6 (production monitoring of conversational AI).
- **Ontology concepts supported:** `hi:TaskExecution` (payload logging), `hi:Evaluation` (metric thresholds/alerts), `hi:HumanAgent` (SMEs providing ground truth, engineers reviewing alerts).

### E-014 — Model Governance — IBM watsonx.governance (product sub-page)
- **URL:** https://www.ibm.com/products/watsonx-governance/model-governance
- **Type:** Official vendor documentation
- **Quality Assessment:** High. Direct vendor description of the three model-governance capabilities (tracking/transparency, evaluation/documentation, monitoring) and the "nutrition label" FactSheet metaphor.
- **Relevance:** Cross-cutting evidence for FactSheets and monitoring across Scenarios 1, 2, 8.
- **Ontology concepts supported:** `hi:Task` (evaluation, documentation, monitoring), `hi:Context` (multi-cloud: Bedrock, Azure, OpenAI).

### E-015 — Evaluating and analysing RAG Application with IBM watsonx.governance (Pratap V)
- **URL:** https://medium.com/trusted-ai/evaluating-and-analysing-rag-application-with-ibm-watsonx-governance-aef0a5d0e971
- **Type:** IBM engineering blog ("Trusted AI")
- **Quality Assessment:** High. Detailed enumeration of retrieval metrics (Context Relevance, Retrieval Precision, Average Precision, Hit Rate, NDCG) and answer metrics (Faithfulness, Answer Relevance, Answer Similarity, Unsuccessful Requests), plus the "RAG circles" root-cause-analysis UI and source-attribution explainability feature.
- **Relevance:** Core evidence for Scenario 2 (RAG application quality evaluation).
- **Ontology concepts supported:** `hi:TaskExecution` (development-phase and production-phase evaluation), `hi:Evaluation`/`hi:Experiment` (LLM-as-judge vs fine-tuned slate-model judge), `hi:HumanAgent` (validators), `hi:Interaction` (root-cause drill-down, source attribution review).

### E-016 — Careerforce Pro case study (IBM)
- **URL:** https://www.ibm.com/case-studies/careerforce-pro
- **Type:** Official vendor case study
- **Quality Assessment:** High for qualitative workflow description; Medium for quantitative outcome claims (vendor-reported, not independently audited).
- **Relevance:** Core evidence for Scenario 7 (AI-governed recruitment screening).
- **Ontology concepts supported:** `hi:HumanAgent` (hiring managers, recruiters, HR leaders), `hi:ArtificialAgent` (IRIS voice assistant, watsonx.ai model), `hi:Task` (résumé parsing, scoring, screening call, interview coordination), `hi:Goal` (reduce time-to-hire), `hi:Evaluation` (bias/drift detection).

### E-017 — IBM watsonx.governance use case (IBM Docs, SaaS)
- **URL:** https://www.ibm.com/docs/en/watsonx/saas?topic=cases-watsonxgovernance-use-case
- **Type:** Official vendor documentation
- **Quality Assessment:** High. Clean enumeration of six named personas (Business Analyst, Data Scientist, Prompt Engineering Team, ML Engineer, ModelOps Engineer, Data Analyst) mapped to specific tasks and tools (Projects, Spaces, Factsheets, Watson OpenScale).
- **Relevance:** Primary persona/role source reused across Scenarios 1, 2, 8.
- **Ontology concepts supported:** `hi:HumanAgent` (all six personas), `hi:Task` (track, evaluate, monitor), `hi:ArtificialAgent` (Watson OpenScale).

### E-018 — AI agent governance and observability — watsonx Orchestrate
- **URL:** https://www.ibm.com/products/watsonx-orchestrate/governance-and-observability
- **Type:** Official vendor documentation
- **Quality Assessment:** Medium-High. Clear on capability claims (audit logs, policy/guardrail enforcement, agent metrics) but does not name specific human roles/titles or granular approval steps — logged as a partial gap.
- **Relevance:** Supplementary evidence for Scenario 5 (agentic AI governance), specifically the runtime/observability side.
- **Ontology concepts supported:** `hi:Context` (centralized operational layer), `hi:Evaluation` (accuracy, tool-call reliability, completion rate, cost, safety).

### E-019 — Governing 3rd Party Machine Learning and Generative AI models Using IBM watsonx.governance (Sam Kwan)
- **URL:** https://medium.com/@samkwan815/governing-3rd-party-machine-learning-and-generative-ai-models-using-ibm-watsonx-governance-1bf55fa19c5b
- **Type:** Engineering blog (Medium, community author)
- **Quality Assessment:** High. Technically precise, includes concrete integration mechanism (custom ML provider / proxy endpoint, detached prompt templates) and a full metrics enumeration across ML and GenAI dimensions, including a "Human Rating/Voting score" custom metric.
- **Relevance:** Core evidence for Scenario 8 (multi-cloud / third-party model governance).
- **Ontology concepts supported:** `hi:Task` (metadata logging, subscribing model, proxy translation), `hi:ArtificialAgent` (third-party models: VertexAI, Bedrock, Azure, OpenAI), `hi:Evaluation` (fairness, quality, drift, explainability, PII/HAP, RAG metrics), `hi:Interaction` (Human Rating/Voting as an interaction-derived metric).

### E-020 — IBM watsonx.governance for management and performance assurance of AI models — A prescriptive approach (Shuvanker Ghosh)
- **URL:** https://medium.com/@shuvanker.ghosh/ibm-watsonx-governance-b16ca5ed95d2
- **Type:** Engineering blog (Medium, community author)
- **Quality Assessment:** High. Provides the clearest six-stage prescriptive workflow (Propose → Build → Evaluate/Approve → Deploy → Monitor/Manage → Operationalize) with five named roles including "Model Risk Officer."
- **Relevance:** Core evidence for Scenario 8 (model risk governance) and cross-cutting workflow structure.
- **Ontology concepts supported:** `hi:HumanAgent` (Model Requestor/Owner, Model Developer/Prompt Engineer, Model Validator/Reviewer, ModelOps Engineer, Model Risk Officer), `hi:Task` (six lifecycle stages), `hi:Evaluation` (quality-metric list).

### E-021 — Explainability using SHAP in IBM Watson OpenScale (Pratap V)
- **URL:** https://medium.com/trusted-ai/explainability-using-shap-in-ibm-watson-openscale-55548adedf38
- **Type:** IBM engineering blog ("Trusted AI")
- **Quality Assessment:** High. Precise technical definition of SHAP values, local vs. global explanations, and the stability metric (NDCG-based) used to monitor explanation consistency over time.
- **Relevance:** Explainability evidence supporting Scenario 1 and the CARE "Explainable" dimension.
- **Ontology concepts supported:** `hi:Capability` (explainability), `hi:TaskExecution` (local/global explanation generation), `hi:Evaluation` (stability metric).

### E-022 — IBM's watsonx Platform Goes the Distance on AI Governance for Financial Institutions (BizTech Magazine)
- **URL:** https://biztechmagazine.com/article/2025/12/ibms-watsonx-platform-goes-distance-ai-governance-financial-institutions
- **Type:** High-quality technical/trade press article (sponsored-adjacent industry publication, not primary vendor source)
- **Quality Assessment:** Medium. Independent framing of financial-services model-risk-management (MRM) regulatory context; explicitly states "keeping human risk oversight in the loop" but does not name specific role titles or granular workflow steps.
- **Relevance:** Regulatory/context evidence for Scenario 8.
- **Ontology concepts supported:** `hi:Context` (banking/insurance MRM standards, multi-jurisdiction compliance), `hi:HumanAgent` (human risk oversight, unnamed role).

---

## B. REJECTED / DOWN-WEIGHTED SOURCES

| Title | URL | Reason for rejection / down-weighting |
|---|---|---|
| IBM watsonx.governance Reviews — G2 | https://www.g2.com/products/ibm-watsonx-governance/reviews | Crowd-sourced review site; not vendor, engineering, or research documentation. Used only to corroborate feature names already found elsewhere, not cited directly. |
| Watsonx.governance Explained (Nexright) | https://nexright.com/watsonx-governance-responsible-ai-regulated-industries/ | Third-party marketing/consulting content, no primary evidence beyond what official docs already provide. |
| From Black Box to Trusted Advisor (ASB Resources) | https://asbresources.com/from-black-box-to-trusted-advisor-how-watsonx-governance-is-making-ai-decisions-auditable-and-ethical/ | Marketing-oriented consulting blog; redundant with E-001/E-014. |
| Why watsonx.governance is The Missing Piece (ASB Resources) | https://asbresources.com/why-watsonx-governance-is-the-missing-piece-in-responsible-genai-deployment/ | Same as above — marketing content, not used as primary evidence. |
| From Policy to Practice (Aligne.ai) | https://www.aligne.ai/blog-posts/from-policy-to-practice-operationalising-responsible-ai-with-ibm-watsonx | Consulting-partner marketing content; not cited. |
| Why AI Governance is No Longer Optional (Aligne.ai) | https://www.aligne.ai/blog-posts/why-ai-governance-is-no-longer-optional-preparing-for-eu-ai-act-with-ibm-watsonx-governance | Consulting-partner marketing content; not cited. |
| AI Agent Bias Auditing in 2025 (Markaicode) | https://markaicode.com/ai-agent-bias-auditing-fairness-ibm-watsonx-governance-toolkit/ | Low-provenance blog aggregator; content not independently verifiable against official docs, excluded. |
| IBM AI Governance: Where watsonx.governance Fits (DeepInspect) | https://www.deepinspect.ai/blog/ibm-ai-governance | Competitor-authored comparison blog; potential bias, used only as background awareness, not cited as evidence. |
| AI Ethics And Governance Principles (IntelligentHQ) | https://www.intelligenthq.com/ai-ethics-and-governance-principles-the-case-study-of-watsonx-governance-model-by-ibm/ | General-audience opinion article; no new factual content beyond official sources. |
| Managing risk and compliance with Governance console (dataplatform.cloud.ibm.com mirror) | https://dataplatform.cloud.ibm.com/docs/content/svc-watsonxgov/wxgov_mrg_example_workflow.html?context=wx&audience=wdp | Fetch returned only navigation chrome (JavaScript-rendered SPA); substantive content inaccessible via automated retrieval in this research window. Logged in `knowledge_gaps.md`. |
| Generative AI quality evaluations (dataplatform.cloud.ibm.com) | https://dataplatform.cloud.ibm.com/docs/content/wsj/model/wos-monitor-gen-quality.html?context=wx | Returned HTTP 500 on all fetch attempts. Logged in `knowledge_gaps.md`. |
| Completing an applicability assessment (dataplatform.cloud.ibm.com) | https://dataplatform.cloud.ibm.com/docs/content/svc-watsonxgov/wxgov_assessing_applic.html?context=wx | Not fetched in full (time/robustness constraints after repeated JS-rendering failures on the same domain); EU AI Act applicability content instead sourced from E-008. Logged as partial gap. |
| watsonx.governance: Governed Agentic Catalog demo (IBM Mediacenter) | https://mediacenter.ibm.com/media/watsonx.governance:+Governed+Agentic+Catalog+demo/1_yz4v2n5i | Blocked by the site's robots.txt; video transcript not retrievable via automated tools. Logged as a gap — a genuine product demo source that could not be accessed. |

---

## C. SOURCE COUNT SUMMARY

- Accepted sources cited with extracted evidence: **22** (E-001–E-022, including sub-entries E-009b, E-009c)
- Rejected / down-weighted sources: **13**
- Official vendor documentation: 9 accepted
- IBM-affiliated engineering blogs (Medium: "IBM Data Science in Practice," "Trusted AI," community.ibm.com): 8 accepted
- Independent/community technical blogs: 2 accepted
- Peer-reviewed / IBM Research academic publications: 3 accepted
- Trade press: 1 accepted
