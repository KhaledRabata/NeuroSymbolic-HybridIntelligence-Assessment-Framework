# Knowledge Gaps — LeapSpace by Elsevier

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **LeapSpace (Elsevier)**
Documents only information that could **not** be found during the Domain Knowledge Acquisition phase, per RAS Section 16 (File 7). No gaps are filled here — they are recorded for the next pipeline phase to address, either through further research, direct vendor/practitioner contact, or explicitly labelled modelling assumptions.

---

## GAP-01: LeapSpace's own internal AI architecture (as opposed to the related Scopus AI product's)

- **Missing information:** LeapSpace's marketing material states it uses "Agentic AI, Generative AI, Reasoning engines, Retrieval-augmented generation (RAG)" and a "multi-model AI approach," but no source describes LeapSpace's own retrieval pipeline, reranking method, specific foundation-model provider(s), or model-selection logic in the level of technical detail that exists for the related, earlier Scopus AI product (search module + reranker + LLM module, OpenAI GPT hosted on private Azure, RAG Fusion).
- **Searches performed:** "Elsevier Scopus AI ScienceDirect AI RAG architecture trust technical whitepaper"; general review of all official LeapSpace pages for architecture detail.
- **Sources consulted:** E-005 (names the architecture components but not their implementation); E-012 (Scopus AI interview — a related but distinct product).
- **Why information could not be found:** LeapSpace launched in January 2026; no engineering blog post, technical whitepaper, or architecture deep-dive equivalent to the Scholarly Kitchen Scopus AI interview has yet been published (or was not surfaced by search) for LeapSpace specifically.
- **Whether modelling assumptions may later be required:** Yes. Every place in `scenarios.md` and `ontology_mapping.md` where Scopus AI's architecture (E-012) is used to describe LeapSpace's likely internals, it is explicitly flagged Inferred at Medium confidence. Before Knowledge Graph construction assigns a specific `hi:ArtificialAgent` sub-typing to "the LLM module," this assumption should be revisited against any future LeapSpace-specific technical disclosure.

---

## GAP-02: Precise Claim Radar and Trust Card computation methodology

- **Missing information:** While Claim Radar's retrieval scope (up to 40 sources via Scopus) and output categories (support/contradict/mixed) are documented, the underlying classification method — e.g., whether it is an LLM-as-judge natural-language-inference classifier, a fine-tuned stance-detection model, or a rules-based heuristic — is not disclosed anywhere.
- **Searches performed:** "LeapSpace "Trust Card" "Claim Radar" how it works Elsevier"; direct fetch of the dedicated Claim Radar explainer page.
- **Sources consulted:** E-007 (most detailed available source; describes behavior and workflow but not the underlying algorithm).
- **Why information could not be found:** Elsevier's public-facing material is written for a researcher audience (feature/benefit framing) rather than an engineering audience; no technical paper or patent filing describing the classifier was located.
- **Whether modelling assumptions may later be required:** Yes, if SHACL constraints in a later phase need to specify the `hi:hasMethodConcept` value for a Claim Radar `hi:TaskExecution` precisely (e.g., distinguishing "stance classification" from "semantic similarity thresholding"). Currently only the input/output behavior is Observed.

---

## GAP-03: Independent, non-Elsevier critical evaluation of LeapSpace

- **Missing information:** A genuinely independent, critical assessment of LeapSpace (accuracy testing, comparison against competing AI research tools, critique of the publisher-neutrality claim, etc.), of the kind RAS Section 8 calls for when it asks researchers to "compare findings" and "remove contradictions" across source types.
- **Searches performed:** General searches throughout Rounds 1–7 surfaced only vendor-published or syndicated-press-release content; a specific attempt was made in Round 7 to fetch a Science/AAAS article that appeared, from its headline, to offer independent critical framing ("Journal giant Elsevier unveiled an AI tool that scans millions of paywalled papers. Is it worth it?").
- **Sources consulted:** science.org/content/article/journal-giant-elsevier-unveiled-ai-tool-scans-millions-paywalled-papers-it-worth-it — fetch failed with HTTP 403 (access blocked to automated retrieval).
- **Why information could not be found:** The single most promising independent source identified was inaccessible to the automated fetch tool; no equivalent alternative independent critique was found in the time available. This is compounded by the product's very recent launch (Jan 2026), which limits how much independent commentary has had time to accumulate at all.
- **Whether modelling assumptions may later be required:** No direct modelling assumption is required, but this gap means the knowledge-acquisition package as a whole is more vendor-source-weighted than the previous (mature-product) target system researched under this RAS. A human researcher with direct browser access (rather than the automated fetch tool used here) should attempt to retrieve this specific article before treating this package as fully saturated for independent perspective.

---

## GAP-04: Author Search ranking/matching mechanism

- **Missing information:** Every source that mentions Author Search describes only its purpose ("explore relevant collaborators, mentors and topic contributors") without any detail on how candidate authors are ranked, matched, or filtered (e.g., co-citation analysis, topical embedding similarity, institutional proximity).
- **Searches performed:** "LeapSpace "Author Search" collaborator discovery feature Elsevier" — this search predominantly surfaced syndicated press-release mirrors rather than any feature-specific documentation.
- **Sources consulted:** E-001 (only source with any Author Search description at all).
- **Why information could not be found:** No dedicated feature-explainer page (analogous to the Claim Radar explainer, E-007) exists yet for Author Search, or was not surfaced by search.
- **Whether modelling assumptions may later be required:** Yes, if Scenario 5's `hi:Task` "Collaborator Identification" needs a `hi:hasMethodConcept` value in a later phase; currently no method can be Observed or even reasonably Inferred from available evidence.

---

## GAP-05: Absence of peer-reviewed literature, conference presentations, or third-party audits (structural gap)

- **Missing information:** RAS source-priority tiers 6–8 (peer-reviewed research papers, conference talks, whitepapers) are essentially unpopulated for LeapSpace specifically.
- **Searches performed:** General academic-literature-style searches were embedded within Rounds 1–7's broader queries; no dedicated academic-database search (e.g., Google Scholar) turned up any peer-reviewed paper evaluating LeapSpace.
- **Sources consulted:** None found meeting this description.
- **Why information could not be found:** This is not a search-execution failure but a genuine feature of the target system's youth: LeapSpace reached institutional general availability on January 21, 2026, which is too recent for the peer-review publication cycle (typically many months to over a year) to have produced independent academic evaluation.
- **Whether modelling assumptions may later be required:** This should not require modelling assumptions so much as an explicit caveat for the thesis: any Knowledge-Graph-derived claims about LeapSpace's HI quality are necessarily grounded predominantly in vendor self-disclosure (which the RAS itself treats as legitimate top-priority evidence, per Section 9's ranking of "official documentation from the vendor / company" as tier 1) rather than independent verification. This asymmetry relative to a more mature target system should be noted when this package is compared against knowledge-acquisition packages for other target systems in the same thesis.

---

## GAP-06: The LeapSpace Use Cases & Prompts Guide (PDF)

- **Missing information:** The official support-center page (E-017) confirms the existence of a downloadable "LeapSpace Use Cases & Prompts Guide" PDF covering engineering, energy, pharma, biotech, and MedTech use cases with "copy-ready prompts," but the PDF itself, hosted on a separate brand-asset platform, was not retrieved.
- **Searches performed:** Direct fetch of the support-center page; the page itself confirmed the PDF's existence and topic scope but the automated fetch tool returned only the landing-page text, not the linked document.
- **Sources consulted:** E-017.
- **Why information could not be found:** The PDF is hosted on a separate platform (Elsevier's brand-asset/DAM system) not directly crawled by the fetch tool from the support-center page in this research window.
- **Whether modelling assumptions may later be required:** Possibly. This PDF likely contains additional concrete, industry-specific worked examples (especially for engineering, energy, and MedTech, which are named in E-017 but have no worked scenario of their own in `scenarios.md` — Scenario 8 covers pharma/biotech/corporate R&D generally but not engineering or energy specifically). A human researcher should retrieve this PDF directly before treating industry coverage as fully saturated.

---

## GAP-07: Contradictory funding-database size figures

- **Missing information:** Not a true "missing" gap but a documented inconsistency: E-010 states "36,000+ active grants" while E-005 states "45,000 active and recurring grants worth over $100 billion" for the same Find Funding feature.
- **Searches performed:** Both figures were found in the normal course of Rounds 2 and 5 research; no additional search was run specifically to reconcile them, since the most likely explanation (database growth between the two publication dates) does not require further evidence to be a reasonable inference, but it has not been confirmed.
- **Sources consulted:** E-005, E-010.
- **Why information could not be found:** No source states both figures together with a timestamp explanation, so the reconciliation offered in `scenarios.md` (Scenario 6) is Inferred, not Observed.
- **Whether modelling assumptions may later be required:** Yes, if a specific numeric value for the grants-database size is needed as a SHACL constraint value later; the correct approach is to treat this as a time-varying property rather than a fixed constant, or to source a currently-live figure directly from the product at KG-construction time.

---

## Summary Table

| Gap ID | Topic | Blocks next phase? | Mitigation applied |
|---|---|---|---|
| GAP-01 | LeapSpace's own AI architecture detail | Partially (architecture agent-typing uses Inferred analogy) | Used Scopus AI as explicitly-flagged background analogy |
| GAP-02 | Claim Radar/Trust Card computation method | No (behavior fully Observed; only internal method unknown) | Modelled at input/output level only |
| GAP-03 | Independent critical evaluation | No | Vendor-weighting acknowledged explicitly; retry recommended |
| GAP-04 | Author Search ranking mechanism | No | Scenario 5 omits method-level claims for this specific task |
| GAP-05 | Absence of peer-reviewed/conference literature | No (structural, not a search failure) | Explicit caveat recorded rather than filled with weak sources |
| GAP-06 | Use Cases & Prompts Guide PDF content | Partially (engineering/energy sub-scenarios thinner than pharma/biotech) | Scenario 8 kept general rather than over-specified |
| GAP-07 | Grants-database size discrepancy | No | Both figures reported; reconciliation flagged Inferred |
