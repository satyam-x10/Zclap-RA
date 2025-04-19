import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Config import config

from agents.extractors.aesthetic_agent import run as aesthetic_agent
from agents.extractors.motion_agent import run as motion_agent
from agents.extractors.caption_alignment_agent import run as caption_alignment_agent
from agents.extractors.redundancy_agent import run as redundancy_agent
from agents.extractors.transition_agent import run as transition_agent

# Actual agent function mapping
Secondary_agents = {    
    "aesthetic_agent": aesthetic_agent,
    "motion_agent": motion_agent,
    "caption_alignment_agent": caption_alignment_agent,
    "redundancy_agent": redundancy_agent,
    "transition_agent": transition_agent,
}

def run_secondary_agents():
    # Run all agents in the primary category
    for agent_name, agent_function in Secondary_agents.items():
        print(f"Running {agent_name}...")
        try:
            agent_function()
        except Exception as e:
            print(f"Error running {agent_name}: {e}")
            continue  # Skip to the next agent if one fails