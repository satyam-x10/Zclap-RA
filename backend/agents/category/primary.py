import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.Config import config

# Primary extractors
from agents.extractors.video_ingestion import run as ingest_video
from agents.extractors.temporal_analysis import run as eval_temporal
from agents.extractors.semantic_analysis import run as eval_semantic
from agents.extractors.dynamics_robustness import run as eval_dynamics
from agents.extractors.generalization import run as eval_generalization
from agents.extractors.perception import run as extract_perception

# Primary conversation agents
from agents.conversation.core.video_ingestion import run as ingest_video_conversation
from agents.conversation.core.temporal_analysis import run as eval_temporal_conversation
from agents.conversation.core.semantic_analysis import run as eval_semantic_conversation
from agents.conversation.core.dynamics_robustness import run as eval_dynamics_conversation
from agents.conversation.core.generalization import run as eval_generalization_conversation
from agents.conversation.core.perception import run as extract_perception_conversation

# Mapping of extractor agents
Primary_agents_extractor = {
    "video_ingestion_agent": ingest_video,
    "perception_agent": extract_perception,
    "semantic_analysis_agent": eval_semantic,
    "temporal_analysis_agent": eval_temporal,
    "dynamics_robustness_agent": eval_dynamics,
    "generalization_agent": eval_generalization
}

# Mapping of conversation agents
Primary_agent_conversations = {
    "video_ingestion_agent": ingest_video_conversation,
    "perception_agent": extract_perception_conversation,
    "semantic_analysis_agent": eval_semantic_conversation,
    "temporal_analysis_agent": eval_temporal_conversation,
    "dynamics_robustness_agent": eval_dynamics_conversation,
    "generalization_agent": eval_generalization_conversation
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


async def run_agents_conversations():
    print("\nRunning primary agent conversations...\n")
    for agent_name, conversation_function in Primary_agent_conversations.items():
        print(f"💬 Running {agent_name} conversation...")
        try:
            await conversation_function()
        except Exception as e:
            print(f"❌ Error in {agent_name} conversation: {e}")
