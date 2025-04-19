# agents/extractors/transition_agent.py

from data.Config import config

agent_manifest = {
    "agent_name": "transition_agent",
    "purpose": "Detects and summarizes scene transitions, cuts, or gradual changes.",
}

async def run() -> None:
    scene_changes = config.analysis.perception_agent.get("scene_changes", [])
    scene_transitions = config.analysis.temporal_analysis_agent.get("scene_transitions", [])

    if not scene_changes and not scene_transitions:
        raise ValueError("No scene transition data found.")

    total_frames = len(scene_changes) if scene_changes else 0
    hard_cuts = [i for i, val in enumerate(scene_changes) if val] if scene_changes else []
    transition_frames = scene_transitions if scene_transitions else []

    transition_density = round(len(hard_cuts + transition_frames) / max(total_frames, 1), 4)

    summary = (
        "Frequent scene transitions detected." if transition_density > 0.1 else
        "Moderate number of transitions." if transition_density > 0.03 else
        "Mostly continuous scenes with minimal cuts."
    )

    config.analysis.transition_agent = {
        "hard_cut_frames": hard_cuts,
        "semantic_transitions": transition_frames,
        "transition_density": transition_density,
        "summary": summary
    }
