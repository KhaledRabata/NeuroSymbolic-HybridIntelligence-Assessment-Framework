"""
Phase 1: Automated Knowledge Acquisition and Information retrieval

In this phase of the pipeline, I Use Claude API with the builtin web search server tool to conduct systematic research 
on a target company AI system, following the Research Acquisition Specification (RAS) protocol defined 
in docs/research_acquisition_spec.md which I engineered as a prompt and used manually in early stages of this project.

After finalizing this python file, I came to realize that it is much more costly and time consuming to run this file
than it is to run the prompt manually, but I will keep this file and phase either way.

In this file, I execute the research through two stages:

Stage A: Research loop
    An agentic loop runs until Claude signals end_turn (or pause_turn is exhausted). 
    Claude searches the web autonomously, following the 7 session RAS protocol. 
    All text output is collected into a single research document.

Stage B: File generation
    Seven focused API calls (no web search) each produce one output file from the Stage A research document: 
    research_log.md, README.md, sources.md, scenarios.md, extractionsheet.csv, ontology_mapping.md, knowledge_gaps.md.

The output is placed in the corresponding version directory
e.g.
    use_cases/{usecase}/phase1/v01/
    use_cases/{usecase}/phase1/v02/
    ...

Completed extractionsheet.csv is also copied to config.csv_path so Phase 2 can read it. Existing csv_path is backed up first.

To reuse an existing Phase 1 run rather than performing new research, pass --reuse-phase1 to run_pipeline.py (skips Phase 1 entirely)

If you decide to run this pipeline you will need API keys for claude and openai
"""

# File set up
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import anthropic
from pipeline.config import Config
from pipeline.metrics import write_metrics


# The model used for the file-generation stage is sonnet because it is cheaper to use when research is done already
GENERATION_MODEL = "claude-sonnet-4-6"

# Maximum tokens per API call
RESEARCH_MAX_TOKENS    = 16000
GENERATION_MAX_TOKENS  = 8500

# Maximum pause_turn continuations before aborting the research loop to prevent an infinite search
MAX_PAUSE_TURNS = 30

# Anthropic web search server tool - results handled server-side
WEB_SEARCH_TOOL_TYPE = "web_search_20250305"

# CSV column header exactly as Phase 2 (kg_builder.py) expects
CSV_HEADER = (
    "Scenario,Human Agents,AI Agents,Goals,Human Tasks,AI Tasks,"
    "Capabilities,Context,Inputs,Outputs,Interactions,Decision Points,"
    "Feedback Mechanisms,Evaluation Metrics,HI Characteristics,"
    "Evidence IDs,Confidence,Observed/Inferred"
)

# The 7 output files Phase 1 must produce, this is based of the prompt I engineered, I asked GPT to transform it into this dict
OUTPUT_FILES: List[Dict[str, str]] = [
    {
        "filename":    "research_log.md",
        "label":       "Research Log",
        "description": (
            "A complete chronological log of every search session performed. "
            "For each session document: objective, search terms used, sources "
            "visited (with URLs), sources rejected and why, sources accepted, "
            "information extracted, ontology concepts discovered, scenarios "
            "supported, and remaining unknowns. Use clear section headers "
            "per session (Session 1 through 7 at minimum)."
        ),
        "format": "Markdown",
    },
    {
        "filename":    "README.md",
        "label":       "Package README",
        "description": (
            "Package overview describing: the target use case, scope of research, "
            "methodology followed (RAS protocol), completion status, search "
            "strategy summary, list of all evidence sources consulted, and "
            "a pointer to each of the 7 output files."
        ),
        "format": "Markdown",
    },
    {
        "filename":    "sources.md",
        "label":       "Source Inventory",
        "description": (
            "Complete inventory of every source consulted. For each source include: "
            "Evidence ID (E-001, E-002, …), title, URL, source type (official doc / "
            "engineering blog / research paper / etc.), quality assessment, relevance "
            "score, and which ontology concepts it supports. Format as a numbered list."
        ),
        "format": "Markdown",
    },
    {
        "filename":    "scenarios.md",
        "label":       "HI Scenarios",
        "description": (
            "Structured descriptions of all identified Hybrid Intelligence scenarios "
            "(label each S1, S2, …). For each scenario include ALL of: Scenario Name, "
            "Description, Goal, Human Actors, Artificial Agents, Context, Input Data, "
            "Knowledge Sources, Processing Method, Processing Tasks, Interaction Points, "
            "Outputs, Evaluation Metrics, Required Capabilities, Decision Points, "
            "Feedback Mechanisms, Expected HI Characteristics (CARE dimensions), "
            "Evidence IDs, and Confidence level."
        ),
        "format": "Markdown",
    },
    {
        "filename":    "extractionsheet.csv",
        "label":       "Extraction Sheet (CSV)",
        "description": (
            "A CSV file where every row is one scenario. "
            "The header must be EXACTLY:\n"
            f"{CSV_HEADER}\n\n"
            "Rules:\n"
            "- Row 1 = header only\n"
            "- One row per scenario (S1, S2, …)\n"
            "- Multi-value cells use semicolons as separators\n"
            "- Cells containing commas must be quoted with double quotes\n"
            "- Observed/Inferred column: 'Observed' or 'Inferred' or mixed description\n"
            "- Confidence column: 'High', 'Medium', or 'Low'\n"
            "- Evidence IDs column: comma-separated, e.g. 'E-001, E-002, E-005'\n"
            "This file will be fed directly into the Knowledge Graph builder."
        ),
        "format": "CSV",
    },
    {
        "filename":    "ontology_mapping.md",
        "label":       "Ontology Mapping",
        "description": (
            "A mapping of every identified concept to its HI ontology class. "
            "Do NOT produce RDF or triples - only document the mappings in plain text. "
            "Organise by ontology class: HITeam, UseCase, HumanAgent, ArtificialAgent, "
            "Goal, Task, Capability, Interaction, Context, TaskExecution, "
            "Evaluation/Experiment, CARE mapping, and Key Properties. "
            "For each mapping note: the concept name, its ontology class, "
            "relevant properties, and Evidence ID."
        ),
        "format": "Markdown",
    },
    {
        "filename":    "knowledge_gaps.md",
        "label":       "Knowledge Gaps",
        "description": (
            "Documentation of information that could NOT be found during research. "
            "Assign each gap a Gap ID (E-GAP-01, E-GAP-02, …). "
            "For every gap document: missing information, searches performed, "
            "sources consulted, why the information could not be found, and whether "
            "a modelling assumption may be required in Phase 2. "
            "Do NOT fill the gaps - only document them. "
            "End with a summary table: Gap ID | Category | HI Dimension Affected | "
            "Modelling Assumption Required."
        ),
        "format": "Markdown",
    },
]


# API helpers: When I first did this file I was calling the API throughout the file, claude recommended building API helpers instead
def _get_client() -> "anthropic.Anthropic":
    """Return an Anthropic client, failing fast if API key is missing."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print(
            "[Phase 1 ERROR] ANTHROPIC_API_KEY environment variable is not set.\n"
            "  Export it before running: export ANTHROPIC_API_KEY='sk-ant-...'",
            file=sys.stderr,
        )
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


# the blocks returned caused some issues so this function helper extracts the human readable text only
def _extract_text(content: List[Any]) -> str:
    """Extract all text blocks from an Anthropic response content list."""
    parts = []
    for block in content:
        if hasattr(block, "text") and block.text.strip():
            parts.append(block.text)
    return "\n\n".join(parts)


# helps me monitor how many searches were made (as a monitoring feature) and because wait times can be long so this helps keep track or progress
def _count_searches(content: List[Any]) -> int:
    """Count how many web_search server_tool_use blocks are in a response."""
    return sum(
        1 for block in content
        if getattr(block, "type", "") == "server_tool_use"
        and getattr(block, "name", "") == "web_search"
    )


# The following part of this file contains the two stages
# Stage A: Research loop 

def _build_research_prompt(target_system: str, ras_text: str, ontology_text: str) -> str:
    """Build the user message that kicks off the research loop, found this on stack and reused it"""
    ontology_section = ""
    if ontology_text:
        # Include only the first 40 000 chars to avoid token bloat
        snippet = ontology_text[:40_000]
        ontology_section = (
            f"\n\n---\n\n## HI Ontology (Turtle, excerpt)\n\n"
            f"Use this for concept mapping:\n\n```turtle\n{snippet}\n```"
        )

    return (
        f"{ras_text}\n\n"
        f"---\n\n"
        f"**Begin your research now for: {target_system}**\n\n"
        f"Search systematically following the 7-session protocol in Section 8. "
        f"Use web search extensively. Document everything as you go. "
        f"When you reach saturation, produce a comprehensive research synthesis "
        f"that organises all findings by: actors, tasks, goals, capabilities, "
        f"interactions, contexts, evaluation metrics, CARE analysis, evidence IDs, "
        f"confidence levels, and knowledge gaps. This synthesis will be used to "
        f"generate the 7 output files."
        f"{ontology_section}"
    )


def _run_research_stage(
    client: "anthropic.Anthropic",
    model: str,
    target_system: str, # this is for the AI system we are using
    ras_text: str, # this has the complete prompt for the research acquisition specification (RAS) protocol from the md file in the docs folder
    ontology_text: str, # this is for loading the HI ontology from the turtle file
    max_searches: int,
) -> Tuple[str, Dict[str, int]]:
    """
    Run the agentic research loop (Stage A).

    Claude searches the web until it signals end_turn. pause_turn continuations
    are handled transparently. Returns (research_text, stage_a_stats) where
    stage_a_stats records API call count, pause_turn count, web searches, and
    cumulative token usage - used for the Phase 1 performance metrics.
    """
    system_prompt = (
        "You are a PhD-level AI research assistant and ontology engineer. "
        "Your task is systematic knowledge acquisition for a Master's thesis on "
        "Neuro-Symbolic AI for Hybrid Intelligence assessment. "
        "Follow the Research Acquisition Specification exactly. "
        "Use web search as many times as needed until saturation. "
        "Document all findings with Evidence IDs and confidence levels. "
        "Think like an ontology engineer: focus on actors, tasks, goals, "
        "capabilities, interactions, contexts, evaluation metrics, and CARE dimensions."
    )

    user_message = _build_research_prompt(target_system, ras_text, ontology_text)

    messages: List[Dict[str, Any]] = [
        {"role": "user", "content": user_message}
    ]

    web_search_tool = {
        "type": WEB_SEARCH_TOOL_TYPE,
        "name": "web_search",
        "max_uses": max_searches,
    }

    collected_texts: List[str] = []
    total_searches = 0
    pause_count = 0
    turn = 0
    total_input_tokens  = 0
    total_output_tokens = 0

    print(f"\n  [Phase 1a] Research loop starting (model={model}, max_searches={max_searches})")

    while True:
        turn += 1
        print(f"  [Phase 1a] API call #{turn} ...", end=" ", flush=True)

        # the following was a recomadation from the feedback I got from an LLM
        try:
            response = client.messages.create(
                model=model,
                max_tokens=RESEARCH_MAX_TOKENS,
                system=system_prompt,
                tools=[web_search_tool],
                messages=messages,
            )
        except anthropic.APIStatusError as e:
            print(f"\n  [Phase 1a] API error: {e}", file=sys.stderr)
            raise

        # Token usage for this turn (for the Phase 1 performance metrics)
        usage = getattr(response, "usage", None)
        if usage is not None:
            total_input_tokens  += getattr(usage, "input_tokens", 0) or 0
            total_output_tokens += getattr(usage, "output_tokens", 0) or 0

        # Collect text from this turn
        turn_text = _extract_text(response.content)
        if turn_text:
            collected_texts.append(f"### Turn {turn}\n\n{turn_text}")

        # Count searches this turn
        n_searches = _count_searches(response.content)
        total_searches += n_searches
        print(f"stop_reason={response.stop_reason}  searches={n_searches}  total={total_searches}")

        # Handle stop reason, it is important to know what caused the stop to know if it was a limit issue or if it was completed
        if response.stop_reason == "end_turn":
            print(f"  [Phase 1a] Research complete: {total_searches} total web searches")
            break

        elif response.stop_reason == "pause_turn":
            pause_count += 1
            if pause_count > MAX_PAUSE_TURNS:
                print(
                    f"  [Phase 1a] Reached pause_turn limit ({MAX_PAUSE_TURNS}) "
                    "Stopping research loop",
                    file=sys.stderr,
                )
                break
            # Here I append assistant message and continue (no user message needed)
            messages.append({"role": "assistant", "content": response.content})
            print(f"  [Phase 1a] pause_turn {pause_count}/{MAX_PAUSE_TURNS} continuing...")

        else:
            # tool_use or unexpected stop
            print(f"  [Phase 1a] Unexpected stop_reason='{response.stop_reason}' Stopping")
            # Collect whatever was produced
            messages.append({"role": "assistant", "content": response.content})
            break

    stage_a_stats = {
        "api_calls":     turn,
        "pause_turns":   pause_count,
        "web_searches":  total_searches,
        "input_tokens":  total_input_tokens,
        "output_tokens": total_output_tokens,
    }
    return "\n\n---\n\n".join(collected_texts), stage_a_stats


# Stage B: File generation

def _generation_system_prompt(target_system: str) -> str:
    return (
        f"You are an expert ontology engineer generating structured knowledge "
        f"acquisition files for a Master's thesis.\n\n"
        f"Target system: {target_system}\n"
        f"Purpose: Neuro-Symbolic AI assessment of Hybrid Intelligence quality.\n"
        f"HI Ontology: VU Amsterdam HI Ontology v2.0.0 "
        f"(namespace: https://w3id.org/hi-ontology#)\n\n"
        f"Generate ONLY the requested file content. "
        f"No preamble, no postamble, no explanatory text outside the file."
    )


def _generate_file(
    client: "anthropic.Anthropic",
    target_system: str,
    research_data: str,
    file_spec: Dict[str, str],
) -> Tuple[str, Dict[str, int]]:
    """
    Generate the content of one output file (Stage B).

    Returns (raw_file_content, token_usage_dict).
    """
    filename    = file_spec["filename"]
    label       = file_spec["label"]
    description = file_spec["description"]
    fmt         = file_spec["format"]

    user_message = (
        f"Based on the research data below, generate the file **{filename}** ({label}).\n\n"
        f"File requirements:\n{description}\n\n"
        f"Output format: {fmt}\n\n"
        f"IMPORTANT: Output ONLY the raw {fmt} content of {filename}. "
        f"Start directly with the file content - no introduction, no explanation.\n\n"
        f"---\n\n"
        f"## RESEARCH DATA\n\n"
        f"{research_data}"
    )

    # issue handling as recommended by llm
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            response = client.messages.create(
                model=GENERATION_MODEL,
                max_tokens=GENERATION_MAX_TOKENS,
                system=_generation_system_prompt(target_system),
                messages=[{"role": "user", "content": user_message}],
            )
            usage = getattr(response, "usage", None)
            usage_dict = {
                "input_tokens":  getattr(usage, "input_tokens", 0) or 0,
                "output_tokens": getattr(usage, "output_tokens", 0) or 0,
            } if usage else {"input_tokens": 0, "output_tokens": 0}

            text = _extract_text(response.content)
            if text.strip():
                return text, usage_dict
            print(f"    [Phase 1b] Empty response for {filename} (attempt {attempt}), retrying...")
        except (anthropic.RateLimitError, anthropic.APITimeoutError) as e:
            wait = 2 ** attempt
            print(f"    [Phase 1b] {type(e).__name__}: waiting {wait}s...", file=sys.stderr)
            time.sleep(wait)
        except anthropic.APIError as e:
            print(f"    [Phase 1b] API error generating {filename}: {e}", file=sys.stderr)
            if attempt == max_retries:
                raise

    raise RuntimeError(f"Failed to generate {filename} after {max_retries} attempts.")


# while costly, but I might need to regenrate files, or research so in case history matters the following is done for versioning

def _create_version_dir(config: Config) -> Path:
    version_dir = config.next_phase1_version_dir
    version_dir.mkdir(parents=True, exist_ok=True)
    return version_dir


def _load_ras_template(target_system: str) -> str:
    """Load the RAS template from docs/ and substitute the target system name"""
    ras_path = Path(__file__).resolve().parent.parent.parent / "docs" / "research_acquisition_spec.md"
    # more error handling (was needed actually)
    if not ras_path.exists():
        print(
            f"[Phase 1 ERROR] RAS template not found at: {ras_path}\n"
            "  Expected: docs/research_acquisition_spec.md",
            file=sys.stderr,
        )
        sys.exit(1)
    template = ras_path.read_text(encoding="utf-8")
    return template.replace("{target_system}", target_system)


def _load_ontology(config: Config) -> str:
    if not config.ontology_path.exists():
        return ""
    try:
        return config.ontology_path.read_text(encoding="utf-8")
    except Exception:
        return ""


# Now I will define the main entry point for Phase 1, which orchestrates the research and file generation stages

def run(config: Config) -> None:
    """
    Phase 1 entry point to be called by run_pipeline.py

    Runs Stage A (research loop) and Stage B (file generation), then copies
    the completed extractionsheet.csv to config.csv_path for Phase 2
    """
    print(f"\n{'═' * 64}")
    print(f"  Phase 1: Knowledge Acquisition  |  {config.usecase.upper()}")
    print(f"  Target system  : {config.phase1_target_system}")
    print(f"  Research model : {config.anthropic_model}")
    print(f"  Gen model      : {GENERATION_MODEL}")
    print(f"  Max searches   : {config.phase1_max_searches}")
    print(f"{'═' * 64}")

    # Check for existing versions for proper version handling
    existing = config.phase1_latest_dir
    if existing:
        print(f"\n  Existing Phase 1 data found: {existing}")
        print(f"  A new version will be created alongside it")

    # Now we create the versioned output directory
    version_dir = _create_version_dir(config)
    print(f"\n  Output directory: {version_dir}")

    # Loading inputs
    client = _get_client()
    ras_text      = _load_ras_template(config.phase1_target_system)
    ontology_text = _load_ontology(config)

    # Implementation of stage A: Research loop
    stage_a_start = time.time()

    research_data, stage_a_stats = _run_research_stage(
        client        = client,
        model         = config.anthropic_model,
        target_system = config.phase1_target_system,
        ras_text      = ras_text,
        ontology_text = ontology_text,
        max_searches  = config.phase1_max_searches,
    )

    # Saving raw research data for debugging and reference in the research_data.md file
    research_data_path = version_dir / "research_data.md"
    research_data_path.write_text(
        f"# Phase 1 Research Data\n"
        f"## Target: {config.phase1_target_system}\n\n"
        f"{research_data}",
        encoding="utf-8",
    )

    # for progress tracking and for future evaluations if needed I will track the time taken for each stage and print it out
    elapsed_a = time.time() - stage_a_start
    print(f"\n  [Phase 1a] Done in {elapsed_a:.0f}s and research saved to {research_data_path.name}")

    # more error handling, if no research data was produced, we should exit with an error 
    if not research_data.strip():
        print(
            "[Phase 1 ERROR] Stage A produced no research data "
            "Check ANTHROPIC_API_KEY and web search availability",
            file=sys.stderr,
        )
        sys.exit(1)

    # Implementation of Stage B: File generation
    print(f"\n  [Phase 1b] Generating {len(OUTPUT_FILES)} output files...")
    stage_b_start = time.time()
    generated: List[str] = []
    failed_files: List[str] = []
    stage_b_input_tokens  = 0
    stage_b_output_tokens = 0

    for i, file_spec in enumerate(OUTPUT_FILES, start=1):
        filename = file_spec["filename"]
        print(f"    [{i}/{len(OUTPUT_FILES)}] {filename} ...", end=" ", flush=True)

        try:
            content, usage = _generate_file(
                client        = client,
                target_system = config.phase1_target_system,
                research_data = research_data,
                file_spec     = file_spec,
            )
            stage_b_input_tokens  += usage.get("input_tokens", 0)
            stage_b_output_tokens += usage.get("output_tokens", 0)
        except Exception as e:
            print(f"FAILED: {e}", file=sys.stderr)
            # error placeholder so the run is traceable
            content = f"# {filename}\n\n[GENERATION FAILED: {e}]\n"
            failed_files.append(filename)

        # Strip markdown code fences if Claude wrapped the content (recommended by llm)
        content = _strip_code_fence(content, file_spec["format"])

        out_path = version_dir / filename
        out_path.write_text(content, encoding="utf-8")
        generated.append(filename)
        print(f"Success  ({len(content)} chars)")

    elapsed_b = time.time() - stage_b_start
    print(f"\n  [Phase 1b] File generation done in {elapsed_b:.0f}s")

    # The extraction sheet shall now be copied to the path used by later phases
    csv_source = version_dir / "extractionsheet.csv"
    if csv_source.exists() and csv_source.stat().st_size > 0:
        # Back up existing csv_path if it exists
        if config.csv_path.exists():
            backup = config.csv_path.with_suffix(".csv.bak")
            shutil.copy2(config.csv_path, backup)
            print(f"\n  Backed up existing CSV --> {backup.name}")

        config.csv_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(csv_source, config.csv_path)
        print(f"  Copied extractionsheet.csv --> {config.csv_path}")
    else:
        print(
            f"\n  [Phase 1 WARNING] extractionsheet.csv not found or empty in {version_dir} "
            "Phase 2 may fail",
            file=sys.stderr,
        )

    # Summary statistics for progress tracking and future evaluation
    total_elapsed = elapsed_a + elapsed_b
    print(f"\n{'─' * 64}")
    print(f"  Phase 1 complete in {total_elapsed:.0f}s")
    print(f"  Version       : {version_dir.name}")
    print(f"  Files written : {len(generated)}/{len(OUTPUT_FILES)}")
    for f in generated:
        p = version_dir / f
        size = p.stat().st_size if p.exists() else 0
        print(f"    Success {f:<30} ({size:,} bytes)")
    print(f"{'─' * 64}")

    # Performance metrics: research effort (API calls / web searches), token
    # usage across both stages, and file-generation reliability. Phase 1 is
    # versioned separately (use_cases/{usecase}/phase1/v{N}/), so the metrics
    # fragment records which version this run corresponds to.
    write_metrics(config, 1, {
        "version":                  version_dir.name,
        "stage_a_runtime_sec":      elapsed_a,
        "stage_b_runtime_sec":      elapsed_b,
        "stage_a_api_calls":        stage_a_stats["api_calls"],
        "stage_a_pause_turns":      stage_a_stats["pause_turns"],
        "web_searches":             stage_a_stats["web_searches"],
        "stage_a_input_tokens":     stage_a_stats["input_tokens"],
        "stage_a_output_tokens":    stage_a_stats["output_tokens"],
        "stage_b_input_tokens":     stage_b_input_tokens,
        "stage_b_output_tokens":    stage_b_output_tokens,
        "total_input_tokens":       stage_a_stats["input_tokens"] + stage_b_input_tokens,
        "total_output_tokens":      stage_a_stats["output_tokens"] + stage_b_output_tokens,
        "files_expected":           len(OUTPUT_FILES),
        "files_written":            len(generated),
        "files_generation_failed":  len(failed_files),
        "failed_files":             failed_files,
    })


# During runs, Claude sometimes wraps the output in markdown code fences, which can cause issues when saving files so the following was
# recommended by an LLM to strip those fences if they exist, and return the raw content only

def _strip_code_fence(content: str, fmt: str) -> str:
    """
    Remove markdown code fences that Claude sometimes wraps output in.

    E.g., ```csv\\n...content...\\n``` → ...content...
    """
    # Match ```<lang>\\n...\\n``` or ``` \\n...\\n```
    fence_pattern = re.compile(
        r"^```(?:csv|markdown|md|text|txt)?\s*\n(.*)\n```\s*$",
        re.DOTALL | re.IGNORECASE,
    )
    m = fence_pattern.match(content.strip())
    if m:
        return m.group(1)
    return content

# LLM also recommended adding dashed lines and = to make output on terminal more readable (I complained about it being compact)
