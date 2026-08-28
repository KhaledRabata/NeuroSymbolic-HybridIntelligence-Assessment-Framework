#!/usr/bin/env python3
"""
run_pipeline.py
This is the Main file for the Neuro-Symbolic HI Assessment Pipeline

Runs phases 1 to 6 for a given use case config file which needs to be prepared.
Phase 1 (Knowledge
Acquisition) is only executed if the config YAML contains a 'phase1' block
AND --reuse-phase1 is NOT specified

Usage summary by llm
    # Full pipeline, Phase 1 disabled in YAML (e.g. linkedin.yaml):
    python run_pipeline.py --config configs/linkedin.yaml

    # Full pipeline including Phase 1 (YAML must have 'phase1' block):
    python run_pipeline.py --config configs/leapspace.yaml

    # Skip Phase 1, reuse existing extraction sheet:
    python run_pipeline.py --config configs/leapspace.yaml --reuse-phase1

    # Start from a specific phase:
    python run_pipeline.py --config configs/linkedin.yaml --from 4

    # Run only specific phases:
    python run_pipeline.py --config configs/linkedin.yaml --phases 5,6

    # Dry run (loads config and prints summary, no execution):
    python run_pipeline.py --config configs/linkedin.yaml --dry-run

Environment requirments
    ANTHROPIC_API_KEY   required for Phase 1
    OPENAI_API_KEY      required for Phases 5 and 6
    LLM_MODEL           optional, defaults to gpt-4o-mini (Phases 5 and 6)
"""

import argparse
import sys
import time
from pathlib import Path

from pipeline.config import Config
from pipeline.metrics import consolidate_metrics

from pipeline.phase1_researcher.researcher     import run as run_phase1
from pipeline.phase2_kg_construction.kg_builder import run as run_phase2
from pipeline.phase3_normalization.normalizer   import run as run_phase3
from pipeline.phase4_shacl_validation.shacl_validator import run as run_phase4
from pipeline.phase5_gap_analysis.gap_analyzer  import run as run_phase5
from pipeline.phase6_recommendations.recommender import run as run_phase6


# Phase registry (this method was recommended by llm)

PHASES = {
    1: ("Knowledge Acquisition",         run_phase1),
    2: ("KG Construction",               run_phase2),
    3: ("Normalization Validation",       run_phase3),
    4: ("SHACL Conformance",             run_phase4),
    5: ("Neuro-Symbolic Gap Analysis",   run_phase5),
    6: ("Recommendation Generation",     run_phase6),
}

PHASE_NOTES = {
    1: "Requires ANTHROPIC_API_KEY + 'phase1' block in YAML",
    5: "Requires OPENAI_API_KEY",
    6: "Requires OPENAI_API_KEY",
}


# Helpers (recommended by llm as well for error handling and formatting)

def _parse_phases(phases_arg: str) -> list:
    try:
        result = sorted(set(int(p.strip()) for p in phases_arg.split(",")))
        invalid = [p for p in result if p not in PHASES]
        if invalid:
            print(
                f"[ERROR] Invalid phase number(s): {invalid}\n"
                f"  Valid phases are: {sorted(PHASES.keys())}",
                file=sys.stderr,
            )
            sys.exit(1)
        return result
    except ValueError:
        print(
            f"[ERROR] --phases must be comma-separated integers, e.g. '1,2,3'\n"
            f"  Got: '{phases_arg}'",
            file=sys.stderr,
        )
        sys.exit(1)


def _format_elapsed(seconds: float) -> str:
    # Formats elapsed seconds as a human-readable string
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs    = seconds % 60
    return f"{minutes}m {secs:.0f}s"


def _print_pipeline_header(config: Config, phases_to_run: list) -> None:
    # printing the header for the pipeline run
    print()
    print("╔" + "═" * 60 + "╗")
    print("║   Neuro-Symbolic HI Assessment Pipeline" + " " * 20 + "║")
    print("╚" + "═" * 60 + "╝")
    print(f"  Use case   : {config.usecase.upper()}")
    print(f"  Output dir : {config.output_dir}")
    print(f"  Phases     : {phases_to_run}")
    print()
    for p in phases_to_run:
        note = PHASE_NOTES.get(p, "")
        note_str = f"  ← {note}" if note else ""
        print(f"    Phase {p}: {PHASES[p][0]}{note_str}")
    print()


def _print_final_summary(
    config: Config,
    phases_run: list,
    timings: dict,
    failed_phase: int,
    total_elapsed: float,
) -> None:
    # prints the post run summary
    print()
    print("=" * 62)
    print(f"  Pipeline Summary : {config.usecase.upper()}")
    print("=" * 62)

    for phase in phases_run:
        name = PHASES[phase][0]
        if phase in timings:
            elapsed = _format_elapsed(timings[phase])
            icon    = "✓" if phase != failed_phase else "✗"
            print(f"  {icon} Phase {phase}: {name:<38} {elapsed}")
        else:
            print(f"  - Phase {phase}: {name:<38} skipped")

    print(f"  {'─' * 55}")
    print(f"  Total elapsed : {_format_elapsed(total_elapsed)}")

    if failed_phase: # error handling recommended by llm during de-bugging tantrums that I had
        print(f"  ✗ Pipeline stopped at Phase {failed_phase}.")
    else:
        print(f"  ✓ Pipeline completed successfully.")
        print()
        print("  Output files:")
        outputs = [
            (config.csv_path,                   "Extraction sheet (CSV)"),
            (config.kg_path,                    "KG (Turtle)"),
            (config.normalization_report_path,  "Normalization report"),
            (config.shacl_report_path,          "SHACL conformance report"),
            (config.gap_analysis_path,          "Gap analysis"),
            (config.assessment_report_path,     "HI assessment report"),
        ]
        for path, label in outputs:
            exists = "✓" if path.exists() else "-"
            print(f"    {exists} {label:<30} {path.name}")

        if config.phase1_enabled:
            latest = config.phase1_latest_dir
            if latest:
                print(f"\n  Phase 1 versioned output:")
                print(f"    ✓ {latest}")

    print("=" * 62)
    print()



# Main of the pipeline

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Neuro-Symbolic HI Assessment Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--config", "-c",
        required=True,
        help="Path to the use-case YAML config file (e.g. configs/linkedin.yaml)",
    )
    parser.add_argument(
        "--phases",
        default=None,
        help="Comma-separated list of phases to run (e.g. '2,3,4'). Default: all.",
    )
    parser.add_argument(
        "--from", dest="from_phase",
        type=int,
        default=None,
        metavar="PHASE",
        help="Start from this phase and run all subsequent phases.",
    )
    parser.add_argument(
        "--reuse-phase1",
        action="store_true",
        help=(
            "Skip Phase 1 even if 'phase1' is present in the YAML. "
            "Reuses the existing extraction sheet at csv_path. "
            "Use when research was already done and you only want to re-run "
            "phases 2 - 6 with the existing data."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load config and print summary without running any phases.",
    )

    args = parser.parse_args()

    # Mutually exclusive flags
    if args.phases and args.from_phase:
        print("[ERROR] --phases and --from are mutually exclusive.", file=sys.stderr)
        sys.exit(1)

    # Load config
    config = Config(args.config)

    # Resolving which phases to run
    if args.phases:
        phases_to_run = _parse_phases(args.phases)
    elif args.from_phase:
        if args.from_phase not in PHASES:
            print(
                f"[ERROR] --from {args.from_phase} is not a valid phase.\n"
                f"  Valid phases: {sorted(PHASES.keys())}",
                file=sys.stderr,
            )
            sys.exit(1)
        phases_to_run = [p for p in sorted(PHASES.keys()) if p >= args.from_phase]
    else:
        # Default: all phases. Include Phase 1 only if config has phase1 block
        if config.phase1_enabled:
            phases_to_run = sorted(PHASES.keys())       # 1–6
        else:
            phases_to_run = [p for p in sorted(PHASES.keys()) if p >= 2]  # 2–6

    # Handling --reuse-phase1 
    if args.reuse_phase1:
        if 1 in phases_to_run:
            phases_to_run = [p for p in phases_to_run if p != 1]
            print(
                f"  [--reuse-phase1] Phase 1 removed from run list "
                f"Using existing CSV: {config.csv_path}"
            )
        # Validate that csv_path actually exists when reusing
        if not config.csv_path.exists():
            print(
                f"[ERROR] --reuse-phase1 specified but csv_path does not exist:\n"
                f"  {config.csv_path}\n"
                f"  Run without --reuse-phase1 to execute Phase 1 first",
                file=sys.stderr,
            )
            sys.exit(1)

    # Validate Phase 1 prerequisites
    if 1 in phases_to_run and not config.phase1_enabled:
        print(
            "[ERROR] Phase 1 requested but 'phase1' block is missing from config YAML.\n"
            f"  Config: {args.config}\n"
            "  Add a 'phase1' block to enable automated knowledge acquisition.\n"
            "  See docs/research_acquisition_spec.md for details.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Print header
    _print_pipeline_header(config, phases_to_run)

    if args.dry_run:
        print(config.summary())
        print("\n[Dry run] No phases executed.\n")
        return

    # Execute phases in sequence
    timings: dict     = {}
    failed_phase: int = 0
    pipeline_start    = time.time()

    for phase in phases_to_run:
        name, run_fn = PHASES[phase]
        phase_start  = time.time()

        print(f"\n{'─' * 62}")
        print(f"  Starting Phase {phase}: {name}")
        print(f"{'─' * 62}")

        try:
            run_fn(config)
            elapsed        = time.time() - phase_start
            timings[phase] = elapsed
            print(f"\n   Phase {phase} completed in {_format_elapsed(elapsed)}")

        except SystemExit as e:
            elapsed        = time.time() - phase_start
            timings[phase] = elapsed
            failed_phase   = phase
            print(
                f"\n   Phase {phase} failed after {_format_elapsed(elapsed)} "
                "Pipeline stopped.",
                file=sys.stderr,
            )
            break

        except Exception as e:
            elapsed        = time.time() - phase_start
            timings[phase] = elapsed
            failed_phase   = phase
            print(
                f"\n   Phase {phase} raised an unexpected error after "
                f"{_format_elapsed(elapsed)}:\n  {type(e).__name__}: {e}",
                file=sys.stderr,
            )
            break

    total_elapsed = time.time() - pipeline_start

    # Consolidate this run's per-phase wall-clock timings with whatever
    # performance metrics each phase wrote on its own (tokens, search counts,
    # KG size, SHACL result counts, fallback triggers, ...) into one
    # performance report for this use case. Runs even if a phase failed, so
    # partial-run timings are still captured.
    perf_report = consolidate_metrics(config, timings)
    print(f"  Performance report written to: {perf_report['_path']}")

    # Final summary
    _print_final_summary(config, phases_to_run, timings, failed_phase, total_elapsed)

    sys.exit(1 if failed_phase else 0)


if __name__ == "__main__":
    main()

