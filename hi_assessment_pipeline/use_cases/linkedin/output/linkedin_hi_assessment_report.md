# HI Assessment Report: LINKEDIN

**Assessment Date:** 2026-08-25  
**HI Ontology Version:** 2.0.0 (VU Amsterdam)  
**Pipeline:** Neuro-Symbolic HI Assessment Pipeline  
**LLM Model:** gpt-4o-mini  

---

## 1. Executive Summary

The assessment of LinkedIn's AI system reveals an overall HI conformance score of 50.0%, placing it at Level 2: Emerging HI on the HI maturity scale. This score reflects a mixed performance across the eight scenarios evaluated, with four scenarios identified as having significant HI gaps. 

The primary strengths of the system lie within the Adaptive, Responsible, and Explainable dimensions of the CARE principles, each achieving a perfect score of 100%. This indicates that the system is well-equipped to adapt to user needs, operates responsibly, and provides clear explanations for its actions. However, the Collaborative dimension presents notable weaknesses, scoring only 50%. The identified gaps in this area include the absence of AI agents in interactions, as well as a lack of human agents in certain contexts. These gaps are significant as they hinder the system's ability to facilitate effective collaboration between users and AI, potentially impacting user trust and engagement.

Overall, while LinkedIn's AI system demonstrates emerging capabilities in HI, the presence of substantial collaborative gaps indicates a need for improvement to enhance user interaction and support. Addressing these gaps will be crucial for advancing the system to a higher maturity level and fostering a more integrated and effective hybrid intelligence environment. With targeted efforts to incorporate collaborative elements, there is substantial potential for LinkedIn to enhance its HI conformance and user experience in the future.

---

## 2. HI Conformance Overview

### 2.1 Overall Score

| Metric | Value |
|--------|-------|
| Overall HI Conformance | [███████████████░░░░░░░░░░░░░░░] 50.0% |
| HI Maturity Level | **Level 2: Emerging HI** |
| Scenarios Assessed | 8 |
| Scenarios PASS | 4 (50%) |
| Scenarios WARNING | 0 |
| Scenarios FAIL | 4 (50%) |
| Total HI Gaps | 4 |

> The system shows clear HI intent but has significant gaps in one or more CARE dimensions. Human-AI collaboration is present but inconsistent across scenarios.

### 2.2 CARE Dimension Analysis

| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| **Collaborative** | ⚠️ 50% | Human and AI agents co-participate in interactions |
| **Adaptive** | ✅ 100% | Feedback loops and learning mechanisms |
| **Responsible** | ✅ 100% | Oversight, fairness, and accountability |
| **Explainable** | ✅ 100% | AI transparency and decision explanation |

### 2.3 Scenario Overview

| Scenario | Label | Status | Gaps |
|----------|-------|--------|------|
| S1 | S1 — AI-Assisted Candidate Sourcing | ✅ PASS | — |
| S2 | S2 — AI-Driven Candidate Evaluation | ❌ FAIL | 1 |
| S3 | S3 — Automated Prescreening via InMail | ✅ PASS | — |
| S4 | S4 — Fairness-Aware Representative Candidate Ranking | ❌ FAIL | 1 |
| S5 | S5 — Explainable AI-Assisted Search | ✅ PASS | — |
| S6 | S6 — Recruiter-Hiring Manager Collaborative Decision Making | ❌ FAIL | 1 |
| S7 | S7 — Long-Term Personalisation via HLTM | ✅ PASS | — |
| S8 | S8 — ATS Integration and Unified Applicant Management (RSC+) | ❌ FAIL | 1 |

---

## 3. Detailed Scenario Analysis

### S1 — S1 — AI-Assisted Candidate Sourcing

**Status:** ✅ PASS  
**HI Gaps:** 0  

> Scenario 'S1 — AI-Assisted Candidate Sourcing' satisfies all evaluated HI conformance constraints. All CARE dimensions (Collaborative, Adaptive, Responsible, Explainable) are structurally and semantically present in the KG.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | No evidence indicates that the AI agent initiates contact or forms its own sub-goals. |
| Adaptive | 1 — Reactive | There is no evidence that the system adapts based on implicit feedback or anticipates human needs. |
| Responsible | 1 — Reactive | The system does not demonstrate the ability to identify or surface the grounds for its decisions. |
| Explainable | 1 — Reactive | Explanations are not mentioned as being tailored or interactive, indicating a lack of contextual adaptation. |

All HI conformance checks passed. This scenario demonstrates well-structured human-AI collaboration across all CARE dimensions.

### S2 — S2 — AI-Driven Candidate Evaluation

**Status:** ❌ FAIL  
**HI Gaps:** 1  

> The AI-driven candidate evaluation system fails to meet fundamental HI requirements, particularly in collaborative interactions. The absence of an AI agent in recorded interactions severely undermines the system's ability to function as a hybrid intelligence.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of an AI agent in the recorded human-AI interaction indicates that the system cannot support effective collaboration, thus limiting it to a reactive level. |
| Adaptive | 2 — Proactive | There is no evidence provided to suggest the system's adaptability, but the maximum admissible level is 3, allowing for a conservative classification at level 2. |
| Responsible | 2 — Proactive | There is no evidence provided regarding the system's responsible capabilities, but the maximum admissible level is 3, allowing for a conservative classification at level 2. |
| Explainable | 2 — Proactive | There is no evidence provided regarding the system's explainability, but the maximum admissible level is 3, allowing for a conservative classification at level 2. |

#### Gap G-S2-01: Missing AI Agent in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | Collaborative |

**Gap Description**
> The recorded human-AI interaction episode lacks the presence of an artificial agent, which is essential for collaboration. This absence means that the system cannot facilitate joint participation between humans and AI, violating the core principle of collaboration in HI.

**Practical Impact**
> Without an AI agent involved, the system cannot support effective teamwork, leading to a breakdown in the collaborative process essential for candidate evaluation.

**Recommendation: Integrate AI Agent for Collaborative Interaction**

Develop and integrate an AI agent that actively participates in the candidate evaluation process. This agent should facilitate real-time interactions, allowing both human evaluators and the AI to contribute insights and feedback, thereby enhancing collaboration.

*Implementation:* Utilize existing NLP frameworks to create a conversational interface for the AI agent, ensuring it can understand and respond to human inputs during evaluations. Test the agent's performance in simulated scenarios to refine its collaborative capabilities.

*Priority:* High | *Expected HI Impact:* This integration enhances the collaborative aspect of the system, ensuring effective teamwork between humans and AI.

### S3 — S3 — Automated Prescreening via InMail

**Status:** ✅ PASS  
**HI Gaps:** 0  

> Scenario 'S3 — Automated Prescreening via InMail' satisfies all evaluated HI conformance constraints. All CARE dimensions (Collaborative, Adaptive, Responsible, Explainable) are structurally and semantically present in the KG.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | No evidence indicates that the AI agent initiates contact or collaborates without being explicitly prompted. |
| Adaptive | 1 — Reactive | The system shows no evidence of adapting its behavior based on implicit feedback or anticipating human needs. |
| Responsible | 1 — Reactive | There is no evidence that the system identifies or reflects on the grounds for its decisions. |
| Explainable | 1 — Reactive | The explanations provided by the system are not indicated to be tailored or context-specific. |

All HI conformance checks passed. This scenario demonstrates well-structured human-AI collaboration across all CARE dimensions.

### S4 — S4 — Fairness-Aware Representative Candidate Ranking

**Status:** ❌ FAIL  
**HI Gaps:** 1  

> The scenario fails to meet HI conformance due to the absence of AI involvement in interactions. This lack of collaboration fundamentally undermines the human-AI partnership.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of AI in interaction episodes indicates that the system cannot facilitate meaningful human-AI interactions, limiting its collaborative capabilities. |
| Adaptive | 2 — Proactive | There is no evidence of gaps in the Adaptive dimension, allowing for a proactive classification. |
| Responsible | 2 — Proactive | There is no evidence of gaps in the Responsible dimension, allowing for a proactive classification. |
| Explainable | 2 — Proactive | There is no evidence of gaps in the Explainable dimension, allowing for a proactive classification. |

#### Gap G-S4-01: Absence of AI in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded human-AI interaction episodes lack any involvement of an Artificial Agent, which is a fundamental requirement for collaborative systems. This absence means that the system cannot facilitate meaningful human-AI interactions, violating the core principle of collaboration.

**Practical Impact**
> Without AI participation, the system cannot support joint decision-making or shared task execution, severely limiting the effectiveness and utility of the AI in real-world applications.

**Recommendation: Integrate AI Agents for Interaction**

Introduce AI agents that can actively participate in human-AI interactions, facilitating joint decision-making and task execution. This change will enhance collaboration by allowing users to engage with AI in a meaningful way, addressing the absence of AI in the interaction process.

*Implementation:* Develop a module that incorporates AI agents capable of understanding user inputs and responding contextually during interactions. Ensure these agents can learn from user behavior to improve their collaborative capabilities over time.

*Priority:* High | *Expected HI Impact:* Enhancing collaboration by enabling meaningful human-AI interactions.

### S5 — S5 — Explainable AI-Assisted Search

**Status:** ✅ PASS  
**HI Gaps:** 0  

> Scenario 'S5 — Explainable AI-Assisted Search' satisfies all evaluated HI conformance constraints. All CARE dimensions (Collaborative, Adaptive, Responsible, Explainable) are structurally and semantically present in the KG.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | No evidence indicates that the AI agent initiates collaboration or maintains a relationship over time. |
| Adaptive | 1 — Reactive | There is no evidence of the system adapting based on implicit feedback or anticipating human needs. |
| Responsible | 1 — Reactive | The system does not demonstrate the ability to identify or reflect on the grounds for its decisions. |
| Explainable | 1 — Reactive | Explanations provided by the system are not described as tailored or interactive. |

All HI conformance checks passed. This scenario demonstrates well-structured human-AI collaboration across all CARE dimensions.

### S6 — S6 — Recruiter-Hiring Manager Collaborative Decision Making

**Status:** ❌ FAIL  
**HI Gaps:** 1  

> The scenario fails to meet HI conformance due to the absence of AI involvement in human interactions. This lack of collaboration fundamentally undermines the system's ability to function as a hybrid intelligence.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of AI involvement in interactions, as indicated by the critical gap, limits collaboration to a reactive level. |
| Adaptive | 2 — Proactive | There is no evidence of gaps in this dimension, allowing for a conservative classification at the proactive level. |
| Responsible | 2 — Proactive | There is no evidence of gaps in this dimension, allowing for a conservative classification at the proactive level. |
| Explainable | 2 — Proactive | There is no evidence of gaps in this dimension, allowing for a conservative classification at the proactive level. |

#### Gap G-S6-01: Absence of AI in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | Collaborative |

**Gap Description**
> The recorded interactions lack any involvement of an Artificial Agent, which is a fundamental requirement for hybrid intelligence. Without AI participation, the essence of collaboration is lost, preventing effective joint decision-making between human agents.

**Practical Impact**
> This absence severely limits the potential for meaningful collaboration between recruiters and hiring managers, ultimately affecting the quality and efficiency of the hiring process.

**Recommendation: Integrate AI Agent for Interaction**

Implement an AI agent that actively participates in the interaction between recruiters and hiring managers. This agent should analyze candidate data and provide real-time insights, facilitating collaborative decision-making and enhancing the overall hiring process.

*Implementation:* Utilize existing AI models to develop a chatbot or virtual assistant that can be integrated into the current recruitment platform, ensuring it can access and analyze relevant candidate information during discussions.

*Priority:* High | *Expected HI Impact:* This integration enhances collaboration by ensuring AI contributes to the decision-making process, fostering a more effective partnership between human agents.

### S7 — S7 — Long-Term Personalisation via HLTM

**Status:** ✅ PASS  
**HI Gaps:** 0  

> Scenario 'S7 — Long-Term Personalisation via HLTM' satisfies all evaluated HI conformance constraints. All CARE dimensions (Collaborative, Adaptive, Responsible, Explainable) are structurally and semantically present in the KG.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | No evidence indicates that the AI agent initiates collaboration or maintains a relationship over time. |
| Adaptive | 1 — Reactive | There is no evidence of the system adapting its behavior based on implicit feedback or anticipating human needs. |
| Responsible | 1 — Reactive | The system does not demonstrate any capability to identify or reflect on the grounds for its decisions. |
| Explainable | 1 — Reactive | Explanations provided by the system are not tailored to the specific user or context. |

All HI conformance checks passed. This scenario demonstrates well-structured human-AI collaboration across all CARE dimensions.

### S8 — S8 — ATS Integration and Unified Applicant Management (RSC+)

**Status:** ❌ FAIL  
**HI Gaps:** 1  

> The scenario fails to meet HI conformance due to the absence of human involvement in interactions, which undermines the collaborative nature of the system. This lack of collaboration significantly impacts the effectiveness of the AI system.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of human agent involvement in the recorded interaction means the system cannot facilitate true collaboration, thus it is classified as Reactive. |
| Adaptive | 1 — Reactive | There is no evidence of adaptive behavior, so the lower level is chosen conservatively. |
| Responsible | 1 — Reactive | Without evidence of responsible behavior, the lower level is assigned conservatively. |
| Explainable | 1 — Reactive | There is no evidence of explainability features, leading to a conservative classification at the lower level. |

#### Gap G-S8-01: Absence of Human Agent in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded human-AI interaction episode lacks any human agent involvement, which is a fundamental requirement for a hybrid intelligence system. This absence means that the system cannot facilitate true collaboration, as it relies solely on AI outputs without human engagement.

**Practical Impact**
> Without human participation, the AI system cannot effectively support decision-making or adapt to user needs, leading to a breakdown in collaborative efforts and reduced overall system efficacy.

**Recommendation: Integrate Human Agents in Decision-Making Process**

Implement a feature that allows human agents to review and interact with AI-generated outputs before final decisions are made. This will ensure that human expertise is incorporated into the decision-making process, fostering true collaboration between AI and human agents.

*Implementation:* Develop a user interface component that presents AI recommendations to human agents, allowing them to provide feedback or override decisions based on their expertise. Ensure this component is seamlessly integrated into the existing ATS workflow.

*Priority:* High | *Expected HI Impact:* Enhances collaborative efforts by ensuring human oversight in AI-driven decisions.

---

## 4. Consolidated Recommendations

### Collaborative Dimension

- **[High Priority] Integrate AI Agent for Collaborative Interaction**  
  *Scenario:* S2 — AI-Driven Candidate Evaluation  
  Develop and integrate an AI agent that actively participates in the candidate evaluation process. This agent should facilitate real-time interactions, allowing both human evaluators and the AI to contribute insights and feedback, thereby enhancing collaboration.  
  *Implementation:* Utilize existing NLP frameworks to create a conversational interface for the AI agent, ensuring it can understand and respond to human inputs during evaluations. Test the agent's performance in simulated scenarios to refine its collaborative capabilities.

- **[High Priority] Integrate AI Agents for Interaction**  
  *Scenario:* S4 — Fairness-Aware Representative Candidate Ranking  
  Introduce AI agents that can actively participate in human-AI interactions, facilitating joint decision-making and task execution. This change will enhance collaboration by allowing users to engage with AI in a meaningful way, addressing the absence of AI in the interaction process.  
  *Implementation:* Develop a module that incorporates AI agents capable of understanding user inputs and responding contextually during interactions. Ensure these agents can learn from user behavior to improve their collaborative capabilities over time.

- **[High Priority] Integrate AI Agent for Interaction**  
  *Scenario:* S6 — Recruiter-Hiring Manager Collaborative Decision Making  
  Implement an AI agent that actively participates in the interaction between recruiters and hiring managers. This agent should analyze candidate data and provide real-time insights, facilitating collaborative decision-making and enhancing the overall hiring process.  
  *Implementation:* Utilize existing AI models to develop a chatbot or virtual assistant that can be integrated into the current recruitment platform, ensuring it can access and analyze relevant candidate information during discussions.

- **[High Priority] Integrate Human Agents in Decision-Making Process**  
  *Scenario:* S8 — ATS Integration and Unified Applicant Management (RSC+)  
  Implement a feature that allows human agents to review and interact with AI-generated outputs before final decisions are made. This will ensure that human expertise is incorporated into the decision-making process, fostering true collaboration between AI and human agents.  
  *Implementation:* Develop a user interface component that presents AI recommendations to human agents, allowing them to provide feedback or override decisions based on their expertise. Ensure this component is seamlessly integrated into the existing ATS workflow.

---

## 5. HI Maturity Assessment

**Maturity Level: Level 2: Emerging HI**

The system shows clear HI intent but has significant gaps in one or more CARE dimensions. Human-AI collaboration is present but inconsistent across scenarios.

| CARE Dimension | Score | Status |
|----------------|-------|--------|
| Collaborative | 50% | Needs Work |
| Adaptive | 100% | Strong |
| Responsible | 100% | Strong |
| Explainable | 100% | Strong |

### Strengths

- **Adaptive**: Feedback loops and learning mechanisms
- **Responsible**: Oversight, fairness, and accountability
- **Explainable**: AI transparency and decision explanation

### Areas for Improvement

- **Collaborative** (50%): See recommendations in Section 4.

---

## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)

This section complements the score-based maturity level in Section 5 with a finer-grained, literature-grounded assessment of *how* each CARE dimension is demonstrated, adapted from the CARE capability-level tables (Hybrid Intelligence Centre Netherlands, 2023; cf. Akata et al. 2020; Zamprogno, Tiddi & Verheij 2025). Each scenario is classified per CARE dimension into one of three levels: **1 — Reactive** (the capability is only exercised upon explicit human instruction), **2 — Proactive** (the AI initiates or anticipates without being explicitly prompted), or **3 — Social** (the capability is sustained, repaired, or co-constructed over time with the human partner). The maximum level admissible for a dimension in a given scenario is capped by the most severe HI gap identified in that dimension in Phase 5 (Critical → capped at 1, Major → capped at 2, Minor/none → uncapped at 3), so the classification stays grounded in the symbolic SHACL evidence rather than unconstrained LLM judgement. This is distinct from the conformance score in Section 2.2, which measures whether a capability is present at all, not how maturely it is exercised.

### 6.1 Per-Scenario CARE Levels

| Scenario | Collaborative | Adaptive | Responsible | Explainable |
|----------|----------------|----------|--------------|-------------|
| S1 — S1 — AI-Assisted Candidate Sourcing | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S2 — S2 — AI-Driven Candidate Evaluation | 1 (Reactive) | 2 (Proactive) | 2 (Proactive) | 2 (Proactive) |
| S3 — S3 — Automated Prescreening via InM | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S4 — S4 — Fairness-Aware Representative  | 1 (Reactive) | 2 (Proactive) | 2 (Proactive) | 2 (Proactive) |
| S5 — S5 — Explainable AI-Assisted Search | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S6 — S6 — Recruiter-Hiring Manager Colla | 1 (Reactive) | 2 (Proactive) | 2 (Proactive) | 2 (Proactive) |
| S7 — S7 — Long-Term Personalisation via  | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S8 — S8 — ATS Integration and Unified Ap | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |

### 6.2 Use-Case CARE Maturity Summary

Levels are an ordinal scale (Reactive < Proactive < Social), so the table below reports the distribution and the modal (most frequent) level per dimension across all scenarios rather than an average.

| Dimension | Level 1 (Reactive) | Level 2 (Proactive) | Level 3 (Social) | Modal Level |
|-----------|---------------------|----------------------|--------------------|-------------|
| Collaborative | 8 | 0 | 0 | **1 — Reactive** |
| Adaptive | 5 | 3 | 0 | **1 — Reactive** |
| Responsible | 5 | 3 | 0 | **1 — Reactive** |
| Explainable | 5 | 3 | 0 | **1 — Reactive** |

---

## 7. Methodology

This report was produced by a **Neuro-Symbolic HI Assessment Pipeline** developed as part of a Master's thesis on Hybrid Intelligence systems evaluation.

### Pipeline Phases

| Phase | Method | Output |
|-------|--------|--------|
| 1 — Knowledge Acquisition | Literature review, public documentation analysis | Extraction sheets |
| 2 — KG Construction | RDFLib mapping to HI Ontology (VU Amsterdam) | RDF Knowledge Graph (Turtle) |
| 3 — Normalization | SHACL structural validation (pySHACL) | Normalization report (JSON) |
| 4 — SHACL Conformance | SHACL-SPARQL semantic validation against CARE shapes | Conformance report (JSON + TTL) |
| 5 — Gap Analysis | **Neuro-symbolic**: LLM interprets SHACL violations | Gap analysis (JSON) |
| 6 — Recommendations | LLM generates actionable design improvements and classifies CARE capability levels | Assessment report (Markdown) |

### Neuro-Symbolic Design

The neuro-symbolic paradigm is applied in Phases 5–6: the **symbolic** component (SHACL constraint engine) formally identifies which HI properties are absent or violated, producing structured symbolic output. The **neural** component (LLM) then interprets these formal violations, reasoning about their significance in the context of HI theory to produce human-readable gap analysis and recommendations. The LLM does not generate descriptions from a feature list — it performs semantic reasoning over formal constraint violations. The CARE capability-level classification in Section 6 follows the same principle: the LLM only selects a level within a ceiling that is computed deterministically from the symbolic gap severities.

### HI Ontology

**HI Ontology v2.0.0**, VU Amsterdam (2024).  
Namespace: `https://w3id.org/hi-ontology#`  
Key classes: UseCase, HITeam, HumanAgent, ArtificialAgent, Goal, Task, Capability, Context, Interaction, TaskExecution, Evaluation.

### Scoring

- **Per-scenario**: PASS = 1.0, WARNING = 0.75, FAIL = 0.0
- **Overall score**: mean of per-scenario scores
- **CARE score**: proportion of scenarios with no gap in that dimension
- **CARE capability level**: 1 (Reactive) / 2 (Proactive) / 3 (Social) per scenario per dimension, LLM-classified from Phase 4/5 evidence and capped by gap severity (Critical → 1, Major → 2, Minor/none → 3); aggregated across scenarios by mode, not by average, since the scale is ordinal (see Section 6.2)

---

*Report generated on 2026-08-25 by the HI Assessment Pipeline.*