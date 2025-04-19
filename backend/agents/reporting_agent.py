from datetime import datetime

agent_manifest = {
    "name": "reporting_agent",
    "description": "Generates a final report based on the outputs from other agents.",
}

async def run(input_data: dict) -> dict:
    temporal = input_data["temporal_output"]
    semantic = input_data["semantic_output"]
    dynamics = input_data["dynamics_output"]
    general = input_data["generalisation_output"]
    reasoning = input_data["reasoning_output"]

    timestamp = str(datetime.utcnow())

    scorecard = {
        "temporal": {
            "score": temporal["temporal_coherence"],
            "summary": "Smooth and consistent" if temporal["temporal_coherence"] > 0.85 else "Irregular or unstable"
        },
        "semantic": {
            "score": semantic["semantic_consistency_score"],
            "summary": semantic["summary"]
        },
        "dynamics": {
            "score": dynamics["dynamics_robustness_score"],
            "summary": dynamics["analysis"]
        },
        "generalization": {
            "score": general["generalisation_score"],
            "summary": general["analysis"]
        }
    }

    formatted_summary = f"""\
Timestamp: {timestamp}

🎯 Scorecard:
- Temporal Coherence: {scorecard['temporal']['score']} — {scorecard['temporal']['summary']}
- Semantic Consistency: {scorecard['semantic']['score']} — {scorecard['semantic']['summary']}
- Dynamic Handling: {scorecard['dynamics']['score']} — {scorecard['dynamics']['summary']}
- Generalization: {scorecard['generalization']['score']} — {scorecard['generalization']['summary']}

🧠 Reasoning Verdict:
{reasoning['explanation']}

✅ Final Recommendation:
{reasoning['verdict']}
"""

    report_data = {
        "final_report": {
            "timestamp": timestamp,
            "scorecard": scorecard,
            "summary": reasoning["explanation"],
            "insights": [
                scorecard["temporal"]["summary"],
                scorecard["semantic"]["summary"],
                scorecard["dynamics"]["summary"],
                scorecard["generalization"]["summary"]
            ],
            "recommendations": reasoning["verdict"]
        },
        "scorecard": scorecard,
        "formatted_summary": formatted_summary.strip()
    }

    print("✅ Final report generated. ")
    return report_data
