# Research Log — IBM watsonx.governance
Research Acquisition Specification (RAS) v1.0 | Phase: Domain Knowledge Acquisition and Structured System Analysis
Session date: 2026-08-24

This log documents every search step performed during this knowledge-acquisition phase, per protocol §14. Search engine used throughout: the session's integrated web search tool (Google-backed web index) plus direct page fetches of URLs surfaced by search.

---

## Search 1

- **Objective:** Establish baseline understanding of watsonx.governance from official sources.
- **Search terms:** `IBM watsonx.governance official product overview documentation`
- **Search engine:** Web search (integrated)
- **Sources visited:** ibm.com/products/watsonx-governance; ibm.com/docs/en/watsonx/saas (overview); github.com/IBM/ibm-watsonx-gov; heidloff.net article
- **Sources rejected:** Microsoft Marketplace listing (reseller listing, not primary documentation); UK Digital Marketplace G-Cloud listing (procurement listing, not technical content)
- **Sources accepted:** E-001, E-002, E-005 (fetched in later steps)
- **Information extracted:** Product exists as part of the broader "watsonx" family (watsonx.ai, watsonx.data, watsonx.governance); positioned as enterprise AI governance/GRC tooling.
- **Ontology concepts discovered:** hi:UseCase, hi:HITeam (implied), hi:Context
- **Scenarios supported:** General platform-overview scenario framing (all scenarios)
- **Remaining unknowns after this search:** Specific roles, tasks, metrics, lifecycle stages.

## Search 2

- **Objective:** Identify the AI-governance lifecycle and model-risk terminology used by the product.
- **Search terms:** `watsonx.governance IBM AI governance lifecycle model risk`
- **Search engine:** Web search (integrated)
- **Sources visited:** ibm.com/docs governance-console page (403 error); ibm.com/products/watsonx-governance; dataplatform.cloud.ibm.com xgov-plan.html (500 error); Medium (Shuvanker Ghosh); Incede.ai glossary; BizTech Magazine; DeepInspect blog; Nexright blog
- **Sources rejected:** Incede.ai (glossary/marketing site, no primary evidence, Tier not sufficiently high given official/technical alternatives existed); DeepInspect (third-party competitor-analysis blog, opinionated framing); Nexright (marketing-style blog)
- **Sources accepted:** E-008 (BizTech Magazine, fetched later)
- **Information extracted:** Confirms model-risk governance is a first-class concept; financial-institution framing.
- **Ontology concepts discovered:** hi:Context (regulated industry), hi:HumanAgent (risk/compliance roles, to be confirmed)
- **Scenarios supported:** Scenario 1 (Predictive Credit-Risk Model Governance)
- **Remaining unknowns:** Exact governance-console workflow mechanics (blocked by 403/500 errors — logged for follow-up).

## Search 3 (direct fetch)

- **Objective:** Extract full content of the official product page.
- **URL fetched:** https://www.ibm.com/products/watsonx-governance
- **Result:** Success. Extracted purpose statement, three pillars (Visibility/Control/Accountability), use cases, regulatory frameworks (EU AI Act, NIST AI, ISO 42001, Data & Trust Alliance), vendor-reported outcome statistics.
- **Accepted as:** E-001
- **Ontology concepts discovered:** hi:Goal (measurable business outcomes), hi:Context, hint:Domain

## Search 4 (direct fetch)

- **Objective:** Extract Governance-console workflow detail.
- **URL fetched:** https://www.ibm.com/docs/en/watsonx/w-and-w/2.4.x?topic=ai-managing-risk-compliance-governance-console
- **Result:** Failed — HTTP 403 client error. Logged as rejected source R-01.

## Search 5 (direct fetch)

- **Objective:** Extract AI-governance planning documentation (roles, lifecycle stages).
- **URL fetched:** https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/xgov-plan.html?context=wx
- **Result:** Failed — HTTP 500 "This page isn't available right now." Logged as rejected source R-02. Retried once later in the session (Search 12) with the same result.

## Search 6 (direct fetch)

- **Objective:** Extract SDK capability detail from the official watsonx.governance SDK repository.
- **URL fetched:** https://github.com/IBM/ibm-watsonx-gov and https://raw.githubusercontent.com/IBM/ibm-watsonx-gov/main/README.md
- **Result:** Partial success — confirmed SDK purpose ("evaluate AI applications and generate insights") but deeper metrics/evaluator listing not exposed in retrievable content.
- **Accepted as:** E-002
- **Ontology concepts discovered:** hi:ArtificialAgent (SDK as a governed tool), hi:Capability

## Search 7

- **Objective:** Find detailed metric definitions (fairness, drift, explainability, quality) used in predictive model monitoring.
- **Search terms:** `IBM watsonx.governance metrics fairness drift explainability quality documentation`
- **Search engine:** Web search (integrated)
- **Sources visited:** ibm.com/docs use-case page (403 error); Medium (Gautam Chutani); TechChannel; G2 reviews; DeepInspect; Aligne.ai; ASBResources; ibm.com pricing page
- **Sources rejected:** TechChannel (general "AI with IBM i" listicle, tangential); G2 (user reviews, not technical documentation — noted separately as a possible qualitative source but not cited); ASBResources, Aligne.ai (marketing-oriented blogs; used only for search triangulation, not cited)
- **Sources accepted:** E-003 (Gautam Chutani Medium article) — fetched and accepted
- **Information extracted:** Full description of Quality/Fairness/Drift/Explainability monitors, thresholds, LIME/SHAP.
- **Ontology concepts discovered:** hi:Capability, hint:Method, hint:Metric, hi:TaskExecution
- **Scenarios supported:** Scenario 1
- **Remaining unknowns:** Generative-AI-specific metrics (addressed in Search 8–9).

## Search 8

- **Objective:** Identify generative-AI evaluation metrics (HAP, PII, faithfulness, answer relevancy, hallucination).
- **Search terms:** `watsonx.governance generative AI evaluation metrics HAP PII faithfulness answer relevancy hallucination`
- **Search engine:** Web search (integrated)
- **Sources visited:** Medium (Sam Kwan); ibm.com agentic-AI announcement; Medium (Ravi Chamarthy, Evaluation Studio); ibm.com agentic-lifecycle announcement; ASBResources; Medium (Doug Stauber, "2.0" article); SalientProcess; heidloff.net (QA scenarios article); GitHub watson-openscale-samples notebook
- **Sources rejected:** SalientProcess (partner/reseller marketing page)
- **Sources accepted:** E-004, E-006, E-007, E-010, E-011 (fetched across this and following searches)
- **Information extracted:** Rich metric detail — Context Relevance, Faithfulness, Answer Similarity/Relevance, HAP, PII, prompt injection, Rouge/SARI/METEOR/BLEU (summarization), Unsuccessful answer rate, Detached Prompt Templates for third-party LLMs.
- **Ontology concepts discovered:** hi:Evaluation, hint:Metric, hi:Experiment, hi:hasMetricConcept
- **Scenarios supported:** Scenario 2, Scenario 4

## Search 9

- **Objective:** Confirm AI Factsheets purpose and model-lifecycle documentation practice.
- **Search terms:** `IBM AI Factsheets watsonx.governance model documentation lifecycle`
- **Search engine:** Web search (integrated)
- **Sources visited:** ClickUp blog; GitHub IBM/ai-governance-factsheet-samples; dataplatform xgov-plan.html (already rejected); ibm.com/products/watsonx-governance; dataplatform factsheets-model-inventory.html (500 error); IBM OpenPages MRG docs (403 error)
- **Sources rejected:** ClickUp blog (marketing/SEO content farm article about IBM's product, not authoritative)
- **Sources accepted:** None new from this search directly; corroborating detail found later in E-009
- **Information extracted:** Confirmed "AI Factsheets" as a named artifact-tracking mechanism; confirmed IBM OpenPages Model Risk Governance exists as a distinct sub-product (inaccessible for direct quotation — R-09).
- **Remaining unknowns:** OpenPages MRG workflow detail (never retrieved directly; substituted by E-013, which documents Model Risk Governance within the Governance Console rather than the standalone OpenPages product).

## Search 10 (direct fetches)

- **Objective:** Extract agentic-AI governance detail.
- **URLs fetched:** https://www.ibm.com/new/announcements/ibms-answer-to-governing-ai-agents-automation-and-evaluation-with-watsonx-governance ; https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/factsheets-model-inventory.html (500 error, rejected R-08)
- **Result:** First URL succeeded — detailed agentic evaluation metrics, agent lifecycle stages, governance challenges ("Agents have unsupervised autonomy...").
- **Accepted as:** E-004
- **Ontology concepts discovered:** hi:Agent (agentic), hi:TaskExecution, hi:Evaluation

## Search 11 (direct fetches)

- **Objective:** Extract independent technical-blog perspective and "what's new" release detail.
- **URLs fetched:** https://heidloff.net/article/watsonx-governance/ ; https://medium.com/ibm-data-ai/watsonx-governance-2-0-heres-what-s-new-8cf0889109e2
- **Result:** Both succeeded. heidloff.net confirmed OpenPages/OpenScale/AI-Factsheets architecture and the Users/Reviewers/Approvers role model. Medium "2.0" article confirmed multi-vendor support, RAG hallucination-detection metrics, and EU AI Act risk-tier categorization (Prohibited/High-Risk/Limited-Risk/Minimal-Risk).
- **Accepted as:** E-005, E-006
- **Ontology concepts discovered:** hint:Role (Reviewer, Approver, Use-case Owner), hint:Constraint (EU AI Act tiers), hi:Context

## Search 12 (direct fetches, retry)

- **Objective:** Retry previously failed governance-planning and agent-lifecycle pages; find governing-AI-agents lifecycle announcement.
- **URLs fetched:** https://www.ibm.com/new/announcements/agentic-ai-governance-evaluation-and-lifecycle ; https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/factsheets-model-inventory.html (still 500, retry failed)
- **Result:** First URL succeeded with rich detail on agent lifecycle stages, SME human-in-the-loop / red-teaming, and RAG-agentic metric list including tool-selection quality, system drift.
- **Accepted as:** E-007
- **Ontology concepts discovered:** hi:hasInteractionIntentConcept (red-teaming/verification intent), hi:HumanAgent (SME)

## Search 13 (direct fetch)

- **Objective:** Extract financial-services regulated-industry context.
- **URL fetched:** https://biztechmagazine.com/article/2025/12/ibms-watsonx-platform-goes-distance-ai-governance-financial-institutions
- **Result:** Success — regulatory context (MRM standards, audit requirements), stakeholder roles (risk/compliance teams, model validators/auditors), tasks (model tracking, production monitoring, bias detection, workflow automation).
- **Accepted as:** E-008
- **Ontology concepts discovered:** hint:Domain (banking, insurance), hi:HumanAgent

## Search 14

- **Objective:** Locate explicit named roles/personas (use case owner, model validator, risk officer) in official terminology.
- **Search terms:** `IBM AI Factsheets watsonx.governance model documentation lifecycle` (continued), `watsonx.governance "use case owner" OR "model validator" OR "model owner" OR "risk officer" role persona IBM`
- **Search engine:** Web search (integrated)
- **Sources visited:** Medium (Shuvanker Ghosh); Aligne.ai (x2 articles); ibm.com/docs SSLSRPV_latest wxgov_reference.html; ibm.com/docs SSLSRPV_2.1.x use-case-watsonx-gov.html (403); ibm.com Model Risk Evaluation Engine announcement; IBM OpenPages docs (403, two mirrors); jp-tok dataplatform wxgov_mrg_desc.html
- **Sources rejected:** Shuvanker Ghosh Medium article (not fetched in full — redundant with already-accepted higher-detail sources; time-boxed); Aligne.ai articles (marketing-style blog, used only for triangulation)
- **Sources accepted:** E-013, E-014 (fetched successfully)
- **Information extracted:** Three governance-console solutions (MRG/ORM/RCM), administrator profiles, inventory libraries (Use Case Library, Foundation Model Library, Discovered AI/"shadow AI" Library, AI Compliance Plan Library), Model Risk Evaluation Engine three-stage workflow (Understand/Identify/Evaluate), named authors/roles (Product Manager, Distinguished Research Staff Member).
- **Ontology concepts discovered:** hi:UseCase, hint:Role (MRG Master, ORM Master, RCM Master, Modules Master), hi:Task, hi:Evaluation, hi:Experiment
- **Scenarios supported:** Scenario 3, Scenario 5

## Search 15

- **Objective:** Locate real-world case studies to ground scenario modelling in documented deployments (protocol §15).
- **Search terms:** `watsonx.governance case study USTA Deloitte customer story AI risk`
- **Search engine:** Web search (integrated)
- **Sources visited:** ibm.com "Governing AI with Confidence" announcement; ibm.com client-quotes page; IntelligentHQ; BizTech (already accepted); techstories.ai; Aligne.ai; Deloitte IBM alliance page
- **Sources rejected:** IntelligentHQ (opinion/ethics-commentary article, not primary evidence); techstories.ai (SEO/content-marketing site); Deloitte alliance page (partner marketing page, no watsonx.governance-specific operational detail retrieved)
- **Sources accepted:** E-012 (fetched)
- **Information extracted:** Confirmed cross-functional team composition intent ("engineering, legal, compliance, risk, security, data and business teams"); named customer references (USTA, Deloitte) exist but detailed case-study content was not independently verified within this session — see `knowledge_gaps.md`.
- **Ontology concepts discovered:** hi:HITeam, hi:hasMember

## Search 16

- **Objective:** Locate the formal risk taxonomy underlying the Model Risk Evaluation Engine, prioritizing peer-reviewed literature per protocol §9 tier 6.
- **Search terms:** `IBM AI Risk Atlas watsonx.governance risk taxonomy categories`
- **Search engine:** Web search (integrated)
- **Sources visited:** ibm.github.io/ai-atlas-nexus; ibm.com/docs SSLSRPV_2.4.x ai-risk-atlas.html (403); arxiv.org/pdf/2503.05780 and arxiv.org/html/2503.05780; GitHub IBM/ai-atlas-nexus; techstories.ai; Aligne.ai
- **Sources rejected:** techstories.ai, Aligne.ai (marketing-style content, not needed given the arXiv paper was located)
- **Sources accepted:** E-015 (fetched via arxiv.org/abs/2503.05780)
- **Information extracted:** Five-category AI risk taxonomy (Training data, Inference, Output, Non-technical, Agentic); risk dimensions (accuracy, fairness, privacy, explainability); Risk Atlas Nexus open-source tooling; explicit statement that the taxonomy "supports IBM's watsonx.governance platform."
- **Ontology concepts discovered:** hint:Phenomenon, hint:Constraint, hi:hasPhenomenonConcept
- **Scenarios supported:** Scenario 3

## Search 17 (direct fetches)

- **Objective:** Confirm product-edition/tier structure and identify any role-differentiated feature gating.
- **URL fetched:** https://www.ibm.com/products/watsonx-governance/pricing
- **Result:** Success — Trial, Model Management, Risk & Compliance Basic/Advanced, and an AWS Marketplace edition; capability gating by tier (use case onboarding, model inventory/documentation, monitoring, concurrent users).
- **Accepted as:** E-016
- **Ontology concepts discovered:** hi:HITeam (concurrent users), hint:Role

## Search 18

- **Objective:** Determine how agentic-AI governance in watsonx.governance relates to the separate watsonx Orchestrate product (agent-building/runtime platform), to avoid conflating the two and to check for a documented integration.
- **Search terms:** `watsonx.governance watsonx orchestrate agent monitoring integration IBM`
- **Search engine:** Web search (integrated)
- **Sources visited:** ibm.com/docs watson-orchestrate monitoring-agents; ibm.com new-agentic-workflows-and-domain-agents announcement; ibm.com Orchestrate observability/governance announcement; ibm.com/products/watsonx-orchestrate; ibm.com Enforcement Tracking announcement; ibm.com/products/watsonx-orchestrate/governance-and-observability; IBM Mediacenter video page; HyperFRAME Research blog; IBM Agent Connect gateway page; ibm.com "Now GA: Monitor agents" announcement
- **Sources rejected:** HyperFRAME Research (independent analyst commentary blog — noted content but not cited as primary evidence given official pages were available); IBM Mediacenter video page (media asset, not text-extractable within session)
- **Sources accepted:** E-017
- **Information extracted:** watsonx Orchestrate provides a distinct "control plane" for agent operation, audit logs/traceability, policy/guardrail enforcement, identity/access control, and runtime performance metrics (accuracy, tool call reliability, completion rates, cost, safety). The explicit data-flow relationship between Orchestrate's runtime telemetry and watsonx.governance's Governance Console was **not stated explicitly** on the fetched page — flagged in `knowledge_gaps.md`.
- **Ontology concepts discovered:** hi:Interaction, hi:TaskExecution, hint:Metric

---

## Saturation Assessment

After 18 search iterations and 24 distinct URL fetch attempts (16 successful, 8 failed/rejected), the following saturation indicators were observed:

- The same core role model (use-case owner/requester → reviewer → approver; model validator/risk-and-compliance teams; developers/data scientists; SMEs performing red-teaming) recurred consistently across E-005, E-006, E-007, E-008, E-012, E-013.
- The same core metric families (Quality, Fairness/Bias, Drift, Explainability for predictive ML; Faithfulness, Answer Relevance/Similarity, Context Relevance, HAP, PII, Unsuccessful-request-rate, task-specific NLG metrics for generative AI; plus agent-specific metrics — tool selection quality, system drift, prompt injection) recurred consistently across E-003, E-004, E-006, E-007, E-009, E-010, E-011.
- The same architectural components (OpenPages / Model Risk Governance, OpenScale-derived monitoring, AI Factsheets, Evaluation Studio, Model Risk Evaluation Engine, AI Risk Atlas) recurred consistently across E-005, E-009, E-013, E-014, E-015.
- New searches (17, 18) began returning material that corroborated rather than added new concept categories, indicating approaching saturation for the **product-mechanics** layer.
- Saturation was **not fully reached** for: (a) internally verified customer case-study detail beyond name-drops (USTA, Deloitte); (b) official demo/conference-presentation transcripts; (c) whitepaper-format documents; (d) several official IBM Docs pages that returned persistent HTTP 403/500 errors during this session. These are documented as explicit gaps in `knowledge_gaps.md` rather than filled with unsupported inference, per protocol §15–16.

Research was concluded at this point because: (1) the marginal new-concept yield per search had dropped to near zero across three consecutive search rounds, and (2) all classes and object/data properties in the supplied HI Ontology TTL (hi:HITeam, hi:UseCase, hi:Agent/HumanAgent/ArtificialAgent, hi:Goal, hi:Task, hi:Capability, hi:TaskExecution, hi:Interaction, hi:Context, hi:Evaluation, hi:Experiment) had at least one, and in most cases several, independent evidence-backed instantiations from the target use case.
