"""
Phase 6: Recommendation Generation & Final HI Assessment Report

This module consumes the gap analysis from Phase 5 and produces:

1. Per-gap recommendations: LLM generates concrete, actionable design improvements for each identified HI gap, grounded in CARE principles.

2. CARE capability-level classification: for each scenario and each CARE
   dimension, classifies the demonstrated maturity as Reactive (1), Proactive
   (2), or Social (3), adapted from the CARE capability-level tables (Hybrid
   Intelligence Centre Netherlands, 2023; cf. Akata et al. 2020), as applied
   in Zamprogno, Tiddi & Verheij (2025), "Autonomous Research Assistants for
   Hybrid Intelligence: Landscape and Challenges". The maximum admissible
   level per dimension is capped by the most severe HI gap identified in
   that dimension in Phase 5, so the classification stays grounded in the
   symbolic SHACL evidence rather than being an unconstrained LLM judgement.

3. Final HI assessment report (.md): a complete Markdown document
   containing:
     - Executive summary with HI conformance score
     - CARE dimension analysis
     - Scenario-by-scenario assessment table
     - Detailed gap analysis with recommendations
     - Consolidated recommendations by CARE dimension
     - HI Maturity Level assessment
     - CARE capability-level assessment (Reactive / Proactive / Social)
     - Methodology notes

HI Conformance Scoring
    Per-scenario score : PASS=1.0  WARNING=0.75  FAIL=0.0
    Overall score      : mean of scenario scores --> percentage
    CARE dimension     : (scenarios with no gap in that dimension) / total

CARE Capability-Level Scoring
    Per scenario, per dimension : 1 (Reactive) / 2 (Proactive) / 3 (Social)
    Ceiling                     : Critical gap -> 1, Major gap -> 2, Minor/none -> 3
    Use-case summary            : distribution + modal level per dimension (ordinal, not averaged)

Setup:
    Same OPENAI_API_KEY used in Phase 5

terminal:
    from pipeline.phase6_recommendations.recommender import run
    run(config)
"""

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from pipeline.config import Config
from pipeline.metrics import write_metrics

from openai import OpenAI, APIError, RateLimitError, APITimeoutError


DEFAULT_MODEL   = "gpt-4o-mini"
MAX_RETRIES     = 3
RETRY_DELAY_SEC = 5
TEMPERATURE     = 0.3

# HI Maturity levels based on overall score
MATURITY_LEVELS = [
    (0.90, "Level 4: Exemplary HI",
     "The system is a strong embodiment of Hybrid Intelligence principles across all "
     "CARE dimensions. Minor gaps exist but do not undermine the fundamental HI design."),
    (0.70, "Level 3: Established HI",
     "The system clearly embodies HI principles in most scenarios. Some gaps are present "
     "but the core human-AI collaboration structure is sound and well-designed."),
    (0.50, "Level 2: Emerging HI",
     "The system shows clear HI intent but has significant gaps in one or more CARE "
     "dimensions. Human-AI collaboration is present but inconsistent across scenarios."),
    (0.25, "Level 1: Partial HI",
     "The system has HI elements but fails to embody core CARE principles in a majority "
     "of scenarios. Substantial redesign is needed to achieve genuine Hybrid Intelligence."),
    (0.00, "Level 0: Pre-HI",
     "The system does not meaningfully embody Hybrid Intelligence principles. "
     "Fundamental changes to the human-AI collaboration model are required."),
]


# ─────────────────────────────────────────────────────────────────────────────
# CARE capability-level rubric (Reactive / Proactive / Social)
#
# Adapted from the CARE capability-level tables (Hybrid Intelligence Centre
# Netherlands, 2023; cf. Akata et al. 2020: "A Research Agenda for Hybrid
# Intelligence"), generalised from their domain-specific sub-capabilities
# (originally framed around scientific research assistants in Zamprogno,
# Tiddi & Verheij 2025) into descriptors applicable across the organizational
# AI systems assessed in this thesis. This rubric is deliberately separate
# from the SHACL-based CARE *conformance* score in Section 2.2 of the report:
# conformance measures whether a structural HI requirement is present at all,
# while this rubric measures the qualitative maturity of a capability that IS
# present.
# ─────────────────────────────────────────────────────────────────────────────

CARE_LEVEL_LABELS = {1: "Reactive", 2: "Proactive", 3: "Social"}

# Ceiling on the admissible level given the most severe Phase-5 gap severity
# found in that CARE dimension for a scenario. No gap in the dimension means
# no ceiling is imposed (full 1-3 range is admissible).
SEVERITY_CEILING = {"Critical": 1, "Major": 2, "Minor": 3}
DEFAULT_CEILING  = 3

CARE_LEVEL_RUBRIC: Dict[str, Dict[str, Any]] = {
    "Collaborative": {
        1: "The AI agent participates in the interaction only when invoked by the human; "
           "it does not initiate contact, form its own sub-goals, or select who/what to "
           "coordinate with.",
        2: "The AI agent initiates parts of the collaboration on its own - surfacing "
           "suggestions, options, or actions without being explicitly prompted - and "
           "establishes a shared awareness of the situation with the human.",
        3: "The AI agent actively maintains and repairs the collaborative relationship over "
           "time (e.g. resolving conflicts, sustaining coordination across sessions) and "
           "demonstrates a common, mutually-verified understanding of the situation with its "
           "human partner(s).",
    },
    "Adaptive": {
        1: "The system changes its behaviour only in response to explicit instruction or "
           "explicit correction from a human.",
        2: "The system adapts based on implicit feedback (usage patterns, interaction "
           "history) and anticipates likely human needs or upcoming situations without "
           "being told.",
        3: "The system shows flexible, ongoing adaptation across multiple human and/or AI "
           "partners and changing circumstances, learning online from both expected and "
           "surprising changes.",
    },
    "Responsible": {
        1: "The system applies a fixed set of rules, policies, or constraints without "
           "surfacing or questioning them.",
        2: "The system can identify and surface the grounds for a decision and flags or "
           "reflects on the legal, ethical, or quality acceptability of its own behaviour.",
        3: "The system engages in a two-way dialogue with humans about the acceptability of "
           "its decisions and contributes evidence that is used to improve the underlying "
           "rules or policies over time.",
    },
    "Explainable": {
        1: "Explanations are fixed and generic, not adapted to the specific user, decision, "
           "or context.",
        2: "Explanations are tailored to the specific user, task, or decision being made.",
        3: "Explanations support an interactive, two-way exchange that builds a shared "
           "understanding between the human and the AI (e.g. the human can question or "
           "probe the explanation and receive a responsive answer).",
    },
}


SYSTEM_PROMPT_RECS = """\
You are a Hybrid Intelligence systems designer specialising in the CARE framework (Collaborative, Adaptive, Responsible, Explainable) and the HI Ontology (VU Amsterdam).

You receive identified HI gaps in a real-world AI system. For each gap, you generate one concrete, actionable recommendation that would address it. Recommendations must be:
- Specific to the gap (not generic HI advice)
- Actionable for a product/engineering team
- Grounded in the CARE principle that is violated
- Realistic given the system's existing architecture

Respond with valid JSON only"""

SYSTEM_PROMPT_EXEC = """\
You are a Hybrid Intelligence assessment expert writing an executive summary for a formal HI conformance report.

You receive a complete gap analysis of a real-world AI system assessed against the HI Ontology (VU Amsterdam) and CARE principles. Write a concise executive summary (200-280 words) that:
- States the system's overall HI conformance level and score
- Identifies the primary CARE strength(s)
- Identifies the primary CARE gap(s) with their significance
- Gives an overall assessment of the system as an HI system
- Ends with a forward-looking sentence about improvement potential

Be precise and analytical. This is for a Master's thesis in HI systems assessment. Respond with plain text only (no JSON, no markdown headers)."""

SYSTEM_PROMPT_CARE_LEVELS = """\
You are a Hybrid Intelligence assessment expert classifying the maturity of a system's CARE capabilities using a fixed three-level rubric (1=Reactive, 2=Proactive, 3=Social).

You will be given, for one scenario: the rubric descriptors for each of the four CARE dimensions, the SHACL/gap evidence recorded for that scenario in each dimension, and the maximum level admissible per dimension (a hard ceiling derived from gap severity - you must never exceed it).

Rules you must follow:
- Base every classification ONLY on the evidence provided. Do not invent facts about the system.
- Never assign a level higher than the given ceiling for that dimension, even if the evidence seems to support it.
- If evidence is limited or absent for a dimension, choose the lower, more conservative level within the admissible range and say so explicitly in the justification.
- Each justification must be one sentence and must reference the specific evidence (or lack of it) that grounds the classification.

Respond with valid JSON only."""



# Scoring

def _compute_scores(
    shacl_scenarios: Dict[str, Dict],
    gap_scenarios: Dict[str, Dict],
) -> Tuple[float, Dict[str, float]]:
    scenario_scores = []
    care_gap_counts: Dict[str, int] = {
        "Collaborative": 0, "Adaptive": 0,
        "Responsible": 0, "Explainable": 0,
    }
    total_scenarios = len(shacl_scenarios)

    for sc_id, sc_data in shacl_scenarios.items():
        status = sc_data.get("status", "PASS")
        scenario_scores.append(1.0 if status == "PASS" else 0.75 if status == "WARNING" else 0.0)

        gaps = gap_scenarios.get(sc_id, {}).get("gaps", [])
        dims_hit = {g.get("care_dimension") for g in gaps}
        for dim in care_gap_counts:
            if dim in dims_hit:
                care_gap_counts[dim] += 1

    overall = sum(scenario_scores) / total_scenarios if total_scenarios else 0.0
    care_scores = {
        dim: (total_scenarios - count) / total_scenarios
        for dim, count in care_gap_counts.items()
    }
    return overall, care_scores


def _maturity_level(score: float) -> Tuple[str, str]:
    # Returns (maturity_label, maturity_description) for a conformance score
    for threshold, label, desc in MATURITY_LEVELS:
        if score >= threshold:
            return label, desc
    return MATURITY_LEVELS[-1][1], MATURITY_LEVELS[-1][2]


def _severity_ceiling(gaps_for_dim: List[Dict]) -> int:
    """
    Returns the maximum CARE level (1-3) admissible for a dimension given the
    gaps recorded against it. The most severe gap present is the binding
    constraint (Critical -> 1, Major -> 2, Minor -> 3); no gaps -> no ceiling.
    """
    if not gaps_for_dim:
        return DEFAULT_CEILING
    return min(
        SEVERITY_CEILING.get(g.get("severity"), DEFAULT_CEILING)
        for g in gaps_for_dim
    )



# LLM callers

def _call_llm(
    client: OpenAI,
    model: str,
    system: str,
    user: str,
    json_mode: bool = True,
) -> Tuple[Optional[str], Optional[Dict[str, int]]]:
    """
    Returns (response_text, token_usage_dict). token_usage_dict is None only
    when every retry failed outright (rate limit / timeout / API error
    exhausted); it is still returned alongside a successful response_text so
    callers can accumulate token usage for the performance metrics.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            kwargs: Dict[str, Any] = dict(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user",   "content": user},
                ],
                temperature=TEMPERATURE,
                max_tokens=2000,
            )
            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}
            response = client.chat.completions.create(**kwargs)

            usage = getattr(response, "usage", None)
            usage_dict = {
                "prompt_tokens":     getattr(usage, "prompt_tokens", 0) or 0,
                "completion_tokens": getattr(usage, "completion_tokens", 0) or 0,
            } if usage else {"prompt_tokens": 0, "completion_tokens": 0}

            return response.choices[0].message.content.strip(), usage_dict

        except RateLimitError:
            wait = RETRY_DELAY_SEC * attempt
            print(f"    [Rate limit] Waiting {wait}s ...")
            time.sleep(wait)
        except APITimeoutError:
            print(f"    [Timeout] Retry {attempt}/{MAX_RETRIES} ...")
            time.sleep(RETRY_DELAY_SEC)
        except APIError as e:
            print(f"    [API error] {e}")
            time.sleep(RETRY_DELAY_SEC)

    return None, None


def _generate_recommendations(
    client: OpenAI,
    model: str,
    usecase: str,
    sc_id: str,
    label: str,
    gaps: List[Dict],
) -> Tuple[List[Dict], Dict[str, int], bool]:
    """Returns (recommendations, token_usage, fallback_used)."""
    gaps_text = json.dumps(gaps, indent=2)

    user_prompt = f"""Generate one concrete recommendation for each HI gap identified in scenario '{label}' of the '{usecase}' assessment.

## Gaps to address
{gaps_text}

## Output schema
Return a JSON object with this exact structure:
{{
  "recommendations": [
    {{
      "gap_id": "<same gap_id as in input>",
      "recommendation_title": "<imperative, max 10 words>",
      "recommendation": "<2-3 sentences: what change to make and why it addresses the gap>",
      "implementation_guidance": "<1-2 sentences: how to implement - concrete and specific>",
      "priority": "<High|Medium|Low>",
      "expected_hi_impact": "<1 sentence: what HI property improves and how>"
    }}
  ]
}}

One recommendation per gap_id. Priority: High = Critical gap, Medium = Major, Low = Minor."""

    raw, usage = _call_llm(client, model, SYSTEM_PROMPT_RECS, user_prompt, json_mode=True)
    usage = usage or {"prompt_tokens": 0, "completion_tokens": 0}
    if raw is None:
        return _fallback_recommendations(gaps), usage, True

    try:
        data = json.loads(raw)
        return data.get("recommendations", []), usage, False
    except json.JSONDecodeError:
        return _fallback_recommendations(gaps), usage, True


def _generate_executive_summary(
    client: OpenAI,
    model: str,
    usecase: str,
    overall_score: float,
    care_scores: Dict[str, float],
    maturity_label: str,
    gap_analysis: Dict,
) -> Tuple[str, Dict[str, int], bool]:
    """Generate a prose executive summary for the final report.
    Returns (summary_text, token_usage, fallback_used)."""
    care_str = "  ".join(
        f"{dim}: {score*100:.0f}%"
        for dim, score in care_scores.items()
    )
    total_gaps = gap_analysis.get("total_gaps", 0)
    scenarios_with_gaps = gap_analysis.get("scenarios_with_gaps", 0)
    total_scenarios = gap_analysis.get("total_scenarios", 0)

    # Collect gap titles for context
    gap_titles = []
    for sc_data in gap_analysis.get("scenarios", {}).values():
        for g in sc_data.get("gaps", []):
            gap_titles.append(
                f"[{g.get('care_dimension','?')}] {g.get('gap_title','?')}"
            )

    user_prompt = f"""Write an executive summary for the HI assessment report for '{usecase}'.

Assessment data:
- Overall HI Conformance Score: {overall_score*100:.1f}%
- HI Maturity Level: {maturity_label}
- Total scenarios assessed: {total_scenarios}
- Scenarios with HI gaps: {scenarios_with_gaps}
- Total gaps identified: {total_gaps}
- CARE dimension scores: {care_str}
- Identified gaps: {'; '.join(gap_titles) if gap_titles else 'None'}

Write the executive summary now (200-280 words, plain text, no markdown)."""

    text, usage = _call_llm(client, model, SYSTEM_PROMPT_EXEC, user_prompt, json_mode=False)
    usage = usage or {"prompt_tokens": 0, "completion_tokens": 0}
    if text:
        return text, usage, False
    return _fallback_executive_summary(usecase, overall_score, maturity_label, total_gaps), usage, True


def _generate_care_levels(
    client: OpenAI,
    model: str,
    usecase: str,
    sc_id: str,
    label: str,
    dim_gaps: Dict[str, List[Dict]],
) -> Tuple[Dict[str, Dict], Dict[str, int], bool]:
    """
    Classifies this scenario's demonstrated CARE capability level (1=Reactive,
    2=Proactive, 3=Social) for each of the four CARE dimensions, using only the
    SHACL/gap evidence already produced by Phases 4-5. The ceiling per
    dimension is computed deterministically (see _severity_ceiling) and passed
    to the LLM as a hard constraint; the response is also clamped in code as a
    safety net in case the model does not respect it.

    Returns (care_levels, token_usage, fallback_used).
    """
    ceilings = {dim: _severity_ceiling(dim_gaps.get(dim, [])) for dim in CARE_LEVEL_RUBRIC}

    rubric_text   = json.dumps(CARE_LEVEL_RUBRIC, indent=2)
    gaps_text     = (
        json.dumps(dim_gaps, indent=2)
        if any(dim_gaps.values())
        else "No HI gaps were identified in any CARE dimension for this scenario."
    )
    ceilings_text = json.dumps(ceilings, indent=2)

    user_prompt = f"""Classify the demonstrated CARE capability level of scenario '{label}' ('{usecase}') for each CARE dimension, using ONLY the evidence below.

## CARE level rubric (keys are level numbers: 1=Reactive, 2=Proactive, 3=Social)
{rubric_text}

## SHACL/gap evidence for this scenario, grouped by CARE dimension
{gaps_text}

## Maximum admissible level per dimension (hard ceiling - do not exceed)
{ceilings_text}

## Output schema
Return a JSON object with this exact structure:
{{
  "care_levels": {{
    "Collaborative": {{"level": <int 1-3>, "level_label": "<Reactive|Proactive|Social>", "justification": "<one sentence citing the evidence above>"}},
    "Adaptive":      {{"level": <int 1-3>, "level_label": "<...>", "justification": "<...>"}},
    "Responsible":   {{"level": <int 1-3>, "level_label": "<...>", "justification": "<...>"}},
    "Explainable":   {{"level": <int 1-3>, "level_label": "<...>", "justification": "<...>"}}
  }}
}}"""

    raw, usage = _call_llm(client, model, SYSTEM_PROMPT_CARE_LEVELS, user_prompt, json_mode=True)
    usage = usage or {"prompt_tokens": 0, "completion_tokens": 0}
    if raw is None:
        return _fallback_care_levels(ceilings), usage, True

    try:
        data   = json.loads(raw)
        levels = data.get("care_levels", {})
        fallback = _fallback_care_levels(ceilings)
        any_fallback_field = False

        for dim, ceiling in ceilings.items():
            entry = levels.get(dim)
            if not entry or "level" not in entry:
                levels[dim] = fallback[dim]
                any_fallback_field = True
                continue
            # Safety-net clamp: never allow the LLM to exceed the computed ceiling
            clamped_level = max(1, min(int(entry.get("level", ceiling)), ceiling))
            entry["level"] = clamped_level
            entry["level_label"] = CARE_LEVEL_LABELS[clamped_level]
            entry.setdefault("justification", "")
        return levels, usage, any_fallback_field
    except (json.JSONDecodeError, ValueError, TypeError):
        return _fallback_care_levels(ceilings), usage, True



# Fallbacks (when LLM is unavailable)

def _fallback_recommendations(gaps: List[Dict]) -> List[Dict]:
    return [
        {
            "gap_id":                g["gap_id"],
            "recommendation_title":  f"Address {g.get('component', 'gap')}",
            "recommendation":        f"Redesign the interaction to include both human and AI agents. {g.get('gap_description','')}",
            "implementation_guidance": "Review interaction design and ensure both agent types are co-participants.",
            "priority":              "High" if g.get("severity") == "Critical" else "Medium",
            "expected_hi_impact":    f"Improves {g.get('care_dimension','HI')} conformance.",
        }
        for g in gaps
    ]


def _fallback_executive_summary(
    usecase: str, score: float, maturity: str, total_gaps: int
) -> str:
    return (
        f"The {usecase} system achieved an overall HI conformance score of "
        f"{score*100:.1f}% ({maturity}). {total_gaps} gap(s) were identified "
        "requiring attention to improve Hybrid Intelligence conformance."
    )


def _fallback_care_levels(ceilings: Dict[str, int]) -> Dict[str, Dict]:
    """
    Deterministic fallback used when the LLM call fails. Conservatively caps
    at Level 2 (Proactive) even when the ceiling allows Level 3, since
    confirming "Social"-level behaviour requires qualitative judgement that
    this fallback cannot provide.
    """
    return {
        dim: {
            "level": min(ceiling, 2),
            "level_label": CARE_LEVEL_LABELS[min(ceiling, 2)],
            "justification": (
                "Fallback classification (LLM unavailable): capped conservatively "
                "pending manual qualitative review."
            ),
        }
        for dim, ceiling in ceilings.items()
    }



# CARE capability-level aggregation (deterministic, no LLM)

def _care_level_summary(
    care_levels_by_scenario: Dict[str, Dict[str, Dict]],
) -> Dict[str, Dict]:
    """
    Aggregates per-scenario CARE levels into a use-case-level summary for each
    dimension. Levels are an ordinal scale (Reactive < Proactive < Social), not
    an interval one, so this reports the full distribution and the modal
    (most frequent) level rather than an average/mean level.
    """
    summary: Dict[str, Dict] = {}
    for dim in CARE_LEVEL_RUBRIC:
        counts = {1: 0, 2: 0, 3: 0}
        for sc_levels in care_levels_by_scenario.values():
            lvl = sc_levels.get(dim, {}).get("level", 1)
            counts[lvl] = counts.get(lvl, 0) + 1
        modal_level = max(counts, key=counts.get) if any(counts.values()) else 1
        summary[dim] = {
            "distribution": counts,
            "modal_level": modal_level,
            "modal_label": CARE_LEVEL_LABELS[modal_level],
        }
    return summary



# Markdown report builder made with LLM completley

_SCORE_BAR_WIDTH = 30

def _score_bar(score: float) -> str:
    filled = round(score * _SCORE_BAR_WIDTH)
    empty  = _SCORE_BAR_WIDTH - filled
    return f"[{'█' * filled}{'░' * empty}] {score*100:.1f}%"


def _status_icon(status: str) -> str:
    return {"PASS": "✅", "WARNING": "⚠️", "FAIL": "❌"}.get(status, "❓")


def _severity_badge(severity: str) -> str:
    return {"Critical": "🔴 Critical", "Major": "🟠 Major",
            "Minor": "🟡 Minor"}.get(severity, severity)


def _build_markdown_report(
    config: Config,
    shacl_report: Dict,
    gap_analysis: Dict,
    recommendations_by_scenario: Dict[str, List[Dict]],
    executive_summary: str,
    overall_score: float,
    care_scores: Dict[str, float],
    maturity_label: str,
    maturity_desc: str,
    model: str,
    care_levels_by_scenario: Dict[str, Dict[str, Dict]],
    care_level_summary: Dict[str, Dict],
) -> str:
    """Assemble the complete Markdown assessment report."""

    shacl_scenarios = shacl_report.get("scenarios", {})
    gap_scenarios   = gap_analysis.get("scenarios", {})
    all_ids         = sorted(shacl_scenarios.keys())
    usecase         = config.usecase.upper()
    now             = datetime.now().strftime("%Y-%m-%d")

    lines: List[str] = []

    # ── Title ─────────────────────────────────────────────────────────────────
    lines += [
        f"# HI Assessment Report: {usecase}",
        f"",
        f"**Assessment Date:** {now}  ",
        f"**HI Ontology Version:** 2.0.0 (VU Amsterdam)  ",
        f"**Pipeline:** Neuro-Symbolic HI Assessment Pipeline  ",
        f"**LLM Model:** {model}  ",
        f"",
        "---",
        "",
    ]

    # ── Executive Summary ──────────────────────────────────────────────────────
    lines += [
        "## 1. Executive Summary",
        "",
        executive_summary,
        "",
        "---",
        "",
    ]

    # ── HI Conformance Overview ────────────────────────────────────────────────
    total_s    = shacl_report.get("total_scenarios", 0)
    pass_s     = shacl_report.get("pass", 0)
    warning_s  = shacl_report.get("warning", 0)
    fail_s     = shacl_report.get("fail", 0)
    total_gaps = gap_analysis.get("total_gaps", 0)

    lines += [
        "## 2. HI Conformance Overview",
        "",
        "### 2.1 Overall Score",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Overall HI Conformance | {_score_bar(overall_score)} |",
        f"| HI Maturity Level | **{maturity_label}** |",
        f"| Scenarios Assessed | {total_s} |",
        f"| Scenarios PASS | {pass_s} ({pass_s/total_s*100:.0f}%) |",
        f"| Scenarios WARNING | {warning_s} |",
        f"| Scenarios FAIL | {fail_s} ({fail_s/total_s*100:.0f}%) |",
        f"| Total HI Gaps | {total_gaps} |",
        "",
        f"> {maturity_desc}",
        "",
    ]

    # CARE dimension scores
    lines += [
        "### 2.2 CARE Dimension Analysis",
        "",
        "| Dimension | Score | Interpretation |",
        "|-----------|-------|----------------|",
    ]
    care_interp = {
        "Collaborative": "Human and AI agents co-participate in interactions",
        "Adaptive":      "Feedback loops and learning mechanisms",
        "Responsible":   "Oversight, fairness, and accountability",
        "Explainable":   "AI transparency and decision explanation",
    }
    for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable"]:
        score = care_scores.get(dim, 1.0)
        interp = care_interp.get(dim, "")
        icon = "✅" if score >= 1.0 else ("⚠️" if score >= 0.5 else "❌")
        lines.append(
            f"| **{dim}** | {icon} {score*100:.0f}% | {interp} |"
        )
    lines += [""]

    # Scenario overview table
    lines += [
        "### 2.3 Scenario Overview",
        "",
        "| Scenario | Label | Status | Gaps |",
        "|----------|-------|--------|------|",
    ]
    for sc_id in all_ids:
        sc      = shacl_scenarios[sc_id]
        label   = sc.get("label", sc_id.upper())
        status  = sc.get("status", "PASS")
        icon    = _status_icon(status)
        n_gaps  = len(gap_scenarios.get(sc_id, {}).get("gaps", []))
        gap_str = str(n_gaps) if n_gaps else "-"
        lines.append(f"| {sc_id.upper()} | {label} | {icon} {status} | {gap_str} |")

    lines += ["", "---", ""]

    # ── Detailed Scenario Analysis ─────────────────────────────────────────────
    lines += ["## 3. Detailed Scenario Analysis", ""]

    for sc_id in all_ids:
        sc_shacl = shacl_scenarios[sc_id]
        sc_gap   = gap_scenarios.get(sc_id, {})
        label    = sc_shacl.get("label", sc_id.upper())
        status   = sc_shacl.get("status", "PASS")
        icon     = _status_icon(status)
        gaps     = sc_gap.get("gaps", [])
        recs     = recommendations_by_scenario.get(sc_id, [])

        lines += [
            f"### {sc_id.upper()} - {label}",
            "",
            f"**Status:** {icon} {status}  ",
            f"**HI Gaps:** {len(gaps)}  ",
            "",
        ]

        # Overall assessment from Phase 5
        overall_assess = sc_gap.get("overall_assessment", "")
        if overall_assess:
            lines += [f"> {overall_assess}", ""]

        # CARE capability levels for this scenario
        sc_care_levels = care_levels_by_scenario.get(sc_id, {})
        if sc_care_levels:
            lines += [
                "**CARE Capability Levels** (1=Reactive, 2=Proactive, 3=Social):",
                "",
                "| Dimension | Level | Rationale |",
                "|-----------|-------|-----------|",
            ]
            for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable"]:
                entry = sc_care_levels.get(dim, {})
                lvl   = entry.get("level", "?")
                lbl   = entry.get("level_label", "?")
                just  = entry.get("justification", "")
                lines.append(f"| {dim} | {lvl} - {lbl} | {just} |")
            lines += [""]

        if not gaps:
            lines += [
                "All HI conformance checks passed. This scenario demonstrates "
                "well-structured human-AI collaboration across all CARE dimensions.",
                "",
            ]
        else:
            for gap in gaps:
                gap_id  = gap.get("gap_id", "?")
                g_title = gap.get("gap_title", "?")
                g_dim   = gap.get("care_dimension", "?")
                g_sev   = gap.get("severity", "?")
                g_desc  = gap.get("gap_description", "")
                g_princ = gap.get("hi_principle_violated", "")
                g_imp   = gap.get("practical_impact", "")

                # Find matching recommendation
                rec = next((r for r in recs if r.get("gap_id") == gap_id), None)

                lines += [
                    f"#### Gap {gap_id}: {g_title}",
                    "",
                    f"| Property | Value |",
                    f"|----------|-------|",
                    f"| CARE Dimension | **{g_dim}** |",
                    f"| Severity | {_severity_badge(g_sev)} |",
                    f"| HI Principle Violated | {g_princ} |",
                    "",
                    f"**Gap Description**",
                    f"> {g_desc}",
                    "",
                    f"**Practical Impact**",
                    f"> {g_imp}",
                    "",
                ]

                if rec:
                    r_title = rec.get("recommendation_title", "")
                    r_text  = rec.get("recommendation", "")
                    r_impl  = rec.get("implementation_guidance", "")
                    r_prio  = rec.get("priority", "")
                    r_himp  = rec.get("expected_hi_impact", "")

                    lines += [
                        f"**Recommendation: {r_title}**",
                        "",
                        r_text,
                        "",
                        f"*Implementation:* {r_impl}",
                        "",
                        f"*Priority:* {r_prio} | *Expected HI Impact:* {r_himp}",
                        "",
                    ]

    lines += ["---", ""]

    # ── Consolidated Recommendations ───────────────────────────────────────────
    lines += ["## 4. Consolidated Recommendations", ""]

    # Group by CARE dimension
    all_recs_by_dim: Dict[str, List[Tuple[str, Dict, Dict]]] = {}
    for sc_id in all_ids:
        sc_gap = gap_scenarios.get(sc_id, {})
        recs   = recommendations_by_scenario.get(sc_id, [])
        label  = shacl_scenarios[sc_id].get("label", sc_id.upper())
        for gap in sc_gap.get("gaps", []):
            gap_id = gap.get("gap_id", "?")
            dim    = gap.get("care_dimension", "General")
            rec    = next((r for r in recs if r.get("gap_id") == gap_id), None)
            if rec:
                all_recs_by_dim.setdefault(dim, []).append((label, gap, rec))

    for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable"]:
        entries = all_recs_by_dim.get(dim, [])
        if not entries:
            continue
        lines += [f"### {dim} Dimension", ""]
        for label, gap, rec in entries:
            lines += [
                f"- **[{rec.get('priority','?')} Priority] {rec.get('recommendation_title','?')}**  ",
                f"  *Scenario:* {label}  ",
                f"  {rec.get('recommendation','')}  ",
                f"  *Implementation:* {rec.get('implementation_guidance','')}",
                "",
            ]

    lines += ["---", ""]

    # ── HI Maturity Assessment ─────────────────────────────────────────────────
    lines += [
        "## 5. HI Maturity Assessment",
        "",
        f"**Maturity Level: {maturity_label}**",
        "",
        maturity_desc,
        "",
        "| CARE Dimension | Score | Status |",
        "|----------------|-------|--------|",
    ]
    for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable"]:
        score = care_scores.get(dim, 1.0)
        status_txt = "Strong" if score >= 0.9 else ("Adequate" if score >= 0.6 else "Needs Work")
        lines.append(f"| {dim} | {score*100:.0f}% | {status_txt} |")

    lines += [
        "",
        "### Strengths",
        "",
    ]
    strong_dims = [d for d, s in care_scores.items() if s >= 0.9]
    if strong_dims:
        for d in strong_dims:
            lines.append(f"- **{d}**: {care_interp[d]}")
    else:
        lines.append("- No dimension achieved full conformance in this assessment.")

    lines += ["", "### Areas for Improvement", ""]
    weak_dims = [d for d, s in care_scores.items() if s < 0.9]
    if weak_dims:
        for d in weak_dims:
            lines.append(f"- **{d}** ({care_scores[d]*100:.0f}%): See recommendations in Section 4.")
    else:
        lines.append("- All dimensions meet the conformance threshold.")

    lines += ["", "---", ""]

    # ── CARE Capability-Level Assessment ───────────────────────────────────────
    lines += [
        "## 6. CARE Capability-Level Assessment (Reactive / Proactive / Social)",
        "",
        "This section complements the score-based maturity level in Section 5 with a "
        "finer-grained, literature-grounded assessment of *how* each CARE dimension is "
        "demonstrated, adapted from the CARE capability-level tables (Hybrid Intelligence "
        "Centre Netherlands, 2023; cf. Akata et al. 2020; Zamprogno, Tiddi & Verheij 2025). "
        "Each scenario is classified per CARE dimension into one of three levels: "
        "**1 - Reactive** (the capability is only exercised upon explicit human "
        "instruction), **2 - Proactive** (the AI initiates or anticipates without being "
        "explicitly prompted), or **3 - Social** (the capability is sustained, repaired, or "
        "co-constructed over time with the human partner). The maximum level admissible for "
        "a dimension in a given scenario is capped by the most severe HI gap identified in "
        "that dimension in Phase 5 (Critical → capped at 1, Major → capped at 2, Minor/none "
        "→ uncapped at 3), so the classification stays grounded in the symbolic SHACL "
        "evidence rather than unconstrained LLM judgement. This is distinct from the "
        "conformance score in Section 2.2, which measures whether a capability is present "
        "at all, not how maturely it is exercised.",
        "",
        "### 6.1 Per-Scenario CARE Levels",
        "",
        "| Scenario | Collaborative | Adaptive | Responsible | Explainable |",
        "|----------|----------------|----------|--------------|-------------|",
    ]
    for sc_id in all_ids:
        sc_levels = care_levels_by_scenario.get(sc_id, {})
        label     = shacl_scenarios[sc_id].get("label", sc_id.upper())
        cells = []
        for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable"]:
            entry = sc_levels.get(dim, {})
            cells.append(f"{entry.get('level','?')} ({entry.get('level_label','?')})")
        lines.append(f"| {sc_id.upper()} - {label[:35]} | " + " | ".join(cells) + " |")

    lines += [
        "",
        "### 6.2 Use-Case CARE Maturity Summary",
        "",
        "Levels are an ordinal scale (Reactive < Proactive < Social), so the table below "
        "reports the distribution and the modal (most frequent) level per dimension across "
        "all scenarios rather than an average.",
        "",
        "| Dimension | Level 1 (Reactive) | Level 2 (Proactive) | Level 3 (Social) | Modal Level |",
        "|-----------|---------------------|----------------------|--------------------|-------------|",
    ]
    for dim in ["Collaborative", "Adaptive", "Responsible", "Explainable"]:
        s    = care_level_summary.get(dim, {})
        dist = s.get("distribution", {1: 0, 2: 0, 3: 0})
        lines.append(
            f"| {dim} | {dist.get(1,0)} | {dist.get(2,0)} | {dist.get(3,0)} | "
            f"**{s.get('modal_level','?')} - {s.get('modal_label','?')}** |"
        )

    lines += ["", "---", ""]

    # ── Methodology ───────────────────────────────────────────────────────────
    lines += [
        "## 7. Methodology",
        "",
        "This report was produced by a **Neuro-Symbolic HI Assessment Pipeline** "
        "developed as part of a Master's thesis on Hybrid Intelligence systems evaluation.",
        "",
        "### Pipeline Phases",
        "",
        "| Phase | Method | Output |",
        "|-------|--------|--------|",
        "| 1 - Knowledge Acquisition | Literature review, public documentation analysis | Extraction sheets |",
        "| 2 - KG Construction | RDFLib mapping to HI Ontology (VU Amsterdam) | RDF Knowledge Graph (Turtle) |",
        "| 3 - Normalization | SHACL structural validation (pySHACL) | Normalization report (JSON) |",
        "| 4 - SHACL Conformance | SHACL-SPARQL semantic validation against CARE shapes | Conformance report (JSON + TTL) |",
        "| 5 - Gap Analysis | **Neuro-symbolic**: LLM interprets SHACL violations | Gap analysis (JSON) |",
        "| 6 - Recommendations | LLM generates actionable design improvements and classifies CARE capability levels | Assessment report (Markdown) |",
        "",
        "### Neuro-Symbolic Design",
        "",
        "The neuro-symbolic paradigm is applied in Phases 5–6: the **symbolic** component "
        "(SHACL constraint engine) formally identifies which HI properties are absent or "
        "violated, producing structured symbolic output. The **neural** component (LLM) "
        "then interprets these formal violations, reasoning about their significance in "
        "the context of HI theory to produce human-readable gap analysis and recommendations. "
        "The LLM does not generate descriptions from a feature list - it performs semantic "
        "reasoning over formal constraint violations. The CARE capability-level "
        "classification in Section 6 follows the same principle: the LLM only selects a "
        "level within a ceiling that is computed deterministically from the symbolic gap "
        "severities.",
        "",
        "### HI Ontology",
        "",
        "**HI Ontology v2.0.0**, VU Amsterdam (2024).  ",
        "Namespace: `https://w3id.org/hi-ontology#`  ",
        "Key classes: UseCase, HITeam, HumanAgent, ArtificialAgent, Goal, Task, "
        "Capability, Context, Interaction, TaskExecution, Evaluation.",
        "",
        "### Scoring",
        "",
        "- **Per-scenario**: PASS = 1.0, WARNING = 0.75, FAIL = 0.0",
        "- **Overall score**: mean of per-scenario scores",
        "- **CARE score**: proportion of scenarios with no gap in that dimension",
        "- **CARE capability level**: 1 (Reactive) / 2 (Proactive) / 3 (Social) per scenario "
        "per dimension, LLM-classified from Phase 4/5 evidence and capped by gap severity "
        "(Critical → 1, Major → 2, Minor/none → 3); aggregated across scenarios by mode, "
        "not by average, since the scale is ordinal (see Section 6.2)",
        "",
        "---",
        "",
        f"*Report generated on {now} by the HI Assessment Pipeline.*",
    ]

    return "\n".join(lines)



# terminal output

def run(config: Config) -> None:

    print("\n" + "=" * 62)
    print(f"  PHASE 6: Recommendation Generation  |  {config.usecase.upper()}")
    print("=" * 62)

    # verifying phase 4 and 5
    for path, label in [
        (config.shacl_report_path, "SHACL report (Phase 4)"),
        (config.gap_analysis_path, "Gap analysis (Phase 5)"),
    ]:
        if not path.exists():
            print(f"[Phase 6 ERROR] {label} not found: {path}", file=sys.stderr)
            sys.exit(1)

    # Loading Phase 4 and Phase 5 outputs
    print(f"[Phase 6] Loading SHACL report  : {config.shacl_report_path}")
    with open(config.shacl_report_path, "r", encoding="utf-8") as f:
        shacl_report = json.load(f)

    print(f"[Phase 6] Loading gap analysis  : {config.gap_analysis_path}")
    with open(config.gap_analysis_path, "r", encoding="utf-8") as f:
        gap_analysis = json.load(f)

    # computing scores
    overall_score, care_scores = _compute_scores(shacl_report.get("scenarios", {}),gap_analysis.get("scenarios", {}),)
    maturity_label, maturity_desc = _maturity_level(overall_score)

    print(f"[Phase 6] Overall score         : {overall_score*100:.1f}%  ({maturity_label})")
    for dim, score in care_scores.items():
        print(f"          {dim:<15}: {score*100:.0f}%")

    # LLM client initialization
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key: # recommended by llm
        print(
            "\n[Phase 6 ERROR] OPENAI_API_KEY is not set.\n"
            "  export OPENAI_API_KEY='sk-...'",
            file=sys.stderr,
        )
        sys.exit(1)

    model  = os.environ.get("LLM_MODEL", DEFAULT_MODEL).strip()
    client = OpenAI(api_key=api_key)
    print(f"[Phase 6] LLM model             : {model}")
    print()

    # Performance tracking (see pipeline/metrics.py): cumulative token usage
    # and how often each LLM-driven step fell back to its non-LLM default.
    total_prompt_tokens      = 0
    total_completion_tokens  = 0
    recommendation_calls     = 0
    recommendation_fallbacks = 0
    care_level_calls         = 0
    care_level_fallbacks     = 0

    # Generate recommendations per scenario
    shacl_scenarios = shacl_report.get("scenarios", {})
    gap_scenarios   = gap_analysis.get("scenarios", {})
    all_ids         = sorted(shacl_scenarios.keys())
    recommendations_by_scenario: Dict[str, List[Dict]] = {}

    for sc_id in all_ids:
        sc_gap = gap_scenarios.get(sc_id, {})
        gaps   = sc_gap.get("gaps", [])
        label  = shacl_scenarios[sc_id].get("label", sc_id.upper())

        if not gaps:
            recommendations_by_scenario[sc_id] = []
            print(f"  ✓ [{sc_id.upper()}] {label[:50]} - no gaps, skipping")
            continue

        print(f"  ✗ [{sc_id.upper()}] {label[:48]}")
        print(f"      {len(gaps)} gap(s) → generating recommendation(s) ...")
        recommendation_calls += 1
        recs, usage, fell_back = _generate_recommendations(
            client, model, config.usecase, sc_id, label, gaps
        )
        total_prompt_tokens     += usage.get("prompt_tokens", 0)
        total_completion_tokens += usage.get("completion_tokens", 0)
        if fell_back:
            recommendation_fallbacks += 1
        recommendations_by_scenario[sc_id] = recs
        print(f"      → {len(recs)} recommendation(s) generated"
              + ("  [FALLBACK]" if fell_back else ""))

    # Generate CARE capability-level classification (Reactive / Proactive / Social)
    print("\n[Phase 6] Classifying CARE capability levels ...")
    care_levels_by_scenario: Dict[str, Dict[str, Dict]] = {}

    for sc_id in all_ids:
        sc_gap = gap_scenarios.get(sc_id, {})
        label  = shacl_scenarios[sc_id].get("label", sc_id.upper())

        # Group this scenario's Phase 5 gaps by CARE dimension
        dim_gaps: Dict[str, List[Dict]] = {dim: [] for dim in CARE_LEVEL_RUBRIC}
        for gap in sc_gap.get("gaps", []):
            dim = gap.get("care_dimension")
            if dim in dim_gaps:
                dim_gaps[dim].append(gap)

        care_level_calls += 1
        levels, usage, fell_back = _generate_care_levels(
            client, model, config.usecase, sc_id, label, dim_gaps
        )
        total_prompt_tokens     += usage.get("prompt_tokens", 0)
        total_completion_tokens += usage.get("completion_tokens", 0)
        if fell_back:
            care_level_fallbacks += 1
        care_levels_by_scenario[sc_id] = levels

        level_str = "  ".join(
            f"{dim[:4]}:{levels.get(dim, {}).get('level', '?')}" for dim in CARE_LEVEL_RUBRIC
        )
        print(f"  [{sc_id.upper()}] {label[:40]:<40} {level_str}"
              + ("  [FALLBACK]" if fell_back else ""))

    care_level_summary = _care_level_summary(care_levels_by_scenario)
    print("[Phase 6] CARE capability-level classification done")

    # Persist the raw CARE-level data alongside the assessment report for
    # traceability (kept next to the existing report path - no new Config
    # attribute needed).
    care_levels_path = config.assessment_report_path.with_name(
        config.assessment_report_path.stem + "_care_levels.json"
    )
    with open(care_levels_path, "w", encoding="utf-8") as f:
        json.dump(
            {"scenarios": care_levels_by_scenario, "summary": care_level_summary},
            f, indent=2,
        )
    print(f"[Phase 6] CARE levels saved      : {care_levels_path.name}")

    # Generate executive summary
    print("\n[Phase 6] Generating executive summary ...")
    executive_summary, exec_usage, exec_fell_back = _generate_executive_summary(
        client, model, config.usecase, overall_score, care_scores,
        maturity_label, gap_analysis,
    )
    total_prompt_tokens     += exec_usage.get("prompt_tokens", 0)
    total_completion_tokens += exec_usage.get("completion_tokens", 0)
    print("[Phase 6] Executive summary done" + ("  [FALLBACK]" if exec_fell_back else ""))

    # Performance metrics: token cost and how often each LLM step fell back
    # to its deterministic default. A high fallback rate here (or in Phase 5)
    # is the clearest "is this practically usable" signal in the pipeline.
    write_metrics(config, 6, {
        "recommendation_calls":     recommendation_calls,
        "recommendation_fallbacks": recommendation_fallbacks,
        "care_level_calls":         care_level_calls,
        "care_level_fallbacks":     care_level_fallbacks,
        "executive_summary_fallback": exec_fell_back,
        "total_llm_fallbacks": (
            recommendation_fallbacks + care_level_fallbacks + int(exec_fell_back)
        ),
        "total_prompt_tokens":     total_prompt_tokens,
        "total_completion_tokens": total_completion_tokens,
        "total_tokens":            total_prompt_tokens + total_completion_tokens,
    })

    # progress of report assembly
    print("[Phase 6] Assembling final report ...")
    md_report = _build_markdown_report(
        config, shacl_report, gap_analysis,
        recommendations_by_scenario, executive_summary,
        overall_score, care_scores, maturity_label, maturity_desc, model,
        care_levels_by_scenario, care_level_summary,
    )

    with open(config.assessment_report_path, "w", encoding="utf-8") as f:
        f.write(md_report)

    print(f"[Phase 6] Report written        : {config.assessment_report_path}")

    # terminal final summary
    print(f"\n  Final HI Assessment: {config.usecase.upper()}")
    print(f"  {'─' * 55}")
    print(f"  Overall Conformance : {overall_score*100:.1f}%")
    print(f"  Maturity Level      : {maturity_label}")
    print(f"  Total Gaps          : {gap_analysis.get('total_gaps', 0)}")
    for dim, score in care_scores.items():
        bar = "▓" * round(score * 20) + "░" * (20 - round(score * 20)) # did not know how to display bars so llm did this part for me
        print(f"  {dim:<15} : [{bar}] {score*100:.0f}%")
    print(f"  {'─' * 55}")
    print(f"  CARE Capability Levels (modal level across scenarios, 1=Reactive/2=Proactive/3=Social)")
    for dim, s in care_level_summary.items():
        print(f"  {dim:<15} : Level {s['modal_level']} ({s['modal_label']})")
    print(f"  {'─' * 55}")
    print(f"  Report saved to: {config.assessment_report_path.name}")
    print(f"\n[Phase 6] Complete\n")
