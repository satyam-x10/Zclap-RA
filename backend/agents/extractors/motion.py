# agents/extractors/motion_agent.py

import numpy as np
from data.Config import config

agent_manifest = {
    "agent_name": "motion_agent",
    "purpose": "Analyzes motion intensity patterns and burstiness in the video.",
}

async def run() -> None:
    motion_vectors = config.analysis.perception_agent.get("motion_vectors", [])
    
    if not motion_vectors:
        raise ValueError("Missing motion vectors from perception agent.")

    mv = np.array(motion_vectors)
    motion_mean = round(np.mean(mv), 4)
    motion_std = round(np.std(mv), 4)
    motion_min = round(np.min(mv), 4)
    motion_max = round(np.max(mv), 4)

    # Detect spikes (motion bursts) and flat regions (static)
    motion_bursts = [i for i, v in enumerate(mv) if v > motion_mean + motion_std]
    static_regions = [i for i, v in enumerate(mv) if v < motion_mean * 0.5]

    summary = (
        "Video shows high motion variability with multiple bursts." if len(motion_bursts) > 5
        else "Mostly stable motion with a few active regions." if len(motion_bursts) > 0
        else "Low-motion or static video."
    )

    config.analysis.motion_agent = {
        "motion_mean": motion_mean,
        "motion_std_dev": motion_std,
        "motion_min": motion_min,
        "motion_max": motion_max,
        "burst_frames": motion_bursts,
        "static_frames": static_regions,
        "summary": summary
    }

    print("Motion Agent Analysis:", config.analysis.motion_agent)
