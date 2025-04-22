from data.Config import config
from utils.constant import STOPWORDS
from sentence_transformers import SentenceTransformer, util

agent_manifest = {
    "agent_name": "caption_alignment_agent",
    "purpose": "Measures how well frame-level captions reflect the prompt using semantic similarity.",
}

sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

def tokenize(text: str):
    return [
        word.strip(".,!?").lower()
        for word in text.split()
        if word.isalpha() and word.lower() not in STOPWORDS
    ]

async def run() -> None:
    semantic_tags = config.analysis.perception_agent.get("semantic_tags", [])
    prompt = config.prompt.lower() if config.prompt else ""

    if not semantic_tags or not prompt:
        raise ValueError("Missing semantic tags or prompt.")

    # Step 1: Clean prompt words
    prompt_words = tokenize(prompt)
    if not prompt_words:
        raise ValueError("No usable words in prompt.")

    # Step 2: Clean caption words
    tag_words = []
    for tags in semantic_tags:
        caption = tags[0]
        tag_words.extend(tokenize(caption))
    tag_words = list(set(tag_words))  # remove duplicates

    if not tag_words:
        raise ValueError("No usable words in captions.")

    # Step 3: Semantic matching
    matched_words = []
    prompt_embeddings = sentence_model.encode(prompt_words, convert_to_tensor=True)
    tag_embeddings = sentence_model.encode(tag_words, convert_to_tensor=True)

    for i, p_word in enumerate(prompt_words):
        sims = util.cos_sim(prompt_embeddings[i], tag_embeddings)
        if sims.max().item() > 0.7:
            matched_words.append(p_word)

    match_ratio = round(len(matched_words) / len(prompt_words), 4)

    summary = (
        "Captions strongly reflect the prompt." if match_ratio > 0.75 else
        "Moderate reflection of prompt." if match_ratio > 0.4 else
        "Weak alignment — prompt details missing in captions."
    )

    config.analysis.caption_alignment_agent = {
        "filtered_prompt_words": prompt_words,
        "matched_words": matched_words,
        "match_ratio": match_ratio,
        "summary": summary
    }
