import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Config import config


from agents.extractors.reasoning import run as reasoning_agent
from agents.extractors.reporting import run as reporting_agent

# Actual agent function mapping
Meta_agents = {
"reasoning_agent": reasoning_agent,
"reporting_agent": reporting_agent,
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