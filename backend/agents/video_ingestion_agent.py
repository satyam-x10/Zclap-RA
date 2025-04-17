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
    },  
}


import cv2

def run(video_path: str):
    frames = []
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret: break
        frames.append(frame)
    cap.release()
    return frames
