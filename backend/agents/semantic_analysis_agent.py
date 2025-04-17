agent_manifest = {
    "agent_name": "semantic_analysis_agent",
    "purpose": "Analyzes visual-prompt alignment using vision-language models.",
    "agent_type": "analysis",
    "input_format": ["video_frames", "text_prompt"],
    "output_format": ["semantic_consistency_score"],
    "dependencies": ["video_ingestion_agent"],
    "supported_tasks": ["CLIP_matching"],
    "prompt_required": True,
    "input_type_details": {
        "video_frames": "List of video frame tensors",
        "text_prompt": "Prompt string"
    },
    "output_type_details": {
        "semantic_consistency_score": "Float between 0 and 1"
    },
}

import numpy as np
import cv2
import torch
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

async def run(input_data: dict) -> dict:
    frames = input_data.get("video_frames", [])
    motion_vectors = input_data.get("motion_vectors", [])
    embeddings = input_data.get("visual_embeddings", [])

    if not frames or not motion_vectors or not embeddings:
        raise ValueError("Missing one or more required inputs: 'video_frames', 'motion_vectors', 'visual_embeddings'")

    captions = []
    entity_map = {}
    event_segments = []
    prev_caption = None
    segment_start = 0

    # Generate captions
    for i, frame in enumerate(frames):
        print(f"Processing frame {i}...")
        
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img)
        inputs = processor(images=pil_img, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        captions.append(caption)

        # Entity tracking
        for word in caption.split():
            if word.lower() not in entity_map:
                entity_map[word.lower()] = [i, i]
            else:
                entity_map[word.lower()][1] = i

        # Segment events
        if caption != prev_caption:
            if prev_caption is not None:
                event_segments.append({"start": segment_start, "end": i - 1, "event": prev_caption})
            segment_start = i
            prev_caption = caption

    if prev_caption:
        event_segments.append({"start": segment_start, "end": len(frames) - 1, "event": prev_caption})

    # Semantic consistency
    from sentence_transformers import SentenceTransformer
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    caption_embeddings = sentence_model.encode(captions)
    similarities = [cosine_similarity([caption_embeddings[i]], [caption_embeddings[i+1]])[0][0] for i in range(len(captions) - 1)]
    semantic_consistency_score = round(np.mean(similarities), 4) if similarities else 1.0

    # Summary generation (simple)
    summary = ". ".join([seg["event"] for seg in event_segments]) + "."

    semantic_output = {
        "captions": captions,
        "semantic_consistency_score": semantic_consistency_score,
        "entity_map": entity_map,
        "event_segments": event_segments,
        "summary": summary
    }
    print("Semantic Analysis Output:")

    return semantic_output
