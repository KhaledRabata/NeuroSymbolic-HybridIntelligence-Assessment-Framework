# Sources — LeapSpace by Elsevier

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **LeapSpace (Elsevier)**
Complete source inventory for the Domain Knowledge Acquisition phase. Sources are listed in the order they were consulted. Each entry states Title, URL, Type, Quality Assessment, Relevance, and the Hybrid Intelligence (HI) ontology concepts it supports. Evidence IDs (E-0xx) assigned here are referenced throughout `scenarios.md`, `extractionsheet.csv`, `ontology_mapping.md`, and `knowledge_gaps.md`.

---

## A. ACCEPTED SOURCES

### E-001 — LeapSpace | The research-grade AI workspace
- **Title:** LeapSpace | The research-grade AI workspace
- **URL:** https://www.elsevier.com/products/leapspace/introducing-research-grade-ai
- **Type:** Official vendor documentation (product overview page)
- **Quality Assessment:** High. Primary vendor source; the single richest page for feature enumeration (Writing Coach, Trust Cards, Claim Radar, Deep Research, Reading Assistant, Compare, Funding Discovery, Author Search) with direct quotations.
- **Relevance:** Core scope definition for the whole use case.
- **Ontology concepts supported:** `hi:UseCase`, `hi:HITeam`, `hi:ArtificialAgent` (multi-model AI approach), `hi:Task` (writing coaching, deep research, comparison, funding search, author search), `hi:Capability` (trust/transparency), `hi:Context` (data privacy/security).

### E-002 — LeapSpace | Research-grade AI for universities and industry R&D
- **URL:** https://www.elsevier.com/products/leapspace
- **Type:** Official vendor documentation (product landing page)
- **Quality Assessment:** High. Corroborates E-001 with additional phrasing on human oversight ("Experts involved in content curation, model evaluation, and validation") and target-user segmentation.
- **Relevance:** Confirms core capabilities and human-oversight roles.
- **Ontology concepts supported:** `hi:HumanAgent` (curators, evaluators, validators), `hi:Task` (research exploration, document analysis), `hi:Context` (institutional vs. individual subscription).

### E-003 — LeapSpace goes live: the Research-Grade AI-Assisted Workspace built on trusted science
- **URL:** https://www.elsevier.com/about/press-releases/leapspace-goes-live-the-research-grade-ai-assisted-workspace
- **Type:** Official vendor documentation (press release)
- **Quality Assessment:** High. States concrete launch date (January 21, 2026), content-corpus figures, and explicit persona list including biopharmaceutical teams.
- **Relevance:** Timeline, scale, and regulated-industry persona grounding.
- **Ontology concepts supported:** `hi:Context` (regulatory compliance for biopharma), `hi:HumanAgent` (biopharmaceutical R&D teams), `hi:ArtificialAgent` (multi-model AI architecture).

### E-004 — LeapSpace: Try for free or subscribe
- **URL:** https://researcher.elsevier.com/
- **Type:** Official vendor documentation (subscription/pricing page)
- **Quality Assessment:** High. Direct enumeration of feature bundle per pricing tier and explicit core-workflow list.
- **Relevance:** Confirms the full feature inventory and links features to concrete user workflows.
- **Ontology concepts supported:** `hi:Task` (literature discovery, research planning, writing support, funding search), `hi:Capability` (unlimited search, deep research, trust cards).

### E-005 — Elsevier Launches LeapSpace: an AI-Assisted Workspace to Accelerate Research and Discovery
- **URL:** https://www.elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery
- **Type:** Official vendor documentation (press release)
- **Quality Assessment:** High. Richest single source for AI architecture ("Agentic AI, Generative AI, Reasoning engines, Retrieval-augmented generation"), Advisory Board governance statement, and development/validation methodology ("Thousands of researchers from 300+ institutions in 64 countries participated in the development and testing").
- **Relevance:** Core evidence for AI architecture, governance, and pre-launch validation process.
- **Ontology concepts supported:** `hi:ArtificialAgent` (agentic/generative/RAG components), `hi:HumanAgent` (Advisory Board, beta-test researchers), `hi:Evaluation` (development/testing validation), `hi:Interaction` (researcher feedback episodes).

### E-006 — Elsevier Launches LeapSpace, an AI Workspace to Accelerate Lab Research (Today's Clinical Lab)
- **URL:** https://www.clinicallab.com/elsevier-launches-leapspace-an-ai-workspace-to-accelerate-lab-research-28481
- **Type:** High-quality technical/trade press article
- **Quality Assessment:** Medium-High. Independent trade publication; adds a named, quotable testimonial from a real deployment (Cure Sanfilippo Foundation) not found verbatim on Elsevier's own pages.
- **Relevance:** Rare-disease-research persona and real-world testimonial grounding for evidence-synthesis scenarios.
- **Ontology concepts supported:** `hi:HumanAgent` (Chief Science Officer, rare-disease nonprofit researcher), `hi:Context` (rare-disease/low-evidence-volume research), `hi:Goal` (confidence in accuracy/rigor of outputs).

### E-007 — Research with confidence: Introducing Claim Radar
- **URL:** https://www.elsevier.com/products/leapspace/resources/research-with-confidence-introducing-claim-radar
- **Type:** Official vendor documentation (feature-explainer resource)
- **Quality Assessment:** High. The single most detailed and mechanistic description of any LeapSpace feature: exact retrieval scope ("up to 40 of the most relevant sources using Scopus"), classification categories (support/contradict/mixed), UI workflow, and a user quotation.
- **Relevance:** Core evidence for the Claim Validation scenario.
- **Ontology concepts supported:** `hi:TaskExecution` (Claim Radar run), `hi:Evaluation` (support/contradict/mixed classification), `hi:Interaction` (user clicking shield icon, reviewing panel).

### E-008 — LeapSpace | How LeapSpace supports trust and security
- **URL:** https://www.elsevier.com/products/leapspace/trust-and-security
- **Type:** Official AI transparency documentation
- **Quality Assessment:** High. Names a specific, identifiable human governance role (Professor Jörg-Rüdiger Sack, Chair of the Scopus Content Selection and Advisory Board) and a specific security standard (ISO 27001) — the most concrete accountability evidence found for this system.
- **Relevance:** Core evidence for governance/oversight (`hi:HumanAgent`) and the CARE "Responsible" dimension.
- **Ontology concepts supported:** `hi:HumanAgent` (Advisory Board Chair), `hi:Context` (ISO 27001 security framework), `hi:Capability` (publisher-neutral ranking).

### E-009 — LeapSpace | What makes LeapSpace different
- **URL:** https://www.elsevier.com/products/leapspace/what-makes-leapspace-different
- **Type:** Official vendor documentation (comparison/positioning page)
- **Quality Assessment:** High. Adds passage-level citation detail ("Trust Cards now show the exact passage used to support a claim") and names a second, distinct governance body (a "new independent AI Advisory Board", separate from the Scopus CSAB).
- **Relevance:** Refines the Trust Card mechanism and the two-Advisory-Board governance structure.
- **Ontology concepts supported:** `hi:Evaluation` (passage-level source attribution), `hi:HumanAgent` (AI Advisory Board, distinct from Scopus CSAB), `hi:Context` (retracted-article exclusion policy).

### E-010 — Six ways LeapSpace can help you move from curiosity to discovery faster
- **URL:** https://www.elsevier.com/en-gb/products/leapspace/resources/6-ways-leapspace-can-help-you-move-from-curiosity-to-discovery-faster
- **Type:** Official vendor documentation (use-case resource guide)
- **Quality Assessment:** High. The single richest source in the entire research effort: six fully worked use cases each with concrete tasks, quotations, and stated outputs.
- **Relevance:** Directly supplies the evidentiary backbone for Scenarios 1, 2, 3, 4, 5, and 6.
- **Ontology concepts supported:** `hi:Task` (literature review, topic exploration, evidence synthesis, claim validation, cross-disciplinary search, funding search), `hi:Goal` (per use case), `hi:Evaluation` (Trust Cards, Claim Radar), `hi:Capability` (natural-language search, semantic+keyword blending).

### E-011 — LeapSpace for R&D (Industry)
- **URL:** https://www.elsevier.com/products/leapspace/industry
- **Type:** Official vendor documentation (industry-segment landing page)
- **Quality Assessment:** High. Names a real, identifiable corporate persona/quote source (Samantha Intriligator, Manager, Regeneron Pharmaceuticals) and states industry-specific trust/compliance framing (traceable citations, IP safeguarding, no training on proprietary data).
- **Relevance:** Core evidence for the corporate/regulated-R&D scenario (Scenario 8).
- **Ontology concepts supported:** `hi:HumanAgent` (R&D scientist, library/information-services manager), `hi:Context` (corporate IP protection, regulatory/compliance), `hi:Task` (evidence verification, drafting/argumentation).

### E-012 — A Look Under the Hood of Scopus AI: An Interview with Maxim Khan (The Scholarly Kitchen)
- **URL:** https://scholarlykitchen.sspnet.org/2024/07/25/interview-with-maxim-khan-about-scopus-ai/
- **Type:** Peer-adjacent industry publication interview (independent scholarly-communications blog, interviewing an Elsevier technical lead)
- **Quality Assessment:** Medium. High-quality and technically detailed, but describes **Scopus AI**, a related and earlier Elsevier product that LeapSpace's own marketing material explicitly says it draws on/extends (LeapSpace content is "Scopus-indexed" and pulls from Scopus). It is **not** a direct description of LeapSpace's own architecture. Used only as background/Inferred technical context, never as Observed fact about LeapSpace itself.
- **Relevance:** Plausible architectural analogue (RAG search+rerank+LLM pipeline, hallucination/bias evaluation framework, alpha-testing methodology) for LeapSpace's own (undocumented) internal architecture.
- **Ontology concepts supported:** `hi:ArtificialAgent` (RAG pipeline: search module, reranker, LLM module) — **Inferred applicability to LeapSpace, Medium confidence**.

### E-013 — 4 tips for optimizing your LeapSpace prompts
- **URL:** https://www.elsevier.com/products/leapspace/resources/4-tips-for-optimizing-your-leapspace-prompts
- **Type:** Official vendor documentation (help/usage-tips resource)
- **Quality Assessment:** High. Concrete, mechanistic detail not found elsewhere: conversational memory window ("approximately the last five exchanges"), the two response modes (Standard vs. Deep Research), and worked filter-query examples.
- **Relevance:** Core evidence for the Interaction mechanics of every conversational scenario.
- **Ontology concepts supported:** `hi:Interaction` (multi-turn dialogue, `hi:hasInteractionModalityConcept` "Natural Language Chat"), `hi:TaskExecution` (mode selection: Standard vs. Deep Research), `hi:Capability` (filtered/faceted natural-language search).

### E-014 — Responsible AI principles (Elsevier Policy)
- **URL:** https://www.elsevier.com/about/policies-and-standards/responsible-ai-principles
- **Type:** Official AI transparency documentation (formal corporate policy)
- **Quality Assessment:** High. The most authoritative, formally worded source in the package — five explicitly named principles with implementation detail, directly usable for the CARE-framework mapping.
- **Relevance:** Primary grounding for the "Responsible," "Explainable," and (partially) "Accountable" dimensions across all scenarios.
- **Ontology concepts supported:** `hi:Context` (governance policy), `hi:Capability` (explainability, bias-prevention), `hi:HumanAgent` (accountable human decision-maker, oversight-responsibility holder).

### E-015 — Ensuring Responsible AI Use and Data Privacy in Elsevier's AI Tools (AI Use FAQ)
- **URL:** https://www.elsevier.com/about/responsible-ai/ai-use-faq
- **Type:** Official AI transparency documentation (FAQ)
- **Quality Assessment:** High. Concrete technical security detail (AES-256, TLS 1.2+, zero-retention contracts with foundation-model providers) not found elsewhere, explicitly stated to apply to LeapSpace.
- **Relevance:** Data-governance and privacy evidence for every scenario involving file upload or proprietary-document analysis.
- **Ontology concepts supported:** `hi:Context` (GDPR/CCPA compliance, zero-retention data contracts).

### E-016 — LeapSpace — AI Literacy Toolkit (Rensselaer Polytechnic Institute Library Guide)
- **URL:** https://guides.lib.rpi.edu/ai-literacy/leapspace
- **Type:** Independent, high-quality technical article (university library research guide)
- **Quality Assessment:** High. Independent (non-Elsevier) source that provides the clearest available definitions of two features (Reading Assistant, Compare Experiments) including the exact table columns Compare Experiments produces (goals, materials, methods, results, conclusions).
- **Relevance:** Core evidence for Reading Assistant and Compare Experiments, used in Scenario 8.
- **Ontology concepts supported:** `hi:Task` (article analysis/summarization, experiment comparison), `hi:TaskExecution` (structured comparison table generation).

### E-017 — LeapSpace Use Cases and Prompts Guide (LeapSpace Support Center)
- **URL:** https://www.elsevier.support/leapspace/answer/leapspace-use-cases-and-prompts-guide
- **Type:** Official help/support documentation
- **Quality Assessment:** Medium. Confirms the existence and cross-industry scope (engineering, energy, pharma, biotech, MedTech) of an official use-case/prompt library, but the substantive content lives in a downloadable PDF that was not directly retrievable through automated fetch in this research window.
- **Relevance:** Corroborates the industry breadth claimed in E-011; the detailed prompts themselves are a logged gap.
- **Ontology concepts supported:** `hi:Context` (cross-industry applicability: engineering, energy, pharma, biotech, MedTech).

---

## B. REJECTED / DOWN-WEIGHTED SOURCES

| Title | URL | Reason for rejection / down-weighting |
|---|---|---|
| Journal giant Elsevier unveiled an AI tool that scans millions of paywalled papers. Is it worth it? (Science/AAAS) | https://www.science.org/content/article/journal-giant-elsevier-unveiled-ai-tool-scans-millions-paywalled-papers-it-worth-it | Fetch returned HTTP 403 (access blocked); an independent critical perspective that would have been valuable (per RAS's mandate to compare findings and remove contradictions) but could not be retrieved in this research window. Logged as a gap in `knowledge_gaps.md`. |
| Elsevier Launches LeapSpace (PRNewswire, WebWire, InfoToday, LibraryTechnology.org, Medical Dialogues, FierceHealthcare, ITBrief, Research Information, Knowledgespeak) | multiple mirrors | These are syndicated/republished copies of the same Elsevier press release already captured in full via E-003 and E-005. Consulted to check for any locally-added independent commentary; none found beyond what the primary press releases already state, so not separately cited to avoid duplicate/inflated evidence counting. |
| CEIBS LibGuide — "the ultimate brain for the academic ecosystem" | https://ceibs.libguides.com/blogs/news/trainings/home/the-ultimate-brain-for-the-academic-ecosystem | Concerns Scopus AI, not LeapSpace specifically; overlaps with E-012's scope limitation and was not independently fetched to avoid redundant background-only evidence. |
| Elsevier Scopus AI Fact Sheet — Using Responsible AI Principles (PDF) | https://researcheracademy.elsevier.com/uploads/2024-08/Scopus%20AI%20-%20Fact%20Sheet%20-%20Using%20Responsible%20AI%20Principles.pdf | Identified via search but not fetched in this research window (PDF, and concerns Scopus AI rather than LeapSpace directly); logged as a partial gap since it likely contains additional Responsible-AI implementation detail transferable by analogy. |
| researcher.elsevier.com/cny/, /gbp/ (regional pricing mirrors) | https://researcher.elsevier.com/cny/ etc. | Regional currency mirrors of E-004 with identical feature content; not separately cited. |

---

## C. SOURCE COUNT SUMMARY

- Accepted sources cited with extracted evidence: **17** (E-001–E-017)
- Rejected / down-weighted sources: **5** (one blocked by HTTP 403, others redundant press-release mirrors or unfetched adjacent-product material)
- Official vendor documentation (product pages, press releases, policy, FAQ, support center): 14 accepted
- Independent high-quality technical articles (trade press, university library guide): 2 accepted
- Industry-publication technical interview (background/Inferred only): 1 accepted
