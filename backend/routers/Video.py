from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.video_utils import save_upload_file
from evaluations.pipeline import run_pipeline

router = APIRouter()

import numpy as np

def convert_numpy_types(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(i) for i in obj]
    elif isinstance(obj, np.generic):
        return obj.item()
    else:
        return obj


@router.post("/video")
async def receive_data(
    jsonData: str = Form(...),
    fileData: UploadFile = File(...)
):
    # Parse the JSON string into a Python dict
    parsed_json = json.loads(jsonData)
    file_path = save_upload_file(fileData)

    # You can save the file or process it
    file_content = await fileData.read()
    analysis = await run_pipeline(file_path, parsed_json)

    file_info = {
        "filename": fileData.filename,
        "content_type": fileData.content_type,
        "size": len(file_content),
    }

    # return analysis

    final_output = {
        "received": True,
        "jsonData": parsed_json,
        "fileData": file_info,
        "savedTo": file_path,
        "analysis": analysis
    }
    print("Final Output:", final_output)

    return convert_numpy_types(final_output)