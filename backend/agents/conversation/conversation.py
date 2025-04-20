from data.valuables import valuablesConfig
from data.Config import config
from utils.functions import class_to_dict
from agents.category.primary import run_agents_conversations as run_primary_agent_conversations
from agents.category.secondary import run_agents_conversations as run_secondary_agent_conversations
from agents.category.meta import run_agents_conversations as run_meta_agent_conversations


async def run_Conversational_agents():

    analysis_from_extractors= class_to_dict(valuablesConfig.analysis)
    pipeline_mode =config.pipeline_mode
    report_format = config.report_format
    primary_agents = config.primary_agents
    secondary_agents = config.secondary_agents
    meta_agents = config.meta_agents
    conversation_history= valuablesConfig.conversation_history

    await run_primary_agent_conversations()
    await run_secondary_agent_conversations()
    await run_meta_agent_conversations()

    pass