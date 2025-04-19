export const DefaultEvaluationCriteria = (fileData) => {
  return {
    video_file: fileData ? fileData.name : "Please upload a video file",
    prompt: "",
    frame_rate: "",
    pipeline_mode: "",
    report_format: "",
    agents: {
      primary_agent: ALL_AGENTS.primary_agent, // fixed
      secondary_agent: [],
      meta_agents: [],
    },
  };
};


export const PIPELINE_MODES = ["default", "parallel", "sequential", "custom"];
export const REPORT_FORMATS = ["summary", "detailed", "diagnostic", "pdf"];

export const ALL_AGENTS = {
  primary_agent: [
    "video_ingestion_agent",
    "perception_agent",
    "temporal_analysis_agent",
    "semantic_analysis_agent",
    "dynamics_robustness_agent",
    "generalization_agent"
  ],
  secondary_agent: [
    "aesthetic_agent",
    "motion_agent",
    "redundancy_agent",
    "transition_agent",
    "caption_alignment_agent"
  ],
  meta_agents: [
    "reasoning_agent",
    "reporting_agent"
  ]
}

export const ProjectDescriptionPrimary =
  "After uploading the video, you can proceed to the next step where this file will be used for analysis or processing. This tool supports temporal segmentation, AI-based labeling, and preview playback directly from the browser. Please ensure your video is trimmed and properly formatted.";
export const ProjectDescriptionSecondary =
  "If you have any questions or need assistance, please refer to our documentation or contact support.";
