from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.video_utils import save_upload_file
from evaluations.pipeline import run_analysis_pipeline
from utils.functions import convert_numpy_types
from data.Config import config
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
    analysis = await run_analysis_pipeline()    

    # return analysis

    final_output = {
        "received": True,
        "jsonData": parsed_config_json,
        "savedTo": video_file_path,
        "analysis": analysis
    }
    print("Final Output:", final_output)

    return convert_numpy_types(final_output)