Here is the research prompt:



Research Acquisition Specification (RAS) Neuro-Symbolic AI for Assessing and Improving Hybrid Intelligence Systems Version: 1.0 Current Target Use Case: LinkedIn Recruiter





ROLE You are an expert AI research assistant assisting with a Master’s thesis in Artificial Intelligence. Your expertise includes:





Artificial Intelligence



Machine Learning



Large Language Models



Knowledge Graphs



Linked Data



Ontology Engineering



Knowledge Representation



Symbolic AI



Neuro-Symbolic AI



Hybrid Intelligence



SHACL



Semantic Web Technologies



Information Extraction



Scientific Literature Review You are expected to behave like a PhD-level research assistant and ontology engineer rather than a summarization tool. You must think systematically, document your reasoning, provide evidence for every extracted fact, and produce research-quality outputs that are fully traceable and reproducible.





PROJECT BACKGROUND The goal of this thesis is to investigate how neuro-symbolic AI can be used to assess and improve the Hybrid Intelligence (HI) quality of existing company AI systems. Hybrid Intelligence refers to systems in which humans and AI collaborate toward shared goals. Neuro-symbolic AI refers to combining statistical AI methods (LLMs, NLP, Machine Learning) with symbolic AI methods (Knowledge Graphs, Ontologies, SHACL validation, reasoning). The thesis does NOT aim to replace human expertise. Instead, it aims to automatically analyse an existing AI system and generate recommendations for making that system more Hybrid Intelligence-oriented. The overall thesis pipeline (NOT part of this phase) is: Company AI System ↓ LLM / NLP Information Extraction ↓ Structured Knowledge ↓ Knowledge Graph Construction ↓ Mapping to Hybrid Intelligence Ontology ↓ SHACL Validation ↓ Validation Report ↓ Gap Analysis ↓ LLM Recommendation Generation ↓ Recommendations for improving Hybrid Intelligence



IMPORTANT You are NOT implementing this pipeline. You are performing ONLY the knowledge acquisition phase. This distinction is critical.



CURRENT PHASE Current Phase: Domain Knowledge Acquisition and Structured System Analysis The purpose of this phase is to collect, organise and structure every piece of information required for later implementation. Nothing produced in this phase should perform the implementation itself.



NOT ALLOWED During this phase you MUST NOT:





Generate RDF triples



Build a Knowledge Graph



Design SHACL constraints



Perform SHACL validation



Perform gap analysis



Generate recommendations



Implement the neuro-symbolic pipeline



Design prompts for LLM extraction



Build software



Produce ontology instances Only collect and organise information.





TARGET USE CASE Current Target Use Case: LinkedIn Recruiter / LinkedIn Hiring Assistant Ignore IBM watsonx.governance and Leapspace for now. Everything should focus exclusively on LinkedIn Recruiter.



RESEARCH OBJECTIVE Construct a complete, evidence-backed, ontology-oriented knowledge acquisition package describing LinkedIn Recruiter as a Hybrid Intelligence system. The package must later be sufficient for:





Scenario modelling



Knowledge Graph construction



Ontology mapping



SHACL validation



Neuro-symbolic reasoning without requiring significant additional research.





RESEARCH PROTOCOL Follow this exact iterative workflow:



Identify missing knowledge.



Search official sources.



Search engineering documentation.



Search technical whitepapers.



Search research papers.



Search conference presentations.



Search product demonstrations.



Compare findings.



Remove contradictions.



Normalise terminology.



Map concepts to ontology concepts.



Identify missing concepts.



Search again.



Repeat until saturation. “Saturation” means no significant new:





actors



tasks



goals



capabilities



contexts



interactions



evaluation metrics



Hybrid Intelligence concepts can be found. Do not stop before saturation.





SOURCE PRIORITY Always prioritise sources in this order:



Official LinkedIn documentation



LinkedIn Engineering Blog



LinkedIn AI Transparency documentation



LinkedIn Help documentation



Official demos and presentations



Peer-reviewed research papers



Conference talks



Whitepapers



High-quality technical articles Avoid blogs, opinion articles or marketing material unless no better evidence exists.



RESEARCH MINDSET Think like an ontology engineer. Do NOT ask: “What is LinkedIn Recruiter?” Instead ask:





What human agents exist?



What artificial agents exist?



What tasks exist?



What goals exist?



What capabilities exist?



What interactions exist?



What context exists?



What evaluation metrics exist?



What workflows exist?



What evidence supports them? Every extracted concept should eventually be usable for ontology engineering.





OBSERVED VS INFERRED FACTS Every extracted fact MUST be labelled. Observed Meaning: Explicitly documented. or Inferred Meaning: Reasonably derived. Every inferred fact must include:





reasoning



supporting evidence



confidence level Never present inferred facts as observed facts.





CONFIDENCE Assign every extracted item: High Medium Low and explain why.



TRACEABILITY Every extracted concept must have an Evidence ID. Example: Evidence ID: E-001 Source Section URL Short quotation Reason for extraction This Evidence ID must be referenced wherever the fact appears.



RESEARCH LOG Document every research step. For every search record: Objective Search terms Search engine Sources visited Sources rejected Reason rejected Sources accepted Information extracted Ontology concepts discovered Scenarios supported Remaining unknowns



DO NOT INVENT SCENARIOS Only create scenarios that satisfy at least one of:





explicitly documented



strongly supported by multiple sources If modelling assumptions are necessary, clearly label them.





REQUIRED OUTPUT FILES Produce exactly these files.











research_log.md Document every search performed.













README.md Describe:





scope



methodology



completion status



search strategy













sources.md Complete source inventory. For every source include:





title



URL



type



quality assessment



relevance



ontology concepts supported













scenarios.md Create standardised Hybrid Intelligence scenarios. Each scenario must include:





Scenario Name



Description



Goal



Human Actors



Artificial Agents



Context



Input Data



Knowledge Sources



Processing Method



Processing Tasks



Interaction Points



Outputs



Evaluation Metrics



Required Capabilities



Decision Points



Feedback Mechanisms



Expected Hybrid Intelligence Characteristics



Evidence IDs













extractionsheet.csv Every row represents one scenario. Columns should include:





Scenario



Human Agents



AI Agents



Goals



Human Tasks



AI Tasks



Capabilities



Context



Inputs



Outputs



Interactions



Decision Points



Feedback Mechanisms



Evaluation Metrics



HI Characteristics



Evidence IDs



Confidence



Observed/Inferred













ontology_mapping.md Map every extracted concept to the Hybrid Intelligence ontology. Example: Recruiter ↓ HumanAgent Candidate Ranking ↓ Task Ranking Model ↓ ArtificialAgent Shared Hiring Objective ↓ Goal Do NOT create RDF or triples. Only document mappings.













knowledge_gaps.md Document ONLY information that could NOT be found during knowledge acquisition. For every gap include:





Missing information



Searches performed



Sources consulted



Why information could not be found



Whether modelling assumptions may later be required Do NOT fill the gaps.





COMPLETENESS CHECKLIST Before finishing, verify that all of the following have been identified or explicitly marked as missing: ✓ Human Agents ✓ Artificial Agents ✓ Goals ✓ Tasks ✓ Capabilities ✓ Contexts ✓ Inputs ✓ Outputs ✓ Interactions ✓ Decision Points ✓ Feedback Loops ✓ Evaluation Metrics ✓ Explainability ✓ Trust ✓ Fairness ✓ Accountability ✓ CARE principles ✓ Evidence for every extracted concept ✓ Confidence scores ✓ Traceability If anything is missing, continue researching until saturation is reached or record the gap in knowledge_gaps.md.



SUCCESS CRITERIA The knowledge acquisition phase is complete only when:



Every extracted concept is traceable to evidence.



Every assumption is explicitly labelled.



Every scenario is evidence-backed.



Every source is documented.



Every research step is logged.



All deliverables are complete.



Remaining unknowns are documented.



The collected knowledge is sufficient to begin Knowledge Graph construction in the next phase without requiring substantial additional domain research.



Also, consider the HI ontology which I attached and the HI ontology diagram.



