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


def run(frames, semantic_score):
    # Mock logic: assume lower semantic score = more OOD
    generalization = 1.0 - abs(semantic_score - 0.5)
    return {"generalization_score": round(generalization, 2)}
