# agents/semantic_analysis_agent.py

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from data.Config import config

agent_manifest = {
    "agent_name": "semantic_analysis_agent",
    "purpose": "Analyzes alignment and coherence of BLIP-generated semantic tags using sentence embeddings.",
}

sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

async def run() -> None:
    semantic_tags = config.analysis.perception_agent.get("semantic_tags", [])

    if not semantic_tags:
        raise ValueError("Missing semantic tags from perception agent.")

    tag_sequence = [tags[0].strip() if tags else "" for tags in semantic_tags]

    # -- Semantic Drift Segmentation
    semantic_segments = []
    prev_tag = None
    segment_start = 0

    for idx, tag in enumerate(tag_sequence):
        if tag != prev_tag:
            if prev_tag is not None:
                semantic_segments.append({
                    "start": segment_start,
                    "end": idx - 1,
                    "tag": prev_tag
                })
            segment_start = idx
            prev_tag = tag
    if prev_tag:
        semantic_segments.append({
            "start": segment_start,
            "end": len(tag_sequence) - 1,
            "tag": prev_tag
        })

    # -- Entity Map Extraction
    entity_map = {}
    for i, tag in enumerate(tag_sequence):
        for word in tag.split():
            word = word.lower()
            if word not in entity_map:
                entity_map[word] = [i, i]
            else:
                entity_map[word][1] = i

    # -- Semantic Consistency Score
    tag_embeddings = sentence_model.encode(tag_sequence)
    similarities = [
        cosine_similarity([tag_embeddings[i]], [tag_embeddings[i + 1]])[0][0]
        for i in range(len(tag_embeddings) - 1)
    ]
    semantic_consistency_score = round(float(np.mean(similarities)), 4) if similarities else 1.0

    # -- Save result to config
    config.analysis.semantic_analysis_agent = {
        "semantic_consistency_score": semantic_consistency_score,
        "semantic_segments": semantic_segments,
        "entity_map": entity_map,
        "sample_tags": tag_sequence[:10]  # preview
    }

    print("Semantic Analysis Agent Results:", config.analysis.semantic_analysis_agent)
