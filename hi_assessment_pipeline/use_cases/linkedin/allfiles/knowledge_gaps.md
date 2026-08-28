# Knowledge Gaps
## Neuro-Symbolic AI — Hybrid Intelligence Knowledge Acquisition
### Target: LinkedIn Recruiter + Hiring Assistant

> **Purpose:** This file documents ONLY information that could NOT be found during knowledge acquisition.
> Gaps are not filled here. They are described, with searches performed, sources consulted, and implications for Phase 2 modelling noted.
> Each gap is labelled with a Gap ID (E-GAP-xx) referenced in other package files where relevant.

---

## E-GAP-01 — AI Disclosure to Candidates

**Missing Information:**
Whether and how candidates are explicitly informed that they are interacting with an AI agent (Hiring Assistant / Outreach Agent) rather than a human recruiter when receiving InMail prescreening messages.

**Searches Performed:**
- "LinkedIn Recruiter responsible AI recruiter fairness 2024 site:linkedin.com"
- "LinkedIn Hiring Assistant candidate disclosure AI transparency"
- "LinkedIn Recruiter InMail AI generated message personalization candidate outreach 2024"
- Direct fetch: `https://business.linkedin.com/hire/ai-transparency/hire`
- Direct fetch: `https://business.linkedin.com/hire/ai-transparency`

**Sources Consulted:**
- LinkedIn AI Transparency page (E-019, E-020)
- LinkedIn Help: AI-Assisted Messages (E-030, E-031)
- LinkedIn Help: Prescreen candidates with Hiring Assistant (E-038)
- LinkedIn Privacy Policy

**Why Information Could Not Be Found:**
The LinkedIn AI Transparency documentation focuses on recruiter-facing transparency (what the recruiter can understand about AI decisions) and data privacy (what data is used). No explicit statement was found regarding whether candidates are disclosed that they are interacting with an AI rather than a human during prescreening InMails. The Help documentation describes the recruiter-side workflow but does not address candidate-side disclosure policy.

**Why This Matters for Modelling:**
Candidate disclosure is relevant to the **Responsible** and **Explainable** dimensions of the CARE framework from the perspective of the candidate as a stakeholder. If candidates are not informed they are interacting with AI, this may be an HI gap when modelling the Responsible characteristic.

**Whether Modelling Assumptions May Be Required:**
Yes. For Phase 2, when modelling the Responsible characteristic from the candidate perspective, an assumption may be required: either (a) disclosure is provided per LinkedIn terms of service / EU AI Act requirement (likely but not documented), or (b) disclosure is not currently explicit (a potential HI gap). This should be documented as an assumption in Phase 2 with confidence Medium.

---

## E-GAP-02 — Prescreening Completion Rate

**Missing Information:**
The percentage of candidates who complete the prescreening Q&A process (respond to all prescreening questions vs. drop off after initial InMail response).

**Searches Performed:**
- "LinkedIn Hiring Assistant InMail prescreening questions candidate engagement workflow"
- "LinkedIn Recruiter prescreening completion rate metric"
- Direct fetch: `https://business.linkedin.com/hire/hiring-assistant`
- Direct fetch: `https://www.linkedin.com/help/recruiter/answer/a7488409`

**Sources Consulted:**
- LinkedIn Hiring Assistant product page (E-005)
- LinkedIn Help: Prescreen candidates (E-038)
- LinkedIn Engineering Blog (E-008)
- LinkedIn Talent Blog (E-032)

**Why Information Could Not Be Found:**
LinkedIn's publicly documented metrics focus on InMail acceptance rates and recruiter time savings. No metric was found describing what proportion of candidates who accept an initial InMail actually complete the full prescreening Q&A. This is an operational metric that is not publicly disclosed.

**Whether Modelling Assumptions May Be Required:**
Modelling may proceed without this metric. It is a performance metric rather than a structural concept. If required for scenario modelling or SHACL constraint design, a placeholder value may be assumed from general industry benchmarks with Low confidence.

---

## E-GAP-03 — EON Model Architecture Details

**Missing Information:**
The internal architecture, training objective, training data composition, and hyperparameter details of the EON model (LinkedIn's fine-tuned in-house LLM for candidate evaluation).

**Searches Performed:**
- "LinkedIn Hiring Assistant EON model fine-tuned Economic Graph candidate evaluation GPT-4o"
- "LinkedIn EON model architecture training objective"
- "site:engineering.linkedin.com EON model"
- ZenML and InfoQ articles on LinkedIn multi-agent architecture

**Sources Consulted:**
- ZenML LLMOps database (E-013)
- InfoQ: LinkedIn multi-agent (E-014)
- MLSavvy Parts 1 and 2 (E-015, E-016)
- QCon London 2025 presentation summary (E-012)
- LinkedIn Engineering Blog (no specific EON article found)

**Why Information Could Not Be Found:**
The existence and general purpose of EON is documented in technical summaries and conference talks (fine-tuned on Economic Graph data; used for at-scale candidate evaluation). However, the specific architecture, training methodology, fine-tuning objective, and hyperparameter choices are proprietary and not publicly disclosed. No LinkedIn Engineering Blog post specifically about EON was found.

**Whether Modelling Assumptions May Be Required:**
For the purposes of Knowledge Graph construction and ontology mapping, EON is sufficiently characterised as an ArtificialAgent (MLModel) fine-tuned on Economic Graph data for candidate evaluation. Internal architecture details are not required for HI assessment. No modelling assumption needed.

---

## E-GAP-04 — HLTM Explainability to Recruiters

**Missing Information:**
Whether LinkedIn Hiring Assistant surfaces HLTM-derived inferences to recruiters as explicit explanations (i.e., whether the recruiter is told "I'm personalising your results based on your past preference for X role type") or whether HLTM personalisation is entirely implicit (the recruiter experiences better results but does not receive an explanation of why).

**Searches Performed:**
- "LinkedIn Hiring Assistant long term memory hierarchical semantic memory explainability recruiter"
- "HLTM LinkedIn explainability user-facing"
- arXiv HLTM paper (E-046) read in detail — explainability to end-user not discussed

**Sources Consulted:**
- arXiv: HLTM paper (E-046) — describes system architecture, metrics, privacy; does not address user-facing explainability of HLTM inferences
- LinkedIn AI Transparency page (E-019, E-020) — discusses qualification match/gap as explainability mechanism; does not mention HLTM transparency

**Why Information Could Not Be Found:**
The HLTM arXiv paper (E-046) focuses on system architecture, memory hierarchy, privacy constraints, and production metrics. It does not describe whether HLTM-derived preferences are disclosed to recruiters or surfaced as explanations. The LinkedIn AI Transparency documentation describes other explainability features (qualification match/gap, filter breakdown) but does not mention HLTM inference disclosure.

**Whether Modelling Assumptions May Be Required:**
Yes. For Phase 2 SHACL modelling of the **Explainable** characteristic, an assumption may be required: HLTM personalisation is currently implicit (not surfaced as user-facing explanation). This is a potential HI gap under the Explainable dimension of CARE. Modelling should mark this as an Inferred gap with Medium-High confidence.

---

## E-GAP-05 — Candidate-Side Privacy Controls for Prescreening Data

**Missing Information:**
Specific privacy controls available to candidates regarding prescreening data collected via Hiring Assistant (i.e., whether candidates can request deletion of prescreening responses, see what was stored, or opt out of AI prescreening specifically).

**Searches Performed:**
- "LinkedIn Recruiter AI responsible use policy transparency disclosure candidates data privacy"
- "LinkedIn Hiring Assistant candidate data rights prescreening GDPR"
- LinkedIn Privacy Policy review

**Sources Consulted:**
- LinkedIn AI Transparency page (E-019, E-020)
- LinkedIn Privacy Policy
- LinkedIn Help: Data and privacy for hiring integrations (referenced in search)

**Why Information Could Not Be Found:**
LinkedIn's privacy documentation focuses on member control of profile data and GenAI training data opt-out. Specific controls for prescreening data collected during Hiring Assistant interactions were not found. The AI Transparency page notes that GDPR applies and that LinkedIn complies with applicable law, but does not detail candidate-specific data rights for prescreening interactions.

**Whether Modelling Assumptions May Be Required:**
For Phase 2, GDPR compliance can be assumed (documented) which implies standard data subject rights (access, deletion, portability) apply. Specific implementation details are not required for structural HI modelling.

---

## E-GAP-06 — Internal Prompt Management and Skill Registry Details

**Missing Information:**
The internal structure of LinkedIn Hiring Assistant's centralised prompt management system and skill registry (used for dynamic tool discovery by agents), including how prompts are versioned, evaluated, and updated.

**Searches Performed:**
- "LinkedIn Hiring Assistant prompt management skill registry"
- "site:engineering.linkedin.com prompt management generative AI"
- ZenML and InfoQ architecture articles (E-013, E-014)

**Sources Consulted:**
- ZenML LLMOps database (E-013) — mentions prompt management and skill registry as components
- InfoQ (E-014) — mentions skill registry
- LinkedIn Engineering Blog — no specific article on prompt management found

**Why Information Could Not Be Found:**
The existence of a centralised prompt management system and skill registry is documented in technical summaries (E-013, E-014). Internal details (versioning strategy, evaluation cadence, prompt update governance) are not publicly disclosed.

**Whether Modelling Assumptions May Be Required:**
Not required for HI assessment. These are internal engineering concerns rather than HI ontology concepts. The skill registry's function (enabling sub-agents to discover tools dynamically) is captured in the ArtificialAgent and Capability mappings.

---

## E-GAP-07 — Downstream Hiring Outcome Diversity Metrics

**Missing Information:**
Whether LinkedIn tracks and reports on downstream diversity outcomes (e.g., whether the use of representative ranking leads to measurable improvements in the diversity of candidates actually contacted, interviewed, or hired — not just in shortlisted results).

**Searches Performed:**
- "LinkedIn Recruiter fairness diversity outcomes downstream hiring results"
- "LinkedIn representative ranking diversity hiring outcome metrics"
- Geyik et al. KDD 2019 paper (E-041) reviewed
- LinkedIn Engineering Blog (E-009, E-010) reviewed

**Sources Consulted:**
- Geyik et al. KDD 2019 (E-041) — notes uncertainty about whether improved representation in candidate recommendations leads to measurable improvements in contact/interview rates
- LinkedIn Engineering Blog: Fairness (E-009) — discusses measurement framework but not downstream outcome data
- LinkedIn AI Transparency page (E-019) — no downstream outcome data

**Why Information Could Not Be Found:**
The fairness research (E-041) explicitly notes uncertainty about whether improved representation in ranking translates to measurable diversity in hiring decisions. LinkedIn's public documentation does not provide longitudinal downstream outcome data (diversity of candidates contacted, interviewed, or hired before vs. after representative ranking deployment).

**Whether Modelling Assumptions May Be Required:**
Yes, partially. For SHACL validation of the Responsible characteristic (fairness), the system can be assessed on the representativeness of search results (documented and measured). Downstream outcome diversity (hiring rates) cannot be validated from available evidence and should be flagged as a limitation of the assessment scope.

---

## E-GAP-08 — Hiring Assistant Interaction Logs and Audit Trail Access

**Missing Information:**
Whether recruiters or organisations have access to Hiring Assistant interaction logs (what the system searched, what decisions it made, what InMails it sent) for audit or compliance purposes.

**Searches Performed:**
- "LinkedIn Hiring Assistant audit trail recruiter logs compliance"
- "LinkedIn Hiring Assistant data flow diagram interaction logs"
- Direct fetch: LinkedIn AI Transparency page (E-019, E-020)

**Sources Consulted:**
- LinkedIn AI Transparency page (E-019, E-020) — mentions governance but not recruiter-accessible audit logs
- LinkedIn Help documentation (various) — no mention of interaction log access

**Why Information Could Not Be Found:**
The AI Transparency documentation describes LinkedIn's internal governance mechanisms (quarterly access reviews, SOC 2, penetration testing) but does not describe whether customer organisations can access interaction logs for their own compliance audit purposes (e.g., to comply with NYC Local Law 144 bias audit requirements, or EU AI Act obligations for high-risk AI systems).

**Whether Modelling Assumptions May Be Required:**
For Phase 2 SHACL modelling of the Accountability characteristic, an assumption may be required: internal audit logs exist (implied by SOC 2 compliance) but customer-accessible audit logs are not confirmed. This may be an HI gap under the Accountable characteristic.

---

## Gap Summary

| Gap ID | Category | HI Dimension Affected | Modelling Assumption Required |
|---|---|---|---|
| E-GAP-01 | Candidate AI disclosure | Responsible, Explainable (candidate perspective) | Yes (Medium confidence assumption) |
| E-GAP-02 | Prescreening completion rate | EvaluationMetric | Not required (operational metric only) |
| E-GAP-03 | EON model architecture | ArtificialAgent (internal detail) | No (functional characterisation sufficient) |
| E-GAP-04 | HLTM explainability to recruiter | Explainable | Yes (HLTM inferences likely implicit) |
| E-GAP-05 | Candidate prescreening data rights | Responsible (candidate perspective) | Partial (GDPR compliance assumed) |
| E-GAP-06 | Prompt management / skill registry details | ArtificialAgent (internal detail) | No (not required for HI assessment) |
| E-GAP-07 | Downstream hiring diversity outcomes | Responsible (fairness outcomes) | Yes (fairness assessed at shortlist level only) |
| E-GAP-08 | Customer-accessible audit trail | Accountable | Yes (internal logs assumed; customer access unconfirmed) |

**Critical Gaps for Phase 2:** E-GAP-01, E-GAP-04, E-GAP-07, E-GAP-08 are the most significant for SHACL constraint design and HI assessment. They should be flagged as modelling assumptions in Phase 2 with appropriate confidence labels.
