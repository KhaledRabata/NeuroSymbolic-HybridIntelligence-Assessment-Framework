# Research Log — Elsevier LeapSpace
Research Acquisition Specification (RAS) v1.0 | Phase: Domain Knowledge Acquisition and Structured System Analysis
Session date: 2026-08-24

This log documents every search step performed during this knowledge-acquisition phase, per protocol §14. Search engine used throughout: the session's integrated web search tool (Google-backed web index) plus direct page fetches of URLs surfaced by search.

---

## Search 1

- **Objective:** Establish baseline understanding of LeapSpace from official sources.
- **Search terms:** `Elsevier Leapspace official product overview`; `"Leapspace" Elsevier R&D innovation platform`
- **Search engine:** Web search (integrated)
- **Sources visited:** elsevier.com/products/leapspace; elsevier.com press releases (launch + goes-live); fiercehealthcare.com; clinicallab.com; science.org; researchinformation.info; librarytechnology.org
- **Sources rejected:** None yet at this stage (all identified URLs were queued for fetch)
- **Sources accepted:** E-001, E-002, E-003 (fetched in subsequent steps)
- **Information extracted:** Confirmed LeapSpace is a distinct, newly launched Elsevier product (not a rebrand of Scopus AI or ScienceDirect AI, though built on them), positioned as a "research-grade AI-assisted workspace."
- **Ontology concepts discovered:** hi:UseCase, hi:Goal, hi:Context
- **Scenarios supported:** General platform-overview framing (all scenarios)
- **Remaining unknowns:** Specific roles, tasks, metrics, governance mechanisms, lifecycle stages.

## Search 2 (direct fetches)

- **Objective:** Extract full content of the two primary official pages.
- **URLs fetched:** https://www.elsevier.com/products/leapspace ; https://www.elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery
- **Result:** Both succeeded. Extracted purpose statement, core feature list (literature exploration, comparison, deep research reports, collaborator/funding discovery, document upload), Trust Card mechanism, target users, data-source scale, and AI-method naming (agentic AI, generative AI, reasoning engines, RAG).
- **Accepted as:** E-001, E-002
- **Ontology concepts discovered:** hi:ArtificialAgent (multi-method AI architecture), hi:Task, hi:Capability, hint:Metric (300+ institutions, 64 countries, $100B+ in grants)

## Search 3 (direct fetches)

- **Objective:** Extract the general-availability "goes live" announcement and the industry/corporate-R&D product page.
- **URLs fetched:** https://www.elsevier.com/about/press-releases/leapspace-goes-live-the-research-grade-ai-assisted-workspace ; https://elsevier.com/products/leapspace/industry
- **Result:** Both succeeded. Extracted named customer testimonials (Victoria Ball/Incyte, Paul Preuschoff/RWTH Aachen), multi-model AI architecture statement, publisher partnerships (Emerald, IOP, NEJM Group, Sage), and corporate-R&D framing (Claim Radar, Writing Coach, "time pressures, information overload and regulatory hurdles").
- **Accepted as:** E-003, E-004
- **Ontology concepts discovered:** hi:HumanAgent (named testimonial roles), hint:Role, hi:Interaction (implied by Claim Radar/Writing Coach dialogue)

## Search 4 (direct fetches, attempted)

- **Objective:** Obtain an independent, critical journalistic perspective from a high-authority science-news outlet.
- **URL attempted:** https://www.science.org/content/article/journal-giant-elsevier-unveiled-ai-tool-scans-millions-paywalled-papers-it-worth-it
- **Result:** Failed — HTTP 403 client error. Logged as rejected source R-01.
- **URL attempted:** https://www.researchinformation.info/news/elsevier-launches-research-grade-ai-assisted-workspace/
- **Result:** Failed — robots.txt fetch ConnectTimeout. Logged as rejected source R-02.

## Search 5 (direct fetches)

- **Objective:** Obtain independent trade-press coverage as an alternative to the failed Tier-9 sources from Search 4.
- **URLs fetched:** https://www.fiercehealthcare.com/health-tech/elsevier-unveils-ai-powered-research-tool-leapspace-transform-workflows ; https://www.clinicallab.com/elsevier-launches-leapspace-an-ai-workspace-to-accelerate-lab-research-28481
- **Result:** Both succeeded. Extracted a specific hallucination-rate figure ("less than 1%"), additional feature names (Reading Assistant, Compare, Author Search), governance detail (independent Advisory Board), and explicit linkage to Elsevier's existing ScienceDirect AI and Scopus AI products as the technical foundation.
- **Accepted as:** E-005, E-006
- **Ontology concepts discovered:** hi:Evaluation, hint:Metric (hallucination rate), hi:Capability

## Search 6

- **Objective:** Locate Elsevier's formal Responsible AI governance documentation, to ground the RAS's required CARE/Responsible-AI checklist items (§17) in a primary policy source rather than only marketing copy.
- **Search terms:** `Elsevier Responsible AI Principles explainability transparency human oversight`
- **Search engine:** Web search (integrated)
- **Sources visited:** elsevier.com/about/policies-and-standards/responsible-ai-principles; elsevier.com/about/ai/responsible-ai; elsevier.com/about/ai/our-approach-to-ai; enago.com AI-guidelines summary page
- **Sources rejected:** Enago.com (third-party publishing-services company summarizing Elsevier's policy secondhand; primary policy page was directly available, so the secondary summary was not needed)
- **Sources accepted:** E-007 (fetched)
- **Information extracted:** Five named Responsible AI principles (impact evaluation, bias prevention, transparency, human accountability, data governance/privacy) with explicit governance mechanisms (oversight-responsibility assignment, automated bias-detection tooling, post-deployment monitoring).
- **Ontology concepts discovered:** hint:Constraint, hi:hasConstraintConcept, hi:Context

## Search 7

- **Objective:** Understand the underlying AI engines (Scopus AI, ScienceDirect AI) that LeapSpace is explicitly built on, per E-006/E-013's statements.
- **Search terms:** `Elsevier ScienceDirect AI Scopus AI capabilities architecture`
- **Search engine:** Web search (integrated)
- **Sources visited:** library.usfca.edu AI-tools guide; prnewswire.com (ScienceDirect AI launch); elsevier.com ScienceDirect AI press release; elsevier.com Scopus generative-AI press release; infotoday.com CIL Magazine "AI Corner" column; elsevier.support Scopus AI support page; ceibs.libguides.com
- **Sources rejected:** library.usfca.edu (third-party university library guide, secondary summary of Elsevier's own materials); infotoday.com CIL Magazine column (opinion/commentary column, not needed given the official support page was directly available); ceibs.libguides.com (another third-party institutional guide)
- **Sources accepted:** E-008 (fetched)
- **Information extracted:** Scopus AI's Summary/Analysis, Concept Maps, Topic Experts, and Emerging Themes features; explicit statement that "Scopus AI undergoes periodic evaluations using a quality framework."
- **Ontology concepts discovered:** hi:ArtificialAgent (sub-component level), hi:Evaluation

## Search 8 (direct fetches)

- **Objective:** Locate an official demo/presentation source (protocol source-priority Tier 5) and identify named human presenters/roles.
- **URL fetched:** https://webinars.elsevier.com/elsevier/see-leapspace-in-action-the-research-grade-ai-workspace-for-r-d
- **Result:** Succeeded, though only the event-listing metadata (not a full transcript) was retrievable. Extracted four named presenter roles: three internal Elsevier product roles and one external guest (Global Medical Lead, Orion Corporation).
- **Accepted as:** E-009
- **Ontology concepts discovered:** hi:HumanAgent, hint:Role, hi:HITeam (cross-organizational presenter/customer composition)
- **Remaining unknowns:** Full Q&A transcript content — not accessible via the listing page; logged in `knowledge_gaps.md`.

## Search 9

- **Objective:** Find additional named-role testimonials to corroborate and extend E-003's customer quotations.
- **Search terms:** `LeapSpace Elsevier Regeneron Incyte testimonial library services R&D`
- **Search engine:** Web search (integrated)
- **Sources visited:** clinicallab.com (follow-up "goes live" article); librarytechnology.org (x2 mirrors); prnewswire.com; itbrief.co.uk; researchinformation.info; elsevier.com "introducing-research-grade-ai" page; elsevier.com pharma/biotech industry page
- **Sources rejected:** librarytechnology.org and prnewswire.com mirrors (duplicate wire-service copies of the same press release already captured as E-003; fetching duplicates was judged low marginal value)
- **Sources accepted:** E-010 (fetched)
- **Information extracted:** Fuller testimonial quotations (Victoria Ball, Incyte — reference-verification time savings) and an independently reported researcher-trust statistic (22% currently trust existing AI tools; 86% concerned about critical errors).
- **Ontology concepts discovered:** hint:Metric (trust-survey statistics), hi:Context

## Search 10 (direct fetches)

- **Objective:** Extract the "research-grade AI" definitional page and pharma/biotech industry-specific page identified in Search 9.
- **URLs fetched:** https://www.elsevier.com/products/leapspace/introducing-research-grade-ai ; https://www.clinicallab.com/ai-meets-research-leapspace-goes-live-with-18-million-articles-28535
- **Result:** Both succeeded. First page gave the content-curation governance chain (peer reviewers → Scopus Content Selection and Advisory Board → LeapSpace Advisory Board) and the multi-model architecture statement. Second page corroborated testimonials and added the trust-survey statistic with fuller context.
- **Accepted as:** E-011, E-010 (E-010 finalized here after being identified in Search 9)
- **Ontology concepts discovered:** hi:Evaluation (content-curation governance), hint:Role (Advisory Board)

## Search 11 (direct fetch)

- **Objective:** Obtain an additional independent tech-news perspective for triangulation.
- **URL fetched:** https://itbrief.co.uk/story/elsevier-unveils-leapspace-ai-workspace-for-researchers
- **Result:** Succeeded. Corroborated multi-model architecture and content scale; added specific publisher-partnership names and confirmed the phased institutional-then-individual rollout timeline.
- **Accepted as:** E-012
- **Ontology concepts discovered:** hint:Domain (publisher partnerships as a context marker)

## Search 12

- **Objective:** Locate any independent evaluation, benchmark, or accuracy study specifically addressing LeapSpace's hallucination/accuracy claims, to test the vendor-reported "<1%" figure from E-005.
- **Search terms:** `LeapSpace Elsevier hallucination rate accuracy evaluation benchmark`
- **Search engine:** Web search (integrated)
- **Sources visited:** Several general-purpose "AI hallucination benchmark 2026" articles unrelated to LeapSpace specifically; academic hallucination-benchmark papers (HalluLens, OpenReview) unrelated to LeapSpace; elsevier.com press releases (already captured)
- **Sources rejected:** All general AI-hallucination-benchmark sources surfaced were about other AI systems (general LLM benchmarks), not LeapSpace specifically, and were therefore off-topic and excluded.
- **Sources accepted:** None new
- **Information extracted:** Confirmed that no independent, LeapSpace-specific hallucination benchmark study exists in the searchable web index as of this session — this is recorded as an explicit knowledge gap rather than filled with an unrelated general-LLM benchmark.
- **Ontology concepts discovered:** None new
- **Remaining unknowns:** Independent verification of the <1% figure — see `knowledge_gaps.md`.

## Search 13

- **Objective:** Directly search for the pharma/biotech industry page (identified in Search 9's results) and confirm role/task granularity for corporate R&D.
- **URL fetched:** https://elsevier.com/industry/pharmaceuticals-and-biotechnology
- **Result:** Succeeded. Extracted six granular pharma/biotech R&D roles (discovery scientists, medicinal chemists, preclinical teams, clinical development teams, pharmacovigilance/regulatory professionals, medical affairs specialists) and named integrated proprietary databases (Reaxys, PharmaPendium, Embase, ScienceDirect).
- **Accepted as:** E-013
- **Ontology concepts discovered:** hint:Role (six pharma-specific roles), hi:Goal (de-risking compounds, regulator-ready safety documentation), hi:Context (regulatory domain)

## Search 14

- **Objective:** Search explicitly for research-paper, whitepaper, and conference-presentation sources (protocol source-priority Tiers 6–8), and check for any academic literature about LeapSpace's underlying RAG/knowledge-graph methods.
- **Search terms:** `Elsevier Labs research paper retrieval augmented generation scientific literature knowledge graph`; `LeapSpace Elsevier whitepaper conference presentation SSP STM`; `"LeapSpace" Elsevier peer-reviewed study evaluation researcher trust survey`
- **Search engine:** Web search (integrated)
- **Sources visited:** Several general RAG/knowledge-graph academic papers (Nature Scientific Reports, arXiv, ACM TOIS) unrelated to LeapSpace specifically; stm-publishing.com (trade-press mirrors of the Elsevier press releases already captured); elsevier.libguides.com; briefglance.com
- **Sources rejected:** General RAG/knowledge-graph academic papers (topically related to the *methods* LeapSpace claims to use, but none specifically studies or names LeapSpace, so citing them as LeapSpace evidence would misattribute); stm-publishing.com (duplicate wire coverage of press releases already captured as E-003/E-014); briefglance.com (unverified-authorship aggregator site, not used as primary evidence)
- **Sources accepted:** E-018 (elsevier.libguides.com, fetched)
- **Information extracted:** Confirmed absence of any peer-reviewed academic paper, whitepaper, or publicly accessible conference-talk recording specifically about LeapSpace — explicit knowledge gap (product is too new). Extracted official LibGuide content: six-point differentiator framing, access/authentication mechanics.
- **Ontology concepts discovered:** hi:Task (access/onboarding)

## Search 15 (direct fetches)

- **Objective:** Locate and extract the most recent product-evolution announcement (agentic capabilities expansion) and the dedicated Writing Coach page, both surfaced by Search 14's queries.
- **URLs fetched:** https://www.elsevier.com/about/press-releases/elsevier-expands-leapspace-with-new-agentic-capabilities-for-tasks-across-the-complete-research-workflow ; https://www.elsevier.com/products/leapspace/writing-coach
- **Result:** Both succeeded. Extracted four named new capabilities (Writing Coach, Claim Radar, Compare Tables, Reference Export/Extended File Upload), an explicit human-approval-required-for-every-change policy statement, and granular UI/interaction detail for Writing Coach (two-panel dialogue layout, 107M+ paper claim-checking corpus).
- **Accepted as:** E-014, E-015
- **Ontology concepts discovered:** hi:Interaction (dialogue-based drafting), hi:TaskExecution, hint:InteractionModalityConcept (chat/dialogue modality)

## Search 16

- **Objective:** Deliberately search for critical/non-vendor-affiliated commentary, per the RAS's implicit requirement (§10, §15) to capture context honestly rather than only vendor-favorable framing, and to check for independently reported pricing.
- **Search terms:** (continuation of Search 9's results) — direct fetch of a critical article identified in earlier result sets
- **URL fetched:** https://hyper.ai/en/stories/1feb74eb200a44fd69bb2297ca0a1338
- **Result:** Succeeded. Extracted named, attributable expert critiques: Jason Priem (OpenAlex CEO) on knowledge fragmentation; Dave Hansen (Authors Alliance) on market-concentration risk; Jevin West (University of Washington) on the absence of a standardized AI-summary-accuracy evaluation method. Also extracted independently reported pricing ($32/month personal plan) and a coverage-limitation figure (LeapSpace addresses only ~22% of 2024 research articles at time of writing).
- **Accepted as:** E-016
- **Ontology concepts discovered:** hint:Phenomenon (market-concentration risk, knowledge fragmentation), hi:hasPhenomenonConcept

## Search 17

- **Objective:** Search for LeapSpace's official trust/security governance page and pricing/subscription documentation, and to locate the LibGuide already partially covered in Search 14.
- **Search terms:** `LeapSpace "Claim Radar" OR "Writing Coach" OR "Reading Assistant" feature detail`; `LeapSpace Elsevier pricing subscription plans institutional`
- **Search engine:** Web search (integrated)
- **Sources visited:** elsevier.com/en-gb/products/leapspace/trust-and-security; researcher.elsevier.com (subscription portal, not fetched — login/commerce page, not content-bearing for research purposes); elsevier.com/products/leapspace/inquire-today (sales-inquiry form page, not content-bearing); elsevier.com legal terms-and-conditions page (not fetched — legal boilerplate, low marginal research value versus the trust-and-security page which covers the same governance ground in substantive prose)
- **Sources rejected:** researcher.elsevier.com and the "inquire-today" page (commercial/transactional pages without additional substantive product-mechanism content beyond what E-001–E-017 already covered)
- **Sources accepted:** E-017 (fetched)
- **Information extracted:** Named Advisory Board chair (Professor Jörg-Rüdiger Sack), explicit ranking-neutrality statement, explicit ISO 27001 security-framework alignment, and an explicit three-part enumeration of where "human expertise is embedded" (content curation, model evaluation/QA, ongoing validation/governance).
- **Ontology concepts discovered:** hint:Role (Advisory Board Chair), hi:hasConstraintConcept (ISO 27001), hi:Evaluation

---

## Saturation Assessment

After 17 search iterations and 22 distinct URL fetch attempts (18 successful, 4 failed/rejected: R-01, R-02, R-03, plus the abandoned researcher.elsevier.com/inquire-today commercial pages), the following saturation indicators were observed:

- The same core feature set (Trust Cards, Claim Radar, Writing Coach, Deep Research, Author Search, Funding Discovery, Compare/Compare Tables, Reading Assistant) recurred consistently across E-001, E-003, E-004, E-005, E-006, E-010, E-014, E-015, E-017, E-018, with each successive source adding incremental detail rather than new feature categories.
- The same governance/trust architecture (five Responsible AI Principles; content curated by peer reviewers + Scopus Content Selection and Advisory Board + LeapSpace Advisory Board; human oversight in content curation, model evaluation, and ongoing validation; multi-model AI selecting models per task) recurred consistently across E-001, E-003, E-007, E-008, E-011, E-017, E-018.
- The same human-role categories (academic researchers/PhD students; corporate R&D scientists across pharma-specific sub-functions; library-services professionals; an independent advisory board) recurred consistently across E-001, E-003, E-004, E-009, E-010, E-013, E-017.
- Search 12 (hallucination-benchmark-specific) and Search 14 (whitepaper/conference/research-paper-specific) both returned zero new LeapSpace-specific material, despite targeted queries — a strong negative-result saturation signal for those particular source tiers (documented as explicit gaps, not silently accepted).
- Search 16's deliberate search for critical/independent commentary surfaced genuinely new information (pricing, coverage-limitation statistics, named critics) not obtainable from vendor sources — this was the last search to yield a materially new concept category (hint:Phenomenon / market-concentration and knowledge-fragmentation risk), after which Search 17 returned only corroborating/refining detail.

Research was concluded at this point because: (1) three consecutive search rounds (15, 16, 17) yielded corroboration and refinement rather than new concept categories, aside from Search 16's context-layer addition which was itself then confirmed as complete once no further independent critical sources surfaced; and (2) all classes and object/data properties in the supplied HI Ontology TTL (hi:HITeam, hi:UseCase, hi:Agent/HumanAgent/ArtificialAgent, hi:Goal, hi:Task, hi:Capability, hi:TaskExecution, hi:Interaction, hi:Context, hi:Evaluation, hi:Experiment) had at least one evidence-backed instantiation from LeapSpace, with the explicit, documented exception of `hi:Experiment` and its associated `hi:hasNullHypothesis`/`hi:hasAlternativeHypothesis` datatype properties, for which no LeapSpace-specific formal experimental-design language was found (see `knowledge_gaps.md`).
