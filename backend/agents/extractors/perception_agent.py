# agents/perception_agent.py

import numpy as np
import cv2
import torch
import torchvision.transforms as T
from PIL import Image
from torchvision.models import resnet18, ResNet18_Weights
from transformers import BlipProcessor, BlipForConditionalGeneration
from data.Config import config
from  utils.constant import STOPWORDS

agent_manifest = {
    "agent_name": "perception_agent",
    "purpose": "Extracts perceptual features, visual embeddings, and semantic tags using BLIP + ResNet.",
}

# Load models once
resnet = resnet18(weights=ResNet18_Weights.DEFAULT)
resnet.eval()

transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model.eval()

async def run() -> None:
    frames_data = config.analysis.video_ingestion_agent.get("frames", [])
    if not frames_data:
        raise ValueError("No frames found for perception analysis.")

    print(f"[perception_agent] Processing {len(frames_data)} frames...")

    brightness_series = []
    motion_vectors = []
    scene_changes = []
    visual_embeddings = []
    semantic_tags = []

    prev_gray = None
    prev_hist = None

    for idx, frame_data in enumerate(frames_data):
        frame = frame_data["frame"]

        # -- Brightness
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        brightness_series.append(np.mean(gray))

        # -- Scene Change Detection
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        scene_changes.append(cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA) > 0.3 if prev_hist is not None else False)
        prev_hist = hist

        # -- Optical Flow Motion
        if prev_gray is not None:
            flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            motion_vectors.append(np.mean(np.linalg.norm(flow, axis=2)))
        else:
            motion_vectors.append(0.0)
        prev_gray = gray

        # -- Visual Embeddings via ResNet
        img_pil = Image.fromarray(frame)
        img_tensor = transform(img_pil).unsqueeze(0)
        with torch.no_grad():
            embedding = resnet(img_tensor).squeeze().numpy()
        visual_embeddings.append(embedding)

        # -- Semantic Tag using BLIP
        with torch.no_grad():
            inputs = processor(images=img_pil, return_tensors="pt")
            output = blip_model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True)
        semantic_tags.append([caption])
        print(f"[Frame {idx}] Caption: {caption}")

    # -- Unique Tags Filtering
    unique_tags = set()
    for tags in semantic_tags:
        unique_tags.update(word.lower() for word in tags[0].split() if word.lower() not in STOPWORDS)

    # -- Save to config
    config.analysis.perception_agent = {
        "visual_embeddings": visual_embeddings,
        "semantic_tags": semantic_tags,
        "unique_tags": unique_tags,
        "motion_vectors": motion_vectors,
        "scene_changes": scene_changes,
        "brightness_series": brightness_series,
    }
