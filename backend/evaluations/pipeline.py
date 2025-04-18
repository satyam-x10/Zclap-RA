
from evaluations.Architecture import start_analysis

async def run_pipeline(video_path: str, parsed_json: str = ""):
    print(f"Running pipeline for video: {video_path} ")
    
    active_agents = []

    for category, agents in parsed_json.get("criteria", {}).items():
        for agent_name in agents:
            active_agents.append(agent_name)

    Research = await start_analysis(video_path,parsed_json)

    return Research
