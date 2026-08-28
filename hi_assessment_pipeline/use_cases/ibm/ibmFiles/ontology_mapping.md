# Ontology Mapping — IBM watsonx.governance

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **IBM watsonx.governance**
Maps every extracted concept to the Hybrid Intelligence (HI) Ontology (VU Amsterdam, KAI Group, v2.0.0) as supplied (`hiontology.ttl` + diagram). Namespaces: `hi: https://w3id.org/hi-ontology#`, `hint: https://w3id.org/hi-thesaurus#`.

This file documents mappings only. **No RDF triples, no ontology instances, and no SHACL shapes are produced here**, per RAS Section 5/15.

---

## 1. Top-level use case framing

| Extracted concept | HI Ontology class/property | Evidence |
|---|---|---|
| IBM watsonx.governance (the product/platform as a governed application domain) | `hi:UseCase` | E-001 |
| Each of the 8 scenarios (Predictive Model Governance, RAG Evaluation, GenAI Use-Case Onboarding, Adversarial Red-Teaming, Agentic AI Governance, Virtual Assistant Monitoring, AI-Governed Recruitment, Multi-Cloud/MRG) | `hi:UseCase` (one instance per scenario, `hi:introducesHITeam`-linked to its `hi:HITeam`) | E-001–E-022 (per-scenario, see `scenarios.md`) |
| The set of human + artificial agents collaborating within one scenario (e.g., recruiter + IRIS + watsonx.ai model) | `hi:HITeam` | All scenarios |
| Domain classification (HR/Recruitment, Financial Services, Enterprise AI Governance, Software Engineering) | `hint:Domain` via `hi:hasDomainConcept` | E-001, E-016, E-022 |

---

## 2. Agents

### Human Agents (`hi:HumanAgent`, subclass of `hi:Agent` and `foaf:Person`)

| Extracted role | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| Business Analyst | `hi:HumanAgent` — role concept "Business Analyst" via `hi:hasRoleConcept` | S1 | E-017 |
| Data Scientist | `hi:HumanAgent` — role "Data Scientist" | S1 | E-017, E-006 |
| ML Engineer | `hi:HumanAgent` — role "ML Engineer" | S1, S8 | E-017, E-020 |
| ModelOps Engineer | `hi:HumanAgent` — role "ModelOps Engineer" | S1, S8 | E-017, E-020 |
| Data Analyst | `hi:HumanAgent` — role "Data Analyst" | S1 | E-017 |
| Prompt Engineering Team / Prompt Engineer | `hi:HumanAgent` — role "Prompt Engineer" | S2, S3, S4 | E-017, E-012, E-020 |
| Model Requestor / Owner | `hi:HumanAgent` — role "Model Owner" | S3, S8 | E-020, E-007 |
| Model Validator / Reviewer | `hi:HumanAgent` — role "Model Validator" | S1, S2, S8 | E-020, E-015 |
| Model Risk Officer | `hi:HumanAgent` — role "Risk Officer" | S8 | E-020, E-001, E-022 |
| Approver | `hi:HumanAgent` — role "Approver" | S3, S8 | E-003, E-020 |
| Legal Reviewer | `hi:HumanAgent` — role "Legal Reviewer" | S3 | E-007 |
| Data Protection Reviewer | `hi:HumanAgent` — role "Data Protection Officer" | S3 | E-007 |
| Brand Team Reviewer | `hi:HumanAgent` — role "Brand Reviewer" | S3 | E-007 |
| Stakeholder Reviewer (business validation) | `hi:HumanAgent` — role "Business Stakeholder" | S3 | E-007 |
| Subject Matter Expert (SME) / Red Teamer | `hi:HumanAgent` — role "SME / Red Teamer" | S4, S5 | E-005, E-012 |
| Application/AppSec Engineer | `hi:HumanAgent` — role "Application Engineer" | S4 | E-012 |
| Agent Developer | `hi:HumanAgent` — role "Agent Developer" | S5 | E-005, E-011 |
| Compliance/Audit Team | `hi:HumanAgent` — role "Compliance Officer" | S1, S8 | E-001, E-006 |
| Recruiter / Talent Team | `hi:HumanAgent` — role "Recruiter" | S7 | E-016 |
| Hiring Manager | `hi:HumanAgent` — role "Hiring Manager" | S7 | E-016 |
| HR Leader | `hi:HumanAgent` — role "HR Leader" | S7 | E-016 |
| Virtual Assistant Owner / Conversation Designer | `hi:HumanAgent` — role "Conversational AI Engineer" | S6 | E-013 |
| Ground-truth-providing SME (conversational) | `hi:HumanAgent` — role "Domain SME" | S6 | E-013 |
| Chief Risk Officer / Model Risk Sign-off (financial services) | `hi:HumanAgent` — role "Risk Officer" *(role title Inferred — see below)* | S8 | E-022 (role title not explicitly named — **Inferred**, Medium confidence: standard MRM industry titles applied to an explicitly stated but unnamed "human risk oversight" role) |

### Artificial Agents (`hi:ArtificialAgent`, subclass of `hi:Agent`, disjoint with `hi:HumanAgent`)

| Extracted component | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| Watson OpenScale (monitoring engine) | `hi:ArtificialAgent` — agent concept "Model Monitoring Engine" | S1, S6, S8 | E-003, E-006, E-013 |
| AutoAI (automated model training) | `hi:ArtificialAgent` — agent concept "AutoML System" | S1 | E-006 |
| SHAP/LIME explainability engine | `hi:ArtificialAgent` — agent concept "Explainability Engine" | S1 | E-006, E-021 |
| AI FactSheets service (documentation automation) | `hi:ArtificialAgent` — agent concept "Documentation Automation Agent" | S1, S2, S8 | E-009, E-014 |
| Governed foundation model (watsonx.ai LLM) | `hi:ArtificialAgent` — agent concept "Foundation Model" | S2, S3, S4, S6, S7 | E-008, E-015, E-016 |
| LLM-as-Judge model | `hi:ArtificialAgent` — agent concept "Judge Model" | S2 | E-015 |
| Fine-tuned slate evaluation model (125M param) | `hi:ArtificialAgent` — agent concept "Evaluation Model" | S2 | E-015 |
| Red-teaming evaluator | `hi:ArtificialAgent` — agent concept "Red-Teaming Agent" | S4 | E-012 |
| Governed Agentic Catalog agents/tools | `hi:ArtificialAgent` — agent concept "Governed Agent" | S5 | E-005 |
| Third-party model via Custom ML Provider proxy (Bedrock, Azure OpenAI, Vertex AI) | `hi:ArtificialAgent` — agent concept "Third-Party Model (proxied)" | S8 | E-019 |
| Detached Prompt Template (representation of externally hosted LLM) | `hi:ArtificialAgent` — agent concept "Detached Prompt Template Agent" | S8 | E-019 |
| IRIS (AI voice screening assistant) | `hi:ArtificialAgent` — agent concept "Conversational Screening Agent" | S7 | E-016 |
| Virtual Assistant / chatbot under monitoring | `hi:ArtificialAgent` — agent concept "Virtual Assistant" | S6 | E-013 |
| Embedded AI governance assistant (onboards use cases) | `hi:ArtificialAgent` — agent concept "Governance Assistant" | S3 | E-001 |
| ibm-watsonx-gov SDK metrics evaluator | `hi:ArtificialAgent` — agent concept "Metrics Evaluator SDK" | S1–S8 (cross-cutting) | E-011 |

---

## 3. Goals, Tasks, Capabilities

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| "Establish trustworthy, compliant, monitored AI in production" | `hi:Goal` | All | E-001 |
| "Reduce time-to-hire while ensuring fair candidate evaluation" | `hi:Goal` | S7 | E-016 |
| "Minimize hallucination and maximize grounded answer quality" | `hi:Goal` | S2 | E-008, E-015 |
| "Achieve EU AI Act compliance for the use case" | `hi:Goal` | S3 | E-008 |
| "Harden prompts against adversarial manipulation" | `hi:Goal` | S4 | E-012 |
| Model inventory creation | `hi:Task` — task concept "Model Onboarding" | S1, S8 | E-006, E-017 |
| Model training (AutoAI) | `hi:Task` — task concept "Model Training" | S1 | E-006 |
| Model deployment as REST endpoint | `hi:Task` — task concept "Model Deployment" | S1 | E-006 |
| Configure monitoring thresholds (fairness/quality/drift/explainability) | `hi:Task` — task concept "Monitor Configuration" | S1 | E-006 |
| Evaluate model against test dataset | `hi:Task` — task concept "Model Evaluation" | S1, S2 | E-006, E-015 |
| Author / update AI FactSheet | `hi:Task` — task concept "Documentation Authoring" | S1, S2, S8 | E-009, E-009c, E-014 |
| Retrieve context passages (RAG retrieval) | `hi:Task` — task concept "Information Retrieval" | S2 | E-015 |
| Generate grounded answer | `hi:Task` — task concept "Answer Generation" | S2 | E-015 |
| Compute retrieval/answer metrics | `hi:Task` — task concept "Quality Evaluation" | S2 | E-015 |
| Root-cause analysis of threshold violation | `hi:Task` — task concept "Root Cause Analysis" | S2 | E-015 |
| Create use case & custom risk fields | `hi:Task` — task concept "Use Case Registration" | S3 | E-007 |
| Complete risk questionnaire | `hi:Task` — task concept "Risk Assessment" | S3, S8 | E-007, E-020 |
| Multi-stage stakeholder review (Legal/Data Protection/Brand) | `hi:Task` — task concept "Stakeholder Review" | S3 | E-007 |
| EU AI Act applicability determination | `hi:Task` — task concept "Regulatory Applicability Assessment" | S3 | E-008 |
| Development authorization / sign-off | `hi:Task` — task concept "Use Case Approval" | S3, S8 | E-007, E-020 |
| Red-team prompt template | `hi:Task` — task concept "Red Teaming" | S4, S5 | E-012, E-005 |
| Compute adversarial robustness / leakage score | `hi:Task` — task concept "Security Evaluation" | S4 | E-012 |
| Harden prompt (add instructions / swap to safety-trained model) | `hi:Task` — task concept "Prompt Hardening" | S4 | E-012 |
| Recompute metrics post-hardening | `hi:Task` — task concept "Regression Evaluation" | S4 | E-012 |
| Agent risk assessment at use-case creation | `hi:Task` — task concept "Agent Risk Assessment" | S5 | E-005 |
| Evaluate agent competence / benchmark tasks | `hi:Task` — task concept "Agent Benchmarking" | S5 | E-005 |
| Human feedback / red-teaming of agent actions | `hi:Task` — task concept "Human-in-the-Loop Verification" | S5 | E-005 |
| Continuous production monitoring with alerting | `hi:Task` — task concept "Production Monitoring" | S1, S5, S6, S8 | E-006, E-005, E-013, E-019 |
| Résumé parsing & candidate scoring | `hi:Task` — task concept "Candidate Screening" | S7 | E-016 |
| AI voice screening call | `hi:Task` — task concept "Automated Interview" | S7 | E-016 |
| Structured interview coordination | `hi:Task` — task concept "Interview Coordination" | S7 | E-016 |
| Manager review of shortlisted candidates | `hi:Task` — task concept "Candidate Review" | S7 | E-016 |
| Payload logging (Q&A interactions) | `hi:Task` — task concept "Interaction Logging" | S6 | E-013 |
| Alert review & prompt improvement | `hi:Task` — task concept "Alert Triage" | S6 | E-013 |
| Log model metadata via Factsheet SDK | `hi:Task` — task concept "Metadata Logging" | S8 | E-019 |
| Subscribe third-party model via proxy | `hi:Task` — task concept "Model Integration" | S8 | E-019 |
| Automate retraining/review workflow from production feedback | `hi:Task` — task concept "Retraining Workflow" | S8 | E-022 |
| Fairness/bias evaluation | `hi:Capability` — capability concept "Fairness Assessment" (`hi:allowsTask` → Model Evaluation, Risk Assessment) | S1, S7, S8 | E-006, E-016, E-022 |
| Explainability generation (SHAP/LIME) | `hi:Capability` — capability concept "Explainability" | S1 | E-006, E-021 |
| Drift detection | `hi:Capability` — capability concept "Drift Detection" | S1, S8 | E-006, E-019 |
| GenAI quality scoring (ROUGE, BLEU, METEOR, SARI, etc.) | `hi:Capability` — capability concept "Text Quality Evaluation" | S2, S6, S8 | E-020, E-013 |
| PII/HAP content detection | `hi:Capability` — capability concept "Content Safety Detection" | S6, S8 | E-013, E-019 |
| Prompt-injection/leakage detection | `hi:Capability` — capability concept "Adversarial Robustness" | S4 | E-012 |
| Retrieval quality assessment (Context Relevance, NDCG, Hit Rate) | `hi:Capability` — capability concept "Retrieval Evaluation" | S2 | E-015 |
| No-code workflow/questionnaire authoring | `hi:Capability` — capability concept "Workflow Configuration" | S3 | E-003 |
| Voice-based candidate interviewing | `hi:Capability` — capability concept "Conversational Screening" | S7 | E-016 |

---

## 4. Task Execution, Interaction, Evaluation, Experiment

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| A single monitored production inference (transaction) | `hi:TaskExecution` — `hi:realizesTask` → Model Evaluation/Production Monitoring; `hi:performedBy` the ArtificialAgent (model) | S1, S6, S8 | E-006, E-013 |
| One RAG query/response cycle logged for evaluation | `hi:TaskExecution` — `hi:realizesTask` → Answer Generation; `hi:evaluatedBy` → Evaluation | S2 | E-015 |
| One red-teaming probe against a prompt template | `hi:TaskExecution` — `hi:realizesTask` → Red Teaming | S4 | E-012 |
| One agent tool-call within a LangGraph application | `hi:TaskExecution` — `hi:realizesTask` → Agent Benchmarking; `hi:hasMethodConcept` → "Python decorator instrumentation" | S5 | E-005 |
| One IRIS screening call with a candidate | `hi:TaskExecution` — `hi:realizesTask` → Automated Interview; `hi:hasInteractionEpisode` → Interaction (candidate + IRIS) | S7 | E-016 |
| Multi-stage stakeholder review episode (Legal + Data Protection + Brand + Stakeholder) | `hi:Interaction` — `hi:hasAgentInvolved` (≥2 agents: requester + each reviewer); `hi:hasInteractionIntentConcept` → "Review/Negotiate" | S3 | E-007 |
| SME red-teaming / human feedback episode on agent actions | `hi:Interaction` — `hi:hasAgentInvolved` (SME + Agent); `hi:hasInteractionIntentConcept` → "Verify/Probe" | S5 | E-005 |
| Root-cause drill-down / source-attribution review by validator | `hi:Interaction` — `hi:hasAgentInvolved` (Validator + Evaluation system); `hi:hasInteractionIntentConcept` → "Explain" | S2 | E-015 |
| Candidate voice conversation with IRIS | `hi:Interaction` — `hi:hasAgentInvolved` (Candidate + IRIS); `hi:hasInteractionModalityConcept` → "Voice/Spoken" | S7 | E-016 |
| Threshold-breach alert reviewed by engineer | `hi:Interaction` — `hi:hasAgentInvolved` (Engineer + Monitoring Agent); `hi:hasInteractionModalityConcept` → "Dashboard/UI Alert" | S1, S6 | E-006, E-013 |
| Fairness/quality/drift/explainability assessment of a deployed model | `hi:Evaluation` — `hi:hasMetricConcept` → (Disparate Impact, Statistical Parity Difference, Accuracy, Drift Magnitude) | S1, S8 | E-006, E-019 |
| RAG retrieval + answer evaluation run | `hi:Evaluation` — `hi:hasExperiment` → Experiment comparing LLM-as-judge vs. slate-model judge | S2 | E-015 |
| Red-teaming security evaluation | `hi:Evaluation` — `hi:hasMetricConcept` → (Adversarial Robustness Score, Prompt Leakage Risk Score); `hi:hasExperiment` → attack-suite run at basic/intermediate/advanced levels | S4 | E-012 |
| Agent benchmarking run | `hi:Evaluation` — `hi:hasMetricConcept` → (Tool-call reliability, Completion rate, Cost, Safety) | S5 | E-005, E-018 |
| Conversational monitoring evaluation | `hi:Evaluation` — `hi:hasMetricConcept` → (PII, HAP, ROUGE, METEOR, Readability) | S6 | E-013 |
| Prompt-hardening A/B experiment (baseline vs. hardened prompt) | `hi:Experiment` — `hi:hasNullHypothesis` "hardening does not reduce adversarial-robustness score"; `hi:hasAlternativeHypothesis` "hardening reduces adversarial-robustness score" *(hypothesis wording — Inferred; the underlying comparison is Observed in E-012, the formal null/alternative phrasing is a modelling convenience)* | S4 | E-012 (Inferred framing) |

---

## 5. Context, Constraint, Phenomenon

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| EU AI Act regulatory environment | `hi:Context` — `hi:hasContextConcept` → "EU AI Act"; `hi:hasConstraintConcept` → risk-category obligations | S3, S8 | E-008 |
| NIST AI RMF, ISO 42001, Data & Trust Alliance frameworks | `hi:Context` — `hi:hasContextConcept` | S1, S8 | E-001 |
| Banking/insurance Model Risk Management (MRM) standards, multi-jurisdiction | `hi:Context` — `hi:hasContextConcept` → "Financial Services Regulation" | S8 | E-022 |
| GDPR / data-protection obligations | `hi:Context` — `hi:hasConstraintConcept` | S3 | E-007 |
| Multi-cloud deployment environment (AWS, Azure, GCP, OpenAI, watsonx.ai) | `hi:Context` — `hi:hasContextConcept` → "Multi-Cloud AI Estate" | S8 | E-014, E-019 |
| High-volume, high-turnover hiring environment | `hi:Context` — `hi:hasContextConcept` → "High-Volume Recruitment" | S7 | E-016 |
| LangGraph / multi-agent orchestration runtime | `hi:Context` — `hi:hasContextConcept` → "Agentic Orchestration Runtime" | S5 | E-005 |
| Bias / demographic disparity emergence in payload data | `hi:Context` `hi:hasPhenomenonConcept` → "Bias Emergence" (phenomenon exhibited by the operating context) | S1, S7, S8 | E-006, E-016, E-022 |
| Model/data drift from shifting market or user-behavior conditions | `hi:Context` `hi:hasPhenomenonConcept` → "Concept Drift" | S1, S8 | E-006, E-022 |
| Hallucination phenomenon in ungrounded LLM output | `hi:Context` `hi:hasPhenomenonConcept` → "Hallucination" | S2 | E-008, E-015 |
| Adversarial manipulation / jailbreak susceptibility | `hi:Context` `hi:hasPhenomenonConcept` → "Adversarial Susceptibility" | S4 | E-012 |
| AI Risk Atlas taxonomy (agentic/generative/ML risks) | `hint:Constraint` / `hint:Phenomenon` concept source (controlled vocabulary reference) | S3, S5, S8 | E-010 |

---

## 6. CARE Framework Dimension Mapping

The HI Ontology does not encode CARE as a formal class, but the RAS (Section 18/17) requires every scenario to be checked against it. CARE dimensions are mapped onto existing `hi:` properties as follows:

| CARE Dimension | HI Ontology anchor | Representative evidence |
|---|---|---|
| **Collaborative** — human and AI agents share tasks/goals | `hi:HITeam` (`hi:hasMember` on both `hi:HumanAgent` and `hi:ArtificialAgent`); `hi:Interaction` | All scenarios; explicitly stated in E-003 (requester/reviewer/approver), E-005 (SME + agent) |
| **Adaptive** — system learns/personalises over time | `hi:Task` "Retraining Workflow"; `hi:Evaluation` drift monitoring feeding back into `hi:Task` "Monitor Configuration" | E-022 (automated retraining from production feedback), E-006 (drift-triggered alerts) |
| **Responsible** — fairness, accountability, transparency | `hi:Capability` "Fairness Assessment"; `hi:Task` "Documentation Authoring" (FactSheets); OpenPages audit trail | E-006, E-009, E-001 (audit, compliance dashboards) |
| **Explainable** — decisions are interpretable | `hi:Capability` "Explainability"; `hi:TaskExecution` local/global SHAP explanation; source-attribution in RAG | E-021, E-006, E-015 |

---

## 7. Data Properties

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| Formal null hypothesis text for a red-teaming/hardening experiment | `hi:hasNullHypothesis` (xsd:string) | S4 | E-012 (Inferred wording) |
| Formal alternative hypothesis text for the same experiment | `hi:hasAlternativeHypothesis` (xsd:string) | S4 | E-012 (Inferred wording) |

---

## 8. Summary table — Concept → Ontology Class (illustrative, per RAS Section 16 File 6 example format)

```
IBM watsonx.governance                          → hi:UseCase
Recruiter                                       → hi:HumanAgent
Hiring Manager                                  → hi:HumanAgent
IRIS (voice screening assistant)                → hi:ArtificialAgent
watsonx.ai foundation model                     → hi:ArtificialAgent
Watson OpenScale                                → hi:ArtificialAgent
Reduce time-to-hire with fair screening         → hi:Goal
Résumé parsing and candidate scoring            → hi:Task
Voice-based candidate interviewing              → hi:Capability
IRIS screening call with a candidate            → hi:TaskExecution
Candidate + IRIS voice conversation             → hi:Interaction
High-volume recruitment environment             → hi:Context
Bias/drift evaluation of screening outcomes     → hi:Evaluation
Model Risk Officer                              → hi:HumanAgent
AI Model Risk Assessment questionnaire          → hi:Task
EU AI Act                                       → hint:Context concept (via hi:hasContextConcept)
Faithfulness (RAG metric)                       → hint:Metric concept (via hi:hasMetricConcept)
Adversarial Robustness Score                    → hint:Metric concept (via hi:hasMetricConcept)
```

No RDF triples, SKOS concept schemes, or SHACL shapes are produced in this document — mappings are documented in natural-language/table form only, per RAS Section 5 and Section 16 (File 6) instructions.
