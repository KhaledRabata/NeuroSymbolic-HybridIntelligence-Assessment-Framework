# Sources Inventory — Elsevier LeapSpace
Research Acquisition Specification (RAS) — Neuro-Symbolic AI for Assessing and Improving Hybrid Intelligence Systems
Target Use Case: LeapSpace (Elsevier) | Version 1.0 | Compiled: 2026-08-24

This file is the master source-of-truth for every piece of evidence used across `scenarios.md`, `ontology_mapping.md`, and `extractionsheet.csv`. Every Evidence ID (E-###) defined here is referenced, never redefined, elsewhere in the package.

**Context note on product maturity:** LeapSpace is a very recently launched Elsevier product (preview access opened shortly before this research; institutional general availability and the "goes live" announcement, plus a subsequent "agentic capabilities" expansion, all occurred within the months immediately preceding this research date of 2026-08-24). This materially shaped source availability — see §3 and `knowledge_gaps.md`: no peer-reviewed academic paper or independent whitepaper about LeapSpace itself exists yet, so Tier 6–8 sources are legitimately absent rather than un-sought.

---

## 1. Accepted Sources (used as evidence)

### E-001
- **Title:** LeapSpace | Research-grade AI for universities and industry R&D (product page)
- **URL:** https://www.elsevier.com/products/leapspace
- **Type:** Official vendor documentation (product overview page)
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High authority (primary vendor source), promotional framing; clearly enumerates core capabilities and named features (Trust Cards, Writing Coach) consistent with other independently obtained sources.
- **Relevance:** Very High — foundational definition of purpose, features, users, and data scope.
- **Ontology Concepts Supported:** hi:UseCase, hi:Goal, hi:Task, hi:ArtificialAgent, hi:Context
- **Key quotation:** "LeapSpace™ is the research-grade AI-assisted workspace that lets researchers work faster, think deeper, and achieve more in a secure environment."
- **Key quotation:** "Trust Cards now show the exact passage used to support a claim."
- **Key quotation:** Researchers retain "full responsibility for interpretation"; "Human oversight throughout" involves experts in content curation and model validation.

### E-002
- **Title:** Elsevier Launches LeapSpace: an AI-Assisted Workspace to Accelerate Research and Discovery (press release)
- **URL:** https://www.elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery
- **Type:** Official vendor announcement
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — precise figures (300+ institutions, 64 countries, 45,000+ grants, $100B+), explicit AI-method naming, explicit availability timeline.
- **Relevance:** Very High — launch-stage baseline for scope, AI architecture, and content volume.
- **Ontology Concepts Supported:** hi:Goal, hi:ArtificialAgent, hi:Task, hint:Metric (content-scale figures), hi:Context
- **Key quotation:** "LeapSpace empowers academic and corporate researchers to uncover deeper insights, accelerate innovation, and collaborate seamlessly - in one secure environment they can trust."
- **Key quotation:** LeapSpace combines "agentic AI, generative AI, reasoning engines, and retrieval-augmented generation to support diverse research workflows."
- **Key quotation:** Draws from "100+ million Scopus records from 7,000+ global publishers" and "15+ million peer-reviewed full-text articles and books."

### E-003
- **Title:** LeapSpace goes live: the Research-Grade AI-Assisted Workspace built on trusted science (press release)
- **URL:** https://www.elsevier.com/about/press-releases/leapspace-goes-live-the-research-grade-ai-assisted-workspace
- **Type:** Official vendor announcement
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — general-availability milestone announcement with named customer testimonials (attributable individuals with titles/affiliations), explicit privacy statements, explicit multi-model architecture claim.
- **Relevance:** Very High — richest single source for trust mechanisms and named human-agent testimonials.
- **Ontology Concepts Supported:** hi:HumanAgent, hi:ArtificialAgent, hi:Capability, hint:Role
- **Key quotation:** "All insights are referenced and can be traced back to their original sources, providing provenance."
- **Key quotation:** "LeapSpace uses a multi-model AI approach, selecting models based on the task to ensure optimal outcomes."
- **Key quotation:** "Use of third-party Large Language Models (LLMs) is private; no information is stored or used to train public models."
- **Key quotation (testimonial):** "LeapSpace has also propelled me to a point in my reading I wouldn't reach otherwise" — Paul Preuschoff, HCI Researcher, RWTH Aachen University.
- **Key quotation (testimonial):** "R&D teams need quick access to verifiable scientific evidence within tight timelines" — Victoria Ball, Incyte.

### E-004
- **Title:** LeapSpace for industry R&D (product page)
- **URL:** https://elsevier.com/products/leapspace/industry
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — names specific corporate roles (Library Services managers/directors) via testimonial attribution and specific corporate-R&D pain points.
- **Relevance:** Very High — primary source for the corporate/industry R&D branch of the use case (as distinct from academic use).
- **Ontology Concepts Supported:** hi:HumanAgent, hi:Task, hi:Capability, hi:Context, hint:Domain
- **Key quotation:** "accelerate ideation and discovery, enhance decision making and optimize workflows."
- **Key quotation:** "Intense time pressures, information overload and regulatory hurdles can significantly impact R&D teams' productivity."
- **Key quotation:** "Claim Radar shows how it holds up across the broader body of research."

### E-005
- **Title:** Elsevier unveils AI-powered research tool to transform workflows
- **URL:** https://www.fiercehealthcare.com/health-tech/elsevier-unveils-ai-powered-research-tool-leapspace-transform-workflows
- **Type:** Trade/industry publication (independent editorial)
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — independent editorial synthesis; corroborates vendor-reported feature list and reports a specific hallucination-rate figure attributed to Elsevier.
- **Relevance:** High — cross-validates the < 1% "serious hallucination" figure and workflow feature list from an independent outlet.
- **Ontology Concepts Supported:** hi:Task, hi:Evaluation, hint:Metric
- **Key quotation:** LeapSpace lets users "generate ideas, plan projects, explore literature, find collaborators and identify funding opportunities."
- **Key quotation:** Risk of serious hallucination is "less than 1%."
- **Key quotation:** Oversight includes "Independent advisory board oversight ensuring algorithms remain explainable."

### E-006
- **Title:** Elsevier Launches LeapSpace, an AI Workspace to Accelerate Lab Research
- **URL:** https://www.clinicallab.com/elsevier-launches-leapspace-an-ai-workspace-to-accelerate-lab-research-28481
- **Type:** Trade/industry publication (independent editorial, life-sciences/clinical-lab trade press)
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — independent, corroborates named features (Reading Assistant, Compare, Author Search) and governance detail (independent Advisory Board) not phrased identically elsewhere, useful for triangulation.
- **Relevance:** High — clearest independent enumeration of the "efficiency tools" tier of features.
- **Ontology Concepts Supported:** hi:Task, hi:Capability, hi:HumanAgent
- **Key quotation:** "Reading Assistant, Compare, and Author Search help researchers rapidly evaluate evidence and identify collaborators."
- **Key quotation:** "An independent Advisory Board will oversee LeapSpace's transparency."
- **Key quotation:** "Every feature reflects Elsevier's Responsible AI Principles, emphasizing transparency, explainability, and human oversight."

### E-007
- **Title:** Responsible AI principles (Elsevier policy)
- **URL:** https://www.elsevier.com/about/policies-and-standards/responsible-ai-principles
- **Type:** Official vendor policy documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — formal, enterprise-wide policy document; enumerates five named principles with governance-process detail; directly maps onto the RAS's required CARE/Responsible-AI checklist items (Fairness, Accountability, Explainability, Trust).
- **Relevance:** Very High — the single most important source for the "Responsible" and "Explainable" CARE dimensions.
- **Ontology Concepts Supported:** hi:Context, hint:Constraint, hi:hasConstraintConcept, hi:Evaluation
- **Key quotation:** Five principles: "We evaluate the real-world impact of our solutions on people"; "We take action to prevent the creation or reinforcement of unfair bias"; "We support transparency and can explain how our solutions work"; "We promote accountability through meaningful human oversight"; "We respect privacy, protect intellectual property, and champion robust data governance."
- **Key quotation:** Oversight requires "Clear assignment of oversight responsibilities, effective review and understanding, capacity to intervene."
- **Key quotation:** "Use of available automated bias detection tools" and "ongoing monitoring and response after deployment."

### E-008
- **Title:** What is Scopus AI? (Scopus Support Center)
- **URL:** https://www.elsevier.support/scopus/answer/what-is-scopus-ai
- **Type:** Official vendor help/support documentation
- **Source Priority Tier:** 4 (Help/support documentation)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — official support-center reference for Scopus AI, one of the two named underlying products (alongside ScienceDirect AI) that LeapSpace is explicitly built on (per E-006, E-013); precise about feature names and quality-assurance process.
- **Relevance:** High — supplies detail on the underlying artificial-agent components (summary/analysis engine, concept maps, topic-expert identification) that LeapSpace's Author Search and Deep Research features build on.
- **Ontology Concepts Supported:** hi:ArtificialAgent, hi:Capability, hi:Evaluation
- **Key quotation:** Scopus AI generates summaries that "help reduce outputs that are factually inaccurate or unreliable" through "quality frameworks and specialized prompts."
- **Key quotation:** "Scopus AI undergoes periodic evaluations using a quality framework."
- **Key quotation:** Named outputs: "Concept Maps," "Topic Experts," "Emerging Themes" (rising/novel).

### E-009
- **Title:** Webinar: See LeapSpace™ in Action — The Research-Grade AI Workspace for R&D
- **URL:** https://webinars.elsevier.com/elsevier/see-leapspace-in-action-the-research-grade-ai-workspace-for-r-d
- **Type:** Official vendor demo/presentation listing
- **Source Priority Tier:** 5 (Official demos and presentations)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — official event listing naming presenters with job titles (internal Elsevier product roles) and one external guest speaker with role/affiliation; the deep Q&A content itself was not transcribable from the listing page (see `knowledge_gaps.md`).
- **Relevance:** High — the single clearest source for named internal-product-team human roles and one named external corporate-R&D "voice of the customer" role.
- **Ontology Concepts Supported:** hi:HumanAgent, hint:Role, hi:HITeam
- **Key quotation:** Presenters: "Cameron Ross — SVP Generative AI, Corporate Markets"; "Yoshiko Kakita — VP Product Management"; "Ben Geary — Portfolio Delivery Lead, AI Innovations"; guest "Jan Erik Timmermann — Global Medical Lead at Orion Corporation."
- **Key quotation:** "Your search queries stay private, encrypted, and never used to train LLMs."

### E-010
- **Title:** AI Meets Research: LeapSpace Goes Live with 18+ Million Articles
- **URL:** https://www.clinicallab.com/ai-meets-research-leapspace-goes-live-with-18-million-articles-28535
- **Type:** Trade/industry publication (independent editorial, follow-up coverage)
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — independent, includes fuller named testimonial quotations (with job titles) than the vendor's own press release, plus a specific researcher-trust statistic.
- **Relevance:** High — corroborates E-003's testimonials with additional direct quotation and supplies an independently reported trust statistic.
- **Ontology Concepts Supported:** hi:HumanAgent, hint:Metric, hi:Context
- **Key quotation (testimonial):** Victoria Ball, Associate Director, Global Library Services, Incyte, praised how the tool shortens reference-verification time and provides "clickable sources and clearly structured tables."
- **Key quotation:** Researcher-trust context: "only 22% currently trust existing AI tools, with 86% concerned about critical errors."

### E-011
- **Title:** LeapSpace | The research-grade AI workspace ("Introducing research-grade AI")
- **URL:** https://www.elsevier.com/products/leapspace/introducing-research-grade-ai
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — the most precise official statement of what distinguishes "research-grade AI" from general-purpose AI, and the clearest statement of the content-curation governance chain (peer reviewers → Scopus Content Selection and Advisory Board → LeapSpace Advisory Board).
- **Relevance:** Very High — core definitional source for the product's central "trust" value proposition.
- **Ontology Concepts Supported:** hi:Context, hi:Evaluation, hint:Constraint, hi:ArtificialAgent
- **Key quotation:** "Content is curated by human experts, including journal peer reviewers, the independent Scopus Content Selection and Advisory Board, and a new independent LeapSpace Advisory Board."
- **Key quotation:** "LeapSpace uses a multi-model AI approach; selecting models based on the task to support optimal outcomes and flexibility as AI technologies evolve."
- **Key quotation:** "Real-time visibility into the steps used to generate an answer, with referenced insights that can be traced back to original sources."

### E-012
- **Title:** Elsevier unveils LeapSpace AI workspace for researchers
- **URL:** https://itbrief.co.uk/story/elsevier-unveils-leapspace-ai-workspace-for-researchers
- **Type:** Independent technology-news publication
- **Source Priority Tier:** 9 (High-quality technical article)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — independent tech-news synthesis; adds specific publisher-partnership names (Emerald, IOP, NEJM Group, Sage) and confirms the corporate/institutional-only initial rollout detail.
- **Relevance:** Medium-High — corroborating source, useful primarily for triangulating content-partnership and rollout-timeline facts.
- **Ontology Concepts Supported:** hi:Context, hint:Domain
- **Key quotation:** "uses a 'multi-model' approach and selects models depending on the task."
- **Key quotation:** Licensing partnerships include "Emerald Publishing, IOP Publishing, NEJM Group, and Sage."

### E-013
- **Title:** Pharmaceuticals and biotechnology (industry page)
- **URL:** https://elsevier.com/industry/pharmaceuticals-and-biotechnology
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — the single richest source for granular, function-specific human-agent roles in the corporate R&D context, and for named integrated proprietary databases beyond the general literature corpus.
- **Relevance:** Very High — essential for the pharma/biotech-specific scenario; without this source, corporate-R&D roles would only be evidenced at a coarse "R&D team" grain.
- **Ontology Concepts Supported:** hi:HumanAgent, hint:Role, hi:Task, hi:Goal, hi:Context, hint:Domain
- **Key quotation:** Named roles: "Discovery scientists (target identification and validation)," "Medicinal chemists (hit identification to lead optimization)," "Preclinical teams (safety and translational research)," "Clinical development teams (trial design and safety monitoring)," "Pharmacovigilance and regulatory professionals (safety signal detection)," "Medical affairs specialists (evidence synthesis)."
- **Key quotation:** "LeapSpace connects with Elsevier's databases including Reaxys, PharmaPendium, Embase, and ScienceDirect for comprehensive evidence synthesis."
- **Key quotation:** Goals include to "de-risk compounds before committing to series development" and "detect safety signals earlier with regulator-ready documentation."

### E-014
- **Title:** Elsevier Expands LeapSpace™ with New Agentic Capabilities for Tasks Across the Complete Research Workflow (press release)
- **URL:** https://www.elsevier.com/about/press-releases/elsevier-expands-leapspace-with-new-agentic-capabilities-for-tasks-across-the-complete-research-workflow
- **Type:** Official vendor announcement
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — the most recent product-evolution announcement found; precisely names four new capabilities and states an explicit human-approval requirement for every AI-recommended change, which is the clearest documented `hi:Interaction`/decision-point evidence in the whole package.
- **Relevance:** Very High — primary source for the platform's shift toward agentic, multi-step AI behavior and its accompanying human-in-the-loop control mechanism.
- **Ontology Concepts Supported:** hi:ArtificialAgent, hi:Task, hi:TaskExecution, hi:Interaction, hi:Capability
- **Key quotation:** Writing Coach provides "a private and encrypted space where researchers draft, refine and strengthen their work in dialogue with an AI assistant."
- **Key quotation:** Claim Radar performs "transparent evidence verification, assessing how closely claims align with the published literature – surfacing corroborating evidence, contradictions and areas of limited or evolving consensus."
- **Key quotation:** "The researcher remains in control, with every recommended change requiring approval. No assumption is hidden; each output is verifiable."

### E-015
- **Title:** LeapSpace | Writing Coach (product page)
- **URL:** https://www.elsevier.com/products/leapspace/writing-coach
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — the most granular official description of a single LeapSpace feature found in this research pass, including UI-layout detail (two-panel editor/assistant) and an explicit statement that Claim Radar checks claims against "107M+ peer-reviewed papers."
- **Relevance:** Very High — best available source for a concrete `hi:Interaction` / `hi:TaskExecution` sequence (dialogue-based drafting with user-approved edits).
- **Ontology Concepts Supported:** hi:Interaction, hi:TaskExecution, hi:Capability, hint:InteractionModalityConcept
- **Key quotation:** "Two-panel layout, document editor on the left...Assistant tab on the right (chat with the AI, ask questions, follow up queries)."
- **Key quotation:** "Claim-level evidence checking against 107M+ peer-reviewed papers, returning sources that support, contradict, or are mixed (and labeled as such)."
- **Key quotation:** "No automatic edits — all changes are user-approved."

### E-016
- **Title:** Elsevier's AI Tool LeapSpace Offers Access to Paywalled Papers Amid Debate Over Scientific Knowledge Access and Market Dominance
- **URL:** https://hyper.ai/en/stories/1feb74eb200a44fd69bb2297ca0a1338
- **Type:** Independent technology/science-news publication (critical/analytical)
- **Source Priority Tier:** 9 (High-quality technical article) — used specifically because it is the only located source offering critical, non-vendor-affiliated expert commentary
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** Medium-High — synthesizes named, attributable expert critiques (not anonymous opinion); directly relevant to the RAS's requirement to capture "context" honestly, including limitations and contested claims, rather than only vendor-favorable framing.
- **Relevance:** High — essential counterweight source; supplies coverage-limitation figures, pricing detail absent from vendor pages, and an explicit statement that no standardized accuracy-evaluation method exists for AI-generated research summaries generally.
- **Ontology Concepts Supported:** hi:Context, hint:Phenomenon, hi:hasPhenomenonConcept, hi:Evaluation (as a documented gap)
- **Key quotation (Jason Priem, OpenAlex CEO):** "You can't understand science by only seeing a piece of it."
- **Key quotation (Dave Hansen, Authors Alliance):** "Elsevier is already huge, and this kind of collaboration could limit competition and innovation."
- **Key quotation:** Personal-plan pricing figure of "$32/month," and coverage limited to "22% of 2024 research articles."
- **Key quotation (Jevin West, University of Washington):** LLMs "are good at pleasing us, but not necessarily at being right"; "No standardized evaluation method exists for assessing AI-generated summary accuracy."

### E-017
- **Title:** LeapSpace | How LeapSpace supports trust and security
- **URL:** https://www.elsevier.com/en-gb/products/leapspace/trust-and-security
- **Type:** Official vendor documentation
- **Source Priority Tier:** 1 (Official documentation from the vendor)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — the most detailed official governance page found; names the Advisory Board chair, states the ranking-neutrality mechanism, and names the specific security-framework standard (ISO 27001) LeapSpace aligns to.
- **Relevance:** Very High — primary source for the "Accountability"/"Trust" completeness-checklist items and for the explicit human-oversight-role enumeration.
- **Ontology Concepts Supported:** hi:HumanAgent, hint:Role, hi:Evaluation, hi:hasConstraintConcept, hint:Constraint
- **Key quotation:** "Human expertise is embedded across LeapSpace, including: Content curation and selection, Model evaluation and quality assurance, Ongoing validation and governance."
- **Key quotation:** "Results are ranked based on relevance, with a small boost for recency. Publisher ownership and discipline do not influence ranking."
- **Key quotation:** Independent advisory board "led by Professor Jörg-Rüdiger Sack, Chair of the Scopus Content Selection and Advisory Board."
- **Key quotation:** "LeapSpace follows Elsevier's robust knowledge and cyber-security framework, aligned with ISO 27001 risk-management principles."

### E-018
- **Title:** Home - LeapSpace LibGuide
- **URL:** https://elsevier.libguides.com/LeapSpace
- **Type:** Official vendor help/support documentation
- **Source Priority Tier:** 4 (Help/support documentation)
- **Date Accessed:** 2026-08-24
- **Quality Assessment:** High — official librarian/end-user-facing support guide; consolidates a "six key differentiators" framing and confirms access mechanics (sign-in via institution email through ScienceDirect).
- **Relevance:** High — best available Tier-4 source; corroborates and consolidates feature claims found piecemeal elsewhere, and provides the access/authentication workflow detail no other source stated explicitly.
- **Ontology Concepts Supported:** hi:Task (access/onboarding), hi:Context, hi:Capability
- **Key quotation:** "Access LeapSpace at https://www.sciencedirect.com/leapspace" and "Sign in with your institution email or your Elsevier account information."
- **Key quotation:** "Uses only curated, peer-reviewed scholarly sources, designed to minimize hallucinations."
- **Key quotation:** "Algorithms and ranking methodologies are governed independently."

---

## 2. Rejected / Inaccessible Sources

| # | Title / URL | Reason Rejected |
|---|---|---|
| R-01 | Journal giant Elsevier unveiled an AI tool that scans millions of paywalled papers. Is it worth it? — science.org — https://www.science.org/content/article/journal-giant-elsevier-unveiled-ai-tool-scans-millions-paywalled-papers-it-worth-it | HTTP 403 client error on fetch; content not retrievable during this session. This is a notable gap since AAAS/Science is normally a high-quality independent science-journalism source — flagged in `knowledge_gaps.md`. |
| R-02 | Elsevier launches 'research-grade AI-assisted workspace' — Research Information — https://www.researchinformation.info/news/elsevier-launches-research-grade-ai-assisted-workspace/ | `robots.txt` fetch failed (ConnectTimeout) on fetch attempt; site's robots policy could not be resolved so content was not fetched, per tooling policy. |
| R-03 | Elsevier adds AI writing and evidence-checking agents to LeapSpace — Research Information — https://www.researchinformation.info/news/elsevier-adds-ai-writing-and-evidence-checking-agents-to-leapspace/ | Same `robots.txt` fetch failure as R-02; both attempts on this domain failed identically. |

Marketing/aggregator or unverified-authorship sources encountered during search (e.g., BriefGlance.com, Knowledgespeak, creati.ai, Enago's guide pages, various library-guide pages from other institutions) were reviewed only for search triangulation and were **not used as evidentiary sources**, per protocol §9, since sufficient Tier-1, Tier-4, Tier-5, and Tier-9 evidence was already obtained directly from Elsevier and from higher-confidence independent outlets (FierceHealthcare, Today's Clinical Lab, ITBrief, HyperAI).

---

## 3. Source Priority Compliance Summary

| Priority Tier | Sources Obtained | Evidence IDs |
|---|---|---|
| 1 — Official vendor documentation | 10 | E-001, E-002, E-003, E-004, E-007, E-011, E-013, E-014, E-015, E-017 |
| 2 — Vendor engineering blog | 0 | Not located as a distinct "engineering blog" channel for LeapSpace specifically; closest analogues are the press releases (Tier 1) and product pages (Tier 1) |
| 3 — AI transparency documentation | 0 (partially covered) | The Responsible AI Principles page (E-007) and Trust & Security page (E-017) jointly function as the closest available analogue to a dedicated "AI transparency documentation" artifact, but neither is titled as such |
| 4 — Help/support documentation | 2 | E-008 (Scopus AI support), E-018 (LeapSpace LibGuide) |
| 5 — Official demos/presentations | 1 | E-009 (webinar listing; full transcript not retrievable — see `knowledge_gaps.md`) |
| 6 — Peer-reviewed research papers | 0 | None located — see `knowledge_gaps.md` (product is too new to have peer-reviewed literature about it) |
| 7 — Conference talks | 0 | None located as publicly accessible transcripts/recordings — see `knowledge_gaps.md` |
| 8 — Whitepapers | 0 | No standalone downloadable whitepaper located — see `knowledge_gaps.md` |
| 9 — High-quality technical articles | 5 | E-005, E-006, E-010, E-012, E-016 |
