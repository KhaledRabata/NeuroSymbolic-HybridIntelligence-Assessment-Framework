# Research Acquisition Specification — LeapSpace by Elsevier

**Phase:** Domain Knowledge Acquisition and Structured System Analysis (Phase 1 of the thesis pipeline)
**Target Use Case:** LeapSpace (Elsevier)
**RAS Version:** 1.0
**Date completed:** 2026-08-24

---

## Scope

This package is the knowledge-acquisition deliverable for a Master's thesis investigating how neuro-symbolic AI can assess and improve the Hybrid Intelligence (HI) quality of existing company AI systems, using LeapSpace (Elsevier's AI-assisted research workspace) as the target system. It does **not** implement any part of the downstream pipeline (no RDF triples, no Knowledge Graph, no SHACL shapes, no gap analysis, no recommendations, no LLM extraction prompts, no software). It contains only collected, organised, evidence-traceable domain knowledge, structured so that Phase 2 (Knowledge Graph construction and ontology mapping) can proceed without substantial additional domain research.

LeapSpace is a research-grade AI workspace for academic and corporate researchers, combining a large scholarly-literature corpus (Scopus abstracts plus Elsevier and partner-publisher full text) with a multi-model AI backend (described by the vendor as combining agentic AI, generative AI, reasoning engines, and retrieval-augmented generation) and two named trust/transparency mechanisms — Trust Cards and Claim Radar. All eight scenarios in this package are scoped strictly to LeapSpace's own documented features (Writing Coach, Trust Cards, Claim Radar, Deep Research, Reading Assistant, Compare Experiments, Funding Discovery, Author Search), not to Elsevier's broader AI product portfolio (Scopus AI, ScienceDirect AI, Mendeley AI), except where those related products are used explicitly as labelled background/Inferred evidence for LeapSpace's own likely architecture.

## Methodology

Research followed the RAS's mandated 14-step iterative protocol (identify missing knowledge → search official sources → engineering docs → whitepapers → research papers → conference/demo material → compare findings → remove contradictions → normalise terminology → map to ontology concepts → identify missing concepts → repeat until saturation), applied across seven research rounds (see `research_log.md` for the full chronology).

Source priority followed RAS Section 9 as strictly as the target system's documentation footprint allowed. LeapSpace reached institutional general availability on **January 21, 2026** — roughly seven months before this research was conducted — which means, unlike a mature enterprise product, its evidentiary base consists almost entirely of tier-1 official vendor documentation (product pages, press releases, formal policy documents, support-center pages) and tier-9 trade press, with essentially no tier-6–8 material (peer-reviewed papers, conference talks, independent whitepapers) yet in existence. This is documented honestly as a structural finding (see `knowledge_gaps.md`, GAP-05) rather than concealed or papered over with weaker sources presented as stronger than they are. Where a related, more mature Elsevier product (Scopus AI) offered plausible architectural background, it was used only as explicitly labelled Inferred evidence, never presented as a direct, Observed description of LeapSpace's own internals.

Every extracted fact is labelled Observed (explicitly documented in a cited source) or Inferred (reasonably derived, with stated reasoning, supporting evidence, and confidence level), per RAS Sections 11–12. No scenario was constructed on speculation alone: each of the eight scenarios in `scenarios.md` is grounded in at least one, and typically several, official vendor sources. One factual discrepancy between two official sources (the size of the funding-opportunities database: "36,000+" vs. "45,000") was identified during the "remove contradictions" step and is reported transparently rather than silently resolved — see `knowledge_gaps.md`, GAP-07.

## Completion Status

All seven required deliverables are complete:

| # | File | Status |
|---|---|---|
| 1 | `research_log.md` | Complete — 7 research rounds, 20+ searches/fetches logged with objective, terms, sources visited/accepted/rejected, extraction, ontology concepts, scenarios supported, remaining unknowns, plus a saturation assessment |
| 2 | `README.md` | Complete (this file) |
| 3 | `sources.md` | Complete — 17 accepted sources (E-001–E-017) with type, quality assessment, relevance, and ontology-concept support; 5 explicitly rejected/down-weighted sources with reasons |
| 4 | `scenarios.md` | Complete — 8 standardised HI scenarios, each with all 18 required fields, Evidence IDs, and explicit Observed/Inferred labelling throughout |
| 5 | `extractionsheet.csv` | Complete — exactly 8 scenario rows (validated programmatically), 18 columns in the exact specified order |
| 6 | `ontology_mapping.md` | Complete — every extracted concept mapped to `hi:` classes/properties from the supplied `hiontology.ttl`, plus a CARE-framework mapping table; documentation only, no RDF/triples produced |
| 7 | `knowledge_gaps.md` | Complete — 7 documented gaps (GAP-01–GAP-07) with missing information, searches performed, sources consulted, reason unresolved, and whether modelling assumptions will later be needed; gaps are recorded, not filled |

### Completeness checklist (RAS Section 17)

- [x] Human Agents — 12 distinct roles identified across scenarios, including two named individuals (Prof. Jörg-Rüdiger Sack, Advisory Board Chair; Cara O'Neill MD, Cure Sanfilippo Foundation) and one named corporate persona (Samantha Intriligator, Regeneron Pharmaceuticals) — see `ontology_mapping.md` §2
- [x] Artificial Agents — 12 distinct components identified (Trust Card generator, Claim Radar, Deep Research engine, Writing Coach, Reading Assistant, Compare Experiments, Author Search, hybrid search engine, Find Funding engine, multi-model backend, foundation LLM)
- [x] Goals — identified per scenario in `scenarios.md`
- [x] Tasks — 20+ distinct tasks identified in `ontology_mapping.md` §3
- [x] Capabilities — 12 distinct capabilities identified
- [x] Contexts — academic, corporate/regulated, rare-disease/evidence-sparse, and cross-disciplinary contexts identified, plus formal governance/regulatory contexts (GDPR/CCPA, ISO 27001)
- [x] Inputs / Outputs — documented per scenario
- [x] Interactions — documented per scenario, mapped to `hi:Interaction`'s ≥2-agent cardinality restriction
- [x] Decision Points — documented per scenario, with several explicitly flagged Inferred where no source narrates the decision moment directly
- [x] Feedback Loops — documented per scenario; two scenarios (Funding Discovery, Author/Collaborator Search) honestly record "not explicitly described" rather than inventing a mechanism
- [x] Evaluation Metrics — Trust Card citation-alignment, Claim Radar support/contradict/mixed classification, source-count scope (40/300), pre-launch validation scale (300+ institutions, 64 countries)
- [x] Explainability — Trust Cards (passage-level citation), reasoning-step visibility, Claim Radar category breakdown
- [x] Trust — the platform's central design theme; Trust Cards, Claim Radar, mandatory-citation guarantee, publisher-neutral ranking
- [x] Fairness — publisher-neutrality mechanism (no discipline/publisher weighting in ranking), bias-prevention as a named Responsible AI Principle
- [x] Accountability — named governance roles (Scopus CSAB Chair, independent AI Advisory Board), Responsible AI Principle 4 ("human accountability")
- [x] CARE principles — explicit mapping table in `ontology_mapping.md` §6
- [x] Evidence for every extracted concept — Evidence IDs traced throughout all files
- [x] Confidence scores — High/Medium/Medium-High assigned per scenario and per uncertain claim
- [x] Traceability — consistent E-0xx Evidence ID scheme across all seven files

### Known limitations (see `knowledge_gaps.md` for full detail)

This package differs structurally from a knowledge-acquisition package for a mature, years-old enterprise product: LeapSpace's January 2026 launch means the evidentiary base is vendor-source-heavy by necessity rather than by research shortcoming, with no independent peer-reviewed or conference literature yet available (GAP-05), and one promising independent trade-press critique could not be retrieved due to an access block (GAP-03, HTTP 403). Two feature-level implementation details (the exact Claim Radar classification algorithm, and the Author Search ranking mechanism) are Observed only at the input/output behavioral level, not the internal-method level (GAP-02, GAP-04). None of these gaps block Phase 2, but all are flagged for a human researcher to revisit — particularly GAP-03 and GAP-06 (the LeapSpace Use Cases & Prompts Guide PDF), both of which a human with direct browser access could likely close quickly.

## Search Strategy Summary

Seven research rounds were run, each opening with a clear objective and closing with a saturation check against newly discovered agents, tasks, goals, capabilities, contexts, interactions, and metrics (see `research_log.md` for full detail):

1. Product identification and official overview (confirming what LeapSpace is, since the target system was supplied only as a name)
2. Full extraction of the three richest official product/launch pages
3. Pricing/subscription detail and launch-press corroboration (including the first named external testimonial)
4. Feature mechanics: Claim Radar, Trust & Security, differentiation, and governance-body identification
5. Fully worked use cases ("Six Ways LeapSpace...") and the corporate/industry segment
6. Interaction mechanics, formal Responsible AI policy, and data-privacy technical detail
7. Reading Assistant, Compare Experiments, and an (unsuccessful) attempt to locate independent critical perspective

Saturation was judged reached when three consecutive rounds (5–7) stopped surfacing new feature components, role archetypes, or trust/evaluation mechanisms — see the Saturation Assessment at the end of `research_log.md` for the full reasoning, including an explicit acknowledgment that the product's youth (not a research-effort shortfall) is the reason tiers 6–8 of the RAS source-priority list remain thin.

## How to use this package in Phase 2

`scenarios.md` and `extractionsheet.csv` are the primary inputs for Knowledge Graph construction. `ontology_mapping.md` gives the class/property assignments to use when instantiating `hi:` and `hint:` individuals. `sources.md` and the Evidence IDs threaded through every file provide the audit trail required to justify each triple that will eventually be created. `knowledge_gaps.md` should be consulted before finalizing SHACL shapes that depend on the precise Claim Radar classification method (GAP-02), the Author Search ranking mechanism (GAP-04), or a fixed numeric value for the funding-database size (GAP-07) — all three should be treated as open or time-varying rather than fixed constants until directly confirmed.
