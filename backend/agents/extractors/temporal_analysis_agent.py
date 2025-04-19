# agents/temporal_analysis_agent.py

import numpy as np
import cv2
import torch
from sklearn.metrics.pairwise import cosine_similarity
import torchvision.transforms as T
import torchvision.models as models
from typing import List
from data.Config import config

agent_manifest = {
    "agent_name": "temporal_analysis_agent",
    "purpose": "Evaluates temporal coherence via embedding smoothness and motion vector variance.",
}

# Load embedding model
resnet_model = models.resnet18(pretrained=True)
resnet_model.eval()

transform = T.Compose([
    T.ToPILImage(),
    T.Resize((224, 224)),
    T.ToTensor()
])

def extract_embeddings(frames: List[np.ndarray]) -> List[np.ndarray]:
    embeddings = []
    for frame in frames:
        img_tensor = transform(frame).unsqueeze(0)
        with torch.no_grad():
            features = resnet_model(img_tensor).squeeze().numpy()
        embeddings.append(features)
    return embeddings

def estimate_motion_vectors(frames: List[np.ndarray]) -> List[float]:
    motions = []
    prev_gray = None
    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        if prev_gray is not None:
            flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None,
                                                0.5, 3, 15, 3, 5, 1.2, 0)
            magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            avg_motion = np.mean(magnitude)
            motions.append(avg_motion)
        prev_gray = gray
    return motions

async def run() -> None:
    frame_data = config.analysis.video_ingestion_agent.get("frames", [])
    if not frame_data or len(frame_data) < 3:
        config.analysis.temporal_analysis_agent = {
            "temporal_coherence": None,
            "reason": "Not enough frames for temporal analysis."
        }
        return

    frames = [f["frame"] for f in frame_data]

    # Step 1: Motion vectors
    motion_vectors = estimate_motion_vectors(frames)

    # Step 2: Frame embeddings
    embeddings = extract_embeddings(frames)
    if len(embeddings) < 2:
        raise ValueError("Not enough embeddings for similarity comparison.")

    # Step 3: Cosine similarity for temporal coherence
    emb_array = np.array(embeddings)
    similarities = [
        cosine_similarity([emb_array[i]], [emb_array[i + 1]])[0][0]
        for i in range(len(emb_array) - 1)
    ]
    coherence_score = round(np.mean(similarities), 4)

    # Step 4: Motion stats
    motion_mean = round(np.mean(motion_vectors), 4)
    motion_std = round(np.std(motion_vectors), 4)
    spike_frames = [
        i for i, val in enumerate(motion_vectors)
        if val > (motion_mean + 2 * motion_std)
    ]

    # Step 5: Scene transitions from embedding jumps
    embedding_jumps = [1 - sim for sim in similarities]
    scene_transitions = [i + 1 for i, jump in enumerate(embedding_jumps) if jump > 0.4]

    # Save to config
    config.analysis.temporal_analysis_agent = {
        "temporal_coherence": coherence_score,
        "mean_motion": motion_mean,
        "motion_std_dev": motion_std,
        "spike_frames": spike_frames,
        "scene_transitions": scene_transitions,
    }
