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

def run(input_data: dict) -> dict:
    # Extract scores & summaries
    temporal = input_data.get("temporal_score", 0)
    semantic = input_data.get("semantic_score", 0)
    dynamics = input_data.get("dynamics_score", 0)
    generalization = input_data.get("generalization_score", 0)

    summary_lines = [
        f"- Temporal: {input_data.get('temporal_summary', 'N/A')} ({temporal})",
        f"- Semantic: {input_data.get('semantic_summary', 'N/A')} ({semantic})",
        f"- Dynamics: {input_data.get('dynamics_summary', 'N/A')} ({dynamics})",
        f"- Generalization: {input_data.get('generalization_summary', 'N/A')} ({generalization})",
    ]

    avg_score = round((temporal + semantic + dynamics + generalization) / 4.0, 4)

    if avg_score > 0.8:
        recommendation = "Excellent video quality across all aspects. Ready for deployment or presentation."
    elif avg_score > 0.6:
        recommendation = "Good overall performance. Consider improving semantic consistency or stability."
    else:
        recommendation = "Several aspects need refinement. Focus on transitions and scene variety."

    print("🧠 Synthesizing reasoning from analysis outputs...")

    return {
        "consolidated_insights": summary_lines,
        "summary": f"Overall coherence score: {avg_score}",
        "recommendations": recommendation
    }