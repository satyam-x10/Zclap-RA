import sys
import os
import asyncio
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.Config import config


# Primary extractors
from agents.extractors.video_ingestion import run as ingest_video
from agents.extractors.temporal_analysis import run as eval_temporal
from agents.extractors.semantic_analysis import run as eval_semantic
from agents.extractors.dynamics_robustness import run as eval_dynamics
from agents.extractors.generalization import run as eval_generalization
from agents.extractors.perception import run as extract_perception

from agents.conversation.handle_pipeline_mode import handle_primary_pipeline_mode as handle_pipeline_mode

# Mapping of extractor agents
Primary_agents_extractor = {
    "video_ingestion_agent": ingest_video,
    "perception_agent": extract_perception,
    "semantic_analysis_agent": eval_semantic,
    "temporal_analysis_agent": eval_temporal,
    "dynamics_robustness_agent": eval_dynamics,
    "generalization_agent": eval_generalization
}



async def run_primary_agents():
    print("Running primary extractors...\n")
    for agent_name, agent_function in Primary_agents_extractor.items():
        print(f"➡️ Running {agent_name} extractor...")
        try:
            await agent_function()
        except Exception as e:
            print(f"❌ Error running {agent_name} extractor: {e}")
        # Optionally: await asyncio.sleep(2)


async def run_agents_conversations(conversation_history,pipeline_mode):

    # export const PIPELINE_MODES = ["default", "parallel", "sequential", ];
    try:
        conversation_history=await  handle_pipeline_mode(pipeline_mode,conversation_history)
        return conversation_history

    except Exception as e:
        print(f"❌ Error in conversation: {e}")