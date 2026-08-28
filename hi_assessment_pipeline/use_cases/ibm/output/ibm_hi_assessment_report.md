# HI Assessment Report: IBM

**Assessment Date:** 2026-08-25  
**HI Ontology Version:** 2.0.0 (VU Amsterdam)  
**Pipeline:** Neuro-Symbolic HI Assessment Pipeline  
**LLM Model:** gpt-4o-mini  

---

## 1. Executive Summary

The assessment of the IBM AI system reveals a concerning overall HI conformance score of 0.0%, indicating a maturity level classified as Level 0: Pre-HI. Out of the eight scenarios assessed, all demonstrated significant gaps, culminating in a total of 21 identified deficiencies across the CARE dimensions. 

The primary strength identified within the CARE framework is the Adaptive dimension, which scored 50%. This suggests some capacity for responsiveness to changes, albeit without the necessary human feedback mechanisms that would enhance its effectiveness. However, this strength is overshadowed by critical gaps, particularly in the Collaborative and Responsible dimensions, both of which scored poorly at 0% and 38%, respectively. The absence of AI participation in interactions and fairness mechanisms significantly undermines the system's potential to operate ethically and effectively in collaborative environments.

The overall assessment categorizes the IBM system as a non-compliant HI system, lacking essential features for collaboration, adaptability, responsibility, and explainability. The absence of explainability capabilities further exacerbates the challenges in ensuring transparency and accountability in AI operations.

Despite these shortcomings, there exists substantial potential for improvement. By addressing the identified gaps, particularly in enhancing collaborative features and implementing fairness mechanisms, IBM can elevate its AI system towards a more compliant and mature HI framework. This proactive approach could significantly enhance user trust and system efficacy in future deployments.

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
| Total HI Gaps | 21 |

> The system does not meaningfully embody Hybrid Intelligence principles. Fundamental changes to the human-AI collaboration model are required.

### 2.2 CARE Dimension Analysis

| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| **Collaborative** | ❌ 0% | Human and AI agents co-participate in interactions |
| **Adaptive** | ⚠️ 50% | Feedback loops and learning mechanisms |
| **Responsible** | ❌ 38% | Oversight, fairness, and accountability |
| **Explainable** | ⚠️ 50% | AI transparency and decision explanation |

### 2.3 Scenario Overview

| Scenario | Label | Status | Gaps |
|----------|-------|--------|------|
| S1 | S1 — Predictive Model Governance & Continuous Monitoring | ❌ FAIL | 2 |
| S2 | S2 — RAG Application Quality Evaluation & Promotion-to-Production | ❌ FAIL | 3 |
| S3 | S3 — GenAI Use-Case Approval & Regulatory Risk Classification | ❌ FAIL | 3 |
| S4 | S4 — Prompt Security Hardening via Automated Red-Teaming | ❌ FAIL | 2 |
| S5 | S5 — Multi-Agent (Agentic AI) Governance Across the Lifecycle | ❌ FAIL | 3 |
| S6 | S6 — Virtual Assistant Production Quality & Safety Monitoring | ❌ FAIL | 4 |
| S7 | S7 — Governed AI-Assisted Candidate Screening and Interview Coordination | ❌ FAIL | 3 |
| S8 | S8 — Enterprise Model Risk Governance (MRG) Across Multi-Cloud Third-Party Models | ❌ FAIL | 1 |

---

## 3. Detailed Scenario Analysis

### S1 — S1 — Predictive Model Governance & Continuous Monitoring

**Status:** ❌ FAIL  
**HI Gaps:** 2  

> The scenario fails to meet critical HI conformance due to the absence of collaborative interactions and adaptive feedback mechanisms. This significantly undermines the potential for effective human-AI collaboration.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The recorded interactions do not involve any artificial agents, indicating a lack of AI participation in interactions, which limits collaborative capabilities. |
| Adaptive | 1 — Reactive | The evaluation process lacks any mention of human feedback, preventing the system from adapting or improving over time. |
| Responsible | 3 — Social | There is no evidence of gaps in the Responsible dimension, allowing for the highest level of maturity. |
| Explainable | 3 — Social | There is no evidence of gaps in the Explainable dimension, allowing for the highest level of maturity. |

#### Gap G-S1-01: Lack of AI Participation in Interactions

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded interactions do not involve any artificial agents, which is a fundamental requirement for human-AI collaboration. Without AI participation, the system cannot facilitate meaningful joint task execution, violating the essence of collaborative intelligence.

**Practical Impact**
> This absence prevents any collaborative decision-making or task execution, severely limiting the effectiveness and utility of the AI system in real-world applications.

**Recommendation: Integrate AI Agents in Interaction Processes**

Modify the interaction framework to include AI agents that can actively participate in dialogues and decision-making processes. This will enhance collaborative efforts by allowing both humans and AI to contribute to task execution, thereby addressing the lack of AI participation.

*Implementation:* Utilize existing AI models to create virtual agents that can engage in real-time interactions, and ensure they are integrated into the user interface for seamless collaboration.

*Priority:* High | *Expected HI Impact:* Enhances collaborative intelligence by enabling joint task execution.

#### Gap G-S1-02: Absence of Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The evaluation process lacks any mention of human feedback, which is essential for adaptive learning in HI systems. Without human signals to inform model updates, the system cannot learn from past interactions, leading to stagnation and reduced performance over time.

**Practical Impact**
> The inability to incorporate human feedback hampers the system's capacity to improve and adapt, resulting in a static model that fails to meet evolving user needs and contexts.

**Recommendation: Implement Human Feedback Collection Mechanism**

Develop a structured feedback system where users can provide input on AI decisions and outputs. This will allow the model to learn from human interactions, fostering adaptability and continuous improvement.

*Implementation:* Incorporate feedback buttons or prompts in the user interface that allow users to rate AI suggestions and provide comments, which can then be used to retrain the model periodically.

*Priority:* High | *Expected HI Impact:* Improves adaptability by enabling the system to learn from user feedback.

### S2 — S2 — RAG Application Quality Evaluation & Promotion-to-Production

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The scenario lacks essential human-AI collaboration and feedback mechanisms. Critical gaps in collaboration and responsibility hinder effective human-AI interaction.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of AI in interaction as highlighted by gap G-S2-01 indicates that the system cannot participate in collaboration, thus limiting it to a reactive level. |
| Adaptive | 1 — Reactive | The lack of a human feedback mechanism as noted in gap G-S2-02 means the system does not adapt or learn from interactions, confining it to a reactive level. |
| Responsible | 1 — Reactive | The absence of fairness mechanisms as described in gap G-S2-03 results in a lack of responsible behavior, restricting the system to a reactive level. |
| Explainable | 3 — Social | There is no evidence of gaps in the explainability dimension, allowing for the highest level of social engagement in explanations. |

#### Gap G-S2-01: Absence of AI in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded human-AI interaction episodes do not involve any artificial agent, which is a fundamental requirement for collaborative systems. Without AI participation, the essence of human-AI collaboration is entirely missing, rendering the system incapable of fulfilling its intended purpose.

**Practical Impact**
> This absence prevents any meaningful collaboration, leading to ineffective task execution and decision-making processes.

**Recommendation: Integrate AI Agents in Interaction Episodes**

Implement AI agents that actively participate in human-AI interaction episodes to facilitate collaboration. This will enhance the system's ability to assist users in decision-making and task execution, fulfilling the collaborative requirement.

*Implementation:* Utilize existing AI models to create virtual agents that can engage with users during interactions, ensuring they can provide suggestions and feedback based on user inputs.

*Priority:* High | *Expected HI Impact:* Enhances collaborative capabilities by enabling meaningful human-AI interactions.

#### Gap G-S2-02: Lack of Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The evaluation process lacks a feedback mechanism that incorporates human actions, which is essential for adaptive learning. Without human signals to inform model updates, the system cannot learn from past interactions, limiting its ability to improve over time.

**Practical Impact**
> This gap results in a static system that does not evolve based on user needs or preferences, reducing its effectiveness and relevance in real-world applications.

**Recommendation: Establish Human Feedback Loop Mechanism**

Develop a feedback mechanism that captures human actions and decisions during the evaluation process to inform adaptive learning. This will allow the system to evolve based on user interactions and preferences.

*Implementation:* Integrate a user interface element that prompts users to provide feedback after interactions, and use this data to adjust model parameters and improve performance over time.

*Priority:* High | *Expected HI Impact:* Improves adaptability by enabling the system to learn from user feedback.

#### Gap G-S2-03: Absence of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system lacks any capabilities related to fairness or bias mitigation, which are crucial for responsible AI design. Without these mechanisms, the system risks producing discriminatory outcomes, undermining trust and accountability.

**Practical Impact**
> The absence of fairness considerations can lead to biased decision-making, harming users and stakeholders and potentially resulting in legal and ethical repercussions.

**Recommendation: Implement Fairness and Bias Mitigation Tools**

Incorporate fairness assessment tools and bias mitigation techniques into the system to ensure responsible AI design. This will help prevent discriminatory outcomes and build trust with users.

*Implementation:* Utilize existing libraries and frameworks for fairness analysis and integrate them into the decision-making processes of the AI system, allowing for real-time bias checks.

*Priority:* High | *Expected HI Impact:* Enhances responsibility by ensuring fair and unbiased decision-making.

### S3 — S3 — GenAI Use-Case Approval & Regulatory Risk Classification

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The ibm AI system fails to meet essential HI principles, particularly in collaboration and responsibility. Key components for human-AI interaction and fairness are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system lacks an Artificial Agent in recorded human-AI interactions, which prevents any collaborative participation, thus limiting it to a reactive state. |
| Adaptive | 2 — Proactive | There is no evidence of gaps in the Adaptive dimension, allowing for a proactive classification within the maximum admissible level. |
| Responsible | 1 — Reactive | The system does not incorporate any fairness or bias mitigation capabilities, which limits its responsible behavior to a reactive state. |
| Explainable | 1 — Reactive | The absence of explainability mechanisms means the AI cannot clarify its decisions, restricting it to a reactive level. |

#### Gap G-S3-01: Absence of AI in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The system lacks an Artificial Agent in recorded human-AI interactions, which is fundamental for collaboration. Without AI participation, the essence of hybrid intelligence is compromised, as human and AI cannot co-participate in tasks.

**Practical Impact**
> This absence severely limits the potential for effective teamwork between humans and AI, undermining the system's ability to leverage AI capabilities in decision-making.

**Recommendation: Integrate AI Agent for Interaction**

Develop and integrate an AI agent that actively participates in human-AI interactions. This will enable collaborative decision-making and enhance the hybrid intelligence aspect of the system.

*Implementation:* Utilize existing AI models to create an interactive agent that can engage in dialogues, provide suggestions, and assist in decision-making processes. Ensure it is embedded within the current interaction framework.

*Priority:* High | *Expected HI Impact:* This enhances collaboration by enabling real-time AI participation, fostering teamwork between humans and AI.

#### Gap G-S3-02: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system does not incorporate any fairness or bias mitigation capabilities, which are essential for responsible AI deployment. This gap raises concerns about potential discriminatory outcomes, violating the principle of accountability.

**Practical Impact**
> Without fairness mechanisms, the system risks perpetuating biases in decision-making, which can lead to unfair treatment of individuals or groups in real-world applications.

**Recommendation: Implement Fairness and Bias Mitigation Tools**

Incorporate fairness algorithms and bias detection mechanisms into the decision-making process of the AI system. This will ensure that outputs are equitable and reduce the risk of discriminatory practices.

*Implementation:* Select and integrate established fairness libraries or frameworks that can analyze and adjust AI outputs for bias. Conduct regular audits to monitor fairness metrics.

*Priority:* High | *Expected HI Impact:* This promotes responsible AI usage by ensuring decisions are fair and accountable, addressing potential biases.

#### Gap G-S3-03: No Explainability Capabilities

| Property | Value |
|----------|-------|
| CARE Dimension | **Explainable** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The absence of explainability mechanisms means that the AI cannot clarify its decisions or recommendations to human agents. This lack of transparency is critical for trust and understanding in human-AI interactions.

**Practical Impact**
> Without the ability to explain its reasoning, the AI's outputs may be viewed as opaque, leading to mistrust and reluctance from humans to engage with the system effectively.

**Recommendation: Add Explainability Features to AI Outputs**

Develop and implement explainability mechanisms that allow the AI to articulate its decision-making process and reasoning. This will build trust and understanding in human-AI interactions.

*Implementation:* Utilize explainable AI frameworks to generate interpretable outputs and visualizations that clarify the AI's reasoning. Ensure these features are integrated into the user interface for easy access.

*Priority:* High | *Expected HI Impact:* This enhances explainability, fostering trust and engagement from users by making AI decisions transparent.

### S4 — S4 — Prompt Security Hardening via Automated Red-Teaming

**Status:** ❌ FAIL  
**HI Gaps:** 2  

> The ibm AI system fails to meet critical HI conformance requirements, particularly in collaboration and responsibility. Key elements such as explainability and fairness mechanisms are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system lacks explainability mechanisms, which severely limits the ability of human agents to engage with the AI, thereby reducing collaboration effectiveness. |
| Adaptive | 1 — Reactive | There is no evidence of adaptive capabilities, leading to a conservative classification at the lowest level. |
| Responsible | 1 — Reactive | The absence of fairness mechanisms indicates a critical gap in responsible AI deployment, necessitating a classification at the lowest level. |
| Explainable | 1 — Reactive | There is no evidence of tailored explanations, which are essential for effective communication and understanding between the AI and human agents. |

#### Gap G-S4-01: Lack of Explainability Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | Explainable |

**Gap Description**
> The system lacks the capability to explain its decisions to human agents, which is essential for effective collaboration. Without explainability, human agents cannot understand or trust the AI's recommendations, undermining the collaborative nature of the human-AI team.

**Practical Impact**
> This absence severely limits the ability of human agents to engage with the AI, reducing the overall effectiveness and trust in the collaboration.

**Recommendation: Implement Explainability Interfaces for AI Decisions**

Develop and integrate an explainability module that provides human agents with clear, understandable rationales for the AI's decisions. This will enhance trust and facilitate better collaboration by allowing users to comprehend the reasoning behind AI recommendations.

*Implementation:* Utilize existing explainable AI frameworks, such as LIME or SHAP, to generate decision explanations and present them through a user-friendly interface in the existing application. Ensure that the explanations are contextually relevant to the tasks at hand.

*Priority:* High | *Expected HI Impact:* This improves the Explainable property by enabling users to understand AI decisions, fostering trust and collaboration.

#### Gap G-S4-02: Absence of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | Responsible |

**Gap Description**
> The system does not incorporate any fairness or bias mitigation capabilities, which are crucial for responsible AI deployment. This lack of fairness mechanisms can lead to discriminatory outcomes, which not only violate ethical standards but also erode trust in the AI system.

**Practical Impact**
> Without fairness considerations, the AI's decisions may disproportionately affect certain groups, leading to significant ethical and operational risks in real-world applications.

**Recommendation: Integrate Fairness Auditing Tools**

Incorporate fairness auditing tools into the AI system to assess and mitigate biases in decision-making processes. This will ensure that the AI operates responsibly and does not lead to discriminatory outcomes.

*Implementation:* Select and integrate fairness assessment libraries, such as AI Fairness 360 or Fairlearn, into the model evaluation pipeline. Regularly audit the AI's outputs for fairness metrics and adjust the training data or algorithms accordingly to address identified biases.

*Priority:* High | *Expected HI Impact:* This enhances the Responsible property by ensuring equitable treatment across diverse user groups, thereby building trust.

### S5 — S5 — Multi-Agent (Agentic AI) Governance Across the Lifecycle

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The ibm AI system fails to meet critical HI conformance requirements, lacking essential collaborative and responsible features. Key capabilities for human-AI interaction and fairness are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The system lacks any artificial agent involvement in recorded human-AI interactions, which is fundamental for collaboration. |
| Adaptive | 1 — Reactive | There is no evidence of adaptive capabilities, so the lower level is chosen conservatively. |
| Responsible | 1 — Reactive | The system does not incorporate any capabilities related to fairness or bias mitigation, which are essential for responsible AI governance. |
| Explainable | 1 — Reactive | The lack of explainability capabilities means that the AI cannot clarify its decisions or recommendations to human agents. |

#### Gap G-S5-01: Missing AI Participation in Interactions

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The system lacks any artificial agent involvement in recorded human-AI interactions, which is fundamental for collaboration. Without AI participation, the essence of hybrid intelligence is lost, as there can be no joint decision-making or task execution.

**Practical Impact**
> This absence severely undermines the potential for effective teamwork between humans and AI, leading to isolated decision-making and reduced overall system efficacy.

**Recommendation: Integrate AI Agents in Interaction Processes**

Develop and implement AI agents that can participate in human-AI interactions, facilitating joint decision-making and task execution. This integration will enhance collaboration by allowing AI to contribute insights and suggestions in real-time.

*Implementation:* Utilize existing natural language processing and machine learning models to create AI agents that can engage in dialogue with human users, ensuring they can understand context and respond appropriately.

*Priority:* High | *Expected HI Impact:* Enhances collaborative capabilities by enabling shared decision-making between humans and AI.

#### Gap G-S5-02: Lack of Fairness Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system does not incorporate any capabilities related to fairness or bias mitigation, which are essential for responsible AI governance. This gap poses significant risks of discriminatory outcomes, undermining trust and accountability in AI decisions.

**Practical Impact**
> Without fairness mechanisms, the AI system could perpetuate biases, leading to unfair treatment of individuals and eroding user confidence in the technology.

**Recommendation: Implement Fairness and Bias Mitigation Tools**

Incorporate fairness algorithms and bias detection mechanisms into the AI system to ensure equitable outcomes across diverse user groups. This will help in identifying and mitigating potential biases in AI decisions.

*Implementation:* Integrate existing fairness libraries, such as AIF360 or Fairlearn, into the system's decision-making processes to continuously monitor and adjust for fairness metrics.

*Priority:* High | *Expected HI Impact:* Improves responsible AI governance by fostering trust and accountability in AI outputs.

#### Gap G-S5-03: Absence of Explainability Features

| Property | Value |
|----------|-------|
| CARE Dimension | **Explainable** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The lack of explainability capabilities means that the AI cannot clarify its decisions or recommendations to human agents. This absence is critical as it prevents users from understanding the rationale behind AI outputs, which is essential for informed decision-making.

**Practical Impact**
> Without explainability, users may distrust AI outputs, leading to reluctance in collaboration and reduced effectiveness of the human-AI partnership.

**Recommendation: Add Explainability Features to AI Outputs**

Develop and integrate explainability tools that allow the AI to articulate the reasoning behind its decisions and recommendations. This will empower users to understand and trust AI outputs, facilitating better collaboration.

*Implementation:* Utilize explainability frameworks like LIME or SHAP to provide clear, interpretable insights into the AI's decision-making process, ensuring these explanations are accessible during user interactions.

*Priority:* High | *Expected HI Impact:* Enhances explainability, fostering user trust and informed decision-making in human-AI partnerships.

### S6 — S6 — Virtual Assistant Production Quality & Safety Monitoring

**Status:** ❌ FAIL  
**HI Gaps:** 4  

> The scenario fails to meet essential HI conformance requirements, particularly in collaboration and responsibility. Key elements such as human-AI interaction and fairness mechanisms are entirely absent.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The interaction episodes recorded do not involve any artificial agent, indicating a lack of AI participation in collaboration. |
| Adaptive | 1 — Reactive | The feedback mechanism lacks any involvement of human actions, preventing the system from adapting to user needs. |
| Responsible | 1 — Reactive | The system does not incorporate any fairness or bias mitigation capabilities, raising concerns about ethical implications. |
| Explainable | 1 — Reactive | The human-AI team lacks any capability for explainability, which is essential for transparency in decision-making. |

#### Gap G-S6-01: Lack of AI Participation in Interaction

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The interaction episodes recorded do not involve any artificial agent, which is a fundamental requirement for human-AI collaboration. Without AI participation, the system cannot facilitate joint task execution or shared decision-making, undermining the collaborative nature of HI.

**Practical Impact**
> This absence severely limits the potential for effective teamwork between humans and AI, resulting in a system that cannot leverage AI capabilities to enhance human performance.

**Recommendation: Integrate AI Participation in Interaction**

Implement an AI agent that actively engages in user interactions, providing suggestions and taking actions based on user inputs. This will enhance collaboration by allowing the AI to contribute to joint task execution and shared decision-making.

*Implementation:* Utilize existing natural language processing capabilities to develop an AI agent that can analyze user queries and respond with relevant information or actions during interactions. Ensure the AI's role is clearly defined in the interaction flow.

*Priority:* High | *Expected HI Impact:* This change enhances collaborative efforts by enabling effective teamwork between humans and AI.

#### Gap G-S6-02: Missing Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The feedback mechanism lacks any involvement of human actions, which is crucial for adaptive learning in HI systems. Without human input, the AI cannot refine its models or improve its performance based on real-world interactions.

**Practical Impact**
> This gap prevents the system from evolving and adapting to user needs, leading to stagnation in performance and reduced effectiveness over time.

**Recommendation: Implement Human Feedback Mechanism**

Create a feedback loop where users can provide input on AI performance and suggestions for improvement. This will enable the AI to adapt and refine its models based on real-world interactions.

*Implementation:* Integrate a simple feedback interface within the existing system that allows users to rate AI responses and suggest changes. Use this data to retrain the AI models regularly.

*Priority:* High | *Expected HI Impact:* This addition fosters adaptive learning, allowing the AI to evolve according to user needs.

#### Gap G-S6-03: Absence of Explainability Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Explainable** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The human-AI team lacks any capability for explainability, which is essential for transparency in decision-making. Without the ability to explain its decisions, the AI cannot build trust or facilitate informed human actions.

**Practical Impact**
> This lack of explainability can lead to misunderstandings and mistrust in AI recommendations, ultimately hindering effective collaboration and decision-making.

**Recommendation: Develop Explainability Features**

Introduce mechanisms that allow the AI to explain its decisions and recommendations in understandable terms. This will build trust and facilitate informed human actions.

*Implementation:* Leverage existing model interpretability techniques, such as LIME or SHAP, to provide explanations for AI decisions. Integrate these explanations into the user interface where AI recommendations are presented.

*Priority:* High | *Expected HI Impact:* This enhancement improves explainability, fostering transparency and trust in AI decision-making.

#### Gap G-S6-04: No Fairness or Bias Mitigation

| Property | Value |
|----------|-------|
| CARE Dimension | **Responsible** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Responsible |

**Gap Description**
> The system does not incorporate any fairness or bias mitigation capabilities, which are critical for responsible AI deployment. This absence raises concerns about discriminatory outcomes and ethical implications of AI decisions.

**Practical Impact**
> Without fairness mechanisms, the system risks perpetuating biases, which can lead to harmful consequences for users and undermine the integrity of the AI system.

**Recommendation: Incorporate Fairness and Bias Mitigation**

Integrate fairness and bias detection algorithms to assess and mitigate potential biases in AI decisions. This will ensure responsible AI deployment and ethical outcomes.

*Implementation:* Utilize tools like Fairlearn or AIF360 to analyze the AI's decision-making process for bias. Implement corrective measures based on the analysis to ensure equitable outcomes.

*Priority:* High | *Expected HI Impact:* This integration promotes responsible AI usage by addressing fairness and reducing discriminatory outcomes.

### S7 — S7 — Governed AI-Assisted Candidate Screening and Interview Coordination

**Status:** ❌ FAIL  
**HI Gaps:** 3  

> The scenario lacks essential collaborative and adaptive elements, severely impacting its HI conformance. Key interactions and feedback mechanisms are missing, which undermines effective human-AI collaboration.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of AI participation in recorded human-AI interaction episodes prevents any collaborative efforts, limiting the system to a reactive state. |
| Adaptive | 1 — Reactive | The lack of a feedback mechanism for human interactions means the system cannot adapt or learn, confining it to a reactive capability. |
| Responsible | 3 — Social | There is no evidence of gaps in this dimension, allowing for the highest level of maturity to be assigned. |
| Explainable | 2 — Proactive | The system's lack of explainability mechanisms indicates a gap, but the ceiling allows for a proactive level based on the potential for tailored explanations. |

#### Gap G-S7-01: Absence of AI in Interactions

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Collaborative |

**Gap Description**
> The recorded human-AI interaction episodes do not involve any artificial agent, which is a fundamental requirement for HI. This absence prevents any collaborative efforts between humans and AI, rendering the system incapable of fulfilling its intended purpose.

**Practical Impact**
> Without AI participation, the system cannot facilitate joint decision-making or support human agents effectively, leading to a breakdown in collaboration quality.

**Recommendation: Integrate AI Agents in Interaction Episodes**

Implement AI agents that actively participate in candidate screening and interview coordination. This will facilitate collaborative decision-making and enhance the overall interaction quality between human users and the AI system.

*Implementation:* Develop a module that allows AI to engage in dialogues with users, providing suggestions and insights during the screening process. Ensure that the AI can respond to user queries and adapt its recommendations based on real-time interactions.

*Priority:* High | *Expected HI Impact:* Enhances collaboration by enabling joint decision-making between humans and AI.

#### Gap G-S7-02: Lack of Human Feedback Mechanism

| Property | Value |
|----------|-------|
| CARE Dimension | **Adaptive** |
| Severity | 🔴 Critical |
| HI Principle Violated | CARE Adaptive |

**Gap Description**
> The system lacks a feedback mechanism that incorporates human actions, such as input from recruiters or users. This absence means the AI cannot learn or adapt based on human interactions, which is essential for improving performance over time.

**Practical Impact**
> Without human-driven feedback loops, the AI's ability to evolve and reduce cognitive burden on users is severely compromised, leading to stagnation in its effectiveness.

**Recommendation: Establish Human Feedback Loops**

Create a structured feedback mechanism that allows recruiters to provide input on AI recommendations and decisions. This will enable the AI to learn from human interactions and adapt its performance over time.

*Implementation:* Integrate a feedback interface within the existing system where users can rate AI suggestions and provide comments. Use this data to train the AI models, allowing them to evolve based on user input.

*Priority:* High | *Expected HI Impact:* Improves adaptability by enabling the AI to learn from human feedback.

#### Gap G-S7-03: No Explainability Mechanisms

| Property | Value |
|----------|-------|
| CARE Dimension | **Explainable** |
| Severity | 🟠 Major |
| HI Principle Violated | CARE Explainable |

**Gap Description**
> The AI system lacks capabilities to explain its decisions or recommendations to human agents. This gap in explainability hinders users' understanding of AI outputs, which is crucial for trust and accountability in human-AI interactions.

**Practical Impact**
> Without explainability, users may struggle to verify AI outputs, leading to potential misinterpretations and a lack of confidence in the AI's recommendations.

**Recommendation: Implement Explainability Features**

Develop and integrate explainability mechanisms that allow the AI to articulate the reasoning behind its recommendations and decisions. This will enhance user understanding and trust in the AI's outputs.

*Implementation:* Utilize techniques such as feature importance scores or decision trees to provide clear explanations for AI decisions. Ensure these explanations are accessible within the user interface during candidate evaluations.

*Priority:* Medium | *Expected HI Impact:* Enhances explainability, fostering trust and accountability in AI interactions.

### S8 — S8 — Enterprise Model Risk Governance (MRG) Across Multi-Cloud Third-Party Models

**Status:** ❌ FAIL  
**HI Gaps:** 1  

> The scenario fails to meet HI conformance due to the absence of AI participation in interactions, which undermines collaborative efforts. This lack of AI involvement critically impacts the system's ability to function as a hybrid intelligence.

**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):

| Dimension | Level | Rationale |
|-----------|-------|-----------|
| Collaborative | 1 — Reactive | The absence of AI participation in human-AI interactions, as noted in gap G-S8-01, means the system cannot facilitate true collaboration. |
| Adaptive | 1 — Reactive | There is no evidence provided for adaptive capabilities, leading to a conservative classification at the lowest level. |
| Responsible | 1 — Reactive | There is no evidence provided for responsible capabilities, leading to a conservative classification at the lowest level. |
| Explainable | 1 — Reactive | There is no evidence provided for explainable capabilities, leading to a conservative classification at the lowest level. |

#### Gap G-S8-01: Absence of AI in Human-AI Interactions

| Property | Value |
|----------|-------|
| CARE Dimension | **Collaborative** |
| Severity | 🔴 Critical |
| HI Principle Violated | Collaborative |

**Gap Description**
> The recorded human-AI interaction episodes lack any involvement of an Artificial Agent, which is a fundamental requirement for hybrid intelligence. This absence means that the system cannot facilitate true collaboration between humans and AI, rendering it ineffective in its intended purpose.

**Practical Impact**
> Without AI participation, the system fails to leverage the strengths of both human and AI agents, leading to ineffective decision-making and reduced overall performance in model risk governance.

**Recommendation: Integrate AI Agents in Interaction Episodes**

Develop and deploy AI agents that can actively participate in human-AI interaction episodes. This integration will facilitate collaboration, allowing both human and AI strengths to be utilized in model risk governance decisions.

*Implementation:* Utilize existing AI models to create virtual agents that can analyze data and provide insights during human decision-making processes. Ensure these agents are embedded within the interaction framework of the system.

*Priority:* High | *Expected HI Impact:* This change enhances collaboration by enabling effective teamwork between humans and AI, improving decision-making quality.

---

## 4. Consolidated Recommendations

### Collaborative Dimension

- **[High Priority] Integrate AI Agents in Interaction Processes**  
  *Scenario:* S1 — Predictive Model Governance & Continuous Monitoring  
  Modify the interaction framework to include AI agents that can actively participate in dialogues and decision-making processes. This will enhance collaborative efforts by allowing both humans and AI to contribute to task execution, thereby addressing the lack of AI participation.  
  *Implementation:* Utilize existing AI models to create virtual agents that can engage in real-time interactions, and ensure they are integrated into the user interface for seamless collaboration.

- **[High Priority] Integrate AI Agents in Interaction Episodes**  
  *Scenario:* S2 — RAG Application Quality Evaluation & Promotion-to-Production  
  Implement AI agents that actively participate in human-AI interaction episodes to facilitate collaboration. This will enhance the system's ability to assist users in decision-making and task execution, fulfilling the collaborative requirement.  
  *Implementation:* Utilize existing AI models to create virtual agents that can engage with users during interactions, ensuring they can provide suggestions and feedback based on user inputs.

- **[High Priority] Integrate AI Agent for Interaction**  
  *Scenario:* S3 — GenAI Use-Case Approval & Regulatory Risk Classification  
  Develop and integrate an AI agent that actively participates in human-AI interactions. This will enable collaborative decision-making and enhance the hybrid intelligence aspect of the system.  
  *Implementation:* Utilize existing AI models to create an interactive agent that can engage in dialogues, provide suggestions, and assist in decision-making processes. Ensure it is embedded within the current interaction framework.

- **[High Priority] Implement Explainability Interfaces for AI Decisions**  
  *Scenario:* S4 — Prompt Security Hardening via Automated Red-Teaming  
  Develop and integrate an explainability module that provides human agents with clear, understandable rationales for the AI's decisions. This will enhance trust and facilitate better collaboration by allowing users to comprehend the reasoning behind AI recommendations.  
  *Implementation:* Utilize existing explainable AI frameworks, such as LIME or SHAP, to generate decision explanations and present them through a user-friendly interface in the existing application. Ensure that the explanations are contextually relevant to the tasks at hand.

- **[High Priority] Integrate AI Agents in Interaction Processes**  
  *Scenario:* S5 — Multi-Agent (Agentic AI) Governance Across the Lifecycle  
  Develop and implement AI agents that can participate in human-AI interactions, facilitating joint decision-making and task execution. This integration will enhance collaboration by allowing AI to contribute insights and suggestions in real-time.  
  *Implementation:* Utilize existing natural language processing and machine learning models to create AI agents that can engage in dialogue with human users, ensuring they can understand context and respond appropriately.

- **[High Priority] Integrate AI Participation in Interaction**  
  *Scenario:* S6 — Virtual Assistant Production Quality & Safety Monitoring  
  Implement an AI agent that actively engages in user interactions, providing suggestions and taking actions based on user inputs. This will enhance collaboration by allowing the AI to contribute to joint task execution and shared decision-making.  
  *Implementation:* Utilize existing natural language processing capabilities to develop an AI agent that can analyze user queries and respond with relevant information or actions during interactions. Ensure the AI's role is clearly defined in the interaction flow.

- **[High Priority] Integrate AI Agents in Interaction Episodes**  
  *Scenario:* S7 — Governed AI-Assisted Candidate Screening and Interview Coordination  
  Implement AI agents that actively participate in candidate screening and interview coordination. This will facilitate collaborative decision-making and enhance the overall interaction quality between human users and the AI system.  
  *Implementation:* Develop a module that allows AI to engage in dialogues with users, providing suggestions and insights during the screening process. Ensure that the AI can respond to user queries and adapt its recommendations based on real-time interactions.

- **[High Priority] Integrate AI Agents in Interaction Episodes**  
  *Scenario:* S8 — Enterprise Model Risk Governance (MRG) Across Multi-Cloud Third-Party Models  
  Develop and deploy AI agents that can actively participate in human-AI interaction episodes. This integration will facilitate collaboration, allowing both human and AI strengths to be utilized in model risk governance decisions.  
  *Implementation:* Utilize existing AI models to create virtual agents that can analyze data and provide insights during human decision-making processes. Ensure these agents are embedded within the interaction framework of the system.

### Adaptive Dimension

- **[High Priority] Implement Human Feedback Collection Mechanism**  
  *Scenario:* S1 — Predictive Model Governance & Continuous Monitoring  
  Develop a structured feedback system where users can provide input on AI decisions and outputs. This will allow the model to learn from human interactions, fostering adaptability and continuous improvement.  
  *Implementation:* Incorporate feedback buttons or prompts in the user interface that allow users to rate AI suggestions and provide comments, which can then be used to retrain the model periodically.

- **[High Priority] Establish Human Feedback Loop Mechanism**  
  *Scenario:* S2 — RAG Application Quality Evaluation & Promotion-to-Production  
  Develop a feedback mechanism that captures human actions and decisions during the evaluation process to inform adaptive learning. This will allow the system to evolve based on user interactions and preferences.  
  *Implementation:* Integrate a user interface element that prompts users to provide feedback after interactions, and use this data to adjust model parameters and improve performance over time.

- **[High Priority] Implement Human Feedback Mechanism**  
  *Scenario:* S6 — Virtual Assistant Production Quality & Safety Monitoring  
  Create a feedback loop where users can provide input on AI performance and suggestions for improvement. This will enable the AI to adapt and refine its models based on real-world interactions.  
  *Implementation:* Integrate a simple feedback interface within the existing system that allows users to rate AI responses and suggest changes. Use this data to retrain the AI models regularly.

- **[High Priority] Establish Human Feedback Loops**  
  *Scenario:* S7 — Governed AI-Assisted Candidate Screening and Interview Coordination  
  Create a structured feedback mechanism that allows recruiters to provide input on AI recommendations and decisions. This will enable the AI to learn from human interactions and adapt its performance over time.  
  *Implementation:* Integrate a feedback interface within the existing system where users can rate AI suggestions and provide comments. Use this data to train the AI models, allowing them to evolve based on user input.

### Responsible Dimension

- **[High Priority] Implement Fairness and Bias Mitigation Tools**  
  *Scenario:* S2 — RAG Application Quality Evaluation & Promotion-to-Production  
  Incorporate fairness assessment tools and bias mitigation techniques into the system to ensure responsible AI design. This will help prevent discriminatory outcomes and build trust with users.  
  *Implementation:* Utilize existing libraries and frameworks for fairness analysis and integrate them into the decision-making processes of the AI system, allowing for real-time bias checks.

- **[High Priority] Implement Fairness and Bias Mitigation Tools**  
  *Scenario:* S3 — GenAI Use-Case Approval & Regulatory Risk Classification  
  Incorporate fairness algorithms and bias detection mechanisms into the decision-making process of the AI system. This will ensure that outputs are equitable and reduce the risk of discriminatory practices.  
  *Implementation:* Select and integrate established fairness libraries or frameworks that can analyze and adjust AI outputs for bias. Conduct regular audits to monitor fairness metrics.

- **[High Priority] Integrate Fairness Auditing Tools**  
  *Scenario:* S4 — Prompt Security Hardening via Automated Red-Teaming  
  Incorporate fairness auditing tools into the AI system to assess and mitigate biases in decision-making processes. This will ensure that the AI operates responsibly and does not lead to discriminatory outcomes.  
  *Implementation:* Select and integrate fairness assessment libraries, such as AI Fairness 360 or Fairlearn, into the model evaluation pipeline. Regularly audit the AI's outputs for fairness metrics and adjust the training data or algorithms accordingly to address identified biases.

- **[High Priority] Implement Fairness and Bias Mitigation Tools**  
  *Scenario:* S5 — Multi-Agent (Agentic AI) Governance Across the Lifecycle  
  Incorporate fairness algorithms and bias detection mechanisms into the AI system to ensure equitable outcomes across diverse user groups. This will help in identifying and mitigating potential biases in AI decisions.  
  *Implementation:* Integrate existing fairness libraries, such as AIF360 or Fairlearn, into the system's decision-making processes to continuously monitor and adjust for fairness metrics.

- **[High Priority] Incorporate Fairness and Bias Mitigation**  
  *Scenario:* S6 — Virtual Assistant Production Quality & Safety Monitoring  
  Integrate fairness and bias detection algorithms to assess and mitigate potential biases in AI decisions. This will ensure responsible AI deployment and ethical outcomes.  
  *Implementation:* Utilize tools like Fairlearn or AIF360 to analyze the AI's decision-making process for bias. Implement corrective measures based on the analysis to ensure equitable outcomes.

### Explainable Dimension

- **[High Priority] Add Explainability Features to AI Outputs**  
  *Scenario:* S3 — GenAI Use-Case Approval & Regulatory Risk Classification  
  Develop and implement explainability mechanisms that allow the AI to articulate its decision-making process and reasoning. This will build trust and understanding in human-AI interactions.  
  *Implementation:* Utilize explainable AI frameworks to generate interpretable outputs and visualizations that clarify the AI's reasoning. Ensure these features are integrated into the user interface for easy access.

- **[High Priority] Add Explainability Features to AI Outputs**  
  *Scenario:* S5 — Multi-Agent (Agentic AI) Governance Across the Lifecycle  
  Develop and integrate explainability tools that allow the AI to articulate the reasoning behind its decisions and recommendations. This will empower users to understand and trust AI outputs, facilitating better collaboration.  
  *Implementation:* Utilize explainability frameworks like LIME or SHAP to provide clear, interpretable insights into the AI's decision-making process, ensuring these explanations are accessible during user interactions.

- **[High Priority] Develop Explainability Features**  
  *Scenario:* S6 — Virtual Assistant Production Quality & Safety Monitoring  
  Introduce mechanisms that allow the AI to explain its decisions and recommendations in understandable terms. This will build trust and facilitate informed human actions.  
  *Implementation:* Leverage existing model interpretability techniques, such as LIME or SHAP, to provide explanations for AI decisions. Integrate these explanations into the user interface where AI recommendations are presented.

- **[Medium Priority] Implement Explainability Features**  
  *Scenario:* S7 — Governed AI-Assisted Candidate Screening and Interview Coordination  
  Develop and integrate explainability mechanisms that allow the AI to articulate the reasoning behind its recommendations and decisions. This will enhance user understanding and trust in the AI's outputs.  
  *Implementation:* Utilize techniques such as feature importance scores or decision trees to provide clear explanations for AI decisions. Ensure these explanations are accessible within the user interface during candidate evaluations.

---

## 5. HI Maturity Assessment

**Maturity Level: Level 0: Pre-HI**

The system does not meaningfully embody Hybrid Intelligence principles. Fundamental changes to the human-AI collaboration model are required.

| CARE Dimension | Score | Status |
|----------------|-------|--------|
| Collaborative | 0% | Needs Work |
| Adaptive | 50% | Needs Work |
| Responsible | 38% | Needs Work |
| Explainable | 50% | Needs Work |

### Strengths

- No dimension achieved full conformance in this assessment.

### Areas for Improvement

- **Collaborative** (0%): See recommendations in Section 4.
- **Adaptive** (50%): See recommendations in Section 4.
- **Responsible** (38%): See recommendations in Section 4.
- **Explainable** (50%): See recommendations in Section 4.

---

## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)

This section complements the score-based maturity level in Section 5 with a finer-grained, literature-grounded assessment of *how* each CARE dimension is demonstrated, adapted from the CARE capability-level tables (Hybrid Intelligence Centre Netherlands, 2023; cf. Akata et al. 2020; Zamprogno, Tiddi & Verheij 2025). Each scenario is classified per CARE dimension into one of three levels: **1 — Reactive** (the capability is only exercised upon explicit human instruction), **2 — Proactive** (the AI initiates or anticipates without being explicitly prompted), or **3 — Social** (the capability is sustained, repaired, or co-constructed over time with the human partner). The maximum level admissible for a dimension in a given scenario is capped by the most severe HI gap identified in that dimension in Phase 5 (Critical → capped at 1, Major → capped at 2, Minor/none → uncapped at 3), so the classification stays grounded in the symbolic SHACL evidence rather than unconstrained LLM judgement. This is distinct from the conformance score in Section 2.2, which measures whether a capability is present at all, not how maturely it is exercised.

### 6.1 Per-Scenario CARE Levels

| Scenario | Collaborative | Adaptive | Responsible | Explainable |
|----------|----------------|----------|--------------|-------------|
| S1 — S1 — Predictive Model Governance &  | 1 (Reactive) | 1 (Reactive) | 3 (Social) | 3 (Social) |
| S2 — S2 — RAG Application Quality Evalua | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 3 (Social) |
| S3 — S3 — GenAI Use-Case Approval & Regu | 1 (Reactive) | 2 (Proactive) | 1 (Reactive) | 1 (Reactive) |
| S4 — S4 — Prompt Security Hardening via  | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S5 — S5 — Multi-Agent (Agentic AI) Gover | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S6 — S6 — Virtual Assistant Production Q | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |
| S7 — S7 — Governed AI-Assisted Candidate | 1 (Reactive) | 1 (Reactive) | 3 (Social) | 2 (Proactive) |
| S8 — S8 — Enterprise Model Risk Governan | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) | 1 (Reactive) |

### 6.2 Use-Case CARE Maturity Summary

Levels are an ordinal scale (Reactive < Proactive < Social), so the table below reports the distribution and the modal (most frequent) level per dimension across all scenarios rather than an average.

| Dimension | Level 1 (Reactive) | Level 2 (Proactive) | Level 3 (Social) | Modal Level |
|-----------|---------------------|----------------------|--------------------|-------------|
| Collaborative | 8 | 0 | 0 | **1 — Reactive** |
| Adaptive | 7 | 1 | 0 | **1 — Reactive** |
| Responsible | 6 | 0 | 2 | **1 — Reactive** |
| Explainable | 5 | 1 | 2 | **1 — Reactive** |

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