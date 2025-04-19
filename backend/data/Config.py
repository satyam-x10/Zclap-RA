# config.py

class Analysis:
    video_ingestion_agent: dict = {}
    temporal_analysis_agent: dict = {}


class Config:
    prompt = None
    frame_rate = None
    pipeline_mode = None
    video_file_path = None

    report_format = None

    primary_agents = []
    secondary_agents = []
    meta_agents = []

    parsed_config_json = None

    analysis = None


config = Analysis()
