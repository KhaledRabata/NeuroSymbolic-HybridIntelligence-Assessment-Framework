# Hybrid Intelligence Scenarios — IBM watsonx.governance

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **IBM watsonx.governance**
Eight standardised Hybrid Intelligence (HI) scenarios, each evidence-backed per RAS Section 15/16 (File 4). Every scenario is either explicitly documented or strongly supported by ≥2 independent sources; where a detail is Inferred rather than Observed, it is explicitly labelled with reasoning, supporting evidence, and confidence.

Evidence IDs (E-0xx) correspond to `sources.md`. Ontology class references correspond to `hiontology.ttl` and are elaborated in `ontology_mapping.md`.

---

## Scenario 1 — Predictive ML Model Lifecycle Governance & Monitoring

**Scenario Name:** Predictive Model Governance & Continuous Monitoring

**Description:** A financial or operational predictive model (e.g., a credit-risk or churn model) is proposed, trained, deployed, and continuously monitored for quality, fairness, drift, and explainability across its lifecycle using the OpenPages (governance/risk), Watson OpenScale (monitoring), and AI FactSheets (documentation) components of watsonx.governance. [Observed — E-003, E-006, E-014, E-017]

**Goal:** Ensure a deployed predictive model remains accurate, fair, and explainable in production, with a continuously updated, auditable record of its lifecycle. [Observed — E-006, E-014]

**Human Actors:**
- Business Analyst — proposes the use case [Observed — E-017]
- Data Scientist — builds, trains, and evaluates the model [Observed — E-017, E-006]
- ML Engineer — trains and prepares models for deployment [Observed — E-017]
- ModelOps Engineer — deploys models and evaluates performance [Observed — E-017]
- Data Analyst — reviews model decisions and explanations [Observed — E-017]
- Compliance/Audit stakeholders — resolve governance issues raised in workflow [Observed — E-006, E-001]

**Artificial Agents:**
- AutoAI (automated feature engineering / model training) [Observed — E-006]
- Watson OpenScale (continuous evaluation engine: accuracy, fairness, drift) [Observed — E-003, E-006]
- SHAP/LIME explainability engine (local & global explanations, stability metric) [Observed — E-006, E-021]
- AI FactSheets service (auto-updating lifecycle documentation) [Observed — E-006, E-009]

**Context:** Enterprise production deployment subject to internal risk-governance policy and (where applicable) external regulatory frameworks (NIST AI RMF, ISO 42001). [Observed — E-001; Inferred applicability to this specific scenario — Medium confidence, reasoning: E-001 states these frameworks generally, not tied specifically to predictive-model use cases, but predictive-model governance is the canonical MRM use case these frameworks target]

**Input Data:** Training data, deployment/payload (production inference) data, ground-truth/feedback data. [Observed — E-006]

**Knowledge Sources:** Model inventory metadata, AI FactSheet fields, historical performance baselines. [Observed — E-006, E-009]

**Processing Method:** Statistical evaluation (accuracy/precision/recall), fairness metrics (disparate impact, statistical parity difference), drift detection algorithms, SHAP/LIME-based explainability computation. [Observed — E-006, E-021]

**Processing Tasks:**
1. Create model inventory/use case in OpenPages [Observed — E-006]
2. Train model (AutoAI) [Observed — E-006]
3. Deploy trained model as REST endpoint [Observed — E-006]
4. Track model in AI FactSheets [Observed — E-006]
5. Configure OpenScale monitoring thresholds [Observed — E-006]
6. Evaluate against test data [Observed — E-006]
7. Monitor dashboards; resolve alerts [Observed — E-006]

**Interaction Points:** Data Scientist ↔ OpenScale (threshold configuration); Data Analyst ↔ explainability engine (reviewing local/global SHAP explanations); stakeholders ↔ OpenPages issue-tracking workflow (assign/track/resolve). [Observed — E-006, E-021]

**Outputs:** Deployed model endpoint; populated AI FactSheet; monitoring dashboard; fairness/drift/quality alerts; SHAP/LIME explanation reports. [Observed — E-006, E-021]

**Evaluation Metrics:** Accuracy, precision, recall; disparate impact, statistical parity difference (fairness); drift magnitude; throughput, latency (health); stability metric (NDCG-based, explanation consistency). [Observed — E-006, E-021]

**Required Capabilities:** Fairness Assessment, Drift Detection, Explainability, Model Evaluation, Documentation Authoring. [Observed — E-006, E-014]

**Decision Points:** Whether to promote model to production after evaluation; whether an alert requires remediation/retraining; issue assignment and resolution. [Observed — E-006]

**Feedback Mechanisms:** Real-time alerts on threshold breach feed back to human stakeholders, who can trigger retraining or reconfiguration. [Observed — E-006]

**Expected HI Characteristics (CARE):** Collaborative (Data Scientist + OpenScale share the evaluation task); Responsible (fairness/audit trail via OpenPages); Explainable (SHAP/LIME); Adaptive (threshold-driven feedback loop, though full closed-loop retraining automation is not explicitly documented for this scenario — Inferred as partial, Medium confidence, reasoning: E-006 documents alerting and issue-resolution but not an automatic retraining trigger).

**Evidence IDs:** E-003, E-006, E-009, E-014, E-017, E-021

---

## Scenario 2 — RAG-Based Generative AI Application Quality Evaluation & Validation

**Scenario Name:** RAG Application Quality Evaluation & Promotion-to-Production

**Description:** A Retrieval-Augmented Generation (RAG) application (e.g., an enterprise knowledge-base Q&A system) is evaluated at development time and validated before production promotion, using retrieval-quality and answer-quality metrics computed either by fine-tuned IBM "slate" evaluation models or by an LLM acting as judge. [Observed — E-015]

**Goal:** Minimize hallucination and maximize grounded, relevant answers before and after a RAG application reaches production. [Observed — E-008, E-015]

**Human Actors:**
- Developer (builds/refines the RAG pipeline) [Observed — E-015]
- Validator (reviews evaluation results in a validation environment, decides on production promotion) [Observed — E-015]

**Artificial Agents:**
- Retrieval component (context retriever) [Observed — E-015]
- Foundation model / LLM (answer generator) [Observed — E-015]
- Fine-tuned slate evaluation model (125M parameters, CPU/GPU) [Observed — E-015]
- LLM-as-Judge model (any watsonx.ai or external LLM) [Observed — E-015]

**Context:** Enterprise Q&A / knowledge-base application built on grounded external sources of knowledge; development, validation, and production environments as distinct governance stages. [Observed — E-015]

**Input Data:** User query, retrieved context passages, generated answer, (in production) logged payload of questions/contexts/answers. [Observed — E-015]

**Knowledge Sources:** External knowledge base / document store queried by the retrieval component; reference answers for similarity comparison. [Observed — E-015]

**Processing Method:** Embedding-based retrieval; LLM generation grounded on retrieved context; metric computation via slate model or LLM-as-judge. [Observed — E-015]

**Processing Tasks:**
1. Retrieve relevant context passages [Observed — E-015]
2. Generate grounded answer [Observed — E-015]
3. Compute retrieval metrics (Context Relevance, Retrieval Precision, Average Precision, Hit Rate, NDCG) [Observed — E-015]
4. Compute answer metrics (Faithfulness, Answer Relevance, Answer Similarity, Unsuccessful Requests) [Observed — E-008, E-015]
5. Validator reviews violations via "RAG circles" UI and root-cause analysis [Observed — E-015]
6. Promote to production / continue monitoring [Observed — E-015]

**Interaction Points:** Validator ↔ RAG-circles UI (drill-down on threshold violations); Validator ↔ source-attribution view (clicking an answer sentence to see supporting context, i.e., explainability review). [Observed — E-015]

**Outputs:** Metric scores (0–1 scale); root-cause analysis report; source-attribution mapping; production-readiness decision. [Observed — E-008, E-015]

**Evaluation Metrics:** Context Relevance, Retrieval Precision, Average Precision, Hit Rate, NDCG, Faithfulness, Answer Relevance, Answer Similarity, Unsuccessful Requests. [Observed — E-008, E-015]

**Required Capabilities:** Retrieval Evaluation, Text Quality Evaluation, Explainability (source attribution). [Observed — E-015]

**Decision Points:** Promote application from development to production; whether a specific violated transaction requires remediation. [Observed — E-015]

**Feedback Mechanisms:** Production payload logging continuously feeds new question/context/answer triples back into the evaluation loop. [Observed — E-015]

**Expected HI Characteristics (CARE):** Collaborative (Validator + Judge model share the quality-assessment task); Explainable (source attribution, root-cause analysis); Responsible (gated promotion to production); Adaptive (continuous production payload evaluation). [Observed — E-015]

**Evidence IDs:** E-008, E-015

---

## Scenario 3 — Generative AI Use-Case Onboarding, Risk Classification & EU AI Act Applicability Assessment

**Scenario Name:** GenAI Use-Case Approval & Regulatory Risk Classification

**Description:** Before a generative-AI application (e.g., an automated marketing email generator) can be built, it must be registered as a use case, classified for risk via a questionnaire-driven assessment (including EU AI Act applicability and risk category determination), and approved through a multi-stakeholder review workflow. [Observed — E-007, E-008]

**Goal:** Ensure only appropriately risk-assessed and approved GenAI use cases proceed to development, in alignment with the EU AI Act and internal policy. [Observed — E-007, E-008]

**Human Actors:**
- Business Stakeholder (requester, business validation) [Observed — E-007]
- Legal Reviewer (regulatory compliance review) [Observed — E-007]
- Data Protection Reviewer (data-authorization review) [Observed — E-007]
- Brand Team Reviewer (message-consistency review) [Observed — E-007]
- Approver (final sign-off) [Observed — E-003]

**Artificial Agents:**
- Embedded AI governance assistant (assists with onboarding/use-case capture) [Observed — E-001]
- Risk-assessment questionnaire engine (generates risk scores) [Observed — E-008]

**Context:** Regulatory environment governed by the EU AI Act (risk categories: Prohibited, High, Limited, Minimal) and internal policies (GDPR/data-protection, brand risk). [Observed — E-008, E-007]

**Input Data:** Use-case description (business context, stakeholder impact, success criteria), custom risk-classification fields (data-usage risk, content-generation scope, audience impact, regulatory exposure, brand-risk factors). [Observed — E-007]

**Knowledge Sources:** EU AI Act risk-category taxonomy; AI Risk Atlas (risk taxonomy reference for agentic/generative/ML risks). [Observed — E-008, E-010]

**Processing Method:** Structured multi-stage questionnaire completion; rule-based/threshold-based risk-category determination. [Observed — E-007, E-008]

**Processing Tasks:**
1. Use-case creation with business/technical documentation [Observed — E-007]
2. Custom field configuration for risk classification [Observed — E-007]
3. Multi-stage stakeholder review (Stakeholder → Legal → Data Protection → Brand) [Observed — E-007]
4. Risk assessment via questionnaire [Observed — E-007]
5. EU AI Act applicability & risk-category determination [Observed — E-008]
6. Development authorization / approval [Observed — E-007]

**Interaction Points:** Sequential/parallel multi-agent review episode among requester and each named reviewer role (a `hi:Interaction` involving ≥2 `hi:HumanAgent`s per the ontology's cardinality restriction). [Observed — E-007]

**Outputs:** Approved (or rejected) use case; risk score; EU AI Act risk-category label; documented compliance rationale. [Observed — E-007, E-008]

**Evaluation Metrics:** Risk score (questionnaire-derived); EU AI Act risk category (categorical: Prohibited/High/Limited/Minimal). [Observed — E-008]

**Required Capabilities:** Workflow Configuration (no-code questionnaire/workflow editor), Regulatory Applicability Assessment. [Observed — E-003, E-008]

**Decision Points:** Approve/reject use case at each review stage; final go/no-go for development. [Observed — E-007]

**Feedback Mechanisms:** Rejected or conditionally-approved use cases are returned to the requester for revision (workflow implies iteration, though an explicit "return-to-requester" loop is not verbatim documented — Inferred, Medium confidence, reasoning: standard multi-stage approval workflows of this kind, and the no-code workflow editor's explicit purpose of accommodating "organizational variation," together imply an iteration/resubmission path, but no source states this explicitly for GenAI use cases). [Partially Inferred — E-003, E-007]

**Expected HI Characteristics (CARE):** Collaborative (four distinct human reviewer roles + AI onboarding assistant); Responsible (regulatory risk classification, audit trail); Explainable (documented risk-assessment rationale). [Observed — E-007, E-008, E-001]

**Evidence IDs:** E-001, E-003, E-007, E-008, E-010

---

## Scenario 4 — Adversarial Robustness Red-Teaming of Prompt Templates

**Scenario Name:** Prompt Security Hardening via Automated Red-Teaming

**Description:** Before a prompt template is deployed, watsonx.governance performs automated red-teaming to detect susceptibility to prompt-injection and prompt-leakage attacks (at basic, intermediate, and advanced sophistication levels), scores the prompt's adversarial robustness, and guides a prompt engineer through a hardening-and-recompute remediation loop. [Observed — E-012]

**Goal:** Ensure a prompt template resists adversarial manipulation before production deployment. [Observed — E-012]

**Human Actors:**
- Prompt Engineer / Application Engineer — reviews red-teaming results and hardens the prompt [Observed — E-012]

**Artificial Agents:**
- Red-teaming evaluator (automated attack-generation and scoring engine) [Observed — E-012]
- The LLM under test (governed by the prompt template) [Observed — E-012]

**Context:** Pre-deployment development environment; threat model spans basic (no safety training), intermediate (instruction-forgetting, role-play/red-teaming-style attacks), and advanced (adversarial-suffix/encoding attacks) sophistication levels. [Observed — E-012]

**Input Data:** Prompt template, model parameters, inferencing configuration (minimal inputs required to run red-teaming). [Observed — E-012]

**Knowledge Sources:** Library of known prompt-injection and prompt-leakage attack patterns (implied by the described three-tier taxonomy). [Observed — E-012]

**Processing Method:** Automated red-teaming (adversarial probe generation), semantic-similarity scoring of responses against original system prompt (for leakage detection). [Observed — E-012]

**Processing Tasks:**
1. Initial red-teaming assessment against the prompt template [Observed — E-012]
2. Results analysis — which attacks succeeded [Observed — E-012]
3. Mitigation: add anti-leakage instructions and/or swap to a safety-trained model [Observed — E-012]
4. Recompute metrics to verify improvement [Observed — E-012]
5. Deployment gate: proceed only once scores clear a threshold [Observed — E-012]

**Interaction Points:** Prompt Engineer ↔ red-teaming evaluator (iterative review-and-harden loop). [Observed — E-012]

**Outputs:** Adversarial Robustness Score (0–1); Prompt Leakage Risk Score (0–1); recommendations for prompt hardening; hardened prompt template. [Observed — E-012]

**Evaluation Metrics:** Adversarial Robustness Score, Prompt Leakage Risk Score (semantic-similarity based). [Observed — E-012]

**Required Capabilities:** Adversarial Robustness (prompt-injection/leakage detection). [Observed — E-012]

**Decision Points:** Whether the hardened prompt clears the deployment threshold; which mitigation strategy to apply. [Observed — E-012]

**Feedback Mechanisms:** Recompute-after-hardening loop is an explicit, tight feedback cycle between human action (editing the prompt) and AI re-evaluation. [Observed — E-012]

**Expected HI Characteristics (CARE):** Collaborative (engineer + evaluator iterate together); Responsible (deployment gated on a safety threshold); Adaptive (iterative hardening based on evaluation feedback). [Observed — E-012]

**Evidence IDs:** E-012

---

## Scenario 5 — Agentic AI Governance & Lifecycle Management

**Scenario Name:** Multi-Agent (Agentic AI) Governance Across the Development-to-Production Lifecycle

**Description:** An agentic AI application (e.g., a LangGraph-based multi-tool agent) is governed across its full lifecycle: risk assessment at use-case creation, tool/node-level performance measurement during development, human feedback and red-teaming for verification, and continuous production monitoring with metric-threshold alerting — supported by a Governed Agentic Catalog (centralized tool/agent repository) and an Experimentation Studio for comparing agents. [Observed — E-005]

**Goal:** Ensure agentic AI applications are reliable, safe, and auditable across creation, development, and production. [Observed — E-005]

**Human Actors:**
- Agent Developer — builds and instruments the agentic application [Observed — E-005, E-011]
- Subject Matter Expert (SME) / Red Teamer — observes and verifies agent actions, tests for susceptibilities (human-in-the-loop) [Observed — E-005]

**Artificial Agents:**
- The agent(s) themselves (tool-calling nodes within, e.g., a LangGraph application) [Observed — E-005]
- Governed Agentic Catalog (centralized tool/agent repository enabling reuse and comparison) [Observed — E-005]
- Experimentation Studio (multi-agent evaluation and cross-platform comparison) [Observed — E-005]
- Metrics Evaluator SDK (Python decorator instrumentation on tool nodes) [Observed — E-005, E-011]

**Context:** Multi-stage AI lifecycle — use-case creation, development, production — potentially spanning multiple agent-orchestration platforms/vendors. [Observed — E-005]

**Input Data:** Agent tool-call traces, benchmark task sets, human feedback annotations. [Observed — E-005]

**Knowledge Sources:** Benchmark suites for agent competence assessment; AI Risk Atlas (agentic-AI risk taxonomy). [Observed — E-005, E-010]

**Processing Method:** Decorator-based instrumentation of tool/agent nodes; benchmark-based scoring; threshold-based alerting. [Observed — E-005]

**Processing Tasks:**
1. Risk assessment at use-case creation [Observed — E-005]
2. Tool/node performance measurement during development [Observed — E-005]
3. Agent benchmarking against evaluation metrics [Observed — E-005]
4. Human feedback / red-teaming verification episode [Observed — E-005]
5. Continuous production monitoring with alerting on metric-limit breach [Observed — E-005]
6. Cross-platform agent comparison in Experimentation Studio [Observed — E-005]

**Interaction Points:** SME ↔ Agent (observation/verification episode, i.e., an `hi:Interaction` with `hi:hasInteractionIntentConcept` "Verify"); Developer ↔ Governed Agentic Catalog (tool selection/reuse). [Observed — E-005]

**Outputs:** Agent competence/benchmark scores; alerts on metric breach; catalog entries for reusable governed tools; comparative evaluation reports. [Observed — E-005]

**Evaluation Metrics:** HAP, PII, prompt injection, context relevance, faithfulness, answer similarity, answer relevance, hit rate, average precision, reciprocal rank, unsuccessful requests [Observed — E-005]; plus runtime metrics: accuracy, tool-call reliability, completion rate, cost, safety [Observed — E-018].

**Required Capabilities:** Agent Benchmarking, Human-in-the-Loop Verification, Production Monitoring. [Observed — E-005]

**Decision Points:** Whether an agent/tool is approved for the Governed Agentic Catalog; whether a metric breach in production requires intervention. [Observed — E-005]

**Feedback Mechanisms:** Production alerts trigger human review; SME red-teaming findings feed back into agent hardening (structurally analogous to Scenario 4's loop, though not verbatim documented for agents specifically — Inferred, Medium confidence, reasoning: the "human feedback or red teaming" phrase is stated as a governance capability but the precise remediation loop for agents is not spelled out to the same level of detail as it is for prompts in E-012). [Partially Inferred — E-005]

**Expected HI Characteristics (CARE):** Collaborative (SME + agent verification loop); Responsible (governed catalog, audit logs per E-018); Explainable (tool-call traceability); Adaptive (continuous benchmarking and re-evaluation). [Observed — E-005, E-018]

**Note on gap:** Specific human role titles for who grants final production approval of an agent (beyond "SME"/"Developer") are not named in the retrieved sources — logged in `knowledge_gaps.md`.

**Evidence IDs:** E-005, E-010, E-011, E-018

---

## Scenario 6 — Production Monitoring of Conversational AI / Virtual Assistants

**Scenario Name:** Virtual Assistant Production Quality & Safety Monitoring

**Description:** Once a virtual assistant (chatbot) is integrated with a deployed prompt template, watsonx.governance automatically logs every user question, retrieved passage, and model response as payload data, continuously computes safety and quality metrics, and raises automatic alerts when thresholds are breached — closing a feedback loop back to prompt engineers. [Observed — E-013]

**Goal:** Ensure a production virtual assistant's responses remain safe, non-toxic, PII-free, and of adequate linguistic quality on an ongoing basis. [Observed — E-013]

**Human Actors:**
- Subject Matter Experts — provide ground truth for evaluation datasets [Observed — E-013]
- Engineers — review alert notifications and metric breaches [Observed — E-013]
- Prompt Engineers — implement improvements based on findings [Observed — E-013]

**Artificial Agents:**
- The Virtual Assistant itself (governed by a deployed prompt) [Observed — E-013]
- Watson OpenScale / monitoring engine (automatic payload logging and metric computation) [Observed — E-013]

**Context:** Live, user-facing production deployment with continuous, automatic interaction capture (no manual intervention required for data collection). [Observed — E-013]

**Input Data:** User questions, retrieved passages, model responses (logged automatically as payload). [Observed — E-013]

**Knowledge Sources:** Ground-truth/reference datasets supplied by SMEs for metrics such as ROUGE/METEOR. [Observed — E-013]

**Processing Method:** Automated payload capture; metric computation (PII/HAP detectors, ROUGE/METEOR text-similarity scoring, readability scoring). [Observed — E-013]

**Processing Tasks:**
1. Automatic interaction logging as payload [Observed — E-013]
2. Metric computation across PII, HAP, ROUGE, METEOR, Readability [Observed — E-013]
3. Automatic alert generation on threshold breach [Observed — E-013]
4. Engineer review of alerts [Observed — E-013]
5. Prompt improvement implementation [Observed — E-013]

**Interaction Points:** Engineer ↔ watsonx.governance UI (alert review); implicit end-user ↔ Virtual Assistant conversational interaction that is itself the object being monitored. [Observed — E-013]

**Outputs:** Logged payload dataset; metric scores; automatic alerts; actionable prompt-improvement insights. [Observed — E-013]

**Evaluation Metrics:** PII, HAP, ROUGE, METEOR, Readability. [Observed — E-013]

**Required Capabilities:** Content Safety Detection, Text Quality Evaluation. [Observed — E-013]

**Decision Points:** Whether a breached metric requires a prompt change; how to prioritize among multiple simultaneous alerts (the latter not explicitly documented — Inferred, Low confidence). [Partially Inferred — E-013]

**Feedback Mechanisms:** Alert → engineer review → prompt-engineer improvement → (implied) re-monitoring, forming a closed loop. [Observed — E-013]

**Expected HI Characteristics (CARE):** Collaborative (SME ground-truth + engineer review + AI monitoring); Responsible (toxicity/PII safety gating); Adaptive (iterative prompt improvement from live feedback). [Observed — E-013]

**Evidence IDs:** E-013

---

## Scenario 7 — AI-Governed Recruitment Screening (Careerforce Pro / IRIS)

**Scenario Name:** Governed AI-Assisted Candidate Screening and Interview Coordination

**Description:** A recruitment platform (Careerforce Pro) uses an AI voice assistant, IRIS, built on IBM watsonx.ai, to conduct first-round candidate screening calls, evaluate skill/role fit, and generate structured candidate report cards, while watsonx.governance provides documentation of AI recommendations, performance monitoring, and detection of bias or drift in the hiring pipeline. [Observed — E-016]

**Goal:** Reduce time-to-hire and improve résumé-screening speed while maintaining fair, auditable, and transparent automated hiring decisions. [Observed — E-016]

**Human Actors:**
- Recruiters / Talent Team — receive structured, actionable candidate insights [Observed — E-016]
- Hiring Managers — engage directly with qualified, pre-screened candidates [Observed — E-016]
- HR Leaders — maintain visibility across the full hiring pipeline [Observed — E-016]

**Artificial Agents:**
- IRIS — AI voice assistant conducting screening calls, evaluating fit, generating report cards, coordinating follow-up interviews [Observed — E-016]
- IBM watsonx.ai — underlying model providing contextual analysis of job descriptions and résumés [Observed — E-016]
- watsonx.governance monitoring layer — documents recommendations, monitors performance, detects bias/drift [Observed — E-016]

**Context:** High-turnover, high-volume-application industries where manual screening previously caused qualified-candidate loss to faster competitors. [Observed — E-016]

**Input Data:** Job descriptions, résumés, candidate voice-call transcripts/audio. [Observed — E-016]

**Knowledge Sources:** Job-role requirements; historical hiring outcome data (implied basis for bias/drift monitoring, though the specific baseline dataset is not documented — Inferred, Low confidence). [Partially Inferred — E-016]

**Processing Method:** Contextual (beyond-keyword) résumé/job-description analysis; voice-based conversational screening; automated scoring. [Observed — E-016]

**Processing Tasks:**
1. Automated job-description creation [Observed — E-016]
2. Résumé parsing and candidate scoring [Observed — E-016]
3. AI-powered shortlisting [Observed — E-016]
4. IRIS voice-based initial screening call [Observed — E-016]
5. Structured interview coordination [Observed — E-016]
6. Hiring-manager review of qualified candidates [Observed — E-016]

**Interaction Points:** Candidate ↔ IRIS (voice screening conversation — an `hi:Interaction` with modality "Voice"); Recruiter ↔ generated report cards; HR Leader ↔ pipeline dashboard. [Observed — E-016]

**Outputs:** Candidate report cards; shortlist; coordinated interview schedule; bias/drift monitoring reports. [Observed — E-016]

**Evaluation Metrics:** Time-to-hire (reported 85% reduction); résumé-screening speed (reported 97% faster); bias/drift detection status (qualitative, monitored continuously). [Observed — E-016; note: quantitative outcome figures are vendor-reported case-study claims, not independently audited — flagged Medium confidence on precision of the exact percentages, High confidence on the qualitative existence of the capability]

**Required Capabilities:** Conversational Screening, Fairness Assessment, Drift Detection, Documentation Authoring. [Observed — E-016]

**Decision Points:** Which candidates are shortlisted for hiring-manager review; whether bias/drift signals require pipeline adjustment. [Observed — E-016]

**Feedback Mechanisms:** Continuous bias/drift monitoring feeding back into pipeline oversight (mechanism named but not procedurally detailed — Inferred loop, Medium confidence). [Partially Inferred — E-016]

**Expected HI Characteristics (CARE):** Collaborative (IRIS handles first-round screening; humans make final hiring decisions — a clear human-final-decision HI pattern); Responsible (governance layer for bias/drift); Explainable (structured report cards as human-readable summaries of AI assessment). [Observed — E-016]

**Evidence IDs:** E-016

---

## Scenario 8 — Multi-Cloud & Third-Party Model Risk Governance for Regulated Industries

**Scenario Name:** Enterprise Model Risk Governance (MRG) Across Multi-Cloud, Third-Party Models

**Description:** A regulated enterprise (e.g., a financial institution) governs a large, heterogeneous inventory of ML and GenAI models — including third-party models hosted on AWS Bedrock, Azure, or Google Vertex AI, integrated via custom ML-provider proxy endpoints or Detached Prompt Templates — through a six-stage prescriptive workflow (Propose → Build → Evaluate/Approve → Deploy → Monitor/Manage → Operationalize) with defined risk-governance roles, satisfying banking/insurance Model Risk Management (MRM) standards across multiple jurisdictions. [Observed — E-019, E-020, E-022]

**Goal:** Maintain enterprise-wide, centralized risk oversight and regulatory compliance across hundreds or thousands of models regardless of where they are built or hosted. [Observed — E-019, E-022]

**Human Actors:**
- Model Requestor/Owner — proposes the use case [Observed — E-020]
- Model Developer / Prompt Engineer — builds and tests prompt templates or models [Observed — E-020]
- Model Validator/Reviewer — evaluates performance and approves [Observed — E-020]
- ModelOps Engineer — deploys and monitors in production [Observed — E-020]
- Model Risk Officer — generates compliance reports [Observed — E-020]
- Human risk-oversight function (unnamed specific title) retained even where retraining/review workflows are automated [Observed generic role, Inferred specific title — E-022]

**Artificial Agents:**
- Third-party models accessed via Custom ML Provider proxy endpoints (e.g., Google Vertex AI) [Observed — E-019]
- Detached Prompt Templates representing externally hosted GenAI models (AWS Bedrock, Azure, OpenAI) [Observed — E-014, E-019]
- Watson OpenScale (fairness, quality, drift, explainability evaluation across all connected models) [Observed — E-019]
- AI FactSheets (automatic sync of evaluation results) [Observed — E-019]

**Context:** Regulated financial/insurance environment; multi-cloud technology estate; multi-jurisdiction compliance obligations (data residency, auditability, consumer protection, third-party risk). [Observed — E-022]

**Input Data:** Model metadata (via Factsheet SDK), production predictions, feedback/payload data returned from third-party providers. [Observed — E-019]

**Knowledge Sources:** MRM regulatory standards (banking/insurance); AI Risk Atlas. [Observed — E-022, E-010]

**Processing Method:** Proxy-based translation of prediction requests/responses; standardized cross-provider evaluation; six-stage prescriptive lifecycle workflow. [Observed — E-019, E-020]

**Processing Tasks:**
1. Propose AI use case [Observed — E-020]
2. Build prompt templates / models with chosen foundation model or provider [Observed — E-020]
3. Log metadata via Factsheet SDK [Observed — E-019]
4. Subscribe / integrate third-party model via proxy endpoint or detached prompt template [Observed — E-019]
5. Evaluate and approve using validation datasets [Observed — E-020]
6. Deploy to production [Observed — E-020]
7. Monitor and manage with continuous tracking (fairness, quality, drift, explainability, PII/HAP) [Observed — E-019, E-020]
8. Automate retraining/review workflows from production feedback, with human risk oversight retained [Observed — E-022]
9. Operationalize through application integration [Observed — E-020]

**Interaction Points:** Model Validator ↔ evaluation dashboard (approval decision); Model Risk Officer ↔ compliance report generation; end users' ratings captured as a "Human Rating/Voting score" custom metric feeding back into evaluation. [Observed — E-019, E-020]

**Outputs:** Model inventory records; synced AI FactSheets; compliance/audit reports; fairness/drift/quality dashboards; retraining triggers. [Observed — E-019, E-020, E-022]

**Evaluation Metrics:** Fairness/bias (training, payload, output); quality (ROC, recall for classification; RMSE, MAE, R² for regression); drift (data, model, LLM prediction-probability, word-count drift); explainability (Shapley/LIME); PII/HAP; RAG metrics (Faithfulness, Answer Relevance, Unsuccessful Answer Rate); custom metrics including Human Rating/Voting score and LLM-as-a-Judge scoring. [Observed — E-019]

**Required Capabilities:** Fairness Assessment, Drift Detection, Explainability, Text Quality Evaluation, Content Safety Detection, Model Integration (cross-provider). [Observed — E-019]

**Decision Points:** Model approval/production promotion; retraining trigger; compliance sign-off. [Observed — E-020, E-022]

**Feedback Mechanisms:** Production feedback automatically triggers retraining/review workflows, "while keeping human risk oversight in the loop." [Observed — E-022]

**Expected HI Characteristics (CARE):** Collaborative (five distinct governance roles + multi-vendor AI models within one HI Team); Responsible (audit, compliance, MRM alignment); Adaptive (automated retraining triggers with retained human oversight); Explainable (Shapley/LIME across all providers). [Observed — E-019, E-020, E-022]

**Note on gap:** The full official Model Risk Governance (MRG) workflow documentation (E-002, E-004) could not be retrieved due to access limitations (JS-rendered content / HTTP errors); this scenario is therefore reconstructed from two independent secondary/engineering-blog sources (E-019, E-020) corroborated by one vendor announcement (E-014) and one trade-press article (E-022), rather than from the primary MRG workflow documentation itself. Confidence is marked Medium-High rather than High for this reason — see `knowledge_gaps.md`.

**Evidence IDs:** E-002, E-004, E-010, E-014, E-019, E-020, E-022

---

## Cross-Scenario Saturation Note

Together, these eight scenarios exercise every HI Ontology class (`hi:UseCase`, `hi:HITeam`, `hi:HumanAgent`, `hi:ArtificialAgent`, `hi:Goal`, `hi:Task`, `hi:Capability`, `hi:TaskExecution`, `hi:Interaction`, `hi:Context`, `hi:Evaluation`, `hi:Experiment`) at least twice, span four distinct business domains (financial/enterprise risk, software engineering/RAG, HR/recruitment, and cross-cutting regulatory compliance), and cover both machine-learning and generative/agentic AI paradigms — satisfying the RAS saturation criterion (Section 8) for this knowledge-acquisition phase.
