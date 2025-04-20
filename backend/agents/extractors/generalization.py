# agents/generalization_agent.py

import numpy as np
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from data.Config import config

agent_manifest = {
    "agent_name": "generalization_agent",
    "purpose": "Evaluates generalization by measuring redundancy, diversity, and visual variability.",
}

async def run() -> None:
    semantic_tags = config.analysis.perception_agent.get("semantic_tags", [])
    visual_embeddings = config.analysis.perception_agent.get("visual_embeddings", [])
    unique_tags = config.analysis.perception_agent.get("unique_tags", set())
    semantic_score = config.analysis.semantic_analysis_agent.get("semantic_consistency_score", 1.0)
    prompt_text = config.prompt.lower() if config.prompt else ""

    if not semantic_tags or not visual_embeddings:
        raise ValueError("Missing semantic tags or visual embeddings.")

    # Flatten semantic captions
    flat_captions = [tag[0].lower() for tag in semantic_tags if tag]

    # -- Diversity Index
    unique_captions = list(set(flat_captions))
    diversity_index = round(len(unique_captions) / len(flat_captions), 4)

    # -- Repetition Ratio
    caption_freq = Counter(flat_captions)
    most_common_sentence, repeat_count = caption_freq.most_common(1)[0]
    repetition_ratio = round(repeat_count / len(flat_captions), 4)

    # -- Visual Embedding Variability
    embeddings = np.array(visual_embeddings)
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    if embeddings.shape[0] < 2:
        visual_variability = 0.0
    else:
        diffs = [
            cosine_similarity([embeddings[i]], [embeddings[i + 1]])[0][0]
            for i in range(len(embeddings) - 1)
        ]
        visual_variability = round(1 - np.mean(diffs), 4) if diffs else 0.0

    # -- Tag-Prompt Overlap
    prompt_words = set(prompt_text.replace(',', '').replace('.', '').split())
    tag_matches = [tag for tag in prompt_words if tag in unique_tags]

    # -- Generalization Score (heuristic formula)
    generalisation_score = (
        0.25 * (1 - repetition_ratio) +
        0.25 * diversity_index +
        0.2 * visual_variability +
        0.1 * semantic_score
    )
    generalisation_score = round(min(1.0, max(0.0, generalisation_score)), 4)

    overfitting_warning = repetition_ratio > 0.8 and diversity_index < 0.2

    if generalisation_score > 0.75:
        analysis = "Model generalizes well across varied scenes."
    elif generalisation_score > 0.5:
        analysis = "Moderate generalization with repetitive bias."
    else:
        analysis = "Poor generalization — high redundancy or overfitting."

    # -- Save to config
    config.analysis.generalization_agent = {
    "generalisation_score": float(generalisation_score),
    "diversity_index": float(diversity_index),
    "repetition_ratio": float(repetition_ratio),
    "visual_variability": float(visual_variability),
    "semantic_score": float(round(semantic_score, 4)),
    "matched_tags": tag_matches,
    "overfitting_warning": bool(overfitting_warning),
    "most_common_sentence": most_common_sentence,
    "summary": analysis
    }
    # print("Generalization Agent Analysis:" ,config.analysis.generalization_agent)
    