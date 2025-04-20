from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.video_utils import save_upload_file
from evaluations.pipeline import run_analysis_pipeline
from utils.functions import convert_numpy_types
from data.Config import config
from utils.functions import extract_config_data
from utils.functions import drop_frames_data
router = APIRouter()
from utils.functions import class_to_dict
from  agents.conversation.conversation import run_Conversational_agents
import numpy as np



@router.post("/analyse")
async def receive_data(
    jsonData: str = Form(...),
    fileData: UploadFile = File(...)
):
    # Parse the JSON string into a Python dict
    parsed_config_json = json.loads(jsonData)
    video_file_path = save_upload_file(fileData)

    config.parsed_config_json = parsed_config_json    
    config.video_file_path = video_file_path
    
    # You can save the file or process it
    await run_analysis_pipeline()    

    valuables= await drop_frames_data()

    final_output = {
        "received": True,
        "jsonData": parsed_config_json,
        "savedTo": video_file_path,
        "config": valuables,
        "conversations": None
    }
    final_output = class_to_dict(valuables)
    print(f"starting converaations")
    conversations = await run_Conversational_agents()

    # add conversations to final output
    final_output["conversations"]= conversations

    # save the config to a file
    with open("config.json", "w") as config_file:
        json.dump(final_output, config_file, indent=4)

    return  final_output