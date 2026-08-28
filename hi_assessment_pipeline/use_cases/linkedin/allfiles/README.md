# README — Knowledge Acquisition Package
## Neuro-Symbolic AI for Assessing Hybrid Intelligence Systems
### Target System: LinkedIn Recruiter + Hiring Assistant
### Phase: Domain Knowledge Acquisition (Phase 1 of N)

---

## 1. Scope

This package contains all knowledge acquisition artefacts produced during Phase 1 of the thesis project:

> **"Neuro-Symbolic AI for Assessing and Improving Hybrid Intelligence Systems"**
> Master's Thesis in Artificial Intelligence
> Target Use Case: LinkedIn Recruiter / LinkedIn Hiring Assistant

The package covers the following domains:

- LinkedIn Recruiter product architecture and feature set
- LinkedIn Hiring Assistant agentic AI system
- Human and artificial agent roles within the system
- Hybrid Intelligence characteristics of the system
- Mapping to the CARE Hybrid Intelligence framework
- Candidate, recruiter, and hiring manager workflows
- Fairness, explainability, accountability, and trust mechanisms
- Identified knowledge gaps

---

## 2. Package Contents

| File | Description |
|------|-------------|
| `README.md` | This file. Scope, methodology, completion status. |
| `research_log.md` | Chronological log of all research steps performed. |
| `sources.md` | Full inventory of all sources consulted, with quality and relevance assessments. |
| `scenarios.md` | Standardised Hybrid Intelligence scenarios with full ontology-oriented fields. |
| `extractionsheet.csv` | Machine-readable extraction table; one row per scenario. |
| `ontology_mapping.md` | Mapping of all extracted concepts to Hybrid Intelligence ontology concepts. |
| `knowledge_gaps.md` | Documented gaps where information could not be found. |

---

## 3. Methodology

This knowledge acquisition followed the iterative research protocol specified in the RAS (Research Acquisition Specification v1.0):

1. Identified missing knowledge categories (human agents, AI agents, tasks, goals, capabilities, contexts, interactions, evaluation metrics, HI characteristics).
2. Searched official LinkedIn sources first (LinkedIn product pages, Help Centre, AI Transparency documentation, Engineering Blog).
3. Searched engineering and technical documentation (LinkedIn Engineering Blog, ZenML LLMOps Database, InfoQ, QCon presentations).
4. Searched research papers (ACM SIGKDD, SIGIR, arXiv, Semantic Scholar).
5. Searched Hybrid Intelligence literature (Akata et al. 2020, taxonomy papers, CARE framework literature).
6. Compared findings, removed contradictions, normalised terminology.
7. Mapped concepts to Hybrid Intelligence ontology categories.
8. Identified remaining gaps.
9. Repeated until saturation.

All facts are labelled **Observed** (explicitly documented) or **Inferred** (reasonably derived), with confidence ratings (High / Medium / Low) and Evidence IDs traceable to `sources.md`.

---

## 4. Search Strategy

Sources were consulted in strict priority order per the RAS:

1. Official LinkedIn documentation (`business.linkedin.com`, `linkedin.com/help`)
2. LinkedIn AI Transparency documentation (`business.linkedin.com/hire/ai-transparency`)
3. LinkedIn Engineering Blog (`engineering.linkedin.com`)
4. LinkedIn Talent Blog (`linkedin.com/business/talent/blog`)
5. Official LinkedIn news releases (`news.linkedin.com`)
6. Conference presentations (QCon London 2025, ACM KDD, ACM SIGIR)
7. Peer-reviewed arXiv preprints and published papers
8. High-quality technical summaries (InfoQ, ZenML LLMOps, ByteByteGo)

Sources assessed as blogs, opinion articles, or marketing material without technical substance were rejected unless no better evidence was available.

---

## 5. Completion Status

| Checklist Category | Status |
|---|---|
| Human Agents | ✅ Complete |
| Artificial Agents | ✅ Complete |
| Goals | ✅ Complete |
| Tasks (Human) | ✅ Complete |
| Tasks (AI) | ✅ Complete |
| Capabilities | ✅ Complete |
| Contexts | ✅ Complete |
| Inputs | ✅ Complete |
| Outputs | ✅ Complete |
| Interactions | ✅ Complete |
| Decision Points | ✅ Complete |
| Feedback Loops | ✅ Complete |
| Evaluation Metrics | ✅ Complete |
| Explainability | ✅ Complete |
| Trust | ✅ Complete |
| Fairness | ✅ Complete |
| Accountability | ✅ Complete |
| CARE Principles | ✅ Complete |
| Evidence for every concept | ✅ Complete |
| Confidence scores | ✅ Complete |
| Traceability | ✅ Complete |
| Remaining unknowns documented | ✅ Complete — see `knowledge_gaps.md` |

**Overall Phase 1 Status: COMPLETE**

The collected knowledge is assessed as sufficient to proceed to Knowledge Graph construction and ontology mapping (Phase 2) without requiring substantial additional domain research. Remaining gaps are documented and assessed as either inferable or minor.

---

## 6. Key Findings Summary

LinkedIn Recruiter + Hiring Assistant is a Hybrid Intelligence system in which human recruiters and an agentic AI system collaborate toward the shared goal of identifying and engaging qualified candidates. The system exhibits all four CARE properties:

- **Collaborative**: Recruiter and Hiring Assistant share tasks across the hiring pipeline; the system is explicitly designed so that humans remain in control of all final hiring decisions.
- **Adaptive**: The system learns from recruiter interaction history (view, contact, archive actions); a Hierarchical Long-Term Semantic Memory (HLTM) module personalises recommendations across sessions.
- **Responsible**: LinkedIn operates a cross-functional Responsible AI team, applies the LinkedIn Fairness Toolkit (LiFT), conducts per-model fairness audits, and complies with GDPR, EU AI Act, and relevant US regulations (e.g., NYC Local Law 144).
- **Explainable**: The system surfaces candidate qualification match/gap indicators, provides evidence-cited candidate summaries, and publishes AI transparency documentation including data flow diagrams and whitepapers.

The system does **not** make autonomous hiring decisions; human judgment is required at all critical decision points.

---

## 7. Version

| Field | Value |
|---|---|
| Version | 1.1 |
| Date produced | 2026-06-28 |
| Last revised | 2026-06-28 |
| RAS version | 1.0 |
| Target system | LinkedIn Recruiter + Hiring Assistant |
| Phase | Domain Knowledge Acquisition |

**v1.1 Change:** `ontology_mapping.md` fully revised to align with the formal Hybrid Intelligence Ontology diagram (hi: and hint: namespaces). The initial version (v1.0) used informal ontology terms. Version 1.1 maps all concepts to the exact `hi:` classes and `hint:` thesaurus concepts shown in the diagram, including `hi:HITeam`, `hi:UseCase`, `hi:TaskExecution`, `hi:Evaluation`, `hi:Experiment`, and all object properties (`hi:requiresTask`, `hi:isAssignedToTask`, `hi:towardsGoal`, `hi:realizedBy`, `hi:evaluatedBy`, etc.). Research log updated with Session 8 documenting this alignment.
