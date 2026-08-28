# Knowledge Gaps — IBM watsonx.governance
RAS v1.0 | Documents ONLY information that could not be found during this knowledge-acquisition phase. No gap listed here has been filled with invented or unlabelled content — per protocol §16, gaps are recorded, not resolved.

---

## Gap 1: Detailed Governance-Console workflow screenshots/step-by-step UI mechanics for Model Risk Governance (MRG)

- **Missing information:** The exact in-product screen flow for registering a model, moving it through validation states, and recording sign-offs within the standalone IBM OpenPages Model Risk Governance module (as distinct from the newer Governance Console MRG solution documented in E-013).
- **Searches performed:** `IBM watsonx.governance AI governance lifecycle model risk`; `IBM AI Factsheets watsonx.governance model documentation lifecycle`; direct fetch attempts of `ibm.com/docs/en/SSFUEU_9.0.0/op_grc_admin/c_adm_mrg.html` and its `SSFUEU_9.1` mirror.
- **Sources consulted:** IBM OpenPages documentation pages (both returned HTTP 403); IBM Docs Governance Console page (`w-and-w/2.4.x`, HTTP 403); `dataplatform.cloud.ibm.com` planning/overview pages (persistent HTTP 500).
- **Why information could not be found:** All primary-source URLs identified for this specific sub-topic returned HTTP errors (403 forbidden or 500 server error) on every fetch attempt during this session, likely due to bot-protection or transient platform issues on IBM's documentation infrastructure rather than the content being genuinely unavailable.
- **Modelling assumptions may later be required:** Yes — if Knowledge Graph construction needs a precise state-machine of MRG workflow states, a modelling assumption (e.g., a generic Register → Validate → Approve → Monitor state sequence, consistent with what E-005 and E-013 do document at a coarser grain) would need to be explicitly flagged as inferred, not sourced from a step-by-step OpenPages walkthrough.

## Gap 2: Explicit, named personas beyond role-function descriptions (e.g., no confirmed official job-title glossary such as "AI Risk Officer" as a formal watsonx.governance-defined role)

- **Missing information:** IBM does not appear to publish an official, fixed taxonomy of persona job titles (e.g., a definitive list like "Chief AI Risk Officer," "Model Risk Manager," "AI Ethics Board Member"). The roles identified in this package (Requester/User, Reviewer, Approver, Risk & Compliance team member, Model Validator/Auditor, LLM Developer, SME/Red-teamer, Governance-Console Administrator profiles) are functional labels drawn from workflow descriptions, not from a single canonical "roles and personas" reference document.
- **Searches performed:** `watsonx.governance "use case owner" OR "model validator" OR "model owner" OR "risk officer" role persona IBM`.
- **Sources consulted:** Multiple Medium articles, Aligne.ai blog posts, IBM Docs pages (several inaccessible per Gap 1).
- **Why information could not be found:** No single IBM source enumerates a formal persona taxonomy; role information had to be triangulated across several documents that each mention roles in the context of a specific workflow (approval, monitoring, onboarding) rather than as a standalone glossary.
- **Modelling assumptions may later be required:** Yes — `hint:Role` instances in a future Knowledge Graph will need to be defined by the research team using the functional labels documented here (see `ontology_mapping.md` §3), explicitly noting they are synthesized from workflow descriptions rather than copied from an official role glossary.

## Gap 3: Independently verified customer case-study detail

- **Missing information:** Concrete, detailed operational descriptions of how named IBM customers (e.g., USTA, Deloitte, referenced in passing in E-012's surrounding search results) actually configured and used watsonx.governance in production — including scenario-specific metrics, timelines, or outcomes attributable to a single, identifiable deployment.
- **Searches performed:** `watsonx.governance case study USTA Deloitte customer story AI risk`.
- **Sources consulted:** IBM "Governing AI with Confidence" announcement (E-012, fetched — contained only a general cross-functional-collaboration statement, no case-specific detail); IBM client-quotes page (listed in search results but not fetched in depth, as available snippets suggested only short pull-quotes rather than operational detail); IntelligentHQ commentary (rejected as opinion/ethics commentary, not primary case evidence); Deloitte–IBM alliance marketing page (rejected, partner-marketing content without watsonx.governance-specific operational detail).
- **Why information could not be found:** Available customer references in vendor materials were name-drops or short testimonial quotes rather than full case studies with reproducible scenario detail; a genuine case-study document was not located within the source-priority tiers available (official docs, engineering blog, research papers).
- **Modelling assumptions may later be required:** No — the five scenarios in `scenarios.md` were deliberately built from general product-mechanics evidence (which is well documented) rather than from a specific named customer deployment, avoiding the need to assume unverified case-study specifics.

## Gap 4: Official demo/conference-presentation transcripts and downloadable whitepapers

- **Missing information:** No official IBM product demo video transcript, conference talk (e.g., IBM Think conference session), or standalone downloadable whitepaper PDF specific to watsonx.governance was retrieved and read as text within this session.
- **Searches performed:** General product searches surfaced an IBM Mediacenter video page (`mediacenter.ibm.com`) and an "IBM's forms" demo-request page (`ibm.com/forms/mkt-demo-dataaiwatsonxgov`), neither of which exposes transcribable textual content through the available tools.
- **Sources consulted:** IBM Mediacenter video landing page (media asset, not text-extractable); IBM demo-request form page (gated content, requires form submission, not accessed).
- **Why information could not be found:** These source types require either video-transcript extraction capability (not available in this session) or form-gated access (declined, as this phase must remain non-interactive/non-account-based per the research protocol's emphasis on publicly documentable evidence).
- **Modelling assumptions may later be required:** No direct modelling impact — the product-mechanics detail these sources would likely have covered was independently corroborated through official docs and engineering-blog sources (Source Priority Tiers 1–2), so this gap is a documentation-completeness gap rather than a knowledge gap that blocks scenario modelling.

## Gap 5: Explicit, documented data-flow / integration mechanism between watsonx Orchestrate (agent runtime) and the watsonx.governance Governance Console

- **Missing information:** The fetched watsonx Orchestrate governance-and-observability page (E-017) describes a control plane, audit logs, and runtime metrics, but does not explicitly state *how* (or whether) that runtime telemetry is automatically synchronized into the watsonx.governance Governance Console's Model Risk Governance / AI Factsheet records, versus being a separate, parallel governance surface.
- **Searches performed:** `watsonx.governance watsonx orchestrate agent monitoring integration IBM`.
- **Sources consulted:** `ibm.com/products/watsonx-orchestrate/governance-and-observability` (fetched, E-017); `ibm.com/new/announcements/from-governance-policies-to-governance-proof-with-enforcement-tracking-for-watsonx-orchestrate` (identified in search results but not fetched in this session due to time-boxing after saturation indicators were reached); `ibm.com/new/announcements/now-ga-monitor-agents-in-runtime-in-watsonx-orchestrate` (identified but not fetched).
- **Why information could not be found:** The specific integration/data-flow announcement pages were identified but not fetched before saturation was judged reached; this is a scoping decision (see `research_log.md` §Saturation Assessment) rather than a source unavailability issue, and is flagged here so a future research pass can close it quickly.
- **Modelling assumptions may later be required:** Possibly — Scenario 4 in `scenarios.md` currently treats watsonx.governance's agentic evaluation layer and watsonx Orchestrate's control plane as complementary but not fully proven to be a single integrated data pipeline. Any Knowledge Graph representation asserting a direct `hi:evaluatedBy` link between an Orchestrate-run `hi:TaskExecution` and a watsonx.governance `hi:Evaluation` should be flagged as an inferred/assumed integration until this gap is closed.

## Gap 6: Formal null/alternative hypothesis usage in Evaluation Studio experiments

- **Missing information:** The HI Ontology's `hi:Experiment` class includes `hi:hasNullHypothesis` and `hi:hasAlternativeHypothesis` datatype properties. No IBM source describes Evaluation Studio or the Model Risk Evaluation Engine in explicit statistical-hypothesis-testing terms (null vs. alternative hypothesis); the evidence describes comparative scoring and ranking, not formal hypothesis tests.
- **Searches performed:** Covered implicitly within Search 8 and Search 14 (see `research_log.md`); no dedicated search for "hypothesis testing" terminology was run separately, since the general Evaluation Studio and Model Risk Evaluation Engine searches did not surface this terminology.
- **Sources consulted:** E-010 (Evaluation Studio), E-014 (Model Risk Evaluation Engine).
- **Why information could not be found:** IBM's public-facing documentation for these tools is written in product/metric terms (scores, thresholds, rankings), not in formal experimental-design terms.
- **Modelling assumptions may later be required:** Yes — `ontology_mapping.md` §9 already flags this mapping as **Inferred, Low-Medium confidence**. Any future SHACL shape or KG instance populating `hi:hasNullHypothesis`/`hi:hasAlternativeHypothesis` for a watsonx.governance experiment would need to be constructed by the research team (e.g., phrasing "Model/Prompt A does not outperform Model/Prompt B on Faithfulness" as an assumed null hypothesis), not sourced directly from IBM documentation.

## Gap 7: Precise definition and thresholds of "System Drift" and "Query Translation Faithfulness" for agentic systems

- **Missing information:** E-007 names these two agent-specific metrics but only provides one-sentence functional descriptions ("track whether agents are operating and inferring as intended" for System Drift; confirms agents "understood user questions correctly without hallucination" for Query Translation Faithfulness) without a precise mathematical definition, default threshold, or computation method.
- **Searches performed:** Covered within Search 8/10/12 (agentic governance searches); no dedicated deep-dive search for these two specific metric names was performed after their initial discovery, since deeper technical/API documentation (e.g., the `ibm-watsonx-gov` SDK's metric reference) was not fully accessible (see Gap 8 and R-13 in `sources.md`).
- **Sources consulted:** E-007 only.
- **Why information could not be found:** The underlying technical reference (likely the `ibm-watsonx-gov` SDK API documentation or its Python docstrings) was not retrievable in sufficient depth through the GitHub landing page (R-13 in `sources.md`).
- **Modelling assumptions may later be required:** Yes — if a future SHACL constraint needs a numeric threshold or computation formula for these metrics, this must be sourced from the SDK's actual code/API reference (out of scope for this session) rather than assumed.

## Gap 8: Full metrics/evaluator catalogue from the `ibm-watsonx-gov` SDK

- **Missing information:** A complete, authoritative enumeration of every metric class implemented in the open-source `ibm-watsonx-gov` SDK (beyond the metric names surfaced piecemeal across E-004, E-006, E-007, E-010, E-011).
- **Searches performed:** Search 6 (`github.com/IBM/ibm-watsonx-gov`), including an attempted fetch of the raw README.
- **Sources consulted:** GitHub repository landing page; raw README.md (both fetched, both returned only the one-line SDK description without the deeper notebook/API content).
- **Why information could not be found:** The tool used to fetch web content renders the GitHub page as a static landing view; the referenced Jupyter notebooks with the full metrics catalogue were not individually navigated to and fetched within this session's scope (a large number of notebook files would need to be enumerated and fetched individually, which was judged to exceed the marginal value once saturation indicators appeared — see `research_log.md`).
- **Modelling assumptions may later be required:** Possibly — the metric list compiled in `ontology_mapping.md` §10 (`hint:Metric` row) should be treated as **representative, not exhaustive**. A future research pass focused specifically on Knowledge Graph construction should enumerate the SDK's notebooks directly (e.g., via `github.com/IBM/ibm-watsonx-gov/tree/samples`) to obtain the complete, authoritative metric catalogue before finalizing SHACL shapes that constrain `hint:Metric` values.

---

## Summary Table

| Gap # | Topic | Blocks Scenario Modelling? | Requires Future Modelling Assumption? |
|---|---|---|---|
| 1 | OpenPages MRG UI workflow detail | No (coarser-grain workflow already evidenced) | Possibly, if fine-grained state machine needed |
| 2 | Formal persona/role glossary | No (functional roles sufficiently evidenced) | Yes, for `hint:Role` instance definitions |
| 3 | Verified customer case studies | No (scenarios built from general mechanics) | No |
| 4 | Demo/conference transcripts, whitepapers | No | No |
| 5 | Orchestrate ↔ Governance Console integration mechanism | Partially (Scenario 4 integration claim) | Yes, if asserting a direct KG link |
| 6 | Null/alternative hypothesis usage | No | Yes, if populating those two datatype properties |
| 7 | System Drift / Query Translation Faithfulness precise definitions | No | Yes, if numeric thresholds needed |
| 8 | Full SDK metrics catalogue | No (representative list sufficient for scenario modelling) | Yes, before finalizing SHACL metric constraints |

None of these gaps required inventing unsupported facts. Where a scenario or mapping needed to bridge a gap to remain complete, the bridging statement is explicitly labelled **[Assumption]** and confidence-scored in `scenarios.md` and `ontology_mapping.md`, consistent with protocol §11, §12, and §15.
