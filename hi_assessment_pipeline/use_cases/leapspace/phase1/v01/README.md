# Knowledge Acquisition Package: Elsevier LeapSpace™
## For Hybrid Intelligence Analysis via the VU Amsterdam HI Ontology v2.0.0

---

## Overview

This knowledge acquisition package documents **Elsevier LeapSpace™**, a research-grade AI-assisted workspace launched on January 21, 2026, as a candidate system for Hybrid Intelligence (HI) quality assessment. The package was produced as part of a Master's thesis research project targeting the **Leapspace** system within the **Leapspace** neuro-symbolic AI assessment pipeline, which evaluates HI system quality against the [VU Amsterdam HI Ontology v2.0.0](https://w3id.org/hi-ontology#).

LeapSpace represents a substantive HI system in which human researchers and multiple AI agents collaborate across the full scientific research lifecycle—from literature discovery and claim verification to research writing, funding identification, and deep synthesis. Its explicit design philosophy of keeping researchers "in the driver's seat" while providing AI-powered capabilities makes it a strong candidate for HI quality analysis.

---

## Target Use Case

**System:** Elsevier LeapSpace™  
**Vendor:** Elsevier (RELX Group)  
**Domain:** Scientific research support — academic and corporate R&D  
**Target Users:** Academic researchers, corporate R&D scientists, PhD students, librarians, and research office administrators  
**Core Value Proposition:** A research-grade, AI-assisted workspace built on the world's most comprehensive collection of scientific content, combining multi-model responsible AI with trust markers, industrial-grade data privacy, and traceable, explainable outputs grounded in peer-reviewed science.

The system addresses a documented trust gap: a 2025 Elsevier survey of 3,200+ researchers across 113 countries found that while 84% use AI tools, only 22% trust them. LeapSpace was designed specifically to bridge this gap through transparency mechanisms (Trust Cards, Claim Radar), responsible AI governance, and an explicit commitment to human oversight.

---

## Scope of Research

The knowledge acquisition covers all major dimensions of the HI Ontology v2.0.0 as applied to LeapSpace, including:

- **Human Agents:** Academic researchers, corporate R&D scientists, PhD students, librarians, research office administrators, peer reviewers
- **Artificial Agents:** LeapSpace platform, RAG engine, Trust Card Generator, Claim Radar, Writing Coach, Deep Research Agent (multi-agent coordinator, query decomposition agent, retrieval agents, synthesis agent, report writer), Reading Assistant, Author Search, Funding Scout, Compare Tables component, Reference Export component, LLM providers (OpenAI/Anthropic hosted on Azure/AWS)
- **Goals:** Research acceleration, discovery improvement, trust and transparency, research integrity, critical thinking support, collaborator and funding discovery
- **Tasks:** Literature search and synthesis, claim verification, evidence assessment, research writing, argument strengthening, gap identification, pattern detection, funding discovery, collaborator discovery, article interrogation, report generation, citation management
- **Capabilities:** Natural language understanding, semantic search, retrieval-augmented generation, full-text parsing, evidence synthesis, transparency generation, citation tracing, claim analysis, multi-agent coordination, contradiction detection, publisher-neutral ranking, document comparison, and the complementary human capabilities of critical evaluation, domain expertise, and research judgment
- **Contexts:** Academic and corporate research environments, institutional and individual access models, privacy/security requirements, governance frameworks
- **Inputs and Outputs:** Per-scenario documentation covering all major workflows
- **Interaction Patterns:** Query-response exchange, Trust Card inspection, claim verification dialogue, Writing Coach conversation, suggestion approval/rejection, source verification click-through, file upload
- **Decision Points:** Search strategy selection, source evaluation, evidence sufficiency, change acceptance, argument direction, scope definition
- **Feedback Mechanisms:** Trust Cards surfacing contradictions, visible reasoning steps, conversational history, no-automatic-edit policy
- **Evaluation Metrics:** Time savings, user satisfaction, citation accuracy, evidence coverage, research design improvement, user trust
- **CARE Framework Dimensions:** Collaborative, Adaptive, Responsible, Explainable — all fully analyzed
- **Access and Equity Considerations:** Content coverage limitations (~22% of 2024 articles indexed with full text), pricing structure, concerns about access for under-resourced institutions
- **Governance:** Five Responsible AI Principles, Independent Advisory Board oversight, ISO 27001 alignment, zero-retention LLM contracts, periodic Algorithmic Impact Assessments, retracted article exclusion, publisher-neutral ranking

---

## Methodology: RAS Protocol

Knowledge acquisition followed the **Research Acquisition Specification (RAS) v1.0** protocol, comprising:

1. **Source Priority Hierarchy:** Official vendor documentation was prioritized as the primary source tier, followed by engineering and support documentation, official press releases, peer-reviewed and independent journalism (Science/AAAS), and finally industry publications.
2. **Iterative Search Protocol:** Seven structured search sessions were conducted, each with defined objectives, explicit search terms, source acceptance/rejection criteria, and extracted ontology concepts.
3. **Saturation Criterion:** Research continued iteratively until no significant new ontology-relevant concepts (agents, goals, tasks, capabilities, contexts, interactions, decision points, feedback mechanisms, or evaluation metrics) emerged across a complete search session. Saturation was declared after Session 7.
4. **Evidence Traceability:** All factual claims were tagged with unique Evidence IDs and coded as either Observed (directly stated in a source) or Inferred (reasonably derived from context).
5. **Confidence Assessment:** High / Medium / Low confidence levels were assigned to each mapping, with justification documented.
6. **Sources Rejected with Rationale:** Three candidate systems sharing the name "Leapspace" or similar were identified and explicitly rejected: Leapspace Ltd (a dissolved UK company unrelated to AI), Leap Motion (a hand-tracking hardware company), and LEAP Legal Software (a legal practice management system).

---

## Completion Status

| Category | Status | Coverage |
|---|---|---|
| Human Agents | ✅ Complete | 6 agent types identified |
| Artificial Agents | ✅ Complete | 13 AI components documented |
| Goals | ✅ Complete | 8 primary goals documented |
| Tasks | ✅ Complete | 15 tasks documented |
| Capabilities | ✅ Complete | 16+ capabilities documented |
| Contexts | ✅ Complete | 6 contexts documented |
| Context Constraints | ✅ Complete | 5 constraints documented |
| Inputs / Outputs | ✅ Complete | Documented per scenario |
| Interaction Types | ✅ Complete | 8 interaction types documented |
| Interaction Modalities | ✅ Complete | 4 modalities documented |
| Interaction Intents | ✅ Complete | 4 intents documented |
| Decision Points | ✅ Complete | 5 decision points documented |
| Feedback Mechanisms | ✅ Complete | 4 mechanisms documented |
| Evaluation Metrics | ✅ Complete | 6 metrics documented |
| CARE Analysis | ✅ Complete | All four dimensions analyzed |
| Use Cases / Scenarios | ✅ Complete | 6 scenarios documented |
| HITeam Composition | ✅ Complete | Documented |
| Knowledge Gaps | ✅ Complete | 8 gaps documented |

---

## Search Strategy Summary

| Item | Detail |
|---|---|
| Total search sessions | 7 |
| Total queries executed | 21+ |
| Primary sources accepted | 12 (official Elsevier documentation) |
| Secondary sources accepted | 8+ (industry and press) |
| Sources explicitly rejected | 3 (unrelated systems) |
| Saturation reached | Yes — after Session 7 |

**Search sessions and focus areas:**

| Session | Focus |
|---|---|
| 1 | System identification and initial product characterisation |
| 2 | Core features: Trust Cards, Claim Radar, Writing Coach, Deep Research Mode |
| 3 | Responsible AI principles, governance, and human oversight |
| 4 | User feedback, evaluation metrics, and institutional adoption |
| 5 | Pricing, access models, limitations, and equity concerns |
| 6 | Technical architecture: multi-model AI, RAG, agentic capabilities, file handling |
| 7 | Researcher of the Future Report and contextual research motivations |

---

## Evidence Sources Consulted

### Primary Sources — Official Elsevier Documentation

| ID | Description | URL / Reference |
|---|---|---|
| S-001 | LeapSpace Official Product Page | elsevier.com/products/leapspace |
| S-002 | Press Release — LeapSpace Launch (Nov 2025) | elsevier.com/about/press-releases/elsevier-launches-leapspace |
| S-003 | LeapSpace Trust and Security Page | elsevier.com/products/leapspace/trust-and-security |
| S-004 | LeapSpace Support Center | elsevier.support/leapspace |
| S-005 | Elsevier Responsible AI Principles | elsevier.com/about/policies-and-standards/responsible-ai-principles |
| S-006 | LeapSpace Writing Coach Feature Page | elsevier.com/products/leapspace/writing-coach |
| S-007 | Press Release — Agentic Capabilities Expansion (Jun 2026) | elsevier.com/about/press-releases/elsevier-expands-leapspace-with-new-agentic-capabilities |
| S-008 | CODiE Award Announcement (Jul 2026) | elsevier.com/resources/elseviers-leapspace-wins-best-generative-ai-solution |
| S-009 | University of Virginia Adoption Case Study | elsevier.com/resources/university-of-virginia-expands-research-resources-with-leapspace |
| S-010 | Elsevier Responsible AI FAQ | elsevier.com/about/responsible-ai/ai-use-faq |
| S-011 | LeapSpace LibGuide (official user guide) | elsevier.libguides.com/LeapSpace |
| S-012 | Researcher of the Future Report | elsevier.com/insights/confidence-in-research/researcher-of-the-future |

### Secondary Sources — Independent and Industry Coverage

| ID | Description | URL / Reference |
|---|---|---|
| S-013 | Science.org / AAAS independent critical analysis | science.org — "Journal giant Elsevier unveiled an AI tool…" |
| S-014 | PRNewswire — LeapSpace Goes Live wire release | prnewswire.com — LeapSpace Goes Live (Jan 2026) |
| S-015 | Clinical Lab industry article | clinicallab.com — Elsevier launches LeapSpace |
| S-016 | Research Information industry article | researchinformation.info — Elsevier launches research-grade AI workspace |
| S-017 | KnowledgeSpeak industry news | knowledgespeak.com — Elsevier debuts LeapSpace |
| S-018 | RD World Online — R&D industry analysis with demo observations | rdworldonline.com — LeapSpace Writing Coach and Claim Radar |
| S-019 | Creati.ai — AI industry technical analysis | creati.ai — Elsevier LeapSpace AI tool |
| S-020 | UVA AI Newsletter — practitioner perspective and alternative comparisons | aiatuva.substack.com — Announcing LeapSpace for UVA |

### Sources Explicitly Rejected

| Candidate | Reason for Rejection |
|---|---|
| Leapspace Ltd (UK Companies House) | Dissolved UK company; unrelated to AI or research |
| Leap Motion | Hand-tracking hardware company; unrelated |
| LEAP Legal Software | Legal practice management system; unrelated |

---

## Output File Inventory

This package comprises seven output files:

| File | Description |
|---|---|
| **README.md** | This file — package overview, scope, methodology, completion status, search strategy, sources, and file inventory |
| **research_log.md** | Detailed log of all seven search sessions: objectives, search terms, sources accepted/rejected, information extracted, and ontology concepts discovered per session, plus saturation assessment |
| **sources.md** | Complete annotated source inventory with quality assessments (High / Medium), relevance descriptions, supported ontology concepts, and access dates for all 20 sources |
| **scenarios.md** | Six standardised HI scenario documents covering: (1) Literature Review Acceleration, (2) Claim Verification and Evidence Assessment, (3) Research Writing Assistance, (4) Funding and Collaborator Discovery, (5) Deep Research Report Generation, (6) Article Reading and Comprehension — each with full agent, goal, task, capability, context, input, output, interaction, decision point, feedback, and CARE documentation |
| **extractionsheet.csv** | Tabular extraction of all scenario data in CSV format, one row per scenario, covering all ontology-relevant fields for direct ingestion into knowledge graph construction pipelines |
| **ontology_mapping.md** | Explicit concept-by-concept mappings from LeapSpace artefacts to HI Ontology v2.0.0 classes and properties (namespace `https://w3id.org/hi-ontology#`), covering: HumanAgent, ArtificialAgent, Goal, Task, Capability, Context, Context Constraints, Interaction, Interaction Modalities, Interaction Intents, Evaluation, UseCase, HITeam, and CARE framework alignment |
| **knowledge_gaps.md** | Documentation of eight identified knowledge gaps (specific LLM model versions, algorithmic assessment results, discipline-level content coverage, processing time metrics, Advisory Board membership, error rate statistics, user telemetry, and API specifications), including searches performed, reasons information was not found, severity assessment, and whether modelling assumptions will be required |

---

## Key Findings Summary

1. **Strong HI Design:** LeapSpace explicitly embodies core HI principles — human oversight is foregrounded throughout all workflows, AI capabilities augment rather than replace researcher judgment, and the "driver's seat" metaphor is used consistently in official documentation.

2. **Trust-Centric Architecture:** The system directly addresses the documented trust gap (only 22% of researchers trust current AI tools) through Trust Cards, Claim Radar, visible reasoning steps, and traceable citations.

3. **Comprehensive CARE Alignment:**
   - **Collaborative:** Researcher and AI share task execution across the full research workflow via a defined HITeam structure
   - **Adaptive:** Multi-model AI selects models by task type; daily content updates; Deep Research mode adapts to query complexity
   - **Responsible:** Five published Responsible AI Principles; Independent Advisory Board; periodic Algorithmic Impact Assessments; ISO 27001 alignment; zero-retention LLM contracts; retracted article exclusion
   - **Explainable:** Trust Cards, Claim Radar, linked citations, and visible planning steps provide multi-layered explainability at both source and reasoning levels

4. **Access Equity Concern:** An independently identified limitation is that full-text coverage covers approximately 22% of 2024 articles, and pricing structures may disadvantage under-resourced institutions — a relevant consideration for the CARE Responsible dimension.

5. **External Validation:** LeapSpace won the Best Generative AI Solution at the 2026 CODiE Awards and has achieved adoption at institutions including the University of Virginia, with reported user outcomes of 97% reporting time savings and more than half saving over 50% of their research time.

---

## Version History

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-08-03 | Initial comprehensive acquisition — saturation achieved after 7 sessions |