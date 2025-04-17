agent_manifest = {
    "agent_name": "dynamics_robustness_agent",
    "purpose": "Tests robustness under fast motion, lighting or angle variation.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["dynamic_scene_handling_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["motion_robustness"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frame tensors"
    },
    "output_type_details": {
        "dynamic_scene_handling_score": "Float between 0 and 1"
    },  
}


import numpy as np
import cv2

def run(frames):
    diffs = []
    for i in range(1, len(frames)):
        diff = cv2.absdiff(frames[i], frames[i-1])
        diffs.append(np.mean(diff))
    stability = 1.0 - np.std(diffs) / 255
    return {"dynamic_scene_handling_score": round(stability, 2)}
