import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Config import config


from agents.extractors.reasoning_agent import run as reasoning_agent
from agents.extractors.reporting_agent import run as reporting_agent

# Actual agent function mapping
Meta_agents = {
"reasoning_agent": reasoning_agent,
"reporting_agent": reporting_agent,
}

async def run_meta_agents():
    # Run all agents in the primary category
    for agent_name, agent_function in Meta_agents.items():
        print(f"Running {agent_name}...")
        try:
           await agent_function()
        except Exception as e:
            print(f"Error running {agent_name}: {e}")
            continue  # Skip to the next agent if one fails