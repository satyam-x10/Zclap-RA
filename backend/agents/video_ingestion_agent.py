agent_manifest = {
    "agent_name": "video_ingestion_agent",
    "purpose": "Handles video loading, format validation, and preprocessing (frame extraction, resizing, etc.).",
    "agent_type": "ingestion",
    "input_format": ["video_file"],
    "output_format": ["video_frames"],
    "dependencies": [],
    "supported_tasks": ["video_validation", "frame_extraction"],
    "prompt_required": False
}
