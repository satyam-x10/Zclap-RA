agent_manifest = {
    "agent_name": "semantic_analysis_agent",
    "purpose": "Analyzes visual-prompt alignment using vision-language models.",
    
}

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

async def run(input_data: dict) -> dict:
    frames = input_data.get("video_frames", [])
    semantic_tags = input_data.get("semantic_tags", [])
    visual_embeddings = input_data.get("visual_embeddings", [])

    if not frames or not semantic_tags or not visual_embeddings:
        raise ValueError("Missing required inputs: 'video_frames', 'semantic_tags', or 'visual_embeddings'.")

    # Semantic Drift Segmentation
    tag_sequence = [tags[0] if tags else "" for tags in semantic_tags]
    semantic_segments = []
    prev_tag, segment_start = None, 0
    for idx, tag in enumerate(tag_sequence):
        if tag != prev_tag:
            if prev_tag is not None:
                semantic_segments.append({"start": segment_start, "end": idx - 1, "tag": prev_tag})
            segment_start = idx
            prev_tag = tag
    if prev_tag:
        semantic_segments.append({"start": segment_start, "end": len(tag_sequence) - 1, "tag": prev_tag})

    # Entity Extraction
    entity_map = {}
    for i, tag in enumerate(tag_sequence):
        for word in tag.split():
            word = word.lower()
            if word not in entity_map:
                entity_map[word] = [i, i]
            else:
                entity_map[word][1] = i

    # Semantic Consistency Score using Sentence Embeddings
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    tag_embeddings = sentence_model.encode(tag_sequence)
    similarities = [cosine_similarity([tag_embeddings[i]], [tag_embeddings[i+1]])[0][0]
                    for i in range(len(tag_embeddings) - 1)]
    semantic_consistency_score = round(np.mean(similarities), 4) if similarities else 1.0

    # Semantic Summary

    semantic_output = {
        "semantic_consistency_score": semantic_consistency_score,
        "semantic_segments": semantic_segments,
        "entity_map": entity_map,
    }
    print(f"Semantic Analysis Output: {semantic_output}")

    return semantic_output
