agent_manifest = {
    "agent_name": "dynamics_robustness_agent",
    "purpose": "Tests robustness under fast motion, lighting or angle variation.",     
}


import numpy as np
import cv2

async def run(input_data: dict) -> dict:
    motion_vectors = input_data.get("motion_vectors", [])
    scene_transitions = input_data.get("scene_transitions", [])
    semantic_score = input_data.get("semantic_consistency_score", 1.0)

    if motion_vectors is None:
        raise ValueError("Missing required inputs: 'motion_vectors', 'event_segments'")

    mv = np.array([float(m) for m in motion_vectors])
    motion_mean = np.mean(mv)
    motion_std = np.std(mv)

    high_motion_indices = [i for i, val in enumerate(mv) if val > (motion_mean + motion_std)]

    # Penalize score if semantic consistency is poor during motion
    robustness_score = semantic_score
    if len(high_motion_indices) > 0 and semantic_score < 0.8:
        robustness_score *= 0.8
    if len(scene_transitions) > 0 and semantic_score < 0.7:
        robustness_score *= 0.75

    robustness_score = round(min(1.0, robustness_score), 4)

    analysis = (
        "Stable under motion and transitions."
        if robustness_score > 0.85 else
        "Minor semantic drift during dynamic parts."
        if robustness_score > 0.6 else
        "Significant loss of consistency during dynamic scenes."
    )

    dynamics_robustness_output = {
        "dynamics_robustness_score": robustness_score,
        "high_motion_zones": high_motion_indices,
        "scene_transitions": scene_transitions,
        "analysis": analysis
    }
    
    print('Dynamics Robustness Output:')

    return dynamics_robustness_output