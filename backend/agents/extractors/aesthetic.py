# agents/extractors/aesthetic_agent.py

import numpy as np
import cv2
from data.Config import config

agent_manifest = {
    "agent_name": "aesthetic_agent",
    "purpose": "Estimates visual appeal of video frames using basic perceptual metrics.",
}

async def run() -> None:
    frames_data = config.analysis.video_ingestion_agent.get("frames", [])
    brightness_series = config.analysis.perception_agent.get("brightness_series", [])

    if not frames_data or not brightness_series:
        raise ValueError("Missing frame data or brightness series.")

    brightness = np.array(brightness_series)
    brightness_mean = round(np.mean(brightness), 2)
    brightness_std = round(np.std(brightness), 2)

    # Brightness quality: penalize too dark (<40) or too bright (>200)
    bad_brightness = np.sum((brightness < 40) | (brightness > 200))
    bad_ratio = round(bad_brightness / len(brightness), 4)

    # Colorfulness metric (simplified)
    colorfulness_scores = []
    for frame_data in frames_data:
        frame = frame_data["frame"]
        (B, G, R) = cv2.split(frame.astype("float"))
        rg = np.absolute(R - G)
        yb = np.absolute(0.5 * (R + G) - B)
        std_root = np.sqrt(np.std(rg) ** 2 + np.std(yb) ** 2)
        mean_root = np.sqrt(np.mean(rg) ** 2 + np.mean(yb) ** 2)
        colorfulness = std_root + (0.3 * mean_root)
        colorfulness_scores.append(colorfulness)

    avg_colorfulness = round(np.mean(colorfulness_scores), 2)

    # Final aesthetic score (normalized heuristic)
    aesthetic_score = round((1 - bad_ratio) * min(1.0, avg_colorfulness / 100), 4)

    summary = (
        "Frames are visually appealing and well-lit." if aesthetic_score > 0.7 else
        "Moderately aesthetic — some visual inconsistency." if aesthetic_score > 0.4 else
        "Poor visual aesthetics — likely dull, noisy, or overexposed frames."
    )

    config.analysis.aesthetic_agent = {
        "brightness_mean": brightness_mean,
        "brightness_std": brightness_std,
        "bad_brightness_ratio": bad_ratio,
        "avg_colorfulness": avg_colorfulness,
        "aesthetic_score": aesthetic_score,
        "summary": summary
    }
    # print (f"Aesthetic Agent: {config.analysis.aesthetic_agent}"