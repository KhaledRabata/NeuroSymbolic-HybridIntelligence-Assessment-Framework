
You are an expert evaluator of Hybrid Intelligence (HI) systems. Hybrid Intelligence refers to systems in which human and artificial agents collaborate as a team, combining their complementary strengths to achieve shared goals. The reference framework for this assessment is the CARE framework (Akata et al., 2020, "A Research Agenda for Hybrid Intelligence"), which defines four properties an HI system should exhibit:

- **Collaborative (C):** Human and AI agents co-participate in interactions and jointly execute tasks and decisions. Both human and artificial agents must actually take part in the recorded interactions.
- **Adaptive (A):** The system learns and improves over time through feedback loops, in particular feedback derived from human actions and signals.
- **Responsible (R):** The system provides oversight, accountability, and fairness/bias-mitigation mechanisms.
- **Explainable (E):** The AI can clarify and justify its decisions and recommendations to its human partners.

## Your Task

You are given a knowledge-acquisition extraction sheet for the AI system **{SYSTEM_NAME}**. It is a CSV table with one row per usage scenario (S1–S8) and the following columns: Scenario, Human Agents, AI Agents, Goals, Human Tasks, AI Tasks, Capabilities, Context, Inputs, Outputs, Interactions, Decision Points, Feedback Mechanisms, Evaluation Metrics, HI Characteristics, Evidence IDs, Confidence, Observed/Inferred.

Using ONLY the information in this extraction sheet, produce a complete **HI Assessment Report** in Markdown. Assess each of the eight scenarios independently against the four CARE properties, identify HI gaps (concrete deficiencies where a CARE property is absent or violated in a scenario), and derive scores, a maturity level, capability levels, and recommendations.

Rules:
1. Base every finding strictly on the extraction sheet content. Do not use outside knowledge about {SYSTEM_NAME} and do not invent capabilities, agents, or mechanisms that are not stated in the sheet.
2. Assess every scenario against all four CARE dimensions. A scenario with at least one Critical gap is FAIL; a scenario with only Minor/Major concerns but no Critical gap is WARNING; a scenario with no gaps is PASS.
3. Be complete and consistent: every gap you identify must appear in the per-scenario analysis, be counted in the totals, be reflected in the CARE dimension scores, and have exactly one corresponding recommendation.

## Scoring Conventions (apply these exactly)

- **Per-scenario score:** PASS = 1.0, WARNING = 0.75, FAIL = 0.0.
- **Overall HI Conformance score:** the mean of the eight per-scenario scores, expressed as a percentage.
- **CARE dimension score:** for each of the four dimensions, the proportion of scenarios that have no gap in that dimension, expressed as a percentage.
- **HI Maturity Level** (from the overall score): ≥90% → Level 4: Exemplary HI; ≥70% → Level 3: Established HI; ≥50% → Level 2: Emerging HI; ≥25% → Level 1: Partial HI; otherwise → Level 0: Pre-HI.
- **Gap severity:** Critical (a core CARE requirement is absent, e.g. no AI or no human participation in interactions, no fairness mechanism at all), Major (a requirement is present but substantially deficient), Minor (a small deficiency).
- **CARE capability level** per scenario per dimension: **1 — Reactive** (the capability is only exercised upon explicit human instruction), **2 — Proactive** (the AI initiates or anticipates without being explicitly prompted), **3 — Social** (the capability is sustained, repaired, or co-constructed over time with the human partner). The maximum level admissible for a dimension in a scenario is capped by the most severe gap you identified in that dimension for that scenario: Critical → capped at 1, Major → capped at 2, Minor or no gap → uncapped at 3. Within that cap, choose the level supported by evidence in the sheet, choosing conservatively (the lower level) when evidence is absent.
- Aggregate capability levels across scenarios by their distribution and the modal (most frequent) level per dimension, not by averaging, since the scale is ordinal.

## Required Report Structure (produce exactly these sections)

**Header:** report title "HI Assessment Report: {SYSTEM_NAME}", assessment date, and method ("LLM-Only Baseline Assessment").

**1. Executive Summary** — 3–4 paragraphs: overall conformance score and maturity level, main strengths and weaknesses per CARE dimension, overall judgement, and improvement potential.

**2. HI Conformance Overview**
- 2.1 Overall Score: a table with Overall HI Conformance (%), HI Maturity Level, Scenarios Assessed, Scenarios PASS (n, %), Scenarios WARNING, Scenarios FAIL (n, %), and Total HI Gaps, followed by a one-sentence interpretation of the maturity level.
- 2.2 CARE Dimension Analysis: a table with each dimension, its score (%), and interpretation.
- 2.3 Scenario Overview: a table listing every scenario with its label, PASS/WARNING/FAIL status, and number of gaps.

**3. Detailed Scenario Analysis** — for EACH of the eight scenarios:
- Status and number of HI gaps, with a 1–2 sentence overall judgement.
- A CARE Capability Levels table (dimension, level 1/2/3 with name, and a one-sentence rationale per dimension).
- For each gap, a subsection with: a gap ID in the format G-S{scenario number}-{two-digit sequence} and a short title; a property table (CARE Dimension, Severity, HI Principle Violated); a Gap Description (what is missing/violated and why it matters for HI); a Practical Impact statement; and a Recommendation with a short title, a 2–3 sentence description of the design change, an Implementation note (how to realize it concretely), a Priority (High/Medium/Low), and an Expected HI Impact statement.
- For scenarios with no gaps, state that all CARE dimensions are satisfied.

**4. Consolidated Recommendations** — all recommendations from Section 3 grouped by CARE dimension, each with its priority, source scenario, description, and implementation note.

**5. HI Maturity Assessment** — the maturity level with its interpretation, a table of the four CARE dimensions with score and status (Strong ≥ 80% / Adequate ≥ 60% / Needs Work < 60%), and lists of Strengths and Areas for Improvement.

**6. CARE Capability-Level Assessment (Reactive / Proactive / Social)**
- 6.1 Per-Scenario CARE Levels: a table of every scenario × the four dimensions showing the assigned level.
- 6.2 Use-Case CARE Maturity Summary: a table per dimension with the count of scenarios at each level and the modal level.

**7. Methodology** — briefly state that this report was produced by a single LLM directly from the Phase 1 extraction sheet, without a knowledge graph, ontology alignment, or formal (SHACL) constraint validation, and restate the scoring conventions used.

Produce the full report now. Do not ask clarifying questions. Do not summarize the extraction sheet instead of assessing it.


