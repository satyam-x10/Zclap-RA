from utils.constant import Main_OBJECTIVES
from agents.llms.services.groq_client import chat_with_groq
from data.Config import config
from agents.llms.prompt import getPromptTemplate
from agents.extractors.video_ingestion import agent_manifest

async def run(conversation_history):
    prompt = getPromptTemplate(agent_manifest["agent_name"],agent_manifest["purpose"],conversation_history)
    resposne = await chat_with_groq(prompt, model="gemma2-9b-it")
    resposne_message = resposne

    
    print("initial conversation history ",conversation_history)
    conversation_history["messages"].append({
        "agent": agent_manifest["agent_name"],
        "content": resposne_message
    })
    print('new conversation history:', conversation_history)

    return  conversation_history
