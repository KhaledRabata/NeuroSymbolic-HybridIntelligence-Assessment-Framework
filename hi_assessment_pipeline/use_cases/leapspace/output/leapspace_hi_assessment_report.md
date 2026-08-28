# HI Assessment Report: LEAPSPACE

**Assessment Date:** 2026-08-25  
**HI Ontology Version:** 2.0.0 (VU Amsterdam)  
**Pipeline:** Neuro-Symbolic HI Assessment Pipeline  
**LLM Model:** gpt-4o-mini  

---

## 1. Executive Summary

The assessment of the AI system 'leapspace' reveals a concerning overall HI conformance score of 0.0%, placing it at HI Maturity Level 0: Pre-HI. Out of the eight scenarios evaluated, all exhibited significant gaps, leading to a total of 25 identified deficiencies. 

The primary strength of 'leapspace' lies within the Explainable dimension, scoring 75%. This indicates a potential for clarity in its operations; however, this strength is overshadowed by critical gaps in the Responsible dimension, which received a score of 0%. The absence of fairness mechanisms raises significant ethical concerns, undermining the system's credibility and trustworthiness. Additionally, the Collaborative and Adaptive dimensions are notably weak, with scores of 25% and 12%, respectively, reflecting a lack of human-AI interaction and feedback mechanisms essential for effective collaboration and adaptability.

Overall, 'leapspace' is assessed as a non-compliant HI system, with pervasive gaps that hinder its alignment with the CARE principles. The absence of responsible practices and collaborative features presents a substantial barrier to its deployment in real-world applications. 

Looking forward, there is considerable improvement potential for 'leapspace'. By addressing the identified gaps, particularly in fairness, collaboration, and adaptability, the system could evolve towards a more compliant and effective HI system, ultimately enhancing its usability and societal acceptance.

---

## 2. HI Conformance Overview

### 2.1 Overall Score

| Metric | Value |
|--------|-------|
| Overall HI Conformance | [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% |
| HI Maturity Level | **Level 0: Pre-HI** |
| Scenarios Assessed | 8 |
| Scenarios PASS | 0 (0%) |
| Scenarios WARNING | 0 |
| Scenarios FAIL | 8 (100%) |
| Total HI Gaps | 25 |

> The system does not meaningfully embody Hybrid Intelligence principles. Fundamental changes to the human-AI collaboration model are required.

### 2.2 CARE Dimension Analysis

| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| **Collaborative** | ❌ 25% | Human and AI agents co-participate in interactions |
| **Adaptive** | ❌ 12% | Feedback loops and learning mechanisms |
| **Responsible** | ❌ 0% | Oversight, fairness, and accountability |
| **Explainable** | ⚠️ 75% | AI transparency and decision explanation |

### 2.3 Scenario Overview

| Scenario | Label | Status | Gaps |
|----------|-------|--------|------|
| S1 | S1 — Departmental Literature Review Synthesis | ❌ FAIL | 4 |
| S2 | S2 — Cross-Domain Onboarding for Unfamiliar Research Areas | ❌ FAIL | 3 |
| S3 | S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature | ❌ FAIL | 4 |
| S4 | S4 — Evidence-Strength Calibration and Hallucination Mitigation | ❌ FAIL | 1 |
| S5 | S5 — Cross-Disciplinary Connection-Finding and Author/Collaborator Search | ❌ FAIL | 3 |
| S6 | S6 — Research-to-Funding Opportunity Matching | ❌ FAIL | 3 |
| S7 | S7 — AI-Assisted Argument Testing and Draft Strengthening | ❌ FAIL | 3 |
| S8 | S8 — Governed Evidence Verification for Corporate and Regulated R&D | ❌ FAIL | 4 |

---

## 3. Detailed Scenario Analysis

### S1 — S1 — Departmental Literature Review Synthesis

**Status:** ❌ FAIL  
**HI Gaps:** 4  

> The leapspace AI system fails to meet critical HI principles, particularly in the areas of responsibility, collaboration, and adaptability. Key capabilities for fairness, explainability, and human feedback mechanisms are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system lacks AI participation in interactions, which means it cannot facilitate joint task execution or shared decision-making. |
| Adaptive | 1 — Reactive | The absence of a human feedback mechanism limits the system's ability to evolve and adapt to user needs. |
| Responsible | 1 — Reactive | The lack of fairness mechanisms in the system risks producing discriminatory outcomes, undermining trust and ethical standards. |
| Explainable | 1 — Reactive | There is no evidence of explainability capabilities, meaning the system cannot clarify its decisions or recommendations. |

#### Gap G-S1-01: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system lacks any capability related to fairness or bias mitigation, which is essential for responsible AI. Without these mechanisms, the system risks producing discriminatory outcomes, undermining trust and ethical standards in human-AI collaboration.

**Practical Impact**
> This absence can lead to biased recommendations, negatively affecting decision-making processes and potentially harming users or stakeholders.

**Recommendation: Implement Fairness Auditing Tools**

Integrate fairness auditing tools into the AI system to identify and mitigate biases in recommendations. This will ensure that the system produces equitable outcomes and maintains ethical standards in human-AI collaboration.

*Implementation:* Utilize existing libraries like AI Fairness 360 or Fairlearn to assess and adjust the model's outputs for fairness, and incorporate these checks into the model training pipeline.

*Priority:* High | *Expected HI Impact:* Enhances Responsible AI by ensuring fairness and reducing bias.

#### Gap G-S1-02: Absence of Explainability

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The AI system does not possess any explainability capabilities, meaning it cannot clarify its decisions or recommendations to human agents. This lack of transparency is detrimental to effective collaboration, as humans cannot understand or trust the AI's outputs.

**Practical Impact**
> Without explainability, users may be hesitant to rely on AI-generated insights, leading to reduced engagement and collaboration between human and AI agents.

**Recommendation: Add Explainability Features**

Incorporate explainability features such as LIME or SHAP to provide insights into the AI's decision-making process. This will help users understand the rationale behind recommendations, fostering trust and collaboration.

*Implementation:* Integrate LIME or SHAP into the model's output layer to generate explanations for each recommendation, and create a user interface element to display these explanations clearly.

*Priority:* High | *Expected HI Impact:* Improves Explainability, enhancing user trust and engagement.

#### Gap G-S1-03: Missing Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The system does not incorporate human feedback into its evaluation processes, which is crucial for adaptive learning. Without human signals to inform updates, the AI cannot improve its performance or align with user preferences over time.

**Practical Impact**
> This gap limits the system's ability to evolve and meet user needs, resulting in a static AI that may become less relevant or effective in dynamic environments.

**Recommendation: Integrate Human Feedback Loops**

Develop a mechanism for collecting human feedback on AI outputs to inform model updates and improvements. This will allow the AI to adapt based on user preferences and performance metrics.

*Implementation:* Implement a feedback interface where users can rate recommendations and provide comments, and use this data to retrain the model periodically based on user input.

*Priority:* High | *Expected HI Impact:* Enhances Adaptability by allowing the AI to learn from user interactions.

#### Gap G-S1-04: No AI Participation in Interactions

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded interactions lack the involvement of an artificial agent, which is essential for true human-AI collaboration. This absence means that the system cannot facilitate joint task execution or shared decision-making.

**Practical Impact**
> Without AI participation, the potential for synergistic collaboration is lost, leading to a fragmented approach where human agents work in isolation from AI capabilities.

**Recommendation: Enable AI Participation in Interactions**

Design the system to allow AI agents to actively participate in user interactions, facilitating joint task execution and decision-making. This will enhance the collaborative potential of the system.

*Implementation:* Develop an interactive interface where AI can suggest actions or decisions during user sessions, and ensure that the AI can respond to user inputs in real-time.

*Priority:* High | *Expected HI Impact:* Boosts Collaborative capabilities by integrating AI into user workflows.

### S2 — S2 — Cross-Domain Onboarding for Unfamiliar Research Areas

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The leapspace AI system fails to meet critical HI conformance requirements, particularly in the areas of responsibility, collaboration, and adaptability. Key mechanisms for fairness, explainability, and human feedback are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The AI system does not provide explanations for its decisions, which hinders effective collaboration and limits its capability to initiate or maintain interactions. |
| Adaptive | 1 — Reactive | The system lacks a feedback mechanism that incorporates human actions, preventing it from adapting or improving based on user interactions. |
| Responsible | 1 — Reactive | The absence of fairness mechanisms in the system indicates a lack of responsible AI practices, resulting in potential biased outcomes. |
| Explainable | 1 — Reactive | There is no evidence of tailored explanations for users, which limits the system's ability to provide context-specific insights. |

#### Gap G-S2-01: Absence of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system lacks any capability for fairness or bias mitigation, which is essential for responsible AI. Without these mechanisms, the system risks producing discriminatory outcomes, undermining trust and ethical standards in human-AI collaboration.

**Practical Impact**
> This absence can lead to biased decisions that affect users negatively, diminishing the quality and reliability of the collaborative experience.

**Recommendation: Implement Fairness Auditing Tools**

Integrate fairness auditing tools that assess and mitigate bias in the AI's decision-making process. This will ensure that the system produces equitable outcomes, thereby enhancing trust and ethical standards in human-AI collaboration.

*Implementation:* Select and integrate an existing fairness library (e.g., AI Fairness 360) into the system's pipeline to evaluate model outputs for bias and implement corrective measures based on the findings.

*Priority:* High | *Expected HI Impact:* Enhances responsible AI by ensuring equitable decision-making.

#### Gap G-S2-02: Lack of Explainability

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The AI system does not provide explanations for its decisions, which is crucial for effective collaboration. Without explainability, human agents cannot understand or trust the AI's outputs, leading to potential misalignment in collaborative tasks.

**Practical Impact**
> This gap can severely hinder the ability of human users to engage with the AI, resulting in reduced effectiveness and potential errors in decision-making.

**Recommendation: Develop Explainability Features**

Create a module that generates clear, user-friendly explanations for the AI's decisions. This will help human agents understand the rationale behind outputs, fostering trust and effective collaboration.

*Implementation:* Utilize explainability frameworks like LIME or SHAP to generate explanations for model predictions and integrate these explanations into the user interface for easy access.

*Priority:* High | *Expected HI Impact:* Improves explainability, enhancing user trust and collaboration.

#### Gap G-S2-03: No Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The system lacks a feedback mechanism that incorporates human actions, which is vital for adaptive learning. Without human signals to inform model updates, the AI cannot improve its performance or align with user preferences over time.

**Practical Impact**
> This deficiency prevents the system from evolving based on user interactions, leading to stagnation and a failure to meet the changing needs of users in unfamiliar research areas.

**Recommendation: Introduce Human Feedback Loop**

Establish a feedback mechanism that allows users to provide input on AI decisions, which will be used to refine and adapt the model over time. This ensures the AI evolves based on real user interactions and preferences.

*Implementation:* Design a user interface component that prompts users for feedback after key decisions, and implement a backend system to collect, analyze, and incorporate this feedback into model retraining processes.

*Priority:* High | *Expected HI Impact:* Enhances adaptability by aligning AI performance with user needs.

### S3 — S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature

**Status:** ❌ FAIL  
**HI Gaps:** 4  

> The leapspace AI system fails to meet essential HI principles, particularly in responsibility and collaboration. Key capabilities for fairness, explainability, and human-AI interaction are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system lacks any AI participation in interactions, which severely limits its collaborative potential as noted in the gap description. |
| Adaptive | 1 — Reactive | The absence of a human feedback mechanism prevents the system from learning and adapting, as highlighted in the gap evidence. |
| Responsible | 1 — Reactive | The system's lack of fairness mechanisms poses a critical risk of biased recommendations, as described in the gap evidence. |
| Explainable | 1 — Reactive | The absence of explainability capabilities undermines users' ability to understand AI outputs, as stated in the gap description. |

#### Gap G-S3-01: Absence of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system lacks any capability related to fairness or bias mitigation, which is crucial for ensuring equitable outcomes in AI decision-making. Without these mechanisms, the system risks perpetuating discriminatory practices, undermining trust and accountability in human-AI collaboration.

**Practical Impact**
> This absence can lead to biased recommendations that adversely affect users, diminishing the overall effectiveness and ethical standing of the AI system.

**Recommendation: Implement Fairness Assessment Tools**

Integrate fairness assessment tools that evaluate model outputs for bias across different demographic groups. This will help ensure equitable outcomes and mitigate discriminatory practices, addressing the critical gap in fairness mechanisms.

*Implementation:* Utilize existing libraries like AI Fairness 360 or Fairlearn to assess and adjust model predictions based on fairness metrics. Incorporate these tools into the model evaluation pipeline.

*Priority:* High | *Expected HI Impact:* Enhances Responsible AI by ensuring equitable treatment of all users.

#### Gap G-S3-02: Lack of Human-AI Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded interactions do not involve any artificial agent, which is a fundamental requirement for collaborative human-AI systems. This absence means that the system cannot facilitate meaningful joint task execution or decision-making, severely limiting its collaborative potential.

**Practical Impact**
> Without AI participation in interactions, users cannot leverage AI capabilities effectively, leading to a disjointed experience that fails to harness the strengths of both human and AI agents.

**Recommendation: Integrate AI Agent for Interaction**

Develop and deploy an AI agent that actively participates in user interactions, facilitating collaborative decision-making. This will enhance the system's collaborative potential by leveraging AI capabilities effectively.

*Implementation:* Create a chatbot or virtual assistant that can engage users in real-time, providing suggestions and insights based on user inputs. Ensure the AI agent can learn from interactions to improve its responses.

*Priority:* High | *Expected HI Impact:* Improves Collaborative AI by enabling meaningful human-AI interactions.

#### Gap G-S3-03: No Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The feedback mechanism does not incorporate human actions, which is essential for the system to learn and adapt over time. Without human input, the AI cannot refine its models or improve its performance based on user preferences and experiences.

**Practical Impact**
> This lack of adaptive learning hinders the system's ability to evolve and meet user needs, resulting in a static solution that may become less relevant over time.

**Recommendation: Establish Human Feedback Channels**

Implement a mechanism for users to provide feedback on AI recommendations, allowing the system to learn and adapt over time. This will address the lack of human feedback and enhance the system's relevance.

*Implementation:* Create a user interface element where users can rate recommendations or provide comments, and use this data to refine AI models through supervised learning techniques.

*Priority:* High | *Expected HI Impact:* Enhances Adaptive capabilities by allowing the system to evolve based on user input.

#### Gap G-S3-04: Absence of Explainability Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Explainable** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The system lacks any explainability capabilities, preventing it from clarifying its decisions or recommendations to human agents. This gap undermines users' ability to understand and trust AI outputs, which is vital for effective collaboration.

**Practical Impact**
> Without explainability, users may be hesitant to act on AI recommendations, leading to reduced engagement and reliance on the system, ultimately compromising the collaborative process.

**Recommendation: Add Explainability Features**

Incorporate explainability mechanisms that provide users with insights into how AI decisions are made. This will enhance user trust and understanding of AI outputs, addressing the explainability gap.

*Implementation:* Utilize frameworks like LIME or SHAP to generate explanations for model predictions and integrate these explanations into the user interface, ensuring they are accessible and understandable.

*Priority:* High | *Expected HI Impact:* Improves Explainable AI by fostering user trust and engagement with the system.

### S4 — S4 — Evidence-Strength Calibration and Hallucination Mitigation

**Status:** ❌ FAIL  
**HI Gaps:** 1  

> The leapspace AI system fails to meet critical HI conformance standards, particularly in responsible AI practices. The absence of fairness mechanisms significantly undermines the system's integrity and trustworthiness.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | There is no evidence of the AI agent initiating collaboration or maintaining a collaborative relationship, indicating a reactive approach. |
| Adaptive | 1 — Reactive | There is no evidence of the system adapting based on feedback or anticipating human needs, suggesting a reactive behavior. |
| Responsible | 1 — Reactive | The system lacks fairness mechanisms, which is critical for responsible AI, thus limiting its capability to a reactive level. |
| Explainable | 1 — Reactive | There is no evidence of tailored explanations or interactive dialogue, indicating a fixed and generic approach. |

#### Gap G-S4-01: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | Responsible |

**Gap Description**
> The system lacks any capability related to fairness or bias mitigation, which is essential for responsible AI. This absence can lead to discriminatory outcomes, undermining trust and accountability in human-AI interactions.

**Practical Impact**
> Without fairness-aware processing, the system risks perpetuating biases, which can alienate users and diminish the effectiveness of collaboration between humans and AI.

**Recommendation: Implement Fairness-Aware Algorithms**

Integrate fairness-aware algorithms into the decision-making processes of the AI system to actively identify and mitigate biases. This change will ensure that the system operates responsibly, promoting equitable outcomes for all users.

*Implementation:* Utilize existing libraries such as Fairlearn or AIF360 to assess and adjust model predictions for fairness metrics during training and evaluation phases. Conduct regular audits to ensure ongoing compliance with fairness standards.

*Priority:* High | *Expected HI Impact:* Enhances the Responsible dimension by ensuring equitable treatment of users, thereby fostering trust.

### S5 — S5 — Cross-Disciplinary Connection-Finding and Author/Collaborator Search

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The leapspace AI system fails to meet essential HI principles, particularly in fairness, explainability, and adaptive feedback mechanisms. These deficiencies critically undermine the collaborative potential of the system.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system's lack of explainability features prevents effective collaboration, limiting it to a reactive level. |
| Adaptive | 1 — Reactive | The absence of human feedback mechanisms restricts the system's ability to adapt, confining it to a reactive state. |
| Responsible | 1 — Reactive | The lack of fairness mechanisms compromises equitable outcomes, resulting in a reactive capability. |
| Explainable | 1 — Reactive | There is no evidence of tailored explanations, indicating a fixed and generic approach to explainability. |

#### Gap G-S5-01: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system lacks any capability for fairness or bias mitigation, which is crucial for ensuring equitable outcomes in AI-assisted decision-making. Without these mechanisms, the system risks perpetuating discrimination and undermining trust in human-AI collaboration.

**Practical Impact**
> The absence of fairness mechanisms can lead to biased recommendations, diminishing the quality of collaboration and potentially harming users' interests.

**Recommendation: Implement Fairness Auditing Tools**

Integrate fairness auditing tools that assess and mitigate bias in the AI's decision-making process. This will ensure equitable outcomes and build trust among users by addressing potential discrimination.

*Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to analyze model outputs for bias and implement corrective measures based on the audit results.

*Priority:* High | *Expected HI Impact:* Enhances Responsible AI by ensuring fairness in decision-making.

#### Gap G-S5-02: Missing Explainability Features

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The system does not include any explainability capabilities, preventing human agents from understanding the AI's decisions and recommendations. This lack of transparency is detrimental to effective collaboration, as humans cannot trust or verify AI outputs.

**Practical Impact**
> Without explainability, users may struggle to engage meaningfully with the AI, leading to reduced collaboration effectiveness and potential rejection of AI suggestions.

**Recommendation: Add Explainability Features to AI Outputs**

Develop and integrate explainability features that provide insights into the AI's decision-making process, such as feature importance scores or decision rationale. This will enhance user trust and facilitate better collaboration.

*Implementation:* Incorporate tools like LIME or SHAP to generate explanations for AI recommendations, ensuring they are easily accessible within the user interface.

*Priority:* High | *Expected HI Impact:* Improves Explainability, fostering trust and collaboration between users and AI.

#### Gap G-S5-03: Absence of Human Feedback Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The system lacks a feedback mechanism that incorporates human actions, which is essential for adaptive learning and improvement. This absence means the AI cannot refine its performance based on user interactions, limiting its effectiveness over time.

**Practical Impact**
> Without human-driven feedback loops, the AI's ability to evolve and better serve user needs is severely compromised, leading to stagnation in performance and user dissatisfaction.

**Recommendation: Establish Human Feedback Loop Mechanism**

Create a feedback loop that allows users to provide input on AI recommendations, which the system can use to adapt and improve its performance over time. This will enhance the AI's relevance and effectiveness.

*Implementation:* Implement a user interface feature that prompts users for feedback after each AI recommendation, and store this feedback to retrain the model periodically.

*Priority:* High | *Expected HI Impact:* Strengthens Adaptive capabilities by enabling continuous learning from user interactions.

### S6 — S6 — Research-to-Funding Opportunity Matching

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The leapspace AI system fails to meet critical HI conformance standards, particularly in the Responsible and Collaborative dimensions, lacking essential fairness, explainability, and adaptive feedback mechanisms.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system's inability to explain its decisions, as highlighted by the critical gap in Explainability, limits its collaborative capabilities to a reactive level. |
| Adaptive | 1 — Reactive | The absence of human feedback mechanisms, as noted in the critical gap, restricts the system's adaptability to a reactive level. |
| Responsible | 1 — Reactive | The lack of fairness mechanisms, identified as a critical gap, confines the system's responsible capabilities to a reactive level. |
| Explainable | 3 — Social | Although there are no gaps in the Explainable dimension, the maximum admissible level is 3, indicating the potential for social-level explanations. |

#### Gap G-S6-01: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system does not incorporate any fairness-aware processing or bias mitigation capabilities, which is essential for ensuring equitable outcomes. This absence undermines the Responsible principle, as it may lead to discriminatory practices in funding opportunity matching.

**Practical Impact**
> Without fairness mechanisms, the AI may perpetuate biases, leading to unfair treatment of applicants and damaging trust in the system.

**Recommendation: Integrate Fairness-Aware Algorithms**

Implement fairness-aware algorithms that assess and mitigate bias in funding opportunity matching. This change will ensure equitable outcomes for all applicants, addressing the critical fairness gap.

*Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to integrate bias detection and mitigation techniques into the matching algorithm, and conduct regular audits to ensure fairness.

*Priority:* High | *Expected HI Impact:* Enhances Responsible property by ensuring equitable treatment of applicants.

#### Gap G-S6-02: Absence of Explainability

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The system lacks the capability to explain its decisions to human agents, which is crucial for fostering collaboration. This gap violates the Explainable principle, as users cannot understand or trust the AI's recommendations without transparency.

**Practical Impact**
> The inability to explain decisions may lead to user frustration and reluctance to engage with the AI, ultimately hindering effective collaboration.

**Recommendation: Develop Explainable Decision Framework**

Create a framework that generates clear explanations for the AI's funding recommendations. This will improve user trust and facilitate collaboration by making the decision-making process transparent.

*Implementation:* Incorporate techniques such as LIME or SHAP to provide interpretable outputs alongside the AI's recommendations, and ensure these explanations are accessible within the user interface.

*Priority:* High | *Expected HI Impact:* Improves Explainable property by fostering user understanding and trust.

#### Gap G-S6-03: Missing Human Feedback Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The system does not incorporate human feedback in its evaluation processes, which is vital for learning and improvement. This absence violates the Adaptive principle, as the AI cannot refine its performance based on user interactions.

**Practical Impact**
> Without human-driven feedback loops, the AI's ability to adapt and enhance its matching capabilities over time is severely limited, reducing its effectiveness.

**Recommendation: Implement Human Feedback Loops**

Establish mechanisms for users to provide feedback on the AI's recommendations, enabling continuous learning and improvement. This will allow the system to adapt based on real-world interactions.

*Implementation:* Create a feedback interface where users can rate recommendations and provide comments, and integrate this feedback into the training pipeline to refine the model iteratively.

*Priority:* High | *Expected HI Impact:* Enhances Adaptive property by enabling the system to learn from user interactions.

### S7 — S7 — AI-Assisted Argument Testing and Draft Strengthening

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The leapspace AI system fails to meet critical HI principles, lacking essential fairness, explainability, and adaptive feedback mechanisms. These deficiencies severely undermine the collaborative potential of the system.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | There is no evidence of the AI agent initiating collaboration or establishing shared awareness, indicating a reactive capability. |
| Adaptive | 1 — Reactive | The system lacks a feedback mechanism for human actions, preventing it from adapting and limiting it to a reactive state. |
| Responsible | 1 — Reactive | The absence of fairness-aware processing capabilities compromises ethical integrity, resulting in a reactive approach to responsibility. |
| Explainable | 1 — Reactive | The lack of explainability features means the AI cannot clarify its decisions, reflecting a reactive capability in this dimension. |

#### Gap G-S7-01: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system does not incorporate any fairness-aware processing capabilities, which is essential for preventing discriminatory outcomes. This absence compromises the ethical integrity of the AI's decisions and recommendations.

**Practical Impact**
> Without fairness mechanisms, the AI may produce biased outputs, leading to unfair treatment of users and eroding trust in the system.

**Recommendation: Integrate Fairness-Aware Algorithms**

Implement fairness-aware algorithms that assess and mitigate bias in the AI's outputs. This will ensure that recommendations are equitable and uphold ethical standards, addressing the lack of fairness mechanisms.

*Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to integrate fairness checks into the decision-making process of the AI system. Conduct regular audits to ensure compliance with fairness benchmarks.

*Priority:* High | *Expected HI Impact:* Enhances Responsible AI by ensuring equitable treatment of all users.

#### Gap G-S7-02: Absence of Explainability Features

| Property | Value |
|----------|-------|
| CARE Dimension | **Explainable** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The lack of explainability capabilities means that the AI cannot clarify its decisions or recommendations to human agents. This gap prevents users from understanding the rationale behind AI outputs, which is crucial for informed decision-making.

**Practical Impact**
> Without explainability, users may struggle to trust or effectively collaborate with the AI, limiting the overall effectiveness of the system.

**Recommendation: Develop Explainability Interfaces**

Create user-facing interfaces that provide clear explanations for AI decisions and recommendations. This will help users understand the rationale behind outputs, fostering trust and collaboration.

*Implementation:* Leverage tools like LIME or SHAP to generate explanations for model predictions and integrate these explanations into the user interface. Ensure that explanations are tailored to the context of the user's queries.

*Priority:* High | *Expected HI Impact:* Improves Explainability by enabling users to comprehend AI reasoning.

#### Gap G-S7-03: Missing Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The system lacks a feedback mechanism that incorporates human actions, which is vital for adaptive learning. Without human input, the AI cannot refine its performance or align with user preferences over time.

**Practical Impact**
> The absence of adaptive feedback limits the system's ability to improve, resulting in a static AI that may not meet evolving user needs or preferences.

**Recommendation: Implement Human Feedback Loop**

Establish a feedback mechanism that allows users to provide input on AI recommendations, enabling the system to adapt and learn from user preferences. This addresses the absence of a human feedback mechanism.

*Implementation:* Design a simple feedback interface where users can rate AI suggestions and provide comments. Use this data to retrain the model periodically, ensuring it evolves with user needs.

*Priority:* High | *Expected HI Impact:* Enhances Adaptive capabilities by allowing the AI to learn from user interactions.

### S8 — S8 — Governed Evidence Verification for Corporate and Regulated R&D

**Status:** ❌ FAIL  
**HI Gaps:** 4  

> The leapspace AI system fails to meet essential HI principles, particularly in responsibility, collaboration, and adaptability. Key capabilities for fairness, explainability, and human feedback are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system does not involve any AI participation in interactions, which limits its collaborative capabilities as evidenced by the gap titled 'No AI Participation in Interactions'. |
| Adaptive | 1 — Reactive | The absence of a human feedback mechanism, as noted in the gap titled 'No Human Feedback Mechanism', prevents the system from adapting to user preferences. |
| Responsible | 1 — Reactive | The lack of fairness mechanisms, highlighted in the gap titled 'Lack of Fairness Mechanisms', indicates that the system does not address critical issues of bias or accountability. |
| Explainable | 1 — Reactive | There is no evidence of explainability capabilities, as indicated by the gap titled 'Absence of Explainability', which undermines user understanding of AI decisions. |

#### Gap G-S8-01: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system lacks any capability related to fairness or bias mitigation, which is crucial for ensuring equitable outcomes. Without these mechanisms, the AI could produce discriminatory results, undermining trust and accountability in the human-AI collaboration.

**Practical Impact**
> This absence can lead to biased decision-making, harming stakeholders and eroding confidence in the AI system.

**Recommendation: Implement Fairness Assessment Tools**

Integrate fairness assessment tools that evaluate model outputs for bias across different demographic groups. This will ensure that the AI system produces equitable outcomes and builds trust among stakeholders.

*Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to assess and mitigate biases in the model's predictions during the training phase. Regularly audit the model outputs for fairness metrics.

*Priority:* High | *Expected HI Impact:* Enhances Responsible AI by ensuring equitable outcomes and accountability.

#### Gap G-S8-02: Absence of Explainability

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The system does not provide any explainability capabilities, preventing human agents from understanding AI decisions or recommendations. This lack of transparency is detrimental to effective collaboration, as humans cannot verify or trust the AI's outputs.

**Practical Impact**
> Without explainability, users may hesitate to rely on AI outputs, diminishing the collaborative potential and effectiveness of the system.

**Recommendation: Add Explainability Features**

Incorporate explainability tools like LIME or SHAP to provide insights into AI decision-making processes. This will enable human agents to understand and trust AI recommendations, fostering better collaboration.

*Implementation:* Integrate these explainability libraries into the existing AI model pipeline, ensuring that explanations are generated alongside predictions and are easily accessible to users.

*Priority:* High | *Expected HI Impact:* Improves Explainable AI, enhancing transparency and user trust.

#### Gap G-S8-03: No Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The feedback mechanism does not incorporate human actions, which is essential for the system to learn and improve over time. This absence of human-driven feedback loops prevents the AI from adapting to user preferences and reduces its overall effectiveness.

**Practical Impact**
> The lack of adaptability means the system cannot evolve based on user interactions, leading to stagnation and potentially irrelevant outputs.

**Recommendation: Establish Human Feedback Loops**

Develop a mechanism for users to provide feedback on AI outputs, which will be used to retrain and adapt the model. This will ensure the AI system evolves based on real user interactions and preferences.

*Implementation:* Create a user interface component where users can rate AI suggestions and provide comments, and implement a feedback processing system that feeds this data back into the model training pipeline.

*Priority:* High | *Expected HI Impact:* Enhances Adaptive AI by allowing the system to learn from user interactions.

#### Gap G-S8-04: No AI Participation in Interactions

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded interactions do not involve any Artificial Agent, which is a fundamental requirement for collaborative human-AI engagement. This absence means that the system cannot facilitate joint task execution, undermining the collaborative aspect of HI.

**Practical Impact**
> Without AI participation, the system fails to leverage the strengths of both human and AI agents, limiting the potential for effective teamwork and problem-solving.

**Recommendation: Integrate AI Agents in Interactions**

Design and implement AI agents that actively participate in user interactions, providing suggestions and insights during collaborative tasks. This will enhance the collaborative capabilities of the system.

*Implementation:* Utilize existing conversational AI frameworks to create agents that can engage with users in real-time, ensuring they are capable of understanding and responding to user queries effectively.

*Priority:* High | *Expected HI Impact:* Strengthens Collaborative AI by facilitating joint task execution and teamwork.

---

## 4. Consolidated Recommendations

### Collaborative Dimension

- **[High Priority] Add Explainability Features**  
  *Scenario:* S1 — Departmental Literature Review Synthesis  
  Incorporate explainability features such as LIME or SHAP to provide insights into the AI's decision-making process. This will help users understand the rationale behind recommendations, fostering trust and collaboration.  
  *Implementation:* Integrate LIME or SHAP into the model's output layer to generate explanations for each recommendation, and create a user interface element to display these explanations clearly.

- **[High Priority] Enable AI Participation in Interactions**  
  *Scenario:* S1 — Departmental Literature Review Synthesis  
  Design the system to allow AI agents to actively participate in user interactions, facilitating joint task execution and decision-making. This will enhance the collaborative potential of the system.  
  *Implementation:* Develop an interactive interface where AI can suggest actions or decisions during user sessions, and ensure that the AI can respond to user inputs in real-time.

- **[High Priority] Develop Explainability Features**  
  *Scenario:* S2 — Cross-Domain Onboarding for Unfamiliar Research Areas  
  Create a module that generates clear, user-friendly explanations for the AI's decisions. This will help human agents understand the rationale behind outputs, fostering trust and effective collaboration.  
  *Implementation:* Utilize explainability frameworks like LIME or SHAP to generate explanations for model predictions and integrate these explanations into the user interface for easy access.

- **[High Priority] Integrate AI Agent for Interaction**  
  *Scenario:* S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature  
  Develop and deploy an AI agent that actively participates in user interactions, facilitating collaborative decision-making. This will enhance the system's collaborative potential by leveraging AI capabilities effectively.  
  *Implementation:* Create a chatbot or virtual assistant that can engage users in real-time, providing suggestions and insights based on user inputs. Ensure the AI agent can learn from interactions to improve its responses.

- **[High Priority] Add Explainability Features to AI Outputs**  
  *Scenario:* S5 — Cross-Disciplinary Connection-Finding and Author/Collaborator Search  
  Develop and integrate explainability features that provide insights into the AI's decision-making process, such as feature importance scores or decision rationale. This will enhance user trust and facilitate better collaboration.  
  *Implementation:* Incorporate tools like LIME or SHAP to generate explanations for AI recommendations, ensuring they are easily accessible within the user interface.

- **[High Priority] Develop Explainable Decision Framework**  
  *Scenario:* S6 — Research-to-Funding Opportunity Matching  
  Create a framework that generates clear explanations for the AI's funding recommendations. This will improve user trust and facilitate collaboration by making the decision-making process transparent.  
  *Implementation:* Incorporate techniques such as LIME or SHAP to provide interpretable outputs alongside the AI's recommendations, and ensure these explanations are accessible within the user interface.

- **[High Priority] Add Explainability Features**  
  *Scenario:* S8 — Governed Evidence Verification for Corporate and Regulated R&D  
  Incorporate explainability tools like LIME or SHAP to provide insights into AI decision-making processes. This will enable human agents to understand and trust AI recommendations, fostering better collaboration.  
  *Implementation:* Integrate these explainability libraries into the existing AI model pipeline, ensuring that explanations are generated alongside predictions and are easily accessible to users.

- **[High Priority] Integrate AI Agents in Interactions**  
  *Scenario:* S8 — Governed Evidence Verification for Corporate and Regulated R&D  
  Design and implement AI agents that actively participate in user interactions, providing suggestions and insights during collaborative tasks. This will enhance the collaborative capabilities of the system.  
  *Implementation:* Utilize existing conversational AI frameworks to create agents that can engage with users in real-time, ensuring they are capable of understanding and responding to user queries effectively.

### Adaptive Dimension

- **[High Priority] Integrate Human Feedback Loops**  
  *Scenario:* S1 — Departmental Literature Review Synthesis  
  Develop a mechanism for collecting human feedback on AI outputs to inform model updates and improvements. This will allow the AI to adapt based on user preferences and performance metrics.  
  *Implementation:* Implement a feedback interface where users can rate recommendations and provide comments, and use this data to retrain the model periodically based on user input.

- **[High Priority] Introduce Human Feedback Loop**  
  *Scenario:* S2 — Cross-Domain Onboarding for Unfamiliar Research Areas  
  Establish a feedback mechanism that allows users to provide input on AI decisions, which will be used to refine and adapt the model over time. This ensures the AI evolves based on real user interactions and preferences.  
  *Implementation:* Design a user interface component that prompts users for feedback after key decisions, and implement a backend system to collect, analyze, and incorporate this feedback into model retraining processes.

- **[High Priority] Establish Human Feedback Channels**  
  *Scenario:* S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature  
  Implement a mechanism for users to provide feedback on AI recommendations, allowing the system to learn and adapt over time. This will address the lack of human feedback and enhance the system's relevance.  
  *Implementation:* Create a user interface element where users can rate recommendations or provide comments, and use this data to refine AI models through supervised learning techniques.

- **[High Priority] Establish Human Feedback Loop Mechanism**  
  *Scenario:* S5 — Cross-Disciplinary Connection-Finding and Author/Collaborator Search  
  Create a feedback loop that allows users to provide input on AI recommendations, which the system can use to adapt and improve its performance over time. This will enhance the AI's relevance and effectiveness.  
  *Implementation:* Implement a user interface feature that prompts users for feedback after each AI recommendation, and store this feedback to retrain the model periodically.

- **[High Priority] Implement Human Feedback Loops**  
  *Scenario:* S6 — Research-to-Funding Opportunity Matching  
  Establish mechanisms for users to provide feedback on the AI's recommendations, enabling continuous learning and improvement. This will allow the system to adapt based on real-world interactions.  
  *Implementation:* Create a feedback interface where users can rate recommendations and provide comments, and integrate this feedback into the training pipeline to refine the model iteratively.

- **[High Priority] Implement Human Feedback Loop**  
  *Scenario:* S7 — AI-Assisted Argument Testing and Draft Strengthening  
  Establish a feedback mechanism that allows users to provide input on AI recommendations, enabling the system to adapt and learn from user preferences. This addresses the absence of a human feedback mechanism.  
  *Implementation:* Design a simple feedback interface where users can rate AI suggestions and provide comments. Use this data to retrain the model periodically, ensuring it evolves with user needs.

- **[High Priority] Establish Human Feedback Loops**  
  *Scenario:* S8 — Governed Evidence Verification for Corporate and Regulated R&D  
  Develop a mechanism for users to provide feedback on AI outputs, which will be used to retrain and adapt the model. This will ensure the AI system evolves based on real user interactions and preferences.  
  *Implementation:* Create a user interface component where users can rate AI suggestions and provide comments, and implement a feedback processing system that feeds this data back into the model training pipeline.

### Responsible Dimension

- **[High Priority] Implement Fairness Auditing Tools**  
  *Scenario:* S1 — Departmental Literature Review Synthesis  
  Integrate fairness auditing tools into the AI system to identify and mitigate biases in recommendations. This will ensure that the system produces equitable outcomes and maintains ethical standards in human-AI collaboration.  
  *Implementation:* Utilize existing libraries like AI Fairness 360 or Fairlearn to assess and adjust the model's outputs for fairness, and incorporate these checks into the model training pipeline.

- **[High Priority] Implement Fairness Auditing Tools**  
  *Scenario:* S2 — Cross-Domain Onboarding for Unfamiliar Research Areas  
  Integrate fairness auditing tools that assess and mitigate bias in the AI's decision-making process. This will ensure that the system produces equitable outcomes, thereby enhancing trust and ethical standards in human-AI collaboration.  
  *Implementation:* Select and integrate an existing fairness library (e.g., AI Fairness 360) into the system's pipeline to evaluate model outputs for bias and implement corrective measures based on the findings.

- **[High Priority] Implement Fairness Assessment Tools**  
  *Scenario:* S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature  
  Integrate fairness assessment tools that evaluate model outputs for bias across different demographic groups. This will help ensure equitable outcomes and mitigate discriminatory practices, addressing the critical gap in fairness mechanisms.  
  *Implementation:* Utilize existing libraries like AI Fairness 360 or Fairlearn to assess and adjust model predictions based on fairness metrics. Incorporate these tools into the model evaluation pipeline.

- **[High Priority] Implement Fairness-Aware Algorithms**  
  *Scenario:* S4 — Evidence-Strength Calibration and Hallucination Mitigation  
  Integrate fairness-aware algorithms into the decision-making processes of the AI system to actively identify and mitigate biases. This change will ensure that the system operates responsibly, promoting equitable outcomes for all users.  
  *Implementation:* Utilize existing libraries such as Fairlearn or AIF360 to assess and adjust model predictions for fairness metrics during training and evaluation phases. Conduct regular audits to ensure ongoing compliance with fairness standards.

- **[High Priority] Implement Fairness Auditing Tools**  
  *Scenario:* S5 — Cross-Disciplinary Connection-Finding and Author/Collaborator Search  
  Integrate fairness auditing tools that assess and mitigate bias in the AI's decision-making process. This will ensure equitable outcomes and build trust among users by addressing potential discrimination.  
  *Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to analyze model outputs for bias and implement corrective measures based on the audit results.

- **[High Priority] Integrate Fairness-Aware Algorithms**  
  *Scenario:* S6 — Research-to-Funding Opportunity Matching  
  Implement fairness-aware algorithms that assess and mitigate bias in funding opportunity matching. This change will ensure equitable outcomes for all applicants, addressing the critical fairness gap.  
  *Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to integrate bias detection and mitigation techniques into the matching algorithm, and conduct regular audits to ensure fairness.

- **[High Priority] Integrate Fairness-Aware Algorithms**  
  *Scenario:* S7 — AI-Assisted Argument Testing and Draft Strengthening  
  Implement fairness-aware algorithms that assess and mitigate bias in the AI's outputs. This will ensure that recommendations are equitable and uphold ethical standards, addressing the lack of fairness mechanisms.  
  *Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to integrate fairness checks into the decision-making process of the AI system. Conduct regular audits to ensure compliance with fairness benchmarks.

- **[High Priority] Implement Fairness Assessment Tools**  
  *Scenario:* S8 — Governed Evidence Verification for Corporate and Regulated R&D  
  Integrate fairness assessment tools that evaluate model outputs for bias across different demographic groups. This will ensure that the AI system produces equitable outcomes and builds trust among stakeholders.  
  *Implementation:* Utilize existing libraries such as AIF360 or Fairlearn to assess and mitigate biases in the model's predictions during the training phase. Regularly audit the model outputs for fairness metrics.

### Explainable Dimension

- **[High Priority] Add Explainability Features**  
  *Scenario:* S3 — Multidisciplinary Evidence Synthesis for Sparse or Fragmented Literature  
  Incorporate explainability mechanisms that provide users with insights into how AI decisions are made. This will enhance user trust and understanding of AI outputs, addressing the explainability gap.  
  *Implementation:* Utilize frameworks like LIME or SHAP to generate explanations for model predictions and integrate these explanations into the user interface, ensuring they are accessible and understandable.

- **[High Priority] Develop Explainability Interfaces**  
  *Scenario:* S7 — AI-Assisted Argument Testing and Draft Strengthening  
  Create user-facing interfaces that provide clear explanations for AI decisions and recommendations. This will help users understand the rationale behind outputs, fostering trust and collaboration.  
  *Implementation:* Leverage tools like LIME or SHAP to generate explanations for model predictions and integrate these explanations into the user interface. Ensure that explanations are tailored to the context of the user's queries.

---

## 5. HI Maturity Assessment

**Maturity Level: Level 0: Pre-HI**

The system does not meaningfully embody Hybrid Intelligence principles. Fundamental changes to the human-AI collaboration model are required.

| CARE Dimension | Score | Status |
|----------------|-------|--------|
| Collaborative | 25% | Needs Work |
| Adaptive | 12% | Needs Work |
| Responsible | 0% | Needs Work |
| Explainable | 75% | Adequate |

### Strengths

- No dimension achieved full conformance in this assessment.

### Areas for Improvement

- **Collaborative** (25%): See recommendations in Section 4.
- **Adaptive** (12%): See recommendations in Section 4.
- **Responsible** (0%): See recommendations in Section 4.
- **Explainable** (75%): See recommendations in Section 4.

---

## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)

This section complements the score-based maturity level in Section 5 with a finer-grained, literature-grounded assessment of *how* each CARE dimension is demonstrated, adapted from the CARE capability-level tables (Hybrid Intelligence Centre Netherlands, 2023; cf. Akata et al. 2020; Zamprogno, Tiddi & Verheij 2025). Each scenario is classified per CARE dimension into one of three levels: **1 — Reactive** (the capability is only exercised upon explicit human instruction), **2 — Proactive** (the AI initiates or anticipates without being explicitly prompted), or **3 — Social** (the capability is sustained, repaired, or co-constructed over time with the human partner). The maximum level admissible for a dimension in a given scenario is capped by the most severe HI gap identified in that dimension in Phase 5 (Critical → capped at 1, Major → capped at 2, Minor/none → uncapped at 3), so the classification stays grounded in the symbolic SHACL evidence rather than unconstrained LLM judgement. This is distinct from the conformance score in Section 2.2, which measures whether a capability is present at all, not how maturely it is exercised.

### 6.1 Per-Scenario CARE Levels

| Scenario | Collaborative | Adaptive | Responsible | Explainable |
|----------|----------------|----------|--------------|-------------|
| S1 — S1 — Departmental Literature Review | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S2 — S2 — Cross-Domain Onboarding for Un | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S3 — S3 — Multidisciplinary Evidence Syn | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S4 — S4 — Evidence-Strength Calibration  | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S5 — S5 — Cross-Disciplinary Connection- | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S6 — S6 — Research-to-Funding Opportunit | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 3 (Social) |
| S7 — S7 — AI-Assisted Argument Testing a | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S8 — S8 — Governed Evidence Verification | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |

### 6.2 Use-Case CARE Maturity Summary

Levels are an ordinal scale (Reactive < Proactive < Social), so the table below reports the distribution and the modal (most frequent) level per dimension across all scenarios rather than an average.

| Dimension | Level 1 (Reactive) | Level 2 (Proactive) | Level 3 (Social) | Modal Level |
|-----------|---------------------|----------------------|--------------------|-------------|
| Collaborative | 8 | 0 | 0 | **1 — Reactive** |
| Adaptive | 8 | 0 | 0 | **1 — Reactive** |
| Responsible | 8 | 0 | 0 | **1 — Reactive** |
| Explainable | 7 | 0 | 1 | **1 — Reactive** |

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