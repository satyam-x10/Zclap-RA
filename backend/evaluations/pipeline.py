
from evaluations.Architecture import start_analysis

async def run_pipeline(video_path: str, parsed_json: str = ""):
    print(f"Running pipeline for video: {video_path} ")

    prompt = parsed_json.get("prompt", "") if parsed_json else ""
    frame_sampling_rate = parsed_json.get("frame_sampling_rate", 1) if parsed_json else 1
    pipeline_mode = parsed_json.get("pipeline_mode", "default") if parsed_json else "default"
    report_format = parsed_json.get("report_format", "json") if parsed_json else "json"

    active_agents = []

    for category, agents in parsed_json.get("criteria", {}).items():
        for agent_name in agents:
            active_agents.append(agent_name)

    # Final Output
    print("Prompt:", prompt)
    print("Frame Sampling Rate:", frame_sampling_rate)
    print("Pipeline Mode:", pipeline_mode)
    print("Report Format:", report_format)
    print("Active Agents:", active_agents)

    Research = await start_analysis(video_path,parsed_json)

    return Research
