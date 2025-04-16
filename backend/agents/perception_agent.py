agent_manifest = {
    "agent_name": "perception_agent",
    "purpose": "Extracts low-level video features like objects, scenes, lighting, and motion cues for downstream agents.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["object_detections", "scene_descriptions", "lighting_profiles"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["object_detection", "scene_understanding", "motion_estimation"],
    "prompt_required": False
}
