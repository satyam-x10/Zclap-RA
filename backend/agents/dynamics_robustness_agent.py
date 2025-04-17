agent_manifest = {
    "agent_name": "dynamics_robustness_agent",
    "purpose": "Tests robustness under fast motion, lighting or angle variation.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["dynamic_scene_handling_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["motion_robustness"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frame tensors"
    },
    "output_type_details": {
        "dynamic_scene_handling_score": "Float between 0 and 1"
    },  
}


import numpy as np
import cv2

def run(input_data: dict) -> dict:
    motion_vectors = input_data.get("motion_vectors", [])
    if not motion_vectors:
        raise ValueError("Missing input: 'motion_vectors'")

    mv = np.array([float(m) for m in motion_vectors])
    std_mv = np.std(mv)
    max_mv = np.max(mv)

    # Heuristic: high variance or big spikes = poor robustness
    # We'll flip it: higher variance = lower score
    score = 1.0 - (std_mv / max_mv if max_mv > 0 else 0)
    score = max(0.0, min(1.0, round(score, 4)))

    summary = "Highly robust under dynamic scenes" if score > 0.8 else \
              "Moderately stable with noticeable transitions" if score > 0.6 else \
              "Prone to jitter or abrupt scene shifts"

    print(f"🎥 Dynamics Score: {score} — {summary}")

    return {
        "dynamics_score": float(score),
        "dynamics_summary": summary
    }