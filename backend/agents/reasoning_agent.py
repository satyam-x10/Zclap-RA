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
async def run(input_data: dict) -> dict:
    print("Running Reasoning Agent...", input_data)

    # Core scores
    temporal = float(input_data.get("temporal_coherence", 0.0))
    semantic = float(input_data.get("semantic_consistency_score", 0.0))
    dynamics = float(input_data.get("dynamics_robustness_score", 0.0))
    general = float(input_data.get("generalisation_score", 0.0))

    # Meta flags and text explanations
    overfitting = input_data.get("overfitting_warning", False)
    general_analysis = input_data.get("generalisation_analysis", "")
    semantic_summary = input_data.get("semantic_summary", "Semantic performance not described.")
    dynamics_analysis = input_data.get("dynamics_analysis", "Dynamics response unavailable.")

    # Weighted aggregate scoring
    final_score = round(0.25 * temporal + 0.3 * semantic + 0.25 * dynamics + 0.2 * general, 4)

    # Verdict inference
    if final_score > 0.85 and not overfitting:
        verdict = "Coherent & Generalizable"
    elif semantic > 0.8 and general < 0.5:
        verdict = "Consistent but Repetitive"
    elif semantic < 0.6 and dynamics < 0.6:
        verdict = "Disjointed"
    elif overfitting and general < 0.4:
        verdict = "Overfitted & Narrow"
    else:
        verdict = "Mixed Consistency"

    # Natural language explanation
    explanation = (
        f"🧠 Temporal Coherence: {temporal:.2f} | "
        f"Semantic Score: {semantic:.2f} | "
        f"Dynamics: {dynamics:.2f} | "
        f"Generalization: {general:.2f}.\n"
        f"{'⚠️ Overfitting detected. ' if overfitting else ''}"
        f"Verdict: **{verdict}**."
    )

    # Final package
    reasoning_output = {
        "final_reasoning_score": final_score,
        "verdict": verdict,
        "explanation": explanation,
        "full_breakdown": {
            "semantic_summary": semantic_summary,
            "dynamics_analysis": dynamics_analysis,
            "generalisation_analysis": general_analysis
        }
    }

    return reasoning_output
