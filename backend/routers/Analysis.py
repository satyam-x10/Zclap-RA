from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.video_utils import save_upload_file
from evaluations.pipeline import run_analysis_pipeline
from utils.functions import convert_numpy_types
from data.Config import config
from utils.functions import extract_config_data

router = APIRouter()

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

    # return analysis
    analysis_data = extract_config_data(config.analysis)
    analysis_data.pop("video_ingestion_agent", None)  # safely remove if exists

    final_output = {
        "received": True,
        "jsonData": parsed_config_json,
        "savedTo": video_file_path,
        "config": extract_config_data(config),
        "analysis": analysis_data,
    }
    print("Final Output:", final_output)

    # save in a json file
    with open("output.json", "w") as outfile:
        json.dump(convert_numpy_types(final_output), outfile, indent=4)

    return convert_numpy_types(final_output)