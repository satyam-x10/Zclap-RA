# agents/video_ingestion_agent.py
import os
import cv2

# Metadata about the agent
agent_manifest = {
    "agent_name": "video_ingestion_agent",
    "purpose": "Handles video loading, format validation, and preprocessing (frame extraction, resizing, etc.).",
    "agent_type": "ingestion",
    "input_format": ["video_file"],
    "output_format": ["video_frames"],
    "dependencies": [],
    "supported_tasks": ["video_validation", "frame_extraction"],
    "prompt_required": False,
    "input_type_details": {
        "video_file": "Path to video file (str)"
    },
    "output_type_details": {
        "video_frames": "List of video frame tensors or image arrays"
    }
}

import os
import cv2

async def run(input_data: dict) -> dict:
    video_path =os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "video.mp4"))
    prompt = input_data.get("prompt", "No prompt provided")

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file '{video_path}' not found.")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Failed to open video file: {video_path}")

    frames = []
    print(f"Ingesting video: {video_path}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Optional
        frames.append(frame)

    cap.release()
    print(f"Extracted {len(frames)} frames from {video_path}")

    return {
        "video_frames": frames,
        "prompt": prompt,
        "metadata": {
            "fps": cap.get(cv2.CAP_PROP_FPS),
            "frame_count": len(frames),
        }
    }
