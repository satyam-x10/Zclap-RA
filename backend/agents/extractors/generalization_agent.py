agent_manifest = {
    "agent_name": "generalization_agent",
    "purpose": "Tests performance on OOD videos to measure generalization.",
    
}

import numpy as np


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

import numpy as np
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

async def run(input_data: dict) -> dict:

    sentences = input_data.get("semantic_tags", [])
    semantic_score = float(input_data.get("semantic_consistency_score", 1.0))
    visual_embeddings = input_data.get("visual_embeddings", [])
    prompt = input_data.get("generation_prompt", "").lower()
    prompt= set(prompt.replace(',', '').replace('.', '').split())
    unique_tags = input_data.get("unique_tags", set())

    print('prompt:', prompt)
    print('unique_tags:', unique_tags)

    if not sentences or not visual_embeddings:
        raise ValueError("Missing required input fields")

    # Flatten semantic captions
    flat_captions = [cap[0].lower() for cap in sentences if cap]

    # 1. Diversity Index: Unique captions / total captions
    unique_captions = list(set(flat_captions))
    diversity_index = round(len(unique_captions) / len(flat_captions), 4)

    # 2. Caption Repetition Ratio
    caption_freq = Counter(flat_captions)
    most_common_sentence, repeat_count = caption_freq.most_common(1)[0]
    repetition_ratio = repeat_count / len(flat_captions)

    # 3. Visual Embedding Variability
    embeddings = np.array(visual_embeddings)
    if len(embeddings.shape) == 1:
        embeddings = embeddings.reshape(1, -1)
    elif len(embeddings.shape) == 2 and embeddings.shape[0] < 2:
        visual_variability = 0.0
    else:
        diffs = [
            cosine_similarity([embeddings[i]], [embeddings[i + 1]])[0][0]
            for i in range(len(embeddings) - 1)
        ]
        visual_variability = 1 - np.mean(diffs) if diffs else 0.0

    # 4. Tag-Prompt Overlap: fraction of unique_tags found in the prompt
    tag_matches = [tag for tag in prompt if tag in unique_tags ]

    # 5. Heuristic Generalization Score
    generalisation_score = (
        0.25 * (1 - repetition_ratio) +
        0.25 * diversity_index +
        0.2 * visual_variability +
        0.1 * semantic_score  # scaled since it's already 0–1
    )
    generalisation_score = round(min(1.0, max(0.0, generalisation_score)), 4)

    overfitting_warning = repetition_ratio > 0.8 and diversity_index < 0.2

    analysis = (
        "Model generalizes well across varied scenes."
        if generalisation_score > 0.75 else
        "Moderate generalization with repetitive bias."
        if generalisation_score > 0.5 else
        "Poor generalization — high redundancy or overfitting."
    )

    return {
        "generalisation_score": generalisation_score,
        "diversity_index": diversity_index,
        "repetition_ratio": round(repetition_ratio, 4),
        "visual_variability": round(visual_variability, 4),
        "semantic_score": round(semantic_score, 4),
        "matched_tags": tag_matches,
        "overfitting_warning": overfitting_warning,
        "analysis": analysis,
        "most_common_sentence": most_common_sentence,
    }
