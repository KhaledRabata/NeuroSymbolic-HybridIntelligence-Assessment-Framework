# Hybrid Intelligence Scenarios: Elsevier LeapSpace™

---

## S1: AI-Assisted Systematic Literature Discovery

### Scenario Name
AI-Assisted Systematic Literature Discovery

### Description
A researcher uses LeapSpace to conduct an efficient, comprehensive literature review. The researcher submits a natural language research question, optionally uploads supplementary documents, and selects standard or Deep Research mode. The LeapSpace multi-model AI system retrieves, synthesizes, and presents findings from across millions of peer-reviewed sources, generating Trust Cards for each cited claim. The researcher critically evaluates the synthesized results, inspects Trust Cards for source alignment, follows up with clarifying questions, and exports references for citation management. Human judgment governs all final research decisions while AI provides scale and speed in retrieval and synthesis.

### Goal
Accelerate literature discovery and synthesis across large corpora of peer-reviewed content while maintaining research rigor, minimising missed insights, and preserving researcher control over interpretation and judgment.

### Human Actors
- **Primary Researcher** (Academic or corporate scientist formulating research questions, evaluating results, and applying domain expertise)
- **Librarian** (Optional; information professional providing access support and guiding search strategies)

### Artificial Agents
- **LeapSpace Core AI** (Multi-model AI system orchestrating retrieval and generation pipelines)
- **RAG Engine** (Retrieval-Augmented Generation component executing semantic search and evidence retrieval)
- **Trust Card Generator** (Component producing source-to-claim alignment metadata for each cited source)
- **Deep Research Coordinator** (Multi-agent orchestrator decomposing complex queries into sub-tasks and coordinating parallel agent execution in Deep Research mode)

### Context
- Academic university research environment or corporate R&D setting
- Time-pressured research workflow with large literature volumes
- Institutional or individual subscription access to LeapSpace
- Underpinning trust gap: only 22% of researchers trust existing AI tools (Researcher of the Future Report, N=3,200+ across 113 countries)
- External validation context: LeapSpace awarded Best Generative AI Solution at 2026 CODiE Awards

### Input Data
- Natural language research question or query (text)
- Optional: uploaded PDF or Word documents (up to 5 files, 10 MB each)
- Optional: mode selection (standard vs. Deep Research)
- Optional: formatting or scope preferences

### Knowledge Sources
- Scopus abstract and citation database (107M+ peer-reviewed records from 7,000+ publishers)
- ScienceDirect full-text repository (20M+ peer-reviewed articles and book chapters)
- Partner publisher content (Emerald, IOP, NEJM Group, Sage, Oxford University Press)
- User-uploaded documents
- Daily updated content index

### Processing Method
- Natural language query parsing and intent extraction
- Retrieval-Augmented Generation (RAG) across full-text and abstract databases
- Multi-model AI selection based on task characteristics and complexity
- Deep Research mode: multi-agent decomposition of question into sub-queries, parallel execution, cross-source synthesis

### Processing Tasks
1. Query understanding and semantic decomposition
2. Literature retrieval from indexed sources using semantic search
3. Evidence synthesis and pattern identification across retrieved documents
4. Gap and contradiction detection within retrieved literature
5. Trust Card generation (claim-to-source alignment metadata)
6. Citation linking to original publisher pages
7. Structured report compilation (Deep Research mode)
8. Scope, assumptions, and limitations articulation (Deep Research mode)

### Interaction Points
1. **Query Submission**: Researcher enters natural language question into LeapSpace workspace
2. **Mode Selection**: Researcher selects standard response or Deep Research mode
3. **Result Review**: Researcher reads synthesised response with inline citations
4. **Trust Card Inspection**: Researcher opens Trust Cards to evaluate source-claim alignment
5. **Source Verification**: Researcher clicks through to original publisher pages for full-text review
6. **Follow-up Questioning**: Researcher submits clarifying or expanding questions using conversational history
7. **Reference Export**: Researcher exports reference list to citation management tool

### Outputs
- Synthesised literature summary with inline, traceable citations
- Trust Cards for each cited source (claim-to-source alignment indicators)
- Direct hyperlinks to source articles on publisher platforms
- Structured multi-page report (Deep Research mode): scope, assumptions, limitations, evidence basis, patterns, gaps, emerging trends
- Exportable reference list

### Evaluation Metrics
- Time savings compared to manual literature review (reported: 97% of users save time; >50% save more than 50% of research time)
- Comprehensiveness of literature coverage relative to research question scope
- Citation traceability and accuracy
- User satisfaction and research confidence improvement
- Research design quality improvement (self-reported by users)
- External recognition: CODiE Award 2026 Best Generative AI Solution

### Required Capabilities
- **AI Capabilities**: Natural language understanding, semantic search, multi-source retrieval, evidence synthesis, structured generation, Trust Card production, multi-agent coordination, contradiction detection
- **Human Capabilities**: Research question formulation, domain expertise, critical evaluation of synthesised evidence, judgment on source reliability, interpretation of findings, final research decision-making

### Decision Points
1. **Search Strategy Selection**: Researcher decides query framing and mode selection (standard vs. Deep Research)
2. **Source Credibility Evaluation**: Researcher inspects Trust Card information and decides whether source alignment is acceptable
3. **Evidence Sufficiency Judgement**: Researcher determines whether synthesised evidence is adequate for research purposes
4. **Follow-up Direction**: Researcher decides which threads to pursue further based on findings
5. **Export and Integration**: Researcher decides which references to retain and integrate into research workflow

### Feedback Mechanisms
1. Trust Cards surface contradictions between claims and cited sources, prompting researcher reconsideration
2. Visible answer steps display AI reasoning process, enabling researcher verification
3. Conversational history enables iterative query refinement and result improvement
4. Implicit feedback through follow-up query patterns informs session coherence

### Expected HI Characteristics (CARE Dimensions)
- **Collaborative**: AI and researcher share the literature exploration task; AI provides scale and retrieval capability while researcher provides domain expertise, critical judgment, and research direction
- **Adaptive**: Multi-model approach selects AI models based on query complexity; daily content updates ensure currency; Deep Research mode adapts to question structure
- **Responsible**: Retrieval restricted to peer-reviewed sources; retracted articles excluded from results; publisher-neutral ranking methodology; Independent Advisory Board oversight; zero-retention contracts with LLM providers; ISO 27001 aligned security
- **Explainable**: Trust Cards provide source-claim alignment transparency; visible answer steps show AI reasoning; all citations directly linked to original sources; scope and limitations explicitly stated in Deep Research reports

### Evidence IDs
E-001, E-002, E-003, E-007, E-010, E-012, E-013, E-015

### Confidence Level
**High** — Core scenario with extensive direct documentary evidence from official Elsevier product pages, press releases, support documentation, and independent industry analysis. User statistics corroborated by multiple independent sources.

---

## S2: AI-Assisted Scientific Claim Validation

### Scenario Name
AI-Assisted Scientific Claim Validation via Claim Radar and Trust Cards

### Description
A researcher submits a specific scientific claim — drawn from a manuscript draft, a paper under peer review, or a grant proposal — to LeapSpace for evidence verification. The Claim Radar component searches the broader published literature to assess how the claim holds up across multiple sources, classifying evidence as supporting, contradicting, or mixed. Trust Cards are generated for each relevant source, linking specific claims to specific papers. The researcher reviews the evidence landscape, inspects individual Trust Cards, clicks through to original publications, and makes an informed human judgment about whether to retain, revise, or qualify the claim. The AI provides systematic, scalable evidence canvassing; the researcher provides domain expertise and final editorial authority.

### Goal
Systematically validate scientific claims against the peer-reviewed evidence base, identify supporting and contradicting literature, surface areas of limited consensus, and enable researchers to strengthen or qualify their claims before publication or submission.

### Human Actors
- **Researcher** (Scientist evaluating claims in manuscripts, grant proposals, review articles, or their own ongoing work)
- **Peer Reviewer** (Optional; reviewer using claim validation to assess submitted manuscripts)

### Artificial Agents
- **Claim Radar** (Evidence verification system assessing how a claim holds up across the broader published literature)
- **Trust Card Generator** (Source-to-claim alignment analyser producing per-source transparency metadata)
- **Citation Linking Engine** (Component tracing direct links between claims and source documents)

### Context
- Manuscript preparation and pre-submission review
- Peer review process for journal submissions
- Grant proposal development requiring evidential robustness
- Research integrity verification workflows
- Post-publication claim re-evaluation

### Input Data
- Scientific claim text (entered or highlighted within a document)
- Optional: draft manuscript or document section (uploaded PDF or Word)
- Optional: domain or discipline specification for scope narrowing

### Knowledge Sources
- Scopus-indexed literature corpus (107M+ peer-reviewed records)
- ScienceDirect full-text articles for detailed claim-level assessment
- Publisher-neutral, retraction-filtered content index

### Processing Method
- Claim segmentation and semantic extraction from input text
- Broad literature search for evidence directly relevant to the claim
- Evidence classification: supporting, contradicting, or mixed/uncertain
- Confidence calibration based on evidence volume and consistency
- Trust Card generation per relevant source
- Citation linking to original publications

### Processing Tasks
1. Claim identification and semantic parsing
2. Evidence retrieval across indexed literature
3. Supporting vs. contradicting evidence classification
4. Strength-of-evidence and confidence scoring
5. Trust Card generation for each relevant source
6. Result presentation with source counts and evidence distribution
7. Direct citation linking to original papers

### Interaction Points
1. **Claim Submission**: Researcher enters claim text or highlights a passage in an uploaded document
2. **Evidence Landscape Review**: Researcher examines supporting and contradicting source counts and classification
3. **Trust Card Inspection**: Researcher opens individual Trust Cards to examine source-claim alignment at the paper level
4. **Source Verification**: Researcher clicks through to original publications for full-text confirmation
5. **Confidence Assessment**: Researcher interprets evidence strength indicators and makes editorial judgment

### Outputs
- Evidence assessment summary indicating supporting reference count and contradicting reference count
- Identification of areas of limited or contested consensus in the literature
- Trust Card for each relevant source with claim-to-source alignment detail
- Direct hyperlinks to source documents on publisher platforms
- Confidence indicators based on evidence volume and consistency

### Evaluation Metrics
- Accuracy of supporting vs. contradicting evidence classification
- Comprehensiveness of evidence coverage across the relevant literature
- Researcher confidence in claim validity following assessment
- Time saved versus manual evidence canvassing
- Rate of claim revision or qualification following Claim Radar use

### Required Capabilities
- **AI Capabilities**: Claim extraction, semantic matching across large corpora, evidence classification, confidence scoring, Trust Card generation, citation linking
- **Human Capabilities**: Domain expertise for contextual evidence interpretation, editorial judgment on claim wording, final decision authority on claim retention or revision

### Decision Points
1. **Evidence Sufficiency Judgement**: Researcher decides whether the retrieved evidence adequately supports, contradicts, or qualifies the claim
2. **Claim Modification Decision**: Researcher determines whether to revise, qualify, or retain the claim based on evidence findings
3. **Source Selection**: Researcher decides which specific sources to cite in support of or against the claim
4. **Scope Adjustment**: Researcher decides whether to narrow or broaden the claim to align with the evidence base

### Feedback Mechanisms
1. Visual evidence strength indicators show the balance of supporting versus contradicting evidence
2. Transparent source counts enable researcher to gauge evidence volume
3. Trust Cards provide granular per-source alignment detail, enabling targeted human review
4. Researcher retains full editorial control over final claim wording

### Expected HI Characteristics (CARE Dimensions)
- **Collaborative**: AI systematically canvasses the literature at scale; human researcher provides domain interpretation and makes final editorial decisions
- **Responsible**: Claim assessment grounded in peer-reviewed, retraction-filtered content; publisher-neutral ranking prevents source bias; transparent evidence classification
- **Explainable**: Trust Cards explicitly link each claim to each supporting or contradicting source; evidence classification rationale is visible; source counts provide quantitative transparency

### Evidence IDs
E-003, E-004, E-008, E-016, E-023

### Confidence Level
**High** — Claim Radar and Trust Cards are explicitly and repeatedly documented as core LeapSpace features across official product pages, press releases, support documentation, and independent industry analysis.

---

## S3: AI-Assisted Research Writing with Writing Coach

### Scenario Name
AI-Assisted Scientific Writing and Argument Strengthening via Writing Coach

### Description
A researcher uses the LeapSpace Writing Coach to iteratively strengthen a research manuscript, grant proposal, or thesis chapter. Working within a private, encrypted workspace, the researcher submits draft text or uploads a document and engages in a structured conversational dialogue with the Writing Coach AI. The AI analyses the text, extracts claims, checks those claims against the broader literature using integrated Claim Radar functionality, identifies gaps in argumentation, surfaces counter-arguments, and suggests relevant citations. Critically, the Writing Coach makes no automatic edits: every suggested change requires explicit researcher approval. The researcher reviews, accepts, rejects, or modifies each suggestion, maintaining full creative and editorial control. The interaction is designed to help researchers test reasoning, identify weak points, and strengthen arguments before submission.

### Goal
Strengthen research manuscripts and proposals by testing reasoning, surfacing evidence gaps, identifying missing citations, and surfacing counter-arguments — all while preserving full researcher editorial authority and ensuring no automatic changes are made without explicit approval.

### Human Actors
- **Researcher / Primary Author** (Scientist drafting or revising research manuscripts, grant proposals, or thesis chapters)
- **Co-Author** (Optional; collaborative writer reviewing AI-suggested improvements)

### Artificial Agents
- **Writing Coach** (Conversational AI providing iterative writing assistance, argument analysis, and gap identification)
- **Claim Radar** (Integrated evidence verification component checking draft claims against the literature)
- **Citation Suggester** (Component recommending relevant peer-reviewed references to support draft arguments)

### Context
- Manuscript preparation for peer-reviewed journal submission
- Grant proposal development requiring evidential robustness
- PhD thesis or dissertation chapter revision
- Private, encrypted LeapSpace workspace (content not used for model training)
- Researcher seeking pre-submission review without external disclosure

### Input Data
- Draft text (typed directly into workspace or pasted)
- Uploaded Word documents or PDFs containing draft content
- Research questions or specific writing goals stated by researcher
- Discipline or journal scope (optional)

### Knowledge Sources
- Publisher-neutral, Scopus-indexed peer-reviewed literature
- ScienceDirect full-text repository for citation suggestions
- User-uploaded documents as additional context
- Peer-reviewed sources only; retracted articles excluded

### Processing Method
- Text segmentation into discrete claims and argumentative units
- Claim-level literature alignment checking via Claim Radar
- Gap identification: arguments lacking evidential support
- Counter-argument retrieval from contradicting literature
- Argument clarity and logical coherence assessment
- Evidence-based suggestion generation with rationale
- Contextualized reasoning display linking suggestions to literature

### Processing Tasks
1. Draft text analysis and claim extraction
2. Literature alignment checking for each extracted claim
3. Evidence gap identification where claims lack supporting literature
4. Counter-argument retrieval and presentation
5. Citation suggestion generation with relevance rationale
6. Argument strength assessment
7. Suggestion presentation requiring explicit user approval
8. Contextualised reasoning display

### Interaction Points
1. **Draft Submission**: Researcher pastes or uploads draft text into Writing Coach workspace
2. **Goal Declaration**: Researcher optionally specifies writing goals or areas of concern
3. **Conversational Dialogue**: Researcher engages in back-and-forth exchange with Writing Coach
4. **Claim Check Trigger**: Researcher or AI triggers Claim Radar on specific passages
5. **Gap and Counter-Argument Review**: Researcher examines identified weaknesses
6. **Suggestion Review**: Researcher reads AI-generated improvement suggestions with rationale
7. **Explicit Approval or Rejection**: Researcher approves or rejects each individual suggestion
8. **Citation Integration**: Researcher incorporates accepted citation suggestions into manuscript

### Outputs
- Iteratively strengthened draft text reflecting researcher-approved changes
- Identified gaps in argumentation requiring additional evidence
- List of relevant citation suggestions with supporting rationale
- Counter-argument identification prompting researcher consideration
- Contextualised reasoning showing how draft claims connect to or diverge from the literature

### Evaluation Metrics
- Improvement in argument strength and evidential coverage (researcher self-reported)
- Completeness of evidence coverage for key claims
- Researcher approval rate for AI suggestions
- Manuscript acceptance rate at target journals (long-term, indirect)
- Time saved in pre-submission revision cycles

### Required Capabilities
- **AI Capabilities**: Claim analysis, evidence gap detection, counter-argument retrieval, citation recommendation, conversational dialogue, contextualised reasoning generation
- **Human Capabilities**: Scientific writing judgment, domain expertise, editorial control, final decision authority over all text changes, assessment of suggestion quality

### Decision Points
1. **Change Acceptance Decision**: Researcher explicitly approves or rejects each individual AI-suggested change
2. **Citation Selection**: Researcher decides which suggested sources to incorporate and in what context
3. **Argument Direction**: Researcher determines the overall argumentative direction of the manuscript independent of AI suggestions
4. **Gap Prioritisation**: Researcher decides which identified gaps are most critical to address before submission
5. **Counter-Argument Response**: Researcher decides how to address or acknowledge surfaced counter-arguments

### Feedback Mechanisms
1. No automatic edits are made; all changes require explicit researcher approval, ensuring human oversight is structurally enforced
2. Transparent suggestion rationale links each recommendation to specific literature evidence
3. Iterative conversational dialogue enables progressive refinement based on researcher responses
4. Private, encrypted workspace with confirmed zero-retention policy ensures no user data is used for model training, enabling candid drafting

### Expected HI Characteristics (CARE Dimensions)
- **Collaborative**: AI provides scale in literature checking and gap identification while researcher maintains creative and editorial authority; both contribute complementary capabilities to the writing task
- **Adaptive**: Writing Coach suggestions adapt dynamically to the specific content of the draft; suggestions are contextualised to the researcher's stated goals and discipline
- **Responsible**: Private, encrypted workspace with zero-retention policy; no automatic edits without explicit researcher approval; peer-reviewed sources only; independent advisory board governance
- **Explainable**: Visible reasoning for all suggestions; claim-to-literature alignment shown; gap identification rationale made explicit; researcher can trace every suggestion to its evidentiary basis

### Evidence IDs
E-005, E-009, E-017, E-025

### Confidence Level
**High** — Writing Coach and integrated Claim Radar are explicitly and consistently documented across official Elsevier product pages, the Writing Coach feature page, press releases, and industry analysis. The no-automatic-edits policy is specifically documented.

---

## S4: AI-Assisted Research Opportunity Identification

### Scenario Name
AI-Assisted Funding Discovery and Collaborator Identification

### Description
A researcher or research office administrator uses LeapSpace to discover relevant funding opportunities and identify potential research collaborators. Using natural language queries, the researcher describes their research area and requirements; the system searches a structured funding database and Scopus author profiles to return ranked, relevant results. The researcher reviews matched funding opportunities with eligibility details, explores potential collaborator profiles grounded in verified publication records, and makes strategic decisions about which opportunities to pursue and which researchers to contact. AI provides systematic, scalable search and relevance ranking across large structured databases; the researcher provides strategic evaluation and relationship judgment.

### Goal
Identify appropriate, currently active funding opportunities and relevant research collaborators to advance specific research projects, reducing time spent on manual database searching and enabling more strategic research development decisions.

### Human Actors
- **Researcher** (Scientist seeking funding opportunities or collaborators to advance a specific research project)
- **Research Office Administrator** (Optional; grants support professional assisting researchers in identifying funding)

### Artificial Agents
- **Funding Scout** (Grant opportunity identification and matching system searching the Elsevier Funding Institutional database)
- **Author Search** (Collaborator discovery component searching Scopus author profiles by expertise and publication record)
- **Profile Analyser** (Researcher expertise assessment component analysing publication records to establish expertise evidence)

### Context
- Grant application planning phase requiring current, relevant opportunity identification
- Research team formation or expansion requiring expertise matching
- Cross-disciplinary collaboration development
- Institutional research strategy planning
- Database: 45,000+ active grants representing $100B+ in funding value; daily updates

### Input Data
- Natural language description of research area, topic, or question
- Eligibility criteria (geographic location, career stage, discipline, funding type)
- Research area descriptions or keywords
- Collaboration interest specifications (expertise required, institutional context)

### Knowledge Sources
- Elsevier Funding Institutional database (45,000+ active grants, $100B+ total value, daily updates)
- Scopus author profiles and verified publication records
- Research affiliation and institutional metadata
- Expertise classification based on publication history

### Processing Method
- Natural language query interpretation and semantic parsing
- Funding database search with structured eligibility filtering
- Publication record analysis for expertise classification
- Semantic relevance ranking of funding opportunities and collaborator profiles
- Profile presentation with evidence base (publications, citation metrics)

### Processing Tasks
1. Query understanding and semantic decomposition
2. Funding database search with eligibility criterion filtering
3. Relevance ranking of funding opportunities
4. Author publication record analysis for expertise classification
5. Collaborator profile matching to stated research needs
6. Ranked result compilation and presentation

### Interaction Points
1. **Query Entry**: Researcher enters natural language description of research area and requirements
2. **Filter Application**: Researcher refines results by eligibility criteria (location, career stage, discipline)
3. **Funding Opportunity Review**: Researcher examines ranked funding opportunities with eligibility and deadline details
4. **Collaborator Profile Review**: Researcher explores suggested researcher profiles with publication-grounded expertise evidence
5. **Detail Exploration**: Researcher investigates specific opportunities or profiles in depth before making contact or application decisions

### Outputs
- Ranked list of funding opportunities with eligibility criteria, funding amounts, and application deadlines
- Potential collaborator profiles with documented expertise areas and publication evidence
- Direct links to funding opportunity details and application portals
- Scopus-based expertise evidence for each suggested collaborator

### Evaluation Metrics
- Relevance of funding opportunity matches to stated research area
- Quality and relevance of collaborator suggestions based on expertise alignment
- Researcher satisfaction with result quality
- Time saved versus manual database searching
- Downstream success rate in funding applications (long-term, indirect)

### Required Capabilities
- **AI Capabilities**: Semantic search, natural language query interpretation, publication record analysis, expertise classification, relevance ranking
- **Human Capabilities**: Strategic evaluation of opportunity suitability, relationship-building judgment, application strategy development, assessment of collaborator fit beyond publication metrics

### Decision Points
1. **Opportunity Prioritisation**: Researcher decides which funding opportunities are worth pursuing given strategic research goals
2. **Collaborator Outreach Decision**: Researcher decides which suggested collaborators to contact and in what context
3. **Application Strategy**: Researcher develops application approach based on retrieved information
4. **Eligibility Confirmation**: Researcher manually confirms eligibility details before committing application effort

### Feedback Mechanisms
1. Filter refinement enables iterative narrowing of results based on researcher response to initial set
2. Iterative natural language query adjustment enables progressive result improvement
3. Daily database updates ensure currency of funding information, reducing researcher exposure to outdated opportunities

### Expected HI Characteristics (CARE Dimensions)
- **Collaborative**: AI systematically searches large structured databases at scale; human researcher evaluates strategic fit and makes relationship and application decisions
- **Adaptive**: Natural language query flexibility accommodates diverse research area descriptions; filter-based refinement enables iterative result improvement
- **Responsible**: Funding data sourced from verified, structured institutional databases with daily updates; collaborator expertise grounded in verifiable Scopus publication records
- **Explainable**: Collaborator suggestions grounded in transparent publication record evidence; funding opportunity matches linked to stated eligibility criteria and research area alignment

### Evidence IDs
E-006, E-011, E-019

### Confidence Level
**High** — Funding Discovery and Author Search are explicitly documented as core LeapSpace features in official product pages, press releases, and the LibGuide. Specific database statistics (45,000+ grants, $100B+ value) are sourced directly from official documentation.

---

## S5: Multi-Agent Deep Research Synthesis

### Scenario Name
Multi-Agent Deep Research Report Generation

### Description
A researcher entering an unfamiliar research domain, or requiring a comprehensive overview of a complex, potentially interdisciplinary topic, uses LeapSpace Deep Research mode to generate a structured, multi-page research report. The researcher submits a complex research question with optional context and documents. A multi-agent AI system decomposes the question into sub-components, executes parallel sub-queries across the full Scopus and ScienceDirect corpus, synthesises evidence from thousands of papers, identifies patterns and contradictions, and generates a structured report with explicit scope, assumptions, and limitations sections. The researcher can observe the reasoning and planning steps as they execute, review the completed report, verify individual citations, and ask follow-up questions. Deep Research mode is acknowledged to take longer than standard queries — sometimes several minutes — reflecting its comprehensive processing scope.

### Goal
Generate detailed, comprehensively sourced research reports on complex topics that highlight evidence patterns, identify research gaps and contradictions, surface emerging trends, and provide a structured evidence base for informed research direction decisions — at a scope and speed not achievable through manual review.

### Human Actors
- **Researcher** (Scientist or analyst requiring comprehensive literature analysis on a complex or unfamiliar topic, or interdisciplinary overview)

### Artificial Agents
- **Deep Research Coordinator** (Orchestrating agent managing the multi-agent workflow and sub-query routing)
- **Query Decomposition Agent** (Agent breaking the complex research question into component sub-queries)
- **Retrieval Agents** (Multiple parallel agents executing sub-queries across different aspects of the topic)
- **Synthesis Agent** (Agent compiling and cross-referencing retrieved evidence into coherent findings)
- **Report Writer Agent** (Agent generating the structured multi-page output with scope, limitations, and citation sections)

### Context
- Researcher entering an unfamiliar research domain requiring rapid onboarding
- Complex, interdisciplinary topic requiring synthesis across multiple sub-fields
- Comprehensive literature overview required to inform research strategy
- Scenario where manual review of relevant literature would take days or weeks
- Processing time acknowledged as longer than standard queries (sometimes several minutes)

### Input Data
- Complex research question (natural language, multi-component)
- Optional: background context or framing provided by researcher
- Optional: uploaded supplementary documents (up to 5 files, 10 MB each)
- Optional: scope constraints or discipline focus

### Knowledge Sources
- Full Scopus abstract corpus (107M+ records)
- ScienceDirect full-text repository (20M+ articles and books)
- Partner publisher full-text content
- User-uploaded documents
- Daily updated content index

### Processing Method
- Complex question analysis and semantic decomposition into sub-components
- Multi-agent parallel sub-query execution across corpus
- Cross-source evidence retrieval and validation
- Pattern identification across retrieved evidence
- Gap and contradiction detection between sources
- Meta-analysis style synthesis across sub-agent findings
- Structured report compilation with explicit scope, assumptions, limitations, and Trust Cards

### Processing Tasks
1. Research question analysis and decomposition into sub-queries
2. Sub-agent parallel query execution across Scopus and ScienceDirect
3. Evidence retrieval and relevance validation per sub-query
4. Cross-source pattern identification
5. Research gap and contradiction detection
6. Emerging trend identification
7. Meta-synthesis across sub-agent findings
8. Structured report compilation with scope and limitations sections
9. Trust Card generation for all cited sources

### Interaction Points
1. **Query Submission**: Researcher enters complex research question with optional context and documents
2. **Process Observation**: Researcher observes displayed planning and reasoning steps as agents execute
3. **Report Review**: Researcher reads multi-page structured report with sections for patterns, gaps, trends
4. **Source Verification**: Researcher opens Trust Cards and clicks through to original cited publications
5. **Follow-up Refinement**: Researcher asks clarifying or expanding questions based on report content

### Outputs
- Multi-page structured research report with clearly delineated sections
- Explicit scope and assumptions section documenting what was and was not covered
- Limitations acknowledgement section transparently noting evidence constraints
- Evidence references throughout with Trust Cards for each cited source
- Pattern analysis: recurring themes across the literature
- Gap analysis: identified areas lacking evidence or awaiting further research
- Emerging trend identification
- Contradiction mapping where sources disagree

### Evaluation Metrics
- Comprehensiveness of topic coverage relative to the scope of the question
- Accuracy of pattern identification verified by domain expert review
- Quality and validity of gap analysis
- Time savings versus manual comprehensive review (reported: more than half of users save over 50% of research time)
- Researcher confidence improvement following report review
- Citation traceability and Trust Card accuracy

### Required Capabilities
- **AI Capabilities**: Complex question decomposition, multi-agent coordination, parallel retrieval execution, cross-source synthesis, pattern detection, gap identification, structured report generation, scope and limitations articulation
- **Human Capabilities**: Complex question formulation, process observation and critical monitoring, report evaluation, domain expertise for result validation, interpretation of patterns and gaps, direction-setting based on findings

### Decision Points
1. **Scope Definition**: Researcher formulates the research question with appropriate scope and framing to guide the multi-agent process
2. **Report Completeness Evaluation**: Researcher assesses whether the generated report adequately covers the intended topic
3. **Finding Validation**: Researcher applies domain expertise to validate reported patterns, gaps, and trends
4. **Research Direction Selection**: Researcher decides which areas identified in the report to pursue further

### Feedback Mechanisms
1. Visible planning and execution steps displayed during agent processing, enabling researcher to monitor and evaluate process coherence
2. Transparent sub-query display shows which components of the question were addressed
3. Explicit scope and limitations sections structurally acknowledge what the report does and does not cover
4. Full source traceability via Trust Cards throughout the report enables researcher verification of every cited claim

### Expected HI Characteristics (CARE Dimensions)
- **Collaborative**: Multi-agent AI system executes comprehensive synthesis at scale beyond human capacity; researcher provides question framing, domain expertise, process oversight, and final interpretation
- **Adaptive**: System refines synthesis approach as sub-agent findings emerge; multi-model selection adapts to different sub-query types across the decomposed question
- **Responsible**: Transparent acknowledgement of scope, assumptions, and limitations structurally built into report format; peer-reviewed content only; retracted articles excluded; zero-retention LLM contracts
- **Explainable**: Full visibility into multi-step agent planning and execution process; visible sub-query decomposition; explicit scope and limitations; Trust Cards for every cited source

### Evidence IDs
E-010, E-013, E-021

### Confidence Level
**High** — Deep Research mode is explicitly documented as a core LeapSpace feature in official press releases, product pages, and the LibGuide. Multi-agent architecture and structured report format are directly described in official documentation.

---

## S6: AI-Assisted Article Reading and Interrogation

### Scenario Name
AI-Assisted Article Reading and Targeted Content Extraction via Reading Assistant

### Description
A researcher identifies a specific full-text article or book chapter of potential relevance and uses the LeapSpace Reading Assistant to interrogate its content through natural language questions, without needing to read the entire document. The researcher selects the article within their access-authorised content, asks targeted questions about specific aspects — methodology, results, conclusions, limitations — and receives answers linked directly to the relevant sections of the paper. The Reading Assistant also suggests relevant follow-up questions. The researcher uses these interactions to efficiently determine article relevance, extract specific information, and decide whether to invest time in full reading. Human judgment governs relevance determination and content interpretation.

### Goal
Efficiently extract targeted insights from specific full-text articles or book chapters through conversational interrogation, enabling rapid relevance determination and selective deep reading, and reducing time spent reading documents of marginal utility.

### Human Actors
- **Researcher** (Scientist evaluating the relevance and content of specific articles or book chapters during literature review or topic exploration)

### Artificial Agents
- **Reading Assistant** (Document-specific conversational Q&A component providing targeted answers linked to document sections)

### Context
- Literature review phase requiring rapid relevance screening of large article sets
- Evaluating methodology or results sections of specific papers
- Access to subscribed content (institutional or individual) or open access articles
- Researcher time-constrained and requiring rapid content extraction

### Input Data
- Selected full-text article or book chapter (within user's access rights)
- Natural language questions about specific aspects of the document content

### Knowledge Sources
- Specific full-text article or book chapter selected by researcher (must have access rights)
- ScienceDirect full-text content
- Mendeley-integrated content (where applicable)

### Processing Method
- Document ingestion and full-text parsing
- Question semantic understanding and intent identification
- Relevant section identification and evidence localisation within document
- Answer generation grounded in document text with section-level citation
- Follow-up question suggestion based on document structure

### Processing Tasks
1. Document ingestion and structural parsing
2. Question understanding and semantic matching to document content
3. Relevant section identification within the document
4. Grounded answer generation linked to specific document sections
5. Follow-up question suggestion generation

### Interaction Points
1. **Article Selection**: Researcher selects article or book chapter for interrogation within LeapSpace
2. **Question Entry**: Researcher enters natural language question about specific document content
3. **Answer Review**: Researcher reads AI-generated answer with direct links to the relevant document sections
4. **Section Navigation**: Researcher follows section links to verify answer in original text
5. **Follow-up Questions**: Researcher pursues additional questions prompted by AI suggestions or own curiosity

### Outputs
- Direct, grounded answers to researcher questions linked to specific document sections
- Section-level citations within the document enabling immediate verification
- Suggested follow-up questions facilitating deeper document exploration
- Highlighted or summarised key sections
- Key insight extraction to support relevance determination

### Evaluation Metrics
- Accuracy of answers relative to actual document content
- Time saved compared to full document reading for relevance determination
- Researcher comprehension improvement for complex articles
- Researcher satisfaction with answer quality and section linkage

### Required Capabilities
- **AI Capabilities**: Document understanding and full-text parsing, question semantic understanding, section-level evidence localisation, grounded answer generation, follow-up question suggestion
- **Human Capabilities**: Targeted question formulation based on research