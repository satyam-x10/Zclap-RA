from utils.constant import Main_OBJECTIVES
from backend.agents.llms.services.groq_client import chat_with_groq
from data.Config import config
from agents.llms.prompt import getPromptTemplate
from agents.extractors.generalization import agent_manifest

async def run(conversation_history):
    prompt = getPromptTemplate(agent_manifest["agent_name"],agent_manifest["purpose"],conversation_history)
    resposne = await chat_with_groq(prompt, model="gemma2-9b-it")
    resposne_message = resposne
    conversation_history.push({"agent": agent_manifest["agent_name"], "content": resposne_message})
    return  conversation_history
