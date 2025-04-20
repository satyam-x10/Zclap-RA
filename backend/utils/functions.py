import numpy as np
from data.Config import config

def convert_numpy_types(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(i) for i in obj]
    elif isinstance(obj, np.generic):
        return obj.item()
    else:
        return obj


def extract_config_data(obj):
    if hasattr(obj, '__dict__'):
        return {k: extract_config_data(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [extract_config_data(i) for i in obj]
    else:
        return obj

def class_to_dict(obj):
    """
    Recursively converts a class instance to a dictionary, skipping any attributes in `exclude`
    and filtering out None, empty dicts/lists/strings.
    """
    exclude = None

    if exclude is None:
        exclude = []

    result = {}
    for key in dir(obj):
        if key.startswith("__") or key in exclude:
            continue

        value = getattr(obj, key)

        # Skip methods and private attributes
        if callable(value):
            continue

        # Recursively handle nested class instances
        if hasattr(value, "__dict__"):
            value = class_to_dict(value)

        # Filter out empty or None values
        if value not in (None, {}, [], ""):
            result[key] = value

    return result


async def drop_frames_data():
    valualables =config
    
    valualables.analysis.video_ingestion_agent = None
    valualables.analysis.perception_agent = None

    # save valuables to file
    with open("valuable.json", 'w') as f:
        f.write(str(valualables))
    
    return valualables
