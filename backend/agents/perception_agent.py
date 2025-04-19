agent_manifest = {
    "agent_name": "perception_agent",
    "purpose": "Extracts perceptual features and embeddings from video frames.",
      
}

import numpy as np
import cv2
import torch
import torchvision.transforms as T
from PIL import Image
from torchvision.models import resnet18

# Preload model once (ResNet for visual embeddings)
resnet = resnet18(pretrained=True)
resnet.eval()
transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


async def run(input_data: dict) -> dict:
    frames = input_data.get("video_frames", [])
    if not frames:
        raise ValueError("Missing input: 'video_frames'")

    print(f"Analyzing {len(frames)} frames...")

    brightness_series = []
    motion_vectors = []
    scene_changes = []
    visual_embeddings = []
    object_tags = []

    prev_gray = None
    prev_hist = None

    for i, frame in enumerate(frames):
        # Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # Brightness
        avg_brightness = np.mean(gray)
        brightness_series.append(avg_brightness)

        # Scene change detection via histogram difference
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        if prev_hist is not None:
            hist_diff = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA)
            scene_changes.append(hist_diff > 0.3)  # threshold: can be tuned
        else:
            scene_changes.append(False)
        prev_hist = hist

        # Motion
        if prev_gray is not None:
            flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None,
                                                 0.5, 3, 15, 3, 5, 1.2, 0)
            mean_flow = np.mean(np.linalg.norm(flow, axis=2))
            motion_vectors.append(mean_flow)
        else:
            motion_vectors.append(0.0)
        prev_gray = gray

        # Convert to PIL for ResNet
        img_pil = Image.fromarray(frame)
        img_tensor = transform(img_pil).unsqueeze(0)
        with torch.no_grad():
            embedding = resnet(img_tensor).squeeze().numpy()
        visual_embeddings.append(embedding)

        # Use BLIP for semantic object understanding
        inputs = processor(images=img_pil, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        object_tags.append([caption])
        print('caption was:', caption)

    unique_tags = set()
    for tags in object_tags:
        unique_tags.update(tags[0].split())
    print('unique_tags:', unique_tags)

    unique_tags_without_stopwords = set()
    stopwords = set(["a", "an", "the", "is", "are", "to", "and", "of"])
    for tag in unique_tags:
        if tag.lower() not in stopwords:
            unique_tags_without_stopwords.add(tag)

    perception_data = {
        "features": {
            "visual_embeddings": visual_embeddings,
            "unique_tags": unique_tags_without_stopwords,
            "semantic_tags": object_tags,
        },
        "motion_vectors": motion_vectors,
        "scene_changes": scene_changes,
        "frame_stats": {
            "brightness_series": brightness_series
        }
    }
    print("Perception data extracted successfully.")
    
    return perception_data
