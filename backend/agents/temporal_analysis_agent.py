agent_manifest = {
    "agent_name": "temporal_analysis_agent",
    "purpose": "Analyzes frame-to-frame transitions to evaluate temporal coherence and detect motion smoothness or jitter.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["temporal_coherence_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["optical_flow_analysis", "jitter_detection"],
    "prompt_required": False
}
