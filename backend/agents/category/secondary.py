import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Config import config

from agents.extractors.aesthetic import run as aesthetic_agent
from agents.extractors.motion import run as motion_agent
from agents.extractors.caption_alignment import run as caption_alignment_agent
from agents.extractors.redundancy import run as redundancy_agent
from agents.extractors.transition import run as transition_agent

from agents.conversation.core.aesthetic import run as aesthetic_agent_conversation
from agents.conversation.core.motion import run as motion_agent_conversation
from agents.conversation.core.caption_alignment import run as caption_alignment_agen_conversationt
from agents.conversation.core.redundancy import run as redundancy_agent_conversation
from agents.conversation.core.transition import run as transition_agent_conversation

# Actual agent function mapping
Secondary_agents = {
    "motion_agent": motion_agent,                        # Needs motion_vectors
    "transition_agent": transition_agent,                # Needs scene_transitions or hist diff
    "caption_alignment_agent": caption_alignment_agent,  # Needs captions vs. frames/prompt
    "redundancy_agent": redundancy_agent,                # Needs tags/embeddings to detect repeats
    "aesthetic_agent": aesthetic_agent,                  # Can run last; general visual eval
}

Secondary_agent_conversations = {
    "motion_agent": motion_agent_conversation,                        # Needs motion_vectors
    "transition_agent": transition_agent_conversation,
    "caption_alignment_agent": caption_alignment_agen_conversationt,  # Needs captions vs. frames/prompt
    "redundancy_agent": redundancy_agent_conversation,                # Needs tags/embeddings to detect repeats
    "aesthetic_agent": aesthetic_agent_conversation,                  # Can run last; general visual eval
}


async def run_secondary_agents():
    # Run all agents in the primary category
    user_selected_agents = config.secondary_agents
    print(f"Running secondary agents: {user_selected_agents}")

    for agent_name, agent_function in Secondary_agents.items():
        if agent_name not in user_selected_agents:
            continue  # Skip agents not selected by the user
        print(f"Running {agent_name}...")
        try:
           await agent_function()
        except Exception as e:
            print(f"Error running {agent_name}: {e}")
            continue  # Skip to the next agent if one fails

async def run_agents_conversations(conversation_history):
    for agent_name, conversation_function in Secondary_agent_conversations.items():
        try:
            conversation_history=  await conversation_function(conversation_history)
        except Exception as e:
            print(f" Error in {agent_name} conversation: {e}")
    return conversation_history
