"""
Configuration loader for the HI Assessment Pipeline, I had so much trouble doing and running this clean and smoothly it was really terrible
at the end I asked an LLM to help me with it and it worked perfectly So I used it 

The file Loads a YAML config file, validates required fields, resolves all file paths
relative to the project root, and exposes a single Config object used by
every phase module.

Usage (from any phase module):
    from pipeline.config import Config
    config = Config("configs/linkedin.yaml")

Phase 1 YAML extension
Add a 'phase1' block to enable automated knowledge acquisition:

    phase1:
      target_system: "IBM watsonx.governance"   # human-readable system name
      anthropic_model: claude-opus-4-5           # optional, default shown
      max_searches: 60                           # optional, default shown

When 'phase1' is present:
  - csv_path existence check is skipped (Phase 1 will create it)
  - Phase 1 versioned outputs go to use_cases/{usecase}/phase1/v{N:02d}/
  - Completed extractionsheet.csv is copied to csv_path for Phase 2
"""

import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML is not installed.\n  Install it with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# Project root: pipeline/config.py → parent = pipeline/ → parent = project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Config:

    # Required fields in every YAML config file
    # csv_path existence is only enforced when phase1 is NOT enabled
    REQUIRED_FIELDS = ["usecase", "csv_path", "ontology_path", "output_dir"]

    def __init__(self, config_path: str):
        """
        Parameters
        ----------
        config_path : str
            Path to the YAML config file, relative to the project root
            or as an absolute path (e.g. 'configs/linkedin.yaml').
        """

        # ── 1. Resolve config file path ───────────────────────────────────────
        config_file = Path(config_path)
        if not config_file.is_absolute():
            config_file = PROJECT_ROOT / config_file

        # ── 2. Load and parse the YAML file ──────────────────────────────────
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except FileNotFoundError:
            print(
                f"[CONFIG ERROR] Config file not found: {config_file}",
                file=sys.stderr,
            )
            sys.exit(1)
        except yaml.YAMLError as e:
            print(
                f"[CONFIG ERROR] Failed to parse YAML file: {config_file}\n  {e}",
                file=sys.stderr,
            )
            sys.exit(1)

        if not isinstance(data, dict):
            print(
                f"[CONFIG ERROR] Config file is empty or not a valid YAML mapping: {config_file}",
                file=sys.stderr,
            )
            sys.exit(1)

        # ── 3. Validate required fields ───────────────────────────────────────
        for field in self.REQUIRED_FIELDS:
            if field not in data or not str(data[field]).strip():
                print(
                    f"[CONFIG ERROR] Required field '{field}' is missing or empty "
                    f"in config file: {config_file}",
                    file=sys.stderr,
                )
                sys.exit(1)

        # ── 4. Store core values ──────────────────────────────────────────────
        self.usecase: str = str(data["usecase"]).strip().lower()

        # ── 5. Resolve input paths (relative to project root) ─────────────────
        self.csv_path: Path      = self._resolve(data["csv_path"])
        self.ontology_path: Path = self._resolve(data["ontology_path"])
        self.output_dir: Path    = self._resolve(data["output_dir"])

        # ── 6. Phase 1 configuration ──────────────────────────────────────────
        _p1 = data.get("phase1", None)
        self.phase1_enabled: bool = _p1 is not None
        self._phase1_cfg: dict    = (_p1 if isinstance(_p1, dict) else {}) if self.phase1_enabled else {}

        # ── 7. Validate input file existence ──────────────────────────────────
        self._assert_exists(self.ontology_path, "HI Ontology TTL")

        if self.phase1_enabled:
            # csv_path will be created by Phase 1 — existence not required yet
            print(
                f"  [Config] phase1 enabled — csv_path will be created by Phase 1: "
                f"{self.csv_path.name}"
            )
        else:
            self._assert_exists(self.csv_path, "Extraction sheet CSV")

        # ── 8. Create output directory if it does not exist ───────────────────
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # ── 9. Derive output file paths ───────────────────────────────────────
        uc = self.usecase

        self.kg_path: Path = \
            self.output_dir / f"{uc}_kg.ttl"

        self.normalization_report_path: Path = \
            self.output_dir / f"{uc}_normalization_report.json"

        self.shacl_report_path: Path = \
            self.output_dir / f"{uc}_shacl_report.ttl"

        self.shacl_report_readable_path: Path = \
            self.output_dir / f"{uc}_shacl_report.txt"

        self.gap_analysis_path: Path = \
            self.output_dir / f"{uc}_gap_analysis.json"

        self.assessment_report_path: Path = \
            self.output_dir / f"{uc}_hi_assessment_report.md"

        # ── 10. SHACL shapes paths (inside the pipeline package) ──────────────
        shapes_root = PROJECT_ROOT / "pipeline"

        self.normalization_shapes_path: Path = (
            shapes_root
            / "phase3_normalization"
            / "shapes"
            / "normalization_shapes.ttl"
        )

        self.hi_conformance_shapes_path: Path = (
            shapes_root
            / "phase4_shacl_validation"
            / "shapes"
            / "hi_conformance_shapes.ttl"
        )

    # ── Phase 1 properties ────────────────────────────────────────────────────

    @property
    def phase1_dir(self) -> Path:
        """Base directory for all Phase 1 versioned runs."""
        return PROJECT_ROOT / "use_cases" / self.usecase / "phase1"

    @property
    def phase1_latest_dir(self) -> Optional[Path]:
        """Most recent phase1 version directory, or None if none exist."""
        if not self.phase1_dir.exists():
            return None
        versions = sorted(self.phase1_dir.glob("v*/"))
        return versions[-1] if versions else None

    @property
    def next_phase1_version_dir(self) -> Path:
        """Path for the next phase1 version directory (not yet created)."""
        existing = sorted(self.phase1_dir.glob("v*/")) if self.phase1_dir.exists() else []
        n = (int(sorted(existing)[-1].name[1:]) + 1) if existing else 1
        return self.phase1_dir / f"v{n:02d}"

    @property
    def anthropic_model(self) -> str:
        """Claude model for Phase 1 research (default: claude-opus-4-5)."""
        return self._phase1_cfg.get("anthropic_model", "claude-opus-4-5")

    @property
    def phase1_target_system(self) -> str:
        """Human-readable name of the target AI system being researched."""
        return self._phase1_cfg.get("target_system", self.usecase.title())

    @property
    def phase1_max_searches(self) -> int:
        """Maximum number of web searches Phase 1 may perform."""
        return int(self._phase1_cfg.get("max_searches", 60))

    # ── Private helpers ───────────────────────────────────────────────────────

    def _resolve(self, raw_path: str) -> Path:
        """Resolve a path string relative to the project root."""
        p = Path(str(raw_path))
        return p if p.is_absolute() else PROJECT_ROOT / p

    def _assert_exists(self, path: Path, label: str) -> None:
        """Exit with a clear error message if a required file does not exist."""
        if not path.exists():
            print(
                f"[CONFIG ERROR] {label} not found at resolved path:\n  {path}",
                file=sys.stderr,
            )
            sys.exit(1)

    # ── Summary ───────────────────────────────────────────────────────────────

    def summary(self) -> str:
        """Return a human-readable summary of the loaded configuration."""

        def status(p: Path) -> str:
            return "✓ exists" if p.exists() else "✗ NOT FOUND"

        lines = [
            "=" * 60,
            "  HI Assessment Pipeline — Configuration",
            "=" * 60,
            f"  Use case         : {self.usecase}",
            f"  Project root     : {PROJECT_ROOT}",
            "",
            "  Input files",
            f"    CSV            : {self.csv_path}",
            f"                     [{status(self.csv_path)}]",
            f"    Ontology       : {self.ontology_path}",
            f"                     [{status(self.ontology_path)}]",
            "",
            "  Output directory",
            f"    {self.output_dir}",
            f"                     [{status(self.output_dir)}]",
            "",
            "  Output files (written during pipeline run)",
            f"    KG             : {self.kg_path.name}",
            f"    Norm. report   : {self.normalization_report_path.name}",
            f"    SHACL report   : {self.shacl_report_path.name}",
            f"    Gap analysis   : {self.gap_analysis_path.name}",
            f"    Assessment     : {self.assessment_report_path.name}",
            "",
            "  SHACL shapes",
            f"    Normalization  : {self.normalization_shapes_path}",
            f"                     [{status(self.normalization_shapes_path)}]",
            f"    HI conformance : {self.hi_conformance_shapes_path}",
            f"                     [{status(self.hi_conformance_shapes_path)}]",
        ]

        if self.phase1_enabled:
            latest = self.phase1_latest_dir
            lines += [
                "",
                "  Phase 1 (Knowledge Acquisition)",
                f"    Target system  : {self.phase1_target_system}",
                f"    Model          : {self.anthropic_model}",
                f"    Max searches   : {self.phase1_max_searches}",
                f"    Phase 1 dir    : {self.phase1_dir}",
                f"    Latest version : {latest.name if latest else '(none yet)'}",
            ]

        lines.append("=" * 60)
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Config(usecase='{self.usecase}', csv='{self.csv_path.name}')"

