# Ontology Mapping — LeapSpace by Elsevier

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **LeapSpace (Elsevier)**
Maps every extracted concept to the Hybrid Intelligence (HI) Ontology (VU Amsterdam, KAI Group, v2.0.0) as supplied (`hiontology.ttl` + diagram). Namespaces: `hi: https://w3id.org/hi-ontology#`, `hint: https://w3id.org/hi-thesaurus#`.

This file documents mappings only. **No RDF triples, no ontology instances, and no SHACL shapes are produced here**, per RAS Section 5/15.

---

## 1. Top-level use case framing

| Extracted concept | HI Ontology class/property | Evidence |
|---|---|---|
| LeapSpace (the product as a governed application domain) | `hi:UseCase` | E-001 |
| Each of the 8 scenarios (Literature Review, New-Topic Exploration, Evidence Synthesis, Claim Validation, Cross-Disciplinary Discovery, Funding Discovery, Writing Coach, Corporate R&D Verification) | `hi:UseCase` (one instance per scenario, `hi:introducesHITeam`-linked to its `hi:HITeam`) | E-001–E-017 (per-scenario, see `scenarios.md`) |
| The set of human + artificial agents collaborating within one scenario (e.g., researcher + Deep Research engine + Claim Radar) | `hi:HITeam` | All scenarios |
| Domain classification (Academic Research, Corporate R&D, Biopharma/Regulated Research, Rare Disease Research) | `hint:Domain` via `hi:hasDomainConcept` | E-003, E-006, E-011 |

---

## 2. Agents

### Human Agents (`hi:HumanAgent`, subclass of `hi:Agent` and `foaf:Person`)

| Extracted role | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| Academic researcher / faculty member | `hi:HumanAgent` — role concept "Academic Researcher" via `hi:hasRoleConcept` | S1, S2, S5, S7 | E-002, E-010 |
| PhD student / postdoctoral researcher | `hi:HumanAgent` — role "PhD Student / Postdoc" | S2, S3 | E-002, E-004 |
| Course instructor | `hi:HumanAgent` — role "Course Instructor" | S1 | E-010 |
| Corporate R&D scientist | `hi:HumanAgent` — role "Corporate R&D Scientist" | S8 | E-011 |
| Library / information-services manager | `hi:HumanAgent` — role "Library/Information Services Manager" | S8 | E-011 |
| Nonprofit/foundation Chief Science Officer | `hi:HumanAgent` — role "Chief Science Officer" | S3 | E-006 |
| Biopharmaceutical/regulatory-compliance researcher | `hi:HumanAgent` — role "Regulatory Compliance Researcher" *(role title Inferred — Medium confidence; reasoning: E-003 states "biopharmaceutical teams requiring regulatory compliance" as a persona category but does not name a specific job title)* | S8 | E-003 |
| Advisory Board Chair (Scopus Content Selection and Advisory Board) | `hi:HumanAgent` — role "Governance Board Chair"; named individual: Professor Jörg-Rüdiger Sack | Cross-cutting (governance) | E-008 |
| Independent AI Advisory Board member(s) | `hi:HumanAgent` — role "AI Advisory Board Member" | Cross-cutting (governance) | E-009 |
| Journal peer reviewers (content curation) | `hi:HumanAgent` — role "Peer Reviewer" | Cross-cutting (content curation) | E-002, E-009 |
| Beta-test researcher cohort (development/validation) | `hi:HumanAgent` — role "Beta Tester" | Cross-cutting (pre-launch validation) | E-005 |
| Accountable human decision-maker (Responsible AI Principle 4) | `hi:HumanAgent` — role "Accountable Decision-Maker" | Cross-cutting | E-014 |

### Artificial Agents (`hi:ArtificialAgent`, subclass of `hi:Agent`, disjoint with `hi:HumanAgent`)

| Extracted component | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| LeapSpace conversational summarization engine (Standard mode) | `hi:ArtificialAgent` — agent concept "Conversational Summarization Engine" | S1, S2, S7 | E-001, E-013 |
| Deep Research agentic synthesis engine | `hi:ArtificialAgent` — agent concept "Agentic Research Synthesizer" | S1, S3 | E-001, E-005, E-010 |
| Trust Card generator | `hi:ArtificialAgent` — agent concept "Citation-Attribution Engine" | S4, S7, S8 | E-001, E-007, E-009 |
| Claim Radar evaluation engine | `hi:ArtificialAgent` — agent concept "Claim Evaluation Engine" | S3, S4 | E-007, E-010 |
| Author Search / collaborator-identification engine | `hi:ArtificialAgent` — agent concept "Collaborator Discovery Engine" | S5 | E-001 |
| Hybrid keyword + semantic (vector) search engine | `hi:ArtificialAgent` — agent concept "Hybrid Search Engine" | S2, S5 | E-008, E-010 |
| Find Funding / Funding Discovery engine | `hi:ArtificialAgent` — agent concept "Funding Matching Engine" | S6 | E-005 |
| Writing Coach dialogue engine | `hi:ArtificialAgent` — agent concept "Argument-Testing Dialogue Agent" | S7 | E-001, E-008 |
| Reading Assistant | `hi:ArtificialAgent` — agent concept "Single-Document Analysis Agent" | S8 | E-016 |
| Compare Experiments engine | `hi:ArtificialAgent` — agent concept "Structured Comparison Generator" | S8 | E-016 |
| Underlying multi-model AI architecture (agentic AI, generative AI, reasoning engines, RAG) | `hi:ArtificialAgent` — agent concept "Multi-Model AI Backend" | Cross-cutting | E-005 |
| Third-party foundation LLM (hosted privately, not used for training) | `hi:ArtificialAgent` — agent concept "Foundation Model (Privately Hosted)" *(specific model identity Inferred by analogy to Scopus AI's OpenAI/Azure deployment — Medium confidence, E-012; LeapSpace's own model provider is not named in any direct source)* | Cross-cutting | E-005, E-012, E-015 |

---

## 3. Goals, Tasks, Capabilities

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| "Keep a literature review current despite publication-volume growth" | `hi:Goal` | S1 | E-010 |
| "Rapidly build foundational understanding of a new field" | `hi:Goal` | S2 | E-010 |
| "Synthesize scattered evidence and surface research gaps" | `hi:Goal` | S3 | E-010 |
| "Reduce reliance on unsupported/hallucinated AI claims" | `hi:Goal` | S4 | E-010 |
| "Discover cross-disciplinary connections and collaborators" | `hi:Goal` | S5 | E-001, E-010 |
| "Match research direction to active funding opportunities" | `hi:Goal` | S6 | E-010 |
| "Strengthen evidentiary/logical rigor of a research draft" | `hi:Goal` | S7 | E-001 |
| "Accelerate evidence-based R&D decisions while protecting IP" | `hi:Goal` | S8 | E-011 |
| Formulate natural-language literature-review query | `hi:Task` — task concept "Literature Query Formulation" | S1, S2 | E-010, E-013 |
| Generate summary response or Deep Research report | `hi:Task` — task concept "Research Synthesis" | S1, S3 | E-010 |
| Visualize findings as tables/flowcharts | `hi:Task` — task concept "Findings Visualization" | S1 | E-010 |
| Tailor response to experience level | `hi:Task` — task concept "Adaptive Explanation" | S2 | E-010 |
| Upload and blend personal documents into analysis | `hi:Task` — task concept "Document Integration" | S3, S8 | E-010, E-011 |
| Run Claim Radar on a specific claim | `hi:Task` — task concept "Claim Evaluation" | S3, S4 | E-007 |
| Review Trust Card for a claim | `hi:Task` — task concept "Source Verification" | S4, S7, S8 | E-001, E-007, E-009 |
| Blend keyword and semantic search | `hi:Task` — task concept "Hybrid Literature Search" | S2, S5 | E-008, E-010 |
| Run Author Search for collaborators | `hi:Task` — task concept "Collaborator Identification" | S5 | E-001 |
| Search/filter Find Funding by topic and country | `hi:Task` — task concept "Funding Search" | S6 | E-010 |
| Submit draft argument to Writing Coach | `hi:Task` — task concept "Argument Testing" | S7 | E-004 |
| Engage in back-and-forth dialogue to refine draft | `hi:Task` — task concept "Iterative Draft Refinement" | S7 | E-004 |
| Analyze/summarize a single article (Reading Assistant) | `hi:Task` — task concept "Single-Document Analysis" | S8 | E-016 |
| Generate structured multi-study comparison table (Compare Experiments) | `hi:Task` — task concept "Multi-Study Comparison" | S8 | E-016 |
| Large-scale literature retrieval | `hi:Capability` — capability concept "Literature Retrieval" (`hi:allowsTask` → Research Synthesis) | S1, S3 | E-001, E-010 |
| Natural-language query interpretation | `hi:Capability` — capability concept "NLU Query Interpretation" | S2 | E-010, E-013 |
| Agentic multi-source synthesis (up to 300 sources) | `hi:Capability` — capability concept "Agentic Synthesis" | S3 | E-010 |
| Claim-level evidence classification (support/contradict/mixed) | `hi:Capability` — capability concept "Claim Classification" | S3, S4 | E-007 |
| Passage-level source attribution | `hi:Capability` — capability concept "Passage Attribution" | S4, S7 | E-009 |
| Hybrid keyword/semantic search across 330+ disciplines | `hi:Capability` — capability concept "Cross-Disciplinary Search" | S2, S5 | E-010 |
| Curated funding-database search | `hi:Capability` — capability concept "Funding Discovery" | S6 | E-005, E-010 |
| Dialogue-based reasoning interrogation | `hi:Capability` — capability concept "Argument Interrogation" | S7 | E-001 |
| Structured five-dimension study comparison | `hi:Capability` — capability concept "Structured Comparison" | S8 | E-016 |
| Enterprise-grade encryption / zero data retention | `hi:Capability` — capability concept "Data Protection" | S8 (cross-cutting) | E-011, E-015 |

---

## 4. Task Execution, Interaction, Evaluation, Experiment

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| One Deep-Research report generation run | `hi:TaskExecution` — `hi:realizesTask` → Research Synthesis; `hi:hasMethodConcept` → "Agentic RAG Synthesis" | S1, S3 | E-005, E-010 |
| One Claim Radar run on a single claim | `hi:TaskExecution` — `hi:realizesTask` → Claim Evaluation; `hi:evaluatedBy` → Evaluation (support/contradict/mixed) | S3, S4 | E-007 |
| One Compare Experiments table generation | `hi:TaskExecution` — `hi:realizesTask` → Multi-Study Comparison; `hi:hasMethodConcept` → "Structured Tabular Extraction" | S8 | E-016 |
| One Writing Coach dialogue turn/session | `hi:TaskExecution` — `hi:realizesTask` → Argument Testing; `hi:hasInteractionEpisode` → Interaction | S7 | E-004 |
| One Reading Assistant conversational session on an article | `hi:TaskExecution` — `hi:realizesTask` → Single-Document Analysis | S8 | E-016 |
| Multi-turn natural-language conversation (researcher + LeapSpace, ~5-exchange memory) | `hi:Interaction` — `hi:hasAgentInvolved` (Researcher + AI agent); `hi:hasInteractionModalityConcept` → "Natural Language Chat"; `hi:hasInteractionIntentConcept` → "Query/Refine" | S1, S2, S3 | E-013 |
| Writing Coach "challenge" dialogue (adversarial-constructive) | `hi:Interaction` — `hi:hasInteractionIntentConcept` → "Challenge/Test" | S7 | E-004 |
| Researcher clicking the Claim Radar shield icon and reviewing category tabs | `hi:Interaction` — `hi:hasInteractionModalityConcept` → "UI Panel Review"; `hi:hasInteractionIntentConcept` → "Verify" | S3, S4 | E-007 |
| Trust Card claim-to-source alignment assessment | `hi:Evaluation` — `hi:hasMetricConcept` → "Citation Alignment" | S4, S7, S8 | E-001, E-009 |
| Claim Radar support/contradict/mixed classification run | `hi:Evaluation` — `hi:hasMetricConcept` → (Support Count, Contradict Count, Mixed Count); `hi:hasExperiment` → Experiment (retrieval scope up to 40 sources via Scopus) | S3, S4 | E-007 |
| Deep Research multi-source synthesis run | `hi:Evaluation`/`hi:Experiment` — retrieval scope up to 300 sources | S3 | E-010 |
| Pre-launch development/validation testing (300+ institutions, 64 countries) | `hi:Evaluation` — `hi:hasExperiment` → Experiment "Pre-Launch User Validation" | Cross-cutting | E-005 |
| Hallucination/bias evaluation checks (Inferred, by analogy to Scopus AI) | `hi:Evaluation` *(Inferred applicability to LeapSpace — Medium confidence)* | Cross-cutting | E-012 |

---

## 5. Context, Constraint, Phenomenon

| Extracted concept | HI mapping | Scenario(s) | Evidence |
|---|---|---|---|
| Rapidly growing publication volume (5.14M+ articles/year) | `hi:Context` — `hi:hasContextConcept` → "Publication Volume Growth" | S1 | E-010 |
| Rare-disease / evidence-sparse research domain | `hi:Context` — `hi:hasContextConcept` → "Evidence-Sparse Domain" | S3 | E-006 |
| Multidisciplinary research spanning 330+ disciplines | `hi:Context` — `hi:hasContextConcept` → "Cross-Disciplinary Research" | S5 | E-010 |
| Corporate IP protection requirement | `hi:Context` — `hi:hasConstraintConcept` → "IP Protection" | S8 | E-011 |
| Biopharmaceutical regulatory compliance | `hi:Context` — `hi:hasConstraintConcept` → "Regulatory Compliance" | S8 | E-003 |
| GDPR/CCPA data-protection obligations | `hi:Context` — `hi:hasConstraintConcept` → "Data Protection Law" | Cross-cutting | E-015 |
| ISO 27001-aligned security framework | `hi:Context` — `hi:hasContextConcept` → "Enterprise Security Standard" | Cross-cutting | E-008 |
| Publisher-neutral content governance | `hi:Context` — `hi:hasConstraintConcept` → "Publisher Neutrality" | Cross-cutting | E-008, E-009 |
| AI-trust gap / hallucination risk (general researcher concern named as a design driver) | `hi:Context` `hi:hasPhenomenonConcept` → "AI Trust Gap" | S4 (cross-cutting) | E-001 |
| Information overload | `hi:Context` `hi:hasPhenomenonConcept` → "Information Overload" | S1 (cross-cutting) | E-001 |
| Time scarcity | `hi:Context` `hi:hasPhenomenonConcept` → "Time Scarcity" | Cross-cutting | E-001 |
| Evidence contradiction emergence across the literature | `hi:Context` `hi:hasPhenomenonConcept` → "Evidentiary Contradiction" | S3, S4 | E-007, E-010 |

---

## 6. CARE Framework Dimension Mapping

The HI Ontology does not encode CARE as a formal class, but the RAS (Section 18/17) requires every scenario to be checked against it. CARE dimensions are mapped onto existing `hi:` properties as follows:

| CARE Dimension | HI Ontology anchor | Representative evidence |
|---|---|---|
| **Collaborative** — human and AI agents share tasks/goals | `hi:HITeam` (`hi:hasMember` on both `hi:HumanAgent` and `hi:ArtificialAgent`); `hi:Interaction` (Writing Coach "challenge" dialogue, multi-turn chat) | E-004, E-013; explicit design statement "reinforce — not replace — human research judgment" (E-008) |
| **Adaptive** — system learns/personalises over time | `hi:Task` "Adaptive Explanation" (response tailored to experience level); conversational memory window | E-010, E-013 |
| **Responsible** — fairness, accountability, transparency | `hi:Capability` "Data Protection"; formal Responsible AI Principles (5 named principles); publisher-neutral ranking; Advisory Board governance | E-008, E-009, E-011, E-014, E-015 |
| **Explainable** — decisions are interpretable | `hi:Capability` "Passage Attribution"; Trust Cards; "real-time visibility into the steps used to generate an answer" | E-001, E-007, E-009 |

---

## 7. Summary table — Concept → Ontology Class (illustrative, per RAS Section 16 File 6 example format)

```
LeapSpace                                       → hi:UseCase
Academic Researcher                             → hi:HumanAgent
Corporate R&D Scientist                         → hi:HumanAgent
Deep Research engine                            → hi:ArtificialAgent
Claim Radar                                     → hi:ArtificialAgent
Trust Card generator                            → hi:ArtificialAgent
Synthesize scattered evidence and find gaps     → hi:Goal
Run Claim Radar on a claim                      → hi:Task
Claim classification (support/contradict/mixed) → hi:Capability
One Claim Radar run on a specific claim         → hi:TaskExecution
Researcher reviewing Claim Radar panel          → hi:Interaction
Rare-disease / evidence-sparse research domain  → hi:Context
Trust Card claim-to-source alignment check      → hi:Evaluation
Advisory Board Chair (Prof. Jörg-Rüdiger Sack)  → hi:HumanAgent
EU/US data-protection law (GDPR/CCPA)           → hint:Constraint concept (via hi:hasConstraintConcept)
Passage Attribution                             → hint:Capability concept (via hi:hasCapabilityConcept)
```

No RDF triples, SKOS concept schemes, or SHACL shapes are produced in this document — mappings are documented in natural-language/table form only, per RAS Section 5 and Section 16 (File 6) instructions.
