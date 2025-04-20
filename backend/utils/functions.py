import numpy as np
from data.Config import config
from data.valuables import valuablesConfig

async def convert_numpy_types(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(i) for i in obj]
    elif isinstance(obj, np.generic):
        return obj.item()
    else:
        return obj


async def extract_config_data(obj):
    if hasattr(obj, '__dict__'):
        return {k: extract_config_data(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [extract_config_data(i) for i in obj]
    else:
        return obj

def class_to_dict(obj, exclude: list = None):
    """
    Recursively converts any class instance into a dictionary.
    Skips attributes in `exclude` and filters out None/empty values.
    """
    if exclude is None:
        exclude = []

    result = {}

    for attr in dir(obj):
        if attr.startswith("__") or attr in exclude:
            continue

        value = getattr(obj, attr)

        # Skip methods
        if callable(value):
            continue

        # Recursively handle nested class instances
        if hasattr(value, "__dict__"):
            value = class_to_dict(value, exclude)

        # Filter out empty or None values
        if value not in (None, {}, [], ""):
            result[attr] = value

    return result

async def drop_frames_data():
    valualables =config  
    
    valualables.analysis.video_ingestion_agent["frames"] = None
    valualables.analysis.perception_agent["visual_embeddings"] = None
    valualables.analysis.perception_agent["motion_vectors"] = None
    valualables.analysis.perception_agent["semantic_tags"] = None
    valualables.analysis.semantic_analysis_agent["semantic_segments"] = None
    valualables.analysis.semantic_analysis_agent["entity_map"] = None

    valuablesConfig.analysis= valualables
      
    return valualables
