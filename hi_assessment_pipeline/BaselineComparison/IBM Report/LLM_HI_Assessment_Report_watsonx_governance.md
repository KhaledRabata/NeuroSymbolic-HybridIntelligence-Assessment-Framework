# HI Assessment Report: IBM watsonx.governance

**Assessment Date:** 2026-08-28
**Method:** LLM-Only Baseline Assessment (single-pass LLM analysis of the Phase 1 knowledge-acquisition extraction sheet, no knowledge graph, ontology alignment, or SHACL constraint validation)

---

## 1. Executive Summary

IBM watsonx.governance achieves an Overall HI Conformance score of **28.1%** across the eight assessed usage scenarios, placing the system at **HI Maturity Level 1: Partial HI**. Of the eight scenarios, none (0%) pass all four CARE checks cleanly, three (37.5%) receive a WARNING status (Minor/Major concerns only), and five (62.5%) FAIL due to at least one Critical gap. A total of eleven concrete HI gaps were identified across the scenario set, distributed across three of the four CARE dimensions.

The system's clearest strength is the **Collaborative** dimension, which scores a perfect 100%: every one of the eight scenarios documents explicit, structured, role-differentiated interactions between named human agents (Data Scientists, Validators, Reviewers, Recruiters, Model Risk Officers, and others) and named AI components (AutoAI, Watson OpenScale, retrieval/LLM stacks, red-teaming evaluators, governed agent catalogs). No scenario shows evidence of AI acting without human co-participation, or vice versa. **Responsible** governance is the second-strongest dimension (62.5%), anchored by strong fairness, drift, and audit mechanisms in the model-scoring scenarios (S1, S7, S8), though it is undermined by a Critical absence of any fairness or content-safety mechanism in the RAG production-quality scenario (S2) and by documentation gaps around exact accountable roles (S8) and alert-triage logic (S6). **Adaptive** and **Explainable** are the weakest dimensions, each scoring 50%. Adaptive gaps recur wherever the sheet itself flags a feedback or learning mechanism as "partial," "inferred," or entirely omitted from a scenario's HI Characteristics (S1, S3, S5, S7); Explainable gaps are concentrated in two scenarios (S4, S6) where no explainability capability is documented at all, despite Explainable being a core CARE pillar.

Taken as a whole, IBM watsonx.governance — as characterized by this extraction sheet — demonstrates a system architecture that is unambiguously built for human-AI co-participation and, in its more mature scenarios (predictive-model governance, RAG evaluation, red-teaming, multi-cloud model risk governance), for meaningful oversight and explanation. However, the evidence base is uneven: several of the most consequential claims about closed-loop learning and end-to-end explainability rest on inference rather than confirmed observation, and two scenarios lack any documented explainability mechanism whatsoever. The system's HI conformance is therefore better described as "collaboratively strong but unevenly adaptive and inconsistently explainable" rather than uniformly mature.

The improvement potential is substantial and concentrated. All five Critical gaps sit in only two dimensions (Adaptive: S3, S7; Explainable: S4, S6; Responsible: S2). If these five Critical gaps alone were resolved — without addressing any of the six remaining Minor/Major gaps — modeled re-scoring shows Overall HI Conformance could rise from 28.1% to approximately **81%**, crossing into Level 3: Established HI. This indicates that the system's underlying architecture already supports most CARE requirements; what is missing in the weakest scenarios is not new capability so much as confirmed evidence, instrumentation, and documentation of mechanisms that may already exist but are not demonstrated in the sheet.

---

## 2. HI Conformance Overview

### 2.1 Overall Score

| Metric | Value |
|---|---|
| Overall HI Conformance | **28.1%** |
| HI Maturity Level | **Level 1: Partial HI** |
| Scenarios Assessed | 8 |
| Scenarios PASS | 0 (0.0%) |
| Scenarios WARNING | 3 (37.5%) |
| Scenarios FAIL | 5 (62.5%) |
| Total HI Gaps | 11 |

*Interpretation:* A Level 1 (Partial HI) rating means the extraction sheet evidences recognizable, structured human-AI collaboration in every scenario, but consistent, fully-verified coverage of all four CARE properties is achieved in no scenario, with over half of scenarios containing at least one Critical deficiency.

### 2.2 CARE Dimension Analysis

| Dimension | Score | Interpretation |
|---|---|---|
| Collaborative (C) | **100.0%** | Every scenario documents explicit, role-differentiated human and AI co-participation in interactions and decisions; no Collaborative gaps were found anywhere in the sheet. |
| Adaptive (A) | **50.0%** | Half of scenarios have a feedback/learning loop that is either explicitly marked partial/inferred in the sheet or entirely omitted from the scenario's own HI Characteristics tag. |
| Responsible (R) | **62.5%** | Oversight and accountability structures are generally strong, but a production-facing scenario has zero fairness/safety mechanism, and two other scenarios have unverified accountability details. |
| Explainable (E) | **50.0%** | Explainability is well-instrumented (SHAP/LIME, source attribution, FactSheets) in half the scenarios, but two scenarios document no explainability mechanism at all and two others rely on generic rationale text rather than a named technique. |

### 2.3 Scenario Overview

| Scenario | Label | Status | Gaps |
|---|---|---|---|
| S1 | Predictive Model Governance & Continuous Monitoring | WARNING | 1 |
| S2 | RAG Application Quality Evaluation & Promotion-to-Production | FAIL | 1 |
| S3 | GenAI Use-Case Approval & Regulatory Risk Classification | FAIL | 2 |
| S4 | Prompt Security Hardening via Automated Red-Teaming | FAIL | 1 |
| S5 | Multi-Agent (Agentic AI) Governance Across the Lifecycle | WARNING | 1 |
| S6 | Virtual Assistant Production Quality & Safety Monitoring | FAIL | 2 |
| S7 | Governed AI-Assisted Candidate Screening and Interview Coordination | FAIL | 2 |
| S8 | Enterprise Model Risk Governance (MRG) Across Multi-Cloud Third-Party Models | WARNING | 1 |

---

## 3. Detailed Scenario Analysis

### S1 — Predictive Model Governance & Continuous Monitoring

**Status: WARNING — 1 gap.** S1 shows strong, well-evidenced Collaborative, Responsible, and Explainable properties through named human-AI review roles, fairness/drift governance under NIST AI RMF/ISO 42001, and SHAP/LIME explanations; its single gap concerns unconfirmed automation of the closed-loop retraining cycle.
*Evidence IDs: E-003, E-006, E-009, E-014, E-017, E-021 · Confidence: High*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | Data Scientist–OpenScale threshold configuration, Data Analyst explainability review, and stakeholder issue-tracking form a sustained, jointly-executed governance workflow rather than a one-off interaction. |
| Adaptive | 2 – Proactive (capped by Major gap) | Real-time threshold-breach alerts are raised by the system without explicit human prompting, but the closed-loop retraining they trigger is only inferred, capping the level below Social. |
| Responsible | 3 – Social | Fairness/drift metrics, FactSheet auto-updates, and a persistent issue-tracking workflow sustain accountability over the model's full lifecycle. |
| Explainable | 2 – Proactive | Local/global SHAP/LIME explanations are generated automatically as part of monitoring, but the sheet shows a review relationship rather than iterative human-AI explanation refinement. |

#### G-S1-01 — Closed-Loop Retraining Automation Not Evidenced

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Major | Learning/improvement via feedback loops derived from human and system signals |

**Gap Description:** The extraction sheet itself tags this scenario's Adaptive property as "(partial)" and its Observed/Inferred status as "Observed (partial Inferred on closed-loop retraining automation)." The Feedback Mechanisms column only confirms that "real-time threshold-breach alerts feed back to stakeholders for remediation" — a human-mediated notification, not a documented automated retrain-and-redeploy cycle. Decision Points list "trigger remediation/retraining on alert" but do not clarify whether this is automatic or requires separate manual initiation. Without confirmed evidence, the system's central Adaptive claim (continuous self-improvement) is unverified.

**Practical Impact:** Governance stakeholders cannot be certain whether a model actually retrains itself after a threshold breach or whether retraining is a manual, easily-delayed action requiring a human to notice the alert and separately kick off a job — a material difference for audit and risk-management purposes.

**Recommendation: Evidence and Formalize Closed-Loop Retraining**
Implement (or, if already implemented, document and expose) an explicit, automated retraining trigger tied directly to threshold-breach alerts, with an audit trail confirming that each cycle executes end-to-end without manual reinitiation.
*Implementation:* Add a logged retraining-trigger event schema, captured in the AI FactSheet or monitoring dashboard, that timestamps alert → retrain-job-start → retrain-job-complete, and expose this trail to Compliance/Audit stakeholders.
*Priority:* Medium
*Expected HI Impact:* Elevates Adaptive from a partially-evidenced claim to a demonstrable, auditable capability, strengthening trust in the model lifecycle's self-improvement story and likely moving S1 to PASS.

---

### S2 — RAG Application Quality Evaluation & Promotion-to-Production

**Status: FAIL — 1 gap.** S2 shows solid Collaborative, Adaptive, and Explainable mechanisms through iterative pipeline refinement and a dedicated source-attribution explainability view, but the scenario documents zero fairness or content-safety evaluation capability anywhere in its Capabilities or Evaluation Metrics columns — a Critical Responsible gap for an application that serves answers to real end users.
*Evidence IDs: E-008, E-015 · Confidence: High*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | The Developer iteratively refines the RAG pipeline based on Validator review and evaluation results, a sustained co-construction cycle rather than a single hand-off. |
| Adaptive | 3 – Social | Continuous production-payload logging feeds the evaluation loop, and the Developer explicitly "refines the pipeline" from that feedback over time. |
| Responsible | 1 – Reactive (capped by Critical gap) | With no fairness or content-safety mechanism at all, the only oversight evidenced is the Validator's on-demand promotion review — an explicitly instructed, one-off check. |
| Explainable | 2 – Proactive | Root-cause analysis and source-attribution reports are generated as standard outputs, but the sheet shows the Validator querying them rather than a sustained explanatory dialogue. |

#### G-S2-01 — No Fairness or Content-Safety Mechanism in Production RAG Pipeline

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Critical | Fairness/bias-mitigation mechanisms (no mechanism present at all) |

**Gap Description:** S2's Capabilities column lists only Retrieval Evaluation, Text Quality Evaluation, and Explainability (source attribution); its Evaluation Metrics list only retrieval- and answer-quality measures (Context Relevance, Retrieval Precision, Average Precision, Hit Rate, NDCG, Faithfulness, Answer Relevance, Answer Similarity, Unsuccessful Requests). Nowhere in the row do the terms "fairness," "bias," "PII," or "HAP" appear. This is a complete absence of the fairness/bias-mitigation sub-component of the Responsible property — not a deficiency in degree, but a total gap — in a scenario whose stated goal is producing grounded, relevant answers for an enterprise knowledge-base application reaching real users.

**Practical Impact:** A RAG application can pass every retrieval/answer-quality gate in this scenario and still be promoted to production while generating biased, unsafe, or personally identifying content, because no such check exists in the evaluated pipeline.

**Recommendation: Introduce Fairness and Content-Safety Evaluation for RAG Outputs**
Add a bias/fairness screening capability (e.g., disparate-impact or demographic-parity checks on generated answers) plus content-safety detectors (PII/HAP, as already used in S1 and S6) into the RAG evaluation pipeline, alongside the existing retrieval/answer-quality metrics.
*Implementation:* Extend the evaluation metric set with fairness and content-safety scores, and make them a blocking gate the Validator must clear before the "promote application to production" decision point.
*Priority:* High
*Expected HI Impact:* Closes a Critical Responsible gap and prevents biased or unsafe generated answers from reaching production users, likely moving S2 to PASS or WARNING.

---

### S3 — GenAI Use-Case Approval & Regulatory Risk Classification

**Status: FAIL — 2 gaps.** S3's multi-stage human review process delivers strong Collaborative and Responsible oversight, but the scenario's own HI Characteristics omit Adaptive entirely, and its only candidate feedback mechanism is explicitly hedged as speculative; its explanation mechanism for automated risk scoring is also comparatively underspecified.
*Evidence IDs: E-001, E-003, E-007, E-008, E-010 · Confidence: High (partial Inferred on resubmission loop)*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | The multi-stage sequential review across Legal, Data Protection, Brand, and Approver roles with the governance assistant is a structured, repeated collaborative workflow. |
| Adaptive | 1 – Reactive (capped by Critical gap) | No confirmed feedback/learning mechanism exists; the only candidate loop (resubmission) is explicitly hedged as "likely...(inferred)." |
| Responsible | 3 – Social | Sequential, multi-role approve/reject review with documented compliance rationale sustains accountability across the full use-case lifecycle. |
| Explainable | 2 – Proactive | The engine generates a risk score and category without being separately asked, but no interactive or factor-level explanation mechanism is documented. |

#### G-S3-01 — No Confirmed Feedback/Learning Loop

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Critical | Learning/improvement via feedback loops (no mechanism confirmed) |

**Gap Description:** Unlike every other scenario except S7, S3's HI Characteristics column ("Collaborative; Responsible; Explainable") does not list Adaptive at all. The Feedback Mechanisms column offers only "Rejected/conditionally-approved use cases likely returned to requester for revision (inferred)" — a mechanism the extraction sheet itself flags with both a hedge word ("likely") and an inference tag. There is no evidence that review criteria, questionnaire scoring, or risk thresholds are ever updated based on accumulated review outcomes.

**Practical Impact:** The GenAI use-case approval process may never improve its own risk-classification accuracy over time, and requesters whose use cases are rejected have no confirmed, documented path back into the process — a governance and user-experience risk in a regulatory workflow.

**Recommendation: Establish a Verified Use-Case Resubmission and Learning Loop**
Formally document and evidence the resubmission/revision cycle for rejected or conditionally-approved use cases, and capture whether/how questionnaire scoring or review thresholds are refined based on accumulated review outcomes.
*Implementation:* Log every rejection/resubmission event in the workflow system, and track whether questionnaire weightings or risk thresholds are periodically updated using aggregated review-stage outcomes.
*Priority:* High
*Expected HI Impact:* Converts a speculative, unevidenced feedback path into a demonstrable Adaptive mechanism, likely moving S3 out of FAIL status.

#### G-S3-02 — Underspecified Risk-Score Explanation Mechanism

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Minor | Justification of AI-generated decisions/recommendations to human partners |

**Gap Description:** S3's HI Characteristics claim Explainable, and Outputs include "documented compliance rationale." However, unlike S1 (SHAP/LIME), S2 (source attribution), or S8 (Shapley/LIME), no named explainability technique or factor-level justification is documented for how the risk-assessment questionnaire engine arrives at its EU AI Act risk category — the rationale output is a general narrative rather than a traceable, factor-by-factor justification.

**Practical Impact:** Reviewers (Legal, Data Protection, Brand) may have to trust the AI-generated risk score and category without being able to see precisely which questionnaire responses drove the classification, weakening their ability to challenge or verify it.

**Recommendation: Add Explicit Risk-Score Justification Output**
Have the risk-assessment questionnaire engine produce a structured, factor-level justification (e.g., which specific questionnaire fields drove the EU AI Act risk category) rather than only a general compliance rationale narrative.
*Implementation:* Extend the AI Tasks to include a rationale-generation step tied to specific risk-classification fields (data-usage risk, content-generation scope, audience impact, regulatory exposure, brand-risk), displayed to reviewers alongside the score.
*Priority:* Low
*Expected HI Impact:* Strengthens reviewer trust and auditability of automated risk categorization.

---

### S4 — Prompt Security Hardening via Automated Red-Teaming

**Status: FAIL — 1 gap.** S4's tight, iterative red-team-and-harden loop strongly evidences Collaborative, Adaptive, and Responsible properties, but the scenario's HI Characteristics list omits Explainable entirely, and no explainability capability appears anywhere in the row.
*Evidence IDs: E-012 · Confidence: High*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | The sheet explicitly describes an "iterative review-and-harden loop" between the Prompt Engineer and the red-teaming evaluator. |
| Adaptive | 3 – Social | A "tight feedback cycle" of human edit followed by AI re-evaluation is explicitly documented as recurring, not a single pass. |
| Responsible | 2 – Proactive | The evaluator proactively generates adversarial probes across three sophistication tiers without per-instance instruction, though oversight remains episodic per hardening round. |
| Explainable | 1 – Reactive (capped by Critical gap) | No explainability mechanism is documented at all; only numeric scores and generic hardening recommendations are produced. |

#### G-S4-01 — No Explainability Mechanism for Red-Teaming Findings

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Critical | AI clarifies and justifies its decisions/recommendations (no mechanism present at all) |

**Gap Description:** S4's HI Characteristics are listed as "Collaborative; Responsible; Adaptive" — Explainable is conspicuously absent, and no row in the Capabilities column names an explainability capability (unlike S1, S2, S5, S7, S8, all of which list Explainable). The Outputs include an "Adversarial Robustness Score," "Prompt Leakage Risk Score," and "hardening recommendations," but nothing in the sheet describes how or why a given probe succeeded, i.e., no per-probe justification accompanies the numeric scores.

**Practical Impact:** The Prompt Engineer receives a robustness score and a generic hardening recommendation but not the specific adversarial technique or reasoning that produced the score, making it harder to target fixes precisely and verify that a hardening change actually addresses the underlying vulnerability rather than coincidentally raising the score.

**Recommendation: Add Explanation Layer to Red-Teaming Findings**
Require the red-teaming evaluator to justify each adversarial robustness/leakage score with the specific probe(s) and reasoning that produced it, rather than only a numeric score and generic recommendation.
*Implementation:* Extend Outputs to include a per-probe rationale (which adversarial technique succeeded or failed, and why) surfaced to the Prompt Engineer during the review-and-harden loop.
*Priority:* High
*Expected HI Impact:* Establishes a previously entirely-absent Explainable capability, enabling engineers to target fixes precisely and likely moving S4 out of FAIL status.

---

### S5 — Multi-Agent (Agentic AI) Governance Across the Lifecycle

**Status: WARNING — 1 gap.** S5 exhibits robust Collaborative and Responsible governance spanning the full agent lifecycle (creation, development, production), but the feedback loop connecting SME red-teaming findings to agent hardening is explicitly flagged as only partially inferred.
*Evidence IDs: E-005, E-010, E-011, E-018 · Confidence: High*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | SME observation/verification episodes and Developer catalog tool-selection span the full creation-development-production lifecycle, indicating sustained joint governance. |
| Adaptive | 2 – Proactive (capped by Major gap) | Production alerts are raised proactively by the system, but the SME-finding-to-hardening remediation loop is explicitly "partially inferred." |
| Responsible | 3 – Social | Benchmark scoring, safety metrics, and catalog approval checkpoints operate continuously across all lifecycle stages with sustained human governance. |
| Explainable | 2 – Proactive | Comparative evaluation reports are produced automatically, but no named explainability capability or interactive justification mechanism is evidenced. |

#### G-S5-01 — Agent Remediation Feedback Loop Only Partially Evidenced

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Major | Learning/improvement via feedback loops derived from human actions and signals |

**Gap Description:** The Feedback Mechanisms column states: "Production alerts trigger human review; SME red-teaming findings feed back into hardening (partially inferred)." While production alerting to humans is clearly evidenced, the mechanism by which SME findings actually translate into agent/tool hardening is explicitly marked as inferred rather than observed — mirroring S1's pattern of an unconfirmed closed loop, here applied to the multi-agent lifecycle rather than a single predictive model.

**Practical Impact:** It is unclear whether agents flagged as susceptible during red-teaming are reliably hardened and re-certified before being trusted again in the Governed Agentic Catalog, or whether this depends on informal, undocumented follow-up.

**Recommendation: Confirm and Instrument the Agent Remediation Feedback Loop**
Document and verify how SME red-teaming findings concretely feed into agent hardening — e.g., automatic re-benchmarking or catalog re-certification — replacing the currently inferred mechanism with an observable, logged workflow.
*Implementation:* Capture red-team-finding-to-remediation events in the Governed Agentic Catalog's audit trail, tied to before/after benchmark and safety scores.
*Priority:* Medium
*Expected HI Impact:* Converts a partially-inferred Adaptive claim into demonstrable evidence, supporting trust in the agent lifecycle and likely moving S5 to PASS.

---

### S6 — Virtual Assistant Production Quality & Safety Monitoring

**Status: FAIL — 2 gaps.** S6's closed alert-review-improve-remonitor loop strongly supports Collaborative and Adaptive properties, but the scenario documents no explainability mechanism at all, and its alert-prioritization logic is only inferred.
*Evidence IDs: E-013 · Confidence: High (partial Inferred on alert prioritization)*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | The documented "alert → engineer review → prompt-engineer improvement → re-monitoring" loop is an explicitly closed, repeating cycle. |
| Adaptive | 3 – Social | The same closed alert-to-improvement-to-re-monitoring loop demonstrates sustained, iterative system improvement driven by human action. |
| Responsible | 2 – Proactive | Alerts are generated automatically and proactively, but the criteria used to prioritize them for review are only "partially inferred," preventing a stronger accountability rating. |
| Explainable | 1 – Reactive (capped by Critical gap) | No explainability capability or mechanism is documented anywhere in the scenario record. |

#### G-S6-01 — No Explainability Mechanism for Flagged Responses

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Critical | AI clarifies and justifies its decisions/recommendations (no mechanism present at all) |

**Gap Description:** S6's HI Characteristics are "Collaborative; Responsible; Adaptive" — Explainable is absent, and the Capabilities column lists only Content Safety Detection and Text Quality Evaluation, with no Explainability capability (in contrast to S1, S2, S5, S7, S8). Metric scores (PII, HAP, ROUGE, METEOR, Readability) tell an engineer *that* a response breached a threshold but nothing in the sheet describes *why* — no flagged-span, contributing-factor, or rationale output is documented.

**Practical Impact:** Engineers reviewing alerts must diagnose the root cause of a flagged response from the raw metric score alone, slowing down the alert-to-prompt-improvement cycle and increasing the risk of misdiagnosing which part of a response triggered the breach.

**Recommendation: Add Explainability Capability to Virtual Assistant Monitoring**
Introduce a mechanism — e.g., response-level rationale, source/citation attribution, or a flagged-span explanation — so engineers understand why a given response triggered a PII/HAP/quality alert, not just the metric score.
*Implementation:* Extend Content Safety Detection / Text Quality Evaluation outputs with a brief flagged-span or contributing-factor explanation attached to each alert.
*Priority:* High
*Expected HI Impact:* Establishes a currently entirely-absent Explainable capability, enabling faster and more targeted prompt improvements, and likely moving S6 out of FAIL status.

#### G-S6-02 — Alert-Prioritization Logic Unverified

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Minor | Oversight and accountability (triage criteria undocumented) |

**Gap Description:** The Decision Points column notes "alert prioritization (partially inferred)." While alerts clearly reach engineers, the criteria used to decide which breached metric takes priority for review is not confirmed in the sheet, only inferred.

**Practical Impact:** Without documented triage criteria, review priority may be applied inconsistently across engineers or over time, weakening the accountability trail for why some alerts are acted on faster than others.

**Recommendation: Formalize Alert Prioritization Criteria**
Define and document explicit, evidenced criteria for how breached metrics are triaged for engineer review, replacing the currently inferred prioritization logic.
*Implementation:* Publish a documented severity/priority matrix (e.g., PII > HAP > readability) within the monitoring dashboard, and log how each alert was classified against it.
*Priority:* Low
*Expected HI Impact:* Strengthens accountability and consistency of the human review step.

---

### S7 — Governed AI-Assisted Candidate Screening and Interview Coordination

**Status: FAIL — 2 gaps.** S7 shows strong Collaborative interaction and a well-instrumented Fairness Assessment capability, but its own HI Characteristics omit Adaptive, its confirmed feedback mechanism is explicitly hedged, and its candidate report cards lack a documented factor-level explanation.
*Evidence IDs: E-016 · Confidence: Medium · Observed (Inferred on exact feedback mechanism and baseline dataset)*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 2 – Proactive | IRIS conducts voice screening calls and generates report cards proactively, but the interaction pattern is more episodic review than sustained co-construction, consistent with the scenario's Medium confidence rating. |
| Adaptive | 1 – Reactive (capped by Critical gap) | Adaptive is absent from the scenario's own characteristics list, and the only feedback mechanism cited is explicitly "partially inferred." |
| Responsible | 2 – Proactive | Fairness and drift monitoring run continuously and automatically, but their translation into pipeline oversight action is not clearly evidenced beyond inference. |
| Explainable | 2 – Proactive | Candidate report cards are generated automatically as a scoring summary, but no factor-level justification mechanism is documented. |

#### G-S7-01 — No Confirmed Adaptive Feedback Loop in Hiring Pipeline

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Adaptive | Critical | Learning/improvement via feedback loops (no mechanism confirmed) |

**Gap Description:** Like S3, S7's HI Characteristics ("Collaborative; Responsible; Explainable") omit Adaptive entirely. The only stated feedback mechanism — "Continuous bias/drift monitoring feeding back into pipeline oversight" — is explicitly qualified as "(partially inferred mechanism)," and the scenario's overall Confidence is Medium (lower than every other scenario except S8's Medium-High), with the Observed/Inferred column further noting inference on "exact feedback mechanism and baseline dataset." No concrete evidence links bias/drift signals to specific pipeline adjustments.

**Practical Impact:** In a high-stakes, high-volume hiring context, an unconfirmed feedback loop means there is no verified assurance that detected bias or drift actually results in a pipeline correction rather than being logged and left unaddressed.

**Recommendation: Evidence the Bias/Drift-to-Pipeline-Oversight Feedback Loop**
Concretely document and log how continuous bias/drift monitoring signals translate into actual pipeline adjustments (e.g., re-weighting, threshold changes, model swaps), replacing the currently partially-inferred mechanism, and clarify the baseline dataset used for bias/drift comparison.
*Implementation:* Capture an auditable event trail linking each bias/drift signal to a specific pipeline-oversight action or an explicit "no action" decision, and document the reference/baseline dataset used.
*Priority:* High
*Expected HI Impact:* Establishes a previously unevidenced Adaptive capability in a high-stakes hiring context, supporting continuous fairness assurance and likely moving S7 out of FAIL status.

#### G-S7-02 — Candidate Report Cards Lack Factor-Level Explanation

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Explainable | Minor | Justification of AI-generated decisions/recommendations to human partners |

**Gap Description:** S7's HI Characteristics claim Explainable, and "candidate report cards" are produced as an Output. However, no Capability in the sheet is named "Explainability," and no mechanism (comparable to S1's SHAP/LIME or S2's source attribution) is documented for how the report card's shortlisting recommendation is justified from the underlying screening-call transcript/audio.

**Practical Impact:** Recruiters reviewing report cards may act on a shortlist recommendation without a clear, auditable basis for why a given candidate scored as they did, which is a meaningful concern in a regulated, fairness-sensitive hiring process.

**Recommendation: Enrich Candidate Report Cards with Decision Rationale**
Extend report cards to include the specific factors (e.g., transcript excerpts, scored competencies) that drove a candidate's shortlisting recommendation, not just a summary score.
*Implementation:* Add a structured rationale field generated alongside the report card, tied to specific evidence from the screening-call transcript/audio.
*Priority:* Medium
*Expected HI Impact:* Improves recruiter trust and auditability of AI-driven shortlisting in a high-volume hiring process.

---

### S8 — Enterprise Model Risk Governance (MRG) Across Multi-Cloud Third-Party Models

**Status: WARNING — 1 gap.** S8 demonstrates comprehensive Collaborative, Adaptive, and Explainable governance across a large, multi-cloud model inventory, with only a Minor Responsible gap around the precision of the accountable human role and the accessibility of primary workflow documentation.
*Evidence IDs: E-002, E-004, E-010, E-014, E-019, E-020, E-022 · Confidence: Medium-High*

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 – Social | Model Validator approval, Model Risk Officer reporting, and end-user rating capture together sustain a governed relationship across a large, ongoing multi-cloud model inventory. |
| Adaptive | 3 – Social | Production feedback "automatically triggers retraining/review workflows with retained human risk oversight," an explicitly closed and sustained loop. |
| Responsible | 2 – Proactive (capped by Minor gap kept conservative) | FactSheets and dashboards proactively surface fairness/drift/quality status, but the exact accountable role and primary workflow documentation remain unverified. |
| Explainable | 3 – Social | Explainability is a named capability with Shapley/LIME metrics synced consistently via FactSheets across multiple third-party providers, indicating a systematic, sustained explanation infrastructure. |

#### G-S8-01 — Accountable Risk-Oversight Role and Primary Workflow Documentation Unverified

| CARE Dimension | Severity | HI Principle Violated |
|---|---|---|
| Responsible | Minor | Accountability (exact accountable role and process documentation unverified) |

**Gap Description:** The Observed/Inferred column notes "Observed (Inferred on exact risk-oversight role title; primary MRG workflow doc inaccessible)." While "human risk-oversight function" is listed as a Human Agent, its precise title, authority, and scope are inferred rather than confirmed, and the primary MRG workflow documentation was inaccessible during extraction. This leaves the exact accountability chain for model risk decisions incompletely evidenced, even though the surrounding oversight activities (Validator approval, Risk Officer reporting, compliance sign-off) are otherwise well documented.

**Practical Impact:** In a regulated, multi-jurisdiction financial/insurance environment, an imprecisely documented accountable role and an inaccessible primary governance workflow document could complicate regulatory audits or create ambiguity about who bears ultimate responsibility for a risk decision.

**Recommendation: Document the Human Risk-Oversight Role and MRG Workflow**
Formally define and publish the exact title, authority, and responsibilities of the human risk-oversight function, and make the primary MRG workflow documentation accessible for audit and verification rather than relying on inference.
*Implementation:* Publish a governance charter naming the accountable role, and link the MRG workflow specification directly to the model inventory system for auditor access.
*Priority:* Medium
*Expected HI Impact:* Closes an evidentiary gap in accountability documentation, strengthening auditability across the multi-cloud model inventory and likely moving S8 to PASS.

---

## 4. Consolidated Recommendations

### Collaborative
*No gaps identified in this dimension; no recommendations required.*

### Adaptive

| Gap ID | Priority | Source Scenario | Recommendation | Implementation Note |
|---|---|---|---|---|
| G-S1-01 | Medium | S1 | Evidence and Formalize Closed-Loop Retraining | Log alert → retrain-start → retrain-complete events in the FactSheet/dashboard and expose the trail to Compliance/Audit stakeholders. |
| G-S3-01 | High | S3 | Establish a Verified Use-Case Resubmission and Learning Loop | Log every rejection/resubmission event and track whether questionnaire weightings/thresholds are updated from aggregated outcomes. |
| G-S5-01 | Medium | S5 | Confirm and Instrument the Agent Remediation Feedback Loop | Capture red-team-finding-to-remediation events in the Governed Agentic Catalog's audit trail, tied to before/after benchmark scores. |
| G-S7-01 | High | S7 | Evidence the Bias/Drift-to-Pipeline-Oversight Feedback Loop | Log an auditable trail linking each bias/drift signal to a pipeline action or explicit "no action," and document the baseline dataset. |

### Responsible

| Gap ID | Priority | Source Scenario | Recommendation | Implementation Note |
|---|---|---|---|---|
| G-S2-01 | High | S2 | Introduce Fairness and Content-Safety Evaluation for RAG Outputs | Add fairness and PII/HAP metrics as a blocking gate before the production-promotion decision. |
| G-S6-02 | Low | S6 | Formalize Alert Prioritization Criteria | Publish a documented severity/priority matrix and log each alert's classification against it. |
| G-S8-01 | Medium | S8 | Document the Human Risk-Oversight Role and MRG Workflow | Publish a governance charter naming the accountable role and link the MRG workflow spec into the model inventory system. |

### Explainable

| Gap ID | Priority | Source Scenario | Recommendation | Implementation Note |
|---|---|---|---|---|
| G-S4-01 | High | S4 | Add Explanation Layer to Red-Teaming Findings | Surface per-probe rationale (technique + reasoning) alongside numeric robustness/leakage scores. |
| G-S6-01 | High | S6 | Add Explainability Capability to Virtual Assistant Monitoring | Attach a flagged-span or contributing-factor explanation to each PII/HAP/quality alert. |
| G-S3-02 | Low | S3 | Add Explicit Risk-Score Justification Output | Generate a factor-level rationale tied to specific risk-classification fields alongside the score. |
| G-S7-02 | Medium | S7 | Enrich Candidate Report Cards with Decision Rationale | Add a structured rationale field tied to specific screening-call evidence. |

---

## 5. HI Maturity Assessment

**HI Maturity Level: Level 1 — Partial HI.** This level indicates that Hybrid Intelligence elements are present and structurally embedded across the system's usage scenarios — particularly consistent, well-defined human-AI collaboration — but that the remaining CARE properties (most notably Adaptive and Explainable) are only inconsistently or partially evidenced, and over half of scenarios contain at least one Critical deficiency that undermines full CARE conformance.

| CARE Dimension | Score | Status |
|---|---|---|
| Collaborative | 100.0% | Strong |
| Responsible | 62.5% | Adequate |
| Adaptive | 50.0% | Needs Work |
| Explainable | 50.0% | Needs Work |

**Strengths**

Every scenario in the sheet documents explicit, structured, role-differentiated interaction between named human agents and named AI components, with no Collaborative gaps found anywhere — this is the system's most consistent CARE property. Responsible governance is strong wherever model outputs are directly scored: S1, S7, and S8 all carry an explicit Fairness Assessment capability with named fairness/bias metrics (disparate impact, statistical parity difference, bias/drift status). Several scenarios (S2, S4, S6) document tightly closed, explicitly evidenced Adaptive feedback loops — iterative pipeline refinement, a "tight feedback cycle" of human-edit-then-AI-re-evaluation, and a closed alert-review-improve-remonitor cycle. Explainability is well-instrumented via named techniques (SHAP/LIME, source attribution, Shapley/LIME synced through FactSheets) in S1, S2, and S8.

**Areas for Improvement**

The Adaptive property is the least consistently evidenced CARE dimension: four scenarios (S1, S3, S5, S7) either omit Adaptive from their own HI Characteristics or have their stated feedback mechanism explicitly flagged as partial/inferred in the sheet. Explainability is entirely absent — not merely weak — in two scenarios (S4, S6), despite Explainable being one of the four defining CARE pillars. A production-facing GenAI application (S2) has no fairness or content-safety mechanism of any kind, a Critical Responsible gap. Accountability documentation has specific, named gaps around the exact human risk-oversight role and workflow documentation (S8) and around alert-triage criteria (S6).

---

## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)

### 6.1 Per-Scenario CARE Levels

| Scenario | Collaborative | Adaptive | Responsible | Explainable |
|---|---|---|---|---|
| S1 | 3 – Social | 2 – Proactive | 3 – Social | 2 – Proactive |
| S2 | 3 – Social | 3 – Social | 1 – Reactive | 2 – Proactive |
| S3 | 3 – Social | 1 – Reactive | 3 – Social | 2 – Proactive |
| S4 | 3 – Social | 3 – Social | 2 – Proactive | 1 – Reactive |
| S5 | 3 – Social | 2 – Proactive | 3 – Social | 2 – Proactive |
| S6 | 3 – Social | 3 – Social | 2 – Proactive | 1 – Reactive |
| S7 | 2 – Proactive | 1 – Reactive | 2 – Proactive | 2 – Proactive |
| S8 | 3 – Social | 3 – Social | 2 – Proactive | 3 – Social |

### 6.2 Use-Case CARE Maturity Summary

| Dimension | Level 1 – Reactive | Level 2 – Proactive | Level 3 – Social | Modal Level |
|---|---|---|---|---|
| Collaborative | 0 | 1 | 7 | **3 – Social** |
| Adaptive | 2 | 2 | 4 | **3 – Social** |
| Responsible | 1 | 4 | 3 | **2 – Proactive** |
| Explainable | 2 | 5 | 1 | **2 – Proactive** |

The Collaborative dimension is overwhelmingly Social (sustained, co-constructed human-AI relationships in 7 of 8 scenarios). Adaptive is bimodal — where evidenced, it tends to be fully Social (closed, iterative loops), but two scenarios have no confirmed loop at all, capping them at Reactive. Responsible and Explainable both cluster at Proactive: the AI in most scenarios initiates monitoring, scoring, or explanation generation without being explicitly re-prompted, but sustained, co-constructed oversight or explanation dialogue (Social) is evidenced in only a minority of scenarios for each dimension.

---

## 7. Methodology

This report was produced by a single large language model working directly from the Phase 1 knowledge-acquisition extraction sheet for IBM watsonx.governance (columns: Scenario, Human Agents, AI Agents, Goals, Human Tasks, AI Tasks, Capabilities, Context, Inputs, Outputs, Interactions, Decision Points, Feedback Mechanisms, Evaluation Metrics, HI Characteristics, Evidence IDs, Confidence, Observed/Inferred). No knowledge graph, ontology alignment, or formal (SHACL) constraint validation was used; all findings are derived directly from the row-level content of the sheet, including its own hedges (e.g., "partial," "inferred," "likely") and omissions from the HI Characteristics column, without introducing outside knowledge of the product.

**Scoring conventions applied:**
- Per-scenario score: PASS = 1.0, WARNING = 0.75, FAIL = 0.0.
- Overall HI Conformance = mean of the eight per-scenario scores, expressed as a percentage.
- CARE dimension score = proportion of scenarios with no gap in that dimension, expressed as a percentage.
- HI Maturity Level (from overall score): ≥90% Level 4 Exemplary HI; ≥70% Level 3 Established HI; ≥50% Level 2 Emerging HI; ≥25% Level 1 Partial HI; otherwise Level 0 Pre-HI.
- Gap severity: Critical (a core CARE requirement is absent, e.g. no AI/human participation, no fairness mechanism at all), Major (a requirement is present but substantially deficient), Minor (a small deficiency).
- CARE capability level per scenario per dimension: 1 – Reactive (only on explicit instruction), 2 – Proactive (AI initiates/anticipates unprompted), 3 – Social (sustained, repaired, or co-constructed over time). The maximum admissible level per dimension per scenario is capped by the most severe identified gap in that dimension: Critical → capped at 1, Major → capped at 2, Minor/no gap → uncapped at 3; within the cap, the level was chosen conservatively where direct evidence was absent.
- Capability levels were aggregated across scenarios by distribution and modal (most frequent) level, not by averaging, since the scale is ordinal.
