

import json
from pathlib import Path
from typing import Any, Dict, Optional


def metrics_path(config, phase: int) -> Path:
    """Path of the metrics fragment written by a given phase for this use case."""
    return config.output_dir / f"{config.usecase}_phase{phase}_metrics.json"


def write_metrics(config, phase: int, data: Dict[str, Any]) -> Path:
    """
    Write one phase's metrics fragment to disk (overwrites any previous run's
    fragment for this use case + phase). Returns the path written.
    """
    path = metrics_path(config, phase)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path


def read_metrics(config, phase: int) -> Optional[Dict[str, Any]]:
    """
    Read one phase's metrics fragment, or None if it was never written
    (e.g. the phase was not part of this run, or predates this instrumentation).
    """
    path = metrics_path(config, phase)
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def consolidate_metrics(config, timings: Dict[int, float]) -> Dict[str, Any]:
    """
    Called once by run_pipeline.py after a run finishes (whether it completed
    all phases or stopped early). Merges the wall-clock `timings` dict that
    run_pipeline.py already collects with each phase's own metrics fragment
    (if that phase ran and wrote one), and writes the combined report to

        {output_dir}/{usecase}_pipeline_performance.json

    A phase with neither a timing nor a fragment (never run) is omitted.
    """
    phases: Dict[str, Any] = {}
    for phase in sorted(set(timings.keys()) | {1, 2, 3, 4, 5, 6}):
        frag = read_metrics(config, phase)
        runtime = timings.get(phase)
        if runtime is None and frag is None:
            continue
        entry: Dict[str, Any] = {"runtime_sec": runtime}
        if frag:
            entry.update(frag)
        phases[str(phase)] = entry

    report: Dict[str, Any] = {
        "usecase": config.usecase,
        "phases": phases,
        "total_runtime_sec": sum(v for v in timings.values() if v is not None),
    }

    out_path = config.output_dir / f"{config.usecase}_pipeline_performance.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    report["_path"] = str(out_path)
    return report
