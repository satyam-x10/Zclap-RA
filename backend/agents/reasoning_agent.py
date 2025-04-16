agent_manifest = {
    "agent_name": "reasoning_agent",
    "purpose": "Aggregates insights from all analysis agents, applies inference rules, and handles contradictions or edge cases.",
    "agent_type": "reasoning",
    "input_format": [
        "temporal_coherence_score",
        "semantic_alignment_score",
        "robustness_score",
        "generalization_score"
    ],
    "output_format": ["final_scores", "reasoning_log"],
    "dependencies": [
        "temporal_analysis_agent",
        "semantic_analysis_agent",
        "dynamics_robustness_agent",
        "generalization_agent"
    ],
    "supported_tasks": ["score_integration", "conflict_resolution"],
    "prompt_required": False
}
