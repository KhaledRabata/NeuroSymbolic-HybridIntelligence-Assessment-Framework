# HI Assessment Report: LinkedIn Recruiter

**Assessment Date:** August 28, 2026
**Method:** LLM-Only Baseline Assessment

---

## 1. Executive Summary

This assessment evaluates LinkedIn Recruiter against the CARE framework (Akata et al., 2020) across its eight documented usage scenarios (S1–S8), using only the content of the Phase 1 knowledge-acquisition extraction sheet. The system achieves an Overall HI Conformance score of **78.1%**, placing it at **HI Maturity Level 3: Established HI**. Of the eight scenarios, one (S1 — AI-Assisted Candidate Sourcing) passes with no identified gaps, and the remaining seven receive a WARNING status due to one or more Minor or Major gaps. No scenario received a FAIL rating, meaning no scenario was found to be missing a CARE property entirely (e.g., no scenario lacks human participation, AI participation, or any fairness mechanism whatsoever). Nine distinct HI gaps were identified across the eight scenarios.

By CARE dimension, **Collaborative** is the system's strongest property (87.5% of scenarios show no gap): almost every scenario documents genuine bidirectional human-AI interaction — natural-language dialogue, iterative refinement, and shared task execution — with the recruiter (and, in S4, the Responsible AI Team) retaining final decision authority throughout. **Explainable** is the second-strongest property (75%), anchored by a dedicated explainability scenario (S5) with visible qualification match/gap indicators, filter breakdowns, and refinement suggestions, though this strength is not uniformly carried into every scenario. **Adaptive** and **Responsible** are tied as the weakest dimensions (62.5% each). Adaptive gaps cluster around feedback mechanisms that the sheet itself marks as "(Inferred)" rather than "Observed" — meaning parts of the learning loop are asserted but not evidenced — and around a hiring-manager feedback channel (S6) that is captured but not shown to close back into system learning. Responsible gaps concern transparency to the candidate (undocumented AI disclosure in S3), the validity of protected-attribute inference used for fairness measurement (S4), and an unsubstantiated bias-auditing claim for the evaluation model (S2).

Overall, the extraction sheet describes a system with substantial, well-evidenced HI characteristics in its core sourcing, evaluation, search, and fairness-ranking workflows, where human oversight is explicit ("human decision only," "human-only" contact and advancement points appear repeatedly) and AI participation is concrete and multi-agent. The gaps identified are, with one exception, Major or Minor rather than Critical — they represent documentation and mechanism-completeness deficiencies rather than absences of collaboration, learning, oversight, or explanation altogether. This is consistent with an Established HI system: the core CARE architecture is in place and operating, but several feedback loops and transparency mechanisms are incompletely evidenced or incompletely surfaced to the humans who would benefit from them.

The improvement potential is concentrated and tractable. Closing the nine identified gaps — most urgently the three Major gaps (candidate AI-disclosure documentation in S3, protected-attribute proxy validation in S4, and HLTM personalisation explanations in S7) — would remove every scenario from WARNING status and could plausibly move the system from Level 3 (Established HI) toward Level 4 (Exemplary HI), since six of the eight scenarios already score at PASS-adjacent levels with only isolated, well-scoped deficiencies.

---

## 2. HI Conformance Overview

### 2.1 Overall Score

| Metric | Value |
|---|---|
| Overall HI Conformance | 78.1% |
| HI Maturity Level | Level 3: Established HI |
| Scenarios Assessed | 8 |
| Scenarios PASS | 1 (12.5%) |
| Scenarios WARNING | 7 (87.5%) |
| Scenarios FAIL | 0 (0%) |
| Total HI Gaps | 9 |

Level 3 (Established HI) indicates that the four CARE properties are consistently implemented and evidenced across most scenarios and agent interactions, but a systematic set of Minor and Major deficiencies — chiefly around feedback-loop closure and transparency documentation — still prevents the system from reaching Exemplary status.

### 2.2 CARE Dimension Analysis

| Dimension | Score | Interpretation |
|---|---|---|
| Collaborative | 87.5% | Human and AI agents co-participate in nearly every scenario via documented dialogue, iterative refinement, and shared task execution; only one scenario (S6) shows a gap, and it concerns the certainty of one supporting agent's participation rather than the core human-AI loop. |
| Adaptive | 62.5% | Feedback loops from recruiter (and in one case hiring-manager) actions are documented in most scenarios, but three scenarios rely on mechanisms the sheet itself labels "(Inferred)" rather than "Observed," or on a feedback channel that is captured but not shown to close back into learning. |
| Responsible | 62.5% | Oversight and human-only decision points are consistently strong, but three scenarios show specific deficiencies in fairness/transparency mechanisms: an unsubstantiated bias-auditing claim, an undocumented candidate-disclosure mechanism, and unvalidated protected-attribute proxy inference. |
| Explainable | 75.0% | A dedicated, well-evidenced explainability scenario (S5) anchors this dimension, but two scenarios show incomplete explanation surfacing — one partial by the sheet's own admission (S7/HLTM) and one relying on external rather than in-workflow documentation (S4/fairness). |

### 2.3 Scenario Overview

| Scenario | Status | Gaps |
|---|---|---|
| S1 — AI-Assisted Candidate Sourcing | PASS | 0 |
| S2 — AI-Driven Candidate Evaluation | WARNING | 1 |
| S3 — Automated Prescreening via InMail | WARNING | 1 |
| S4 — Fairness-Aware Representative Candidate Ranking | WARNING | 2 |
| S5 — Explainable AI-Assisted Search | WARNING | 1 |
| S6 — Recruiter-Hiring Manager Collaborative Decision Making | WARNING | 2 |
| S7 — Long-Term Personalisation via HLTM | WARNING | 1 |
| S8 — ATS Integration and Unified Applicant Management (RSC+) | WARNING | 1 |

---

## 3. Detailed Scenario Analysis

### S1 — AI-Assisted Candidate Sourcing

**Status:** PASS · **HI Gaps:** 0

The extraction sheet documents a fully-formed HI loop for this scenario: the recruiter and Hiring Assistant conduct natural-language dialogue, the AI performs multi-pass ranking and fairness-aware re-ranking, and the recruiter's implicit actions (view/contact/archive) feed both in-session personalisation and offline retraining. All supporting evidence is marked "Observed" with no inferred or undocumented elements, so no gap is recorded against any CARE dimension.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | Interactions include sustained NL dialogue ("Recruiter ↔ Hiring Assistant") plus recruiter refinement of qualifications and continuous background search, indicating a co-constructed working relationship rather than a single reactive exchange. |
| Adaptive | 3 — Social | HLTM stores preferences across sessions and combines with in-session personalisation and offline retraining, a sustained learning relationship built up over repeated recruiter interactions. |
| Responsible | 2 — Proactive | Fairness-aware re-ranking is applied automatically on every search without explicit recruiter instruction, but the sheet shows no sustained, co-constructed oversight relationship specific to this scenario (that role belongs to S4). |
| Explainable | 2 — Proactive | Qualification match/gap indicators and Economic Graph insights are surfaced automatically with every shortlist, but there is no evidence of iterative, dialogic explanation refinement within this scenario. |

All CARE dimensions are satisfied; no gaps identified.

---

### S2 — AI-Driven Candidate Evaluation

**Status:** WARNING · **HI Gaps:** 1

The scenario shows strong Collaborative, Adaptive, and Explainable evidence (evidence-cited summaries, human-only advance/archive decisions, HLTM personalisation), but its Responsible dimension rests partly on an unsubstantiated claim.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | Interactions show bidirectional "qualification refinement" dialogue between recruiter and Hiring Assistant, plus optional profile sharing with the hiring manager, sustained across the evaluation session. |
| Adaptive | 3 — Social | HLTM personalisation and recruiter advance/archive actions both feed model retraining, and hallucination-rate monitoring provides an ongoing quality-correction loop. |
| Responsible | 2 — Proactive | Hallucination-rate monitoring runs continuously without explicit human instruction (proactive), but the capped/weak evidence for bias auditing (see gap below) prevents a higher, more assured rating. |
| Explainable | 2 — Proactive | Evidence-cited summaries and match/gap indicators are generated automatically for every candidate, without a documented mechanism for iterative explanation dialogue. |

#### G-S2-01 — Unsubstantiated Bias-Auditing Claim for the Evaluation Model

| Field | Value |
|---|---|
| CARE Dimension | Responsible |
| Severity | Minor |
| HI Principle Violated | Fairness/bias-mitigation mechanisms must be concretely evidenced, not merely asserted |

**Gap Description:** The HI Characteristics column asserts "Responsible (no sensitive data in evaluation; no autonomous decisions; bias auditing)," but no AI Task, Capability, or Feedback Mechanism entry elsewhere in the S2 row names a bias-auditing process for the EON evaluation model. The scenario's own evidence supports "no sensitive data" and "no autonomous decisions" (human decision only), but the bias-auditing claim is not backed by a stated mechanism within this scenario's data, unlike the explicit LiFT/Fair Model Analyser apparatus described for the ranking model in S4.

**Practical Impact:** Recruiters and auditors reviewing this scenario in isolation have no documented basis for confirming that AI-driven candidate evaluations are checked for bias, even though the evaluation stage directly determines which candidates advance.

**Recommendation: Document and Instrument Evaluation-Stage Bias Auditing**
Extend a concrete, named bias-auditing mechanism (analogous to LiFT) to the EON-based evaluation and summary-generation pipeline, and record its outputs alongside the existing hallucination-rate monitoring.
*Implementation:* Add an evaluation-stage fairness audit log (subgroup-level match/gap and advance-rate parity metrics) to the internal monitoring already used for hallucination rate, and reference it explicitly in the scenario's Feedback Mechanisms.
*Priority:* Medium
*Expected HI Impact:* Converts an asserted Responsible property into a concretely evidenced one, closing the gap between claimed and demonstrated fairness oversight at the evaluation stage.

---

### S3 — Automated Prescreening via InMail

**Status:** WARNING · **HI Gaps:** 1

Collaborative, Adaptive, and Explainable evidence is solid (recruiter defines and edits, AI conducts volume Q&A and follow-ups, message model retrains from feedback, results are transparent). The sheet itself flags a Responsible transparency gap.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | The recruiter co-authors the InMail (drafts reviewed/edited before sending) and monitors an ongoing "Recruiter ↔ Hiring Assistant" loop while the AI autonomously handles volume Q&A and follow-ups. |
| Adaptive | 3 — Social | The message model retrains from recruiter thumbs-up/down feedback and follow-ups adapt to candidate non-response, an evolving, repaired interaction pattern over time. |
| Responsible | 2 — Proactive | The recruiter defines prescreening questions and the AI proactively conducts Q&A and follow-ups without per-message instruction; the level is capped by the disclosure gap below. |
| Explainable | 2 — Proactive | Full prescreening Q&A and aggregated results are made available to the recruiter automatically, without evidence of a further iterative explanation exchange. |

#### G-S3-01 — Candidate AI-Disclosure Not Documented

| Field | Value |
|---|---|
| CARE Dimension | Responsible |
| Severity | Major |
| HI Principle Violated | Accountability toward all interacting parties, including the candidate, not only the recruiter |

**Gap Description:** The sheet's own Observed/Inferred column explicitly flags this as a gap: "candidate AI disclosure not documented (GAP E-GAP-02)." The Hiring Assistant conducts personalised InMail outreach, prescreening Q&A, role-question answering, and automated follow-ups directly with candidates, but no evidence in the extraction sheet documents whether or how candidates are informed they are interacting with an AI system rather than the recruiter directly.

**Practical Impact:** Candidates may reasonably believe they are corresponding with a human recruiter throughout initial outreach and prescreening, which undermines the accountability and transparency expected of a Responsible HI system toward every party the AI interacts with, not just the recruiter who supervises it.

**Recommendation: Implement Explicit Candidate AI-Disclosure Notice**
Introduce and document a clear, consistent disclosure — surfaced at first AI-initiated contact (InMail) and reiterated during prescreening Q&A — informing candidates they are interacting with an AI-assisted system, with an easy path to reach the human recruiter.
*Implementation:* Add a disclosure line/template to the AI-generated InMail and prescreening message templates, and record its presence as a documented Capability/Evidence item in future extraction updates.
*Priority:* High
*Expected HI Impact:* Directly resolves the sheet-flagged accountability gap and brings candidate-facing accountability in line with the recruiter-facing oversight already documented elsewhere in the scenario.

---

### S4 — Fairness-Aware Representative Candidate Ranking

**Status:** WARNING · **HI Gaps:** 2

As the dedicated fairness scenario, S4 shows the most developed Responsible infrastructure in the sheet (LiFT, Fair Model Analyser, Mitigation Trainer, recurring audits, a Responsible AI Team with defined governance tasks). Two deficiencies nonetheless emerge from close reading of the scenario's own inputs and interactions.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | The LinkedIn Responsible AI Team engages in a recurring cycle of defining criteria, reviewing LiFT audit results, and approving model changes — a sustained, co-constructed oversight relationship with the AI system over time. |
| Adaptive | 3 — Social | LiFT performs continuous, recurring bias audits feeding an offline retraining/deramping cycle with updated fairness constraints — an explicitly sustained learning loop. |
| Responsible | 2 — Proactive (capped) | LiFT and the fairness re-ranking operate automatically and continuously (proactive), but the Major gap below (unvalidated protected-attribute proxies) caps this dimension below full Social-level maturity. |
| Explainable | 2 — Proactive | Re-ranked results are delivered "transparently" on every query automatically, but see the Minor gap below regarding in-workflow explanation to the recruiter. |

#### G-S4-01 — Protected Attributes Inferred via Unvalidated Proxies

| Field | Value |
|---|---|
| CARE Dimension | Responsible |
| Severity | Major |
| HI Principle Violated | Fairness/bias-mitigation mechanisms require accurate, accountable handling of sensitive attributes |

**Gap Description:** The Inputs column states that fairness measurement relies on "protected attribute proxies (gender/age inferred from profile signals)." The sheet documents the downstream audit and retraining apparatus (LiFT, Fair Model Analyser) in detail, but nowhere documents a validation, accuracy-checking, or consent/disclosure mechanism for the underlying proxy inference itself — the fairness system's entire measurement basis rests on an inferred, not verified, sensitive attribute.

**Practical Impact:** If the underlying gender/age proxies are systematically inaccurate for any subgroup, the entire representative-ranking correction built on top of them could misrepresent true fairness outcomes, while appearing statistically sound in LiFT's audit reports.

**Recommendation: Validate and Govern Protected-Attribute Proxy Inference**
Establish and document an explicit accuracy-validation and governance process for the gender/age inference step that precedes fairness measurement, distinct from the downstream ranking-fairness audit.
*Implementation:* Add a proxy-accuracy validation step (e.g., periodic sampling against self-reported data where available) to the Responsible AI Team's review cycle, and log its results as a distinct evidence item alongside LiFT's bias reports.
*Priority:* High
*Expected HI Impact:* Strengthens the credibility of the entire fairness-ranking apparatus by grounding it in a validated rather than assumed sensitive-attribute signal.

#### G-S4-02 — Fairness Rationale Not Surfaced to Recruiter In-Workflow

| Field | Value |
|---|---|
| CARE Dimension | Explainable |
| Severity | Minor |
| HI Principle Violated | The AI must clarify and justify its decisions to its human partners, not only to internal/external auditors |

**Gap Description:** The scenario's Explainable evidence consists of "fairness documented publicly; KDD paper; AI transparency page" and results being delivered "transparently" — but these are external/academic-facing artifacts, not an in-workflow explanation shown to the recruiter at the point of use (contrast with S1/S2/S5, which document explicit per-candidate match/gap indicators). No mechanism is described for a recruiter to see, at the moment of viewing results, why or how fairness re-ranking altered a given candidate's position.

**Practical Impact:** Recruiters using the system day to day have no documented in-context way to understand why fairness constraints changed their result ordering, limiting their ability to build informed trust in or scrutinise the mechanism they rely on.

**Recommendation: Surface In-Workflow Fairness Rationale to Recruiters**
Extend the existing qualification match/gap explanation pattern (already used in S1/S2/S5) to include a lightweight, recruiter-facing indicator of when and how fairness re-ranking affected the displayed order.
*Implementation:* Add a fairness-adjustment indicator to the candidate shortlist UI, reusing the explanation-surfacing pattern already implemented for qualification match/gap.
*Priority:* Medium
*Expected HI Impact:* Brings the recruiter-facing explainability of the fairness scenario up to the standard already achieved elsewhere in the system, improving recruiter trust and scrutiny capacity.

---

### S5 — Explainable AI-Assisted Search

**Status:** WARNING · **HI Gaps:** 1

Designated in the sheet as the "primary explainability scenario," S5 shows the strongest Explainable evidence of any scenario. Its Adaptive dimension, however, rests partly on a mechanism the sheet marks as inferred rather than observed.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | The recruiter provides intent via NL query and then iteratively accepts, modifies, or expands/narrows criteria based on AI explanations — a repaired, co-constructed search process within the session. |
| Adaptive | 2 — Proactive (conservative) | One feedback channel (recruiter contact actions → implicit model improvement) is Observed, but the sheet marks the other ("filter adjustment patterns → NL query parsing improvement") explicitly "(Inferred)," so a conservative, evidence-based level is chosen. |
| Responsible | 2 — Proactive | Search results are automatically "blocked from sensitive personal data" and equal treatment is tested, operating without explicit per-query instruction, but no sustained/social oversight relationship is documented specific to this scenario. |
| Explainable | 3 — Social | As the primary explainability scenario, results include filter breakdowns and suggested refinements that the recruiter iteratively acts on and refines against — a sustained, repaired explanation exchange within the session. |

#### G-S5-01 — Query-Refinement Learning Loop Only Inferred, Not Confirmed

| Field | Value |
|---|---|
| CARE Dimension | Adaptive |
| Severity | Minor |
| HI Principle Violated | Feedback loops must be derived from, and demonstrably closed with, human actions and signals |

**Gap Description:** The Feedback Mechanisms column lists two learning channels: "Recruiter contact actions → implicit model improvement signal" (stated as fact) and "filter adjustment patterns → NL query parsing improvement (Inferred)." The second — arguably the more direct signal of the recruiter's explanatory feedback loop — is explicitly marked as not confirmed/observed in the sheet.

**Practical Impact:** It cannot currently be verified from the available evidence that the system actually learns from how recruiters adjust their filters in response to explanations, meaning a core part of the "primary explainability scenario's" adaptive loop may not be operating as described.

**Recommendation: Confirm and Instrument the Query-Refinement Learning Loop**
Verify empirically whether filter-adjustment patterns are in fact used to improve NL query parsing, and if so, instrument and document the mechanism with the same evidentiary rigor as the confirmed contact-action signal.
*Implementation:* Add logging/evaluation of filter-adjustment-to-parsing-improvement correlation, and update the extraction evidence from "Inferred" to "Observed" once confirmed, or build the mechanism if it does not yet exist.
*Priority:* Medium
*Expected HI Impact:* Converts an unconfirmed adaptive claim into either verified evidence or a genuine capability, strengthening the credibility of the explainability scenario's learning loop.

---

### S6 — Recruiter-Hiring Manager Collaborative Decision Making

**Status:** WARNING · **HI Gaps:** 2

This scenario documents genuine human-human collaboration (recruiter and hiring manager) facilitated by AI-generated summaries and Microsoft Teams integration, with a clearly human-only final hiring decision. Two deficiencies emerge, both flagged by uncertainty markers in the sheet's own evidence columns.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 2 — Proactive (conservative) | The Observed/Inferred column itself notes "collaboration dynamics partially Inferred," and the supporting AI Follow-Up agent is explicitly labelled "(optional/Inferred)," so a conservative level is chosen despite solid evidence of AI-generated summaries facilitating the core recruiter-hiring manager exchange. |
| Adaptive | 2 — Proactive (capped) | Recruiter advance/reject decisions feed model retraining (proactive), but this dimension is capped by the Major gap below concerning hiring-manager feedback. |
| Responsible | 2 — Proactive | The final hiring decision is explicitly "human-only" and non-autonomous, a defined and automatic constraint on the AI's role. |
| Explainable | 2 — Proactive | AI-generated summaries with qualification match/gap are produced automatically to facilitate hiring-manager review, without evidence of iterative explanation dialogue specific to this scenario. |

#### G-S6-01 — AI Co-Participation in Follow-Up Only Optional/Inferred

| Field | Value |
|---|---|
| CARE Dimension | Collaborative |
| Severity | Minor |
| HI Principle Violated | Both human and artificial agents must actually take part in the recorded interactions |

**Gap Description:** The AI Agents column lists "AI Follow-Up (optional/Inferred)," and the AI Tasks column similarly hedges: "surface AI Follow-Ups if hiring manager feedback pending (Inferred)." The Observed/Inferred column further notes that "collaboration dynamics partially Inferred." This means the extent and consistency of the AI's own participation in this collaborative loop — beyond generating shareable summaries — is not confirmed by the sheet.

**Practical Impact:** Without confirmation, it is unclear whether the AI reliably supports the recruiter-hiring manager collaboration when feedback stalls, or whether this support is inconsistent/absent in practice, which affects the reliability of the collaborative workflow during delays.

**Recommendation: Confirm and Formalise AI Follow-Up Participation**
Verify whether the AI Follow-Up mechanism is actually deployed and, if so, document it as a standard (not optional/inferred) part of the collaborative workflow with clear triggering conditions.
*Implementation:* Audit production logs for AI Follow-Up trigger events tied to pending hiring-manager feedback, and update the scenario documentation from "Inferred" to "Observed" with concrete trigger criteria.
*Priority:* Low
*Expected HI Impact:* Removes ambiguity about AI participation in this workflow, strengthening confidence in the Collaborative property for this scenario.

#### G-S6-02 — Hiring-Manager Feedback Stored but Not Shown to Close the Loop

| Field | Value |
|---|---|
| CARE Dimension | Adaptive |
| Severity | Major |
| HI Principle Violated | Feedback loops must, in particular, incorporate feedback derived from human actions and signals |

**Gap Description:** The Feedback Mechanisms column states: "Hiring manager interview feedback stored in ATS/Recruiter notes; recruiter advance/reject decisions → model retraining signal." Only the recruiter's advance/reject decisions are explicitly described as feeding "model retraining"; the hiring manager's structured interview feedback — a distinct and valuable human signal specific to this scenario — is described only as being "stored," with no stated mechanism connecting it back into system learning or personalisation. This is compounded by all three Evaluation Metrics for this scenario being marked "(Inferred)," meaning there is no documented, measured evidence that the collaborative loop's outcomes are even being tracked.

**Practical Impact:** The hiring manager's domain expertise and interview-derived judgement — arguably the highest-value human signal in the hiring funnel — risks being captured but never used to improve future sourcing, evaluation, or ranking, wasting a valuable feedback source and leaving the scenario's adaptive claims largely unmeasured.

**Recommendation: Close the Hiring-Manager Feedback Loop**
Extend the model-retraining signal pathway that already ingests recruiter advance/reject actions to also ingest structured hiring-manager interview feedback, and instrument at least one of the currently-inferred evaluation metrics with real measurement.

*Implementation:* Route hiring-manager feedback stored in ATS/Recruiter notes into the same retraining pipeline used for recruiter actions, and begin tracking "alignment between recruiter and hiring manager" as a measured (not inferred) metric.
*Priority:* High
*Expected HI Impact:* Converts a currently one-directional, partially-measured collaboration into a fully closed, evidenced Adaptive loop that uses the hiring manager's expert judgement to improve future recommendations.

---

### S7 — Long-Term Personalisation via HLTM

**Status:** WARNING · **HI Gaps:** 1

Described as the "primary adaptivity scenario," S7 shows the strongest Adaptive evidence in the sheet, including a production-measured 5–10 percentage-point reduction in negative feedback. The sheet itself flags a corresponding Explainable deficiency.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | The recruiter validates HLTM-inferred preferences and provides ongoing feedback that updates long-term memory across sessions — an explicitly sustained, evolving collaboration built up over repeated hiring projects. |
| Adaptive | 3 — Social | Explicitly the "primary adaptivity scenario": HLTM ingests session outcomes continuously, with every session feeding forward into future personalisation, evidenced by a measured production metric. |
| Responsible | 2 — Proactive | HLTM scope boundaries (seat/project level) are defined and enforced automatically by LinkedIn Engineering/Privacy, a proactive built-in constraint, though no sustained/social oversight dialogue with the recruiter is documented for this dimension. |
| Explainable | 1 — Reactive (conservative) | The sheet explicitly states this dimension is "PARTIAL — HLTM inferences not surfaced as explicit explanations," meaning the scenario's defining capability (long-term personalisation) is not explained to the recruiter at all; a conservative level is chosen given this stated absence. |

#### G-S7-01 — HLTM-Driven Personalisation Not Explained to Recruiter

| Field | Value |
|---|---|
| CARE Dimension | Explainable |
| Severity | Major |
| HI Principle Violated | The AI must clarify and justify its decisions and recommendations to its human partners |

**Gap Description:** The HI Characteristics column explicitly states: "Explainable (PARTIAL — HLTM inferences not surfaced as explicit explanations; identified as gap E-GAP-04)." While the recruiter receives "personalised recommendations without explicit re-specification," the sheet documents no mechanism by which the recruiter is told which historical preferences HLTM applied, or why a given candidate was surfaced on the basis of accumulated history rather than the current session's stated qualifications alone.

**Practical Impact:** Recruiters cannot verify or correct the specific historical assumptions driving a personalised shortlist, which is especially consequential given the scenario's own Human Tasks require the recruiter to "validate HLTM-inferred preferences still apply" — a validation task that is difficult to perform without visibility into what is being inferred.

**Recommendation: Surface HLTM-Based Personalisation Explanations**
Add explicit, recruiter-facing indicators showing which historical preferences HLTM contributed to a given session's recommendations, enabling the validation step already required of the recruiter.
*Implementation:* Extend the existing qualification match/gap explanation surface to include a distinct "based on your history" annotation identifying which HLTM-sourced preference(s) influenced each recommendation.
*Priority:* High
*Expected HI Impact:* Directly resolves the sheet-flagged E-GAP-04 deficiency and makes the recruiter's required preference-validation task actually performable, strengthening trust in the system's primary adaptivity mechanism.

---

### S8 — ATS Integration and Unified Applicant Management (RSC+)

**Status:** WARNING · **HI Gaps:** 1

The scenario documents solid Collaborative (Recruiter Admin consent, recruiter decision authority), Responsible (opt-in-gated automation, customer data control), and Explainable (consistent evaluation summaries across sources) evidence. Its Adaptive dimension includes one mechanism marked as inferred.

**CARE Capability Levels**

| Dimension | Level | Rationale |
|---|---|---|
| Collaborative | 3 — Social | Continuous RSC+↔ATS data pull combines with sustained recruiter management of a unified applicant pipeline and an evolving, opt-in-negotiated customer relationship around automated stage syncing. |
| Adaptive | 2 — Proactive (conservative) | "Recruiter actions in unified view → model retraining signals" is stated as fact, but "ATS stage data → signals for future candidate pipeline modelling" is explicitly marked "(Inferred)," so a conservative level is chosen. |
| Responsible | 1 — Reactive | Automated stage syncing is explicitly gated behind "explicit opt-in," meaning this Responsible-relevant capability is, by the sheet's own description, only exercised upon explicit customer instruction. |
| Explainable | 2 — Proactive | Evaluation summaries are generated automatically for ATS-sourced applicants "same as LinkedIn-sourced," without documented evidence of further iterative explanation exchange. |

#### G-S8-01 — ATS-Driven Pipeline-Modelling Feedback Loop Only Inferred

| Field | Value |
|---|---|
| CARE Dimension | Adaptive |
| Severity | Minor |
| HI Principle Violated | Feedback loops must be derived from, and demonstrably closed with, human actions and signals |

**Gap Description:** The Feedback Mechanisms column states: "Recruiter actions in unified view → model retraining signals; ATS stage data → signals for future candidate pipeline modelling (Inferred)." The second channel — using ATS-side stage progression as a learning signal for future candidate pipeline modelling — is explicitly unconfirmed in the sheet, unlike the first, which is stated as an established fact.

**Practical Impact:** It cannot currently be verified from the available evidence that data flowing from the ATS side of the unified pipeline (as opposed to actions taken directly in the LinkedIn Recruiter view) actually contributes to system learning, leaving part of this scenario's adaptive claim unsubstantiated.

**Recommendation: Confirm and Instrument ATS Pipeline-Modelling Feedback**
Verify and, if necessary, build a concrete mechanism by which ATS stage-progression data feeds future candidate pipeline modelling, and document it with the same evidentiary standard as the confirmed recruiter-action signal.
*Implementation:* Instrument ATS stage-transition events (via the existing RSC+ API sync) as a logged training signal, and update the extraction evidence from "Inferred" to "Observed" once confirmed.
*Priority:* Medium
*Expected HI Impact:* Converts an unconfirmed adaptive claim into verified, documented evidence, strengthening confidence that the unified ATS/LinkedIn pipeline genuinely learns from both of its data sources.

---

## 4. Consolidated Recommendations

### Collaborative

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Confirm and Formalise AI Follow-Up Participation | Low | S6 | Verify whether the AI Follow-Up mechanism is actually deployed and document it as a standard, non-optional part of the collaborative workflow with clear triggering conditions. | Audit production logs for AI Follow-Up trigger events tied to pending hiring-manager feedback; update documentation from "Inferred" to "Observed." |

### Adaptive

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Confirm and Instrument the Query-Refinement Learning Loop | Medium | S5 | Verify whether filter-adjustment patterns are used to improve NL query parsing, and instrument/document the mechanism with the same rigor as the confirmed contact-action signal. | Add logging/evaluation of filter-adjustment-to-parsing-improvement correlation; update evidence status once confirmed. |
| Close the Hiring-Manager Feedback Loop | High | S6 | Extend the model-retraining pathway that ingests recruiter actions to also ingest structured hiring-manager interview feedback, and instrument a currently-inferred evaluation metric with real measurement. | Route ATS/Recruiter-notes hiring-manager feedback into the existing retraining pipeline; begin measuring recruiter-hiring manager alignment. |
| Confirm and Instrument ATS Pipeline-Modelling Feedback | Medium | S8 | Verify and, if necessary, build a mechanism by which ATS stage-progression data feeds future candidate pipeline modelling. | Instrument ATS stage-transition events via the existing RSC+ API sync as a logged training signal. |

### Responsible

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Document and Instrument Evaluation-Stage Bias Auditing | Medium | S2 | Extend a concrete, named bias-auditing mechanism to the EON-based evaluation pipeline, analogous to the LiFT system used for ranking. | Add an evaluation-stage fairness audit log (subgroup match/gap and advance-rate parity) alongside existing hallucination-rate monitoring. |
| Implement Explicit Candidate AI-Disclosure Notice | High | S3 | Introduce and document a clear disclosure at first AI-initiated candidate contact and during prescreening Q&A, informing candidates they are interacting with an AI system. | Add a disclosure line/template to AI-generated InMail and prescreening messages; record as a documented evidence item. |
| Validate and Govern Protected-Attribute Proxy Inference | High | S4 | Establish and document an accuracy-validation and governance process for the gender/age proxy inference underlying fairness measurement, distinct from the downstream ranking-fairness audit. | Add a periodic proxy-accuracy validation step to the Responsible AI Team's review cycle; log results as a distinct evidence item. |

### Explainable

| Recommendation | Priority | Source | Description | Implementation |
|---|---|---|---|---|
| Surface In-Workflow Fairness Rationale to Recruiters | Medium | S4 | Extend the existing qualification match/gap explanation pattern to include a recruiter-facing indicator of when and how fairness re-ranking affected result ordering. | Add a fairness-adjustment indicator to the candidate shortlist UI, reusing the existing explanation-surfacing pattern. |
| Surface HLTM-Based Personalisation Explanations | High | S7 | Add recruiter-facing indicators showing which historical preferences HLTM contributed to a session's recommendations, enabling the recruiter's required validation task. | Extend the match/gap explanation surface with a "based on your history" annotation identifying HLTM-sourced influences. |

---

## 5. HI Maturity Assessment

**HI Maturity Level: Level 3 — Established HI**

This level indicates that all four CARE properties are consistently implemented with concrete, mostly-Observed evidence across the great majority of documented usage scenarios, human oversight and decision authority is preserved throughout, and no scenario is missing a CARE property outright — but a recurring pattern of incompletely-closed feedback loops and incompletely-surfaced transparency mechanisms keeps the system below Exemplary status.

| Dimension | Score | Status |
|---|---|---|
| Collaborative | 87.5% | Strong |
| Adaptive | 62.5% | Adequate |
| Responsible | 62.5% | Adequate |
| Explainable | 75.0% | Adequate |

**Strengths**

Collaborative interaction is the system's clearest strength: seven of eight scenarios document genuine bidirectional human-AI exchange (natural-language dialogue, iterative refinement, shared drafting) with human decision authority explicitly preserved at every recorded decision point ("human decision only," "human-only," "explicitly non-autonomous"). Explainability is well-evidenced in the system's core search and evaluation workflows, anchored by a dedicated explainability scenario (S5) with visible filter breakdowns, qualification match/gap indicators, and actionable refinement suggestions. The fairness-ranking scenario (S4) demonstrates the most mature Responsible infrastructure in the sheet, with a dedicated Responsible AI Team, recurring automated audits (LiFT), and a defined retrain/deramp escalation path.

**Areas for Improvement**

Adaptive and Responsible are tied as the weakest dimensions. Three scenarios (S5, S6, S8) contain feedback mechanisms the sheet itself marks "(Inferred)" rather than "Observed," meaning parts of the system's claimed learning behavior are not yet confirmed by evidence; S6 additionally shows a hiring-manager feedback channel that is captured but not demonstrably used for learning. On Responsible, three scenarios show specific, addressable deficiencies: an unsubstantiated bias-auditing claim at the evaluation stage (S2), an explicitly sheet-flagged absence of candidate AI-disclosure documentation (S3), and unvalidated protected-attribute proxy inference underlying the fairness-ranking mechanism itself (S4). Explainability, while generally strong, has one scenario (S7) where the sheet explicitly documents a partial absence of explanation for the system's primary adaptivity mechanism, and one scenario (S4) where explanation exists only at an external/documentation level rather than in the recruiter's actual workflow.

---

## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)

### 6.1 Per-Scenario CARE Levels

| Scenario | Collaborative | Adaptive | Responsible | Explainable |
|---|---|---|---|---|
| S1 — AI-Assisted Candidate Sourcing | 3 — Social | 3 — Social | 2 — Proactive | 2 — Proactive |
| S2 — AI-Driven Candidate Evaluation | 3 — Social | 3 — Social | 2 — Proactive | 2 — Proactive |
| S3 — Automated Prescreening via InMail | 3 — Social | 3 — Social | 2 — Proactive | 2 — Proactive |
| S4 — Fairness-Aware Representative Candidate Ranking | 3 — Social | 3 — Social | 2 — Proactive | 2 — Proactive |
| S5 — Explainable AI-Assisted Search | 3 — Social | 2 — Proactive | 2 — Proactive | 3 — Social |
| S6 — Recruiter-Hiring Manager Collaborative Decision Making | 2 — Proactive | 2 — Proactive | 2 — Proactive | 2 — Proactive |
| S7 — Long-Term Personalisation via HLTM | 3 — Social | 3 — Social | 2 — Proactive | 1 — Reactive |
| S8 — ATS Integration and Unified Applicant Management (RSC+) | 3 — Social | 2 — Proactive | 1 — Reactive | 2 — Proactive |

### 6.2 Use-Case CARE Maturity Summary

**Collaborative**

| Level | Count | Scenarios |
|---|---|---|
| 1 — Reactive | 0 | — |
| 2 — Proactive | 1 | S6 |
| 3 — Social | 7 | S1, S2, S3, S4, S5, S7, S8 |

**Modal Level: 3 — Social**

**Adaptive**

| Level | Count | Scenarios |
|---|---|---|
| 1 — Reactive | 0 | — |
| 2 — Proactive | 3 | S5, S6, S8 |
| 3 — Social | 5 | S1, S2, S3, S4, S7 |

**Modal Level: 3 — Social**

**Responsible**

| Level | Count | Scenarios |
|---|---|---|
| 1 — Reactive | 2 | S6, S8 |
| 2 — Proactive | 6 | S1, S2, S3, S4, S5, S7 |
| 3 — Social | 0 | — |

**Modal Level: 2 — Proactive**

**Explainable**

| Level | Count | Scenarios |
|---|---|---|
| 1 — Reactive | 1 | S7 |
| 2 — Proactive | 6 | S1, S2, S3, S4, S6, S8 |
| 3 — Social | 1 | S5 |

**Modal Level: 2 — Proactive**

---

## 7. Methodology

This report was produced by a single LLM working directly from the Phase 1 knowledge-acquisition extraction sheet for LinkedIn Recruiter, without construction of a knowledge graph, without ontology alignment, and without formal (e.g., SHACL) constraint validation. All findings, gap identifications, and scores are derived solely from the sheet's own column content — including its explicit "(Inferred)" evidentiary markers and its two sheet-flagged gaps (E-GAP-02, E-GAP-04), which anchor two of the nine gaps identified — and no external knowledge of the LinkedIn Recruiter system was used.

The scoring conventions applied throughout are as specified for this assessment: each scenario is scored PASS = 1.0, WARNING = 0.75, or FAIL = 0.0, where a scenario with at least one Critical gap is FAIL, a scenario with only Minor/Major gaps is WARNING, and a scenario with no gaps is PASS. The Overall HI Conformance score is the unweighted mean of the eight per-scenario scores, expressed as a percentage. Each CARE dimension score is the proportion of the eight scenarios showing no gap in that dimension. The HI Maturity Level is derived from the overall score using the thresholds: ≥90% Level 4 (Exemplary HI), ≥70% Level 3 (Established HI), ≥50% Level 2 (Emerging HI), ≥25% Level 1 (Partial HI), otherwise Level 0 (Pre-HI). Gap severity is classified as Critical (a core CARE requirement absent — e.g., no AI or no human participation, no fairness mechanism at all), Major (a requirement present but substantially deficient), or Minor (a small deficiency), and this severity caps the maximum admissible CARE capability level for that scenario-dimension pair (Critical → cap 1, Major → cap 2, Minor/none → uncapped at 3); within any applicable cap, the specific level (1 — Reactive, 2 — Proactive, 3 — Social) was chosen based on the strongest evidence available in the sheet, defaulting to the more conservative (lower) level wherever supporting evidence was itself marked "(Inferred)" or otherwise absent. Capability levels are aggregated across scenarios by frequency distribution and modal value, consistent with their ordinal (non-interval) nature.
