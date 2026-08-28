# Ontology Mapping: LeapSpace to HI Ontology v2.0.0

## Namespace Reference

```
hi:   https://w3id.org/hi-ontology#
hint: https://w3id.org/hi-thesaurus#
```

---

## 1. HITeam

### hi:HITeam

**Concept Name:** LeapSpace Human-AI Research Team

**Ontology Class:** `hi:HITeam`

**Description:** The overarching hybrid team composed of one or more human researcher agents and the LeapSpace AI system working toward shared research goals. The team is constituted dynamically per use case (e.g., literature review, claim verification, writing assistance).

**Relevant Properties:**
- `hi:hasMember` → Academic Researcher (hi:HumanAgent)
- `hi:hasMember` → Corporate Researcher (hi:HumanAgent)
- `hi:hasMember` → Librarian (hi:HumanAgent)
- `hi:hasMember` → Research Office Administrator (hi:HumanAgent)
- `hi:hasMember` → LeapSpace Platform (hi:ArtificialAgent)
- `hi:hasGoal` → Accelerate Research Discovery (hi:Goal)
- `hi:hasGoal` → Maintain Research Integrity (hi:Goal)
- `hi:operatesInContext` → Academic Research Environment (hi:Context)
- `hi:operatesInContext` → Corporate R&D Environment (hi:Context)

**Evidence IDs:** E-001, E-002, E-015, E-018

**Confidence:** High

**Observed/Inferred:** Observed

---

## 2. UseCase

### hi:UseCase — Literature Review Acceleration

**Concept Name:** AI-Assisted Systematic Literature Discovery

**Ontology Class:** `hi:UseCase`

**Description:** A researcher uses LeapSpace to conduct an efficient literature review, leveraging AI to search, synthesise, and identify patterns across large bodies of peer-reviewed literature while maintaining critical human oversight and judgement.

**Relevant Properties:**
- `hi:hasGoal` → Accelerate Discovery (hi:Goal)
- `hi:involvesTask` → Literature Search (hi:Task)
- `hi:involvesTask` → Literature Synthesis (hi:Task)
- `hi:involvesTask` → Gap Identification (hi:Task)
- `hi:hasParticipant` → Academic Researcher (hi:HumanAgent)
- `hi:hasParticipant` → LeapSpace Core AI (hi:ArtificialAgent)
- `hi:hasParticipant` → RAG Engine (hi:ArtificialAgent)
- `hi:hasParticipant` → Deep Research Agent (hi:ArtificialAgent)
- `hi:hasParticipant` → Trust Card Generator (hi:ArtificialAgent)
- `hi:operatesInContext` → Academic/Corporate Research Environment (hi:Context)

**Evidence IDs:** E-001, E-002, E-003, E-007, E-012, E-015

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:UseCase — Claim Verification and Evidence Assessment

**Concept Name:** AI-Assisted Scientific Claim Validation

**Ontology Class:** `hi:UseCase`

**Description:** A researcher uses Claim Radar and Trust Cards to verify the evidential support for scientific claims, assessing how claims align with individual sources and the broader published literature.

**Relevant Properties:**
- `hi:hasGoal` → Maintain Research Integrity (hi:Goal)
- `hi:hasGoal` → Support Critical Thinking (hi:Goal)
- `hi:involvesTask` → Claim Verification (hi:Task)
- `hi:involvesTask` → Evidence Assessment (hi:Task)
- `hi:hasParticipant` → Researcher (hi:HumanAgent)
- `hi:hasParticipant` → Claim Radar (hi:ArtificialAgent)
- `hi:hasParticipant` → Trust Card Generator (hi:ArtificialAgent)
- `hi:hasParticipant` → Citation Linking Engine (hi:ArtificialAgent)

**Evidence IDs:** E-004, E-008, E-016, E-023

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:UseCase — Research Writing Assistance

**Concept Name:** AI-Assisted Scientific Writing with Writing Coach

**Ontology Class:** `hi:UseCase`

**Description:** A researcher uses LeapSpace Writing Coach to draft, refine, and strengthen research manuscripts through iterative dialogue with an AI assistant that contextualises reasoning, challenges assumptions, and identifies evidence gaps.

**Relevant Properties:**
- `hi:hasGoal` → Improve Research Design (hi:Goal)
- `hi:hasGoal` → Build Research Confidence (hi:Goal)
- `hi:involvesTask` → Research Writing (hi:Task)
- `hi:involvesTask` → Argument Strengthening (hi:Task)
- `hi:involvesTask` → Gap Identification (hi:Task)
- `hi:hasParticipant` → Researcher/Author (hi:HumanAgent)
- `hi:hasParticipant` → Writing Coach (hi:ArtificialAgent)
- `hi:hasParticipant` → Claim Radar (hi:ArtificialAgent)
- `hi:hasParticipant` → Citation Suggester (hi:ArtificialAgent)

**Evidence IDs:** E-005, E-009, E-017, E-025

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:UseCase — Funding and Collaborator Discovery

**Concept Name:** AI-Assisted Research Opportunity Identification

**Ontology Class:** `hi:UseCase`

**Description:** A researcher uses LeapSpace to discover relevant funding opportunities and potential collaborators by searching structured databases using natural language queries.

**Relevant Properties:**
- `hi:hasGoal` → Find Collaborators (hi:Goal)
- `hi:hasGoal` → Identify Funding (hi:Goal)
- `hi:involvesTask` → Collaborator Discovery (hi:Task)
- `hi:involvesTask` → Funding Discovery (hi:Task)
- `hi:hasParticipant` → Researcher (hi:HumanAgent)
- `hi:hasParticipant` → Research Office Administrator (hi:HumanAgent)
- `hi:hasParticipant` → Funding Scout (hi:ArtificialAgent)
- `hi:hasParticipant` → Author Search Component (hi:ArtificialAgent)
- `hi:hasParticipant` → Profile Analyzer (hi:ArtificialAgent)

**Evidence IDs:** E-006, E-011, E-019

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:UseCase — Deep Research Report Generation

**Concept Name:** Multi-Agent Deep Research Synthesis

**Ontology Class:** `hi:UseCase`

**Description:** A researcher uses LeapSpace Deep Research mode to generate comprehensive, structured reports on complex topics, leveraging a multi-agent system that decomposes questions, retrieves evidence, and synthesises findings across thousands of papers.

**Relevant Properties:**
- `hi:hasGoal` → Accelerate Discovery (hi:Goal)
- `hi:hasGoal` → Build Research Confidence (hi:Goal)
- `hi:involvesTask` → Report Generation (hi:Task)
- `hi:involvesTask` → Pattern Detection (hi:Task)
- `hi:involvesTask` → Gap Identification (hi:Task)
- `hi:hasParticipant` → Researcher (hi:HumanAgent)
- `hi:hasParticipant` → Deep Research Coordinator (hi:ArtificialAgent)
- `hi:hasParticipant` → Query Decomposition Agent (hi:ArtificialAgent)
- `hi:hasParticipant` → Retrieval Agents (hi:ArtificialAgent)
- `hi:hasParticipant` → Synthesis Agent (hi:ArtificialAgent)
- `hi:hasParticipant` → Report Writer Agent (hi:ArtificialAgent)

**Evidence IDs:** E-010, E-013, E-021

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:UseCase — Article Reading and Comprehension

**Concept Name:** AI-Assisted Reading and Article Interrogation

**Ontology Class:** `hi:UseCase`

**Description:** A researcher uses LeapSpace Reading Assistant to interrogate specific full-text articles or book chapters, asking questions about content to quickly understand key points without reading entire documents.

**Relevant Properties:**
- `hi:hasGoal` → Accelerate Discovery (hi:Goal)
- `hi:involvesTask` → Article Interrogation (hi:Task)
- `hi:hasParticipant` → Researcher (hi:HumanAgent)
- `hi:hasParticipant` → Reading Assistant (hi:ArtificialAgent)
- `hi:operatesInContext` → Subscribed Content Access (hi:Context)

**Evidence IDs:** E-014, E-020

**Confidence:** High

**Observed/Inferred:** Observed

---

## 3. HumanAgent

### hi:HumanAgent — Academic Researcher

**Concept Name:** Academic Researcher

**Ontology Class:** `hi:HumanAgent`

**Description:** A university- or institute-based scientist or scholar conducting peer-reviewed research. The primary target user of LeapSpace across all use cases.

**Relevant Properties:**
- `hi:hasCapability` → Critical Evaluation (hi:Capability)
- `hi:hasCapability` → Domain Expertise (hi:Capability)
- `hi:hasCapability` → Research Judgement (hi:Capability)
- `hi:hasCapability` → Evidence Interpretation (hi:Capability)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)
- `hi:participatesIn` → Claim Verification (hi:UseCase)
- `hi:participatesIn` → Research Writing Assistance (hi:UseCase)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)
- `hi:participatesIn` → Article Reading and Comprehension (hi:UseCase)
- `hi:operatesInContext` → Academic Research Environment (hi:Context)

**Evidence IDs:** E-001, E-002, E-022

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:HumanAgent — Corporate Researcher

**Concept Name:** Corporate Researcher / R&D Scientist

**Ontology Class:** `hi:HumanAgent`

**Description:** A scientist employed in industry or corporate research and development. Uses LeapSpace to accelerate innovation and competitive intelligence within a corporate R&D context.

**Relevant Properties:**
- `hi:hasCapability` → Domain Expertise (hi:Capability)
- `hi:hasCapability` → Strategic Evaluation (hi:Capability)
- `hi:operatesInContext` → Corporate R&D Environment (hi:Context)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)
- `hi:participatesIn` → Funding and Collaborator Discovery (hi:UseCase)

**Evidence IDs:** E-001, E-002

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:HumanAgent — PhD Student

**Concept Name:** PhD Student / Early-Career Researcher

**Ontology Class:** `hi:HumanAgent`

**Description:** A doctoral researcher using LeapSpace to navigate large bodies of literature, build confidence in research design, and strengthen academic writing.

**Relevant Properties:**
- `hi:hasCapability` → Research Judgement (hi:Capability)
- `hi:hasCapability` → Domain Expertise (hi:Capability) — developing
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)
- `hi:participatesIn` → Research Writing Assistance (hi:UseCase)
- `hi:operatesInContext` → Academic Research Environment (hi:Context)

**Evidence IDs:** E-022

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:HumanAgent — Librarian

**Concept Name:** Research Librarian / Information Professional

**Ontology Class:** `hi:HumanAgent`

**Description:** An academic library professional who supports researchers in accessing LeapSpace, manages institutional subscriptions, and provides guidance on research tools.

**Relevant Properties:**
- `hi:hasCapability` → Information Literacy (hi:Capability)
- `hi:hasCapability` → Access Management (hi:Capability)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase) — support role
- `hi:operatesInContext` → Institutional Subscription Access (hi:Context)

**Evidence IDs:** E-018

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:HumanAgent — Research Office Administrator

**Concept Name:** Research Office Administrator / Grants Manager

**Ontology Class:** `hi:HumanAgent`

**Description:** An administrative professional who supports researchers in identifying and applying for funding opportunities. Uses LeapSpace to assist with grant discovery.

**Relevant Properties:**
- `hi:hasCapability` → Strategic Evaluation (hi:Capability)
- `hi:hasCapability` → Relationship Building (hi:Capability)
- `hi:participatesIn` → Funding and Collaborator Discovery (hi:UseCase)
- `hi:operatesInContext` → Institutional Subscription Access (hi:Context)

**Evidence IDs:** E-018

**Confidence:** Medium

**Observed/Inferred:** Observed

---

### hi:HumanAgent — Peer Reviewer

**Concept Name:** Peer Reviewer

**Ontology Class:** `hi:HumanAgent`

**Description:** A subject-matter expert assessing submitted manuscripts. May use LeapSpace Claim Radar to verify claims during peer review.

**Relevant Properties:**
- `hi:hasCapability` → Domain Expertise (hi:Capability)
- `hi:hasCapability` → Critical Evaluation (hi:Capability)
- `hi:participatesIn` → Claim Verification and Evidence Assessment (hi:UseCase)
- `hi:operatesInContext` → Academic Research Environment (hi:Context)

**Evidence IDs:** Inferred from E-004, E-008

**Confidence:** Medium

**Observed/Inferred:** Inferred

---

## 4. ArtificialAgent

### hi:ArtificialAgent — LeapSpace Platform

**Concept Name:** LeapSpace Platform (Core System)

**Ontology Class:** `hi:ArtificialAgent`

**Description:** The overarching AI-assisted workspace system launched January 21, 2026 by Elsevier. Coordinates all AI sub-components and provides the unified researcher-facing interface. Built on multi-model AI and RAG architecture.

**Relevant Properties:**
- `hi:hasCapability` → Natural Language Understanding (hi:Capability)
- `hi:hasCapability` → Semantic Search (hi:Capability)
- `hi:hasCapability` → Evidence Synthesis (hi:Capability)
- `hi:hasCapability` → Transparency Generation (hi:Capability)
- `hi:hasCapability` → Multi-Agent Coordination (hi:Capability)
- `hi:participatesIn` → All Use Cases (hi:UseCase)
- `hi:operatesInContext` → Academic Research Environment (hi:Context)
- `hi:operatesInContext` → Corporate R&D Environment (hi:Context)
- `hi:usesMethod` → Retrieval-Augmented Generation
- `hi:usesMethod` → Multi-model AI selection
- `hi:usesMethod` → Agentic AI workflows

**Evidence IDs:** E-001, E-002, E-007, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — RAG Engine

**Concept Name:** Retrieval-Augmented Generation Engine

**Ontology Class:** `hi:ArtificialAgent`

**Description:** The core retrieval component that grounds AI-generated responses in peer-reviewed literature. Queries Scopus and ScienceDirect corpora and provides retrieved documents to the generative component.

**Relevant Properties:**
- `hi:hasCapability` → Retrieval-Augmented Generation (hi:Capability)
- `hi:hasCapability` → Full-Text Parsing (hi:Capability)
- `hi:hasCapability` → Semantic Search (hi:Capability)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)

**Evidence IDs:** E-007, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Trust Card Generator

**Concept Name:** Trust Card Generator

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component that generates Trust Cards — structured metadata artefacts showing claim-to-source alignment, enabling researchers to verify the accuracy of AI-generated claims against the underlying peer-reviewed sources.

**Relevant Properties:**
- `hi:hasCapability` → Transparency Generation (hi:Capability)
- `hi:hasCapability` → Citation Tracing (hi:Capability)
- `hi:hasCapability` → Citation Linking (hi:Capability)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)
- `hi:participatesIn` → Claim Verification and Evidence Assessment (hi:UseCase)
- `hi:produces` → Trust Card artefacts (output)

**Evidence IDs:** E-003, E-004

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Claim Radar

**Concept Name:** Claim Radar

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI verification component that assesses how scientific claims hold up across the broader published literature — not just individual cited sources. Identifies supporting, contradicting, and uncertain evidence distributions.

**Relevant Properties:**
- `hi:hasCapability` → Claim Analysis (hi:Capability)
- `hi:hasCapability` → Contradiction Detection (hi:Capability)
- `hi:hasCapability` → Evidence Classification (hi:Capability)
- `hi:participatesIn` → Claim Verification and Evidence Assessment (hi:UseCase)
- `hi:participatesIn` → Research Writing Assistance (hi:UseCase)

**Evidence IDs:** E-004, E-008

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Writing Coach

**Concept Name:** Writing Coach

**Ontology Class:** `hi:ArtificialAgent`

**Description:** A conversational AI assistant embedded in a private, encrypted workspace that helps researchers draft and strengthen scientific manuscripts. Surfaces evidence gaps, challenges assumptions, and suggests citations without making automatic edits.

**Relevant Properties:**
- `hi:hasCapability` → Claim Analysis (hi:Capability)
- `hi:hasCapability` → Gap Detection (hi:Capability)
- `hi:hasCapability` → Evidence Matching (hi:Capability)
- `hi:participatesIn` → Research Writing Assistance (hi:UseCase)
- `hi:operatesInContext` → Private Encrypted Workspace (hi:Context)

**Evidence IDs:** E-005, E-009

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Deep Research Coordinator

**Concept Name:** Deep Research Coordinator

**Ontology Class:** `hi:ArtificialAgent`

**Description:** The orchestrating agent in the Deep Research multi-agent workflow. Decomposes complex research questions into sub-queries, coordinates specialised retrieval agents, and oversees the synthesis of findings into a structured report.

**Relevant Properties:**
- `hi:hasCapability` → Multi-Agent Coordination (hi:Capability)
- `hi:hasCapability` → Complex Synthesis (hi:Capability)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)
- `hi:coordinates` → Query Decomposition Agent (hi:ArtificialAgent)
- `hi:coordinates` → Retrieval Agents (hi:ArtificialAgent)
- `hi:coordinates` → Synthesis Agent (hi:ArtificialAgent)
- `hi:coordinates` → Report Writer Agent (hi:ArtificialAgent)

**Evidence IDs:** E-010, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Query Decomposition Agent

**Concept Name:** Query Decomposition Agent

**Ontology Class:** `hi:ArtificialAgent`

**Description:** A specialised AI sub-agent within the Deep Research workflow that parses complex research questions into discrete, tractable sub-queries for parallel retrieval.

**Relevant Properties:**
- `hi:hasCapability` → Natural Language Understanding (hi:Capability)
- `hi:hasCapability` → Question Decomposition (hi:Capability)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)

**Evidence IDs:** E-010, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Retrieval Agents

**Concept Name:** Retrieval Agents (multiple parallel agents)

**Ontology Class:** `hi:ArtificialAgent`

**Description:** Multiple parallel AI agents within the Deep Research workflow that execute sub-queries against Scopus and ScienceDirect, retrieving evidence for different aspects of a complex research question simultaneously.

**Relevant Properties:**
- `hi:hasCapability` → Semantic Search (hi:Capability)
- `hi:hasCapability` → Full-Text Parsing (hi:Capability)
- `hi:hasCapability` → Retrieval-Augmented Generation (hi:Capability)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)

**Evidence IDs:** E-010, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Synthesis Agent

**Concept Name:** Synthesis Agent

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI sub-agent within the Deep Research workflow that compiles and cross-analyses evidence retrieved by parallel retrieval agents, identifying patterns, contradictions, gaps, and emerging trends.

**Relevant Properties:**
- `hi:hasCapability` → Evidence Synthesis (hi:Capability)
- `hi:hasCapability` → Contradiction Detection (hi:Capability)
- `hi:hasCapability` → Pattern Detection (hi:Capability)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)

**Evidence IDs:** E-010, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Report Writer Agent

**Concept Name:** Report Writer Agent

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI sub-agent within the Deep Research workflow that generates the final structured multi-page report, including explicit scope, assumptions, limitations sections, and full citation linkage.

**Relevant Properties:**
- `hi:hasCapability` → Structured Generation (hi:Capability)
- `hi:participatesIn` → Deep Research Report Generation (hi:UseCase)
- `hi:produces` → Multi-page structured research report (output)

**Evidence IDs:** E-010, E-013

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Reading Assistant

**Concept Name:** Reading Assistant

**Ontology Class:** `hi:ArtificialAgent`

**Description:** A document-specific conversational Q&A component that enables researchers to interrogate full-text articles or book chapters by asking natural language questions, receiving answers linked to specific document sections.

**Relevant Properties:**
- `hi:hasCapability` → Document Understanding (hi:Capability)
- `hi:hasCapability` → Section Linking (hi:Capability)
- `hi:participatesIn` → Article Reading and Comprehension (hi:UseCase)
- `hi:operatesInContext` → Subscribed Content Access (hi:Context)

**Evidence IDs:** E-014, E-020

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Author Search Component

**Concept Name:** Author Search Component

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component that enables researchers to discover potential collaborators by searching and analysing Scopus author profiles, publication records, and research expertise areas.

**Relevant Properties:**
- `hi:hasCapability` → Semantic Search (hi:Capability)
- `hi:hasCapability` → Profile Analysis (hi:Capability)
- `hi:participatesIn` → Funding and Collaborator Discovery (hi:UseCase)

**Evidence IDs:** E-006

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Funding Scout

**Concept Name:** Funding Scout

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component that searches the Elsevier Funding Institutional database (45,000+ active grants, $100B+ value) using natural language queries to match researchers with relevant funding opportunities.

**Relevant Properties:**
- `hi:hasCapability` → Semantic Search (hi:Capability)
- `hi:hasCapability` → Relevance Ranking (hi:Capability)
- `hi:participatesIn` → Funding and Collaborator Discovery (hi:UseCase)

**Evidence IDs:** E-006

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Profile Analyzer

**Concept Name:** Profile Analyzer

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component that analyses researcher publication records and affiliations to assess expertise alignment with funding opportunities or collaboration requirements.

**Relevant Properties:**
- `hi:hasCapability` → Profile Analysis (hi:Capability)
- `hi:hasCapability` → Relevance Ranking (hi:Capability)
- `hi:participatesIn` → Funding and Collaborator Discovery (hi:UseCase)

**Evidence IDs:** E-006

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Compare Tables Component

**Concept Name:** Compare Tables Component

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component that enables side-by-side structured comparison of multiple articles or publications, supporting efficient literature evaluation.

**Relevant Properties:**
- `hi:hasCapability` → Document Comparison (hi:Capability)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)

**Evidence IDs:** E-012

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Citation Linking Engine

**Concept Name:** Citation Linking Engine

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component that traces and links AI-generated claims directly to their source documents, enabling click-through verification to original publications on publisher platforms.

**Relevant Properties:**
- `hi:hasCapability` → Citation Tracing (hi:Capability)
- `hi:participatesIn` → Claim Verification and Evidence Assessment (hi:UseCase)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)

**Evidence IDs:** E-004

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Citation Suggester

**Concept Name:** Citation Suggester

**Ontology Class:** `hi:ArtificialAgent`

**Description:** An AI component embedded in the Writing Coach workflow that recommends relevant references based on manuscript content and identified evidence gaps.

**Relevant Properties:**
- `hi:hasCapability` → Evidence Matching (hi:Capability)
- `hi:hasCapability` → Relevance Ranking (hi:Capability)
- `hi:participatesIn` → Research Writing Assistance (hi:UseCase)

**Evidence IDs:** E-005, E-009

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — Reference Export Component

**Concept Name:** Reference Export Component

**Ontology Class:** `hi:ArtificialAgent`

**Description:** A component that enables researchers to export citations in standard reference management formats for integration with tools such as Mendeley, Zotero, or EndNote.

**Relevant Properties:**
- `hi:hasCapability` → Citation Management (hi:Capability)
- `hi:participatesIn` → Literature Review Acceleration (hi:UseCase)

**Evidence IDs:** E-026

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — LLM Provider: OpenAI

**Concept Name:** OpenAI LLM Provider

**Ontology Class:** `hi:ArtificialAgent`

**Description:** External large language model provider (OpenAI) contracted under zero-retention agreements to supply generative AI capabilities to the LeapSpace platform. Hosted on Azure.

**Relevant Properties:**
- `hi:hasCapability` → Natural Language Understanding (hi:Capability)
- `hi:hasCapability` → Structured Generation (hi:Capability)
- `hi:operatesInContext` → Zero-Retention Contract Constraint (hi:Context)

**Evidence IDs:** E-007

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:ArtificialAgent — LLM Provider: Anthropic

**Concept Name:** Anthropic LLM Provider

**Ontology Class:** `hi:ArtificialAgent`

**Description:** External large language model provider (Anthropic) contracted under zero-retention agreements to supply generative AI capabilities to the LeapSpace platform. Hosted on AWS.

**Relevant Properties:**
- `hi:hasCapability` → Natural Language Understanding (hi:Capability)
- `hi:hasCapability` → Structured Generation (hi:Capability)
- `hi:operatesInContext` → Zero-Retention Contract Constraint (hi:Context)

**Evidence IDs:** E-007

**Confidence:** High

**Observed/Inferred:** Observed

---

## 5. Goal

### hi:Goal — Accelerate Discovery

**Concept Name:** Accelerate Research Discovery and Innovation

**Ontology Class:** `hi:Goal`

**Description:** The primary shared goal of LeapSpace — to help researchers uncover deeper insights and accelerate the pace of scientific discovery by reducing the time spent on manual literature work.

**Relevant Properties:**
- `hi:isGoalOf` → LeapSpace HITeam (hi:HITeam)
- `hi:isAchievedVia` → Literature Review Acceleration (hi:UseCase)
- `hi:isAchievedVia` → Deep Research Report Generation (hi:UseCase)
- `hi:isAchievedVia` → Article Reading and Comprehension (hi:UseCase)

**Evidence IDs:** E-001, E-002, E-015

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:Goal — Improve Research Design

**Concept Name:** Improve Research Design Quality

**Ontology Class:** `hi:Goal`

**Description:** The goal of strengthening the methodological quality of research projects by surfacing relevant evidence, identifying gaps, and challenging assumptions prior to and during the research process.

**Relevant Properties:**
- `hi:isGoalOf` → Academic Researcher (hi:HumanAgent)
- `hi:isAchievedVia` → Research Writing Assistance (hi:UseCase)
- `hi:isAchievedVia` → Claim Verification and Evidence Assessment (hi:UseCase)

**Evidence IDs:** E-015

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:Goal — Build Research Confidence

**Concept Name:** Build Researcher Confidence in Findings

**Ontology Class:** `hi:Goal`

**Description:** The goal of enabling researchers — particularly early-career researchers — to develop greater confidence in their research questions, methods, and conclusions through AI-assisted evidence grounding.

**Relevant Properties:**
- `hi:isGoalOf` → Academic Researcher (hi:HumanAgent)
- `hi:isGoalOf` → PhD Student (hi:HumanAgent)
- `hi:isAchievedVia` → Research Writing Assistance (hi:UseCase)
- `hi:isAchievedVia` → Deep Research Report Generation (hi:UseCase)

**Evidence IDs:** E-022

**Confidence:** High

**Observed/Inferred:** Observed

---

### hi:Goal — Maintain Research Integrity

**Concept Name:** Maintain Scientific Research Integrity

**Ontology Class:** `hi:Goal`

**Description:** The goal of ensuring that AI-generated outputs are grounded in, and traceable to, peer-reviewed scientific evidence — preventing hallucinations and mi