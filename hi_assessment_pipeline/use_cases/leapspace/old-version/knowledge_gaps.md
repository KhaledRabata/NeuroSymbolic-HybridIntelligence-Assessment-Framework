# Knowledge Gaps — Elsevier LeapSpace
RAS v1.0 | Documents ONLY information that could not be found during this knowledge-acquisition phase. No gap listed here has been filled with invented or unlabelled content — per protocol §16, gaps are recorded, not resolved.

---

## Gap 1: No peer-reviewed research paper, whitepaper, or independent academic study of LeapSpace itself

- **Missing information:** A peer-reviewed paper, formal whitepaper, or independent academic evaluation specifically studying LeapSpace (its architecture, accuracy, or effect on research outcomes).
- **Searches performed:** `Elsevier Labs research paper retrieval augmented generation scientific literature knowledge graph`; `LeapSpace Elsevier whitepaper conference presentation SSP STM`; `"LeapSpace" Elsevier peer-reviewed study evaluation researcher trust survey`.
- **Sources consulted:** General RAG/knowledge-graph academic papers (Nature Scientific Reports, arXiv survey papers, ACM TOIS) were reviewed but found to be about the general *methods* class LeapSpace claims to use, not about LeapSpace itself; no result named or studied LeapSpace directly.
- **Why information could not be found:** LeapSpace is a newly launched product — preview access, institutional general availability ("goes live"), and a subsequent agentic-capabilities expansion all occurred within roughly the months immediately preceding this research date (2026-08-24). The academic publication cycle (submission → peer review → publication) typically lags a product launch by many months to years, so the absence of peer-reviewed literature is expected given the product's age rather than a search failure.
- **Modelling assumptions may later be required:** Yes — any Knowledge Graph representation of LeapSpace's *technical* internals (e.g., specific model architectures, training data composition, or a formal accuracy benchmark methodology) will need to rely on vendor self-disclosure (as captured in this package) until independent academic literature exists. This should be flagged as a limitation of evidentiary independence, not filled with a fabricated citation.

## Gap 2: Independent, LeapSpace-specific accuracy/hallucination benchmark

- **Missing information:** An independently conducted (i.e., non-Elsevier) benchmark verifying the vendor-reported "less than 1%" serious-hallucination-risk figure (E-005).
- **Searches performed:** `LeapSpace Elsevier hallucination rate accuracy evaluation benchmark`.
- **Sources consulted:** General "AI hallucination rate benchmark 2026" articles and academic hallucination-benchmark papers (HalluLens, OpenReview submissions) were reviewed but found to benchmark other, general-purpose AI systems, not LeapSpace specifically.
- **Why information could not be found:** No independent third party appears to have yet run a controlled hallucination/accuracy study against LeapSpace specifically; this is consistent with Gap 1's explanation (product recency) and with E-016's explicit expert observation (Jevin West, University of Washington) that "no standardized evaluation method exists for assessing AI-generated summary accuracy" for this class of tool generally.
- **Modelling assumptions may later be required:** Yes — the <1% figure should be represented in any future Knowledge Graph as a **vendor-reported, methodology-undisclosed metric**, not as an independently verified fact. `ontology_mapping.md` §9 already flags this with Medium confidence rather than High.

## Gap 3: Full Q&A transcript / recorded content of the official demo webinar

- **Missing information:** The substantive Q&A discussion and any live demo walkthrough detail from the "See LeapSpace in Action" webinar (E-009) beyond the event-listing metadata (presenter names/titles, date, format).
- **Searches performed:** Direct fetch of the webinar registration/listing page only; no separate search for a post-event recording or transcript was conducted, since the event (dated 2026-02-12 per the listing) may not yet have occurred relative to when the listing was indexed, or a recording may be gated behind registration.
- **Sources consulted:** webinars.elsevier.com listing page only.
- **Why information could not be found:** Webinar listing pages typically expose only promotional/registration metadata before the event and gate the actual recording behind a registration/login wall afterward; neither form of access was available through this session's web-fetch tooling.
- **Modelling assumptions may later be required:** Possibly minor — the four named presenter roles and the general feature list already corroborated elsewhere (Trust Cards, Deep Research Mode, IP protection) are sufficient for role/capability modelling; the gap mainly affects fine-grained interaction-sequence detail (e.g., the exact order of UI steps in a live demo), which is not required for scenario-level modelling at the granularity `scenarios.md` currently uses.

## Gap 4: Detailed technical description of the ScienceDirect AI engine specifically

- **Missing information:** A dedicated, fetched technical description of ScienceDirect AI (the second named underlying engine, alongside Scopus AI, that LeapSpace is built on per E-006 and E-013) parallel in depth to what was obtained for Scopus AI (E-008).
- **Searches performed:** `Elsevier ScienceDirect AI Scopus AI capabilities architecture` — this search surfaced a ScienceDirect AI press release (prnewswire.com and elsevier.com mirrors) and a library guide, but the session's research budget was allocated toward fetching the Scopus AI support page (E-008) and the higher-priority LeapSpace-specific pages instead of also fetching the ScienceDirect AI press release in full.
- **Sources consulted:** Search-result snippets only for the ScienceDirect AI press release; not independently fetched and quoted in this pass.
- **Why information could not be found:** A scoping/time-allocation decision, not a source-unavailability issue — the ScienceDirect AI launch press release is very likely fetchable in a future research pass focused specifically on closing this gap.
- **Modelling assumptions may later be required:** Yes — `ontology_mapping.md` §3 currently marks the ScienceDirect AI `hi:ArtificialAgent` mapping as **Medium confidence** specifically because it is named but not independently detailed in this pass. A future pass should fetch `https://www.elsevier.com/about/press-releases/elsevier-launches-sciencedirect-ai-to-transform-research-with-rapid-mission-critical-insights-from-trusted-content` (identified but not fetched) before treating ScienceDirect AI's capabilities as equally well-evidenced as Scopus AI's.

## Gap 5: Quantitative fairness/bias metric values

- **Missing information:** Any specific, disclosed numeric fairness or bias metric (analogous to, e.g., a disparate-impact score) resulting from Elsevier's stated "automated bias detection tools" (E-007) as applied to LeapSpace or its underlying models.
- **Searches performed:** Covered within Search 6 (Responsible AI Principles) and Search 17 (Trust and Security page); no dedicated separate search for numeric bias-metric disclosure was run, since the Responsible AI Principles page (E-007) and Trust & Security page (E-017) were both reviewed in full and neither discloses a specific number.
- **Sources consulted:** E-007, E-017.
- **Why information could not be found:** Elsevier's public-facing documentation describes the *existence* of bias-detection processes and governance structures but does not publish specific quantitative results, which is consistent with typical corporate AI-governance disclosure practice (process transparency without raw metric publication).
- **Modelling assumptions may later be required:** Yes — `ontology_mapping.md` §9 and Scenario 5 in `scenarios.md` both explicitly flag the absence of a disclosed fairness-metric value with Low confidence; any future SHACL constraint requiring a populated `hi:hasMetricConcept` value for a "fairness" evaluation of LeapSpace would need either newly disclosed data or an explicitly labelled placeholder/assumption.

## Gap 6: Formal `hi:Experiment` instance with null/alternative hypotheses

- **Missing information:** Any LeapSpace-specific description of a formal experimental setup using explicit null-hypothesis/alternative-hypothesis language, as would populate the ontology's `hi:Experiment`, `hi:hasNullHypothesis`, and `hi:hasAlternativeHypothesis` properties.
- **Searches performed:** No dedicated search for "hypothesis testing" terminology was run separately; this gap was identified by systematically checking every ontology class against the accumulated evidence base during `ontology_mapping.md` construction (per protocol §12 "identify missing concepts").
- **Sources consulted:** All 18 accepted sources were reviewed for this concept; none uses formal hypothesis-testing language.
- **Why information could not be found:** LeapSpace's documented evaluation activities (Scopus AI's "quality framework," Claim Radar's support/contradict/mixed labeling, Elsevier's bias-detection tooling) are all described in product/process terms, not in formal experimental-design terms. This may reflect a genuine absence of publicly disclosed formal A/B-testing or hypothesis-driven evaluation methodology, or simply that such methodology (if it exists internally at Elsevier) is not part of LeapSpace's public-facing documentation.
- **Modelling assumptions may later be required:** Yes — this is the single clearest "no confident mapping" entry in `ontology_mapping.md` §9. Any future population of `hi:Experiment` for LeapSpace would need to be constructed as an explicit modelling assumption (e.g., treating a hypothetical "Model A vs. Model B" comparison as an implied experiment) rather than sourced from Elsevier's documentation.

## Gap 7: Independent corroboration of the ~22% content-coverage figure

- **Missing information:** A second, independent source corroborating the E-016 (HyperAI) claim that LeapSpace addresses only "22% of 2024 research articles."
- **Searches performed:** This figure was encountered once, in Search 16, while specifically seeking critical/independent commentary; no follow-up search was run to seek a second corroborating source, since the general product-scale figures (18–20+ million full-text articles, 100+ million abstracts) were already well corroborated across E-002, E-003, E-011, E-012, and a coverage-percentage claim is a distinct, more specific computation (coverage of a denominator — "2024 research articles" — not independently defined in the source).
- **Sources consulted:** E-016 only for this specific percentage.
- **Why information could not be found:** This is a single-source, independently-calculated critical statistic rather than a vendor-disclosed figure; no second source repeating the same percentage was located within this session's search scope.
- **Modelling assumptions may later be required:** Yes — `ontology_mapping.md` §7 and Scenario 1/5 context already mark this figure as Medium confidence, single-source. It should not be treated as an Elsevier-endorsed statistic in any downstream Knowledge Graph representation.

## Gap 8: science.org (AAAS) independent journalistic analysis

- **Missing information:** The full content of what is likely a high-quality, editorially independent piece of science journalism specifically evaluating LeapSpace ("Is it worth it?"), given AAAS/Science's general reputation for rigorous science journalism.
- **Searches performed:** Direct fetch attempt as part of Search 4.
- **Sources consulted:** science.org URL only — fetch failed.
- **Why information could not be found:** HTTP 403 client error on every fetch attempt; likely bot-protection or access-control on science.org's infrastructure rather than the content being genuinely unavailable to human readers.
- **Modelling assumptions may later be required:** No direct modelling impact — the HyperAI article (E-016) independently surfaced substantially similar critical themes (market concentration, coverage limitations, evaluation-standardization concerns) with named, attributable experts, partially substituting for this gap. However, a future research pass should retry this URL (possibly via a different access method available to the research team, respecting AAAS's terms of service) since Science/AAAS coverage would meaningfully strengthen the evidentiary independence of the "critical perspective" material in `sources.md` and `scenarios.md` Scenario 5.

---

## Summary Table

| Gap # | Topic | Blocks Scenario Modelling? | Requires Future Modelling Assumption? |
|---|---|---|---|
| 1 | No peer-reviewed research on LeapSpace itself | No (product mechanics well evidenced from vendor + trade press) | Yes, for any claim requiring independent academic verification |
| 2 | No independent hallucination/accuracy benchmark | No | Yes, if asserting the <1% figure as verified fact |
| 3 | Webinar Q&A/demo transcript not accessible | No (role/feature detail sufficiently evidenced elsewhere) | No |
| 4 | ScienceDirect AI technical detail thin | No (Scopus AI detail is sufficient for the ArtificialAgent-subcomponent pattern) | Yes, before treating ScienceDirect AI as equally well-evidenced as Scopus AI |
| 5 | No disclosed quantitative fairness/bias metric | No | Yes, if populating a specific fairness `hint:Metric` value |
| 6 | No `hi:Experiment`/hypothesis-testing instance | No | Yes, if `hi:Experiment` must be populated for LeapSpace |
| 7 | Single-source coverage-percentage figure | No | Yes, if asserting the 22%-coverage figure as fact rather than as a contested/single-source claim |
| 8 | science.org article inaccessible (403) | No (HyperAI substantially substitutes) | No, though retrying would strengthen evidentiary independence |

None of these gaps required inventing unsupported facts. Where a scenario or mapping needed to bridge a gap to remain complete, the bridging statement is explicitly labelled **[Assumption]** and confidence-scored in `scenarios.md`, `extractionsheet.csv`, and `ontology_mapping.md`, consistent with protocol §11, §12, and §15.
