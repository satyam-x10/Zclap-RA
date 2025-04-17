agent_manifest = {
    "agent_name": "temporal_analysis_agent",
    "purpose": "Evaluates temporal coherence via motion smoothness and jitter detection.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["temporal_coherence_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["optical_flow_analysis", "jitter_detection"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frames"
    },
    "output_type_details": {
        "temporal_coherence_score": "Float between 0 and 1"
    },
}

import numpy as np
import cv2

async def run(input_data: dict) -> dict:
    motion_vectors = input_data.get("motion_vectors", [])
    if not motion_vectors:
        raise ValueError("Missing input: 'motion_vectors'")

    # Convert to plain float array
    mv = np.array([float(m) for m in motion_vectors])

    # Normalize & invert: Lower motion = smoother → higher score
    max_mv = np.max(mv) if len(mv) > 0 else 1.0
    norm_mv = mv / max_mv
    score = 1.0 - np.mean(norm_mv)

    # Clamp to [0, 1]
    score = max(0.0, min(1.0, round(score, 4)))

    summary = "Smooth transitions" if score > 0.75 else \
              "Moderately smooth with occasional jumps" if score > 0.5 else \
              "Notably jittery or abrupt"

    print(f" Temporal Score: {score} — {summary}")

    return {
        "temporal_score": score,
        "temporal_summary": summary
    }