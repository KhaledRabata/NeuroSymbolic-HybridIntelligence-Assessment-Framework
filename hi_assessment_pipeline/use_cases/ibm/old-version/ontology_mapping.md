# Ontology Mapping — IBM watsonx.governance → Hybrid Intelligence Ontology (hi:) / HINT Thesaurus (hint:)
RAS v1.0 | Namespaces: `hi: https://w3id.org/hi-ontology#` | `hint: https://w3id.org/hi-thesaurus#`

This file maps every concept extracted from the evidence base (`sources.md`) onto the classes and object/data properties defined in the supplied `hiontology.ttl` (v2.0.0) and the accompanying diagram. **No RDF triples, instances, or SHACL shapes are produced here** — this is a documentation-only mapping table, per protocol §3 and §16 (File 6).

Each row cites its supporting Evidence ID(s) from `sources.md`. Confidence and Observed/Inferred status follow protocol §11–§12.

---

## 1. hi:HITeam mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| The cross-functional group of engineering, legal, compliance, risk, security, data and business staff plus the AI system(s) they govern, collaborating toward "policy management, auditability and transparency" | `hi:HITeam` | Observed | High | E-012 |
| A named use case (e.g., a credit-risk model, a RAG assistant, an autonomous agent) instantiates a team pursuing a governance goal | `hi:hasGoal` (HITeam → Goal) | Inferred — the TTL requires every HITeam to have ≥1 Goal; watsonx.governance evidence describes goals (compliance, trust, risk reduction) but does not use the literal word "HITeam" | Medium | E-001, E-008, E-011 |
| Human roles (Users, Reviewers, Approvers, risk/compliance teams, developers) plus artificial components (monitoring engine, evaluation engine, agents) jointly constitute the team | `hi:hasMember` (HITeam → Agent), satisfying the OWL restriction requiring ≥1 `hi:HumanAgent` and ≥1 `hi:ArtificialAgent` | Observed (role list) / Inferred (team framing) | High (roles) / Medium (explicit "team" framing) | E-005, E-011, E-012 |
| "Concurrent users" as a licensed/tiered capacity concept | `hi:hasMember`, `hint:Role` | Observed | Medium | E-016 |

## 2. hi:UseCase mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| "AI Use Case" as a first-class governed object (Use Case Library, Use Case Risk Identification questionnaire) | `hi:UseCase` | Observed | High | E-013, E-014 |
| A use case is linked to a HINT thesaurus concept describing its purpose | `hi:hasUseCaseConcept` | Inferred — the mechanism (tagging/categorizing use cases) is documented; explicit SKOS-concept linkage is a modelling assumption | Medium | E-013 |
| Use case tied to an industry/domain (e.g., financial services, credit risk, customer service RAG assistant) | `hi:hasDomainConcept` → `hint:Domain` | Observed (domain examples) / Inferred (formal property linkage) | Medium-High | E-008, E-011 |
| Each use case introduces/is governed by a team of stakeholders | `hi:hasHITeam` (UseCase → HITeam) | Inferred | Medium | E-001, E-012 |

## 3. hi:Agent / hi:HumanAgent / hi:ArtificialAgent mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| "Users" who request approval for new AI use cases | `hi:HumanAgent`; `hint:Role` = Use-Case Requester/Owner | Observed | High | E-005 |
| "Reviewers" who complete questionnaire-based risk/compliance assessments | `hi:HumanAgent`; `hint:Role` = Reviewer | Observed | High | E-005, E-013 |
| "Approvers" with designated authority to authorize use cases | `hi:HumanAgent`; `hint:Role` = Approver | Observed | High | E-005 |
| Risk & compliance teams ensuring alignment to MRM standards, audit, and AI regulations | `hi:HumanAgent`; `hint:Role` = Risk/Compliance Officer | Observed | High | E-008 |
| Model validators / internal auditors who satisfy audit and validation needs | `hi:HumanAgent`; `hint:Role` = Model Validator / Auditor | Observed | High | E-008 |
| LLM application developers who build/compare prompts and models in Evaluation Studio | `hi:HumanAgent`; `hint:Role` = AI/ML Developer | Observed | High | E-010 |
| Subject-matter experts (SMEs) performing human-in-the-loop feedback and red-teaming of agents | `hi:HumanAgent`; `hint:Role` = SME / Red-Teamer; participates via `hi:hasAgentInvolved` in an `hi:Interaction` | Observed | High | E-007 |
| Organizational leaders setting AI governance policy and accountability | `hi:HumanAgent`; `hint:Role` = Governance/Policy Leader | Observed | Medium | E-011 |
| Model Risk Governance (MRG) Master, Operational Risk Management (ORM) Master, Regulatory Compliance Management (RCM) Master, Modules Master administrator profiles | `hi:HumanAgent`; `hint:Role` = Governance-Console Administrator (per-module) | Observed | High | E-013 |
| Product Manager and Distinguished Research Staff Member credited with the Model Risk Evaluation Engine | `hi:HumanAgent`; `hint:Role` = Governance Tool Developer/Researcher (upstream of the deployed system, not a runtime team member) | Observed | Medium — role is about the tool's creators, not its in-use governance team | E-014 |
| watsonx.governance's monitoring engine (OpenScale-derived) that computes quality/fairness/drift/explainability metrics | `hi:ArtificialAgent` | Observed | High | E-003, E-005, E-009 |
| The ibm-watsonx-gov SDK and Evaluation Studio that evaluate AI applications and generate insights | `hi:ArtificialAgent` | Observed | High | E-002, E-010 |
| The Model Risk Evaluation Engine that computes AI Risk Atlas–based risk metrics for foundation models | `hi:ArtificialAgent` | Observed | High | E-014, E-015 |
| "LLM-as-a-Judge" models (e.g., Mistral AI) used to score other models' outputs | `hi:ArtificialAgent` — a governed/governing AI acting on another AI's output | Observed | High | E-010 |
| The governed predictive ML models and generative AI models/agents themselves (the subject of governance) | `hi:ArtificialAgent` | Observed | High | E-001, E-003, E-004, E-006, E-007, E-009, E-011 |
| watsonx Orchestrate's agent control plane (routes/operates agents, enforces guardrails) | `hi:ArtificialAgent` | Observed | High | E-017 |
| Discovered/"shadow AI" — AI systems operating outside formal governance | `hi:ArtificialAgent` (unmanaged instance) — a distinct governance-relevant subtype | Observed | Medium | E-001, E-013 |

## 4. hi:Goal mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Enable responsible, transparent, explainable, trustworthy AI at enterprise scale | `hi:Goal`; `hi:hasGoalConcept` → `hint:Goal` (trust/transparency) | Observed | High | E-001, E-009, E-011 |
| Achieve measurable business outcomes from AI investment (efficiency, cost, risk reduction) | `hi:Goal` | Observed | Medium-High (vendor-reported metrics, not independently audited) | E-001 |
| Satisfy regulatory compliance obligations (EU AI Act, NIST AI RMF, ISO 42001) | `hi:Goal`; each goal `hi:requiresTask` a compliance-assessment task | Observed | High | E-001, E-006, E-013 |
| Mitigate fairness/bias risk in high-stakes decisions (credit, insurance, hiring-adjacent) | `hi:Goal` | Observed | High | E-008, E-011 |
| Reduce hallucination and increase groundedness of generative AI outputs | `hi:Goal` | Observed | High | E-006, E-007, E-010 |
| Prevent unsupervised/unsafe autonomous agent actions | `hi:Goal` | Observed | High | E-004, E-007 |
| Strengthen cross-functional collaboration (engineering/legal/compliance/risk/security/data/business) | `hi:Goal`, closely tied to `hi:HITeam` | Observed | Medium | E-012 |

## 5. hi:Task / hi:TaskExecution mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Onboard an AI use case (register in Use Case Library, complete risk questionnaire) | `hi:Task`; `hi:hasTaskConcept` → `hint:Task` (Use-Case Onboarding) | Observed | High | E-013, E-016 |
| Register/subscribe a model or prompt template for monitoring | `hi:Task` | Observed | High | E-003, E-011 |
| Configure quality, fairness, drift, and explainability monitors (thresholds, sample size, favorable/unfavorable outcomes) | `hi:Task`; realized by `hi:TaskExecution` each time "Evaluate now" runs | Observed | High | E-003 |
| Compute Generative AI evaluation metrics (Faithfulness, Answer Relevance, Context Relevance, HAP, PII) over a prompt/response pair | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution`; `hi:towardsGoal` → hallucination-reduction goal | Observed | High | E-006, E-010, E-011 |
| Perform Model Risk Evaluation Engine risk-metric computation for a foundation model (Understand → Identify → Evaluate) | `hi:Task` (three sub-tasks); each `hi:realizedBy` a `hi:TaskExecution` | Observed | High | E-014 |
| Approve/authorize a use case via workflow (Reviewer → Approver chain) | `hi:Task`; realized through an `hi:Interaction` between Reviewer and Approver `hi:HumanAgent`s | Observed | High | E-005 |
| Human feedback / red-teaming of an agent | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution`; `hi:hasInteractionEpisode` → `hi:Interaction` between SME and agent | Observed | High | E-007 |
| Generate an AI Factsheet documenting model lineage, metrics, and development activity | `hi:Task`; output feeds `hi:hasExecutionConcept` metadata | Observed | High | E-009, E-011 |
| Retrain a model based on production feedback (automated retraining workflow) | `hi:Task`, with `hi:isEligibleForTask`/`hi:isAssignedToTask` distinguishing eligible vs. formally assigned agents (automated pipeline vs. human sign-off) | Observed | Medium-High | E-008 |
| Monitor an agent at runtime via watsonx Orchestrate's control plane (audit logging, policy enforcement) | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution` | Observed | Medium (integration mechanism with watsonx.governance's Governance Console not explicitly documented — see `knowledge_gaps.md`) | E-017 |

## 6. hi:Capability mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Explainability computation (LIME, SHAP) | `hi:Capability`; `hi:allowsTask` → explainability-generation task; `hi:hasCapabilityConcept` → `hint:Capability` (Explainability) | Observed | High | E-003, E-011 |
| Fairness/bias detection (Disparate Impact, Statistical Parity Difference) | `hi:Capability` | Observed | High | E-003, E-011 |
| Drift detection (data drift, model drift, system drift for agents) | `hi:Capability` | Observed | High | E-003, E-007, E-011 |
| Content-safety detection (HAP, PII, prompt-injection detection) | `hi:Capability` | Observed | High | E-004, E-007, E-009, E-011 |
| RAG-quality assessment (Faithfulness, Context Relevance, Answer Relevance/Similarity, hit rate, average precision, reciprocal rank) | `hi:Capability` | Observed | High | E-004, E-006, E-007, E-010 |
| Multi-vendor / multi-cloud model governance (watsonx.ai, Bedrock, Azure, OpenAI, VertexAI) | `hi:Capability` | Observed | High | E-006, E-009, E-011 |
| Automated Factsheet generation and lifecycle metadata capture | `hi:Capability` | Observed | High | E-009 |
| Regulatory-risk assessment against EU AI Act categories (Prohibited/High-Risk/Limited-Risk/Minimal-Risk) | `hi:Capability`; requires `hi:hasConstraintConcept` linkage to regulation-derived `hint:Constraint` | Observed | High | E-006, E-013 |
| Foundation-model risk-metric computation against the AI Risk Atlas taxonomy (accuracy, fairness, privacy, explainability dimensions across training-data/inference/output/non-technical/agentic risk categories) | `hi:Capability` | Observed | High | E-014, E-015 |
| Agent control-plane governance: policy/guardrail enforcement, identity & access control, audit logging | `hi:Capability` | Observed | High | E-017 |
| LLM-as-a-Judge comparative evaluation across models/prompts | `hi:Capability` | Observed | Medium-High | E-010 |

## 7. hi:Context mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Regulatory frameworks: EU AI Act, NIST AI RMF, ISO 42001, Data & Trust Alliance | `hi:Context`; `hi:hasContextConcept` → `hint:Context`; also `hi:hasConstraintConcept` → `hint:Constraint` | Observed | High | E-001, E-006, E-013 |
| Regulated industries: banking, insurance (fair lending, equitable pricing, AML) | `hi:Context`; `hi:hasContextConcept` → `hint:Domain`(financial services) | Observed | High | E-008 |
| Multi-cloud / multi-vendor operating environment (on-prem, IBM Cloud, AWS, Azure, GCP) | `hi:Context` | Observed | High | E-006, E-009, E-011, E-016 |
| Unmanaged/"shadow AI" operating context — AI deployed outside governance visibility | `hi:Context`; `hi:hasPhenomenonConcept` → `hint:Phenomenon` (governance gap) | Observed | Medium | E-001, E-013 |
| Autonomous/agentic operating conditions with unsupervised action-taking | `hi:Context`; `hi:hasPhenomenonConcept` → `hint:Phenomenon` (agent autonomy risk) | Observed | High | E-004, E-007 |
| Five-category AI risk landscape (training data, inference, output, non-technical, agentic risks) as the phenomena the Context gives rise to | `hi:hasPhenomenonConcept` → `hint:Phenomenon`; `hi:hasInfluenceOn` → HITeam (the risk landscape shapes how the team must operate) | Observed | High | E-015 |
| Context influencing team collaboration/task performance (regulatory pressure shaping governance workflow design) | `hi:hasInfluenceOn` (Context → HITeam) | Inferred — relationship is logically implied by the evidence but not phrased in these exact ontological terms by IBM | Medium | E-001, E-008, E-013 |

## 8. hi:Interaction mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Use-case approval workflow exchange between Requester → Reviewer → Approver | `hi:Interaction`; `hi:hasAgentInvolved` (≥2 HumanAgents); `hi:hasInteractionIntentConcept` = approval/authorization | Observed | High | E-005 |
| SME red-teaming / human-feedback session with an agent | `hi:Interaction`; `hi:hasAgentInvolved` (HumanAgent SME + ArtificialAgent agent); `hi:hasInteractionIntentConcept` = verification/probing | Observed | High | E-007 |
| Developer comparing multiple LLMs/prompts in Evaluation Studio (human directing, AI responding, human judging via LLM-as-Judge assistance) | `hi:Interaction`; `hi:hasInteractionModalityConcept` = interactive UI/experiment configuration | Observed | Medium-High | E-010 |
| Embedded AI assistants used by humans to onboard use cases and capture governance information via "conversational interfaces" | `hi:Interaction`; `hi:hasInteractionModalityConcept` = conversational/chat | Observed | High | E-001 |
| Cross-functional collaboration across engineering/legal/compliance/risk/security/data/business roles | `hi:Interaction` (recurring, policy-level) | Observed | Medium | E-012 |

## 9. hi:Evaluation / hi:Experiment mappings

| watsonx.governance concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| A configured monitor run ("Evaluate now") producing quality/fairness/drift/explainability results | `hi:Evaluation`; `hi:evaluatedBy` (TaskExecution → Evaluation) | Observed | High | E-003 |
| Evaluation Studio experiment comparing multiple LLMs/prompt templates with weighted metric ranking | `hi:Experiment`; `hi:hasExperiment` (Evaluation → Experiment) | Observed | High | E-010 |
| Model Risk Evaluation Engine's foundation-model risk-metric computation and PDF report generation | `hi:Evaluation`; `hi:hasEvaluationConcept`, `hi:hasMetricConcept` → risk metrics | Observed | High | E-014 |
| RAG evaluation metrics used as the tested variables of an experiment (Faithfulness, Context Relevance, Answer Relevance/Similarity) | `hi:hasMetricTested` (Experiment → metric concepts) | Observed | High | E-004, E-006, E-007, E-010 |
| Null/alternative hypothesis formulation for an A/B-style prompt or model comparison | `hi:hasNullHypothesis`, `hi:hasAlternativeHypothesis` | Inferred — Evaluation Studio performs comparative experiments consistent with hypothesis-testing structure, but IBM sources do not use formal null/alternative-hypothesis language | Low-Medium | E-010 (inferred extension) |
| Runtime agent performance evaluation (accuracy, tool-call reliability, completion rate, cost, safety) via watsonx Orchestrate | `hi:Evaluation`; `hint:Metric` | Observed | High | E-017 |

## 10. hint: Thesaurus concept mappings (representative, non-exhaustive)

| watsonx.governance term | hint: concept type |
|---|---|
| Use-Case Owner, Reviewer, Approver, Risk/Compliance Officer, Model Validator/Auditor, AI/ML Developer, SME/Red-Teamer, Governance-Console Administrator | `hint:Role` |
| Credit-risk scoring, fraud detection, RAG customer-support assistant, autonomous investment-assistant agent | `hint:Domain` / `hint:UseCase` |
| Use-Case Onboarding, Model Registration, Monitor Configuration, Risk Questionnaire Completion, Factsheet Generation, Approval Review, Red-Teaming | `hint:Task` |
| Explainability (LIME/SHAP), Fairness Detection, Drift Detection, Content-Safety Screening, Multi-Vendor Model Integration, EU AI Act Risk Assessment | `hint:Capability` |
| EU AI Act, NIST AI RMF, ISO 42001, Data & Trust Alliance, Banking/Insurance MRM standards | `hint:Constraint` / `hint:Context` |
| Shadow-AI prevalence, agent autonomy risk, hallucination tendency, training-data bias | `hint:Phenomenon` |
| Disparate Impact, Statistical Parity Difference, Accuracy/ROC/RMSE/MAE/R², Rouge/SARI/METEOR/BLEU, Faithfulness, Answer Relevance/Similarity, Context Relevance, HAP score, PII detection rate, Unsuccessful-request rate, Hit Rate, Average Precision, Reciprocal Rank, Tool-Selection Quality, System Drift, Completion Rate, Tool-Call Reliability | `hint:Metric` |
| Approval workflow, Conversational onboarding assistant, Red-teaming session | `hint:InteractionModalityConcept` / `hint:InteractionIntentConcept` |
| LIME, SHAP, LLM-as-a-Judge, Detached Prompt Template, Custom ML Provider Proxy | `hint:Method` |

---

## Notes on Mapping Method

1. Every mapping above is anchored to at least one Evidence ID from `sources.md`; rows marked **Inferred** state explicitly why the inference was necessary (usually: the TTL's formal cardinality/property structure implies a relationship that IBM's marketing/technical prose does not phrase in ontology-native terms).
2. No `skos:Concept` instances, class instances, or property assertions are created here — this table only names the mapping target class/property from the ontology; instantiation is deferred to the (out-of-scope) Knowledge Graph construction phase.
3. Where the HI Ontology has an OWL cardinality restriction (e.g., `hi:HITeam` requires ≥1 `hi:HumanAgent` and ≥1 `hi:ArtificialAgent`; `hi:Task` requires ≥1 `hi:Capability`; `hi:Goal` requires ≥1 `hi:Task`; `hi:Interaction` requires ≥2 `hi:Agent`), the mapping table was checked against that restriction and, where evidence for one side was thin, this is flagged in the Observed/Inferred column rather than silently assumed.
