# Research Acquisition Package — IBM watsonx.governance
Neuro-Symbolic AI for Assessing and Improving Hybrid Intelligence Systems | Master's Thesis Support
Research Acquisition Specification (RAS) v1.0 | Phase: Domain Knowledge Acquisition and Structured System Analysis
Compiled: 2026-08-24

---

## 1. Scope

This package is the output of the **knowledge-acquisition phase only**, as strictly bounded by the RAS (§3, §4, §5). It does **not** contain RDF triples, a Knowledge Graph, SHACL shapes, SHACL validation results, gap-analysis conclusions, recommendations, LLM extraction prompts, or software. It contains only collected, organized, evidence-traceable domain knowledge about **IBM watsonx.governance**, structured so that a later phase can build a Knowledge Graph, map it to the supplied Hybrid Intelligence (HI) Ontology (`hi:`, v2.0.0) and HINT thesaurus (`hint:`), and run SHACL validation without needing substantial additional domain research (RAS §19.8).

**Target Use Case:** IBM watsonx.governance — an enterprise AI governance, risk, and compliance (GRC) platform for directing, managing, and monitoring AI activities across the model and generative-AI lifecycle.

**Ontology used as the acquisition frame:** The supplied `hiontology.ttl` (VU Amsterdam KAI Group, v2.0.0), whose core classes are `hi:HITeam`, `hi:UseCase`, `hi:Agent`/`hi:HumanAgent`/`hi:ArtificialAgent`, `hi:Goal`, `hi:Task`, `hi:Capability`, `hi:TaskExecution`, `hi:Interaction`, `hi:Context`, `hi:Evaluation`, and `hi:Experiment`, plus the `hint:` thesaurus concept classes referenced by the ontology's object properties. Every extracted fact in this package was actively steered toward these categories (RAS §10).

---

## 2. Methodology

The work followed the exact 14-step iterative protocol specified in RAS §8: identify missing knowledge → search official sources → engineering documentation → whitepapers → research papers → conference presentations → product demos → compare findings → remove contradictions → normalize terminology → map to ontology concepts → identify missing concepts → search again → repeat until saturation.

Concretely, this meant:

1. **Web search**, always followed by **direct page fetch and full-text extraction** of the most promising results, rather than relying on search-snippet text alone.
2. **Source prioritization** strictly per RAS §9: official IBM documentation and engineering blogs first; peer-reviewed/preprint research (one arXiv paper on the AI Risk Atlas, co-authored by IBM Research, was located and used) next; high-quality independent technical articles (practitioner Medium walkthroughs with verifiable procedural detail) used to fill gaps where official IBM Docs pages returned HTTP errors; marketing/opinion blogs deliberately excluded as citable evidence once sufficient higher-tier evidence existed.
3. **Every extracted fact tagged with an Evidence ID** (`E-001`…`E-017`) carrying source title, URL, type, a verbatim short quotation, and the reason for extraction — see `sources.md`.
4. **Observed vs. Inferred labelling** applied to every fact that appears in `scenarios.md` and `ontology_mapping.md`, with reasoning and confidence attached to every Inferred item, per RAS §11–§12.
5. **Failed/inaccessible sources logged, not silently skipped** — 13 URLs returned HTTP 403/429/500 errors or insufficient content across the session; each is recorded in `sources.md` §2 (Rejected/Inaccessible Sources) and cross-referenced in `knowledge_gaps.md`.

---

## 3. Search Strategy

18 distinct search iterations were run (full detail in `research_log.md`), moving from broad product-overview queries to progressively narrower technical queries:

1. Product overview and architecture
2. AI-governance lifecycle and model-risk terminology
3. Predictive-model monitoring metrics (quality, fairness, drift, explainability)
4. Generative-AI evaluation metrics (HAP, PII, faithfulness, answer relevancy, hallucination)
5. AI Factsheets and model-lifecycle documentation
6. Agentic-AI governance (evaluation, lifecycle, human-in-the-loop)
7. Financial-services regulated-industry context
8. Named roles/personas (use-case owner, model validator, risk officer)
9. Customer case studies (for scenario grounding, per RAS §15's "do not invent scenarios" rule)
10. The AI Risk Atlas taxonomy and its academic/research-paper basis
11. Product editions/pricing tiers (as a proxy for capability structure and multi-user/team concepts)
12. The relationship between watsonx.governance and the separate watsonx Orchestrate agent-runtime product

Each search's objective, terms, engine, sources visited/accepted/rejected, extracted information, discovered ontology concepts, supported scenarios, and remaining unknowns are logged in full in `research_log.md`.

---

## 4. Completion Status

### 4.1 Deliverables (RAS §16)

| # | File | Status | Notes |
|---|---|---|---|
| 1 | `research_log.md` | ✅ Complete | 18 logged search iterations + saturation assessment |
| 2 | `README.md` | ✅ Complete | This file |
| 3 | `sources.md` | ✅ Complete | 17 accepted evidence sources (E-001–E-017) + 13 rejected/inaccessible sources (R-01–R-13) + source-priority compliance summary |
| 4 | `scenarios.md` | ✅ Complete | 5 evidence-backed HI scenarios, each with all 18 required fields |
| 5 | `extractionsheet.csv` | ✅ Complete | 5 data rows (one per scenario) + header, exact column order per spec, CSV-validated |
| 6 | `ontology_mapping.md` | ✅ Complete | Concept-to-ontology mapping across all `hi:` classes/properties and representative `hint:` concept types; no RDF/triples produced |
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
| Feedback Loops | ✓ Identified (one explicitly flagged as an unsupported-assumption gap in Scenario 5) | `scenarios.md`, `knowledge_gaps.md` Gap references |
| Evaluation Metrics | ✓ Identified (extensively — see metric lists in `ontology_mapping.md` §10) | `ontology_mapping.md`, `scenarios.md` |
| Explainability | ✓ Identified (LIME, SHAP, Faithfulness/Context-Relevance scoring, decomposed per-tool agent metrics) | Scenarios 1, 2, 4; `ontology_mapping.md` §6, §9 |
| Trust | ✓ Identified (explicit vendor language: "transparent, fair, and trustworthy") | E-011; Scenarios throughout |
| Fairness | ✓ Identified (Disparate Impact, Statistical Parity Difference, fair-lending/insurance-pricing framing) | Scenario 1; `ontology_mapping.md` §6 |
| Accountability | ✓ Identified (audit trails, Factsheets, audit logs, risk reports) | Scenarios 1, 2, 3, 4; `ontology_mapping.md` |
| CARE principles | ✓ Addressed per scenario (Collaborative/Adaptive/Responsible/Explainable), each sub-claim individually Observed/Inferred-labelled | `scenarios.md`, end of each scenario |
| Evidence for every extracted concept | ✓ Every concept in `ontology_mapping.md` and `scenarios.md` carries ≥1 Evidence ID | `sources.md`, `ontology_mapping.md`, `scenarios.md` |
| Confidence scores | ✓ Applied throughout (High/Medium/Low, with reasoning) | `sources.md`, `ontology_mapping.md`, `scenarios.md`, `extractionsheet.csv` |
| Traceability | ✓ Every fact resolves to an Evidence ID defined once in `sources.md` and referenced elsewhere | All files |

### 4.3 Saturation

Research was concluded after 18 search iterations when marginal new-concept yield across three consecutive rounds approached zero and every `hi:` class and property in the supplied ontology had at least one, and typically several, independent evidence-backed instantiation from IBM watsonx.governance. Full reasoning is in `research_log.md` §Saturation Assessment. Saturation was **not** claimed for case-study-level operational detail, conference/demo transcripts, or the complete SDK metrics catalogue — these are explicit, documented gaps (`knowledge_gaps.md`), not silently accepted as "done."

---

## 5. How to Use This Package in the Next Phase

1. Start from `ontology_mapping.md` to see which `hi:`/`hint:` class or property each watsonx.governance concept should become an instance of.
2. Use `scenarios.md` as the source material for scenario-level Knowledge Graph instances — each scenario is already structured close to the ontology's relational shape (Goal → requiresTask → Task → requiresCapability → Capability; Agent → performsExecution → TaskExecution → realizesTask → Task; etc.).
3. Use `extractionsheet.csv` as a flat, spreadsheet-importable version of the same five scenarios for rapid triage or for feeding into an LLM-extraction prompt-design phase (out of scope here, but this sheet is the intended input).
4. Before writing SHACL shapes or instantiating triples, re-check `knowledge_gaps.md` for any property (e.g., `hi:hasNullHypothesis`, precise agent-metric thresholds) that this package flagged as **Inferred/Low confidence** — those should not be hard-constrained without either sourcing the missing detail or explicitly modelling them as assumptions.
5. Every quotation in `sources.md` is verbatim and URL-anchored; if a fact needs re-verification before being asserted as an RDF triple in the next phase, follow the Evidence ID back to its source there.
