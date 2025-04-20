# agents/extractors/redundancy_agent.py

from data.Config import config
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

agent_manifest = {
    "agent_name": "redundancy_agent",
    "purpose": "Detects semantic and visual redundancy in video frames.",
}

async def run() -> None:
    semantic_tags = config.analysis.perception_agent.get("semantic_tags", [])
    visual_embeddings = config.analysis.perception_agent.get("visual_embeddings", [])

    if not semantic_tags or not visual_embeddings:
        raise ValueError("Missing semantic tags or visual embeddings.")

    # -- Semantic Redundancy
    captions = [tags[0].strip().lower() for tags in semantic_tags if tags]
    total = len(captions)
    unique = len(set(captions))
    semantic_redundancy = round(1 - (unique / total), 4) if total > 0 else 1.0

    # -- Visual Redundancy
    embeddings = np.array(visual_embeddings)
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    if embeddings.shape[0] < 2:
        visual_variability = 0.0
    else:
        similarities = [
            cosine_similarity([embeddings[i]], [embeddings[i+1]])[0][0]
            for i in range(len(embeddings) - 1)
        ]
        visual_variability = round(1 - np.mean(similarities), 4) if similarities else 0.0

    # -- Redundancy Summary
    if semantic_redundancy > 0.8 and visual_variability < 0.2:
        summary = "High semantic and visual redundancy detected."
    elif semantic_redundancy > 0.6 or visual_variability < 0.3:
        summary = "Moderate redundancy — content repeats observed."
    else:
        summary = "Low redundancy — video content is diverse."

    config.analysis.redundancy_agent = {
        "semantic_redundancy": semantic_redundancy,
        "visual_variability": visual_variability,
        "summary": summary
    }

    print(f"[redundancy_agent] {config.analysis.redundancy_agent}")
