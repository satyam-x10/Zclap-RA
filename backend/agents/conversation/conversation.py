import os
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# # # Add the root project directory to sys.path


from data.valuables import valuablesConfig
from data.Config import config
from utils.functions import class_to_dict
from agents.category.primary import run_agents_conversations as run_primary_agent_conversations
from agents.category.secondary import run_agents_conversations as run_secondary_agent_conversations
from agents.category.meta import run_agents_conversations as run_meta_agent_conversations


async def run_Conversational_agents():

    pipeline_mode =config.pipeline_mode
    report_format = config.report_format
    conversation_history={}

    conversation_history= await run_primary_agent_conversations(conversation_history,pipeline_mode)
    conversation_history= await run_secondary_agent_conversations(conversation_history)
    conversation_history= await run_meta_agent_conversations(conversation_history,report_format)

    return conversation_history


# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(run_Conversational_agents())