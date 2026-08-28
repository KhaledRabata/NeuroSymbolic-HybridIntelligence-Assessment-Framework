# Ontology Mapping — Elsevier LeapSpace → Hybrid Intelligence Ontology (hi:) / HINT Thesaurus (hint:)
RAS v1.0 | Namespaces: `hi: https://w3id.org/hi-ontology#` | `hint: https://w3id.org/hi-thesaurus#`

This file maps every concept extracted from the evidence base (`sources.md`) onto the classes and object/data properties defined in the supplied `hiontology.ttl` (v2.0.0) and the accompanying diagram. **No RDF triples, instances, or SHACL shapes are produced here** — this is a documentation-only mapping table, per protocol §3 and §16 (File 6).

Each row cites its supporting Evidence ID(s) from `sources.md`. Confidence and Observed/Inferred status follow protocol §11–§12.

---

## 1. hi:HITeam mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| A researcher (or an R&D team) working alongside LeapSpace's multi-model AI system toward a shared research or discovery goal | `hi:HITeam` | Inferred — LeapSpace's own language never uses the literal word "team," but the OWL restriction (≥1 HumanAgent, ≥1 ArtificialAgent jointly pursuing a goal) is directly satisfied by the documented human-AI collaboration pattern | Medium-High | E-001, E-003, E-011 |
| Product team + external guest customer jointly presenting at the "See LeapSpace in Action" webinar | `hi:hasMember` (HITeam → Agent), satisfying the requirement of ≥1 HumanAgent | Observed | Medium | E-009 |
| Content-governance ensemble: peer reviewers + Scopus Content Selection and Advisory Board + LeapSpace Advisory Board, jointly responsible for what counts as trustworthy content | `hi:hasMember`; a distinct, curation-focused HITeam-like grouping distinguished from the researcher-facing usage team | Observed | High | E-011, E-017 |
| Cross-functional pharma R&D roles (discovery scientists, medicinal chemists, preclinical, clinical development, pharmacovigilance/regulatory, medical affairs) who may all interact with LeapSpace on a shared program | `hi:hasMember`, `hi:hasGoal` (shared program-level goal, e.g., de-risking a compound) | Observed (roles) / Inferred (single shared-goal framing across all six roles) | Medium | E-013 |

## 2. hi:UseCase mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| "LeapSpace" itself as a structured application of AI to a research/discovery situation | `hi:UseCase` | Observed | High | E-001, E-002 |
| Distinct sub-use-cases: academic literature exploration vs. corporate/industry R&D vs. pharma-specific R&D | `hi:UseCase` (multiple instances); `hi:hasDomainConcept` → `hint:Domain` (Higher Education vs. Corporate R&D vs. Pharmaceuticals/Biotechnology) | Observed | High | E-001, E-004, E-013 |
| Each use case introduces a governed, human-AI collaborative workspace | `hi:hasHITeam` (UseCase → HITeam) | Inferred — the property linkage is a natural formalization of the documented "researchers work alongside AI in one workspace" pattern | Medium | E-001, E-011 |

## 3. hi:Agent / hi:HumanAgent / hi:ArtificialAgent mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| University researchers and PhD students | `hi:HumanAgent`; `hint:Role` = Academic Researcher / PhD Student | Observed | High | E-001 |
| R&D professionals in industry (general) | `hi:HumanAgent`; `hint:Role` = Industry R&D Professional | Observed | High | E-001, E-004 |
| Discovery scientists, medicinal chemists, preclinical teams, clinical development teams, pharmacovigilance/regulatory professionals, medical affairs specialists | `hi:HumanAgent`; `hint:Role` = six distinct pharma-R&D role types | Observed | High | E-013 |
| Library Services managers/directors (e.g., Associate Director, Global Library Services) | `hi:HumanAgent`; `hint:Role` = Library/Information Services Professional | Observed | High | E-004, E-010 |
| Named internal Elsevier product roles (SVP Generative AI; VP Product Management; Portfolio Delivery Lead, AI Innovations) | `hi:HumanAgent`; `hint:Role` = Product/AI Innovation Team Member — upstream of the runtime user-facing HITeam, shapes the tool rather than uses it operationally | Observed | Medium — relevant to system design/governance, not day-to-day research task execution | E-009 |
| External guest researcher-customer (Global Medical Lead, Orion Corporation) | `hi:HumanAgent`; `hint:Role` = Corporate R&D End User / Voice-of-Customer | Observed | Medium | E-009 |
| Journal peer reviewers | `hi:HumanAgent`; `hint:Role` = Content Curator/Peer Reviewer | Observed | High | E-011 |
| Independent Scopus Content Selection and Advisory Board; independent LeapSpace Advisory Board (chaired by a named professor) | `hi:HumanAgent`; `hint:Role` = Governance/Advisory Board Member | Observed | High | E-011, E-017 |
| LeapSpace's multi-model AI system (selects models per task) | `hi:ArtificialAgent` | Observed | High | E-001, E-003, E-011, E-012 |
| The underlying Scopus AI engine (summary/analysis, concept maps, topic-expert identification) | `hi:ArtificialAgent` (sub-component) | Observed | High | E-008 |
| The underlying ScienceDirect AI engine | `hi:ArtificialAgent` (sub-component) | Observed | Medium — named as a foundation in E-006/E-013 but not independently fetched/detailed in this pass (see `knowledge_gaps.md`) | E-006, E-013 |
| Writing Coach (dialogue-based drafting assistant) | `hi:ArtificialAgent` | Observed | High | E-014, E-015 |
| Claim Radar (evidence-verification agent) | `hi:ArtificialAgent` | Observed | High | E-004, E-014, E-015 |
| Compare Tables (structured literature-comparison extraction agent) | `hi:ArtificialAgent` | Observed | High | E-014 |
| Reasoning-engine and retrieval-augmented-generation (RAG) components underpinning Deep Research reports | `hi:ArtificialAgent` | Observed | High | E-002, E-006 |

## 4. hi:Goal mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Help researchers "work faster, think deeper, and achieve more" while remaining in control | `hi:Goal`; `hi:hasGoalConcept` → `hint:Goal` (research acceleration with human primacy) | Observed | High | E-001 |
| Move research "from curiosity to discovery, faster" / "from curiosity to discovery without leaving trusted ground" | `hi:Goal` | Observed | High | E-001, E-006 |
| De-risk compounds before committing to series development; detect safety signals earlier with regulator-ready documentation (pharma-specific) | `hi:Goal` | Observed | High | E-013 |
| Rebuild researcher trust in AI tools (addressing the fact that "only 22% currently trust existing AI tools") | `hi:Goal` | Observed | Medium-High — the trust statistic is independently reported (E-010), but framing it as an explicit product *goal* rather than a market-context observation is a reasonable, evidence-consistent inference | E-010, E-011 |
| Reinforce, not replace, human research judgment | `hi:Goal` | Observed | High | E-001, E-017, E-018 |
| Preserve publisher-neutral, unbiased access to scholarly literature ("Publisher-neutral insights") | `hi:Goal` | Observed | High | E-001, E-017 |

## 5. hi:Task / hi:TaskExecution mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Explore complex research/scientific questions against scholarly literature | `hi:Task`; `hi:hasTaskConcept` → `hint:Task` (Literature Exploration) | Observed | High | E-001, E-013 |
| Compare papers/evidence and perspectives via synthesized insights | `hi:Task`; realized via Compare/Compare Tables `hi:TaskExecution` | Observed | High | E-001, E-004, E-006, E-014 |
| Generate a Deep Research report (outlined scope, assumptions, evidence, patterns and gaps) | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution`; `hi:towardsGoal` → discovery-acceleration goal | Observed | High | E-001, E-002, E-006 |
| Identify collaborators/topic experts (Author Search) using natural-language querying | `hi:Task` | Observed | High | E-001, E-006 |
| Discover funding opportunities from curated institutional grant data | `hi:Task` | Observed | High | E-001, E-002 |
| Upload and analyze personal/proprietary documents alongside scholarly literature | `hi:Task` | Observed | High | E-001, E-003 |
| Draft, refine, and strengthen written research arguments in dialogue with Writing Coach | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution`; `hi:hasInteractionEpisode` → dialogue `hi:Interaction` | Observed | High | E-014, E-015 |
| Verify a claim's alignment with, and consensus across, the published literature (Claim Radar) | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution` | Observed | High | E-004, E-014, E-015 |
| Extract evidence into a structured comparison table along researcher-defined dimensions | `hi:Task` | Observed | High | E-014 |
| Content curation and selection (peer review, advisory-board oversight) as an upstream governance task | `hi:Task` | Observed | High | E-011, E-017 |
| Model evaluation and quality assurance; ongoing validation and governance (periodic Scopus AI quality-framework evaluation) | `hi:Task`; `hi:realizedBy` → `hi:TaskExecution`; `hi:evaluatedBy` → `hi:Evaluation` | Observed | High | E-008, E-017 |
| Sign in and access LeapSpace via institutional or individual account (onboarding task) | `hi:Task` | Observed | High | E-018 |

## 6. hi:Capability mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Multi-model AI selection (choosing the right model per task) | `hi:Capability`; `hi:hasCapabilityConcept` → `hint:Capability` (Adaptive Model Selection) | Observed | High | E-001, E-003, E-011, E-012 |
| Agentic AI, generative AI, reasoning-engine, and retrieval-augmented-generation methods | `hi:Capability` | Observed | High | E-002 |
| Real-time visibility into reasoning steps ("shows the steps used to generate each answer in real time") | `hi:Capability`; `hi:allowsTask` → explanation/transparency task | Observed | High | E-011, E-012 |
| Claim-to-source traceability and evidence provenance (Trust Card) | `hi:Capability` | Observed | High | E-001, E-002, E-003, E-011, E-017, E-018 |
| Cross-literature consensus/contradiction detection (Claim Radar) | `hi:Capability` | Observed | High | E-004, E-014, E-015 |
| Natural-language, non-keyword collaborator search | `hi:Capability` | Observed | High | E-006 |
| Structured comparison-table extraction along user-defined dimensions | `hi:Capability` | Observed | High | E-014 |
| Hallucination minimization via curated, peer-reviewed source grounding | `hi:Capability` | Observed | High | E-005, E-018 |
| Publisher-neutral, recency-boosted, ownership-independent ranking | `hi:Capability` | Observed | High | E-017 |
| Enterprise-grade data security/privacy (encryption, no third-party LLM training on user data), aligned to ISO 27001 | `hi:Capability`; `hi:hasConstraintConcept` → `hint:Constraint` (ISO 27001) | Observed | High | E-003, E-004, E-009, E-014, E-017 |
| Automated bias-detection tooling and post-deployment monitoring (enterprise-wide Responsible AI capability, applied to LeapSpace as a covered product) | `hi:Capability` | Observed | High | E-007 |

## 7. hi:Context mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Higher-education / academic research environment | `hi:Context`; `hi:hasContextConcept` → `hint:Domain` (Higher Education) | Observed | High | E-001, E-003 |
| Corporate/industrial R&D environment generally | `hi:Context`; `hi:hasContextConcept` → `hint:Domain` (Industry R&D) | Observed | High | E-001, E-004 |
| Pharmaceutical/biotechnology R&D, spanning discovery through pharmacovigilance and regulatory affairs | `hi:Context`; `hi:hasContextConcept` → `hint:Domain` (Pharma/Biotech) | Observed | High | E-013 |
| Publisher-partnership ecosystem (Elsevier + Emerald + IOP + NEJM Group + Sage + 7,000+ Scopus-indexed publishers) as the operating content environment | `hi:Context` | Observed | High | E-002, E-003, E-012 |
| Elsevier's enterprise-wide Responsible AI policy framework as a governing context/constraint | `hi:Context`; `hi:hasConstraintConcept` → `hint:Constraint` (Responsible AI Principles) | Observed | High | E-007 |
| ISO 27001-aligned cyber-security framework as an operating constraint | `hi:hasConstraintConcept` → `hint:Constraint` (ISO 27001) | Observed | High | E-017 |
| Researcher-trust deficit toward AI tools generally (22% trust / 86% concerned about critical errors) as a background phenomenon shaping why LeapSpace's trust features exist | `hi:hasPhenomenonConcept` → `hint:Phenomenon` (AI-trust deficit); `hi:hasInfluenceOn` → HITeam design | Observed | Medium-High | E-010 |
| Market-concentration / knowledge-fragmentation concerns raised by independent critics (multi-publisher AI-tool consolidation; paywalled-content monetization layered atop subscription costs) | `hi:hasPhenomenonConcept` → `hint:Phenomenon` (market concentration, access fragmentation) | Observed | High (as a documented external critique; not an Elsevier-endorsed framing) | E-016 |
| Only ~22% of 2024 research articles covered at time of reporting, due to paywall/licensing constraints | `hi:hasConstraintConcept` → `hint:Constraint` (content-coverage limitation) | Observed | Medium — single-source figure from an independent critical article, not corroborated elsewhere in this research pass | E-016 |

## 8. hi:Interaction mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Two-panel, dialogue-based Writing Coach session (document editor + chat assistant panel) | `hi:Interaction`; `hi:hasAgentInvolved` (HumanAgent researcher + ArtificialAgent Writing Coach); `hi:hasInteractionModalityConcept` = chat/dialogue | Observed | High | E-015 |
| Human approval required for every AI-recommended change ("every recommended change requiring approval") | `hi:Interaction`; `hi:hasInteractionIntentConcept` = approval/verification | Observed | High | E-014 |
| Researcher querying LeapSpace with natural-language research questions and receiving structured, referenced answers | `hi:Interaction`; `hi:hasInteractionModalityConcept` = conversational Q&A | Observed | High | E-001, E-006 |
| Webinar-style demo interaction between Elsevier product team and prospective/existing customers | `hi:Interaction`; `hi:hasAgentInvolved` (multiple HumanAgents) | Observed | Medium | E-009 |
| Content-governance interaction: peer reviewers and advisory-board members jointly deciding what content is trustworthy/included | `hi:Interaction` | Observed | Medium | E-011, E-017 |

## 9. hi:Evaluation / hi:Experiment mappings

| LeapSpace concept | hi: Class/Property | Observed/Inferred | Confidence | Evidence |
|---|---|---|---|---|
| Periodic Scopus AI "quality framework" evaluation | `hi:Evaluation` | Observed | High | E-008 |
| Model evaluation and quality assurance as an explicit, named human-oversight function | `hi:Evaluation`; `hi:evaluatedBy` (TaskExecution → Evaluation) | Observed | High | E-017 |
| Vendor-reported hallucination-risk figure ("less than 1%" serious hallucination) | `hi:Evaluation`; `hi:hasMetricConcept` → `hint:Metric` (Hallucination Rate) | Observed (as a vendor claim) | Medium — single-source, methodology not disclosed, and Search 12 found no independent corroborating benchmark (see `knowledge_gaps.md`) | E-005 |
| Claim Radar's claim-level evidence checking against 107M+ peer-reviewed papers, returning support/contradict/mixed labels | `hi:Evaluation` | Observed | High | E-015 |
| Automated bias-detection tooling as an evaluation mechanism | `hi:Evaluation` | Observed | High | E-007 |
| A formal, LeapSpace-specific experimental setup with a stated null/alternative hypothesis (`hi:Experiment`, `hi:hasNullHypothesis`, `hi:hasAlternativeHypothesis`) | *(No confident mapping)* | **Not found** — Inferred only as a structural possibility | Low | *(none — explicit gap, see `knowledge_gaps.md`)* |
| Independent critical assessment that "no standardized evaluation method exists for assessing AI-generated summary accuracy" | `hi:hasPhenomenonConcept` → `hint:Phenomenon` (evaluation-standardization gap); relevant as context bounding the confidence of any `hi:Evaluation` instance built from vendor-reported metrics | Observed | High (as a documented expert critique) | E-016 |

## 10. hint: Thesaurus concept mappings (representative, non-exhaustive)

| LeapSpace term | hint: concept type |
|---|---|
| Academic Researcher, PhD Student, Industry R&D Professional, Discovery Scientist, Medicinal Chemist, Preclinical Researcher, Clinical Development Professional, Pharmacovigilance/Regulatory Professional, Medical Affairs Specialist, Library/Information Services Professional, Advisory Board Member, Peer Reviewer | `hint:Role` |
| Higher Education, Corporate/Industry R&D, Pharmaceuticals and Biotechnology | `hint:Domain` |
| Literature Exploration, Deep Research Report Generation, Evidence Comparison, Collaborator/Expert Identification, Funding Discovery, Document Upload & Analysis, Argument Drafting/Strengthening (Writing Coach), Claim Verification (Claim Radar), Structured Table Extraction (Compare Tables), Content Curation, Model Evaluation/QA | `hint:Task` |
| Multi-Model AI Selection, Real-Time Reasoning-Step Visibility, Claim-to-Source Traceability, Consensus/Contradiction Detection, Natural-Language Search, Hallucination Minimization, Publisher-Neutral Ranking, Enterprise-Grade Security/Privacy | `hint:Capability` |
| Responsible AI Principles, ISO 27001, Publisher-Neutrality Governance, Institutional Data-Privacy Terms | `hint:Constraint` |
| AI-Trust Deficit (22%/86% survey figures), Market Concentration Risk, Knowledge-Access Fragmentation, Evaluation-Standardization Gap | `hint:Phenomenon` |
| Hallucination Rate, Content-Coverage Percentage, Claim-Support/Contradict/Mixed Labels, Quality-Framework Score | `hint:Metric` |
| Multi-model selection, retrieval-augmented generation, reasoning engines, agentic AI orchestration | `hint:Method` |
| Chat/dialogue interface, two-panel editor+assistant layout, webinar/demo format | `hint:InteractionModalityConcept` |
| Approval/verification, explanation/justification, drafting/refinement, contradiction-surfacing | `hint:InteractionIntentConcept` |

---

## Notes on Mapping Method

1. Every mapping above is anchored to at least one Evidence ID from `sources.md`; rows marked **Inferred** state explicitly why the inference was necessary.
2. No `skos:Concept` instances, class instances, or property assertions are created here — this table only names the mapping target class/property from the ontology; instantiation is deferred to the (out-of-scope) Knowledge Graph construction phase.
3. Where the HI Ontology has an OWL cardinality restriction (e.g., `hi:HITeam` requires ≥1 `hi:HumanAgent` and ≥1 `hi:ArtificialAgent`; `hi:Task` requires ≥1 `hi:Capability`; `hi:Goal` requires ≥1 `hi:Task`; `hi:Interaction` requires ≥2 `hi:Agent`), the mapping table was checked against that restriction and, where evidence for one side was thin, this is flagged in the Observed/Inferred column rather than silently assumed.
4. `hi:Experiment` (and its two datatype properties) is the one core ontology class for which **no confident LeapSpace-specific mapping could be constructed** from the available evidence — this is treated as a documented gap (`knowledge_gaps.md`), not papered over with an invented example.
