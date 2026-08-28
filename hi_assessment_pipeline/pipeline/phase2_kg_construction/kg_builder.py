#!/usr/bin/env python3
"""
Neuro-Symbolic HI Assessment Pipeline Phase 2: KG Construction
kg_builder.py: Knowledge Graph Builder

In this file, I import the extraction sheet generated in phase 1 and then it generates an RDF
Knowledge Graph (ABox) aligned to the HI Ontology (hi: / hint: namespaces)

To run this file here is the following info:
Specify the CSV path explicitly:
    python kg_builder.py --usecase linkedin --input use_cases/linkedin/extractionsheet.csv
    python kg_builder.py --usecase ibm      --input use_cases/ibm/IBM_extractionsheet.csv

Or let the script resolve the default path:
    python kg_builder.py --usecase linkedin 

Output:
    use_cases/{usecase}/kg_output/{usecase}_kg.ttl
    use_cases/{usecase}/kg_output/{usecase}_kg_report.txt

The generated kg is divided into the two layers TBox and Abox
Ontology alignment:
    TBox : https://w3id.org/hi-ontology#  (HI Ontology v2.0.0)
    ABox : http://example.org/hi/{usecase}/{ClassName}/{slug}
    The output declares owl:imports on the TBox do NOT load the TBox .ttl
    into the same graph; keep TBox and ABox separate.

Key ontology facts used in this script (from HI Ontology v2.0.0):
    hi:hasHITeam          UseCase     --> HITeam
    hi:hasMember          HITeam      --> Agent (Human | Artificial)
    hi:hasGoal            HITeam      --> Goal
    hi:requiresTask       Goal        --> Task
    hi:hasCapability      Agent       --> Capability
    hi:allowsTask         Capability  --> Task
    hi:requiresCapability Task        --> Capability   (inverse; OWL restriction ≥1)
    hi:isAssignedToTask   Agent       --> Task
    hi:operatesInContext  Agent       --> Context
    hi:hasInfluenceOn     Context     --> HITeam
    hi:isInfluencedBy     HITeam      --> Context      (inverse)
    hi:performsExecution  Agent       --> TaskExecution
    hi:performedBy        TaskExecution --> Agent      (inverse)
    hi:realizesTask       TaskExecution --> Task
    hi:realizedBy         Task        --> TaskExecution (inverse)
    hi:towardsGoal        TaskExecution --> Goal
    hi:hasInteractionEpisode TaskExecution --> Interaction
    hi:hasAgentInvolved   Interaction --> Agent        (OWL restriction ≥2)
    hi:evaluatedBy        TaskExecution --> Evaluation
    hi:hasMetricConcept   Evaluation  --> skos:Concept
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, OWL, XSD
from rdflib.namespace import SKOS

# Namespaces

HI   = Namespace("https://w3id.org/hi-ontology#")
HINT = Namespace("https://w3id.org/hi-thesaurus#")
META = Namespace("http://example.org/hi/meta/")
BASE_URI = "http://example.org/hi/"


# Utility functions: My coding was not too organized, I kept rewriting code that could be reused, LLM advised cleaning and adding such code
# into the following utility functions 

def slugify(text: str) -> str:
    """Convert free text to a URI-safe lowercase slug.

    Removes parenthesised qualifiers such as '(secondary)' and '(GBDT/GLMix)'
    before normalising so that 'Hiring Manager (secondary)' and
    'Hiring Manager (optional)' both map to 'hiring_manager'
    """
    text = str(text).strip()
    text = re.sub(r'\(.*?\)', '', text)          # drop (...) qualifiers
    text = text.lower().strip()
    text = re.sub(r'[^\w\s\-]', ' ', text)       # punctuation --> space
    text = re.sub(r'[\s\-]+', '_', text)          # whitespace/hyphens --> _
    return text.strip('_')

# instead of splitting every time, I call to split the csv once using this function
def split_semi(value: str) -> List[str]:
    if not value or not value.strip():
        return []
    return [v.strip() for v in value.split(';') if v.strip()]


def make_uri(usecase: str, cls: str, identifier: str) -> URIRef:
    """
       http://example.org/hi/{usecase}/{cls}/{slug}
    """
    return URIRef(f"{BASE_URI}{usecase}/{cls}/{slugify(identifier)}")


def scenario_id(scenario_str: str) -> str:
    """Extract the scenario ID slug from a cell like 'S1  AI-Assisted Sourcing'
    Returns 's1', 's2', etc
    """
    m = re.match(r'^(S\d+)', scenario_str.strip(), re.IGNORECASE)
    return m.group(1).lower() if m else slugify(scenario_str)[:16]



# KGBuilder class

class KGBuilder:
    """
    Builds an RDF ABox for one use case from its extraction sheet CSV

    Summary of some design decisions built
    - Agents and capabilities duplicates are removed across all scenarios
    - Tasks and interactions are scoped per scenario (they may have the same
      surface text but represent distinct executions in different scenarios)
    - Capabilities are linked to AI agents via hi:hasCapability and to AI tasks
      via hi:allowsTask / hi:requiresCapability (OWL restriction ≥1 satisfied)
    - Human tasks are linked to the first available capability to satisfy the
      hi:Task OWL restriction (≥1 hi:requiresCapability)
    - Interactions are parsed from free text using '<-->' and '-->' separators
      Agent names in interaction text are matched against the scenario's agent
      pool using slug-containment (fuzzy) matching to handle abbreviated names
    - The Interaction OWL restriction (≥2 hi:hasAgentInvolved) is enforced with
      a fallback: if fewer than 2 agents are resolved, a fallback agent is added
    """

    # Default CSV discovery paths per use case (used when --input is omitted)
    DEFAULT_INPUTS: Dict[str, List[str]] = {
        'linkedin':  ['use_cases/linkedin/extractionsheet.csv'],
        'ibm':       ['use_cases/ibm/extractionsheet.csv'],
        'leapspace': ['use_cases/leapspace/extractionsheet.csv'],
        # more can be added later
    }

    def __init__(self, usecase: str):
        self.usecase = usecase

        # RDF graph (ABox only TBox is declared via owl:imports)
        self.g = Graph()
        self.g.bind('hi',   HI)
        self.g.bind('hint', HINT)
        self.g.bind('meta', META)
        self.g.bind('skos', SKOS)
        self.g.bind('rdfs', RDFS)
        self.g.bind('owl',  OWL)
        self.g.bind('xsd',  XSD)

        # I declare this ABox as an OWL ontology that imports the HI TBox
        kg_base = URIRef(f"{BASE_URI}{usecase}/kg")
        self.g.add((kg_base, RDF.type, OWL.Ontology))
        self.g.add((kg_base, OWL.imports, URIRef("https://w3id.org/hi-ontology#")))
        self.g.add((kg_base, RDFS.label,
                    Literal(f"HI Knowledge Graph: {usecase.title()}", lang='en')))
        self.g.add((kg_base, RDFS.comment,
                    Literal(
                        f"ABox for the '{usecase}' use case, generated by kg_builder.py "
                        "from the Phase 1 extraction sheet "
                        "TBox imported from the HI Ontology (https://w3id.org/hi-ontology#)",
                        lang='en'
                    )))

        # Deduplication registries (name --> URI)
        self._human_agents: Dict[str, URIRef] = {}
        self._ai_agents:    Dict[str, URIRef] = {}
        self._capabilities: Dict[str, URIRef] = {}
        self._metrics:      Dict[str, URIRef] = {}

        # Statistics dict
        self.stats: Dict[str, int] = {
            'usecases':     0,
            'hiteams':      0,
            'human_agents': 0,
            'ai_agents':    0,
            'goals':        0,
            'human_tasks':  0,
            'ai_tasks':     0,
            'capabilities': 0,
            'contexts':     0,
            'interactions': 0,
            'evaluations':  0,
            'metrics':      0,
        }

    # some helpers

    def _uri(self, cls: str, identifier: str) -> URIRef:
        return make_uri(self.usecase, cls, identifier)

    def _get_or_create(self,
                       registry: Dict[str, URIRef],
                       rdf_type: URIRef,
                       cls: str,
                       name: str,
                       stat_key: str) -> URIRef:
        """Return an existing URI or create a new deduplicated instance"""
        if name not in registry:
            uri = self._uri(cls, name)
            self.g.add((uri, RDF.type, rdf_type))
            self.g.add((uri, RDFS.label, Literal(name, lang='en')))
            registry[name] = uri
            self.stats[stat_key] += 1
        return registry[name]

    def _human_agent(self, name: str) -> URIRef:
        return self._get_or_create(
            self._human_agents, HI.HumanAgent, 'HumanAgent', name, 'human_agents')

    def _ai_agent(self, name: str) -> URIRef:
        return self._get_or_create(
            self._ai_agents, HI.ArtificialAgent, 'ArtificialAgent', name, 'ai_agents')

    def _capability(self, name: str) -> URIRef:
        return self._get_or_create(
            self._capabilities, HI.Capability, 'Capability', name, 'capabilities')

    def _metric_concept(self, name: str) -> URIRef:
        """Metrics are SKOS concepts (hint:Metric), not OWL instances"""
        if name not in self._metrics:
            uri = self._uri('Metric', name)
            self.g.add((uri, RDF.type, SKOS.Concept))
            self.g.add((uri, SKOS.prefLabel, Literal(name, lang='en')))
            self._metrics[name] = uri
            self.stats['metrics'] += 1
        return self._metrics[name]

    def _resolve_agent(self,
                       name: str,
                       agent_pool: Dict[str, URIRef]) -> Optional[URIRef]:
        """
        Fuzzy-match an agent name extracted from interaction text against the
        scenario's registered agents
        Tries in order:
          1. Exact name match
          2. Slug-containment match  (handles abbreviated names like
             'Hiring Assistant' matching 'Hiring Assistant (supervisor)',
             or 'LiFT' matching 'LinkedIn Fairness Toolkit (LiFT)')
        """
        if name in agent_pool:
            return agent_pool[name]
        q = slugify(name)
        if not q:
            return None
        for agent_name, uri in agent_pool.items():
            s = slugify(agent_name)
            if q in s or s in q:
                return uri
        return None

    def _add_provenance(self, subject: URIRef, row: dict, fields: List[tuple]):
        """Add provenance/annotation triples from selected CSV fields"""
        for field_name, prop in fields:
            val = row.get(field_name, '').strip()
            if val:
                self.g.add((subject, prop, Literal(val, lang='en')))

    # Row processing
    def process_row(self, row: dict):
        """Build all RDF triples for one scenario row from the CSV"""
        scenario_str = row.get('Scenario', '').strip()
        if not scenario_str:
            return

        sc = scenario_id(scenario_str)
        print(f"\n  [{sc.upper()}] {scenario_str}")

        # UseCase
        uc_uri = self._uri('UseCase', sc)
        self.g.add((uc_uri, RDF.type, HI.UseCase))
        self.g.add((uc_uri, RDFS.label, Literal(scenario_str, lang='en')))
        self._add_provenance(uc_uri, row, [
            ('Evidence IDs',     META.evidenceIDs),
            ('Confidence',       META.confidence),
            ('Observed/Inferred', META.observedInferred),
        ])
        self.stats['usecases'] += 1

        # HITeam
        team_uri = self._uri('HITeam', f"{sc}_team")
        self.g.add((team_uri, RDF.type, HI.HITeam))
        self.g.add((team_uri, RDFS.label,
                    Literal(f"{scenario_str} - HI Team", lang='en')))
        self.g.add((uc_uri, HI.hasHITeam, team_uri))  # correct property (not introducesHITeam)
        hi_char = row.get('HI Characteristics', '').strip()
        if hi_char:
            self.g.add((team_uri, META.careCharacteristics, Literal(hi_char, lang='en')))
        self.stats['hiteams'] += 1

        # Context
        ctx_text = row.get('Context', '').strip()
        ctx_uri = self._uri('Context', f"{sc}_context")
        self.g.add((ctx_uri, RDF.type, HI.Context))
        self.g.add((ctx_uri, RDFS.label, Literal(f"{sc} operational context", lang='en')))
        if ctx_text:
            self.g.add((ctx_uri, RDFS.comment, Literal(ctx_text, lang='en')))
        # Context <--> HITeam
        self.g.add((ctx_uri, HI.hasInfluenceOn, team_uri))
        self.g.add((team_uri, HI.isInfluencedBy, ctx_uri))
        self.stats['contexts'] += 1

        # Human Agents
        human_agents: Dict[str, URIRef] = {}
        for name in split_semi(row.get('Human Agents', '')):
            uri = self._human_agent(name)
            self.g.add((team_uri, HI.hasMember, uri))
            self.g.add((uri, HI.operatesInContext, ctx_uri))
            human_agents[name] = uri

        # AI Agents
        ai_agents: Dict[str, URIRef] = {}
        for name in split_semi(row.get('AI Agents', '')):
            uri = self._ai_agent(name)
            self.g.add((team_uri, HI.hasMember, uri))
            self.g.add((uri, HI.operatesInContext, ctx_uri))
            ai_agents[name] = uri

        all_agents = {**human_agents, **ai_agents}

        # Goal
        goal_text = row.get('Goals', '').strip()
        goal_uri = self._uri('Goal', f"{sc}_goal")
        self.g.add((goal_uri, RDF.type, HI.Goal))
        label = (goal_text[:120] + '…') if len(goal_text) > 120 else goal_text
        self.g.add((goal_uri, RDFS.label, Literal(label or f"{sc} goal", lang='en')))
        if goal_text:
            self.g.add((goal_uri, RDFS.comment, Literal(goal_text, lang='en')))
        self.g.add((team_uri, HI.hasGoal, goal_uri))
        self.stats['goals'] += 1

        # Capabilities
        cap_names = split_semi(row.get('Capabilities', ''))
        cap_uris: List[URIRef] = []
        for cap_name in cap_names:
            cap_uri = self._capability(cap_name)
            cap_uris.append(cap_uri)
            # Assign each capability to every AI agent in this scenario
            for agent_uri in ai_agents.values():
                self.g.add((agent_uri, HI.hasCapability, cap_uri))

        # Human Tasks
        human_tasks: List[URIRef] = []
        for i, task_text in enumerate(split_semi(row.get('Human Tasks', ''))):
            t_uri = self._uri('Task', f"{sc}_ht{i+1:02d}")
            self.g.add((t_uri, RDF.type, HI.Task))
            label = (task_text[:120] + '…') if len(task_text) > 120 else task_text
            self.g.add((t_uri, RDFS.label, Literal(label, lang='en')))
            self.g.add((t_uri, RDFS.comment, Literal(task_text, lang='en')))
            self.g.add((t_uri, META.taskType, Literal('human')))
            # Goal → Task
            self.g.add((goal_uri, HI.requiresTask, t_uri))
            # Human agents assigned to this task
            for agent_uri in human_agents.values():
                self.g.add((agent_uri, HI.isAssignedToTask, t_uri))
            # OWL restriction: hi:Task must have ≥1 hi:requiresCapability
            # Use the first scenario capability as a satisfying minimum
            if cap_uris:
                self.g.add((t_uri, HI.requiresCapability, cap_uris[0]))
            human_tasks.append(t_uri)
            self.stats['human_tasks'] += 1

        # AI Tasks
        ai_tasks: List[URIRef] = []
        for i, task_text in enumerate(split_semi(row.get('AI Tasks', ''))):
            t_uri = self._uri('Task', f"{sc}_at{i+1:02d}")
            self.g.add((t_uri, RDF.type, HI.Task))
            label = (task_text[:120] + '…') if len(task_text) > 120 else task_text
            self.g.add((t_uri, RDFS.label, Literal(label, lang='en')))
            self.g.add((t_uri, RDFS.comment, Literal(task_text, lang='en')))
            self.g.add((t_uri, META.taskType, Literal('artificial')))
            # Goal ---> Task
            self.g.add((goal_uri, HI.requiresTask, t_uri))
            # AI agents assigned to this task
            for agent_uri in ai_agents.values():
                self.g.add((agent_uri, HI.isAssignedToTask, t_uri))
            # Linking capability to task: index match where possible, else fallback to first
            cap = (cap_uris[i] if i < len(cap_uris)
                   else cap_uris[0] if cap_uris
                   else None)
            if cap:
                self.g.add((t_uri, HI.requiresCapability, cap))
                self.g.add((cap, HI.allowsTask, t_uri))
            ai_tasks.append(t_uri)
            self.stats['ai_tasks'] += 1

        all_tasks = human_tasks + ai_tasks

        # TaskExecution
        te_uri = self._uri('TaskExecution', f"{sc}_execution")
        self.g.add((te_uri, RDF.type, HI.TaskExecution))
        self.g.add((te_uri, RDFS.label,
                    Literal(f"{scenario_str} - Task Execution", lang='en')))
        self.g.add((te_uri, HI.towardsGoal, goal_uri))

        for agent_uri in all_agents.values():
            self.g.add((agent_uri, HI.performsExecution, te_uri))
            self.g.add((te_uri, HI.performedBy, agent_uri))
        for t_uri in all_tasks:
            self.g.add((te_uri, HI.realizesTask, t_uri))
            self.g.add((t_uri, HI.realizedBy, te_uri))

        # Inputs / Outputs as provenance annotations
        self._add_provenance(te_uri, row, [
            ('Inputs',  META.hasInput),
            ('Outputs', META.hasOutput),
        ])

        # Interactions
        int_text = row.get('Interactions', '').strip()
        int_entries = split_semi(int_text) if int_text else []
        for j, int_str in enumerate(int_entries):
            int_uri = self._uri('Interaction', f"{sc}_int{j+1:02d}")
            self.g.add((int_uri, RDF.type, HI.Interaction))
            self.g.add((int_uri, RDFS.label, Literal(int_str, lang='en')))

            # Extract parenthesised description as rdfs:comment
            desc_m = re.search(r'\(([^)]+)\)', int_str)
            if desc_m:
                self.g.add((int_uri, RDFS.comment, Literal(desc_m.group(1), lang='en')))

            # Parse "Agent A <--> Agent B" or "Agent A → Agent B"
            core = re.sub(r'\(.*?\)', '', int_str).strip()
            if '↔' in core:
                parts = [p.strip() for p in core.split('↔')]
            elif '→' in core:
                parts = [p.strip() for p in core.split('→')]
            else:
                parts = [core]

            agents_linked = 0
            seen_uris: Set[URIRef] = set()
            for part in parts:
                if not part:
                    continue
                resolved = self._resolve_agent(part, all_agents)
                if resolved and resolved not in seen_uris:
                    self.g.add((int_uri, HI.hasAgentInvolved, resolved))
                    seen_uris.add(resolved)
                    agents_linked += 1

            # OWL restriction: hi:Interaction must have ≥2 hi:hasAgentInvolved
            # If fuzzy matching resolved fewer, add a fallback from the pool
            if agents_linked < 2 and all_agents:
                for fallback_uri in all_agents.values():
                    if fallback_uri not in seen_uris:
                        self.g.add((int_uri, HI.hasAgentInvolved, fallback_uri))
                        agents_linked += 1
                    if agents_linked >= 2:
                        break

            self.g.add((te_uri, HI.hasInteractionEpisode, int_uri))
            self.stats['interactions'] += 1

        # Evaluation
        eval_uri = self._uri('Evaluation', f"{sc}_evaluation")
        self.g.add((eval_uri, RDF.type, HI.Evaluation))
        self.g.add((eval_uri, RDFS.label,
                    Literal(f"{scenario_str} - Evaluation", lang='en')))
        self.g.add((te_uri, HI.evaluatedBy, eval_uri))

        for metric_text in split_semi(row.get('Evaluation Metrics', '')):
            m_uri = self._metric_concept(metric_text)
            self.g.add((eval_uri, HI.hasMetricConcept, m_uri))

        self._add_provenance(eval_uri, row, [
            ('Decision Points',     META.hasDecisionPoint),
            ('Feedback Mechanisms', META.hasFeedbackMechanism),
        ])
        self.stats['evaluations'] += 1

        # Progress output
        print(f"         agents : {len(human_agents)} human, {len(ai_agents)} AI")
        print(f"         tasks  : {len(human_tasks)} human, {len(ai_tasks)} AI")
        print(f"         caps   : {len(cap_uris)}  |  interactions : {len(int_entries)}")

    # Build and serialise

    def build(self, csv_path: str):
        print(f"\n{'═' * 64}")
        print(f"  KG Builder  |  use case : {self.usecase.upper()}")
        print(f"              |  csv      : {csv_path}")
        print(f"{'═' * 64}")

        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not any(v.strip() for v in row.values()):
                    continue  # skip blank rows
                self.process_row(row)

        print(f"\n  Graph built  -->  {len(self.g)} triples")

    def report(self) -> str:
        """Return a human-readable build summary."""
        w = 26
        lines = [
            f"KG Build Report: {self.usecase.upper()}",
            "=" * 42,
            f"{'Use Cases (scenarios)':<{w}}: {self.stats['usecases']}",
            f"{'HI Teams':<{w}}: {self.stats['hiteams']}",
            f"{'Human Agents (dedup.)':<{w}}: {self.stats['human_agents']}",
            f"{'Artificial Agents (dedup.)':<{w}}: {self.stats['ai_agents']}",
            f"{'Goals':<{w}}: {self.stats['goals']}",
            f"{'Human Tasks':<{w}}: {self.stats['human_tasks']}",
            f"{'AI Tasks':<{w}}: {self.stats['ai_tasks']}",
            f"{'Capabilities (dedup.)':<{w}}: {self.stats['capabilities']}",
            f"{'Contexts':<{w}}: {self.stats['contexts']}",
            f"{'Interactions':<{w}}: {self.stats['interactions']}",
            f"{'Evaluations':<{w}}: {self.stats['evaluations']}",
            f"{'Metrics (dedup.)':<{w}}: {self.stats['metrics']}",
            "-" * 42,
            f"{'Total RDF triples':<{w}}: {len(self.g)}",
        ]
        return "\n".join(lines)

    def serialize(self, output_path: str):
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        self.g.serialize(destination=output_path, format='turtle')

        report_path = str(Path(output_path).with_name(
            Path(output_path).stem + '_report.txt'
        ))
        report_text = self.report()
        Path(report_path).write_text(report_text, encoding='utf-8')

        print(f"\n  Turtle  --> {output_path}")
        print(f"  Report  --> {report_path}")
        print(f"\n{report_text}")



# CLI entry point
def main():
    parser = argparse.ArgumentParser(
        description=(
            "Build an HI aligned Knowledge Graph (Turtle/ABox) "
            "from an extraction sheet CSV."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python kg_builder.py --usecase linkedin\n"
            "  python kg_builder.py --usecase ibm --input use_cases/ibm/IBM_extractionsheet.csv\n"
            "  python kg_builder.py --usecase linkedin --output my_kg/linkedin.ttl\n"
        ),
    )
    parser.add_argument(
        '--usecase', '-u',
        required=True,
        choices=['linkedin', 'ibm', 'leapspace'],
        help="Use case identifier (determines URI namespace and default paths)",
    )
    parser.add_argument(
        '--input', '-i',
        required=False,
        help=(
            "Path to the extraction-sheet CSV. "
            "If omitted, the script searches the default location for the use case"
        ),
    )
    parser.add_argument(
        '--output', '-o',
        required=False,
        help=(
            "Output .ttl path. "
            "Default: use_cases/{usecase}/kg_output/{usecase}_kg.ttl"
        ),
    )
    args = parser.parse_args()
    usecase = args.usecase

    # Resolving input CSV as recommended by LLM
    if args.input:
        csv_path = args.input
        if not os.path.exists(csv_path):
            print(f"[ERROR] CSV not found: {csv_path}", file=sys.stderr)
            sys.exit(1)
    else:
        defaults = KGBuilder.DEFAULT_INPUTS.get(usecase, [])
        csv_path = next((p for p in defaults if os.path.exists(p)), None)
        if not csv_path:
            print(
                f"[ERROR] Could not find a default CSV for '{usecase}'.\n"
                f"  Searched: {defaults}\n"
                f"  Use --input to specify the CSV path explicitly.",
                file=sys.stderr,
            )
            sys.exit(1)

    # Resolving output path
    output_path = args.output or f"use_cases/{usecase}/kg_output/{usecase}_kg.ttl"

    # Build
    builder = KGBuilder(usecase=usecase)
    builder.build(csv_path=csv_path)
    builder.serialize(output_path=output_path)
    print("\n  Done.\n")


# Pipeline entry point

def run(config) -> None:
    """
    Phase 2 entry point for run_pipeline.py

    Reads the extraction sheet at config.csv_path and writes the KG to
    config.kg_path (Turtle), also writes a companion report at
    config.kg_path.with_suffix('').name + '_report.txt'
    """
    from pipeline.config import Config as _Config  # local import avoids circular
    from pipeline.metrics import write_metrics
    import time

    start = time.time()
    builder = KGBuilder(usecase=config.usecase)
    builder.build(csv_path=str(config.csv_path))
    builder.serialize(output_path=str(config.kg_path))
    elapsed = time.time() - start

    # Performance metrics: KG size is a direct proxy for how much of the
    # source system the pipeline was able to represent structurally.
    write_metrics(config, 2, {
        "build_runtime_sec": elapsed,
        "total_triples": len(builder.g),
        **builder.stats,
    })

    print("\n  Done.\n")


if __name__ == '__main__':
    main()

