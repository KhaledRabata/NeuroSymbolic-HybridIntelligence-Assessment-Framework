# Knowledge Gaps: Elsevier LeapSpace Knowledge Acquisition
## Version: 1.0 | Date: 2026-08-03

---

## Overview

This document records information that could **not** be found during systematic knowledge acquisition for Elsevier LeapSpace™ across seven research sessions (21+ queries). Gaps are documented for transparency and to flag where Phase 2 modelling assumptions may be required. No gap-filling has been performed here.

---

## E-GAP-01: Specific LLM Model Versions and Routing Logic

**Missing Information:**
Elsevier describes a "multi-model approach" drawing on providers including OpenAI and Anthropic, hosted on Azure and AWS. However, the following remain undisclosed:
- Specific model versions in use (e.g., GPT-4o, Claude 3.5 Sonnet, or equivalent)
- The algorithmic criteria by which the system routes a given query to a specific model
- Any performance benchmarks comparing models within the LeapSpace routing framework
- Whether model selection is static (per feature) or dynamic (per query)

**Searches Performed:**
- `"LeapSpace multi-model AI LLM RAG architecture"`
- `"Elsevier LeapSpace model selection criteria"`
- `"LeapSpace OpenAI Anthropic model version"`
- `"Elsevier AI technology stack LeapSpace"`

**Sources Consulted:**
- `elsevier.com/products/leapspace` (official product page)
- `elsevier.com/products/leapspace/trust-and-security`
- `elsevier.com/about/responsible-ai/ai-use-faq`
- `elsevier.support/leapspace/` (support centre)
- `prnewswire.com` – launch press release
- `rdworldonline.com` – feature coverage and demo observations

**Why the Information Could Not Be Found:**
Elsevier discloses provider names at a high level for transparency purposes but treats model selection logic and version identifiers as proprietary technical detail. No engineering blog, technical white paper, or third-party audit report containing this information was publicly accessible at the time of research.

**Modelling Assumption Required in Phase 2:**
**Yes.** If the Phase 2 ontology requires `hi:ArtificialAgent` instances to be typed or attributed at model-version level, assumptions will be needed. A reasonable assumption is that the routing is task-type-driven (e.g., deep synthesis tasks routed to higher-capability models), but this is unverified.

---

## E-GAP-02: Algorithmic Impact Assessment Results and Bias Metrics

**Missing Information:**
Elsevier's Responsible AI Principles state that periodic Algorithmic Impact Assessments (AIAs) are conducted and that a "quality and harmful bias evaluation framework" is in place. The following are not publicly available:
- Quantitative results from any completed AIA
- Specific bias dimensions assessed (e.g., disciplinary, linguistic, geographic, gender)
- Fairness metrics used and threshold values
- Frequency and process of AIA reviews
- Outcomes of any identified bias remediation

**Searches Performed:**
- `"LeapSpace bias evaluation results"`
- `"Elsevier Responsible AI Algorithmic Impact Assessment"`
- `"Elsevier AI bias audit findings LeapSpace"`
- `"Elsevier Responsible AI Principles documentation"`

**Sources Consulted:**
- `elsevier.com/about/policies-and-standards/responsible-ai-principles`
- `elsevier.com/about/responsible-ai/ai-use-faq`
- `elsevier.com/products/leapspace/trust-and-security`
- Science.org independent critical analysis

**Why the Information Could Not Be Found:**
AIA results are internal governance documents. Elsevier publishes the *existence* of the AIA process as evidence of responsible practice but does not release findings publicly. No leaked, peer-reviewed, or regulatorily mandated disclosure of AIA results was found.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For modelling the `hi:Evaluation` dimension and the Responsible CARE axis at a fine-grained level, assumptions about what the bias framework covers may be needed. The assumption that the framework covers at minimum geographic and disciplinary bias (given Elsevier's global publisher base) would be defensible but unverified.

---

## E-GAP-03: Discipline-Specific Content Coverage Statistics

**Missing Information:**
Aggregate coverage figures are documented (18M+ full-text articles and books; 100M+ abstracts; 7,000+ publishers). Missing:
- Breakdown of article coverage by major research discipline (e.g., % STEM vs. social sciences vs. humanities)
- Coverage ratios for specific fields relative to the total published literature in that field
- Publisher contribution percentages by content category
- Temporal coverage distributions (e.g., proportion of articles from the last five years vs. older)
- Coverage of non-English-language publications

**Searches Performed:**
- `"LeapSpace content coverage by discipline"`
- `"LeapSpace Scopus coverage statistics by field"`
- `"Elsevier ScienceDirect subject area coverage"`
- `"LeapSpace non-English content coverage"`

**Sources Consulted:**
- `elsevier.com/products/leapspace`
- `elsevier.libguides.com/LeapSpace`
- Science.org analysis (notes ~22% of 2024 articles covered overall)
- `knowledgespeak.com` – industry coverage

**Why the Information Could Not Be Found:**
Discipline-specific breakdowns are not published in product documentation or press releases. The Science.org article provided an overall 2024 coverage estimate (~22%) but not by field. Scopus publishes general subject area distributions for its abstract database separately, but the intersection with LeapSpace full-text coverage is not documented.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For context modelling of domain-specific research scenarios, an assumption that STEM and health sciences are more comprehensively covered than humanities and social sciences would align with Elsevier's known publisher portfolio, but remains unconfirmed for the LeapSpace-specific content layer.

---

## E-GAP-04: Quantitative System Performance Metrics

**Missing Information:**
- Average query response times for standard mode
- Average generation times for Deep Research reports
- Performance variation by query complexity or corpus size
- System uptime and reliability statistics
- Latency introduced by multi-agent coordination vs. single-agent responses

**Searches Performed:**
- `"LeapSpace response time performance"`
- `"LeapSpace Deep Research duration processing time"`
- `"Elsevier LeapSpace system performance benchmarks"`

**Sources Consulted:**
- `elsevier.support/leapspace/`
- `elsevier.libguides.com/LeapSpace`
- Product documentation and feature pages

**Why the Information Could Not Be Found:**
Documentation acknowledges only that Deep Research mode "takes longer to run — sometimes several minutes" without quantitative specification. No SLA documentation, performance white paper, or third-party benchmark study was publicly available.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For modelling task execution efficiency or temporal aspects of the human-AI interaction loop, approximate time ranges may need to be assumed. The documented phrase "sometimes several minutes" can serve as a qualitative bound.

---

## E-GAP-05: Independent Advisory Board Composition and Operational Procedures

**Missing Information:**
- Full membership list of the Independent Advisory Board for LeapSpace
- Board meeting cadence and decision-making procedures
- Scope of the board's mandate (e.g., whether it covers all Elsevier AI or LeapSpace specifically)
- Reporting structure and how board recommendations translate to system changes
- Distinction between the LeapSpace Advisory Board and the existing Scopus Content Selection and Advisory Board (CSAB)

**Searches Performed:**
- `"LeapSpace Advisory Board governance transparency"`
- `"Elsevier Independent Advisory Board AI members"`
- `"Elsevier AI governance board composition"`

**Sources Consulted:**
- `elsevier.com/products/leapspace/trust-and-security`
- `elsevier.com/about/policies-and-standards/responsible-ai-principles`
- Press releases and governance documentation

**Why the Information Could Not Be Found:**
At time of research, documentation stated that Elsevier is "currently recruiting an independent Advisory Board," indicating it may not yet have been formally constituted or publicly announced. The CSAB exists separately for Scopus content but its relationship to the LeapSpace AI Advisory Board is undefined in public sources.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For governance modelling under the Responsible CARE axis, the existence of an oversight body can be asserted; its composition and authority must be treated as undetermined. An assumption that the board functions in an advisory rather than veto capacity may be needed.

---

## E-GAP-06: Quantitative Accuracy and Hallucination Rate Data

**Missing Information:**
- Measured hallucination rates for LeapSpace outputs compared to baseline LLMs
- Citation accuracy rates (percentage of citations correctly matched to claims)
- False positive and false negative rates for Claim Radar classifications
- Methodology used to evaluate hallucination within Elsevier's internal testing
- Any third-party or independent accuracy audit results

**Searches Performed:**
- `"LeapSpace hallucination rate accuracy"`
- `"Elsevier LeapSpace citation accuracy"`
- `"LeapSpace Claim Radar false positive rate"`
- `"LeapSpace accuracy evaluation independent"`

**Sources Consulted:**
- `elsevier.com/products/leapspace/trust-and-security`
- `elsevier.com/products/leapspace/introducing-research-grade-ai`
- Science.org independent analysis
- `rdworldonline.com` – demo observations

**Why the Information Could Not Be Found:**
Elsevier states the system is "designed to minimize hallucinations" and is "grounded in peer-reviewed content," but provides no quantitative accuracy data. Science.org independently notes that "there is no standardized way to evaluate the accuracy of AI-generated summaries," which explains the broader absence of comparable benchmarks across the sector. No third-party audit report was located.

**Modelling Assumption Required in Phase 2:**
**Yes.** For modelling evaluation metrics under `hi:Evaluation` and assigning confidence to AI output quality, an assumption will be required. A reasonable assumption is that RAG-based grounding reduces (but does not eliminate) hallucination relative to ungrounded LLM outputs, but a specific rate cannot be stated.

---

## E-GAP-07: Detailed User Interaction Telemetry and Behavioural Patterns

**Missing Information:**
- Feature usage frequency distribution (e.g., which features are used most often)
- Average session duration per use case type
- Query refinement rates (how often users follow up or reformulate queries)
- Suggestion acceptance rates in Writing Coach (how often users approve AI suggestions)
- Drop-off points in multi-step workflows (e.g., Deep Research mode)

**Searches Performed:**
- `"LeapSpace user analytics usage telemetry"`
- `"LeapSpace Writing Coach suggestion acceptance rate"`
- `"LeapSpace feature usage statistics"`
- `"LeapSpace user behaviour research"`

**Sources Consulted:**
- Press releases (provide only aggregate statistics: 97% report time savings; >50% save >50% of time)
- `elsevier.com/resources/university-of-virginia-expands-research-resources-with-leapspace`
- `rdworldonline.com` – demo observations

**Why the Information Could Not Be Found:**
Published user statistics are high-level marketing metrics derived from the development research programme (3,200+ researchers). Granular telemetry data, feature-level analytics, and behavioural patterns are internal operational data not disclosed publicly.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For modelling interaction feedback loops and adaptive behaviour, interaction frequency distributions may need to be approximated. The information that "every change requires user approval" (Writing Coach) can anchor one decision-point assumption.

---

## E-GAP-08: Public-Facing API and Technical Integration Specifications

**Missing Information:**
- Existence and scope of any public or institutional API for LeapSpace
- Technical integration protocols for embedding LeapSpace into institutional systems (e.g., library management systems, CRIS systems)
- Authentication and authorisation mechanisms for institutional deployments
- Data exchange formats and standards used
- Webhook or event-driven integration capabilities

**Searches Performed:**
- `"LeapSpace API documentation"`
- `"LeapSpace institutional integration technical specifications"`
- `"Elsevier LeapSpace CRIS LMS integration"`
- `"LeapSpace embed institutional system"`

**Sources Consulted:**
- `elsevier.com/products/leapspace`
- `elsevier.libguides.com/LeapSpace`
- `elsevier.support/leapspace/`
- Product documentation and institutional pages

**Why the Information Could Not Be Found:**
Documentation references "institutional capabilities" and "integrations" but technical API specifications are not publicly documented. These are likely available only to institutional customers under contractual agreement. No developer portal or public API reference for LeapSpace was found.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For modelling the system boundary of `hi:ArtificialAgent` in institutional deployment contexts, the assumption that integration occurs at the authentication layer (e.g., institutional SSO) rather than through deep API embedding may be required.

---

## E-GAP-09: Longitudinal Outcome Data on Research Quality

**Missing Information:**
- Long-term impact of LeapSpace use on research output quality (e.g., publication rates, citation counts, grant success rates)
- Comparison of research outcomes between LeapSpace users and non-users
- Evidence of improved research design beyond self-reported satisfaction
- Peer-reviewed studies independently evaluating LeapSpace's impact on scientific rigour

**Searches Performed:**
- `"LeapSpace research outcomes longitudinal study"`
- `"LeapSpace impact research quality publication"`
- `"Elsevier LeapSpace independent evaluation"`
- `"LeapSpace grant success rate improvement"`

**Sources Consulted:**
- Press releases and user statistics documents
- Science.org analysis
- `elsevier.com/resources/university-of-virginia-expands-research-resources-with-leapspace`
- General academic literature on AI in research workflows

**Why the Information Could Not Be Found:**
LeapSpace launched on January 21, 2026. Insufficient time has elapsed for longitudinal outcome studies to have been completed, published, and indexed. Existing evaluation data is limited to self-reported productivity metrics collected during the pre-launch development programme. No independent peer-reviewed evaluation of LeapSpace's impact on research quality was found.

**Modelling Assumption Required in Phase 2:**
**Yes.** For modelling `hi:Evaluation` with outcome-level metrics, the evaluation dimension will need to be limited to process metrics (time savings, user satisfaction) rather than outcome metrics (research quality, publication impact). This is a substantive limitation that should be flagged in Phase 2 knowledge graph construction.

---

## E-GAP-10: Reading Assistant Access Requirements and Full Coverage Scope

**Missing Information:**
- Exact access rules determining which articles are available for Reading Assistant interrogation
- Whether Reading Assistant functions on abstracts only when full-text access is unavailable
- The full list of content partners whose articles are accessible through Reading Assistant
- Behaviour of Reading Assistant when a user's institutional subscription does not cover a specific article
- Coverage of grey literature, preprints, or conference proceedings within Reading Assistant

**Searches Performed:**
- `"LeapSpace Reading Assistant access requirements"`
- `"LeapSpace full text access Reading Assistant limitations"`
- `"LeapSpace article interrogation subscription required"`
- `"LeapSpace preprint grey literature coverage"`

**Sources Consulted:**
- `elsevier.com/support/leapspace/`
- `elsevier.libguides.com/LeapSpace`
- Science.org analysis (notes separate subscription requirements)
- UVA AI newsletter practitioner notes

**Why the Information Could Not Be Found:**
Documentation confirms that full Reading Assistant functionality requires appropriate access rights to the underlying article, and that separate subscriptions may be needed. However, the precise fallback behaviour, coverage matrix by content partner, and treatment of open access vs. paywalled content within the Reading Assistant workflow are not documented in publicly available sources.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For modelling the `hi:Context` constraints governing the Reading Assistant scenario, an assumption that the feature degrades gracefully (e.g., abstract-only mode when full-text is unavailable) may be needed, but cannot be confirmed from available evidence.

---

## E-GAP-11: Equity and Access Pricing Details for Under-Resourced Institutions

**Missing Information:**
- Whether Elsevier offers discounted, tiered, or subsidised access for institutions in low- and middle-income countries (LMICs)
- Specific pricing structures for different institution sizes and types
- Whether any open or free access tier exists beyond the 7-day trial
- Elsevier's formal policy position on the documented equity access concern raised by researchers and critics
- Comparison of access costs relative to institutional budgets in different global regions

**Searches Performed:**
- `"LeapSpace pricing low-income institutions access equity"`
- `"Elsevier LeapSpace LMIC developing country access"`
- `"LeapSpace free access open tier"`
- `"LeapSpace institutional pricing structure"`
- `"LeapSpace criticism equity access under-resourced"`

**Sources Consulted:**
- `elsevier.com/products/leapspace` (individual: $32/month or $320/year; institutional: size-based)
- Science.org analysis (raises equity concerns explicitly)
- Research Information article
- General sources on Elsevier pricing debates

**Why the Information Could Not Be Found:**
Institutional pricing is negotiated confidentially and not published. Elsevier does not publicly address the equity access concern in available LeapSpace documentation. Science.org raises the concern as a critical limitation, but Elsevier's formal policy response was not found in public sources at time of research.

**Modelling Assumption Required in Phase 2:**
**Possibly.** For modelling the `hi:Context` fairness constraints and the access equity dimension of the Responsible CARE axis, the assumption that access is currently primarily available to well-resourced institutions may be required. This is partially supported by the Science.org critique but is not formally confirmed by Elsevier.

---

## Summary Table

| Gap ID | Category | HI Dimension Affected | Modelling Assumption Required |
|--------|----------|-----------------------|-------------------------------|
| E-GAP-01 | Technical Architecture | `hi:ArtificialAgent` (component typing); Adaptive (CARE) | Yes |
| E-GAP-02 | AI Governance / Bias | `hi:Evaluation`; Responsible (CARE) | Possibly |
| E-GAP-03 | Content Coverage | `hi:Context` (domain constraints); UseCase scope | Possibly |
| E-GAP-04 | System Performance | `hi:Interaction` (temporal dynamics); Task execution | Possibly |
| E-GAP-05 | Governance Structure | `hi:Context` (oversight constraints); Responsible (CARE) | Possibly |
| E-GAP-06 | Output Quality / Accuracy | `hi:Evaluation` (accuracy metrics); Explainable (CARE) | Yes |
| E-GAP-07 | User Behaviour Telemetry | `hi:Interaction` (feedback loops); `hi:Evaluation` | Possibly |
| E-GAP-08 | Technical Integration | `hi:ArtificialAgent` (system boundary); `hi:Context` | Possibly |
| E-GAP-09 | Longitudinal Outcomes | `hi:Evaluation` (outcome metrics); all CARE dimensions | Yes |
| E-GAP-10 | Feature Access Conditions | `hi:Context` (access constraints); `hi:UseCase` scope | Possibly |
| E-GAP-11 | Equity and Access | `hi:Context` (fairness constraints); Responsible (CARE) | Possibly |