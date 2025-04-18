import os
import cv2

async def run(input_data: dict, target_frame_rate: int = 2) -> dict:
    video_path = input_data.get("video_file")

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file '{video_path}' not found.")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Failed to open video file: {video_path}")

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    if original_fps <= 0:
        raise ValueError("Could not retrieve FPS from video.")

    frame_interval = int(original_fps // target_frame_rate)
    if frame_interval == 0:
        frame_interval = 1  # Don't skip any frames if target is very high

    frames = []
    frame_idx = 0
    print(f"Ingesting video: {video_path}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_interval == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame)

        frame_idx += 1

    cap.release()
    print(f"Extracted {len(frames)} sampled frames from {video_path}")

    return {
        "video_frames": frames,
        "metadata": {
            "original_fps": original_fps,
            "target_frame_rate": target_frame_rate,
            "frame_count": len(frames),
        }
    }
