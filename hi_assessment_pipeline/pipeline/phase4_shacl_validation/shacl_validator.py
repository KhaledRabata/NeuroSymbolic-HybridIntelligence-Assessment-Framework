"""
Phase 4: HI Conformance Validation

Validates the Knowledge Graph against hi_conformance_shapes.ttl to check
whether the assessed AI system genuinely embodies the CARE principles of
Hybrid Intelligence:
    Collaborative:   human and AI agents work together toward a shared goal
    Adaptive:        feedback loops allow the system to learn and adapt
    Responsible:     human oversight, fairness, and accountability are present 
    Explainable:     the AI can explain its behaviour to human agents

The output combines symbolic SHACL constraint checking with natural grouping of results by CARE dimension and scenario, 
producing a machine-readable SHACL results graph (TTL) for Phase 5 (Gap Analysis) and a human-readable text summary.

Severity levels
    sh:Violation   a required HI property is absent (hard fail)
    sh:Warning    an HI property is weak or implicit (soft flag)

Per-scenario status
    PASS      no violations and no warnings 
    WARNING   no violations, but at least one warning
    FAIL      at least one violation

Terminal interface
    from pipeline.phase4_shacl_validation.shacl_validator import run
    run(config)   # config is a pipeline.config.Config instance
"""

import json
import re
import sys
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS
from pyshacl import validate as shacl_validate
from pipeline.config import Config
from pipeline.metrics import write_metrics


# Namespaces
HI   = Namespace("https://w3id.org/hi-ontology#")
SH   = Namespace("http://www.w3.org/ns/shacl#")
META = Namespace("http://example.org/hi/meta/")
BASE_URI = "http://example.org/hi/"

# CARE dimension keywords: used to tag each violation with a dimension
_CARE_TAGS = {
    "Collaborative": ["collaborative", "human agent", "artificial agent",
                      "shared goal", "interaction", "human-ai"],
    "Adaptive":      ["adaptive", "feedback", "learn", "adapt"],
    "Responsible":   ["responsible", "oversight", "decision point",
                      "accountability", "fairness", "bias", "equit"],
    "Explainable":   ["explainable", "explainab", "xai", "transparen",
                      "interpret"],
}



# Helpers
def _extract_scenario_id(uri_str: str) -> Optional[str]:
    """
    Extract scenario ID (e.g. 's1') from any KG node URI

    Works for UseCase, HITeam, Goal, Task, TaskExecution, Evaluation,
    Interaction and Capability URIs all of which embed the scenario ID
    at the start of the last URI segment
    """
    last_seg = uri_str.rstrip("/").split("/")[-1]
    m = re.match(r"^(s\d+)", last_seg, re.IGNORECASE)
    return m.group(1).lower() if m else None


def _scenario_label(kg_graph: Graph, usecase: str, sc_id: str) -> str:
    uc_uri = URIRef(f"{BASE_URI}{usecase}/UseCase/{sc_id}")
    label = kg_graph.value(uc_uri, RDFS.label)
    return str(label) if label else sc_id.upper()


def _all_scenario_ids(kg_graph: Graph) -> List[str]:
    # Return sorted list of all scenario IDs present in the KG
    ids = []
    for uc_uri in kg_graph.subjects(RDF.type, HI.UseCase):
        sc_id = _extract_scenario_id(str(uc_uri))
        if sc_id:
            ids.append(sc_id)
    return sorted(ids)


def _care_dimension(message: str, component: str) -> str:
    """
    Infer the CARE dimension a violation belongs to from its message text
    Returns the first matching dimension, or 'General' if none match
    """
    text = (message + " " + component).lower()
    for dimension, keywords in _CARE_TAGS.items():
        for kw in keywords:
            if kw in text:
                return dimension
    return "General"


def _severity_label(severity_uri: Optional[str]) -> str:
    # Map a sh:resultSeverity URI to a short label
    if severity_uri is None:
        return "Violation"
    uri = str(severity_uri)
    if uri.endswith("Warning"):
        return "Warning"
    if uri.endswith("Info"):
        return "Info"
    return "Violation"


def _parse_violations(
    results_graph: Graph,
    shapes_graph: Graph,
    all_scenario_ids: List[str],
) -> Dict[str, List[dict]]:
    """
    Parse the pySHACL results graph and group violations by scenario ID

    For each sh:ValidationResult extracts:
      - focus_node   : the KG node that failed
      - message      : the sh:resultMessage
      - component    : the sh:name of the source property shape (if available)
      - severity     : 'Violation' or 'Warning'
      - care_dim     : inferred CARE dimension ('Collaborative', 'Adaptive', etc.)
      - source_shape : raw URI of the source shape

    Returns a dict mapping scenario_id --> list of violation dicts
    Violations that cannot be mapped to a scenario go under '_unmapped'
    """
    by_scenario: Dict[str, List[dict]] = {sc: [] for sc in all_scenario_ids}
    by_scenario["_unmapped"] = []

    for viol in results_graph.subjects(RDF.type, SH.ValidationResult):
        focus_node    = results_graph.value(viol, SH.focusNode)
        message       = results_graph.value(viol, SH.resultMessage)
        source_shape  = results_graph.value(viol, SH.sourceShape)
        severity_node = results_graph.value(viol, SH.resultSeverity)

        # Try to get sh:name from the source shape node in either graph
        comp_name = None
        if source_shape is not None:
            comp_name = (
                results_graph.value(source_shape, SH.name)
                or shapes_graph.value(source_shape, SH.name)
            )

        msg_str  = str(message)  if message       else "Constraint violated."
        sev_str  = _severity_label(str(severity_node) if severity_node else None)
        comp_str = str(comp_name) if comp_name else _infer_component(msg_str)
        care_dim = _care_dimension(msg_str, comp_str)

        viol_dict = {
            "component":   comp_str,
            "care_dim":    care_dim,
            "severity":    sev_str,
            "message":     msg_str,
            "focus_node":  str(focus_node) if focus_node else "unknown",
            "source_shape": str(source_shape) if source_shape else "unknown",
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


def _infer_component(message: str) -> str:
    """
    This was recommended by the llm
    Fallback: infer a short component name from the violation message when
    sh:name is not available in the results graph
    """
    patterns = [
        (r"Human Agent",               "Human Agent"),
        (r"Artificial Agent",          "Artificial Agent"),
        (r"shared Goal",               "Shared Goal"),
        (r"Capabilit",                 "Capabilities"),
        (r"Responsible.*annot",        "Responsible CARE Annotation"),
        (r"Explainable.*annot",        "Explainable CARE Annotation"),
        (r"Fairness|fairness",         "Fairness Mechanism"),
        (r"XAI|Explainability",        "XAI Capability"),
        (r"Human.*Interaction|human.*interaction", "Human in Interaction"),
        (r"AI.*Interaction",           "AI in Interaction"),
        (r"Human Oversight",           "Human Oversight"),
        (r"Accountability|Evaluation", "Accountability via Evaluation"),
        (r"Interaction.*Execut",       "Interaction in Execution"),
        (r"Feedback",                  "Feedback Mechanism"),
        (r"Decision Point",            "Decision Points"),
        (r"Metric",                    "Evaluation Metrics"),
        (r"requiresCapability|Capability", "Required Capability"),
    ]
    for pattern, label in patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return label
    return "Unknown Component"


def _scenario_status(violations: List[dict]) -> Tuple[str, int, int]:
    """
    Determine scenario status from its violations list

    Returns (status, violation_count, warning_count) where:
        status = 'PASS', 'WARNING', or 'FAIL'
    """
    hard = sum(1 for v in violations if v["severity"] == "Violation")
    soft = sum(1 for v in violations if v["severity"] == "Warning")

    if hard > 0:
        return "FAIL", hard, soft
    if soft > 0:
        return "WARNING", hard, soft
    return "PASS", 0, 0



# Report writers

def _write_json_report(
    config: Config,
    all_ids: List[str],
    kg_graph: Graph,
    scenarios_report: dict,
    conforms: bool,
    results_graph: Graph,
    total_pass: int,
    total_warn: int,
    total_fail: int,
) -> None:
    # Write the SHACL report as a machine-readable JSON file (for Phase 5)
    report = {
        "usecase":          config.usecase,
        "phase":            "4-shacl-conformance",
        "timestamp":        datetime.now(timezone.utc).isoformat(),
        "kg_file":          str(config.kg_path),
        "shapes_file":      str(config.hi_conformance_shapes_path),
        "total_scenarios":  len(all_ids),
        "pass":             total_pass,
        "warning":          total_warn,
        "fail":             total_fail,
        "overall_conforms": conforms,
        "scenarios":        scenarios_report,
    }
    with open(config.shacl_report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Also here I serialise the raw SHACL results graph as Turtle (for Phase 5 LLM input)
    raw_ttl_path = str(config.shacl_report_path).replace(".ttl", "_raw.ttl")
    results_graph.serialize(destination=raw_ttl_path, format="turtle")


def _write_text_report(
    config: Config,
    all_ids: List[str],
    scenarios_report: dict,
    total_pass: int,
    total_warn: int,
    total_fail: int,
) -> None:
    # we then write the SHACL report as a human-readable text summary
    lines = []
    lines.append("=" * 70)
    lines.append(f"  HI Conformance Report  {config.usecase.upper()}")
    lines.append(f"  Phase 4: SHACL Conformance Validation")
    lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 70)
    lines.append("")
    lines.append("  CARE PRINCIPLES EVALUATED")
    lines.append("  ─────────────────────────────────────────────────────────")
    lines.append("  C  Collaborative : human and AI agents work together")
    lines.append("  A  Adaptive      : feedback loops support learning")
    lines.append("  R  Responsible   : oversight, fairness, accountability")
    lines.append("  E  Explainable   : AI explains decisions to humans")
    lines.append("")
    lines.append(f"  Scenarios: {len(all_ids)}   "
                 f"PASS: {total_pass}   WARNING: {total_warn}   FAIL: {total_fail}")
    lines.append("  ─────────────────────────────────────────────────────────")
    lines.append("")

    for sc_id in all_ids:
        info   = scenarios_report[sc_id]
        status = info["status"]
        label  = info["label"]
        icon   = {"PASS": "✓", "WARNING": "⚠", "FAIL": "✗"}.get(status, "?")

        lines.append(f"  {icon} [{sc_id.upper()}] {label}")
        lines.append(f"      Status       : {status}")

        viols_by_dim: Dict[str, List[dict]] = {}
        for v in info["violations"]:
            dim = v.get("care_dim", "General")
            viols_by_dim.setdefault(dim, []).append(v)

        if not viols_by_dim:
            lines.append("      No HI conformance issues detected.")
        else:
            for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable", "General"]:
                if dim not in viols_by_dim:
                    continue
                lines.append(f"      [{dim}]")
                for v in viols_by_dim[dim]:
                    sev_icon = "✗" if v["severity"] == "Violation" else "⚠"
                    lines.append(f"        {sev_icon} {v['component']}")
                    # Wrap message at ~65 chars
                    msg = v["message"]
                    words = msg.split()
                    line_buf, col = [], 0
                    msg_lines = []
                    for w in words:
                        if col + len(w) > 65:
                            msg_lines.append(" ".join(line_buf))
                            line_buf, col = [w], len(w)
                        else:
                            line_buf.append(w)
                            col += len(w) + 1
                    if line_buf:
                        msg_lines.append(" ".join(line_buf))
                    lines.append(f"           {msg_lines[0]}")
                    for extra in msg_lines[1:]:
                        lines.append(f"           {extra}")
        lines.append("")

    lines.append("  ─────────────────────────────────────────────────────────")
    if total_fail == 0 and total_warn == 0:
        lines.append("  ✓ ALL SCENARIOS CONFORM TO HI PRINCIPLES")
    elif total_fail == 0:
        lines.append(f"  ⚠ ALL SCENARIOS PASS (with {total_warn} WARNING scenario(s))")
        lines.append("    Warnings indicate areas for improvement, not hard failures.")
    else:
        lines.append(f"  ✗ {total_fail} SCENARIO(S) FAIL HI CONFORMANCE")
        lines.append("    See violations above. Feed this report to Phase 5 (Gap Analysis).")
    lines.append("=" * 70)

    with open(config.shacl_report_readable_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")



# terminal output

def run(config: Config) -> None:
    """Phase 4 entry point called by run_pipeline.py"""

    print("\n" + "=" * 62)
    print(f"  PHASE 4: HI Conformance Validation  |  {config.usecase.upper()}")
    print("=" * 62)

    # I need to veryify that phase 2 was run
    if not config.kg_path.exists():
        print(
            f"[Phase 4 ERROR] KG file not found: {config.kg_path}\n"
            "  Run Phase 2 (KG Construction) first.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Loading the KG
    print(f"[Phase 4] Loading KG            : {config.kg_path}")
    kg_graph = Graph()
    kg_graph.parse(str(config.kg_path), format="turtle")
    print(f"[Phase 4] KG loaded             : {len(kg_graph)} triples")

    # Loading the HI conformance shapes 
    print(f"[Phase 4] Loading shapes        : {config.hi_conformance_shapes_path}")
    shapes_graph = Graph()
    shapes_graph.parse(str(config.hi_conformance_shapes_path), format="turtle")
    print(f"[Phase 4] Shapes loaded         : {len(shapes_graph)} triples")

    # Loading the ontology for inference
    # pySHACL uses the ontology graph for RDFS inference so that subclass
    # relationships (HumanAgent ⊑ Agent, ArtificialAgent ⊑ Agent) are applied
    # during qualified value shape checks
    print(f"[Phase 4] Loading ontology      : {config.ontology_path}")
    ont_graph = Graph()
    ont_graph.parse(str(config.ontology_path), format="turtle")
    print(f"[Phase 4] Ontology loaded       : {len(ont_graph)} triples")

    # Run SHACL validation
    print("[Phase 4] Running SHACL-SPARQL conformance check ...")
    conforms, results_graph, results_text = shacl_validate(
        data_graph=kg_graph,
        shacl_graph=shapes_graph,
        ont_graph=ont_graph,        # this provides class hierarchy for inference
        inference="rdfs",           # this enable RDFS class reasoning
        abort_on_first=False,       # this collect all violations, not just the first
        meta_shacl=False,
        debug=False,
    )
    print(f"[Phase 4] Validation done       : conforms = {conforms}")

    # Collect scenario IDs from KG
    all_ids = _all_scenario_ids(kg_graph)

    # Parse and group violations by scenario
    violations_by_scenario = _parse_violations(results_graph, shapes_graph, all_ids)

    # Build per-scenario report entries
    scenarios_report = {}
    total_pass = total_warn = total_fail = 0

    for sc_id in all_ids:
        viols  = violations_by_scenario.get(sc_id, [])
        status, hard_count, soft_count = _scenario_status(viols)

        if status == "PASS":
            total_pass += 1
        elif status == "WARNING":
            total_warn += 1
        else:
            total_fail += 1

        scenarios_report[sc_id] = {
            "label":            _scenario_label(kg_graph, config.usecase, sc_id),
            "status":           status,
            "violation_count":  hard_count,
            "warning_count":    soft_count,
            "care_gaps":        sorted({v["care_dim"] for v in viols
                                        if v["severity"] == "Violation"}),
            "violations":       viols,
        }

    unmapped = violations_by_scenario.get("_unmapped", [])

    # Write outputs
    _write_json_report(
        config, all_ids, kg_graph, scenarios_report, conforms,
        results_graph, total_pass, total_warn, total_fail,
    )
    print(f"[Phase 4] JSON report written   : {config.shacl_report_path}")

    _write_text_report(
        config, all_ids, scenarios_report, total_pass, total_warn, total_fail,
    )
    print(f"[Phase 4] Text report written   : {config.shacl_report_readable_path}")

    if unmapped:
        print(f"[Phase 4] Unmapped violations   : {len(unmapped)} (check _unmapped in JSON)")

    # Performance metrics: total SHACL results (violations + warnings) this
    # phase processed, which is the direct input volume Phase 5 has to
    # interpret next.
    total_results = sum(len(v["violations"]) for v in scenarios_report.values()) + len(unmapped)
    write_metrics(config, 4, {
        "kg_triples":          len(kg_graph),
        "shapes_triples":      len(shapes_graph),
        "ontology_triples":    len(ont_graph),
        "total_scenarios":     len(all_ids),
        "pass":                total_pass,
        "warning":             total_warn,
        "fail":                total_fail,
        "shacl_results_total": total_results,
        "unmapped_results":    len(unmapped),
        "overall_conforms":    conforms,
    })

    # Print terminal summary
    _print_summary(
        config.usecase, all_ids, scenarios_report,
        total_pass, total_warn, total_fail,
    )

    print("\n[Phase 4] Complete.\n")


def _print_summary(
    usecase: str,
    all_ids: List[str],
    scenarios_report: dict,
    total_pass: int,
    total_warn: int,
    total_fail: int,
) -> None:
    # Print a compact CARE conformance summary to the terminal
    print(f"\n  HI Conformance Summary: {usecase.upper()}")
    print(f"  {'─' * 55}")
    print(f"  Total scenarios : {len(all_ids)}")
    print(f"  PASS            : {total_pass}")
    print(f"  WARNING         : {total_warn}")
    print(f"  FAIL            : {total_fail}")
    print(f"  {'─' * 55}")

    for sc_id in all_ids:
        info   = scenarios_report[sc_id]
        status = info["status"]
        icon   = {"PASS": "✓", "WARNING": "⚠", "FAIL": "✗"}.get(status, "?") # these icons were suggested by claude for readability
        label  = info["label"][:50]
        print(f"  {icon} [{sc_id.upper()}] {label}")

        # Print hard violations only (Warnings shown in text report)
        for v in info["violations"]:
            if v["severity"] == "Violation":
                print(f"        ✗ [{v['care_dim']}] {v['component']}")
        for v in info["violations"]:
            if v["severity"] == "Warning":
                print(f"        ⚠ [{v['care_dim']}] {v['component']}")

    print(f"  {'─' * 55}")
    if total_fail == 0 and total_warn == 0:
        overall = "✓ ALL SCENARIOS CONFORM TO HI PRINCIPLES"
    elif total_fail == 0:
        overall = f"⚠ PASSES WITH WARNINGS ({total_warn} scenario(s) have soft gaps)"
    else:
        overall = f"✗ {total_fail} SCENARIO(S) FAIL HI CONFORMANCE"
    print(f"  {overall}")

