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

def run(frames):
    embeddings = [np.mean(frame, axis=(0, 1)).tolist() for frame in frames]
    return {"frame_embeddings": embeddings}
