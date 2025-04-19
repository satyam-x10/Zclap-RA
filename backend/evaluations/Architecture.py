from  agents.category.primary import run_primary_agents
from  agents.category.secondary import run_secondary_agents
from  agents.category.meta import run_meta_agents
from  agents.conversation.conversation import run_Conversational_agents

async def  start_analysis ():


    await run_primary_agents()
    await run_secondary_agents()
    await run_meta_agents()

    await run_Conversational_agents()
