# Research Acquisition Package — Elsevier LeapSpace
Neuro-Symbolic AI for Assessing and Improving Hybrid Intelligence Systems | Master's Thesis Support
Research Acquisition Specification (RAS) v1.0 | Phase: Domain Knowledge Acquisition and Structured System Analysis
Compiled: 2026-08-24

---

## 1. Scope

This package is the output of the **knowledge-acquisition phase only**, as strictly bounded by the RAS (§3, §4, §5). It does **not** contain RDF triples, a Knowledge Graph, SHACL shapes, SHACL validation results, gap-analysis conclusions, recommendations, LLM extraction prompts, or software. It contains only collected, organized, evidence-traceable domain knowledge about **Elsevier LeapSpace**, structured so that a later phase can build a Knowledge Graph, map it to the supplied Hybrid Intelligence (HI) Ontology (`hi:`, v2.0.0) and HINT thesaurus (`hint:`), and run SHACL validation without needing substantial additional domain research (RAS §19.8).

**Target Use Case:** Elsevier LeapSpace — a "research-grade AI-assisted workspace" combining publisher-neutral scholarly content with agentic AI, generative AI, reasoning engines, and retrieval-augmented generation, aimed at university researchers and corporate R&D teams.

**Ontology used as the acquisition frame:** The supplied `hiontology.ttl` (VU Amsterdam KAI Group, v2.0.0), whose core classes are `hi:HITeam`, `hi:UseCase`, `hi:Agent`/`hi:HumanAgent`/`hi:ArtificialAgent`, `hi:Goal`, `hi:Task`, `hi:Capability`, `hi:TaskExecution`, `hi:Interaction`, `hi:Context`, `hi:Evaluation`, and `hi:Experiment`, plus the `hint:` thesaurus concept classes referenced by the ontology's object properties. Every extracted fact in this package was actively steered toward these categories (RAS §10).

---

## 2. Methodology

The work followed the exact 14-step iterative protocol specified in RAS §8: identify missing knowledge → search official sources → engineering documentation → whitepapers → research papers → conference presentations → product demos → compare findings → remove contradictions → normalize terminology → map to ontology concepts → identify missing concepts → search again → repeat until saturation.

Concretely, this meant:

1. **Web search**, always followed by **direct page fetch and full-text extraction** of the most promising results, rather than relying on search-snippet text alone.
2. **Source prioritization** strictly per RAS §9: official Elsevier product pages, press releases, and policy documents first; official help/support documentation (Scopus AI support center, the LeapSpace LibGuide) and an official demo-webinar listing next; independent trade-press and technology-news coverage used both to corroborate vendor claims and — deliberately — to surface critical, non-vendor-affiliated commentary (market-concentration concerns, pricing, coverage limitations) that a vendor-only source set would have missed.
3. **Every extracted fact tagged with an Evidence ID** (`E-001`…`E-018`) carrying source title, URL, type, a verbatim short quotation, and the reason for extraction — see `sources.md`.
4. **Observed vs. Inferred labelling** applied to every fact that appears in `scenarios.md` and `ontology_mapping.md`, with reasoning and confidence attached to every Inferred item, per RAS §11–§12.
5. **Failed/inaccessible sources logged, not silently skipped** — 3 URLs returned HTTP 403 errors or `robots.txt` fetch failures across the session; each is recorded in `sources.md` §2 (Rejected/Inaccessible Sources) and cross-referenced in `knowledge_gaps.md`.

**A note on product maturity and its effect on methodology:** LeapSpace is a very recently launched product — preview access, institutional general availability, and a subsequent "agentic capabilities" expansion all occurred within the months immediately preceding this research date. This means Source Priority Tiers 6–8 (peer-reviewed research papers, conference talks, whitepapers) are **genuinely empty for LeapSpace specifically**, not under-searched — this is documented as an explicit, reasoned gap (`knowledge_gaps.md` Gap 1) rather than papered over with tangentially related general-AI literature.

---

## 3. Search Strategy

17 distinct search iterations were run (full detail in `research_log.md`), moving from broad product-overview queries to progressively narrower technical and governance-focused queries:

1. Product overview, purpose, and launch announcements
2. General-availability ("goes live") milestone and named customer testimonials
3. Corporate/industry R&D-specific product framing
4. Independent journalistic/trade-press coverage (attempted and successful variants)
5. Elsevier's enterprise-wide Responsible AI Principles policy
6. The underlying Scopus AI and ScienceDirect AI engines LeapSpace is built on
7. Official demo/webinar listing and named presenter roles
8. Additional named-role customer testimonials (Regeneron, Incyte)
9. The "research-grade AI" definitional page and content-governance chain
10. Independent hallucination/accuracy-benchmark verification (explicitly checked, found absent)
11. Pharmaceutical/biotechnology industry-specific roles and integrated databases
12. Whitepaper, conference-talk, and peer-reviewed-paper search (explicitly checked, found absent)
13. The newest "agentic capabilities" expansion announcement and Writing Coach feature detail
14. Deliberate search for critical, non-vendor-affiliated expert commentary
15. LeapSpace's dedicated trust-and-security governance page and pricing/subscription documentation

Each search's objective, terms, engine, sources visited/accepted/rejected, extracted information, discovered ontology concepts, supported scenarios, and remaining unknowns are logged in full in `research_log.md`.

---

## 4. Completion Status

### 4.1 Deliverables (RAS §16)

| # | File | Status | Notes |
|---|---|---|---|
| 1 | `research_log.md` | ✅ Complete | 17 logged search iterations + saturation assessment |
| 2 | `README.md` | ✅ Complete | This file |
| 3 | `sources.md` | ✅ Complete | 18 accepted evidence sources (E-001–E-018) + 3 rejected/inaccessible sources (R-01–R-03) + source-priority compliance summary |
| 4 | `scenarios.md` | ✅ Complete | 5 evidence-backed HI scenarios, each with all 18 required fields |
| 5 | `extractionsheet.csv` | ✅ Complete | 5 data rows (one per scenario) + header, exact column order per spec, CSV-validated (18 columns × 6 rows) |
| 6 | `ontology_mapping.md` | ✅ Complete | Concept-to-ontology mapping across all `hi:` classes/properties and representative `hint:` concept types; no RDF/triples produced; one class (`hi:Experiment`) explicitly documented as unmapped rather than force-mapped |
| 7 | `knowledge_gaps.md` | ✅ Complete | 8 documented gaps, none silently filled |

### 4.2 Completeness Checklist (RAS §17)

| Item | Status | Where documented |
|---|---|---|
| Human Agents | ✓ Identified | `ontology_mapping.md` §3, `scenarios.md` (all 5 scenarios) |
| Artificial Agents | ✓ Identified | `ontology_mapping.md` §3, `scenarios.md` (all 5 scenarios) |
| Goals | ✓ Identified | `ontology_mapping.md` §4, `scenarios.md` |
| Tasks | ✓ Identified | `ontology_mapping.md` §5, `scenarios.md` |
| Capabilities | ✓ Identified | `ontology_mapping.md` §6, `scenarios.md` |
| Contexts | ✓ Identified | `ontology_mapping.md` §7, `scenarios.md` |
| Inputs | ✓ Identified | `scenarios.md`, `extractionsheet.csv` |
| Outputs | ✓ Identified | `scenarios.md`, `extractionsheet.csv` |
| Interactions | ✓ Identified | `ontology_mapping.md` §8, `scenarios.md` |
| Decision Points | ✓ Identified | `scenarios.md`, `extractionsheet.csv` |
| Feedback Loops | ✓ Identified where documented; explicitly flagged as **[Assumption], Low confidence** in 4 of 5 scenarios where no source describes one | `scenarios.md`, `knowledge_gaps.md` |
| Evaluation Metrics | ✓ Identified (hallucination-rate figure, quality-framework evaluation, claim-support/contradict/mixed labeling, trust-survey statistics); absence of a disclosed quantitative fairness metric explicitly noted | `ontology_mapping.md` §9, `scenarios.md`, `knowledge_gaps.md` Gap 5 |
| Explainability | ✓ Identified (Trust Cards, real-time reasoning-step visibility, Claim Radar support/contradict/mixed labeling) | Scenarios 1, 2, 5; `ontology_mapping.md` §6, §9 |
| Trust | ✓ Identified (explicit "research-grade" trust value proposition; independently reported researcher-trust deficit statistics the product targets) | E-001, E-010, E-011; scenarios throughout |
| Fairness | ✓ Identified as a named Responsible AI principle ("prevent the creation or reinforcement of unfair bias") and publisher-neutral ranking mechanism; **quantitative fairness metric explicitly documented as absent/undisclosed**, not invented | E-007, E-017; `knowledge_gaps.md` Gap 5 |
| Accountability | ✓ Identified (human-approval-required-for-every-change policy; "meaningful human oversight" principle; advisory-board governance) | Scenarios 2, 5; `ontology_mapping.md` |
| CARE principles | ✓ Addressed per scenario (Collaborative/Adaptive/Responsible/Explainable), each sub-claim individually Observed/Inferred-labelled | `scenarios.md`, end of each scenario |
| Evidence for every extracted concept | ✓ Every concept in `ontology_mapping.md` and `scenarios.md` carries ≥1 Evidence ID | `sources.md`, `ontology_mapping.md`, `scenarios.md` |
| Confidence scores | ✓ Applied throughout (High/Medium/Low, with reasoning) | `sources.md`, `ontology_mapping.md`, `scenarios.md`, `extractionsheet.csv` |
| Traceability | ✓ Every fact resolves to an Evidence ID defined once in `sources.md` and referenced elsewhere | All files |

### 4.3 Saturation

Research was concluded after 17 search iterations when three consecutive rounds yielded corroboration/refinement rather than new concept categories, and every `hi:` class and property in the supplied ontology had at least one evidence-backed instantiation from LeapSpace — **with one explicit, documented exception**: `hi:Experiment` (and its `hi:hasNullHypothesis`/`hi:hasAlternativeHypothesis` datatype properties) could not be confidently mapped, because no source describes a LeapSpace-specific evaluation in formal hypothesis-testing terms (`knowledge_gaps.md` Gap 6). This exception is treated as a genuine saturation-at-the-limits-of-available-evidence finding, not a research shortfall — two dedicated search rounds (12 and 14) specifically targeting research papers, whitepapers, and conference talks (the source tiers most likely to contain formal experimental design language) both returned negative results, which is itself informative given the product's very recent launch.

---

## 5. How to Use This Package in the Next Phase

1. Start from `ontology_mapping.md` to see which `hi:`/`hint:` class or property each LeapSpace concept should become an instance of.
2. Use `scenarios.md` as the source material for scenario-level Knowledge Graph instances — each scenario is already structured close to the ontology's relational shape (Goal → requiresTask → Task → requiresCapability → Capability; Agent → performsExecution → TaskExecution → realizesTask → Task; etc.).
3. Use `extractionsheet.csv` as a flat, spreadsheet-importable version of the same five scenarios for rapid triage or for feeding into an LLM-extraction prompt-design phase (out of scope here, but this sheet is the intended input).
4. Before writing SHACL shapes or instantiating triples, re-check `knowledge_gaps.md` for any property (e.g., `hi:hasNullHypothesis`, a quantitative fairness metric, feedback-loop mechanisms in 4 of 5 scenarios) that this package flagged as **Inferred/Low confidence** — those should not be hard-constrained without either sourcing the missing detail or explicitly modelling them as assumptions.
5. Given LeapSpace's product recency, treat this package as a **snapshot as of 2026-08-24**: re-verify time-sensitive facts (content-scale figures, publisher-partnership list, pricing, feature availability) before Knowledge Graph construction if significant time has passed, since the evidence base itself documents an active, fast-moving feature-expansion cadence (E-014's "agentic capabilities" expansion occurred after the original launch).
6. Every quotation in `sources.md` is verbatim and URL-anchored; if a fact needs re-verification before being asserted as an RDF triple in the next phase, follow the Evidence ID back to its source there.
