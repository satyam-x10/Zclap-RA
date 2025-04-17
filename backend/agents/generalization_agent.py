agent_manifest = {
    "agent_name": "generalization_agent",
    "purpose": "Tests performance on OOD videos to measure generalization.",
    "agent_type": "analysis",
    "input_format": ["video_frames", "semantic_consistency_score"],
    "output_format": ["generalization_score"],
    "dependencies": ["semantic_analysis_agent"],
    "supported_tasks": ["ood_detection", "distribution_shift_analysis"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frames",
        "semantic_consistency_score": "Float"
    },
    "output_type_details": {
        "generalization_score": "Float between 0 and 1"
    },
}

import numpy as np
async def run(input_data: dict) -> dict:
    motion_vectors = input_data.get("motion_vectors", [])
    brightness_series = input_data.get("frame_stats", {}).get("brightness_series", [])

    if not motion_vectors or not brightness_series:
        raise ValueError("Missing required inputs for generalization analysis.")

    mv = np.array([float(m) for m in motion_vectors])
    brightness = np.array([float(b) for b in brightness_series])

    mv_entropy = np.std(mv)
    brightness_entropy = np.std(brightness)

    # Combine entropy metrics and normalize to 0–1 range (higher = more novel)
    entropy_score = (mv_entropy + brightness_entropy) / 50.0
    score = max(0.0, min(1.0, round(entropy_score, 4)))

    summary = "Shows high diversity and generalization" if score > 0.7 else \
              "Some novel scenes but limited variability" if score > 0.4 else \
              "Visually repetitive and under-generalized"

    print(f"🧬 Generalization Score: {score} — {summary}")

    return {
        "generalization_score": float(score),
        "generalization_summary": summary
    }