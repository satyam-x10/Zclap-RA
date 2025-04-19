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
    "perception_agent": extract_perception,              # Step 2: Generate embeddings, semantic tags, motion
    "semantic_analysis_agent": eval_semantic,            # Step 3: Uses semantic tags
    "temporal_analysis_agent": eval_temporal,            # Step 4: Uses frame sequence + embeddings
    "dynamics_robustness_agent": eval_dynamics,          # Step 5: Uses motion + scene change
    "generalization_agent": eval_generalization          # Step 6: Uses all data to assess generalization
}


async def run_primary_agents():
    # Run all agents in the primary category
    for agent_name, agent_function in Primary_agents.items():
        print(f"Running {agent_name}...")
        try:
            await agent_function()
        except Exception as e:
            print(f"Error running {agent_name}: {e}")
            continue  # Skip to the next agent if one fails