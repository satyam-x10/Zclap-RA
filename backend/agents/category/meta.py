import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Config import config


from agents.extractors.reasoning import run as reasoning_agent
from agents.extractors.reporting import run as reporting_agent

from agents.conversation.core.reasoning import run as reasoning_agent_conversation
from agents.conversation.core.reporting import run as reporting_agentconversation


# Actual agent function mapping
Meta_agents = {
"reasoning_agent": reasoning_agent,
"reporting_agent": reporting_agent,
}

Meta_agents_conversation = {
"reasoning_agent": reasoning_agent_conversation,
"reporting_agent": reporting_agentconversation,
}

async def run_meta_agents():
    # Run all agents in the primary category
    user_selected_agents = config.meta_agents
    for agent_name, agent_function in Meta_agents.items():
        if agent_name not in user_selected_agents:
            continue
        print(f"Running {agent_name}...")
        try:
           await agent_function()
        except Exception as e:
            print(f"Error running {agent_name}: {e}")
            continue  # Skip to the next agent if one fails

async def run_agents_conversations(conversation_history,report_format):
    for agent_name, conversation_function in Meta_agents_conversation.items():
        try:
            conversation_history=  await conversation_function(conversation_history,report_format)

        except Exception as e:
            print(f" Error in {agent_name} conversation: {e}")
    return conversation_history
