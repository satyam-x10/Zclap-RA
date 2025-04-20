import os
import sys

# # Add the root project directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import asyncio
# export const PIPELINE_MODES = ["default", "parallel", "sequential", ];

# Primary conversation agents
from agents.conversation.core.video_ingestion import run as ingest_video_conversation
from agents.conversation.core.temporal_analysis import run as eval_temporal_conversation
from agents.conversation.core.semantic_analysis import run as eval_semantic_conversation
from agents.conversation.core.dynamics_robustness import run as eval_dynamics_conversation
from agents.conversation.core.generalization import run as eval_generalization_conversation
from agents.conversation.core.perception import run as extract_perception_conversation

from agents.conversation.core.redundancy import run as  eval_redundancy_conversation
from agents.conversation.core.aesthetic import run as  aesthetic_conversation
from agents.conversation.core.motion import run as  motion_conversation
from agents.conversation.core.transition import run as  transition_conversation
from agents.conversation.core.caption_alignment import run as  caption_alignment


from agents.conversation.core.reasoning import run as eval_reasoning_conversation
from agents.conversation.core.reporting import run as eval_reporting_conversation

Primary_agent_conversations = {
    "video_ingestion_agent": ingest_video_conversation,
    "perception_agent": extract_perception_conversation,
    "semantic_analysis_agent": eval_semantic_conversation,
    "temporal_analysis_agent": eval_temporal_conversation,
    "dynamics_robustness_agent": eval_dynamics_conversation,
    "generalization_agent": eval_generalization_conversation
}

Secondary_agent_conversations = {
    "aesthetic_agent": aesthetic_conversation,
    "motion_agent": motion_conversation,
    "redundancy_agent": eval_redundancy_conversation,
    "transition_agent": transition_conversation,
    "caption_alignment_agent": caption_alignment,
}

Meta_agent_conversations = {
    "reasoning_agent": eval_reasoning_conversation,
    "reporting_agent": eval_reporting_conversation,
}

async def handle_primary_pipeline_mode(pipeline_mode: str, conversation_history: str) -> str:
    

    if pipeline_mode == "hybrid":
        # Step 1: Run ingestion → perception (sequential)
        for agent_name in ["video_ingestion_agent", "perception_agent"]:
            conversation_history = await Primary_agent_conversations[agent_name](conversation_history)

        # Step 2: Run semantic + temporal in parallel
        async def run_dual(name):
            return await Primary_agent_conversations[name](conversation_history)

        semantic_task = run_dual("semantic_analysis_agent")
        temporal_task = run_dual("temporal_analysis_agent")
        semantic_out, temporal_out = await asyncio.gather(semantic_task, temporal_task)

        conversation_history += semantic_out + temporal_out

        # Step 3: dynamics (depends on temporal), generalization (depends on semantic)
        for agent_name in ["dynamics_robustness_agent", "generalization_agent"]:
            conversation_history = await Primary_agent_conversations[agent_name](conversation_history)

    # Optional: run reasoning agent after all (if defined)
    elif pipeline_mode == "parallel":

        async def run_agent(agent_name, func):
            nonlocal conversation_history
            try:
                updated = await func(conversation_history)
                conversation_history += f"[{agent_name}] Parallel conversation complete.\n"
                return updated
            except Exception as e:
                return conversation_history + f"[{agent_name}] ❌ Error: {e}\n"

        tasks = [run_agent(agent_name, func) for agent_name, func in Primary_agent_conversations.items()]
        results = await asyncio.gather(*tasks)
        # merge all returned conversations
        conversation_history = "\n".join(results)

    elif pipeline_mode == "sequential":
        sequence = list(Primary_agent_conversations.keys())
        for agent_name in sequence:
            try:
                conversation_history = await Primary_agent_conversations[agent_name](conversation_history)
            except Exception as e:
                print(f"Error in {agent_name}: {e}")

    else:
        print(f"Unknown pipeline mode: {pipeline_mode}")

    return conversation_history


# async def handle_secondary_pipeline_mode(conversation_history: str) -> str:

# if __name__ == "__main__":
#     # Example usage
#     pipeline_mode = "parallel"  # or "parallel", "sequential" ,hybrid
#     conversation_history = ""
#     result = asyncio.run(handle_pipeline_mode(pipeline_mode, conversation_history))
#     print(result)