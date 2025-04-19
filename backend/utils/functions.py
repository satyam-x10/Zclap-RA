import numpy as np

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
