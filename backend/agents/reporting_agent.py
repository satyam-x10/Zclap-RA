agent_manifest = {
    "agent_name": "reporting_agent",
    "purpose": "Generates final report with metrics and qualitative summary.",
    "agent_type": "reporting",
    "input_format": ["score_dict", "insight_dict"],
    "output_format": ["report"],
    "dependencies": ["reasoning_agent"],
    "supported_tasks": ["report_formatting"],
    "prompt_required": False,
    "input_type_details": {
        "score_dict": "Raw aspect scores",
        "insight_dict": "Reasoned insights"
    },
    "output_type_details": {
        "report": "Structured dict with full evaluation report"
    },
}

def run(score_dict, insight_dict):
    return {
        "metrics": score_dict,
        "summary": insight_dict["remarks"],
        "overall_score": insight_dict["overall_score"]
    }
