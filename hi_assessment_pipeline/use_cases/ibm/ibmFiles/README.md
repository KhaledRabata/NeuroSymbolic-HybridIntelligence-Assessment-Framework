# Research Acquisition Specification — IBM watsonx.governance

**Phase:** Domain Knowledge Acquisition and Structured System Analysis (Phase 1 of the thesis pipeline)
**Target Use Case:** IBM watsonx.governance
**RAS Version:** 1.0
**Date completed:** 2026-08-24

---

## Scope

This package is the knowledge-acquisition deliverable for a Master's thesis investigating how neuro-symbolic AI can assess and improve the Hybrid Intelligence (HI) quality of existing company AI systems, using IBM watsonx.governance as the target system. It does **not** implement any part of the downstream pipeline (no RDF triples, no Knowledge Graph, no SHACL shapes, no gap analysis, no recommendations, no LLM extraction prompts, no software). It contains only collected, organised, evidence-traceable domain knowledge, structured so that Phase 2 (Knowledge Graph construction and ontology mapping) can proceed without substantial additional domain research.

IBM watsonx.governance was treated as a single target system with eight internally distinct workflows/use cases, because the product itself is composed of multiple sub-capabilities (OpenPages, Watson OpenScale, AI FactSheets, the Governance console, the Governed Agentic Catalog, Experimentation Studio, and multi-cloud/third-party model integration) that IBM documentation and engineering material consistently present as one governed platform. All eight scenarios are scoped strictly to watsonx.governance and its documented sub-components — not to the broader watsonx.ai or watsonx Orchestrate platforms, except where those platforms are explicitly governed *by* watsonx.governance (e.g., watsonx Orchestrate agent observability, Scenario 5).

## Methodology

Research followed the RAS's mandated 14-step iterative protocol (identify missing knowledge → search official sources → engineering docs → whitepapers → research papers → conference/demo material → compare findings → remove contradictions → normalise terminology → map to ontology concepts → identify missing concepts → repeat until saturation), applied across seven research rounds (see `research_log.md` for the full chronology).

Source priority followed RAS Section 9 strictly: official IBM vendor documentation and product pages were treated as primary; IBM-affiliated engineering blogs (the "IBM Data Science in Practice" and "Trusted AI" Medium publications, and IBM's own community.ibm.com blog) were treated as secondary-but-high-quality, since several are authored by IBM Distinguished Engineers and offering managers and are technically precise and internally consistent with official material; independent community technical blogs and IBM Research academic publications were used to corroborate or fill gaps; marketing-oriented consulting-partner blogs, crowd-review sites, and unverifiable secondary summaries (e.g., student study-note aggregators) were explicitly excluded from evidence, even when they appeared in search results (see `sources.md`, Section B, for the full rejection list with reasons).

Every extracted fact is labelled Observed (explicitly documented in a cited source) or Inferred (reasonably derived, with stated reasoning, supporting evidence, and confidence level), per RAS Sections 11–12. No scenario was constructed on speculation alone: each of the eight scenarios in `scenarios.md` is grounded in at least one primary or high-quality secondary source, and most are corroborated by two or more independent sources. One candidate scenario (a fairness claim associated with the US Open case study) was deliberately **excluded** after investigation revealed it likely refers to a different IBM AI capability, not a watsonx.governance-specific workflow — see `knowledge_gaps.md`, GAP-06.

## Completion Status

All seven required deliverables are complete:

| # | File | Status |
|---|---|---|
| 1 | `research_log.md` | Complete — 7 research rounds, 25+ searches/fetches logged with objective, terms, sources visited/accepted/rejected, extraction, ontology concepts, scenarios supported, remaining unknowns, plus a saturation assessment |
| 2 | `README.md` | Complete (this file) |
| 3 | `sources.md` | Complete — 22 accepted sources (E-001–E-022, incl. sub-entries) with type, quality assessment, relevance, and ontology-concept support; 13 explicitly rejected sources with reasons |
| 4 | `scenarios.md` | Complete — 8 standardised HI scenarios, each with all 18 required fields, Evidence IDs, and explicit Observed/Inferred labelling throughout |
| 5 | `extractionsheet.csv` | Complete — exactly 8 scenario rows (validated programmatically), 18 columns in the exact specified order |
| 6 | `ontology_mapping.md` | Complete — every extracted concept mapped to `hi:` classes/properties from the supplied `hiontology.ttl`, plus a CARE-framework mapping table; documentation only, no RDF/triples produced |
| 7 | `knowledge_gaps.md` | Complete — 7 documented gaps (GAP-01–GAP-07) with missing information, searches performed, sources consulted, reason unresolved, and whether modelling assumptions will later be needed; gaps are recorded, not filled |

### Completeness checklist (RAS Section 17)

- [x] Human Agents — 20+ distinct roles identified across scenarios (see `ontology_mapping.md` §2)
- [x] Artificial Agents — 15+ distinct components identified (OpenScale, OpenPages, AI FactSheets, AutoAI, SHAP/LIME engine, IRIS, Governed Agentic Catalog, Experimentation Studio, detached prompt templates, custom ML provider proxies, red-teaming evaluator, LLM-as-judge, slate evaluation models, embedded governance assistant, ibm-watsonx-gov SDK)
- [x] Goals — identified per scenario in `scenarios.md`
- [x] Tasks — 30+ distinct tasks identified in `ontology_mapping.md` §3
- [x] Capabilities — 15 distinct capabilities identified
- [x] Contexts — regulatory (EU AI Act, GDPR, NIST AI RMF, ISO 42001, banking/insurance MRM), technical (multi-cloud, agentic orchestration), and business (high-volume recruitment) contexts identified
- [x] Inputs / Outputs — documented per scenario
- [x] Interactions — documented per scenario, mapped to `hi:Interaction`'s ≥2-agent cardinality restriction
- [x] Decision Points — documented per scenario
- [x] Feedback Loops — documented per scenario, with Inferred loops explicitly flagged where the closure mechanism was not verbatim documented
- [x] Evaluation Metrics — 40+ named metrics collected across predictive, GenAI, RAG, security, and agentic dimensions
- [x] Explainability — SHAP/LIME (local & global explanations, stability metric), RAG source attribution
- [x] Trust — AI FactSheets / Supplier's Declarations of Conformity, academically grounded (E-009b)
- [x] Fairness — disparate impact, statistical parity difference, bias monitoring across 4 scenarios
- [x] Accountability — OpenPages audit trails, compliance dashboards, Model Risk Officer role
- [x] CARE principles — explicit mapping table in `ontology_mapping.md` §6
- [x] Evidence for every extracted concept — Evidence IDs traced throughout all files
- [x] Confidence scores — High/Medium/Medium-High assigned per scenario and per uncertain claim
- [x] Traceability — consistent E-0xx Evidence ID scheme across all seven files

### Known limitations (see `knowledge_gaps.md` for full detail)

Two specific gaps were not fully closed despite dedicated search effort: (1) the primary official Model Risk Governance workflow documentation could not be retrieved due to JavaScript-rendering/HTTP-error access limitations across three separate domains, so Scenario 8 relies on strong secondary corroboration rather than the primary source directly; (2) a small number of human role titles in runtime/regulatory-approval contexts (agentic AI production approval; financial-services MRM sign-off) are not explicitly named in any retrieved source and are modelled as Inferred, using the closest documented analogous role. Neither gap blocks Phase 2, but both are flagged for a human researcher to verify against IBM's live, authenticated documentation before final Knowledge Graph population.

## Search Strategy Summary

Seven research rounds were run, each opening with a clear objective and closing with a saturation check against newly discovered agents, tasks, goals, capabilities, contexts, interactions, and metrics (see `research_log.md` for full detail):

1. Product scope and official overview
2. Architecture (OpenPages / OpenScale / AI FactSheets) and approval-workflow pattern
3. Metrics, fairness, explainability, and the AI FactSheets research paper lineage
4. RAG metrics, EU AI Act assessment mechanics, third-party/multi-cloud governance, adversarial prompt security
5. RAG evaluation workflow detail, virtual assistant monitoring, and a concrete recruitment case study
6. Agent runtime observability and a background scan of adjacent neuro-symbolic/knowledge-graph literature
7. Explainability workflow detail, financial-services MRM context, and demo/conference material attempts

Saturation was judged reached when three consecutive rounds (5–7) stopped surfacing new agent types, role archetypes, or metric families — see the Saturation Assessment at the end of `research_log.md` for the full reasoning.

## How to use this package in Phase 2

`scenarios.md` and `extractionsheet.csv` are the primary inputs for Knowledge Graph construction. `ontology_mapping.md` gives the class/property assignments to use when instantiating `hi:` and `hint:` individuals. `sources.md` and the Evidence IDs threaded through every file provide the audit trail required to justify each triple that will eventually be created. `knowledge_gaps.md` should be consulted before finalizing SHACL shapes for Scenario 8 and for any shape that depends on exact GenAI metric formulas (GAP-04) or the specific MRG workflow structure (GAP-01).
