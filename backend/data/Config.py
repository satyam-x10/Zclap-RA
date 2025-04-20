# config.py

class Analysis:
    # Primary agents
    video_ingestion_agent: dict = {}
    perception_agent: dict = {}
    semantic_analysis_agent: dict = {}
    temporal_analysis_agent: dict = {}
    dynamics_robustness_agent: dict = {}
    generalization_agent: dict = {}

    # Secondary agents
    motion_agent: dict = {}
    transition_agent: dict = {}
    caption_alignment_agent: dict = {}
    redundancy_agent: dict = {}
    aesthetic_agent: dict = {}

    # Meta agents
    reasoning_agent: dict = {}
    reporting_agent: dict = {}


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

    analysis = Analysis()


config = Config()
