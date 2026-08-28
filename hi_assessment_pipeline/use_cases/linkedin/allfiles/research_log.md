# Research Log
## Neuro-Symbolic AI — Hybrid Intelligence Knowledge Acquisition
### Target: LinkedIn Recruiter + Hiring Assistant
### Date: 2026-06-28

---

## SEARCH SESSION 1 — Official LinkedIn Product Documentation

### Objective
Identify officially documented features, capabilities, workflows, agents, and goals of LinkedIn Recruiter and LinkedIn Hiring Assistant.

### Search Terms
- `LinkedIn Recruiter AI features hiring assistant 2024 2025 official documentation`
- `LinkedIn Hiring Assistant AI agent features capabilities workflow recruiter 2025`

### Search Engine
Web search (current-date aware)

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-001 | LinkedIn News: Hiring Assistant globally available | https://news.linkedin.com/2025/hiring-assistant-globally-available |
| E-002 | LinkedIn Recruiter + Hiring Assistant product page | https://business.linkedin.com/hire/recruiter |
| E-003 | 2024 LinkedIn Hiring Release features | https://business.linkedin.com/talent-solutions/product-update/hire-release |
| E-004 | Reimagining Hiring with AI — LinkedIn Blog | https://www.linkedin.com/business/talent/blog/talent-acquisition/reimagining-hiring-and-learning-with-power-of-ai |
| E-005 | Hiring Assistant product page | https://business.linkedin.com/hire/hiring-assistant |
| E-006 | AI-Assisted Search and Projects in Recruiter | https://business.linkedin.com/talent-solutions/ai-assisted-search-and-projects |
| E-007 | Introducing Hiring Assistant blog post | https://www.linkedin.com/business/talent/blog/talent-acquisition/introducing-hiring-assistant |

### Sources Rejected
- Blog posts with no primary source backing — rejected as insufficient evidence without corroboration.
- Marketing material with no technical specifics.

### Information Extracted
- Hiring Assistant is LinkedIn's first AI agent for recruiters (agentic product).
- Launched October 2024 to charter customers; globally available in English by end September 2025; German and French rolling out in 2026.
- Core tasks automated by Hiring Assistant: (1) sourcing — searching 1.2B+ profiles; (2) evaluating — profiling candidates against qualifications; (3) engaging — InMail prescreening.
- Recruiter specifies qualifications in natural language; HA refines into search queries.
- Key efficiency metrics: 4+ hours saved per role; 81% fewer profiles reviewed; 66% higher InMail acceptance vs traditional sourcing.
- Human remains in control; Hiring Assistant does not make autonomous decisions.
- AI learns from recruiter past activity on similar roles.
- Available to customers as an add-on to LinkedIn Recruiter.

### Ontology Concepts Discovered
- HumanAgent: Recruiter
- ArtificialAgent: Hiring Assistant
- Task: CandidateSourcing, CandidateEvaluation, CandidateEngagement
- Goal: HireQualifiedCandidates, ReduceRecruiterBurden
- Interaction: RecruiterHiringAssistantDialogue, HiringAssistantCandidateInMail
- Evaluation Metric: InMailAcceptanceRate, ProfilesReviewedPerHire, TimeSavedPerRole

### Scenarios Supported
- S1 (AI-Assisted Candidate Sourcing), S2 (AI-Driven Candidate Evaluation), S3 (Automated Prescreening)

### Remaining Unknowns After Session 1
- Internal architecture details (sub-agents, orchestration)
- Training data details
- Fairness mechanisms in detail

---

## SEARCH SESSION 2 — LinkedIn Engineering Blog: AI Architecture

### Objective
Identify internal architecture, ML models, ranking systems, and technical design of LinkedIn Recruiter AI.

### Search Terms
- `LinkedIn Engineering Blog recruiter AI ranking model fairness explainability` (site:engineering.linkedin.com)
- `LinkedIn talent search ranking model machine learning recruiter system architecture` (site:engineering.linkedin.com)
- `LinkedIn Hiring Assistant architecture multi-agent supervisor orchestration QCon 2025`

### Search Engine
Web search (site-filtered and general)

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-008 | Engineering Blog: AI Behind LinkedIn Recruiter Search | https://engineering.linkedin.com/blog/2019/04/ai-behind-linkedin-recruiter-search-and-recommendation-systems |
| E-009 | Engineering Blog: Fairness in AI products | https://engineering.linkedin.com/blog/2022/a-closer-look-at-how-linkedin-integrates-fairness-into-its-ai-pr |
| E-010 | Engineering Blog: Building Representative Talent Search | https://engineering.linkedin.com/blog/2018/10/building-representative-talent-search-at-linkedin |
| E-011 | Engineering Blog: Transparent and Explainable AI | https://engineering.linkedin.com/blog/2021/transparent-and-explainable-AI-systems |
| E-012 | QCon London 2025: Lessons Learned Building LinkedIn's First Agent | https://qconlondon.com/presentation/apr2025/lessons-learned-building-linkedins-first-agent-hiring-assistant |
| E-013 | ZenML: Building LinkedIn's First Production Agent | https://www.zenml.io/llmops-database/building-linkedin-s-first-production-agent-hiring-assistant-platform-and-architecture |
| E-014 | InfoQ: LinkedIn Builds Enterprise Multi-Agent AI | https://www.infoq.com/news/2025/09/linkedin-multi-agent/ |
| E-015 | MLSavvy Part 1: Inside LinkedIn's AI Agents | https://mlsavvy.substack.com/p/part-1-inside-linkedins-ai-agents |
| E-016 | MLSavvy Part 2: Inside LinkedIn's AI Agents | https://mlsavvy.substack.com/p/part-2-inside-linkedins-ai-agents |
| E-017 | Engineering Blog: LiFT — LinkedIn Fairness Toolkit | https://engineering.linkedin.com/blog/2020/lift-addressing-bias-in-large-scale-ai-applications |
| E-018 | Engineering Blog: LinkedIn Fairness Toolkit Large-Scale | https://engineering.linkedin.com/blog/2021/using-the-linkedin-fairness-toolkit-large-scale-ai |

### Sources Rejected
- Generic ML blog posts without specific LinkedIn system details.

### Information Extracted

**Recruiter Search System (pre-Hiring Assistant):**
- Online system: Galene search engine broker fans out queries to multiple index partitions; ML models rank candidates per partition.
- Offline system: Periodic model retraining using recruiter usage logs.
- Ranking models: Gradient Boosted Decision Trees (GBDT) for search ranking; Generalized Linear Mixed (GLMix) models for entity-level personalisation.
- Two-pass ranking: First pass coarse; second pass reranking over smaller set.
- Features: work experience/skills similarity, job location, likelihood of candidate response.

**Hiring Assistant Architecture (agentic):**
- Supervisor-and-sub-agent architecture (org-chart model).
- Sub-agents: Intake Agent (qualifications), Sourcing Agent (discovery), Evaluation Agent (evidence-cited summaries), Outreach/Screening Agent.
- Orchestration: LangChain / LangGraph; reuses LinkedIn's existing messaging infrastructure.
- Dual model: GPT-4o (Azure OpenAI) for complex instruction-following + EON (fine-tuned on Economic Graph data) for large-scale candidate evaluation.
- Speculative decoding for latency optimisation.
- Prompt management system; LLM inference abstraction layer; skill registry for dynamic tool discovery.

**Fairness:**
- LinkedIn Fairness Toolkit (LiFT): measures bias in training data, evaluates fairness notions for ML models, detects statistical differences across subgroups.
- Fair model analyser and mitigation trainer.
- Representative Ranking: fairness-aware re-ranking deployed to 100% of LinkedIn Recruiter users worldwide; ~3x increase in queries with representative results (Geyik et al. KDD 2019).
- Definition of fairness: ranked results representative of the qualified population.

**Explainability:**
- XAI approach: unravelling the "AI mystery box."
- Actionable insights: e.g., suggest expanding search criteria to include related skills.
- Qualification match/gap indicators shown in results.

### Ontology Concepts Discovered
- ArtificialAgent: SupervisorAgent, IntakeAgent, SourcingAgent, EvaluationAgent, OutreachAgent, GBDTRankingModel, GLMixPersonalisationModel, EONModel, LiFTFairnessToolkit, RepresentativeRankingSystem
- Capability: FairnessAwareReranking, NaturalLanguageQueryParsing, CandidateEvaluationWithEvidenceCitation, SpeculativeDecoding
- Interaction: SupervisorSubAgentOrchestration
- FeedbackMechanism: RecruiterUsageLogTraining

### Scenarios Supported
- S1, S2, S4 (Representative Ranking / Fairness), S5 (Explainability)

### Remaining Unknowns After Session 2
- Exact EON model training details
- Specific SHACL constraints or schema definitions used internally (not public)
- Detailed prompt management internals

---

## SEARCH SESSION 3 — LinkedIn AI Transparency Documentation (Official)

### Objective
Extract official statements on responsible AI principles, governance, fairness, explainability, data privacy, and compliance.

### Search Terms
- `LinkedIn AI transparency responsible AI recruiter fairness 2024 site:linkedin.com`
- Direct fetch: `https://business.linkedin.com/talent-solutions/ai-transparency`
- Direct fetch: `https://business.linkedin.com/hire/ai-transparency/hire`

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-019 | LinkedIn AI Transparency — Main Page | https://business.linkedin.com/hire/ai-transparency |
| E-020 | LinkedIn AI Transparency — Hire Products Spotlight | https://business.linkedin.com/hire/ai-transparency/hire |
| E-021 | LinkedIn Engineering: Responsible AI Update | https://engineering.linkedin.com/blog/2021/responsible-ai-update |
| E-022 | LinkedIn Engineering: Fairness Privacy Transparency by Design | https://engineering.linkedin.com/blog/2019/fairness-privacy-transparency-by-design |

### Information Extracted

**Five Responsible AI Principles (Observed, High Confidence):**
1. Advance Economic Opportunity — skills taxonomy promotes equal treatment.
2. Uphold Trust — proactive privacy, security, safety; rigorous assessments.
3. Promote Fairness and Inclusion — cross-functional Responsible AI team; fair model analyser; mitigation trainer.
4. Provide Transparency — empower customers with transparency and education.
5. Embrace Accountability — robust governance; cross-disciplinary assessments; human oversight.

**Governance (Observed, High Confidence):**
- Quarterly review of access rights to production environments.
- Continuous monitoring for abnormal activity.
- Independent annual SOC 2 audit.
- Penetration testing.
- Model testing: jailbreak, harmful content, hallucinations, stability, latency, output quality.
- Equal Treatment Testing: per-model audits on recurring basis.
- Compliance: GDPR, EU AI Act, applicable US law (NYC Local Law 144 — inferred, Medium Confidence).

**Data Handling (Observed, High Confidence):**
- Hiring Assistant learnings confined to user + specific role; does not feed into OpenAI models.
- No processing of sensitive personal data (name, age, gender identity, race, religion, sex, disability).
- User inputs prompting sensitive personal data are blocked.
- ATS data stored in LinkedIn-owned US data centres; programmatically segmented.
- Members control data for GenAI model training (opt-in/out).

**Explainability (Observed, High Confidence):**
- Hiring Assistant: qualification match/gap indicators; candidate summaries with evidence citations.
- AI-Assisted Search: identifies which qualifications found vs. missing per candidate.
- Published: Hiring Assistant Whitepaper, Data Flow Diagram, General and Compliance FAQs.

**Human Control (Observed, High Confidence):**
- Hiring Assistant does NOT make autonomous or automatic decisions.
- Human involvement remains central; mitigates excessive reliance on automation.
- No applicant stage movements automated unless customer explicitly enables automation settings.

### Ontology Concepts Discovered
- Accountability: SOC2Audit, PenetrationTesting, ModelTestingFramework, EqualTreatmentTesting
- Trust: DataConfidentiality, MemberDataControl, GDPRCompliance
- Fairness: SensitiveDataExclusion, BiasAuditCycle
- Explainability: QualificationMatchIndicator, EvidenceCitedSummary, CandidateDataFlowDiagram
- HI Characteristic: HumanCenteredDecisionMaking (non-autonomous)

### Scenarios Supported
- S4 (Representative Ranking / Fairness), S5 (Explainability), S6 (Accountability / Governance)

---

## SEARCH SESSION 4 — LinkedIn Engineering: Economic Graph, Skills Graph, Memory

### Objective
Understand knowledge sources used by LinkedIn's AI: the Economic Graph, Skills Graph, and HLTM memory system.

### Search Terms
- `LinkedIn Economic Graph skills ontology knowledge graph talent intelligence`
- `LinkedIn AI Hiring Assistant long term memory hierarchical semantic memory arxiv 2025`
- `LinkedIn Engineering Blog recruiter AI applicant evaluation skills matching job recommendation 2024`

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-023 | Engineering Blog: Extracting Skills from Content | https://engineering.linkedin.com/blog/2023/extracting-skills-from-content-to-fuel-the-linkedin-skills-graph |
| E-024 | LinkedIn Engineering: Building LinkedIn's Skills Graph | https://www.linkedin.com/blog/engineering/skills-graph/building-linkedin-s-skills-graph-to-power-a-skills-first-world |
| E-025 | LinkedIn Economic Graph: Workforce Insights | https://economicgraph.linkedin.com/workforce-data |
| E-026 | arXiv: Hierarchical Long-Term Semantic Memory (HLTM) | https://arxiv.org/abs/2604.26197 |
| E-027 | Engineering Blog: Learning Hiring Preferences — AI Behind LinkedIn Jobs | https://engineering.linkedin.com/blog/2019/02/learning-hiring-preferences--the-ai-behind-linkedin-jobs |
| E-028 | Engineering Blog: Quality Matches via Personalised AI | https://engineering.linkedin.com/blog/2020/quality-matches-via-personalized-ai |
| E-029 | Engineering Blog: Improving Job Matching with Machine-Learned Activity Features | https://engineering.linkedin.com/blog/2022/improving-job-matching-with-machine-learned-activity-features- |

### Information Extracted

**Economic Graph (Observed, High Confidence):**
- Digital map of the global economy.
- Contains: members, jobs, titles, skills, companies, locations, schools, relationships.
- Generates real-time supply/demand insights: number of members with a given skill (supply) vs. jobs requiring it (demand).
- Powers EON model fine-tuning.

**Skills Graph (Observed, High Confidence):**
- 36,000+ skills taxonomy.
- Machine learning combs data to suggest new skills and skill relationships.
- Feeds into LinkedIn Recruiter search and ranking.
- Supports skills-first economy vision.

**HLTM — Hierarchical Long-Term Semantic Memory (Observed, High Confidence):**
- Schema-aligned memory tree; multi-granularity representations.
- Massively parallel execution; lossless incremental ingestion.
- Low-latency retrieval; privacy constraints by aligning memory with business scopes (seat, project).
- Deployed in production in LinkedIn Hiring Assistant for 6+ months.
- Effect: 5–10 percentage-point reduction in negative feedback rate when using historical memory.
- Enables personalisation without re-specifying requirements already inferable from past behaviour.

**QA Model — Qualified Applicant (Observed, High Confidence):**
- Predicts probability of positive recruiter action conditional on member applying to job.
- Learns skills and experience patterns from recruiter engagement with past candidates.
- Online learning: real-time updates as recruiters interact.

### Ontology Concepts Discovered
- KnowledgeSource: EconomicGraph, SkillsGraph
- Capability: LongTermMemory (HLTM), SkillsTaxonomyMatching, SupplyDemandInsights
- ArtificialAgent: QualifiedApplicantModel, HTLMMemoryModule
- FeedbackMechanism: OnlineLearning, HLTM-based personalisation
- Evaluation Metric: NegativeFeedbackRate

### Scenarios Supported
- S1, S2, S7 (Long-term Learning and Personalisation)

---

## SEARCH SESSION 5 — LinkedIn Recruiter: Workflows, Pipeline, ATS Integration

### Objective
Map the end-to-end hiring workflow, pipeline stages, human roles, and ATS integration (RSC+).

### Search Terms
- `LinkedIn Recruiter InMail AI generated message personalization candidate outreach 2024`
- `LinkedIn Recruiter System Connect ATS integration recruiter workflow human AI collaboration`
- `LinkedIn Recruiter candidate pipeline stages workflow sourcing screening shortlisting offer`
- `LinkedIn Recruiter hiring manager collaboration feedback interview decision making roles`

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-030 | LinkedIn Help: AI-Assisted Messages in Recruiter | https://www.linkedin.com/help/recruiter/answer/a1445743 |
| E-031 | LinkedIn Help: AI-Assisted Messages FAQ | https://www.linkedin.com/help/recruiter/answer/a1480502 |
| E-032 | LinkedIn Talent Blog: 6 Best Practices for AI-Assisted Messages | https://www.linkedin.com/business/talent/blog/talent-acquisition/ai-assisted-messaging-recruiter |
| E-033 | LinkedIn Help: Recruiter System Connect (RSC) overview | https://www.linkedin.com/help/recruiter/answer/a414363 |
| E-034 | LinkedIn Help: ATS integrations in Recruiter | https://www.linkedin.com/help/recruiter/answer/a496957 |
| E-035 | LinkedIn Hire: ATS Integrations | https://business.linkedin.com/hire/hiring-integrations/ats-integrations |
| E-036 | LinkedIn Help: Pipeline stages | https://www.linkedin.com/help/recruiter/answer/a412213 |
| E-037 | LinkedIn Help: Automated pipeline stages | https://www.linkedin.com/help/recruiter/answer/a413316 |
| E-038 | LinkedIn Help: Prescreen candidates with Hiring Assistant | https://www.linkedin.com/help/recruiter/answer/a7488409 |
| E-039 | LinkedIn Help: Hiring Manager role in Recruiter | https://www.linkedin.com/help/recruiter/answer/a416532 |
| E-040 | LinkedIn Talent Solutions: Recruiter-Hiring Manager Relationships | https://business.linkedin.com/talent-solutions/resources/talent-strategy/recruiter-hiring-manager-relationships |

### Information Extracted

**Pipeline Stages (Observed, High Confidence):**
1. Uncontacted — manually added or applied candidates.
2. Contacted — candidates contacted via InMail or email.
3. Replied — candidates who responded to InMail.
4. Custom stages configurable by contract admin.
5. ATS-synced stages via RSC+.

**AI-Assisted Messages (Observed, High Confidence):**
- Drafted using: recruiter info (name, title, company), candidate info (title, company, open-to-work, mutual connections, past applicant), job info (title, skills, location, compensation).
- Recruiter edits draft before sending.
- Feedback: thumbs up / thumbs down on message draft.
- Result: 40% increase in InMail acceptance when messages are personalised; 55% higher acceptance with AI-assisted messages vs manual.
- Automated Follow-Ups: 39% increase in InMail accepts vs manual follow-up.

**RSC+ (Observed, High Confidence):**
- Pulls ATS data continuously: candidate name/email/status/notes, application records, resumes, interview feedback, job requisition metadata, access control lists.
- Hiring Assistant can then evaluate applicants from both LinkedIn and ATS in a Connected Projects view.
- No stage movements automated unless customer enables explicitly.
- Data stored in LinkedIn US data centres; programmatically segmented.
- Recruiters save up to 3.5 hours/week with RSC active.

**Hiring Manager Role (Observed, High Confidence):**
- Can receive profile shares from recruiter.
- Provides interview feedback.
- Makes final hiring decision (debrief and decision).
- Can collaborate via Microsoft Teams integration with Hiring Assistant updates.
- Teams integration: recruiter and hiring manager align on candidate feedback in real time.

### Ontology Concepts Discovered
- HumanAgent: HiringManager, RecruiterAdmin
- Task (Human): ReviewShortlist, ShareCandidateProfile, ConductInterview, ProvideFeedback, MakeHiringDecision, EditInMailDraft
- Task (AI): GenerateInMailDraft, AutomatedFollowUp, PrescreeningQA, ATSDataSync, PipelineStageUpdate
- Interaction: HiringAssistantHiringManagerTeams, RecruiterHiringManagerFeedbackLoop
- FeedbackMechanism: ThumbsUpDownOnMessageDraft

### Scenarios Supported
- S3 (Automated Prescreening), S8 (Hiring Manager Collaboration), S9 (ATS Integration)

---

## SEARCH SESSION 6 — Research Papers

### Objective
Gather peer-reviewed evidence for AI system design, fairness-aware ranking, and candidate evaluation.

### Search Terms
- `LinkedIn talent search recommendation system research paper ACM KDD RecSys 2022 2023 2024`
- `LinkedIn Recruiter AI diversity nudge representative search algorithmic fairness Geyik KDD 2019`
- `LinkedIn AI Hiring Assistant long term memory hierarchical semantic memory arxiv 2025`

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-041 | Geyik et al. (2019) — Fairness-Aware Ranking, KDD | https://dl.acm.org/doi/10.1145/3292500.3330691 |
| E-042 | Geyik et al. (2018) — Talent Search and Recommendation, SIGIR | https://dl.acm.org/doi/10.1145/3209978.3210205 |
| E-043 | arXiv: Towards Deep and Representation Learning for Talent Search | https://arxiv.org/pdf/1809.06473 |
| E-044 | arXiv: In-Session Personalization for Talent Search | https://arxiv.org/pdf/1809.06488 |
| E-045 | arXiv: Talent Search and Recommendation Systems at LinkedIn | https://arxiv.org/pdf/1809.06481 |
| E-046 | arXiv: HLTM for LinkedIn's Hiring Agent (Xu et al. 2026) | https://arxiv.org/abs/2604.26197 |
| E-047 | arXiv: Human, Algorithm, or Both? Gender Bias in Recruiting | https://arxiv.org/pdf/2603.06240 |

### Information Extracted

**Fairness-Aware Ranking (Geyik et al. KDD 2019, E-041):**
- Framework for quantifying and mitigating algorithmic bias in ranking.
- Proposes measures for bias w.r.t. protected attributes (gender, age).
- Algorithms for fairness-aware re-ranking to achieve desired distribution.
- Result: ~3x increase in queries with representative results; deployed to 100% of LinkedIn Recruiter users.

**Talent Search Architecture (E-042, E-043, E-045):**
- Multi-objective ranking: skill match, location match, candidate response likelihood.
- GBDT models; GLMix models for entity-level personalisation.
- Offline training pipeline; online learning from recruiter interactions.

**In-Session Personalization (E-044):**
- Real-time model adapting to recruiter's session-specific interactions.
- Signals: candidate views, contacts, archives within current session.

**HLTM (E-046):**
- Schema-aligned memory tree; multi-granularity; privacy-aligned to business scope.
- 5–10% reduction in negative feedback rate in production.

**Human + Algorithm Recruiting Study (E-047):**
- Combination of human and AI candidate recommendation provides fairer gender distribution than human-only recruiting.
- Deliberate evaluation (more recruiter engagement) leads to fairer outcomes.

### Ontology Concepts Discovered
- Evaluation Metric: RepresentativeRankingCoverage, GenderRepresentationRatio, NegativeFeedbackRate
- Capability: FairnessAwareRerankingWithProtectedAttributes, InSessionPersonalisation
- HI Characteristic: CollaborativeDecisionMaking (human+AI fairer than human-only)

### Scenarios Supported
- S4, S7

---

## SEARCH SESSION 7 — Hybrid Intelligence Framework

### Objective
Map LinkedIn Recruiter concepts to the Hybrid Intelligence CARE framework and ontological concepts.

### Search Terms
- `Hybrid Intelligence CARE principles Collaborative Adaptive Responsible Explainable AI definition`
- `Akata Verhagen Neerincx "hybrid intelligence" research agenda IEEE Computer 2020`
- `Hybrid Intelligence ontology human agent artificial agent task goal interaction SHACL`

### Sources Accepted

| Evidence ID | Source | URL |
|---|---|---|
| E-048 | Akata et al. (2020) — Research Agenda for Hybrid Intelligence, IEEE Computer | https://www.computer.org/csdl/magazine/co/2020/08/09153877/1lUB5gL2CnS |
| E-049 | van den Bosch & Bronkhorst (2018) — Human-Machine Teaming taxonomy | (cited in literature) |
| E-050 | arXiv: The future of human-AI collaboration taxonomy | https://arxiv.org/pdf/2105.03354 |
| E-051 | Hybrid Intelligence Centre — About | https://www.hybrid-intelligence-centre.nl/ |
| E-052 | ResearchGate: HI Augmenting Human Intellect | https://www.researchgate.net/publication/343373955 |

### Information Extracted

**CARE Framework (Akata et al. 2020, E-048):**
- Collaborative: AI cooperates in synergy with human actors; accounts for strengths/limitations of both.
- Adaptive: adapts to changing contexts, variable team structures, preferences, roles.
- Responsible: integrates ethical/legal considerations; transparency, accountability, privacy, fairness.
- Explainable: explanations for shared awareness, goals, and collaborative strategies.

**HI Definition:**
> "The ability to achieve complex goals by combining human and artificial intelligence, reaching superior results to those each could have accomplished separately, and continuously improve by learning from each other."

**Core HI Ontology Concepts:**
- HumanAgent, ArtificialAgent
- SharedGoal
- Task (Human, AI, Shared)
- Capability (Human, AI)
- Context
- Interaction / InteractionPoint
- FeedbackMechanism
- DecisionPoint
- EvaluationMetric
- HI Characteristics: Collaborative, Adaptive, Responsible, Explainable

### Ontology Concepts Discovered
- HybridIntelligenceSystem: LinkedIn Recruiter + Hiring Assistant
- SharedGoal: IdentifyAndEngageQualifiedCandidates

### Scenarios Supported
- All scenarios (framework applies globally)

---

---

## SEARCH SESSION 8 — HI Ontology Diagram Integration

### Objective
Align the ontology_mapping.md with the formal Hybrid Intelligence Ontology diagram (hi: and hint: namespaces) provided by the thesis supervisor. The diagram was not available during Sessions 1–7; it was supplied after initial package completion.

### Source
- HI Ontology diagram (image provided directly); shows formal class hierarchy and object properties for the hi: ontology and hint: thesaurus.

### Information Extracted

**Classes discovered in the HI Ontology (not fully used in initial mapping):**
- `hi:HITeam` — central class; replaces informal "HybridIntelligenceSystem"
- `hi:UseCase` — introduces an HITeam; corresponds to scenarios S1–S8
- `hi:TaskExecution` — separate from `hi:Task`; the actual running of a task; evaluated by `hi:Evaluation`
- `hi:Evaluation` + `hi:Experiment` — formal evaluation structure with null/alternative hypotheses and metric concepts
- `hint:Role` — separate from `hint:Agent`; roles linked via `hi:hasRoleConcept`
- `hint:Domain` — required by `hi:UseCase`; maps to TalentAcquisition
- `hint:Method` — execution method concept; linked via `hi:hasMethodConcept`
- `hint:Metric` — metric concept; linked via `hi:hasMetricConcept`
- `hint:Constraint` — linked from `hi:Context` via `hi:hasConstraintConcept`
- `hint:Phenomenon` — linked from `hi:Context` via `hi:hasPhenomenonConcept`
- `hint:InteractionIntentConcept` — linked via `hi:hasInteractionIntentConcept`
- `hint:InteractionModalityConcept` — linked via `hi:hasInteractionModalityConcept`

**Object properties discovered:**
- `hi:requiresTask` (task dependency), `hi:isAssignedToTask`, `hi:isEligibleForTask`, `hi:hasAgentInvolved`, `hi:towardsGoal`, `hi:realizedBy` / `hi:realizesTask`, `hi:evaluatedBy`, `hi:hasMethodConcept`, `hi:hasMetricConcept`, `hi:hasNullHypothesis`, `hi:hasAlternativeHypothesis`, `hi:hasExperiment`, `hi:introducesHITeam`, `hi:hasDomainConcept`, `hi:hasUseCaseConcept`, `hi:hasConstraintConcept`, `hi:hasPhenomenonConcept`, `hi:influenceOn`, `hi:performedBy`, `hi:hasInteractionIntentConcept`, `hi:hasInteractionModalityConcept`

### Actions Taken
- `ontology_mapping.md` completely revised to use formal hi: and hint: classes and properties throughout.
- 14 new concept categories added (see Section 14 of ontology_mapping.md).
- 8 UseCase instances mapped (one per scenario).
- 9 TaskExecution instances mapped with method concepts.
- 9 Evaluation + Experiment structures with null/alternative hypotheses and metric concepts.
- 15 Metric concepts formalised via hint:Metric.
- 11 Method concepts formalised via hint:Method.
- 9 Constraints and 7 Phenomena formalised under hi:Context.
- All interactions revised with intent and modality concepts.
- Task dependency graph (hi:requiresTask) added.
- Agent assignment vs eligibility distinction (hi:isAssignedToTask vs hi:isEligibleForTask) added.

### Ontology Concepts Newly Formalised
All concepts now explicitly use hi: or hint: namespace prefixes matching the formal ontology diagram.

### Scenarios Affected
All scenarios (S1–S8) impacted — UseCase instances added for each.

---

## SATURATION ASSESSMENT

After 7 search sessions, no significant new actors, tasks, goals, capabilities, contexts, interactions, evaluation metrics, or HI concepts were identified in the final searches. All categories from the RAS completeness checklist have been addressed or explicitly marked as gaps in `knowledge_gaps.md`.

**Research phase declared SATURATED.**

---

## Iterations Summary

| Session | Focus | New Concepts Found |
|---|---|---|
| 1 | Official product docs | Core agents, tasks, metrics, goals |
| 2 | Engineering architecture | Sub-agents, ranking models, fairness system |
| 3 | AI Transparency docs | Governance, accountability, data handling |
| 4 | Economic Graph, Memory | HLTM, Skills Graph, QA model |
| 5 | Workflow, ATS, Roles | Pipeline stages, hiring manager, RSC+, InMail |
| 6 | Research papers | Fairness metrics, in-session personalisation |
| 7 | HI Framework | CARE mapping, HI ontology concepts |
