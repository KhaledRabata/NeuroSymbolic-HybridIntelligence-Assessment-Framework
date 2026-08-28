# Ontology Mapping (Revised)
## Neuro-Symbolic AI — Hybrid Intelligence Knowledge Acquisition
### Target: LinkedIn Recruiter + Hiring Assistant
### Revision: Aligned to formal HI Ontology (hi: namespace) + HI Thesaurus (hint: namespace)

> **Important:** This document maps extracted LinkedIn Recruiter concepts to the **formal Hybrid Intelligence Ontology** as depicted in the HI Ontology diagram.
>
> The ontology uses two layers:
> - **`hi:` classes** (yellow in diagram) — the formal ontology instances (HITeam, Agent, Task, etc.)
> - **`hint:` classes** (purple in diagram) — the Hybrid Intelligence Thesaurus; controlled vocabulary linked via `hi:hasXxxConcept` properties
>
> This document does NOT produce RDF triples, OWL axioms, SHACL shapes, or ontology instances.
> Only conceptual mappings are documented.
>
> All mappings labelled **Observed** (explicitly documented) or **Inferred** (reasonably derived).
> Confidence: High / Medium / Low. Evidence IDs trace to `sources.md`.

---

## Namespace Prefixes (Reference)

| Prefix | Meaning |
|---|---|
| `hi:` | Hybrid Intelligence Ontology classes and object properties |
| `hint:` | Hybrid Intelligence Thesaurus (controlled vocabulary concepts) |
| `xsd:` | XML Schema Datatypes |
| `rdfs:` | RDF Schema (used for subClassOf relationships shown as dashed lines) |

---

## Structural Overview of the HI Ontology (from diagram)

The diagram shows the following key classes and relationships:

**Central class:** `hi:HITeam`
- `hi:HITeam` `hi:hasMember` → `hi:Agent`
- `hi:HITeam` `hi:hasGoal` → `hi:Goal`
- `hi:HITeam` `hi:operatesInContext` → `hi:Context`

**Agent hierarchy:**
- `hi:HumanAgent` rdfs:subClassOf `hi:Agent`
- `hi:ArtificialAgent` rdfs:subClassOf `hi:Agent`
- `hi:Agent` `hi:hasAgentConcept` → `hint:Agent`
- `hi:Agent` `hi:hasRoleConcept` → `hint:Role`
- `hi:Agent` `hi:hasCapability` → `hi:Capability`
- `hi:Agent` `hi:isAssignedToTask` → `hi:Task`
- `hi:Agent` `hi:isEligibleForTask` → `hi:Task`
- `hi:Agent` `hi:hasAgentInvolved` → `hi:Agent`

**Task and Capability:**
- `hi:Task` `hi:requiresCapability` → `hi:Capability`
- `hi:Capability` `hi:allowsTask` → `hi:Task`
- `hi:Task` `hi:towardsGoal` → `hi:Goal`
- `hi:Task` `hi:realizedBy` → `hi:TaskExecution`
- `hi:Task` `hi:requiresTask` → `hi:Task` (dependency)
- `hi:Task` `hi:hasTaskConcept` → `hint:Task`
- `hi:Capability` `hi:hasCapabilityConcept` → `hint:Capability`
- `hi:Goal` `hi:hasGoalConcept` → `hint:Goal`

**Execution and Evaluation:**
- `hi:TaskExecution` `hi:realizesTask` → `hi:Task`
- `hi:TaskExecution` `hi:evaluatedBy` → `hi:Evaluation`
- `hi:TaskExecution` `hi:hasMethodConcept` → `hint:Method`
- `hi:Evaluation` `hi:hasExperiment` → `hi:Experiment`
- `hi:Experiment` `hi:hasNullHypothesis` → xsd:string
- `hi:Experiment` `hi:hasAlternativeHypothesis` → xsd:string
- `hi:Experiment` `hi:hasMetricConcept` → `hint:Metric`

**Interaction:**
- `hi:Interaction` `hi:hasInteractionEpisode` → (episode)
- `hi:Interaction` `hi:performedBy` → `hi:Agent`
- `hi:Interaction` `hi:hasInteractionIntentConcept` → `hint:InteractionIntentConcept`
- `hi:Interaction` `hi:hasInteractionModalityConcept` → `hint:InteractionModalityConcept`

**Context:**
- `hi:Context` `hi:hasContextConcept` → `hint:Context`
- `hi:Context` `hi:hasConstraintConcept` → `hint:Constraint`
- `hi:Context` `hi:hasPhenomenonConcept` → `hint:Phenomenon`
- `hi:Context` `hi:influenceOn` → (HITeam / TaskExecution)

**Use Case:**
- `hi:UseCase` `hi:introducesHITeam` → `hi:HITeam`
- `hi:UseCase` `hi:hasUseCaseConcept` → `hint:UseCase`
- `hi:UseCase` `hi:hasDomainConcept` → `hint:Domain`

---

## 1. hi:HITeam

The `hi:HITeam` is the central organising class — the collaborative team of human and artificial agents working toward shared goals in context.

| LinkedIn Recruiter Concept | hi: Class | Confidence | Observed/Inferred | Evidence IDs | Notes |
|---|---|---|---|---|---|
| LinkedIn Recruiter + Hiring Assistant (per hiring project) | `hi:HITeam` | High | Observed | E-001, E-002, E-019 | The team constituted by a recruiter + Hiring Assistant sub-agents + hiring manager; collaborating toward shared hiring goals in the context of a specific role |

**Mapping notes:**
- Each `hi:HITeam` instance corresponds to a specific hiring project (one team per active role).
- The team is constituted dynamically: recruiter + Hiring Assistant agents + optionally hiring manager.
- The `hi:HITeam` has members (`hi:hasMember`), goals (`hi:hasGoal`), and operates in context (`hi:operatesInContext`).

---

## 2. hi:UseCase

Each Hybrid Intelligence scenario maps to a `hi:UseCase`. The UseCase `hi:introducesHITeam` (the specific team configuration) and links to a domain.

| Scenario | hi:UseCase Instance | hint:UseCase Concept | hint:Domain | Confidence | Evidence IDs |
|---|---|---|---|---|---|
| S1 — AI-Assisted Candidate Sourcing | UseCase_CandidateSourcing | CandidateSourcing | TalentAcquisition | High | E-001, E-002, E-005, E-007 |
| S2 — AI-Driven Candidate Evaluation | UseCase_CandidateEvaluation | CandidateEvaluation | TalentAcquisition | High | E-002, E-005, E-013, E-020 |
| S3 — Automated Prescreening via InMail | UseCase_AutomatedPrescreening | CandidatePrescreening | TalentAcquisition | High | E-001, E-005, E-030, E-038 |
| S4 — Fairness-Aware Representative Ranking | UseCase_FairnessAwareRanking | FairnessAwareRanking | TalentAcquisition / ResponsibleAI | High | E-009, E-010, E-041 |
| S5 — Explainable AI-Assisted Search | UseCase_ExplainableSearch | ExplainableSearch | TalentAcquisition | High | E-006, E-011, E-020 |
| S6 — Recruiter–Hiring Manager Collaboration | UseCase_HiringManagerCollaboration | HiringManagerCollaboration | TalentAcquisition | High | E-039, E-040 |
| S7 — Long-Term Personalisation via HLTM | UseCase_LongTermPersonalisation | LongTermPersonalisation | TalentAcquisition / AdaptiveAI | High | E-046 |
| S8 — ATS Integration (RSC+) | UseCase_ATSIntegration | ATSIntegration | TalentAcquisition / EnterpriseIntegration | High | E-020, E-033, E-035 |

**hint:Domain:** `TalentAcquisition` is the overarching domain. Sub-domains include `ResponsibleAI` (S4), `AdaptiveAI` (S7), `EnterpriseIntegration` (S8).

---

## 3. hi:Agent → hi:HumanAgent

`hi:HumanAgent` rdfs:subClassOf `hi:Agent`. Each human agent links to a `hint:Agent` concept (controlled vocabulary) and a `hint:Role` concept.

| LinkedIn Recruiter Concept | hi: Class | hint:Agent Concept | hint:Role Concept | Confidence | Observed/Inferred | Evidence IDs |
|---|---|---|---|---|---|---|
| Recruiter | `hi:HumanAgent` | RecruiterAgent | RecruiterRole | High | Observed | E-001, E-002, E-007, E-039 |
| Hiring Manager | `hi:HumanAgent` | HiringManagerAgent | HiringManagerRole | High | Observed | E-039, E-040 |
| Candidate | `hi:HumanAgent` | CandidateAgent | CandidateRole | High | Observed | E-030, E-031, E-038 |
| Recruiter Admin | `hi:HumanAgent` | RecruiterAdminAgent | AdminRole | High | Observed | E-033, E-036, E-037 |
| LinkedIn Responsible AI Team Member | `hi:HumanAgent` | ResponsibleAITeamMemberAgent | ResponsibleAIGovernanceRole | High | Observed | E-009, E-019, E-021 |

**hi:hasMember** (from `hi:HITeam`):
- Recruiter: core member of every `hi:HITeam` instance.
- Hiring Manager: member of the HITeam in S6.
- LinkedIn Responsible AI Team: members of the governance team; involved in S4 use case.
- Candidate: passive member — receives outputs from the HITeam but does not configure or direct the system.

**hi:isAssignedToTask vs hi:isEligibleForTask:**

| Agent | Assigned Tasks | Eligible (but not exclusively assigned) Tasks |
|---|---|---|
| Recruiter | DefineQualifications, ReviewShortlist, AdvanceOrArchiveCandidates, MakeHiringDecision, EnableRSC+ | EditInMailDraft, DefinePrescreeningQuestions, ShareCandidateProfiles |
| Hiring Manager | ConductInterview, ProvideInterviewFeedback, MakeFinalHiringDecision | ReviewAICandidateSummaries |
| Candidate | RespondToPrescreeningQuestions | — |
| Recruiter Admin | EnableRSC+, ConfigureCustomPipelineStages | ManageAccessControl |
| Responsible AI Team | ReviewLiFTAuditResults, ApproveMitigationActions, DefineFairnessCriteria | — |

---

## 4. hi:Agent → hi:ArtificialAgent

`hi:ArtificialAgent` rdfs:subClassOf `hi:Agent`. Each AI agent links to a `hint:Agent` concept.

| LinkedIn Recruiter Concept | hi: Class | hint:Agent Concept | Confidence | Observed/Inferred | Evidence IDs |
|---|---|---|---|---|---|
| Hiring Assistant (top-level agentic system) | `hi:ArtificialAgent` | HiringAssistantAgent | High | Observed | E-001, E-002, E-005 |
| Supervisor Agent (orchestrator) | `hi:ArtificialAgent` | SupervisorAgent | High | Observed | E-012, E-013, E-014 |
| Intake Agent (sub-agent) | `hi:ArtificialAgent` | IntakeAgent | High | Observed | E-012, E-013 |
| Sourcing Agent (sub-agent) | `hi:ArtificialAgent` | SourcingAgent | High | Observed | E-012, E-013 |
| Evaluation Agent (sub-agent) | `hi:ArtificialAgent` | EvaluationAgent | High | Observed | E-012, E-013, E-015 |
| Outreach/Screening Agent (sub-agent) | `hi:ArtificialAgent` | OutreachScreeningAgent | High | Observed | E-012, E-013 |
| EON Model | `hi:ArtificialAgent` | EONModelAgent | High | Observed | E-013, E-014, E-015 |
| GPT-4o (Azure OpenAI) | `hi:ArtificialAgent` | GPT4oAgent | High | Observed | E-013, E-014 |
| Ranking Model (GBDT) | `hi:ArtificialAgent` | GBDTRankingModelAgent | High | Observed | E-008, E-042, E-045 |
| GLMix Personalisation Model | `hi:ArtificialAgent` | GLMixModelAgent | High | Observed | E-008, E-045 |
| Qualified Applicant (QA) Model | `hi:ArtificialAgent` | QualifiedApplicantModelAgent | High | Observed | E-027, E-028 |
| Representative Ranking System | `hi:ArtificialAgent` | RepresentativeRankingAgent | High | Observed | E-010, E-041 |
| LinkedIn Fairness Toolkit (LiFT) | `hi:ArtificialAgent` | LiFTFairnessAgent | High | Observed | E-017, E-018 |
| Fair Model Analyser | `hi:ArtificialAgent` | FairModelAnalyserAgent | High | Observed | E-019 |
| Mitigation Trainer | `hi:ArtificialAgent` | MitigationTrainerAgent | High | Observed | E-019 |
| HLTM (Hierarchical Long-Term Semantic Memory) | `hi:ArtificialAgent` | HLTMMemoryAgent | High | Observed | E-046 |
| AI-Assisted Messages Module | `hi:ArtificialAgent` | AIAssistedMessagesAgent | High | Observed | E-030, E-031, E-032 |
| Automated Follow-Up System | `hi:ArtificialAgent` | AutomatedFollowUpAgent | High | Observed | E-032 |
| Advanced AI-Assisted Search | `hi:ArtificialAgent` | AIAssistedSearchAgent | High | Observed | E-006, E-020 |
| Galene Search Engine | `hi:ArtificialAgent` | GaleneSearchAgent | High | Observed | E-008, E-042 |
| RSC+ Integration Module | `hi:ArtificialAgent` | RSCPlusIntegrationAgent | High | Observed | E-020, E-033 |
| In-Session Personalisation Module | `hi:ArtificialAgent` | InSessionPersonalisationAgent | High | Observed | E-044 |

**hi:isAssignedToTask (AI agents):**

| AI Agent | Assigned Tasks |
|---|---|
| Supervisor Agent | OrchestrateWorkflow, RouteToSubAgent |
| Intake Agent | ParseNLQualifications, StructureHiringIntent |
| Sourcing Agent | ExecuteCandidateSearch, GenerateSearchQueries |
| Evaluation Agent | EvaluateCandidatesAgainstQualifications, GenerateEvidenceCitedSummaries |
| Outreach/Screening Agent | GenerateInMailDraft, SendPrescreeningQuestions, ProcessCandidateResponses, AnswerRoleQuestions |
| EON Model | LargeScaleCandidateEvaluation |
| GPT-4o | ComplexQualificationReasoning, NaturalLanguageSummaryGeneration |
| GBDT Ranking Model | MultiPassCandidateRanking |
| GLMix Model | EntityLevelPersonalisedRanking |
| QA Model | PredictRecruiterActionLikelihood |
| Representative Ranking System | FairnessAwareReranking |
| LiFT | MeasureBiasInTrainingData, MeasureBiasInModelOutputs |
| Fair Model Analyser | PerModelBiasAudit |
| Mitigation Trainer | RetrainOrDerampBiasedModel |
| HLTM | StoreRecruiterPreferences, RetrieveHistoricalPreferences |
| AI-Assisted Messages | GeneratePersonalisedInMailDraft |
| Automated Follow-Up | SendAutomatedFollowUpInMail |
| AI-Assisted Search | ParseNLQuery, GenerateSearchFilters, ReturnExplainedResults |
| Galene | ExecuteDistributedCandidateSearch |
| RSC+ | PullATSDataContinuously, UnifyApplicantView |
| In-Session Personalisation | AdaptRankingWithinSession |

**hi:hasAgentInvolved** (agent-to-agent relationships within tasks):
- Supervisor Agent `hi:hasAgentInvolved` → Intake Agent, Sourcing Agent, Evaluation Agent, Outreach Agent (orchestration)
- Recruiter `hi:hasAgentInvolved` → Hiring Assistant (primary collaboration)
- Hiring Manager `hi:hasAgentInvolved` → Recruiter (review and decision collaboration)

---

## 5. hi:Goal

Goals belong to the `hi:HITeam` via `hi:hasGoal`. Each goal links to a `hint:Goal` concept.

| LinkedIn Recruiter Concept | hi: Class | hint:Goal Concept | Confidence | Observed/Inferred | Evidence IDs |
|---|---|---|---|---|---|
| Identify and engage qualified candidates efficiently | `hi:Goal` | IdentifyQualifiedCandidates | High | Observed | E-001, E-002, E-005 |
| Reduce recruiter time on high-volume repetitive tasks | `hi:Goal` | ReduceRecruiterBurden | High | Observed | E-001, E-002, E-007 |
| Ensure equal economic opportunity for all qualified candidates | `hi:Goal` | EnsureEqualOpportunity | High | Observed | E-010, E-019, E-041 |
| Make informed, aligned, accountable hiring decisions | `hi:Goal` | MakeAccountableHiringDecisions | High | Observed | E-019, E-020, E-039 |
| Personalise AI recommendations based on recruiter history | `hi:Goal` | PersonaliseAIRecommendations | High | Observed | E-046 |
| Mitigate model bias and maintain fairness across protected attributes | `hi:Goal` | MitigateBiasAndMaintainFairness | High | Observed | E-009, E-041 |

**hi:towardsGoal** (Tasks that serve each Goal — see Section 6):
- All sourcing and evaluation tasks → IdentifyQualifiedCandidates
- Prescreening, InMail automation tasks → ReduceRecruiterBurden
- Representative ranking, LiFT audit tasks → EnsureEqualOpportunity + MitigateBiasAndMaintainFairness
- Hiring manager collaboration, final decision tasks → MakeAccountableHiringDecisions
- HLTM query/update tasks → PersonaliseAIRecommendations

---

## 6. hi:Task

Each task maps to `hi:Task`, links to a `hint:Task` concept, and connects to goals (`hi:towardsGoal`), capabilities (`hi:requiresCapability`), and task executions (`hi:realizedBy`). Task dependencies are captured via `hi:requiresTask`.

### 6.1 Human Tasks

| LinkedIn Recruiter Concept | hi: Class | hint:Task Concept | hi:towardsGoal | hi:requiresTask (depends on) | Confidence | Evidence IDs |
|---|---|---|---|---|---|---|
| Define hiring qualifications | `hi:Task` | DefineHiringQualifications | IdentifyQualifiedCandidates | — | High | E-001, E-002, E-020 |
| Guide Hiring Assistant with context | `hi:Task` | GuideHiringAssistant | IdentifyQualifiedCandidates | DefineHiringQualifications | High | E-002, E-020 |
| Review AI-generated candidate shortlist | `hi:Task` | ReviewCandidateShortlist | IdentifyQualifiedCandidates / MakeAccountableHiringDecisions | DefineHiringQualifications | High | E-002, E-005, E-020 |
| Advance or archive candidates | `hi:Task` | AdvanceOrArchiveCandidates | IdentifyQualifiedCandidates | ReviewCandidateShortlist | High | E-020, E-036 |
| Edit AI-generated InMail draft | `hi:Task` | EditInMailDraft | ReduceRecruiterBurden | GeneratePersonalisedInMailDraft (AI task) | High | E-030, E-031 |
| Define prescreening questions | `hi:Task` | DefinePrescreeningQuestions | ReduceRecruiterBurden | AdvanceOrArchiveCandidates | High | E-038, E-020 |
| Review aggregated prescreening results | `hi:Task` | ReviewPrescreeningResults | ReduceRecruiterBurden / MakeAccountableHiringDecisions | SendPrescreeningQuestions (AI task) | High | E-038 |
| Share candidate profiles with hiring manager | `hi:Task` | ShareCandidateProfiles | MakeAccountableHiringDecisions | ReviewCandidateShortlist | High | E-039, E-040 |
| Conduct interview | `hi:Task` | ConductInterview | MakeAccountableHiringDecisions | ShareCandidateProfiles | High | E-039, E-040 |
| Provide structured interview feedback | `hi:Task` | ProvideInterviewFeedback | MakeAccountableHiringDecisions | ConductInterview | High | E-039, E-040 |
| Make final hiring decision | `hi:Task` | MakeFinalHiringDecision | MakeAccountableHiringDecisions | ProvideInterviewFeedback | High | E-019, E-020, E-039 |
| Provide thumbs up/down on InMail draft | `hi:Task` | ProvideMessageFeedback | PersonaliseAIRecommendations | EditInMailDraft | High | E-030, E-031 |
| Enable RSC+ | `hi:Task` | EnableRSCPlus | IdentifyQualifiedCandidates | — | High | E-020, E-033 |
| Link project to ATS requisition | `hi:Task` | LinkProjectToATSRequisition | IdentifyQualifiedCandidates | EnableRSCPlus | High | E-020, E-033 |
| Review LiFT audit results and approve model changes | `hi:Task` | ReviewAndApproveFairnessActions | MitigateBiasAndMaintainFairness / EnsureEqualOpportunity | MeasureBiasInModelOutputs (AI task) | High | E-009, E-019 |
| Define fairness criteria | `hi:Task` | DefineFairnessCriteria | EnsureEqualOpportunity | — | High | E-009, E-019, E-041 |

### 6.2 AI Tasks

| LinkedIn Recruiter Concept | hi: Class | hint:Task Concept | hi:towardsGoal | hi:requiresTask (depends on) | Confidence | Evidence IDs |
|---|---|---|---|---|---|---|
| Parse NL qualifications into structured search query | `hi:Task` | ParseNLQualifications | IdentifyQualifiedCandidates | DefineHiringQualifications (human) | High | E-006, E-012, E-020 |
| Generate multiple search queries | `hi:Task` | GenerateSearchQueries | IdentifyQualifiedCandidates | ParseNLQualifications | High | E-020 |
| Retrieve candidates from Galene index | `hi:Task` | RetrieveCandidates | IdentifyQualifiedCandidates | GenerateSearchQueries | High | E-008, E-042 |
| Apply multi-pass ML ranking (GBDT/GLMix) | `hi:Task` | ApplyMLRanking | IdentifyQualifiedCandidates | RetrieveCandidates | High | E-008, E-045 |
| Apply fairness-aware re-ranking | `hi:Task` | ApplyFairnessReranking | EnsureEqualOpportunity | ApplyMLRanking | High | E-010, E-041 |
| Evaluate candidates against qualifications | `hi:Task` | EvaluateCandidateQualifications | IdentifyQualifiedCandidates | RetrieveCandidates | High | E-013, E-020 |
| Generate evidence-cited candidate summaries | `hi:Task` | GenerateEvidenceCitedSummaries | MakeAccountableHiringDecisions | EvaluateCandidateQualifications | High | E-012, E-013, E-020 |
| Surface qualification match/gap indicators | `hi:Task` | SurfaceQualificationMatchGap | MakeAccountableHiringDecisions | EvaluateCandidateQualifications | High | E-020, E-006 |
| Generate personalised InMail draft | `hi:Task` | GeneratePersonalisedInMailDraft | ReduceRecruiterBurden | AdvanceOrArchiveCandidates (human) | High | E-030, E-031 |
| Send prescreening questions via InMail | `hi:Task` | SendPrescreeningQuestions | ReduceRecruiterBurden | CandidateRepliesInitialInMail | High | E-038 |
| Process candidate prescreening responses | `hi:Task` | ProcessCandidateResponses | ReduceRecruiterBurden | SendPrescreeningQuestions | High | E-038, E-013 |
| Answer candidate role questions via InMail | `hi:Task` | AnswerCandidateRoleQuestions | ReduceRecruiterBurden | SendPrescreeningQuestions | High | E-001, E-005 |
| Send automated follow-up InMails | `hi:Task` | SendAutomatedFollowUpInMail | ReduceRecruiterBurden | GeneratePersonalisedInMailDraft | High | E-032 |
| Pull ATS data via RSC+ | `hi:Task` | PullATSData | IdentifyQualifiedCandidates | EnableRSCPlus (human) | High | E-020, E-033 |
| Generate Economic Graph sourcing insights | `hi:Task` | GenerateEconomicGraphInsights | IdentifyQualifiedCandidates | ParseNLQualifications | High | E-025, E-013 |
| Measure bias in training data and model outputs (LiFT) | `hi:Task` | MeasureBiasInModelOutputs | MitigateBiasAndMaintainFairness | — | High | E-017, E-018 |
| Retrain or deramp biased model | `hi:Task` | RetrainOrDerampBiasedModel | MitigateBiasAndMaintainFairness | ReviewAndApproveFairnessActions (human) | High | E-019 |
| Query HLTM for historical preferences | `hi:Task` | QueryHLTMForPreferences | PersonaliseAIRecommendations | — | High | E-046 |
| Update HLTM with session outcomes | `hi:Task` | UpdateHLTMWithSessionOutcomes | PersonaliseAIRecommendations | GenerateEvidenceCitedSummaries | High | E-046 |
| Apply in-session personalisation | `hi:Task` | ApplyInSessionPersonalisation | PersonaliseAIRecommendations | RetrieveCandidates | High | E-044 |
| Orchestrate sub-agent workflow (Supervisor) | `hi:Task` | OrchestrateSubAgentWorkflow | IdentifyQualifiedCandidates | DefineHiringQualifications (human) | High | E-012, E-013, E-014 |

---

## 7. hi:Capability

Each capability maps to `hi:Capability` and links to a `hint:Capability` concept. Capabilities `hi:allowsTask` → the tasks they enable.

| LinkedIn Recruiter Concept | hi: Class | hint:Capability Concept | hi:allowsTask (enables) | Confidence | Evidence IDs |
|---|---|---|---|---|---|
| Natural language query parsing | `hi:Capability` | NLQueryParsing | ParseNLQualifications | High | E-006, E-020 |
| Multi-filter structured candidate search | `hi:Capability` | MultiFilterCandidateSearch | RetrieveCandidates | High | E-002, E-006 |
| Multi-pass ML ranking (GBDT + GLMix) | `hi:Capability` | MultiPassMLRanking | ApplyMLRanking | High | E-008, E-045 |
| Fairness-aware re-ranking | `hi:Capability` | FairnessAwareReranking | ApplyFairnessReranking | High | E-041, E-010 |
| Large-scale candidate evaluation (EON) | `hi:Capability` | LargeScaleCandidateEvaluation | EvaluateCandidateQualifications | High | E-013, E-014 |
| Evidence-cited NL summary generation | `hi:Capability` | EvidenceCitedSummaryGeneration | GenerateEvidenceCitedSummaries | High | E-012, E-013, E-020 |
| AI-generated personalised InMail drafting | `hi:Capability` | PersonalisedInMailDrafting | GeneratePersonalisedInMailDraft | High | E-030, E-031 |
| Automated prescreening Q&A | `hi:Capability` | AutomatedPrescreeningQA | SendPrescreeningQuestions, ProcessCandidateResponses | High | E-038 |
| Automated follow-up generation | `hi:Capability` | AutomatedFollowUpGeneration | SendAutomatedFollowUpInMail | High | E-032 |
| ATS data ingestion (RSC+) | `hi:Capability` | ATSDataIngestion | PullATSData | High | E-020, E-033 |
| Resume parsing for ATS applicants | `hi:Capability` | ResumeParsing | EvaluateCandidateQualifications | High | Inferred | E-020 |
| Economic Graph insight generation | `hi:Capability` | EconomicGraphInsightGeneration | GenerateEconomicGraphInsights | High | E-025, E-013 |
| Skills taxonomy matching | `hi:Capability` | SkillsTaxonomyMatching | ParseNLQualifications, EvaluateCandidateQualifications | High | E-023, E-024 |
| HLTM hierarchical memory retrieval | `hi:Capability` | HierarchicalMemoryRetrieval | QueryHLTMForPreferences | High | E-046 |
| In-session personalisation | `hi:Capability` | InSessionPersonalisation | ApplyInSessionPersonalisation | High | E-044 |
| Bias measurement across subgroups (LiFT) | `hi:Capability` | BiasSubgroupMeasurement | MeasureBiasInModelOutputs | High | E-017, E-018 |
| Per-model recurring bias auditing | `hi:Capability` | PerModelBiasAuditing | MeasureBiasInModelOutputs | High | E-019 |
| Speculative decoding for latency optimisation | `hi:Capability` | SpeculativeDecoding | LargeScaleCandidateEvaluation | High | E-014 |
| Qualification match/gap indicator computation | `hi:Capability` | QualificationMatchGapComputation | SurfaceQualificationMatchGap | High | E-020, E-006 |
| XAI search refinement suggestion | `hi:Capability` | XAISearchRefinementSuggestion | ParseNLQualifications | High | E-011 |
| Multi-agent orchestration (LangChain/LangGraph) | `hi:Capability` | MultiAgentOrchestration | OrchestrateSubAgentWorkflow | High | E-012, E-014 |
| Skill and title expansion (query augmentation) | `hi:Capability` | SkillAndTitleExpansion | GenerateSearchQueries | High | E-006, E-023 |
| Candidate pipeline stage tracking | `hi:Capability` | PipelineStageTracking | AdvanceOrArchiveCandidates | High | E-036, E-037 |

---

## 8. hi:Interaction

Each meaningful interaction maps to `hi:Interaction`. Interactions link to `hint:InteractionIntentConcept` (why) and `hint:InteractionModalityConcept` (how). They are `hi:performedBy` one or more `hi:Agent` instances.

| LinkedIn Recruiter Concept | hi: Class | hint:InteractionIntentConcept | hint:InteractionModalityConcept | hi:performedBy | Confidence | Evidence IDs |
|---|---|---|---|---|---|---|
| Recruiter specifies qualifications to Hiring Assistant | `hi:Interaction` | SpecifyHiringIntent | NaturalLanguageTextInput (UI chat) | Recruiter → HiringAssistant | High | E-001, E-002, E-020 |
| Hiring Assistant delivers ranked shortlist to recruiter | `hi:Interaction` | DeliverCandidateShortlist | UIDisplay (ranked list with match/gap) | HiringAssistant → Recruiter | High | E-002, E-020 |
| Hiring Assistant sends personalised InMail to candidate | `hi:Interaction` | OutreachForEngagement | InMailMessage | OutreachAgent → Candidate | High | E-030, E-031 |
| Candidate responds to InMail (initial) | `hi:Interaction` | ExpressInterest | InMailMessage | Candidate → OutreachAgent | High | E-038 |
| Hiring Assistant sends prescreening questions to candidate | `hi:Interaction` | CollectQualificationConfirmation | InMailMessage | OutreachAgent → Candidate | High | E-038 |
| Candidate responds to prescreening questions | `hi:Interaction` | ProvideQualificationInformation | InMailMessage | Candidate → OutreachAgent | High | E-038 |
| Hiring Assistant answers candidate role questions | `hi:Interaction` | AnswerRoleQuery | InMailMessage | OutreachAgent → Candidate | High | E-001, E-005 |
| Recruiter advances/archives candidate (implicit feedback) | `hi:Interaction` | ProvideFeedbackOnCandidate | UIAction (button click) | Recruiter → HiringAssistant (implicit) | High | E-008, E-027 |
| Recruiter provides thumbs up/down on InMail | `hi:Interaction` | ProvideExplicitMessageFeedback | UIFeedbackAction (thumbs up/down) | Recruiter → AIAssistedMessages | High | E-030, E-031 |
| Recruiter shares candidate profile with hiring manager | `hi:Interaction` | SolicitHiringManagerReview | ProfileShare (Recruiter platform) | Recruiter → HiringManager | High | E-039, E-040 |
| Recruiter and hiring manager align via Microsoft Teams | `hi:Interaction` | AlignOnCandidateFeedback | MicrosoftTeamsMessage | Recruiter ↔ HiringManager | High | E-002, E-005 |
| RSC+ pulls data from ATS | `hi:Interaction` | SyncApplicantData | APICall (RSC+ API) | RSCPlusAgent → ATS | High | E-020, E-033 |
| LiFT delivers bias report to Responsible AI Team | `hi:Interaction` | ReportBiasFindings | InternalReportDelivery | LiFTAgent → ResponsibleAITeam | High | E-009, E-017, E-018 |
| Supervisor Agent routes task to sub-agent | `hi:Interaction` | DelegateSubTask | InternalMessageBroker (LangGraph) | SupervisorAgent → SubAgent | High | E-012, E-013, E-014 |
| Hiring Assistant surfaces Economic Graph insights to recruiter | `hi:Interaction` | InformSourcingStrategy | UIDisplay (insights panel) | HiringAssistant → Recruiter | High | E-025, E-013 |

---

## 9. hi:Context

The `hi:HITeam` `hi:operatesInContext` → `hi:Context`. Each context links to a `hint:Context` concept, `hint:Constraint` (limiting conditions), and `hint:Phenomenon` (observable patterns or conditions in the environment).

### 9.1 Context Instances

| LinkedIn Recruiter Concept | hi: Class | hint:Context Concept | Confidence | Evidence IDs |
|---|---|---|---|---|
| Corporate in-house recruiting environment | `hi:Context` | CorporateRecruiting | High | E-002, E-007 |
| Staffing agency recruiting environment | `hi:Context` | StaffingAgencyRecruiting | High | E-002 |
| High-volume hiring context | `hi:Context` | HighVolumeHiring | High | E-001, E-007 |
| Diversity hiring initiative context | `hi:Context` | DiversityHiringInitiative | High | E-010, E-041 |
| Global English-language hiring | `hi:Context` | GlobalEnglishHiring | High | E-001, E-005 |
| ATS-connected recruiting environment | `hi:Context` | ATSConnectedRecruiting | High | E-033, E-034, E-035 |
| Repeat-role hiring with HLTM history | `hi:Context` | RepeatRoleHiringWithHistory | High | E-046 |

### 9.2 hint:Constraint (Limiting Conditions)

| Constraint | hint:Constraint Concept | Affects | Confidence | Evidence IDs |
|---|---|---|---|---|
| Hiring Assistant does not make autonomous decisions — human must decide | HumanControlConstraint | All tasks involving hiring decisions | High | E-019, E-020 |
| Sensitive personal data (gender, race, age, etc.) may not be processed in evaluation | SensitiveDataExclusionConstraint | EvaluateCandidateQualifications | High | E-020 |
| ATS data only accessible with explicit customer consent | CustomerConsentConstraint | PullATSData | High | E-020 |
| Automated ATS stage movements require explicit customer opt-in | AutomationOptInConstraint | PipelineStageTracking | High | E-020 |
| HLTM data scoped to seat/project level (no cross-customer contamination) | HLTMPrivacyScopeConstraint | QueryHLTMForPreferences, UpdateHLTMWithSessionOutcomes | High | E-046 |
| Hiring Assistant learnings confined to user + specific role; do not feed into OpenAI models | ModelLearningBoundaryConstraint | UpdateHLTMWithSessionOutcomes | High | E-020 |
| Language availability: English globally; German + French rolling out 2026 | LanguageAvailabilityConstraint | All NL interaction tasks | High | E-001, E-005 |
| User inputs prompting sensitive personal data are blocked | SensitiveInputBlockConstraint | ParseNLQualifications, EvaluateCandidateQualifications | High | E-020 |
| GDPR compliance applies to all member data processing | GDPRConstraint | All data processing tasks | High | E-019 |

### 9.3 hint:Phenomenon (Observable Conditions in the Environment)

| Phenomenon | hint:Phenomenon Concept | Relevance | Confidence | Evidence IDs |
|---|---|---|---|---|
| Historical bias in training data favouring certain demographics | HistoricalBiasInTrainingData | Motivation for LiFT and Representative Ranking | High | E-009, E-041 |
| High volume of profiles relative to available recruiter time | ProfileReviewBurden | Core motivation for Hiring Assistant automation | High | E-001, E-002 |
| Skills taxonomy gaps (new skills not yet in Skills Graph) | SkillsTaxonomyGap | Limitation of skills-based matching | Medium | E-023, E-024 |
| Talent market dynamics (supply/demand shifts for specific skills) | TalentMarketDynamics | Captured by Economic Graph; informs sourcing insights | High | E-025 |
| Recruiter-hiring manager information asymmetry | RecruiterHiringManagerInformationAsymmetry | Motivation for Teams collaboration integration | High | E-002, E-040 |
| Candidate drop-off in prescreening (non-response) | CandidateNonResponse | Motivation for Automated Follow-Up | High | E-032 |
| Model drift over time (models becoming less accurate as market changes) | ModelDrift | Motivation for recurring LiFT audits and model retraining | High | E-008, E-019 |

---

## 10. hi:TaskExecution

`hi:TaskExecution` instances represent the actual running of a task. Each `hi:TaskExecution` `hi:realizesTask` → `hi:Task`, and `hi:evaluatedBy` → `hi:Evaluation`. The method used is captured as `hi:hasMethodConcept` → `hint:Method`.

| Task Being Executed | hi:TaskExecution Instance | hint:Method Concept | hi:evaluatedBy (Evaluation) | Confidence | Evidence IDs |
|---|---|---|---|---|---|
| Candidate sourcing workflow (full pipeline) | TaskExecution_Sourcing | SupervisedMultiAgentOrchestration | Evaluation_SourcingEfficiency | High | E-012, E-013, E-014 |
| Candidate evaluation (EON + GPT-4o) | TaskExecution_Evaluation | LLMBasedEvidenceCitedEvaluation | Evaluation_EvaluationQuality | High | E-013, E-014, E-046 |
| InMail draft generation (AI-Assisted Messages) | TaskExecution_InMailGeneration | LLMPersonalisedMessageGeneration | Evaluation_InMailAcceptance | High | E-030, E-031, E-032 |
| Prescreening Q&A session | TaskExecution_Prescreening | NLPBasedConversationalQA | Evaluation_PrescreeningCompletionQuality | High | E-038 |
| Fairness-aware re-ranking | TaskExecution_FairnessReranking | FairnessAwareRerankingAlgorithm | Evaluation_RepresentativeRanking | High | E-041, E-010 |
| LiFT bias measurement cycle | TaskExecution_BiasAudit | StatisticalSubgroupFairnessAnalysis | Evaluation_FairnessAudit | High | E-017, E-018 |
| HLTM query and personalisation | TaskExecution_HLTMPersonalisation | HierarchicalSemanticMemoryRetrieval | Evaluation_PersonalisationQuality | High | E-046 |
| In-session personalisation | TaskExecution_InSessionPersonalisation | OnlineModelAdaptation | Evaluation_InSessionQuality | High | E-044 |
| ATS data synchronisation (RSC+) | TaskExecution_ATSSync | ContinuousAPIDataIngestion | Evaluation_ATSSyncEfficiency | High | E-020, E-033 |

### hint:Method Concepts (Controlled Vocabulary)

| hint:Method Concept | Description | Used In |
|---|---|---|
| SupervisedMultiAgentOrchestration | Supervisor-and-sub-agent pattern via LangChain/LangGraph messaging layer | TaskExecution_Sourcing |
| LLMBasedEvidenceCitedEvaluation | Dual model (GPT-4o + EON) generates evidence-cited summaries; speculative decoding for latency | TaskExecution_Evaluation |
| LLMPersonalisedMessageGeneration | GPT-4o generates personalised InMails using recruiter + candidate + job fields | TaskExecution_InMailGeneration |
| NLPBasedConversationalQA | InMail-based Q&A; NLP extraction of structured answers from candidate responses | TaskExecution_Prescreening |
| FairnessAwareRerankingAlgorithm | Geyik et al. (KDD 2019) algorithm; re-ranks to match qualified population distribution | TaskExecution_FairnessReranking |
| StatisticalSubgroupFairnessAnalysis | LiFT; measures bias across protected attribute subgroups in training data and model outputs | TaskExecution_BiasAudit |
| HierarchicalSemanticMemoryRetrieval | HLTM schema-aligned tree; multi-granularity retrieval; massively parallel; lossless ingestion | TaskExecution_HLTMPersonalisation |
| OnlineModelAdaptation | Real-time model update within recruiter session from view/contact/archive signals | TaskExecution_InSessionPersonalisation |
| ContinuousAPIDataIngestion | RSC+ API pulls ATS data continuously; programmatic segmentation; US data centre storage | TaskExecution_ATSSync |
| GradientBoostedDecisionTreeRanking | GBDT applied to candidate features; two-pass ranking (coarse + reranking) | TaskExecution_Sourcing |
| GeneralizedLinearMixedModelling | GLMix entity-level personalisation applied to ranking | TaskExecution_Sourcing |

---

## 11. hi:Evaluation and hi:Experiment

Each `hi:TaskExecution` is `hi:evaluatedBy` → `hi:Evaluation`. Each `hi:Evaluation` `hi:hasExperiment` → `hi:Experiment`. The experiment documents the null hypothesis, alternative hypothesis, and metric concepts.

| Evaluation | hi:Experiment | Null Hypothesis | Alternative Hypothesis | hint:Metric Concept | Confidence | Evidence IDs |
|---|---|---|---|---|---|---|
| Evaluation_SourcingEfficiency | Experiment_SourcingEfficiency | "Hiring Assistant does not reduce the number of profiles a recruiter reviews per hire" | "Hiring Assistant reduces profiles reviewed per hire by at least 60%" | ProfilesReviewedPerHire; TimeSavedPerRole | High | E-001, E-002 |
| Evaluation_EvaluationQuality | Experiment_EvaluationQuality | "AI-generated candidate summaries do not reduce recruiter review time" | "Evidence-cited AI summaries enable recruiters to assess candidates faster and with equal accuracy" | HallucinationRate; FulfillmentFailureRate; NegativeFeedbackRate | High | E-019, E-046 |
| Evaluation_InMailAcceptance | Experiment_InMailAcceptance | "AI-generated InMails do not improve candidate response rates" | "AI-generated InMails increase InMail acceptance by at least 40%" | InMailAcceptanceRate; AutomatedFollowUpAcceptanceRate | High | E-001, E-030, E-032 |
| Evaluation_PrescreeningCompletionQuality | Experiment_Prescreening | "Automated prescreening does not save recruiter time on qualification confirmation" | "Automated prescreening saves at least 1.5 hours per role in applicant identification" | ApplicantIdentificationTimeSaved; PrescreeningCompletionRate (GAP) | High | E-005 |
| Evaluation_RepresentativeRanking | Experiment_RepresentativeRanking | "Fairness-aware re-ranking does not improve representation of protected groups in candidate shortlists" | "Fairness-aware re-ranking produces approximately 3x more queries with representative results without harming engagement metrics" | RepresentativeRankingCoverage; GenderRepresentationRatioInTopK | High | E-041, E-010 |
| Evaluation_FairnessAudit | Experiment_FairnessAudit | "Deployed ranking models do not exhibit detectable bias toward protected attribute subgroups" | "LiFT identifies statistically significant bias patterns that require model retraining or demotion" | BiasDetectionRate; ModelRetestFrequency | High | E-017, E-018, E-019 |
| Evaluation_PersonalisationQuality | Experiment_PersonalisationQuality | "HLTM-based personalisation does not improve candidate recommendation quality for repeat-role recruiters" | "HLTM reduces the negative feedback rate by 5–10 percentage points vs. no long-term memory baseline" | NegativeFeedbackRateReduction | High | E-046 |
| Evaluation_InSessionQuality | Experiment_InSessionQuality | "In-session personalisation does not improve candidate match quality within a single session" | "In-session adaption leads to measurably higher recruiter engagement with later results in a session vs. earlier results" | InSessionEngagementDelta (Inferred) | Medium | E-044 |
| Evaluation_ATSSyncEfficiency | Experiment_ATSSyncEfficiency | "RSC+ integration does not reduce recruiter time spent switching between LinkedIn and ATS" | "RSC+ saves recruiters at least 3.5 hours per week vs. manual ATS toggling" | RecruiterTimeSavedWithRSC; InMailAcceptanceRateWithRSC | High | E-033 |

### hint:Metric Concepts (Controlled Vocabulary)

| hint:Metric Concept | Value (where documented) | Confidence | Evidence IDs |
|---|---|---|---|
| ProfilesReviewedPerHire | 62–81% reduction with Hiring Assistant | High | E-001, E-002 |
| TimeSavedPerRole | 4+ hours average per user per role | High | E-001, E-002 |
| InMailAcceptanceRate | +66% HA vs traditional; +55% AI messages vs manual | High | E-001, E-030 |
| AutomatedFollowUpAcceptanceRate | +39% vs manual follow-up | High | E-032 |
| ApplicantIdentificationTimeSaved | 1.5 hours per role | High | E-005 |
| PrescreeningCompletionRate | Not publicly documented — Gap E-GAP-02 | — | E-GAP-02 |
| RepresentativeRankingCoverage | ~3x increase in queries with representative results | High | E-041 |
| GenderRepresentationRatioInTopK | Results match qualified population distribution for gender/age | High | E-041 |
| BiasDetectionRate | Measured internally; not publicly disclosed | Low | E-017, E-018 |
| NegativeFeedbackRateReduction | 5–10 percentage-point reduction with HLTM vs. baseline | High | E-046 |
| RecruiterTimeSavedWithRSC | 3.5 hours/week | High | E-033 |
| InMailAcceptanceRateWithRSC | +7% with RSC vs. without | High | E-033 |
| HallucinationRate | Internal model testing metric; not publicly disclosed | Low | E-019 |
| FulfillmentFailureRate | Internal model testing metric; not publicly disclosed | Low | E-019 |
| InSessionEngagementDelta | Not documented; inferred from in-session personalisation design | Low | E-044 |

---

## 12. CARE Principles Mapped to hi: Classes

The CARE principles (Akata et al. 2020, E-048) map onto the formal ontology as follows:

| CARE Principle | Primary hi: Classes | Evidence | Assessment |
|---|---|---|---|
| **Collaborative** | `hi:HITeam`, `hi:Interaction`, `hi:Task` (shared), `hi:Goal` (shared) | Recruiter + HA jointly execute sourcing/evaluation; human controls all final decisions; Teams collaboration with hiring manager | ✅ Strongly evidenced (E-001, E-002, E-019, E-020, E-047) |
| **Adaptive** | `hi:ArtificialAgent` (HLTM, QA Model, GLMix, InSessionPersonalisation), `hi:TaskExecution` (HLTMPersonalisation, InSessionPersonalisation) | HLTM cross-session learning; QA model online learning; in-session adaptation; LiFT-triggered model retraining | ✅ Strongly evidenced (E-027, E-044, E-046, E-008) |
| **Responsible** | `hi:Context` (Constraints), `hi:ArtificialAgent` (LiFT, RepresentativeRanking), `hi:Task` (ReviewAndApproveFairnessActions, DefineFairnessCriteria), `hint:Constraint` | 5 Responsible AI Principles; GDPR; SOC2; no sensitive data processed; no autonomous decisions; fairness-by-design | ✅ Strongly evidenced (E-009, E-010, E-017, E-019, E-020, E-041) |
| **Explainable** | `hi:TaskExecution` (EvaluationAgent outputs), `hi:Interaction` (SurfaceQualificationMatchGap, DeliverCandidateShortlist), `hint:Method` (LLMBasedEvidenceCitedEvaluation) | Match/gap indicators; evidence-cited summaries; filter breakdown; XAI suggestions; public AI Transparency docs | ✅ Partially evidenced — HLTM inferences not surfaced (E-GAP-04) |

---

## 13. Summary: Key Ontology Properties Used

| Property | Domain → Range | Usage in LinkedIn Recruiter Mapping |
|---|---|---|
| `hi:hasMember` | `hi:HITeam` → `hi:Agent` | Links recruiter, hiring manager, AI agents to the hiring project team |
| `hi:hasGoal` | `hi:HITeam` → `hi:Goal` | Links team to shared hiring goals |
| `hi:operatesInContext` | `hi:HITeam` → `hi:Context` | Links team to recruiting environment, constraints, and phenomena |
| `hi:introducesHITeam` | `hi:UseCase` → `hi:HITeam` | Each scenario (UseCase) introduces the team configuration for that scenario |
| `hi:hasDomainConcept` | `hi:UseCase` → `hint:Domain` | Maps all scenarios to the TalentAcquisition domain |
| `hi:hasUseCaseConcept` | `hi:UseCase` → `hint:UseCase` | Links use case instances to controlled vocabulary concepts |
| `hi:hasAgentConcept` | `hi:Agent` → `hint:Agent` | Links agent instances to thesaurus concepts |
| `hi:hasRoleConcept` | `hi:Agent` → `hint:Role` | Links each agent to their role concept |
| `hi:hasCapability` | `hi:Agent` → `hi:Capability` | Maps agents to their capabilities |
| `hi:isAssignedToTask` | `hi:Agent` → `hi:Task` | Maps primarily responsible agents to tasks |
| `hi:isEligibleForTask` | `hi:Agent` → `hi:Task` | Maps agents who can participate but are not primary |
| `hi:hasAgentInvolved` | `hi:Agent` → `hi:Agent` | Captures agent-to-agent coordination (supervisor→sub-agent; recruiter→HA) |
| `hi:requiresCapability` | `hi:Task` → `hi:Capability` | Maps tasks to the capabilities they require |
| `hi:allowsTask` | `hi:Capability` → `hi:Task` | Inverse: capabilities enable tasks |
| `hi:towardsGoal` | `hi:Task` → `hi:Goal` | Every task is oriented toward one or more shared goals |
| `hi:requiresTask` | `hi:Task` → `hi:Task` | Captures task dependencies (e.g., ParseNLQualifications requires DefineHiringQualifications) |
| `hi:realizedBy` | `hi:Task` → `hi:TaskExecution` | Connects tasks to their executions |
| `hi:realizesTask` | `hi:TaskExecution` → `hi:Task` | Inverse of realizedBy |
| `hi:hasMethodConcept` | `hi:TaskExecution` → `hint:Method` | Captures how a task execution is performed |
| `hi:evaluatedBy` | `hi:TaskExecution` → `hi:Evaluation` | Links executions to their formal evaluation |
| `hi:hasExperiment` | `hi:Evaluation` → `hi:Experiment` | Links evaluation to formal experiment structure |
| `hi:hasNullHypothesis` | `hi:Experiment` → xsd:string | Null hypothesis text |
| `hi:hasAlternativeHypothesis` | `hi:Experiment` → xsd:string | Alternative hypothesis text |
| `hi:hasMetricConcept` | `hi:Experiment` → `hint:Metric` | Links experiment to evaluation metric |
| `hi:performedBy` | `hi:Interaction` → `hi:Agent` | Identifies which agent(s) participate in the interaction |
| `hi:hasInteractionIntentConcept` | `hi:Interaction` → `hint:InteractionIntentConcept` | Captures the why of the interaction |
| `hi:hasInteractionModalityConcept` | `hi:Interaction` → `hint:InteractionModalityConcept` | Captures the how/channel of the interaction |
| `hi:hasContextConcept` | `hi:Context` → `hint:Context` | Maps context instances to controlled vocabulary |
| `hi:hasConstraintConcept` | `hi:Context` → `hint:Constraint` | Maps limiting conditions on the context |
| `hi:hasPhenomenonConcept` | `hi:Context` → `hint:Phenomenon` | Maps observable environmental conditions |
| `hi:influenceOn` | `hi:Context` → `hi:HITeam` / `hi:TaskExecution` | Context shapes team behaviour and task execution |
| `hi:hasCapabilityConcept` | `hi:Capability` → `hint:Capability` | Thesaurus link for capability |
| `hi:hasTaskConcept` | `hi:Task` → `hint:Task` | Thesaurus link for task |
| `hi:hasGoalConcept` | `hi:Goal` → `hint:Goal` | Thesaurus link for goal |

---

## 14. Concepts Not in Previous Mapping (Added by HI Ontology Alignment)

The following concepts were absent from the previous version and are now added:

| Newly Added Concept | hi:/hint: Class | Why Added |
|---|---|---|
| `hi:HITeam` | `hi:HITeam` | The actual central ontology class — previously I used the informal "HybridIntelligenceSystem" |
| `hi:UseCase` (8 instances, one per scenario) | `hi:UseCase` | Scenarios must map to the formal UseCase class that introduces a HITeam |
| `hint:Domain` = TalentAcquisition | `hint:Domain` | Domain concept was missing; required by UseCase |
| `hint:Role` (5 role concepts) | `hint:Role` | Roles are separate from agents in the ontology; e.g., RecruiterRole ≠ RecruiterAgent |
| `hi:TaskExecution` (9 instances) | `hi:TaskExecution` | Tasks must be separated from their executions; executions are what are evaluated |
| `hi:Evaluation` + `hi:Experiment` (9 instances) | `hi:Evaluation`, `hi:Experiment` | Formal evaluation structure including null/alternative hypotheses was missing |
| `hint:Metric` (15 concepts) | `hint:Metric` | Metrics were listed informally; now properly linked via hasMetricConcept |
| `hint:Method` (11 concepts) | `hint:Method` | Processing methods were described narratively; now formally captured |
| `hi:requiresTask` (task dependency graph) | Property | Task ordering/dependencies were not captured; now mapped |
| `hi:isAssignedToTask` vs `hi:isEligibleForTask` | Properties | The distinction between primary assignment and eligibility was missing |
| `hint:Constraint` (9 constraints) | `hint:Constraint` | Context constraints were described in scenarios but not mapped to ontology |
| `hint:Phenomenon` (7 phenomena) | `hint:Phenomenon` | Environmental conditions motivating system design were not mapped |
| `hint:InteractionIntentConcept` | `hint:InteractionIntentConcept` | Interaction intent (the why) was missing from interaction mappings |
| `hint:InteractionModalityConcept` | `hint:InteractionModalityConcept` | Interaction modality (the channel/how) was missing from interaction mappings |
| `hi:hasAgentInvolved` | Property | Agent-to-agent coordination relationships were not formally captured |
