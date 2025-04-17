agent_manifest = {
    "agent_name": "reasoning_agent",
    "purpose": "Synthesizes scores into insights and computes final score.",
    "agent_type": "synthesis",
    "input_format": ["score_dict"],
    "output_format": ["insight_dict"],
    "dependencies": ["all_analysis_agents"],
    "supported_tasks": ["insight_generation"],
    "prompt_required": False,
    "input_type_details": {
        "score_dict": "Dictionary of aspect scores"
    },
    "output_type_details": {
        "insight_dict": "Remarks + overall score"
    },
}

def run(score_dict):
    vals = list(score_dict.values())
    avg = round(sum(vals) / len(vals), 2)
    insight = "Good coherence and prompt match. Could improve on motion handling."
    return {"overall_score": avg, "remarks": insight}
