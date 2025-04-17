agent_manifest = {
    "agent_name": "perception_agent",
    "purpose": "Extracts perceptual features and embeddings from video frames.",
    "agent_type": "feature_extractor",
    "input_format": ["video_frames"],
    "output_format": ["frame_embeddings"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["feature_embedding"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frames"
    },
    "output_type_details": {
        "frame_embeddings": "List of feature vectors"
    },  
}

import numpy as np
import cv2

def run(input_data: dict) -> dict:
    frames = input_data.get("video_frames", [])
    if not frames:
        raise ValueError("Missing input: 'video_frames'")

    print(f" Analyzing {len(frames)} frames...")

    frame_shape = frames[0].shape
    num_frames = len(frames)

    avg_brightness = []
    motion_vectors = []

    prev_gray = None

    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_brightness.append(np.mean(gray))

        if prev_gray is not None:
            diff = cv2.absdiff(prev_gray, gray)
            motion_vectors.append(np.mean(diff))  # Simplified motion
        prev_gray = gray

    # Compute aggregates
    features = {
        "resolution": f"{frame_shape[1]}x{frame_shape[0]}",
        "frame_count": num_frames,
        "avg_brightness": round(np.mean(avg_brightness), 2),
        "brightness_std": round(np.std(avg_brightness), 2),
    }

    return {
        "features": features,
        "motion_vectors": motion_vectors,
        "frame_stats": {
            "brightness_series": avg_brightness
        }
    }