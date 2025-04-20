from utils.constant import Main_OBJECTIVES
from agents.llms.services.groq_client import chat_with_groq
from data.Config import config
from agents.llms.prompt import getPromptTemplate
from agents.extractors.caption_alignment import agent_manifest

async def run(conversation_history):
    prompt = getPromptTemplate(agent_manifest["agent_name"],agent_manifest["purpose"],conversation_history)
    resposne = chat_with_groq(prompt, model="gemma2-9b-it")
    resposne_message = resposne
    conversation_history["messages"].append({
    "agent": agent_manifest["agent_name"],
    "content": resposne_message
})
    return  conversation_history
