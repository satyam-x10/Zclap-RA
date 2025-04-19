import os
from fastapi import UploadFile
from datetime import datetime
from data.Config import config

UPLOAD_DIR = "data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(upload_file: UploadFile) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{upload_file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path

def extract_config():

    parsed_json = config.parsed_config_json

    config.prompt = parsed_json["prompt"]
    config.frame_rate = parsed_json["frame_rate"]
    config.pipeline_mode = parsed_json["pipeline_mode"]
    config.report_format = parsed_json["report_format"]
    config.primary_agents = parsed_json["agents"]["primary_agents"]
    config.secondary_agents = parsed_json["agents"]["secondary_agents"]
    config.meta_agents = parsed_json["agents"]["meta_agents"]
