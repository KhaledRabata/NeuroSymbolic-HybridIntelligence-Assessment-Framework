# Hybrid Intelligence Scenarios
## Neuro-Symbolic AI — Knowledge Acquisition Package
### Target: LinkedIn Recruiter + Hiring Assistant

> **Note:** All scenarios describe Hybrid Intelligence interactions within LinkedIn Recruiter + Hiring Assistant. Each scenario is evidence-backed. Where modelling assumptions are used, they are explicitly labelled **[ASSUMPTION]**. Facts not directly observed are labelled **[INFERRED]**.

---

## S1 — AI-Assisted Candidate Sourcing

**Scenario Name:** AI-Assisted Candidate Sourcing

**Description:**
A recruiter opens a new hiring project in LinkedIn Recruiter and expresses their hiring needs in natural language to the Hiring Assistant. The Hiring Assistant interprets the qualifications, translates them into optimised search queries, and autonomously searches LinkedIn's network of 1B+ member profiles to surface a ranked shortlist of qualified candidates, running continuously in the background. The recruiter reviews the shortlist and decides which candidates to contact.

**Goal:**
Identify qualified candidates matching defined role requirements from a network of 1B+ profiles, reducing recruiter time and effort while increasing candidate match quality.

**Human Actors:**
- Recruiter (primary): Specifies hiring qualifications in natural language; reviews shortlist; decides which candidates to contact or archive.
- Hiring Manager (secondary): May contribute hiring criteria during intake; provides role context.

**Artificial Agents:**
- Hiring Assistant (supervisor agent): Orchestrates the overall sourcing workflow.
- Intake Agent (sub-agent): Refines and structures qualifications from recruiter input.
- Sourcing Agent (sub-agent): Executes searches across the member database.
- Ranking Model (GBDT, GLMix): Ranks retrieved candidates by predicted match and response likelihood.
- Qualified Applicant (QA) Model: Predicts recruiter action likelihood per candidate.
- EON Model: Fine-tuned on Economic Graph data; evaluates candidates at scale for qualifications alignment.
- Economic Graph: Provides real-time market insights (skill supply/demand, talent flows).

**Context:**
- Corporate recruiting environment (in-house recruiter or staffing agency).
- Recruiter holds a LinkedIn Recruiter seat with Hiring Assistant add-on.
- Role may be new or a repeat of a similar previous role.
- Language: English (German, French rolling out 2026).

**Input Data:**
- Natural language hiring qualifications from recruiter (or job description + intake notes).
- Historical recruiter activity for similar roles (from HLTM long-term memory).
- LinkedIn member profiles (skills, experience, education, activity signals).
- Economic Graph data (skill supply/demand, location talent pools).
- 40+ structured search filters (titles, skills, location, industry, etc.).

**Knowledge Sources:**
- LinkedIn Skills Graph (36,000+ skills taxonomy).
- LinkedIn Economic Graph (1B+ members, 65M+ companies, 40K+ skills).
- HLTM — Hierarchical Long-Term Semantic Memory (past recruiter preferences).
- LinkedIn Recruiter search index (Galene search engine).

**Processing Method:**
- Natural language understanding → structured search query generation.
- Multi-pass ranking (coarse pass → re-ranking pass).
- GBDT and GLMix models applied per candidate.
- EON model for qualification-level evaluation.
- Fairness-aware re-ranking applied to results.
- Continuous background search with real-time updates.

**Processing Tasks (AI):**
1. Parse natural language qualifications into structured search parameters.
2. Generate multiple search queries covering the qualification space.
3. Retrieve matching candidates from the Galene search index.
4. Score and rank candidates (multi-pass ML models).
5. Apply fairness-aware re-ranking for representative results.
6. Generate candidate shortlist with summaries and qualification match/gap indicators.
7. Surface insights from Economic Graph (e.g., recommended locations, skill variants).

**Human Tasks:**
1. Define hiring qualifications in natural language or via job description.
2. Guide the Hiring Assistant with additional context if needed.
3. Review ranked shortlist.
4. Move candidates to next pipeline stage (Contacted) or archive them.
5. Provide implicit feedback (view, contact, archive) that feeds model retraining.

**Interaction Points:**
- Recruiter ↔ Hiring Assistant: Natural language dialogue to specify and refine qualifications.
- Hiring Assistant → Recruiter: Delivers ranked shortlist with qualification match/gap indicators.
- Recruiter → Model (implicit): Recruiter actions (view, contact, archive) used as training signals.

**Outputs:**
- Ranked candidate shortlist (with qualification match/gap per candidate).
- Economic Graph sourcing insights (recommended skills, locations, talent pools).
- Updated hiring project with candidates in Sourced/Uncontacted stage.

**Evaluation Metrics:**
- Profiles reviewed per qualified match (reported: 62–81% reduction vs. traditional search). [E-001, E-002, E-005]
- Time saved per role (reported: 4+ hours average). [E-001, E-002]
- Candidate shortlist quality (as assessed by recruiter via feedback signals). [E-027]
- Representative ranking coverage (gender/age proportionality). [E-010, E-041]

**Required Capabilities:**
- Natural language query parsing.
- Multi-filter structured search (40+ filters).
- Multi-pass ML ranking (GBDT, GLMix, QA model, EON model).
- Fairness-aware re-ranking.
- Economic Graph insight generation.
- Background continuous search.
- HLTM-based personalisation from past recruiter sessions.

**Decision Points:**
- Recruiter: Which candidates from the shortlist to contact (human decision only).
- Recruiter: Whether to refine qualifications after seeing initial results.
- Recruiter: Choice to enable or disable Hiring Assistant for a given project.

**Feedback Mechanisms:**
- Recruiter view/contact/archive actions → offline model retraining (GBDT, GLMix, QA model). [E-008, E-027]
- HLTM: Stores recruiter preferences across sessions; informs future sourcing without re-specification. [E-046]
- In-session personalisation: Real-time model adaptation within current session. [E-044]

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: Recruiter and Hiring Assistant jointly define and execute sourcing strategy; the AI handles search volume while the human exercises judgment over which candidates to pursue.
- **Adaptive**: HLTM adapts to recruiter preferences over time; in-session personalisation adapts within session; QA model continuously retrains on recruiter feedback.
- **Responsible**: Fairness-aware re-ranking ensures representative results (gender/age proportionality); no processing of sensitive personal data in ranking.
- **Explainable**: Qualification match/gap indicators shown per candidate; Economic Graph insights explain why certain candidates or locations are recommended.

**Evidence IDs:** E-001, E-002, E-005, E-006, E-007, E-008, E-010, E-012, E-013, E-014, E-023, E-024, E-025, E-027, E-028, E-041, E-042, E-043, E-044, E-045, E-046

**Confidence:** High (core scenario fully documented in official sources)

---

## S2 — AI-Driven Candidate Evaluation

**Scenario Name:** AI-Driven Candidate Evaluation

**Description:**
After sourcing a pool of candidates (either from LinkedIn search or ATS applicants via RSC+), the Hiring Assistant evaluates each candidate's profile and resume against the role's qualifications. It generates structured summaries of each candidate's suitability, citing evidence from the candidate's profile. The recruiter reviews these summaries and makes decisions on which candidates to advance or discard.

**Goal:**
Rapidly evaluate large numbers of candidates against role qualifications, producing evidence-cited summaries that enable recruiters to make informed decisions faster.

**Human Actors:**
- Recruiter: Reviews AI-generated candidate summaries; decides to advance or discard candidates; provides feedback (implicit via actions).
- Hiring Manager (secondary, optional): May review AI summaries shared by recruiter.

**Artificial Agents:**
- Hiring Assistant (supervisor agent): Coordinates evaluation workflow.
- Evaluation Agent (sub-agent): Evaluates candidates; generates evidence-cited qualification summaries.
- EON Model: Large-scale candidate evaluation on LinkedIn Economic Graph data.
- GPT-4o (Azure OpenAI): Complex qualification reasoning and summary generation.
- Qualified Applicant (QA) Model: Predicts recruiter action likelihood for additional scoring.
- RSC+ Integration: Supplies ATS-sourced applicant profiles and resumes to Hiring Assistant.

**Context:**
- Post-sourcing phase; pool of candidates already identified.
- May include both LinkedIn-sourced candidates and ATS applicants (via RSC+ Connected Projects).
- Recruiter has specified qualifications for the role.

**Input Data:**
- Candidate profiles from LinkedIn (experience, skills, education, activity signals, open-to-work status).
- ATS resume data and application records (via RSC+, with customer consent).
- Recruiter-defined qualifications for the role.
- Historical recruiter preferences (from HLTM).

**Knowledge Sources:**
- LinkedIn Skills Graph (skills taxonomy and relationships).
- Economic Graph (industry/title context).
- HLTM (recruiter's past preferences for similar roles).

**Processing Method:**
- EON model evaluates each candidate profile at scale against qualifications.
- GPT-4o used for complex reasoning, generating natural-language summaries.
- Speculative decoding used for latency optimisation.
- Evidence-citation mechanism: summaries reference specific profile sections.

**Processing Tasks (AI):**
1. Retrieve candidate profiles (LinkedIn + ATS if RSC+ enabled).
2. Match each profile against role qualifications (per qualification: found / not found / partial).
3. Generate evidence-cited candidate summary (citing profile sections that support each qualification match).
4. Rank candidates by overall qualification alignment score.
5. Surface qualification match/gap indicators in the UI.

**Human Tasks:**
1. Review AI-generated candidate summaries and match/gap indicators.
2. Evaluate whether AI assessment aligns with judgment.
3. Advance (contact) or archive candidates (the decision is always human).
4. Optionally share candidate summaries with hiring manager for input.
5. Provide feedback (view, advance, discard) that retrains models.

**Interaction Points:**
- Hiring Assistant → Recruiter: Delivers evaluation summaries with qualification match/gap indicators.
- Recruiter ↔ Hiring Assistant: Recruiter can refine qualifications if initial evaluation seems off.
- Recruiter → Hiring Manager: Profile/summary sharing (optional).
- Recruiter → Model (implicit feedback): Advance/discard actions used as training signals.

**Outputs:**
- Per-candidate qualification match/gap indicators.
- Evidence-cited candidate suitability summary.
- Ranked evaluation list.
- Updated pipeline (candidates advanced or archived).

**Evaluation Metrics:**
- Profiles reviewed per hire (62–81% reduction with HA). [E-001, E-002]
- Candidate summary accuracy (hallucination testing — internal). [E-019, E-020]
- Recruiter satisfaction with AI summaries (implicit via feedback signals).
- Negative feedback rate (5–10% reduction with HLTM personalisation). [E-046]

**Required Capabilities:**
- Large-scale candidate evaluation (EON model).
- Evidence-cited natural language summary generation (GPT-4o).
- Qualification match/gap indicator computation.
- ATS profile ingestion (RSC+).
- HLTM-based preference personalisation.
- Speculative decoding for latency management.

**Decision Points:**
- Recruiter: Advance or archive each candidate (human decision only).
- Recruiter: Override AI qualification assessment based on own judgment.
- Recruiter: Decide whether to use RSC+ Connected Projects.

**Feedback Mechanisms:**
- Recruiter advance/archive actions → model retraining. [E-008]
- HLTM updates: recruiter preferences from this session stored for future sessions. [E-046]
- Hallucination rate monitoring and model refinement (internal). [E-019]

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: AI performs volume evaluation; human reviews and decides; neither could effectively do this at scale alone.
- **Adaptive**: HLTM adapts to recruiter's preferences; models retrain from session actions.
- **Responsible**: No sensitive personal data processed in evaluation; no autonomous decisions; bias auditing per model; ATS data only used with customer consent.
- **Explainable**: Every AI evaluation is evidence-cited; qualification match/gap is shown transparently; recruiter can override.

**Evidence IDs:** E-002, E-005, E-013, E-014, E-015, E-016, E-019, E-020, E-033, E-034, E-035, E-046

**Confidence:** High

---

## S3 — Automated Prescreening via InMail

**Scenario Name:** Automated Prescreening via InMail

**Description:**
After shortlisted candidates are identified and first contact InMails are sent (either by recruiter manually or by Hiring Assistant), Hiring Assistant conducts prescreening Q&A sessions with candidates via InMail. It sends recruiter-defined prescreening questions, collects candidate responses, and confirms qualifications such as location preferences, work authorisation, salary expectations, and availability. Responses are aggregated and surfaced to the recruiter for review.

**Goal:**
Automate first-stage candidate qualification confirmation, reducing recruiter time on manual phone screens while maintaining candidate engagement quality.

**Human Actors:**
- Recruiter: Defines prescreening questions; reviews prescreening results; decides which candidates to advance to interview.
- Candidate (passive human actor): Responds to prescreening questions via InMail; may ask role clarification questions.

**Artificial Agents:**
- Hiring Assistant (supervisor agent): Manages prescreening workflow.
- Outreach/Screening Agent (sub-agent): Sends prescreening InMails; processes responses; answers candidate role questions.
- AI-Assisted Messages: Generates personalised initial outreach InMail.
- Automated Follow-Up System: Sends follow-up InMails if no response.

**Context:**
- Post-sourcing phase; candidates have been identified and initial contact InMail sent.
- Candidates are being screened before recruiter phone/video interview.
- Prescreening questions defined by recruiter for this specific role.

**Input Data:**
- Recruiter-defined prescreening questions (location, work authorisation, availability, salary, etc.).
- Candidate profile data (for personalised initial outreach).
- Candidate InMail responses.
- Job description / role details (for answering candidate questions).

**Knowledge Sources:**
- LinkedIn member profile (for personalisation of messages).
- Job requisition data.
- Recruiter-specified qualifications.

**Processing Method:**
- GPT-4o generates personalised initial InMail using recruiter info, candidate info, job info.
- Prescreening questions sent as follow-up after candidate responds to initial InMail.
- NLP processing of candidate responses to extract structured answers.
- Automated Follow-Up if no response received.

**Processing Tasks (AI):**
1. Generate personalised initial outreach InMail (AI-Assisted Messages).
2. Send prescreening questions when candidate replies to initial InMail.
3. Process candidate responses; extract and structure answers.
4. Answer candidate questions about the role (based on job description).
5. Send automated follow-up InMails if no response (Automated Follow-Ups).
6. Aggregate prescreening results; surface to recruiter.

**Human Tasks:**
1. Define prescreening questions before Hiring Assistant begins.
2. Review AI-drafted initial InMail; edit to reflect own tone before sending (optional — [INFERRED: recruiter may choose auto-send or review first]).
3. Review prescreening responses aggregated by Hiring Assistant.
4. Decide which candidates passed prescreening and should advance to interview.
5. Override AI prescreening assessment if needed.

**Interaction Points:**
- Hiring Assistant → Candidate: Sends personalised initial outreach InMail.
- Candidate → Hiring Assistant: Replies to InMail (candidate does not know whether interacting with AI or human — [ASSUMPTION: disclosure handled per platform terms; gap noted]).
- Hiring Assistant → Candidate: Sends prescreening questions; answers role questions.
- Hiring Assistant → Recruiter: Surfaces aggregated prescreening results.
- Recruiter ↔ Hiring Assistant: Recruiter can monitor and intervene at any point.

**Outputs:**
- Completed prescreening records per candidate (location confirmed/not confirmed, work auth, availability, salary, etc.).
- Candidates advanced to Replied stage in pipeline.
- Aggregated prescreening summary for recruiter review.
- Candidates meeting all criteria flagged for recruiter action.

**Evaluation Metrics:**
- InMail acceptance rate (66% higher with Hiring Assistant vs. traditional; 55% with AI-assisted messages; 39% with automated follow-ups). [E-001, E-002, E-030, E-032]
- Prescreening completion rate [INFERRED — not explicitly documented; gap E-GAP-02].
- Time saved in applicant identification (reported: 1.5 hours per role). [E-005]

**Required Capabilities:**
- AI-generated personalised InMail drafting (AI-Assisted Messages).
- Automated prescreening Q&A (NLP-based).
- Automated Follow-Up generation.
- Natural language processing of candidate responses.
- Role question answering (RAG over job description).

**Decision Points:**
- Recruiter: Which prescreening questions to include.
- Recruiter: Whether to review/edit InMail draft before sending.
- Recruiter: Which candidates passed prescreening and advance to interview.
- Recruiter: Whether to override Hiring Assistant's prescreening assessment.

**Feedback Mechanisms:**
- Recruiter thumbs up/down on InMail draft → refines AI message model. [E-030, E-031]
- InMail acceptance/response rates used as signal for model improvement [INFERRED]. [E-008]
- Recruiter advance/archive after prescreening → retraining signal. [E-008]

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: Hiring Assistant handles volume Q&A; recruiter handles final judgement; neither replaces the other.
- **Adaptive**: Message models retrain from recruiter feedback; Automated Follow-Ups adapt to non-response.
- **Responsible**: Recruiters define the questions; no autonomous advancement decisions; candidate data protected.
- **Explainable**: Recruiter can view full transcript of prescreening conversation [INFERRED]; prescreening results are structured and transparent.

**Evidence IDs:** E-001, E-002, E-005, E-012, E-013, E-030, E-031, E-032, E-038

**Confidence:** High (prescreening workflow well-documented; some interaction details inferred)

---

## S4 — Fairness-Aware Representative Candidate Ranking

**Scenario Name:** Fairness-Aware Representative Candidate Ranking

**Description:**
During candidate sourcing and ranking, LinkedIn Recruiter's ranking system applies a fairness-aware re-ranking step to ensure that search results are representative of the qualified candidate population. This corrects for model biases and historical data biases that might otherwise lead to under-representation of protected groups (gender, age). The recruiter sees a diversified shortlist reflecting the actual qualified population rather than a biased subset.

**Goal:**
Ensure ranked candidate results are statistically representative of the qualified candidate population with respect to protected attributes (gender, age), providing equal economic opportunity to all qualified candidates.

**Human Actors:**
- Recruiter: Interacts with the ranked results; may or may not be aware of the underlying fairness mechanism.
- LinkedIn Responsible AI Team: Designs and audits the fairness system; defines fairness criteria; monitors for drift.

**Artificial Agents:**
- Representative Ranking System: Applies fairness-aware re-ranking over candidate lists.
- LinkedIn Fairness Toolkit (LiFT): Measures bias in training data and model outputs; computes fairness metrics across subgroups.
- Fair Model Analyser: Audits models for detectable biases.
- Mitigation Trainer: Retrains models when bias is identified.
- Ranking Model (GBDT, GLMix): Base ranking; fairness-aware re-ranking applied on top.

**Context:**
- Deployed to 100% of LinkedIn Recruiter users worldwide (as of deployment). [E-010]
- Applied whenever a recruiter performs a candidate search query.
- Operates transparently in the background — recruiter does not explicitly invoke it.

**Input Data:**
- Ranked candidate list from base ML models.
- Protected attribute proxies (gender, age — inferred from profile signals — [INFERRED]).
- Qualified population distribution for the query (computed from the qualified candidate pool).
- Historical training data (audited for bias by LiFT).

**Knowledge Sources:**
- LinkedIn Fairness Toolkit (LiFT) bias measurement framework.
- Qualified candidate population distribution (derived from search results pool).
- Historical recruiter interaction logs (used to train models and detect bias).

**Processing Method:**
- LiFT measures bias in training data and model outputs.
- Fairness-aware re-ranking (Geyik et al. KDD 2019): re-ranks to achieve desired distribution of protected attributes in top-K results.
- Results: top-K results match protected attribute distribution of the qualified population.

**Processing Tasks (AI):**
1. Compute qualified candidate population distribution for the current query.
2. Apply base ranking (GBDT, GLMix).
3. Apply fairness-aware re-ranking to top-K results.
4. Surface re-ranked results to recruiter.
5. LiFT monitors training data and model outputs for bias (offline, recurring).
6. If bias detected: investigate, retrain (or deramp) model.

**Human Tasks:**
1. LinkedIn Responsible AI Team: Define fairness criteria and measurement framework. [E-009, E-019]
2. LinkedIn Responsible AI Team: Review LiFT audit results; approve/mandate model changes. [E-009]
3. Recruiter: Review ranked results (unaware of fairness mechanism in most cases — [INFERRED]).
4. Recruiter: Make final contact decisions based on reviewed results.

**Interaction Points:**
- LiFT → Responsible AI Team: Automated bias reports requiring human review.
- Responsible AI Team → Engineering: Trigger retraining or model demotion.
- Ranking System → Recruiter: Delivers re-ranked results (transparent to recruiter).

**Outputs:**
- Candidate shortlist with representative distribution of qualified candidates.
- ~3x increase in search queries with representative results (vs. pre-fairness-system). [E-041]
- LiFT bias audit reports (internal).

**Evaluation Metrics:**
- Representative ranking coverage: % of queries returning representative results. [E-041]
- Gender representation ratio in top-K results vs. qualified population. [E-041, E-009]
- Bias detection rate (LiFT outputs). [E-017, E-018]
- InMail acceptance rate impact (system must not harm engagement metrics). [E-041]

**Required Capabilities:**
- Fairness-aware re-ranking (Geyik et al. algorithm). [E-041]
- LiFT bias measurement across protected attribute subgroups. [E-017, E-018]
- Qualified population distribution estimation. [E-041]
- Per-model bias auditing (fair model analyser). [E-019]
- Model retraining with bias mitigation (mitigation trainer). [E-019]

**Decision Points:**
- LinkedIn Responsible AI Team: What constitutes the "qualified population" for a query.
- LinkedIn Responsible AI Team: Which protected attributes to include in fairness constraints.
- LinkedIn Responsible AI Team: Whether to retrain, deramp, or modify a model.
- Recruiter: Final candidate contact decisions (human decision only).

**Feedback Mechanisms:**
- LiFT continuous monitoring: recurring bias audits. [E-017, E-018]
- Recruiter contact patterns: monitored for emergent bias (downstream). [E-009]
- Model retraining cycle: offline periodic retraining incorporates updated fairness constraints. [E-008]

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: LinkedIn AI team + ranking AI collaborate to maintain fairness; recruiter benefits without direct involvement.
- **Adaptive**: Fairness system adapts through recurring LiFT audits and model retraining.
- **Responsible**: Core responsibility scenario; fairness constraints embedded in the ranking pipeline by design.
- **Explainable**: Fairness mechanisms documented publicly (AI Transparency page); research published at KDD; recruiter can understand why diverse results appear.

**Evidence IDs:** E-009, E-010, E-017, E-018, E-019, E-020, E-041, E-047

**Confidence:** High (well-documented in both official sources and peer-reviewed research)

---

## S5 — Explainable AI-Assisted Search

**Scenario Name:** Explainable AI-Assisted Search

**Description:**
A recruiter uses LinkedIn Recruiter's Advanced AI-Assisted Search to find candidates using natural language instead of manually filling in structured search filters. The system interprets the recruiter's natural language query, translates it into filters, and executes the search. The system also identifies which qualifications are present and which are absent in each candidate's profile, providing transparent explanations that help the recruiter quickly assess fit.

**Goal:**
Enable recruiters to search for candidates using natural language while receiving transparent, explainable results that show why specific candidates are ranked highly and where qualifications are missing.

**Human Actors:**
- Recruiter: Types natural language search query; interprets and acts on results; adjusts query based on explanations.

**Artificial Agents:**
- Advanced AI-Assisted Search: Interprets natural language query; generates filters; executes search.
- XAI Explanation Module: Generates per-candidate qualification match/gap indicators.
- Galene Search Engine: Executes search queries across member index.
- Ranking Model (GBDT): Applies base ranking over retrieved candidates.

**Context:**
- Recruiter performing ad hoc candidate search, not using full Hiring Assistant workflow.
- Available as a feature within LinkedIn Recruiter (all customers as of May 2024). [E-006]

**Input Data:**
- Natural language search query from recruiter.
- LinkedIn member profiles.
- 40+ structured search filter taxonomy.

**Knowledge Sources:**
- LinkedIn Skills Graph (for skill interpretation and expansion).
- Economic Graph (for job title normalisation, industry context).

**Processing Method:**
- GenAI model (LLM) interprets natural language query; maps to structured filters (job titles, skills, location, industry, etc.).
- Galene executes structured query; retrieves matching candidates.
- GBDT model ranks candidates.
- XAI module computes per-candidate qualification match/gap.
- Results displayed with match/gap indicators.

**Processing Tasks (AI):**
1. Parse natural language query into structured filter taxonomy.
2. Generate expanded variants (e.g., related skills, title variations).
3. Execute search via Galene search engine.
4. Rank results (GBDT model).
5. Compute qualification match/gap per candidate.
6. Return results with explanations.

**Human Tasks:**
1. Type natural language search query.
2. Review results with qualification match/gap indicators.
3. Refine query based on explanations (e.g., expand criteria if too narrow).
4. Select candidates to contact or add to project.

**Interaction Points:**
- Recruiter → AI-Assisted Search: Natural language query input.
- AI-Assisted Search → Recruiter: Returns results with filter breakdown and qualification match/gap.
- AI-Assisted Search → Recruiter: Suggests filter adjustments (e.g., expand to related skills). [E-011]

**Outputs:**
- Candidate results with applied filter breakdown (transparency of how query was interpreted).
- Per-candidate qualification match/gap indicators.
- Suggested search refinements (related skills, expanded criteria).

**Evaluation Metrics:**
- Search result quality (implicit — recruiter contact actions). [E-008]
- Filter interpretation accuracy (internal evaluation). [E-019, E-020]
- Time to first qualified contact [INFERRED — not explicitly documented].

**Required Capabilities:**
- Natural language query parsing and filter mapping.
- Skill and title expansion (Skills Graph).
- Per-candidate qualification match/gap computation.
- XAI recommendation generation (expand search criteria).

**Decision Points:**
- Recruiter: Whether to accept AI-suggested filter interpretation or modify.
- Recruiter: Whether to expand search criteria based on AI suggestions.
- Recruiter: Which candidates to contact based on results.

**Feedback Mechanisms:**
- Recruiter contact actions → model improvement signal (implicit). [E-008]
- Filter adjustment patterns used to improve NL query parsing [INFERRED, Medium Confidence].

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: Recruiter provides intent in natural language; AI handles query formalisation and ranking.
- **Adaptive**: Skills Graph and search models continuously updated as new skills and titles emerge. [E-023]
- **Responsible**: Blocked from returning results based on sensitive personal data inputs; equal treatment tested. [E-020]
- **Explainable**: This is the primary explainability scenario — qualification match/gap visible per candidate; filter interpretation shown; suggestions provided for query refinement.

**Evidence IDs:** E-006, E-008, E-011, E-019, E-020, E-023, E-024, E-041, E-042

**Confidence:** High

---

## S6 — Recruiter-Hiring Manager Collaborative Decision Making

**Scenario Name:** Recruiter-Hiring Manager Collaborative Decision Making

**Description:**
After the Hiring Assistant produces a shortlist of candidates and initial prescreening is complete, the recruiter and hiring manager collaborate to evaluate candidates and make the final hiring decision. LinkedIn Recruiter facilitates this through profile sharing, collaborative feedback, and Microsoft Teams integration for real-time alignment on candidate feedback.

**Goal:**
Enable structured collaboration between recruiter and hiring manager to make an informed, aligned, and accountable final hiring decision.

**Human Actors:**
- Recruiter: Manages the hiring project; shares candidate profiles with hiring manager; collects and synthesises feedback; coordinates scheduling; presents final recommendation.
- Hiring Manager: Reviews shared candidate profiles; provides interview feedback; makes final hiring decision.

**Artificial Agents:**
- Hiring Assistant (supervisor): Surfaces candidate shortlist; provides AI-generated summaries to facilitate review.
- Microsoft Teams Integration: Supports real-time recruiter-hiring manager collaboration.
- AI Follow-Up (optional): Helps recruiter follow up with hiring manager if feedback pending [INFERRED from Teams integration feature description].

**Context:**
- Post-shortlisting phase; candidates have been sourced, evaluated, and prescreened.
- Recruiter and hiring manager may be in different locations / time zones.
- Organisation using Microsoft Teams.

**Input Data:**
- AI-generated candidate summaries (with qualification match/gap).
- Recruiter's own assessment of candidates.
- Prescreening results (from S3).
- Hiring manager's interview notes and feedback.
- Job description and hiring criteria.

**Knowledge Sources:**
- Hiring project data (collected candidate history, pipeline stage, notes).
- ATS records (if RSC+ enabled).

**Processing Method:**
- Recruiter shares candidate profiles and AI summaries via Recruiter or Teams.
- Hiring manager provides feedback (structured or unstructured).
- Recruiter synthesises feedback and recommendation.
- Final hiring decision made by hiring manager (human-only).

**Processing Tasks (AI):**
1. Generate candidate summaries for sharing.
2. Facilitate sharing of profiles via Teams.
3. Surface AI Follow-Ups if hiring manager feedback is pending [INFERRED].

**Human Tasks:**
1. Recruiter: Share shortlisted candidate profiles with hiring manager.
2. Hiring Manager: Review profiles and AI-generated summaries.
3. Hiring Manager: Provide structured interview feedback.
4. Recruiter: Synthesise hiring manager feedback with own assessment.
5. Hiring Manager: Make final hiring decision.
6. Recruiter: Communicate decision; initiate offer process.

**Interaction Points:**
- Recruiter ↔ Hiring Manager (via Teams): Real-time alignment on candidate feedback.
- Hiring Assistant → Recruiter (via AI summaries): AI summaries facilitate hiring manager review.
- Hiring Manager → Recruiter: Structured/unstructured interview feedback.

**Outputs:**
- Agreed shortlist of finalists for offer.
- Hiring decision (to hire or reject each candidate).
- Interview feedback records.
- Offer initiation (human-driven).

**Evaluation Metrics:**
- Time from shortlist to hiring decision [INFERRED — no explicit metric documented; noted as gap].
- Hiring manager satisfaction with candidate quality [INFERRED].
- Alignment between recruiter and hiring manager assessments [INFERRED].

**Required Capabilities:**
- Profile sharing between recruiter and hiring manager.
- Microsoft Teams collaboration integration.
- AI-generated candidate summaries (for sharing).

**Decision Points:**
- Hiring Manager: Final hiring decision — this is always human; explicitly non-autonomous. [E-019, E-020]
- Recruiter: Which candidates to advance to hiring manager review.
- Recruiter: How to synthesise conflicting feedback.

**Feedback Mechanisms:**
- Hiring manager interview feedback → recruiter-managed (stored in ATS/Recruiter notes).
- Recruiter advance/reject decisions → model retraining signal. [E-008]

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: Core human-human collaboration scenario facilitated by AI tools; both recruiter and hiring manager must align.
- **Adaptive**: AI summaries adapt to candidate profile data; system adapts from recruiter post-decision actions.
- **Responsible**: Final decision explicitly human-only; accountability clear between recruiter and hiring manager.
- **Explainable**: AI summaries provide transparent evidence for each candidate; hiring manager can see what the AI found and why.

**Evidence IDs:** E-002, E-005, E-019, E-020, E-039, E-040

**Confidence:** Medium-High (Teams integration documented; some collaboration details inferred)

---

## S7 — Long-Term Personalisation via Hierarchical Memory (HLTM)

**Scenario Name:** Long-Term Personalisation via Hierarchical Memory

**Description:**
LinkedIn Hiring Assistant uses a Hierarchical Long-Term Semantic Memory (HLTM) system to remember recruiter preferences across multiple sessions and multiple similar roles. When a recruiter begins a new hiring project for a role similar to previously filled roles, the system draws on stored preferences to personalise sourcing and evaluation recommendations without requiring the recruiter to re-specify requirements they have already implicitly communicated through past behaviour.

**Goal:**
Personalise Hiring Assistant recommendations based on accumulated recruiter preference history, reducing cognitive burden and improving candidate quality from the first interaction of each new session.

**Human Actors:**
- Recruiter: Benefits from personalised recommendations without needing to re-specify past preferences; may observe improved recommendation quality over time.

**Artificial Agents:**
- HLTM (Hierarchical Long-Term Semantic Memory): Schema-aligned memory tree; stores recruiter preferences at multiple granularity levels (seat, project, role type).
- Hiring Assistant (supervisor): Queries HLTM at session start to personalise sourcing/evaluation.
- Sourcing Agent: Uses HLTM-derived preferences in search query generation.
- Evaluation Agent: Uses HLTM-derived preferences in candidate scoring.

**Context:**
- Recruiter is beginning a new hiring project for a role similar to previously filled roles.
- HLTM has been populated from prior recruiter sessions.
- System deployed in production for 6+ months as of publication of HLTM paper (2026). [E-046]

**Input Data:**
- Current session recruiter input (natural language qualifications for new role).
- HLTM historical preference data (from past sessions for similar roles).
- LinkedIn member profiles.

**Knowledge Sources:**
- HLTM: Hierarchical semantic memory tree (seat-level, project-level, role-type-level).
- LinkedIn Skills Graph, Economic Graph (for matching preferences to current market data).

**Processing Method:**
- At session start: HLTM queried for relevant historical preference data.
- Multi-granularity retrieval: low-latency lookup across preference tree levels.
- Preferences merged with current-session recruiter input.
- Personalised sourcing and evaluation executed.
- Session results: new interactions stored back to HLTM (lossless incremental ingestion).

**Processing Tasks (AI):**
1. Query HLTM for preference data relevant to current role type.
2. Merge historical preferences with current session specifications.
3. Execute personalised sourcing and evaluation (as per S1, S2).
4. Ingest current session outcomes back into HLTM.
5. Maintain privacy alignment (data scoped to seat/project boundaries).

**Human Tasks:**
1. Recruiter: Specify current role qualifications (may be briefer due to HLTM pre-population).
2. Recruiter: Validate that HLTM-inferred preferences still apply to new role.
3. Recruiter: Provide feedback actions (advance/archive) that further update HLTM.

**Interaction Points:**
- Hiring Assistant → Recruiter: Personalised recommendations without explicit re-specification.
- Recruiter → HLTM (implicit): Advance/archive actions update long-term preferences.

**Outputs:**
- Higher-quality initial candidate shortlist (from first interaction of new session).
- 5–10 percentage-point reduction in negative feedback rate vs. non-HLTM baseline. [E-046]

**Evaluation Metrics:**
- Negative feedback rate reduction (5–10% measured in production). [E-046]
- Recruiter re-specification rate [INFERRED — if HLTM works, recruiter should specify less].
- Session start to first qualified candidate time [INFERRED].

**Required Capabilities:**
- Schema-aligned hierarchical memory tree construction and querying.
- Massively parallel memory ingestion.
- Low-latency retrieval for serving.
- Privacy-scoped data segmentation (seat, project).
- Lossless incremental memory update.
- Multi-granularity semantic representation.

**Decision Points:**
- Recruiter: Whether to accept HLTM-inferred preferences or override with explicit specification.
- LinkedIn Engineering/Privacy: What scope boundaries to apply to HLTM data (seat, project level).

**Feedback Mechanisms:**
- Recruiter actions (advance, archive, contact) in current session → HLTM update. [E-046]
- Continuous: every session feeds forward into future personalisation.

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: HLTM enables smoother human-AI collaboration by reducing re-specification burden.
- **Adaptive**: This is the primary adaptivity scenario — system explicitly learns from recruiter history across sessions.
- **Responsible**: Memory scoped to privacy boundaries; member data not cross-contaminated between customers.
- **Explainable**: [PARTIAL] HLTM inferences are not currently surfaced to the recruiter as explicit explanations of why recommendations changed — identified as gap (E-GAP-04).

**Evidence IDs:** E-008, E-027, E-044, E-046

**Confidence:** High (HLTM paper provides direct evidence; production deployment confirmed)

---

## S8 — ATS Integration and Unified Applicant Management (RSC+)

**Scenario Name:** ATS Integration and Unified Applicant Management via RSC+

**Description:**
A recruiter using an ATS (Applicant Tracking System) connected to LinkedIn via Recruiter System Connect Plus (RSC+) creates a Connected Project that links a LinkedIn hiring project to an ATS job requisition. Hiring Assistant evaluates both LinkedIn-sourced candidates and ATS-sourced applicants in a single unified view, using profile data from both platforms.

**Goal:**
Eliminate the need for recruiters to toggle between LinkedIn Recruiter and ATS by creating a unified view of all applicants, allowing Hiring Assistant to evaluate ATS candidates in addition to LinkedIn-sourced candidates.

**Human Actors:**
- Recruiter: Connects project to ATS via RSC+; reviews unified applicant list; manages pipeline across both systems; advances or rejects candidates.
- Recruiter Admin: Activates RSC+ feature at the contract level; manages access control.

**Artificial Agents:**
- RSC+ Integration: Continuously pulls ATS data (profiles, resumes, application records, interview feedback) into LinkedIn.
- Hiring Assistant (supervisor): Evaluates candidates from both LinkedIn and ATS sources.
- Evaluation Agent: Applies evaluation summaries to ATS-sourced applicants using resume data.
- ATS Sync Module: Maintains data consistency between LinkedIn and ATS.

**Context:**
- Organisation uses both LinkedIn Recruiter with Hiring Assistant add-on and an integrated ATS (from LinkedIn's ATS partner list).
- RSC+ has been enabled by Recruiter Admin.
- Recruiters save up to 3.5 hours/week with RSC active. [E-033]

**Input Data:**
- ATS data: candidate name, email, current status, candidate notes/tags, application records, resumes, interview feedback, job requisition metadata.
- LinkedIn profile data for same candidates (where available).
- Hiring qualifications for the role.

**Knowledge Sources:**
- ATS system (via RSC+ API).
- LinkedIn member profiles.
- LinkedIn Skills Graph (for skills extraction from resumes).

**Processing Method:**
- RSC+ continuously pulls ATS data; data stored in LinkedIn US data centres.
- Hiring Assistant evaluates applicants using both LinkedIn profile data + ATS resume data.
- Results displayed in unified Connected Projects view.
- No stage movements automated unless customer explicitly enables.

**Processing Tasks (AI):**
1. Pull applicant data from ATS via RSC+ API.
2. Match ATS applicants with LinkedIn profiles (where possible).
3. Evaluate applicants using Hiring Assistant (LinkedIn + ATS data).
4. Surface unified ranked applicant list with qualification match/gap.
5. Optionally sync stage updates back to ATS (requires explicit customer enablement).

**Human Tasks:**
1. Recruiter Admin: Enable RSC+ and consent to data access.
2. Recruiter: Connect LinkedIn project to ATS requisition.
3. Recruiter: Review unified applicant list.
4. Recruiter: Advance, reject, or schedule interviews for candidates.
5. Recruiter: Manually update stages in ATS (or enable sync if available).

**Interaction Points:**
- RSC+ ↔ ATS: Continuous data pull.
- Hiring Assistant → Recruiter: Unified evaluation view.
- Recruiter → ATS (indirect): Stage updates (via Recruiter or directly in ATS).

**Outputs:**
- Unified view of all applicants (LinkedIn-sourced + ATS applicants).
- Evaluation summaries for ATS applicants.
- Time savings (3.5 hours/week with RSC; 7% higher InMail acceptance). [E-033]

**Evaluation Metrics:**
- Recruiter time saved with RSC active (3.5 hours/week). [E-033]
- InMail acceptance rate increase with RSC (7%). [E-033]
- Applicant coverage rate (% of all applicants evaluated by HA). [INFERRED]

**Required Capabilities:**
- Continuous ATS data ingestion (RSC+ API).
- Cross-platform applicant deduplication (LinkedIn + ATS).
- Resume parsing for ATS-sourced applicants.
- Unified evaluation with multi-source data.
- Privacy-compliant data storage and segmentation.

**Decision Points:**
- Recruiter Admin: Whether to enable RSC+.
- Recruiter: Whether to link project to ATS requisition.
- Recruiter: All applicant advancement/rejection decisions (human-only).
- Customer: Whether to enable automated stage syncing (opt-in).

**Feedback Mechanisms:**
- Recruiter actions in unified view → model retraining signals. [E-008]
- ATS stage data → signals for future candidate pipeline modelling [INFERRED].

**Expected Hybrid Intelligence Characteristics:**
- **Collaborative**: Combines AI evaluation with recruiter decision-making across two data sources.
- **Adaptive**: System learns from recruiter actions across unified candidate pool.
- **Responsible**: Customer controls data access; no automated decisions without explicit opt-in; data stored and segmented per LinkedIn policy. [E-020]
- **Explainable**: Evaluation summaries shown for ATS applicants same as LinkedIn-sourced candidates.

**Evidence IDs:** E-019, E-020, E-033, E-034, E-035

**Confidence:** High (RSC+ documented in both official transparency and help documentation)
