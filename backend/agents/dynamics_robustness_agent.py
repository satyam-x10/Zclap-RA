agent_manifest = {
    "agent_name": "dynamics_robustness_agent",
    "purpose": "Assesses system robustness during rapid changes in scenes, such as object movement, lighting, or camera shifts.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["robustness_score"],
    "dependencies": ["perception_agent"],
    "supported_tasks": ["scene_change_detection", "lighting_variation_analysis", "motion_adaptability"],
    "prompt_required": False
}
