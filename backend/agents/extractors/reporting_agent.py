# agents/meta/reporting_agent.py

from data.Config import config

agent_manifest = {
    "agent_name": "reporting_agent",
    "purpose": "Compiles scores and reasoning trace into a final report.",
}

async def run() -> None:
    try:
        # Collect all agent scores
        scorecard = {
            "temporal": config.analysis.temporal_analysis_agent.get("temporal_coherence"),
            "semantic": config.analysis.semantic_analysis_agent.get("semantic_consistency_score"),
            "dynamics": config.analysis.dynamics_robustness_agent.get("dynamics_robustness_score"),
            "generalization": config.analysis.generalization_agent.get("generalisation_score"),
            "aesthetic": config.analysis.aesthetic_agent.get("aesthetic_score"),
            "redundancy": 1 - config.analysis.redundancy_agent.get("semantic_redundancy", 0),  # Inverted
            "caption_alignment": config.analysis.caption_alignment_agent.get("match_ratio"),
        }

        # Normalize None to 0.0
        normalized_scores = {
            k: round(v if v is not None else 0.0, 4)
            for k, v in scorecard.items()
        }

        avg_score = round(sum(normalized_scores.values()) / len(normalized_scores), 4)

        # Verdict based on average
        if avg_score > 0.75:
            verdict = "Excellent generation quality with strong coherence and appeal."
        elif avg_score > 0.5:
            verdict = "Moderate quality with room for improvement."
        else:
            verdict = "Poor generation — major issues detected across metrics."

        # Reasoning trace
        reasoning_summary = config.analysis.reasoning_agent.get("summary", "")
        reasoning_trace = config.analysis.reasoning_agent.get("reasoning_trace", [])

        config.analysis.reporting_agent = {
            "scorecard": normalized_scores,
            "average_score": avg_score,
            "verdict": verdict,
            "reasoning_trace": reasoning_trace,
            "summary": reasoning_summary
        }

        print(f"[reporting_agent] Final Report: Avg Score = {avg_score:.2f} | Verdict: {verdict}")
    except Exception as e:
        config.analysis.reporting_agent = {
            "scorecard": {},
            "average_score": 0.0,
            "verdict": f"Report generation failed: {str(e)}",
            "reasoning_trace": [],
            "summary": ""
        }
        print(f"[reporting_agent] Error: {e}")
