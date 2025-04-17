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

import datetime


def run(input_data: dict) -> dict:
    now = datetime.datetime.now().isoformat()

    print(" Generating final report...")

    # Build scorecard
    scorecard = {
        "temporal": {
            "score": input_data.get("temporal_score"),
            "summary": input_data.get("temporal_summary")
        },
        "semantic": {
            "score": input_data.get("semantic_score"),
            "summary": input_data.get("semantic_summary")
        },
        "dynamics": {
            "score": input_data.get("dynamics_score"),
            "summary": input_data.get("dynamics_summary")
        },
        "generalization": {
            "score": input_data.get("generalization_score"),
            "summary": input_data.get("generalization_summary")
        }
    }

    insights = input_data.get("consolidated_insights", [])
    overall = input_data.get("summary", "")
    recommendations = input_data.get("recommendations", "")

    formatted_text = f"""
 Timestamp: {now}

 Scorecard:
- Temporal Coherence: {scorecard['temporal']['score']} — {scorecard['temporal']['summary']}
- Semantic Consistency: {scorecard['semantic']['score']} — {scorecard['semantic']['summary']}
- Dynamic Handling: {scorecard['dynamics']['score']} — {scorecard['dynamics']['summary']}
- Generalization: {scorecard['generalization']['score']} — {scorecard['generalization']['summary']}

 Reasoning Summary:
{overall}

 Consolidated Insights:
{chr(10).join(insights)}

✅ Final Recommendation:
{recommendations}
""".strip()

    return {
        "final_report": {
            "timestamp": now,
            "scorecard": scorecard,
            "summary": overall,
            "insights": insights,
            "recommendations": recommendations
        },
        "scorecard": scorecard,
        "formatted_summary": formatted_text
    }