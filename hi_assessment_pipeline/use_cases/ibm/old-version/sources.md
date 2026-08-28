# Sources Inventory — IBM watsonx.governance
Research Acquisition Specification (RAS) — Neuro-Symbolic AI for Assessing and Improving Hybrid Intelligence Systems
Target Use Case: IBM watsonx.governance | Version 1.0 | Compiled: 2026-08-24

This file is the master source-of-truth for every piece of evidence used across `scenarios.md`, `ontology_mapping.md`, and `extractionsheet.csv`. Every Evidence ID (E-###) defined here is referenced, never redefined, elsewhere in the package.

---

## 1. Accepted Sources (used as evidence)

### E-001
- **Title:** IBM watsonx.governance (product page)
- **URL:** https://www.ibm.com/products/watsonx-governance
- **Type:** Official vendor documentation (product marketing/overview page)
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High authority (primary vendor source) but promotional in tone; quantitative claims (e.g., "150% operational efficiency increase," "50% reduction in audit fees") are vendor-reported outcome statistics without independent methodology disclosed — treated as vendor claims, not independently verified facts.
- **Relevance:** Very High — defines product purpose, three pillars (Visibility/Control/Accountability), target users, use cases, regulatory frameworks supported.
- **Ontology Concepts Supported:** hi:UseCase, hi:HITeam, hi:Goal, hi:Context, hi:hasContextConcept, hint:Domain
- **Key quotation:** "IBM watsonx.governance helps enterprises govern any AI, anywhere with real-time visibility, enterprise controls, and continuous accountability, powered by AI-native governance and enterprise-grade GRC."
- **Key quotation:** "Use embedded AI assistants to onboard AI use cases, capture governance information and automate governance workflows directly within enterprise tools and conversational interfaces."
- **Key quotation:** The platform supports "EU AI Act, NIST AI, ISO 42001, and Data & Trust Alliance frameworks."

### E-002
- **Title:** GitHub - IBM/ibm-watsonx-gov (SDK repository landing page)
- **URL:** https://github.com/IBM/ibm-watsonx-gov
- **Type:** Official vendor engineering documentation (open-source SDK repository)
- **Source Priority Tier:** 2 (Engineering blog / repository of the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High authority, low depth — only the repository landing description was retrievable; deeper README content could not be fully rendered (see `knowledge_gaps.md`).
- **Relevance:** Medium — confirms an SDK exists specifically for evaluating AI applications and generating governance insights, i.e., a distinct hi:ArtificialAgent / hi:TaskExecution tool.
- **Ontology Concepts Supported:** hi:ArtificialAgent, hi:Capability, hi:TaskExecution
- **Key quotation:** "IBM watsonx.governance SDK provides capabilities to evaluate AI applications and generate insights."

### E-003
- **Title:** Predictive Model Monitoring with IBM watsonx.governance
- **Author:** Gautam Chutani
- **URL:** https://gautam75.medium.com/predictive-model-monitoring-with-ibm-watsonx-governance-c182b0c6095f
- **Type:** Technical article / engineering walkthrough (third-party, hands-on tutorial with screenshots)
- **Source Priority Tier:** 9 (High-quality technical article — used because it provides operational detail on monitor configuration not found on official pages that returned HTTP errors)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — practitioner-authored, procedurally detailed, internally consistent with official terminology (Fairness/Quality/Drift/Explainability monitors); not vendor-published so cannot be taken as authoritative on product roadmap, but reliable for describing product mechanics as they exist in the UI.
- **Relevance:** Very High — most detailed available description of the predictive-model monitoring workflow, thresholds, and explainability algorithms.
- **Ontology Concepts Supported:** hi:Capability, hi:Task, hi:TaskExecution, hi:Evaluation, hint:Metric, hint:Method
- **Key quotation:** "Drift refers to the decline in model performance due to changes in data or shifts in the relationships between inputs and outputs."
- **Key quotation:** Fairness metrics: "Disparate Impact (default, 80% threshold)" and "Statistical Parity Difference."
- **Key quotation:** Explainability: "LIME (Local Interpretable Model-Agnostic Explanations) – local predictions" and "SHAP (SHapley Additive exPlanations) – both local and global explanations."

### E-004
- **Title:** IBM's answer to governing AI Agents: Automation and Evaluation with watsonx.governance
- **URL:** https://www.ibm.com/new/announcements/ibms-answer-to-governing-ai-agents-automation-and-evaluation-with-watsonx-governance
- **Type:** Official vendor announcement / engineering blog (IBM Think / IBM "new" announcements channel)
- **Source Priority Tier:** 2 (Engineering blog of the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — vendor-authored, technically specific (named metrics, tech-preview date of 2025-03-03), explicit about maturity level ("possible... today," enhanced functionality "planned for later in 2025").
- **Relevance:** Very High — primary source for agentic-AI-specific evaluation metrics and governance workflow.
- **Ontology Concepts Supported:** hi:ArtificialAgent (agent), hi:TaskExecution, hi:Evaluation, hint:Metric, hi:Context
- **Key quotation:** "Context Relevance: Measures how well does the data retrieved by the model align with the question specified in the prompt."
- **Key quotation:** "Faithfulness... Higher scores indicate that the output is more grounded and less hallucinated."
- **Key quotation:** "Agents have unsupervised autonomy and can take actions that are at times harmful to organizations or their customers."

### E-005
- **Title:** Introduction to watsonx.governance
- **Author:** Niklas Heidloff (IBM developer advocate; independently published technical blog)
- **URL:** https://heidloff.net/article/watsonx-governance/
- **Type:** Technical blog (author has direct IBM technical affiliation; independently hosted, not an official ibm.com property)
- **Source Priority Tier:** 9 (High-quality technical article), treated with Tier-2-adjacent confidence given the author's domain expertise
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — precise, structured, consistent with official product architecture (OpenPages + OpenScale + AI Factsheets); explicitly names role types (Users, Reviewers, Approvers).
- **Relevance:** Very High — clearest available description of the three underlying components and the approval-workflow role model.
- **Ontology Concepts Supported:** hi:HumanAgent, hi:ArtificialAgent, hi:Interaction, hi:Task, hint:Role
- **Key quotation:** "IBM watsonx.governance was built to help you direct, manage and monitor the artificial intelligence (AI) activities of your organization."
- **Key quotation:** Three components: "OpenPages – A governance, risk and compliance solution... OpenScale – Monitoring capabilities... AI Factsheets – Documentation and metadata tracking."
- **Key quotation:** "Users requesting approvals for new use cases... Reviewers answering questionnaire-based assessments... Approvers with designated roles authorizing use cases."

### E-006
- **Title:** watsonx.governance 2.0 — here's what's new
- **Author:** Doug Stauber (IBM Data Science in Practice, Medium publication affiliated with IBM Data & AI)
- **URL:** https://medium.com/ibm-data-ai/watsonx-governance-2-0-heres-what-s-new-8cf0889109e2
- **Type:** Vendor-affiliated engineering blog (IBM Data & AI Medium publication)
- **Source Priority Tier:** 2 (Engineering blog of the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — names specific release details (GA mid-June 2024), explicit metric definitions, and EU AI Act risk-tier categories.
- **Relevance:** Very High — primary source for RAG hallucination-detection metrics and EU AI Act risk categorization.
- **Ontology Concepts Supported:** hi:Evaluation, hint:Metric, hi:Context, hint:Constraint, hi:Task
- **Key quotation:** "watsonx.governance can monitor all metrics, from quality to faithfulness to drift, regardless of the AI platform you are using."
- **Key quotation:** "Faithfulness: measures how faithful the model output is to the reference data provided." "Answer relevance: measures how relevant was the LLM output/response to the user query." "Unsuccessful requests: measures the ratio of questions answered unsuccessfully out of total questions."
- **Key quotation:** EU AI Act applicability tool categorizes systems as "Prohibited, High-Risk, Limited-Risk, or Minimal-Risk."

### E-007
- **Title:** Agentic AI governance, evaluation and lifecycle
- **URL:** https://www.ibm.com/new/announcements/agentic-ai-governance-evaluation-and-lifecycle
- **Type:** Official vendor announcement / engineering blog
- **Source Priority Tier:** 2 (Engineering blog of the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — vendor-authored, technically specific, explicitly distinguishes current vs. future capability ("Future releases will provide...").
- **Relevance:** Very High — primary source for agent lifecycle stages, human-in-the-loop / SME red-teaming role, and the RAG-agentic metric list.
- **Ontology Concepts Supported:** hi:HumanAgent (SME), hi:ArtificialAgent (agent), hi:Interaction, hi:TaskExecution, hi:Evaluation, hint:Metric, hi:hasInteractionIntentConcept
- **Key quotation:** The platform supports governance across "use case creation, development and validation to monitoring in production."
- **Key quotation:** "Human feedback or red teaming: Allows SMEs to observe and verify the agent's actions (human in the loop) and test agents for susceptibilities."
- **Key quotation:** RAG agentic metrics: "HAP, PII detection, prompt injection, context relevance, faithfulness, answer similarity, answer relevance, hit rate, average precision, reciprocal rank, and unsuccessful request tracking."
- **Key quotation:** "These metrics will be available by adding a simple python decorator to the tool node in a LangGraph application."

### E-008
- **Title:** IBM's watsonx Platform Goes the Distance on AI Governance for Financial Institutions
- **URL:** https://biztechmagazine.com/article/2025/12/ibms-watsonx-platform-goes-distance-ai-governance-financial-institutions
- **Type:** Trade/industry publication (independent editorial, not vendor-authored)
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — independent editorial voice, grounded in named regulatory concerns (model risk management standards, audit requirements); no primary data disclosed, journalistic synthesis of vendor + industry context.
- **Relevance:** High — best available evidence for the banking/insurance regulated-industry context and named stakeholder groups (risk/compliance teams, model validators/auditors).
- **Ontology Concepts Supported:** hi:HumanAgent (roles), hi:Context, hint:Domain (financial services), hi:Task
- **Key quotation:** "automated decisions may affect credit access, insurance pricing, trading behavior or anti-money laundering alerts."
- **Key quotation:** Risk/compliance teams must ensure "alignment to banking and insurance MRM standards, internal audit requirements and emerging AI regulations."
- **Key quotation:** "Evaluate models for potential bias — critical for fair lending, equitable insurance pricing."

### E-009
- **Title:** Governing AI models in watsonx.governance (model-governance product page)
- **URL:** https://www.ibm.com/products/watsonx-governance/model-governance
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High authority, promotional framing similar to E-001; concrete product-mechanic claims (factsheets, monitoring thresholds) are consistent with independently authored sources (E-003, E-011), which corroborates reliability.
- **Relevance:** Very High — defines AI Factsheets, gen-AI content-safety monitoring, and multi-vendor model support.
- **Ontology Concepts Supported:** hi:Task, hi:TaskExecution, hint:Task, hi:Capability, hi:Evaluation
- **Key quotation:** Factsheets are described as "'nutritional labels' for models" that "automatically log model information, performance metrics, and development activities throughout the lifecycle."
- **Key quotation:** The platform "monitor[s] both the inputs and the outputs of the gen AI model" with preset thresholds detecting "toxic language, hate speech, abusive language or profanity."
- **Key quotation:** Governs "gen AI models that are built on IBM watsonx.ai and models that are developed on third-party platforms, including Amazon Bedrock, Microsoft Azure and OpenAI."

### E-010
- **Title:** IBM watsonx.governance Evaluation Studio for Advanced Prompt Assessment
- **Author:** Ravi Chamarthy
- **URL:** https://ravi-chamarthy.medium.com/ibm-watsonx-governance-evaluation-studio-for-advanced-prompt-assessment-d18c41fb06ca
- **Type:** Technical article (practitioner walkthrough)
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — procedurally specific, names the "LLM-as-a-Judge" evaluation mechanism and a concrete example model (Mistral AI), consistent with official terminology found elsewhere (E-006, E-011).
- **Relevance:** High — best available description of Evaluation Studio as a developer-facing artificial-agent tool for comparative prompt/model assessment.
- **Ontology Concepts Supported:** hi:ArtificialAgent, hi:HumanAgent (LLM app developer), hi:Task, hi:Evaluation, hi:Experiment, hint:Metric
- **Key quotation:** "evaluate and compare generative AI assets using quality metrics and customizable criteria tailored to specific application needs."
- **Key quotation:** Metrics: "Faithfulness, Answer Relevance, Context Relevance, plus optional data safety checks (HAP and PII detection)."
- **Key quotation:** Primary users are "LLM application developers to evaluate and compare generative AI assets."

### E-011
- **Title:** Governing 3rd Party Machine Learning and Generative AI models Using IBM watsonx.governance
- **Author:** Sam Kwan
- **URL:** https://medium.com/@samkwan815/governing-3rd-party-machine-learning-and-generative-ai-models-using-ibm-watsonx-governance-1bf55fa19c5b
- **Type:** Technical article (practitioner walkthrough, IBM-affiliated author based on content depth)
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — the most operationally detailed single source found; enumerates exact metric names per task type (Rouge, SARI, METEOR, BLEU for summarization; Faithfulness, Answer Relevance, Unsuccessful answer rate for RAG) and the "Detached Prompt Template" mechanism for governing externally hosted generative models.
- **Relevance:** Very High — the richest single evidence source for capability/task/metric detail across both predictive ML and generative AI governance.
- **Ontology Concepts Supported:** hi:ArtificialAgent, hi:Task, hi:Capability, hi:TaskExecution, hi:Evaluation, hint:Metric, hint:Method
- **Key quotation:** "Trust: Aligning AI activities with core values enables organizations to develop systems that are transparent, fair, and trustworthy."
- **Key quotation:** ML monitoring dimensions: "Fairness/Bias... Quality... Drift... Explainability: Shapley values and LIME-based transaction explanations."
- **Key quotation:** Gen AI monitoring: "Evaluate if there is any Personal Identifiable Information (PII) or Hate, Abuse and Profanity (HAP) content in both the input prompt and LLM generated output."
- **Key quotation:** "Other than watsonx.ai models, watsonx.governance can also monitor third-party Generative AI model as a Detached Prompt Template."

### E-012
- **Title:** Governing AI with Confidence: Our Journey with watsonx.governance
- **URL:** https://www.ibm.com/new/announcements/governing-ai-with-confidence-our-journey-with-watsonx-governance
- **Type:** Official vendor announcement
- **Source Priority Tier:** 1/2 (Official vendor announcement)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium — largely promotional (Forrester Wave recognition, customer name-drops), but contains one directly usable statement about the cross-functional team composition the tool is designed to support.
- **Relevance:** Medium — supports the multi-stakeholder / HITeam composition concept.
- **Ontology Concepts Supported:** hi:HITeam, hi:hasMember, hint:Role
- **Key quotation:** "Our goal with watsonx.governance is to strengthen that collaboration by offering tools that support policy management, auditability and transparency throughout the AI lifecycle" across "engineering, legal, compliance, risk, security, data and business teams."

### E-013
- **Title:** Solution components in Governance console
- **URL:** https://www.ibm.com/docs/en/SSLSRPV_latest/svc-watsonxgov/wxgov_reference.html
- **Type:** Official vendor product documentation (IBM Docs)
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — direct reference documentation; enumerates the three governance-console solutions and their libraries precisely.
- **Relevance:** Very High — defines Model Risk Governance (MRG), Operational Risk Management (ORM), Regulatory Compliance Management (RCM) as the three constituent governance solutions, plus concrete artifact libraries (Use Case Library, Foundation Model Library, Discovered AI / "shadow AI" Library, AI Compliance Plan Library, AI Risk Library).
- **Ontology Concepts Supported:** hi:UseCase, hi:Agent, hi:Context, hint:Constraint, hi:hasConstraintConcept, hi:Task
- **Key quotation:** "Model Risk Governance (MRG): Manage all tracked models and prompt templates so that you can review all of your AI solutions across the AI lifecycle."
- **Key quotation:** "Operational Risk Management (ORM): Track model risk and other operational risks across the enterprise. Link use cases to business processes."
- **Key quotation:** "Discovered AI library for 'shadow AI' deployments not following governance practices."
- **Key quotation:** Risk questionnaires include "AI Model Onboarding Risk Identification," "AI Use Case Risk Identification," and EU AI Act applicability assessments drawing from a "predefined AI Risk Library."

### E-014
- **Title:** IBM enhances the capabilities of watsonx.governance with the new Model Risk Evaluation Engine
- **URL:** https://www.ibm.com/new/announcements/ibm-enhances-the-capabilities-of-watsonx-governance-with-the-new-model-risk-evaluation-engine
- **Type:** Official vendor announcement, co-authored with IBM Research
- **Source Priority Tier:** 1/2 (Official vendor announcement; authored jointly with IBM Research staff)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — named authors with disclosed roles (Marc Cassagnol, Product Manager; Michael Hind, Distinguished Research Staff Member), specific about capability scope and named risks (prompt injection, toxic output, jailbreaking, hallucination, bias, data provenance, reidentification).
- **Relevance:** Very High — defines the "Understand → Identify → Evaluate" onboarding workflow and links watsonx.governance directly to the AI Risk Atlas taxonomy (cf. E-015).
- **Ontology Concepts Supported:** hi:Task, hi:TaskExecution, hi:Evaluation, hi:Experiment, hint:Metric, hi:Context
- **Key quotation:** The engine works by "computing metrics related to risk dimensions from the AI Risk Atlas" enabling "comparison of risk metrics across different foundation models."
- **Key quotation:** Three-stage workflow: "Understand" (access AI Risk Atlas), "Identify" (three assessment types), "Evaluate" (quantitative risk-metric computation feeding back into the Governance Console).

### E-015
- **Title:** AI Risk Atlas: Taxonomy and Tooling for Navigating AI Risks and Resources
- **URL:** https://arxiv.org/abs/2503.05780
- **Type:** Peer-reviewed / preprint research paper (arXiv), authored by IBM Research
- **Source Priority Tier:** 6 (Peer-reviewed / research paper)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — formal research artifact with explicit taxonomy, motivating gap analysis, and open-source tooling (Risk Atlas Nexus) description; strongest available source for the theoretical risk-taxonomy underpinning watsonx.governance's Model Risk Evaluation Engine.
- **Relevance:** Very High — supplies the five-category AI risk taxonomy (training data, inference, output, non-technical, agentic) and named risk dimensions (accuracy, fairness, privacy, explainability) that watsonx.governance operationalizes.
- **Ontology Concepts Supported:** hint:Constraint, hint:Phenomenon, hi:hasPhenomenonConcept, hi:Context, hi:Evaluation
- **Key quotation:** "The lack of interoperability between [existing taxonomies] creates challenges for researchers, practitioners, and policymakers seeking to operationalise AI governance."
- **Key quotation:** Five categories: "Training data, Inference, Output, Non-technical, and Agentic" risks, each subdivided by "risk dimensions such as accuracy, fairness, privacy, and explainability."
- **Key quotation:** Risk Atlas Nexus provides "efficient execution of intermediate stages in the compliance workflow" for watsonx.governance.

### E-016
- **Title:** watsonx.governance purchasing options (pricing page)
- **URL:** https://www.ibm.com/products/watsonx-governance/pricing
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High authority for edition/tier structure; commercial in nature, so used only for structural facts (editions, feature gating by tier, concurrent-user concept), not for qualitative governance claims.
- **Relevance:** Medium — corroborates a tiered capability model (Model Management vs. Risk & Compliance Basic/Advanced) and the existence of "concurrent users" as an explicit multi-human-agent concept.
- **Ontology Concepts Supported:** hi:HITeam, hint:Role, hi:Capability
- **Key quotation:** Tiers include "Trial," "Model Management," "Risk & Compliance - Basic," "Risk & Compliance - Advanced," each gating capabilities such as "Use case onboarding," "Model inventory and documentation," and "Model monitoring."

### E-017
- **Title:** AI agent governance and observability — Watsonx Orchestrate
- **URL:** https://www.ibm.com/products/watsonx-orchestrate/governance-and-observability
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — official but page did not explicitly state the integration mechanism with watsonx.governance (noted as a gap); content is otherwise concrete (control-plane, audit logs, policy/guardrails, identity, performance metrics).
- **Relevance:** High — extends the agentic-governance picture from evaluation (E-004, E-007) to runtime operational control and audit.
- **Ontology Concepts Supported:** hi:Agent, hi:Interaction, hi:TaskExecution, hi:Evaluation, hint:Metric
- **Key quotation:** "Operate all your AI agents from a single control plane—no matter where they're built or run."
- **Key quotation:** "Understand every decision your agents make with full audit logs and traceability."
- **Key quotation:** Runtime metrics include "accuracy, tool call reliability and completion rates" plus "quality, accuracy, cost, and safety."

---

## 2. Rejected / Inaccessible Sources

These were identified as potentially relevant but could not be used as evidence, either because they returned HTTP errors on every attempt or because retrieved content was insufficient. Documented per protocol §14 ("Sources rejected — reason") and carried into `knowledge_gaps.md`.

| # | Title / URL | Reason Rejected |
|---|---|---|
| R-01 | Managing risk and compliance with Governance console — https://www.ibm.com/docs/en/watsonx/w-and-w/2.4.x?topic=ai-managing-risk-compliance-governance-console | HTTP 403 on fetch (IBM Docs bot-protection); content not retrievable during this session |
| R-02 | Planning for AI governance — https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/xgov-plan.html | Persistent HTTP 500 "This page isn't available right now" on repeated fetch |
| R-03 | Governing assets with watsonx.governance — https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/xgov-overview.html | Persistent HTTP 500 on repeated fetch |
| R-04 | Overview of the watsonx experience — https://www.ibm.com/docs/en/watsonx/saas?topic=overview-watsonx | HTTP 403 on fetch |
| R-05 | Governing assets with watsonx.governance (saas docs) — https://www.ibm.com/docs/en/watsonx/saas?topic=governing-ai | HTTP 403 on fetch |
| R-06 | IBM watsonx.governance use case — https://www.ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=cases-watsonxgovernance-use-case | HTTP 403 on fetch |
| R-07 | IBM watsonx.governance use case (SSLSRPV mirror) — https://www.ibm.com/docs/en/SSLSRPV_2.1.x/wsj/getting-started/use-case-watsonx-gov.html | HTTP 403 on fetch |
| R-08 | Using AI Factsheets for AI Governance — https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/factsheets-model-inventory.html | Persistent HTTP 500 on repeated fetch |
| R-09 | IBM OpenPages Model Risk Governance — https://www.ibm.com/docs/en/SSFUEU_9.0.0/op_grc_admin/c_adm_mrg.html | HTTP 403 on fetch |
| R-10 | wxgov mrg desc — https://jp-tok.dataplatform.cloud.ibm.com/docs/content/svc-watsonxgov/wxgov_mrg_desc.html | Page loaded but returned only a one-line meta-description; substantive body content (roles, workflow stages, risk tiers) was not present in the retrievable content |
| R-11 | (PDF) AI Governance and Ethics with IBM Watsonx: Ensuring Trustworthy AI Implementation — ResearchGate — https://www.researchgate.net/publication/393849929 | HTTP 429 (rate-limited) on fetch attempt; not retried further to respect source-server limits |
| R-12 | AI Risk Atlas (IBM Docs) — https://www.ibm.com/docs/en/SSLSRPV_2.4.x/wsj/ai-risk-atlas/ai-risk-atlas.html | HTTP 403 on fetch |
| R-13 | GitHub IBM/ibm-watsonx-gov raw README.md | Fetched successfully but the rendered content did not expose the deeper metrics/evaluator listing (page functions mainly as a landing/index page pointing to notebooks not individually fetched) |

Marketing/opinion sources encountered during search (e.g., Nexright, ASBResources, Cresco International, Aligne.ai, Incede.ai, TechChannel, ClickUp blog, DeepInspect, IntelligentHQ, HyperFRAME Research, G2 reviews) were **deliberately not used as evidentiary sources** per protocol §9 ("Avoid blogs, opinion articles or marketing material unless no better evidence exists"), since sufficient Tier-1/Tier-2/Tier-6/Tier-9 evidence was obtained. They were reviewed only as triangulation/pointer material during search and are not cited.

---

## 3. Source Priority Compliance Summary

| Priority Tier | Sources Obtained | Evidence IDs |
|---|---|---|
| 1 — Official vendor documentation | 6 | E-001, E-009, E-013, E-014 (co-authored), E-016, E-017 |
| 2 — Vendor engineering blog | 5 | E-002, E-004, E-006, E-007, E-012 |
| 3 — AI transparency documentation | 0 | Not located as a distinct document type; closest analogue is the AI Risk Atlas (E-015) and Factsheets (E-009) |
| 4 — Help/support documentation | 0 | Not separately located; overlaps with Tier-1 IBM Docs pages, several inaccessible (see Rejected Sources) |
| 5 — Official demos/presentations | 0 | Not located within session scope; see `knowledge_gaps.md` |
| 6 — Peer-reviewed research papers | 1 | E-015 |
| 7 — Conference talks | 0 | Not located; see `knowledge_gaps.md` |
| 8 — Whitepapers | 0 | Not located as a distinct downloadable whitepaper; see `knowledge_gaps.md` |
| 9 — High-quality technical articles | 5 | E-003, E-005, E-008, E-010, E-011 |
