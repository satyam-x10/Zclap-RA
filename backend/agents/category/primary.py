import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Config import config


from agents.extractors.video_ingestion_agent import run as ingest_video
from agents.extractors.temporal_analysis_agent import run as eval_temporal
from agents.extractors.semantic_analysis_agent import run as eval_semantic
from agents.extractors.dynamics_robustness_agent import run as eval_dynamics
from agents.extractors.generalization_agent import run as eval_generalization
from agents.extractors.perception_agent import run as extract_perception

# Actual agent function mapping
Primary_agents = {
    "video_ingestion_agent": ingest_video,               # Step 1: Extract frames from video
    "temporal_analysis_agent": eval_temporal,            # Step 2: Analyze sequence/timing of frames
    "semantic_analysis_agent": eval_semantic,            # Step 3: Extract high-level meaning (objects, scenes, actions)
    "perception_agent": extract_perception,              # Step 4: Evaluate perception (attention, emotion, saliency)
    "dynamics_robustness_agent": eval_dynamics,          # Step 5: Analyze motion stability / dynamic consistency
    "generalization_agent": eval_generalization          # Step 6: Assess if model can generalize to other contexts
}


def run_primary_agents():
    # Run all agents in the primary category
    for agent_name, agent_function in Primary_agents.items():
        print(f"Running {agent_name}...")
        try:
            agent_function()
        except Exception as e:
            print(f"Error running {agent_name}: {e}")
            continue  # Skip to the next agent if one fails