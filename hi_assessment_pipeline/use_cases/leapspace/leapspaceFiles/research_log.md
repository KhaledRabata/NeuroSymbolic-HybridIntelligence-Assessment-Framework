# Research Log — LeapSpace by Elsevier

Research Acquisition Specification (RAS) v1.0 | Target Use Case: **LeapSpace (Elsevier)**
Chronological log of every research step performed during the Domain Knowledge Acquisition phase, per RAS Section 14. Each entry follows the Research Protocol (RAS Section 8): identify missing knowledge → search official sources → search engineering docs → search whitepapers → search research papers → search conference/demo material → compare findings → normalise terminology → map to ontology → repeat until saturation.

Search engine used throughout: web search tool (Google-backed), supplemented by direct URL fetches of pages surfaced in results.

**Note on target system:** LeapSpace is a newly launched Elsevier product (institutional availability began January 21, 2026; individual academic/student access began February 2026), so unlike a mature enterprise platform, its documentation footprint consists almost entirely of Elsevier's own official marketing/product/policy pages plus early trade-press coverage. This is reflected honestly in `sources.md` — there is very little independent academic or peer-reviewed literature yet, which is itself logged as a finding, not concealed.

---

## Round 1 — Product Identification & Official Overview

**Objective:** Confirm what LeapSpace is (the target system was supplied only as a name), establish scope, and locate the primary official product pages.

**Search terms:**
- "LeapSpace Elsevier official"
- ""LeapSpace" Elsevier AI research platform"

**Sources visited:** elsevier.com product pages (introducing-research-grade-ai, /products/leapspace), press releases (launch, goes-live), clinicallab.com, researcher.elsevier.com, researchinformation.info, knowledgespeak.com, itbrief.co.uk.

**Sources accepted:** E-001, E-002, E-003 (initial pass; later fetched in full in Round 2).
**Sources rejected:** researchinformation.info, knowledgespeak.com, itbrief.co.uk — all syndicated summaries of the same Elsevier press release with no independent added content; not cited to avoid duplicate evidence.

**Information extracted:** LeapSpace confirmed as a "research-grade AI-assisted workspace" for academic and corporate researchers, addressing time scarcity, information overload, and AI-trust gaps; core feature names surfaced (Writing Coach, Trust Cards, Claim Radar, Deep Research, Reading Assistant, Compare, Funding Discovery, Author Search); initial persona list (academic researchers, PhD students, corporate R&D, library professionals).

**Ontology concepts discovered:** `hi:UseCase`, `hi:HITeam`, `hi:HumanAgent` (researcher personas), `hi:ArtificialAgent` (multi-model AI), `hi:Task` (feature-level tasks).

**Scenarios supported:** Seeds for all eight scenarios.

**Remaining unknowns after this round:** Mechanistic detail on Trust Cards/Claim Radar; AI architecture detail; governance/Advisory Board detail; pricing/access tiers; concrete worked use cases.

---

## Round 2 — Full Fetch of Core Product & Launch Pages

**Objective:** Extract complete detail from the three richest-looking official pages identified in Round 1.

**Sources visited (direct fetch):** elsevier.com/products/leapspace/introducing-research-grade-ai; elsevier.com/products/leapspace; elsevier.com/about/press-releases/leapspace-goes-live-the-research-grade-ai-assisted-workspace.

**Sources accepted:** E-001, E-002, E-003 (confirmed and fully extracted).

**Information extracted:** Trust Cards ("show how a claim aligns with its cited source"); Claim Radar ("shows how a claim holds up across the broader body of research"); Deep Research reports; Reading Assistant (conversational full-text interrogation); Compare Feature (experiment-breakdown tables); Funding Discovery (40,000+ opportunities); Author Search; file-upload limits (5 PDFs/conversation, private/encrypted, never used for training); multi-model AI architecture; data corpus figures (18–20+ million full-text articles, 100–107+ million Scopus abstracts, 7,000+ publishers); launch date (Jan 21, 2026, institutional; Feb 2026, individual); persona list including biopharmaceutical teams needing regulatory compliance; Judy Verses (President, Academic and Government) executive quote.

**Ontology concepts discovered:** `hi:Evaluation` (Trust Cards, Claim Radar as evaluation mechanisms), `hi:Context` (regulatory compliance for biopharma), `hi:Capability` (multi-model task-routing).

**Scenarios supported:** Seeds for Scenarios 3, 4, 8.

**Remaining unknowns:** Exact Claim Radar computation method; pricing/feature-tier detail; governance body composition; concrete step-by-step worked use cases; industry-specific (corporate) detail.

---

## Round 3 — Pricing, Subscription, and Launch-Press Corroboration

**Objective:** Fill in the feature-to-pricing-tier mapping and cross-check the launch press release for additional persona/architecture detail not in the product pages.

**Search terms:** (direct fetch, continuing from Round 2 leads)

**Sources visited:** researcher.elsevier.com (pricing page); elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery; clinicallab.com.

**Sources accepted:** E-004 (pricing/features), E-005 (richest architecture/governance source), E-006 (Cure Sanfilippo testimonial).

**Information extracted:** Free trial (14-day) and Individual plan ($320/yr) tiers; full feature bundle per tier including Mendeley AI features and "every new feature as it launches"; AI architecture explicitly named as "Agentic AI, Generative AI, Reasoning engines, Retrieval-augmented generation (RAG)"; Advisory Board oversight statement ("independent Advisory Board will oversee LeapSpace's transparency, ensuring its algorithms remain explainable and publisher-neutral"); pre-launch validation methodology ("Thousands of researchers from 300+ institutions in 64 countries participated in the development and testing"); named testimonial from Cara O'Neill MD, Chief Science Officer, Cure Sanfilippo Foundation (rare-disease research nonprofit).

**Ontology concepts discovered:** `hi:HumanAgent` (Advisory Board, beta-test researcher cohort, nonprofit Chief Science Officer), `hi:Evaluation` (pre-launch validation/testing), `hi:Context` (rare-disease/low-evidence-density research).

**Scenarios supported:** Scenario 3 (evidence synthesis — rare disease grounding), cross-cutting governance evidence for all scenarios.

**Remaining unknowns:** Precise Claim Radar/Trust Card mechanics; concrete worked task examples; corporate/industry-specific detail; formal Responsible AI policy text; prompt/interaction mechanics.

---

## Round 4 — Feature Mechanics: Claim Radar, Trust & Security, Differentiation

**Objective:** Obtain mechanistic (not just marketing-level) detail on the platform's two named trust features, and confirm governance-body composition.

**Search terms:**
- "LeapSpace "Trust Card" "Claim Radar" how it works Elsevier"
- "LeapSpace Elsevier "Deep Research" "Reading Assistant" "Compare" feature help documentation"
- "Elsevier LeapSpace Advisory Board members responsible AI governance"
- "Elsevier Scopus AI ScienceDirect AI RAG architecture trust technical whitepaper"

**Sources visited:** elsevier.com/products/leapspace/resources/research-with-confidence-introducing-claim-radar; elsevier.com/products/leapspace/trust-and-security; elsevier.com/products/leapspace/what-makes-leapspace-different; elsevier.support (Scopus AI answer, background only); scholarlykitchen.sspnet.org (Scopus AI interview); sciencedirect.com AI product page (background only, not separately cited).

**Sources accepted:** E-007 (Claim Radar mechanics), E-008 (Trust & Security, names Prof. Jörg-Rüdiger Sack as Scopus CSAB Chair, ISO 27001), E-009 (differentiation page, passage-level citations, second "AI Advisory Board" identified), E-012 (Scopus AI architecture interview — accepted as background/Inferred only, not as direct LeapSpace evidence).

**Information extracted:** Claim Radar retrieves "up to 40 of the most relevant sources using Scopus," classifies into support/contradict/mixed (neutral excluded), displays a line graph and category tabs, accessed via a shield icon; Trust and Claim Radar together form "two layers of trust: claim-to-source accuracy, and research-level context"; ISO 27001-aligned security framework; two distinct governance bodies identified — the pre-existing Scopus Content Selection and Advisory Board (chaired by Prof. Jörg-Rüdiger Sack) and a new, LeapSpace-specific independent AI Advisory Board; publisher-neutral ranking ("relevance, with a small boost for recency" only, no discipline/publisher weighting); Scopus AI's underlying RAG architecture (search module + reranking + LLM module, vector search, RAG Fusion, OpenAI GPT-4-class model hosted on private Azure, zero-retention data agreement, hallucination/bias evaluation checks, alpha-test methodology with randomly selected existing users) — logged explicitly as background evidence about a *related* Elsevier product, not a confirmed description of LeapSpace's own internals.

**Ontology concepts discovered:** `hi:Evaluation` (support/contradict/mixed classification), `hi:HumanAgent` (two distinct named/typed governance bodies), `hi:Context` (ISO 27001), `hi:ArtificialAgent` (RAG pipeline components, Inferred applicability).

**Scenarios supported:** Scenario 4 (claim validation), cross-cutting governance evidence.

**Remaining unknowns:** Concrete worked task/use-case examples with outputs; corporate/industry-specific detail; formal policy text; interaction/prompt mechanics.

---

## Round 5 — Worked Use Cases ("Six Ways") and Industry/Corporate Segment

**Objective:** Locate concrete, fully worked use-case narratives (not just feature lists) to serve as the direct evidentiary backbone for individual scenarios, and fill the corporate-R&D gap.

**Search terms:** (direct fetch of URLs surfaced in Round 4's search results)

**Sources visited:** elsevier.com/en-gb/products/leapspace/resources/6-ways-leapspace-can-help-you-move-from-curiosity-to-discovery-faster; elsevier.com/products/leapspace/industry.

**Sources accepted:** E-010 (six fully worked use cases), E-011 (industry/corporate R&D page, names Samantha Intriligator of Regeneron Pharmaceuticals).

**Information extracted:** Six worked use cases, each with quotations, concrete tasks, and stated outputs: (1) Review Literature and Stay Current, (2) Explore a New Topic or Field, (3) Synthesize Evidence and Identify Gaps (Deep Research up to 300 sources), (4) Validate Claims and Evidence Strength ("at least one reference is always required" for any claim), (5) Explore Across Disciplines (keyword + semantic/vector search blending, 330+ disciplines), (6) Find Funding Opportunities (36,000+ active grants). Industry page: personas (R&D scientists, library/information-services managers), named quote source (Samantha Intriligator, Regeneron), industry-specific trust framing (traceable citations for audit, IP safeguarding, no training on proprietary data).

**Ontology concepts discovered:** `hi:Task` (six distinct, fully specified task types), `hi:Goal` (per use case), `hi:Context` (corporate IP protection), `hi:HumanAgent` (named corporate persona).

**Scenarios supported:** Scenarios 1, 2, 3, 4, 5, 6, and corporate grounding for Scenario 8.

**Remaining unknowns:** Prompt/interaction mechanics; Reading Assistant and Compare feature detail; formal Responsible AI policy text; data-privacy technical detail.

---

## Round 6 — Interaction Mechanics, Responsible AI Policy, Data Privacy

**Objective:** Close the interaction-mechanics gap (how users actually converse with the system) and obtain the formal, citable Responsible AI policy text for CARE-framework mapping.

**Search terms:**
- "Elsevier "Responsible AI Principles" document publisher neutrality explainability"
- "Cure Sanfilippo Foundation LeapSpace case study rare disease research"
- "Regeneron Pharmaceuticals LeapSpace Elsevier library case study"
- "LeapSpace Mendeley ScienceDirect AI integration bundled features"

**Sources visited:** elsevier.support/leapspace/answer/leapspace-use-cases-and-prompts-guide; elsevier.com/about/policies-and-standards/responsible-ai-principles; elsevier.com/about/responsible-ai/ai-use-faq; elsevier.com/products/leapspace/resources/4-tips-for-optimizing-your-leapspace-prompts.

**Sources accepted:** E-013 (prompt-optimization mechanics), E-014 (formal Responsible AI Principles — five named principles), E-015 (AI Use FAQ — data privacy/security technical detail), E-017 (support-center confirmation of cross-industry use-case guide, partial).

**Sources rejected:** none new this round, though E-017's underlying PDF guide could not be fetched directly (logged as a gap).

**Information extracted:** Conversational memory window (~5 prior exchanges); Standard-summary vs. Deep-Research response modes; worked filtered-search example ("Identify trends in large language model development in Germany over the past five years. Only include papers with 25 citations or more."); five formal Responsible AI Principles (real-world impact evaluation, bias prevention, transparency, human accountability, data governance) with implementation detail on human-oversight requirements ("clear assignment of oversight responsibilities, effective review and understanding, capacity to intervene where needed"); technical data-security detail (AES-256 at rest, TLS 1.2+ in transit, GDPR/CCPA compliance, zero-retention contracts with foundation-model providers).

**Ontology concepts discovered:** `hi:Interaction` (multi-turn dialogue with bounded memory), `hi:TaskExecution` (mode selection), `hi:Context` (formal governance policy, GDPR/CCPA), `hi:HumanAgent` (accountable human decision-maker, per Responsible AI Principle 4).

**Scenarios supported:** Cross-cutting interaction and governance evidence for all eight scenarios; direct evidence for Scenario 7 (Writing Coach) interaction pattern.

**Remaining unknowns:** Reading Assistant and Compare Experiments feature-level mechanics; independent/critical perspective on the product; Author Search mechanics.

---

## Round 7 — Reading Assistant, Compare Experiments, Independent Perspective

**Objective:** Close the remaining feature-mechanics gaps (Reading Assistant, Compare Experiments, Author Search) and attempt to locate an independent, non-Elsevier critical perspective per RAS Section 8 (compare findings, remove contradictions).

**Search terms:**
- "LeapSpace "Author Search" collaborator discovery feature Elsevier"
- "LeapSpace "Reading Assistant" conversational full text article Elsevier"

**Sources visited:** guides.lib.rpi.edu/ai-literacy/leapspace (Rensselaer Polytechnic Institute library guide); science.org (AAAS) article on Elsevier's AI tool (fetch attempt).

**Sources accepted:** E-016 (RPI library guide — independent source, defines Reading Assistant and Compare Experiments with exact table-column detail).
**Sources rejected:** science.org/AAAS article — fetch returned HTTP 403 (access blocked). This was the single most promising lead for an independent, critical (non-vendor) perspective and its inaccessibility is logged as a genuine gap in `knowledge_gaps.md`, rather than silently dropped.

**Information extracted:** Reading Assistant defined as "a versatile tool for analyzing or summarizing individual articles and book chapters"; Compare Experiments defined as producing "a structured table of studies... comparing each study's goals, materials, methods, results, and conclusions"; confirmation that LeapSpace draws on both Elsevier-published content and "vetted Open Access materials validated through Scopus."

**Ontology concepts discovered:** `hi:Task` (single-article analysis, structured multi-study comparison), `hi:TaskExecution` (comparison-table generation with named output columns).

**Scenarios supported:** Scenario 8 (corporate R&D — Reading Assistant and Compare Experiments as the primary evidence-verification tools).

**Remaining unknowns after this round:** Author Search's precise ranking/matching mechanism (only the general description "explore relevant collaborators, mentors and topic contributors" was ever found, across every round); the LeapSpace Use Cases & Prompts Guide PDF content (E-017); any independent academic/peer-reviewed evaluation of LeapSpace specifically (none exists yet, consistent with the product's January 2026 launch date — this is a genuine, not a search-failure, gap).

---

## SATURATION ASSESSMENT

After 7 rounds covering 20+ distinct searches/fetches, concentrated almost entirely on official Elsevier sources (by necessity, given LeapSpace's January 2026 launch date leaves little time for independent literature to accumulate), the following saturation criteria (RAS Section 8) are judged met:

- **No new artificial-agent/feature components** emerged after Round 5 (Writing Coach, Trust Cards, Claim Radar, Deep Research, Reading Assistant, Compare Experiments, Funding Discovery, Author Search, and the underlying multi-model/agentic/RAG architecture together account for every capability named across all 17 accepted sources).
- **No new human-role archetypes** emerged after Round 6 (academic researcher, PhD student/postdoc, faculty, corporate R&D scientist, library/information-services manager, biopharmaceutical/regulatory-compliance researcher, nonprofit Chief Science Officer, and the two governance-board roles cover the full observed range).
- **No new evaluation/trust mechanisms** emerged after Round 4 (Trust Cards, Claim Radar, publisher-neutral ranking, ISO 27001 security, and the five formal Responsible AI Principles were each independently confirmed by at least two sources).
- One systematic limitation is judged genuinely unresolved rather than simply unsearched: LeapSpace is too new (institutional launch January 21, 2026) to have generated independent peer-reviewed literature, conference presentations with public recordings, or third-party audits — so RAS source-priority tiers 6–8 (peer-reviewed papers, conference talks, whitepapers) are structurally thin for this specific target system, through no lack of search effort. This is documented as GAP-05 in `knowledge_gaps.md` rather than papered over with adjacent-product material presented as direct evidence.

Research is judged to have reached practical saturation, given the product's actual maturity and documentation footprint, for the purpose of constructing eight evidence-backed, non-overlapping Hybrid Intelligence scenarios sufficient for the next pipeline phase (Knowledge Graph construction).
