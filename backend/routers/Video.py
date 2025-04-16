from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.video_utils import save_upload_file
router = APIRouter()

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
    file_info = {
        "filename": fileData.filename,
        "content_type": fileData.content_type,
        "size": len(file_content),
    }

    return {
        "received": True,
        "jsonData": parsed_json,
        "fileData": file_info,
        "savedTo": file_path
    }