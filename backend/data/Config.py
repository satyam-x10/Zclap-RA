# config.py

class Analysis:
    def __init__(self):
        self.video_ingestion_agent = {}
        self.perception_agent = {}
        self.semantic_analysis_agent = {}
        self.temporal_analysis_agent = {}
        self.dynamics_robustness_agent = {}
        self.generalization_agent = {}

        self.motion_agent = {}
        self.transition_agent = {}
        self.caption_alignment_agent = {}
        self.redundancy_agent = {}
        self.aesthetic_agent = {}

        self.reasoning_agent = {}
        self.reporting_agent = {}

    def to_dict(self):
        return self.__dict__


class Config:
    def __init__(self):
        self.prompt = None
        self.frame_rate = None
        self.pipeline_mode = None
        self.video_file_path = None
        self.report_format = None
        self.primary_agents = []
        self.secondary_agents = []
        self.meta_agents = []
        self.parsed_config_json = None
        self.analysis = Analysis()

    def to_dict(self):
        return {
            "prompt": self.prompt,
            "frame_rate": self.frame_rate,
            "pipeline_mode": self.pipeline_mode,
            "video_file_path": self.video_file_path,
            "report_format": self.report_format,
            "primary_agents": self.primary_agents,
            "secondary_agents": self.secondary_agents,
            "meta_agents": self.meta_agents,
            "parsed_config_json": self.parsed_config_json,
            "analysis": self.analysis.to_dict(),
        }


config = Config()
