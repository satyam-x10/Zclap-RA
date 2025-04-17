# agents/video_ingestion_agent.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import cv2
import agents.perception_agent as perception_agent
import agents.temporal_analysis_agent as temporal_agent
import agents.semantic_analysis_agent as semantic_agent
import agents.dynamics_robustness_agent as dynamics_agent
import agents.generalization_agent as generalization_agent
import agents.reasoning_agent as reasoning_agent
import agents.reporting_agent as reporting_agent

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

def run(input_data: dict) -> dict:
    video_path = input_data.get("video_file", "video.mp4")

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file '{video_path}' not found.")

    frames = []
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Failed to open video file: {video_path}")

    print(f" Ingesting video: {video_path}")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    print(f" Extracted {len(frames)} frames from {video_path}")

    return {"video_frames": frames,"prompt":"A video of a cat playing with a ball"} 


def start_analysis():
    # Example usage
    input_data = {
        "video_file": "../video.mp4"
    }
    output_data = run(input_data)
    perception_data = perception_agent.run(output_data)
    temporal_data = temporal_agent.run(perception_data)
    semantic_data = semantic_agent.run(output_data)
    dynamics_data = dynamics_agent.run(perception_data)
    generalised_data = generalization_agent.run(perception_data)

    reasoning_input = {
    **temporal_data,
    **semantic_data,
    **dynamics_data,
    **generalised_data
}

    reasoning_data = reasoning_agent.run(reasoning_input)

    reporting_data = reporting_agent.run(reasoning_data)
    print(f"Output data: {reporting_data}")