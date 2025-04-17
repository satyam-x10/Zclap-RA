agent_manifest = {
    "agent_name": "generalization_agent",
    "purpose": "Tests performance on OOD videos to measure generalization.",
    "agent_type": "analysis",
    "input_format": ["video_frames", "semantic_consistency_score"],
    "output_format": ["generalization_score"],
    "dependencies": ["semantic_analysis_agent"],
    "supported_tasks": ["ood_detection", "distribution_shift_analysis"],
    "prompt_required": False,
    "input_type_details": {
        "video_frames": "List of video frames",
        "semantic_consistency_score": "Float"
    },
    "output_type_details": {
        "generalization_score": "Float between 0 and 1"
    },
}

import numpy as np


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

async def run(input_data: dict) -> dict:
    captions = input_data.get("captions", [])
    event_segments = input_data.get("event_segments", [])
    semantic_score = input_data.get("semantic_consistency_score", 1.0)
    visual_embeddings = input_data.get("visual_embeddings", [])

    if not captions or not event_segments or not visual_embeddings:
        raise ValueError("Missing required input fields")

    # 1. Diversity Index: Unique captions / total captions
    unique_captions = list(set(captions))
    diversity_index = round(len(unique_captions) / len(captions), 4)

    # 2. Caption Distribution
    caption_freq = Counter(captions)
    most_common_caption, repeat_count = caption_freq.most_common(1)[0]
    repetition_ratio = repeat_count / len(captions)

    # 3. Coverage: extract top entities or key terms from event descriptions
    coverage_terms = list(set(seg["event"] for seg in event_segments))

    # 4. Visual embedding spread: cosine variance as generalization marker
    embeddings = np.array(visual_embeddings)
    embedding_diffs = [
        cosine_similarity([embeddings[i]], [embeddings[i+1]])[0][0]
        for i in range(len(embeddings) - 1)
    ]
    visual_variability = 1 - np.mean(embedding_diffs) if embedding_diffs else 0.0

    # 5. Heuristic Scoring
    generalisation_score = (
        0.4 * (1 - repetition_ratio) +
        0.3 * diversity_index +
        0.3 * visual_variability
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

    generalisation_output = {
        "generalisation_score": generalisation_score,
        "diversity_index": diversity_index,
        "repetition_ratio": round(repetition_ratio, 4),
        "coverage": coverage_terms,
        "visual_variability": round(visual_variability, 4),
        "overfitting_warning": overfitting_warning,
        "analysis": analysis
    }

    print("Generalization Analysis:")

    return generalisation_output
