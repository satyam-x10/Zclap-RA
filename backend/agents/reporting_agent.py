agent_manifest = {
    "agent_name": "reporting_agent",
    "purpose": "Generates structured and natural language reports based on analysis results, including visualizations and summaries.",
    "agent_type": "reporting",
    "input_format": ["final_scores", "reasoning_log"],
    "output_format": ["json_report", "nlp_summary", "charts"],
    "dependencies": ["reasoning_agent"],
    "supported_tasks": ["report_generation", "data_visualization", "summary_extraction"],
    "prompt_required": False
}
