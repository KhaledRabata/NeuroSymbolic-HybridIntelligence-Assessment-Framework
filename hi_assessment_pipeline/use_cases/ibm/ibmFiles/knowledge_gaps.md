# Knowledge Gaps — IBM watsonx.governance

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **IBM watsonx.governance**
Documents only information that could **not** be found during the Domain Knowledge Acquisition phase, per RAS Section 16 (File 7). No gaps are filled here — they are recorded for the next pipeline phase to address, either through further research, direct vendor/practitioner contact, or explicitly labelled modelling assumptions.

---

## GAP-01: Full official Model Risk Governance (MRG) workflow documentation

- **Missing information:** The complete, stage-by-stage official documentation of the Model Risk Governance (MRG) solution within the watsonx.governance Governance console — specifically the exact named workflow stages, RACI-style role assignments, and artifact templates as defined by IBM itself (as opposed to reconstructed from secondary sources).
- **Searches performed:** "IBM watsonx.governance AI model risk governance lifecycle"; "IBM watsonx.governance model validator risk officer workflow approve model use case"; direct URL fetches of `dataplatform.cloud.ibm.com/docs/content/svc-watsonxgov/wxgov_mrg_desc.html` and `.../wxgov_mrg_example_workflow.html`; direct fetch of `www.ibm.com/docs/en/watsonx/w-and-w/2.4.x?topic=ai-managing-risk-compliance-governance-console`; direct fetch of `www.ibm.com/docs/en/watsonx/saas?topic=components-model-risk-governance-workflows`.
- **Sources consulted:** IBM Docs / dataplatform.cloud.ibm.com pages listed above (E-002, E-004 in `sources.md`).
- **Why information could not be found:** These pages are rendered client-side (JavaScript single-page application); the automated fetch tool retrieved only navigation chrome (login/logout links, menu structure) rather than the substantive page body. One URL variant additionally returned an HTTP 403 error and another an HTTP 500 error on separate attempts.
- **Whether modelling assumptions may later be required:** Yes. Scenario 8 in `scenarios.md` and the corresponding row in `extractionsheet.csv` were reconstructed from two independent secondary engineering-blog sources (E-019, E-020) rather than this primary source. Before Knowledge Graph construction, a manual (human) visit to the live, authenticated watsonx.governance console — or a request for IBM's PDF/exportable documentation — is recommended to confirm or correct the six-stage workflow and role set used here.

---

## GAP-02: Named human role titles for agentic AI runtime/production approval

- **Missing information:** watsonx Orchestrate's agent-governance-and-observability materials describe policy enforcement, guardrails, and audit logging, but do not name the specific human role(s) (e.g., "Agent Owner," "AI Operations Lead") responsible for granting production approval or responding to a policy violation at runtime.
- **Searches performed:** "IBM watsonx Orchestrate agent governance human in the loop approval."
- **Sources consulted:** `www.ibm.com/products/watsonx-orchestrate/governance-and-observability` (E-018); IBM Mediacenter agent-observability demo video (link discovered but blocked by robots.txt, so its transcript — which might have named roles — was not accessible).
- **Why information could not be found:** The product marketing page is capability-focused rather than role/process-focused, and the demo video that likely shows an actual workflow with named personas could not be retrieved due to the hosting platform's robots.txt restrictions.
- **Whether modelling assumptions may later be required:** Yes. In `scenarios.md` (Scenario 5) and `ontology_mapping.md`, the generic "SME / Red Teamer" and "Agent Developer" roles from E-005 are used as the closest documented substitutes; a distinct "Agent Approver" role is plausible but was not modelled as Observed anywhere in this package, and should not be assumed present without further evidence.

---

## GAP-03: Exact human role titles for financial-services Model Risk Management (MRM) sign-off

- **Missing information:** The BizTech Magazine article on financial-institution use of watsonx.governance explicitly states that human risk oversight is retained ("keeping human risk oversight in the loop") but does not name specific titles (e.g., "Chief Risk Officer," "Model Validation Lead," "Second Line of Defense") standard in banking/insurance MRM practice.
- **Searches performed:** Covered under the broader Round 4/7 searches for MRG and financial-services governance; no dedicated additional search turned up a watsonx.governance-specific role taxonomy for this context.
- **Sources consulted:** `biztechmagazine.com/article/2025/12/ibms-watsonx-platform-goes-distance-ai-governance-financial-institutions` (E-022).
- **Why information could not be found:** The source is a trade-press overview article, not a detailed process document; it summarizes capabilities rather than documenting an implementation with named organizational roles.
- **Whether modelling assumptions may later be required:** Yes. Scenario 8 uses "Model Risk Officer" (borrowed from E-020, which is a general watsonx.governance workflow source, not finance-specific) as a reasonable proxy. This substitution is explicitly flagged as Inferred (not Observed) in both `scenarios.md` and `ontology_mapping.md`.

---

## GAP-04: Full generative AI quality-metrics reference documentation

- **Missing information:** The canonical, complete IBM Docs reference page enumerating every generative AI quality metric with its full mathematical definition (as opposed to the subset of metric names and short descriptions recovered piecemeal from engineering blogs).
- **Searches performed:** "watsonx.governance evaluate metrics quality fairness drift explainability documentation"; "watsonx.governance generative AI quality metrics hallucination faithfulness prompt evaluation"; direct fetch of `dataplatform.cloud.ibm.com/docs/content/wsj/model/wos-monitor-gen-quality.html`.
- **Sources consulted:** heidloff.net gen-AI-quality-metrics article (rejected — did not itself enumerate the metrics, only pointed to the official doc); the official doc page itself (returned HTTP 500 on every fetch attempt in this research window).
- **Why information could not be found:** Server-side error on the authoritative documentation page; the linking secondary article deliberately deferred to that page rather than duplicating its content.
- **Whether modelling assumptions may later be required:** Partially mitigated. The metric list was still reconstructed with reasonable completeness by triangulating across four independent sources (E-008, E-013, E-019, E-020), each of which named overlapping but not identical subsets of metrics (ROUGE, SARI, METEOR, BLEU, Text quality, Sentence similarity, PII, HAP, Readability, Exact match, F1/precision/recall, Faithfulness, Answer Relevance, Unsuccessful Requests, Context Relevance, Retrieval Precision, Average Precision, Hit Rate, NDCG). No modelling assumption should be needed for the metric *names*; a modelling assumption **would** be needed if exact mathematical formulas are required for SHACL constraint value ranges in a later phase — those formulas were not recovered.

---

## GAP-05: Product demo / conference presentation transcripts

- **Missing information:** RAS Section 9 (Source Priority tier 5) calls for official demos and presentations. Several were located (IBM Mediacenter: "Governed Agentic Catalog demo," "Direct, manage and monitor your GenAI and ML models, anywhere," "Model monitoring with IBM watsonx.governance") but none could be transcribed or summarized from primary access.
- **Searches performed:** ""watsonx.governance" OR "Watson OpenScale" conference presentation demo IBM Think 2025."
- **Sources consulted:** `mediacenter.ibm.com` video pages (URLs identified but not retrievable — E-005's Round 7 note in `research_log.md`).
- **Why information could not be found:** IBM Mediacenter's robots.txt disallows automated fetching of video/media pages, and no transcript or closed-caption text was surfaced through search results.
- **Whether modelling assumptions may later be required:** No — this gap did not block scenario construction, since equivalent information (the Governed Agentic Catalog's function, model-monitoring workflow) was independently confirmed via E-005 and E-006. This gap is recorded for completeness/traceability rather than because it blocks the next phase; a human researcher with a browser (rather than automated fetch) could likely close it quickly if richer detail is later required.

---

## GAP-06: US Open "court fairness" figure — relevance ambiguity

- **Missing information:** The IBM watsonx.governance product page (E-001) lists "US Open: 11% increase in court fairness (71% to 82%)" among its customer outcomes. On investigation, this figure appears to relate to a different IBM AI capability (electronic line-calling / fan-engagement systems at the US Open) rather than a documented watsonx.governance workflow specifically.
- **Searches performed:** "IBM watsonx.governance US Open case study fairness court."
- **Sources consulted:** `ibm.com/case-studies/blog/us-open-heralds-new-era-of-fan-engagement-with-watsonx-and-generative-ai` (reviewed, found to describe fan-engagement generative AI, not a watsonx.governance-specific fairness workflow).
- **Why information could not be found:** No dedicated case-study page connecting this specific figure to a watsonx.governance workflow (as opposed to the broader watsonx platform) could be located.
- **Whether modelling assumptions may later be required:** This ambiguity is why the US Open example was **deliberately excluded** from the eight constructed scenarios rather than turned into a ninth or substituted for a weaker one — per RAS Section 15 ("Do Not Invent Scenarios"), a scenario should not be built on a metric whose underlying workflow cannot be confirmed as belonging to the target system.

---

## GAP-07: Independently audited outcome metrics

- **Missing information:** All quantitative outcome figures used in this package (85% reduction in time-to-hire, 97% faster résumé screening, 150% increase in operational efficiency, 58% reduction in data-clearance processing time, etc.) are vendor-published case-study claims. No independently audited or third-party-verified figures were located for any of them.
- **Searches performed:** Covered incidentally during Rounds 1 and 5 while investigating case studies; no dedicated independent-audit search was run, since this is a known characteristic of vendor case-study material rather than a distinct research question.
- **Sources consulted:** E-001, E-016.
- **Why information could not be found:** Vendor case studies are self-reported by design; independent audits of individual customer deployments are generally not public.
- **Whether modelling assumptions may later be required:** Yes, if these figures are to be used as ground-truth benchmark values in later SHACL validation or evaluation-metric thresholds, they should be treated as illustrative/qualitative rather than as validated quantitative targets. This caveat is already reflected in the Confidence ratings (Medium, not High) for Scenario 7 in `extractionsheet.csv`.

---

## Summary Table

| Gap ID | Topic | Blocks next phase? | Mitigation applied |
|---|---|---|---|
| GAP-01 | Official MRG workflow docs | Partially (Scenario 8 confidence lowered to Medium-High) | Reconstructed from 2 independent secondary sources |
| GAP-02 | Agent runtime approval role titles | No | Used closest documented role (SME/Developer), flagged Inferred |
| GAP-03 | Financial-services MRM role titles | No | Borrowed general "Model Risk Officer" role, flagged Inferred |
| GAP-04 | Full GenAI metric formulas | No (names recovered; formulas not) | Triangulated metric names from 4 sources |
| GAP-05 | Demo/conference transcripts | No | Equivalent info confirmed via other accepted sources |
| GAP-06 | US Open figure relevance | No (scenario excluded rather than guessed) | Excluded from scenario set per RAS Section 15 |
| GAP-07 | Independent outcome audits | No | Confidence downgraded where relevant, not fabricated as High |
