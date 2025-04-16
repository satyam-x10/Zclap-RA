agent_manifest = {
    "agent_name": "semantic_analysis_agent",
    "purpose": "Evaluates alignment between video content and provided text prompts using vision-language models like CLIP.",
    "agent_type": "analysis",
    "input_format": ["video_frames", "text_prompt"],
    "output_format": ["semantic_alignment_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["vision_language_matching", "semantic_consistency_scoring"],
    "prompt_required": True
}
