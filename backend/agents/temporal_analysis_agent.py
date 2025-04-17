agent_manifest = {
    "agent_name": "temporal_analysis_agent",
    "purpose": "Evaluates temporal coherence via motion smoothness and jitter detection.",
    "agent_type": "analysis",
    "input_format": ["video_frames"],
    "output_format": ["temporal_coherence_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["optical_flow_analysis", "jitter_detection"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frames"
    },
    "output_type_details": {
        "temporal_coherence_score": "Float between 0 and 1"
    },
}

import numpy as np
import cv2

def run(frames):
    scores = []
    for i in range(1, len(frames)):
        flow = cv2.absdiff(frames[i], frames[i-1])
        scores.append(np.mean(flow))
    temporal_score = 1.0 - np.mean(scores) / 255  # Normalize
    return {"temporal_coherence_score": round(temporal_score, 2)}
