agent_manifest = {
    "agent_name": "generalization_agent",
    "purpose": "Tests performance on videos that differ from training distribution to measure generalization capability.",
    "agent_type": "analysis",
    "input_format": ["video_frames", "semantic_alignment_score"],
    "output_format": ["generalization_score"],
    "dependencies": ["semantic_analysis_agent"],
    "supported_tasks": ["ood_detection", "distribution_shift_analysis"],
    "prompt_required": False
}
