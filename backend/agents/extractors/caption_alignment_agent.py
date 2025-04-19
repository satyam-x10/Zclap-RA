# agents/extractors/caption_alignment_agent.py

from data.Config import config
from collections import Counter
from utils.constant import STOPWORDS
agent_manifest = {
    "agent_name": "caption_alignment_agent",
    "purpose": "Measures how well frame-level captions reflect the prompt.",
}


async def run() -> None:
    semantic_tags = config.analysis.perception_agent.get("semantic_tags", [])
    prompt = config.prompt.lower() if config.prompt else ""

    if not semantic_tags or not prompt:
        raise ValueError("Missing semantic tags or prompt.")

    # -- Step 1: Extract clean words from prompt (minus stopwords)
    prompt_words = set([
        word.strip(",.") for word in prompt.split()
        if word not in STOPWORDS
    ])

    # -- Step 2: Extract clean words from all BLIP captions
    tag_words = []
    for tags in semantic_tags:
        caption = tags[0].lower()
        tag_words.extend([
            word.strip(",.") for word in caption.split()
            if word not in STOPWORDS
        ])

    tag_counter = Counter(tag_words)

    # -- Step 3: Match only prompt → semantic_tags
    matched_prompt_words = [word for word in prompt_words if word in tag_counter]
    match_ratio = round(len(matched_prompt_words) / len(prompt_words), 4) if prompt_words else 0.0

    summary = (
        "Captions strongly reflect the prompt." if match_ratio > 0.75 else
        "Moderate reflection of prompt." if match_ratio > 0.4 else
        "Weak alignment — prompt details missing in captions."
    )

    config.analysis.caption_alignment_agent = {
        "filtered_prompt_words": list(prompt_words),
        "matched_words": matched_prompt_words,
        "match_ratio": match_ratio,
        "summary": summary
    }

    print(f"[caption_alignment_agent] {summary}")
