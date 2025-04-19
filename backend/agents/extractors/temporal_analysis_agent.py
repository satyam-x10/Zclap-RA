agent_manifest = {
    "agent_name": "temporal_analysis_agent",
    "purpose": "Evaluates temporal coherence via motion smoothness and jitter detection.", 
}

import numpy as np
import cv2
import torch
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import cv2
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
import torch
import torchvision.transforms as T
import torchvision.models as models
from data.Config import config
# Optional embedding model for temporal coherence
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
            flow = cv2.calcOpticalFlowFarneback(prev_gray, gray,
                                                None, 0.5, 3, 15, 3, 5, 1.2, 0)
            magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            avg_motion = np.mean(magnitude)
            motions.append(avg_motion)
        prev_gray = gray
    return motions

async def run() -> dict:
    frames = config.analysis.video_ingestion_agent.frames
    if not frames:
        raise ValueError("No frames found in input data.")
    if len(frames) < 3:
        return {"temporal_coherence": None, "reason": "Not enough frames for analysis"}

    # Step 1: Extract motion vectors
    motion_vectors = estimate_motion_vectors(frames)

    # Step 2: Extract embeddings
    embeddings = extract_embeddings(frames)

    if len(embeddings) < 2 or len(motion_vectors) < 1:
        raise ValueError("Not enough data to evaluate temporal coherence.")

    # Step 3: Compute cosine similarity between consecutive embeddings
    emb_array = np.array(embeddings)
    similarities = [cosine_similarity([emb_array[i]], [emb_array[i+1]])[0][0] for i in range(len(emb_array)-1)]
    coherence_score = round(np.mean(similarities), 4)

    # Step 4: Analyze motion spikes
    mv_array = np.array(motion_vectors)
    motion_mean = round(np.mean(mv_array), 4)
    motion_std = round(np.std(mv_array), 4)
    motion_spikes = [i for i, val in enumerate(mv_array) if val > (motion_mean + 2 * motion_std)]

    # Step 5: Scene transitions via embedding jumps
    embedding_jumps = [1 - s for s in similarities]
    scene_transitions = [i+1 for i, val in enumerate(embedding_jumps) if val > 0.4]  # configurable threshold
    
    config.analysis.temporal_analysis_agent = {
        "temporal_coherence": coherence_score,
        "motion_statistics": {
            "mean_motion": motion_mean,
            "motion_std_dev": motion_std,
            "spike_frames": motion_spikes
        },
        "scene_transitions": scene_transitions,
    }
