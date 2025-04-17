agent_manifest = {
    "agent_name": "coordinator_agent",
    "purpose": "Orchestrates all agents, controls flow and memory.",
    "agent_type": "controller",
    "input_format": ["video_file", "prompt"],
    "output_format": ["final_report"],
    "dependencies": ["all_agents"],
    "supported_tasks": ["pipeline_execution"],
    "prompt_required": True,
    "input_type_details": {
        "video_file": "Path to uploaded video file",
        "prompt": "Textual description to compare against"
    },
    "output_type_details": {
        "final_report": "JSON response with metrics and insights"
    },
}

from agents.video_ingestion_agent import run as ingest
from agents.temporal_analysis_agent import run as temporal
from agents.perception_agent import run as semantic
from agents.dynamics_robustness_agent import run as dynamics
from agents.generalization_agent import run as generalization
from agents.reasoning_agent import run as reason    
from agents.reporting_agent import run as report


def run(video_path, prompt):
    frames = ingest(video_path)
    temporal_score = temporal(frames)["temporal_coherence_score"]
    semantic_score = semantic(frames, prompt)["semantic_consistency_score"]
    dynamics_score = dynamics(frames)["dynamic_scene_handling_score"]
    generalization_score = generalization(frames, semantic_score)["generalization_score"]

    scores = {
        "temporal_coherence": temporal_score,
        "semantic_consistency": semantic_score,
        "dynamic_scene_handling": dynamics_score,
        "generalization": generalization_score
    }

    insight = reason(scores)
    return report(scores, insight)