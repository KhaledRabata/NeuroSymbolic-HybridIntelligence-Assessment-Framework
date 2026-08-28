"""
Phase 3: Normalization Validation

Validates that every hi:UseCase in the Knowledge Graph is structurally
complete according to the standardized HI scenario template defined in
normalization_shapes.ttl

Violations are mapped back to their scenario using URI patterns so the
report is always expressed in terms of scenarios (s1, s2, …) rather than
raw RDF node URIs

Public interface:
    from pipeline.phase3_normalization.normalizer import run
    run(config)   # config is a pipeline.config.Config instance
"""

import json
import re
import sys
from datetime import datetime, timezone
from typing import Dict, List, Optional

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

from pyshacl import validate as shacl_validate

from pipeline.config import Config
from pipeline.metrics import write_metrics


# Namespaces needed for parsing the SHACL results graph
HI   = Namespace("https://w3id.org/hi-ontology#")
SH   = Namespace("http://www.w3.org/ns/shacl#")
META = Namespace("http://example.org/hi/meta/")
BASE_URI = "http://example.org/hi/"



# Helpers
def _extract_scenario_id(uri_str: str) -> Optional[str]:
    """
    Extract the scenario ID (e.g. 's1') from a KG node URI

    Works for all scenario-scoped node types:
      .../UseCase/s1              --> 's1'
      .../HITeam/s1_team          --> 's1'
      .../Goal/s1_goal            --> 's1'
      .../TaskExecution/s1_...    --> 's1'
      .../Evaluation/s1_...       --> 's1'
    """
    last_seg = uri_str.rstrip("/").split("/")[-1]
    m = re.match(r"^(s\d+)", last_seg, re.IGNORECASE)
    return m.group(1).lower() if m else None


def _scenario_label(kg_graph: Graph, usecase: str, sc_id: str) -> str:
    # Look up the scenario's rdfs:label from the KG
    uc_uri = URIRef(f"{BASE_URI}{usecase}/UseCase/{sc_id}")
    label = kg_graph.value(uc_uri, RDFS.label)
    return str(label) if label else sc_id.upper()


def _all_scenario_ids(kg_graph: Graph) -> List[str]:
    """Return sorted list of all scenario IDs present in the KG"""
    ids = []
    for uc_uri in kg_graph.subjects(RDF.type, HI.UseCase):
        sc_id = _extract_scenario_id(str(uc_uri))
        if sc_id:
            ids.append(sc_id)
    return sorted(ids)


def _parse_violations(
    results_graph: Graph,
    shapes_graph: Graph,
    all_scenario_ids: List[str],
) -> Dict[str, List[dict]]:
    """
    Parse the pySHACL results graph and group violations by scenario ID

    For each sh:ValidationResult node extracts:
      - focus_node  : the KG node that failed
      - message     : the sh:resultMessage (human-readable description)
      - component   : the sh:name of the source property shape (if available)
      - source_node : raw URI of the source shape

    Returns a dict mapping scenario_id --> list of violation dicts
    Violations on nodes that cannot be mapped to a scenario are collected
    under the key '_unmapped'.
    """
    by_scenario: Dict[str, List[dict]] = {sc: [] for sc in all_scenario_ids}
    by_scenario["_unmapped"] = []

    for viol in results_graph.subjects(RDF.type, SH.ValidationResult):
        focus_node   = results_graph.value(viol, SH.focusNode)
        message      = results_graph.value(viol, SH.resultMessage)
        source_shape = results_graph.value(viol, SH.sourceShape)

        # Try to get the component name from sh:name on the source shape
        # pySHACL may store the sh:name of the property constraint in the
        # results graph; if not, fall back to parsing the message string
        comp_name = None
        if source_shape is not None:
            comp_name = (
                results_graph.value(source_shape, SH.name)
                or shapes_graph.value(source_shape, SH.name)
            )

        viol_dict = {
            "component":   str(comp_name) if comp_name else _parse_component_from_message(str(message)),
            "message":     str(message) if message else "Constraint violated.",
            "focus_node":  str(focus_node) if focus_node else "unknown",
        }

        if focus_node is None:
            by_scenario["_unmapped"].append(viol_dict)
            continue

        sc_id = _extract_scenario_id(str(focus_node))
        if sc_id and sc_id in by_scenario:
            by_scenario[sc_id].append(viol_dict)
        else:
            by_scenario["_unmapped"].append(viol_dict)

    return by_scenario


def _parse_component_from_message(message: str) -> str:
    """
    Fallback: extract a short component name from the violation message
    Used when sh:name is not available from the source shape

    Examples:
      "Scenario is missing a name (rdfs:label)."  --> "Scenario Name"
      "HI Team has no Human Agent …"              -->  "Human Agent"
    """
    patterns = [
        (r"missing a name",            "Scenario Name"),
        (r"Evidence ID",               "Evidence IDs"),
        (r"no HI Team",                "HI Team"),
        (r"no Goal",                   "Goal"),
        (r"no.*Context",               "Context"),
        (r"CARE.*Characteristic|HI Char", "HI Characteristics"),
        (r"Human Agent",               "Human Agent"),
        (r"Artificial Agent",          "Artificial Agent"),
        (r"Capabilit",                 "Required Capabilities"),
        (r"no.*Task|requires.*Task",   "Tasks"),
        (r"no.*Evaluation",            "Evaluation"),
        (r"Interaction",               "Interaction Points"),
        (r"Input Data|hasInput",       "Input Data"),
        (r"Outputs|hasOutput",         "Outputs"),
        (r"Metric",                    "Evaluation Metrics"),
        (r"Decision Point",            "Decision Points"),
        (r"Feedback",                  "Feedback Mechanisms"),
    ]
    for pattern, label in patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return label
    return "Unknown Component"



# the following is for the output on terminal

def run(config: Config) -> None:
    """Phase 3 entry point called by run_pipeline.py"""

    print("\n" + "=" * 62)
    print(f"  PHASE 3: Normalization Validation  |  {config.usecase.upper()}")
    print("=" * 62)

    # Verify Phase 2 has run first
    if not config.kg_path.exists():
        print(
            f"[Phase 3 ERROR] KG file not found: {config.kg_path}\n"
            "  Run Phase 2 first",
            file=sys.stderr,
        )
        sys.exit(1)

    # Load KG
    print(f"[Phase 3] Loading KG       : {config.kg_path}")
    kg_graph = Graph()
    kg_graph.parse(str(config.kg_path), format="turtle")
    print(f"[Phase 3] KG loaded        : {len(kg_graph)} triples")

    # Load normalization shapes 
    print(f"[Phase 3] Loading shapes   : {config.normalization_shapes_path}")
    shapes_graph = Graph()
    shapes_graph.parse(str(config.normalization_shapes_path), format="turtle")
    print(f"[Phase 3] Shapes loaded    : {len(shapes_graph)} triples")

    # Run SHACL validation 
    print("[Phase 3] Running SHACL validation ...")
    conforms, results_graph, results_text = shacl_validate(
        data_graph=kg_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",       # enables class hierarchy reasoning
        abort_on_first=False,   # collect every violation, not just the first
        meta_shacl=False,
        debug=False,
    )
    print(f"[Phase 3] Validation done  : conforms = {conforms}")

    # Collect all scenario IDs from the KG
    all_ids = _all_scenario_ids(kg_graph)

    # Parse violations and group by scenario
    violations_by_scenario = _parse_violations(results_graph, shapes_graph, all_ids)

    # Build per-scenario report entries 
    scenarios_report = {}
    total_passed = 0
    total_failed = 0

    for sc_id in all_ids:
        viols  = violations_by_scenario.get(sc_id, [])
        status = "PASS" if not viols else "FAIL"
        if status == "PASS":
            total_passed += 1
        else:
            total_failed += 1

        scenarios_report[sc_id] = {
            "label":              _scenario_label(kg_graph, config.usecase, sc_id),
            "status":             status,
            "violation_count":    len(viols),
            "missing_components": sorted({v["component"] for v in viols}),
            "violations":         viols,
        }

    # Capturing any violations that could not be mapped to a scenario
    unmapped = violations_by_scenario.get("_unmapped", [])

    # Assemble full report
    report = {
        "usecase":          config.usecase,
        "timestamp":        datetime.now(timezone.utc).isoformat(),
        "kg_file":          str(config.kg_path),
        "shapes_file":      str(config.normalization_shapes_path),
        "total_scenarios":  len(all_ids),
        "passed":           total_passed,
        "failed":           total_failed,
        "overall_conforms": conforms,
        "scenarios":        scenarios_report,
        "unmapped_violations": unmapped,
    }

    # JSON report
    with open(config.normalization_report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"[Phase 3] Report written   : {config.normalization_report_path}")

    # Performance metrics: how many SHACL results this phase had to process,
    # and how much of the KG passed structural normalization without
    # needing any manual fixes.
    total_results = sum(len(v["violations"]) for v in scenarios_report.values()) + len(unmapped)
    write_metrics(config, 3, {
        "kg_triples":          len(kg_graph),
        "shapes_triples":      len(shapes_graph),
        "total_scenarios":     len(all_ids),
        "passed":              total_passed,
        "failed":              total_failed,
        "shacl_results_total": total_results,
        "unmapped_results":    len(unmapped),
        "overall_conforms":    conforms,
    })

    # Print summary to terminal
    _print_summary(config.usecase, all_ids, scenarios_report, total_passed, total_failed)

    print("\n[Phase 3] Complete\n")


def _print_summary(
    usecase: str,
    all_ids: List[str],
    scenarios_report: dict,
    total_passed: int,
    total_failed: int,
) -> None:
    print(f"\n  Normalization Summary: {usecase.upper()}")
    print(f"  {'─' * 50}")
    print(f"  Total scenarios : {len(all_ids)}")
    print(f"  Passed          : {total_passed}")
    print(f"  Failed          : {total_failed}")
    print(f"  {'─' * 50}")

# recommended ammendment by llm
    for sc_id in all_ids:
        info   = scenarios_report[sc_id]
        icon   = "✓" if info["status"] == "PASS" else "✗"
        label  = info["label"][:55]
        print(f"  {icon} [{sc_id.upper()}] {label}")
        for v in info["violations"]:
            print(f"        → {v['component']}: {v['message']}")

    print(f"  {'─' * 50}")
    overall = "✓ ALL SCENARIOS NORMALIZED" if total_failed == 0 else f"✗ {total_failed} SCENARIO(S) NOT NORMALIZED"
    print(f"  {overall}")

