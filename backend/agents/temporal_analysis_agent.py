agent_manifest = {
    "agent_name": "temporal_analysis_agent",
    "purpose": "Evaluates temporal coherence via motion smoothness and jitter detection.",
    
}

import numpy as np
import cv2
import torch
from sklearn.metrics.pairwise import cosine_similarity

async def run(input_data: dict) -> dict:
    frames = input_data.get("video_frames", [])
    motion_vectors = input_data.get("motion_vectors", [])
    embeddings = input_data.get("visual_embeddings", [])

    # print("Input Data:", input_data)

    if not frames or not motion_vectors or not embeddings:
        raise ValueError("Missing one or more required inputs: 'video_frames', 'motion_vectors', 'visual_embeddings'")

    # Temporal Coherence (using cosine similarity of embeddings)
    emb_array = np.array(embeddings)
    similarities = [cosine_similarity([emb_array[i]], [emb_array[i+1]])[0][0] for i in range(len(emb_array)-1)]
    coherence_score = round(np.mean(similarities), 4)

    # Motion Analysis (mean, spikes)
    mv_array = np.array([float(m) for m in motion_vectors])
    motion_mean = round(np.mean(mv_array), 4)
    motion_std = round(np.std(mv_array), 4)
    motion_spikes = [i for i, val in enumerate(mv_array) if val > (motion_mean + 2 * motion_std)]

    # Scene Transitions by embedding jump
    embedding_jumps = [1 - similarities[i] for i in range(len(similarities))]
    scene_transitions = [i+1 for i, val in enumerate(embedding_jumps) if val > 0.4]  # 0.4 is an empirical threshold
    
    temporal_output = {
        "temporal_coherence": coherence_score,
        "motion_statistics": {
            "mean_motion": motion_mean,
            "motion_std_dev": motion_std,
            "spike_frames": motion_spikes
        },
        "scene_transitions": scene_transitions,
    }
    print("Temporal Output:")
    
    return temporal_output
