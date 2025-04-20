import os
import cv2
from typing import Dict, Any, List

from data.Config import config 

agent_manifest = {
    "agent_name": "video_ingestion_agent",
    "purpose": "Agent for ingesting video files and extracting frames.",
}

async def run() -> Dict[str, Any]:
    video_path = config.video_file_path
    target_frame_rate = config.frame_rate

    if not video_path or not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file '{video_path}' not found.")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Failed to open video file: {video_path}")

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = total_frames / original_fps if original_fps > 0 else None

    frame_interval = int(original_fps // target_frame_rate) if original_fps > 0 else 1
    if frame_interval == 0:
        frame_interval = 1

    extracted_frames: List[Dict[str, Any]] = []
    frame_idx = 0
    extracted_idx = 0

    print(f"Ingesting video: {video_path} at {target_frame_rate} fps...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_interval == 0:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            extracted_frames.append({
                "id": extracted_idx,
                "frame": rgb_frame
            })
            extracted_idx += 1

        frame_idx += 1

    cap.release()

    config.analysis.video_ingestion_agent = {
        "frames": extracted_frames,
        "metadata": {
            "original_fps": original_fps,
            "target_fps": target_frame_rate,
            "frame_dimensions": (width, height),
            "duration_seconds": duration,
            "total_frames_extracted": len(extracted_frames)
        }
    }
    # print(f"Video ingestion completed. {config.analysis.video_ingestion_agent}")
