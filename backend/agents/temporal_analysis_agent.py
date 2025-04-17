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
import torch
from sklearn.metrics.pairwise import cosine_similarity

async def run(input_data: dict) -> dict:
    frames = input_data.get("video_frames", [])
    motion_vectors = input_data.get("motion_vectors", [])
    embeddings = input_data.get("visual_embeddings", [])
    object_tags = input_data.get("object_tags", [])

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

    # Semantic Drift
    tag_sequence = [tags[0] if tags else "" for tags in object_tags]
    semantic_segments = []
    prev_tag = None
    segment_start = 0
    for idx, tag in enumerate(tag_sequence):
        if tag != prev_tag:
            if prev_tag is not None:
                semantic_segments.append({"start": segment_start, "end": idx-1, "tag": prev_tag})
            segment_start = idx
            prev_tag = tag
    if prev_tag:
        semantic_segments.append({"start": segment_start, "end": len(tag_sequence)-1, "tag": prev_tag})

    temporal_output = {
        "temporal_coherence": coherence_score,
        "motion_statistics": {
            "mean_motion": motion_mean,
            "motion_std_dev": motion_std,
            "spike_frames": motion_spikes
        },
        "scene_transitions": scene_transitions,
        "semantic_drift": semantic_segments
    }
    print("Temporal Output:", temporal_output)
    
    return temporal_output
