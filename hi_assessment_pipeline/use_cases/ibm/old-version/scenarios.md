# Hybrid Intelligence Scenarios — IBM watsonx.governance
RAS v1.0 | 5 evidence-backed scenarios | Namespaces: `hi:`, `hint:` per supplied `hiontology.ttl`

Each scenario below is either (a) explicitly documented by IBM in the accepted evidence, or (b) strongly supported by convergence across ≥2 independent accepted sources, per protocol §15. Modelling assumptions, where unavoidable to complete a scenario's field, are labelled inline as **[Assumption]**. No scenario asserts a fact without a cited Evidence ID.

---

## Scenario 1: Predictive Model Risk Monitoring in Regulated Financial Services

**Scenario Name:** Predictive Credit/Insurance Risk Model Governance and Continuous Monitoring

**Description:** A bank or insurer deploys a predictive machine-learning model (e.g., credit scoring, fraud detection, insurance pricing) and uses watsonx.governance to continuously monitor it for quality decay, fairness/bias, and data drift, with human risk-and-compliance oversight of automated retraining and audit trail generation.

**Goal:** Maintain a compliant, fair, and accurate predictive model in production, satisfying banking/insurance Model Risk Management (MRM) standards and audit requirements while minimizing manual review overhead. (hi:Goal)

**Human Actors:**
- Risk & Compliance team member — ensures alignment to MRM standards, internal audit requirements, and AI regulations (E-008)
- Model validator / internal auditor — reviews documented model iteration history to satisfy audit and validation needs (E-008)
- Data scientist / model owner — configures monitors (thresholds, favorable/unfavorable outcome labels, monitored groups) (E-003)
- Human risk overseer — kept "in the loop" during automated retraining workflows (E-008)

**Artificial Agents:**
- The governed predictive ML model itself (e.g., a classification model) (E-003, E-008)
- watsonx.governance's OpenScale-derived monitoring engine computing Quality, Fairness, Drift, and Explainability metrics (E-003, E-005)
- Explainability sub-agent computing LIME/SHAP explanations (E-003)

**Context:** Regulated financial-services environment where "automated decisions may affect credit access, insurance pricing, trading behavior or anti-money laundering alerts"; subject to banking/insurance MRM standards and internal audit requirements (E-008). (hi:Context)

**Input Data:** Training data (for baseline statistics and drift comparison), payload data (live prediction requests/responses), feedback data (ground-truth outcomes) (E-003).

**Knowledge Sources:** Historical training-data statistics; user-flagged "important features" for enhanced drift monitoring; configured fairness group definitions (E-003).

**Processing Method:** Statistical monitoring against configurable thresholds; Disparate Impact and Statistical Parity Difference computation for fairness; LIME/SHAP for explainability; minimum-sample-size-gated drift detection (E-003). (hi:Method)

**Processing Tasks:**
1. Upload training data and define model output columns (E-003)
2. Configure fairness, quality, explainability, and drift monitors with thresholds and minimum sample sizes (E-003)
3. Execute "Evaluate now" against payload and feedback data (E-003)
4. Automate retraining and review workflows based on production feedback (E-008)
5. Document model iteration history for audit (E-008)

**Interaction Points:** Human risk-oversight review of automated retraining triggers (E-008); data scientist configuration of monitor thresholds (E-003); dashboard review of monitoring insights by risk/compliance staff (E-003). (hi:Interaction)

**Outputs:** Quality/fairness/drift/explainability scores and alerts; dashboard insights (E-003); documented model iteration history for audit (E-008).

**Evaluation Metrics:** Disparate Impact (80% default threshold), Statistical Parity Difference, model accuracy/quality score, drift score, LIME/SHAP explanation outputs (E-003).

**Required Capabilities:** Fairness/bias detection, drift detection, explainability computation (LIME, SHAP), quality/accuracy monitoring, automated workflow triggering (E-003, E-008, E-011).

**Decision Points:** Whether a monitored metric breaches its threshold (triggers alert); whether to trigger automated retraining; whether a model passes audit/validation review (E-003, E-008).

**Feedback Mechanisms:** Production feedback data closes the loop into drift/quality recalculation; automated retraining workflows triggered by monitoring results, with human risk oversight retained in that loop (E-008).

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Data scientists configure and interpret monitors; risk/compliance humans review and gate retraining decisions triggered by AI-computed metrics (E-003, E-008) — **Observed**.
- *Adaptive:* Automated retraining workflows respond to production feedback (E-008) — **Observed**.
- *Responsible:* Fairness metrics (Disparate Impact, Statistical Parity Difference) directly target discriminatory outcomes in fair lending/insurance pricing (E-008, E-011) — **Observed**.
- *Explainable:* LIME/SHAP provide local and global explanations of individual predictions (E-003) — **Observed**.

**Evidence IDs:** E-003, E-008, E-011

---

## Scenario 2: Generative AI / RAG Assistant Governance and Evaluation

**Scenario Name:** Enterprise RAG Question-Answering Assistant — Quality, Faithfulness, and Safety Governance

**Description:** An enterprise builds a retrieval-augmented-generation (RAG) assistant (e.g., customer support or internal knowledge Q&A) on watsonx.ai or a third-party LLM, and uses watsonx.governance's Evaluation Studio and production monitoring to assess and continuously govern response quality, groundedness, and content safety before and after deployment.

**Goal:** Deploy a generative AI assistant whose answers are relevant, faithful to retrieved source documents (low hallucination), and free of unsafe or non-compliant content (hate/abuse/profanity, PII exposure). (hi:Goal)

**Human Actors:**
- LLM application developer — builds and compares prompt templates and models in Evaluation Studio (E-010)
- AI/ML governance reviewer — reviews Factsheet-logged evaluation results before promotion to production (E-009, E-011)

**Artificial Agents:**
- The RAG assistant itself (retriever + generator LLM), potentially hosted on watsonx.ai, Amazon Bedrock, Microsoft Azure, or another third-party platform (E-006, E-009)
- Evaluation Studio's evaluation engine (E-010)
- An "LLM-as-a-Judge" model (e.g., Mistral AI) used to score answer/retrieval quality (E-010)
- watsonx.governance's production content-safety monitor (HAP/PII detection) (E-004, E-011)

**Context:** Multi-vendor generative AI deployment environment; enterprise customer-facing or internal knowledge-work setting where hallucination and unsafe content carry reputational/compliance risk (E-006, E-009). (hi:Context)

**Input Data:** Prompt templates with variables; validation datasets mapping questions, retrieved contexts, and reference answers (E-010); production input prompts and generated outputs (E-009, E-011).

**Knowledge Sources:** Retrieved documents/context passages used by the RAG pipeline (E-004); reference answers for Answer Similarity scoring (E-004).

**Processing Method:** LLM-as-a-Judge scoring; task-specific NLG metrics (Rouge, SARI, METEOR, BLEU for summarization) (E-011); embedding/semantic comparison for Faithfulness, Context Relevance, Answer Relevance/Similarity (E-004, E-006, E-010). (hi:Method)

**Processing Tasks:**
1. Create prompt-template assets across candidate LLMs (E-010)
2. Configure an evaluation experiment (task type, metric dimensions, thresholds) (E-010)
3. Map validation-data columns (questions, contexts, reference answers) (E-010)
4. Execute the evaluation and compare candidate model/prompt combinations (E-010)
5. Publish selected configuration's metadata to the AI Factsheet (E-011)
6. Promote to a deployment space and activate production monitoring (E-011)
7. Continuously monitor live inputs/outputs for HAP, PII, and quality metrics (E-004, E-009, E-011)

**Interaction Points:** Developer-in-the-loop comparison and selection among multiple LLM/prompt candidates (E-010); embedded conversational AI assistants used to capture governance information during onboarding (E-001); reviewer sign-off on Factsheet-recorded evaluation results (E-009). (hi:Interaction)

**Outputs:** Comparative evaluation scores per LLM/prompt combination; weighted composite rankings (E-010); AI Factsheet entries; production monitoring alerts (E-009, E-011).

**Evaluation Metrics:** Faithfulness, Answer Relevance, Context Relevance, Answer Similarity, Unsuccessful-request rate, HAP score, PII detection rate, and (for summarization tasks) Rouge/SARI/METEOR/BLEU (E-004, E-006, E-010, E-011).

**Required Capabilities:** RAG-quality assessment, content-safety screening, multi-vendor model integration, LLM-as-a-Judge comparative evaluation, automated Factsheet generation (E-004, E-006, E-009, E-010, E-011).

**Decision Points:** Which LLM/prompt configuration to promote to production based on weighted metric ranking (E-010); whether a production output should be flagged/blocked for content-safety violation (E-004, E-009).

**Feedback Mechanisms:** Production input/output data captured and fed back for ongoing evaluation and Factsheet update (E-011); comparative experiment results inform iterative prompt/model refinement (E-010).

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Developers direct which models/prompts to test; an AI judge model assists in scoring, with humans making the final promotion decision (E-010) — **Observed**.
- *Adaptive:* Production monitoring and Factsheet updates continuously reflect live performance (E-011) — **Observed**.
- *Responsible:* Explicit HAP/PII safety screening protects against harmful or privacy-violating outputs (E-004, E-009, E-011) — **Observed**.
- *Explainable:* Faithfulness/Context Relevance scoring surfaces whether an answer is grounded in retrieved evidence, supporting interpretability of "why" an answer was trusted or flagged (E-004, E-006) — **Observed**.

**Evidence IDs:** E-001, E-004, E-006, E-009, E-010, E-011

---

## Scenario 3: Third-Party / Multi-Cloud Foundation Model Onboarding and Risk Assessment

**Scenario Name:** Foundation Model Onboarding via the AI Risk Atlas and Model Risk Evaluation Engine

**Description:** An organization wants to adopt a foundation model — either from watsonx.ai or a third-party/multi-cloud provider (AWS, Azure, GCP) — and uses the watsonx.governance Governance Console's Model Risk Governance (MRG) module, the AI Risk Atlas taxonomy, and the Model Risk Evaluation Engine to systematically identify and quantify risk before onboarding.

**Goal:** Select and onboard a foundation model whose quantified risk profile (across bias, hallucination, prompt injection, jailbreaking, data-provenance, and reidentification dimensions) matches the organization's risk tolerance, with a documented, auditable decision trail. (hi:Goal)

**Human Actors:**
- Governance-console administrator (MRG Master / Modules Master profile) — configures and reviews the model inventory and risk library (E-013)
- Risk assessor — completes "AI Model Onboarding Risk Identification" and "Use Case + Model Combined Risk Identification" questionnaires (E-013)
- AI governance product/research team (upstream) — defines the risk taxonomy and evaluation engine (not part of the runtime governance team, but shapes its tooling) (E-014, E-015)

**Artificial Agents:**
- The candidate foundation model(s) being assessed, whether hosted on watsonx.ai or externally (E-014)
- The Model Risk Evaluation Engine — computes AI-Risk-Atlas-based risk metrics and generates a PDF report (E-014)
- Risk Atlas Nexus tooling — knowledge-graph mapping across risk taxonomies, LLM-assisted compliance questionnaires (E-015)
- A custom ML-provider proxy endpoint enabling governance access to a third-party-hosted model (E-011)

**Context:** Multi-cloud enterprise environment; formal AI risk taxonomy spanning training-data, inference, output, non-technical, and agentic risk categories, each subdivided by dimensions of accuracy, fairness, privacy, and explainability (E-015). Governance Console structured into Model Risk Governance, Operational Risk Management, and Regulatory Compliance Management solutions, with dedicated Foundation Model, Use Case, Discovered-AI ("shadow AI"), and AI Compliance Plan libraries (E-013). (hi:Context)

**Input Data:** Candidate model metadata and API access; questionnaire responses; the predefined AI Risk Library content (E-013, E-014).

**Knowledge Sources:** The AI Risk Atlas taxonomy itself, functioning as a structured knowledge base of risks, dimensions, and mitigation links (E-014, E-015).

**Processing Method:** Three-stage workflow — **Understand** (consult the AI Risk Atlas), **Identify** (complete risk-identification questionnaires), **Evaluate** (quantitative metric computation by the Model Risk Evaluation Engine) (E-014); LLM-as-a-judge-assisted use-case risk prioritization (E-015). (hi:Method)

**Processing Tasks:**
1. Access the AI Risk Atlas library within the Governance Console (E-014)
2. Complete AI use-case risk identification and AI model onboarding risk identification questionnaires (E-013, E-014)
3. Run the Model Risk Evaluation Engine to compute quantitative risk metrics for the candidate model(s) (E-014)
4. Compare risk metrics across candidate foundation models (E-014)
5. Store computed metrics in the Governance Console and generate a PDF risk report (E-014)
6. Register the approved model in the Foundation Model Library (E-013)

**Interaction Points:** Risk assessor completing structured questionnaires (human data entry into an AI-assisted governance workflow) (E-013); administrator review of computed risk-comparison output before onboarding approval (E-014). (hi:Interaction)

**Outputs:** Quantified per-model risk-dimension scores; comparative risk report (PDF); an inventoried, risk-scored entry in the Foundation Model Library (E-013, E-014).

**Evaluation Metrics:** Risk metrics for prompt injection, toxic output, jailbreaking, hallucination, bias, data-provenance issues, and reidentification risk (E-014); risk dimensions of accuracy, fairness, privacy, and explainability across the five AI Risk Atlas categories (E-015).

**Required Capabilities:** Foundation-model risk-metric computation, risk-taxonomy-based comparison, automated questionnaire-driven risk identification, knowledge-graph mapping across risk taxonomies (E-014, E-015).

**Decision Points:** Whether a candidate foundation model's risk profile is acceptable for onboarding; which of several candidate models best matches organizational risk tolerance (E-014).

**Feedback Mechanisms:** Risk-identification questionnaire data "flows back into the Governance Console" to inform the subsequent risk-assessment step (E-014) — an explicit closed loop between identification and evaluation stages.

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Human risk assessors provide structured judgments (questionnaires) that combine with automated metric computation (E-013, E-014) — **Observed**.
- *Adaptive:* [Assumption — Inferred] The risk library and taxonomy are described as extensible/updatable, implying the system adapts as new risk categories emerge, though continuous automatic adaptation is not explicitly documented. **Confidence: Low-Medium**.
- *Responsible:* Directly targets accountability and risk mitigation prior to deployment, with an auditable PDF report (E-014) — **Observed**.
- *Explainable:* Risk dimensions are decomposed and individually scored (not a single opaque score), supporting interpretability of *why* a model is judged risky (E-015) — **Observed**.

**Evidence IDs:** E-013, E-014, E-015, E-011 (for the custom-provider onboarding mechanism)

---

## Scenario 4: Agentic AI System Governance (Agent Lifecycle Oversight)

**Scenario Name:** Autonomous Multi-Step Agent Governance — Evaluation, Human-in-the-Loop Oversight, and Runtime Control

**Description:** An organization builds an autonomous or semi-autonomous AI agent (e.g., an "automated investment assistant," a LangGraph-based tool-using agent, or an agent built on watsonx Orchestrate) and governs it across its lifecycle — from use-case creation and validation through production monitoring — using watsonx.governance's agentic evaluation metrics combined with SME human-in-the-loop review and watsonx Orchestrate's runtime control plane.

**Goal:** Ensure an autonomous agent's tool selection, reasoning, and actions remain safe, accurate, and aligned with intended use, despite the agent's "unsupervised autonomy" and capacity to "take actions that are at times harmful to organizations or their customers" (E-004). (hi:Goal)

**Human Actors:**
- Subject-matter expert (SME) — observes and verifies agent actions via human feedback and red-teaming; tests agents for susceptibilities (E-007)
- Agent developer — instruments tool nodes (e.g., in a LangGraph application) with governance metric decorators (E-007)
- Governance/risk reviewer — assesses agent-specific risk at use-case creation and validation stages (E-007)

**Artificial Agents:**
- The autonomous agent itself, e.g., an "automated investment assistant" (E-004)
- The orchestrator component selecting and invoking tools (E-004)
- watsonx.governance's agentic evaluation metric computation layer (context relevance, faithfulness, answer similarity, and RAG-agentic metrics) (E-004, E-007)
- watsonx Orchestrate's control plane — operates agents, enforces guardrails, performs identity/access control and audit logging (E-017)

**Context:** Agentic AI deployment where the agent has multi-step, tool-using autonomy; heightened governance risk due to unsupervised decision-making (E-004, E-007). Cross-framework, cross-cloud agent operation ("no matter where they're built or run") (E-017). (hi:Context)

**Input Data:** User queries/prompts to the agent; tool outputs and intermediate reasoning steps; retrieved context for RAG-augmented agent steps (E-004, E-007).

**Knowledge Sources:** Retrieved documents/tools available to the agent; benchmark task sets used for competence evaluation (E-007).

**Processing Method:** Python-decorator-based metric instrumentation of LangGraph tool nodes (E-007); human red-teaming/adversarial probing (E-007); runtime policy/guardrail enforcement (E-017). (hi:Method)

**Processing Tasks:**
1. Establish the agentic use case and associate specific agents to it (E-004)
2. Conduct an initial risk assessment of the agent (E-004)
3. Instrument the agent's tool nodes with governance metric decorators (E-007)
4. Run evaluation-metric-with-benchmark assessments of agent competence overall and per task (E-007)
5. Conduct SME human feedback / red-teaming sessions (E-007)
6. Monitor the agent post-deployment for performance and system drift (E-004, E-007)
7. Operate the agent under Orchestrate's control plane with policy/guardrail enforcement and audit logging (E-017)

**Interaction Points:** SME-to-agent red-teaming dialogue (human in the loop) (E-007); developer instrumentation choices determining what is measured (E-007); (future capability, not yet GA per E-004) real-time flow decisions made using computed metrics during agent execution. (hi:Interaction)

**Outputs:** Per-tool and per-task evaluation scores; red-teaming findings; audit logs of agent decisions; risk-assessment results feeding the use case's governance record (E-004, E-007, E-017).

**Evaluation Metrics:** Context Relevance, Faithfulness, Answer Similarity (E-004); HAP, PII, prompt injection, context relevance, faithfulness, answer similarity, answer relevance, hit rate, average precision, reciprocal rank, unsuccessful-request tracking, Query Translation Faithfulness, System Drift, Tool Selection Quality (E-007); accuracy, tool-call reliability, completion rate, cost, safety (E-017).

**Required Capabilities:** Agent-specific drift detection, tool-selection quality assessment, RAG-agentic metric computation, human-feedback/red-teaming facilitation, runtime policy/guardrail enforcement, audit logging (E-004, E-007, E-017).

**Decision Points:** Whether an agent's initial risk assessment permits production deployment (E-004); whether red-teaming reveals a susceptibility requiring remediation before go-live (E-007); real-time in-flow tool-selection or continuation decisions (planned capability) (E-007).

**Feedback Mechanisms:** Post-deployment monitoring results loop back into the use case's governance record (E-004); (planned) continuous-oversight alerts when metrics exceed predefined limits (E-007); Orchestrate audit logs provide traceable decision history for retrospective review (E-017).

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* SMEs actively probe and verify agent behavior rather than passively consuming output (E-007) — **Observed**.
- *Adaptive:* Experimentation tracking is described as enabling "rapid comparison and iteration across multiple agentic applications" (E-007) — **Observed**.
- *Responsible:* Explicit acknowledgment that agent autonomy is a governance risk requiring active mitigation (bias, hallucination, confidential-information exposure) (E-004, E-007) — **Observed**.
- *Explainable:* Decomposed, per-tool and per-step metrics (rather than a single end-to-end score) support tracing *which* step of an agent's reasoning failed (E-007) — **Observed**. Audit logs additionally support after-the-fact explainability of agent decisions (E-017) — **Observed**.

**Evidence IDs:** E-004, E-007, E-017

**Note on maturity:** Several capabilities in this scenario (real-time in-flow governance decisions, continuous production oversight with automatic alerting) were explicitly described by IBM as forthcoming/planned rather than generally available at the time of the cited announcements (E-004: tech preview dated 2025-03-03, "enhanced functionality... planned for later in 2025"; E-007: "Future releases will provide..."). This scenario is therefore evidence-backed for its *design intent and partially released capability*, not for a fully mature production capability set. This maturity caveat is carried into `knowledge_gaps.md`.

---

## Scenario 5: AI Use Case Regulatory Compliance Onboarding (EU AI Act)

**Scenario Name:** Cross-Functional AI Use Case Onboarding with EU AI Act Risk-Tier Classification

**Description:** Before a new AI use case (predictive or generative) is allowed to proceed to development or production, a cross-functional team uses watsonx.governance's Governance Console to register the use case, classify it against the EU AI Act's risk tiers, and route it through a policy-configurable approval workflow involving reviewers and approvers from multiple business functions.

**Goal:** Ensure every AI use case in the organization is inventoried, classified by regulatory risk tier, and formally approved before deployment, closing the "AI governance gap" and preventing "shadow AI" (E-001, E-013). (hi:Goal)

**Human Actors:**
- Use-case requester ("User") — initiates the onboarding request (E-005)
- Reviewer — completes questionnaire-based risk/compliance assessments (E-005)
- Approver — authorizes the use case under a designated role (E-005)
- Cross-functional stakeholders from engineering, legal, compliance, risk, security, data, and business teams (E-012)

**Artificial Agents:**
- The Governance Console's EU AI Act applicability assessment tool (E-006)
- Embedded AI assistants that help capture governance information conversationally during onboarding (E-001)
- The workflow engine executing the no-code-configured approval process (E-005)

**Context:** Enterprise operating under the EU AI Act (and, per E-001, also NIST AI RMF, ISO 42001, and Data & Trust Alliance frameworks), where use cases must be triaged into **Prohibited, High-Risk, Limited-Risk, or Minimal-Risk** categories (E-006). (hi:Context)

**Input Data:** Use-case description and intended purpose; questionnaire responses characterizing the AI system's function, users, and data (E-006, E-013).

**Knowledge Sources:** The predefined AI Risk Library and EU AI Act applicability rule set built into the Governance Console (E-013).

**Processing Method:** Customizable questionnaire-based risk assessment yielding a risk score; no-code workflow, questionnaire, and dashboard editors for organization-specific customization (E-005, E-006). (hi:Method)

**Processing Tasks:**
1. Requester submits a new use case for governance review (E-005)
2. System runs the EU AI Act applicability assessment, assigning a risk tier (E-006)
3. Risk tier determines monitoring frequency and approval requirements (E-006)
4. Reviewer(s) complete the risk/compliance questionnaire (E-005, E-013)
5. Approver(s) authorize or reject the use case (E-005)
6. Approved use case is registered in the Use Case Library, linked to relevant business processes (E-013)

**Interaction Points:** Requester ↔ conversational onboarding assistant (E-001); Reviewer ↔ questionnaire workflow (E-005); Reviewer → Approver handoff (E-005); cross-functional stakeholder collaboration on policy design (E-012). (hi:Interaction)

**Outputs:** A risk-tier classification (Prohibited/High-Risk/Limited-Risk/Minimal-Risk); an approval decision; a registered, auditable use-case record with linked business process (E-006, E-013).

**Evaluation Metrics:** EU AI Act risk-tier score/category (E-006); [Assumption — Inferred] approval-cycle-time and audit-fee-reduction outcome metrics implied by the vendor's reported "62% reduction in processing time" and "50% reduction in audit fees" (E-001) are organizational KPIs, not per-use-case technical metrics — **Confidence: Medium**, since these are vendor-reported aggregate figures without disclosed methodology.

**Required Capabilities:** Regulatory-risk assessment automation, no-code workflow/questionnaire/dashboard configuration, conversational governance-information capture, use-case-to-business-process linkage (E-001, E-005, E-006, E-013).

**Decision Points:** Risk-tier assignment (determines downstream rigor); Reviewer's assessment outcome; Approver's authorize/reject decision (E-005, E-006).

**Feedback Mechanisms:** [Assumption — Inferred] Approved/rejected use-case outcomes and their risk-tier assignments plausibly inform later policy tuning and risk-library refinement, consistent with the platform's "policy creation" and "regulatory alignment" use cases (E-001), though no source explicitly documents a formal feedback loop from approval outcomes back into policy configuration — **Confidence: Low**, flagged as an assumption.

**Expected Hybrid Intelligence Characteristics (CARE):**
- *Collaborative:* Multiple human roles (Requester, Reviewer, Approver) plus cross-functional stakeholders jointly execute the governance process, assisted by AI-driven risk classification (E-005, E-006, E-012) — **Observed**.
- *Adaptive:* No-code editors let the organization tailor workflows, questionnaires, and dashboards to evolving governance needs (E-005) — **Observed**.
- *Responsible:* Directly operationalizes a named external regulatory framework (EU AI Act) into a repeatable internal control (E-006) — **Observed**.
- *Explainable:* Risk-tier classification is decomposed via questionnaire responses rather than an opaque single score, allowing reviewers to see which answers drove the classification (E-006, E-013) — **Observed** (mechanism), though the underlying classification algorithm's internal logic was not documented in the accessible sources — **Confidence: Medium**.

**Evidence IDs:** E-001, E-005, E-006, E-012, E-013

---

## Cross-Scenario Summary Table

| Scenario | Primary HI Ontology Classes Instantiated | Evidence Breadth |
|---|---|---|
| 1. Predictive Risk Model Monitoring | HITeam, Agent(Human/Artificial), Task, TaskExecution, Capability, Evaluation, Context | 3 sources |
| 2. Generative AI / RAG Governance | HITeam, Agent, Task, TaskExecution, Interaction, Evaluation, Experiment | 6 sources |
| 3. Foundation Model Onboarding | UseCase, Agent, Context, Task, Evaluation, Experiment | 4 sources |
| 4. Agentic AI Governance | Agent, Interaction, Task, TaskExecution, Evaluation, Context | 3 sources |
| 5. EU AI Act Use Case Onboarding | UseCase, HITeam, Agent, Interaction, Task, Context | 5 sources |
