from data.valuables import valuablesConfig
from data.Config import config
from utils.functions import class_to_dict

async def run_Conversational_agents():

    analysis_from_extractors= class_to_dict(valuablesConfig.analysis)
    pipeline_mode =config.pipeline_mode
    report_format = config.report_format

    pass