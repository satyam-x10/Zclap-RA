from utils.constant import Main_OBJECTIVES
from data.Config import config

from utils.functions import class_to_dict

def getPromptTemplate(agent_name,agent_job,conversation_history):
    prompt = f"$The main objective is to {Main_OBJECTIVES}. You are one of the agents in this system. You are an {agent_name} that {agent_job}. You are being provided with a conversation history of all the agents and data extracted usiong tools. Please analyze the aesthetic quality of the video based on the conversation history and provide your insights. Please dont do formalities and only to the point work. The conversation history is: {conversation_history}. Also the analysis from the extractors is: {class_to_dict(config.analysis)}. " 
    return prompt