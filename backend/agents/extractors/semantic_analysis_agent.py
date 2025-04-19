# agents/semantic_analysis_agent.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from data.Config import config
import numpy as np

agent_manifest = {
    "agent_name": "semantic_analysis_agent",
    "purpose": "Analyzes visual-prompt alignment and semantic coherence using vision-language embeddings.",
}

async def run() -> None:
    frames_data = config.analysis.video_ingestion_agent.get("frames", [])
    prompt = config.prompt

    if not frames_data or not prompt:
        raise ValueError("Missing frames or prompt in config.")

    frame_captions = [prompt for _ in frames_data]  # Placeholder: replace with actual captions per frame

    # -- Tag Sequence (stubbed; ideally generated via a vision-language model like BLIP)
    semantic_tags = [caption.lower().split()[:4] for caption in frame_captions]  # Tokenized prompts
    tag_sequence = [tags[0] if tags else "" for tags in semantic_tags]

    # -- Semantic Drift Segmentation
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
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    tag_embeddings = sentence_model.encode(tag_sequence)
    similarities = [
        cosine_similarity([tag_embeddings[i]], [tag_embeddings[i + 1]])[0][0]
        for i in range(len(tag_embeddings) - 1)
    ]
    semantic_consistency_score = round(np.mean(similarities), 4) if similarities else 1.0

    # -- Store in config
    config.analysis.semantic_analysis_agent = {
        "semantic_consistency_score": semantic_consistency_score,
        "semantic_segments": semantic_segments,
        "entity_map": entity_map,
        "tags_used": tag_sequence[:10],  # Optional preview
    }

    print(f"[semantic_analysis_agent] Semantic Consistency Score: {semantic_consistency_score}")
