# agents/dynamics_robustness_agent.py

import numpy as np
from data.Config import config

agent_manifest = {
    "agent_name": "dynamics_robustness_agent",
    "purpose": "Tests robustness under fast motion, lighting, or scene variation.",
}

async def run() -> None:
    motion_vectors = config.analysis.perception_agent.get("motion_vectors", [])
    scene_transitions = config.analysis.temporal_analysis_agent.get("scene_transitions", [])
    semantic_score = config.analysis.semantic_analysis_agent.get("semantic_consistency_score", 1.0)

    if not motion_vectors:
        raise ValueError("Missing motion vectors from perception agent.")
    if semantic_score is None:
        raise ValueError("Missing semantic consistency score.")
    
    # Convert motion vectors to np array
    mv = np.array([float(m) for m in motion_vectors])
    motion_mean = np.mean(mv)
    motion_std = np.std(mv)

    # High motion indices (1 std above mean)
    high_motion_indices = [i for i, val in enumerate(mv) if val > (motion_mean + motion_std)]

    # Base robustness score from semantic coherence
    robustness_score = semantic_score

    # Penalize based on motion spikes and transitions
    if high_motion_indices and semantic_score < 0.8:
        robustness_score *= 0.8
    if scene_transitions and semantic_score < 0.7:
        robustness_score *= 0.75

    robustness_score = round(min(1.0, robustness_score), 4)

    # Generate qualitative analysis
    if robustness_score > 0.85:
        summary = "Stable under motion and transitions."
    elif robustness_score > 0.6:
        summary = "Minor semantic drift during dynamic parts."
    else:
        summary = "Significant loss of consistency during dynamic scenes."

    # Save result
    config.analysis.dynamics_robustness_agent = {
        "dynamics_robustness_score": robustness_score,
        "high_motion_zones": high_motion_indices,
        "scene_transitions": scene_transitions,
        "summary": summary
    }
