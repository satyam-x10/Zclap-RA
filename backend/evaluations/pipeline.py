
from evaluations.Architecture import start_analysis
from utils.video_utils import extract_config
from data.Config import config

async def run_analysis_pipeline():    
    
    extract_config()

    print(f"config mode: {config.__dict__}")

    analysis = await start_analysis()

    return analysis
